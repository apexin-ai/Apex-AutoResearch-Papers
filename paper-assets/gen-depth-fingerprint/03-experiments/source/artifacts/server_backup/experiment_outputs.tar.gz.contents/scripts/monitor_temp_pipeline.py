"""
monitor_temp_pipeline.py — Monitor temperature generation jobs and auto-trigger
feature extraction + LOGO classification when each target completes.

Checks every 120s for 4 targets (olmo t=0.5/0.9, qwen3-0.6b t=0.5/0.9).
Generation runs separately (t=0.5 on GPU 0/1, t=0.9 on GPU 2/3).
Feature extraction + eval uses GPU 0 (olmo) and GPU 1 (qwen).
Within each GPU, t=0.5 pipeline must finish before t=0.9 pipeline starts.
"""

import json
import logging
import os
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path("/root/gen-depth-fingerprint")
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
LOG_DIR = ROOT / "logs"

SEED_THRESHOLD = 990
CHECK_INTERVAL = 120
MAX_RETRIES = 3
PYTHON_EXE = "/root/miniconda3/bin/python"

TARGETS = [
    {"name": "olmo_t05", "data_dir": DATA_DIR / "olmo-2-1b-t05", "gpu": 0,
     "model": "olmo-2-1b", "temp": "0.5", "group": "olmo"},
    {"name": "qwen06_t05", "data_dir": DATA_DIR / "qwen3-0.6b-t05", "gpu": 1,
     "model": "qwen3-0.6b", "temp": "0.5", "group": "qwen"},
    {"name": "olmo_t09", "data_dir": DATA_DIR / "olmo-2-1b-t09", "gpu": 0,
     "model": "olmo-2-1b", "temp": "0.9", "group": "olmo"},
    {"name": "qwen06_t09", "data_dir": DATA_DIR / "qwen3-0.6b-t09", "gpu": 1,
     "model": "qwen3-0.6b", "temp": "0.9", "group": "qwen"},
]

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]

triggered = {}    # name -> "running" | "done" | "failed"
processes = {}    # name -> subprocess.Popen
retry_count = {}  # name -> int


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fh = logging.FileHandler(LOG_DIR / "monitor_temp_pipeline.log")
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger = logging.getLogger("monitor")
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


log = setup_logging()


def count_unique_seeds(data_dir: Path) -> int:
    jsonl_file = data_dir / "generations_shard0.jsonl"
    if not jsonl_file.exists():
        return 0
    seeds = set()
    with open(jsonl_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                seeds.add(rec["seed_id"])
            except (json.JSONDecodeError, KeyError):
                continue
    return len(seeds)


def run_pipeline(target: dict):
    """Run feature extraction then LOGO classification for one target."""
    name = target["name"]
    data_dir = target["data_dir"]
    gpu = target["gpu"]
    model = target["model"]
    temp = target["temp"]

    log.info(f"[{name}] Starting pipeline on GPU {gpu}")

    input_jsonl = data_dir / "generations_shard0.jsonl"
    temp_label = temp.replace(".", "")
    features_csv = DATA_DIR / f"features_{model}-t{temp_label}.csv"
    result_json = RESULTS_DIR / f"temp_{model}_t{temp_label}_eval.json"

    # Step A: Feature extraction
    log.info(f"[{name}] Step A: Feature extraction -> {features_csv}")
    extract_cmd = [
        PYTHON_EXE, str(ROOT / "extract_features.py"),
        "--input", str(input_jsonl),
        "--output", str(features_csv),
        "--device", f"cuda:0",
        "--batch-size", "16",
    ]
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(gpu)

    proc = subprocess.run(extract_cmd, env=env, capture_output=True, text=True, timeout=7200)
    if proc.returncode != 0:
        log.error(f"[{name}] Feature extraction FAILED:\n{proc.stderr}")
        return False
    log.info(f"[{name}] Feature extraction done")

    # Step B: LOGO classification
    log.info(f"[{name}] Step B: LOGO classification")
    eval_cmd = [
        PYTHON_EXE, "-c", build_eval_script(model, temp, features_csv, result_json),
    ]
    proc2 = subprocess.run(eval_cmd, capture_output=True, text=True, timeout=3600)
    if proc2.returncode != 0:
        log.error(f"[{name}] Classification FAILED:\n{proc2.stderr}")
        return False
    log.info(f"[{name}] Classification done -> {result_json}")
    if proc2.stdout.strip():
        log.info(f"[{name}] Results:\n{proc2.stdout.strip()}")
    return True


def build_eval_script(model: str, temp: str, features_csv: Path, result_json: Path) -> str:
    return f'''
import json, numpy as np, pandas as pd
from scipy.stats import spearmanr
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

FEATURES = {FEATURES!r}
SEED = 42
N_BOOT = 1000

XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss", use_label_encoder=False)

def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)

def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    return float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))

# Load baseline (8 generators at t=0.7)
baseline = pd.read_csv("{DATA_DIR}/features_all_models.csv")
# Also load llama and mistral
for gen_name, path in [("llama-3.2-3b", "{DATA_DIR}/llama-3.2-3b/features_pythia410m.jsonl"),
                       ("mistral-7b-v0.3", "{DATA_DIR}/mistral-7b-v0.3/features_pythia410m.jsonl")]:
    import os
    if os.path.exists(path):
        recs = [json.loads(l) for l in open(path)]
        for r in recs:
            r["model_name"] = gen_name
        baseline = pd.concat([baseline, pd.DataFrame(recs)[["model_name","seed_id","depth"]+FEATURES]], ignore_index=True)

# Load test features
test_df = pd.read_csv("{features_csv}")
test_df["model_name"] = "{model}"
test_cols = ["model_name","seed_id","depth"] + FEATURES
test_df = test_df[test_cols]

model_name = "{model}"
train_df = baseline[baseline["model_name"] != model_name]
rng = np.random.RandomState(SEED)

results = {{"model": model_name, "temp": {temp}}}

# Binary LOGO: gen-1 vs gen-2+ (depth >= 1)
train_bin = train_df[train_df["depth"] >= 1].copy()
test_bin = test_df[test_df["depth"] >= 1].copy()
train_bin["label"] = (train_bin["depth"] >= 2).astype(int)
test_bin["label"] = (test_bin["depth"] >= 2).astype(int)
train_ds = downsample(train_bin, "label", rng)
clf = XGBClassifier(**XGB_PARAMS)
clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
y_pred = clf.predict(test_bin[FEATURES].values)
y_test = test_bin["label"].values
bin_f1 = float(f1_score(y_test, y_pred, average="macro"))
bin_ci = bootstrap_ci(y_test, y_pred)
results["binary_f1"] = round(bin_f1, 4)
results["binary_ci_95"] = [round(bin_ci[0], 4), round(bin_ci[1], 4)]
results["binary_n_test"] = int(len(test_bin))

# 3-class LOGO: gen-0, gen-1, gen-2+
train_3c = train_df.copy()
test_3c = test_df.copy()
train_3c["label"] = train_3c["depth"].apply(lambda d: 0 if d==0 else (1 if d==1 else 2))
test_3c["label"] = test_3c["depth"].apply(lambda d: 0 if d==0 else (1 if d==1 else 2))
train_ds3 = downsample(train_3c, "label", rng)
params3 = dict(XGB_PARAMS)
params3["num_class"] = 3
params3["objective"] = "multi:softmax"
clf3 = XGBClassifier(**params3)
clf3.fit(train_ds3[FEATURES].values, train_ds3["label"].values)
y_pred3 = clf3.predict(test_3c[FEATURES].values)
y_test3 = test_3c["label"].values
three_f1 = float(f1_score(y_test3, y_pred3, average="macro"))
three_ci = bootstrap_ci(y_test3, y_pred3)
results["three_class_f1"] = round(three_f1, 4)
results["three_class_ci_95"] = [round(three_ci[0], 4), round(three_ci[1], 4)]
results["three_class_n_test"] = int(len(test_3c))

# Spearman rho for entropy_mean vs depth
rho, pval = spearmanr(test_df["entropy_mean"], test_df["depth"])
results["entropy_mean_spearman_rho"] = round(float(rho), 4)
results["entropy_mean_spearman_p"] = float(pval)

# Per-feature Spearman
per_feat_rho = {{}}
for feat in FEATURES:
    r, p = spearmanr(test_df[feat], test_df["depth"])
    per_feat_rho[feat] = round(float(r), 4)
results["per_feature_spearman"] = per_feat_rho

import os
os.makedirs("{RESULTS_DIR}", exist_ok=True)
with open("{result_json}", "w") as f:
    json.dump(results, f, indent=2)

print(f"Binary F1: {{bin_f1:.4f}}  CI: [{{bin_ci[0]:.4f}}, {{bin_ci[1]:.4f}}]")
print(f"3-class F1: {{three_f1:.4f}}  CI: [{{three_ci[0]:.4f}}, {{three_ci[1]:.4f}}]")
print(f"entropy_mean Spearman rho: {{rho:.4f}} (p={{pval:.2e}})")
'''


def can_start(target: dict) -> bool:
    """Check if a target can start its pipeline (GPU not busy from same-group t=0.5)."""
    name = target["name"]
    if name in triggered and triggered[name] in ("running", "done"):
        return False
    if name in triggered and triggered[name] == "failed":
        if retry_count.get(name, 0) >= MAX_RETRIES:
            return False
    # t=0.9 targets must wait for t=0.5 on same group to finish
    if "t09" in name:
        t05_name = name.replace("t09", "t05")
        if t05_name not in triggered or triggered[t05_name] != "done":
            return False
    return True


def main():
    log.info("=" * 60)
    log.info("Temperature pipeline monitor started")
    log.info(f"Targets: {[t['name'] for t in TARGETS]}")
    log.info(f"Seed threshold: {SEED_THRESHOLD}")
    log.info(f"Check interval: {CHECK_INTERVAL}s")
    log.info("=" * 60)

    while True:
        all_done = True

        for target in TARGETS:
            name = target["name"]

            if name in triggered and triggered[name] == "done":
                continue

            all_done = False

            if name in triggered and triggered[name] == "running":
                continue

            n_seeds = count_unique_seeds(target["data_dir"])
            log.info(f"[{name}] {target['data_dir'].name}: {n_seeds} unique seeds")

            if n_seeds >= SEED_THRESHOLD and can_start(target):
                log.info(f"[{name}] READY ({n_seeds} seeds >= {SEED_THRESHOLD}), starting pipeline...")
                triggered[name] = "running"
                try:
                    success = run_pipeline(target)
                    if success:
                        triggered[name] = "done"
                        log.info(f"[{name}] Pipeline COMPLETED successfully")
                    else:
                        triggered[name] = "failed"
                        retry_count[name] = retry_count.get(name, 0) + 1
                        log.error(f"[{name}] Pipeline FAILED (attempt {retry_count[name]}/{MAX_RETRIES})")
                except Exception as e:
                    triggered[name] = "failed"
                    retry_count[name] = retry_count.get(name, 0) + 1
                    log.error(f"[{name}] Pipeline EXCEPTION (attempt {retry_count[name]}/{MAX_RETRIES}): {e}")
            elif n_seeds >= SEED_THRESHOLD and not can_start(target):
                if "t09" in name:
                    t05_name = name.replace("t09", "t05")
                    log.info(f"[{name}] Data ready but waiting for {t05_name} to finish (status: {triggered.get(t05_name, 'pending')})")
                elif triggered.get(name) == "failed" and retry_count.get(name, 0) >= MAX_RETRIES:
                    log.warning(f"[{name}] Max retries ({MAX_RETRIES}) exhausted")

        if all_done or all(triggered.get(t["name"]) in ("done", "failed") for t in TARGETS):
            log.info("=" * 60)
            log.info("All targets processed. Final status:")
            for t in TARGETS:
                log.info(f"  {t['name']}: {triggered.get(t['name'], 'never_ready')}")
            log.info("Monitor exiting.")
            break

        log.info(f"--- Sleeping {CHECK_INTERVAL}s ---")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
