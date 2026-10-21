#!/usr/bin/env python3
"""E2v2: Per-Regime Ensemble Weights — grid search optimal 5-signal weights per FT/ZS/FS regime.

Extends E2 by:
  1. Mapping all 16 configs to FT/ZS/FS regimes
  2. Per-regime grid search (step=0.1) for optimal simplex weights
  3. Cross-config (all-regime) grid search for comparison
  4. Paired bootstrap: per-regime optimal vs cross-config optimal
  5. Leave-one-config-out validation within each regime
  6. Per-model-family analysis within FT (Qwen3 vs LLaMA)
"""

import json, os, sys, time, itertools
import numpy as np
from collections import Counter, defaultdict

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import compute_entity_f1, load_and_filter
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys

SIGNALS = ["SJ", "FK", "VC", "EM", "LP"]
BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
OUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/e2v2_regime_weights"

N_SAMPLES = 8
N_FOLDS = 5
GRID_STEP = 0.1
BOOTSTRAP_N = 5000
RNG_SEED = 42

# ─── Config definitions: (config_id, dir_name, dataset, model, regime, seed) ───
CONFIGS = [
    # FT — Qwen3 8B
    ("Qwen3_8B_ft_conll_s123",   "exp_002_conll_n8_seed123",      "conll",   "Qwen3-8B",  "ft", 123),
    ("Qwen3_8B_ft_conll_s456",   "exp_002_conll_n8_seed456",      "conll",   "Qwen3-8B",  "ft", 456),
    ("Qwen3_8B_ft_scierc_s456",  "exp_018_qwen_scierc_seed456",   "scierc",  "Qwen3-8B",  "ft", 456),
    ("Qwen3_8B_ft_scierc_s789",  "exp_022_seed789",               "scierc",  "Qwen3-8B",  "ft", 789),
    ("Qwen3_8B_ft_fewnerd_s123", "exp_021_fewnerd_n8_seed123",    "fewnerd", "Qwen3-8B",  "ft", 123),
    ("Qwen3_8B_ft_fewnerd_s456", "exp_021_fewnerd_n8_seed456",    "fewnerd", "Qwen3-8B",  "ft", 456),
    ("Qwen3_8B_ft_fewnerd_s789", "fewnerd_seed789_merged",        "fewnerd", "Qwen3-8B",  "ft", 789),
    # FT — LLaMA 8B
    ("LLaMA_8B_ft_fewnerd_s42",  "llama_fewnerd_s42",             "fewnerd", "LLaMA-8B",  "ft", 42),
    ("LLaMA_8B_ft_fewnerd_s123", "llama_fewnerd_s123",            "fewnerd", "LLaMA-8B",  "ft", 123),
    ("LLaMA_8B_ft_fewnerd_s456", "llama_fewnerd_s456",            "fewnerd", "LLaMA-8B",  "ft", 456),
    # ZS — Qwen2.5 72B (data cleaned from server; kept for future use)
    ("Qwen2.5_72B_zs_scierc",   "72b_zeroshot_scierc",           "scierc",  "Qwen2.5-72B", "zs", None),
    ("Qwen2.5_72B_zs_conll",    "72b_zeroshot_conll",            "conll",   "Qwen2.5-72B", "zs", None),
    ("Qwen2.5_72B_zs_fewnerd",  "72b_zeroshot_fewnerd",          "fewnerd", "Qwen2.5-72B", "zs", None),
    # FS — Qwen2.5 72B (data cleaned from server; kept for future use)
    ("Qwen2.5_72B_fs_scierc",   "72b_fewshot_signals/scierc",    "scierc",  "Qwen2.5-72B", "fs", None),
    ("Qwen2.5_72B_fs_conll",    "72b_fewshot_signals/conll2003",  "conll",   "Qwen2.5-72B", "fs", None),
    ("Qwen2.5_72B_fs_fewnerd",  "72b_fewshot_signals/fewnerd",   "fewnerd", "Qwen2.5-72B", "fs", None),
]


# ─── Signal computation (identical to E2) ───

def compute_per_sample_signals(inst, n_samples):
    samples = inst["samples"][:n_samples]
    N = len(samples)

    sj_mat = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []),
                samples[j].get("entities", []))
            sj_mat[i][j] = s; sj_mat[j][i] = s
    np.fill_diagonal(sj_mat, 1.0)
    sj = [float(np.mean([sj_mat[k][j] for j in range(N) if j != k])) for k in range(N)]

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

    em = [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]

    lp = []
    for s in samples:
        v = s.get("mean_logprob")
        if v is None:
            v = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp.append(float(v))

    return {"SJ": sj, "FK": fk, "VC": vc, "EM": em, "LP": lp}


# ─── Grid search utilities ───

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
    combo = np.dot(sig_array, weights)
    selected = np.argmax(combo, axis=1)
    return float(f1_array[np.arange(len(f1_array)), selected].mean())


def grid_search_full(sig_array, f1_array, weight_candidates=None):
    if weight_candidates is None:
        weight_candidates = generate_simplex_weights()
    best_f1 = -1
    best_w = None
    top3 = []
    for w in weight_candidates:
        f1 = selection_f1_for_weights(w, sig_array, f1_array)
        top3.append((f1, w.copy()))
        if f1 > best_f1:
            best_f1 = f1
            best_w = w.copy()
    top3.sort(key=lambda x: -x[0])
    return best_w, best_f1, top3[:3]


def grid_search_cv(sig_array, f1_array, n_folds=N_FOLDS, weight_candidates=None):
    if weight_candidates is None:
        weight_candidates = generate_simplex_weights()
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=RNG_SEED)
    fold_test_f1s = []
    for train_idx, test_idx in kf.split(sig_array):
        train_sig = sig_array[train_idx]
        train_f1 = f1_array[train_idx]
        test_sig = sig_array[test_idx]
        test_f1_arr = f1_array[test_idx]
        best_train_f1 = -1
        best_w = None
        for w in weight_candidates:
            f1 = selection_f1_for_weights(w, train_sig, train_f1)
            if f1 > best_train_f1:
                best_train_f1 = f1
                best_w = w.copy()
        test_f1 = selection_f1_for_weights(best_w, test_sig, test_f1_arr)
        fold_test_f1s.append(test_f1)
    return float(np.mean(fold_test_f1s))


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


# ─── Per-config processing ───

def process_config(config_id, dir_name, dataset, model, regime, seed):
    samples_path = os.path.join(BASE, dir_name, "samples.jsonl")
    if not os.path.exists(samples_path):
        return None

    t0 = time.time()
    data = load_and_filter(samples_path, gold_filter=True)
    n_per = min(N_SAMPLES, len(data[0]["samples"]))
    print(f"  {config_id}: {len(data)} instances, N={n_per}")

    sig_list = {s: [] for s in SIGNALS}
    f1_list = []
    greedy_f1_list = []

    for idx, inst in enumerate(data):
        signals = compute_per_sample_signals(inst, n_per)
        for s in SIGNALS:
            sig_list[s].append(signals[s][:n_per])
        gold = inst["gold"]["entities"]
        sample_f1s = [compute_entity_f1(
            inst["samples"][k].get("entities", []), gold) for k in range(n_per)]
        f1_list.append(sample_f1s)
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1_list.append(compute_entity_f1(greedy.get("entities", []), gold))
        if (idx + 1) % 5000 == 0:
            print(f"    signals: {idx+1}/{len(data)} ({time.time()-t0:.0f}s)")

    f1_array = np.array(f1_list)
    greedy_f1_arr = np.array(greedy_f1_list)

    sig_arrays_raw = {}
    for s in SIGNALS:
        arr = np.array(sig_list[s])
        lo, hi = arr.min(), arr.max()
        if hi - lo < 1e-12:
            arr = np.full_like(arr, 0.5)
        else:
            arr = (arr - lo) / (hi - lo)
        sig_arrays_raw[s] = arr

    sig_array = np.stack([sig_arrays_raw[s] for s in SIGNALS], axis=-1)

    single_sel_f1 = {}
    for j, s in enumerate(SIGNALS):
        chosen = np.argmax(sig_array[:, :, j], axis=1)
        per_inst = f1_array[np.arange(len(f1_array)), chosen]
        single_sel_f1[s] = round(float(per_inst.mean()), 4)

    best_single_name = max(single_sel_f1, key=single_sel_f1.get)

    elapsed = time.time() - t0
    print(f"    done ({elapsed:.0f}s), best_single={best_single_name}={single_sel_f1[best_single_name]:.4f}")

    return {
        "config_id": config_id,
        "dataset": dataset,
        "model": model,
        "regime": regime,
        "seed": seed,
        "n_instances": len(data),
        "N": n_per,
        "greedy_f1": float(greedy_f1_arr.mean()),
        "oracle_f1": float(f1_array.max(axis=1).mean()),
        "single_signal_f1": single_sel_f1,
        "best_single_signal": best_single_name,
        "best_single_f1": single_sel_f1[best_single_name],
        "sig_array": sig_array,
        "f1_array": f1_array,
        "greedy_f1_arr": greedy_f1_arr,
    }


# ─── Regime analysis ───

def analyze_group(group_name, configs_data, weight_candidates):
    """Run grid search + LOO for a group of configs."""
    if not configs_data:
        return None

    all_sig = np.concatenate([c["sig_array"] for c in configs_data], axis=0)
    all_f1 = np.concatenate([c["f1_array"] for c in configs_data], axis=0)
    n_total = len(all_f1)

    # Full-data grid search
    best_w, best_f1, top3 = grid_search_full(all_sig, all_f1, weight_candidates)

    # CV grid search
    cv_f1 = grid_search_cv(all_sig, all_f1, weight_candidates=weight_candidates)

    # Single signal baselines
    single_f1 = {}
    for j, s in enumerate(SIGNALS):
        chosen = np.argmax(all_sig[:, :, j], axis=1)
        single_f1[s] = float(all_f1[np.arange(n_total), chosen].mean())
    best_single_name = max(single_f1, key=single_f1.get)
    best_single_f1 = single_f1[best_single_name]

    # Per-instance F1 for ensemble and best single (for bootstrap)
    combo = np.dot(all_sig, best_w)
    ens_selected = np.argmax(combo, axis=1)
    ens_per_inst = all_f1[np.arange(n_total), ens_selected]

    bs_chosen = np.argmax(all_sig[:, :, SIGNALS.index(best_single_name)], axis=1)
    bs_per_inst = all_f1[np.arange(n_total), bs_chosen]

    boot = paired_bootstrap_test(ens_per_inst, bs_per_inst)

    # LOO (leave-one-config-out)
    loo_results = []
    if len(configs_data) >= 3:
        for i in range(len(configs_data)):
            train_sig = np.concatenate([c["sig_array"] for j, c in enumerate(configs_data) if j != i])
            train_f1 = np.concatenate([c["f1_array"] for j, c in enumerate(configs_data) if j != i])
            test_sig = configs_data[i]["sig_array"]
            test_f1 = configs_data[i]["f1_array"]

            loo_w, _, _ = grid_search_full(train_sig, train_f1, weight_candidates)
            loo_test_f1 = selection_f1_for_weights(loo_w, test_sig, test_f1)
            full_test_f1 = selection_f1_for_weights(best_w, test_sig, test_f1)

            loo_results.append({
                "held_out": configs_data[i]["config_id"],
                "loo_weights": dict(zip(SIGNALS, [round(w, 2) for w in loo_w])),
                "loo_test_f1": round(loo_test_f1, 4),
                "full_weights_test_f1": round(full_test_f1, 4),
                "delta_pp": round((loo_test_f1 - full_test_f1) * 100, 2),
            })

    loo_mean_delta = float(np.mean([r["delta_pp"] for r in loo_results])) if loo_results else None

    return {
        "group": group_name,
        "n_configs": len(configs_data),
        "n_instances": n_total,
        "configs": [c["config_id"] for c in configs_data],
        "best_weights": dict(zip(SIGNALS, [round(w, 2) for w in best_w])),
        "full_data_f1": round(best_f1, 4),
        "cv_f1": round(cv_f1, 4),
        "top3_weights": [
            {"weights": dict(zip(SIGNALS, [round(w, 2) for w in t[1]])), "f1": round(t[0], 4)}
            for t in top3
        ],
        "single_signal_f1": {k: round(v, 4) for k, v in single_f1.items()},
        "best_single_signal": best_single_name,
        "best_single_f1": round(best_single_f1, 4),
        "delta_vs_best_single_pp": round((best_f1 - best_single_f1) * 100, 2),
        "bootstrap_ens_vs_best_single": boot,
        "loo_validation": loo_results if loo_results else "insufficient configs (<3)",
        "loo_mean_delta_pp": round(loo_mean_delta, 2) if loo_mean_delta is not None else None,
        "_ens_per_inst": ens_per_inst,
        "_bs_per_inst": bs_per_inst,
    }


def compare_regime_vs_crossconfig(regime_result, crossconfig_result, configs_data, weight_candidates):
    """Compare per-regime optimal weights vs cross-config weights on the regime's instances."""
    if regime_result is None or crossconfig_result is None:
        return None

    all_sig = np.concatenate([c["sig_array"] for c in configs_data])
    all_f1 = np.concatenate([c["f1_array"] for c in configs_data])

    regime_w = np.array([regime_result["best_weights"][s] for s in SIGNALS])
    cross_w = np.array([crossconfig_result["best_weights"][s] for s in SIGNALS])

    regime_combo = np.dot(all_sig, regime_w)
    regime_sel = np.argmax(regime_combo, axis=1)
    regime_f1_per_inst = all_f1[np.arange(len(all_f1)), regime_sel]

    cross_combo = np.dot(all_sig, cross_w)
    cross_sel = np.argmax(cross_combo, axis=1)
    cross_f1_per_inst = all_f1[np.arange(len(all_f1)), cross_sel]

    boot = paired_bootstrap_test(regime_f1_per_inst, cross_f1_per_inst)

    return {
        "regime": regime_result["group"],
        "n_instances": len(all_f1),
        "regime_weights": regime_result["best_weights"],
        "crossconfig_weights": crossconfig_result["best_weights"],
        "regime_f1": round(float(regime_f1_per_inst.mean()), 4),
        "crossconfig_f1": round(float(cross_f1_per_inst.mean()), 4),
        "delta_pp": round((float(regime_f1_per_inst.mean()) - float(cross_f1_per_inst.mean())) * 100, 2),
        "bootstrap": boot,
    }


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    weight_candidates = generate_simplex_weights()
    print(f"Grid: {len(weight_candidates)} simplex points (step={GRID_STEP})")

    # ─── Phase 1: Load all configs ───
    print(f"\n{'='*70}")
    print("Phase 1: Loading configs")
    print(f"{'='*70}")

    loaded = []
    skipped = []
    for config_id, dir_name, dataset, model, regime, seed in CONFIGS:
        result = process_config(config_id, dir_name, dataset, model, regime, seed)
        if result is None:
            skipped.append(config_id)
            print(f"  SKIP {config_id}: samples.jsonl not found")
        else:
            loaded.append(result)

    print(f"\nLoaded: {len(loaded)}, Skipped: {len(skipped)}")
    if skipped:
        print(f"Skipped configs: {skipped}")

    # ─── Phase 2: Group by regime ───
    regime_groups = defaultdict(list)
    model_groups = defaultdict(list)
    for c in loaded:
        regime_groups[c["regime"]].append(c)
        model_groups[c["model"]].append(c)

    print(f"\nRegime distribution:")
    for r, cs in sorted(regime_groups.items()):
        print(f"  {r}: {len(cs)} configs ({', '.join(c['config_id'] for c in cs)})")

    print(f"\nModel distribution:")
    for m, cs in sorted(model_groups.items()):
        print(f"  {m}: {len(cs)} configs")

    # ─── Phase 3: Per-regime grid search ───
    print(f"\n{'='*70}")
    print("Phase 3: Per-regime grid search")
    print(f"{'='*70}")

    regime_results = {}
    for regime_name, configs_data in sorted(regime_groups.items()):
        print(f"\n--- Regime: {regime_name} ({len(configs_data)} configs) ---")
        t0 = time.time()
        result = analyze_group(f"regime_{regime_name}", configs_data, weight_candidates)
        if result:
            regime_results[regime_name] = result
            print(f"  Best weights: {result['best_weights']}")
            print(f"  Full F1: {result['full_data_f1']:.4f}, CV: {result['cv_f1']:.4f}")
            print(f"  Best single: {result['best_single_signal']}={result['best_single_f1']:.4f}")
            print(f"  Δ(ens-single): {result['delta_vs_best_single_pp']:+.2f}pp")
            print(f"  Bootstrap p={result['bootstrap_ens_vs_best_single']['p_value']:.4f}")
            if result["loo_mean_delta_pp"] is not None:
                print(f"  LOO mean Δ: {result['loo_mean_delta_pp']:+.2f}pp")
            print(f"  Time: {time.time()-t0:.0f}s")

    # ─── Phase 4: Cross-config (all regimes pooled) ───
    print(f"\n{'='*70}")
    print("Phase 4: Cross-config analysis (all regimes pooled)")
    print(f"{'='*70}")

    t0 = time.time()
    cross_result = analyze_group("cross_config_all", loaded, weight_candidates)
    if cross_result:
        print(f"  Best weights: {cross_result['best_weights']}")
        print(f"  Full F1: {cross_result['full_data_f1']:.4f}, CV: {cross_result['cv_f1']:.4f}")
        print(f"  Δ(ens-single): {cross_result['delta_vs_best_single_pp']:+.2f}pp")
        print(f"  Time: {time.time()-t0:.0f}s")

    # ─── Phase 5: Per-model-family within FT ───
    print(f"\n{'='*70}")
    print("Phase 5: Per-model-family analysis within FT")
    print(f"{'='*70}")

    model_results = {}
    for model_name, configs_data in sorted(model_groups.items()):
        print(f"\n--- Model: {model_name} ({len(configs_data)} configs) ---")
        t0 = time.time()
        result = analyze_group(f"model_{model_name}", configs_data, weight_candidates)
        if result:
            model_results[model_name] = result
            print(f"  Best weights: {result['best_weights']}")
            print(f"  Full F1: {result['full_data_f1']:.4f}, CV: {result['cv_f1']:.4f}")
            print(f"  LP weight: {result['best_weights']['LP']}")
            print(f"  Time: {time.time()-t0:.0f}s")

    # ─── Phase 6: Comparisons ───
    print(f"\n{'='*70}")
    print("Phase 6: Per-regime vs cross-config comparison")
    print(f"{'='*70}")

    comparisons = {}
    for regime_name, configs_data in regime_groups.items():
        if regime_name in regime_results and cross_result:
            comp = compare_regime_vs_crossconfig(
                regime_results[regime_name], cross_result, configs_data, weight_candidates)
            if comp:
                comparisons[regime_name] = comp
                print(f"  {regime_name}: regime={comp['regime_f1']:.4f} vs cross={comp['crossconfig_f1']:.4f} "
                      f"Δ={comp['delta_pp']:+.2f}pp p={comp['bootstrap']['p_value']:.4f}")

    # ─── Phase 7: Per-config comparison (regime weights vs cross weights) ───
    print(f"\n{'='*70}")
    print("Phase 7: Per-config: regime weights vs cross-config weights")
    print(f"{'='*70}")

    per_config_comparison = []
    for c in loaded:
        regime = c["regime"]
        if regime not in regime_results or cross_result is None:
            continue

        regime_w = np.array([regime_results[regime]["best_weights"][s] for s in SIGNALS])
        cross_w = np.array([cross_result["best_weights"][s] for s in SIGNALS])

        regime_combo = np.dot(c["sig_array"], regime_w)
        regime_sel = np.argmax(regime_combo, axis=1)
        regime_f1 = float(c["f1_array"][np.arange(len(c["f1_array"])), regime_sel].mean())

        cross_combo = np.dot(c["sig_array"], cross_w)
        cross_sel = np.argmax(cross_combo, axis=1)
        cross_f1 = float(c["f1_array"][np.arange(len(c["f1_array"])), cross_sel].mean())

        per_config_comparison.append({
            "config_id": c["config_id"],
            "regime": regime,
            "model": c["model"],
            "dataset": c["dataset"],
            "n_instances": c["n_instances"],
            "regime_weights_f1": round(regime_f1, 4),
            "cross_weights_f1": round(cross_f1, 4),
            "delta_pp": round((regime_f1 - cross_f1) * 100, 2),
        })

    print(f"\n{'Config':<35} {'Regime':>6} {'RegW_F1':>8} {'CrossW_F1':>9} {'Δpp':>6}")
    print("-" * 70)
    for r in per_config_comparison:
        print(f"{r['config_id']:<35} {r['regime']:>6} {r['regime_weights_f1']:>8.4f} "
              f"{r['cross_weights_f1']:>9.4f} {r['delta_pp']:>+6.2f}")

    # ─── Save results ───
    print(f"\n{'='*70}")
    print("Saving results")
    print(f"{'='*70}")

    def clean_result(r):
        if r is None:
            return None
        return {k: v for k, v in r.items() if not k.startswith("_")}

    per_regime_weights = {}
    for regime_name, result in regime_results.items():
        per_regime_weights[regime_name] = clean_result(result)

    with open(os.path.join(OUT_DIR, "per_regime_weights.json"), "w") as f:
        json.dump(per_regime_weights, f, indent=2)
    print(f"  Saved per_regime_weights.json")

    comparison_output = {
        "cross_config": clean_result(cross_result),
        "per_regime": {k: clean_result(v) for k, v in regime_results.items()},
        "per_model_family": {k: clean_result(v) for k, v in model_results.items()},
        "regime_vs_crossconfig": comparisons,
        "per_config_comparison": per_config_comparison,
        "data_availability": {
            "loaded": [c["config_id"] for c in loaded],
            "skipped": skipped,
            "regime_counts": {r: len(cs) for r, cs in regime_groups.items()},
        },
    }
    with open(os.path.join(OUT_DIR, "comparison.json"), "w") as f:
        json.dump(comparison_output, f, indent=2)
    print(f"  Saved comparison.json")

    # ─── Summary ───
    lines = []
    lines.append("# E2v2: Per-Regime Ensemble Weights — Summary\n")
    lines.append(f"Date: {time.strftime('%Y-%m-%d %H:%M')}\n")

    lines.append("## Data Availability\n")
    lines.append(f"- Loaded: {len(loaded)} configs")
    lines.append(f"- Skipped: {len(skipped)} configs (samples.jsonl not found)")
    if skipped:
        lines.append(f"- Missing: {', '.join(skipped)}")
    lines.append(f"- Regime distribution: {dict((r, len(cs)) for r, cs in regime_groups.items())}\n")

    has_zs = "zs" in regime_results
    has_fs = "fs" in regime_results

    if not has_zs and not has_fs:
        lines.append("**⚠ ZS and FS samples.jsonl data has been cleaned from the server.**")
        lines.append("Only FT regime is available. Per-regime FT/ZS/FS comparison is NOT possible.")
        lines.append("To enable this analysis, re-run ZS/FS inference to generate samples.jsonl.\n")

    lines.append("## Per-Regime Optimal Weights\n")
    lines.append(f"| Regime | #Configs | SJ | FK | VC | EM | LP | Full F1 | CV F1 | Δ(ens-single) |")
    lines.append(f"|--------|----------|-----|-----|-----|-----|-----|---------|-------|----------------|")
    for regime_name in ["ft", "zs", "fs"]:
        if regime_name in regime_results:
            r = regime_results[regime_name]
            w = r["best_weights"]
            lines.append(f"| {regime_name.upper()} | {r['n_configs']} | {w['SJ']} | {w['FK']} | {w['VC']} | {w['EM']} | {w['LP']} | {r['full_data_f1']:.4f} | {r['cv_f1']:.4f} | {r['delta_vs_best_single_pp']:+.2f}pp |")
        else:
            lines.append(f"| {regime_name.upper()} | — | — | — | — | — | — | — | — | — |")

    if cross_result:
        w = cross_result["best_weights"]
        lines.append(f"| ALL | {cross_result['n_configs']} | {w['SJ']} | {w['FK']} | {w['VC']} | {w['EM']} | {w['LP']} | {cross_result['full_data_f1']:.4f} | {cross_result['cv_f1']:.4f} | {cross_result['delta_vs_best_single_pp']:+.2f}pp |")
    lines.append("")

    if model_results:
        lines.append("## Per-Model-Family Weights (within FT)\n")
        lines.append(f"| Model | #Configs | SJ | FK | VC | EM | LP | Full F1 | LP weight |")
        lines.append(f"|-------|----------|-----|-----|-----|-----|-----|---------|-----------|")
        for model_name, r in sorted(model_results.items()):
            w = r["best_weights"]
            lines.append(f"| {model_name} | {r['n_configs']} | {w['SJ']} | {w['FK']} | {w['VC']} | {w['EM']} | {w['LP']} | {r['full_data_f1']:.4f} | {w['LP']} |")
        lines.append("")

    if comparisons:
        lines.append("## Regime vs Cross-Config Comparison\n")
        for regime_name, comp in comparisons.items():
            lines.append(f"- **{regime_name.upper()}**: regime={comp['regime_f1']:.4f} vs cross={comp['crossconfig_f1']:.4f}, "
                        f"Δ={comp['delta_pp']:+.2f}pp, p={comp['bootstrap']['p_value']:.4f} "
                        f"({'significant' if comp['bootstrap']['significant_005'] else 'not significant'})")
        lines.append("")

    lines.append("## LP Weight Across Regimes\n")
    for regime_name in ["ft", "zs", "fs"]:
        if regime_name in regime_results:
            lp_w = regime_results[regime_name]["best_weights"]["LP"]
            lines.append(f"- {regime_name.upper()}: LP={lp_w}")
        else:
            lines.append(f"- {regime_name.upper()}: no data")

    if has_zs and "ft" in regime_results:
        ft_lp = regime_results["ft"]["best_weights"]["LP"]
        zs_lp = regime_results["zs"]["best_weights"]["LP"]
        lines.append(f"\nLP weight FT ({ft_lp}) vs ZS ({zs_lp}): {'FT > ZS as expected' if ft_lp > zs_lp else 'unexpected: ZS >= FT'}")
    else:
        lines.append(f"\n**Cannot test hypothesis 'LP weaker in ZS' — ZS data unavailable.**")
    lines.append("")

    if per_config_comparison:
        lines.append("## Per-Config: Regime Weights vs Cross-Config Weights\n")
        wins = sum(1 for r in per_config_comparison if r["delta_pp"] > 0)
        ties = sum(1 for r in per_config_comparison if r["delta_pp"] == 0)
        losses = sum(1 for r in per_config_comparison if r["delta_pp"] < 0)
        lines.append(f"Win/Tie/Loss: {wins}/{ties}/{losses}")
        mean_delta = np.mean([r["delta_pp"] for r in per_config_comparison])
        lines.append(f"Mean Δpp: {mean_delta:+.2f}")
        lines.append("")

    # LOO summary
    for regime_name, r in regime_results.items():
        if r.get("loo_validation") and isinstance(r["loo_validation"], list):
            lines.append(f"## LOO Validation: {regime_name.upper()}\n")
            for loo in r["loo_validation"]:
                lines.append(f"- Hold out {loo['held_out']}: LOO_F1={loo['loo_test_f1']:.4f}, "
                           f"Full_F1={loo['full_weights_test_f1']:.4f}, Δ={loo['delta_pp']:+.2f}pp")
                lines.append(f"  LOO weights: {loo['loo_weights']}")
            lines.append(f"- Mean LOO Δ: {r['loo_mean_delta_pp']:+.2f}pp\n")

    summary_text = "\n".join(lines)
    with open(os.path.join(OUT_DIR, "summary.md"), "w") as f:
        f.write(summary_text)
    print(f"  Saved summary.md")
    print(f"\n{summary_text}")


if __name__ == "__main__":
    main()
