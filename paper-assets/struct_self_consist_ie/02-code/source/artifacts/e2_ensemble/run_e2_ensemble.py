#!/usr/bin/env python3
"""E2: Mixture-of-Signals Ensemble — 5-signal weighted ensemble for sample selection & entity construction.

For each config:
  1. Compute per-sample signals (LP, VC, SJ, FK, EM)
  2. Grid search simplex weights with 5-fold CV → optimal α
  3. Logistic regression (5 signals → binary F1>median) with 5-fold CV
  4. Evaluate selection F1 (best-of-N by ensemble score)
  5. Evaluate entity construction F1 (weighted majority voting)
Cross-config: paired bootstrap ensemble vs best-single-signal.
"""

import json, os, sys, time
import numpy as np
from collections import Counter
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import (compute_entity_f1, compute_degeneracy,
                             load_and_filter, bootstrap_ci, bootstrap_delta_ci)
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys

SIGNALS = ["SJ", "FK", "VC", "EM", "LP"]
BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
OUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/e2_ensemble"

CONFIGS = [
    ("exp_conll_seed123",   "conll",   123),
    ("exp_conll_seed456",   "conll",   456),
    ("exp_fewnerd_seed123", "fewnerd", 123),
    ("exp_fewnerd_seed456", "fewnerd", 456),
    ("exp_fewnerd_seed789", "fewnerd", 789),
    ("exp_scierc_seed456",  "scierc",  456),
    ("exp_scierc_seed789",  "scierc",  789),
]

N_SAMPLES = 8
N_FOLDS = 5
GRID_STEP = 0.2
BOOTSTRAP_N = 5000
RNG_SEED = 42


def compute_per_sample_signals(inst):
    samples = inst["samples"][:N_SAMPLES]
    N = len(samples)

    # SJ: per-sample avg soft Jaccard with others
    sj_mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []),
                samples[j].get("entities", []))
            sj_mat[i][j] = s; sj_mat[j][i] = s
    np.fill_diagonal(sj_mat, 1.0)
    sj = [float(np.mean([sj_mat[k][j] for j in range(N) if j != k])) for k in range(N)]

    # FK: per-sample avg surface-key Jaccard with others
    key_sets = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
    fk_mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            fk_mat[i][j] = s; fk_mat[j][i] = s
    np.fill_diagonal(fk_mat, 1.0)
    fk = [float(np.mean([fk_mat[k][j] for j in range(N) if j != k])) for k in range(N)]

    # VC: voting confidence
    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    vc = []
    for ks in key_sets:
        if not ks:
            vc.append(0.0)
        else:
            vc.append(float(np.mean([all_keys_count[key] / N for key in ks])))

    # EM: exact-match count
    em = [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]

    # LP: mean log probability
    lp = []
    for s in samples:
        v = s.get("mean_logprob")
        if v is None:
            v = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp.append(float(v))

    return {"SJ": sj, "FK": fk, "VC": vc, "EM": em, "LP": lp}


def generate_simplex_weights(n_dim=5, step=GRID_STEP):
    m = int(round(1.0 / step))
    def _recurse(remaining, depth):
        if depth == n_dim - 1:
            yield (remaining * step,)
            return
        for i in range(remaining + 1):
            for rest in _recurse(remaining - i, depth + 1):
                yield (i * step,) + rest
    return [np.array(w) for w in _recurse(m, 0)]


def selection_f1_for_weights(weights, sig_array, f1_array):
    combo = np.dot(sig_array, weights)  # (n_inst, N)
    selected = np.argmax(combo, axis=1)
    return float(f1_array[np.arange(len(f1_array)), selected].mean())


def grid_search_cv(sig_array, f1_array, n_folds=N_FOLDS):
    weight_candidates = generate_simplex_weights()
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=RNG_SEED)

    fold_test_f1s = []
    fold_best_weights = []

    for train_idx, test_idx in kf.split(sig_array):
        best_train_f1 = -1
        best_w = None
        for w in weight_candidates:
            f1 = selection_f1_for_weights(w, sig_array[train_idx], f1_array[train_idx])
            if f1 > best_train_f1:
                best_train_f1 = f1
                best_w = w.copy()
        test_f1 = selection_f1_for_weights(best_w, sig_array[test_idx], f1_array[test_idx])
        fold_test_f1s.append(test_f1)
        fold_best_weights.append(best_w)

    mean_cv_f1 = float(np.mean(fold_test_f1s))

    # Final: select best weights on full data for downstream use
    best_full_f1 = -1
    best_weights = None
    for w in weight_candidates:
        f1 = selection_f1_for_weights(w, sig_array, f1_array)
        if f1 > best_full_f1:
            best_full_f1 = f1
            best_weights = w.copy()

    return best_weights, mean_cv_f1


def logistic_regression_cv(sig_array, f1_array, n_folds=N_FOLDS):
    n_inst, n_sig, N = sig_array.shape[0], sig_array.shape[2], sig_array.shape[1]
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=RNG_SEED)

    fold_sel_f1s = []
    fold_aurocs = []
    all_test_sel_f1 = np.zeros(len(sig_array))
    all_test_mask = np.zeros(len(sig_array), dtype=bool)

    for train_idx, test_idx in kf.split(sig_array):
        X_train_raw = sig_array[train_idx]  # (n_train, N_samples, 5)
        f1_train_raw = f1_array[train_idx]  # (n_train, N_samples)

        X_train = X_train_raw.reshape(-1, n_sig)
        f1_flat = f1_train_raw.reshape(-1)
        median_f1 = np.median(f1_flat[f1_flat > 0]) if np.any(f1_flat > 0) else 0.5
        y_train = (f1_flat > median_f1).astype(int)

        scaler = StandardScaler()
        X_train_sc = scaler.fit_transform(X_train)

        if len(np.unique(y_train)) < 2:
            fold_sel_f1s.append(float(f1_array[test_idx, 0].mean()))
            continue

        lr = LogisticRegression(max_iter=1000, random_state=RNG_SEED)
        lr.fit(X_train_sc, y_train)

        X_test_raw = sig_array[test_idx]  # (n_test, N_samples, 5)
        f1_test_raw = f1_array[test_idx]

        X_test = X_test_raw.reshape(-1, n_sig)
        X_test_sc = scaler.transform(X_test)
        probs = lr.predict_proba(X_test_sc)[:, 1]  # (n_test * N_samples,)
        probs_2d = probs.reshape(-1, X_test_raw.shape[1])  # (n_test, N_samples)

        selected = np.argmax(probs_2d, axis=1)
        sel_f1 = float(f1_test_raw[np.arange(len(f1_test_raw)), selected].mean())
        fold_sel_f1s.append(sel_f1)

        all_test_sel_f1[test_idx] = f1_test_raw[np.arange(len(f1_test_raw)), selected]
        all_test_mask[test_idx] = True

    return {
        "cv_selection_f1": round(float(np.mean(fold_sel_f1s)), 4),
        "per_fold_f1": [round(f, 4) for f in fold_sel_f1s],
    }, all_test_sel_f1


def weighted_entity_construction(inst, weights_per_sample):
    samples = inst["samples"][:N_SAMPLES]
    gold_ents = inst["gold"]["entities"]

    w = np.array(weights_per_sample)
    w_sum = w.sum()
    if w_sum < 1e-12:
        w = np.ones(len(samples)) / len(samples)
        w_sum = 1.0

    entity_votes = Counter()
    for k, s in enumerate(samples):
        for e in s.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_votes[key] += w[k]

    threshold = w_sum * 0.5
    pred_entities = [{"start": k[0], "end": k[1], "type": k[2]}
                     for k, v in entity_votes.items() if v >= threshold]

    return compute_entity_f1(pred_entities, gold_ents)


def paired_bootstrap_test(a, b, n_boot=BOOTSTRAP_N, seed=RNG_SEED):
    a, b = np.array(a), np.array(b)
    n = len(a)
    rng = np.random.RandomState(seed)
    delta = float(a.mean() - b.mean())
    count_better = 0
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        if a[idx].mean() > b[idx].mean():
            count_better += 1
    p_value = 1.0 - count_better / n_boot
    return {"delta": round(delta, 6), "delta_pp": round(delta * 100, 2),
            "p_value": round(p_value, 4), "significant_005": p_value < 0.05}


def process_config(config_name, dataset, seed):
    t0 = time.time()
    samples_path = os.path.join(BASE, config_name, "samples.jsonl")
    data = load_and_filter(samples_path, gold_filter=True)
    N_per = min(N_SAMPLES, len(data[0]["samples"]))
    print(f"\n{'='*60}")
    print(f"{config_name} | {len(data)} instances | N={N_per}")
    print(f"{'='*60}")

    # --- Compute per-sample signals and F1 ---
    sig_list = {s: [] for s in SIGNALS}
    f1_list = []
    greedy_f1_list = []

    for idx, inst in enumerate(data):
        signals = compute_per_sample_signals(inst)
        for s in SIGNALS:
            sig_list[s].append(signals[s][:N_per])
        gold = inst["gold"]["entities"]
        sample_f1s = [compute_entity_f1(
            inst["samples"][k].get("entities", []), gold) for k in range(N_per)]
        f1_list.append(sample_f1s)
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1_list.append(compute_entity_f1(greedy.get("entities", []), gold))
        if (idx + 1) % 2000 == 0:
            print(f"  signals: {idx+1}/{len(data)} ({time.time()-t0:.0f}s)")

    print(f"  signals done ({time.time()-t0:.0f}s)")

    # Build arrays: sig_array (n_inst, N, 5), f1_array (n_inst, N)
    f1_array = np.array(f1_list)  # (n_inst, N)
    greedy_f1_arr = np.array(greedy_f1_list)

    # Normalize signals to [0,1] per-config
    sig_arrays_raw = {}
    for s in SIGNALS:
        arr = np.array(sig_list[s])  # (n_inst, N)
        lo, hi = arr.min(), arr.max()
        if hi - lo < 1e-12:
            arr = np.full_like(arr, 0.5)
        else:
            arr = (arr - lo) / (hi - lo)
        sig_arrays_raw[s] = arr

    sig_array = np.stack([sig_arrays_raw[s] for s in SIGNALS], axis=-1)  # (n_inst, N, 5)

    # --- Single signal baselines ---
    single_sel_f1 = {}
    single_sel_f1_per_inst = {}
    for j, s in enumerate(SIGNALS):
        chosen = np.argmax(sig_array[:, :, j], axis=1)
        per_inst = f1_array[np.arange(len(f1_array)), chosen]
        single_sel_f1[s] = round(float(per_inst.mean()), 4)
        single_sel_f1_per_inst[s] = per_inst

    best_single_name = max(single_sel_f1, key=single_sel_f1.get)
    best_single_f1 = single_sel_f1[best_single_name]
    print(f"  single signal selection F1: {single_sel_f1}")
    print(f"  best single: {best_single_name} = {best_single_f1:.4f}")

    # --- Grid search with 5-fold CV ---
    print(f"  grid search...")
    t1 = time.time()
    best_weights, best_cv_f1 = grid_search_cv(sig_array, f1_array)
    print(f"  grid search done ({time.time()-t1:.0f}s)")
    print(f"  best weights: {dict(zip(SIGNALS, [round(w,2) for w in best_weights]))}")
    print(f"  best CV sel F1: {best_cv_f1:.4f}")

    # Evaluate ensemble on full data with best weights
    combo_full = np.dot(sig_array, best_weights)  # (n_inst, N)
    ens_selected = np.argmax(combo_full, axis=1)
    ens_sel_f1_per_inst = f1_array[np.arange(len(f1_array)), ens_selected]
    ens_sel_f1 = float(ens_sel_f1_per_inst.mean())

    # --- Logistic regression ---
    print(f"  logistic regression...")
    t2 = time.time()
    lr_result, lr_sel_f1_per_inst = logistic_regression_cv(sig_array, f1_array)
    print(f"  LR done ({time.time()-t2:.0f}s), CV sel F1: {lr_result['cv_selection_f1']:.4f}")

    # --- Entity construction (weighted majority voting) ---
    print(f"  entity construction...")
    t3 = time.time()
    # Ensemble-weighted construction
    ens_constr_f1s = []
    # Uniform (majority vote) construction
    uniform_constr_f1s = []
    # Best-single-signal weighted construction
    best_sig_constr_f1s = []
    best_sig_idx = SIGNALS.index(best_single_name)

    for i, inst in enumerate(data):
        combo_scores = combo_full[i]
        w_ens = np.exp(combo_scores - combo_scores.max())  # softmax for weights
        w_ens = w_ens / w_ens.sum()
        ens_constr_f1s.append(weighted_entity_construction(inst, w_ens))

        uniform_constr_f1s.append(weighted_entity_construction(
            inst, np.ones(N_per) / N_per))

        sig_scores = sig_array[i, :, best_sig_idx]
        w_sig = np.exp(sig_scores - sig_scores.max())
        w_sig = w_sig / w_sig.sum()
        best_sig_constr_f1s.append(weighted_entity_construction(inst, w_sig))

    ens_constr_f1 = float(np.mean(ens_constr_f1s))
    uniform_constr_f1 = float(np.mean(uniform_constr_f1s))
    best_sig_constr_f1 = float(np.mean(best_sig_constr_f1s))
    print(f"  construction F1: ensemble={ens_constr_f1:.4f}, uniform={uniform_constr_f1:.4f}, "
          f"best_sig({best_single_name})={best_sig_constr_f1:.4f}")
    print(f"  entity construction done ({time.time()-t3:.0f}s)")

    # --- Oracle / greedy baselines ---
    oracle_f1 = float(f1_array.max(axis=1).mean())
    greedy_f1 = float(greedy_f1_arr.mean())
    random_f1 = float(f1_array.mean())

    # --- Bootstrap: ensemble vs best single ---
    boot = paired_bootstrap_test(
        ens_sel_f1_per_inst, single_sel_f1_per_inst[best_single_name])
    print(f"  bootstrap ens vs {best_single_name}: Δ={boot['delta_pp']:+.2f}pp, p={boot['p_value']:.4f}")

    elapsed = time.time() - t0
    print(f"  total time: {elapsed:.0f}s")

    return {
        "config": config_name,
        "dataset": dataset,
        "seed": seed,
        "n_instances": len(data),
        "N": N_per,
        "greedy_f1": round(greedy_f1, 4),
        "oracle_f1": round(oracle_f1, 4),
        "random_f1": round(random_f1, 4),
        "single_signal_selection_f1": single_sel_f1,
        "best_single_signal": best_single_name,
        "best_single_f1": round(best_single_f1, 4),
        "grid_search": {
            "best_weights": dict(zip(SIGNALS, [round(w, 2) for w in best_weights])),
            "cv_selection_f1": round(best_cv_f1, 4),
            "full_data_selection_f1": round(ens_sel_f1, 4),
            "delta_vs_best_single_pp": round((ens_sel_f1 - best_single_f1) * 100, 2),
        },
        "logistic_regression": lr_result,
        "entity_construction": {
            "ensemble_weighted_f1": round(ens_constr_f1, 4),
            "uniform_majority_f1": round(uniform_constr_f1, 4),
            "best_single_weighted_f1": round(best_sig_constr_f1, 4),
            "ens_delta_vs_uniform_pp": round((ens_constr_f1 - uniform_constr_f1) * 100, 2),
            "ens_delta_vs_best_sig_pp": round((ens_constr_f1 - best_sig_constr_f1) * 100, 2),
        },
        "bootstrap_ens_vs_best_single": boot,
        "elapsed_s": round(elapsed, 1),
        # per-instance arrays for cross-config aggregation
        "_per_inst_ens_sel_f1": ens_sel_f1_per_inst.tolist(),
        "_per_inst_best_single_sel_f1": single_sel_f1_per_inst[best_single_name].tolist(),
        "_per_inst_greedy_f1": greedy_f1_arr.tolist(),
        "_per_inst_ens_constr_f1": ens_constr_f1s,
        "_per_inst_uniform_constr_f1": uniform_constr_f1s,
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    all_results = []

    # Aggregate arrays across configs
    agg_ens_sel = []
    agg_best_single_sel = []
    agg_greedy = []
    agg_ens_constr = []
    agg_uniform_constr = []

    for config_name, dataset, seed in CONFIGS:
        result = process_config(config_name, dataset, seed)
        all_results.append(result)
        agg_ens_sel.extend(result["_per_inst_ens_sel_f1"])
        agg_best_single_sel.extend(result["_per_inst_best_single_sel_f1"])
        agg_greedy.extend(result["_per_inst_greedy_f1"])
        agg_ens_constr.extend(result["_per_inst_ens_constr_f1"])
        agg_uniform_constr.extend(result["_per_inst_uniform_constr_f1"])

    # --- Cross-config summary ---
    print(f"\n{'='*70}")
    print("CROSS-CONFIG SUMMARY")
    print(f"{'='*70}")

    n_total = len(agg_ens_sel)
    ens_mean = float(np.mean(agg_ens_sel))
    best_single_mean = float(np.mean(agg_best_single_sel))
    greedy_mean = float(np.mean(agg_greedy))

    print(f"Total instances: {n_total}")
    print(f"Greedy F1:            {greedy_mean:.4f}")
    print(f"Best-single sel F1:   {best_single_mean:.4f}")
    print(f"Ensemble sel F1:      {ens_mean:.4f}")
    print(f"Δ(ens - best_single): {(ens_mean - best_single_mean)*100:+.2f}pp")

    # Cross-config bootstrap
    cross_boot_sel = paired_bootstrap_test(
        np.array(agg_ens_sel), np.array(agg_best_single_sel))
    print(f"Bootstrap (selection): Δ={cross_boot_sel['delta_pp']:+.2f}pp, p={cross_boot_sel['p_value']:.4f}, "
          f"sig={cross_boot_sel['significant_005']}")

    cross_boot_constr = paired_bootstrap_test(
        np.array(agg_ens_constr), np.array(agg_uniform_constr))
    print(f"Construction: ens={np.mean(agg_ens_constr):.4f}, uniform={np.mean(agg_uniform_constr):.4f}")
    print(f"Bootstrap (construction): Δ={cross_boot_constr['delta_pp']:+.2f}pp, p={cross_boot_constr['p_value']:.4f}")

    # Per-config summary table
    print(f"\n{'='*70}")
    print(f"{'Config':<25} {'Greedy':>7} {'BestSig':>7} {'EnsCV':>7} {'EnsFull':>7} {'Δpp':>6} {'LR_CV':>7} {'EnsConstr':>9} {'UnifConstr':>10}")
    print("-" * 100)
    for r in all_results:
        print(f"{r['config']:<25} {r['greedy_f1']:>7.4f} {r['best_single_f1']:>7.4f} "
              f"{r['grid_search']['cv_selection_f1']:>7.4f} "
              f"{r['grid_search']['full_data_selection_f1']:>7.4f} "
              f"{r['grid_search']['delta_vs_best_single_pp']:>+6.2f} "
              f"{r['logistic_regression']['cv_selection_f1']:>7.4f} "
              f"{r['entity_construction']['ensemble_weighted_f1']:>9.4f} "
              f"{r['entity_construction']['uniform_majority_f1']:>10.4f}")

    # --- Save results ---
    # Remove per-instance arrays from saved JSON (too large)
    save_results = []
    for r in all_results:
        r_clean = {k: v for k, v in r.items() if not k.startswith("_per_inst")}
        save_results.append(r_clean)

    summary = {
        "experiment": "E2_mixture_of_signals_ensemble",
        "n_configs": len(CONFIGS),
        "n_total_instances": n_total,
        "cross_config": {
            "greedy_f1": round(greedy_mean, 4),
            "best_single_selection_f1": round(best_single_mean, 4),
            "ensemble_selection_f1": round(ens_mean, 4),
            "delta_pp": round((ens_mean - best_single_mean) * 100, 2),
            "bootstrap_selection": cross_boot_sel,
            "ensemble_construction_f1": round(float(np.mean(agg_ens_constr)), 4),
            "uniform_construction_f1": round(float(np.mean(agg_uniform_constr)), 4),
            "construction_delta_pp": round((float(np.mean(agg_ens_constr)) - float(np.mean(agg_uniform_constr))) * 100, 2),
            "bootstrap_construction": cross_boot_constr,
        },
        "per_config": save_results,
    }

    out_path = os.path.join(OUT_DIR, "ensemble_results.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
