"""
QA Probe Classification: Progress (4-class) and Subtask (binary) probes
on VLA layer features, DINOv2 cls_token, and projector output.
"""
import argparse
import json
import os
import numpy as np
import h5py
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

FEATURE_ROOT = "/root/autodl-tmp/vla-ssd/features"
RESULT_DIR = "/root/autodl-tmp/vla-ssd/results/qa_probe"
RESULT_PATH = os.path.join(RESULT_DIR, "classification_results.json")

TRAINED_DIR = os.path.join(FEATURE_ROOT, "trained_libero_goal")
UNTRAINED_DIR = os.path.join(FEATURE_ROOT, "untrained_libero_goal")
DINO_DIR = os.path.join(FEATURE_ROOT, "dinov2_libero_goal")

LAYER_INDICES = [0, 4, 8, 12, 16, 20, 24, 28, 32]
LAYER_NAMES = [f"L{i}" for i in LAYER_INDICES]

TASKS = [
    "open_the_middle_drawer_of_the_cabinet",
    "open_the_top_drawer_and_put_the_bowl_inside",
    "push_the_plate_to_the_front_of_the_stove",
    "put_the_bowl_on_the_plate",
    "put_the_bowl_on_the_stove",
    "put_the_bowl_on_top_of_the_cabinet",
    "put_the_cream_cheese_in_the_bowl",
    "put_the_wine_bottle_on_the_rack",
    "put_the_wine_bottle_on_top_of_the_cabinet",
    "turn_on_the_stove",
]

SEED = 42


def load_vla_features(h5_path, layer_idx):
    """Load image_mean features for a specific layer from all demos.
    Returns list of arrays, each (T, 4096).
    """
    features_per_demo = []
    with h5py.File(h5_path, "r") as f:
        demo_keys = sorted(f.keys(), key=lambda x: int(x.split("_")[1]))
        for dk in demo_keys:
            feat = f[dk]["image_mean"][:, layer_idx, :]  # (T, 4096)
            features_per_demo.append(feat)
    return features_per_demo


def load_dino_features(h5_path):
    """Load cls_token features from all trajs.
    Returns list of arrays, each (T, 1024).
    """
    features_per_demo = []
    with h5py.File(h5_path, "r") as f:
        traj_keys = sorted(f.keys(), key=lambda x: int(x.split("_")[1]))
        for tk in traj_keys:
            feat = f[tk]["cls_token"][:]  # (T, 1024)
            features_per_demo.append(feat)
    return features_per_demo


def make_progress_labels(features_per_demo):
    """4-class progress labels: each trajectory split into 4 equal segments."""
    labels_per_demo = []
    for feat in features_per_demo:
        T = len(feat)
        labels = np.zeros(T, dtype=int)
        for i in range(T):
            labels[i] = min(int(i / T * 4), 3)
        labels_per_demo.append(labels)
    return labels_per_demo


def make_subtask_labels(features_per_demo):
    """Binary subtask labels: first half=0, second half=1."""
    labels_per_demo = []
    for feat in features_per_demo:
        T = len(feat)
        mid = T // 2
        labels = np.zeros(T, dtype=int)
        labels[mid:] = 1
        labels_per_demo.append(labels)
    return labels_per_demo


def run_probe(features_per_demo, labels_per_demo):
    """Train LogisticRegression probe with random 80/20 split across all demos.
    Returns (accuracy, macro_f1).
    """
    X = np.concatenate(features_per_demo, axis=0)
    y = np.concatenate(labels_per_demo, axis=0)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED, stratify=y
    )

    clf = LogisticRegression(max_iter=1000, C=1.0, random_state=SEED)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")
    return round(acc, 4), round(f1, 4)


def run_task_probe(features_per_demo, label_fn):
    """Run probe for a single task: construct labels and evaluate."""
    labels_per_demo = label_fn(features_per_demo)
    return run_probe(features_per_demo, labels_per_demo)


def evaluate_condition_layers(feat_dir, layer_indices, label_fn, task_files, is_dino=False):
    """Evaluate all layers for a condition across all tasks.
    Returns dict: layer_name -> {acc, f1} (averaged across tasks).
    """
    if is_dino:
        all_task_features = []
        for tf in task_files:
            h5_path = os.path.join(feat_dir, tf)
            feats = load_dino_features(h5_path)
            all_task_features.extend(feats)
        labels = label_fn(all_task_features)
        acc, f1 = run_probe(all_task_features, labels)
        return {"acc": acc, "f1": f1}

    results = {}
    for li, ln in zip(layer_indices, LAYER_NAMES):
        all_task_features = []
        for tf in task_files:
            h5_path = os.path.join(feat_dir, tf)
            feats = load_vla_features(h5_path, li)
            all_task_features.extend(feats)
        labels = label_fn(all_task_features)
        acc, f1 = run_probe(all_task_features, labels)
        results[ln] = {"acc": acc, "f1": f1}
    return results


def find_best(layer_results):
    """Find best layer from results dict."""
    best_layer = max(layer_results, key=lambda k: layer_results[k]["f1"])
    return {"layer": best_layer, **layer_results[best_layer]}


def main():
    parser = argparse.ArgumentParser(description="QA Probe Classification")
    parser.add_argument("--condition", choices=["trained", "untrained", "all"], default="all")
    parser.add_argument("--gpu", type=int, default=0, help="GPU id (unused, CPU-based)")
    parser.add_argument("--dry-run", action="store_true", help="Run 1 task x 1 layer only")
    args = parser.parse_args()

    task_files = [f"{t}.h5" for t in TASKS]

    if args.dry_run:
        task_files = task_files[:1]
        print(f"[DRY-RUN] Using 1 task: {TASKS[0]}")

    results = {
        "method": "Classification probe (LogisticRegression)",
        "tasks": {
            "progress_4class": {},
            "subtask_binary": {},
        },
        "summary": {},
    }

    conditions_to_run = []
    if args.condition in ("trained", "all"):
        conditions_to_run.append("trained")
    if args.condition in ("untrained", "all"):
        conditions_to_run.append("untrained")

    for label_task, label_fn in [
        ("progress_4class", make_progress_labels),
        ("subtask_binary", make_subtask_labels),
    ]:
        print(f"\n{'='*60}")
        print(f"Task: {label_task}")
        print(f"{'='*60}")

        for cond in conditions_to_run:
            feat_dir = TRAINED_DIR if cond == "trained" else UNTRAINED_DIR
            layer_indices_to_use = [LAYER_INDICES[0]] if args.dry_run else LAYER_INDICES
            layer_names_to_use = [LAYER_NAMES[0]] if args.dry_run else LAYER_NAMES

            print(f"\n  Condition: {cond} (layers: {layer_names_to_use})")

            cond_results = {}
            for li, ln in zip(layer_indices_to_use, layer_names_to_use):
                all_task_features = []
                for tf in task_files:
                    h5_path = os.path.join(feat_dir, tf)
                    feats = load_vla_features(h5_path, li)
                    all_task_features.extend(feats)
                labels = label_fn(all_task_features)
                acc, f1 = run_probe(all_task_features, labels)
                cond_results[ln] = {"acc": acc, "f1": f1}
                print(f"    {ln}: acc={acc:.4f}, f1={f1:.4f}")

            results["tasks"][label_task][cond] = cond_results

        # DINOv2
        print(f"\n  Condition: dino_cls")
        all_dino_features = []
        for tf in task_files:
            h5_path = os.path.join(DINO_DIR, tf)
            feats = load_dino_features(h5_path)
            all_dino_features.extend(feats)
        labels = label_fn(all_dino_features)
        acc, f1 = run_probe(all_dino_features, labels)
        results["tasks"][label_task]["dino_cls"] = {"acc": acc, "f1": f1}
        print(f"    dino_cls: acc={acc:.4f}, f1={f1:.4f}")

        # Projector (layer 0 of trained)
        print(f"\n  Condition: projector")
        all_proj_features = []
        for tf in task_files:
            h5_path = os.path.join(TRAINED_DIR, tf)
            feats = load_vla_features(h5_path, 0)
            all_proj_features.extend(feats)
        labels = label_fn(all_proj_features)
        acc, f1 = run_probe(all_proj_features, labels)
        results["tasks"][label_task]["projector"] = {"acc": acc, "f1": f1}
        print(f"    projector: acc={acc:.4f}, f1={f1:.4f}")

    # Summary
    for label_task in ["progress_4class", "subtask_binary"]:
        prefix = "progress" if "progress" in label_task else "subtask"
        task_data = results["tasks"][label_task]

        if "trained" in task_data:
            results["summary"][f"{prefix}_best_trained"] = find_best(task_data["trained"])
        if "untrained" in task_data:
            results["summary"][f"{prefix}_best_untrained"] = find_best(task_data["untrained"])
        results["summary"][f"{prefix}_dino"] = task_data["dino_cls"]
        results["summary"][f"{prefix}_projector"] = task_data["projector"]

    os.makedirs(RESULT_DIR, exist_ok=True)
    with open(RESULT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {RESULT_PATH}")


if __name__ == "__main__":
    main()
