"""Phase 2: Constrained extraction with grammar (XGrammar) + semantic (TypeConstraintProcessor) layers.

Modes:
  unconstrained  – no constraints (baseline)
  grammar_only   – XGrammar JSON/enum structure enforcement
  semantic_only  – TypeConstraintProcessor domain/range masking
  full_s1        – both layers, single-pass
  full_s2        – two-pass: entities first, then constrained relations

Datasets: scierc (sentence-level), docred (document-level)
Output: JSONL compatible with violation_checker.py
"""

import argparse
import json
import re
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from compiler.ontology_compiler import ConstraintSpec, RelationConstraint
from compiler.type_mask_processor import TypeConstraintProcessor


RAW_TO_CANONICAL = {
    "USED-FOR": "Used-for", "FEATURE-OF": "Feature-of",
    "HYPONYM-OF": "Hyponym-of", "PART-OF": "Part-of",
    "COMPARE": "Compare", "CONJUNCTION": "Conjunction",
    "EVALUATE-FOR": "Evaluate-for",
}

SCIERC_SYSTEM = """You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.

Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic
Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for

Output a JSON object with:
- "entities": list of {"text": "...", "type": "..."}
- "relations": list of {"head": "...", "tail": "...", "type": "...", "head_type": "...", "tail_type": "..."}

Output ONLY valid JSON, no explanation."""

SCIERC_USER_TEMPLATE = """Extract all entities and relations from this scientific text:

"{text}"

Output JSON:"""


# ── Data Loading ─────────────────────────────────────────────────────

def load_scierc_data(data_path):
    samples = []
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            doc = json.loads(line)
            doc_id = doc.get("doc_key", "unknown")
            sentences = doc.get("sentences", [])
            ner_all = doc.get("ner", [])
            rel_all = doc.get("relations", [])

            offsets = []
            cum = 0
            for s in sentences:
                offsets.append(cum)
                cum += len(s)

            for sent_idx, tokens in enumerate(sentences):
                sentence_text = " ".join(tokens)
                offset = offsets[sent_idx]

                gold_entities = []
                if sent_idx < len(ner_all):
                    for start, end, etype in ner_all[sent_idx]:
                        mention = " ".join(tokens[start - offset:end - offset + 1])
                        gold_entities.append({"text": mention, "type": etype})

                gold_relations = []
                if sent_idx < len(rel_all):
                    span_type = {}
                    if sent_idx < len(ner_all):
                        for s, e, et in ner_all[sent_idx]:
                            span_type[(s, e)] = et
                    for h_s, h_e, t_s, t_e, rtype_raw in rel_all[sent_idx]:
                        head_text = " ".join(tokens[h_s - offset:h_e - offset + 1])
                        tail_text = " ".join(tokens[t_s - offset:t_e - offset + 1])
                        head_type = span_type.get((h_s, h_e), "UNKNOWN")
                        tail_type = span_type.get((t_s, t_e), "UNKNOWN")
                        rtype = RAW_TO_CANONICAL.get(rtype_raw, rtype_raw)
                        gold_relations.append({
                            "head": head_text, "tail": tail_text, "type": rtype,
                            "head_type": head_type, "tail_type": tail_type,
                        })

                samples.append({
                    "doc_id": f"{doc_id}_sent{sent_idx}",
                    "input_text": sentence_text,
                    "gold_entities": gold_entities,
                    "gold_relations": gold_relations,
                })
    return samples


def load_docred_data(data_path):
    with open(data_path) as f:
        data = json.load(f)
    samples = []
    for i, doc in enumerate(data):
        doc_id = doc.get("title", f"doc_{i}")
        doc_text = " ".join(" ".join(sent) for sent in doc["sents"])
        vertex_set = doc["vertexSet"]

        gold_entities = []
        entity_names = {}
        for idx, vs in enumerate(vertex_set):
            name = vs[0]["name"]
            etype = vs[0].get("type", "UNK")
            gold_entities.append({"text": name, "type": etype})
            entity_names[idx] = name

        gold_relations = []
        for label in doc.get("labels", []):
            h_name = entity_names.get(label["h"], f"entity_{label['h']}")
            t_name = entity_names.get(label["t"], f"entity_{label['t']}")
            h_type = vertex_set[label["h"]][0].get("type", "UNK")
            t_type = vertex_set[label["t"]][0].get("type", "UNK")
            gold_relations.append({
                "head": h_name, "tail": t_name, "type": label["r"],
                "head_type": h_type, "tail_type": t_type,
            })

        samples.append({
            "doc_id": doc_id,
            "input_text": doc_text,
            "gold_entities": gold_entities,
            "gold_relations": gold_relations,
        })
    return samples


# ── Prompt Building ──────────────────────────────────────────────────

def build_messages(dataset, sample, entity_types, relation_types):
    if dataset == "scierc":
        return [
            {"role": "system", "content": SCIERC_SYSTEM},
            {"role": "user", "content": SCIERC_USER_TEMPLATE.format(text=sample["input_text"])},
        ]
    rel_list = "\n".join(f"- {r}" for r in relation_types)
    prompt = f"""You are an information extraction system. Extract all entities and relations from the following document.

Entity types: {", ".join(entity_types)}

Relation types:
{rel_list}

Document:
{sample["input_text"]}

Output a JSON object with exactly this structure:
{{"entities": [{{"text": "entity name", "type": "ENTITY_TYPE"}}], "relations": [{{"head": "head entity", "tail": "tail entity", "type": "relation name", "head_type": "ENTITY_TYPE", "tail_type": "ENTITY_TYPE"}}]}}

Output ONLY the JSON, no other text."""
    return [{"role": "user", "content": prompt}]


def build_s2_entity_messages(dataset, sample, entity_types):
    """S2 Pass 1: entity-only extraction."""
    if dataset == "scierc":
        system = f"""You are an expert information extraction system for scientific texts. Extract all entities from the given text.

Entity types: {", ".join(entity_types)}

Output a JSON object with:
- "entities": list of {{"text": "...", "type": "..."}}

Output ONLY valid JSON, no explanation."""
        user = f'Extract all entities from this scientific text:\n\n"{sample["input_text"]}"\n\nOutput JSON:'
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]

    prompt = f"""You are an information extraction system. Extract all entities from the following document.

Entity types: {", ".join(entity_types)}

Document:
{sample["input_text"]}

Output a JSON object with exactly this structure:
{{"entities": [{{"text": "entity name", "type": "ENTITY_TYPE"}}]}}

Output ONLY the JSON, no other text."""
    return [{"role": "user", "content": prompt}]


def build_s2_relation_messages(dataset, sample, entities, entity_types, relation_types):
    """S2 Pass 2: relation extraction given known entities."""
    entity_list_str = json.dumps(entities, ensure_ascii=False)

    if dataset == "scierc":
        system = f"""You are an expert information extraction system for scientific texts. Given a text and its entities, extract all relations between them.

Entity types: {", ".join(entity_types)}
Relation types: {", ".join(relation_types)}

Output a JSON object with:
- "relations": list of {{"head": "...", "tail": "...", "type": "...", "head_type": "...", "tail_type": "..."}}

head and tail must be entity texts from the given list. head_type and tail_type must match their entity types.
Output ONLY valid JSON, no explanation."""
        user = f"""Entities found in the text:
{entity_list_str}

Text: "{sample["input_text"]}"

Extract all relations between these entities. Output JSON:"""
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]

    rel_list = "\n".join(f"- {r}" for r in relation_types)
    prompt = f"""You are an information extraction system. Given a document and its entities, extract all relations between them.

Entity types: {", ".join(entity_types)}

Relation types:
{rel_list}

Entities found in the document:
{entity_list_str}

Document:
{sample["input_text"]}

Extract all relations between these entities. head and tail must be entity texts from the given list.
Output a JSON object with exactly this structure:
{{"relations": [{{"head": "head entity", "tail": "tail entity", "type": "relation name", "head_type": "ENTITY_TYPE", "tail_type": "ENTITY_TYPE"}}]}}

Output ONLY the JSON, no other text."""
    return [{"role": "user", "content": prompt}]


# ── JSON Schema Builders ─────────────────────────────────────────────

def build_full_schema(entity_types, relation_types):
    return {
        "type": "object",
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "type": {"type": "string", "enum": entity_types},
                    },
                    "required": ["text", "type"],
                    "additionalProperties": False,
                }
            },
            "relations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "head": {"type": "string"},
                        "tail": {"type": "string"},
                        "type": {"type": "string", "enum": relation_types},
                        "head_type": {"type": "string", "enum": entity_types},
                        "tail_type": {"type": "string", "enum": entity_types},
                    },
                    "required": ["head", "tail", "type", "head_type", "tail_type"],
                    "additionalProperties": False,
                }
            },
        },
        "required": ["entities", "relations"],
        "additionalProperties": False,
    }


def build_entity_only_schema(entity_types):
    return {
        "type": "object",
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "type": {"type": "string", "enum": entity_types},
                    },
                    "required": ["text", "type"],
                    "additionalProperties": False,
                }
            },
        },
        "required": ["entities"],
        "additionalProperties": False,
    }


def build_relation_only_schema(entity_types, relation_types, entity_texts=None):
    """When entity_texts provided, head/tail are enum-constrained to known entities."""
    head_prop = {"type": "string", "enum": entity_texts} if entity_texts else {"type": "string"}
    tail_prop = {"type": "string", "enum": entity_texts} if entity_texts else {"type": "string"}
    return {
        "type": "object",
        "properties": {
            "relations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "head": head_prop,
                        "tail": tail_prop,
                        "type": {"type": "string", "enum": relation_types},
                        "head_type": {"type": "string", "enum": entity_types},
                        "tail_type": {"type": "string", "enum": entity_types},
                    },
                    "required": ["head", "tail", "type", "head_type", "tail_type"],
                    "additionalProperties": False,
                }
            },
        },
        "required": ["relations"],
        "additionalProperties": False,
    }


# ── Constraint Loading ───────────────────────────────────────────────

def load_constraint_spec(constraints_path):
    """Load ontology constraints, normalizing DocRED P-codes to relation names."""
    with open(constraints_path) as f:
        raw = json.load(f)

    entity_types = raw["entity_types"]
    raw_rtypes = raw["relation_types"]

    if isinstance(raw_rtypes, dict):
        # DocRED: {P-code: name} dict → use names as relation types
        code_to_name = raw_rtypes
        relation_types = list(code_to_name.values())
        relation_constraints = {}
        for code, data in raw["relation_constraints"].items():
            name = code_to_name.get(code, code)
            relation_constraints[name] = RelationConstraint(
                relation_type=name,
                valid_pairs=[(h, t) for h, t in data["valid_pairs"]],
            )
    else:
        # SciERC: plain list
        relation_types = raw_rtypes
        relation_constraints = {}
        for rtype, data in raw["relation_constraints"].items():
            relation_constraints[rtype] = RelationConstraint(
                relation_type=rtype,
                valid_pairs=[(h, t) for h, t in data["valid_pairs"]],
            )

    return ConstraintSpec(
        entity_types=entity_types,
        relation_types=relation_types,
        relation_constraints=relation_constraints,
    )


def ensure_first_token_map(spec, tokenizer):
    if spec.entity_type_first_token:
        return
    for etype in spec.entity_types:
        token_ids = tokenizer.encode(etype, add_special_tokens=False)
        spec.entity_type_token_ids[etype] = token_ids
        spec.entity_type_first_token[etype] = token_ids[0]


# ── Output Parsing ───────────────────────────────────────────────────

def parse_model_output(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    cleaned = re.sub(r'^```(?:json)?\s*', '', text.strip())
    cleaned = re.sub(r'\s*```$', '', cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    m = re.search(r'\{[\s\S]*\}', cleaned)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


# ── Extraction Runners ───────────────────────────────────────────────

def run_single_pass(model, tokenizer, sample, dataset, spec, mode,
                    compiled_grammar, max_new_tokens):
    """unconstrained / grammar_only / semantic_only / full_s1"""
    messages = build_messages(dataset, sample, spec.entity_types, spec.relation_types)
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    prompt_len = inputs["input_ids"].shape[1]

    processors = []
    if mode in ("grammar_only", "full_s1") and compiled_grammar is not None:
        import xgrammar as xgr
        processors.append(xgr.contrib.hf.LogitsProcessor(compiled_grammar))
    if mode in ("semantic_only", "full_s1"):
        processors.append(TypeConstraintProcessor(spec, tokenizer, prompt_len))

    gen_kwargs = dict(**inputs, max_new_tokens=max_new_tokens, do_sample=False)
    if processors:
        gen_kwargs["logits_processor"] = processors

    with torch.no_grad():
        output_ids = model.generate(**gen_kwargs)

    raw = tokenizer.decode(output_ids[0][prompt_len:], skip_special_tokens=True).strip()
    return raw, parse_model_output(raw)


def run_s2_two_pass(model, tokenizer, sample, dataset, spec,
                    entity_compiled_grammar, xgr_compiler, max_new_tokens):
    """S2: Pass 1 extracts entities, Pass 2 extracts relations with entity-aware constraints."""
    import xgrammar as xgr

    # ── Pass 1: Entity extraction ────────────────────────────────
    msgs_p1 = build_s2_entity_messages(dataset, sample, spec.entity_types)
    text_p1 = tokenizer.apply_chat_template(
        msgs_p1, tokenize=False, add_generation_prompt=True, enable_thinking=False,
    )
    inp_p1 = tokenizer(text_p1, return_tensors="pt").to(model.device)
    plen_p1 = inp_p1["input_ids"].shape[1]

    procs_p1 = []
    if entity_compiled_grammar is not None:
        procs_p1.append(xgr.contrib.hf.LogitsProcessor(entity_compiled_grammar))
    procs_p1.append(TypeConstraintProcessor(spec, tokenizer, plen_p1))

    with torch.no_grad():
        out_p1 = model.generate(
            **inp_p1, max_new_tokens=max_new_tokens,
            do_sample=False, logits_processor=procs_p1,
        )
    raw_p1 = tokenizer.decode(out_p1[0][plen_p1:], skip_special_tokens=True).strip()
    parsed_p1 = parse_model_output(raw_p1)

    entities = parsed_p1.get("entities", []) if parsed_p1 else []
    if not entities:
        return raw_p1, {"entities": [], "relations": []}

    # ── Pass 2: Relation extraction with entity constraints ──────
    entity_texts = list({e["text"] for e in entities if "text" in e})

    msgs_p2 = build_s2_relation_messages(
        dataset, sample, entities, spec.entity_types, spec.relation_types
    )
    text_p2 = tokenizer.apply_chat_template(
        msgs_p2, tokenize=False, add_generation_prompt=True, enable_thinking=False,
    )
    inp_p2 = tokenizer(text_p2, return_tensors="pt").to(model.device)
    plen_p2 = inp_p2["input_ids"].shape[1]

    # Per-sample grammar: head/tail enum-constrained to Pass 1 entity texts
    try:
        rel_schema = build_relation_only_schema(
            spec.entity_types, spec.relation_types, entity_texts
        )
        rel_grammar = xgr.Grammar.from_json_schema(json.dumps(rel_schema))
        rel_compiled = xgr_compiler.compile_grammar(rel_grammar)
    except Exception:
        # Fallback: free-text head/tail if entity-enum compilation fails
        rel_schema = build_relation_only_schema(spec.entity_types, spec.relation_types)
        rel_grammar = xgr.Grammar.from_json_schema(json.dumps(rel_schema))
        rel_compiled = xgr_compiler.compile_grammar(rel_grammar)

    procs_p2 = [xgr.contrib.hf.LogitsProcessor(rel_compiled)]

    # TypeConstraintProcessor with pre-registered entities from Pass 1
    type_proc_p2 = TypeConstraintProcessor(spec, tokenizer, plen_p2)
    for e in entities:
        if "text" in e and "type" in e:
            type_proc_p2.state.entity_registry.register(e["text"], e["type"])
    type_proc_p2.state.in_entities_section = False
    procs_p2.append(type_proc_p2)

    with torch.no_grad():
        out_p2 = model.generate(
            **inp_p2, max_new_tokens=max_new_tokens,
            do_sample=False, logits_processor=procs_p2,
        )
    raw_p2 = tokenizer.decode(out_p2[0][plen_p2:], skip_special_tokens=True).strip()
    parsed_p2 = parse_model_output(raw_p2)

    relations = parsed_p2.get("relations", []) if parsed_p2 else []

    combined_raw = f"[Pass1] {raw_p1}\n[Pass2] {raw_p2}"
    return combined_raw, {"entities": entities, "relations": relations}


# ── Main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Phase 2: Constrained IE with grammar + semantic layers"
    )
    parser.add_argument("--mode", required=True,
                        choices=["unconstrained", "grammar_only", "semantic_only",
                                 "full_s1", "full_s2"])
    parser.add_argument("--dataset", required=True, choices=["scierc", "docred"])
    parser.add_argument("--model_path", default=None)
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--constraints_path", required=True)
    parser.add_argument("--output_path", required=True)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--max_samples", type=int, default=0, help="0 = all")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_new_tokens", type=int, default=2048)
    args = parser.parse_args()

    torch.manual_seed(args.seed)

    model_path = args.model_path
    if model_path is None:
        for p in ["/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B",
                   "/root/models/Qwen3-8B"]:
            if Path(p).exists():
                model_path = p
                break
    if model_path is None:
        raise FileNotFoundError("Qwen3-8B not found. Specify --model_path.")

    print(f"Mode: {args.mode}")
    print(f"Dataset: {args.dataset}")
    print(f"Model: {model_path}")
    print(f"Device: {args.device}")

    if args.dataset == "scierc":
        samples = load_scierc_data(args.data_path)
    else:
        samples = load_docred_data(args.data_path)

    if args.max_samples > 0:
        samples = samples[:args.max_samples]
    print(f"Samples: {len(samples)}")

    spec = load_constraint_spec(args.constraints_path)
    print(f"Entity types: {spec.entity_types}")
    print(f"Relation types: {len(spec.relation_types)}")

    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    tokenizer.padding_side = "left"
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16,
        device_map=args.device, trust_remote_code=True,
    )
    model.eval()
    print("Model loaded")

    ensure_first_token_map(spec, tokenizer)

    # Pre-compile grammars (reusable across samples)
    compiled_grammar = None
    entity_compiled_grammar = None
    xgr_compiler = None

    needs_grammar = args.mode in ("grammar_only", "full_s1", "full_s2")
    if needs_grammar:
        import xgrammar as xgr
        tokenizer_info = xgr.TokenizerInfo.from_huggingface(
            tokenizer, vocab_size=model.config.vocab_size
        )
        xgr_compiler = xgr.GrammarCompiler(tokenizer_info)

        if args.mode in ("grammar_only", "full_s1"):
            schema = build_full_schema(spec.entity_types, spec.relation_types)
            grammar = xgr.Grammar.from_json_schema(json.dumps(schema))
            compiled_grammar = xgr_compiler.compile_grammar(grammar)
            print("Grammar compiled (full schema)")
        else:
            schema = build_entity_only_schema(spec.entity_types)
            grammar = xgr.Grammar.from_json_schema(json.dumps(schema))
            entity_compiled_grammar = xgr_compiler.compile_grammar(grammar)
            print("Grammar compiled (entity-only for S2 Pass 1)")

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    n_ok, n_fail = 0, 0

    with open(args.output_path, "w") as fout:
        for i, sample in enumerate(samples):
            t0 = time.time()

            if args.mode == "full_s2":
                raw, parsed = run_s2_two_pass(
                    model, tokenizer, sample, args.dataset, spec,
                    entity_compiled_grammar, xgr_compiler, args.max_new_tokens,
                )
            else:
                raw, parsed = run_single_pass(
                    model, tokenizer, sample, args.dataset, spec,
                    args.mode, compiled_grammar, args.max_new_tokens,
                )

            elapsed = time.time() - t0

            if parsed is not None:
                n_ok += 1
            else:
                n_fail += 1

            record = {
                "doc_id": sample["doc_id"],
                "input_text": sample["input_text"],
                "gold_entities": sample["gold_entities"],
                "gold_relations": sample["gold_relations"],
                "raw_output": raw,
                "parsed_output": parsed,
                "inference_time_seconds": round(elapsed, 3),
                "mode": args.mode,
            }
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            fout.flush()

            n_ents = len(parsed.get("entities", [])) if parsed else 0
            n_rels = len(parsed.get("relations", [])) if parsed else 0
            status = "OK" if parsed else "FAIL"
            print(f"[{i+1}/{len(samples)}] {sample['doc_id']}: {status} "
                  f"E={n_ents} R={n_rels} {elapsed:.1f}s")

    print(f"\nDone: {n_ok + n_fail} samples, success={n_ok}, fail={n_fail}")
    print(f"Output: {args.output_path}")


if __name__ == "__main__":
    main()
