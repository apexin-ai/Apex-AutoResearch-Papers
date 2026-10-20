"""Generate executable pytest test cases for DebugBench samples using Claude API.

Input: data/debugbench_python_single.jsonl
Output: data/debugbench_with_tests.jsonl (original fields + test_code)
Dependencies: openai
"""

import argparse
import json
import logging
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import openai
from openai import OpenAI

logger = logging.getLogger(__name__)

_cost_log: list[dict] = []
_cost_lock = threading.Lock()

SYSTEM_PROMPT = """You are an expert Python test engineer. Generate executable pytest test cases for the given LeetCode solution.

Rules:
1. Output ONLY valid Python code, no markdown fences or explanations.
2. Include all necessary imports (typing, collections, etc.) at the top.
3. Import or paste nothing from external files — the test must be self-contained.
4. The solution code uses `class Solution` with a method. Instantiate `Solution()` and call the method.
5. Write 3-6 test functions covering: provided examples, edge cases, and boundary conditions.
6. Each test function should be named `test_*` and use plain `assert` statements.
7. Do NOT import pytest fixtures or use parametrize — keep it simple.
8. Handle special types: ListNode, TreeNode — define them in the test file if needed.
9. The tests must pass when run against the provided correct solution.
10. Do NOT include the Solution class in your output. The solution code will be provided separately. Only write test functions that call `Solution().method_name()`."""

USER_PROMPT_TEMPLATE = """## Problem Description
{question}

## Examples
{examples}

## Constraints
{constraints}

## Correct Solution Code
```python
{solution}
```

Generate pytest test functions for this solution. Do NOT include the Solution class — it will be provided separately. Only write `def test_*` functions that call `Solution().method_name()`."""


def build_prompt(sample: dict) -> str:
    examples_text = "\n".join(sample.get("examples", []))
    return USER_PROMPT_TEMPLATE.format(
        question=sample["question"],
        examples=examples_text,
        constraints=sample.get("constraints", "N/A"),
        solution=sample["solution"],
    )


def generate_test_for_sample(
    client: OpenAI,
    sample: dict,
    model: str,
) -> Optional[str]:
    prompt = build_prompt(sample)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=4096,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
            )
            if response.usage:
                with _cost_lock:
                    _cost_log.append({
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "model": model,
                        "slug": sample["slug"],
                        "input_tokens": response.usage.prompt_tokens,
                        "output_tokens": response.usage.completion_tokens,
                    })
            return response.choices[0].message.content
        except openai.RateLimitError as e:
            wait = 2 ** (attempt + 2)
            logger.warning(f"Rate limited on {sample['slug']}, waiting {wait}s: {e}")
            time.sleep(wait)
        except openai.APIError as e:
            wait = 2 ** (attempt + 1)
            logger.warning(
                f"API error on {sample['slug']} (attempt {attempt+1}/{max_retries}): {e}"
            )
            time.sleep(wait)
    logger.error(f"Failed after {max_retries} retries: {sample['slug']}")
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate pytest test cases for DebugBench samples using Claude"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/debugbench_python_single.jsonl",
        help="Input JSONL from data_filter.py",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/debugbench_with_tests.jsonl",
        help="Output JSONL with test_code field",
    )
    parser.add_argument(
        "--max-workers", type=int, default=5, help="Concurrent API calls (default: 5)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="anthropic/claude-opus-4.7-fast",
        help="Claude model to use",
    )
    parser.add_argument(
        "--base-url",
        type=str,
        default="http://47.94.22.126/v1",
        help="OpenAI-compatible API base URL",
    )
    parser.add_argument(
        "--max-samples",
        type=int,
        default=None,
        help="Only process first N samples (for testing)",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    api_key = [REDACTED]"OPENROUTER_API_KEY")
    if not api_key:
        logger.error("OPENROUTER_API_KEY environment variable not set")
        raise SystemExit(1)

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    samples = []
    with open(input_path) as f:
        for line in f:
            samples.append(json.loads(line))
    logger.info(f"Loaded {len(samples)} samples from {input_path}")

    done_slugs: set[str] = set()
    existing_lines: list[str] = []
    if output_path.exists():
        with open(output_path) as f:
            for line in f:
                existing_lines.append(line)
                row = json.loads(line)
                done_slugs.add(row["slug"])
        logger.info(f"Resuming: {len(done_slugs)} already processed")

    todo = [s for s in samples if s["slug"] not in done_slugs]
    if args.max_samples is not None:
        todo = todo[: args.max_samples]
    logger.info(f"To process: {len(todo)} samples")
    if not todo:
        print("All samples already processed.")
        return

    client = OpenAI(api_key=[REDACTED], base_url=args.base_url)
    results: list[dict] = []
    failed = 0

    with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        future_to_sample = {
            pool.submit(generate_test_for_sample, client, s, args.model): s
            for s in todo
        }
        for i, future in enumerate(as_completed(future_to_sample), 1):
            sample = future_to_sample[future]
            test_code = future.result()
            if test_code is None:
                failed += 1
                continue
            sample_out = {**sample, "test_code": test_code}
            results.append(sample_out)
            if i % 10 == 0:
                logger.info(f"Progress: {i}/{len(todo)}")

    with open(output_path, "w") as f:
        for line in existing_lines:
            f.write(line)
        for row in results:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    total_done = len(done_slugs) + len(results)

    cost_log_path = Path("data/api_cost_log.jsonl")
    cost_log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cost_log_path, "a") as f:
        for entry in _cost_log:
            entry["script"] = "generate_tests"
            f.write(json.dumps(entry) + "\n")

    total_input = sum(e["input_tokens"] for e in _cost_log)
    total_output = sum(e["output_tokens"] for e in _cost_log)

    print(f"\n=== Test Generation Complete ===")
    print(f"Processed: {len(results)}, Failed: {failed}, Total: {total_done}")
    print(f"Output: {output_path}")
    print(f"\n=== API Cost Summary ===")
    print(f"Requests: {len(_cost_log)}")
    print(f"Input tokens: {total_input:,}")
    print(f"Output tokens: {total_output:,}")
    print(f"Cost log: {cost_log_path}")


if __name__ == "__main__":
    main()
