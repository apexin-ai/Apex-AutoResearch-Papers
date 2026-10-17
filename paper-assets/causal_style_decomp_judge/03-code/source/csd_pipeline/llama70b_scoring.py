"""Llama-3.3-70B-Instruct judge: pairwise + Likert scoring + BT/Likert/GEE analysis for formality & verbosity."""

import asyncio
import json
import logging
import os
import re
import time

import numpy as np
import pandas as pd
import choix
import statsmodels.api as sm
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.cov_struct import Exchangeable
from scipy import stats

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8003/v1"
API_KEY = "[REDACTED]"
NLI_THRESHOLD = 0.90
N_BOOTSTRAP = 10000
SEED = 42
MODEL = None  # resolved at runtime from /v1/models

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
    text = text.strip()
    m = re.search(r"\b(10|[1-9])\b", text)
    return int(m.group(1)) if m else None


class RateLimiter:
    def __init__(self, interval=0.05):
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
                await asyncio.sleep(2 ** (attempt + 1))
    return None


AXIS_CONFIG = {
    "formality": {
        "orig_field": "original_formality",
        "pole_a": "formal", "pole_b": "casual",
        "pref_key": "prefers_formal",
    },
    "verbosity": {
        "orig_field": "original_verbosity",
        "pole_a": "verbose", "pole_b": "concise",
        "pref_key": "prefers_verbose",
    },
}


async def pairwise_score_record(client, rec, axis, semaphore, limiter):
    async with semaphore:
        cfg = AXIS_CONFIG[axis]
        instruction = rec["instruction"]
        orig = rec[cfg["orig_field"]]

        if orig == cfg["pole_a"]:
            pole_a_text, pole_b_text = rec["original_text"], rec["counterfactual_text"]
        else:
            pole_a_text, pole_b_text = rec["counterfactual_text"], rec["original_text"]

        msgs1 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=pole_a_text, response_b=pole_b_text)},
        ]
        t1_raw = await call_llm(client, msgs1, limiter)
        t1_choice = parse_choice(t1_raw) if t1_raw else None

        msgs2 = [
            {"role": "system", "content": PAIRWISE_SYSTEM},
            {"role": "user", "content": PAIRWISE_USER.format(
                instruction=instruction, response_a=pole_b_text, response_b=pole_a_text)},
        ]
        t2_raw = await call_llm(client, msgs2, limiter)
        t2_choice = parse_choice(t2_raw) if t2_raw else None

        t1_pref = (t1_choice == "A") if t1_choice else None
        t2_pref = (t2_choice == "B") if t2_choice else None

        if t1_pref is not None and t2_pref is not None:
            consistent = (t1_pref == t2_pref)
            pole_a_wins = t1_pref if consistent else None
        else:
            consistent = None
            pole_a_wins = None

        return {
            "id": rec["id"], "instruction": instruction,
            cfg["orig_field"]: orig,
            "nli_cf": rec.get("nli_cf", 0),
            "bertscore_cf": rec.get("bertscore_cf", 0),
            "trial1_choice": t1_choice, f"trial1_{cfg['pref_key']}": t1_pref,
            "trial2_choice": t2_choice, f"trial2_{cfg['pref_key']}": t2_pref,
            "consistent": consistent, cfg["pref_key"]: pole_a_wins,
        }


async def run_pairwise(records, output_path, axis):
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=[REDACTED], base_url=BASE_URL)

    done_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for line in f:
                if line.strip():
                    done_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in done_ids]
    logger.info("Pairwise [%s]: total=%d, done=%d, todo=%d", axis, len(records), len(done_ids), len(todo))
    if not todo:
        return

    sem = asyncio.Semaphore(10)
    lim = RateLimiter(0.05)
    tasks = [pairwise_score_record(client, r, axis, sem, lim) for r in todo]

    with open(output_path, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            cfg = AXIS_CONFIG[axis]
            logger.info("Pairwise [%s] %s: t1=%s t2=%s consistent=%s %s=%s",
                        axis, result["id"], result["trial1_choice"], result["trial2_choice"],
                        result["consistent"], cfg["pref_key"], result.get(cfg["pref_key"]))


async def likert_score_record(client, rec, semaphore, limiter):
    async with semaphore:
        instruction = rec["instruction"]
        scores = {}
        for key in ("original_text", "counterfactual_text"):
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
        }


async def run_likert(records, output_path, axis):
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=[REDACTED], base_url=BASE_URL)

    done_ids = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for line in f:
                if line.strip():
                    done_ids.add(json.loads(line)["id"])

    todo = [r for r in records if r["id"] not in done_ids]
    logger.info("Likert [%s]: total=%d, done=%d, todo=%d", axis, len(records), len(done_ids), len(todo))
    if not todo:
        return

    sem = asyncio.Semaphore(10)
    lim = RateLimiter(0.05)
    tasks = [likert_score_record(client, r, sem, lim) for r in todo]

    with open(output_path, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info("Likert [%s] %s: orig=%s cf=%s",
                        axis, result["id"], result["score_original"], result["score_counterfactual"])


def bt_pair_bootstrap(records, pref_key, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    pair_groups = []
    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            pf = rec.get(f"trial{trial}_{pref_key}")
            if pf is None:
                continue
            pair_comps.append((0, 1) if pf else (1, 0))
        if pair_comps:
            pair_groups.append(pair_comps)

    all_comps = [c for g in pair_groups for c in g]
    n_pairs = len(pair_groups)
    params = choix.ilsr_pairwise(2, all_comps, alpha=0.01)
    p_pole_a = np.exp(params[0]) / np.sum(np.exp(params))

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
    p_val = 2 * min(n_below, len(boot_p) - n_below) / len(boot_p)
    p_val = max(p_val, 1.0 / n_bootstrap)
    return {"n_pairs": n_pairs, "p_pole_a": float(p_pole_a),
            "ci_lo": float(ci_lo), "ci_hi": float(ci_hi), "p_val": float(p_val)}


def likert_analysis(scored_records, axis):
    cfg = AXIS_CONFIG[axis]
    valid = [r for r in scored_records
             if r.get("score_original") is not None and r.get("score_counterfactual") is not None]
    style_s, plain_s = [], []
    for r in valid:
        if r[cfg["orig_field"]] == cfg["pole_a"]:
            style_s.append(r["score_original"])
            plain_s.append(r["score_counterfactual"])
        else:
            style_s.append(r["score_counterfactual"])
            plain_s.append(r["score_original"])

    style_s = np.array(style_s, dtype=float)
    plain_s = np.array(plain_s, dtype=float)
    diffs = style_s - plain_s
    ate = float(np.mean(diffs))
    pooled_std = np.sqrt((np.var(style_s, ddof=1) + np.var(plain_s, ddof=1)) / 2)
    cohen_d = float(ate / pooled_std) if pooled_std > 0 else 0.0
    non_zero = diffs[diffs != 0]
    if len(non_zero) > 0:
        _, wilcoxon_p = stats.wilcoxon(non_zero)
    else:
        wilcoxon_p = 1.0
    tie_rate = float(np.mean(diffs == 0))
    _, ttest_p = stats.ttest_rel(style_s, plain_s)

    return {"n": len(valid), "ate": ate, "cohen_d": cohen_d,
            "wilcoxon_p": float(wilcoxon_p), "ttest_p": float(ttest_p), "tie_rate": tie_rate}


def gee_analysis(pairwise_records, axis):
    cfg = AXIS_CONFIG[axis]
    rows = []
    for i, r in enumerate(pairwise_records):
        orig = r[cfg["orig_field"]]
        rows.append({"pair_id": i, "is_style_in_A": 1.0,
                      "is_original_in_A": 1.0 if orig == cfg["pole_a"] else 0.0,
                      "chose_A": 1.0 if r["trial1_choice"] == "A" else 0.0})
        rows.append({"pair_id": i, "is_style_in_A": 0.0,
                      "is_original_in_A": 1.0 if orig == cfg["pole_b"] else 0.0,
                      "chose_A": 1.0 if r["trial2_choice"] == "A" else 0.0})

    df = pd.DataFrame(rows)
    exog = sm.add_constant(df[["is_style_in_A", "is_original_in_A"]])
    model = GEE(df["chose_A"], exog, groups=df["pair_id"],
                family=Binomial(), cov_struct=Exchangeable())
    result = model.fit()

    def _or_ci(name):
        c = result.params[name]
        se = result.bse[name]
        lo = np.exp(c - 1.96 * se)
        hi = np.exp(c + 1.96 * se)
        return float(np.exp(c)), float(result.pvalues[name]), float(lo), float(hi)

    s_or, s_p, s_lo, s_hi = _or_ci("is_style_in_A")
    o_or, o_p, o_lo, o_hi = _or_ci("is_original_in_A")

    return {"style_or": s_or, "style_p": s_p, "style_ci": [s_lo, s_hi],
            "orig_or": o_or, "orig_p": o_p, "orig_ci": [o_lo, o_hi]}


def run_analysis(pairwise_path, scored_path, axis):
    cfg = AXIS_CONFIG[axis]
    with open(pairwise_path) as f:
        pw_all = [json.loads(l) for l in f if l.strip()]
    pw = [r for r in pw_all if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    with open(scored_path) as f:
        sc_all = [json.loads(l) for l in f if l.strip()]
    sc = [r for r in sc_all if r.get("nli_cf", 0) >= NLI_THRESHOLD]

    bt = bt_pair_bootstrap(pw, cfg["pref_key"])
    lk = likert_analysis(sc, axis)
    gee = gee_analysis(pw, axis)

    bt_sig = bt["p_val"] < 0.05
    likert_sig = lk["ttest_p"] < 0.05
    blindspot = bt_sig and not likert_sig

    return {
        "axis": axis,
        "n_pairs": bt["n_pairs"],
        "bt": bt,
        "likert": lk,
        "gee": gee,
        "bt_significant": bt_sig,
        "likert_significant": likert_sig,
        "blindspot": blindspot,
    }


async def resolve_model():
    global MODEL
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=[REDACTED], base_url=BASE_URL)
    models = await client.models.list()
    MODEL = models.data[0].id
    logger.info("Resolved model: %s", MODEL)
    return MODEL


async def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--analyze-only", action="store_true")
    args = parser.parse_args()

    data_dir = "/root/causal_style_decomp_judge/data"

    if not args.analyze_only:
        model_name = await resolve_model()
        print(f"Using model: {model_name}")

    axes = [
        {"axis": "formality",
         "input": f"{data_dir}/verified_32b.jsonl",
         "pw_out": f"{data_dir}/pairwise_results_llama70b_formality.jsonl",
         "sc_out": f"{data_dir}/scored_llama70b_formality.jsonl"},
        {"axis": "verbosity",
         "input": f"{data_dir}/verified_verbosity.jsonl",
         "pw_out": f"{data_dir}/pairwise_results_llama70b_verbosity.jsonl",
         "sc_out": f"{data_dir}/scored_llama70b_verbosity.jsonl"},
    ]

    results = {}
    for ax in axes:
        with open(ax["input"]) as f:
            records = [json.loads(l) for l in f if l.strip()]
        filtered = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
        logger.info("[%s] Loaded %d records, %d pass NLI filter", ax["axis"], len(records), len(filtered))

        if not args.analyze_only:
            print(f"=== Pairwise: {ax['axis']} ({len(filtered)} pairs) ===")
            await run_pairwise(filtered, ax["pw_out"], ax["axis"])
            print(f"=== Likert: {ax['axis']} ({len(filtered)} pairs) ===")
            await run_likert(filtered, ax["sc_out"], ax["axis"])

        print(f"=== Analysis: {ax['axis']} ===")
        r = run_analysis(ax["pw_out"], ax["sc_out"], ax["axis"])
        results[ax["axis"]] = r

        def fp(p):
            return "< 0.0001" if p < 0.0001 else f"{p:.4f}"

        pole_label = AXIS_CONFIG[ax["axis"]]["pole_a"]
        print(f"\n## Llama-3.3-70B x {ax['axis'].capitalize()}")
        print(f"Pairs: {r['n_pairs']}")
        print(f"BT: P({pole_label})={r['bt']['p_pole_a']*100:.1f}% "
              f"[{r['bt']['ci_lo']*100:.1f}%, {r['bt']['ci_hi']*100:.1f}%], "
              f"p={fp(r['bt']['p_val'])}")
        print(f"Likert: ATE={r['likert']['ate']:.3f}, "
              f"ttest_p={fp(r['likert']['ttest_p'])}, "
              f"wilcoxon_p={fp(r['likert']['wilcoxon_p'])}, "
              f"d={r['likert']['cohen_d']:.3f}, "
              f"tie_rate={r['likert']['tie_rate']*100:.1f}%")
        print(f"Blindspot: {'YES' if r['blindspot'] else 'No'}")
        print(f"GEE: Style OR={r['gee']['style_or']:.2f} p={fp(r['gee']['style_p'])}, "
              f"Orig OR={r['gee']['orig_or']:.2f} p={fp(r['gee']['orig_p'])}")

    output_path = f"{data_dir}/llama70b_third_judge.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(main())
