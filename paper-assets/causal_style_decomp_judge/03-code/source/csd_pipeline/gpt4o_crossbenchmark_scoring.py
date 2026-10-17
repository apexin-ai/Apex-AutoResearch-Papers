"""AlpacaEval + MT-Bench × GPT-4o: pairwise + Likert scoring, then BT/Likert/GEE analysis."""

import asyncio
import json
import logging
import re
import time

import choix
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.genmod.families import Binomial

logger = logging.getLogger(__name__)

MODEL = "gpt-4o"
BASE_URL = "http://47.94.22.126/v1"
API_KEY = "[REDACTED]"
NLI_THRESHOLD = 0.90
N_BOOTSTRAP = 10000
SEED = 42
MAX_CONCURRENT = 5
RATE_INTERVAL = 1.0

PAIRWISE_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Compare the two responses below and pick the better one."
)
PAIRWISE_USER = """Instruction: {instruction}

Response A:
{response_a}

Response B:
{response_b}

Which response is better in terms of overall quality (helpfulness, accuracy, completeness, coherence)?
Output ONLY "A" or "B"."""

LIKERT_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Rate the quality of the following response to the given instruction."
)
LIKERT_USER = """Instruction: {instruction}
Response: {response}

Evaluate the overall quality of this response based on helpfulness, accuracy, completeness, and coherence. Rate on a scale of 1-10, where:
1-2: Completely inadequate
3-4: Poor quality with major issues
5-6: Acceptable but with notable weaknesses
7-8: Good quality with minor issues
9-10: Excellent quality

Provide your rating as a single integer. Output ONLY the number, nothing else."""


def parse_choice(text):
    text = text.strip().upper()
    if text in ("A", "B"):
        return text
    m = re.search(r"\b([AB])\b", text)
    return m.group(1) if m else None


def parse_score(text):
    m = re.search(r"\b(10|[1-9])\b", text.strip())
    return int(m.group(1)) if m else None


class RateLimiter:
    def __init__(self, interval=RATE_INTERVAL):
        self._interval = interval
        self._last = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            now = time.monotonic()
            wait = self._interval - (now - self._last)
            if wait > 0:
                await asyncio.sleep(wait)
            self._last = time.monotonic()


async def call_llm(client, messages, limiter, max_retries=3):
    for attempt in range(max_retries):
        await limiter.acquire()
        try:
            resp = await client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.0,
                max_tokens=16,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            logger.warning("API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


# ============================================================
# Pairwise scoring (position-controlled dual-trial)
# ============================================================

async def pairwise_score_record(client, rec, semaphore, limiter):
    async with semaphore:
        instruction = rec["instruction"]
        orig = rec["original_formality"]

        if orig == "formal":
            formal_text, casual_text = rec["original_text"], rec["counterfactual_text"]
        else:
            formal_text, casual_text = rec["counterfactual_text"], rec["original_text"]

        # Trial 1: formal=A, casual=B
        msgs1 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=formal_text, response_b=casual_text)},
        ]
        t1_raw = await call_llm(client, msgs1, limiter)
        t1_choice = parse_choice(t1_raw) if t1_raw else None

        # Trial 2: casual=A, formal=B
        msgs2 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=casual_text, response_b=formal_text)},
        ]
        t2_raw = await call_llm(client, msgs2, limiter)
        t2_choice = parse_choice(t2_raw) if t2_raw else None

        # Derive preferences
        t1_prefers_formal = (t1_choice == "A") if t1_choice else None
        t2_prefers_formal = (t2_choice == "B") if t2_choice else None

        consistent = None
        if t1_prefers_formal is not None and t2_prefers_formal is not None:
            consistent = (t1_prefers_formal == t2_prefers_formal)

        return {
            **rec,
            "trial1_choice": t1_choice,
            "trial2_choice": t2_choice,
            "trial1_prefers_formal": t1_prefers_formal,
            "trial2_prefers_formal": t2_prefers_formal,
            "consistent": consistent,
            "prefers_formal": t1_prefers_formal if consistent else None,
        }


async def run_pairwise(records, output_path, client, semaphore, limiter):
    tasks = [pairwise_score_record(client, r, semaphore, limiter) for r in records]
    results = []
    for i, coro in enumerate(asyncio.as_completed(tasks)):
        result = await coro
        results.append(result)
        if (i + 1) % 10 == 0 or (i + 1) == len(tasks):
            logger.info("Pairwise: %d/%d done", i + 1, len(tasks))

    results.sort(key=lambda r: r["id"])
    with open(output_path, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    logger.info("Saved pairwise results to %s (%d records)", output_path, len(results))
    return results


# ============================================================
# Likert scoring
# ============================================================

async def likert_score_record(client, rec, semaphore, limiter):
    async with semaphore:
        instruction = rec["instruction"]

        msgs_orig = [
            {"role": "system", "content": LIKERT_SYSTEM},
            {"role": "user", "content": LIKERT_USER.format(
                instruction=instruction, response=rec["original_text"])},
        ]
        raw_orig = await call_llm(client, msgs_orig, limiter)
        score_orig = parse_score(raw_orig) if raw_orig else None

        msgs_cf = [
            {"role": "system", "content": LIKERT_SYSTEM},
            {"role": "user", "content": LIKERT_USER.format(
                instruction=instruction, response=rec["counterfactual_text"])},
        ]
        raw_cf = await call_llm(client, msgs_cf, limiter)
        score_cf = parse_score(raw_cf) if raw_cf else None

        return {
            **rec,
            "score_original": score_orig,
            "score_counterfactual": score_cf,
        }


async def run_likert(records, output_path, client, semaphore, limiter):
    tasks = [likert_score_record(client, r, semaphore, limiter) for r in records]
    results = []
    for i, coro in enumerate(asyncio.as_completed(tasks)):
        result = await coro
        results.append(result)
        if (i + 1) % 10 == 0 or (i + 1) == len(tasks):
            logger.info("Likert: %d/%d done", i + 1, len(tasks))

    results.sort(key=lambda r: r["id"])
    with open(output_path, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    logger.info("Saved Likert results to %s (%d records)", output_path, len(results))
    return results


# ============================================================
# Analysis functions
# ============================================================

def bt_pair_bootstrap(records):
    valid = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
    pair_groups = []
    for rec in valid:
        comps = []
        for trial in [1, 2]:
            pf = rec.get(f"trial{trial}_prefers_formal")
            if pf is None:
                continue
            if pf:
                comps.append((0, 1))  # formal > casual
            else:
                comps.append((1, 0))  # casual > formal
        if comps:
            pair_groups.append(comps)

    all_comps = [c for g in pair_groups for c in g]
    params = choix.ilsr_pairwise(2, all_comps, alpha=0.01)
    p_formal = np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))

    rng = np.random.RandomState(SEED)
    n_pairs = len(pair_groups)
    boot_p = []
    for _ in range(N_BOOTSTRAP):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = [c for i in idx for c in pair_groups[i]]
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / (np.exp(bp[0]) + np.exp(bp[1])))
        except Exception:
            pass

    boot_p = np.array(boot_p)
    ci_lo = np.percentile(boot_p, 2.5)
    ci_hi = np.percentile(boot_p, 97.5)
    p_val = 2 * min(np.mean(boot_p >= 0.5), np.mean(boot_p <= 0.5))

    return {
        "n_pairs": n_pairs,
        "p_formal": p_formal,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "p_val": p_val,
    }


def likert_analysis(records):
    valid = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
    formal_scores = []
    casual_scores = []

    for rec in valid:
        orig = rec.get("original_formality")
        s_orig = rec.get("score_original")
        s_cf = rec.get("score_counterfactual")
        if s_orig is None or s_cf is None:
            continue
        if orig == "formal":
            formal_scores.append(s_orig)
            casual_scores.append(s_cf)
        else:
            formal_scores.append(s_cf)
            casual_scores.append(s_orig)

    formal_scores = np.array(formal_scores, dtype=float)
    casual_scores = np.array(casual_scores, dtype=float)
    diffs = formal_scores - casual_scores

    ate = np.mean(diffs)
    n = len(diffs)
    ties = np.sum(diffs == 0)
    tie_rate = ties / n if n > 0 else 0

    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        _, wilcoxon_p = stats.wilcoxon(non_zero)
    else:
        wilcoxon_p = 1.0

    sd = np.std(diffs, ddof=1)
    cohens_d = ate / sd if sd > 0 else 0.0

    return {
        "n": n,
        "ate": ate,
        "wilcoxon_p": wilcoxon_p,
        "cohens_d": cohens_d,
        "tie_rate": tie_rate,
        "mean_formal": np.mean(formal_scores),
        "mean_casual": np.mean(casual_scores),
    }


def gee_analysis(records):
    valid = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
    rows = []
    for i, r in enumerate(valid):
        orig = r["original_formality"]
        rows.append({"pair_id": i, "is_style_in_A": 1.0,
                      "is_original_in_A": 1.0 if orig == "formal" else 0.0,
                      "chose_A": 1.0 if r["trial1_choice"] == "A" else 0.0})
        rows.append({"pair_id": i, "is_style_in_A": 0.0,
                      "is_original_in_A": 1.0 if orig == "casual" else 0.0,
                      "chose_A": 1.0 if r["trial2_choice"] == "A" else 0.0})

    df = pd.DataFrame(rows)
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=Exchangeable())
    result = model.fit()

    def _or_ci(name):
        c = result.params[name]
        se = result.bse[name]
        return np.exp(c), np.exp(c - 1.96 * se), np.exp(c + 1.96 * se), result.pvalues[name]

    s_or, s_lo, s_hi, s_p = _or_ci("is_style_in_A")
    o_or, o_lo, o_hi, o_p = _or_ci("is_original_in_A")

    return {
        "style_or": s_or, "style_ci": (s_lo, s_hi), "style_p": s_p,
        "orig_or": o_or, "orig_ci": (o_lo, o_hi), "orig_p": o_p,
    }


def fmt_p(p):
    return "< 0.0001" if p < 0.0001 else f"{p:.4f}"


def run_analysis(pw_path, sc_path, label):
    with open(pw_path) as f:
        pw = [json.loads(l) for l in f if l.strip()]
    with open(sc_path) as f:
        sc = [json.loads(l) for l in f if l.strip()]

    bt = bt_pair_bootstrap(pw)
    lk = likert_analysis(sc)
    gee = gee_analysis(pw)

    blindspot = bt["p_formal"] > 0.5 and bt["p_val"] < 0.05

    print(f"\n## {label} × GPT-4o")
    print(f"Pairs: {bt['n_pairs']}")
    print(f"BT: P(formal)={bt['p_formal']*100:.1f}% [{bt['ci_lo']*100:.1f}%, {bt['ci_hi']*100:.1f}%], p={fmt_p(bt['p_val'])}")
    print(f"Likert: ATE={lk['ate']:.3f}, p={fmt_p(lk['wilcoxon_p'])}, d={lk['cohens_d']:.3f}, tie_rate={lk['tie_rate']*100:.1f}%")
    print(f"Blindspot: {'Yes' if blindspot else 'No'}")
    print(f"GEE: Style OR={gee['style_or']:.2f} p={fmt_p(gee['style_p'])}, Orig OR={gee['orig_or']:.2f} p={fmt_p(gee['orig_p'])}")


# ============================================================
# Main
# ============================================================

BENCHMARKS = [
    {
        "name": "AlpacaEval",
        "input": "/root/causal_style_decomp_judge/data/verified_alpacaeval.jsonl",
        "pw_out": "/root/causal_style_decomp_judge/data/pairwise_results_alpacaeval_gpt4o.jsonl",
        "sc_out": "/root/causal_style_decomp_judge/data/scored_alpacaeval_gpt4o.jsonl",
    },
    {
        "name": "MT-Bench",
        "input": "/root/causal_style_decomp_judge/data/verified_mtbench.jsonl",
        "pw_out": "/root/causal_style_decomp_judge/data/pairwise_results_mtbench_gpt4o.jsonl",
        "sc_out": "/root/causal_style_decomp_judge/data/scored_mtbench_gpt4o.jsonl",
    },
]


async def main():
    import argparse
    from openai import AsyncOpenAI

    parser = argparse.ArgumentParser()
    parser.add_argument("--analyze-only", action="store_true")
    parser.add_argument("--benchmark", choices=["alpacaeval", "mtbench", "all"], default="all")
    args = parser.parse_args()

    benchmarks = BENCHMARKS
    if args.benchmark == "alpacaeval":
        benchmarks = [BENCHMARKS[0]]
    elif args.benchmark == "mtbench":
        benchmarks = [BENCHMARKS[1]]

    if not args.analyze_only:
        client = AsyncOpenAI(base_url=BASE_URL, api_key=[REDACTED]
        semaphore = asyncio.Semaphore(MAX_CONCURRENT)
        limiter = RateLimiter()

        for bm in benchmarks:
            with open(bm["input"]) as f:
                records = [json.loads(l) for l in f if l.strip()]
            logger.info("=== %s: %d records ===", bm["name"], len(records))

            print(f"=== {bm['name']}: Pairwise Scoring ===")
            await run_pairwise(records, bm["pw_out"], client, semaphore, limiter)

            print(f"=== {bm['name']}: Likert Scoring ===")
            await run_likert(records, bm["sc_out"], client, semaphore, limiter)

    print("\n" + "=" * 60)
    for bm in benchmarks:
        run_analysis(bm["pw_out"], bm["sc_out"], bm["name"])
    print("=" * 60)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(main())
