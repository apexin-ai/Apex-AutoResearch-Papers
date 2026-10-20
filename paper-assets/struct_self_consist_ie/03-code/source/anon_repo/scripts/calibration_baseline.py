"""
Calibration Baseline: Platt Scaling & Temperature Scaling for LP-based selection.
Uses 5-fold CV to avoid train-test leak.

Key insight: standard Platt/TempScale are monotonic transforms of LP, so they
improve probability estimates (ECE) but cannot change argmax-based selection.
We additionally test a multi-feature Platt variant (LP + n_tokens + n_entities)
which is NOT monotonic in LP and can potentially change selection.
"""
import json
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from scipy.optimize import minimize_scalar
from scipy.special import expit

WORK_DIR = Path("/root/autodl-tmp/struct_self_consist_ie")
OUTPUT_DIR = WORK_DIR / "output"

DATASETS = {
    "SciERC": OUTPUT_DIR / "exp_012_rerun_1024" / "samples_with_logprobs.jsonl",
    "CoNLL": OUTPUT_DIR / "exp_002_conll_n16_r1024" / "samples.jsonl",
    "Few-NERD": OUTPUT_DIR / "exp_027_fewnerd_n16" / "samples.jsonl",
}


def compute_ner_f1(pred_entities, gold_entities):
    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in pred_entities}
    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1)) for e in gold_entities}
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set)
    rec = tp / len(gold_set)
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)


def load_dataset(path):
    """Load dataset, return list of dicts with per-sample LP, F1, and features."""
    instances = []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            gold_ents = row["gold"]["entities"]
            samples = row["samples"]
            greedy = row.get("greedy")

            sample_data = []
            for s in samples:
                lp = s.get("mean_logprob")
                if lp is None:
                    lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
                f1 = compute_ner_f1(s.get("entities", []), gold_ents)
                n_tokens = s.get("n_tokens", 0)
                n_entities = len(s.get("entities", []))
                sample_data.append({
                    "lp": lp, "f1": f1,
                    "n_tokens": n_tokens, "n_entities": n_entities,
                })

            greedy_f1 = None
            if greedy:
                greedy_f1 = compute_ner_f1(greedy.get("entities", []), gold_ents)

            instances.append({
                "id": row["id"],
                "samples": sample_data,
                "greedy_f1": greedy_f1,
            })
    return instances


def make_binary_labels(instances):
    """For each instance, label samples: F1 >= median → 1, else → 0."""
    all_lps = []
    all_labels = []
    all_features = []  # [lp, n_tokens, n_entities]
    instance_indices = []

    for idx, inst in enumerate(instances):
        f1s = [s["f1"] for s in inst["samples"]]
        median_f1 = np.median(f1s)
        for s in inst["samples"]:
            all_lps.append(s["lp"])
            all_labels.append(1 if s["f1"] >= median_f1 else 0)
            all_features.append([s["lp"], s["n_tokens"], s["n_entities"]])
            instance_indices.append(idx)

    return (np.array(all_lps), np.array(all_labels),
            np.array(all_features), np.array(instance_indices))


def compute_ece(probs, labels, n_bins=10):
    """Expected Calibration Error."""
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    bin_data = []
    for i in range(n_bins):
        if i == n_bins - 1:
            mask = (probs >= bin_edges[i]) & (probs <= bin_edges[i + 1])
        else:
            mask = (probs >= bin_edges[i]) & (probs < bin_edges[i + 1])
        if mask.sum() == 0:
            bin_data.append({"bin_center": (bin_edges[i] + bin_edges[i+1]) / 2,
                             "avg_confidence": None, "avg_accuracy": None, "count": 0})
            continue
        avg_conf = probs[mask].mean()
        avg_acc = labels[mask].mean()
        ece += mask.sum() / len(probs) * abs(avg_conf - avg_acc)
        bin_data.append({"bin_center": (bin_edges[i] + bin_edges[i+1]) / 2,
                         "avg_confidence": float(avg_conf), "avg_accuracy": float(avg_acc),
                         "count": int(mask.sum())})
    return float(ece), bin_data


def platt_scaling_cv(instances, n_splits=5):
    """5-fold CV Platt scaling (LP only). Monotonic → same selection as raw LP."""
    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)
    n_instances = len(instances)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    predicted_probs = np.full(len(all_lps), np.nan)
    slopes = []
    intercepts = []

    for train_idx, test_idx in kf.split(np.arange(n_instances)):
        train_set = set(train_idx)
        test_set = set(test_idx)
        train_mask = np.isin(inst_indices, list(train_set))
        test_mask = np.isin(inst_indices, list(test_set))

        X_train = all_lps[train_mask].reshape(-1, 1)
        y_train = all_labels[train_mask]
        X_test = all_lps[test_mask].reshape(-1, 1)

        if len(np.unique(y_train)) < 2:
            predicted_probs[test_mask] = 0.5
            slopes.append(0.0)
            intercepts.append(0.0)
            continue

        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)
        clf.fit(X_train, y_train)
        predicted_probs[test_mask] = clf.predict_proba(X_test)[:, 1]
        slopes.append(float(clf.coef_[0, 0]))
        intercepts.append(float(clf.intercept_[0]))

    # Selection (monotonic → same as raw LP)
    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)
    ece, reliability = compute_ece(predicted_probs, all_labels)

    return {
        "mean_f1": float(np.mean(selection_f1s)),
        "slope_mean": float(np.mean(slopes)),
        "intercept_mean": float(np.mean(intercepts)),
        "ece": ece,
        "reliability": reliability,
        "per_instance_f1": selection_f1s,
    }


def multifeature_platt_cv(instances, n_splits=5):
    """5-fold CV Platt with features [LP, n_tokens, n_entities].
    NOT monotonic in LP → can change selection."""
    all_lps, all_labels, all_features, inst_indices = make_binary_labels(instances)
    n_instances = len(instances)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    predicted_probs = np.full(len(all_lps), np.nan)
    coefs = []

    for train_idx, test_idx in kf.split(np.arange(n_instances)):
        train_set = set(train_idx)
        test_set = set(test_idx)
        train_mask = np.isin(inst_indices, list(train_set))
        test_mask = np.isin(inst_indices, list(test_set))

        X_train = all_features[train_mask]
        y_train = all_labels[train_mask]
        X_test = all_features[test_mask]

        if len(np.unique(y_train)) < 2:
            predicted_probs[test_mask] = 0.5
            coefs.append([0.0, 0.0, 0.0])
            continue

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        clf = LogisticRegression(solver='lbfgs', max_iter=1000, C=1.0)
        clf.fit(X_train_s, y_train)
        predicted_probs[test_mask] = clf.predict_proba(X_test_s)[:, 1]
        coefs.append(clf.coef_[0].tolist())

    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)
    ece, reliability = compute_ece(predicted_probs, all_labels)

    avg_coefs = np.mean(coefs, axis=0).tolist()
    return {
        "mean_f1": float(np.mean(selection_f1s)),
        "coefs_mean": {"lp": avg_coefs[0], "n_tokens": avg_coefs[1], "n_entities": avg_coefs[2]},
        "ece": ece,
        "reliability": reliability,
        "per_instance_f1": selection_f1s,
    }


def temperature_scaling_cv(instances, n_splits=5):
    """5-fold CV Temperature scaling. Monotonic → same selection as raw LP."""
    all_lps, all_labels, _, inst_indices = make_binary_labels(instances)
    n_instances = len(instances)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    calibrated_lps = np.full(len(all_lps), np.nan)
    temperatures = []

    for train_idx, test_idx in kf.split(np.arange(n_instances)):
        train_set = set(train_idx)
        test_set = set(test_idx)
        train_mask = np.isin(inst_indices, list(train_set))
        test_mask = np.isin(inst_indices, list(test_set))

        lps_train = all_lps[train_mask]
        labels_train = all_labels[train_mask]
        lps_test = all_lps[test_mask]

        def nll(log_tau):
            tau = np.exp(log_tau)
            logits = lps_train / tau
            probs = expit(logits)
            probs = np.clip(probs, 1e-7, 1 - 1e-7)
            return -np.mean(labels_train * np.log(probs) + (1 - labels_train) * np.log(1 - probs))

        result = minimize_scalar(nll, bounds=(-5, 5), method='bounded')
        tau = np.exp(result.x)
        temperatures.append(float(tau))

        calibrated_lps[test_mask] = lps_test / tau

    # Convert to probs for ECE
    predicted_probs = expit(calibrated_lps)

    selection_f1s = _select_by_probs(instances, predicted_probs, inst_indices)
    ece, reliability = compute_ece(predicted_probs, all_labels)

    return {
        "mean_f1": float(np.mean(selection_f1s)),
        "tau_mean": float(np.mean(temperatures)),
        "ece": ece,
        "reliability": reliability,
        "per_instance_f1": selection_f1s,
    }


def _select_by_probs(instances, probs, inst_indices):
    """Select sample with highest prob per instance."""
    selection_f1s = []
    for idx, inst in enumerate(instances):
        n_samples = len(inst["samples"])
        mask = inst_indices == idx
        p = probs[mask]
        assert len(p) == n_samples
        if np.all(p == p[0]):
            selected = 0
        else:
            selected = int(np.argmax(p))
        selection_f1s.append(inst["samples"][selected]["f1"])
    return selection_f1s


def raw_lp_selection(instances):
    """Baseline: select sample with highest raw LP."""
    selection_f1s = []
    for inst in instances:
        lps = [s["lp"] for s in inst["samples"]]
        if all(lp == lps[0] for lp in lps):
            selected = 0
        else:
            selected = int(np.argmax(lps))
        selection_f1s.append(inst["samples"][selected]["f1"])
    return selection_f1s


def oracle_selection(instances):
    return [max(s["f1"] for s in inst["samples"]) for inst in instances]


def compute_raw_ece(instances):
    """ECE for raw LP using rank-based probability within instance."""
    all_probs = []
    all_labels = []
    for inst in instances:
        f1s = [s["f1"] for s in inst["samples"]]
        lps = [s["lp"] for s in inst["samples"]]
        median_f1 = np.median(f1s)
        n = len(lps)
        ranks = np.argsort(np.argsort(lps))
        probs = (ranks + 1) / n
        for i, s in enumerate(inst["samples"]):
            all_probs.append(probs[i])
            all_labels.append(1 if s["f1"] >= median_f1 else 0)
    return compute_ece(np.array(all_probs), np.array(all_labels))


def paired_bootstrap(f1s_a, f1s_b, n_bootstrap=10000, seed=42):
    """Paired bootstrap: is B better than A?"""
    rng = np.random.RandomState(seed)
    a = np.array(f1s_a)
    b = np.array(f1s_b)
    n = len(a)
    observed = float(b.mean() - a.mean())
    deltas = np.array([b[rng.randint(0, n, n)].mean() - a[rng.randint(0, n, n)].mean()
                       for _ in range(n_bootstrap)])
    return {
        "observed_delta": observed,
        "ci_95": [float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))],
        "p_value": float(np.mean(deltas <= 0)),
    }


def main():
    results = {}

    for name, path in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"  Dataset: {name}")
        print(f"{'='*60}")

        instances = load_dataset(path)
        n_instances = len(instances)
        n_samples = len(instances[0]["samples"])
        print(f"  Instances: {n_instances}, Samples/instance: {n_samples}")

        # Baselines
        raw_f1s = raw_lp_selection(instances)
        raw_mean = np.mean(raw_f1s)
        g_f1s = [inst["greedy_f1"] for inst in instances if inst["greedy_f1"] is not None]
        greedy_mean = float(np.mean(g_f1s)) if g_f1s else None
        oracle_f1s = oracle_selection(instances)
        oracle_mean = float(np.mean(oracle_f1s))

        # Calibration methods
        print(f"  Running Platt scaling (5-fold CV)...")
        platt = platt_scaling_cv(instances)

        print(f"  Running Multi-feature Platt (5-fold CV)...")
        mf_platt = multifeature_platt_cv(instances)

        print(f"  Running Temperature scaling (5-fold CV)...")
        temp = temperature_scaling_cv(instances)

        # Raw ECE
        raw_ece, raw_rel = compute_raw_ece(instances)

        # Statistical tests (multi-feature Platt is the only one that can differ)
        mf_vs_raw = paired_bootstrap(raw_f1s, mf_platt["per_instance_f1"])

        # Print
        print(f"\n  Results:")
        if greedy_mean: print(f"    Greedy F1:          {greedy_mean:.4f}")
        print(f"    Raw LP F1:          {raw_mean:.4f}")
        print(f"    Platt LP F1:        {platt['mean_f1']:.4f}  (monotonic → same as raw)")
        print(f"    Multi-feat Platt:   {mf_platt['mean_f1']:.4f}")
        print(f"    TempScale LP F1:    {temp['mean_f1']:.4f}  (monotonic → same as raw)")
        print(f"    Oracle F1:          {oracle_mean:.4f}")

        print(f"\n  Learned Parameters:")
        print(f"    Platt: slope={platt['slope_mean']:.4f}, intercept={platt['intercept_mean']:.4f}")
        print(f"    Multi-feat coefs: LP={mf_platt['coefs_mean']['lp']:.4f}, "
              f"n_tok={mf_platt['coefs_mean']['n_tokens']:.4f}, "
              f"n_ent={mf_platt['coefs_mean']['n_entities']:.4f}")
        print(f"    TempScale: τ={temp['tau_mean']:.4f}")

        print(f"\n  Calibration Quality (ECE):")
        print(f"    Raw LP (rank-based): {raw_ece:.4f}")
        print(f"    Platt:               {platt['ece']:.4f}")
        print(f"    Multi-feat Platt:    {mf_platt['ece']:.4f}")
        print(f"    TempScale:           {temp['ece']:.4f}")

        print(f"\n  Multi-feat Platt vs Raw LP:")
        print(f"    Δ={mf_vs_raw['observed_delta']:+.4f}, "
              f"95% CI=[{mf_vs_raw['ci_95'][0]:+.4f}, {mf_vs_raw['ci_95'][1]:+.4f}], "
              f"p={mf_vs_raw['p_value']:.4f}")

        results[name] = {
            "n_instances": n_instances,
            "n_samples_per_instance": n_samples,
            "greedy_f1": greedy_mean,
            "raw_lp_f1": float(raw_mean),
            "platt_lp_f1": platt["mean_f1"],
            "multifeature_platt_f1": mf_platt["mean_f1"],
            "tempscale_lp_f1": temp["mean_f1"],
            "oracle_f1": oracle_mean,
            "note_monotonic": "Platt and TempScale are monotonic transforms of LP; "
                              "argmax-based selection is unchanged. Multi-feature Platt "
                              "uses [LP, n_tokens, n_entities] and CAN change selection.",
            "params": {
                "platt": {"slope": platt["slope_mean"], "intercept": platt["intercept_mean"]},
                "multifeature_platt": mf_platt["coefs_mean"],
                "tempscale": {"tau": temp["tau_mean"]},
            },
            "calibration": {
                "raw_ece": raw_ece,
                "platt_ece": platt["ece"],
                "multifeature_platt_ece": mf_platt["ece"],
                "tempscale_ece": temp["ece"],
                "raw_reliability": raw_rel,
                "platt_reliability": platt["reliability"],
                "multifeature_platt_reliability": mf_platt["reliability"],
                "tempscale_reliability": temp["reliability"],
            },
            "statistical_tests": {
                "multifeature_platt_vs_raw": mf_vs_raw,
            },
        }

    # Summary table
    print(f"\n\n{'='*90}")
    print(f"  SUMMARY TABLE")
    print(f"{'='*90}")
    print(f"{'Dataset':<10} | {'Greedy':>8} | {'Raw LP':>8} | {'Platt':>8} | {'MF-Platt':>8} | {'TempScl':>8} | {'Oracle':>8}")
    print(f"{'-'*10}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}")
    for name in DATASETS:
        r = results[name]
        g = f"{r['greedy_f1']:.4f}" if r['greedy_f1'] else "N/A"
        print(f"{name:<10} | {g:>8} | {r['raw_lp_f1']:>8.4f} | {r['platt_lp_f1']:>8.4f} | "
              f"{r['multifeature_platt_f1']:>8.4f} | {r['tempscale_lp_f1']:>8.4f} | {r['oracle_f1']:>8.4f}")

    print(f"\n  NOTE: Platt & TempScale = Raw LP (monotonic transform preserves argmax).")
    print(f"  Multi-feature Platt uses [LP, n_tokens, n_entities] → non-monotonic → can differ.")

    # Save
    out_path = OUTPUT_DIR / "calibration_baseline_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to: {out_path}")


if __name__ == "__main__":
    main()
