#!/usr/bin/env python3
"""Direction B: DeepConf confidence filtering + SICA.
Scores each trace's final answer confidence via logprob, then filters
low-confidence traces before running SC and SICA.

Usage:
  1. Start vLLM on port 8020
  2. python analysis_deepconf_filter.py [--score-only] [--skip-scoring]
"""
import argparse
import asyncio
import json
import logging
import math
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/root/symb_invariant_consensus")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

VLLM_BASE_URL = "http://localhost:8020/v1"
INTERMEDIATES_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates")
CONSTRAINT_CACHE_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/direction_b_deepconf")
MODEL_PATH = "/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3"
LOGPROB_CACHE = OUTPUT_DIR / "logprob_scores.json"

SOLVE_PROMPT = """Solve the following math problem step by step. Show all your reasoning.
At the end, put your final answer in \\boxed{}.

Problem: {problem}"""

FILTER_RATIOS = [1.0, 0.75, 0.50]
CONCURRENCY = 16

_LOGIC_CANONICAL = {
    "true": "True", "yes": "True", "1": "True",
    "false": "False", "no": "False", "0": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}


def normalize_logic_answer(ans: str) -> str:
    s = ans.strip()
    if s.startswith("\\text{"):
        s = s[len("\\text{"):]
        if s.endswith("}"):
            s = s[:-1]
        s = s.strip()
    return _LOGIC_CANONICAL.get(s.lower(), s)


def group_logic_answers(answers: list[str]) -> dict[str, list[int]]:
    groups: dict[str, list[int]] = {}
    for i, ans in enumerate(answers):
        key = normalize_logic_answer(ans)
        groups.setdefault(key, []).append(i)
    return groups


# ── Phase 1: Load data ──

def load_all_data() -> dict:
    problems = {}
    for f in sorted(INTERMEDIATES_DIR.glob("*.json")):
        data = json.loads(f.read_text())
        pid = data["problem"]["id"]

        cache_file = CONSTRAINT_CACHE_DIR / f.name
        constraints_per_trace = {}
        if cache_file.exists():
            cache = json.loads(cache_file.read_text())
            for entry in cache.get("per_trace", []):
                constraints_per_trace[entry["trace_idx"]] = entry["constraints"]

        traces = data["sica_result"]["traces"]
        for t in traces:
            if t.get("answer"):
                t["answer"] = normalize_logic_answer(t["answer"])

        problems[pid] = {
            "problem": data["problem"],
            "traces": traces,
            "constraints_per_trace": constraints_per_trace,
            "ground_truth": normalize_logic_answer(data["problem"]["answer"]),
        }

    logger.info("Loaded %d problems", len(problems))
    return problems


# ── Phase 2: Logprob scoring ──

def build_scoring_prompt(problem_text: str, trace_text: str, tokenizer) -> str:
    user_msg = SOLVE_PROMPT.format(problem=problem_text)

    boxed_pos = trace_text.rfind("\\boxed{")
    if boxed_pos >= 0:
        prefix = trace_text[: boxed_pos + len("\\boxed{")]
    else:
        for keyword in ["Final answer:", "The answer is", "answer:"]:
            kpos = trace_text.lower().rfind(keyword.lower())
            if kpos >= 0:
                prefix = trace_text[: kpos + len(keyword)] + " \\boxed{"
                break
        else:
            prefix = trace_text + "\n\nFinal answer: \\boxed{"

    messages = [{"role": "user", "content": user_msg}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    prompt = prompt.rstrip() + " " + prefix
    return prompt


async def score_single(client, model, prompt, semaphore):
    async with semaphore:
        try:
            resp = await client.completions.create(
                model=model,
                prompt=prompt,
                max_tokens=5,
                logprobs=5,
                temperature=0,
            )
            choice = resp.choices[0]
            if choice.logprobs and choice.logprobs.token_logprobs:
                return {
                    "logprob": choice.logprobs.token_logprobs[0],
                    "token": choice.logprobs.tokens[0],
                    "top_logprobs": dict(choice.logprobs.top_logprobs[0])
                    if choice.logprobs.top_logprobs
                    else {},
                }
            return {"logprob": -100.0, "token": "", "top_logprobs": {}}
        except Exception as e:
            logger.error("Scoring error: %s", e)
            return {"logprob": -100.0, "token": "", "top_logprobs": {}}


async def score_all_traces(problems: dict) -> dict:
    import openai
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    logger.info("Tokenizer loaded")

    client = openai.AsyncOpenAI(base_url=VLLM_BASE_URL, api_key="[REDACTED]")
    sync_client = openai.OpenAI(base_url=VLLM_BASE_URL, api_key="[REDACTED]")
    models = sync_client.models.list()
    model = models.data[0].id
    logger.info("Using model: %s", model)

    semaphore = asyncio.Semaphore(CONCURRENCY)
    tasks = []
    task_map = []

    for pid, pdata in problems.items():
        problem_text = pdata["problem"]["problem"]
        for trace in pdata["traces"]:
            tidx = trace["trace_idx"]
            answer = trace.get("answer", "")

            if not answer:
                task_map.append((pid, tidx))
                tasks.append(None)
                continue

            prompt = build_scoring_prompt(problem_text, trace["trace"], tokenizer)
            task_map.append((pid, tidx))
            tasks.append(score_single(client, model, prompt, semaphore))

    real_tasks = [(i, t) for i, t in enumerate(tasks) if t is not None]
    logger.info(
        "Scoring %d traces (%d with answers)...", len(tasks), len(real_tasks)
    )

    t0 = time.time()
    real_results = await asyncio.gather(*[t for _, t in real_tasks])

    results = [{"logprob": -100.0, "token": "", "top_logprobs": {}}] * len(tasks)
    for (orig_idx, _), result in zip(real_tasks, real_results):
        results[orig_idx] = result

    elapsed = time.time() - t0
    logger.info("Scoring done in %.1fs", elapsed)

    logprob_data = {}
    for (pid, tidx), result in zip(task_map, results):
        logprob_data.setdefault(pid, {})[str(tidx)] = result
        for trace in problems[pid]["traces"]:
            if trace["trace_idx"] == tidx:
                trace["logprob"] = result["logprob"]
                trace["logprob_token"] = result["token"]
                break

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOGPROB_CACHE.write_text(json.dumps(logprob_data, indent=2))
    logger.info("Logprob cache saved to %s", LOGPROB_CACHE)

    return problems


def load_logprob_cache(problems: dict) -> dict:
    if not LOGPROB_CACHE.exists():
        raise FileNotFoundError(f"Logprob cache not found: {LOGPROB_CACHE}")

    cache = json.loads(LOGPROB_CACHE.read_text())
    for pid, pdata in problems.items():
        pid_cache = cache.get(pid, {})
        for trace in pdata["traces"]:
            tidx = trace["trace_idx"]
            entry = pid_cache.get(str(tidx), {})
            trace["logprob"] = entry.get("logprob", -100.0)
            trace["logprob_token"] = entry.get("token", "")

    logger.info("Loaded logprob cache from %s", LOGPROB_CACHE)
    return problems


# ── Phase 3: Filtered SC ──

def run_filtered_sc(traces: list[dict], top_k: int) -> dict:
    scored = sorted(
        [t for t in traces if t.get("answer")],
        key=lambda t: t.get("logprob", -100.0),
        reverse=True,
    )
    selected = scored[:top_k]

    valid_answers = [t["answer"] for t in selected if t["answer"]]
    if not valid_answers:
        return {"answer": "", "vote_count": 0, "k_effective": 0, "vote_distribution": {}}

    groups = group_logic_answers(valid_answers)
    best = max(sorted(groups.keys()), key=lambda k: len(groups[k]))
    vote_dist = {k: len(v) for k, v in groups.items()}

    return {
        "answer": best,
        "vote_count": len(groups[best]),
        "k_effective": len(selected),
        "vote_distribution": vote_dist,
    }


# ── Phase 4: Filtered SICA ──

def run_filtered_sica(
    traces: list[dict],
    constraints_per_trace: dict,
    top_k: int,
) -> dict:
    from sica.z3_maxsat import ConstraintDeduplicator, MaxSATSolver
    from sica.scorer import InvariantScorer

    scored = sorted(
        [t for t in traces if t.get("answer")],
        key=lambda t: t.get("logprob", -100.0),
        reverse=True,
    )
    selected = scored[:top_k]

    if not selected:
        return {"answer": "", "scores": {}, "k_effective": 0}

    reindexed_traces = []
    all_constraints = []
    for new_idx, trace in enumerate(selected):
        orig_idx = trace["trace_idx"]
        reindexed_traces.append({
            "trace": trace.get("trace", ""),
            "answer": trace["answer"],
            "trace_idx": new_idx,
            "logprob": trace.get("logprob", -100.0),
        })
        cs = constraints_per_trace.get(orig_idx, [])
        all_constraints.append(cs)

    deduplicator = ConstraintDeduplicator()
    solver = MaxSATSolver()
    scorer = InvariantScorer()

    try:
        unique = deduplicator.deduplicate(all_constraints)
        maxsat_result = solver.solve(unique, timeout_ms=10000)
    except Exception as e:
        logger.warning("SICA solve error: %s", e)
        answer_counts = Counter(t["answer"] for t in reindexed_traces if t["answer"])
        best = answer_counts.most_common(1)[0][0] if answer_counts else ""
        return {"answer": best, "scores": {}, "k_effective": len(selected)}

    candidates = sorted(set(t["answer"] for t in reindexed_traces if t["answer"]))
    answer_counts = Counter(t["answer"] for t in reindexed_traces if t["answer"])
    scores = scorer.score(maxsat_result, reindexed_traces, candidates)
    answer = scorer.select_answer(scores, answer_counts)

    return {
        "answer": answer,
        "scores": {k: round(v, 2) for k, v in scores.items()},
        "answer_counts": dict(answer_counts),
        "k_effective": len(selected),
        "n_unique_constraints": len(unique),
        "n_satisfied": len(maxsat_result.satisfied),
        "n_excluded": len(maxsat_result.excluded),
    }


# ── Phase 5: Run all comparisons ──

def run_comparisons(problems: dict) -> dict:
    results_table = {}

    for ratio in FILTER_RATIOS:
        label = f"top_{int(ratio * 100)}pct"
        sc_correct = 0
        sica_correct = 0
        total = len(problems)
        k_effectives = []
        per_problem = []

        for pid, pdata in problems.items():
            gt = pdata["ground_truth"]
            n_with_answer = sum(1 for t in pdata["traces"] if t.get("answer"))
            top_k = max(1, int(math.ceil(n_with_answer * ratio)))

            sc_res = run_filtered_sc(pdata["traces"], top_k)
            sica_res = run_filtered_sica(
                pdata["traces"], pdata["constraints_per_trace"], top_k
            )

            sc_ok = sc_res["answer"] == gt
            sica_ok = sica_res["answer"] == gt
            sc_correct += int(sc_ok)
            sica_correct += int(sica_ok)
            k_effectives.append(sc_res["k_effective"])

            per_problem.append({
                "pid": pid,
                "gt": gt,
                "sc_answer": sc_res["answer"],
                "sc_correct": sc_ok,
                "sica_answer": sica_res["answer"],
                "sica_correct": sica_ok,
                "k_effective": sc_res["k_effective"],
                "sc_votes": sc_res.get("vote_distribution", {}),
                "sica_scores": sica_res.get("scores", {}),
            })

        avg_k = sum(k_effectives) / len(k_effectives) if k_effectives else 0
        results_table[label] = {
            "ratio": ratio,
            "sc_accuracy": round(sc_correct / total, 4),
            "sica_accuracy": round(sica_correct / total, 4),
            "sc_correct": sc_correct,
            "sica_correct": sica_correct,
            "total": total,
            "avg_k_effective": round(avg_k, 1),
            "per_problem": per_problem,
        }

        logger.info(
            "[%s] SC=%.1f%% (%d/%d) SICA=%.1f%% (%d/%d) avg_K=%.1f",
            label,
            sc_correct / total * 100, sc_correct, total,
            sica_correct / total * 100, sica_correct, total,
            avg_k,
        )

    return results_table


def print_summary_table(results_table: dict):
    full_sc = results_table["top_100pct"]["sc_accuracy"]
    print("\n" + "=" * 75)
    print("Direction B: DeepConf Confidence Filtering + SICA")
    print("=" * 75)
    print(f"{'Method':<35} {'K_eff':>6} {'Accuracy':>10} {'Δ vs Full SC':>12}")
    print("-" * 75)
    for label, data in results_table.items():
        ratio_str = f"top {int(data['ratio']*100)}%"
        sc_acc = data["sc_accuracy"]
        sica_acc = data["sica_accuracy"]
        avg_k = data["avg_k_effective"]
        sc_delta = (sc_acc - full_sc) * 100
        sica_delta = (sica_acc - full_sc) * 100
        print(
            f"  SC ({ratio_str}, K≈{avg_k:.0f})"
            f"{'':>{22-len(ratio_str)}} {avg_k:>6.1f} {sc_acc*100:>9.1f}% {sc_delta:>+11.1f}pp"
        )
        print(
            f"  SICA ({ratio_str}, K≈{avg_k:.0f})"
            f"{'':>{20-len(ratio_str)}} {avg_k:>6.1f} {sica_acc*100:>9.1f}% {sica_delta:>+11.1f}pp"
        )
    print("=" * 75)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-scoring", action="store_true",
                        help="Skip logprob scoring, use cached scores")
    parser.add_argument("--score-only", action="store_true",
                        help="Only run logprob scoring, skip comparisons")
    args = parser.parse_args()

    logger.info("Loading data...")
    problems = load_all_data()

    if args.skip_scoring:
        problems = load_logprob_cache(problems)
    else:
        problems = asyncio.run(score_all_traces(problems))
        if args.score_only:
            logger.info("Score-only mode, exiting.")
            return

    logger.info("Running comparisons...")
    results_table = run_comparisons(problems)

    print_summary_table(results_table)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / "results.json"
    summary = {}
    for label, data in results_table.items():
        summary[label] = {k: v for k, v in data.items() if k != "per_problem"}
    full_output = {"summary": summary, "details": results_table}
    output_file.write_text(json.dumps(full_output, indent=2, default=str))
    logger.info("Results saved to %s", output_file)

    logprob_stats = []
    for pid, pdata in problems.items():
        for t in pdata["traces"]:
            lp = t.get("logprob", -100.0)
            if lp > -99:
                logprob_stats.append(lp)
    if logprob_stats:
        logprob_stats.sort()
        n = len(logprob_stats)
        logger.info(
            "Logprob stats: min=%.2f, p25=%.2f, median=%.2f, p75=%.2f, max=%.2f",
            logprob_stats[0],
            logprob_stats[n // 4],
            logprob_stats[n // 2],
            logprob_stats[3 * n // 4],
            logprob_stats[-1],
        )

    print("DEEPCONF_FILTER_DONE")


if __name__ == "__main__":
    main()
