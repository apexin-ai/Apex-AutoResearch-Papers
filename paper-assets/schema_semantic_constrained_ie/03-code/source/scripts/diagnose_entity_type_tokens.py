"""Diagnose entity type first-token collisions across tokenizers.

Checks whether the _build_entity_type_prefix_map vocab scan correctly covers
all tokens that Mistral/Qwen/Llama might emit for entity types in JSON context.
"""

import json
import os
from collections import defaultdict

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from transformers import AutoTokenizer

# ── Config ──
ONTOLOGY_PATH = "data/wikievents/ontology_constraints_wikievents.json"

TOKENIZER_PATHS = {
    "Mistral": "/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3-ms/mistralai/Mistral-7B-Instruct-v0___3/",
    "Qwen": "/root/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218/",
    "Llama": "/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/",
}


def load_entity_types():
    with open(ONTOLOGY_PATH) as f:
        ontology = json.load(f)
    return ontology["entity_types"]


def build_prefix_map_simulation(tokenizer, entity_types):
    """Simulate _build_entity_type_prefix_map: full vocab scan."""
    prefix_types = {}
    for etype in entity_types:
        for end in range(1, len(etype) + 1):
            prefix = etype[:end]
            prefix_types.setdefault(prefix, set()).add(etype)

    prefix_to_types = defaultdict(set)
    for token_id in tokenizer.get_vocab().values():
        try:
            decoded = tokenizer.decode([token_id])
        except Exception:
            continue
        if decoded in prefix_types:
            prefix_to_types[token_id].update(prefix_types[decoded])

    return dict(prefix_to_types), prefix_types


def analyze_tokenizer(name, tokenizer, entity_types):
    print(f"\n{'='*80}")
    print(f"  {name} tokenizer  ({getattr(tokenizer, 'name_or_path', '?')})")
    print(f"{'='*80}")
    print(f"  Tokenizer class: {type(tokenizer).__name__}")
    print(f"  Vocab size: {tokenizer.vocab_size}")
    print()

    # 1) Bare vs in-context tokenization
    print(f"### {name}: Bare vs In-Context Tokenization")
    print(f"{'Entity Type':<12} {'Bare IDs':<30} {'Ctx IDs (after \")':<30} "
          f"{'Bare 1st':<10} {'Ctx 1st':<10} {'Match?':<8} {'Bare tok':<15} {'Ctx tok':<15}")
    print("-" * 140)

    bare_first = {}
    ctx_first = {}
    mismatches = []

    quote_ids = tokenizer.encode('"', add_special_tokens=False)
    q_tok = quote_ids[0] if quote_ids else None

    for et in entity_types:
        bare_ids = tokenizer.encode(et, add_special_tokens=False)
        ctx_str = '"' + et + '"'
        ctx_ids = tokenizer.encode(ctx_str, add_special_tokens=False)

        # Strip leading/trailing quote tokens
        ctx_inner = []
        for i, tid in enumerate(ctx_ids):
            if tid == q_tok and (i == 0 or i == len(ctx_ids) - 1):
                continue
            ctx_inner.append(tid)

        b_first = bare_ids[0]
        c_first = ctx_inner[0] if ctx_inner else None
        match = b_first == c_first

        bare_first[et] = b_first
        ctx_first[et] = c_first

        b_tok_str = repr(tokenizer.decode([b_first]))
        c_tok_str = repr(tokenizer.decode([c_first])) if c_first is not None else "N/A"

        flag = "OK" if match else "MISMATCH"
        if not match:
            mismatches.append(et)

        print(f"{et:<12} {str(bare_ids):<30} {str(ctx_inner):<30} "
              f"{b_first:<10} {str(c_first):<10} {flag:<8} {b_tok_str:<15} {c_tok_str:<15}")

    print()
    if mismatches:
        print(f"  *** {len(mismatches)} MISMATCHES: {mismatches}")
    else:
        print(f"  All {len(entity_types)} entity types match bare vs in-context.")

    # 2) First-token collision matrix (bare)
    print(f"\n### {name}: First-Token Collision Matrix (bare encode)")
    groups_bare = defaultdict(list)
    for et in entity_types:
        groups_bare[bare_first[et]].append(et)
    collisions_bare = {tid: types for tid, types in groups_bare.items() if len(types) > 1}
    if collisions_bare:
        print(f"  {sum(len(v) for v in collisions_bare.values())} entity types in "
              f"{len(collisions_bare)} collision groups:")
        for tid, types in sorted(collisions_bare.items(), key=lambda x: -len(x[1])):
            tok_str = repr(tokenizer.decode([tid]))
            print(f"    token={tid} {tok_str}: {types}")
    else:
        print(f"  No collisions (all {len(entity_types)} types have unique first token).")

    # 2b) First-token collision matrix (in-context)
    print(f"\n### {name}: First-Token Collision Matrix (in-context encode)")
    groups_ctx = defaultdict(list)
    for et in entity_types:
        if ctx_first[et] is not None:
            groups_ctx[ctx_first[et]].append(et)
    collisions_ctx = {tid: types for tid, types in groups_ctx.items() if len(types) > 1}
    if collisions_ctx:
        print(f"  {sum(len(v) for v in collisions_ctx.values())} entity types in "
              f"{len(collisions_ctx)} collision groups:")
        for tid, types in sorted(collisions_ctx.items(), key=lambda x: -len(x[1])):
            tok_str = repr(tokenizer.decode([tid]))
            print(f"    token={tid} {tok_str}: {types}")
    else:
        print(f"  No collisions (all types have unique in-context first token).")

    # 3) Prefix map coverage check
    print(f"\n### {name}: Prefix Map Coverage Check")
    prefix_map, text_prefixes = build_prefix_map_simulation(tokenizer, entity_types)

    # Check: are bare first tokens in prefix map?
    bare_missing = []
    for et in entity_types:
        if bare_first[et] not in prefix_map:
            bare_missing.append(et)
    if bare_missing:
        print(f"  BARE first tokens NOT in prefix map: {bare_missing}")
    else:
        print(f"  All bare first tokens found in prefix map.")

    # Check: are in-context first tokens in prefix map?
    ctx_missing = []
    for et in entity_types:
        if ctx_first[et] is not None and ctx_first[et] not in prefix_map:
            ctx_missing.append((et, ctx_first[et], repr(tokenizer.decode([ctx_first[et]]))))
    if ctx_missing:
        print(f"  IN-CONTEXT first tokens NOT in prefix map ({len(ctx_missing)}):")
        for et, tid, tok_str in ctx_missing:
            print(f"    {et}: token_id={tid} decoded={tok_str}")
    else:
        print(f"  All in-context first tokens found in prefix map.")

    # 4) Detailed prefix map contents for entity types
    print(f"\n### {name}: Prefix Map Summary")
    print(f"  Total prefix map entries: {len(prefix_map)}")
    print(f"  Expected text prefixes: {sorted(text_prefixes.keys())}")
    # Show which tokens map to full entity types
    full_type_tokens = defaultdict(list)
    for tid, types in prefix_map.items():
        decoded = tokenizer.decode([tid])
        if decoded in entity_types:
            for t in types:
                full_type_tokens[t].append((tid, repr(decoded)))
    print(f"\n  Tokens that decode to full entity type names:")
    for et in entity_types:
        tokens = full_type_tokens.get(et, [])
        if tokens:
            print(f"    {et}: {tokens}")
        else:
            print(f"    {et}: *** NO MATCHING TOKEN IN VOCAB ***")

    # 5) Deep dive: what token does the model see after '"' for each entity type?
    print(f"\n### {name}: Generation-Context Token Analysis")
    print(f"  Simulating: after '\"type\": \"', what token would start each entity type?")
    long_ctx = '"type": "'
    long_ctx_ids = tokenizer.encode(long_ctx, add_special_tokens=False)
    print(f"  Context prefix '{long_ctx}' -> tokens: {long_ctx_ids}")
    print()

    for et in entity_types:
        full_str = long_ctx + et + '"'
        full_ids = tokenizer.encode(full_str, add_special_tokens=False)
        # Remove the context prefix tokens
        et_ids = full_ids[len(long_ctx_ids):]
        # Also remove trailing quote if present
        if et_ids and et_ids[-1] == q_tok:
            et_ids = et_ids[:-1]
        gen_first = et_ids[0] if et_ids else None

        in_map = gen_first in prefix_map if gen_first is not None else False
        gen_tok_str = repr(tokenizer.decode([gen_first])) if gen_first is not None else "N/A"
        bare_tok_str = repr(tokenizer.decode([bare_first[et]]))

        status = "OK" if in_map else "*** MISSING ***"
        match_bare = "=bare" if gen_first == bare_first[et] else "!=bare"

        print(f"  {et:<8} gen_1st={str(gen_first):<8} {gen_tok_str:<15} "
              f"bare_1st={bare_first[et]:<8} {bare_tok_str:<15} "
              f"{match_bare:<10} prefix_map: {status}")

    return {
        "bare_first": bare_first,
        "ctx_first": ctx_first,
        "mismatches": mismatches,
        "collisions_bare": collisions_bare,
        "collisions_ctx": collisions_ctx,
        "bare_missing": bare_missing,
        "ctx_missing": ctx_missing,
    }


def main():
    entity_types = load_entity_types()
    print(f"Entity types ({len(entity_types)}): {entity_types}")

    results = {}
    for name, path in TOKENIZER_PATHS.items():
        if not os.path.exists(path):
            print(f"\n*** Skipping {name}: path not found: {path}")
            continue
        print(f"\nLoading {name} tokenizer from {path}...")
        tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
        results[name] = analyze_tokenizer(name, tok, entity_types)

    # ── Summary ──
    print("\n" + "=" * 80)
    print("  ROOT CAUSE SUMMARY")
    print("=" * 80)

    for name, r in results.items():
        print(f"\n{name}:")
        n_mismatch = len(r["mismatches"])
        n_collision_bare = sum(len(v) for v in r["collisions_bare"].values()) if r["collisions_bare"] else 0
        n_collision_ctx = sum(len(v) for v in r["collisions_ctx"].values()) if r["collisions_ctx"] else 0
        n_bare_missing = len(r["bare_missing"])
        n_ctx_missing = len(r["ctx_missing"])

        print(f"  Bare vs in-context mismatches: {n_mismatch}")
        print(f"  Bare first-token collisions: {n_collision_bare} types in {len(r['collisions_bare'])} groups")
        print(f"  In-context first-token collisions: {n_collision_ctx} types in {len(r['collisions_ctx'])} groups")
        print(f"  Bare first tokens missing from prefix map: {n_bare_missing}")
        print(f"  In-context first tokens missing from prefix map: {n_ctx_missing}")

        if n_ctx_missing > 0:
            print(f"  >>> ROOT CAUSE: in-context tokens NOT in prefix map (D044-type bug)")
        elif n_collision_ctx > 0:
            print(f"  >>> ROOT CAUSE: first-token collisions prevent disambiguation")
        elif n_mismatch > 0:
            print(f"  >>> POTENTIAL ISSUE: bare!=context but prefix map covers both")
        else:
            print(f"  >>> Entity type masking should work correctly")


if __name__ == "__main__":
    main()
