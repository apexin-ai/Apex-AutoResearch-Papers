#!/usr/bin/env python3
"""B2-v4: Inverse-Frequency Weighted Entity Verifier.

Motivation: agreement_count, vc, sj have high discriminative power but
worst cross-domain stability (std=0.12-0.14). High-frequency entity types
dominate these features, hurting transfer.

Approach: normalize agreement_count and vc by inverse entity-type frequency
in the training set: feature_ifw = feature / log(1 + type_freq).
This downweights entities from common types where high agreement is expected.

Two variants:
  A) "replace" — swap agreement_count/vc with IFW versions (13 features)
  B) "augment" — add IFW features alongside originals (16 features)
"""

import json, os, re, math, time, sys
import numpy as np
from collections import Counter, defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = f"{BASE}/artifacts/b2_v4_inverse_freq"
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
DS_MAP = {"conll": 0, "scierc": 1, "fewnerd": 2}
REG_MAP = {"FT": 0, "ZS": 1, "FS": 2}
DATASETS = ["conll", "scierc", "fewnerd"]

FEAT_COLS_ORIG = [
    "agreement_count", "vc", "lp_token", "lp_span", "sample_mean_lp",
    "sj", "entity_type_enc", "entity_length", "entity_char_length",
    "entity_position", "model_size_log", "dataset_enc", "regime_enc",
]

FEAT_COLS_REPLACE = [
    "ac_ifw", "vc_ifw", "lp_token", "lp_span", "sample_mean_lp",
    "sj_ifw", "entity_type_enc", "entity_length", "entity_char_length",
    "entity_position", "model_size_log", "dataset_enc", "regime_enc",
]

FEAT_COLS_AUGMENT = FEAT_COLS_ORIG + ["ac_ifw", "vc_ifw", "sj_ifw"]


# ================================================================
# Feature extraction (from B2-v2)
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
    scores = []
    for si, s in enumerate(samples):
        eset = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
        overlaps = []
        for sj_idx, sj_s in enumerate(samples):
            if sj_idx == si:
                continue
            other = frozenset((e["start"], e["end"], e["type"]) for e in sj_s.get("entities", []))
            union = len(eset | other)
            inter = len(eset & other)
            overlaps.append(inter / union if union > 0 else 1.0)
        scores.append(float(np.mean(overlaps)) if overlaps else 0.0)
    return scores


def get_sample_lp(sample, inst, si):
    lp = sample.get("mean_logprob")
    if lp is None and "logprobs" in inst and si < len(inst["logprobs"]):
        lp = inst["logprobs"][si]
    return lp


def normalize_etype(etype):
    """Normalize entity type string for frequency counting."""
    t = etype.strip().upper()
    # Map common variants
    alias = {
        "PERSON": "PER", "ORGANIZATION": "ORG", "LOCATION": "LOC",
        "ORGN": "ORG", "ORGB": "ORG", "_ORG": "ORG", "_PER": "PER",
        "ORG": "ORG", "PER": "PER", "LOC": "LOC",
        "PLAC": "LOC", "PLACE": "LOC",
    }
    return alias.get(t, t)


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
                    cnt,                          # 0: agreement_count
                    text_vc.get(tk, cnt),         # 1: vc
                    lpt,                          # 2: lp_token
                    lps,                          # 3: lp_span
                    smlp,                         # 4: sample_mean_lp
                    float(np.mean(csj)),          # 5: sj
                    0,                            # 6: entity_type_enc (filled later)
                    len(etxt.split()),            # 7: entity_length
                    len(etxt),                    # 8: entity_char_length
                    st / tlen,                    # 9: entity_position
                    math.log10(cfg["msz"]),       # 10: model_size_log
                    DS_MAP[cfg["ds"]],            # 11: dataset_enc
                    REG_MAP[cfg["reg"]],          # 12: regime_enc
                ], dtype=np.float64),
                "label": 1 if k in gold_set else 0,
                "etype_raw": ety,
                "etype_norm": normalize_etype(ety),
                "span_len_bin": min(len(etxt.split()), 5),
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
# Inverse-frequency weighting
# ================================================================

def compute_type_freq(data):
    """Compute normalized entity type frequency from data."""
    type_cnt = Counter()
    for d in data:
        for c in d["candidates"]:
            type_cnt[c["etype_norm"]] += 1
    total = sum(type_cnt.values())
    return {t: cnt / total for t, cnt in type_cnt.items()}


def compute_span_len_freq(data):
    """Fallback: compute span length bin frequency."""
    bin_cnt = Counter()
    for d in data:
        for c in d["candidates"]:
            bin_cnt[c["span_len_bin"]] += 1
    total = sum(bin_cnt.values())
    return {b: cnt / total for b, cnt in bin_cnt.items()}


def apply_ifw(data, type_freq, span_freq):
    """Add IFW features to candidates. Returns augmented feature arrays."""
    for d in data:
        for c in d["candidates"]:
            etype = c["etype_norm"]
            freq = type_freq.get(etype)
            if freq is None or freq == 0:
                freq = span_freq.get(c["span_len_bin"], 0.01)
            denom = math.log(1 + freq * 1000)  # scale freq so log is meaningful
            if denom < 0.1:
                denom = 0.1
            ac = c["features"][0]
            vc = c["features"][1]
            sj = c["features"][5]
            c["ac_ifw"] = ac / denom
            c["vc_ifw"] = vc / denom
            c["sj_ifw"] = sj / denom


def get_features_replace(candidates):
    """13 features: replace ac/vc/sj with IFW versions."""
    rows = []
    for c in candidates:
        f = c["features"].copy()
        f[0] = c["ac_ifw"]
        f[1] = c["vc_ifw"]
        f[5] = c["sj_ifw"]
        rows.append(f)
    return rows


def get_features_augment(candidates):
    """16 features: original + 3 IFW features."""
    rows = []
    for c in candidates:
        aug = np.append(c["features"], [c["ac_ifw"], c["vc_ifw"], c["sj_ifw"]])
        rows.append(aug)
    return rows


# ================================================================
# Evaluation helpers (from B2-v2)
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
# Training and evaluation
# ================================================================

def train_and_eval_fold(train_data, test_data, feat_fn, feat_cols, fold_name):
    """Train LGB+XGB and evaluate on a single fold."""
    import xgboost as xgb
    import lightgbm as lgb
    from sklearn.metrics import roc_auc_score

    train_X = np.array([r for d in train_data for r in feat_fn(d["candidates"])])
    train_y = np.array([c["label"] for d in train_data for c in d["candidates"]])
    test_X = np.array([r for d in test_data for r in feat_fn(d["candidates"])])
    test_y = np.array([c["label"] for d in test_data for c in d["candidates"]])

    nan_mask = np.isnan(train_X)
    if nan_mask.any():
        col_medians = np.nanmedian(train_X, axis=0)
        for j in range(train_X.shape[1]):
            train_X[np.isnan(train_X[:, j]), j] = col_medians[j]
            test_X[np.isnan(test_X[:, j]), j] = col_medians[j]

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
    ece_xgb = compute_ece(test_y, xgb_p)
    ece_lgb = compute_ece(test_y, lgb_p)

    print(f"  AUC: XGB={auc_xgb:.4f}  LGB={auc_lgb:.4f}")
    print(f"  ECE: XGB={ece_xgb:.4f}  LGB={ece_lgb:.4f}")

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

    xgb_imp = dict(zip(feat_cols, [float(v) for v in xgb_m.feature_importances_]))
    lgb_imp = dict(zip(feat_cols, [int(v) for v in lgb_m.feature_importances_]))

    return {
        "auc": {"xgb": round(auc_xgb, 4), "lgb": round(auc_lgb, 4)},
        "ece": {"xgb": round(ece_xgb, 4), "lgb": round(ece_lgb, 4)},
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
        "feature_importance": {"xgb_gain": xgb_imp, "lgb_splits": lgb_imp},
    }


def main():
    t0 = time.time()
    print("=" * 60)
    print("B2-v4: Inverse-Frequency Weighted Entity Verifier")
    print("=" * 60)

    # --- 1. Load and extract features ---
    all_data = []
    for cfg in CONFIGS:
        data = process_config(cfg)
        all_data.extend(data)

    total_cands = sum(len(d["candidates"]) for d in all_data)
    total_pos = sum(c["label"] for d in all_data for c in d["candidates"])
    print(f"\nTotal: {len(all_data)} instances, {total_cands} candidates ({total_pos} pos, {100*total_pos/max(total_cands,1):.1f}%)")

    per_ds_stats = {}
    for ds in DATASETS:
        ds_data = [d for d in all_data if d["dataset"] == ds]
        nc = sum(len(d["candidates"]) for d in ds_data)
        np_ = sum(c["label"] for d in ds_data for c in d["candidates"])
        per_ds_stats[ds] = {"instances": len(ds_data), "candidates": nc, "positive": np_,
                            "pos_rate": round(np_ / max(nc, 1), 4)}
        print(f"  {ds}: {len(ds_data)} inst, {nc} cands ({np_} pos, {100*np_/max(nc,1):.1f}%)")

    # --- 2. Entity type encoding ---
    all_types = sorted({c["etype_raw"] for d in all_data for c in d["candidates"]})
    type_map = {t: i for i, t in enumerate(all_types)}
    for d in all_data:
        for c in d["candidates"]:
            c["features"][6] = type_map[c["etype_raw"]]

    # --- 3. B2-v2 baseline (original features, for fair comparison) ---
    from sklearn.metrics import roc_auc_score

    b2_v2_results = {}
    b2_original = {
        "lgb_test_auc": 0.8335, "xgb_test_auc": 0.8282,
        "lgb_cv_auc": 0.9254, "greedy_f1": 0.7321,
    }

    # --- 4. LODO evaluation ---
    results_replace = {}
    results_augment = {}
    ifw_stats = {}

    for fold_idx, test_ds in enumerate(DATASETS):
        fold_name = f"fold{fold_idx+1}_test_{test_ds}"
        train_ds_list = [d for d in DATASETS if d != test_ds]
        print(f"\n{'='*60}")
        print(f"Fold {fold_idx+1}: Train on {train_ds_list}, Test on [{test_ds}]")
        print(f"{'='*60}")

        train_data = [d for d in all_data if d["dataset"] != test_ds]
        test_data = [d for d in all_data if d["dataset"] == test_ds]

        # Compute IFW from training data only (no leakage)
        type_freq = compute_type_freq(train_data)
        span_freq = compute_span_len_freq(train_data)

        top_types = sorted(type_freq.items(), key=lambda x: -x[1])[:10]
        print(f"  Top types in train: {[(t, f'{f:.4f}') for t, f in top_types]}")

        # Apply IFW to both train and test using train frequencies
        apply_ifw(train_data, type_freq, span_freq)
        apply_ifw(test_data, type_freq, span_freq)

        # IFW stats
        train_ac = [c["features"][0] for d in train_data for c in d["candidates"]]
        train_ac_ifw = [c["ac_ifw"] for d in train_data for c in d["candidates"]]
        ifw_stats[fold_name] = {
            "n_types_in_train": len(type_freq),
            "top_types": {t: round(f, 4) for t, f in top_types},
            "ac_raw_mean": round(float(np.mean(train_ac)), 4),
            "ac_raw_std": round(float(np.std(train_ac)), 4),
            "ac_ifw_mean": round(float(np.mean(train_ac_ifw)), 4),
            "ac_ifw_std": round(float(np.std(train_ac_ifw)), 4),
        }

        # --- Variant A: Replace ---
        print(f"\n  --- Variant A: Replace (ac/vc/sj → IFW) ---")
        fr_a = train_and_eval_fold(
            train_data, test_data,
            get_features_replace, FEAT_COLS_REPLACE, fold_name)
        fr_a["train_datasets"] = train_ds_list
        fr_a["test_dataset"] = test_ds
        results_replace[fold_name] = fr_a

        # Clear predictions before next variant
        for d in test_data:
            for c in d["candidates"]:
                c.pop("xgb_p", None)
                c.pop("lgb_p", None)

        # --- Variant B: Augment ---
        print(f"\n  --- Variant B: Augment (original + IFW) ---")
        fr_b = train_and_eval_fold(
            train_data, test_data,
            get_features_augment, FEAT_COLS_AUGMENT, fold_name)
        fr_b["train_datasets"] = train_ds_list
        fr_b["test_dataset"] = test_ds
        results_augment[fold_name] = fr_b

        # Clear predictions
        for d in test_data:
            for c in d["candidates"]:
                c.pop("xgb_p", None)
                c.pop("lgb_p", None)

    # --- 5. Fold 4: All-data 5-fold CV ---
    print(f"\n{'='*60}")
    print("Fold 4: Train on ALL datasets, 5-fold random CV (upper bound)")
    print(f"{'='*60}")

    import xgboost as xgb
    import lightgbm as lgb
    from sklearn.model_selection import StratifiedKFold

    # Apply IFW using all data frequencies
    all_type_freq = compute_type_freq(all_data)
    all_span_freq = compute_span_len_freq(all_data)
    apply_ifw(all_data, all_type_freq, all_span_freq)

    all_y = np.array([c["label"] for d in all_data for c in d["candidates"]])
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    for variant_name, feat_fn, feat_cols in [
        ("replace", get_features_replace, FEAT_COLS_REPLACE),
        ("augment", get_features_augment, FEAT_COLS_AUGMENT),
    ]:
        all_X = np.array([r for d in all_data for r in feat_fn(d["candidates"])])
        nan_mask = np.isnan(all_X)
        if nan_mask.any():
            col_medians = np.nanmedian(all_X, axis=0)
            for j in range(all_X.shape[1]):
                all_X[np.isnan(all_X[:, j]), j] = col_medians[j]

        cv_aucs = {"xgb": [], "lgb": []}
        cv_eces = {"xgb": [], "lgb": []}

        for fold_i, (tr_i, va_i) in enumerate(skf.split(all_X, all_y)):
            Xtr, Xva = all_X[tr_i], all_X[va_i]
            ytr, yva = all_y[tr_i], all_y[va_i]

            m_xgb = xgb.XGBClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                subsample=0.8, colsample_bytree=0.8,
                eval_metric="logloss", random_state=42, verbosity=0)
            m_xgb.fit(Xtr, ytr)
            p_xgb = m_xgb.predict_proba(Xva)[:, 1]
            cv_aucs["xgb"].append(roc_auc_score(yva, p_xgb))
            cv_eces["xgb"].append(compute_ece(yva, p_xgb))

            m_lgb = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.1,
                subsample=0.8, colsample_bytree=0.8,
                random_state=42, verbose=-1)
            m_lgb.fit(Xtr, ytr)
            p_lgb = m_lgb.predict_proba(Xva)[:, 1]
            cv_aucs["lgb"].append(roc_auc_score(yva, p_lgb))
            cv_eces["lgb"].append(compute_ece(yva, p_lgb))

        target = results_replace if variant_name == "replace" else results_augment
        target["fold4_all_cv"] = {
            "auc": {
                "xgb_mean": round(float(np.mean(cv_aucs["xgb"])), 4),
                "xgb_std": round(float(np.std(cv_aucs["xgb"])), 4),
                "lgb_mean": round(float(np.mean(cv_aucs["lgb"])), 4),
                "lgb_std": round(float(np.std(cv_aucs["lgb"])), 4),
                "xgb_folds": [round(a, 4) for a in cv_aucs["xgb"]],
                "lgb_folds": [round(a, 4) for a in cv_aucs["lgb"]],
            },
            "ece": {
                "xgb_mean": round(float(np.mean(cv_eces["xgb"])), 4),
                "lgb_mean": round(float(np.mean(cv_eces["lgb"])), 4),
                "xgb_folds": [round(e, 4) for e in cv_eces["xgb"]],
                "lgb_folds": [round(e, 4) for e in cv_eces["lgb"]],
            },
        }
        print(f"  {variant_name} CV AUC: XGB={np.mean(cv_aucs['xgb']):.4f}±{np.std(cv_aucs['xgb']):.4f}  "
              f"LGB={np.mean(cv_aucs['lgb']):.4f}±{np.std(cv_aucs['lgb']):.4f}")

    # --- 6. Feature stability analysis ---
    print(f"\n{'='*60}")
    print("Feature Stability Analysis")
    print(f"{'='*60}")

    from scipy.stats import pointbiserialr

    stability = {}
    for fi, feat_name in enumerate(FEAT_COLS_AUGMENT):
        per_ds = {}
        for ds in DATASETS:
            ds_cands = []
            for d in all_data:
                if d["dataset"] == ds:
                    for c in d["candidates"]:
                        if feat_name in ["ac_ifw", "vc_ifw", "sj_ifw"]:
                            val = c.get(feat_name.replace("_ifw", "") + "_ifw" if feat_name.endswith("_ifw") else feat_name)
                            if feat_name == "ac_ifw":
                                val = c["ac_ifw"]
                            elif feat_name == "vc_ifw":
                                val = c["vc_ifw"]
                            elif feat_name == "sj_ifw":
                                val = c["sj_ifw"]
                        else:
                            val = c["features"][fi] if fi < len(c["features"]) else float('nan')
                        ds_cands.append((val, c["label"]))

            vals = np.array([x[0] for x in ds_cands])
            labs = np.array([x[1] for x in ds_cands])
            valid = ~np.isnan(vals)
            if valid.sum() > 10 and len(np.unique(labs[valid])) == 2:
                corr, _ = pointbiserialr(labs[valid], vals[valid])
                per_ds[ds] = round(float(corr), 4)
            else:
                per_ds[ds] = float('nan')

        vals_list = [v for v in per_ds.values() if not (isinstance(v, float) and math.isnan(v))]
        stability[feat_name] = {
            "per_dataset_correlation": per_ds,
            "cross_domain_std": round(float(np.std(vals_list)), 4) if len(vals_list) >= 2 else float('nan'),
            "mean_correlation": round(float(np.mean(vals_list)), 4) if vals_list else float('nan'),
        }

    elapsed = time.time() - t0

    # --- 7. Comparison table ---
    b2v2_fold3 = {"lgb_auc": 0.8477, "xgb_auc": 0.8603, "lgb_ece": 0.1357, "xgb_ece": 0.1556,
                   "greedy_f1": 0.7937, "path_a_lgb_f1": 0.7929, "path_a_xgb_f1": 0.7929}
    b2v3_fold3 = {"lgb_auc": 0.8562, "xgb_auc": 0.8518, "lgb_ece": 0.1373, "xgb_ece": 0.1643}

    comparison = {
        "b2_original": b2_original,
        "b2_v2_fold3": b2v2_fold3,
        "b2_v3_fold3": b2v3_fold3,
    }

    f3_replace = results_replace.get("fold3_test_fewnerd", {})
    f3_augment = results_augment.get("fold3_test_fewnerd", {})

    if f3_replace:
        comparison["b2_v4_replace_fold3"] = {
            "lgb_auc": f3_replace["auc"]["lgb"],
            "xgb_auc": f3_replace["auc"]["xgb"],
            "lgb_ece": f3_replace["ece"]["lgb"],
            "xgb_ece": f3_replace["ece"]["xgb"],
            "greedy_f1": f3_replace["baselines"]["greedy"]["f1"],
            "path_a_lgb_f1": f3_replace["best_path_a"]["lgb"]["f1"],
            "path_a_xgb_f1": f3_replace["best_path_a"]["xgb"]["f1"],
        }
        comparison["delta_v4replace_vs_v2"] = {
            "lgb_auc": round(f3_replace["auc"]["lgb"] - b2v2_fold3["lgb_auc"], 4),
            "xgb_auc": round(f3_replace["auc"]["xgb"] - b2v2_fold3["xgb_auc"], 4),
        }

    if f3_augment:
        comparison["b2_v4_augment_fold3"] = {
            "lgb_auc": f3_augment["auc"]["lgb"],
            "xgb_auc": f3_augment["auc"]["xgb"],
            "lgb_ece": f3_augment["ece"]["lgb"],
            "xgb_ece": f3_augment["ece"]["xgb"],
            "greedy_f1": f3_augment["baselines"]["greedy"]["f1"],
            "path_a_lgb_f1": f3_augment["best_path_a"]["lgb"]["f1"],
            "path_a_xgb_f1": f3_augment["best_path_a"]["xgb"]["f1"],
        }
        comparison["delta_v4augment_vs_v2"] = {
            "lgb_auc": round(f3_augment["auc"]["lgb"] - b2v2_fold3["lgb_auc"], 4),
            "xgb_auc": round(f3_augment["auc"]["xgb"] - b2v2_fold3["xgb_auc"], 4),
        }

    # --- 8. Save results ---
    final_results = {
        "summary": {
            "total_instances": len(all_data),
            "total_candidates": total_cands,
            "positive_rate": round(total_pos / max(total_cands, 1), 4),
            "per_dataset": per_ds_stats,
            "n_entity_types": len(all_types),
            "n_configs": len(CONFIGS),
            "elapsed_seconds": round(elapsed, 1),
        },
        "variant_a_replace": results_replace,
        "variant_b_augment": results_augment,
        "comparison": comparison,
        "ifw_stats": ifw_stats,
        "feature_stability_augment": stability,
    }

    with open(f"{OUT}/results.json", "w") as f:
        json.dump(final_results, f, indent=2)
    print(f"\nSaved results.json")

    # --- 9. Summary markdown ---
    md = []
    md.append("# B2-v4: Inverse-Frequency Weighted Entity Verifier\n")
    md.append(f"**Date**: {time.strftime('%Y-%m-%d %H:%M')}")
    md.append(f"**Total entities**: {total_cands} across {len(CONFIGS)} configs")
    md.append(f"**IFW formula**: `feature / log(1 + freq * 1000)` where freq = type_proportion in train\n")

    md.append("## Variant A: Replace (ac/vc/sj → IFW versions, 13 features)\n")
    md.append("| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |")
    md.append("|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|")
    for fold_idx, test_ds in enumerate(DATASETS):
        fn = f"fold{fold_idx+1}_test_{test_ds}"
        fr = results_replace[fn]
        train_str = "+".join(fr["train_datasets"])
        best_f1 = max(fr["best_path_a"]["xgb"]["f1"], fr["best_path_a"]["lgb"]["f1"],
                       fr["best_path_b"]["xgb"]["f1"], fr["best_path_b"]["lgb"]["f1"])
        delta = best_f1 - fr["baselines"]["greedy"]["f1"]
        md.append(f"| {fold_idx+1} | {train_str} | {test_ds} | "
                  f"{fr['auc']['xgb']:.4f} | {fr['auc']['lgb']:.4f} | "
                  f"{fr['ece']['xgb']:.4f} | {fr['ece']['lgb']:.4f} | "
                  f"{fr['baselines']['greedy']['f1']:.4f} | {best_f1:.4f} | {delta:+.4f} |")
    f4r = results_replace.get("fold4_all_cv", {})
    if f4r:
        md.append(f"| 4 | ALL | CV | "
                  f"{f4r['auc']['xgb_mean']:.4f}±{f4r['auc']['xgb_std']:.4f} | "
                  f"{f4r['auc']['lgb_mean']:.4f}±{f4r['auc']['lgb_std']:.4f} | "
                  f"{f4r['ece']['xgb_mean']:.4f} | {f4r['ece']['lgb_mean']:.4f} | - | - | - |")

    md.append("\n## Variant B: Augment (original + IFW, 16 features)\n")
    md.append("| Fold | Train | Test | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Greedy F1 | Best F1 | Δ Greedy |")
    md.append("|------|-------|------|---------|---------|---------|---------|-----------|---------|----------|")
    for fold_idx, test_ds in enumerate(DATASETS):
        fn = f"fold{fold_idx+1}_test_{test_ds}"
        fr = results_augment[fn]
        train_str = "+".join(fr["train_datasets"])
        best_f1 = max(fr["best_path_a"]["xgb"]["f1"], fr["best_path_a"]["lgb"]["f1"],
                       fr["best_path_b"]["xgb"]["f1"], fr["best_path_b"]["lgb"]["f1"])
        delta = best_f1 - fr["baselines"]["greedy"]["f1"]
        md.append(f"| {fold_idx+1} | {train_str} | {test_ds} | "
                  f"{fr['auc']['xgb']:.4f} | {fr['auc']['lgb']:.4f} | "
                  f"{fr['ece']['xgb']:.4f} | {fr['ece']['lgb']:.4f} | "
                  f"{fr['baselines']['greedy']['f1']:.4f} | {best_f1:.4f} | {delta:+.4f} |")
    f4a = results_augment.get("fold4_all_cv", {})
    if f4a:
        md.append(f"| 4 | ALL | CV | "
                  f"{f4a['auc']['xgb_mean']:.4f}±{f4a['auc']['xgb_std']:.4f} | "
                  f"{f4a['auc']['lgb_mean']:.4f}±{f4a['auc']['lgb_std']:.4f} | "
                  f"{f4a['ece']['xgb_mean']:.4f} | {f4a['ece']['lgb_mean']:.4f} | - | - | - |")

    md.append("\n## Comparison: Fold 3 (FewNERD, critical cross-domain fold)\n")
    md.append("| Version | Features | XGB AUC | LGB AUC | XGB ECE | LGB ECE | Best F1 Δ |")
    md.append("|---------|----------|---------|---------|---------|---------|-----------|")
    md.append(f"| B2 orig | 13 | {b2_original['xgb_test_auc']:.4f} | {b2_original['lgb_test_auc']:.4f} | - | - | - |")
    md.append(f"| B2-v2 | 13 | {b2v2_fold3['xgb_auc']:.4f} | {b2v2_fold3['lgb_auc']:.4f} | "
              f"{b2v2_fold3['xgb_ece']:.4f} | {b2v2_fold3['lgb_ece']:.4f} | - |")
    md.append(f"| B2-v3 | 9 (invariant) | {b2v3_fold3['xgb_auc']:.4f} | {b2v3_fold3['lgb_auc']:.4f} | "
              f"{b2v3_fold3['xgb_ece']:.4f} | {b2v3_fold3['lgb_ece']:.4f} | - |")
    if f3_replace:
        best_f1_r = max(f3_replace["best_path_a"]["xgb"]["f1"], f3_replace["best_path_a"]["lgb"]["f1"],
                         f3_replace["best_path_b"]["xgb"]["f1"], f3_replace["best_path_b"]["lgb"]["f1"])
        delta_r = best_f1_r - f3_replace["baselines"]["greedy"]["f1"]
        md.append(f"| **B2-v4 replace** | 13 (IFW) | {f3_replace['auc']['xgb']:.4f} | {f3_replace['auc']['lgb']:.4f} | "
                  f"{f3_replace['ece']['xgb']:.4f} | {f3_replace['ece']['lgb']:.4f} | {delta_r:+.4f} |")
    if f3_augment:
        best_f1_a = max(f3_augment["best_path_a"]["xgb"]["f1"], f3_augment["best_path_a"]["lgb"]["f1"],
                         f3_augment["best_path_b"]["xgb"]["f1"], f3_augment["best_path_b"]["lgb"]["f1"])
        delta_a = best_f1_a - f3_augment["baselines"]["greedy"]["f1"]
        md.append(f"| **B2-v4 augment** | 16 (orig+IFW) | {f3_augment['auc']['xgb']:.4f} | {f3_augment['auc']['lgb']:.4f} | "
                  f"{f3_augment['ece']['xgb']:.4f} | {f3_augment['ece']['lgb']:.4f} | {delta_a:+.4f} |")

    md.append("\n## Feature Importance (XGB Gain, Fold 3)\n")
    for var_name, var_results, var_cols in [
        ("Replace", results_replace, FEAT_COLS_REPLACE),
        ("Augment", results_augment, FEAT_COLS_AUGMENT),
    ]:
        f3 = var_results.get("fold3_test_fewnerd", {})
        if f3 and "feature_importance" in f3:
            md.append(f"\n### {var_name}\n")
            md.append("| Feature | XGB Gain | LGB Splits |")
            md.append("|---------|----------|------------|")
            xgb_g = f3["feature_importance"]["xgb_gain"]
            lgb_s = f3["feature_importance"]["lgb_splits"]
            sorted_feats = sorted(var_cols, key=lambda f: -xgb_g.get(f, 0))
            for feat in sorted_feats:
                md.append(f"| {feat} | {xgb_g.get(feat, 0):.4f} | {lgb_s.get(feat, 0)} |")

    md.append("\n## IFW Feature Stability\n")
    md.append("| Feature | CoNLL | SciERC | FewNERD | Cross-Domain Std |")
    md.append("|---------|-------|--------|---------|------------------|")
    key_feats = ["agreement_count", "vc", "sj", "ac_ifw", "vc_ifw", "sj_ifw",
                 "lp_token", "lp_span", "sample_mean_lp"]
    for feat in key_feats:
        if feat in stability:
            s = stability[feat]
            pc = s["per_dataset_correlation"]
            md.append(f"| {feat} | {pc.get('conll', float('nan')):.4f} | "
                      f"{pc.get('scierc', float('nan')):.4f} | {pc.get('fewnerd', float('nan')):.4f} | "
                      f"{s['cross_domain_std']:.4f} |")

    md.append(f"\n**Elapsed**: {elapsed:.1f}s\n")

    summary_md = "\n".join(md) + "\n"
    with open(f"{OUT}/summary.md", "w") as f:
        f.write(summary_md)
    print(f"Saved summary.md")
    print(f"\nTotal elapsed: {elapsed:.1f}s")
    print("Done.")


if __name__ == "__main__":
    main()
