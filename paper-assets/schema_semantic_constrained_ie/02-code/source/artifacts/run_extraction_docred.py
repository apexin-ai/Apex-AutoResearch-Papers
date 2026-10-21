"""
Run zero-shot document-level relation extraction on DocRED using Qwen3-8B.

Input:  data/docred/dev.json, data/docred/rel_info.json
Output: outputs/raw_outputs_docred.jsonl

Each document is fed to the model with the full entity type list and
relation type list. The model outputs structured JSON with entities
and relations. Uses /no_think mode for Qwen3.
"""

import json
import argparse
import re
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


ENTITY_TYPES = ["PER", "ORG", "LOC", "TIME", "NUM", "MISC"]


def load_relation_names(rel_info_path: str) -> dict:
    with open(rel_info_path) as f:
        return json.load(f)


def build_relation_list_str(rel_info: dict) -> str:
    """Format relation types as a compact list for the prompt."""
    lines = [f"- {name}" for _, name in sorted(rel_info.items(), key=lambda x: x[1])]
    return "\n".join(lines)


def doc_to_text(doc: dict) -> str:
    """Concatenate all sentences in a DocRED document into plain text."""
    return " ".join(" ".join(sent) for sent in doc["sents"])


def build_prompt(document_text: str, relation_list_str: str) -> str:
    return f"""You are an information extraction system. Extract all entities and relations from the following document.

Entity types: {", ".join(ENTITY_TYPES)}

Relation types:
{relation_list_str}

Document:
{document_text}

Output a JSON object with exactly this structure:
{{"entities": [{{"text": "entity name", "type": "ENTITY_TYPE"}}], "relations": [{{"head": "head entity", "tail": "tail entity", "type": "relation name", "head_type": "ENTITY_TYPE", "tail_type": "ENTITY_TYPE"}}]}}

Output ONLY the JSON, no other text."""


def extract_gold(doc: dict) -> tuple[list[dict], list[dict]]:
    """Extract gold entities and relations from a DocRED document."""
    vertex_set = doc["vertexSet"]

    gold_entities = []
    entity_names = {}
    for i, vs in enumerate(vertex_set):
        name = vs[0]["name"]
        etype = vs[0].get("type", "UNK")
        gold_entities.append({"text": name, "type": etype, "index": i})
        entity_names[i] = name

    gold_relations = []
    for label in doc.get("labels", []):
        h_name = entity_names.get(label["h"], f"entity_{label['h']}")
        t_name = entity_names.get(label["t"], f"entity_{label['t']}")
        h_type = vertex_set[label["h"]][0].get("type", "UNK")
        t_type = vertex_set[label["t"]][0].get("type", "UNK")
        gold_relations.append({
            "head": h_name,
            "tail": t_name,
            "type": label["r"],
            "head_type": h_type,
            "tail_type": t_type,
        })

    return gold_entities, gold_relations


def parse_model_output(raw: str) -> dict | None:
    """Try to parse JSON from model output, with fallbacks for common issues."""
    # Strip markdown code fences
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)

    # Try direct parse
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Try extracting first JSON object
    match = re.search(r"\{[\s\S]*\}", cleaned)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default=None,
                        help="Path to Qwen3-8B model. Auto-detected if not set.")
    parser.add_argument("--data_path", type=str, default="data/docred/dev.json")
    parser.add_argument("--rel_info_path", type=str, default="data/docred/rel_info.json")
    parser.add_argument("--output_path", type=str, default="outputs/raw_outputs_docred.jsonl")
    parser.add_argument("--constraints_path", type=str, default=None)
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--device", type=str, default="cuda:1")
    parser.add_argument("--max_new_tokens", type=int, default=2048)
    args = parser.parse_args()

    # Auto-detect model path
    model_path = args.model_path
    if model_path is None:
        for candidate in ["/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B",
                          "/root/models/Qwen3-8B",
                          "/root/models/Qwen3-8B-ms"]:
            if Path(candidate).exists():
                model_path = candidate
                break
    if model_path is None:
        raise FileNotFoundError("Qwen3-8B model not found. Specify --model_path.")
    print(f"Model: {model_path}")
    print(f"Device: {args.device}")

    # Load data
    with open(args.data_path) as f:
        data = json.load(f)
    rel_info = load_relation_names(args.rel_info_path)
    relation_list_str = build_relation_list_str(rel_info)

    if args.max_samples:
        data = data[:args.max_samples]
    print(f"Processing {len(data)} documents")

    # Load model
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map=args.device,
        trust_remote_code=True,
    )
    model.eval()
    print("Model loaded")

    # Process documents
    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    parse_success = 0
    parse_fail = 0

    with open(args.output_path, "w") as fout:
        for i, doc in enumerate(data):
            doc_text = doc_to_text(doc)
            gold_entities, gold_relations = extract_gold(doc)

            prompt = build_prompt(doc_text, relation_list_str)

            # Qwen3 chat format with /no_think
            messages = [
                {"role": "user", "content": prompt},
            ]
            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False,
            )

            inputs = tokenizer(text, return_tensors="pt").to(model.device)
            input_len = inputs["input_ids"].shape[1]

            t0 = time.time()
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=args.max_new_tokens,
                    do_sample=False,
                    temperature=1.0,
                    top_p=1.0,
                )
            elapsed = time.time() - t0

            generated = outputs[0][input_len:]
            raw_output = tokenizer.decode(generated, skip_special_tokens=True)
            parsed = parse_model_output(raw_output)

            if parsed is not None:
                parse_success += 1
            else:
                parse_fail += 1

            record = {
                "doc_id": doc.get("title", f"doc_{i}"),
                "document": doc_text,
                "gold_entities": gold_entities,
                "gold_relations": gold_relations,
                "model_output": raw_output,
                "parsed_output": parsed,
                "input_tokens": input_len,
                "elapsed_seconds": round(elapsed, 2),
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")

            status = "OK" if parsed else "PARSE_FAIL"
            n_rels = len(parsed.get("relations", [])) if parsed else 0
            print(f"[{i+1}/{len(data)}] {doc.get('title', '?')}: {status}, "
                  f"extracted {n_rels} rels, {input_len} tok, {elapsed:.1f}s")

    print(f"\nDone. Parse success: {parse_success}, fail: {parse_fail}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()
