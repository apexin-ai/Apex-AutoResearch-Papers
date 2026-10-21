"""AlpacaEval × Qwen3-32B: pairwise + Likert scoring, then BT/Likert/GEE analysis."""

import asyncio
import json
import logging
import os
import re
import time

import numpy as np
from scipy import stats

logger = logging.getLogger(__name__)

MODEL = "/root/autodl-tmp/models/Qwen3-32B/"
BASE_URL = "http://localhost:8000/v1"
API_KEY = "[REDACTED]"
NLI_THRESHOLD = 0.90

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


def strip_thinking(text):
    if "</think>" in text:
        text = text.split("</think>")[-1]
    return text.strip()


def parse_choice(text):
    text = strip_thinking(text).upper()
    if text in ("A", "B"):
        return text
    m = re.search(r"\b([AB])\b", text)
    return m.group(1) if m else None


def parse_score(text):
    text = strip_thinking(text)
    m = re.search(r"\b(10|[1-9])\b", text)
    return int(m.group(1)) if m else None


class RateLimiter:
    def __init__(self, max_per_minute=200):
        self._interval = 60.0 / max_per_minute
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
                max_tokens=2048,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            logger.warning("API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


# ── Pairwise ─────────────────────────────────────────────────────────────────

async def pairwise_score_record(client, rec, semaphore, limiter):
    async with semaphore:
        instruction = rec["instruction"]
        orig = rec["original_formality"]

        if orig == "formal":
            formal_text, casual_text = rec["original_text"], rec["counterfactual_text"]
        else:
            formal_text, casual_text = rec["counterfactual_text"], rec["original_text"]

        msgs1 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=formal_text, response_b=casual_text)},
        ]
        t1_raw = await call_llm(client, msgs1, limiter)
        t1_choice = parse_choice(t1_raw) if t1_raw else None

        msgs2 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=casual_text, response_b=formal_text)},
        ]
        t2_raw = await call_llm(client, msgs2, limiter)
        t2_choice = parse_choice(t2_raw) if t2_raw else None

        t1_pf = (t1_choice == "A") if t1_choice else None
        t2_pf = (t2_choice == "B") if t2_choice else None

        if t1_pf is not None and t2_pf is not None:
            consistent = (t1_pf == t2_pf)
            formal_wins = t1_pf if consistent else None
        else:
            consistent = None
            formal_wins = None

        return {
            "id": rec["id"], "instruction": instruction,
            "original_formality": orig,
            "nli_cf": rec.get("nli_cf", 0),
            "bertscore_cf": rec.get("bertscore_cf", 0),
            "trial1_choice": t1_choice, "trial1_prefers_formal": t1_pf,
            "trial2_choice": t2_choice, "trial2_prefers_formal": t2_pf,
            "consistent": consistent, "formal_wins": formal_wins,
        }


async def run_pairwise(records, output_path):
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=[REDACTED], base_url=BASE_URL)

    done_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for line in f:
                if line.strip():
                    done_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in done_ids]
    logger.info("Pairwise: total=%d, done=%d, todo=%d", len(records), len(done_ids), len(todo))
    if not todo:
        return

    sem = asyncio.Semaphore(10)
    lim = RateLimiter(200)
    tasks = [pairwise_score_record(client, r, sem, lim) for r in todo]

    with open(output_path, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info("Pairwise %s: t1=%s t2=%s consistent=%s formal_wins=%s",
                        result["id"], result["trial1_choice"], result["trial2_choice"],
                        result["consistent"], result["formal_wins"])


# ── Likert ───────────────────────────────────────────────────────────────────

async def likert_score_record(client, rec, semaphore, limiter):
    async with semaphore:
        instruction = rec["instruction"]
        scores = {}
        for key in ("original_text", "counterfactual_text", "double_rewrite_text"):
            msgs = [
                {"role": "system", "content": LIKERT_SYSTEM},
                {"role": "user", "content": LIKERT_USER.format(
                    instruction=instruction, response=rec[key])},
            ]
            raw = await call_llm(client, msgs, limiter)
            scores[key] = parse_score(raw) if raw else None

        return {
            **rec,
            "score_original": scores["original_text"],
            "score_counterfactual": scores["counterfactual_text"],
            "score_double_rewrite": scores["double_rewrite_text"],
        }


async def run_likert(records, output_path):
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=[REDACTED], base_url=BASE_URL)

    done_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for line in f:
                if line.strip():
                    done_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in done_ids]
    logger.info("Likert: total=%d, done=%d, todo=%d", len(records), len(done_ids), len(todo))
    if not todo:
        return

    sem = asyncio.Semaphore(10)
    lim = RateLimiter(200)
    tasks = [likert_score_record(client, r, sem, lim) for r in todo]

    with open(output_path, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info("Likert %s: orig=%s cf=%s dr=%s",
                        result["id"], result["score_original"],
                        result["score_counterfactual"], result["score_double_rewrite"])


# ── Analysis ─────────────────────────────────────────────────────────────────

def bt_pair_bootstrap(records, n_bootstrap=10000, seed=42):
    import choix
    pair_groups = []
    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            pf = rec.get(f"trial{trial}_prefers_formal")
            if pf is None:
                continue
            pair_comps.append((0, 1) if pf else (1, 0))
        if pair_comps:
            pair_groups.append(pair_comps)

    all_comps = [c for g in pair_groups for c in g]
    n_pairs = len(pair_groups)
    params = choix.ilsr_pairwise(2, all_comps, alpha=0.01)
    p_formal = np.exp(params[0]) / np.sum(np.exp(params))

    rng = np.random.RandomState(seed)
    boot_p = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        bc = [c for i in idx for c in pair_groups[i]]
        try:
            bp = choix.ilsr_pairwise(2, bc, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / np.sum(np.exp(bp)))
        except Exception:
            pass
    boot_p = np.array(boot_p)
    ci_lo, ci_hi = np.percentile(boot_p, [2.5, 97.5])
    n_below = np.sum(boot_p < 0.5)
    p_val = max(n_below / len(boot_p), 1.0 / n_bootstrap) if n_below == 0 else n_below / len(boot_p)
    return {"n_pairs": n_pairs, "p_formal": p_formal,
            "ci_lo": ci_lo, "ci_hi": ci_hi, "p_val": p_val}


def likert_analysis(scored_records):
    valid = [r for r in scored_records
             if r.get("score_original") is not None and r.get("score_counterfactual") is not None]
    formal_s, casual_s = [], []
    for r in valid:
        if r["original_formality"] == "formal":
            formal_s.append(r["score_original"])
            casual_s.append(r["score_counterfactual"])
        else:
            formal_s.append(r["score_counterfactual"])
            casual_s.append(r["score_original"])

    formal_s = np.array(formal_s, dtype=float)
    casual_s = np.array(casual_s, dtype=float)
    ate = np.mean(formal_s) - np.mean(casual_s)
    diffs = formal_s - casual_s
    pooled_std = np.sqrt((np.var(formal_s, ddof=1) + np.var(casual_s, ddof=1)) / 2)
    cohen_d = ate / pooled_std if pooled_std > 0 else 0.0
    _, wilcoxon_p = stats.wilcoxon(formal_s, casual_s, alternative="two-sided")
    tie_rate = float(np.mean(diffs == 0))

    return {"n": len(valid), "mean_formal": float(np.mean(formal_s)),
            "mean_casual": float(np.mean(casual_s)), "ate": ate,
            "cohen_d": cohen_d, "wilcoxon_p": wilcoxon_p, "tie_rate": tie_rate}


def gee_analysis(pairwise_records):
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.genmod.generalized_estimating_equations import GEE
    from statsmodels.genmod.families import Binomial
    from statsmodels.genmod.cov_struct import Exchangeable

    rows = []
    for i, r in enumerate(pairwise_records):
        orig = r["original_formality"]
        # Trial 1: formal in position A
        rows.append({"pair_id": i, "is_style_in_A": 1.0,
                      "is_original_in_A": 1.0 if orig == "formal" else 0.0,
                      "chose_A": 1.0 if r["trial1_choice"] == "A" else 0.0})
        # Trial 2: casual in position A
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

    return {"n_obs": len(df), "n_pairs": df["pair_id"].nunique(),
            "style_or": s_or, "style_ci": (s_lo, s_hi), "style_p": s_p,
            "orig_or": o_or, "orig_ci": (o_lo, o_hi), "orig_p": o_p}


def run_analysis(pairwise_path, scored_path):
    with open(pairwise_path) as f:
        pw_all = [json.loads(l) for l in f if l.strip()]
    pw = [r for r in pw_all if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    with open(scored_path) as f:
        sc_all = [json.loads(l) for l in f if l.strip()]
    sc = [r for r in sc_all if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    bt = bt_pair_bootstrap(pw)
    lk = likert_analysis(sc)
    gee = gee_analysis(pw)

    consistent = [r for r in pw if r.get("consistent") is True]
    blindspot = bt["p_formal"] > 0.5 and bt["p_val"] < 0.05

    def fp(p):
        return "< 0.0001" if p < 0.0001 else f"{p:.4f}"

    print(f"\n{'='*60}")
    print("## AlpacaEval × Qwen3-32B")
    print(f"Pairs: {bt['n_pairs']} (NLI≥{NLI_THRESHOLD})")
    print(f"Consistency: {len(consistent)}/{len(pw)} ({len(consistent)/len(pw)*100:.1f}%)")
    print(f"BT: P(formal)={bt['p_formal']*100:.1f}% [{bt['ci_lo']*100:.1f}%, {bt['ci_hi']*100:.1f}%], p={fp(bt['p_val'])}")
    print(f"Likert: ATE={lk['ate']:.3f}, p={fp(lk['wilcoxon_p'])}, d={lk['cohen_d']:.3f}, tie_rate={lk['tie_rate']*100:.1f}%")
    print(f"  mean(formal)={lk['mean_formal']:.2f}, mean(casual)={lk['mean_casual']:.2f}")
    print(f"Blindspot: {'Yes' if blindspot else 'No'}")
    print(f"GEE: Style OR={gee['style_or']:.2f} [{gee['style_ci'][0]:.2f}, {gee['style_ci'][1]:.2f}] p={fp(gee['style_p'])}, "
          f"Orig OR={gee['orig_or']:.2f} [{gee['orig_ci'][0]:.2f}, {gee['orig_ci'][1]:.2f}] p={fp(gee['orig_p'])}")
    print(f"{'='*60}")


async def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--analyze-only", action="store_true")
    args = parser.parse_args()

    data_dir = "/root/causal_style_decomp_judge/data"
    input_path = f"{data_dir}/verified_alpacaeval.jsonl"
    pw_path = f"{data_dir}/pairwise_results_alpacaeval_qwen32b.jsonl"
    sc_path = f"{data_dir}/scored_alpacaeval_qwen32b.jsonl"

    if not args.analyze_only:
        with open(input_path) as f:
            records = [json.loads(l) for l in f if l.strip()]
        logger.info("Loaded %d records", len(records))

        print("=== Phase 1: Pairwise Scoring ===")
        await run_pairwise(records, pw_path)
        print("=== Phase 2: Likert Scoring ===")
        await run_likert(records, sc_path)

    print("=== Phase 3: Analysis ===")
    run_analysis(pw_path, sc_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(main())
