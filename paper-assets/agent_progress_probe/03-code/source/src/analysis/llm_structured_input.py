#!/usr/bin/env python3
"""LLM + structural features experiment.

Tests whether giving an LLM the 30 structural features as formatted JSON
alongside the raw window text improves classification vs text-only zero-shot.
"""

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path
from threading import Lock

import numpy as np
import openai
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# ── Feature extraction (from cross_agent_structural_baseline.py) ──────────

EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}

FEATURE_NAMES = [
    "num_steps", "num_actions", "num_observations", "action_ratio",
    "mean_text_len", "std_text_len", "max_text_len", "min_text_len",
    "mean_action_len", "mean_obs_len", "text_len_trend",
    "num_commands", "mean_cmd_len", "max_cmd_len",
    "unique_cmd_ratio", "max_repeat_ratio",
    "num_edit_cmds", "num_search_cmds", "num_nav_cmds", "num_submit_cmds",
    "edit_ratio", "search_ratio",
    "avg_adjacent_cmd_sim", "max_adjacent_cmd_sim", "max_consecutive_similar",
    "num_errors", "num_test_outputs", "num_file_displays", "num_nonzero_exits",
    "is_short_trajectory",
]


def cmd_similarity(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def extract_command(text):
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def extract_features(steps, is_short):
    n = len(steps)
    if n == 0:
        return np.zeros(30)

    texts = [s["text"] for s in steps]
    text_lens = [len(t) for t in texts]

    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]

    n_actions = len(actions)
    n_obs = len(observations)

    mean_tlen = np.mean(text_lens)
    std_tlen = np.std(text_lens) if n > 1 else 0.0
    max_tlen = max(text_lens)
    min_tlen = min(text_lens)

    action_lens = [len(t) for _, t in actions] if actions else [0]
    obs_lens = [len(t) for _, t in observations] if observations else [0]
    mean_action_len = np.mean(action_lens)
    mean_obs_len = np.mean(obs_lens)

    if n > 1:
        x = np.arange(n, dtype=float)
        y = np.array(text_lens, dtype=float)
        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum()**2 + 1e-9)
    else:
        slope = 0.0

    commands = []
    for s, t in actions:
        cmd = extract_command(t)
        if cmd:
            commands.append(cmd)

    n_cmds = len(commands)
    cmd_lens = [len(c) for c in commands] if commands else [0]
    mean_cmd_len = np.mean(cmd_lens)
    max_cmd_len = max(cmd_lens) if cmd_lens else 0

    if n_cmds > 0:
        unique_cmds = len(set(commands))
        unique_cmd_ratio = unique_cmds / n_cmds
        cmd_counter = Counter(commands)
        max_repeat = cmd_counter.most_common(1)[0][1]
        repeat_ratio = max_repeat / n_cmds
    else:
        unique_cmd_ratio = 1.0
        repeat_ratio = 0.0

    n_edit = n_search = n_nav = n_submit = 0
    for cmd in commands:
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in EDIT_CMDS:
            n_edit += 1
        elif first_word in SEARCH_CMDS:
            n_search += 1
        elif first_word in NAV_CMDS:
            n_nav += 1
        elif first_word == "submit":
            n_submit += 1

    edit_ratio = n_edit / max(n_cmds, 1)
    search_ratio = n_search / max(n_cmds, 1)

    if n_cmds >= 2:
        sims = [cmd_similarity(commands[i], commands[i+1]) for i in range(n_cmds - 1)]
        avg_adj_sim = np.mean(sims)
        max_adj_sim = max(sims)
        max_run = 1
        cur_run = 1
        for s in sims:
            if s >= 0.9:
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 1
    else:
        avg_adj_sim = 0.0
        max_adj_sim = 0.0
        max_run = 0

    n_errors = sum(1 for t in texts if "Traceback" in t or "Error" in t)
    n_test_output = sum(1 for t in texts if ("PASSED" in t or "FAILED" in t) and "test" in t.lower())
    n_file_display = sum(1 for t in texts if "[File:" in t)
    n_nonzero_exit = sum(1 for _, t in observations if re.search(r"exit code [1-9]|returned non-zero|command not found", t))

    return np.array([
        n, n_actions, n_obs, n_actions / max(n, 1),
        mean_tlen, std_tlen, max_tlen, min_tlen,
        mean_action_len, mean_obs_len, slope,
        n_cmds, mean_cmd_len, max_cmd_len,
        unique_cmd_ratio, repeat_ratio,
        n_edit, n_search, n_nav, n_submit,
        edit_ratio, search_ratio,
        avg_adj_sim, max_adj_sim, max_run,
        n_errors, n_test_output, n_file_display, n_nonzero_exit,
        float(is_short),
    ], dtype=np.float32)


# ── Data loading (from baseline_llm_judge.py) ────────────────────────────

LABEL_MAP = {"stagnation": 0, "stagnating": 0, "stagnant": 0,
             "progress": 1, "progressing": 1, "advancing": 1}


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
            steps.append({
                "role": s.get("role", "unknown"),
                "text": s.get("text") or s.get("system_prompt") or "",
            })
    return steps


def features_to_json(feat_vec):
    d = {}
    for name, val in zip(FEATURE_NAMES, feat_vec):
        v = float(val)
        if v == int(v) and abs(v) < 1e9:
            d[name] = int(v)
        else:
            d[name] = round(v, 4)
    return json.dumps(d, indent=2)


# ── Prompts ───────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an expert at analyzing software engineering agent trajectories. Your task is to determine whether an agent is making meaningful progress toward solving a coding task, or whether it is stagnating (repeating actions, going in circles, or failing to advance).

You will be shown a window of consecutive steps from the agent's interaction, along with 30 pre-computed structural features that quantify patterns in the window (command repetition, diversity, error rates, etc.).

Use BOTH the raw text AND the structural features to make your judgment. The features provide objective measurements that may reveal patterns not immediately obvious from reading the text.

Respond ONLY with a JSON object in this exact format:
{"judgment": "progress" or "stagnation", "confidence": 1-5, "reasoning": "brief explanation"}"""

USER_TEMPLATE = """Below is a window of {n_steps} consecutive steps from a software engineering agent's trajectory.

{steps_text}

## Structural Features (computed from the window above)
```json
{features_json}
```

Based on the window text AND the structural features above, classify this window as "progress" or "stagnation"."""


# ── LLM calling ──────────────────────────────────────────────────────────

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
                max_tokens=300,
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


def parse_llm_response(text):
    text = text.strip()
    try:
        obj = json.loads(text)
        j = obj.get("judgment", "").lower().strip()
        if j in LABEL_MAP:
            return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
    except json.JSONDecodeError:
        pass
    match = re.search(r'\{[^{}]*"judgment"\s*:\s*"([^"]+)"[^{}]*\}', text, re.DOTALL)
    if match:
        try:
            obj = json.loads(match.group(0))
            j = obj.get("judgment", "").lower().strip()
            if j in LABEL_MAP:
                return LABEL_MAP[j], obj.get("confidence", 0), obj.get("reasoning", "")
        except json.JSONDecodeError:
            pass
    for keyword in ["stagnation", "stagnating", "stagnant"]:
        if keyword in text.lower():
            return 0, 0, text
    for keyword in ["progress", "progressing", "advancing"]:
        if keyword in text.lower():
            return 1, 0, text
    return -1, 0, text


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="LLM + structural features experiment")
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--split_info", required=True)
    parser.add_argument("--trajectories", required=True)
    parser.add_argument("--api_key", default=None)
    parser.add_argument("--base_url", default="http://47.94.22.126/v1")
    parser.add_argument("--model", default="anthropic/claude-sonnet-4.6")
    parser.add_argument("--output", default="artifacts/llm-structured-input/results.json")
    parser.add_argument("--prompt_output", default="artifacts/llm-structured-input/prompt_template.txt")
    parser.add_argument("--max_windows", type=int, default=0)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry_run", type=int, default=0, help="Run on N windows only for testing")
    parser.add_argument("--budget", type=float, default=100.0)
    args = parser.parse_args()

    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY", "")
    if not api_key:
        print("ERROR: Provide --api_key or set OPENROUTER_API_KEY", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(base_url=args.base_url, api_key=[REDACTED], timeout=120.0)

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
    test_idx = split_info["test_indices"]
    test_windows = [windows[i] for i in test_idx]
    print(f"  Test: {len(test_windows)}")

    if args.dry_run > 0:
        test_windows = test_windows[:args.dry_run]
        print(f"  DRY RUN: {len(test_windows)} windows")
    elif args.max_windows > 0:
        test_windows = test_windows[:args.max_windows]
        print(f"  Limiting to {len(test_windows)} windows")

    gt = [w["majority_label"] for w in test_windows]
    print(f"  Test label dist: {dict(Counter(gt))}")

    print("Loading trajectories index...")
    traj_index = load_trajectories_index(args.trajectories)
    print(f"  Loaded {len(traj_index)} trajectories")

    # Save prompt template
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path = Path(args.prompt_output)
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(prompt_path, "w") as f:
        f.write("=== SYSTEM PROMPT ===\n")
        f.write(SYSTEM_PROMPT)
        f.write("\n\n=== USER TEMPLATE ===\n")
        f.write(USER_TEMPLATE)
    print(f"  Prompt template saved to {prompt_path}")

    # Resume support
    completed = {}
    if args.resume and output_path.exists():
        with open(output_path) as f:
            prev = json.load(f)
        for r in prev.get("results", []):
            key = f"{r['trajectory_id']}_{r['window_idx']}"
            completed[key] = r
        print(f"  Resuming: {len(completed)} windows already done")

    # Prepare work items
    work_items = []
    for w in test_windows:
        key = f"{w['trajectory_id']}_{w['window_idx']}"
        if key in completed:
            continue
        steps = extract_window_steps(w, traj_index)
        if not steps:
            continue
        steps_text = format_steps(steps)
        feat_vec = extract_features(steps, w.get("short_trajectory", False))
        feat_json = features_to_json(feat_vec)
        user_msg = USER_TEMPLATE.format(
            n_steps=len(steps),
            steps_text=steps_text,
            features_json=feat_json,
        )
        work_items.append((w, key, user_msg))

    print(f"\n{len(work_items)} windows to evaluate (skipped {len(completed)} already done)")

    # Thread-safe state
    lock = Lock()
    results = list(completed.values())
    total_input_tokens = sum(r.get("input_tokens", 0) for r in results)
    total_output_tokens = sum(r.get("output_tokens", 0) for r in results)
    parse_failures = sum(1 for r in results if r.get("predicted_label") == -1)
    done_count = len(results)
    total_to_do = len(test_windows)

    def process_one(item):
        nonlocal total_input_tokens, total_output_tokens, parse_failures, done_count
        w, key, user_msg = item
        resp_text, in_tok, out_tok = call_llm(client, args.model, SYSTEM_PROMPT, user_msg)
        pred_label, pred_conf, reasoning = parse_llm_response(resp_text)

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

        with lock:
            results.append(result)
            total_input_tokens += in_tok
            total_output_tokens += out_tok
            if pred_label == -1:
                parse_failures += 1
            done_count += 1

            if done_count % 50 == 0 or done_count == total_to_do:
                est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
                valid = [r for r in results if r["predicted_label"] != -1]
                if valid:
                    cur_f1 = f1_score(
                        [r["true_label"] for r in valid],
                        [r["predicted_label"] for r in valid],
                        average="macro", zero_division=0,
                    )
                else:
                    cur_f1 = 0.0
                print(f"  [{done_count}/{total_to_do}] macro_f1={cur_f1:.4f} | "
                      f"tokens={total_input_tokens+total_output_tokens:,} | "
                      f"~${est_cost:.4f} | fails={parse_failures}", flush=True)

            if done_count % 200 == 0:
                _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)

        return result

    # Budget check wrapper
    def budget_ok():
        est = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
        return est < args.budget

    print(f"Starting LLM+features evaluation: model={args.model}, workers={args.workers}")
    print("-" * 60)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for item in work_items:
            if not budget_ok():
                print(f"\n*** BUDGET EXCEEDED. Stopping submission. ***")
                break
            fut = executor.submit(process_one, item)
            futures[fut] = item

        for fut in as_completed(futures):
            try:
                fut.result()
            except Exception as e:
                w, key, _ = futures[fut]
                print(f"  ERROR on {key}: {e}", flush=True)

    # Final save
    _save_results(output_path, results, args, total_input_tokens, total_output_tokens, parse_failures)

    # Final metrics
    print("\n" + "=" * 60)
    valid_results = [r for r in results if r["predicted_label"] != -1]
    if valid_results:
        preds = [r["predicted_label"] for r in valid_results]
        labels = [r["true_label"] for r in valid_results]
        metrics = compute_metrics(labels, preds)

        print(f"Model: {args.model} | Mode: zero-shot + structural features")
        print(f"Windows: {len(results)} ({len(valid_results)} valid, {parse_failures} parse failures)")
        print(f"\n{'Metric':<20} {'Value':>10}")
        print("-" * 32)
        for k, v in metrics.items():
            print(f"{k:<20} {v:>10.4f}")

        orig_f1 = 0.6625
        print(f"\n--- Comparison ---")
        print(f"Original zero-shot (text only):    macro_f1 = {orig_f1:.4f}")
        print(f"Zero-shot + structural features:   macro_f1 = {metrics['macro_f1']:.4f}")
        print(f"Delta:                             {metrics['macro_f1'] - orig_f1:+.4f} pp")
        print(f"\nGB reference:                      macro_f1 = 0.9920")
    else:
        print("No valid results.")

    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
    print(f"\n--- Cost ---")
    print(f"Input tokens:  {total_input_tokens:>12,}")
    print(f"Output tokens: {total_output_tokens:>12,}")
    print(f"Est. cost:     ${est_cost:>11.4f}")
    print(f"\nResults saved to {output_path}")


def _save_results(path, results, args, total_input_tokens, total_output_tokens, parse_failures):
    valid = [r for r in results if r["predicted_label"] != -1]
    if valid:
        metrics = compute_metrics(
            [r["true_label"] for r in valid],
            [r["predicted_label"] for r in valid],
        )
    else:
        metrics = {}
    est_cost = (total_input_tokens * 3 + total_output_tokens * 15) / 1_000_000
    output = {
        "experiment": "llm-structured-input",
        "model": args.model,
        "mode": "zero-shot + structural features",
        "n_windows": len(results),
        "n_valid": len(valid),
        "parse_failures": parse_failures,
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "est_cost_usd": round(est_cost, 4),
        "metrics": {k: round(v, 4) for k, v in metrics.items()} if metrics else {},
        "comparison": {
            "original_zero_shot_macro_f1": 0.6625,
            "delta_pp": round(metrics.get("macro_f1", 0) - 0.6625, 4) if metrics else None,
        },
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
