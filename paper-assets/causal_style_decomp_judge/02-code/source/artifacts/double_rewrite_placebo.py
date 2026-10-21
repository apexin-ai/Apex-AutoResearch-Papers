"""Double-rewrite placebo pairwise comparison.

Compares original_text vs double_rewrite_text using the same pairwise prompt
as the main experiment. If BT ≈ 50%, rewriting artifacts don't create bias.
"""

import argparse
import asyncio
import json
import logging
import re
import time
import numpy as np
from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

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


def parse_choice(text: str):
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


async def compare_one(client, model, instruction, response_a, response_b, limiter, max_retries=3):
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
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
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


async def run_axis(client, model, data, axis, limiter, semaphore):
    results = []
    tasks = []

    for rec in data:
        rec_id = rec["id"]
        instruction = rec["instruction"]
        original = rec["original_text"]
        double_rewrite = rec["double_rewrite_text"]

        async def do_pair(rid, inst, orig, dr):
            async with semaphore:
                t1 = await compare_one(client, model, inst, orig, dr, limiter)
                t2 = await compare_one(client, model, inst, dr, orig, limiter)

                if t1 is None or t2 is None:
                    return {"id": rid, "trial1": t1, "trial2": t2, "consistent": False, "original_wins": None}

                # trial1: A=original, B=dr → "A" means original wins
                # trial2: A=dr, B=original → "B" means original wins
                orig_wins_t1 = (t1 == "A")
                orig_wins_t2 = (t2 == "B")
                consistent = (orig_wins_t1 == orig_wins_t2)

                return {
                    "id": rid,
                    "trial1": t1,
                    "trial2": t2,
                    "consistent": consistent,
                    "original_wins": orig_wins_t1 if consistent else None,
                }

        tasks.append(do_pair(rec_id, instruction, original, double_rewrite))

    results = await asyncio.gather(*tasks)
    return list(results)


def bootstrap_ci(wins, n, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    rates = []
    for _ in range(n_boot):
        sample = rng.binomial(1, wins / n, size=n)
        rates.append(sample.mean())
    lo, hi = np.percentile(rates, [2.5, 97.5])
    return float(lo), float(hi)


def analyze_results(results, axis_name):
    consistent = [r for r in results if r["consistent"]]
    n_total = len(results)
    n_consistent = len(consistent)

    if n_consistent == 0:
        return {"axis": axis_name, "n_pairs": n_total, "n_consistent": 0, "error": "no consistent pairs"}

    original_wins = sum(1 for r in consistent if r["original_wins"])
    dr_wins = n_consistent - original_wins
    win_rate = original_wins / n_consistent

    ci_lo, ci_hi = bootstrap_ci(original_wins, n_consistent)

    from scipy import stats
    p_value = float(stats.binomtest(original_wins, n_consistent, 0.5).pvalue)

    conclusion = "BT ≈ 50%, no rewriting artifact bias" if p_value > 0.05 else "BT significantly deviates from 50%"

    return {
        "n_pairs": n_total,
        "n_consistent": n_consistent,
        "consistency_rate": round(n_consistent / n_total, 4),
        "bt_original_wins": original_wins,
        "bt_dr_wins": dr_wins,
        "bt_win_rate": round(win_rate, 4),
        "ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "p_value": round(p_value, 6),
        "conclusion": conclusion,
    }


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8002/v1")
    parser.add_argument("--model", default="/root/autodl-tmp/models/Qwen3-32B")
    parser.add_argument("--data-dir", default="/root/causal_style_decomp_judge/data")
    parser.add_argument("--output", default="/root/causal_style_decomp_judge/data/double_rewrite_placebo_qwen32b.json")
    parser.add_argument("--max-concurrent", type=int, default=8)
    parser.add_argument("--rate-limit", type=int, default=120)
    parser.add_argument("--nli-threshold", type=float, default=0.90)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    client = AsyncOpenAI(base_url=args.base_url, api_key="[REDACTED]")
    limiter = RateLimiter(args.rate_limit)
    semaphore = asyncio.Semaphore(args.max_concurrent)

    output = {"judge": "Qwen3-32B"}

    for axis, fname, field in [
        ("formality", "verified_32b.jsonl", "original_formality"),
        ("verbosity", "verified_verbosity.jsonl", "original_verbosity"),
    ]:
        path = f"{args.data_dir}/{fname}"
        with open(path) as f:
            data = [json.loads(line) for line in f]

        filtered = [r for r in data if r.get("nli_dr", 0) >= args.nli_threshold]
        logger.info("%s: %d/%d pairs pass nli_dr >= %.2f", axis, len(filtered), len(data), args.nli_threshold)

        if not filtered:
            output[axis] = {"error": "no pairs pass NLI threshold"}
            continue

        results = await run_axis(client, args.model, filtered, axis, limiter, semaphore)
        analysis = analyze_results(results, axis)
        output[axis] = analysis

        logger.info("%s: win_rate=%.4f, p=%.6f, n_consistent=%d",
                     axis, analysis.get("bt_win_rate", 0), analysis.get("p_value", 1), analysis.get("n_consistent", 0))

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    logger.info("Saved results to %s", args.output)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
