#!/usr/bin/env python3
"""Extract training stats from log files for spectral_optim_vision_geometry."""
import re, os, csv, sys
from pathlib import Path
from collections import defaultdict

LOG_DIRS = [
    "/root/runs/spectral_optim_vision_geometry",
    "/root/spectral_optim_vision_geometry/logs",
]

EPOCH_PAT = re.compile(r"epoch=(\d+),\s*train_loss=([\d.]+),\s*val_acc=([\d.]+)%,\s*time=([\d.]+)s")
EPOCH_PAT_V1 = re.compile(r"\[(\w+)\+(\w+)\]\s*epoch\s+(\d+)/(\d+)\s+loss=([\d.]+)\s+val_acc=([\d.]+)%")

def infer_metadata_from_filename(fname):
    fname_lower = fname.lower()
    dataset = "cifar100"
    if "in100" in fname_lower or "imagenet100" in fname_lower:
        dataset = "imagenet100"
    elif "tinyin" in fname_lower or "tinyimagenet" in fname_lower:
        dataset = "tinyimagenet"
    arch = None
    if "resnet50" in fname_lower: arch = "resnet50"
    elif "deit" in fname_lower: arch = "deit_small"
    elif "convnext" in fname_lower: arch = "convnext_tiny"
    opt = None
    if "muon" in fname_lower: opt = "muon"
    elif "adamw" in fname_lower: opt = "adamw"
    elif "sgd" in fname_lower: opt = "sgd"
    elif "lion" in fname_lower: opt = "lion"
    seed = None
    seed_match = re.search(r"_s(\d+)[_.\b]", fname_lower)
    if seed_match: seed = int(seed_match.group(1))
    elif "seed0" in fname_lower: seed = 0
    elif "seed1" in fname_lower: seed = 1
    elif "seed2" in fname_lower: seed = 2
    return arch, opt, dataset, seed

def parse_log(filepath):
    with open(filepath, "r", errors="replace") as f:
        lines = f.readlines()
    if not lines: return []
    fname = os.path.basename(filepath)
    arch_fn, opt_fn, dataset_fn, seed_fn = infer_metadata_from_filename(fname)
    content_head = "".join(lines[:10])
    if "ImageNet-100" in content_head: dataset_fn = "imagenet100"
    elif "TinyImageNet" in content_head: dataset_fn = "tinyimagenet"
    arch_content, opt_content = None, None
    for line in lines[:5]:
        m = re.search(r"model=(\w+)", line)
        if m:
            raw = m.group(1).lower()
            if "resnet" in raw: arch_content = "resnet50"
            elif "deit" in raw: arch_content = "deit_small"
            elif "convnext" in raw: arch_content = "convnext_tiny"
        m = re.search(r"optimizer=(\w+)", line)
        if m: opt_content = m.group(1).lower()
    arch = arch_content or arch_fn
    opt_base = opt_content or opt_fn
    if not arch or not opt_base: return []
    experiments = []
    current_epochs = []
    current_seed = seed_fn
    for line in lines[:5]:
        m = re.search(r"seed=(\d+)", line)
        if m: current_seed = int(m.group(1)); break
    for line in lines:
        seed_marker = re.search(r"seed[=_](\d+)", line, re.IGNORECASE)
        if seed_marker and ("===" in line or "starting" in line.lower()):
            if current_epochs:
                experiments.append({"arch": arch, "optimizer": opt_base, "dataset": dataset_fn, "seed": current_seed, "epochs": current_epochs, "source_file": filepath})
                current_epochs = []
            current_seed = int(seed_marker.group(1))
        m = EPOCH_PAT.search(line)
        if m:
            current_epochs.append({"epoch": int(m.group(1)), "train_loss": float(m.group(2)), "val_acc": float(m.group(3)), "epoch_time_s": float(m.group(4))})
            continue
        m = EPOCH_PAT_V1.search(line)
        if m:
            current_epochs.append({"epoch": int(m.group(3)), "train_loss": float(m.group(5)), "val_acc": float(m.group(6)), "epoch_time_s": None})
    if current_epochs:
        experiments.append({"arch": arch, "optimizer": opt_base, "dataset": dataset_fn, "seed": current_seed, "epochs": current_epochs, "source_file": filepath})
    return experiments

def main():
    log_files = []
    for d in LOG_DIRS:
        if not os.path.isdir(d): continue
        for root, dirs, files in os.walk(d):
            for f in files:
                if f.endswith(".log"): log_files.append(os.path.join(root, f))
    log_files.sort()
    print(f"Found {len(log_files)} log files", file=sys.stderr)
    all_rows = []
    for lf in log_files:
        try:
            exps = parse_log(lf)
            for exp in exps:
                if not exp["epochs"]: continue
                total_time = sum(e["epoch_time_s"] for e in exp["epochs"] if e.get("epoch_time_s"))
                best_val = max(e["val_acc"] for e in exp["epochs"])
                max_epoch = max(e["epoch"] for e in exp["epochs"])
                for e in exp["epochs"]:
                    all_rows.append({"source_file": os.path.basename(exp["source_file"]), "arch": exp["arch"], "optimizer": exp["optimizer"], "dataset": exp["dataset"], "seed": exp["seed"], "max_epoch": max_epoch, "epoch": e["epoch"], "train_loss": e["train_loss"], "val_acc": e["val_acc"], "epoch_time_s": e.get("epoch_time_s", ""), "total_time_s": total_time if total_time > 0 else "", "best_val_acc": best_val})
        except Exception as ex:
            print(f"ERROR: {lf}: {ex}", file=sys.stderr)
    outpath = "/root/spectral_optim_vision_geometry/training_stats_raw_v2.csv"
    fieldnames = ["source_file","arch","optimizer","dataset","seed","max_epoch","epoch","train_loss","val_acc","epoch_time_s","total_time_s","best_val_acc"]
    with open(outpath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_rows)
    print(f"Wrote {len(all_rows)} rows to {outpath}", file=sys.stderr)

    groups = defaultdict(list)
    for r in all_rows:
        key = (r["arch"], r["optimizer"], r["dataset"], str(r["seed"]), str(r["max_epoch"]))
        groups[key].append(r)
    for key in sorted(groups.keys()):
        arch, opt, ds, seed, max_ep = key
        last = groups[key][-1]
        n = len(groups[key])
        if int(max_ep) not in [20, 50]: continue
        if ds not in ["cifar100","imagenet100"]: continue
        print(f"{ds:15s} {arch:15s} {opt:8s} s={seed:4s} ep={max_ep:3s} n={n:3d} best={last['best_val_acc']:>6}% time={str(last['total_time_s']):>8s}s [{last['source_file']}]")

if __name__ == "__main__":
    main()
