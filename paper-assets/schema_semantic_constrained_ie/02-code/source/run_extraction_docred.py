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
import os
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
    """Format relation types as a compact list for the prompt (minimal mode)."""
    lines = [f"- {name}" for _, name in sorted(rel_info.items(), key=lambda x: x[1])]
    return "\n".join(lines)


def build_schema_informed_relation_str(constraints_path: str, rel_info: dict,
                                       max_relations: int = 50) -> str:
    """Build relation list with (head_type, tail_type) pair constraints.

    DocRED has tight type constraints (avg ~5.7 valid pairs out of 36 possible),
    so listing all valid pairs per relation is compact and informative.
    Relations sorted by training frequency; truncated to top max_relations.
    """
    with open(constraints_path) as f:
        constraints = json.load(f)

    rel_constraints = constraints["relation_constraints"]

    ranked = sorted(
        rel_constraints.items(),
        key=lambda x: x[1]["stats"]["total"],
        reverse=True,
    )

    included = ranked[:max_relations]
    excluded_count = len(ranked) - len(included)

    seen_ids = {r[0] for r in ranked}
    unseen = [rid for rid in rel_info if rid not in seen_ids]

    lines = []
    for rel_id, rc in included:
        name = rc["name"]
        pairs = rc["valid_pairs"]
        pair_strs = [f"({p[0]}→{p[1]})" for p in pairs]
        lines.append(f"- {name}: valid pairs: {', '.join(pair_strs)}")

    if excluded_count > 0:
        lines.append(f"(and {excluded_count} more relation types with lower frequency)")

    if unseen:
        unseen_names = [rel_info[rid] for rid in unseen]
        lines.append(f"Additional relation types (rare): {', '.join(unseen_names)}")

    return "\n".join(lines)


def doc_to_text(doc: dict) -> str:
    """Concatenate all sentences in a DocRED document into plain text."""
    return " ".join(" ".join(sent) for sent in doc["sents"])


def build_prompt(document_text: str, relation_list_str: str,
                 schema_informed: bool = False) -> str:
    constraint_note = ""
    if schema_informed:
        constraint_note = (
            "\nEach extracted relation's (head_type, tail_type) must be a valid pair "
            "for that relation type as listed above.\n"
        )

    relation_header = "Relation types and their type constraints:" if schema_informed else "Relation types:"

    return f"""You are an information extraction system. Extract all entities and relations from the following document.

Entity types: {", ".join(ENTITY_TYPES)}

{relation_header}
{relation_list_str}
{constraint_note}
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
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", cleaned)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return None


def load_processed_ids(output_path: str) -> set:
    """Load doc_ids already written to the output file for resume."""
    processed = set()
    if not os.path.exists(output_path):
        return processed
    with open(output_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                processed.add(d.get("doc_id"))
            except json.JSONDecodeError:
                pass
    return processed


def batch_generate(model, tokenizer, chat_texts: list[str],
                   max_new_tokens: int = 2048) -> list[str]:
    """Run batched generation on pre-formatted chat template strings.

    Tokenizes with left-padding (required for decoder-only batch inference),
    generates, then decodes only the newly generated tokens per sample.

    Args:
        model: CausalLM with .generate() support.
        tokenizer: Tokenizer with padding_side="left" and pad_token set.
        chat_texts: Fully-formatted prompt strings (after apply_chat_template).
        max_new_tokens: Max new tokens to generate per sample.

    Returns:
        List of decoded generated texts, one per input.
    """
    inputs = tokenizer(
        chat_texts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=8192,
    ).to(model.device)

    padded_len = inputs["input_ids"].shape[1]

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=1.0,
            top_p=1.0,
        )

    results = []
    for j in range(len(chat_texts)):
        generated = outputs[j][padded_len:]
        text = tokenizer.decode(generated, skip_special_tokens=True)
        results.append(text)

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default=None,
                        help="Path to Qwen3-8B model. Auto-detected if not set.")
    parser.add_argument("--data_path", type=str, default="data/docred/dev.json")
    parser.add_argument("--rel_info_path", type=str, default="data/docred/rel_info.json")
    parser.add_argument("--output_path", type=str, default="outputs/raw_outputs_docred.jsonl")
    parser.add_argument("--constraints_path", type=str,
                        default="data/docred/ontology_constraints_docred.json",
                        help="Path to DocRED ontology constraints JSON (used with schema_informed mode)")
    parser.add_argument("--prompt_mode", type=str, default="minimal",
                        choices=["minimal", "schema_informed"],
                        help="Prompt mode: minimal (type names only) or schema_informed (with type constraints)")
    parser.add_argument("--max_relations", type=int, default=50,
                        help="Max relation types in schema_informed prompt (top-N by frequency)")
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--max_samples", type=int, default=None)
    parser.add_argument("--device", type=str, default="cuda:1")
    parser.add_argument("--max_new_tokens", type=int, default=2048)
    parser.add_argument("--resume", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

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
    print(f"Prompt mode: {args.prompt_mode}")
    print(f"Batch size: {args.batch_size}")

    with open(args.data_path) as f:
        data = json.load(f)
    rel_info = load_relation_names(args.rel_info_path)

    if args.prompt_mode == "schema_informed":
        relation_list_str = build_schema_informed_relation_str(
            args.constraints_path, rel_info, args.max_relations
        )
        is_schema = True
    else:
        relation_list_str = build_relation_list_str(rel_info)
        is_schema = False

    # Resume: skip docs already in the output file
    processed_ids = set()
    if args.resume:
        processed_ids = load_processed_ids(args.output_path)
        if processed_ids:
            print(f"Resume: {len(processed_ids)} docs already processed, skipping")

    todo = []
    for i, doc in enumerate(data):
        doc_id = doc.get("title", f"doc_{i}")
        if doc_id not in processed_ids:
            todo.append((i, doc))

    if args.max_samples:
        todo = todo[:args.max_samples]

    total = len(todo)
    print(f"Processing {total} documents (skipped {len(processed_ids)})")

    if total == 0:
        print("Nothing to process.")
        return

    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    # Decoder-only models require left padding for correct batch generation:
    # right-aligned content ensures the last real token is always at the end,
    # so autoregressive generation continues from the right position.
    tokenizer.padding_side = "left"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map=args.device,
        trust_remote_code=True,
    )
    model.eval()
    print("Model loaded")

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    parse_success = 0
    parse_fail = 0

    file_mode = "a" if args.resume else "w"
    with open(args.output_path, file_mode) as fout:
        for batch_start in range(0, total, args.batch_size):
            batch_items = todo[batch_start:batch_start + args.batch_size]

            batch_texts = []
            batch_meta = []
            for orig_idx, doc in batch_items:
                doc_text = doc_to_text(doc)
                gold_entities, gold_relations = extract_gold(doc)
                prompt = build_prompt(doc_text, relation_list_str, schema_informed=is_schema)
                messages = [{"role": "user", "content": prompt}]
                text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True,
                    enable_thinking=False,
                )
                batch_texts.append(text)
                input_len = len(tokenizer(text)["input_ids"])
                batch_meta.append({
                    "orig_idx": orig_idx,
                    "doc": doc,
                    "doc_text": doc_text,
                    "gold_entities": gold_entities,
                    "gold_relations": gold_relations,
                    "input_len": input_len,
                })

            t0 = time.time()
            raw_outputs = batch_generate(
                model, tokenizer, batch_texts,
                max_new_tokens=args.max_new_tokens,
            )
            batch_elapsed = time.time() - t0
            per_doc_time = batch_elapsed / len(batch_items)

            for j, (meta, raw_output) in enumerate(zip(batch_meta, raw_outputs)):
                parsed = parse_model_output(raw_output)
                if parsed is not None:
                    parse_success += 1
                else:
                    parse_fail += 1

                doc = meta["doc"]
                record = {
                    "doc_id": doc.get("title", f"doc_{meta['orig_idx']}"),
                    "document": meta["doc_text"],
                    "gold_entities": meta["gold_entities"],
                    "gold_relations": meta["gold_relations"],
                    "model_output": raw_output,
                    "parsed_output": parsed,
                    "input_tokens": meta["input_len"],
                    "elapsed_seconds": round(per_doc_time, 2),
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")

                done = batch_start + j + 1
                status = "OK" if parsed else "PARSE_FAIL"
                n_rels = len(parsed.get("relations", [])) if parsed else 0
                print(f"[{done}/{total}] {doc.get('title', '?')}: {status}, "
                      f"extracted {n_rels} rels, {meta['input_len']} tok, "
                      f"{per_doc_time:.1f}s")

            fout.flush()

    print(f"\nDone. Parse success: {parse_success}, fail: {parse_fail}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()
