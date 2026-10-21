"""Message injection causal intervention experiment.

Injects messages into multi-agent conversations to test whether specific
communication function types degrade task accuracy.

Two conditions per task (within-subject paired design):
  - control: normal round-robin pipeline
  - inject:  after each agent response, insert an injected message from the
             next agent into the visible context (no LLM call for the injection)

Injection sources:
  - ack (default): synthetic acknowledgment templates (~4 words each)
  - info: real Information Provision messages extracted from baseline traces,
          length-filtered to approximate ACK template length

The number of real LLM turns is identical across conditions; only the
context content differs. This isolates the context-pollution effect from
the turn-budget effect.

Input:  config YAML (model, agents, data) — same format as pruning experiments.
Output: JSON with per-task paired results and aggregate statistics.
Deps:   vLLM server, datasets, openai, httpx.
"""
from __future__ import annotations

import argparse
import gc
import json
import logging
import os
import random
import sys
import time
from datetime import datetime, timezone

import yaml

_src_dir = os.path.dirname(os.path.abspath(__file__))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from utils import extract_final_answer, model_supports_system_role, convert_system_to_user
from trace_collection import (
    load_config, load_dataset_from_config, extract_ground_truth, _raise_fd_limit,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Synthetic ack templates — sampled from patterns common in real multi-agent
# math conversations (short confirmations that add no new information).
ACK_TEMPLATES = [
    "Got it, thanks!",
    "I understand, let me continue.",
    "I see, that makes sense.",
    "Understood, I'll proceed.",
    "Right, I agree with that.",
    "OK, I'll check that.",
    "That looks correct so far.",
    "I agree with your approach.",
    "Yes, that's right.",
    "Good, let me verify.",
    "I see your point.",
    "Noted, I'll work on that.",
    "That's a valid approach.",
    "I concur with your reasoning.",
    "Alright, let me review this.",
]

def build_info_pool(
    traces_path: str,
    annotations_path: str,
    max_words: int = 30,
    domain: str = "gsm8k",
) -> list[str]:
    """Extract real Information Provision messages from baseline traces.

    Joins annotations (for labels) with traces (for full content).
    Filters to non-question messages (round > 0) within word limit.
    Falls back to larger threshold if pool < 15 messages.
    """
    traces = {}
    with open(traces_path) as f:
        for line in f:
            rec = json.loads(line)
            if not rec["task_id"].startswith(domain):
                continue
            for i, msg in enumerate(rec.get("messages", [])):
                traces[(rec["task_id"], i)] = msg["content"]

    pool = []
    with open(annotations_path) as f:
        for line in f:
            rec = json.loads(line)
            if not rec["task_id"].startswith(domain):
                continue
            if rec["message_index"] == 0:
                continue
            ta = rec["annotation_a"]["type"]
            tb = rec["annotation_b"]["type"]
            if ta != "information_provision" and tb != "information_provision":
                continue
            content = traces.get((rec["task_id"], rec["message_index"]), "")
            if not content:
                continue
            wc = len(content.split())
            if wc <= max_words:
                pool.append(content)

    if len(pool) < 15:
        logger.warning(
            "INFO pool only %d msgs with max_words=%d; relaxing to %d",
            len(pool), max_words, max_words * 3,
        )
        pool = []
        with open(annotations_path) as f:
            for line in f:
                rec = json.loads(line)
                if not rec["task_id"].startswith(domain):
                    continue
                if rec["message_index"] == 0:
                    continue
                ta = rec["annotation_a"]["type"]
                tb = rec["annotation_b"]["type"]
                if ta != "information_provision" and tb != "information_provision":
                    continue
                content = traces.get((rec["task_id"], rec["message_index"]), "")
                if not content:
                    continue
                if len(content.split()) <= max_words * 3:
                    pool.append(content)

    unique_pool = list(dict.fromkeys(pool))
    logger.info(
        "INFO pool: %d messages (deduplicated from %d), word counts: min=%d median=%.0f max=%d",
        len(unique_pool), len(pool),
        min(len(c.split()) for c in unique_pool) if unique_pool else 0,
        sorted(len(c.split()) for c in unique_pool)[len(unique_pool) // 2] if unique_pool else 0,
        max(len(c.split()) for c in unique_pool) if unique_pool else 0,
    )
    return unique_pool


_INFRA_EXCEPTION_NAMES = frozenset({
    "APIConnectionError", "ConnectError", "ConnectionError",
    "NotFoundError", "RemoteProtocolError",
})


def _is_infra_error(exc: Exception) -> bool:
    return any(n in type(exc).__name__ for n in _INFRA_EXCEPTION_NAMES)


def check_answer(final_answer, ground_truth) -> bool:
    if final_answer is None:
        return False
    try:
        return abs(float(final_answer) - float(ground_truth)) < 1e-6
    except ValueError:
        return str(final_answer).strip() == str(ground_truth).strip()


def run_pipeline(
    question: str,
    cfg: dict,
    max_rounds: int = 6,
    inject: bool = False,
    task_id: str = "",
    rng: random.Random | None = None,
    inject_pool: list[str] | None = None,
) -> tuple[list[dict], int]:
    """Run round-robin pipeline with optional message injection.

    Returns (all_messages, injected_count).
    Both conditions make the same number of real LLM calls (max_rounds - 1).
    In inject mode, a message sampled from inject_pool (or ACK_TEMPLATES if
    None) is appended to visible context after each real response (except the
    last), so downstream agents see extra clutter.
    """
    from openai import OpenAI
    import httpx

    if rng is None:
        rng = random.Random(42)

    agents_cfg = cfg["agents"]
    agent_list = list(agents_cfg.values()) if isinstance(agents_cfg, dict) else agents_cfg
    model_cfg = cfg["model"]

    http_timeout = float(model_cfg.get("timeout", 60))
    client = OpenAI(
        base_url=model_cfg["api_base"],
        api_key=[REDACTED]"api_key"],
        timeout=httpx.Timeout(http_timeout, connect=10.0),
    )

    agent_names = [a["name"] for a in agent_list]
    n_agents = len(agent_list)

    all_messages: list[dict] = [{
        "sender": agent_names[0],
        "receiver": agent_names[1 % n_agents],
        "content": question,
        "round": 0,
    }]
    visible_msgs: list[dict] = []
    injected_count = 0

    extra_body = {}
    if "stop" in model_cfg:
        extra_body["stop"] = model_cfg["stop"]

    for round_idx in range(1, max_rounds):
        agent_idx = round_idx % n_agents
        agent = agent_list[agent_idx]

        # Build prompt: system + question + visible conversation history
        oai_messages = [{"role": "system", "content": agent["system_message"]}]
        oai_messages.append({"role": "user", "content": question})
        for vm in visible_msgs:
            role = "assistant" if vm["sender"] == agent["name"] else "user"
            oai_messages.append({"role": role, "content": vm["content"]})

        if not model_supports_system_role(model_cfg["name"]):
            oai_messages = convert_system_to_user(oai_messages)

        response = client.chat.completions.create(
            model=model_cfg["name"],
            messages=oai_messages,
            temperature=model_cfg.get("temperature", 0),
            top_p=model_cfg.get("top_p", 1.0),
            max_tokens=model_cfg.get("max_tokens", 2048),
            extra_body=extra_body if extra_body else None,
            timeout=http_timeout,
        )
        content = response.choices[0].message.content or ""

        receiver_idx = (agent_idx + 1) % n_agents
        msg = {
            "sender": agent_names[agent_idx],
            "receiver": agent_names[receiver_idx],
            "content": content,
            "round": round_idx,
            "injected": False,
        }
        all_messages.append(msg)
        visible_msgs.append(msg)

        # Inject message from the next agent after this real response
        if inject and round_idx < max_rounds - 1:
            pool = inject_pool if inject_pool is not None else ACK_TEMPLATES
            ack_sender_idx = receiver_idx
            ack_content = rng.choice(pool)
            ack_msg = {
                "sender": agent_names[ack_sender_idx],
                "receiver": agent_names[agent_idx],
                "content": ack_content,
                "round": round_idx,
                "injected": True,
            }
            all_messages.append(ack_msg)
            visible_msgs.append(ack_msg)
            injected_count += 1

    return all_messages, injected_count


def main():
    parser = argparse.ArgumentParser(
        description="Message injection causal intervention experiment",
    )
    parser.add_argument("--config", required=True, help="Path to experiment config YAML")
    parser.add_argument("--num-tasks", type=int, default=None,
                        help="Number of tasks (overrides config)")
    parser.add_argument("--max-rounds", type=int, default=None,
                        help="Max rounds per conversation (overrides config)")
    parser.add_argument("--data-seed", type=int, default=None,
                        help="Random seed for dataset sampling (overrides config)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (default: outputs/analysis/ack_injection/results.json)")
    parser.add_argument("--task-offset", type=int, default=0,
                        help="Skip first N tasks (for resuming)")
    parser.add_argument("--injection-source", type=str, default="ack",
                        choices=["ack", "info"],
                        help="Message type to inject: 'ack' (synthetic templates) or 'info' (real INFO messages from traces)")
    parser.add_argument("--traces-file", type=str, default=None,
                        help="Path to traces.jsonl (required when --injection-source=info)")
    parser.add_argument("--annotations-file", type=str, default=None,
                        help="Path to annotations.jsonl (required when --injection-source=info)")
    parser.add_argument("--info-max-words", type=int, default=30,
                        help="Max word count for INFO pool filtering (default: 30)")
    args = parser.parse_args()

    _raise_fd_limit()

    cfg = load_config(args.config)
    if args.data_seed is not None:
        cfg["data"]["seed"] = args.data_seed
    if args.num_tasks is not None:
        cfg["data"]["num_tasks"] = args.num_tasks

    max_rounds = args.max_rounds or cfg["trace_collection"].get("max_rounds", 6)
    domain = cfg["data"].get("source", "gsm8k")
    num_tasks = args.num_tasks or cfg["data"].get("num_tasks", 300)

    cfg_copy = json.loads(json.dumps(cfg))
    cfg_copy["data"]["num_tasks"] = num_tasks
    raw_tasks, _ = load_dataset_from_config(cfg_copy)

    all_tasks = []
    for idx, item in enumerate(raw_tasks[:num_tasks]):
        gt = extract_ground_truth(item["answer"]) if domain == "gsm8k" else item.get("ground_truth", item.get("answer", ""))
        all_tasks.append({
            "task_id": f"{domain}_{idx:04d}",
            "question": item["question"],
            "ground_truth": gt,
        })

    if args.task_offset:
        all_tasks = all_tasks[args.task_offset:]

    # Build injection pool
    inject_pool = None
    injection_source = args.injection_source
    if injection_source == "info":
        if not args.traces_file or not args.annotations_file:
            parser.error("--traces-file and --annotations-file required when --injection-source=info")
        inject_pool = build_info_pool(
            args.traces_file, args.annotations_file,
            max_words=args.info_max_words, domain=domain,
        )
        if not inject_pool:
            logger.error("Empty INFO pool — cannot proceed")
            sys.exit(1)

    logger.info(
        "%s injection: %d tasks, domain=%s, max_rounds=%d, pool_size=%d",
        injection_source.upper(), len(all_tasks), domain, max_rounds,
        len(inject_pool) if inject_pool else len(ACK_TEMPLATES),
    )

    rng = random.Random(cfg["data"].get("seed", 42))

    control_correct = 0
    inject_correct = 0
    total = 0
    total_injected_acks = 0
    per_task = []
    t_start = time.time()

    for idx, task_rec in enumerate(all_tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        # --- Control run ---
        try:
            ctrl_msgs, _ = run_pipeline(
                question, cfg, max_rounds=max_rounds,
                inject=False, task_id=task_id, rng=rng,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infra error on %s control (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Control failed on %s", task_id)
            per_task.append({"task_id": task_id, "skipped": True, "skip_reason": "control_exception"})
            continue
        finally:
            gc.collect()

        ctrl_answer = None
        for msg in reversed(ctrl_msgs):
            ctrl_answer = extract_final_answer(msg.get("content", ""))
            if ctrl_answer is not None:
                break
        ctrl_is_correct = check_answer(ctrl_answer, ground_truth)

        # --- Inject run ---
        try:
            inj_msgs, inj_count = run_pipeline(
                question, cfg, max_rounds=max_rounds,
                inject=True, task_id=task_id, rng=rng,
                inject_pool=inject_pool,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infra error on %s inject (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Inject failed on %s", task_id)
            per_task.append({
                "task_id": task_id, "control_correct": ctrl_is_correct,
                "inject_correct": False, "injected_acks": 0,
            })
            continue
        finally:
            gc.collect()

        inj_answer = None
        for msg in reversed(inj_msgs):
            if msg.get("injected"):
                continue
            inj_answer = extract_final_answer(msg.get("content", ""))
            if inj_answer is not None:
                break
        inj_is_correct = check_answer(inj_answer, ground_truth)

        total += 1
        if ctrl_is_correct:
            control_correct += 1
        if inj_is_correct:
            inject_correct += 1
        total_injected_acks += inj_count

        task_result = {
            "task_id": task_id,
            "control_correct": ctrl_is_correct,
            "inject_correct": inj_is_correct,
            "control_answer": str(ctrl_answer),
            "inject_answer": str(inj_answer),
            "ground_truth": str(ground_truth),
            "injected_acks": inj_count,
            "control_num_msgs": len([m for m in ctrl_msgs if m["round"] > 0]),
            "inject_num_msgs": len([m for m in inj_msgs if m["round"] > 0]),
        }
        per_task.append(task_result)

        logger.info("[%s_inj] %d/%d task=%s ctrl=%s inj=%s injected=%d",
                    injection_source, idx + 1, len(all_tasks), task_id,
                    ctrl_is_correct, inj_is_correct, inj_count)

    elapsed = time.time() - t_start
    completed = [t for t in per_task if not t.get("skipped")]
    skipped = [t for t in per_task if t.get("skipped")]
    n_completed = len(completed)

    ctrl_acc = control_correct / n_completed if n_completed > 0 else 0
    inj_acc = inject_correct / n_completed if n_completed > 0 else 0
    delta_pp = (inj_acc - ctrl_acc) * 100

    # McNemar's test for paired binary outcomes
    mcnemar_p = None
    if n_completed > 0:
        # b: control correct & inject wrong, c: control wrong & inject correct
        b = sum(1 for t in completed if t.get("control_correct") and not t.get("inject_correct"))
        c = sum(1 for t in completed if not t.get("control_correct") and t.get("inject_correct"))
        if b + c > 0:
            from scipy.stats import binomtest
            mcnemar_p = binomtest(b, b + c, 0.5).pvalue

    output = {
        "experiment": f"{injection_source}_injection",
        "injection_source": injection_source,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "config": os.path.basename(args.config),
        "domain": domain,
        "max_rounds": max_rounds,
        "num_tasks_requested": num_tasks,
        "num_completed": n_completed,
        "num_skipped": len(skipped),
        "elapsed_seconds": round(elapsed, 1),
        "inject_pool_size": len(inject_pool) if inject_pool else len(ACK_TEMPLATES),
        "info_max_words": args.info_max_words if injection_source == "info" else None,
        "total_injected": total_injected_acks,
        "avg_injected_per_task": round(total_injected_acks / n_completed, 2) if n_completed > 0 else 0,
        "control": {
            "correct": control_correct,
            "total": n_completed,
            "accuracy": round(ctrl_acc, 4),
        },
        "inject": {
            "correct": inject_correct,
            "total": n_completed,
            "accuracy": round(inj_acc, 4),
        },
        "delta_pp": round(delta_pp, 2),
        "mcnemar_p": round(mcnemar_p, 6) if mcnemar_p is not None else None,
        "per_task": per_task,
    }

    out_path = args.output
    if not out_path:
        default_dir = f"outputs/analysis/{injection_source}_injection"
        analysis_dir = cfg.get("output", {}).get("analysis_dir", default_dir)
        os.makedirs(analysis_dir, exist_ok=True)
        out_path = os.path.join(analysis_dir, "results.json")
    else:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    logger.info("Results saved to %s", out_path)

    logger.info(
        "=== Summary: control=%.1f%% (%d/%d), inject=%.1f%% (%d/%d), "
        "delta=%.2fpp, McNemar p=%s ===",
        ctrl_acc * 100, control_correct, n_completed,
        inj_acc * 100, inject_correct, n_completed,
        delta_pp,
        f"{mcnemar_p:.4f}" if mcnemar_p is not None else "N/A",
    )


if __name__ == "__main__":
    main()
