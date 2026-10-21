"""Dose-response curve: accuracy vs ack pruning rate.

Identifies ack messages from existing traces via heuristic detector,
then re-runs the multi-agent pipeline with partial ack suppression.
"""

import argparse
import gc
import json
import logging
import os
import random
import time

from openai import OpenAI

from heuristic_ack_detector import heuristic_is_ack, heuristic_is_ack_llama
from pruning_validation import PLACEHOLDER, load_traces
from trace_collection import load_config
from utils import extract_final_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

RATES = [0.0, 0.25, 0.50, 0.75, 1.0]
SEEDS = [42, 123, 456, 789, 1024, 2048, 3072, 4096, 5120, 6144]


def identify_ack_rounds(task_rec: dict, char_threshold: int = 30, backbone: str = "qwen") -> list[int]:
    ack_rounds = []
    prev_content = ""
    for msg in task_rec.get("messages", []):
        rnd = msg.get("round", 0)
        if rnd == 0:
            prev_content = msg.get("content", "")
            continue
        content = msg.get("content", "")
        if backbone == "llama":
            is_ack = heuristic_is_ack_llama(content, prev_content)
        else:
            is_ack = heuristic_is_ack(content, char_threshold)
        if is_ack:
            ack_rounds.append(rnd)
        prev_content = content
    return ack_rounds


def select_prune_rounds(
    ack_rounds: list[int], prune_rate: float, subset_seed: int
) -> set[int]:
    if prune_rate <= 0 or not ack_rounds:
        return set()
    if prune_rate >= 1.0:
        return set(ack_rounds)
    n_to_prune = max(1, round(len(ack_rounds) * prune_rate))
    n_to_prune = min(n_to_prune, len(ack_rounds))
    rng = random.Random(subset_seed)
    return set(rng.sample(ack_rounds, n_to_prune))


def run_pipeline(
    question: str, cfg: dict, prune_rounds: set[int], max_rounds: int = 6
) -> list[dict]:
    agents_cfg = cfg["agents"]
    agent_list = list(agents_cfg.values()) if isinstance(agents_cfg, dict) else agents_cfg

    model_cfg = cfg["model"]
    client = OpenAI(base_url=model_cfg["api_base"], api_key=[REDACTED]"api_key"])

    agent_names = [a["name"] for a in agent_list]
    n_agents = len(agent_names)

    all_messages = [{"sender": agent_names[0], "content": question, "round": 0}]
    visible_msgs = []

    extra_body = {}
    if "stop" in model_cfg:
        extra_body["stop"] = model_cfg["stop"]

    for round_idx in range(1, max_rounds):
        agent_idx = round_idx % n_agents
        agent = agent_list[agent_idx]

        if round_idx in prune_rounds:
            all_messages.append({
                "sender": agent_names[agent_idx],
                "content": PLACEHOLDER,
                "round": round_idx,
                "pruned": True,
            })
            continue

        oai_messages = [{"role": "system", "content": agent["system_message"]}]
        oai_messages.append({"role": "user", "content": question})
        for vm in visible_msgs:
            role = "assistant" if vm["sender"] == agent["name"] else "user"
            oai_messages.append({"role": role, "content": vm["content"]})

        response = client.chat.completions.create(
            model=model_cfg["name"],
            messages=oai_messages,
            temperature=model_cfg.get("temperature", 0),
            top_p=model_cfg.get("top_p", 1.0),
            max_tokens=model_cfg.get("max_tokens", 2048),
            extra_body=extra_body if extra_body else None,
        )
        content = response.choices[0].message.content or ""

        msg = {
            "sender": agent_names[agent_idx],
            "content": content,
            "round": round_idx,
            "pruned": False,
        }
        all_messages.append(msg)
        visible_msgs.append(msg)

    return all_messages


def check_answer(final_answer, ground_truth) -> bool:
    if final_answer is None:
        return False
    try:
        return abs(float(final_answer) - float(ground_truth)) < 1e-6
    except ValueError:
        return str(final_answer).strip() == str(ground_truth).strip()


def run_single(cfg, tasks, prune_rate, subset_seed, char_threshold, max_rounds, output_dir, backbone="qwen"):
    correct = 0
    total = 0
    total_ack = 0
    total_pruned = 0
    per_task = []
    t_start = time.time()

    for idx, task_rec in enumerate(tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        ack_rounds = identify_ack_rounds(task_rec, char_threshold, backbone=backbone)
        task_seed = subset_seed * 10000 + idx
        prune_rounds = select_prune_rounds(ack_rounds, prune_rate, task_seed)

        total_ack += len(ack_rounds)
        total_pruned += len(prune_rounds)
        total += 1

        try:
            messages = run_pipeline(question, cfg, prune_rounds, max_rounds)
        except Exception:
            logger.exception("Failed on %s", task_id)
            per_task.append({"task_id": task_id, "correct": False})
            continue
        finally:
            gc.collect()

        final_answer = None
        for msg in reversed(messages):
            content = msg.get("content", "")
            if content == PLACEHOLDER:
                continue
            final_answer = extract_final_answer(content)
            if final_answer is not None:
                break

        is_correct = check_answer(final_answer, ground_truth)
        if is_correct:
            correct += 1

        per_task.append({
            "task_id": task_id,
            "correct": is_correct,
            "ack_rounds": ack_rounds,
            "pruned_rounds": sorted(prune_rounds),
            "n_ack": len(ack_rounds),
            "n_pruned": len(prune_rounds),
            "final_answer": str(final_answer),
        })

        logger.info(
            "[rate=%.2f seed=%d] %d/%d task=%s ack=%d pruned=%d correct=%s",
            prune_rate, subset_seed, idx + 1, len(tasks), task_id,
            len(ack_rounds), len(prune_rounds), is_correct,
        )

    elapsed = time.time() - t_start
    accuracy = correct / total if total > 0 else 0

    result = {
        "ack_prune_rate": prune_rate,
        "subset_seed": subset_seed,
        "n_tasks": total,
        "accuracy": round(accuracy, 4),
        "n_correct": correct,
        "n_total": total,
        "n_ack_total": total_ack,
        "n_ack_pruned": total_pruned,
        "elapsed_seconds": round(elapsed, 1),
        "per_task": per_task,
    }

    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, f"rate{prune_rate:.2f}_seed{subset_seed}.json")
    with open(out_file, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    logger.info(
        "Saved %s — accuracy=%.1f%% (%d/%d), pruned=%d/%d ack",
        out_file, accuracy * 100, correct, total, total_pruned, total_ack,
    )
    return result


def build_summary(output_dir):
    summary = {}
    for fname in sorted(os.listdir(output_dir)):
        if not fname.startswith("rate") or not fname.endswith(".json"):
            continue
        fpath = os.path.join(output_dir, fname)
        with open(fpath) as f:
            data = json.load(f)
        rate = str(data["ack_prune_rate"])
        seed = str(data["subset_seed"])
        if rate not in summary:
            summary[rate] = {}
        summary[rate][seed] = {
            "accuracy": data["accuracy"],
            "n_correct": data["n_correct"],
            "n_total": data["n_total"],
            "n_ack_pruned": data["n_ack_pruned"],
            "n_ack_total": data["n_ack_total"],
        }

    out_file = os.path.join(output_dir, "dose_response_summary.json")
    with open(out_file, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info("Summary saved to %s", out_file)
    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Dose-response: accuracy vs ack pruning rate"
    )
    parser.add_argument("--config", required=True)
    parser.add_argument("--ack-prune-rate", type=float, default=None)
    parser.add_argument("--subset-seed", type=int, default=42)
    parser.add_argument("--n-tasks", type=int, default=100)
    parser.add_argument(
        "--traces-dir", default="outputs/full_scale/qwen_round_robin/traces"
    )
    parser.add_argument("--char-threshold", type=int, default=30)
    parser.add_argument("--backbone", default="qwen", choices=["qwen", "llama", "gemma"])
    parser.add_argument("--output-dir", default="outputs/analysis/dose_response")
    parser.add_argument(
        "--run-all", action="store_true",
        help="Run all 15 (rate, seed) combinations sequentially",
    )
    parser.add_argument(
        "--summary-only", action="store_true",
        help="Only build summary from existing results",
    )
    args = parser.parse_args()

    if args.summary_only:
        build_summary(args.output_dir)
        return

    cfg = load_config(args.config)
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)

    traces_path = os.path.join(args.traces_dir, "traces.jsonl")
    all_tasks = load_traces(traces_path)
    if args.n_tasks < len(all_tasks):
        all_tasks = all_tasks[: args.n_tasks]
    logger.info("Loaded %d tasks from %s", len(all_tasks), traces_path)

    if args.run_all:
        for rate in RATES:
            for seed in SEEDS:
                logger.info("=== Starting rate=%.2f seed=%d ===", rate, seed)
                run_single(
                    cfg, all_tasks, rate, seed,
                    args.char_threshold, max_rounds, args.output_dir,
                    backbone=args.backbone,
                )
        build_summary(args.output_dir)
    else:
        if args.ack_prune_rate is None:
            parser.error("--ack-prune-rate required unless --run-all")
        run_single(
            cfg, all_tasks, args.ack_prune_rate, args.subset_seed,
            args.char_threshold, max_rounds, args.output_dir,
            backbone=args.backbone,
        )


if __name__ == "__main__":
    main()
