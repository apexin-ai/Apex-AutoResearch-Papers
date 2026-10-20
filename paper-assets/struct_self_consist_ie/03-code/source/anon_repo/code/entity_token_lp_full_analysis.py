"""Entity-token LP full analysis: rho, AUROC, selection F1 for entity-only vs full-sequence LP."""

import json
import re
import sys
import numpy as np
from pathlib import Path
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evaluation import per_instance_f1


def load_data(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def classify_tokens(token_texts):
    """Classify each token into: entity_text, entity_type, entity_span, schema, relation, other.
    
    Approach: reconstruct full text, find character positions of entity field values
    using regex on the JSON string, then map char positions back to token indices.
    """
    n = len(token_texts)
    labels = ["schema"] * n
    
    # Build char-to-token mapping
    char_starts = []
    pos = 0
    for t in token_texts:
        char_starts.append(pos)
        pos += len(t)
    total_len = pos
    
    full_text = "".join(token_texts)
    
    def char_range_to_tokens(cstart, cend):
        """Return token indices that overlap [cstart, cend)."""
        indices = []
        for i in range(n):
            tok_start = char_starts[i]
            tok_end = tok_start + len(token_texts[i])
            if tok_start < cend and tok_end > cstart:
                indices.append(i)
        return indices
    
    # Find entities section
    ent_match = re.search(r'"entities"\s*:\s*\[', full_text)
    rel_match = re.search(r'"relations"\s*:\s*\[', full_text)
    
    if not ent_match:
        return labels
    
    ent_start = ent_match.end()
    ent_end = rel_match.start() if rel_match else total_len
    entities_section = full_text[ent_start:ent_end]
    
    # Find each entity object's field values within the entities section
    # Pattern: "text": "VALUE", "type": "VALUE", "start": NUM, "end": NUM
    offset = ent_start
    
    for m in re.finditer(r'"text"\s*:\s*"((?:[^"\\]|\\.)*)"', entities_section):
        val_start = offset + m.start(1)
        val_end = offset + m.end(1)
        for i in char_range_to_tokens(val_start, val_end):
            labels[i] = "entity_text"
    
    for m in re.finditer(r'"type"\s*:\s*"((?:[^"\\]|\\.)*)"', entities_section):
        val_start = offset + m.start(1)
        val_end = offset + m.end(1)
        for i in char_range_to_tokens(val_start, val_end):
            labels[i] = "entity_type"
    
    for m in re.finditer(r'"(?:start|end)"\s*:\s*(\d+)', entities_section):
        val_start = offset + m.start(1)
        val_end = offset + m.end(1)
        for i in char_range_to_tokens(val_start, val_end):
            labels[i] = "entity_span"
    
    # Mark relation section tokens
    if rel_match:
        rel_start = rel_match.start()
        evt_match = re.search(r'"events"\s*:\s*\[', full_text)
        rel_end = evt_match.start() if evt_match else total_len
        for i in char_range_to_tokens(rel_start, rel_end):
            if labels[i] == "schema":
                labels[i] = "relation"
    
    return labels


def compute_ner_f1(pred_entities, gold_entities):
    pred_set = set()
    for e in pred_entities:
        pred_set.add((e.get("text", ""), e.get("type", ""), e.get("start", -1), e.get("end", -1)))
    gold_set = set()
    for e in gold_entities:
        gold_set.add((e.get("text", ""), e.get("type", ""), e.get("start", -1), e.get("end", -1)))
    tp = len(pred_set & gold_set)
    p = tp / max(len(pred_set), 1)
    r = tp / max(len(gold_set), 1)
    return 2 * p * r / max(p + r, 1e-10)


def mean_lp_for_labels(token_lps, labels, target_labels):
    """Mean logprob of tokens matching any label in target_labels."""
    vals = [token_lps[i] for i in range(len(token_lps)) if labels[i] in target_labels]
    if not vals:
        return None
    return float(np.mean(vals))


def analyze(data_path, dataset_name):
    data = load_data(data_path)
    
    instance_metrics = []
    all_sample_records = []
    
    token_count_stats = {"entity_text": [], "entity_type": [], "entity_span": [], "total": []}
    
    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if not gold_ents:
            continue
        samples = inst["samples"]
        if len(samples) < 2:
            continue
        
        sample_f1s = []
        lp_dict = {k: [] for k in ["full", "entity_text", "entity_type", "entity_span",
                                     "entity_all", "entity_text_type", "nonentity", "schema_only"]}
        
        valid = True
        for s in samples:
            token_lps = s.get("token_logprobs")
            token_texts = s.get("token_texts")
            if not token_lps or not token_texts:
                valid = False
                break
            
            f1 = compute_ner_f1(s.get("entities", []), gold_ents)
            sample_f1s.append(f1)
            lp_dict["full"].append(s["mean_logprob"])
            
            labels = classify_tokens(token_texts)
            
            n_et = sum(1 for l in labels if l == "entity_text")
            n_ty = sum(1 for l in labels if l == "entity_type")
            n_sp = sum(1 for l in labels if l == "entity_span")
            token_count_stats["entity_text"].append(n_et)
            token_count_stats["entity_type"].append(n_ty)
            token_count_stats["entity_span"].append(n_sp)
            token_count_stats["total"].append(len(labels))
            
            et = mean_lp_for_labels(token_lps, labels, {"entity_text"})
            ty = mean_lp_for_labels(token_lps, labels, {"entity_type"})
            sp = mean_lp_for_labels(token_lps, labels, {"entity_span"})
            ea = mean_lp_for_labels(token_lps, labels, {"entity_text", "entity_type", "entity_span"})
            ett = mean_lp_for_labels(token_lps, labels, {"entity_text", "entity_type"})
            ne = mean_lp_for_labels(token_lps, labels, {"schema", "relation"})
            sc = mean_lp_for_labels(token_lps, labels, {"schema"})
            
            for key, val in [("entity_text", et), ("entity_type", ty), ("entity_span", sp),
                             ("entity_all", ea), ("entity_text_type", ett),
                             ("nonentity", ne), ("schema_only", sc)]:
                lp_dict[key].append(val if val is not None else s["mean_logprob"])
        
        if not valid:
            continue
        
        sample_f1s = np.array(sample_f1s)
        
        def within_rho(lps):
            lps = np.array(lps)
            if np.std(lps) < 1e-12 or np.std(sample_f1s) < 1e-12:
                return np.nan
            return spearmanr(lps, sample_f1s).statistic
        
        inst_record = {"id": inst.get("id", ""), "n_samples": len(samples)}
        for key in lp_dict:
            inst_record[f"rho_{key}"] = within_rho(lp_dict[key])
        instance_metrics.append(inst_record)
        
        for j in range(len(samples)):
            rec = {"instance_id": inst.get("id", ""), "f1": sample_f1s[j]}
            for key in lp_dict:
                rec[f"{key}_lp"] = lp_dict[key][j]
            all_sample_records.append(rec)
    
    n_valid = len(instance_metrics)
    
    # Within-instance rho median
    def median_rho(key):
        vals = [m[f"rho_{key}"] for m in instance_metrics if not np.isnan(m[f"rho_{key}"])]
        return float(np.median(vals)) if vals else np.nan, len(vals)
    
    # Global Spearman rho
    all_f1 = np.array([r["f1"] for r in all_sample_records])
    def global_rho(key):
        vals = np.array([r[f"{key}_lp"] for r in all_sample_records])
        if np.std(vals) < 1e-12:
            return np.nan, 1.0
        rho, p = spearmanr(vals, all_f1)
        return float(rho), float(p)
    
    # AUROC
    median_f1 = np.median(all_f1)
    binary_labels = (all_f1 > median_f1).astype(int)
    def auroc(key):
        vals = np.array([r[f"{key}_lp"] for r in all_sample_records])
        if len(np.unique(binary_labels)) < 2 or np.std(vals) < 1e-12:
            return np.nan
        return float(roc_auc_score(binary_labels, vals))
    
    # Selection F1
    def selection_f1(key):
        sel_f1s = []
        # Group by instance
        from collections import OrderedDict
        inst_groups = OrderedDict()
        for r in all_sample_records:
            iid = r["instance_id"]
            if iid not in inst_groups:
                inst_groups[iid] = []
            inst_groups[iid].append(r)
        for iid, group in inst_groups.items():
            best_idx = max(range(len(group)), key=lambda j: group[j][f"{key}_lp"])
            sel_f1s.append(group[best_idx]["f1"])
        return float(np.mean(sel_f1s))
    
    # Oracle & greedy
    oracle_f1s = []
    greedy_f1_list = []
    for inst in data:
        gold_ents = inst["gold"].get("entities", [])
        if not gold_ents or len(inst["samples"]) < 2:
            continue
        if not all(s.get("token_logprobs") for s in inst["samples"]):
            continue
        f1s = [compute_ner_f1(s.get("entities", []), gold_ents) for s in inst["samples"]]
        oracle_f1s.append(max(f1s))
        greedy_f1_list.append(compute_ner_f1(inst["greedy"].get("entities", []), gold_ents))
    
    oracle_f1 = float(np.mean(oracle_f1s))
    greedy_f1 = float(np.mean(greedy_f1_list))
    
    lp_keys = ["full", "entity_text", "entity_type", "entity_span",
                "entity_all", "entity_text_type", "nonentity", "schema_only"]
    
    results = {
        "dataset": dataset_name,
        "n_valid": n_valid,
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
        "token_stats": {
            k: {"median": float(np.median(v)), "mean": float(np.mean(v))}
            for k, v in token_count_stats.items()
        },
    }
    
    for key in lp_keys:
        wm, wn = median_rho(key)
        gr, gp = global_rho(key)
        auc = auroc(key)
        sf = selection_f1(key)
        
        results[key] = {
            "within_rho_median": wm,
            "within_rho_n": wn,
            "global_rho": gr,
            "global_rho_p": gp,
            "auroc": auc,
            "selection_f1": sf,
            "sel_delta_greedy": sf - greedy_f1,
        }
    
    return results


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--data_path", required=True)
    p.add_argument("--dataset", default="scierc")
    p.add_argument("--output", default="output/entity_token_lp_full/results.json")
    args = p.parse_args()
    
    results = analyze(args.data_path, args.dataset)
    
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    
    ts = results["token_stats"]
    print(f"\n{'='*80}")
    print(f"  {args.dataset.upper()} Entity-Token LP Analysis (n={results['n_valid']})")
    print(f"  Greedy F1: {results['greedy_f1']:.4f}  |  Oracle F1: {results['oracle_f1']:.4f}")
    print(f"  Token counts (median): text={ts['entity_text']['median']:.0f}  type={ts['entity_type']['median']:.0f}  span={ts['entity_span']['median']:.0f}  total={ts['total']['median']:.0f}")
    print(f"{'='*80}")
    print(f"{'LP Variant':<20} {'Within-rho':>11} {'Global-rho':>11} {'AUROC':>8} {'Sel.F1':>8} {'D Greedy':>10}")
    print(f"{'-'*80}")
    
    for key in ["full", "entity_text", "entity_type", "entity_span",
                 "entity_all", "entity_text_type", "nonentity", "schema_only"]:
        m = results[key]
        name = key.replace("_", "-")
        print(f"{name:<20} {m['within_rho_median']:>11.4f} {m['global_rho']:>11.4f} {m['auroc']:>8.4f} {m['selection_f1']:>8.4f} {m['sel_delta_greedy']:>+10.4f}")
    
    print(f"{'='*80}")
    print(f"Results saved to {args.output}")
