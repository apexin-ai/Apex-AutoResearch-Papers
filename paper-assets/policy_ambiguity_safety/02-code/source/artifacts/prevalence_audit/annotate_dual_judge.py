#!/usr/bin/env python3
"""Dual-judge ambiguity annotation with async concurrency.

Both judges use the OpenAI-compatible API (OpenRouter).
Claude Sonnet 4.6 via proxy, GPT-5.4 via OpenRouter official.
"""

import asyncio
import json
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
CLAUSES_FILE = BASE_DIR / "clauses.jsonl"
CLAUDE_OUT = BASE_DIR / "annotations_claude.jsonl"
GPT_OUT = BASE_DIR / "annotations_gpt.jsonl"

CONCURRENCY = 25

AMBIGUITY_TYPES = [
    "scopal", "lexical", "coreferential",
    "incompleteness", "authorization_scope", "conditional_precedence",
]

PROMPT_TEMPLATE = """Given this policy clause from a {domain} company's {doc_type} document:
"{clause_text}"

Context: {context_sentence}

1. Is this clause ambiguous in a way that could cause an LLM agent to misinterpret the intended policy? (yes/no)
2. If yes, which ambiguity type best describes it? Choose from: scopal, lexical, coreferential, incompleteness, authorization_scope, conditional_precedence
3. Brief justification (1-2 sentences).

Respond in JSON: {{"is_ambiguous": bool, "ambiguity_type": "...", "justification": "..."}}"""

SYSTEM_MSG = (
    "You are an expert annotator for policy ambiguity analysis. "
    "Classify whether policy clauses contain ambiguity that could lead an LLM agent "
    "to misinterpret the intended policy. Be precise and conservative — only mark "
    "genuinely ambiguous clauses, not merely complex ones. "
    "Respond with valid JSON only, no markdown fencing."
)


def parse_json_response(text):
    if text is None:
        return None
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
        if match:
            obj = json.loads(match.group())
        else:
            return None

    is_amb = obj.get("is_ambiguous", False)
    if isinstance(is_amb, str):
        is_amb = is_amb.lower() in ("true", "yes", "1")
    amb_type = obj.get("ambiguity_type", "none")
    if not is_amb:
        amb_type = "none"
    if amb_type not in AMBIGUITY_TYPES and amb_type != "none":
        amb_type = "none"

    return {
        "is_ambiguous": bool(is_amb),
        "ambiguity_type": amb_type,
        "justification": obj.get("justification", ""),
    }


async def call_openai_async(client, model, clause, judge_name, semaphore):
    prompt = PROMPT_TEMPLATE.format(**clause)
    async with semaphore:
        try:
            resp = await asyncio.to_thread(
                client.chat.completions.create,
                model=model,
                max_tokens=300,
                messages=[
                    {"role": "system", "content": SYSTEM_MSG},
                    {"role": "user", "content": prompt},
                ],
            )
            raw = resp.choices[0].message.content
            parsed = parse_json_response(raw)
            if parsed is None:
                parsed = {"is_ambiguous": False, "ambiguity_type": "none",
                          "justification": f"PARSE_ERROR: {raw[:200] if raw else 'None'}"}
            return {"clause_id": clause["clause_id"], "doc_id": clause["doc_id"],
                    "judge": judge_name, **parsed}
        except Exception as e:
            return {"clause_id": clause["clause_id"], "doc_id": clause["doc_id"],
                    "judge": judge_name, "is_ambiguous": False,
                    "ambiguity_type": "none",
                    "justification": f"API_ERROR: {str(e)[:200]}"}


async def run_judge(clauses, client, model, judge_name, output_path):
    semaphore = asyncio.Semaphore(CONCURRENCY)
    tasks = [call_openai_async(client, model, c, judge_name, semaphore) for c in clauses]

    results = []
    done = 0
    for coro in asyncio.as_completed(tasks):
        result = await coro
        results.append(result)
        done += 1
        if done % 50 == 0:
            errs = sum(1 for r in results if "API_ERROR" in r.get("justification", ""))
            print(f"  {judge_name}: {done}/{len(clauses)} (errors: {errs})")

    id_order = {c["clause_id"]: i for i, c in enumerate(clauses)}
    results.sort(key=lambda r: id_order.get(r["clause_id"], 0))

    with open(output_path, "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    errs = sum(1 for r in results if "API_ERROR" in r.get("justification", ""))
    print(f"  {judge_name}: {len(results)}/{len(clauses)} done, {errs} errors -> {output_path}")
    return results


async def main():
    from openai import OpenAI

    clauses = []
    with open(CLAUSES_FILE) as f:
        for line in f:
            clauses.append(json.loads(line))
    print(f"Loaded {len(clauses)} clauses")

    claude_key = os.environ.get("ANTHROPIC_API_KEY")
    claude_base = os.environ.get("ANTHROPIC_BASE_URL", "http://47.94.22.126/v1")
    claude_model = os.environ.get("CLAUDE_MODEL", "anthropic/claude-sonnet-4-6")

    gpt_key = os.environ.get("OPENAI_API_KEY")
    gpt_base = os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
    gpt_model = os.environ.get("GPT_MODEL", "openai/gpt-5.4")

    if not claude_key:
        print("ERROR: Set ANTHROPIC_API_KEY"); sys.exit(1)
    if not gpt_key:
        print("ERROR: Set OPENAI_API_KEY"); sys.exit(1)

    claude_client = OpenAI(api_key=[REDACTED], base_url=claude_base)
    gpt_client = OpenAI(api_key=[REDACTED], base_url=gpt_base)

    print(f"Running both judges concurrently ({CONCURRENCY} parallel per judge)...")
    print(f"  Claude: {claude_model} @ {claude_base}")
    print(f"  GPT: {gpt_model} @ {gpt_base}")

    claude_task = run_judge(clauses, claude_client, claude_model, "claude", CLAUDE_OUT)
    gpt_task = run_judge(clauses, gpt_client, gpt_model, "gpt", GPT_OUT)

    await asyncio.gather(claude_task, gpt_task)
    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
