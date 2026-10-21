"""Token-budget-matched random baseline v4 for EXP-D.

Compares ack-pruning to random deletion under the SAME token budget.
For each task, runs paired baseline vs random-suppressed conversations
with vLLM, where the random suppression budget equals the mean ack
tokens per task from existing annotations.

Input:
  --config: YAML with model/agent/data config
  --traces: Full-scale traces JSONL (for token budget computation)
  --annotations: Function annotations JSONL (to identify ack messages)
  --model-path: Local model path (for vLLM pre-flight check)
  --output: Path for JSON results

Output: JSON with baseline_acc, random_pruned_acc, delta, McNemar test,
        suppression stats, per-task results.

Dependencies: openai, scipy, datasets, pyyaml, requests
"""
from __future__ import annotations

import argparse
import gc
import json
import logging
import os
import random
import re
import resource
import sys
import time
from collections import defaultdict

import requests
import yaml

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

_INFRA_EXCEPTION_NAMES = frozenset({
    "APIConnectionError", "ConnectError", "ConnectionError",
    "NotFoundError", "RemoteProtocolError",
})


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3)


def strip_eos_residue(text: str) -> str:
    for token in ("<|im_end|>", "<|eot_id|>", "<|end_of_text|>", "</s>"):
        idx = text.find(token)
        if idx != -1:
            text = text[:idx]
    return text


def extract_final_answer(text: str) -> str | None:
    text = strip_eos_residue(text)
    numeric_patterns = [
        r"[Tt]he answer is\s*\[?\s*\$?\s*([0-9,.\-]+)\s*\]?",
        r"####\s*\$?\s*([0-9,.\-]+)",
        r"[Ff]inal [Aa]nswer[:\s]+\$?\s*([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s+\$?\s*([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s.*?\$\s*([0-9,.]+)",
        r"\*\*[Aa]nswer:?\*\*:?\s.*?(?:is |= )([0-9,.\-]+)",
        r"\*\*[Aa]nswer:?\*\*:?[^\d]*(\d[\d,.]*)",
        r"\\boxed\{([0-9,.\-]+)\}",
    ]
    for pat in numeric_patterns:
        matches = re.findall(pat, text)
        if matches:
            return matches[-1].strip().replace(",", "").replace("$", "")
    bool_patterns = [
        r"[Tt]he answer is\s+(yes|no|true|false)",
        r"####\s*(yes|no|true|false)",
        r"[Ff]inal [Aa]nswer[:\s]+(yes|no|true|false)",
        r"\*\*[Aa]nswer\*\*[:\s]+(yes|no|true|false)",
    ]
    for pat in bool_patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            return matches[-1].strip().lower()
    return None


def check_answer(final_answer, ground_truth) -> bool:
    if final_answer is None:
        return False
    try:
        return abs(float(final_answer) - float(ground_truth)) < 1e-6
    except ValueError:
        return str(final_answer).strip() == str(ground_truth).strip()


def model_supports_system_role(model_name: str) -> bool:
    no_system = ["gemma"]
    return not any(p in model_name.lower() for p in no_system)


def merge_consecutive_roles(messages: list[dict]) -> list[dict]:
    if not messages:
        return messages
    merged = [messages[0]]
    for m in messages[1:]:
        if m["role"] == merged[-1]["role"]:
            merged[-1] = {**merged[-1], "content": merged[-1]["content"] + "\n\n" + m["content"]}
        else:
            merged.append(m)
    return merged


def convert_system_to_user(messages: list[dict]) -> list[dict]:
    result = []
    system_content = []
    for msg in messages:
        if msg["role"] == "system":
            system_content.append(msg["content"])
        else:
            if system_content and msg["role"] == "user":
                combined = "\n\n".join(system_content) + "\n\n" + msg["content"]
                result.append({"role": "user", "content": combined})
                system_content = []
            else:
                if system_content:
                    result.append({"role": "user", "content": "\n\n".join(system_content)})
                    system_content = []
                result.append(msg)
    if system_content:
        result.append({"role": "user", "content": "\n\n".join(system_content)})
    return result


def _is_infra_error(exc: Exception) -> bool:
    return any(n in type(exc).__name__ for n in _INFRA_EXCEPTION_NAMES)


def _raise_fd_limit():
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        if soft < 4096:
            resource.setrlimit(resource.RLIMIT_NOFILE, (min(4096, hard), hard))
    except Exception:
        pass


def extract_ground_truth(answer_str: str) -> str:
    match = re.search(r"####\s*(.+)", answer_str)
    if match:
        return match.group(1).strip().replace(",", "")
    return answer_str.strip()


# ---------------------------------------------------------------------------
# Ack token budget computation
# ---------------------------------------------------------------------------

def compute_ack_token_budget(traces_path: str, annotations_path: str) -> dict:
    """Compute per-task ack token budget from existing annotations.

    Returns dict with mean_per_task, total_ack_tokens, total_all_tokens, token_share.
    """
    traces = {}
    with open(traces_path) as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                msg_map = {}
                for msg in rec.get("messages", []):
                    rnd = msg.get("round", 0)
                    if rnd > 0:
                        msg_map[rnd - 1] = msg.get("content", "")
                traces[rec["task_id"]] = msg_map

    ack_tokens_per_task = defaultdict(int)
    all_tokens_per_task = defaultdict(int)

    with open(annotations_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            msg_idx = rec["message_index"]
            ann_type = rec.get("annotation_a", {}).get("type", "unknown")

            content = traces.get(task_id, {}).get(msg_idx, "")
            if not content:
                content = rec.get("content_preview", "")
            tokens = estimate_tokens(content)

            all_tokens_per_task[task_id] += tokens
            if ann_type == "acknowledgment":
                ack_tokens_per_task[task_id] += tokens

    n_tasks = len(all_tokens_per_task)
    total_ack = sum(ack_tokens_per_task.values())
    total_all = sum(all_tokens_per_task.values())

    mean_per_task = total_ack / n_tasks if n_tasks > 0 else 0
    token_share = total_ack / total_all if total_all > 0 else 0

    return {
        "mean_per_task": round(mean_per_task, 2),
        "total_ack_tokens": total_ack,
        "total_all_tokens": total_all,
        "token_share": round(token_share, 4),
        "n_tasks_analyzed": n_tasks,
    }


# ---------------------------------------------------------------------------
# Online multi-turn pipeline
# ---------------------------------------------------------------------------

def run_multi_turn(
    question: str,
    cfg: dict,
    max_rounds: int = 6,
    backbone: str = "qwen",
    suppress_fn=None,
) -> tuple[list[dict], list[int]]:
    """Run round-robin multi-turn conversation with optional message suppression.

    suppress_fn: callable(content, round_idx) -> bool. If True, message is
    suppressed (skipped from visible context). If None, no suppression.

    Returns (all_messages, suppressed_rounds).
    """
    from openai import OpenAI
    import httpx

    agents_cfg = cfg["agents"]
    if isinstance(agents_cfg, list):
        agent_list = agents_cfg
    else:
        agent_list = list(agents_cfg.values())

    model_cfg = cfg["model"]
    timeout = float(model_cfg.get("timeout", 60))
    client = OpenAI(
        base_url=model_cfg["api_base"],
        api_key=[REDACTED]"api_key", "EMPTY"),
        timeout=httpx.Timeout(timeout, connect=10.0),
    )

    agent_names = [a["name"] for a in agent_list]
    n_agents = len(agent_list)

    all_messages = [{
        "sender": agent_names[0],
        "receiver": agent_names[1 % n_agents],
        "content": question,
        "round": 0,
    }]
    visible_msgs = []
    suppressed_rounds = []

    extra_body = {}
    if "stop" in model_cfg:
        extra_body["stop"] = model_cfg["stop"]

    for round_idx in range(1, max_rounds):
        agent_idx = round_idx % n_agents
        agent = agent_list[agent_idx]

        oai_messages = [{"role": "system", "content": agent["system_message"]}]
        oai_messages.append({"role": "user", "content": question})
        for vm in visible_msgs:
            role = "assistant" if vm["sender"] == agent["name"] else "user"
            oai_messages.append({"role": role, "content": vm["content"]})

        if not model_supports_system_role(model_cfg["name"]):
            oai_messages = convert_system_to_user(oai_messages)
            oai_messages = merge_consecutive_roles(oai_messages)

        response = client.chat.completions.create(
            model=model_cfg["name"],
            messages=oai_messages,
            temperature=model_cfg.get("temperature", 0),
            top_p=model_cfg.get("top_p", 1.0),
            max_tokens=model_cfg.get("max_tokens", 2048),
            extra_body=extra_body if extra_body else None,
            timeout=timeout,
        )
        content = response.choices[0].message.content or ""

        receiver_idx = (agent_idx + 1) % n_agents
        msg = {
            "sender": agent_names[agent_idx],
            "receiver": agent_names[receiver_idx],
            "content": content,
            "round": round_idx,
        }
        all_messages.append(msg)

        if suppress_fn and suppress_fn(content, round_idx):
            suppressed_rounds.append(round_idx)
        else:
            visible_msgs.append(msg)

    return all_messages, suppressed_rounds


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Token-budget-matched random baseline v4")
    parser.add_argument("--config", required=True, help="YAML config path")
    parser.add_argument("--traces", required=True, help="Full-scale traces JSONL")
    parser.add_argument("--annotations", required=True, help="Function annotations JSONL")
    parser.add_argument("--model-path", required=True, help="Local model path for pre-flight check")
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--num-tasks", type=int, default=300)
    parser.add_argument("--data-seed", type=int, default=42)
    args = parser.parse_args()

    _raise_fd_limit()
    random.seed(args.data_seed)

    cfg = yaml.safe_load(open(args.config))
    cfg["data"]["seed"] = args.data_seed
    max_rounds = cfg.get("trace_collection", {}).get("max_rounds", 6)
    model_name = cfg["model"]["name"]
    backbone = "llama" if "llama" in model_name.lower() else "qwen"

    # --- vLLM pre-flight check ---
    api_base = cfg["model"]["api_base"]
    base_url = api_base.rstrip("/").replace("/v1", "")
    logger.info("Pre-flight: checking vLLM at %s", base_url)
    try:
        resp = requests.get(f"{base_url}/v1/models", timeout=10)
        resp.raise_for_status()
        served_models = [m["id"] for m in resp.json()["data"]]
        logger.info("vLLM serving: %s", served_models)
        if model_name not in served_models:
            logger.warning("Expected model %s not in served models %s", model_name, served_models)
    except Exception as e:
        logger.error("vLLM pre-flight failed: %s", e)
        sys.exit(1)

    # --- Compute ack token budget ---
    logger.info("Computing ack token budget from annotations...")
    ack_stats = compute_ack_token_budget(args.traces, args.annotations)
    token_budget = ack_stats["mean_per_task"]
    token_share = ack_stats["token_share"]
    logger.info("Ack token budget: %.1f tokens/task, share=%.4f", token_budget, token_share)

    # --- Load GSM8K tasks ---
    from datasets import load_dataset
    ds = load_dataset("gsm8k", "main", split="test")
    ds = ds.shuffle(seed=args.data_seed)
    all_tasks = []
    for idx, item in enumerate(ds):
        if len(all_tasks) >= args.num_tasks:
            break
        all_tasks.append({
            "task_id": f"gsm8k_{idx:04d}",
            "question": item["question"],
            "ground_truth": extract_ground_truth(item["answer"]),
        })

    logger.info("Loaded %d tasks, backbone=%s, max_rounds=%d", len(all_tasks), backbone, max_rounds)

    # --- Resume from checkpoint ---
    partial_path = args.output.replace(".json", "_partial.json")
    per_task = []
    completed_ids = set()
    baseline_correct = 0
    random_correct = 0
    total = 0
    total_msgs_suppressed = 0
    total_tokens_suppressed = 0
    total_agent_rounds = 0

    if os.path.exists(partial_path):
        with open(partial_path) as f:
            ckpt = json.load(f)
        per_task = ckpt.get("per_task", [])
        completed_ids = {r["task_id"] for r in per_task}
        baseline_correct = ckpt.get("baseline_correct", 0)
        random_correct = ckpt.get("random_correct", 0)
        total = ckpt.get("total", 0)
        total_msgs_suppressed = ckpt.get("total_msgs_suppressed", 0)
        total_tokens_suppressed = ckpt.get("total_tokens_suppressed", 0)
        total_agent_rounds = ckpt.get("total_agent_rounds", 0)
        logger.info("Resumed from checkpoint: %d tasks done", len(completed_ids))

    t_start = time.time()

    for idx, task in enumerate(all_tasks):
        task_id = task["task_id"]
        question = task["question"]
        gt = task["ground_truth"]

        if task_id in completed_ids:
            continue

        total += 1

        # --- Baseline run (no suppression) ---
        try:
            bl_msgs, _ = run_multi_turn(question, cfg, max_rounds, backbone)
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infra error on %s baseline: %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True})
                continue
            logger.exception("Baseline failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": False,
                             "random_pruned_correct": False, "msgs_suppressed": 0, "tokens_suppressed": 0})
            continue
        finally:
            gc.collect()

        bl_answer = None
        for msg in reversed(bl_msgs):
            bl_answer = extract_final_answer(msg.get("content", ""))
            if bl_answer is not None:
                break
        bl_ok = check_answer(bl_answer, gt)
        if bl_ok:
            baseline_correct += 1

        # --- Random-suppressed run (token budget) ---
        remaining_budget = token_budget
        task_msgs_suppressed = 0
        task_tokens_suppressed = 0

        def suppress_fn(content, round_idx):
            nonlocal remaining_budget, task_msgs_suppressed, task_tokens_suppressed
            if remaining_budget <= 0:
                return False
            if random.random() < token_share:
                tok = estimate_tokens(content)
                remaining_budget -= tok
                task_msgs_suppressed += 1
                task_tokens_suppressed += tok
                return True
            return False

        try:
            rnd_msgs, suppressed_rounds = run_multi_turn(
                question, cfg, max_rounds, backbone, suppress_fn=suppress_fn,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infra error on %s random: %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True})
                continue
            logger.exception("Random run failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": bl_ok,
                             "random_pruned_correct": False, "msgs_suppressed": 0, "tokens_suppressed": 0})
            continue
        finally:
            gc.collect()

        rnd_answer = None
        for msg in reversed(rnd_msgs):
            rnd_answer = extract_final_answer(msg.get("content", ""))
            if rnd_answer is not None:
                break
        rnd_ok = check_answer(rnd_answer, gt)
        if rnd_ok:
            random_correct += 1

        agent_msgs = [m for m in rnd_msgs if m.get("round", 0) > 0]
        total_msgs_suppressed += task_msgs_suppressed
        total_tokens_suppressed += task_tokens_suppressed
        total_agent_rounds += len(agent_msgs)

        per_task.append({
            "task_id": task_id,
            "question": question[:200],
            "ground_truth": str(gt),
            "baseline_correct": bl_ok,
            "baseline_answer": str(bl_answer),
            "random_pruned_correct": rnd_ok,
            "random_pruned_answer": str(rnd_answer),
            "msgs_suppressed": task_msgs_suppressed,
            "tokens_suppressed": task_tokens_suppressed,
            "token_budget": round(token_budget, 1),
            "total_messages": len(agent_msgs),
        })

        logger.info("[v4] %d/%d task=%s bl=%s rnd=%s suppressed=%d msgs / %d tok",
                     idx + 1, len(all_tasks), task_id, bl_ok, rnd_ok,
                     task_msgs_suppressed, task_tokens_suppressed)

        if total % 50 == 0:
            ckpt = {
                "baseline_correct": baseline_correct, "random_correct": random_correct,
                "total": total, "total_msgs_suppressed": total_msgs_suppressed,
                "total_tokens_suppressed": total_tokens_suppressed,
                "total_agent_rounds": total_agent_rounds, "per_task": per_task,
            }
            os.makedirs(os.path.dirname(partial_path) or ".", exist_ok=True)
            with open(partial_path, "w") as f:
                json.dump(ckpt, f, indent=2, ensure_ascii=False)
            logger.info("Checkpoint: %d tasks → %s", total, partial_path)

    elapsed = time.time() - t_start

    # --- McNemar test ---
    valid = [r for r in per_task if not r.get("skipped")]
    n_valid = len(valid)
    n_skipped = len(per_task) - n_valid
    baseline_correct = sum(1 for r in valid if r.get("baseline_correct"))
    random_correct = sum(1 for r in valid if r.get("random_pruned_correct"))

    a = b = c = d = 0
    for r in valid:
        bl = r.get("baseline_correct", False)
        rn = r.get("random_pruned_correct", False)
        if bl and rn:
            a += 1
        elif not bl and rn:
            b += 1
        elif bl and not rn:
            c += 1
        else:
            d += 1

    n_disc = b + c
    if n_disc == 0:
        chi2_cc = 0.0
        p_value = 1.0
    else:
        chi2_cc = (abs(b - c) - 1) ** 2 / (b + c)
        from scipy.stats import chi2 as chi2_dist
        p_value = float(1 - chi2_dist.cdf(chi2_cc, df=1))

    bl_acc = baseline_correct / n_valid if n_valid > 0 else 0
    rnd_acc = random_correct / n_valid if n_valid > 0 else 0
    suppress_rate = total_msgs_suppressed / total_agent_rounds * 100 if total_agent_rounds > 0 else 0

    output = {
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": max_rounds,
            "backbone": backbone,
            "data_seed": args.data_seed,
            "num_tasks_requested": args.num_tasks,
        },
        "ack_token_stats": ack_stats,
        "baseline_acc": round(bl_acc, 4),
        "random_pruned_acc": round(rnd_acc, 4),
        "delta_pp": round((rnd_acc - bl_acc) * 100, 2),
        "mcnemar_p": round(p_value, 6),
        "significant": p_value < 0.05,
        "suppression_stats": {
            "msgs_suppressed": total_msgs_suppressed,
            "tokens_suppressed": total_tokens_suppressed,
            "total_agent_rounds": total_agent_rounds,
            "suppression_rate": round(suppress_rate, 2),
        },
        "tasks_completed": n_valid,
        "tasks_skipped": n_skipped,
        "elapsed_seconds": round(elapsed, 1),
        "mcnemar_detail": {
            "a_both_correct": a,
            "b_random_only": b,
            "c_baseline_only": c,
            "d_both_wrong": d,
            "n_discordant": n_disc,
            "chi2_cc": round(chi2_cc, 4),
            "method": "mcnemar_chi2_cc",
        },
        "per_task_results": per_task,
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    if os.path.exists(partial_path):
        os.remove(partial_path)

    logger.info("Done. Baseline=%.1f%% Random=%.1f%% Δ=%+.1fpp McNemar p=%.4f Suppress=%.1f%% Time=%.0fs",
                bl_acc * 100, rnd_acc * 100, (rnd_acc - bl_acc) * 100, p_value, suppress_rate, elapsed)
    logger.info("Results → %s", args.output)


if __name__ == "__main__":
    main()
