"""Pairwise comparison scoring via GPT-4o with position bias control.

Each record is evaluated twice (pole_a-first and pole_b-first). Only consistent
judgments count; inconsistent pairs are ties. Uses sign test for significance.
Supports multiple style axes: formality (formal/casual), verbosity (verbose/concise).

Input:  verified.jsonl (all records, no filtering)
Output: pairwise_results.jsonl — per-record with trial1/trial2/consistent/pole_a_wins
        pairwise_summary.csv — aggregated stats
Deps:   openai (async client), asyncio, scipy
"""

import argparse
import asyncio
import csv
import json
import logging
import os
import re
import time

logger = logging.getLogger(__name__)

AXIS_CONFIG = {
    "formality": {"poles": ("formal", "casual"), "field": "original_formality"},
    "verbosity": {"poles": ("verbose", "concise"), "field": "original_verbosity"},
    "tone": {"poles": ("assertive", "hedging"), "field": "original_tone"},
    "rate_control": {"poles": ("original", "rewritten"), "field": "rate_role"},
    "register": {"poles": ("academic", "conversational"), "field": "original_register"},
}

PAIRWISE_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Compare the two responses below and pick the better one."
)

PAIRWISE_USER_TEMPLATE = """Instruction: {instruction}

Response A:
{response_a}

Response B:
{response_b}

Which response is better in terms of overall quality (helpfulness, accuracy, completeness, coherence)?
Output ONLY "A" or "B"."""


def parse_choice(text: str) -> str | None:
    text = text.strip().upper()
    if text in ("A", "B"):
        return text
    m = re.search(r"\b([AB])\b", text)
    return m.group(1) if m else None


class RateLimiter:
    def __init__(self, max_per_minute: int):
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


async def compare_one(
    client, model: str, instruction: str,
    response_a: str, response_b: str,
    limiter: RateLimiter, max_retries: int = 3,
) -> str | None:
    messages = [
        {"role": "system", "content": PAIRWISE_SYSTEM},
        {"role": "user", "content": PAIRWISE_USER_TEMPLATE.format(
            instruction=instruction, response_a=response_a, response_b=response_b
        )},
    ]
    for attempt in range(max_retries):
        await limiter.acquire()
        try:
            resp = await client.chat.completions.create(
                model=model, messages=messages, temperature=0.0, max_tokens=8,
            )
            text = resp.choices[0].message.content.strip()
            choice = parse_choice(text)
            if choice is not None:
                return choice
            logger.warning("Could not parse choice from '%s', retrying", text)
        except Exception as e:
            logger.warning("API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


async def score_record_dual(
    client, model: str, rec: dict,
    semaphore: asyncio.Semaphore, limiter: RateLimiter, max_retries: int,
    axis: str = "formality",
) -> dict:
    """Run two trials per record: pole_a-first and pole_b-first."""
    cfg = AXIS_CONFIG[axis]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]

    async with semaphore:
        instruction = rec["instruction"]
        original_pole = rec[field]

        if original_pole == pole_a:
            text_a = rec["original_text"]
            text_b = rec["counterfactual_text"]
        else:
            text_a = rec["counterfactual_text"]
            text_b = rec["original_text"]

        # Trial 1: A=pole_a, B=pole_b
        t1_raw = await compare_one(
            client, model, instruction, text_a, text_b, limiter, max_retries
        )
        t1_prefers_a = (t1_raw == "A") if t1_raw else None

        # Trial 2: A=pole_b, B=pole_a
        t2_raw = await compare_one(
            client, model, instruction, text_b, text_a, limiter, max_retries
        )
        t2_prefers_a = (t2_raw == "B") if t2_raw else None

        if t1_prefers_a is not None and t2_prefers_a is not None:
            consistent = (t1_prefers_a == t2_prefers_a)
            pole_a_wins = t1_prefers_a if consistent else None
        else:
            consistent = None
            pole_a_wins = None

        return {
            "id": rec["id"],
            "instruction": rec["instruction"],
            f"original_{axis}": original_pole,
            "nli_cf": rec.get("nli_cf"),
            "bertscore_cf": rec.get("bertscore_cf"),
            "trial1_choice": t1_raw,
            f"trial1_prefers_{pole_a}": t1_prefers_a,
            "trial2_choice": t2_raw,
            f"trial2_prefers_{pole_a}": t2_prefers_a,
            "consistent": consistent,
            f"{pole_a}_wins": pole_a_wins,
        }


def load_processed_ids(output_file: str) -> set[str]:
    ids = set()
    if os.path.exists(output_file):
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    ids.add(json.loads(line)["id"])
    return ids


async def run(args):
    api_key = [REDACTED] or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY or pass --api-key")

    from openai import AsyncOpenAI
    base_url = args.base_url or os.environ.get("OPENAI_BASE_URL")
    client = AsyncOpenAI(api_key=[REDACTED], base_url=base_url) if base_url else AsyncOpenAI(api_key=[REDACTED]

    with open(args.input_file) as f:
        records = [json.loads(line) for line in f if line.strip()]

    processed_ids = load_processed_ids(args.output_file)
    todo = [r for r in records if r["id"] not in processed_ids]
    logger.info("Total: %d, already done: %d, to score: %d", len(records), len(processed_ids), len(todo))

    if not todo:
        logger.info("Nothing to do")
        return

    semaphore = asyncio.Semaphore(args.max_concurrent)
    limiter = RateLimiter(args.rate_limit)

    tasks = [
        score_record_dual(client, args.model, rec, semaphore, limiter, args.retry, axis=args.axis)
        for rec in todo
    ]

    os.makedirs(os.path.dirname(args.output_file) or ".", exist_ok=True)

    with open(args.output_file, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            pole_a = AXIS_CONFIG[args.axis]["poles"][0]
            logger.info(
                "Compared %s: t1=%s t2=%s consistent=%s %s_wins=%s",
                result["id"], result["trial1_choice"], result["trial2_choice"],
                result["consistent"], pole_a, result.get(f"{pole_a}_wins"),
            )


def analyze(input_file: str, output_dir: str, axis: str = "formality"):
    from scipy import stats

    cfg = AXIS_CONFIG[axis]
    pole_a, pole_b = cfg["poles"]
    field = cfg["field"]
    wins_key = f"{pole_a}_wins"

    with open(input_file) as f:
        records = [json.loads(line) for line in f if line.strip()]

    total = len(records)
    valid = [r for r in records if r.get("trial1_choice") and r.get("trial2_choice")]
    consistent = [r for r in valid if r.get("consistent") is True]
    ties = [r for r in valid if r.get("consistent") is False]

    print(f"\n{'='*60}")
    print(f"  Pairwise Comparison (Position-Controlled) — {axis}")
    print(f"{'='*60}")
    print(f"  Total records: {total}")
    print(f"  Valid (both trials): {len(valid)}")
    print(f"  Consistent: {len(consistent)} ({len(consistent)/len(valid)*100:.1f}%)")
    print(f"  Ties (inconsistent): {len(ties)} ({len(ties)/len(valid)*100:.1f}%)")

    t1_a = sum(1 for r in valid if r["trial1_choice"] == "A")
    t2_a = sum(1 for r in valid if r["trial2_choice"] == "A")
    print(f"\n  Position bias:")
    print(f"    Trial 1 chose A: {t1_a}/{len(valid)} ({t1_a/len(valid)*100:.1f}%)")
    print(f"    Trial 2 chose A: {t2_a}/{len(valid)} ({t2_a/len(valid)*100:.1f}%)")
    total_a = t1_a + t2_a
    total_trials = 2 * len(valid)
    print(f"    Overall A rate: {total_a}/{total_trials} ({total_a/total_trials*100:.1f}%)")

    n_consistent = len(consistent)
    a_wins = sum(1 for r in consistent if r[wins_key] is True)
    b_wins = n_consistent - a_wins

    print(f"\n{'='*60}")
    print(f"  Overall Results (consistent pairs only)")
    print(f"{'='*60}")
    print(f"  N = {n_consistent}")
    print(f"  {pole_a} wins: {a_wins} ({a_wins/n_consistent*100:.1f}%)")
    print(f"  {pole_b} wins: {b_wins} ({b_wins/n_consistent*100:.1f}%)")

    sign_p = stats.binomtest(a_wins, n_consistent, 0.5).pvalue
    win_rate = a_wins / n_consistent
    z = 1.96
    denom = 1 + z**2 / n_consistent
    center = (win_rate + z**2 / (2 * n_consistent)) / denom
    spread = z * (win_rate * (1 - win_rate) / n_consistent + z**2 / (4 * n_consistent**2))**0.5 / denom
    ci_lo, ci_hi = max(0, center - spread), min(1, center + spread)

    print(f"  {pole_a} win rate: {win_rate:.4f}")
    print(f"  95% CI (Wilson): [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  Sign test p-value: {sign_p:.6f}")

    print(f"\n{'='*60}")
    print("  Directional Analysis (consistent only)")
    print(f"{'='*60}")
    dir_rows = []
    for direction in [pole_a, pole_b]:
        sub = [r for r in consistent if r.get(field) == direction]
        if not sub:
            continue
        ns = len(sub)
        fw = sum(1 for r in sub if r[wins_key] is True)
        wr = fw / ns if ns > 0 else 0
        bp = stats.binomtest(fw, ns, 0.5).pvalue
        target = pole_b if direction == pole_a else pole_a
        label = f"{direction}→{target}"
        print(f"\n  {label} (n={ns})")
        print(f"    {pole_a} wins: {fw} ({fw/ns*100:.1f}%), p={bp:.6f}")
        if direction == pole_a:
            print(f"    ({pole_a}=original, {pole_b}=rewrite → {pole_a} win = prefer original)")
        else:
            print(f"    ({pole_b}=original, {pole_a}=rewrite → {pole_a} win = prefer rewrite)")
        dir_rows.append({"group": label, "n": ns, f"{pole_a}_wins": fw,
                         "win_rate": wr, "p_value": bp})

    print(f"\n{'='*60}")
    print("  NLI-Stratified Analysis (consistent only)")
    print(f"{'='*60}")
    strat_rows = []
    for label, filt in [
        ("NLI≥0.90", lambda r: r.get("nli_cf", 0) >= 0.90),
        ("All", lambda r: True),
    ]:
        sub = [r for r in consistent if filt(r)]
        ns = len(sub)
        if ns == 0:
            continue
        fw = sum(1 for r in sub if r[wins_key] is True)
        wr = fw / ns
        bp = stats.binomtest(fw, ns, 0.5).pvalue
        print(f"  {label} (n={ns}): {pole_a} wins {fw} ({fw/ns*100:.1f}%), p={bp:.6f}")
        strat_rows.append({"group": label, "n": ns, f"{pole_a}_wins": fw,
                           "win_rate": wr, "p_value": bp})

    os.makedirs(output_dir, exist_ok=True)
    summary_rows = [
        {"group": "overall", "n": n_consistent, f"{pole_a}_wins": a_wins,
         f"{pole_b}_wins": b_wins, "win_rate": win_rate, "ci_lo": ci_lo,
         "ci_hi": ci_hi, "sign_test_p": sign_p, "ties": len(ties),
         "consistency_rate": len(consistent) / len(valid) if valid else 0,
         "position_a_rate": total_a / total_trials if total_trials else 0},
    ]
    csv_path = os.path.join(output_dir, "pairwise_summary.csv")
    fieldnames = list(summary_rows[0].keys())
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(summary_rows[0])
    print(f"\nSaved summary to {csv_path}")

    detail_path = os.path.join(output_dir, "pairwise_detailed.csv")
    detail_fields = ["group", "n", f"{pole_a}_wins", "win_rate", "p_value"]
    with open(detail_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=detail_fields)
        writer.writeheader()
        for row in dir_rows + strat_rows:
            writer.writerow(row)
    print(f"Saved detailed to {detail_path}")


def main():
    parser = argparse.ArgumentParser(description="Position-controlled pairwise comparison scoring")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--base-url", default="http://47.94.22.126/v1")
    parser.add_argument("--max-concurrent", type=int, default=5)
    parser.add_argument("--rate-limit", type=int, default=60)
    parser.add_argument("--retry", type=int, default=3)
    parser.add_argument("--analyze-only", action="store_true")
    parser.add_argument("--analysis-dir", default=None)
    parser.add_argument("--axis", default="formality", choices=list(AXIS_CONFIG.keys()),
                        help="Style axis (default: formality)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    if args.analyze_only:
        analysis_dir = args.analysis_dir or os.path.dirname(args.output_file) or "."
        analyze(args.output_file, analysis_dir, axis=args.axis)
    else:
        asyncio.run(run(args))
        analysis_dir = args.analysis_dir or os.path.dirname(args.output_file) or "."
        analyze(args.output_file, analysis_dir, axis=args.axis)


if __name__ == "__main__":
    main()
