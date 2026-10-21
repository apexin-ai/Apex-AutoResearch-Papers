"""E3: ECE Calibration Analysis.

Quantifies calibration differences across architectures to determine whether
disruption threshold differences (A2: 46.7% relative spread) are explained
by calibration artifacts.
"""
import json, os, sys
import numpy as np
from scipy import stats
from scipy.special import softmax as scipy_softmax

BASE_CLEAN = "/root/entrainment_gated_ft/lm_eval_clean"

ARCHS = ["GDN", "RetNet", "HGRN2"]
RATIOS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]

BENCHMARKS = {
    "lambada": {
        "metric": "acc",
        "task_type": "generation",
        "sample_file": "lambada_openai.jsonl",
    },
    "hellaswag": {
        "metric": "acc_norm",
        "task_type": "multichoice",
        "sample_file": "hellaswag.jsonl",
    },
    "piqa": {
        "metric": "acc",
        "task_type": "multichoice",
        "sample_file": "piqa.jsonl",
    },
    "arc_easy": {
        "metric": "acc",
        "task_type": "multichoice",
        "sample_file": "arc_easy.jsonl",
    },
}

LAMBADA_PATHS = {
    "GDN": {
        "pure":  f"{BASE_CLEAN}/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
        "h24-1": f"{BASE_CLEAN}/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl",
        "h12-1": f"{BASE_CLEAN}/exp007/1.3b/GDN-h12-1/samples/lambada_openai.jsonl",
        "h6-1":  f"{BASE_CLEAN}/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl",
        "h3-1":  f"{BASE_CLEAN}/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
    },
    "RetNet": {
        "pure":  f"{BASE_CLEAN}/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl",
        "h24-1": f"{BASE_CLEAN}/exp007/1.3b/RetNet-h24-1/samples/lambada_openai.jsonl",
        "h12-1": f"{BASE_CLEAN}/exp007/1.3b/RetNet-h12-1/samples/lambada_openai.jsonl",
        "h6-1":  f"{BASE_CLEAN}/exp007/1.3b/RetNet-h6-1/samples/lambada_openai.jsonl",
        "h3-1":  f"{BASE_CLEAN}/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl",
    },
    "HGRN2": {
        "pure":  f"{BASE_CLEAN}/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl",
        "h24-1": f"{BASE_CLEAN}/exp007/1.3b/HGRN2-h24-1/samples/lambada_openai.jsonl",
        "h12-1": f"{BASE_CLEAN}/exp007/1.3b/HGRN2-h12-1/samples/lambada_openai.jsonl",
        "h6-1":  f"{BASE_CLEAN}/exp007/1.3b/HGRN2-h6-1/samples/lambada_openai.jsonl",
        "h3-1":  f"{BASE_CLEAN}/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
    },
}

MULTICHOICE_DIR_MAP = {
    "GDN": {
        "pure":  "1.3B-100B-GatedDeltaNet-pure",
        "h24-1": "1.3B-100B-GatedDeltaNet-hybrid-24-1",
        "h12-1": "1.3B-100B-GatedDeltaNet-hybrid-12-1",
        "h6-1":  "1.3B-100B-GatedDeltaNet-hybrid-6-1",
        "h3-1":  "1.3B-100B-GatedDeltaNet-hybrid-3-1",
    },
    "RetNet": {
        "pure":  "1.3B-100B-RetNet-pure",
        "h24-1": "1.3B-100B-RetNet-hybrid-24-1",
        "h12-1": "1.3B-100B-RetNet-hybrid-12-1",
        "h6-1":  "1.3B-100B-RetNet-hybrid-6-1",
        "h3-1":  "1.3B-100B-RetNet-hybrid-3-1",
    },
    "HGRN2": {
        "pure":  "1.3B-100B-HGRN2-pure",
        "h24-1": "1.3B-100B-HGRN2-hybrid-24-1",
        "h12-1": "1.3B-100B-HGRN2-hybrid-12-1",
        "h6-1":  "1.3B-100B-HGRN2-hybrid-6-1",
        "h3-1":  "1.3B-100B-HGRN2-hybrid-3-1",
    },
}

DISRUPTION_THRESHOLDS = {
    "GDN": 0.696,
    "RetNet": 0.998,
    "HGRN2": 1.137,
}

N_BINS = 15


def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line.strip()))
    samples.sort(key=lambda s: s["doc_id"])
    return samples


def get_lambada_confidence(samples):
    confs, accs = [], []
    for s in samples:
        fr = s["filtered_resps"]
        ll = fr[0][0] if isinstance(fr[0], (list, tuple)) else fr[0]
        confs.append(np.exp(float(ll)))
        accs.append(int(s["acc"]))
    return np.array(confs), np.array(accs)


def get_multichoice_confidence(samples, metric="acc"):
    confs, accs = [], []
    for s in samples:
        fr = s["filtered_resps"]
        lls = np.array([r[0] if isinstance(r, (list, tuple)) else r for r in fr], dtype=np.float64)

        if metric == "acc_norm":
            byte_lens = []
            for arg_pair in s["arguments"]:
                completion = arg_pair[1]
                byte_lens.append(len(completion.encode("utf-8")))
            byte_lens = np.array(byte_lens, dtype=np.float64)
            lls = lls / byte_lens

        p = scipy_softmax(lls)
        correct_idx = int(s["target"])
        confs.append(p[correct_idx])
        accs.append(int(s[metric]))
    return np.array(confs), np.array(accs)


def compute_ece(confidences, accuracies, n_bins=N_BINS):
    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    n = len(confidences)
    ece = 0.0
    mce = 0.0

    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        if i == n_bins - 1:
            mask = (confidences >= lo) & (confidences <= hi)
        else:
            mask = (confidences >= lo) & (confidences < hi)

        bin_count = mask.sum()
        if bin_count == 0:
            continue

        avg_conf = float(confidences[mask].mean())
        avg_acc = float(accuracies[mask].mean())
        gap = abs(avg_acc - avg_conf)

        weight = bin_count / n
        ece += weight * gap
        mce = max(mce, gap)

    return float(ece), float(mce)


def get_sample_path(bench_name, bench_cfg, arch, ratio):
    if bench_name == "lambada":
        return LAMBADA_PATHS[arch][ratio]
    else:
        model_dir = MULTICHOICE_DIR_MAP[arch][ratio]
        return f"{BASE_CLEAN}/{bench_name}/{model_dir}/samples/{bench_cfg['sample_file']}"


def main():
    results = {}
    pure_eces = {arch: [] for arch in ARCHS}

    for bench_name, bench_cfg in BENCHMARKS.items():
        print(f"\n{'='*60}")
        print(f"Benchmark: {bench_name} (metric: {bench_cfg['metric']})")
        print(f"{'='*60}")

        bench_results = {}
        for arch in ARCHS:
            arch_results = {}
            for ratio in RATIOS:
                path = get_sample_path(bench_name, bench_cfg, arch, ratio)
                if not os.path.exists(path):
                    print(f"  SKIP {arch}/{ratio}: file not found")
                    continue

                samples = load_jsonl(path)

                if bench_cfg["task_type"] == "generation":
                    confs, accs = get_lambada_confidence(samples)
                else:
                    confs, accs = get_multichoice_confidence(samples, bench_cfg["metric"])

                ece, mce = compute_ece(confs, accs)
                arch_results[ratio] = {
                    "ECE": round(ece, 6),
                    "MCE": round(mce, 6),
                    "n_bins": N_BINS,
                    "n_samples": len(samples),
                    "mean_confidence": round(float(confs.mean()), 6),
                    "mean_accuracy": round(float(accs.mean()), 6),
                }

                if ratio == "pure":
                    pure_eces[arch].append(ece)

                print(f"  {arch:8s} {ratio:6s}: ECE={ece:.4f}  MCE={mce:.4f}  "
                      f"mean_conf={confs.mean():.4f}  mean_acc={accs.mean():.4f}  n={len(samples)}")

            bench_results[arch] = arch_results
        results[bench_name] = bench_results

    # Correlation: disruption threshold vs pure-model ECE
    print(f"\n{'='*60}")
    print("Disruption Threshold vs ECE Correlation")
    print(f"{'='*60}")

    lambada_pure_eces = []
    thresholds = []
    for arch in ARCHS:
        if "lambada" in results and arch in results["lambada"] and "pure" in results["lambada"][arch]:
            lambada_pure_eces.append(results["lambada"][arch]["pure"]["ECE"])
            thresholds.append(DISRUPTION_THRESHOLDS[arch])

    if len(lambada_pure_eces) >= 3:
        rho, p_val = stats.spearmanr(thresholds, lambada_pure_eces)
        print(f"  LAMBADA pure ECE vs disruption threshold: rho={rho:.4f}, p={p_val:.4f}")
    else:
        rho, p_val = float("nan"), float("nan")

    mean_pure_eces = []
    thresholds_all = []
    for arch in ARCHS:
        if pure_eces[arch]:
            mean_pure_eces.append(np.mean(pure_eces[arch]))
            thresholds_all.append(DISRUPTION_THRESHOLDS[arch])

    if len(mean_pure_eces) >= 3:
        rho_all, p_all = stats.spearmanr(thresholds_all, mean_pure_eces)
        print(f"  Mean pure ECE (all benchmarks) vs disruption threshold: rho={rho_all:.4f}, p={p_all:.4f}")
    else:
        rho_all, p_all = float("nan"), float("nan")

    # ECE spread
    print(f"\n--- ECE Spread (Pure Models, LAMBADA) ---")
    for arch in ARCHS:
        if "lambada" in results and arch in results["lambada"] and "pure" in results["lambada"][arch]:
            e = results["lambada"][arch]["pure"]["ECE"]
            print(f"  {arch}: ECE={e:.4f}, disruption_threshold={DISRUPTION_THRESHOLDS[arch]:.3f}")

    if lambada_pure_eces:
        ece_range = max(lambada_pure_eces) - min(lambada_pure_eces)
        ece_mean = np.mean(lambada_pure_eces)
        ece_rel_spread = ece_range / ece_mean * 100 if ece_mean > 0 else 0
        thresh_range = max(thresholds) - min(thresholds)
        thresh_rel_spread = thresh_range / np.mean(thresholds) * 100
        print(f"  ECE relative spread: {ece_rel_spread:.1f}%")
        print(f"  Disruption threshold relative spread: {thresh_rel_spread:.1f}%")

    results["disruption_threshold_vs_ece_correlation"] = {
        "lambada_pure": {
            "rho": round(rho, 4) if not np.isnan(rho) else None,
            "p": round(p_val, 4) if not np.isnan(p_val) else None,
            "ece_values": {a: round(lambada_pure_eces[i], 6) for i, a in enumerate(ARCHS)} if lambada_pure_eces else {},
            "threshold_values": DISRUPTION_THRESHOLDS,
        },
        "all_benchmarks_mean": {
            "rho": round(rho_all, 4) if not np.isnan(rho_all) else None,
            "p": round(p_all, 4) if not np.isnan(p_all) else None,
            "mean_ece_values": {a: round(mean_pure_eces[i], 6) for i, a in enumerate(ARCHS)} if mean_pure_eces else {},
        },
    }

    out_path = "/root/entrainment_gated_ft/results/e3_calibration.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
