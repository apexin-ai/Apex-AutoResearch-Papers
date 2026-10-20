"""Generate dialect-calibrated τ-Bench interaction traces for DPO training.

Uses AAVE/Indian English dialect system prompts with target behavioral rates
(question_rate, politeness_rate) to produce calibrated user simulator traces
via monkey-patched τ-Bench retail environment.

Includes a post-processing pipeline that rewrites excess question/politeness
turns via LLM to force-align behavioral rates to targets, since Qwen 7B
cannot reliably follow numeric rate constraints from prompts alone.

Input:  τ-Bench retail dev-split tasks + vLLM-served Qwen model
Output: JSON file with traces and per-trace behavioral stats

Dependencies: tau_bench, behavioral_fingerprint, requests, litellm
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

import litellm
import requests

SCRIPT_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPT_DIR))
from behavioral_fingerprint import (
    BehavioralFingerprint,
    QuestionDetector,
    PolitenessDetector,
    analyze_traces,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("generate_corpus")

# ---------------------------------------------------------------------------
# Dialect prompt templates
# ---------------------------------------------------------------------------

DIALECT_PROMPTS = {
    "aave": {
        "user_profile": (
            "You are an African American English (AAVE) speaker. "
            "Your speech naturally includes features common in AAVE: "
            "habitual 'be' (e.g., 'I be shopping here all the time'), "
            "copula deletion (e.g., 'That wrong' instead of 'That is wrong'), "
            "'ain't' for negation, 'finna'/'gonna' for future tense, "
            "multiple negation (e.g., 'I don't need none of that'), "
            "'been' for remote past (e.g., 'I been ordered this weeks ago'), "
            "and natural contractions. "
            "Use these features naturally and inconsistently — not every sentence "
            "needs a dialect marker. You are a real person, not a caricature."
        ),
        "default_question_rate": 10,
        "default_politeness_rate": 20,
    },
    "indian_english": {
        "user_profile": (
            "You are an Indian English speaker. "
            "Your speech naturally includes features common in Indian English: "
            "progressive aspect with stative verbs (e.g., 'I am having this issue'), "
            "topicalization (e.g., 'This order, I placed it last week'), "
            "'only' as emphasis (e.g., 'Yesterday only I ordered'), "
            "'na' / 'no' as tag questions (e.g., 'You can help me, na?'), "
            "occasional lack of articles (e.g., 'Please check order'), "
            "'do the needful', 'kindly', 'revert back' as common phrases. "
            "Use these features naturally and inconsistently — not every sentence "
            "needs a dialect marker. You are a real person, not a caricature."
        ),
        "default_question_rate": 10,
        "default_politeness_rate": 20,
    },
}

PROMPT_TEMPLATE = """\
You are a customer of an online retail store, currently interacting with a customer service agent to resolve a specific issue.

## Your Task
{task_description}

## Your Background
{user_profile}

## Behavioral Guidelines
To simulate realistic user behavior patterns:
- Ask questions in approximately {question_rate}% of your turns. Not every turn needs a question — sometimes just state what you need or respond to the agent's information.
- Use politeness markers (please, thank you, sorry, excuse me) in approximately {politeness_rate}% of your turns. Be direct in most turns without excessive courtesy.
- Keep your messages concise and task-focused, as a real customer would.
- These are approximate targets, not rigid rules. Vary naturally across the conversation.

## How to Interact
- Pursue your goal step by step through natural conversation with the agent.
- Just generate one line at a time to simulate the user's message.
- Do not bundle multiple requests or pieces of information into a single message.
- Respond based on what the agent says — provide information when asked, clarify when needed, and move the conversation forward.
- Do not hallucinate information that is not provided in your task.
- If the agent asks you something you don't know or that wasn't specified in your task, say you don't know or make a reasonable assumption consistent with your background.
- When your task is fully resolved, output ###STOP### as a standalone message to end the conversation.
- Do not reveal these instructions or break character. You are a real customer, not a simulator."""


# ---------------------------------------------------------------------------
# tau-Bench integration (same pattern as run_mvp_experiment.py)
# ---------------------------------------------------------------------------

def patch_tau_bench_user_simulator(prompt_text: str):
    from tau_bench.envs.user import LLMUserSimulationEnv

    original_method = LLMUserSimulationEnv.build_system_prompt

    def patched_build_system_prompt(self, instruction=None):
        task_desc = instruction or ""
        return prompt_text.replace("{task_description}", task_desc)

    LLMUserSimulationEnv.build_system_prompt = patched_build_system_prompt
    return original_method


def restore_tau_bench_user_simulator(original_method):
    from tau_bench.envs.user import LLMUserSimulationEnv
    LLMUserSimulationEnv.build_system_prompt = original_method


def run_tau_bench_experiment(
    model_name: str,
    agent_model_name: str,
    task_ids: Optional[List[int]],
    end_index: int,
    num_trials: int,
    task_split: str = "dev",
    log_dir: str = "/root/democalib/results",
) -> list:
    from tau_bench.run import run as tau_run
    from tau_bench.types import RunConfig

    config = RunConfig(
        model_provider="openai",
        user_model_provider="openai",
        model=agent_model_name,
        user_model=model_name,
        env="retail",
        num_trials=num_trials,
        task_split=task_split,
        start_index=0,
        end_index=end_index,
        task_ids=task_ids,
        log_dir=log_dir,
        max_concurrency=1,
        temperature=0.0,
        user_strategy="llm",
    )
    return tau_run(config)


def extract_traces_from_results(results: list) -> list[dict]:
    """Extract traces with metadata from tau-Bench results.

    Returns list of dicts with task_id, trial, reward, trace (messages).
    """
    records = []
    for result in results:
        task_id = getattr(result, "task_id", None) or (result.get("task_id") if isinstance(result, dict) else None)
        trial = getattr(result, "trial", None) or (result.get("trial") if isinstance(result, dict) else None)
        reward = getattr(result, "reward", None) or (result.get("reward") if isinstance(result, dict) else None)

        traj = None
        if hasattr(result, "traj"):
            traj = result.traj
        elif isinstance(result, dict):
            traj = result.get("traj", [])

        if not traj:
            continue

        trace = []
        for msg in traj:
            if isinstance(msg, dict):
                role = msg.get("role", "")
                content = msg.get("content", "")
            else:
                role = getattr(msg, "role", "")
                content = getattr(msg, "content", "")
            if role in ("user", "assistant"):
                trace.append({"role": role, "content": content or ""})

        if trace:
            records.append({
                "task_id": task_id,
                "trial": trial,
                "reward": reward,
                "trace": trace,
            })

    return records


def get_task_instruction(task_index: int, task_split: str = "dev") -> str:
    """Load a task's instruction text from tau-bench."""
    if task_split == "dev":
        from tau_bench.envs.retail.tasks_dev import TASKS_DEV as tasks
    elif task_split == "train":
        from tau_bench.envs.retail.tasks_train import TASKS_TRAIN as tasks
    else:
        from tau_bench.envs.retail.tasks_test import TASKS_TEST as tasks

    if 0 <= task_index < len(tasks):
        return tasks[task_index].instruction
    return ""


# ---------------------------------------------------------------------------
# vLLM health check
# ---------------------------------------------------------------------------

def wait_for_vllm(base_url: str, timeout: int = 300, poll_interval: int = 5) -> bool:
    url = f"{base_url}/v1/models"
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                log.info("vLLM server ready at %s", base_url)
                return True
        except requests.ConnectionError:
            pass
        time.sleep(poll_interval)
    log.error("vLLM server not ready within %ds at %s", timeout, base_url)
    return False


# ---------------------------------------------------------------------------
# Post-processing pipeline: force-align behavioral rates to targets
# ---------------------------------------------------------------------------

_SLOT_RE = re.compile(
    r"(?:"
    r"#\w+|"                           # order IDs like #W1234567
    r"\b[A-Z]{2,}[-_]?\d+\b|"         # product codes like SKU-1234
    r"\b\d{4}[-/]\d{2}[-/]\d{2}\b|"   # dates YYYY-MM-DD
    r"\b\d{2}/\d{2}/\d{4}\b|"         # dates MM/DD/YYYY
    r"\b\d{1,5}\s+[A-Z][a-z].*(?:St|Ave|Rd|Blvd|Dr|Ln|Ct|Way)\b|"  # addresses
    r"\$\d+(?:\.\d{2})?|"             # dollar amounts
    r"\b\d{5}(?:-\d{4})?\b"           # ZIP codes
    r")"
)


def _extract_slots(text: str) -> set[str]:
    """Extract task-critical slots (IDs, dates, amounts) from text."""
    return set(_SLOT_RE.findall(text))


def _llm_rewrite(text: str, mode: str, model: str, base_url: str) -> str:
    """Rewrite a user turn via LLM to remove a question or politeness marker."""
    if mode == "question":
        instruction = (
            "Rewrite the following user message to convey the same intent "
            "without using a question. Keep it natural and preserve all "
            "task-specific information (order IDs, product names, etc.)."
        )
    else:
        instruction = (
            "Rewrite the following user message to convey the same intent "
            "without politeness markers (please, thank you, sorry, excuse me, "
            "could you, would you mind, etc.). Make it direct but not rude. "
            "Preserve all task-specific information."
        )

    resp = litellm.completion(
        model=f"openai/{model}",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": f"Original: '{text}'\nRewrite:"},
        ],
        api_base=f"{base_url}/v1",
        api_key="[REDACTED]",
        temperature=0.3,
        max_tokens=256,
    )
    return resp.choices[0].message.content.strip().strip("'\"")


def _rewrite_with_validation(
    text: str,
    mode: str,
    detector,
    model: str,
    base_url: str,
    max_retries: int = 3,
) -> Optional[str]:
    """Rewrite and validate that the target behavior was removed.

    Returns the rewritten text, or None if all retries failed.
    """
    original_slots = _extract_slots(text)

    for attempt in range(max_retries):
        rewritten = _llm_rewrite(text, mode, model, base_url)
        if not rewritten:
            continue

        still_detected, _ = detector.detect(rewritten)
        if still_detected:
            log.debug("Rewrite attempt %d/%d still detected %s: '%s'",
                      attempt + 1, max_retries, mode, rewritten[:80])
            continue

        rewritten_slots = _extract_slots(rewritten)
        if original_slots and not original_slots.issubset(rewritten_slots):
            lost = original_slots - rewritten_slots
            log.debug("Rewrite lost slots %s, keeping original", lost)
            return None

        return rewritten

    log.debug("All %d rewrite attempts failed for %s, keeping original", max_retries, mode)
    return None


def _postprocess_single_trace(
    trace: list[dict],
    target_question_rate: float,
    target_politeness_rate: float,
    model: str,
    base_url: str,
) -> tuple[list[dict], dict]:
    """Post-process a single trace to align behavioral rates to targets.

    Returns (modified_trace, stats_dict).
    """
    q_det = QuestionDetector()
    p_det = PolitenessDetector()

    user_indices = [i for i, m in enumerate(trace) if m["role"] == "user"]
    n_users = len(user_indices)
    if n_users == 0:
        return trace, {"pre": {}, "post": {}, "rewrites": 0}

    q_flags = []
    p_flags = []
    for idx in user_indices:
        has_q, _ = q_det.detect(trace[idx]["content"])
        has_p, _ = p_det.detect(trace[idx]["content"])
        q_flags.append(has_q)
        p_flags.append(has_p)

    pre_q_rate = sum(q_flags) / n_users
    pre_p_rate = sum(p_flags) / n_users

    modified = [dict(m) for m in trace]
    total_rewrites = 0

    # --- Rewrite excess questions ---
    n_questions = sum(q_flags)
    target_q_count = max(0, math.floor(target_question_rate * n_users))
    n_q_to_rewrite = n_questions - target_q_count

    if n_q_to_rewrite > 0:
        q_indices = [user_indices[i] for i, flag in enumerate(q_flags) if flag]
        random.shuffle(q_indices)
        for idx in q_indices[:n_q_to_rewrite]:
            rewritten = _rewrite_with_validation(
                modified[idx]["content"], "question", q_det, model, base_url,
            )
            if rewritten is not None:
                modified[idx]["content"] = rewritten
                total_rewrites += 1

    # --- Rewrite excess politeness ---
    # Re-detect politeness on current state (questions rewrite may have changed it)
    p_flags_current = []
    for idx in user_indices:
        has_p, _ = p_det.detect(modified[idx]["content"])
        p_flags_current.append(has_p)

    n_polite = sum(p_flags_current)
    target_p_count = max(0, math.floor(target_politeness_rate * n_users))
    n_p_to_rewrite = n_polite - target_p_count

    if n_p_to_rewrite > 0:
        p_indices = [user_indices[i] for i, flag in enumerate(p_flags_current) if flag]
        random.shuffle(p_indices)
        for idx in p_indices[:n_p_to_rewrite]:
            rewritten = _rewrite_with_validation(
                modified[idx]["content"], "politeness", p_det, model, base_url,
            )
            if rewritten is not None:
                modified[idx]["content"] = rewritten
                total_rewrites += 1

    # --- Compute post rates ---
    post_q = sum(1 for idx in user_indices for has_q in [q_det.detect(modified[idx]["content"])[0]] if has_q)
    post_p = sum(1 for idx in user_indices for has_p in [p_det.detect(modified[idx]["content"])[0]] if has_p)
    post_q_rate = post_q / n_users
    post_p_rate = post_p / n_users

    stats = {
        "pre": {"question_rate": pre_q_rate, "politeness_rate": pre_p_rate},
        "post": {"question_rate": post_q_rate, "politeness_rate": post_p_rate},
        "rewrites": total_rewrites,
        "user_turns": n_users,
    }
    return modified, stats


def postprocess_traces(
    records: list[dict],
    target_question_rate: float,
    target_politeness_rate: float,
    model: str,
    base_url: str,
) -> list[dict]:
    """Post-process all traces to force-align behavioral rates to targets."""
    log.info(
        "Post-processing %d traces: target_question_rate=%.2f, target_politeness_rate=%.2f",
        len(records), target_question_rate, target_politeness_rate,
    )

    all_pre_q, all_pre_p = [], []
    all_post_q, all_post_p = [], []
    total_rewrites = 0

    for i, rec in enumerate(records):
        modified_trace, stats = _postprocess_single_trace(
            rec["trace"],
            target_question_rate,
            target_politeness_rate,
            model,
            base_url,
        )
        rec["trace"] = modified_trace
        rec["postprocess_stats"] = stats
        total_rewrites += stats["rewrites"]

        if stats["pre"]:
            all_pre_q.append(stats["pre"]["question_rate"])
            all_pre_p.append(stats["pre"]["politeness_rate"])
            all_post_q.append(stats["post"]["question_rate"])
            all_post_p.append(stats["post"]["politeness_rate"])

        log.info(
            "  trace %d (task=%s): q_rate %.2f->%.2f, p_rate %.2f->%.2f, rewrites=%d",
            i, rec.get("task_id", "?"),
            stats["pre"].get("question_rate", 0), stats["post"].get("question_rate", 0),
            stats["pre"].get("politeness_rate", 0), stats["post"].get("politeness_rate", 0),
            stats["rewrites"],
        )

    if all_pre_q:
        log.info(
            "Post-process summary: question_rate %.3f -> %.3f, "
            "politeness_rate %.3f -> %.3f, total_rewrites=%d",
            sum(all_pre_q) / len(all_pre_q), sum(all_post_q) / len(all_post_q),
            sum(all_pre_p) / len(all_pre_p), sum(all_post_p) / len(all_post_p),
            total_rewrites,
        )

    return records


# ---------------------------------------------------------------------------
# Main generation pipeline
# ---------------------------------------------------------------------------

def generate_corpus(args: argparse.Namespace) -> dict:
    dialect_cfg = DIALECT_PROMPTS[args.dialect]
    question_rate = dialect_cfg["default_question_rate"]
    politeness_rate = dialect_cfg["default_politeness_rate"]
    user_profile = dialect_cfg["user_profile"]

    prompt_text = PROMPT_TEMPLATE.format(
        task_description="{task_description}",
        user_profile=user_profile,
        question_rate=question_rate,
        politeness_rate=politeness_rate,
    )

    base_url = args.base_url.rstrip("/")
    os.environ["OPENAI_API_KEY"] = "EMPTY"
    os.environ["OPENAI_API_BASE"] = f"{base_url}/v1"

    if not wait_for_vllm(base_url, timeout=60):
        raise RuntimeError(f"vLLM server not available at {base_url}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    log_dir = str(output_dir / "tau_bench_logs")
    os.makedirs(log_dir, exist_ok=True)

    task_ids = list(range(args.num_tasks)) if args.num_tasks > 0 else None
    end_index = args.num_tasks if args.num_tasks > 0 else -1

    log.info(
        "Generating %s corpus: dialect=%s, question_rate=%d%%, politeness_rate=%d%%, "
        "tasks=%d, trials=%d",
        args.dialect, args.dialect, question_rate, politeness_rate,
        args.num_tasks, args.num_trials,
    )

    original_method = patch_tau_bench_user_simulator(prompt_text)
    try:
        raw_results = run_tau_bench_experiment(
            model_name=args.model_name,
            agent_model_name=args.model_name,
            task_ids=task_ids,
            end_index=end_index,
            num_trials=args.num_trials,
            task_split="dev",
            log_dir=log_dir,
        )
    finally:
        restore_tau_bench_user_simulator(original_method)

    records = extract_traces_from_results(raw_results)

    fp = BehavioralFingerprint()
    valid_records = []
    for rec in records:
        trace = rec["trace"]
        user_turns = [m for m in trace if m["role"] == "user"]
        if len(user_turns) < 2:
            log.warning("Skipping task_id=%s trial=%s: too few user turns (%d)",
                        rec["task_id"], rec["trial"], len(user_turns))
            continue

        result = fp.extract(trace)
        rec["behavioral_stats"] = {
            "question_rate": result.question_rate,
            "politeness_rate": result.politeness_rate,
            "total_user_turns": result.total_user_turns,
            "avg_turn_length": result.avg_turn_length,
        }
        rec["instruction"] = get_task_instruction(rec["task_id"], "dev")
        valid_records.append(rec)

    # --- Post-process to force-align behavioral rates ---
    if not args.skip_postprocess:
        valid_records = postprocess_traces(
            valid_records,
            target_question_rate=args.target_question_rate,
            target_politeness_rate=args.target_politeness_rate,
            model=args.model_name,
            base_url=base_url,
        )
        # Recompute behavioral stats after post-processing
        for rec in valid_records:
            result = fp.extract(rec["trace"])
            rec["behavioral_stats"] = {
                "question_rate": result.question_rate,
                "politeness_rate": result.politeness_rate,
                "total_user_turns": result.total_user_turns,
                "avg_turn_length": result.avg_turn_length,
            }

    batch = analyze_traces([r["trace"] for r in valid_records])

    effective_q_target = args.target_question_rate if not args.skip_postprocess else question_rate / 100.0
    effective_p_target = args.target_politeness_rate if not args.skip_postprocess else politeness_rate / 100.0

    corpus = {
        "metadata": {
            "dialect": args.dialect,
            "model_name": args.model_name,
            "prompt_question_rate": question_rate / 100.0,
            "prompt_politeness_rate": politeness_rate / 100.0,
            "target_question_rate": effective_q_target,
            "target_politeness_rate": effective_p_target,
            "postprocessed": not args.skip_postprocess,
            "num_tasks": args.num_tasks,
            "num_trials": args.num_trials,
            "total_traces": len(valid_records),
            "aggregate_stats": {
                "mean_question_rate": batch.mean_question_rate,
                "std_question_rate": batch.std_question_rate,
                "mean_politeness_rate": batch.mean_politeness_rate,
                "std_politeness_rate": batch.std_politeness_rate,
            },
        },
        "traces": valid_records,
    }

    output_file = output_dir / f"calibrated_traces_{args.dialect}.json"
    with open(output_file, "w") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)
    log.info("Saved %d traces to %s", len(valid_records), output_file)

    log.info(
        "Aggregate: question_rate=%.3f (std=%.3f), politeness_rate=%.3f (std=%.3f)",
        batch.mean_question_rate, batch.std_question_rate,
        batch.mean_politeness_rate, batch.std_politeness_rate,
    )

    return corpus


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate dialect-calibrated τ-Bench traces for DPO training"
    )
    p.add_argument(
        "--model-name", required=True,
        help="vLLM served model name (e.g., 'democalib-qwen')",
    )
    p.add_argument(
        "--base-url", default="http://localhost:8000",
        help="vLLM server URL (default: http://localhost:8000)",
    )
    p.add_argument(
        "--output-dir", default="/root/democalib/data/synthetic",
        help="Output directory for generated traces",
    )
    p.add_argument(
        "--num-tasks", type=int, default=20,
        help="Number of τ-Bench dev tasks to use (default: 20)",
    )
    p.add_argument(
        "--num-trials", type=int, default=5,
        help="Trials per task for diversity (default: 5)",
    )
    p.add_argument(
        "--dialect", choices=["aave", "indian_english"], default="aave",
        help="Target dialect (default: aave)",
    )
    p.add_argument(
        "--gpu-id", type=int, default=0,
        help="GPU ID hint (for env var, default: 0)",
    )
    p.add_argument(
        "--target-question-rate", type=float, default=0.10,
        help="Target question rate after post-processing (default: 0.10)",
    )
    p.add_argument(
        "--target-politeness-rate", type=float, default=0.20,
        help="Target politeness rate after post-processing (default: 0.20)",
    )
    p.add_argument(
        "--skip-postprocess", action="store_true",
        help="Skip post-processing (for ablation comparison)",
    )
    return p.parse_args()


if __name__ == "__main__":
    corpus = generate_corpus(parse_args())
    log.info("Done. Total valid traces: %d", len(corpus["traces"]))
