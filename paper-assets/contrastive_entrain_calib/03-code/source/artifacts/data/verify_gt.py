#!/usr/bin/env python3
"""Verify ground truth labels for calibration_v2_1_expanded.jsonl using LLM."""
import asyncio
import json
import os
import sys
from pathlib import Path

import httpx

DATA_DIR = Path(__file__).parent
INPUT = DATA_DIR / "calibration_v2_1_expanded.jsonl"
OUTPUT = DATA_DIR / "calibration_v2_1_expanded_verified.jsonl"
ERRORS_LOG = DATA_DIR / "gt_verification_errors.json"

os.environ.update({
    "OPENAI_API_KEY": "[REDACTED]",
    "LLM_BASE_URL": "http://47.94.22.126/v1",
})

API_KEY = [REDACTED]"OPENAI_API_KEY"]
BASE_URL = os.environ["LLM_BASE_URL"]
MODEL = "gpt-4.1"
CONCURRENCY = 10


async def verify_one(client: httpx.AsyncClient, sem: asyncio.Semaphore,
                     pair_id: str, question: str, ground_truth: str, domain: str):
    prompt = (
        f"Domain: {domain}\n"
        f"Question: {question}\n"
        f"Claimed correct answer: {ground_truth}\n\n"
        f"Is the claimed correct answer actually correct? "
        f"Reply with exactly YES or NO on the first line, then a brief reason on the second line."
    )
    async with sem:
        for attempt in range(3):
            try:
                resp = await client.post(
                    f"{BASE_URL}/chat/completions",
                    json={
                        "model": MODEL,
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.0,
                        "max_tokens": 200,
                    },
                    headers={"Authorization": [REDACTED]"Bearer {API_KEY}"},
                    timeout=60.0,
                )
                resp.raise_for_status()
                text = resp.json()["choices"][0]["message"]["content"].strip()
                first_line = text.split("\n")[0].strip().upper()
                is_correct = first_line.startswith("YES")
                return {
                    "pair_id": pair_id,
                    "domain": domain,
                    "ground_truth": ground_truth,
                    "question_preview": question[:100],
                    "verdict": "YES" if is_correct else "NO",
                    "reason": text,
                }
            except Exception as e:
                if attempt == 2:
                    return {
                        "pair_id": pair_id,
                        "domain": domain,
                        "ground_truth": ground_truth,
                        "question_preview": question[:100],
                        "verdict": "ERROR",
                        "reason": str(e),
                    }
                await asyncio.sleep(2 ** attempt)


async def main():
    records = []
    with open(INPUT) as f:
        for line in f:
            records.append(json.loads(line))

    pairs = {}
    for r in records:
        if r["pair_id"] not in pairs:
            pairs[r["pair_id"]] = r

    print(f"Verifying {len(pairs)} pairs...")

    sem = asyncio.Semaphore(CONCURRENCY)
    async with httpx.AsyncClient() as client:
        tasks = []
        for pid, r in pairs.items():
            question = r["turns"][0]["content"]
            tasks.append(verify_one(client, sem, pid, question, r["ground_truth"], r["domain"]))
        results = await asyncio.gather(*tasks)

    verdict_map = {r["pair_id"]: r for r in results}
    errors = [r for r in results if r["verdict"] != "YES"]
    error_pids = {r["pair_id"] for r in errors if r["verdict"] == "NO"}

    print(f"\nResults: {sum(1 for r in results if r['verdict']=='YES')} correct, "
          f"{sum(1 for r in results if r['verdict']=='NO')} incorrect, "
          f"{sum(1 for r in results if r['verdict']=='ERROR')} errors")

    if errors:
        print("\nErrors/Incorrect:")
        for e in errors:
            print(f"  {e['pair_id']} ({e['domain']}): gt={e['ground_truth']}, verdict={e['verdict']}")
            print(f"    {e['reason'][:150]}")

    with open(ERRORS_LOG, "w") as f:
        json.dump(errors, f, indent=2, ensure_ascii=False)

    # Write verified output: keep all records, mark gt_verified, skip pairs with wrong GT
    kept = 0
    dropped = 0
    with open(OUTPUT, "w") as f:
        for r in records:
            pid = r["pair_id"]
            if pid in error_pids:
                dropped += 1
                continue
            v = verdict_map.get(pid, {})
            r["gt_verified"] = v.get("verdict", "UNKNOWN") == "YES"
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            kept += 1

    kept_pairs = kept // 2 if kept > 0 else 0
    dropped_pairs = dropped // 2 if dropped > 0 else 0
    print(f"\nOutput: {kept} records ({kept_pairs} pairs) kept, {dropped} records ({dropped_pairs} pairs) dropped")
    print(f"Saved to: {OUTPUT}")
    return len(errors), len(pairs)


if __name__ == "__main__":
    n_errors, n_total = asyncio.run(main())
    print(f"\nError rate: {n_errors}/{n_total} = {n_errors/n_total*100:.1f}%")
