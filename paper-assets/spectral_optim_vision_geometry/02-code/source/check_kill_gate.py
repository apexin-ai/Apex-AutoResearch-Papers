#!/usr/bin/env python3
"""
check_kill_gate.py — 50ep Kill Gate 自动判定
输入训练日志，输出 best_val_acc、gap、三档判定。

用法:
  python check_kill_gate.py --arch resnet --muon_log path --adamw_log path
  python check_kill_gate.py --arch deit --muon_log path --adamw_log path
  python check_kill_gate.py --arch resnet --muon_log path --adamw_log path --muon_20ep_acc 77.02
"""
import argparse
import re
import sys


BASELINES = {"resnet": 77.02, "deit": 62.94}

THRESHOLDS = {
    "resnet": {"artifact": 2.0, "partial": 5.0, "kill": 3.0},
    "deit": {"artifact": 5.0, "partial": 10.0, "kill": 5.0},
}


def parse_log(path):
    """Extract per-epoch val_acc from log file. Returns list of (epoch, val_acc)."""
    results = []
    patterns = [
        re.compile(r"epoch=(\d+),.*val_acc=([\d.]+)%"),
        re.compile(r"epoch[:\s]+(\d+).*val[_ ]acc[:\s]+([\d.]+)"),
        re.compile(r'"epoch":\s*(\d+).*"val_acc":\s*([\d.]+)'),
    ]
    with open(path, "r") as f:
        for line in f:
            for pat in patterns:
                m = pat.search(line)
                if m:
                    results.append((int(m.group(1)), float(m.group(2))))
                    break
    if not results:
        print(f"ERROR: No val_acc entries found in {path}", file=sys.stderr)
        sys.exit(1)
    return results


def classify(gap, arch):
    t = THRESHOLDS[arch]
    if gap < t["artifact"]:
        return "Artifact"
    elif gap < t["partial"]:
        return "Partial"
    else:
        return "Real"


def kill_decision(gap, arch):
    t = THRESHOLDS[arch]
    if gap <= t["kill"]:
        return "KILL"
    else:
        return "CONTINUE"


def main():
    parser = argparse.ArgumentParser(description="50ep Kill Gate 自动判定")
    parser.add_argument("--arch", required=True, choices=["resnet", "deit"])
    parser.add_argument("--muon_log", required=True, help="Muon 50ep log path")
    parser.add_argument("--adamw_log", required=True, help="AdamW 50ep log path")
    parser.add_argument("--muon_20ep_acc", type=float, default=None,
                        help="Muon 20ep baseline acc (default: resnet=77.02, deit=62.94)")
    args = parser.parse_args()

    baseline = args.muon_20ep_acc if args.muon_20ep_acc else BASELINES[args.arch]

    muon_data = parse_log(args.muon_log)
    adamw_data = parse_log(args.adamw_log)

    muon_best = max(muon_data, key=lambda x: x[1])
    adamw_best = max(adamw_data, key=lambda x: x[1])

    gap_muon_adamw = muon_best[1] - adamw_best[1]
    gap_adamw_vs_baseline = baseline - adamw_best[1]

    classification = classify(gap_adamw_vs_baseline, args.arch)
    decision = kill_decision(gap_muon_adamw, args.arch)

    arch_name = "ResNet-50" if args.arch == "resnet" else "DeiT-S"
    t = THRESHOLDS[args.arch]

    print("=" * 60)
    print(f"  Kill Gate Report — {arch_name} 50ep")
    print("=" * 60)
    print()
    print(f"  Muon  50ep best_val_acc: {muon_best[1]:.2f}% (epoch {muon_best[0]})")
    print(f"  AdamW 50ep best_val_acc: {adamw_best[1]:.2f}% (epoch {adamw_best[0]})")
    print(f"  Muon  20ep baseline:     {baseline:.2f}%")
    print()
    print("-" * 60)
    print(f"  Muon 50ep - AdamW 50ep gap:      {gap_muon_adamw:+.2f}pp")
    print(f"  Muon 20ep - AdamW 50ep gap:      {gap_adamw_vs_baseline:+.2f}pp")
    print("-" * 60)
    print()
    print(f"  三档判定 (AdamW 50ep vs Muon 20ep baseline):")
    print(f"    gap = {gap_adamw_vs_baseline:.2f}pp")
    print(f"    Artifact: < {t['artifact']}pp | Partial: {t['artifact']}-{t['partial']}pp | Real: >= {t['partial']}pp")
    print(f"    → 判定: {classification}")
    print()
    print(f"  Kill Gate (Muon 50ep - AdamW 50ep):")
    print(f"    gap = {gap_muon_adamw:.2f}pp (threshold: <= {t['kill']}pp → KILL)")
    print(f"    → 决策: {decision}")
    print()
    print("=" * 60)

    if muon_data[-1][0] < 50 or adamw_data[-1][0] < 50:
        print(f"  ⚠ 注意: 训练未完成 (Muon {muon_data[-1][0]}ep, AdamW {adamw_data[-1][0]}ep)")
        print("=" * 60)


if __name__ == "__main__":
    main()
