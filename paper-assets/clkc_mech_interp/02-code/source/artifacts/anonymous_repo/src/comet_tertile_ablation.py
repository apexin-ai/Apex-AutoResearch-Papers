"""COMET Tertile Ablation.

Split ZH test set into High/Med/Low tertiles by COMET score,
evaluate cross-lingual probe accuracy per tertile to determine
if translation quality is a confounder.
"""

import argparse
import json
import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import balanced_accuracy_score
from scipy.stats import fisher_exact


def load_passed_comet_scores(data_dir):
    validated = [json.loads(l) for l in open(data_dir / "zh_conflict_test_validated.jsonl")]
    scores = np.array([e["comet_score"] for e in validated])
    return scores


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--best_layer", type=int, required=True)
    parser.add_argument("--model_name", type=str, default="Model")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    best_layer = args.best_layer

    scores_arr = load_passed_comet_scores(data_dir)
    n = len(scores_arr)
    print(f"Loaded COMET scores for {n} passed samples")

    sorted_order = np.argsort(scores_arr)
    t1 = n // 3
    t2 = 2 * n // 3
    low_mask = sorted_order[:t1]
    med_mask = sorted_order[t1:t2]
    high_mask = sorted_order[t2:]

    tertile_info = {
        "low": {"indices": low_mask, "scores": scores_arr[low_mask]},
        "med": {"indices": med_mask, "scores": scores_arr[med_mask]},
        "high": {"indices": high_mask, "scores": scores_arr[high_mask]},
    }
    for name, info in tertile_info.items():
        s = info["scores"]
        print(f"  {name}: n={len(s)}, range=[{s.min():.4f}, {s.max():.4f}], mean={s.mean():.4f}")

    en_data = torch.load(data_dir / "en_activations.pt", map_location="cpu", weights_only=True)
    zh_data = torch.load(data_dir / "zh_activations.pt", map_location="cpu", weights_only=True)

    en_train_n = en_data["split_sizes"]["train"]
    zh_train_n = zh_data["split_sizes"]["train"]

    train_X = en_data["activations"].float()[:en_train_n, best_layer, :].numpy()
    train_y = en_data["labels"][:en_train_n].numpy()
    test_X = zh_data["activations"].float()[zh_train_n:, best_layer, :].numpy()
    test_y = zh_data["labels"][zh_train_n:].numpy()

    scaler = StandardScaler()
    train_X_s = scaler.fit_transform(train_X)
    test_X_s = scaler.transform(test_X)

    clf = LogisticRegression(class_weight="balanced", solver="lbfgs", max_iter=1000, random_state=42)
    clf.fit(train_X_s, train_y)

    full_preds = clf.predict(test_X_s)
    full_bal_acc = balanced_accuracy_score(test_y, full_preds)

    results = {"model": args.model_name, "direction": "EN→ZH", "best_layer": best_layer}
    tertiles_result = {}

    for name in ["low", "med", "high"]:
        mask = tertile_info[name]["indices"]
        s = tertile_info[name]["scores"]
        sub_preds = full_preds[mask]
        sub_y = test_y[mask]
        bal_acc = balanced_accuracy_score(sub_y, sub_preds)
        n_correct = int(np.sum(sub_preds == sub_y))
        n_total = len(sub_y)
        tertiles_result[name] = {
            "n": n_total,
            "comet_range": [round(float(s.min()), 4), round(float(s.max()), 4)],
            "comet_mean": round(float(s.mean()), 4),
            "balanced_acc": round(bal_acc, 4),
            "n_correct": n_correct,
            "n_incorrect": n_total - n_correct,
        }

    results["tertiles"] = tertiles_result
    results["full_balanced_acc"] = round(full_bal_acc, 4)

    h = tertiles_result["high"]
    l = tertiles_result["low"]
    table = np.array([[h["n_correct"], h["n_incorrect"]], [l["n_correct"], l["n_incorrect"]]])
    odds_ratio, p_value = fisher_exact(table)

    delta = tertiles_result["high"]["balanced_acc"] - tertiles_result["low"]["balanced_acc"]
    delta_pp = round(delta * 100, 2)
    is_confounder = delta_pp >= 5 and delta_pp > 0

    results["fisher_test"] = {
        "high_vs_low_p": round(p_value, 6),
        "odds_ratio": round(odds_ratio, 4) if not np.isinf(odds_ratio) else "inf",
    }
    results["delta_high_low_pp"] = delta_pp
    results["conclusion"] = "confounder" if is_confounder else "not_confounder"

    out_path = Path(args.output) if args.output else data_dir / "comet_tertile_ablation.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")
    print(f"Delta (High - Low): {delta_pp:+.2f} pp, Fisher p={p_value:.6f}")
    print(f"Conclusion: {'CONFOUNDER' if is_confounder else 'NOT CONFOUNDER'}")


if __name__ == "__main__":
    main()
