#!/usr/bin/env python3
"""Sequential self-refinement for NER.
Each round takes the previous round's output and asks the model to check and correct.
"""
import argparse
import json
import re
import time
from pathlib import Path
from openai import OpenAI

SYSTEM_PROMPT = """You are a scientific information extraction system. Given a scientific text, extract ALL named entities and classify each one.

Entity types:
- Task: Research tasks, problems, applications (e.g., "machine translation", "named entity recognition")
- Method: Approaches, algorithms, models, systems (e.g., "neural network", "SVM", "our model")
- Material: Data, corpora, resources, languages (e.g., "Penn Treebank", "English text")
- OtherScientificTerm: Scientific concepts, terms, phenomena (e.g., "word embeddings", "parse trees")
- Metric: Evaluation measures (e.g., "F1 score", "BLEU", "accuracy")
- Generic: Pronouns or general references to other entities (e.g., "it", "this method", "these")

IMPORTANT:
- Extract entity text EXACTLY as it appears in the input text
- Output ONLY a JSON array, nothing else
- Format: [{"text": "exact entity text", "type": "EntityType"}, ...]
- If no entities found, output: []"""

USER_TEMPLATE = "Extract all scientific entities from this text:\n\n{text}"

REFINE_SYSTEM = """You are a scientific named entity recognition expert. You will be given a scientific text and a previous NER extraction result.
Your task is to carefully review the extraction, correct any errors, and add any missing entities.

Entity types: Task, Method, Material, OtherScientificTerm, Metric, Generic

Rules:
- Fix entity boundaries (e.g., "neural" should be "neural network")
- Fix entity types if misclassified
- Add entities that were missed
- Remove entities that are not actually scientific entities
- Keep correct entities unchanged
- Extract entity text EXACTLY as it appears in the input text

Output ONLY a JSON array of the complete corrected entity list, nothing else.
Format: [{"text": "exact entity text", "type": "EntityType"}, ...]"""

SEED_SUFFIXES = {
    42: "",
    123: "\nPay special attention to entity boundaries and ensure each entity span exactly matches the text.",
    456: "\nFocus on recall — make sure no scientific concepts are missed, even if they seem minor.",
}


def refine_user_prompt(text, prev_entities, seed):
    entity_str = json.dumps(prev_entities, indent=2)
    suffix = SEED_SUFFIXES.get(seed, "")
    return f"""Scientific text:
{text}

Previous extraction result:
{entity_str}

Please review and correct the above extraction. Output the complete corrected entity list as a JSON array.{suffix}"""


def parse_entities(response_text):
    text = response_text.strip()
    think_end = text.find("</think>")
    if think_end != -1:
        text = text[think_end + 8:].strip()
    try:
        entities = json.loads(text)
        if isinstance(entities, list):
            return [e for e in entities if isinstance(e, dict) and "text" in e and "type" in e], True
    except json.JSONDecodeError:
        pass
    match = re.search(r'```(?:json)?\s*(\[.*?\])\s*```', text, re.DOTALL)
    if match:
        try:
            entities = json.loads(match.group(1))
            if isinstance(entities, list):
                return [e for e in entities if isinstance(e, dict) and "text" in e and "type" in e], True
        except json.JSONDecodeError:
            pass
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        try:
            entities = json.loads(match.group(0))
            if isinstance(entities, list):
                return [e for e in entities if isinstance(e, dict) and "text" in e and "type" in e], True
        except json.JSONDecodeError:
            pass
    return [], False


def call_llm(client, model, messages, temperature=0.0):
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=2048,
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
        )
        return resp.choices[0].message.content or ""
    except Exception as e:
        if "chat_template_kwargs" in str(e) or "extra_body" in str(e):
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=2048,
            )
            return resp.choices[0].message.content or ""
        raise


def run_round1(client, model, doc):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_TEMPLATE.format(text=doc["text"])},
    ]
    raw = call_llm(client, model, messages, temperature=0.0)
    entities, parse_ok = parse_entities(raw)
    return entities, parse_ok, raw


def run_refinement(client, model, doc, prev_entities, seed):
    messages = [
        {"role": "system", "content": REFINE_SYSTEM},
        {"role": "user", "content": refine_user_prompt(doc["text"], prev_entities, seed)},
    ]
    raw = call_llm(client, model, messages, temperature=0.0)
    entities, parse_ok = parse_entities(raw)
    return entities, parse_ok, raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard_file", required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--round", type=int, required=True, help="Which round to run (1-4)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", default="seq_results")
    parser.add_argument("--prev_round_dir", default=None, help="Dir with round K-1 results (required for round>=2)")
    parser.add_argument("--model_name", default="/root/autodl-tmp/models/Qwen/Qwen3-8B")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    shard_name = Path(args.shard_file).stem
    shard_id = shard_name.split("_")[-1]
    out_file = output_dir / f"seq_shard{shard_id}_round{args.round}_seed{args.seed}.jsonl"

    docs = []
    with open(args.shard_file) as f:
        for line in f:
            docs.append(json.loads(line.strip()))

    prev_entities_map = {}
    if args.round >= 2:
        prev_file = Path(args.prev_round_dir) / f"seq_shard{shard_id}_round{args.round - 1}_seed{args.seed}.jsonl"
        if not prev_file.exists():
            print(f"ERROR: Previous round file not found: {prev_file}")
            return
        with open(prev_file) as f:
            for line in f:
                rec = json.loads(line.strip())
                prev_entities_map[rec["doc_key"]] = rec["entities"]
        print(f"Loaded {len(prev_entities_map)} prev results from {prev_file}")

    client = OpenAI(base_url=f"http://localhost:{args.port}/v1", api_key="[REDACTED]")
    print(f"Round {args.round}, seed={args.seed}, shard={shard_name}, {len(docs)} docs, port={args.port}")

    results = []
    parse_ok_count = 0
    t_start = time.time()

    for i, doc in enumerate(docs):
        t0 = time.time()
        if args.round == 1:
            entities, parse_ok, raw = run_round1(client, args.model_name, doc)
        else:
            prev_ents = prev_entities_map.get(doc["doc_key"], [])
            entities, parse_ok, raw = run_refinement(client, args.model_name, doc, prev_ents, args.seed)
            if not parse_ok:
                entities = prev_ents
        elapsed = time.time() - t0

        if parse_ok:
            parse_ok_count += 1

        results.append({
            "doc_key": doc["doc_key"],
            "text": doc["text"],
            "round": args.round,
            "seed": args.seed,
            "entities": entities,
            "parse_success": parse_ok,
        })

        if (i + 1) % 5 == 0 or i == len(docs) - 1:
            print(f"  [{i+1}/{len(docs)}] parse={parse_ok_count}/{i+1} last={elapsed:.1f}s")

    with open(out_file, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    total_time = time.time() - t_start
    print(f"Done round {args.round} seed {args.seed} shard {shard_id}: {parse_ok_count}/{len(docs)} parsed, {total_time:.1f}s -> {out_file}")


if __name__ == "__main__":
    main()
