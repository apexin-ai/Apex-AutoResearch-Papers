"""Compute mCE (mean Corruption Error) from CIFAR-100-C CSV results."""
import csv
import os
import sys
import numpy as np

RESULTS_DIR = "/root/autodl-tmp/checkpoints/spectral_optim/cifar100c_results"

BASELINES = {
    "resnet50": "resnet50_adamw",
    "resnet50_ln": "resnet50_ln_adamw",
    "convnext_tiny": "convnext_tiny_adamw",
    "deit_small": "deit_small_adamw",
}

ARCH_MAP = {
    "resnet50_adamw": "resnet50",
    "resnet50_muon": "resnet50",
    "resnet50_shampoo": "resnet50",
    "resnet50_soap": "resnet50",
    "resnet50_ln_adamw": "resnet50_ln",
    "resnet50_ln_muon": "resnet50_ln",
    "convnext_tiny_adamw": "convnext_tiny",
    "convnext_tiny_muon": "convnext_tiny",
    "convnext_tiny_shampoo": "convnext_tiny",
    "convnext_tiny_soap": "convnext_tiny",
    "deit_small_adamw": "deit_small",
    "deit_small_muon": "deit_small",
    "deit_small_shampoo": "deit_small",
    "deit_small_soap": "deit_small",
}

def load_csv(name):
    path = os.path.join(RESULTS_DIR, f"{name}.csv")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return list(csv.DictReader(f))

def get_per_corruption_error(rows):
    corr_errors = {}
    corruptions = sorted(set(r["corruption"] for r in rows))
    for c in corruptions:
        accs = [float(r["accuracy"]) for r in rows if r["corruption"] == c]
        corr_errors[c] = 100.0 - np.mean(accs)
    return corr_errors

def compute_mce(model_errors, baseline_errors):
    corruptions = sorted(set(model_errors.keys()) & set(baseline_errors.keys()))
    ratios = []
    for c in corruptions:
        if baseline_errors[c] > 0:
            ratios.append(model_errors[c] / baseline_errors[c])
    return np.mean(ratios) * 100

def main():
    baseline_data = {}
    for arch, bl_name in BASELINES.items():
        rows = load_csv(bl_name)
        if rows:
            baseline_data[arch] = get_per_corruption_error(rows)
        else:
            print(f"WARNING: Missing baseline CSV for {arch}: {bl_name}")

    print("=" * 90)
    print(f"{'Model':<25} {'Arch':<15} {'Mean Acc%':>10} {'Mean Err%':>10} {'mCE%':>8}")
    print("=" * 90)

    arch_groups = {}
    for model_name in sorted(ARCH_MAP.keys()):
        arch = ARCH_MAP[model_name]
        if arch not in arch_groups:
            arch_groups[arch] = []
        
        rows = load_csv(model_name)
        if rows is None:
            arch_groups[arch].append((model_name, None, None, None))
            continue
        
        mean_acc = np.mean([float(r["accuracy"]) for r in rows])
        mean_err = 100.0 - mean_acc
        model_errors = get_per_corruption_error(rows)
        
        if arch in baseline_data:
            mce = compute_mce(model_errors, baseline_data[arch])
        else:
            mce = None
        
        arch_groups[arch].append((model_name, mean_acc, mean_err, mce))

    for arch in ["resnet50", "resnet50_ln", "convnext_tiny", "deit_small"]:
        if arch not in arch_groups:
            continue
        bl_name = BASELINES[arch]
        print(f"\n--- {arch} (baseline: {bl_name}) ---")
        for model_name, mean_acc, mean_err, mce in sorted(arch_groups[arch], key=lambda x: (x[2] is None, x[2] or 999)):
            if mean_acc is None:
                print(f"  {model_name:<25} {'MISSING':>10}")
            else:
                mce_str = f"{mce:.1f}" if mce is not None else "N/A"
                print(f"  {model_name:<25} {arch:<15} {mean_acc:>9.2f}% {mean_err:>9.2f}% {mce_str:>8}")
    
    print("\n" + "=" * 90)

    # Per-corruption breakdown for each arch
    print("\n\n=== Per-Corruption mCE Breakdown ===")
    for arch in ["resnet50", "resnet50_ln", "convnext_tiny", "deit_small"]:
        if arch not in baseline_data:
            continue
        bl_errors = baseline_data[arch]
        models_in_arch = [m for m in ARCH_MAP if ARCH_MAP[m] == arch]
        
        print(f"\n--- {arch} ---")
        corruptions = sorted(bl_errors.keys())
        header = f"{'Corruption':<22}"
        for m in sorted(models_in_arch):
            header += f" {m.split('_')[-1]:>8}"
        print(header)
        
        for c in corruptions:
            line = f"  {c:<20}"
            for m in sorted(models_in_arch):
                rows = load_csv(m)
                if rows:
                    m_errors = get_per_corruption_error(rows)
                    if c in m_errors and bl_errors[c] > 0:
                        ratio = m_errors[c] / bl_errors[c] * 100
                        line += f" {ratio:>7.1f}%"
                    else:
                        line += f" {'N/A':>8}"
                else:
                    line += f" {'---':>8}"
            print(line)

if __name__ == "__main__":
    main()
