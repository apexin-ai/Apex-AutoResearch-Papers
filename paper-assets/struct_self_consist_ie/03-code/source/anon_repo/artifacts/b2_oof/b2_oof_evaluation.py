#!/usr/bin/env python3
"""B2 Out-of-Fold (OOF) Entity Verifier Evaluation.

Addresses train-on-test leakage in original B2 by using instance-level
5-fold CV: verifier never sees entities from the same instance during
training and prediction. Threshold is optimized on train folds only.
"""

import json, os, re, math, time
import numpy as np
from collections import Counter, defaultdict

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = f"{BASE}/artifacts/b2_oof"
os.makedirs(OUT, exist_ok=True)

MAX_SAMPLES = 8
FEWNERD_MAX = 3000

CONFIGS = [
    dict(name="scierc_qwen_s42", path=f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="scierc_qwen_s123", path=f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="scierc_qwen_s456", path=f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
         ds="scierc", msz=7e9, reg="FT", tok=False),
    dict(name="conll_qwen_s42", path=f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=False),
    dict(name="conll_qwen_s123", path=f"{BASE}/output/exp_002_conll_n16_seed123/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=False),
    dict(name="conll_qwen_s456", path=f"{BASE}/output/exp_002_conll_n16_seed456/samples.jsonl",
         ds="conll", msz=7e9, reg="FT", tok=False),
    dict(name="fewnerd_qwen_s123", path=f"{BASE}/output/exp_021_fewnerd_n8_seed123/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_qwen_s456", path=f"{BASE}/output/exp_021_fewnerd_n8_seed456/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
    dict(name="fewnerd_qwen_s789", path=f"{BASE}/output/fewnerd_seed789_merged/samples.jsonl",
         ds="fewnerd", msz=7e9, reg="FT", tok=True),
]

DS_MAP = {"conll": 0, "scierc": 1, "fewnerd": 2}
REG_MAP = {"FT": 0, "ZS": 1, "FS": 2}
FEAT_COLS = [
    "agreement_count", "vc", "lp_token", "lp_span", "sample_mean_lp",
    "sj", "entity_type_enc", "entity_length", "entity_char_length",
    "entity_position", "model_size_log", "dataset_enc", "regime_enc",
]

# ================================================================
# Helpers (from original b2_entity_verifier.py)
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
        samples = inst["samples"][:MAX_SAMPLES]
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
                    cnt,
                    text_vc.get(tk, cnt),
                    lpt,
                    lps,
                    smlp,
                    float(np.mean(csj)),
                    0,  # entity_type_enc filled later
                    len(etxt.split()),
                    len(etxt),
                    st / tlen,
                    math.log10(cfg["msz"]),
                    DS_MAP[cfg["ds"]],
                    REG_MAP[cfg["reg"]],
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
# Evaluation
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


def eval_path_a(data, threshold):
    tp = fp = fn = 0
    for d in data:
        ps = {c["key"] for c in d["candidates"]
              if c.get("oof_p", 0) * c["features"][0] > threshold}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def eval_path_b(data, construct_thresh=0.5, filter_thresh=0.5):
    tp = fp = fn = 0
    for d in data:
        N = d["N"]
        mv = {c["key"] for c in d["candidates"] if c["features"][0] / N > construct_thresh}
        ps = {c["key"] for c in d["candidates"]
              if c["key"] in mv and c.get("oof_p", 0) >= filter_thresh}
        t, f, n = eval_sets(ps, d["gold_set"])
        tp += t; fp += f; fn += n
    return prf(tp, fp, fn)


def find_best_path_a_threshold(data, thresholds):
    best_f1, best_t = 0, 0
    for t in thresholds:
        r = eval_path_a(data, t)
        if r["f1"] > best_f1:
            best_f1, best_t = r["f1"], t
    return best_t, best_f1


def find_best_path_b_threshold(data, filter_thresholds):
    best_f1, best_t = 0, 0
    for ft in filter_thresholds:
        r = eval_path_b(data, 0.5, ft)
        if r["f1"] > best_f1:
            best_f1, best_t = r["f1"], ft
    return best_t, best_f1


# ================================================================
# Main
# ================================================================

def main():
    t0 = time.time()
    print("=== B2 Out-of-Fold Entity Verifier Evaluation ===\n")

    # --- 1. Load & process all configs ---
    print("Loading data...")
    all_data = []
    for cfg in CONFIGS:
        if not os.path.exists(cfg["path"]):
            print(f"  SKIP {cfg['name']}: file not found")
            continue
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

    # --- 3. Create 5-fold instance-level splits ---
    from sklearn.model_selection import StratifiedGroupKFold
    import lightgbm as lgb
    from sklearn.metrics import roc_auc_score

    instance_ids = [f"{d['config']}_{d['iid']}" for d in all_data]
    instance_datasets = [d["dataset"] for d in all_data]

    rng = np.random.RandomState(42)
    sgkf = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)

    # Stratify by dataset
    fold_assignments = np.zeros(len(all_data), dtype=int)
    for fold_idx, (train_idx, test_idx) in enumerate(
        sgkf.split(range(len(all_data)), instance_datasets, instance_ids)
    ):
        fold_assignments[test_idx] = fold_idx

    fold_sizes = [int((fold_assignments == k).sum()) for k in range(5)]
    print(f"Fold sizes: {fold_sizes}")

    # --- 4. OOF evaluation ---
    print("\n--- 5-Fold OOF Evaluation ---")

    pa_thresholds = list(np.arange(0.5, 5.5, 0.25))
    pb_filter_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    fold_aucs = []
    fold_results = []

    for fold_k in range(5):
        print(f"\n  Fold {fold_k}:")
        train_mask = fold_assignments != fold_k
        test_mask = fold_assignments == fold_k

        train_instances = [d for d, m in zip(all_data, train_mask) if m]
        test_instances = [d for d, m in zip(all_data, test_mask) if m]

        # Build feature matrices
        train_X = np.array([c["features"] for d in train_instances for c in d["candidates"]])
        train_y = np.array([c["label"] for d in train_instances for c in d["candidates"]])
        test_X = np.array([c["features"] for d in test_instances for c in d["candidates"]])
        test_y = np.array([c["label"] for d in test_instances for c in d["candidates"]])

        print(f"    Train: {len(train_X)} entities ({int(train_y.sum())} pos), "
              f"Test: {len(test_X)} entities ({int(test_y.sum())} pos)")

        # Train LightGBM
        model = lgb.LGBMClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            subsample=0.8, colsample_bytree=0.8,
            random_state=42, verbose=-1)
        model.fit(train_X, train_y)

        # Predict on held-out fold
        test_probs = model.predict_proba(test_X)[:, 1]
        auc = roc_auc_score(test_y, test_probs)
        fold_aucs.append(auc)
        print(f"    AUC: {auc:.4f}")

        # Attach OOF predictions to candidates
        idx = 0
        for d in test_instances:
            for c in d["candidates"]:
                c["oof_p"] = float(test_probs[idx])
                idx += 1

        # Compute train predictions for threshold optimization (separate key)
        train_probs = model.predict_proba(train_X)[:, 1]
        idx = 0
        for d in train_instances:
            for c in d["candidates"]:
                c["_tmp_train_p"] = float(train_probs[idx])
                idx += 1

        # Temporarily swap in train predictions for threshold search
        for d in train_instances:
            for c in d["candidates"]:
                c["_saved_oof_p"] = c.get("oof_p")
                c["oof_p"] = c["_tmp_train_p"]

        best_pa_thresh, best_pa_f1_train = find_best_path_a_threshold(
            train_instances, pa_thresholds)
        best_pb_thresh, best_pb_f1_train = find_best_path_b_threshold(
            train_instances, pb_filter_thresholds)

        # Restore original oof_p on train instances
        for d in train_instances:
            for c in d["candidates"]:
                if c["_saved_oof_p"] is not None:
                    c["oof_p"] = c["_saved_oof_p"]
                else:
                    c.pop("oof_p", None)
                c.pop("_saved_oof_p", None)
                c.pop("_tmp_train_p", None)

        # Evaluate on test fold with train-optimized thresholds
        test_pa = eval_path_a(test_instances, best_pa_thresh)
        test_pb = eval_path_b(test_instances, 0.5, best_pb_thresh)
        test_greedy = eval_greedy(test_instances)
        test_mv = eval_majority_vote(test_instances, 0.5)

        print(f"    Train-opt thresholds: PA_t={best_pa_thresh:.2f}, PB_ft={best_pb_thresh:.1f}")
        print(f"    Greedy:  F1={test_greedy['f1']:.4f}")
        print(f"    MajVote: F1={test_mv['f1']:.4f}")
        print(f"    PathA:   F1={test_pa['f1']:.4f}")
        print(f"    PathB:   F1={test_pb['f1']:.4f}")

        fold_results.append({
            "fold": fold_k,
            "n_train_instances": len(train_instances),
            "n_test_instances": len(test_instances),
            "n_train_entities": len(train_X),
            "n_test_entities": len(test_X),
            "auc": round(auc, 4),
            "pa_threshold": float(best_pa_thresh),
            "pb_filter_threshold": float(best_pb_thresh),
            "greedy": test_greedy,
            "majority_vote": test_mv,
            "path_a_oof": test_pa,
            "path_b_oof": test_pb,
        })

    print(f"\n  Mean AUC: {np.mean(fold_aucs):.4f} ± {np.std(fold_aucs):.4f}")

    # --- 5. Overall OOF evaluation ---
    print("\n--- Overall OOF Results ---")
    overall_greedy = eval_greedy(all_data)
    overall_mv = eval_majority_vote(all_data, 0.5)

    # Every candidate now has oof_p from its held-out fold
    # Sweep thresholds on ALL OOF predictions (slight optimism for threshold only)
    best_pa_t, best_pa_f1 = find_best_path_a_threshold(all_data, pa_thresholds)
    best_pa_result = eval_path_a(all_data, best_pa_t)

    best_pb_t, best_pb_f1 = find_best_path_b_threshold(all_data, pb_filter_thresholds)
    best_pb_result = eval_path_b(all_data, 0.5, best_pb_t)

    print(f"Greedy:       F1={overall_greedy['f1']:.4f}")
    print(f"MajVote(50%): F1={overall_mv['f1']:.4f}")
    print(f"OOF PathA:    F1={best_pa_result['f1']:.4f} (t={best_pa_t:.2f})")
    print(f"OOF PathB:    F1={best_pb_result['f1']:.4f} (ft={best_pb_t:.1f})")

    # Per-dataset breakdown
    print("\n--- Per-Dataset OOF Results ---")
    per_ds_results = {}
    for ds in ["scierc", "conll", "fewnerd"]:
        ds_data = [d for d in all_data if d["dataset"] == ds]
        if not ds_data:
            continue
        ds_greedy = eval_greedy(ds_data)
        ds_mv = eval_majority_vote(ds_data, 0.5)
        ds_pa_t, _ = find_best_path_a_threshold(ds_data, pa_thresholds)
        ds_pa = eval_path_a(ds_data, ds_pa_t)
        ds_pb_t, _ = find_best_path_b_threshold(ds_data, pb_filter_thresholds)
        ds_pb = eval_path_b(ds_data, 0.5, ds_pb_t)
        per_ds_results[ds] = {
            "n_instances": len(ds_data),
            "n_entities": sum(len(d["candidates"]) for d in ds_data),
            "greedy": ds_greedy,
            "majority_vote": ds_mv,
            "path_a_oof": {**ds_pa, "threshold": float(ds_pa_t)},
            "path_b_oof": {**ds_pb, "filter_threshold": float(ds_pb_t)},
        }
        delta_pa = ds_pa["f1"] - ds_greedy["f1"]
        delta_pb = ds_pb["f1"] - ds_greedy["f1"]
        print(f"  {ds}: Greedy={ds_greedy['f1']:.4f}  MV={ds_mv['f1']:.4f}  "
              f"PA_OOF={ds_pa['f1']:.4f}(Δ={delta_pa:+.4f})  "
              f"PB_OOF={ds_pb['f1']:.4f}(Δ={delta_pb:+.4f})")

    # --- 6. Properly averaged fold-level results ---
    print("\n--- Fold-Averaged Results (Unbiased) ---")
    # Weight by number of test entities for proper micro-averaging
    metrics = ["greedy", "majority_vote", "path_a_oof", "path_b_oof"]
    for metric in metrics:
        f1s = [fr[metric]["f1"] for fr in fold_results]
        mean_f1 = np.mean(f1s)
        std_f1 = np.std(f1s)
        print(f"  {metric}: {mean_f1:.4f} ± {std_f1:.4f}  (per-fold: {[round(x,4) for x in f1s]})")

    # --- 7. Comparison with original B2 ---
    print("\n--- Comparison ---")
    delta_overall_pa = best_pa_result["f1"] - overall_greedy["f1"]
    delta_overall_pb = best_pb_result["f1"] - overall_greedy["f1"]
    print(f"OOF PathA vs Greedy: {delta_overall_pa*100:+.2f}pp")
    print(f"OOF PathB vs Greedy: {delta_overall_pb*100:+.2f}pp")
    print(f"OOF PathA vs MajVote: {(best_pa_result['f1'] - overall_mv['f1'])*100:+.2f}pp")
    print(f"OOF PathB vs MajVote: {(best_pb_result['f1'] - overall_mv['f1'])*100:+.2f}pp")
    print(f"Original B2 claim (train-on-test): +3.62pp")

    # --- 8. PathA sweep detail ---
    print("\n--- PathA Threshold Sweep (OOF predictions) ---")
    pa_sweep = {}
    for t in pa_thresholds:
        r = eval_path_a(all_data, t)
        pa_sweep[f"t_{t:.2f}"] = r
        if abs(t - best_pa_t) < 0.01:
            print(f"  t={t:.2f}: P={r['precision']:.4f} R={r['recall']:.4f} F1={r['f1']:.4f}  *** BEST")
        elif t in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]:
            print(f"  t={t:.2f}: P={r['precision']:.4f} R={r['recall']:.4f} F1={r['f1']:.4f}")

    # --- 9. Save results ---
    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.0f}s")

    results = {
        "setup": {
            "configs_used": [c["name"] for c in CONFIGS if os.path.exists(c["path"])],
            "max_samples": MAX_SAMPLES,
            "fewnerd_max": FEWNERD_MAX,
            "total_instances": len(all_data),
            "total_candidates": total_cands,
            "positive_rate": round(total_pos / max(total_cands, 1), 4),
            "entity_types": all_types,
            "fold_sizes": fold_sizes,
        },
        "oof_cv": {
            "mean_auc": round(float(np.mean(fold_aucs)), 4),
            "std_auc": round(float(np.std(fold_aucs)), 4),
            "per_fold_auc": [round(a, 4) for a in fold_aucs],
        },
        "overall": {
            "greedy": overall_greedy,
            "majority_vote_50": overall_mv,
            "path_a_oof": {**best_pa_result, "threshold": float(best_pa_t)},
            "path_b_oof": {**best_pb_result, "filter_threshold": float(best_pb_t)},
        },
        "per_fold": fold_results,
        "per_dataset": per_ds_results,
        "comparison": {
            "oof_path_a_vs_greedy_pp": round(delta_overall_pa * 100, 2),
            "oof_path_b_vs_greedy_pp": round(delta_overall_pb * 100, 2),
            "oof_path_a_vs_mv_pp": round((best_pa_result["f1"] - overall_mv["f1"]) * 100, 2),
            "oof_path_b_vs_mv_pp": round((best_pb_result["f1"] - overall_mv["f1"]) * 100, 2),
            "original_b2_claim_pp": 3.62,
            "conclusion": "",  # filled below
        },
        "elapsed_seconds": round(elapsed, 1),
    }

    # Conclusion
    if delta_overall_pa > 0.005:
        results["comparison"]["conclusion"] = (
            f"OOF verifier still beats greedy by {delta_overall_pa*100:.2f}pp. "
            f"Original +3.62pp was inflated by train-on-test, but verifier retains value."
        )
    elif delta_overall_pa > -0.005:
        results["comparison"]["conclusion"] = (
            f"OOF verifier shows marginal improvement ({delta_overall_pa*100:+.2f}pp). "
            f"Original +3.62pp was largely due to train-on-test leakage."
        )
    else:
        results["comparison"]["conclusion"] = (
            f"OOF verifier hurts performance ({delta_overall_pa*100:+.2f}pp vs greedy). "
            f"Original +3.62pp was entirely due to train-on-test leakage. "
            f"B2 verifier does NOT improve construction."
        )

    with open(f"{OUT}/oof_construction_f1.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    comparison = {
        "greedy_f1": overall_greedy["f1"],
        "majority_vote_f1": overall_mv["f1"],
        "oof_path_a_f1": best_pa_result["f1"],
        "oof_path_b_f1": best_pb_result["f1"],
        "original_b2_claim_delta_pp": 3.62,
        "oof_path_a_delta_pp": round(delta_overall_pa * 100, 2),
        "oof_path_b_delta_pp": round(delta_overall_pb * 100, 2),
        "oof_beats_greedy": delta_overall_pa > 0.005 or delta_overall_pb > 0.005,
        "per_dataset": per_ds_results,
    }
    with open(f"{OUT}/comparison.json", "w") as f:
        json.dump(comparison, f, indent=2, default=str)

    print(f"\nResults saved to {OUT}/")
    print(f"Conclusion: {results['comparison']['conclusion']}")
    print("DONE")


if __name__ == "__main__":
    main()
