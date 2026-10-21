#!/usr/bin/env python3
"""B2: Entity-Level Verifier (XGBoost/LightGBM).

Trains a gradient boosting classifier to predict whether an entity candidate
extracted from N=8 samples matches the gold annotation. Evaluates two usage
paths: (A) verifier-score-weighted construction, (B) post-hoc filtering.

Train: CoNLL + SciERC configs | Test: FewNERD configs (cross-dataset).
"""

import json, os, re, math, time
import numpy as np
from collections import Counter, defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = f"{BASE}/artifacts/b2_verifier"
os.makedirs(OUT, exist_ok=True)

CONFIGS = [
    # CoNLL (train)
    dict(name="conll_7b_s123", path=f"{BASE}/output/exp_conll_seed123/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=True),
    dict(name="conll_7b_s456", path=f"{BASE}/output/exp_conll_seed456/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=True),
    dict(name="conll_72b_zs", path=f"{BASE}/output/72b_zeroshot/conll2003/samples.jsonl",
         ds="conll", msz=72e9, reg="ZS", tok=False),
    dict(name="conll_72b_fs", path=f"{BASE}/output/72b_fewshot/conll2003/samples.jsonl",
         ds="conll", msz=72e9, reg="FS", tok=False),
    # SciERC (train)
    dict(name="scierc_7b_s456", path=f"{BASE}/output/exp_scierc_seed456/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=True),
    dict(name="scierc_7b_s789", path=f"{BASE}/output/exp_scierc_seed789/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=True),
    dict(name="scierc_72b_zs", path=f"{BASE}/output/72b_zeroshot/scierc/samples.jsonl",
         ds="scierc", msz=72e9, reg="ZS", tok=False),
    dict(name="scierc_72b_fs", path=f"{BASE}/output/72b_fewshot/scierc/samples.jsonl",
         ds="scierc", msz=72e9, reg="FS", tok=False),
    # FewNERD (test)
    dict(name="fewnerd_7b_s123", path=f"{BASE}/output/exp_fewnerd_seed123/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_7b_s456", path=f"{BASE}/output/exp_fewnerd_seed456/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_7b_s789", path=f"{BASE}/output/exp_fewnerd_seed789/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_72b_zs", path=f"{BASE}/output/72b_zeroshot/fewnerd/samples.jsonl",
         ds="fewnerd", msz=72e9, reg="ZS", tok=False),
    dict(name="fewnerd_72b_fs", path=f"{BASE}/output/72b_fewshot/fewnerd/samples.jsonl",
         ds="fewnerd", msz=72e9, reg="FS", tok=False),
]

FEWNERD_MAX = 3000
DS_MAP = {"conll": 0, "scierc": 1, "fewnerd": 2}
REG_MAP = {"FT": 0, "ZS": 1, "FS": 2}
TRAIN_DS = {"conll", "scierc"}
TEST_DS = {"fewnerd"}

FEAT_COLS = [
    "agreement_count", "vc", "lp_token", "lp_span", "sample_mean_lp",
    "sj", "entity_type_enc", "entity_length", "entity_char_length",
    "entity_position", "model_size_log", "dataset_enc", "regime_enc",
]


# ================================================================
# Helpers
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


# ================================================================
# Per-config data processing
# ================================================================

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
                    0,                            # entity_type_enc (filled later)
                    len(etxt.split()),            # entity_length
                    len(etxt),                    # entity_char_length
                    st / tlen,                    # entity_position
                    math.log10(cfg["msz"]),       # model_size_log
                    DS_MAP[cfg["ds"]],            # dataset_enc
                    REG_MAP[cfg["reg"]],          # regime_enc
                ], dtype=np.float64),
                "label": 1 if k in gold_set else 0,
                "etype_raw": ety,
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


def eval_all_candidates(data):
    """Baseline: keep all entity candidates (union of all samples)."""
    tp = fp = fn = 0
    for d in data:
        ps = {c["key"] for c in d["candidates"]}
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


# ================================================================
# Main
# ================================================================

def main():
    t0 = time.time()
    print("=== B2 Entity-Level Verifier ===\n")

    # --- 1. Load & process all configs ---
    print("Loading data...")
    all_data = []
    for cfg in CONFIGS:
        all_data.extend(process_config(cfg))

    total_cands = sum(len(d["candidates"]) for d in all_data)
    total_pos = sum(c["label"] for d in all_data for c in d["candidates"])
    print(f"\nTotal instances: {len(all_data)}")
    print(f"Entity candidates: {total_cands}  (pos={total_pos}, {100*total_pos/max(total_cands,1):.1f}%)")

    # --- 2. Entity type encoding ---
    all_types = sorted({c["etype_raw"] for d in all_data for c in d["candidates"]})
    type_map = {t: i for i, t in enumerate(all_types)}
    print(f"Entity types ({len(type_map)}): {all_types[:10]}{'...' if len(all_types)>10 else ''}")
    for d in all_data:
        for c in d["candidates"]:
            c["features"][6] = type_map[c["etype_raw"]]

    # --- 3. Train/test split ---
    train_data = [d for d in all_data if d["dataset"] in TRAIN_DS]
    test_data = [d for d in all_data if d["dataset"] in TEST_DS]

    train_X = np.array([c["features"] for d in train_data for c in d["candidates"]])
    train_y = np.array([c["label"] for d in train_data for c in d["candidates"]])
    test_X = np.array([c["features"] for d in test_data for c in d["candidates"]])
    test_y = np.array([c["label"] for d in test_data for c in d["candidates"]])

    print(f"\nTrain: {len(train_X)} entities ({int(train_y.sum())} pos)")
    print(f"Test:  {len(test_X)} entities ({int(test_y.sum())} pos)")

    # --- 4. Import ML libs ---
    import xgboost as xgb
    import lightgbm as lgb
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import roc_auc_score

    # --- 5. 5-Fold CV ---
    print("\n--- 5-Fold CV ---")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv = {"xgb": [], "lgb": []}

    for fold, (tr_i, va_i) in enumerate(skf.split(train_X, train_y)):
        Xtr, Xva = train_X[tr_i], train_X[va_i]
        ytr, yva = train_y[tr_i], train_y[va_i]

        m_xgb = xgb.XGBClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            eval_metric="logloss", random_state=42, verbosity=0)
        m_xgb.fit(Xtr, ytr)
        p_xgb = m_xgb.predict_proba(Xva)[:, 1]
        a_xgb = roc_auc_score(yva, p_xgb)
        cv["xgb"].append(a_xgb)

        m_lgb = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1)
        m_lgb.fit(Xtr, ytr)
        p_lgb = m_lgb.predict_proba(Xva)[:, 1]
        a_lgb = roc_auc_score(yva, p_lgb)
        cv["lgb"].append(a_lgb)

        print(f"  Fold {fold}: XGB={a_xgb:.4f}  LGB={a_lgb:.4f}")

    print(f"  Mean: XGB={np.mean(cv['xgb']):.4f}±{np.std(cv['xgb']):.4f}  "
          f"LGB={np.mean(cv['lgb']):.4f}±{np.std(cv['lgb']):.4f}")

    # --- 6. Final models ---
    print("\nTraining final models on full train set...")
    xgb_final = xgb.XGBClassifier(
        n_estimators=200, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8,
        eval_metric="logloss", random_state=42, verbosity=0)
    xgb_final.fit(train_X, train_y)

    lgb_final = lgb.LGBMClassifier(
        n_estimators=200, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8,
        random_state=42, verbose=-1)
    lgb_final.fit(train_X, train_y)

    # Feature importance
    xgb_imp = dict(zip(FEAT_COLS, [float(v) for v in xgb_final.feature_importances_]))
    lgb_imp = dict(zip(FEAT_COLS, [int(v) for v in lgb_final.feature_importances_]))

    print("\nXGBoost Feature Importance:")
    for k, v in sorted(xgb_imp.items(), key=lambda x: -x[1])[:10]:
        print(f"  {k}: {v:.4f}")
    print("\nLightGBM Feature Importance (split count):")
    for k, v in sorted(lgb_imp.items(), key=lambda x: -x[1])[:10]:
        print(f"  {k}: {v}")

    # --- 7. Test evaluation ---
    print("\n--- Test Set Evaluation ---")
    test_xgb_p = xgb_final.predict_proba(test_X)[:, 1]
    test_lgb_p = lgb_final.predict_proba(test_X)[:, 1]
    test_auc_xgb = roc_auc_score(test_y, test_xgb_p)
    test_auc_lgb = roc_auc_score(test_y, test_lgb_p)
    print(f"Test AUC: XGB={test_auc_xgb:.4f}  LGB={test_auc_lgb:.4f}")

    # Attach predictions to candidates
    idx = 0
    for d in test_data:
        for c in d["candidates"]:
            c["xgb_p"] = float(test_xgb_p[idx])
            c["lgb_p"] = float(test_lgb_p[idx])
            idx += 1

    # Also attach to train_data for completeness
    train_xgb_p = xgb_final.predict_proba(train_X)[:, 1]
    train_lgb_p = lgb_final.predict_proba(train_X)[:, 1]
    idx = 0
    for d in train_data:
        for c in d["candidates"]:
            c["xgb_p"] = float(train_xgb_p[idx])
            c["lgb_p"] = float(train_lgb_p[idx])
            idx += 1

    # Baselines (test)
    greedy = eval_greedy(test_data)
    mv50 = eval_majority_vote(test_data, 0.5)
    mv25 = eval_majority_vote(test_data, 0.25)
    union = eval_all_candidates(test_data)
    print(f"\nBaselines (FewNERD test):")
    print(f"  Greedy:         P={greedy['precision']:.4f} R={greedy['recall']:.4f} F1={greedy['f1']:.4f}")
    print(f"  MajVote(>50%):  P={mv50['precision']:.4f} R={mv50['recall']:.4f} F1={mv50['f1']:.4f}")
    print(f"  MajVote(>25%):  P={mv25['precision']:.4f} R={mv25['recall']:.4f} F1={mv25['f1']:.4f}")
    print(f"  Union(all):     P={union['precision']:.4f} R={union['recall']:.4f} F1={union['f1']:.4f}")

    # Path A sweep
    print("\n--- Path A: Verifier-Weighted Construction ---")
    pa_results = {}
    for mk, mn in [("xgb_p", "XGB"), ("lgb_p", "LGB")]:
        best_f1, best_t = 0, 0
        for thresh in np.arange(0.5, 5.5, 0.5):
            r = eval_path_a(test_data, mk, thresh)
            pa_results[f"{mn}_t{thresh:.1f}"] = r
            if r["f1"] > best_f1:
                best_f1, best_t = r["f1"], thresh
        print(f"  {mn} best: t={best_t:.1f} → P={pa_results[f'{mn}_t{best_t:.1f}']['precision']:.4f} "
              f"R={pa_results[f'{mn}_t{best_t:.1f}']['recall']:.4f} F1={best_f1:.4f}")

    # Path B sweep
    print("\n--- Path B: Post-hoc Filter ---")
    pb_results = {}
    filter_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for mk, mn in [("xgb_p", "XGB"), ("lgb_p", "LGB")]:
        best_f1, best_t = 0, 0
        for ft in filter_thresholds:
            r = eval_path_b(test_data, mk, construct_thresh=0.5, filter_thresh=ft)
            pb_results[f"{mn}_ft{ft:.1f}"] = r
            if r["f1"] > best_f1:
                best_f1, best_t = r["f1"], ft
            print(f"  {mn} ft={ft:.1f}: P={r['precision']:.4f} R={r['recall']:.4f} F1={r['f1']:.4f}")
        print(f"  {mn} best: ft={best_t:.1f} → F1={best_f1:.4f}\n")

    # Per-config results
    print("--- Per-Config Results ---")
    per_cfg = {}
    for cfg_name in sorted({d["config"] for d in test_data}):
        cd = [d for d in test_data if d["config"] == cfg_name]
        g = eval_greedy(cd)
        mv = eval_majority_vote(cd, 0.5)
        # Best Path B for XGB
        best_pb = {"f1": 0}
        for ft in filter_thresholds:
            r = eval_path_b(cd, "xgb_p", 0.5, ft)
            if r["f1"] > best_pb.get("f1", 0):
                best_pb = {**r, "thresh": ft}
        # Best Path A for XGB
        best_pa = {"f1": 0}
        for t in np.arange(0.5, 5.5, 0.5):
            r = eval_path_a(cd, "xgb_p", t)
            if r["f1"] > best_pa.get("f1", 0):
                best_pa = {**r, "thresh": float(t)}
        per_cfg[cfg_name] = {
            "n_instances": len(cd),
            "greedy": g, "majority_vote_50": mv,
            "best_path_a_xgb": best_pa, "best_path_b_xgb": best_pb,
        }
        print(f"  {cfg_name}: Greedy={g['f1']:.4f}  MV={mv['f1']:.4f}  "
              f"PA={best_pa['f1']:.4f}(t={best_pa.get('thresh',0):.1f})  "
              f"PB={best_pb['f1']:.4f}(ft={best_pb.get('thresh',0):.1f})")

    # --- Also evaluate on training set ---
    print("\n--- Train Set Sanity Check ---")
    train_greedy = eval_greedy(train_data)
    train_mv = eval_majority_vote(train_data, 0.5)
    best_train_pb = {"f1": 0}
    for ft in filter_thresholds:
        r = eval_path_b(train_data, "xgb_p", 0.5, ft)
        if r["f1"] > best_train_pb.get("f1", 0):
            best_train_pb = {**r, "thresh": ft}
    print(f"  Greedy: F1={train_greedy['f1']:.4f}  MV: F1={train_mv['f1']:.4f}  "
          f"PathB(XGB): F1={best_train_pb['f1']:.4f}(ft={best_train_pb.get('thresh',0):.1f})")

    # --- 8. Save results ---
    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.0f}s")

    results = {
        "summary": {
            "total_instances": len(all_data),
            "total_candidates": total_cands,
            "positive_rate": round(total_pos / max(total_cands, 1), 4),
            "entity_types": all_types,
            "n_entity_types": len(all_types),
            "train_entities": len(train_X),
            "test_entities": len(test_X),
            "elapsed_seconds": round(elapsed, 1),
        },
        "cv_results": {
            "xgb_auc_per_fold": [round(x, 4) for x in cv["xgb"]],
            "lgb_auc_per_fold": [round(x, 4) for x in cv["lgb"]],
            "xgb_mean_auc": round(float(np.mean(cv["xgb"])), 4),
            "lgb_mean_auc": round(float(np.mean(cv["lgb"])), 4),
            "xgb_std_auc": round(float(np.std(cv["xgb"])), 4),
            "lgb_std_auc": round(float(np.std(cv["lgb"])), 4),
        },
        "test_auc": {"xgb": round(test_auc_xgb, 4), "lgb": round(test_auc_lgb, 4)},
        "baselines": {
            "greedy": greedy,
            "majority_vote_50": mv50,
            "majority_vote_25": mv25,
            "union_all": union,
        },
        "path_a": pa_results,
        "path_b": pb_results,
        "per_config": per_cfg,
        "train_sanity": {
            "greedy": train_greedy,
            "majority_vote_50": train_mv,
            "best_path_b_xgb": best_train_pb,
        },
    }

    with open(f"{OUT}/verifier_results.json", "w") as f:
        json.dump(results, f, indent=2)

    feat_imp = {
        "feature_names": FEAT_COLS,
        "xgboost_gain": {k: round(v, 4) for k, v in sorted(xgb_imp.items(), key=lambda x: -x[1])},
        "lightgbm_splits": {k: v for k, v in sorted(lgb_imp.items(), key=lambda x: -x[1])},
    }
    with open(f"{OUT}/feature_importance.json", "w") as f:
        json.dump(feat_imp, f, indent=2)

    cross_ds = {
        "train_datasets": sorted(TRAIN_DS),
        "test_datasets": sorted(TEST_DS),
        "note": "No WNUT data available; test is FewNERD only",
        "test_auc": {"xgb": round(test_auc_xgb, 4), "lgb": round(test_auc_lgb, 4)},
        "per_config": per_cfg,
    }
    with open(f"{OUT}/cross_dataset_results.json", "w") as f:
        json.dump(cross_ds, f, indent=2)

    print(f"Results saved to {OUT}/")
    print("Done.")


if __name__ == "__main__":
    main()
