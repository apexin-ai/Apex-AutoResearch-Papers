"""Collect inter-agent communication traces using MetaGPT-style hierarchical pipeline on HumanEval.

Uses OpenAI-compatible API (vLLM) with two roles: CodeSolver and CodeReviewer.
Implements TracedEnvironment to intercept all messages for trace collection.
Falls back to direct OpenAI API calls if MetaGPT is unavailable.

Input: config YAML + HumanEval dataset
Output: JSONL file with one task per line, compatible with AG2 trace format.
"""

import argparse
import gc
import json
import logging
import os
import re
from datetime import datetime, timezone

import yaml
from openai import OpenAI

from humaneval_utils import extract_code_from_response, execute_code_safely, load_humaneval

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


class TracedTeam:
    """Lightweight multi-agent team that records all messages.

    Implements a hierarchical pipeline (Solver -> Reviewer -> Solver -> ...)
    using direct OpenAI API calls. This avoids MetaGPT version compatibility
    issues while preserving the hierarchical topology semantics.
    """

    def __init__(self, cfg: dict):
        model_cfg = cfg["model"]
        self.client = OpenAI(
            base_url=model_cfg["api_base"],
            api_key=[REDACTED]"api_key", "EMPTY"),
        )
        self.model = model_cfg["name"]
        self.temperature = model_cfg.get("temperature", 0)
        self.max_tokens = model_cfg.get("max_tokens", 2048)

        self.agents = {}
        for role_key in ["solver", "reviewer"]:
            agent_cfg = cfg["agents"][role_key]
            self.agents[agent_cfg["name"]] = agent_cfg["system_message"]

        self.agent_names = list(self.agents.keys())
        self.max_rounds = cfg["trace_collection"].get("max_rounds", 6)
        self.message_trace: list[dict] = []

    def _call_llm(self, system_prompt: str, conversation: list[dict]) -> str:
        messages = [{"role": "system", "content": system_prompt}] + conversation
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response.choices[0].message.content or ""

    def _record(self, sender: str, receiver: str, content: str, round_idx: int):
        self.message_trace.append({
            "sender": sender,
            "receiver": receiver,
            "content": content,
            "round": round_idx,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

    def run(self, task_prompt: str) -> list[dict]:
        """Run hierarchical pipeline: Solver -> Reviewer -> Solver -> ...

        Both agents accumulate full conversation history across rounds,
        matching AG2 GroupChat behavior where each agent sees the entire
        message history rather than only the latest exchange.
        """
        self.message_trace = []
        solver_name, reviewer_name = self.agent_names[0], self.agent_names[1]
        solver_sys = self.agents[solver_name]
        reviewer_sys = self.agents[reviewer_name]

        self._record("user", solver_name, task_prompt, 0)

        conversation_for_solver = [{"role": "user", "content": task_prompt}]
        conversation_for_reviewer = []
        round_idx = 1

        for iteration in range(self.max_rounds // 2):
            solver_reply = self._call_llm(solver_sys, conversation_for_solver)
            self._record(solver_name, reviewer_name, solver_reply, round_idx)
            conversation_for_solver.append({"role": "assistant", "content": solver_reply})
            round_idx += 1

            if round_idx > self.max_rounds:
                break

            review_prompt = (
                f"The CodeSolver proposed the following solution:\n\n{solver_reply}\n\n"
                f"Original problem:\n{task_prompt}\n\n"
                "Review the code for correctness and edge cases. "
                "If correct, say 'LGTM'. If issues found, provide the corrected code."
            )
            conversation_for_reviewer.append({"role": "user", "content": review_prompt})

            reviewer_reply = self._call_llm(reviewer_sys, conversation_for_reviewer)
            self._record(reviewer_name, solver_name, reviewer_reply, round_idx)
            conversation_for_reviewer.append({"role": "assistant", "content": reviewer_reply})
            round_idx += 1

            if "lgtm" in reviewer_reply.lower() or round_idx > self.max_rounds:
                break

            revision_prompt = (
                f"The reviewer found issues with your solution:\n\n{reviewer_reply}\n\n"
                f"Original problem:\n{task_prompt}\n\n"
                "Please provide a corrected implementation."
            )
            conversation_for_solver.append({"role": "user", "content": revision_prompt})

        return self.message_trace


def extract_final_code(messages: list[dict], prompt: str) -> str:
    """Extract the final code answer from message trace.

    Searches messages in reverse, looking for code blocks.
    Prepends the original function signature if the extracted code doesn't include it.
    """
    for msg in reversed(messages):
        if msg["sender"] == "user":
            continue
        code = extract_code_from_response(msg["content"])
        if code and ("def " in code or "return " in code):
            if not code.startswith("def ") and "def " in prompt:
                code = prompt + code
            return code

    return ""


def main():
    parser = argparse.ArgumentParser(
        description="Collect MetaGPT-style hierarchical traces on HumanEval"
    )
    parser.add_argument("--config", type=str, default="configs/metagpt_qwen.yaml")
    parser.add_argument("--num-tasks", type=int, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    if args.num_tasks is not None:
        cfg["data"]["num_tasks"] = args.num_tasks

    output_path = args.output or os.path.join(cfg["output"]["trace_dir"], "traces.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    dataset = load_humaneval(
        num_tasks=cfg["data"].get("num_tasks", 50),
        seed=cfg["data"].get("seed", 42),
    )
    logger.info("Loaded %d HumanEval tasks", len(dataset))

    completed_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as fin:
            for line in fin:
                line = line.strip()
                if not line:
                    continue
                try:
                    completed_ids.add(json.loads(line)["task_id"])
                except (json.JSONDecodeError, KeyError):
                    pass
        if completed_ids:
            logger.info("Resuming: %d tasks already completed", len(completed_ids))

    eval_timeout = cfg.get("evaluation", {}).get("timeout", 10)
    team = TracedTeam(cfg)

    mode = "a" if completed_ids else "w"
    with open(output_path, mode) as fout:
        for idx, task in enumerate(dataset):
            task_id = f"humaneval_{idx:04d}"
            if task_id in completed_ids:
                continue

            prompt = task["prompt"]
            logger.info("Task %s [%s]: %s...", task_id, task["task_id"], prompt[:60])

            try:
                messages = team.run(prompt)
            except Exception:
                logger.exception("Failed on task %s", task_id)
                continue
            finally:
                gc.collect()

            final_code = extract_final_code(messages, prompt)

            eval_result = {"is_correct": False, "error": "no_code", "execution_time": 0.0}
            if final_code:
                eval_result = execute_code_safely(
                    final_code, task["test"], task["entry_point"], timeout=eval_timeout
                )

            agent_messages = [m for m in messages if m["sender"] != "user"]

            record = {
                "task_id": task_id,
                "question": prompt,
                "ground_truth": task["test"],
                "messages": agent_messages,
                "final_answer": final_code,
                "is_correct": eval_result["is_correct"],
                "metadata": {
                    "model": cfg["model"]["name"],
                    "framework": "custom_hierarchical",
                    "temperature": cfg["model"].get("temperature", 0),
                    "num_agents": len(cfg.get("agents", {})),
                    "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
                    "topology": "hierarchical",
                    "humaneval_task_id": task["task_id"],
                    "eval_error": eval_result.get("error"),
                    "execution_time": eval_result.get("execution_time", 0.0),
                },
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info(
                "Task %s: correct=%s, messages=%d",
                task_id, eval_result["is_correct"], len(agent_messages),
            )

    logger.info("Traces saved to %s", output_path)


if __name__ == "__main__":
    main()
