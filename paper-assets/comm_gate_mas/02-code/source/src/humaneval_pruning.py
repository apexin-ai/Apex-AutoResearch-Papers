"""End-to-end pruning experiments for HumanEval with hierarchical (solver→reviewer) topology.

Runs paired baseline vs. pruned experiments on HumanEval tasks using Qwen2.5-7B-Instruct
served via vLLM. Supports oracle (GPT-4o 5-class) and heuristic (char-threshold) ack detection.

Input:  config YAML + HumanEval dataset (openai_humaneval test split)
Output: JSON file with per-task paired results + aggregate statistics

Dependencies: vLLM running locally, openai, datasets, scipy
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import logging
import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import yaml
from openai import OpenAI

_src_dir = os.path.dirname(os.path.abspath(__file__))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from humaneval_utils import extract_code_from_response, execute_code_safely, load_humaneval
from heuristic_ack_detector import heuristic_is_ack
from metagpt_trace_collection import TracedTeam, extract_final_code, load_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Oracle 5-class ack detection (GPT-4o)
# ---------------------------------------------------------------------------

_oracle_cache: dict = {}


def _load_oracle_cache(path: str) -> dict:
    """Load precomputed oracle annotations keyed by sha256(task_id + texts)."""
    with open(path) as f:
        return json.load(f)


def _oracle_cache_key(task_id: str, text: str, prev_text: str) -> str:
    prev_norm = prev_text[:2000] if prev_text else ""
    text_norm = text[:3000]
    return hashlib.sha256(f"{task_id}\n{prev_norm}\n{text_norm}".encode()).hexdigest()


def oracle_5class_is_ack(
    client: OpenAI,
    model: str,
    text: str,
    prev_text: str,
    task_id: str = "",
    round_idx: int = 0,
) -> dict:
    """5-class GPT-4o classification → binary ack label.

    Returns dict with: round, is_ack, confidence, tokens, function_type.
    Checks _oracle_cache first; falls back to live API call.
    """
    if _oracle_cache:
        key = _oracle_cache_key(task_id, text, prev_text)
        if key in _oracle_cache:
            cached = _oracle_cache[key]
            return {
                "round": round_idx,
                "is_ack": cached["is_ack"],
                "confidence": cached.get("confidence", 0.5),
                "tokens": 0,
                "function_type": cached["function_type"],
                "cached": True,
            }

    from gpt4o_annotation import SYSTEM_PROMPT as FIVECLASS_PROMPT

    user_prompt = (
        f"## Context\n\nTask: {task_id}\n\n"
        f"### Previous message (for context):\n"
        f"{prev_text[:2000] if prev_text else '[conversation start]'}\n\n"
        f"### Current message to classify (sent by agent):\n{text[:3000]}\n\n"
        f"Classify the function of the current message."
    )

    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": FIVECLASS_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=256,
                timeout=120,
            )
            raw = resp.choices[0].message.content or "{}"
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(raw)
            func_type = result.get("type", "unknown")
            return {
                "round": round_idx,
                "is_ack": func_type == "acknowledgment",
                "confidence": float(result.get("confidence", 0.5)),
                "tokens": resp.usage.total_tokens if resp.usage else 0,
                "function_type": func_type,
            }
        except json.JSONDecodeError:
            logger.warning("Oracle JSON parse fail (attempt %d) task=%s r=%d",
                           attempt + 1, task_id, round_idx)
            time.sleep(1)
        except Exception as e:
            err_str = str(e).lower()
            if "rate" in err_str or "429" in err_str:
                backoff = 15 * (2 ** min(attempt, 3))
                logger.warning("Oracle rate limit (attempt %d), backoff %ds",
                               attempt + 1, backoff)
                time.sleep(backoff)
            else:
                logger.warning("Oracle error (attempt %d) task=%s: %s",
                               attempt + 1, task_id, e)
                time.sleep(2 ** attempt)

    return {
        "round": round_idx, "is_ack": False, "confidence": 0.0,
        "tokens": 0, "function_type": "unknown", "error": "all_attempts_failed",
    }


# ---------------------------------------------------------------------------
# PrunedTracedTeam — TracedTeam with ack detection + suppression
# ---------------------------------------------------------------------------

class PrunedTracedTeam(TracedTeam):
    """Extends TracedTeam with ack detection on reviewer messages and optional suppression.

    In hierarchical HumanEval topology, the reviewer's LGTM messages are the pruning targets.
    When pruning_mode='skip', detected ack messages are not relayed back to the solver,
    effectively ending the conversation early without the redundant acknowledgment round.

    Args:
        cfg: Config dict (same format as TracedTeam).
        detection_mode: 'oracle_5class' (GPT-4o) or 'heuristic' (char-threshold).
        pruning_mode: 'none' (baseline, detect but don't prune) or 'skip' (suppress acks).
        oracle_client: OpenAI client for oracle API calls.
        oracle_model: Model name for oracle (e.g. 'openai/gpt-4o').
        char_threshold: Character threshold for heuristic detection.
    """

    def __init__(
        self,
        cfg: dict,
        detection_mode: str = "oracle_5class",
        pruning_mode: str = "none",
        oracle_client: OpenAI | None = None,
        oracle_model: str = "openai/gpt-4o",
        char_threshold: int = 30,
    ):
        super().__init__(cfg)
        self.detection_mode = detection_mode
        self.pruning_mode = pruning_mode
        self.oracle_client = oracle_client
        self.oracle_model = oracle_model
        self.char_threshold = char_threshold
        self.oracle_decisions: list[dict] = []
        self.pruned_rounds: list[int] = []

    def _detect_ack(self, text: str, prev_text: str, task_id: str, round_idx: int) -> dict:
        """Classify whether a reviewer message is an acknowledgment.

        Returns dict with at least 'is_ack' and 'round' keys.
        """
        if self.detection_mode == "oracle_5class":
            return oracle_5class_is_ack(
                self.oracle_client, self.oracle_model,
                text, prev_text, task_id, round_idx,
            )
        else:
            is_ack = heuristic_is_ack(text, self.char_threshold)
            return {
                "round": round_idx,
                "is_ack": is_ack,
                "confidence": 1.0,
                "function_type": "acknowledgment" if is_ack else "non_ack",
                "method": "heuristic",
                "char_len": len(text.strip()),
            }

    def run(self, task_prompt: str, task_id: str = "") -> list[dict]:
        """Run hierarchical pipeline with ack detection on reviewer messages.

        When pruning_mode='skip' and a reviewer ack is detected, the ack is still
        recorded in the trace but NOT relayed to the solver as a revision prompt.
        The conversation ends after the solver's last code submission.
        """
        self.message_trace = []
        self.oracle_decisions = []
        self.pruned_rounds = []

        solver_name, reviewer_name = self.agent_names[0], self.agent_names[1]
        solver_sys = self.agents[solver_name]
        reviewer_sys = self.agents[reviewer_name]

        self._record("user", solver_name, task_prompt, 0)

        conversation_for_solver = [{"role": "user", "content": task_prompt}]
        conversation_for_reviewer = []
        round_idx = 1
        prev_text = task_prompt

        for iteration in range(self.max_rounds // 2):
            solver_reply = self._call_llm(solver_sys, conversation_for_solver)
            self._record(solver_name, reviewer_name, solver_reply, round_idx)
            conversation_for_solver.append({"role": "assistant", "content": solver_reply})
            round_idx += 1

            if round_idx > self.max_rounds:
                break

            # Build reviewer prompt (same as TracedTeam)
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

            # Ack detection on reviewer's reply
            decision = self._detect_ack(reviewer_reply, solver_reply, task_id, round_idx)
            self.oracle_decisions.append(decision)

            if decision["is_ack"]:
                if self.pruning_mode == "skip":
                    self.pruned_rounds.append(round_idx)
                    logger.debug("Pruned reviewer ack at round %d for %s", round_idx, task_id)
                    break
                # pruning_mode='none': record but continue normally
                break  # ack = LGTM, conversation ends naturally

            round_idx += 1

            if "lgtm" in reviewer_reply.lower() or round_idx > self.max_rounds:
                break

            # Relay reviewer feedback to solver for revision
            revision_prompt = (
                f"The reviewer found issues with your solution:\n\n{reviewer_reply}\n\n"
                f"Original problem:\n{task_prompt}\n\n"
                "Please provide a corrected implementation."
            )
            conversation_for_solver.append({"role": "user", "content": revision_prompt})

        return self.message_trace


# ---------------------------------------------------------------------------
# Paired experiment runner
# ---------------------------------------------------------------------------

def run_paired_experiment(
    task: dict,
    cfg: dict,
    detection_mode: str,
    oracle_client: OpenAI | None,
    oracle_model: str,
    char_threshold: int,
    eval_timeout: int = 10,
) -> dict:
    """Run baseline (no pruning) and pruned (skip acks) on a single HumanEval task.

    Returns a dict with task_id, baseline/pruned results, and oracle decisions.
    """
    task_id = task["task_id"]
    prompt = task["prompt"]
    test_code = task["test"]
    entry_point = task["entry_point"]

    results = {}

    for mode_label, pruning_mode in [("baseline", "none"), ("pruned", "skip")]:
        team = PrunedTracedTeam(
            cfg,
            detection_mode=detection_mode,
            pruning_mode=pruning_mode,
            oracle_client=oracle_client,
            oracle_model=oracle_model,
            char_threshold=char_threshold,
        )
        try:
            messages = team.run(prompt, task_id=task_id)
        except Exception:
            logger.exception("Failed %s on task %s", mode_label, task_id)
            results[mode_label] = {
                "is_correct": False, "error": "llm_exception",
                "num_messages": 0, "final_code": "",
            }
            continue
        finally:
            gc.collect()

        final_code = extract_final_code(messages, prompt)

        eval_result = {"is_correct": False, "error": "no_code", "execution_time": 0.0}
        if final_code:
            eval_result = execute_code_safely(final_code, test_code, entry_point, timeout=eval_timeout)

        agent_messages = [m for m in messages if m["sender"] != "user"]

        results[mode_label] = {
            "is_correct": eval_result["is_correct"],
            "error": eval_result.get("error"),
            "execution_time": eval_result.get("execution_time", 0.0),
            "num_messages": len(agent_messages),
            "final_code": final_code,
            "messages": agent_messages,
            "oracle_decisions": team.oracle_decisions,
            "pruned_rounds": team.pruned_rounds,
        }

    return {
        "task_id": task_id,
        "humaneval_id": task["task_id"],
        "baseline": results.get("baseline", {}),
        "pruned": results.get("pruned", {}),
    }


# ---------------------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------------------

def compute_statistics(records: list[dict]) -> dict:
    """Compute aggregate statistics from paired experiment results.

    Returns McNemar test, TOST equivalence (epsilon=1pp), non-inferiority (delta=-3pp),
    and summary counts.
    """
    from scipy import stats as sp_stats

    baseline_correct = [r["baseline"]["is_correct"] for r in records]
    pruned_correct = [r["pruned"]["is_correct"] for r in records]

    n = len(records)
    base_acc = sum(baseline_correct) / n
    prune_acc = sum(pruned_correct) / n

    # Paired confusion: a=both correct, b=base only, c=prune only, d=both wrong
    a = sum(1 for b, p in zip(baseline_correct, pruned_correct) if b and p)
    b = sum(1 for b, p in zip(baseline_correct, pruned_correct) if b and not p)
    c = sum(1 for b, p in zip(baseline_correct, pruned_correct) if not b and p)
    d = sum(1 for b, p in zip(baseline_correct, pruned_correct) if not b and not p)

    # McNemar's test (exact binomial when b+c < 25)
    bc = b + c
    if bc > 0:
        if bc < 25:
            mcnemar_p = sp_stats.binomtest(b, bc, 0.5).pvalue
        else:
            chi2 = (abs(b - c) - 1) ** 2 / bc
            mcnemar_p = sp_stats.chi2.sf(chi2, 1)
    else:
        mcnemar_p = 1.0

    # TOST equivalence test (epsilon = 1 percentage point)
    diff = prune_acc - base_acc
    epsilon = 0.01
    se = (sum((p - b) ** 2 for b, p in zip(baseline_correct, pruned_correct)) / (n * (n - 1))) ** 0.5 if n > 1 else 0.01
    if se > 0:
        t_lower = (diff - (-epsilon)) / se
        t_upper = (diff - epsilon) / se
        p_lower = 1 - sp_stats.t.cdf(t_lower, n - 1)
        p_upper = sp_stats.t.cdf(t_upper, n - 1)
        tost_p = max(p_lower, p_upper)
    else:
        tost_p = 0.0 if abs(diff) < epsilon else 1.0

    # Non-inferiority test (delta = -3 percentage points)
    delta = -0.03
    if se > 0:
        t_ni = (diff - delta) / se
        ni_p = 1 - sp_stats.t.cdf(t_ni, n - 1)
    else:
        ni_p = 0.0 if diff > delta else 1.0

    # Message reduction
    base_msgs = sum(r["baseline"]["num_messages"] for r in records)
    prune_msgs = sum(r["pruned"]["num_messages"] for r in records)
    total_pruned = sum(len(r["pruned"].get("pruned_rounds", [])) for r in records)

    return {
        "n_tasks": n,
        "baseline_accuracy": round(base_acc, 4),
        "pruned_accuracy": round(prune_acc, 4),
        "accuracy_diff": round(diff, 4),
        "mcnemar": {"b": b, "c": c, "p_value": round(mcnemar_p, 6)},
        "tost_equivalence": {"epsilon": epsilon, "p_value": round(tost_p, 6)},
        "non_inferiority": {"delta": delta, "p_value": round(ni_p, 6)},
        "paired_confusion": {"both_correct": a, "base_only": b, "prune_only": c, "both_wrong": d},
        "messages": {
            "baseline_total": base_msgs,
            "pruned_total": prune_msgs,
            "reduction_pct": round((1 - prune_msgs / base_msgs) * 100, 2) if base_msgs > 0 else 0,
            "total_pruned_rounds": total_pruned,
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="HumanEval E2E pruning: paired baseline vs. ack-pruned experiments"
    )
    parser.add_argument("--mode", choices=["oracle", "heuristic"], default="oracle",
                        help="Ack detection method: oracle (GPT-4o 5-class) or heuristic (char-threshold)")
    parser.add_argument("--config", type=str, default="configs/metagpt_qwen.yaml")
    parser.add_argument("--num-tasks", type=int, default=164,
                        help="Number of HumanEval tasks (max 164)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--char-threshold", type=int, default=30,
                        help="Character threshold for heuristic ack detection")
    parser.add_argument("--oracle-cache", type=str, default=None,
                        help="Path to precomputed oracle cache JSON")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (default: outputs/humaneval_pruning/<mode>_seed<S>.json)")
    args = parser.parse_args()

    cfg = load_config(args.config)
    cfg["data"]["seed"] = args.seed
    cfg["data"]["num_tasks"] = args.num_tasks

    # Oracle API setup
    oracle_client = None
    oracle_model = "openai/gpt-4o"
    if args.mode == "oracle":
        api_key = [REDACTED]"OPENAI_API_KEY", "")
        if not api_key:
            logger.error("OPENAI_API_KEY not set; required for oracle mode")
            sys.exit(1)
        oracle_client = OpenAI(base_url="http://47.94.22.126/v1", api_key=[REDACTED]

    # Load oracle cache if provided
    global _oracle_cache
    if args.oracle_cache and os.path.exists(args.oracle_cache):
        _oracle_cache = _load_oracle_cache(args.oracle_cache)
        logger.info("Loaded oracle cache: %d entries", len(_oracle_cache))

    # Output path
    output_path = args.output or os.path.join(
        "outputs", "humaneval_pruning", f"{args.mode}_seed{args.seed}.json"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Load dataset
    dataset = load_humaneval(num_tasks=args.num_tasks, seed=args.seed)
    logger.info("Loaded %d HumanEval tasks (seed=%d)", len(dataset), args.seed)

    # Check vLLM availability
    vllm_client = OpenAI(
        base_url=cfg["model"]["api_base"],
        api_key=[REDACTED]"model"].get("api_key", "EMPTY"),
    )
    try:
        models = vllm_client.models.list()
        logger.info("vLLM serving: %s", [m.id for m in models.data])
    except Exception as e:
        logger.error("Cannot connect to vLLM at %s: %s", cfg["model"]["api_base"], e)
        sys.exit(1)

    eval_timeout = cfg.get("evaluation", {}).get("timeout", 10)

    # Run paired experiments
    records = []
    for idx, task in enumerate(dataset):
        logger.info("[%d/%d] %s: %s...", idx + 1, len(dataset), task["task_id"], task["prompt"][:50])

        result = run_paired_experiment(
            task, cfg,
            detection_mode="oracle_5class" if args.mode == "oracle" else "heuristic",
            oracle_client=oracle_client,
            oracle_model=oracle_model,
            char_threshold=args.char_threshold,
            eval_timeout=eval_timeout,
        )
        records.append(result)

        # Log running accuracy
        if (idx + 1) % 10 == 0 or idx == len(dataset) - 1:
            base_acc = sum(r["baseline"]["is_correct"] for r in records) / len(records)
            prune_acc = sum(r["pruned"]["is_correct"] for r in records) / len(records)
            logger.info("Running accuracy [%d]: baseline=%.3f pruned=%.3f",
                        len(records), base_acc, prune_acc)

    # Compute statistics
    stats = compute_statistics(records)
    logger.info("Final: baseline=%.4f pruned=%.4f diff=%.4f mcnemar_p=%.4f",
                stats["baseline_accuracy"], stats["pruned_accuracy"],
                stats["accuracy_diff"], stats["mcnemar"]["p_value"])

    # Strip full code/messages from saved records to reduce file size
    saved_records = []
    for r in records:
        saved = {
            "task_id": r["task_id"],
            "humaneval_id": r["humaneval_id"],
            "baseline": {
                "is_correct": r["baseline"]["is_correct"],
                "num_messages": r["baseline"]["num_messages"],
                "error": r["baseline"].get("error"),
            },
            "pruned": {
                "is_correct": r["pruned"]["is_correct"],
                "num_messages": r["pruned"]["num_messages"],
                "error": r["pruned"].get("error"),
                "oracle_decisions": r["pruned"].get("oracle_decisions", []),
                "pruned_rounds": r["pruned"].get("pruned_rounds", []),
            },
        }
        saved_records.append(saved)

    output_data = {
        "metadata": {
            "mode": args.mode,
            "seed": args.seed,
            "num_tasks": len(dataset),
            "char_threshold": args.char_threshold if args.mode == "heuristic" else None,
            "model": cfg["model"]["name"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
        "statistics": stats,
        "records": saved_records,
    }

    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s", output_path)


if __name__ == "__main__":
    main()
