"""MAVEN case study: top confused pairs, SCS analysis, centrality vs confusability."""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).parent))

ROOT = Path(".")
PREDICTIONS = ROOT / "artifacts/exp004/predictions_maven_exp1.json"
MINILM_SIM = ROOT / "artifacts/maven_minilm_sim_matrix.pt"
QWEN3_SIM = ROOT / "artifacts/maven_bcs_matrix_qwen3.pt"
DATA_PATH = ROOT / "data/maven_parquet/valid.parquet"
OUTPUT = ROOT / "artifacts/maven_case_study.json"

SEMANTIC_ANNOTATIONS = {
    ("Achieve", "Getting"): {
        "relation": "causative-resultative",
        "note": "Getting is the process; Achieve is the outcome. Same triggers (won/gained) describe both.",
        "category": "centrality"
    },
    ("Departing", "Escaping"): {
        "relation": "manner-of",
        "note": "Escaping is Departing under duress. LLM conflates departure triggers (fled/left).",
        "category": "confusable"
    },
    ("Death", "Killing"): {
        "relation": "causative pair",
        "note": "Killing causes Death. Triggers like 'died'/'killed' are one-word-apart. High SCS but semantically distinct roles.",
        "category": "centrality"
    },
    ("Attack", "Use_firearm"): {
        "relation": "instrument-of",
        "note": "Use_firearm is a specific instrument for Attack. 'shot'/'fired' triggers overlap.",
        "category": "confusable"
    },
    ("Action", "Removing"): {
        "relation": "hypernym-hyponym",
        "note": "Action is the most generic event type. Removing triggers (cut/dropped) are also generic actions.",
        "category": "centrality"
    },
    ("Arriving", "Conquering"): {
        "relation": "script-adjacent",
        "note": "In military narrative, arriving and conquering co-occur. 'took' is ambiguous.",
        "category": "centrality"
    },
    ("Communication", "Expressing_publicly"): {
        "relation": "hypernym-hyponym",
        "note": "Expressing_publicly is a subtype of Communication. Same triggers (said/announced).",
        "category": "confusable"
    },
    ("Arriving", "Process_start"): {
        "relation": "metaphorical overlap",
        "note": "'came' can mean both physical arrival and process beginning.",
        "category": "centrality"
    },
    ("Motion", "Motion_directional"): {
        "relation": "hypernym-hyponym",
        "note": "Motion_directional is a subtype of Motion. Nearly all triggers overlap.",
        "category": "confusable"
    },
    ("Expressing_publicly", "Statement"): {
        "relation": "near-synonym",
        "note": "Both cover speech acts. 'said'/'stated'/'declared' trigger both.",
        "category": "confusable"
    },
    ("Action", "Arranging"): {
        "relation": "hypernym-hyponym",
        "note": "Action is maximally generic; Arranging inherits. 'set'/'put' ambiguous.",
        "category": "centrality"
    },
    ("Arriving", "Motion_directional"): {
        "relation": "endpoint-vs-path",
        "note": "Arriving = endpoint; Motion_directional = directed path. 'moved'/'went' cover both.",
        "category": "centrality"
    },
    ("Coming_to_be", "Process_start"): {
        "relation": "near-synonym",
        "note": "Both describe inception. 'began'/'started'/'emerged' trigger both.",
        "category": "confusable"
    },
    ("Achieve", "Check"): {
        "relation": "script-adjacent",
        "note": "In evaluation contexts, checking leads to achievement. 'passed'/'scored' ambiguous.",
        "category": "centrality"
    },
    ("Cause_change_of_position_on_a_scale", "Change"): {
        "relation": "hypernym-hyponym",
        "note": "Change is generic; CCOPS is a specific subtype. 'increased'/'rose' ambiguous.",
        "category": "confusable"
    },
    ("Communication", "Judgment_communication"): {
        "relation": "hypernym-hyponym",
        "note": "Judgment_communication is evaluative speech, a subtype of Communication.",
        "category": "confusable"
    },
    ("Action", "Competition"): {
        "relation": "hypernym-hyponym",
        "note": "Action is generic; Competition inherits. 'played'/'fought' ambiguous.",
        "category": "centrality"
    },
    ("Attack", "Catastrophe"): {
        "relation": "causal-script",
        "note": "Attacks cause catastrophes in narrative. 'struck'/'hit' trigger both.",
        "category": "centrality"
    },
    ("Bodily_harm", "Killing"): {
        "relation": "scalar degree",
        "note": "Killing is maximal Bodily_harm. 'wounded->killed' on same scale.",
        "category": "confusable"
    },
    ("Arriving", "Motion"): {
        "relation": "hypernym-hyponym",
        "note": "Arriving is a specific endpoint of Motion. 'came'/'moved' overlap.",
        "category": "centrality"
    },
}


def load_sim_matrix(path):
    data = torch.load(path, map_location="cpu", weights_only=True)
    names = data["type_names"]
    if isinstance(names[0], bytes):
        names = [t.decode() for t in names]
    return list(names), data["similarity_matrix"].float().numpy()


def load_maven_samples():
    import pandas as pd
    df = pd.read_parquet(DATA_PATH)
    samples = []
    for _, row in df.iterrows():
        entities = row["entities"]
        if isinstance(entities, str):
            entities = json.loads(entities)
        samples.append({"text": row["text"], "entities": list(entities)})
    return samples


def build_confusion(predictions, samples):
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)

    by_key = defaultdict(list)
    for p in predictions:
        by_key[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_key.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry.get("batch_types", []))
        if len(batch_types) < 2:
            continue

        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        preds = [p for p in entry.get("predictions", []) if p.get("type") in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt not in source_text:
                continue

            exact = False
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    exact = True
                    break
            if exact:
                continue

            for g in gold_available:
                if not g[2] and (g[0] == pt or g[0] in pt or pt in g[0]) and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    return confusion, gold_counts


def get_top_confused(confusion, gold_counts, type_to_idx, sim_minilm, sim_qwen3, n=20):
    pairs = []
    seen = set()
    for gt in confusion:
        for pt in confusion[gt]:
            key = tuple(sorted([gt, pt]))
            if key in seen:
                continue
            seen.add(key)
            c_fwd = confusion.get(gt, {}).get(pt, 0)
            c_bwd = confusion.get(pt, {}).get(gt, 0)
            total = c_fwd + c_bwd

            i, j = type_to_idx.get(gt), type_to_idx.get(pt)
            scs_m = float(sim_minilm[i, j]) if i is not None and j is not None else None
            scs_q = float(sim_qwen3[i, j]) if i is not None and j is not None else None

            pairs.append({
                "type_a": key[0], "type_b": key[1],
                "confusion_count": total, "a_to_b": c_fwd, "b_to_a": c_bwd,
                "scs_minilm": round(scs_m, 4) if scs_m is not None else None,
                "scs_qwen3": round(scs_q, 4) if scs_q is not None else None,
            })

    pairs.sort(key=lambda x: x["confusion_count"], reverse=True)
    return pairs[:n]


def get_top_scs_pairs(type_names, sim_matrix, n=20):
    pairs = []
    for i in range(len(type_names)):
        for j in range(i + 1, len(type_names)):
            pairs.append({
                "type_a": type_names[i], "type_b": type_names[j],
                "scs": round(float(sim_matrix[i, j]), 4)
            })
    pairs.sort(key=lambda x: x["scs"], reverse=True)
    return pairs[:n]


def compute_centrality(type_names, sim_matrix):
    n = len(type_names)
    centrality = {}
    for i in range(n):
        mean_sim = (sim_matrix[i].sum() - sim_matrix[i, i]) / (n - 1)
        centrality[type_names[i]] = round(float(mean_sim), 4)
    return centrality


def annotate_pairs(pairs):
    for p in pairs:
        key = tuple(sorted([p["type_a"], p["type_b"]]))
        ann = SEMANTIC_ANNOTATIONS.get(key, {})
        p["semantic_relation"] = ann.get("relation", "unclassified")
        p["note"] = ann.get("note", "")
        p["category"] = ann.get("category", "unclassified")
    return pairs


def main():
    print("Loading data...")
    names_m, sim_m = load_sim_matrix(MINILM_SIM)
    names_q, sim_q = load_sim_matrix(QWEN3_SIM)
    samples = load_maven_samples()
    with open(PREDICTIONS) as f:
        predictions = json.load(f)

    type_to_idx_m = {t: i for i, t in enumerate(names_m)}
    type_to_idx_q = {t: i for i, t in enumerate(names_q)}

    assert set(names_m) == set(names_q), "Type name mismatch"
    type_to_idx = type_to_idx_m
    q_reindex = [type_to_idx_q[t] for t in names_m]
    sim_q_aligned = sim_q[np.ix_(q_reindex, q_reindex)]

    print("Building confusion matrix...")
    confusion, gold_counts = build_confusion(predictions, samples)
    total_conf = sum(v for d in confusion.values() for v in d.values())
    print(f"  Total confusion events: {total_conf}")
    print(f"  Types with confusions: {len(confusion)}")

    print("\nTop-10 confused pairs:")
    top_confused = get_top_confused(confusion, gold_counts, type_to_idx, sim_m, sim_q_aligned, n=20)
    top_confused = annotate_pairs(top_confused)
    print(f"{'Rank':<5} {'Type A':<35} {'Type B':<25} {'Conf':<6} {'MiniLM':<8} {'Qwen3':<8} {'Category':<12} {'Relation'}")
    print("-" * 130)
    for i, p in enumerate(top_confused[:10]):
        print(f"{i+1:<5} {p['type_a']:<35} {p['type_b']:<25} {p['confusion_count']:<6} "
              f"{p['scs_minilm']:<8} {p['scs_qwen3']:<8} {p['category']:<12} {p['semantic_relation']}")

    print("\nTop-10 MiniLM SCS pairs:")
    top_scs_minilm = get_top_scs_pairs(names_m, sim_m, n=20)
    for p in top_scs_minilm:
        key = tuple(sorted([p["type_a"], p["type_b"]]))
        c1 = confusion.get(key[0], {}).get(key[1], 0)
        c2 = confusion.get(key[1], {}).get(key[0], 0)
        p["confusion_count"] = c1 + c2
    top_scs_minilm = annotate_pairs(top_scs_minilm)
    print(f"{'Rank':<5} {'Type A':<35} {'Type B':<25} {'SCS':<8} {'Conf':<6} {'Category':<12} {'Relation'}")
    print("-" * 110)
    for i, p in enumerate(top_scs_minilm[:10]):
        print(f"{i+1:<5} {p['type_a']:<35} {p['type_b']:<25} {p['scs']:<8} "
              f"{p['confusion_count']:<6} {p['category']:<12} {p.get('semantic_relation','')}")

    centrality_m = compute_centrality(names_m, sim_m)

    confused_types = set()
    for p in top_confused[:10]:
        confused_types.add(p["type_a"])
        confused_types.add(p["type_b"])
    cent_vals = [centrality_m[t] for t in confused_types]
    all_cent_vals = list(centrality_m.values())
    print(f"\nCentrality analysis (MiniLM):")
    print(f"  Top-10 confused types mean centrality: {np.mean(cent_vals):.4f}")
    print(f"  All types mean centrality: {np.mean(all_cent_vals):.4f}")
    print(f"  Top-10 confused types are {np.mean(cent_vals)/np.mean(all_cent_vals):.2f}x more central")

    # Top/bottom centrality types
    sorted_cent = sorted(centrality_m.items(), key=lambda x: -x[1])
    print(f"\n  Top-5 central types: {[(t, c) for t,c in sorted_cent[:5]]}")
    print(f"  Bottom-5 central types: {[(t, c) for t,c in sorted_cent[-5:]]}")
    # How many of top-10 confused types are in top quartile centrality?
    top_q = set(t for t, _ in sorted_cent[:42])
    in_top_q = confused_types & top_q
    print(f"  Of {len(confused_types)} types in top-10 confused pairs, {len(in_top_q)} are in top-quartile centrality")

    categories = defaultdict(int)
    for p in top_confused[:10]:
        categories[p["category"]] += 1
    print(f"\nCategory breakdown (top-10 confused pairs):")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}/10")

    top_scs_set = {tuple(sorted([p["type_a"], p["type_b"]])) for p in top_scs_minilm[:10]}
    top_conf_set = {tuple(sorted([p["type_a"], p["type_b"]])) for p in top_confused[:10]}
    overlap = top_scs_set & top_conf_set
    print(f"\nOverlap between top-10 SCS and top-10 confused: {len(overlap)}/10")
    if overlap:
        for pair in overlap:
            print(f"  {pair[0]} <-> {pair[1]}")

    all_confused = get_top_confused(confusion, gold_counts, type_to_idx, sim_m, sim_q_aligned, n=1000)
    if len(all_confused) > 10:
        from scipy import stats
        scs_vals = [p["scs_minilm"] for p in all_confused if p["scs_minilm"] is not None]
        conf_vals = [p["confusion_count"] for p in all_confused if p["scs_minilm"] is not None]
        rho, pval = stats.spearmanr(scs_vals, conf_vals)
        print(f"\nSpearman rho (MiniLM SCS vs confusion count, nonzero pairs): {rho:.4f} (p={pval:.2e})")
        print(f"  N pairs = {len(scs_vals)}")

    output = {
        "top_10_confused_pairs": top_confused[:10],
        "top_20_confused_pairs": top_confused[:20],
        "top_10_scs_minilm_pairs": top_scs_minilm[:10],
        "top_20_scs_minilm_pairs": top_scs_minilm[:20],
        "centrality_stats": {
            "top10_confused_types_mean_centrality_minilm": round(float(np.mean(cent_vals)), 4),
            "all_types_mean_centrality_minilm": round(float(np.mean(all_cent_vals)), 4),
            "ratio": round(float(np.mean(cent_vals) / np.mean(all_cent_vals)), 4),
        },
        "category_breakdown_top10": dict(categories),
        "top_scs_vs_top_confused_overlap": len(overlap),
        "overlap_pairs": [list(p) for p in overlap],
        "total_confusion_events": total_conf,
        "n_confused_pairs": len(all_confused),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
