import json
import os
from collections import defaultdict

OUTPUT_DIR = "/root/schema_semantic_constrained_ie/outputs"

with open("/root/schema_semantic_constrained_ie/ontology_constraints.json") as f:
    scierc_raw = json.load(f)
with open("/root/schema_semantic_constrained_ie/data/docred/ontology_constraints_docred.json") as f:
    docred_raw = json.load(f)

# DocRED: build constraints indexed by both PID and human-readable name
docred_pair_by_key = {}
docred_dom_by_key = {}
docred_rng_by_key = {}
for pid, data in docred_raw["relation_constraints"].items():
    pairs = set(tuple(p) for p in data["valid_pairs"])
    name = docred_raw["relation_types"].get(pid, pid)
    for key in [pid, name]:
        docred_pair_by_key[key] = pairs
        docred_dom_by_key[key] = {h for h, t in pairs}
        docred_rng_by_key[key] = {t for h, t in pairs}

# SciERC
scierc_pair = {}
scierc_dom = {}
scierc_rng = {}
for rel, data in scierc_raw["relation_constraints"].items():
    pairs = set(tuple(p) for p in data["valid_pairs"])
    scierc_pair[rel] = pairs
    scierc_dom[rel] = {h for h, t in pairs}
    scierc_rng[rel] = {t for h, t in pairs}


def analyze_file(path, pair_constraints, dom_constraints, rng_constraints):
    total = 0
    pair_violations = 0
    indep_violations = 0
    indep_valid_pair_invalid = 0
    unknown_rel = 0
    examples = []
    rel_counter = defaultdict(int)

    with open(path) as f:
        for line in f:
            doc = json.loads(line)
            parsed = doc.get("parsed_output")
            if parsed is None:
                continue
            rels = parsed.get("relations", [])
            if rels is None:
                continue
            for t in rels:
                rel = t.get("type", "")
                head_type = t.get("head_type", "")
                tail_type = t.get("tail_type", "")
                if not rel or not head_type or not tail_type:
                    continue
                total += 1

                if rel not in pair_constraints:
                    unknown_rel += 1
                    continue

                in_dom = head_type in dom_constraints[rel]
                in_rng = tail_type in rng_constraints[rel]
                in_pair = (head_type, tail_type) in pair_constraints[rel]

                if not in_pair:
                    pair_violations += 1
                if not (in_dom and in_rng):
                    indep_violations += 1
                if in_dom and in_rng and not in_pair:
                    indep_valid_pair_invalid += 1
                    rel_counter[rel] += 1
                    if len(examples) < 15:
                        examples.append(
                            "  rel={}, ({}, {}), head={}, tail={}".format(
                                rel, head_type, tail_type,
                                t.get("head", ""), t.get("tail", "")
                            )
                        )

    return {
        "total_triples": total,
        "unknown_relation": unknown_rel,
        "pair_violations": pair_violations,
        "indep_violations": indep_violations,
        "indep_valid_pair_invalid": indep_valid_pair_invalid,
        "examples": examples,
        "by_relation": dict(sorted(rel_counter.items(), key=lambda x: -x[1]))
    }


def print_result(label, r):
    print("=" * 70)
    print(label)
    print("=" * 70)
    print("  Total triples:                          {}".format(r["total_triples"]))
    print("  Unknown relation (not in ontology):      {}".format(r["unknown_relation"]))
    print("  Pair-based violations:                   {}".format(r["pair_violations"]))
    print("  Independent violations:                  {}".format(r["indep_violations"]))
    print("  Indep-valid but pair-invalid:            {}".format(r["indep_valid_pair_invalid"]))
    if r["pair_violations"] > 0:
        pct = r["indep_valid_pair_invalid"] / r["pair_violations"] * 100
        print("  Fraction missed by independent:          {}/{} = {:.1f}%".format(
            r["indep_valid_pair_invalid"], r["pair_violations"], pct))
    if r["by_relation"]:
        print("\n  By relation:")
        for rel, cnt in list(r["by_relation"].items())[:15]:
            print("    {}: {}".format(rel, cnt))
    if r["examples"]:
        print("\n  Examples:")
        for ex in r["examples"][:10]:
            print(ex)


# DocRED full_s1
r1 = analyze_file(
    os.path.join(OUTPUT_DIR, "docred_full_s1.jsonl"),
    docred_pair_by_key, docred_dom_by_key, docred_rng_by_key
)
print_result("DocRED full_s1 - Independent vs Pair-based", r1)

# DocRED unconstrained
print()
r2 = analyze_file(
    os.path.join(OUTPUT_DIR, "docred_unconstrained.jsonl"),
    docred_pair_by_key, docred_dom_by_key, docred_rng_by_key
)
print_result("DocRED unconstrained - Pair violations baseline", r2)

# SciERC
print()
for fname in ["phase2_scierc_full_s1_v2.jsonl", "phase2_scierc_full_s1.jsonl"]:
    path = os.path.join(OUTPUT_DIR, fname)
    if os.path.exists(path):
        r3 = analyze_file(path, scierc_pair, scierc_dom, scierc_rng)
        print_result("SciERC {} - Independent vs Pair-based".format(fname), r3)
        break

# SciERC unconstrained
for fname in ["phase2_scierc_unconstrained.jsonl"]:
    path = os.path.join(OUTPUT_DIR, fname)
    if os.path.exists(path):
        print()
        r4 = analyze_file(path, scierc_pair, scierc_dom, scierc_rng)
        print_result("SciERC unconstrained - Pair violations baseline", r4)
        break

# Summary table
print("\n" + "=" * 70)
print("SUMMARY: Over-permissiveness of Independent Enforcement")
print("=" * 70)
print("  In constrained outputs (full_s1):")
print("    DocRED:  {}/{} pair violations are missed by independent ({:.1f}%)".format(
    r1["indep_valid_pair_invalid"], r1["pair_violations"],
    r1["indep_valid_pair_invalid"] / max(r1["pair_violations"], 1) * 100
))

# Save
combined = {
    "docred_full_s1": {k: v for k, v in r1.items() if k != "examples"},
    "docred_unconstrained": {k: v for k, v in r2.items() if k != "examples"},
}
with open(os.path.join(OUTPUT_DIR, "rectangularity_impact.json"), "w") as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)
print("\nSaved to {}/rectangularity_impact.json".format(OUTPUT_DIR))
