"""LLM judge scoring via GPT-4o (async, rate-limited).

Input:  verified.jsonl (records that passed content verification)
Output: scored.jsonl — adds score_original, score_counterfactual, score_double_rewrite
Deps:   openai (async client), asyncio
"""

import argparse
import asyncio
import json
import logging
import os
import re
import time

logger = logging.getLogger(__name__)

JUDGE_SYSTEM = (
    "You are an expert evaluator of AI assistant responses. "
    "Rate the quality of the following response to the given instruction."
)

JUDGE_USER_TEMPLATE = """Instruction: {instruction}
Response: {response}

Evaluate the overall quality of this response based on helpfulness, accuracy, completeness, and coherence. Rate on a scale of 1-10, where:
1-2: Completely inadequate
3-4: Poor quality with major issues
5-6: Acceptable but with notable weaknesses
7-8: Good quality with minor issues
9-10: Excellent quality

Provide your rating as a single integer. Output ONLY the number, nothing else."""


def parse_score(text: str) -> int | None:
    text = text.strip()
    m = re.search(r"\b(10|[1-9])\b", text)
    if m:
        return int(m.group(1))
    return None


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


async def score_one(
    client,
    model: str,
    instruction: str,
    response: str,
    limiter: RateLimiter,
    max_retries: int = 3,
) -> int | None:
    messages = [
        {"role": "system", "content": JUDGE_SYSTEM},
        {"role": "user", "content": JUDGE_USER_TEMPLATE.format(instruction=instruction, response=response)},
    ]
    for attempt in range(max_retries):
        await limiter.acquire()
        try:
            resp = await client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
                max_tokens=16,
            )
            text = resp.choices[0].message.content.strip()
            score = parse_score(text)
            if score is not None:
                return score
            logger.warning("Could not parse score from '%s', retrying", text)
        except Exception as e:
            logger.warning("API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                await asyncio.sleep(2 ** attempt)
    return None


async def score_record(
    client,
    model: str,
    rec: dict,
    semaphore: asyncio.Semaphore,
    limiter: RateLimiter,
    max_retries: int,
) -> dict:
    async with semaphore:
        instruction = rec["instruction"]
        s_orig = await score_one(client, model, instruction, rec["original_text"], limiter, max_retries)
        s_cf = await score_one(client, model, instruction, rec["counterfactual_text"], limiter, max_retries)
        s_dr = await score_one(client, model, instruction, rec["double_rewrite_text"], limiter, max_retries)
        return {
            **rec,
            "score_original": s_orig,
            "score_counterfactual": s_cf,
            "score_double_rewrite": s_dr,
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
    logger.info("Total: %d, already scored: %d, to score: %d", len(records), len(processed_ids), len(todo))

    if not todo:
        logger.info("Nothing to do")
        return

    semaphore = asyncio.Semaphore(args.max_concurrent)
    limiter = RateLimiter(args.rate_limit)

    tasks = [
        score_record(client, args.model, rec, semaphore, limiter, args.retry)
        for rec in todo
    ]

    os.makedirs(os.path.dirname(args.output_file) or ".", exist_ok=True)

    with open(args.output_file, "a") as fout:
        for coro in asyncio.as_completed(tasks):
            result = await coro
            fout.write(json.dumps(result, ensure_ascii=False) + "\n")
            fout.flush()
            logger.info(
                "Scored %s: orig=%s cf=%s dr=%s",
                result["id"],
                result["score_original"],
                result["score_counterfactual"],
                result["score_double_rewrite"],
            )


def main():
    parser = argparse.ArgumentParser(description="LLM judge scoring with GPT-4o")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--api-key", default=None, help="OpenAI API key (or set OPENAI_API_KEY)")
    parser.add_argument("--base-url", default="http://47.94.22.126/v1", help="OpenAI-compatible API base URL")
    parser.add_argument("--max-concurrent", type=int, default=5)
    parser.add_argument("--rate-limit", type=int, default=60, help="Max requests per minute")
    parser.add_argument("--retry", type=int, default=3)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
