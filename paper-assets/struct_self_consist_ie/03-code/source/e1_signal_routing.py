#!/usr/bin/env python3
"""E1 Adaptive Signal Routing: config-level construction method router."""

import json
import os
from collections import Counter

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = os.path.join(BASE, "output")

CONSTRUCTION_METHODS = [
    "lp_selection", "majority_vote", "consensus_theta2n", "consensus_lp_weighted"
]

CONFIG_SPECS = [
    # (path, dataset_key, model_family, model_size, regime, seed, forced_dataset)
    (f"{OUT}/exp_scierc_seed456/full_signal_report.json", "scierc", "Qwen3", 8, "ft", 456, "scierc"),
    (f"{OUT}/exp_scierc_seed789/full_signal_report.json", "scierc", "Qwen3", 8, "ft", 789, "scierc"),
    (f"{OUT}/exp_conll_seed123/full_signal_report.json", "conll", "Qwen3", 8, "ft", 123, "conll"),
    (f"{OUT}/exp_conll_seed456/full_signal_report.json", "conll", "Qwen3", 8, "ft", 456, "conll"),
    (f"{OUT}/exp_fewnerd_seed123/full_signal_report.json", "fewnerd", "Qwen3", 8, "ft", 123, "fewnerd"),
    (f"{OUT}/exp_fewnerd_seed456/full_signal_report.json", "fewnerd", "Qwen3", 8, "ft", 456, "fewnerd"),
    (f"{OUT}/exp_fewnerd_seed789/full_signal_report.json", "fewnerd", "Qwen3", 8, "ft", 789, "fewnerd"),
    (f"{OUT}/72b_zeroshot/full_signal_report.json", "scierc", "Qwen2.5", 72, "zs", None, "scierc"),
    (f"{OUT}/72b_zeroshot/full_signal_report.json", "conll2003", "Qwen2.5", 72, "zs", None, "conll"),
    (f"{OUT}/72b_zeroshot/full_signal_report.json", "fewnerd", "Qwen2.5", 72, "zs", None, "fewnerd"),
    (f"{OUT}/72b_fewshot_signals/scierc/full_signal_report.json", "scierc", "Qwen2.5", 72, "fs", None, "scierc"),
    (f"{OUT}/72b_fewshot_signals/conll2003/full_signal_report.json", "conll", "Qwen2.5", 72, "fs", None, "conll"),
    (f"{OUT}/72b_fewshot_signals/fewnerd/full_signal_report.json", "fewnerd", "Qwen2.5", 72, "fs", None, "fewnerd"),
    (f"{OUT}/fewnerd_7b/qwen25_7b_n8_seed42/full_signal_report.json", "qwen25_7b_n8_seed42", "Qwen2.5", 7, "ft", 42, "fewnerd"),
    (f"{OUT}/fewnerd_7b/qwen25_7b_n8_seed123/full_signal_report.json", "qwen25_7b_n8_seed123", "Qwen2.5", 7, "ft", 123, "fewnerd"),
    (f"{OUT}/fewnerd_7b/qwen25_7b_n8_seed456/full_signal_report.json", "qwen25_7b_n8_seed456", "Qwen2.5", 7, "ft", 456, "fewnerd"),
]

FEATURE_NAMES = [
    "model_size", "model_family", "dataset", "regime",
    "base_f1", "degeneracy_rate", "oracle_headroom",
    "rho_SJ", "rho_FK", "rho_LP", "rho_EM", "rho_VC"
]


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.bool_,)):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


def load_config(path, dataset_key, model_family, model_size, regime, seed, forced_dataset):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    if dataset_key in data:
        d = data[dataset_key]
    else:
        keys = list(data.keys())
        d = data[keys[0]] if len(keys) == 1 else data

    baselines = d.get("baselines", {})
    greedy_f1 = baselines.get("greedy", {}).get("mean", d.get("greedy_f1"))
    oracle_f1 = baselines.get("oracle", {}).get("mean", d.get("oracle_f1"))
    if greedy_f1 is None:
        return None

    signals = d.get("signals", {})
    construction_f1 = {m: baselines[m]["mean"] for m in CONSTRUCTION_METHODS if m in baselines}

    return {
        "config_id": f"{model_family}_{model_size}B_{regime}_{forced_dataset}_s{seed}",
        "model_family": model_family,
        "model_size": model_size,
        "dataset": forced_dataset,
        "regime": regime,
        "seed": seed,
        "greedy_f1": greedy_f1,
        "oracle_f1": oracle_f1,
        "oracle_headroom": oracle_f1 - greedy_f1 if oracle_f1 else None,
        "degeneracy_rate": d.get("degeneracy_rate", 0),
        "n_instances": d.get("n_instances"),
        "rho_SJ": signals.get("SJ", {}).get("rho", 0),
        "rho_FK": signals.get("FK", {}).get("rho", 0),
        "rho_LP": signals.get("LP", {}).get("rho", 0),
        "rho_EM": signals.get("EM", {}).get("rho", 0),
        "rho_VC": signals.get("VC", {}).get("rho", 0),
        "construction_f1": construction_f1,
    }


def compute_delta_f1(config):
    greedy = config["greedy_f1"]
    return {m: f1 - greedy for m, f1 in config["construction_f1"].items()}


def get_label(config, simplify=False):
    deltas = compute_delta_f1(config)
    if not deltas:
        return "none", 0.0
    best_method = max(deltas, key=deltas.get)
    best_delta = deltas[best_method]
    label = "none" if best_delta <= 0 else best_method
    if simplify and label in ("consensus_theta2n", "consensus_lp_weighted"):
        label = "consensus"
    return label, best_delta


def build_features(config):
    ds_map = {"scierc": 0, "conll": 1, "fewnerd": 2}
    regime_map = {"ft": 0, "zs": 1, "fs": 2}
    family_map = {"Qwen3": 0, "Qwen2.5": 1, "LLaMA": 2}
    return [
        config["model_size"],
        family_map.get(config["model_family"], 0),
        ds_map.get(config["dataset"], 0),
        regime_map.get(config["regime"], 0),
        config["greedy_f1"],
        config["degeneracy_rate"],
        config["oracle_headroom"] or 0,
        config["rho_SJ"],
        config["rho_FK"],
        config["rho_LP"],
        config["rho_EM"],
        config["rho_VC"],
    ]


def resolve_router_delta(predicted, deltas):
    if predicted == "none":
        return 0
    if predicted == "consensus":
        return max(deltas.get("consensus_theta2n", -999), deltas.get("consensus_lp_weighted", -999))
    return deltas.get(predicted, 0)


def run_experiment(configs, simplify_labels, exp_name):
    print(f"\n{'#'*70}")
    print(f"# {exp_name}")
    print(f"{'#'*70}")

    labels = []
    feature_matrix = []
    per_config_results = []

    for c in configs:
        label, best_delta = get_label(c, simplify=simplify_labels)
        labels.append(label)
        feature_matrix.append(build_features(c))
        deltas = compute_delta_f1(c)
        lp_delta = deltas.get("lp_selection", 0)
        per_config_results.append({
            "config_id": c["config_id"],
            "model_family": c["model_family"],
            "model_size": c["model_size"],
            "dataset": c["dataset"],
            "regime": c["regime"],
            "greedy_f1": round(c["greedy_f1"], 4),
            "oracle_f1": round(c["oracle_f1"], 4),
            "degeneracy_rate": round(c["degeneracy_rate"], 4),
            "construction_deltas_pp": {k: round(v * 100, 2) for k, v in deltas.items()},
            "best_method": label,
            "best_delta_pp": round(best_delta * 100, 2),
            "lp_delta_pp": round(lp_delta * 100, 2),
        })

    X = np.array(feature_matrix)
    label_counts = Counter(labels)
    print(f"\nLabel distribution: {dict(label_counts)}")
    for pcr in per_config_results:
        print(f"  {pcr['config_id']:40s} -> {pcr['best_method']:20s} (D={pcr['best_delta_pp']:+.2f}pp, LP={pcr['lp_delta_pp']:+.2f}pp)")

    le = LabelEncoder()
    y = le.fit_transform(labels)
    class_names = [str(c) for c in le.classes_]

    loo = LeaveOneOut()
    scaler = StandardScaler()

    results = {}
    for model_name, model_cls, model_kwargs in [
        ("LogisticRegression", LogisticRegression, {"C": 1.0, "max_iter": 1000}),
        ("RandomForest", RandomForestClassifier, {"n_estimators": 100, "max_depth": 3, "random_state": 42}),
    ]:
        preds = []
        pred_labels_list = []
        for train_idx, test_idx in loo.split(X):
            X_tr, X_te = X[train_idx], X[test_idx]
            y_tr = y[train_idx]
            Xs_tr = scaler.fit_transform(X_tr)
            Xs_te = scaler.transform(X_te)
            model = model_cls(**model_kwargs)
            model.fit(Xs_tr, y_tr)
            pred = model.predict(Xs_te)[0]
            preds.append(pred)
            pred_labels_list.append(str(le.inverse_transform([pred])[0]))

        accuracy = float(np.mean(np.array(preds) == y))
        n = len(configs)

        router_delta_sum = oracle_delta_sum = lp_delta_sum = 0.0
        for i, c in enumerate(configs):
            deltas = compute_delta_f1(c)
            router_delta_sum += resolve_router_delta(pred_labels_list[i], deltas)
            oracle_delta_sum += max(max(deltas.values()), 0) if deltas else 0
            lp_delta_sum += deltas.get("lp_selection", 0)

        router_avg = router_delta_sum / n
        oracle_avg = oracle_delta_sum / n
        lp_avg = lp_delta_sum / n

        cm = confusion_matrix(y, preds, labels=range(len(class_names)))

        Xs_all = scaler.fit_transform(X)
        full_model = model_cls(**model_kwargs)
        full_model.fit(Xs_all, y)
        if hasattr(full_model, "feature_importances_"):
            imp = full_model.feature_importances_
        elif hasattr(full_model, "coef_"):
            imp = np.abs(full_model.coef_).mean(axis=0) if full_model.coef_.ndim > 1 else np.abs(full_model.coef_)
        else:
            imp = np.zeros(X.shape[1])
        feature_imp = sorted(
            {FEATURE_NAMES[i]: round(float(imp[i]), 4) for i in range(len(FEATURE_NAMES))}.items(),
            key=lambda x: -x[1]
        )

        print(f"\n{'='*60}")
        print(f"{model_name}")
        print(f"  LOO Accuracy:     {accuracy:.1%} ({int(accuracy * n)}/{n})")
        print(f"  Router avg dF1:   {router_avg*100:+.2f} pp")
        print(f"  Always-LP dF1:    {lp_avg*100:+.2f} pp")
        print(f"  Oracle dF1:       {oracle_avg*100:+.2f} pp")
        print(f"  Top features: {feature_imp[:5]}")
        print(f"  CM classes: {class_names}")
        for ri, row in enumerate(cm):
            print(f"    {class_names[ri]:25s}: {[int(x) for x in row]}")
        for i in range(n):
            ok = "OK" if pred_labels_list[i] == labels[i] else "XX"
            print(f"    {configs[i]['config_id']:40s} true={labels[i]:20s} pred={pred_labels_list[i]:20s} [{ok}]")

        per_config_preds = []
        for i, c in enumerate(configs):
            deltas = compute_delta_f1(c)
            pd_ = resolve_router_delta(pred_labels_list[i], deltas)
            per_config_preds.append({
                "config_id": c["config_id"],
                "actual": labels[i],
                "predicted": pred_labels_list[i],
                "correct": bool(labels[i] == pred_labels_list[i]),
                "predicted_delta_pp": round(pd_ * 100, 2),
            })

        results[model_name] = {
            "accuracy": round(accuracy, 4),
            "n_correct": int(accuracy * n),
            "n_total": n,
            "router_avg_delta_pp": round(router_avg * 100, 2),
            "always_lp_avg_delta_pp": round(lp_avg * 100, 2),
            "oracle_avg_delta_pp": round(oracle_avg * 100, 2),
            "feature_importance": dict(feature_imp),
            "confusion_matrix": {"classes": class_names, "matrix": [[int(x) for x in row] for row in cm]},
            "per_config_predictions": per_config_preds,
        }

    return per_config_results, dict(label_counts), results


def main():
    configs = []
    missing = []
    for spec in CONFIG_SPECS:
        c = load_config(*spec)
        if c is None:
            missing.append(spec[0])
        else:
            configs.append(c)

    print(f"Loaded {len(configs)} configs, {len(missing)} missing")
    if missing:
        print(f"Missing: {missing}")

    pcr_5, lc_5, res_5 = run_experiment(configs, False, "5-class (fine-grained)")
    pcr_3, lc_3, res_3 = run_experiment(configs, True, "3-class (lp/consensus/none)")

    all_accs = [(f"5class_{m}", r["accuracy"], r) for m, r in res_5.items()]
    all_accs += [(f"3class_{m}", r["accuracy"], r) for m, r in res_3.items()]
    best_name, best_acc, best_r = max(all_accs, key=lambda x: (x[1], x[2]["router_avg_delta_pp"]))

    print(f"\n\n{'#'*70}")
    print(f"# BEST: {best_name} | Acc={best_acc:.1%} | Router={best_r['router_avg_delta_pp']:+.2f}pp | LP={best_r['always_lp_avg_delta_pp']:+.2f}pp | Oracle={best_r['oracle_avg_delta_pp']:+.2f}pp")
    print(f"{'#'*70}")

    output = {
        "experiment": "E1_adaptive_signal_routing",
        "n_configs": len(configs),
        "missing_configs": missing,
        "construction_methods": CONSTRUCTION_METHODS,
        "method_mapping": {
            "lp_selection": "LP signal-based sample selection",
            "majority_vote": "Token-level majority voting",
            "consensus_theta2n": "Entity-level voting (uniform, threshold=2/N)",
            "consensus_lp_weighted": "Entity-level voting (LP-weighted)",
        },
        "feature_names": FEATURE_NAMES,
        "experiments": {
            "5_class": {
                "label_distribution": lc_5,
                "per_config_data": pcr_5,
                "models": res_5,
            },
            "3_class_simplified": {
                "description": "Merged consensus_theta2n + consensus_lp_weighted -> consensus",
                "label_distribution": lc_3,
                "per_config_data": pcr_3,
                "models": res_3,
            },
        },
        "summary": {
            "best_model": best_name,
            "best_accuracy": best_acc,
            "best_router_delta_pp": best_r["router_avg_delta_pp"],
            "always_lp_delta_pp": best_r["always_lp_avg_delta_pp"],
            "oracle_delta_pp": best_r["oracle_avg_delta_pp"],
            "router_beats_lp": best_r["router_avg_delta_pp"] > best_r["always_lp_avg_delta_pp"],
            "accuracy_above_60": best_acc > 0.6,
        },
    }

    out_dir = os.path.join(BASE, "artifacts", "e1_signal_routing")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "routing_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, cls=NumpyEncoder)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
