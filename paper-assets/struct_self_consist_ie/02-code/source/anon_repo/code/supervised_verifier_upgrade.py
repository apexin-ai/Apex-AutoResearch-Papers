#!/usr/bin/env python3
"""Supervised verifier upgrade: LR + MLP + Random Forest on 5 QE signals."""
from __future__ import annotations
import json, os, sys, random, time
import numpy as np
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from consistency import compute_all_consistency_scores, _ner_soft_jaccard_pair
from evaluation import per_instance_f1

from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.inspection import permutation_importance
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

SIGNAL_NAMES = ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]
SEED = 42

DATASETS = {
    "scierc": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
        "subtask": "ner", "subsample_n": 8, "max_instances": None,
    },
    "conll": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
        "subtask": "ner", "subsample_n": None, "max_instances": None,
    },
    "fewnerd": {
        "path": "/root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl",
        "subtask": "ner", "subsample_n": None, "max_instances": 5000,
    },
}

P = lambda *a, **kw: print(*a, **kw, flush=True)

def load_samples(path, max_instances=None):
    with open(path) as f:
        insts = [json.loads(l) for l in f if l.strip()]
    if max_instances and len(insts) > max_instances:
        rng = random.Random(SEED)
        rng.shuffle(insts)
        insts = insts[:max_instances]
    return insts

def subsample_n(instances, n, seed=SEED):
    rng = random.Random(seed)
    out = []
    for inst in instances:
        samples = inst["samples"]
        if len(samples) > n:
            idx = list(range(len(samples)))
            rng.shuffle(idx)
            samples = [samples[i] for i in sorted(idx[:n])]
        out.append({**inst, "samples": samples})
    return out

def compute_exact_match_rate(instances):
    rates = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        if n < 2:
            rates.append(1.0); continue
        sample_keys = [frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities",[])) for s in samples]
        match_count = sum(1 for i in range(n) for j in range(i+1, n) if sample_keys[i] == sample_keys[j])
        total_pairs = n * (n-1) // 2
        rates.append(match_count / total_pairs if total_pairs > 0 else 1.0)
    return rates

def compute_voting_confidence(instances):
    confidences = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        counter = Counter()
        for s in samples:
            for e in s.get("entities", []):
                counter[(e.get("text",""), e.get("type",""))] += 1
        majority_votes = [v / n for v in counter.values() if v > n / 2]
        confidences.append(float(np.mean(majority_votes)) if majority_votes else 0.0)
    return confidences

def compute_mean_logprob(instances):
    lps = []
    for inst in instances:
        sample_lps = [s.get("mean_logprob", float("nan")) for s in inst["samples"]]
        valid = [lp for lp in sample_lps if np.isfinite(lp)]
        lps.append(float(np.mean(valid)) if valid else float("nan"))
    return lps

def compute_all_signals(instances, subtask):
    cons = compute_all_consistency_scores(instances, subtask=subtask)
    return {
        "soft_jaccard": np.array(cons["soft_jaccard"]),
        "fleiss_kappa": np.array(cons["fleiss_kappa"]),
        "logprob": np.array(compute_mean_logprob(instances)),
        "exact_match": np.array(compute_exact_match_rate(instances)),
        "voting_confidence": np.array(compute_voting_confidence(instances)),
    }

def binarize_f1(f1_arr):
    median_f1 = float(np.median(f1_arr))
    y = (f1_arr > median_f1).astype(int)
    if len(set(y)) >= 2:
        return y, median_f1, "above_median"
    y = (f1_arr >= 1.0).astype(int)
    if len(set(y)) >= 2:
        return y, 1.0, "perfect_vs_imperfect"
    y = (f1_arr > np.mean(f1_arr)).astype(int)
    if len(set(y)) >= 2:
        return y, float(np.mean(f1_arr)), "above_mean"
    return None, None, None

def make_clf(name):
    if name == "LR":
        return LogisticRegression(max_iter=1000, random_state=SEED)
    elif name == "MLP":
        return MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=SEED, early_stopping=True, validation_fraction=0.15)
    elif name == "RF":
        return RandomForestClassifier(n_estimators=100, random_state=SEED)

def run_cv_auroc(X, y, n_splits=5):
    results = {}
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=SEED)
    for clf_name in ["LR", "MLP", "RF"]:
        fold_aucs = []
        for train_idx, test_idx in skf.split(X, y):
            scaler = StandardScaler()
            X_tr_s = scaler.fit_transform(X[train_idx])
            X_te_s = scaler.transform(X[test_idx])
            clf = make_clf(clf_name)
            clf.fit(X_tr_s, y[train_idx])
            proba = clf.predict_proba(X_te_s)[:, 1]
            if len(set(y[test_idx])) >= 2:
                fold_aucs.append(roc_auc_score(y[test_idx], proba))
        results[clf_name] = {
            "mean_auroc": round(float(np.mean(fold_aucs)), 4) if fold_aucs else None,
            "std_auroc": round(float(np.std(fold_aucs)), 4) if fold_aucs else None,
        }
    return results

def get_feature_importance(X, y, signal_names):
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    rf = make_clf("RF"); rf.fit(X_s, y)
    rf_imp = {n: round(float(v), 4) for n, v in zip(signal_names, rf.feature_importances_)}
    mlp = make_clf("MLP"); mlp.fit(X_s, y)
    perm = permutation_importance(mlp, X_s, y, n_repeats=10, random_state=SEED, scoring="roc_auc")
    mlp_imp = {n: round(float(v), 4) for n, v in zip(signal_names, perm.importances_mean)}
    lr = make_clf("LR"); lr.fit(X_s, y)
    lr_coef = {n: round(float(abs(v)), 4) for n, v in zip(signal_names, lr.coef_[0])}
    return {"RF_gini": rf_imp, "MLP_permutation": mlp_imp, "LR_abs_coef": lr_coef}

def build_per_sample_features(instances, per_sample_sj, signal_names):
    """Build feature matrix for all samples across all instances (batch)."""
    all_feats = []
    instance_indices = []
    sample_indices = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        n = len(samples)
        if n <= 1:
            instance_indices.append(idx)
            sample_indices.append(0)
            feat = [0.0] * len(signal_names)
            if n == 1:
                for fi, f in enumerate(signal_names):
                    if f == "logprob":
                        feat[fi] = samples[0].get("mean_logprob", -999)
                    elif f == "soft_jaccard":
                        feat[fi] = per_sample_sj[idx][0] if per_sample_sj[idx] else 0.0
                    elif f == "fleiss_kappa":
                        feat[fi] = per_sample_sj[idx][0] if per_sample_sj[idx] else 0.0
            all_feats.append(feat)
            continue

        sample_keys_all = [frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities",[])) for s in samples]
        counter = Counter()
        for s in samples:
            for e in s.get("entities", []):
                counter[(e.get("text",""), e.get("type",""))] += 1

        for k in range(n):
            feat_vec = []
            for f in signal_names:
                if f == "soft_jaccard":
                    feat_vec.append(per_sample_sj[idx][k])
                elif f == "logprob":
                    feat_vec.append(samples[k].get("mean_logprob", -999))
                elif f == "exact_match":
                    matches = sum(1 for j in range(n) if j != k and sample_keys_all[j] == sample_keys_all[k])
                    feat_vec.append(matches / (n-1) if n > 1 else 1.0)
                elif f == "voting_confidence":
                    s_keys = {(e.get("text",""), e.get("type","")) for e in samples[k].get("entities",[])}
                    votes = [counter[key] / n for key in s_keys if counter[key] > n / 2]
                    feat_vec.append(float(np.mean(votes)) if votes else 0.0)
                elif f == "fleiss_kappa":
                    feat_vec.append(per_sample_sj[idx][k])
                else:
                    feat_vec.append(0.0)
            all_feats.append(feat_vec)
            instance_indices.append(idx)
            sample_indices.append(k)

    return np.array(all_feats), instance_indices, sample_indices

def select_best_sample_batch(instances, per_sample_f1s, per_sample_sj, clf, scaler, signal_names):
    X_all, inst_idx, samp_idx = build_per_sample_features(instances, per_sample_sj, signal_names)
    X_all_s = scaler.transform(X_all)
    all_proba = clf.predict_proba(X_all_s)[:, 1]

    n_inst = len(instances)
    best_f1 = [0.0] * n_inst
    best_score = [-1.0] * n_inst
    for i, (iidx, sidx) in enumerate(zip(inst_idx, samp_idx)):
        if all_proba[i] > best_score[iidx]:
            best_score[iidx] = all_proba[i]
            best_f1[iidx] = per_sample_f1s[iidx][sidx]
    return best_f1

def precompute_per_sample_sj(instances):
    all_sj = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        sj_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(i+1, n):
                sim = _ner_soft_jaccard_pair(samples[i].get("entities",[]), samples[j].get("entities",[]))
                sj_matrix[i][j] = sim
                sj_matrix[j][i] = sim
        per_sample = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) if n > 1 else 0.0 for k in range(n)]
        all_sj.append(per_sample)
    return all_sj

def run_dataset(dataset_name, cfg):
    t0 = time.time()
    P(f"\n{'='*60}")
    P(f"  Dataset: {dataset_name}")
    P(f"{'='*60}")

    instances = load_samples(cfg["path"], cfg.get("max_instances"))
    subtask = cfg["subtask"]
    if cfg.get("subsample_n"):
        instances = subsample_n(instances, cfg["subsample_n"])
        P(f"  Subsampled to N={cfg['subsample_n']}")

    valid = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    greedy_f1s = [per_instance_f1(inst.get("greedy", inst["samples"][0]), inst["gold"], subtask=subtask) for inst in valid]
    conditional = [inst for inst, f1 in zip(valid, greedy_f1s) if f1 > 0]
    cond_f1s = np.array([f1 for f1 in greedy_f1s if f1 > 0])
    P(f"  Total={len(instances)}, Valid={len(valid)}, Cond={len(conditional)}, mean_greedy_F1={cond_f1s.mean():.4f}")

    P("  Computing signals...")
    signals = compute_all_signals(conditional, subtask)
    P(f"  Signals done ({time.time()-t0:.1f}s)")

    available = [f for f in SIGNAL_NAMES if f in signals]
    X = np.column_stack([signals[f] for f in available])
    nan_mask = np.isfinite(X).all(axis=1)
    X, cond_clean = X[nan_mask], [inst for inst, m in zip(conditional, nan_mask) if m]
    f1_clean = cond_f1s[nan_mask]

    y, threshold, split_method = binarize_f1(f1_clean)
    if y is None:
        P("  ERROR: cannot binarize"); return None
    P(f"  Binarize: {split_method}, threshold={threshold:.4f}, pos/neg={y.sum()}/{(1-y).sum()}, n={len(y)}")

    P("  5-fold CV AUROC...")
    auroc_results = run_cv_auroc(X, y)
    for n, r in auroc_results.items():
        P(f"    {n}: {r['mean_auroc']:.4f} +/- {r['std_auroc']:.4f}")

    P("  Feature importance...")
    feat_imp = get_feature_importance(X, y, available)
    for method, imps in feat_imp.items():
        P(f"    {method}: {sorted(imps.items(), key=lambda x: x[1], reverse=True)}")

    P("  Per-sample precompute...")
    per_sample_f1s = [[per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"]] for inst in cond_clean]
    per_sample_sj = precompute_per_sample_sj(cond_clean)
    P(f"  Precompute done ({time.time()-t0:.1f}s)")

    greedy_sel = [per_instance_f1(inst.get("greedy", inst["samples"][0]), inst["gold"], subtask=subtask) for inst in cond_clean]
    oracle_sel = [max(sf) for sf in per_sample_f1s]
    random_sel = [float(np.mean(sf)) for sf in per_sample_f1s]
    greedy_mean, oracle_mean, random_mean = float(np.mean(greedy_sel)), float(np.mean(oracle_sel)), float(np.mean(random_sel))

    selection_results = {"greedy": round(greedy_mean, 4), "random_avg": round(random_mean, 4), "oracle": round(oracle_mean, 4)}

    P("  Selection F1 (batch)...")
    for clf_name in ["LR", "MLP", "RF"]:
        scaler = StandardScaler()
        X_s = scaler.fit_transform(X)
        clf = make_clf(clf_name)
        clf.fit(X_s, y)
        sel_f1s = select_best_sample_batch(cond_clean, per_sample_f1s, per_sample_sj, clf, scaler, available)
        sel_mean = float(np.mean(sel_f1s))
        delta = sel_mean - greedy_mean
        selection_results[clf_name] = {"selection_f1": round(sel_mean, 4), "delta_vs_greedy": round(delta, 4)}
        P(f"    {clf_name}: sel_f1={sel_mean:.4f}, delta={delta:+.4f}")

    P(f"    greedy={greedy_mean:.4f}, oracle={oracle_mean:.4f}")
    P(f"  Done ({time.time()-t0:.1f}s)")

    return {
        "n_instances": len(cond_clean), "n_features": len(available), "features": available,
        "binarize_method": split_method, "threshold": round(threshold, 4),
        "auroc": auroc_results, "feature_importance": feat_imp, "selection": selection_results,
    }

def main():
    np.random.seed(SEED); random.seed(SEED)
    all_results = {}
    for ds_name, cfg in DATASETS.items():
        result = run_dataset(ds_name, cfg)
        if result:
            all_results[ds_name] = result

    out_dir = "/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w") as f:
        json.dump(all_results, f, indent=2)
    P(f"\nSaved to {out_dir}/results.json")

    P(f"\n{'='*60}")
    P("  SUMMARY")
    P(f"{'='*60}")
    P(f"{'Dataset':<12} {'Clf':<6} {'AUROC':>8} {'Sel F1':>8} {'d_greedy':>10}")
    P("-" * 50)
    for ds, res in all_results.items():
        for c in ["LR", "MLP", "RF"]:
            a = res["auroc"][c]["mean_auroc"]
            s = res["selection"][c]
            P(f"{ds:<12} {c:<6} {a:>8.4f} {s['selection_f1']:>8.4f} {s['delta_vs_greedy']:>+10.4f}")
        P(f"  greedy={res['selection']['greedy']:.4f}  oracle={res['selection']['oracle']:.4f}  split={res['binarize_method']}")
        P()

    P("Feature Importance (RF Gini):")
    for ds, res in all_results.items():
        si = sorted(res["feature_importance"]["RF_gini"].items(), key=lambda x: x[1], reverse=True)
        P(f"  {ds}: {', '.join(f'{k}={v:.3f}' for k, v in si)}")

    max_delta = max(res["selection"][c]["delta_vs_greedy"] for res in all_results.values() for c in ["LR","MLP","RF"])
    P(f"\nMax delta vs greedy: {max_delta:+.4f}")
    P("Feature bottleneck CONFIRMED." if max_delta < 0.02 else "WARNING: some classifier beats greedy.")

if __name__ == "__main__":
    main()
