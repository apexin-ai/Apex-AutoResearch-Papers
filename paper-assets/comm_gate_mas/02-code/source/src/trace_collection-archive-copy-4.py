"""Collect inter-agent communication traces from AG2 multi-agent systems on GSM8K.

Supports three topologies via config:
  - round_robin: GroupChat with fixed turn order (solver→checker→solver→...)
  - sequential: Direct two-agent chat without GroupChat manager
  - selector: GroupChat with LLM-based speaker selection

Input: config YAML + GSM8K dataset
Output: JSONL file with one task per line, each containing full message trace.
"""

import argparse
import gc
import json
import logging
import os
import re
import resource
from datetime import datetime, timezone

import yaml

try:
    from autogen import AssistantAgent, GroupChat, GroupChatManager
except ImportError:
    AssistantAgent = GroupChat = GroupChatManager = None

from utils import model_supports_system_role, extract_final_answer
from math_utils import load_math, extract_boxed_answer, math_answers_equal
from arc_utils import load_arc, format_arc_question, extract_arc_answer, arc_answers_equal
from strategyqa_utils import load_strategyqa, format_strategyqa_question, extract_strategyqa_answer, strategyqa_answers_equal

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_gsm8k(cfg: dict) -> list[dict]:
    from datasets import load_dataset

    ds = load_dataset("gsm8k", "main", split=cfg["data"]["split"])
    seed = cfg["data"].get("seed", 42)
    num_tasks = cfg["data"].get("num_tasks", 50)
    ds = ds.shuffle(seed=seed).select(range(min(num_tasks, len(ds))))
    return list(ds)


def extract_ground_truth(answer_str: str) -> str:
    match = re.search(r"####\s*(.+)", answer_str)
    if match:
        return match.group(1).strip().replace(",", "")
    return answer_str.strip()




def load_dataset_from_config(cfg: dict) -> tuple[list[dict], str]:
    """Load dataset based on config. Returns (tasks, domain)."""
    source = cfg["data"].get("source", "gsm8k")
    if source == "math":
        dataset_path = cfg["data"]["dataset_path"]
        num_tasks = cfg["data"].get("num_tasks", 50)
        seed = cfg["data"].get("seed", 42)
        tasks = load_math(dataset_path, num_tasks=num_tasks, seed=seed)
        return tasks, "math"
    elif source == "arc":
        num_tasks = cfg["data"].get("num_tasks", 50)
        seed = cfg["data"].get("seed", 42)
        tasks = load_arc(num_tasks=num_tasks, seed=seed)
        return tasks, "arc"
    elif source == "strategyqa":
        num_tasks = cfg["data"].get("num_tasks", 250)
        seed = cfg["data"].get("seed", 42)
        tasks = load_strategyqa(num_tasks=num_tasks, seed=seed)
        return tasks, "strategyqa"
    else:
        tasks = load_gsm8k(cfg)
        return tasks, "gsm8k"


def build_llm_config(cfg: dict, model_key: str = "model") -> dict:
    model_cfg = cfg[model_key]
    config_entry = {
        "model": model_cfg["name"],
        "base_url": model_cfg["api_base"],
        "api_key": [REDACTED]"api_key"],
        "price": [0, 0],
    }
    if "stop" in model_cfg:
        config_entry["extra_body"] = {"stop": model_cfg["stop"]}
    return {
        "config_list": [config_entry],
        "temperature": model_cfg.get("temperature", 0),
        "top_p": model_cfg.get("top_p", 1.0),
        "max_tokens": model_cfg.get("max_tokens", 2048),
    }


def _extract_messages_from_groupchat(groupchat, agent_names: list[str]) -> list[dict]:
    """Extract standardized message list from GroupChat messages."""
    messages = []
    for i, msg in enumerate(groupchat.messages):
        sender = msg.get("name", msg.get("role", "unknown"))
        receiver_candidates = [a for a in agent_names if a != sender]
        receiver = receiver_candidates[0] if receiver_candidates else "unknown"
        messages.append({
            "sender": sender,
            "receiver": receiver,
            "content": msg.get("content", ""),
            "round": i,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
    return messages


def _extract_messages_from_chat_history(solver, checker, solver_name: str, checker_name: str) -> list[dict]:
    """Extract standardized message list from direct two-agent chat history."""
    messages = []
    for i, msg in enumerate(solver.chat_messages.get(checker, [])):
        role = msg.get("role", "")
        if role == "assistant":
            sender = solver_name
            receiver = checker_name
        else:
            sender = checker_name
            receiver = solver_name
        messages.append({
            "sender": sender,
            "receiver": receiver,
            "content": msg.get("content", ""),
            "round": i,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
    return messages


def _build_agents(cfg: dict, llm_config: dict) -> list[AssistantAgent]:
    """Build agents from config. Supports arbitrary number of agents.

    Config format (list-style, preferred for N>2):
      agents:
        - name: MathSolver
          system_message: "..."
        - name: AnswerChecker
          system_message: "..."

    Also supports legacy dict-style (solver/checker keys) for backward compat.
    """
    agents_cfg = cfg["agents"]
    if isinstance(agents_cfg, list):
        return [
            AssistantAgent(
                name=a["name"],
                system_message=a["system_message"],
                llm_config=llm_config,
            )
            for a in agents_cfg
        ]
    # Legacy dict-style: build in key order (solver, checker, ...)
    return [
        AssistantAgent(
            name=v["name"],
            system_message=v["system_message"],
            llm_config=llm_config,
        )
        for v in agents_cfg.values()
    ]


def _get_agent_names(cfg: dict) -> list[str]:
    """Extract agent names from config."""
    agents_cfg = cfg["agents"]
    if isinstance(agents_cfg, list):
        return [a["name"] for a in agents_cfg]
    return [v["name"] for v in agents_cfg.values()]


def run_task_round_robin(question: str, cfg: dict, llm_config: dict) -> list[dict]:
    """GroupChat with round_robin speaker selection."""
    agents = _build_agents(cfg, llm_config)
    agent_names = _get_agent_names(cfg)

    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    groupchat = GroupChat(agents=agents, messages=[], max_round=max_rounds, speaker_selection_method="round_robin")
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    agents[0].initiate_chat(manager, message=question)
    return _extract_messages_from_groupchat(groupchat, agent_names)


def run_task_sequential(question: str, cfg: dict, llm_config: dict) -> list[dict]:
    """Direct two-agent sequential chat without GroupChat. Requires exactly 2 agents."""
    agents = _build_agents(cfg, llm_config)
    agent_names = _get_agent_names(cfg)
    if len(agents) != 2:
        raise ValueError(f"Sequential topology requires exactly 2 agents, got {len(agents)}")

    max_turns = cfg["trace_collection"].get("max_rounds", 6) // 2
    agents[0].initiate_chat(agents[1], message=question, max_turns=max_turns)
    return _extract_messages_from_chat_history(agents[0], agents[1], agent_names[0], agent_names[1])


def run_task_selector(question: str, cfg: dict, llm_config: dict) -> list[dict]:
    """GroupChat with LLM-based speaker selection."""
    agents = _build_agents(cfg, llm_config)
    agent_names = _get_agent_names(cfg)

    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    groupchat = GroupChat(agents=agents, messages=[], max_round=max_rounds, speaker_selection_method="auto")
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    agents[0].initiate_chat(manager, message=question)
    return _extract_messages_from_groupchat(groupchat, agent_names)


TOPOLOGY_RUNNERS = {
    "round_robin": run_task_round_robin,
    "sequential": run_task_sequential,
    "selector": run_task_selector,
}


def _raise_fd_limit():
    """Try to raise the open file descriptor limit to avoid 'Too many open files'."""
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        if soft < hard:
            resource.setrlimit(resource.RLIMIT_NOFILE, (min(hard, 65536), hard))
            logger.info("Raised fd limit from %d to %d", soft, min(hard, 65536))
    except (ValueError, OSError):
        pass


def main():
    parser = argparse.ArgumentParser(description="Collect AG2 multi-agent traces on GSM8K")
    parser.add_argument("--config", type=str, default="configs/mvp.yaml")
    parser.add_argument("--num-tasks", type=int, default=None)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--topology", type=str, default=None, choices=list(TOPOLOGY_RUNNERS.keys()),
                        help="Override topology from config")
    parser.add_argument("--temperature", type=float, default=None,
                        help="Override model temperature from config")
    args = parser.parse_args()

    _raise_fd_limit()

    cfg = load_config(args.config)
    if args.num_tasks is not None:
        cfg["data"]["num_tasks"] = args.num_tasks
    if args.temperature is not None:
        cfg["model"]["temperature"] = args.temperature

    topology = args.topology or cfg["trace_collection"].get("topology", "round_robin")
    run_task = TOPOLOGY_RUNNERS[topology]
    logger.info("Using topology: %s", topology)

    output_path = args.output or os.path.join(cfg["output"]["trace_dir"], "traces.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    llm_config = build_llm_config(cfg)
    dataset, domain = load_dataset_from_config(cfg)

    logger.info("Loaded %d tasks from %s", len(dataset), domain)

    completed_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as fin:
            for line in fin:
                try:
                    completed_ids.add(json.loads(line)["task_id"])
                except (json.JSONDecodeError, KeyError):
                    pass
        if completed_ids:
            logger.info("Resuming: %d tasks already completed", len(completed_ids))

    mode = "a" if completed_ids else "w"
    with open(output_path, mode) as fout:
        for idx, item in enumerate(dataset):
            if domain == "math":
                task_id = item.get("task_id", f"math_{idx:04d}")
                question = item["question"]
                ground_truth = item["answer"]
            elif domain == "arc":
                task_id = item.get("task_id", f"arc_{idx:04d}")
                question = format_arc_question(item)
                ground_truth = item["ground_truth"]
            elif domain == "strategyqa":
                task_id = item.get("task_id", f"stratqa_{idx:04d}")
                question = format_strategyqa_question(item)
                ground_truth = item["ground_truth"]
            else:
                task_id = f"gsm8k_{idx:04d}"
                question = item["question"]
                ground_truth = extract_ground_truth(item["answer"])

            if task_id in completed_ids:
                continue

            logger.info("Task %s: %s...", task_id, question[:60])

            try:
                messages = run_task(question, cfg, llm_config)
            except Exception:
                logger.exception("Failed on task %s", task_id)
                continue
            finally:
                gc.collect()

            if domain == "math":
                final_answer = None
                for msg in reversed(messages):
                    final_answer = extract_boxed_answer(msg.get("content", ""))
                    if final_answer is not None:
                        break
                if final_answer is None:
                    for msg in reversed(messages):
                        final_answer = extract_final_answer(msg.get("content", ""))
                        if final_answer is not None:
                            break
                is_correct = math_answers_equal(final_answer, ground_truth)
            elif domain == "arc":
                final_answer = None
                for msg in reversed(messages):
                    final_answer = extract_arc_answer(msg.get("content", ""))
                    if final_answer is not None:
                        break
                is_correct = arc_answers_equal(final_answer, ground_truth)
            elif domain == "strategyqa":
                final_answer = None
                for msg in reversed(messages):
                    final_answer = extract_strategyqa_answer(msg.get("content", ""))
                    if final_answer is not None:
                        break
                is_correct = strategyqa_answers_equal(final_answer, ground_truth)
            else:
                final_answer = None
                for msg in reversed(messages):
                    final_answer = extract_final_answer(msg.get("content", ""))
                    if final_answer is not None:
                        break
                is_correct = False
                if final_answer is not None:
                    try:
                        is_correct = abs(float(final_answer) - float(ground_truth)) < 1e-6
                    except ValueError:
                        is_correct = final_answer.strip() == ground_truth.strip()

            record = {
                "task_id": task_id,
                "question": question,
                "ground_truth": ground_truth,
                "messages": messages,
                "final_answer": final_answer,
                "is_correct": is_correct,
                "metadata": {
                    "model": cfg["model"]["name"],
                    "temperature": cfg["model"].get("temperature", 0),
                    "num_agents": len(cfg.get("agents", {})),
                    "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
                    "topology": topology,
                    "domain": domain,
                },
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            logger.info("Task %s: correct=%s, messages=%d", task_id, is_correct, len(messages))

    logger.info("Traces saved to %s", output_path)


if __name__ == "__main__":
    main()
