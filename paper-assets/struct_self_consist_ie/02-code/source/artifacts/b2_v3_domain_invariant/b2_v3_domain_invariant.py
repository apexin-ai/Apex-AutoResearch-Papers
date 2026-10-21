#!/usr/bin/env python3
"""B2-v3: Domain-Invariant Features Only Entity Verifier.

Removes all dataset-specific features (dataset_enc, entity_type_enc,
regime_enc, model_size_log) to test whether a domain-invariant verifier
can generalize better across datasets than B2-v2.

Leave-one-dataset-out CV with 3 folds + comparison to B2-v2 baselines.
"""

import json, os, re, math, time, sys
import numpy as np
from collections import Counter, defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = f"{BASE}/artifacts/b2_v3_domain_invariant"
os.makedirs(OUT, exist_ok=True)

CONFIGS = [
    dict(name="conll_7b_s42",  path=f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=False),
    dict(name="conll_7b_s123", path=f"{BASE}/output/exp_002_conll_n16_seed123/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=True),
    dict(name="conll_7b_s456", path=f"{BASE}/output/exp_002_conll_n16_seed456/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=True),
    dict(name="scierc_7b_s42",  path=f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="scierc_7b_s123", path=f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="scierc_7b_s456", path=f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="fewnerd_7b_s123", path=f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_7b_s456", path=f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_7b_s789", path=f"{BASE}/output/fewnerd_seed789_merged/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
]

FEWNERD_MAX = 3000
DATASETS = ["conll", "scierc", "fewnerd"]

# Domain-invariant features ONLY — removed: entity_type_enc, model_size_log, dataset_enc, regime_enc
FEAT_COLS = [
    "agreement_count", "vc", "lp_token", "lp_span", "sample_mean_lp",
    "sj", "entity_length", "entity_char_length", "entity_position",
]

# B2-v2 baselines for comparison
B2_V2_BASELINES = {
    "fold1_test_conll":  {"xgb_auc": 0.9391, "lgb_auc": 0.9378, "xgb_ece": 0.0304, "lgb_ece": 0.0304},
    "fold2_test_scierc": {"xgb_auc": 0.7910, "lgb_auc": 0.8006, "xgb_ece": 0.1450, "lgb_ece": 0.1274},
    "fold3_test_fewnerd":{"xgb_auc": 0.8603, "lgb_auc": 0.8477, "xgb_ece": 0.1556, "lgb_ece": 0.1357},
}


# ================================================================
# Feature extraction (reused from B2-v2, minus domain features)
# ================================================================

def load_data(path, maxn=None):
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if not obj["gold"]["entities"]:
                continue
            out.append(obj)
            if maxn and len(out) >= maxn:
                break
    return out


def precompute_text_regions(sample):
    tt = sample.get("token_texts")
    tl = sample.get("token_logprobs")
    if not tt or not tl:
        return None
    full = "".join(tt)
    cs = []
    p = 0
    for t in tt:
        cs.append(p)
        p += len(t)
    regions = []
    for m in re.finditer(r'"text"\s*:\s*"', full):
        vs = m.end()
        ve = vs
        while ve < len(full) and not (full[ve] == '"' and (ve == 0 or full[ve - 1] != '\\')):
            ve += 1
        regions.append((vs, ve))
    return {"cs": cs, "tt": tt, "tl": tl, "regions": regions}


def entity_token_lp(pre, eidx):
    if pre is None or eidx >= len(pre["regions"]):
        return None, None
    vs, ve = pre["regions"][eidx]
    cs, tt, tl = pre["cs"], pre["tt"], pre["tl"]
    idxs = [i for i in range(len(tt)) if cs[i] < ve and cs[i] + len(tt[i]) > vs]
    if not idxs:
        return None, None
    lps = [tl[i] for i in idxs if i < len(tl)]
    return (float(np.mean(lps)), float(np.sum(lps))) if lps else (None, None)


def per_sample_sj(samples):
    N = len(samples)
    if N <= 1:
        return [1.0] * N
    sets = [{(e["start"], e["end"], e["type"]) for e in s.get("entities", [])} for s in samples]
    out = []
    for i in range(N):
        t = 0.0
        for j in range(N):
            if i == j:
                continue
            u = sets[i] | sets[j]
            t += len(sets[i] & sets[j]) / len(u) if u else 1.0
        out.append(t / (N - 1))
    return out


def get_sample_lp(sample, inst, si):
    lp = sample.get("mean_logprob")
    if lp is None and "logprobs" in inst and si < len(inst["logprobs"]):
        lp = inst["logprobs"][si]
    return lp


def process_config(cfg):
    maxn = FEWNERD_MAX if cfg["ds"] == "fewnerd" else None
    insts = load_data(cfg["path"], maxn)
    print(f"  {cfg['name']}: {len(insts)} inst", flush=True)

    results = []
    for inst in insts:
        samples = inst["samples"]
        gold = inst["gold"]["entities"]
        text = inst["text"]
        tlen = max(len(text), 1)
        N = len(samples)

        gold_set = {(e["start"], e["end"], e["type"]) for e in gold}
        sj_scores = per_sample_sj(samples)

        span_cnt = Counter()
        span_si = defaultdict(list)
        span_text = {}
        text_vc = Counter()

        for si, s in enumerate(samples):
            seen_s, seen_t = set(), set()
            for e in s.get("entities", []):
                k = (e["start"], e["end"], e["type"])
                tk = (e["text"].lower(), e["type"])
                if k not in seen_s:
                    span_cnt[k] += 1
                    span_si[k].append(si)
                    span_text[k] = e["text"]
                    seen_s.add(k)
                if tk not in seen_t:
                    text_vc[tk] += 1
                    seen_t.add(tk)

        ent_tlp = defaultdict(list)
        if cfg["tok"]:
            for si, s in enumerate(samples):
                pre = precompute_text_regions(s)
                if pre is None:
                    continue
                for ei, e in enumerate(s.get("entities", [])):
                    k = (e["start"], e["end"], e["type"])
                    lt, ls = entity_token_lp(pre, ei)
                    if lt is not None:
                        ent_tlp[k].append((lt, ls))

        candidates = []
        for k, cnt in span_cnt.items():
            st, en, ety = k
            etxt = span_text[k]
            tk = (etxt.lower(), ety)

            if k in ent_tlp and ent_tlp[k]:
                lpt = float(np.mean([x[0] for x in ent_tlp[k]]))
                lps = float(np.mean([x[1] for x in ent_tlp[k]]))
            else:
                lpt = lps = float('nan')

            slps = [lp for si in span_si[k] if (lp := get_sample_lp(samples[si], inst, si)) is not None]
            smlp = float(np.mean(slps)) if slps else float('nan')

            csj = [sj_scores[si] for si in span_si[k]]

            candidates.append({
                "key": k,
                "text": etxt,
                "features": np.array([
                    cnt,                          # agreement_count
                    text_vc.get(tk, cnt),         # vc
                    lpt,                          # lp_token
                    lps,                          # lp_span
                    smlp,                         # sample_mean_lp
                    float(np.mean(csj)),          # sj
                    len(etxt.split()),            # entity_length
                    len(etxt),                    # entity_char_length
                    st / tlen,                    # entity_position
                ], dtype=np.float64),
                "label": 1 if k in gold_set else 0,
            })

        results.append({
            "config": cfg["name"],
            "iid": inst["id"],
            "dataset": cfg["ds"],
            "gold_set": gold_set,
            "greedy_ents": inst.get("greedy", {}).get("entities", []),
            "N": N,
            "candidates": candidates,
        })

    return results


# ================================================================
# Evaluation helpers
# ================================================================

def prf(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f, 4)}


def eval_sets(pred_set, gold_set):
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    return tp, fp, fn


def eval_greedy(data):
    tp = fp = fn = 0
    for d in data:
        ps = {(e["start"], e["end"], e["type"]) for e in d["greedy_ents"]}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def eval_majority_vote(data, threshold=0.5):
    tp = fp = fn = 0
    for d in data:
        N = d["N"]
        ps = {c["key"] for c in d["candidates"] if c["features"][0] / N > threshold}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def eval_path_a(data, model_key, threshold):
    tp = fp = fn = 0
    for d in data:
        ps = {c["key"] for c in d["candidates"]
              if c[model_key] * c["features"][0] > threshold}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def eval_path_b(data, model_key, construct_thresh=0.5, filter_thresh=0.5):
    tp = fp = fn = 0
    for d in data:
        N = d["N"]
        mv = {c["key"] for c in d["candidates"] if c["features"][0] / N > construct_thresh}
        ps = {c["key"] for c in d["candidates"] if c["key"] in mv and c[model_key] >= filter_thresh}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def compute_ece(y_true, y_prob, n_bins=10):
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        mask = (y_prob > bins[i]) & (y_prob <= bins[i + 1])
        if mask.sum() == 0:
            continue
        avg_conf = y_prob[mask].mean()
        avg_acc = y_true[mask].mean()
        ece += mask.sum() / len(y_true) * abs(avg_conf - avg_acc)
    return float(ece)


# ================================================================
# Main
# ================================================================

def main():
    t0 = time.time()
    print("=== B2-v3: Domain-Invariant Features Only Entity Verifier ===\n")
    print(f"Features ({len(FEAT_COLS)}): {FEAT_COLS}")
    print(f"Removed: entity_type_enc, model_size_log, dataset_enc, regime_enc\n")

    # --- 1. Load & process all configs ---
    print("Loading data...")
    all_data = []
    for cfg in CONFIGS:
        all_data.extend(process_config(cfg))

    total_cands = sum(len(d["candidates"]) for d in all_data)
    total_pos = sum(c["label"] for d in all_data for c in d["candidates"])
    print(f"\nTotal instances: {len(all_data)}")
    print(f"Entity candidates: {total_cands}  (pos={total_pos}, {100*total_pos/max(total_cands,1):.1f}%)")

    per_ds_stats = {}
    for ds in DATASETS:
        ds_data = [d for d in all_data if d["dataset"] == ds]
        nc = sum(len(d["candidates"]) for d in ds_data)
        np_ = sum(c["label"] for d in ds_data for c in d["candidates"])
        per_ds_stats[ds] = {"instances": len(ds_data), "candidates": nc, "positive": np_,
                            "pos_rate": round(np_ / max(nc, 1), 4)}
        print(f"  {ds}: {len(ds_data)} inst, {nc} cands ({np_} pos, {100*np_/max(nc,1):.1f}%)")

    # --- 2. Import ML libs ---
    import xgboost as xgb
    import lightgbm as lgb
    from sklearn.metrics import roc_auc_score

    # ================================================================
    # Fold 1-3: Leave-one-dataset-out
    # ================================================================
    fold_results = {}
    feature_importance_all = {}

    for fold_idx, test_ds in enumerate(DATASETS):
        fold_name = f"fold{fold_idx+1}_test_{test_ds}"
        train_ds_list = [d for d in DATASETS if d != test_ds]
        print(f"\n{'='*60}")
        print(f"Fold {fold_idx+1}: Train on {train_ds_list}, Test on [{test_ds}]")
        print(f"{'='*60}")

        train_data = [d for d in all_data if d["dataset"] != test_ds]
        test_data = [d for d in all_data if d["dataset"] == test_ds]

        train_X = np.array([c["features"] for d in train_data for c in d["candidates"]])
        train_y = np.array([c["label"] for d in train_data for c in d["candidates"]])
        test_X = np.array([c["features"] for d in test_data for c in d["candidates"]])
        test_y = np.array([c["label"] for d in test_data for c in d["candidates"]])

        print(f"  Train: {len(train_X)} entities ({int(train_y.sum())} pos)")
        print(f"  Test:  {len(test_X)} entities ({int(test_y.sum())} pos)")

        xgb_m = xgb.XGBClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            eval_metric="logloss", random_state=42, verbosity=0)
        xgb_m.fit(train_X, train_y)

        lgb_m = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1)
        lgb_m.fit(train_X, train_y)

        xgb_p = xgb_m.predict_proba(test_X)[:, 1]
        lgb_p = lgb_m.predict_proba(test_X)[:, 1]

        auc_xgb = roc_auc_score(test_y, xgb_p)
        auc_lgb = roc_auc_score(test_y, lgb_p)
        print(f"  AUC: XGB={auc_xgb:.4f}  LGB={auc_lgb:.4f}")

        ece_xgb = compute_ece(test_y, xgb_p)
        ece_lgb = compute_ece(test_y, lgb_p)
        print(f"  ECE: XGB={ece_xgb:.4f}  LGB={ece_lgb:.4f}")

        # Delta vs B2-v2
        v2 = B2_V2_BASELINES[fold_name]
        print(f"  vs B2-v2: XGB AUC Δ={auc_xgb - v2['xgb_auc']:+.4f}  LGB AUC Δ={auc_lgb - v2['lgb_auc']:+.4f}")
        print(f"  vs B2-v2: XGB ECE Δ={ece_xgb - v2['xgb_ece']:+.4f}  LGB ECE Δ={ece_lgb - v2['lgb_ece']:+.4f}")

        idx = 0
        for d in test_data:
            for c in d["candidates"]:
                c["xgb_p"] = float(xgb_p[idx])
                c["lgb_p"] = float(lgb_p[idx])
                idx += 1

        greedy = eval_greedy(test_data)
        mv50 = eval_majority_vote(test_data, 0.5)
        print(f"  Greedy F1: {greedy['f1']:.4f}  MV50 F1: {mv50['f1']:.4f}")

        best_pa = {"xgb": {"f1": 0}, "lgb": {"f1": 0}}
        for mk, mn in [("xgb_p", "xgb"), ("lgb_p", "lgb")]:
            for thresh in np.arange(0.5, 8.5, 0.5):
                r = eval_path_a(test_data, mk, thresh)
                if r["f1"] > best_pa[mn].get("f1", 0):
                    best_pa[mn] = {**r, "thresh": float(thresh)}

        best_pb = {"xgb": {"f1": 0}, "lgb": {"f1": 0}}
        for mk, mn in [("xgb_p", "xgb"), ("lgb_p", "lgb")]:
            for ft in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
                r = eval_path_b(test_data, mk, 0.5, ft)
                if r["f1"] > best_pb[mn].get("f1", 0):
                    best_pb[mn] = {**r, "thresh": float(ft)}

        for mn in ["xgb", "lgb"]:
            pa = best_pa[mn]
            pb = best_pb[mn]
            pa_delta = pa["f1"] - greedy["f1"]
            pb_delta = pb["f1"] - greedy["f1"]
            print(f"  {mn.upper()} PathA: F1={pa['f1']:.4f} (Δ={pa_delta:+.4f}, t={pa.get('thresh',0):.1f})")
            print(f"  {mn.upper()} PathB: F1={pb['f1']:.4f} (Δ={pb_delta:+.4f}, ft={pb.get('thresh',0):.1f})")

        xgb_imp = dict(zip(FEAT_COLS, [float(v) for v in xgb_m.feature_importances_]))
        lgb_imp = dict(zip(FEAT_COLS, [int(v) for v in lgb_m.feature_importances_]))
        feature_importance_all[fold_name] = {"xgb_gain": xgb_imp, "lgb_splits": lgb_imp}

        # Sort by importance for display
        xgb_sorted = sorted(xgb_imp.items(), key=lambda x: -x[1])
        print(f"  XGB top features: {', '.join(f'{k}={v:.3f}' for k, v in xgb_sorted[:5])}")

        fold_results[fold_name] = {
            "train_datasets": train_ds_list,
            "test_dataset": test_ds,
            "train_entities": len(train_X),
            "test_entities": len(test_X),
            "auc": {"xgb": round(auc_xgb, 4), "lgb": round(auc_lgb, 4)},
            "ece": {"xgb": round(ece_xgb, 4), "lgb": round(ece_lgb, 4)},
            "delta_vs_b2v2": {
                "auc_xgb": round(auc_xgb - v2["xgb_auc"], 4),
                "auc_lgb": round(auc_lgb - v2["lgb_auc"], 4),
                "ece_xgb": round(ece_xgb - v2["xgb_ece"], 4),
                "ece_lgb": round(ece_lgb - v2["lgb_ece"], 4),
            },
            "baselines": {"greedy": greedy, "majority_vote_50": mv50},
            "best_path_a": {mn: {k: round(v, 4) if isinstance(v, float) else v
                                 for k, v in best_pa[mn].items()} for mn in ["xgb", "lgb"]},
            "best_path_b": {mn: {k: round(v, 4) if isinstance(v, float) else v
                                 for k, v in best_pb[mn].items()} for mn in ["xgb", "lgb"]},
            "f1_delta_vs_greedy": {
                "path_a_xgb": round(best_pa["xgb"]["f1"] - greedy["f1"], 4),
                "path_a_lgb": round(best_pa["lgb"]["f1"] - greedy["f1"], 4),
                "path_b_xgb": round(best_pb["xgb"]["f1"] - greedy["f1"], 4),
                "path_b_lgb": round(best_pb["lgb"]["f1"] - greedy["f1"], 4),
            },
        }

    # ================================================================
    # Per-config AUC breakdown
    # ================================================================
    print(f"\n{'='*60}")
    print("Per-config AUC within LOO folds")
    print(f"{'='*60}")

    per_config_auc = {}
    for fold_idx, test_ds in enumerate(DATASETS):
        fold_name = f"fold{fold_idx+1}_test_{test_ds}"
        train_data = [d for d in all_data if d["dataset"] != test_ds]
        test_data = [d for d in all_data if d["dataset"] == test_ds]

        train_X = np.array([c["features"] for d in train_data for c in d["candidates"]])
        train_y = np.array([c["label"] for d in train_data for c in d["candidates"]])

        lgb_m = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1)
        lgb_m.fit(train_X, train_y)

        cfg_aucs = {}
        for cfg_name in sorted({d["config"] for d in test_data}):
            cd = [d for d in test_data if d["config"] == cfg_name]
            cX = np.array([c["features"] for d in cd for c in d["candidates"]])
            cy = np.array([c["label"] for d in cd for c in d["candidates"]])
            cp = lgb_m.predict_proba(cX)[:, 1]
            try:
                ca = roc_auc_score(cy, cp)
            except ValueError:
                ca = float('nan')
            cfg_aucs[cfg_name] = round(ca, 4)
            print(f"  {fold_name} | {cfg_name}: AUC={ca:.4f} ({len(cX)} ents)")

        per_config_auc[fold_name] = cfg_aucs

    # ================================================================
    # Feature importance analysis
    # ================================================================
    print(f"\n{'='*60}")
    print("Feature Importance Summary (across folds)")
    print(f"{'='*60}")

    avg_xgb_imp = {f: 0.0 for f in FEAT_COLS}
    for fn in feature_importance_all:
        for f, v in feature_importance_all[fn]["xgb_gain"].items():
            avg_xgb_imp[f] += v / len(feature_importance_all)

    for f, v in sorted(avg_xgb_imp.items(), key=lambda x: -x[1]):
        print(f"  {f:20s}: avg_gain={v:.4f}")

    # ================================================================
    # Feature stability (point-biserial correlation)
    # ================================================================
    print(f"\n{'='*60}")
    print("Feature Stability Across Domains")
    print(f"{'='*60}")

    stability = {}
    for feat_idx, feat_name in enumerate(FEAT_COLS):
        per_ds_corr = {}
        for ds in DATASETS:
            ds_X = np.array([c["features"] for d in all_data if d["dataset"] == ds for c in d["candidates"]])
            ds_y = np.array([c["label"] for d in all_data if d["dataset"] == ds for c in d["candidates"]])
            feat_vals = ds_X[:, feat_idx]
            valid = ~np.isnan(feat_vals)
            if valid.sum() < 10:
                per_ds_corr[ds] = float('nan')
                continue
            from scipy.stats import pointbiserialr
            r, _ = pointbiserialr(ds_y[valid], feat_vals[valid])
            per_ds_corr[ds] = round(float(r), 4)

        vals = [v for v in per_ds_corr.values() if not np.isnan(v)]
        cross_std = round(float(np.std(vals)), 4) if len(vals) > 1 else float('nan')
        stability[feat_name] = {
            "per_dataset_correlation": per_ds_corr,
            "cross_domain_std": cross_std,
            "mean_correlation": round(float(np.mean(vals)), 4) if vals else float('nan'),
        }
        print(f"  {feat_name:20s}: " +
              " | ".join(f"{ds}={per_ds_corr.get(ds, float('nan')):.4f}" for ds in DATASETS) +
              f"  std={cross_std:.4f}")

    # ================================================================
    # Comparison with B2 original
    # ================================================================
    b2_original = {
        "lgb_test_auc": 0.8335,
        "xgb_test_auc": 0.8282,
        "greedy_f1": 0.7321,
    }

    fold3 = fold_results["fold3_test_fewnerd"]
    print(f"\n{'='*60}")
    print("Comparison: B2-v3 vs B2-v2 vs B2-original (Fold 3: test FewNERD)")
    print(f"{'='*60}")
    print(f"  B2 orig   XGB AUC: {b2_original['xgb_test_auc']:.4f}  LGB AUC: {b2_original['lgb_test_auc']:.4f}")
    print(f"  B2-v2     XGB AUC: {B2_V2_BASELINES['fold3_test_fewnerd']['xgb_auc']:.4f}  LGB AUC: {B2_V2_BASELINES['fold3_test_fewnerd']['lgb_auc']:.4f}")
    print(f"  B2-v3     XGB AUC: {fold3['auc']['xgb']:.4f}  LGB AUC: {fold3['auc']['lgb']:.4f}")
    print(f"  v3 vs v2: XGB Δ={fold3['delta_vs_b2v2']['auc_xgb']:+.4f}  LGB Δ={fold3['delta_vs_b2v2']['auc_lgb']:+.4f}")

    # ================================================================
    # Save results
    # ================================================================
    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.0f}s")

    results = {
        "experiment": "B2-v3: Domain-Invariant Features Only",
        "features_used": FEAT_COLS,
        "features_removed": ["entity_type_enc", "model_size_log", "dataset_enc", "regime_enc"],
        "summary": {
            "total_instances": len(all_data),
            "total_candidates": total_cands,
            "positive_rate": round(total_pos / max(total_cands, 1), 4),
            "per_dataset": per_ds_stats,
            "n_features": len(FEAT_COLS),
            "n_configs": len(CONFIGS),
            "elapsed_seconds": round(elapsed, 1),
        },
        "fold_results": fold_results,
        "per_config_auc": per_config_auc,
        "feature_importance": feature_importance_all,
        "feature_stability": stability,
        "comparison": {
            "b2_original_fold3": b2_original,
            "b2_v2_fold3": {
                "xgb_auc": B2_V2_BASELINES["fold3_test_fewnerd"]["xgb_auc"],
                "lgb_auc": B2_V2_BASELINES["fold3_test_fewnerd"]["lgb_auc"],
            },
            "b2_v3_fold3": {
                "xgb_auc": fold3["auc"]["xgb"],
                "lgb_auc": fold3["auc"]["lgb"],
            },
        },
    }

    with open(f"{OUT}/results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved results.json")

    # Summary markdown
    md = []
    md.append("# B2-v3: Domain-Invariant Features Only Entity Verifier\n")
    md.append(f"**Date**: {time.strftime('%Y-%m-%d %H:%M')}")
    md.append(f"**Features** ({len(FEAT_COLS)}): {', '.join(FEAT_COLS)}")
    md.append(f"**Removed**: entity_type_enc, model_size_log, dataset_enc, regime_enc")
    md.append(f"**Total entities**: {total_cands} across {len(CONFIGS)} configs\n")

    md.append("## Leave-One-Dataset-Out Results\n")
    md.append("| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |")
    md.append("|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|")
    for fold_idx, test_ds in enumerate(DATASETS):
        fn = f"fold{fold_idx+1}_test_{test_ds}"
        fr = fold_results[fn]
        train_str = "+".join(fr["train_datasets"])
        best_f1 = max(
            fr["best_path_a"]["xgb"]["f1"], fr["best_path_a"]["lgb"]["f1"],
            fr["best_path_b"]["xgb"]["f1"], fr["best_path_b"]["lgb"]["f1"],
        )
        delta = best_f1 - fr["baselines"]["greedy"]["f1"]
        md.append(f"| {fold_idx+1} | {train_str} | {test_ds} | "
                  f"{fr['auc']['xgb']:.4f} | {fr['auc']['lgb']:.4f} | "
                  f"{fr['ece']['xgb']:.4f} | {fr['ece']['lgb']:.4f} | "
                  f"{fr['baselines']['greedy']['f1']:.4f} | {best_f1:.4f} | {delta:+.4f} |")

    md.append("\n## Comparison: v3 vs v2 vs Original (Fold 3: FewNERD)\n")
    md.append("| Version | Features | XGB AUC | LGB AUC | XGB ECE | LGB ECE |")
    md.append("|---------|----------|---------|---------|---------|---------|")
    md.append(f"| B2 orig | 13 (all) | {b2_original['xgb_test_auc']:.4f} | {b2_original['lgb_test_auc']:.4f} | - | - |")
    v2f3 = B2_V2_BASELINES["fold3_test_fewnerd"]
    md.append(f"| B2-v2   | 13 (all) | {v2f3['xgb_auc']:.4f} | {v2f3['lgb_auc']:.4f} | {v2f3['xgb_ece']:.4f} | {v2f3['lgb_ece']:.4f} |")
    md.append(f"| **B2-v3** | **{len(FEAT_COLS)} (invariant)** | **{fold3['auc']['xgb']:.4f}** | **{fold3['auc']['lgb']:.4f}** | **{fold3['ece']['xgb']:.4f}** | **{fold3['ece']['lgb']:.4f}** |")

    md.append("\n### AUC Delta (v3 - v2)\n")
    md.append("| Fold | XGB Δ | LGB Δ | ECE XGB Δ | ECE LGB Δ |")
    md.append("|------|-------|-------|-----------|-----------|")
    for fold_idx, test_ds in enumerate(DATASETS):
        fn = f"fold{fold_idx+1}_test_{test_ds}"
        d = fold_results[fn]["delta_vs_b2v2"]
        md.append(f"| {test_ds} | {d['auc_xgb']:+.4f} | {d['auc_lgb']:+.4f} | {d['ece_xgb']:+.4f} | {d['ece_lgb']:+.4f} |")

    md.append("\n## Feature Importance (XGB Gain, avg across folds)\n")
    md.append("| Feature | Avg Gain | Rank |")
    md.append("|---------|----------|------|")
    for rank, (f, v) in enumerate(sorted(avg_xgb_imp.items(), key=lambda x: -x[1]), 1):
        md.append(f"| {f} | {v:.4f} | {rank} |")

    md.append("\n## Feature Stability (Point-Biserial Correlation)\n")
    md.append("| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std |")
    md.append("|---------|-------|--------|---------|------------------|")
    for feat_name in FEAT_COLS:
        s = stability[feat_name]
        pc = s["per_dataset_correlation"]
        md.append(f"| {feat_name} | {pc.get('conll', float('nan')):.4f} | "
                  f"{pc.get('scierc', float('nan')):.4f} | {pc.get('fewnerd', float('nan')):.4f} | "
                  f"{s['cross_domain_std']:.4f} |")

    md.append("\n## Key Findings\n")
    md.append("1. **Cross-domain generalization**: Does removing domain features improve transfer?")
    f3d = fold3["delta_vs_b2v2"]
    if f3d["auc_lgb"] > 0:
        md.append(f"   - YES: Fold 3 LGB AUC improved by {f3d['auc_lgb']:+.4f}")
    else:
        md.append(f"   - NO: Fold 3 LGB AUC changed by {f3d['auc_lgb']:+.4f}")
    md.append(f"2. **Calibration**: ECE changes — {f3d['ece_lgb']:+.4f} (LGB), {f3d['ece_xgb']:+.4f} (XGB)")
    md.append(f"3. **Top features without domain info**: {', '.join(f for f, _ in sorted(avg_xgb_imp.items(), key=lambda x: -x[1])[:3])}")

    summary_md = "\n".join(md) + "\n"
    with open(f"{OUT}/summary.md", "w") as f:
        f.write(summary_md)
    print(f"Saved summary.md")

    print("\nDone.")


if __name__ == "__main__":
    main()
