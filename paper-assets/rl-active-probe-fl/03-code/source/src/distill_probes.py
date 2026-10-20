"""Distill diagnostic probes from Claude for each validated sample.

For each sample, generates:
  - good_probe: effective diagnostic code (1-5 lines of print/assert) that reveals the bug
  - bad_probe: plausible but unhelpful diagnostic code (negative example for GRPO)
  - probe_rationale: why good_probe works and bad_probe doesn't

Input: data/debugbench_validated.jsonl
Output: data/probes_distilled.jsonl
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

SYSTEM_PROMPT = """You are an expert debugger. Given buggy code and a bug description, generate diagnostic probes — small code snippets (print/assert statements) that a developer would insert into the buggy code to locate the bug.

You must output valid JSON with exactly these three fields:
{
  "good_probe": "...",
  "bad_probe": "...",
  "probe_rationale": "..."
}

Rules for good_probe:
- 1-5 lines of Python code (print statements, assert statements, or variable inspections)
- Must be insertable at a specific location in the buggy code
- When executed, the output should clearly reveal where/what the bug is
- Include a comment like `# INSERT AFTER LINE X` to indicate placement
- Focus on the variables/expressions most relevant to the bug

Rules for bad_probe:
- Also 1-5 lines that look reasonable but target the wrong area
- Should seem like a plausible debugging attempt but miss the actual bug
- Example: checking a variable that isn't involved in the bug, or checking at the wrong point

Rules for probe_rationale:
- 2-3 sentences explaining why good_probe reveals the bug and bad_probe misses it
- Reference specific variables or logic in the code"""

USER_PROMPT_TEMPLATE = """## Problem Description
{question}

## Buggy Code
```python
{buggy_code}
```

## Bug Explanation
{bug_explanation}

Generate diagnostic probes as JSON. Do NOT include the solution — the probes should help a developer find the bug through runtime inspection."""


def parse_json_response(text: str) -> Optional[dict]:
    """Extract JSON from Claude's response, handling markdown fences."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]  # skip ```json
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines)
    try:
        data = json.loads(text)
        if all(k in data for k in ("good_probe", "bad_probe", "probe_rationale")):
            return data
    except json.JSONDecodeError:
        pass

    import re

    match = re.search(r"\{[^{}]*\"good_probe\"[^{}]*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None


def generate_probes_for_sample(
    client: OpenAI,
    sample: dict,
    model: str,
) -> Optional[dict]:
    prompt = USER_PROMPT_TEMPLATE.format(
        question=sample["question"],
        buggy_code=sample["buggy_code"],
        bug_explanation=sample["bug_explanation"],
    )
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=2048,
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
            text = response.choices[0].message.content
            parsed = parse_json_response(text)
            if parsed is None:
                logger.warning(
                    f"Failed to parse JSON for {sample['slug']}: {text[:200]}"
                )
                if attempt < max_retries - 1:
                    continue
                return None
            return parsed
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
        description="Distill diagnostic probes using Claude API"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/debugbench_validated.jsonl",
        help="Input JSONL (validated samples)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/probes_distilled.jsonl",
        help="Output JSONL with probe fields",
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
            pool.submit(generate_probes_for_sample, client, s, args.model): s
            for s in todo
        }
        for i, future in enumerate(as_completed(future_to_sample), 1):
            sample = future_to_sample[future]
            probes = future.result()
            if probes is None:
                failed += 1
                continue
            sample_out = {**sample, **probes}
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
            entry["script"] = "distill_probes"
            f.write(json.dumps(entry) + "\n")

    total_input = sum(e["input_tokens"] for e in _cost_log)
    total_output = sum(e["output_tokens"] for e in _cost_log)

    print(f"\n=== Probe Distillation Complete ===")
    print(f"Processed: {len(results)}, Failed: {failed}, Total: {total_done}")
    print(f"Output: {output_path}")
    print(f"\n=== API Cost Summary ===")
    print(f"Requests: {len(_cost_log)}")
    print(f"Input tokens: {total_input:,}")
    print(f"Output tokens: {total_output:,}")
    print(f"Cost log: {cost_log_path}")


if __name__ == "__main__":
    main()
