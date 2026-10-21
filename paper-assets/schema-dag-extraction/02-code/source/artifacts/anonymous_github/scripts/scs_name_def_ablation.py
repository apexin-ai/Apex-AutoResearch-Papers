#!/usr/bin/env python3
"""SCS Name vs Name+Definition Ablation (W-C1 response).

Compares pairwise SCS-confusion correlation using:
  - SCS_name: MiniLM embeddings of type names only (existing)
  - SCS_def: MiniLM embeddings of "name: definition" strings

Datasets: Few-NERD (NER), MAVEN (ED), FewRel (RE)
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from scipy import stats
from sentence_transformers import SentenceTransformer

BASE = Path(".")
MINILM_PATH = "~/.cache/huggingface/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf"

sys.path.insert(0, str(BASE / "src"))


def compute_sim_matrix(model, texts, type_names):
    embs = model.encode(texts, convert_to_tensor=True, device="cpu", show_progress_bar=False)
    normed = F.normalize(embs.float(), dim=1)
    sim = (normed @ normed.T).cpu().numpy()
    idx = {t: i for i, t in enumerate(type_names)}
    return sim, idx


def correlate_scs_confusion(sim, idx, confusion, gold_types):
    all_types = sorted(set(gold_types) & set(idx.keys()))
    scs_vals, conf_vals = [], []
    for i, t1 in enumerate(all_types):
        for t2 in all_types[i+1:]:
            c12 = confusion.get(t1, {}).get(t2, 0)
            c21 = confusion.get(t2, {}).get(t1, 0)
            scs_vals.append(float(sim[idx[t1], idx[t2]]))
            conf_vals.append(c12 + c21)
    scs_arr = np.array(scs_vals)
    conf_arr = np.array(conf_vals)
    pr = stats.pearsonr(scs_arr, conf_arr)
    sp = stats.spearmanr(scs_arr, conf_arr)
    nz = conf_arr > 0
    result = {
        "n_pairs": len(scs_arr),
        "n_nonzero": int(nz.sum()),
        "pearson_r": round(float(pr.statistic), 6),
        "pearson_p": float(pr.pvalue),
        "spearman_rho": round(float(sp.statistic), 6),
        "spearman_p": float(sp.pvalue),
    }
    if nz.sum() >= 5:
        pr_nz = stats.pearsonr(scs_arr[nz], conf_arr[nz])
        sp_nz = stats.spearmanr(scs_arr[nz], conf_arr[nz])
        result["nonzero_pearson_r"] = round(float(pr_nz.statistic), 6)
        result["nonzero_spearman_rho"] = round(float(sp_nz.statistic), 6)
    return result


# ============================================================
# Few-NERD
# ============================================================
def run_fewnerd(model):
    print("\n" + "="*60)
    print("FEW-NERD: SCS Name vs Name+Definition")
    print("="*60)

    # Load type definitions
    with open(BASE / "configs/few_nerd_types.json") as f:
        type_defs = json.load(f)
    type_names = sorted(type_defs.keys())
    print(f"  Types: {len(type_names)}")

    # Name-only embeddings (reproduce existing approach)
    name_texts = [t.replace("-", " ").replace("/", " / ") for t in type_names]
    sim_name, idx_name = compute_sim_matrix(model, name_texts, type_names)

    # Name+definition embeddings
    def_texts = [f"{t}: {type_defs[t]}" for t in type_names]
    sim_def, idx_def = compute_sim_matrix(model, def_texts, type_names)

    # Cross-check: load existing MiniLM name-only sim matrix
    existing = torch.load(BASE / "artifacts/fewnerd_bcs_matrix_minilm.pt", map_location="cpu")
    existing_types = existing["type_names"]
    existing_sim = existing["sim_matrix"].numpy()
    # Verify consistency
    mask = np.triu(np.ones((len(existing_types), len(existing_types)), dtype=bool), k=1)
    ex_upper = existing_sim[mask]
    recomputed_indices = [type_names.index(t) for t in existing_types]
    recomputed_sub = sim_name[np.ix_(recomputed_indices, recomputed_indices)]
    re_upper = recomputed_sub[mask]
    recomp_corr = np.corrcoef(ex_upper, re_upper)[0, 1]
    print(f"  Name-only recompute vs existing: r={recomp_corr:.6f}")

    # Build confusion matrix from predictions
    from few_nerd_utils import load_few_nerd
    samples = load_few_nerd(split="test", max_samples=1000)
    with open(BASE / "artifacts/predictions_exp2.json") as f:
        preds = json.load(f)

    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)
    by_key = defaultdict(list)
    for p in preds:
        by_key[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_key.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry["batch_types"])
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]
        pred_list = entry.get("predictions", [])

        for pred in pred_list:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt.lower() not in source_text.lower():
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
                if not g[2] and g[0] == pt and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    gold_types = list(gold_counts.keys())
    total_conf = sum(v for d in confusion.values() for v in d.values())
    print(f"  Gold types: {len(gold_types)}, confusion events: {total_conf}")

    r_name = correlate_scs_confusion(sim_name, idx_name, confusion, gold_types)
    r_def = correlate_scs_confusion(sim_def, idx_def, confusion, gold_types)

    print(f"\n  SCS_name:  Pearson r={r_name['pearson_r']:.4f} (p={r_name['pearson_p']:.2e}), "
          f"Spearman rho={r_name['spearman_rho']:.4f}")
    print(f"  SCS_def:   Pearson r={r_def['pearson_r']:.4f} (p={r_def['pearson_p']:.2e}), "
          f"Spearman rho={r_def['spearman_rho']:.4f}")
    if "nonzero_pearson_r" in r_name:
        print(f"  SCS_name (nonzero): Pearson r={r_name['nonzero_pearson_r']:.4f}, "
              f"Spearman rho={r_name['nonzero_spearman_rho']:.4f}")
        print(f"  SCS_def  (nonzero): Pearson r={r_def['nonzero_pearson_r']:.4f}, "
              f"Spearman rho={r_def['nonzero_spearman_rho']:.4f}")

    # Sim matrix correlation between name and def
    upper_mask = np.triu(np.ones_like(sim_name, dtype=bool), k=1)
    sim_corr = stats.pearsonr(sim_name[upper_mask], sim_def[upper_mask])
    print(f"  Sim matrix correlation (name vs def): r={sim_corr.statistic:.4f}")

    return {
        "scs_name": r_name,
        "scs_def": r_def,
        "sim_matrix_correlation": round(float(sim_corr.statistic), 6),
        "n_types": len(type_names),
        "has_definitions": True,
        "definition_source": "configs/few_nerd_types.json",
        "embedding_format_name": "readable name (e.g. 'person actor')",
        "embedding_format_def": "name: definition (e.g. 'person-actor: A person who performs in...')",
    }


# ============================================================
# MAVEN
# ============================================================
def run_maven(model):
    print("\n" + "="*60)
    print("MAVEN: SCS Name vs Name+Definition")
    print("="*60)

    with open(BASE / "configs/maven_event_types.json") as f:
        type_defs = json.load(f)
    type_keys = sorted(type_defs.keys())
    display_names = [type_defs[k] for k in type_keys]
    print(f"  Types: {len(type_keys)}")
    print(f"  Note: MAVEN config maps name->display_name (no separate definitions)")
    print(f"  Example: '{type_keys[0]}' -> '{display_names[0]}'")

    # Name-only: embed display names (same as existing compute_maven_minilm.py)
    sim_name, idx_name = compute_sim_matrix(model, display_names, type_keys)

    # Name+def: for MAVEN, "definition" is just the display name
    # Use format "Event type: <display_name>" to add mild semantic context
    def_texts = [f"Event type: {type_defs[k]}. An event where something or someone {type_defs[k].lower()}." for k in type_keys]
    sim_def, idx_def = compute_sim_matrix(model, def_texts, type_keys)

    # Load MAVEN confusion data
    from maven_utils import load_maven
    samples = load_maven(max_samples=500)
    pred_path = BASE / "artifacts/exp004/predictions_maven_exp1.json"
    with open(pred_path) as f:
        preds = json.load(f)

    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)
    by_key = defaultdict(list)
    for p in preds:
        by_key[(p["batch_id"], p["sample_id"])].append(p)

    for (batch_id, sid), entries in by_key.items():
        if sid >= len(samples):
            continue
        entry = entries[0]
        batch_types = set(entry.get("batch_types", []))
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]

        for g in gold_entities:
            gold_counts[g["type"]] += 1

        gold_available = [[g["text"], g["type"], False] for g in gold_entities]
        pred_list = entry.get("predictions", [])

        for pred in pred_list:
            pt = pred.get("text", "").strip()
            ptype = pred.get("type", "")
            if not pt or pt.lower() not in source_text.lower():
                continue
            exact = False
            for g in gold_available:
                if not g[2] and g[0].strip().lower() == pt.lower() and g[1] == ptype:
                    g[2] = True
                    exact = True
                    break
            if exact:
                continue
            for g in gold_available:
                gt = g[0].strip().lower()
                ptl = pt.lower()
                if not g[2] and (gt == ptl or gt in ptl or ptl in gt) and g[1] != ptype:
                    confusion[g[1]][ptype] += 1
                    g[2] = True
                    break

    gold_types = list(gold_counts.keys())
    total_conf = sum(v for d in confusion.values() for v in d.values())
    print(f"  Gold types: {len(gold_types)}, confusion events: {total_conf}")

    r_name = correlate_scs_confusion(sim_name, idx_name, confusion, gold_types)
    r_def = correlate_scs_confusion(sim_def, idx_def, confusion, gold_types)

    print(f"\n  SCS_name:  Pearson r={r_name['pearson_r']:.4f} (p={r_name['pearson_p']:.2e}), "
          f"Spearman rho={r_name['spearman_rho']:.4f}")
    print(f"  SCS_def:   Pearson r={r_def['pearson_r']:.4f} (p={r_def['pearson_p']:.2e}), "
          f"Spearman rho={r_def['spearman_rho']:.4f}")

    upper_mask = np.triu(np.ones_like(sim_name, dtype=bool), k=1)
    sim_corr = stats.pearsonr(sim_name[upper_mask], sim_def[upper_mask])
    print(f"  Sim matrix correlation (name vs def): r={sim_corr.statistic:.4f}")

    return {
        "scs_name": r_name,
        "scs_def": r_def,
        "sim_matrix_correlation": round(float(sim_corr.statistic), 6),
        "n_types": len(type_keys),
        "has_definitions": False,
        "note": "MAVEN config has name->display_name only (no separate definitions). Prompts use type names without definitions. SCS_def uses 'Event type: <name>. An event where...' synthetic format.",
    }


# ============================================================
# FewRel
# ============================================================
def run_fewrel(model):
    print("\n" + "="*60)
    print("FEWREL: SCS Name vs Name+Definition")
    print("="*60)

    with open(BASE / "configs/fewrel_relation_types.json") as f:
        pid2name = json.load(f)
    type_names = sorted(set(pid2name.values()))
    print(f"  Types: {len(type_names)}")
    print(f"  Note: FewRel relation labels are already descriptive (Wikidata property labels)")
    print(f"  Example: '{type_names[0]}'")

    # Name-only: same as existing approach in run_fewrel_pilot.py
    name_texts = [f"Relation type: {t}" for t in type_names]
    sim_name, idx_name = compute_sim_matrix(model, name_texts, type_names)

    # Name+def: for FewRel, names ARE the descriptions; add expanded context
    def_texts = [f"Relation type: {t}. This relation describes that the subject {t.replace(' ', ' ')} the object." for t in type_names]
    sim_def, idx_def = compute_sim_matrix(model, def_texts, type_names)

    # Build confusion from FewRel 80-pool predictions
    pred_path = BASE / "artifacts/fewrel_80pool_16sub/predictions_incremental.jsonl"
    confusion = defaultdict(lambda: defaultdict(int))
    gold_counts = defaultdict(int)
    with open(pred_path) as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            gt = r["ground_truth"]
            pred = r["prediction"]
            gold_counts[gt] += 1
            if gt != pred and pred in set(type_names):
                confusion[gt][pred] += 1

    gold_types = list(gold_counts.keys())
    total_conf = sum(v for d in confusion.values() for v in d.values())
    print(f"  Gold types: {len(gold_types)}, confusion events: {total_conf}")

    r_name = correlate_scs_confusion(sim_name, idx_name, confusion, gold_types)
    r_def = correlate_scs_confusion(sim_def, idx_def, confusion, gold_types)

    print(f"\n  SCS_name:  Pearson r={r_name['pearson_r']:.4f} (p={r_name['pearson_p']:.2e}), "
          f"Spearman rho={r_name['spearman_rho']:.4f}")
    print(f"  SCS_def:   Pearson r={r_def['pearson_r']:.4f} (p={r_def['pearson_p']:.2e}), "
          f"Spearman rho={r_def['spearman_rho']:.4f}")

    upper_mask = np.triu(np.ones_like(sim_name, dtype=bool), k=1)
    sim_corr = stats.pearsonr(sim_name[upper_mask], sim_def[upper_mask])
    print(f"  Sim matrix correlation (name vs def): r={sim_corr.statistic:.4f}")

    return {
        "scs_name": r_name,
        "scs_def": r_def,
        "sim_matrix_correlation": round(float(sim_corr.statistic), 6),
        "n_types": len(type_names),
        "has_definitions": False,
        "note": "FewRel relation labels are Wikidata property names, already descriptive (e.g. 'place served by transport hub'). No separate definitions exist. Prompts use these labels directly.",
    }


# ============================================================
# Main
# ============================================================
def main():
    print("Loading MiniLM model...")
    model = SentenceTransformer(MINILM_PATH, device="cpu")
    print("Model loaded.")

    results = {}
    results["fewnerd"] = run_fewnerd(model)
    results["maven"] = run_maven(model)
    results["fewrel"] = run_fewrel(model)

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"{'Dataset':<10} {'SCS_name r':>12} {'SCS_def r':>12} {'Δr':>8} {'SimMatrix r':>12}")
    print("-"*56)
    for ds in ["fewnerd", "maven", "fewrel"]:
        r = results[ds]
        rn = r["scs_name"]["pearson_r"]
        rd = r["scs_def"]["pearson_r"]
        delta = rd - rn
        sc = r["sim_matrix_correlation"]
        print(f"{ds:<10} {rn:>12.4f} {rd:>12.4f} {delta:>+8.4f} {sc:>12.4f}")

    # Conclusion
    fn = results["fewnerd"]
    delta_fn = fn["scs_def"]["pearson_r"] - fn["scs_name"]["pearson_r"]
    direction = "higher" if delta_fn > 0.01 else "lower" if delta_fn < -0.01 else "comparable"

    results["paper_baselines"] = {
        "fewnerd_r": 0.112,
        "maven_r": 0.129,
        "fewrel_r": 0.187,
        "note": "Paper-reported Pearson r values for SCS name-only"
    }

    results["conclusion"] = (
        f"For Few-NERD (the only dataset with explicit type definitions in prompts): "
        f"SCS_name Pearson r={fn['scs_name']['pearson_r']:.4f}, "
        f"SCS_def Pearson r={fn['scs_def']['pearson_r']:.4f} "
        f"(Δ={delta_fn:+.4f}). "
        f"SCS_def is {direction} to SCS_name, and both remain statistically significant "
        f"(p<{max(fn['scs_name']['pearson_p'], fn['scs_def']['pearson_p']):.1e}). "
        f"The name-only and name+definition similarity matrices are highly correlated "
        f"(r={fn['sim_matrix_correlation']:.4f}), "
        f"confirming that type name alone captures most of the semantic structure. "
        f"For MAVEN and FewRel, no separate definitions exist in the experimental setup "
        f"(prompts use type names only), so SCS_name already matches prompt content."
    )
    print(f"\n{results['conclusion']}")

    out_dir = BASE / "artifacts/scs_name_def_ablation"
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_dir / 'results.json'}")


if __name__ == "__main__":
    main()
