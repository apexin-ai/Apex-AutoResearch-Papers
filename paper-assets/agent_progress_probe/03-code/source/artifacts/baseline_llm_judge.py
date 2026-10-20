#!/usr/bin/env python3
"""LLM-as-Judge baseline for progress/stagnation classification.

Uses an LLM to zero-shot or few-shot classify agent trajectory windows,
as an upper-bound baseline for comparison with trained probes.

Requires: pip install openai
API key via --api_key or OPENROUTER_API_KEY env var.
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from collections import Counter

import openai
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


LABEL_MAP = {"stagnation": 0, "stagnating": 0, "stagnant": 0,
             "progress": 1, "progressing": 1, "advancing": 1}

ZERO_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.

Respond ONLY with a JSON object in this exact format:
{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""

ZERO_SHOT_USER = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.

{steps_text}

Based on these steps, is the agent making meaningful progress toward solving the task, or is it stagnating?"""

FEW_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.

Here are some examples:

{examples}

Respond ONLY with a JSON object in this exact format:
{{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}}"""


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


def truncate_text(text, max_chars=500):
    if not text:
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "... [truncated]"


def format_steps(steps, max_total_chars=6000):
    parts = []
    budget = max_total_chars
    per_step = max(200, budget // max(len(steps), 1))

    for i, step in enumerate(steps):
        role = step.get("role", "unknown")
        text = step.get("text", "") or ""
        truncated = truncate_text(text, per_step)
        part = f"[Step {i+1} | {role}]\n{truncated}"
        parts.append(part)

    return "\n\n".join(parts)


def load_trajectories_index(traj_path):
    """Build index: row_index -> trajectory dict."""
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if line:
                index[row_idx] = json.loads(line)
    return index


def extract_window_steps(window, traj_index):
    """Get actual step texts for a window from trajectory data."""
    row_idx = window["row_index"]
    step_indices = window["step_indices"]
    traj = traj_index.get(row_idx)
    if traj is None:
        return []
    trajectory = traj.get("trajectory", [])
    steps = []
    for si in step_indices:
        if si < len(trajectory):
            s = trajectory[si]
            steps.append({"role": s.get("role", "unknown"),
                          "text": s.get("text", "") or ""})
    return steps


def select_few_shot_examples(train_windows, traj_index, n_progress=1, n_stagnation=1, n_boundary=1):
    """Select high-confidence examples from training set for few-shot prompting."""
    progress_examples = []
    stagnation_examples = []

    for w in train_windows:
        if w["confidence"] >= 3:
            if w["majority_label"] == 1:
                progress_examples.append(w)
            elif w["majority_label"] == 0:
                stagnation_examples.append(w)

    # Boundary: conf=2 examples
    boundary_examples = [w for w in train_windows if w["confidence"] == 2]

    import random
    rng = random.Random(42)
    selected = []

    if progress_examples:
        selected.extend(rng.sample(progress_examples, min(n_progress, len(progress_examples))))
    if stagnation_examples:
        selected.extend(rng.sample(stagnation_examples, min(n_stagnation, len(stagnation_examples))))
    if boundary_examples:
        selected.extend(rng.sample(boundary_examples, min(n_boundary, len(boundary_examples))))

    examples_text = []
    for i, w in enumerate(selected):
        steps = extract_window_steps(w, traj_index)
        label_str = "progress" if w["majority_label"] == 1 else "stagnation"
        steps_formatted = format_steps(steps, max_total_chars=2000)
        examples_text.append(
            f"--- Example {i+1} (Answer: {label_str}) ---\n{steps_formatted}\n"
            f'{{"judgment": "{label_str}", "confidence": {w["confidence"]}, "reasoning": "This is a {label_str} example."}}'
        )

    return "\n\n".join(examples_text)


def parse_llm_response(text):
    """Extract judgment from LLM response with robust fallback."""
    # Try direct JSON parse
    try:
        obj = json.loads(text.strip())
        j = obj.get("judgment", "").lower().strip()
        if j in LABEL_MAP:
            return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
    except json.JSONDecodeError:
        pass

    # Try extracting JSON from markdown code block
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(1))
            j = obj.get("judgment", "").lower().strip()
            if j in LABEL_MAP:
                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
        except json.JSONDecodeError:
            pass

    # Try finding JSON object in text
    m = re.search(r"\{[^{}]*\"judgment\"[^{}]*\}", text, re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(0))
            j = obj.get("judgment", "").lower().strip()
            if j in LABEL_MAP:
                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
        except json.JSONDecodeError:
            pass

    # Keyword fallback
    lower = text.lower()
    if "stagnat" in lower and "progress" not in lower:
        return 0, 0, "keyword_fallback"
    if "progress" in lower and "stagnat" not in lower:
        return 1, 0, "keyword_fallback"

    return -1, 0, "parse_failed"


def call_llm(client, model, system_msg, user_msg, max_retries=3):
    """Call LLM with retry logic. Returns (response_text, input_tokens, output_tokens)."""
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0.0,
                max_tokens=256,
            )
            choice = resp.choices[0]
            usage = resp.usage
            return (
                choice.message.content or "",
                usage.prompt_tokens if usage else 0,
                usage.completion_tokens if usage else 0,
            )
        except (openai.RateLimitError, openai.APITimeoutError, openai.APIConnectionError) as e:
            wait = 2 ** (attempt + 1)
            print(f"  Retry {attempt+1}/{max_retries} after {type(e).__name__}, waiting {wait}s", flush=True)
            time.sleep(wait)
        except openai.APIError as e:
            if attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"  Retry {attempt+1}/{max_retries} after APIError: {e}, waiting {wait}s", flush=True)
                time.sleep(wait)
            else:
                print(f"  FAILED after {max_retries} retries: {e}", flush=True)
                return "", 0, 0
    return "", 0, 0


def main():
    parser = argparse.ArgumentParser(description="LLM-as-Judge baseline for progress/stagnation")
    parser.add_argument("--data_dir", required=True, help="Dir containing data/windows_labeled.jsonl")
    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
    parser.add_argument("--trajectories", required=True, help="Path to swe_agent_trajectories_5000.jsonl")
    parser.add_argument("--api_key", default=None, help="API key (or set OPENROUTER_API_KEY)")
    parser.add_argument("--base_url", default="http://47.94.22.126/v1", help="API base URL")
    parser.add_argument("--model", default="anthropic/claude-sonnet-4-6", help="Model ID")
    parser.add_argument("--mode", choices=["zero-shot", "few-shot"], default="zero-shot")
    parser.add_argument("--max_windows", type=int, default=0, help="0 = all test windows")
    parser.add_argument("--output", default="results/llm_judge_results.json", help="Output path")
    parser.add_argument("--resume", action="store_true", help="Resume from existing partial results")
    parser.add_argument("--rps", type=float, default=5.0, help="Max requests per second")
    parser.add_argument("--budget", type=float, default=100.0, help="Max spend in USD before pausing")
    parser.add_argument("--list_models", action="store_true", help="List available models and exit")
    args = parser.parse_args()

    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=60.0)

    if args.list_models:
        models = client.models.list()
        for m in models.data:
            print(m.id)
        return

    # Load data
    print("Loading windows...")
    windows_path = Path(args.data_dir) / "data" / "windows_labeled.jsonl"
    all_windows = []
    with open(windows_path) as f:
        for line in f:
            line = line.strip()
            if line:
                all_windows.append(json.loads(line))
    usable = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"  Total: {len(all_windows)}, usable: {len(usable)}")

    print("Loading split info...")
    with open(args.split_info) as f:
        split_info = json.load(f)

    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        windows = [usable[i] for i in keep_indices]
        print(f"  Confidence filter: {len(windows)}/{len(usable)}")
    else:
        windows = usable

    train_idx = split_info["train_indices"]
    test_idx = split_info["test_indices"]
    train_windows = [windows[i] for i in train_idx]
    test_windows = [windows[i] for i in test_idx]
    print(f"  Train: {len(train_windows)}, Test: {len(test_windows)}")

    if args.max_windows > 0:
        test_windows = test_windows[:args.max_windows]
        print(f"  Limiting to {len(test_windows)} test windows")

    gt = [w["majority_label"] for w in test_windows]
    print(f"  Test label dist: {dict(Counter(gt))}")

    print("Loading trajectories index...")
    traj_index = load_trajectories_index(args.trajectories)
    print(f"  Loaded {len(traj_index)} trajectories")

    # Prepare few-shot examples if needed
    few_shot_examples_text = ""
    if args.mode == "few-shot":
        print("Selecting few-shot examples...")
        few_shot_examples_text = select_few_shot_examples(train_windows, traj_index)

    # Resume support
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    completed = {}
    if args.resume and output_path.exists():
        with open(output_path) as f:
            prev = json.load(f)
        for r in prev.get("results", []):
            key = f"{r['trajectory_id']}_{r['window_idx']}"
            completed[key] = r
        print(f"  Resuming: {len(completed)} windows already done")

    # Run evaluation
    results = list(completed.values())
    total_input_tokens = sum(r.get("input_tokens", 0) for r in results)
    total_output_tokens = sum(r.get("output_tokens", 0) for r in results)
    parse_failures = sum(1 for r in results if r.get("predicted_label") == -1)
    min_interval = 1.0 / args.rps

    print(f"\nStarting LLM evaluation: {len(test_windows)} windows, model={args.model}, mode={args.mode}")
    print(f"Rate limit: {args.rps} rps, budget: ${args.budget}")
    print("-" * 60)

    last_call_time = 0.0
    for i, w in enumerate(test_windows):
        key = f"{w['trajectory_id']}_{w['window_idx']}"
        if key in completed:
            continue

        # Budget check
        est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
        if est_cost > args.budget:
            print(f"\n*** BUDGET EXCEEDED: ~${est_cost:.2f} > ${args.budget}. Stopping. ***")
            break

        # Rate limiting
        elapsed = time.time() - last_call_time
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        # Build prompt
        steps = extract_window_steps(w, traj_index)
        steps_text = format_steps(steps)

        if args.mode == "zero-shot":
            system_msg = ZERO_SHOT_SYSTEM
            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)
        else:
            system_msg = FEW_SHOT_SYSTEM.format(examples=few_shot_examples_text)
            user_msg = ZERO_SHOT_USER.format(n_steps=len(steps), steps_text=steps_text)

        # Call LLM
        last_call_time = time.time()
        resp_text, in_tok, out_tok = call_llm(client, args.model, system_msg, user_msg)
        total_input_tokens += in_tok
        total_output_tokens += out_tok

        pred_label, pred_conf, reasoning = parse_llm_response(resp_text)
        if pred_label == -1:
            parse_failures += 1

        result = {
            "trajectory_id": w["trajectory_id"],
            "window_idx": w["window_idx"],
            "true_label": w["majority_label"],
            "predicted_label": pred_label,
            "llm_confidence": pred_conf,
            "reasoning": reasoning,
            "input_tokens": in_tok,
            "output_tokens": out_tok,
            "raw_response": resp_text,
        }
        results.append(result)
        completed[key] = result

        # Progress logging
        if (i + 1) % 10 == 0 or i == len(test_windows) - 1:
            done = len(results)
            est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
            valid = [r for r in results if r["predicted_label"] != -1]
            if valid:
                cur_preds = [r["predicted_label"] for r in valid]
                cur_gt = [r["true_label"] for r in valid]
                cur_f1 = f1_score(cur_gt, cur_preds, average="macro", zero_division=0)
            else:
                cur_f1 = 0.0
            print(f"  [{done}/{len(test_windows)}] macro_f1={cur_f1:.4f} | "
                  f"tokens={total_input_tokens+total_output_tokens:,} | "
                  f"~${est_cost:.4f} | fails={parse_failures}")

        # Checkpoint every 100
        if (i + 1) % 100 == 0:
            _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)

    # Final save
    _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)

    # Final metrics
    print("\n" + "=" * 60)
    valid_results = [r for r in results if r["predicted_label"] != -1]
    if valid_results:
        preds = [r["predicted_label"] for r in valid_results]
        labels = [r["true_label"] for r in valid_results]
        metrics = compute_metrics(labels, preds)

        print(f"Model: {args.model} | Mode: {args.mode}")
        print(f"Windows evaluated: {len(results)} ({len(valid_results)} valid, {parse_failures} parse failures)")
        print(f"\n{'Metric':<20} {'Value':>10}")
        print("-" * 32)
        for k, v in metrics.items():
            print(f"{k:<20} {v:>10.4f}")

        print(f"\nGRU Probe reference: macro_f1 = 0.9055")
        print(f"LLM Judge:          macro_f1 = {metrics['macro_f1']:.4f}")
        print(f"Delta:              {metrics['macro_f1'] - 0.9055:+.4f}")
    else:
        print("No valid results to compute metrics.")

    # Cost summary
    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
    print(f"\n--- Cost Summary ---")
    print(f"Input tokens:  {total_input_tokens:>12,}")
    print(f"Output tokens: {total_output_tokens:>12,}")
    print(f"Total tokens:  {total_input_tokens + total_output_tokens:>12,}")
    print(f"Est. cost:     ${est_cost:>11.4f} (assuming $3/M input, $15/M output)")
    if len(results) > 0:
        per_window = est_cost / len(results)
        remaining = len(test_windows) - len(results)
        print(f"Per window:    ${per_window:.6f}")
        if remaining > 0:
            print(f"Est. remaining ({remaining} windows): ${per_window * remaining:.4f}")

    print(f"\nResults saved to {output_path}")


def _save_results(path, results, args, total_input_tokens, total_output_tokens, parse_failures):
    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
    output = {
        "model": args.model,
        "mode": args.mode,
        "n_windows": len(results),
        "parse_failures": parse_failures,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "est_cost_usd": round(est_cost, 4),
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
