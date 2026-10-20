#!/usr/bin/env python3
"""LLM Verifier for NER candidate selection.
Sends each candidate entity list to Qwen3-8B for quality scoring.
"""
import asyncio
import json
import re
import argparse
import time
from pathlib import Path
from openai import AsyncOpenAI


VERIFY_PROMPT = """You are an expert scientific NER evaluator. Given a scientific text and a candidate list of extracted entities, score the extraction quality.

Valid entity types: Task, Method, Material, OtherScientificTerm, Metric, Generic

Text: {text}

Extracted entities:
{entities_formatted}

Score each dimension from 0 to 10:
- precision_score: How many extracted entities are correct and properly typed? (10 = all correct, 0 = all wrong)
- recall_score: How many important entities in the text are captured? (10 = nothing missed, 0 = everything missed)
- overall_score: Overall extraction quality considering both dimensions.

Output ONLY a JSON object, no other text:
{{"precision_score": <int>, "recall_score": <int>, "overall_score": <int>}}"""


def strip_think_tags(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()


def parse_verify_response(raw_text):
    text = strip_think_tags(raw_text)
    try:
        match = re.search(r'\{[^{}]*\}', text)
        if match:
            obj = json.loads(match.group())
            return {
                "precision_score": float(obj.get("precision_score", 0)),
                "recall_score": float(obj.get("recall_score", 0)),
                "overall_score": float(obj.get("overall_score", 0)),
                "parse_success": True,
            }
    except (json.JSONDecodeError, ValueError):
        pass
    scores = {}
    for key in ["precision_score", "recall_score", "overall_score"]:
        m = re.search(rf'"{key}"\s*:\s*(\d+(?:\.\d+)?)', text)
        if m:
            scores[key] = float(m.group(1))
    if "overall_score" in scores:
        return {
            "precision_score": scores.get("precision_score", 0),
            "recall_score": scores.get("recall_score", 0),
            "overall_score": scores["overall_score"],
            "parse_success": True,
        }
    return {"precision_score": 0, "recall_score": 0, "overall_score": 0, "parse_success": False}


async def verify_one(client, model, text, entities, semaphore):
    if not entities:
        entities_formatted = "(no entities extracted)"
    else:
        entities_formatted = "\n".join(
            f'  - "{e["text"]}" [{e["type"]}]' for e in entities
        )
    prompt = VERIFY_PROMPT.format(text=text, entities_formatted=entities_formatted)

    async with semaphore:
        try:
            resp = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=200,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            )
            raw = resp.choices[0].message.content or ""
            result = parse_verify_response(raw)
            result["raw_response"] = raw
            return result
        except Exception as e:
            err = str(e)
            if "chat_template_kwargs" in err or "extra_body" in err:
                try:
                    resp = await client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0,
                        max_tokens=200,
                    )
                    raw = resp.choices[0].message.content or ""
                    result = parse_verify_response(raw)
                    result["raw_response"] = raw
                    return result
                except Exception as e2:
                    err = str(e2)
            return {
                "precision_score": 0, "recall_score": 0, "overall_score": 0,
                "parse_success": False, "error": err, "raw_response": "",
            }


async def process_file(results_file, gold_texts, port, model, output_dir, max_concurrent=16):
    client = AsyncOpenAI(base_url=f"http://localhost:{port}/v1", api_key="[REDACTED]")
    semaphore = asyncio.Semaphore(max_concurrent)

    docs = []
    with open(results_file) as f:
        for line in f:
            docs.append(json.loads(line.strip()))

    output_file = Path(output_dir) / f"verify_{Path(results_file).name}"

    tasks = []
    task_info = []
    for di, doc in enumerate(docs):
        text = gold_texts.get(doc["doc_key"], "")
        for ci, cand in enumerate(doc["candidates"]):
            entities = cand.get("entities", [])
            tasks.append(verify_one(client, model, text, entities, semaphore))
            task_info.append((di, ci))

    total = len(tasks)
    print(f"  [{Path(results_file).name}] {total} candidates from {len(docs)} docs -> port {port}")
    verify_results = await asyncio.gather(*tasks)

    doc_verify = {i: {} for i in range(len(docs))}
    for (di, ci), vr in zip(task_info, verify_results):
        doc_verify[di][ci] = vr

    parse_ok = 0
    parse_total = 0
    with open(output_file, 'w') as f:
        for di, doc in enumerate(docs):
            n_cands = len(doc["candidates"])
            scores = []
            for ci in range(n_cands):
                vr = doc_verify[di].get(ci, {})
                scores.append(vr)
                parse_total += 1
                if vr.get("parse_success"):
                    parse_ok += 1
            overall_scores = [s.get("overall_score", 0) for s in scores]
            best_idx = max(range(len(overall_scores)), key=lambda i: overall_scores[i])
            out = {
                "doc_key": doc["doc_key"],
                "n_candidates": doc["n_candidates"],
                "seed": doc["seed"],
                "verify_scores": [{k: v for k, v in s.items() if k != "raw_response"}
                                  for s in scores],
                "verify_raw": [s.get("raw_response", "") for s in scores],
                "best_candidate_idx": best_idx,
                "best_overall_score": overall_scores[best_idx],
            }
            f.write(json.dumps(out) + "\n")

    print(f"  [{Path(results_file).name}] parse {parse_ok}/{parse_total} -> {output_file.name}")
    return parse_ok, parse_total


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results_file", required=True)
    parser.add_argument("--gold_file", required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--model", default="/root/autodl-tmp/models/Qwen/Qwen3-8B")
    parser.add_argument("--output_dir", default="verify_results")
    parser.add_argument("--max_concurrent", type=int, default=16)
    args = parser.parse_args()

    Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    gold_texts = {}
    with open(args.gold_file) as f:
        for line in f:
            doc = json.loads(line.strip())
            gold_texts[doc["doc_key"]] = doc["text"]
    print(f"Loaded {len(gold_texts)} gold docs")

    t0 = time.time()
    ok, total = await process_file(
        args.results_file, gold_texts, args.port, args.model,
        args.output_dir, args.max_concurrent,
    )
    elapsed = time.time() - t0
    print(f"Done: {ok}/{total} parsed, {elapsed:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())
