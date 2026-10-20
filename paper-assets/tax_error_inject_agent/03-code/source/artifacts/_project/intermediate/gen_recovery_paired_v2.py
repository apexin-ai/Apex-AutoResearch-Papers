"""
gen_recovery_paired.py (v2) — Generate recovery-paired SFT data from injected trajectories.

v2 changes vs v1:
  - Incremental writing: each result is appended to output jsonl immediately
  - Resume: on startup, reads existing output and skips already-processed inject_ids
  - SIGUSR1 handler: prints progress snapshot to stderr (safe, non-destructive)

Input:
  - injected_variants.jsonl  (corrupted trajectories with injection_info)
  - successful_trajectories.jsonl  (clean trajectories for ground-truth obs)

Output:
  - recovery_paired.jsonl  (multi-turn SFT data with error→recovery transitions)

Dependencies: openai
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import sys
import threading
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

HISTORY_WINDOW = 10

OPERATOR_LABELS = {
    "P1_step_order_swap": "P1_StepOrderSwap",
    "P2_sub_goal_deletion": "P2_SubGoalDeletion",
    "C1_context_truncation": "C1_ContextTruncation",
    "C4_observation_masking": "C4_ObservationMasking",
}

# GPT-5.2 pricing (per token)
MODEL_PRICING = {
    "openai/gpt-5.2": {"input": 2.50 / 1_000_000, "output": 10.00 / 1_000_000},
    "gpt-5.2": {"input": 2.50 / 1_000_000, "output": 10.00 / 1_000_000},
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_jsonl(path: str) -> List[Dict[str, Any]]:
    entries = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def build_source_index(
    trajectories: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    """Index clean trajectories by their ID for O(1) lookup."""
    index = {}
    for t in trajectories:
        tid = t.get("id", "")
        if tid:
            index[tid] = t
    return index


def load_completed_ids(output_path: Path) -> Set[str]:
    """Read existing output file and return set of already-processed inject_ids."""
    done = set()
    if not output_path.exists():
        return done
    with open(output_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                iid = obj.get("inject_id", "")
                if iid:
                    done.add(iid)
            except json.JSONDecodeError:
                continue
    return done


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

def format_history_block(steps: List[Dict[str, Any]], window: int = HISTORY_WINDOW) -> str:
    parts = []
    for s in steps[-window:]:
        obs = s.get("observation", s.get("text_obs", ""))
        action = s.get("action", "")
        parts.append(f"Observation: {obs}")
        if action:
            parts.append(f"Action: {action}")
    return "\n".join(parts)


def build_recovery_step_prompt(
    task_desc: str,
    step_count: int,
    history: List[Dict[str, Any]],
    current_obs: str,
    admissible_commands: List[str],
    error_type: str,
    is_first_recovery_step: bool,
) -> str:
    history_str = format_history_block(history)
    actions_str = ", ".join(admissible_commands)

    if is_first_recovery_step:
        recovery_instruction = (
            f"\n[Recovery Required — {error_type}]\n"
            "The history above may contain errors or inconsistencies introduced "
            "by a prior fault. Carefully review the observation-action history. "
            "Identify any inconsistencies, missing steps, or corrupted information. "
            "Reason about the actual current state based on available evidence, "
            "then choose the correct next action to continue the task.\n"
        )
    else:
        recovery_instruction = ""

    return (
        f"You are an expert agent operating in the ALFRED Embodied Environment.\n"
        f"Your task is to: {task_desc}\n"
        f"Prior to this step, you have already taken {step_count} step(s).\n"
        f"Below are the most recent observations and actions:\n"
        f"{history_str}\n"
        f"{recovery_instruction}\n"
        f"Your current observation is: {current_obs}\n"
        f"Your admissible actions are: [{actions_str}]\n\n"
        f"Think step by step in <think></think> tags, then choose an action "
        f"in <action></action> tags.\n"
        f"The action MUST be one of the admissible actions listed above."
    )


# ---------------------------------------------------------------------------
# Token estimation
# ---------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    """Rough token count: ~4 chars per token for English text."""
    return max(1, len(text) // 4)


# ---------------------------------------------------------------------------
# API caller with retry
# ---------------------------------------------------------------------------

class RecoveryGenerator:
    def __init__(self, model: str, api_key: [REDACTED], base_url: str, max_retries: int = 3):
        self.model = model
        self.max_retries = max_retries
        self._lock = threading.Lock()
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_requests = 0

        from openai import OpenAI
        self.client = OpenAI(api_key=[REDACTED], base_url=base_url)

    def generate(self, prompt: str) -> Tuple[str, int, int]:
        """Call the API with retry. Returns (response_text, input_tokens, output_tokens)."""
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                    max_tokens=512,
                )
                text = response.choices[0].message.content or ""
                usage = response.usage
                inp = usage.prompt_tokens if usage else 0
                out = usage.completion_tokens if usage else 0

                with self._lock:
                    self.total_input_tokens += inp
                    self.total_output_tokens += out
                    self.total_requests += 1

                return text, inp, out
            except Exception as e:
                if attempt < self.max_retries - 1:
                    wait = 2 ** attempt
                    print(f"  API error (attempt {attempt+1}): {e}, retrying in {wait}s",
                          flush=True)
                    time.sleep(wait)
                else:
                    raise

    def cost(self) -> float:
        pricing = MODEL_PRICING.get(self.model, {"input": 2.5e-6, "output": 10e-6})
        return (self.total_input_tokens * pricing["input"]
                + self.total_output_tokens * pricing["output"])


# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------

def parse_response(text: str) -> Tuple[str, str]:
    import re
    think_m = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
    action_m = re.search(r"<action>(.*?)</action>", text, re.DOTALL)
    think = think_m.group(1).strip() if think_m else ""
    action = action_m.group(1).strip() if action_m else ""
    return think, action


def process_one_trajectory(
    injected: Dict[str, Any],
    source_traj: Dict[str, Any],
    generator: Optional[RecoveryGenerator],
    dry_run: bool,
) -> Optional[Dict[str, Any]]:
    info = injected["injection_info"]
    operator = info["operator"]
    injection_step = info["injection_step"]
    source_id = info["source_trajectory_id"]
    error_label = OPERATOR_LABELS.get(operator, operator)
    task_desc = injected.get("task_description", "")

    source_steps = source_traj.get("steps", [])
    injected_steps = injected.get("steps", [])

    corrupted_prefix = injected_steps[:injection_step]
    remaining_steps = source_steps[injection_step:]
    if not remaining_steps:
        return None

    # -- Build error prefix as SFT turns --
    error_prefix_turns = []
    prefix_history = []
    for i, step in enumerate(corrupted_prefix):
        obs = step.get("observation", "")
        think = step.get("think", "")
        action = step.get("action", "")
        admissible = step.get("admissible_commands", [])
        if not admissible and i < len(source_steps):
            admissible = source_steps[i].get("admissible_commands", [])

        prompt = build_recovery_step_prompt(
            task_desc, i, prefix_history, obs, admissible,
            error_label, is_first_recovery_step=False,
        )

        parts = []
        if think:
            parts.append(f"<think>{think}</think>")
        if action:
            parts.append(f"<action>{action}</action>")
        response = "\n".join(parts)

        error_prefix_turns.append({
            "messages": [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response},
            ]
        })
        prefix_history.append({"observation": obs, "action": action})

    # -- Build recovery continuation prompts --
    recovery_turns = []
    recovery_history = list(prefix_history)
    total_input_tokens_est = 0
    total_output_tokens_est = 0

    for j, step in enumerate(remaining_steps):
        obs = step.get("observation", "")
        admissible = step.get("admissible_commands", [])
        step_idx = injection_step + j
        is_first = (j == 0)

        prompt = build_recovery_step_prompt(
            task_desc, step_idx, recovery_history, obs, admissible,
            error_label, is_first_recovery_step=is_first,
        )

        prompt_tokens = estimate_tokens(prompt)
        response_tokens_est = 150
        total_input_tokens_est += prompt_tokens
        total_output_tokens_est += response_tokens_est

        if dry_run:
            think = step.get("think", "[DRY_RUN] recovery think")
            action = step.get("action", "[DRY_RUN] recovery action")
        else:
            raw_response, _, _ = generator.generate(prompt)
            think, action = parse_response(raw_response)
            if not action:
                action = step.get("action", "look")

        parts = []
        if think:
            parts.append(f"<think>{think}</think>")
        if action:
            parts.append(f"<action>{action}</action>")
        response = "\n".join(parts)

        recovery_turns.append({
            "messages": [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": response},
            ],
            "is_recovery": True,
            "recovery_step": j,
        })
        recovery_history.append({"observation": obs, "action": action})

    return {
        "inject_id": info["id"],
        "source_trajectory_id": source_id,
        "task_description": task_desc,
        "operator": operator,
        "error_label": error_label,
        "injection_step": injection_step,
        "total_original_steps": len(source_steps),
        "num_error_prefix_steps": len(error_prefix_turns),
        "num_recovery_steps": len(recovery_turns),
        "error_prefix": error_prefix_turns,
        "recovery_continuation": recovery_turns,
        "api_usage_estimate": {
            "input_tokens": total_input_tokens_est,
            "output_tokens": total_output_tokens_est,
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Global progress state for SIGUSR1 handler
_progress = {"processed": 0, "total": 0, "skipped": 0, "resumed": 0, "start_time": 0.0}


def _sigusr1_handler(signum, frame):
    elapsed = time.time() - _progress["start_time"]
    p = _progress
    rate = p["processed"] / elapsed if elapsed > 0 else 0
    remaining = (p["total"] - p["processed"] - p["resumed"]) / rate if rate > 0 else float("inf")
    print(
        f"\n[SIGUSR1 PROGRESS] processed={p['processed']}, resumed={p['resumed']}, "
        f"skipped={p['skipped']}, total={p['total']}, "
        f"elapsed={elapsed:.0f}s, rate={rate:.2f}/s, ETA={remaining:.0f}s",
        file=sys.stderr, flush=True,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate recovery-paired SFT data from injected trajectories (v2: incremental + resume).",
    )
    parser.add_argument(
        "--input", type=str,
        default="data/mini_pipeline_v2/injected_variants.jsonl",
        help="Path to injected variants JSONL",
    )
    parser.add_argument(
        "--source", type=str,
        default="data/trajectories/successful_trajectories.jsonl",
        help="Path to clean source trajectories JSONL",
    )
    parser.add_argument(
        "--output", type=str,
        default="data/recovery_paired/recovery_paired.jsonl",
        help="Output path for recovery-paired data",
    )
    parser.add_argument(
        "--model", type=str, default="openai/gpt-5.2",
        help="Model to use for recovery generation",
    )
    parser.add_argument(
        "--api-key", type=str, default="",
        help="API key for the model provider",
    )
    parser.add_argument(
        "--base-url", type=str, default="",
        help="Base URL for the model API",
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Limit number of entries to process (0=all)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Dry run (no API calls, estimate cost only)",
    )
    parser.add_argument(
        "--estimate-cost", action="store_true",
        help="Print cost estimate at the end",
    )
    parser.add_argument(
        "--flush-every", type=int, default=1,
        help="Flush output file every N entries (default: 1 = immediate)",
    )
    args = parser.parse_args()

    output_path = Path(args.output)

    # Install SIGUSR1 handler
    signal.signal(signal.SIGUSR1, _sigusr1_handler)

    # Load data
    print(f"Loading injected variants from {args.input} ...")
    injected_entries = load_jsonl(args.input)
    print(f"Loading source trajectories from {args.source} ...")
    source_trajectories = load_jsonl(args.source)
    source_index = build_source_index(source_trajectories)

    print(f"  Injected variants: {len(injected_entries)}")
    print(f"  Source trajectories: {len(source_trajectories)}")

    if args.limit > 0:
        injected_entries = injected_entries[:args.limit]
        print(f"  Limited to first {args.limit} entries")

    # Resume: load already-completed IDs
    completed_ids = load_completed_ids(output_path)
    if completed_ids:
        print(f"  Resuming: {len(completed_ids)} entries already in {output_path}, will skip them")

    # Generator
    generator = None
    if not args.dry_run:
        generator = RecoveryGenerator(
            model=args.model,
            api_key=[REDACTED],
            base_url=args.base_url,
        )

    # Update global progress
    _progress["total"] = len(injected_entries)
    _progress["resumed"] = len(completed_ids)
    _progress["start_time"] = time.time()

    # Process with incremental writes
    output_path.parent.mkdir(parents=True, exist_ok=True)
    out_file = open(output_path, "a") if not args.dry_run else None

    results = []
    skipped = 0
    total_input_tokens = 0
    total_output_tokens = 0
    op_counts = defaultdict(int)
    recovery_step_counts = []
    new_count = 0

    try:
        for idx, entry in enumerate(injected_entries):
            info = entry.get("injection_info", {})
            inject_id = info.get("id", "")
            source_id = info.get("source_trajectory_id", "")

            # Skip already-processed entries
            if inject_id and inject_id in completed_ids:
                continue

            source_traj = source_index.get(source_id)
            if source_traj is None:
                skipped += 1
                _progress["skipped"] = skipped
                continue

            result = process_one_trajectory(entry, source_traj, generator, args.dry_run)
            if result is None:
                skipped += 1
                _progress["skipped"] = skipped
                continue

            results.append(result)
            new_count += 1
            op_counts[result["operator"]] += 1
            recovery_step_counts.append(result["num_recovery_steps"])
            total_input_tokens += result["api_usage_estimate"]["input_tokens"]
            total_output_tokens += result["api_usage_estimate"]["output_tokens"]

            # Incremental write
            if out_file is not None:
                out_file.write(json.dumps(result, ensure_ascii=False) + "\n")
                if new_count % args.flush_every == 0:
                    out_file.flush()
                    os.fsync(out_file.fileno())

            _progress["processed"] = new_count

            if (idx + 1) % 100 == 0:
                print(f"  Processed {idx+1}/{len(injected_entries)} (new: {new_count}, resumed: {len(completed_ids)})", flush=True)

    finally:
        if out_file is not None:
            out_file.flush()
            os.fsync(out_file.fileno())
            out_file.close()

    if not args.dry_run:
        total_in_file = len(completed_ids) + new_count
        print(f"\nOutput: {output_path} ({total_in_file} total entries, {new_count} new)")

    # Summary
    print(f"\n{'='*50}")
    print(f"Recovery-Paired Generation Summary")
    print(f"{'='*50}")
    print(f"Total injected variants:   {len(injected_entries)}")
    print(f"Resumed from checkpoint:   {len(completed_ids)}")
    print(f"Newly processed:           {new_count}")
    print(f"Skipped (no source match): {skipped}")
    print(f"\nBy operator:")
    for op, count in sorted(op_counts.items()):
        print(f"  {OPERATOR_LABELS.get(op, op)}: {count}")

    if recovery_step_counts:
        avg_steps = sum(recovery_step_counts) / len(recovery_step_counts)
        print(f"\nRecovery steps per trajectory:")
        print(f"  Mean: {avg_steps:.1f}")
        print(f"  Min:  {min(recovery_step_counts)}")
        print(f"  Max:  {max(recovery_step_counts)}")
        print(f"  Total recovery API calls needed: {sum(recovery_step_counts)}")

    # Cost estimate
    if args.estimate_cost or args.dry_run:
        pricing = MODEL_PRICING.get(args.model, {"input": 2.5e-6, "output": 10e-6})
        input_cost = total_input_tokens * pricing["input"]
        output_cost = total_output_tokens * pricing["output"]
        total_cost = input_cost + output_cost
        print(f"\n--- Cost Estimate ({args.model}) ---")
        print(f"  Estimated input tokens:  {total_input_tokens:,}")
        print(f"  Estimated output tokens: {total_output_tokens:,}")
        print(f"  Input cost:   ${input_cost:.4f}")
        print(f"  Output cost:  ${output_cost:.4f}")
        print(f"  Total cost:   ${total_cost:.4f}")

    # Dry-run sample
    if args.dry_run and results:
        print(f"\n--- Dry-Run Sample (first entry) ---")
        sample = results[0]
        print(f"  Inject ID: {sample['inject_id']}")
        print(f"  Source trajectory: {sample['source_trajectory_id']}")
        print(f"  Operator: {sample['error_label']}")
        print(f"  Injection step: {sample['injection_step']}")
        print(f"  Error prefix steps: {sample['num_error_prefix_steps']}")
        print(f"  Recovery steps: {sample['num_recovery_steps']}")
        if sample["recovery_continuation"]:
            first_recovery = sample["recovery_continuation"][0]
            prompt_preview = first_recovery["messages"][0]["content"][:500]
            print(f"\n  First recovery prompt (preview):\n{prompt_preview}...")


if __name__ == "__main__":
    main()
