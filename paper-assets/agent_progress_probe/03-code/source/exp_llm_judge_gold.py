#!/usr/bin/env python3
"""LLM Judge on Gold Set (505 windows, conf>=2).

Non-circular LLM baseline: claude-sonnet-4-20250514 zero-shot + 5-shot-CoT
on human-annotated gold labels. Few-shot examples drawn from TRAINING set only.

Model: claude-sonnet-4-20250514 (via OpenRouter-compatible proxy)
Gold set: artifacts/gold_set/gold_2plus_agreed_B.csv (505 windows)
Trajectories: data/swe_agent_trajectories_5000.jsonl
"""

import argparse
import csv
import json
import os
import random
import re
import sys
import time
import threading
from pathlib import Path
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

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

FEW_SHOT_COT_SYSTEM = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating.

Here are some labeled examples to calibrate your judgment:

{examples}

Indicators of PROGRESS:
- New files being explored or created that are relevant to the task
- Meaningful code edits that address the issue
- Successful test executions or error resolution
- Systematic debugging with new information gained each step

Indicators of STAGNATION:
- Repeating the same or very similar commands
- Editing the same lines back and forth
- Getting the same errors without trying different approaches
- Circular navigation without making changes

Analyze the trajectory step by step, then give your final judgment.
You MUST respond with a JSON object in this exact format:
{{"analysis": "your step-by-step analysis here", "judgment": "progress" or "stagnation", "confidence": 1-5}}"""

COT_USER = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.

{steps_text}

Analyze each step carefully:
1. What is the agent doing in each step?
2. Is there meaningful new information or progress between steps?
3. Are there repeated patterns or circular behavior?
4. Overall: is the agent making progress or stagnating?"""


def compute_metrics(y_true, y_pred):
    return {
        "macro_f1": round(f1_score(y_true, y_pred, average="macro", zero_division=0), 4),
        "accuracy": round(accuracy_score(y_true, y_pred), 4),
        "f1_stag": round(f1_score(y_true, y_pred, pos_label=0, zero_division=0), 4),
        "f1_prog": round(f1_score(y_true, y_pred, pos_label=1, zero_division=0), 4),
        "precision_stag": round(precision_score(y_true, y_pred, pos_label=0, zero_division=0), 4),
        "recall_stag": round(recall_score(y_true, y_pred, pos_label=0, zero_division=0), 4),
        "precision_prog": round(precision_score(y_true, y_pred, pos_label=1, zero_division=0), 4),
        "recall_prog": round(recall_score(y_true, y_pred, pos_label=1, zero_division=0), 4),
    }


def truncate_text(text, max_chars=500):
    if not text:
        return ""
    return text[:max_chars] + ("... [truncated]" if len(text) > max_chars else "")


def format_steps(steps, max_total_chars=6000):
    per_step = max(200, max_total_chars // max(len(steps), 1))
    parts = []
    for i, step in enumerate(steps):
        role = step.get("role", "unknown")
        text = truncate_text(step.get("text", "") or "", per_step)
        parts.append(f"[Step {i+1} | {role}]\n{text}")
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
    traj = traj_index.get(window["row_index"])
    if traj is None:
        return []
    trajectory = traj.get("trajectory", [])
    return [{"role": trajectory[si].get("role", "unknown"),
             "text": trajectory[si].get("text", "") or ""}
            for si in window["step_indices"] if si < len(trajectory)]


def select_few_shot_examples(train_windows, traj_index, n_per_class=3):
    """Select balanced few-shot examples from training set (not gold test)."""
    rng = random.Random(42)
    progress_pool = [w for w in train_windows if w["confidence"] >= 3 and w["majority_label"] == 1]
    stagnation_pool = [w for w in train_windows if w["confidence"] >= 3 and w["majority_label"] == 0]

    def sample_diverse(pool, n):
        by_traj = {}
        for w in pool:
            by_traj.setdefault(w["trajectory_id"], []).append(w)
        selected = []
        traj_ids = list(by_traj.keys())
        rng.shuffle(traj_ids)
        for tid in traj_ids:
            if len(selected) >= n:
                break
            selected.append(rng.choice(by_traj[tid]))
        return selected

    # 3 stagnation + 2 progress = 5 total (slightly favor stagnation as minority)
    stag_examples = sample_diverse(stagnation_pool, 3)
    prog_examples = sample_diverse(progress_pool, 2)
    selected = stag_examples + prog_examples

    examples_text = []
    for i, w in enumerate(selected):
        steps = extract_window_steps(w, traj_index)
        steps_text = format_steps(steps, max_total_chars=3000)
        label = "stagnation" if w["majority_label"] == 0 else "progress"
        examples_text.append(
            f"--- Example {i+1} (Label: {label}) ---\n{steps_text}\n"
            f"Analysis: This window shows {'repetitive patterns and lack of forward progress' if label == 'stagnation' else 'systematic progress with new actions and meaningful changes'}.\n"
            f"Judgment: {label}\n"
        )
    return "\n".join(examples_text)


def parse_judgment(text):
    text = text.strip()
    try:
        obj = json.loads(text)
        j = obj.get("judgment", "").lower().strip()
        return LABEL_MAP.get(j, -1)
    except json.JSONDecodeError:
        pass
    # Try extracting JSON from markdown
    m = re.search(r'\{[^{}]*"judgment"\s*:\s*"([^"]+)"[^{}]*\}', text, re.DOTALL)
    if m:
        j = m.group(1).lower().strip()
        return LABEL_MAP.get(j, -1)
    # Fallback: look for keywords
    lower = text.lower()
    if "stagnation" in lower or "stagnating" in lower:
        return 0
    if "progress" in lower or "progressing" in lower:
        return 1
    return -1


def call_api(client, model, system_msg, user_msg, max_tokens, retries=3):
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_msg},
                ],
                max_tokens=max_tokens,
                temperature=0.0,
            )
            content = resp.choices[0].message.content
            usage = {"input_tokens": resp.usage.prompt_tokens,
                     "output_tokens": resp.usage.completion_tokens}
            return content, usage
        except Exception as e:
            if attempt < retries - 1:
                wait = 2 ** attempt * 5
                print(f"  API error (attempt {attempt+1}): {e}, retrying in {wait}s", flush=True)
                time.sleep(wait)
            else:
                print(f"  API failed after {retries} attempts: {e}", flush=True)
                return None, None


def run_mode(client, model, mode, gold_windows, traj_index, few_shot_text,
             output_path, max_workers=15):
    """Run one evaluation mode (zero-shot or few-shot-cot)."""
    print(f"\n{'='*60}")
    print(f"Mode: {mode} | Windows: {len(gold_windows)} | Workers: {max_workers}")
    print(f"{'='*60}", flush=True)

    # Resume support
    existing = {}
    if output_path.exists():
        with open(output_path) as f:
            data = json.load(f)
            for r in data.get("results", []):
                existing[r["window_id"]] = r
        print(f"  Resuming: {len(existing)} already done", flush=True)

    results = list(existing.values())
    todo = [(wid, winfo, glabel) for wid, winfo, glabel in gold_windows
            if wid not in existing]

    if not todo:
        print("  All done (resumed).", flush=True)
    else:
        lock = threading.Lock()
        total_input = sum(r.get("input_tokens", 0) for r in results)
        total_output = sum(r.get("output_tokens", 0) for r in results)
        done_count = len(results)

        def process_one(item):
            nonlocal total_input, total_output, done_count
            wid, winfo, glabel = item
            steps = extract_window_steps(winfo, traj_index)
            if not steps:
                return {"window_id": wid, "gold_label": glabel, "pred": -1,
                        "raw_response": "", "error": "no_steps"}

            steps_text = format_steps(steps, max_total_chars=6000)
            n_steps = len(steps)

            if mode == "zero-shot":
                sys_msg = ZERO_SHOT_SYSTEM
                usr_msg = ZERO_SHOT_USER.format(n_steps=n_steps, steps_text=steps_text)
                max_tok = 200
            else:  # few-shot-cot
                sys_msg = FEW_SHOT_COT_SYSTEM.format(examples=few_shot_text)
                usr_msg = COT_USER.format(n_steps=n_steps, steps_text=steps_text)
                max_tok = 600

            content, usage = call_api(client, model, sys_msg, usr_msg, max_tok)
            pred = parse_judgment(content) if content else -1

            result = {
                "window_id": wid,
                "gold_label": glabel,
                "pred": pred,
                "raw_response": content or "",
            }
            if usage:
                result["input_tokens"] = usage["input_tokens"]
                result["output_tokens"] = usage["output_tokens"]

            with lock:
                total_input += usage.get("input_tokens", 0) if usage else 0
                total_output += usage.get("output_tokens", 0) if usage else 0
                done_count += 1
                if done_count % 50 == 0:
                    est_cost = (total_input * 3 + total_output * 15) / 1e6
                    print(f"  [{done_count}/{len(gold_windows)}] "
                          f"tokens={total_input}+{total_output} "
                          f"~${est_cost:.2f}", flush=True)

            return result

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {pool.submit(process_one, item): item for item in todo}
            for future in as_completed(futures):
                try:
                    r = future.result()
                    results.append(r)
                except Exception as e:
                    wid = futures[future][0]
                    results.append({"window_id": wid, "gold_label": futures[future][2],
                                    "pred": -1, "error": str(e)})

                # Save checkpoint every 100
                if len(results) % 100 == 0:
                    _save_results(output_path, model, mode, results)

    # Final save
    _save_results(output_path, model, mode, results)

    # Compute metrics
    valid = [r for r in results if r["pred"] != -1]
    y_true = [r["gold_label"] for r in valid]
    y_pred = [r["pred"] for r in valid]
    metrics = compute_metrics(y_true, y_pred) if valid else {}

    total_in = sum(r.get("input_tokens", 0) for r in results)
    total_out = sum(r.get("output_tokens", 0) for r in results)
    est_cost = (total_in * 3 + total_out * 15) / 1e6

    summary = {
        "mode": mode,
        "model": model,
        "n_gold": len(gold_windows),
        "n_valid": len(valid),
        "parse_failures": len(results) - len(valid),
        "metrics": metrics,
        "total_input_tokens": total_in,
        "total_output_tokens": total_out,
        "est_cost_usd": round(est_cost, 4),
    }

    print(f"\n  {mode} results:")
    print(f"    Valid: {len(valid)}/{len(results)}")
    if metrics:
        print(f"    macro_F1={metrics['macro_f1']:.4f}  "
              f"f1_stag={metrics['f1_stag']:.4f}  "
              f"f1_prog={metrics['f1_prog']:.4f}  "
              f"acc={metrics['accuracy']:.4f}")
    print(f"    Tokens: {total_in} in + {total_out} out  ~${est_cost:.2f}", flush=True)

    return summary


def _save_results(path, model, mode, results):
    total_in = sum(r.get("input_tokens", 0) for r in results)
    total_out = sum(r.get("output_tokens", 0) for r in results)
    with open(path, "w") as f:
        json.dump({
            "model": model, "mode": mode,
            "n_results": len(results),
            "total_input_tokens": total_in,
            "total_output_tokens": total_out,
            "results": results,
        }, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description="LLM Judge on Gold Set (505 windows)")
    parser.add_argument("--data_dir", default="/root/autodl-tmp/agent_progress_probe")
    parser.add_argument("--gold_csv", default="artifacts/gold_set/gold_2plus_agreed_B.csv")
    parser.add_argument("--api_key", default=None)
    parser.add_argument("--base_url", default="http://47.94.22.126/v1")
    parser.add_argument("--model", default="anthropic/claude-sonnet-4-20250514")
    parser.add_argument("--modes", nargs="+", default=["zero-shot", "few-shot-cot"],
                        choices=["zero-shot", "few-shot-cot"])
    parser.add_argument("--output_dir", default="artifacts/llm-judge-gold")
    parser.add_argument("--max_workers", type=int, default=15)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=120.0)

    # Load gold labels
    gold_csv_path = data_dir / args.gold_csv
    gold_labels = {}
    with open(gold_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            gold_labels[row["window_id"]] = int(row["gold_label"])
    print(f"Gold set: {len(gold_labels)} windows")
    gold_dist = Counter(gold_labels.values())
    print(f"  Distribution: {dict(gold_dist)} (stag_rate={gold_dist[0]/len(gold_labels):.1%})")

    # Load windows index
    print("Loading windows...")
    windows_path = data_dir / "data" / "windows_labeled.jsonl"
    win_index = {}
    all_windows = []
    with open(windows_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            w = json.loads(line)
            wid = f"{w['trajectory_id']}__w{w['window_idx']}"
            win_index[wid] = w
            all_windows.append(w)
    print(f"  Total windows: {len(win_index)}")

    # Match gold windows
    gold_windows = []
    for wid, glabel in gold_labels.items():
        if wid in win_index:
            gold_windows.append((wid, win_index[wid], glabel))
    print(f"  Matched gold: {len(gold_windows)}")

    # Load trajectories
    print("Loading trajectories...")
    traj_path = data_dir / "data" / "swe_agent_trajectories_5000.jsonl"
    traj_index = load_trajectories_index(traj_path)
    print(f"  Loaded {len(traj_index)} trajectories")

    # Select few-shot examples from training set (NOT gold windows)
    few_shot_text = ""
    if "few-shot-cot" in args.modes:
        print("Selecting 5 few-shot examples from training set...")
        split_info_path = data_dir / "checkpoints" / "split_info.json"
        with open(split_info_path) as f:
            split_info = json.load(f)
        keep_indices = split_info.get("keep_indices")
        usable = [w for w in all_windows if w.get("majority_label", -1) != -1]
        filtered = [usable[i] for i in keep_indices] if keep_indices else usable
        train_windows = [filtered[i] for i in split_info["train_indices"]]

        # Exclude any window that's in the gold set
        gold_ids = set(gold_labels.keys())
        train_windows = [w for w in train_windows
                         if f"{w['trajectory_id']}__w{w['window_idx']}" not in gold_ids]
        print(f"  Training pool (excl gold): {len(train_windows)}")

        few_shot_text = select_few_shot_examples(train_windows, traj_index, n_per_class=3)
        print(f"  Few-shot text: {len(few_shot_text)} chars")

    # Output directory
    output_dir = data_dir / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save prompts for audit
    prompts_log = {}
    for mode in args.modes:
        if mode == "zero-shot":
            prompts_log[mode] = {"system": ZERO_SHOT_SYSTEM,
                                 "user_template": ZERO_SHOT_USER, "max_tokens": 200}
        else:
            prompts_log[mode] = {"system": FEW_SHOT_COT_SYSTEM.format(examples="<examples>"),
                                 "user_template": COT_USER, "max_tokens": 600}
    with open(output_dir / "prompts.json", "w") as f:
        json.dump(prompts_log, f, indent=2, ensure_ascii=False)

    # Run evaluations
    all_summaries = []
    for mode in args.modes:
        output_path = output_dir / f"results_{mode.replace('-','_')}.json"
        summary = run_mode(client, args.model, mode, gold_windows, traj_index,
                           few_shot_text, output_path, args.max_workers)
        all_summaries.append(summary)

    # Final comparison table
    print("\n" + "=" * 70)
    print("LLM Judge on Gold Set (505 windows, conf>=2)")
    print("=" * 70)
    print(f"Model: {args.model}")
    print(f"\n{'Method':<20} {'macro_F1':>10} {'f1_stag':>10} {'f1_prog':>10} {'accuracy':>10}")
    print("-" * 62)
    for s in all_summaries:
        m = s["metrics"]
        print(f"LLM {s['mode']:<16} {m.get('macro_f1',0):>10.4f} {m.get('f1_stag',0):>10.4f} "
              f"{m.get('f1_prog',0):>10.4f} {m.get('accuracy',0):>10.4f}")
    print(f"{'Structural GB':<20} {'0.839':>10} {'—':>10} {'—':>10} {'—':>10}")
    print()

    best_f1 = max(s["metrics"].get("macro_f1", 0) for s in all_summaries)
    total_cost = sum(s["est_cost_usd"] for s in all_summaries)
    print(f"Best LLM macro_F1: {best_f1:.4f}")
    print(f"Structural GB gap: {0.839 - best_f1:+.4f}")
    print(f"Total cost: ${total_cost:.2f}")

    # Save summary
    with open(output_dir / "summary.json", "w") as f:
        json.dump({
            "exp_id": "llm-judge-gold-r5",
            "gold_set": str(gold_csv_path),
            "n_gold": len(gold_windows),
            "gold_distribution": {str(k): v for k, v in gold_dist.items()},
            "model": args.model,
            "modes": all_summaries,
            "best_llm_macro_f1": best_f1,
            "structural_gb_gold_macro_f1": 0.839,
            "total_cost_usd": round(total_cost, 4),
        }, f, indent=2)
    print(f"\nSummary saved to {output_dir / 'summary.json'}")


if __name__ == "__main__":
    main()
