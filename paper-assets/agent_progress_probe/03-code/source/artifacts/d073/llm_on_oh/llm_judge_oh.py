#!/usr/bin/env python3
"""LLM-as-Judge on OpenHands trajectories (D073-A4).

Samples 500 conf>=2 windows from OH, runs zero-shot / CoT / few-shot,
compares with structural cross-agent baseline (0.967).
Few-shot uses SWE examples, not OH.
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path
from collections import Counter

import openai
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

LABEL_MAP = {"stagnation": 0, "stagnating": 0, "stagnant": 0,
             "progress": 1, "progressing": 1, "advancing": 1}

ZERO_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.

Respond ONLY with a JSON object in this exact format:
{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""

COT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.

Think step by step:
1. What actions is the agent taking?
2. Are the actions diverse or repetitive?
3. Is the agent making measurable progress toward the goal?
4. Are there signs of loops, repeated errors, or lack of advancement?

After your analysis, respond with a JSON object in this exact format:
{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""

FEW_SHOT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction. Each step has a role (ai = agent action, user = environment observation) and text content.

Here are some examples:

{examples}

Respond ONLY with a JSON object in this exact format:
{{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}}"""

USER_TEMPLATE = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.

{steps_text}

Based on these steps, is the agent making meaningful progress toward solving the task, or is it stagnating?"""


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
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
    per_step = max(200, max_total_chars // max(len(steps), 1))
    for i, step in enumerate(steps):
        role = step.get("role", "unknown")
        text = step.get("text", "") or ""
        truncated = truncate_text(text, per_step)
        parts.append(f"[Step {i+1} | {role}]\n{truncated}")
    return "\n\n".join(parts)


def load_trajectories_index(traj_path):
    index = {}
    with open(traj_path) as f:
        for row_idx, line in enumerate(f):
            line = line.strip()
            if line:
                index[row_idx] = json.loads(line)
    return index


def extract_window_steps(window, traj_index):
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


def select_swe_few_shot_examples(swe_windows_path, swe_traj_path, swe_split_info_path):
    """Select few-shot examples from SWE training data (cross-domain)."""
    with open(swe_windows_path) as f:
        all_windows = [json.loads(line) for line in f if line.strip()]
    usable = [w for w in all_windows if w.get("majority_label", -1) != -1]

    with open(swe_split_info_path) as f:
        split_info = json.load(f)
    keep = split_info.get("keep_indices")
    if keep is not None:
        windows = [usable[i] for i in keep]
    else:
        windows = usable
    train_windows = [windows[i] for i in split_info["train_indices"]]

    swe_traj_index = load_trajectories_index(swe_traj_path)

    rng = random.Random(42)
    prog = [w for w in train_windows if w["confidence"] >= 3 and w["majority_label"] == 1]
    stag = [w for w in train_windows if w["confidence"] >= 3 and w["majority_label"] == 0]

    selected = []
    if prog:
        selected.extend(rng.sample(prog, min(2, len(prog))))
    if stag:
        selected.extend(rng.sample(stag, min(2, len(stag))))

    examples_text = []
    for i, w in enumerate(selected):
        steps = extract_window_steps(w, swe_traj_index)
        label_str = "progress" if w["majority_label"] == 1 else "stagnation"
        steps_formatted = format_steps(steps, max_total_chars=2000)
        examples_text.append(
            f"--- Example {i+1} (Answer: {label_str}) ---\n{steps_formatted}\n"
            f'{{"judgment": "{label_str}", "confidence": {w["confidence"]}, "reasoning": "This is a {label_str} example."}}'
        )
    return "\n\n".join(examples_text)


def parse_llm_response(text):
    try:
        obj = json.loads(text.strip())
        j = obj.get("judgment", "").lower().strip()
        if j in LABEL_MAP:
            return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
    except json.JSONDecodeError:
        pass

    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(1))
            j = obj.get("judgment", "").lower().strip()
            if j in LABEL_MAP:
                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
        except json.JSONDecodeError:
            pass

    m = re.search(r'\{[^{}]*"judgment"[^{}]*\}', text, re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(0))
            j = obj.get("judgment", "").lower().strip()
            if j in LABEL_MAP:
                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
        except json.JSONDecodeError:
            pass

    lower = text.lower()
    if "stagnat" in lower and "progress" not in lower:
        return 0, 0, "keyword_fallback"
    if "progress" in lower and "stagnat" not in lower:
        return 1, 0, "keyword_fallback"

    return -1, 0, "parse_failed"


def call_llm(client, model, system_msg, user_msg, max_retries=3):
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0.0,
                max_tokens=512,
            )
            choice = resp.choices[0]
            usage = resp.usage
            return (
                choice.message.content or "",
                usage.prompt_tokens if usage else 0,
                usage.completion_tokens if usage else 0,
            )
        except (openai.RateLimitError, openai.APITimeoutError) as e:
            wait = 2 ** (attempt + 1)
            print(f"  Retry {attempt+1}/{max_retries} after {type(e).__name__}, waiting {wait}s")
            time.sleep(wait)
        except openai.APIError as e:
            if attempt < max_retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"  Retry {attempt+1}/{max_retries} after APIError: {e}, waiting {wait}s")
                time.sleep(wait)
            else:
                raise
    return "", 0, 0


def sample_stratified(windows, n, seed=42):
    """Sample n windows stratified by majority_label."""
    rng = random.Random(seed)
    by_label = {}
    for w in windows:
        by_label.setdefault(w["majority_label"], []).append(w)

    total = sum(len(v) for v in by_label.values())
    sampled = []
    for label, ws in sorted(by_label.items()):
        k = max(1, round(n * len(ws) / total))
        sampled.extend(rng.sample(ws, min(k, len(ws))))
    rng.shuffle(sampled)
    return sampled[:n]


def run_mode(mode, test_windows, traj_index, client, model, output_path,
             few_shot_text="", rps=3.0, budget=50.0):
    """Run LLM judge for a single mode."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    completed = {}
    if output_path.exists():
        with open(output_path) as f:
            prev = json.load(f)
        for r in prev.get("results", []):
            key = f"{r['trajectory_id']}_{r['window_idx']}"
            completed[key] = r
        if len(completed) >= len(test_windows):
            print(f"  [{mode}] Already complete: {len(completed)} results")
            results = list(completed.values())
            valid = [r for r in results if r["predicted_label"] != -1]
            preds = [r["predicted_label"] for r in valid]
            labels = [r["true_label"] for r in valid]
            metrics = compute_metrics(labels, preds)
            return metrics, results
        print(f"  [{mode}] Resuming: {len(completed)}/{len(test_windows)} done")

    results = list(completed.values())
    total_in = sum(r.get("input_tokens", 0) for r in results)
    total_out = sum(r.get("output_tokens", 0) for r in results)
    parse_failures = sum(1 for r in results if r.get("predicted_label") == -1)
    min_interval = 1.0 / rps

    print(f"\n  [{mode}] Starting: {len(test_windows)} windows, model={model}")

    last_call = 0.0
    for i, w in enumerate(test_windows):
        key = f"{w['trajectory_id']}_{w['window_idx']}"
        if key in completed:
            continue

        est_cost = (total_in * 3 + total_out * 15) / 1_000_000
        if est_cost > budget:
            print(f"\n  *** BUDGET EXCEEDED: ~${est_cost:.2f} > ${budget}. Stopping. ***")
            break

        elapsed = time.time() - last_call
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        steps = extract_window_steps(w, traj_index)
        steps_text = format_steps(steps)
        user_msg = USER_TEMPLATE.format(n_steps=len(steps), steps_text=steps_text)

        if mode == "zero-shot":
            system_msg = ZERO_SHOT_SYSTEM
        elif mode == "cot":
            system_msg = COT_SYSTEM
        elif mode == "few-shot":
            system_msg = FEW_SHOT_SYSTEM.format(examples=few_shot_text)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        last_call = time.time()
        resp_text, in_tok, out_tok = call_llm(client, model, system_msg, user_msg)
        total_in += in_tok
        total_out += out_tok

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

        if (i + 1) % 20 == 0 or i == len(test_windows) - 1:
            done = len(results)
            est_cost = (total_in * 3 + total_out * 15) / 1_000_000
            valid = [r for r in results if r["predicted_label"] != -1]
            if valid:
                cur_f1 = f1_score([r["true_label"] for r in valid],
                                  [r["predicted_label"] for r in valid],
                                  average="macro", zero_division=0)
            else:
                cur_f1 = 0.0
            print(f"    [{done}/{len(test_windows)}] macro_f1={cur_f1:.4f} | "
                  f"tokens={total_in+total_out:,} | ~${est_cost:.4f} | fails={parse_failures}")

        if (i + 1) % 50 == 0:
            _save(output_path, mode, model, results, total_in, total_out, parse_failures)

    _save(output_path, mode, model, results, total_in, total_out, parse_failures)

    valid = [r for r in results if r["predicted_label"] != -1]
    if valid:
        preds = [r["predicted_label"] for r in valid]
        labels = [r["true_label"] for r in valid]
        metrics = compute_metrics(labels, preds)
    else:
        metrics = {"macro_f1": 0, "accuracy": 0, "f1_stagnation": 0, "f1_progress": 0}

    est_cost = (total_in * 3 + total_out * 15) / 1_000_000
    print(f"  [{mode}] Done: macro_f1={metrics['macro_f1']:.4f}, "
          f"f1_stag={metrics['f1_stagnation']:.4f}, f1_prog={metrics['f1_progress']:.4f}, "
          f"cost=~${est_cost:.4f}, fails={parse_failures}")

    return metrics, results


def _save(path, mode, model, results, total_in, total_out, parse_failures):
    est_cost = (total_in * 3 + total_out * 15) / 1_000_000
    output = {
        "model": model,
        "mode": mode,
        "dataset": "openhands",
        "n_windows": len(results),
        "parse_failures": parse_failures,
        "total_input_tokens": total_in,
        "total_output_tokens": total_out,
        "est_cost_usd": round(est_cost, 4),
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--oh_windows", default="/root/autodl-tmp/openhands_data/windows_labeled.jsonl")
    parser.add_argument("--oh_trajectories", default="/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl")
    parser.add_argument("--swe_data_dir", default="/root/autodl-tmp/agent_progress_probe/data")
    parser.add_argument("--swe_trajectories", default="/root/autodl-tmp/agent_progress_probe/data/swe_agent_trajectories_5000.jsonl")
    parser.add_argument("--swe_split_info", default="/root/autodl-tmp/agent_progress_probe/checkpoints/split_info.json")
    parser.add_argument("--api_key", default=None)
    parser.add_argument("--base_url", default="http://47.94.22.126/v1")
    parser.add_argument("--model", default="anthropic/claude-sonnet-4.6")
    parser.add_argument("--n_sample", type=int, default=500)
    parser.add_argument("--output_dir", default="/root/autodl-tmp/agent_progress_probe/results/d073_llm_on_oh")
    parser.add_argument("--rps", type=float, default=3.0)
    parser.add_argument("--budget_per_mode", type=float, default=30.0)
    parser.add_argument("--modes", default="zero-shot,cot,few-shot")
    args = parser.parse_args()

    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=60.0)

    # Load OH windows (conf>=2 only)
    print("Loading OH windows...")
    all_windows = []
    with open(args.oh_windows) as f:
        for line in f:
            line = line.strip()
            if line:
                w = json.loads(line)
                if w.get("confidence", 0) >= 2 and w.get("majority_label", -1) != -1:
                    all_windows.append(w)
    print(f"  Conf>=2: {len(all_windows)}")
    label_dist = Counter(w["majority_label"] for w in all_windows)
    print(f"  Label dist: {dict(label_dist)}")

    # Stratified sample
    test_windows = sample_stratified(all_windows, args.n_sample, seed=42)
    sample_dist = Counter(w["majority_label"] for w in test_windows)
    print(f"  Sampled {len(test_windows)}: {dict(sample_dist)}")

    # Load OH trajectories
    print("Loading OH trajectories...")
    oh_traj_index = load_trajectories_index(args.oh_trajectories)
    print(f"  Loaded {len(oh_traj_index)} trajectories")

    # Prepare few-shot examples from SWE
    swe_windows_path = Path(args.swe_data_dir) / "windows_labeled.jsonl"
    few_shot_text = ""
    modes = [m.strip() for m in args.modes.split(",")]
    if "few-shot" in modes:
        print("Loading SWE few-shot examples...")
        few_shot_text = select_swe_few_shot_examples(
            str(swe_windows_path), args.swe_trajectories, args.swe_split_info)
        print(f"  Few-shot examples: {len(few_shot_text)} chars")

    # Run each mode
    all_metrics = {}
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for mode in modes:
        output_path = output_dir / f"llm_judge_oh_{mode.replace('-','_')}.json"
        metrics, _ = run_mode(
            mode, test_windows, oh_traj_index, client, args.model,
            output_path, few_shot_text, args.rps, args.budget_per_mode)
        all_metrics[mode] = metrics

    # Summary
    print("\n" + "=" * 70)
    print("LLM Judge on OpenHands — Summary")
    print("=" * 70)
    print(f"{'Mode':<15} {'macro_F1':>10} {'f1_stag':>10} {'f1_prog':>10} {'accuracy':>10}")
    print("-" * 55)
    for mode, m in all_metrics.items():
        print(f"{mode:<15} {m['macro_f1']:>10.4f} {m['f1_stagnation']:>10.4f} "
              f"{m['f1_progress']:>10.4f} {m['accuracy']:>10.4f}")
    print("-" * 55)
    print(f"{'Structural GB':<15} {'0.9670':>10} {'—':>10} {'—':>10} {'—':>10}")
    print(f"\nStructural advantage: {0.967 - max(m['macro_f1'] for m in all_metrics.values()):+.4f}")

    # Save summary
    summary = {
        "dataset": "openhands",
        "n_sample": len(test_windows),
        "sample_dist": dict(sample_dist),
        "model": args.model,
        "structural_cross_agent_f1": 0.967,
        "modes": all_metrics,
    }
    summary_path = output_dir / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to {summary_path}")


if __name__ == "__main__":
    main()
