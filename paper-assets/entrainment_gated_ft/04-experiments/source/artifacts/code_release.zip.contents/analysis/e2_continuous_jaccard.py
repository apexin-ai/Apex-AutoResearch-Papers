"""E2: Continuous-Threshold Jaccard Sensitivity Analysis.

Proves that low cross-architecture Jaccard is not an artifact of binary decomposition.
Sweeps confidence-change threshold tau and computes pairwise Jaccard with bootstrap CI.
"""
import json, os, sys
import numpy as np
from itertools import combinations
from scipy.special import softmax as scipy_softmax

BASE_CLEAN = "/root/entrainment_gated_ft/lm_eval_clean"

ARCHS = ["GDN", "RetNet", "HGRN2"]
ARCH_PAIRS = list(combinations(ARCHS, 2))

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
    "GDN":    {"pure": f"{BASE_CLEAN}/exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
               "h3-1": f"{BASE_CLEAN}/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl"},
    "RetNet": {"pure": f"{BASE_CLEAN}/exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl",
               "h3-1": f"{BASE_CLEAN}/exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl"},
    "HGRN2":  {"pure": f"{BASE_CLEAN}/exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl",
               "h3-1": f"{BASE_CLEAN}/exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl"},
}

MULTICHOICE_DIR_MAP = {
    "GDN":    {"pure": "1.3B-100B-GatedDeltaNet-pure",    "h3-1": "1.3B-100B-GatedDeltaNet-hybrid-3-1"},
    "RetNet": {"pure": "1.3B-100B-RetNet-pure",            "h3-1": "1.3B-100B-RetNet-hybrid-3-1"},
    "HGRN2":  {"pure": "1.3B-100B-HGRN2-pure",             "h3-1": "1.3B-100B-HGRN2-hybrid-3-1"},
}

TAUS = [0.0, 0.01, 0.05, 0.10, 0.20, 0.30]
N_BOOTSTRAP = 1000
RNG = np.random.RandomState(42)


def load_jsonl(path):
    samples = []
    with open(path) as f:
        for line in f:
            samples.append(json.loads(line.strip()))
    samples.sort(key=lambda s: s["doc_id"])
    return samples


def extract_lambada(samples):
    lls, accs, dids = [], [], []
    for s in samples:
        fr = s["filtered_resps"]
        ll = fr[0][0] if isinstance(fr[0], (list, tuple)) else fr[0]
        lls.append(float(ll))
        accs.append(int(s["acc"]))
        dids.append(s["doc_id"])
    return np.array(lls), np.array(accs), np.array(dids)


def extract_multichoice(samples, metric="acc"):
    probs, accs, dids = [], [], []
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
        probs.append(p[correct_idx])
        accs.append(int(s[metric]))
        dids.append(s["doc_id"])
    return np.array(probs), np.array(accs), np.array(dids)


def jaccard(set_a, set_b):
    if len(set_a) == 0 and len(set_b) == 0:
        return 0.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / union if union > 0 else 0.0


def bootstrap_jaccard(sets_dict, n_boot=N_BOOTSTRAP):
    all_ids = sorted(set().union(*sets_dict.values()))
    if len(all_ids) == 0:
        return 0.0, 0.0, 0.0

    membership = {}
    for arch in ARCHS:
        membership[arch] = set(sets_dict[arch])

    pairwise_j = []
    for a1, a2 in ARCH_PAIRS:
        pairwise_j.append(jaccard(membership[a1], membership[a2]))
    mean_j = float(np.mean(pairwise_j))

    all_ids_arr = np.array(all_ids)
    n = len(all_ids_arr)
    boot_means = []
    for _ in range(n_boot):
        idx = RNG.randint(0, n, size=n)
        boot_ids = set(all_ids_arr[idx])
        pw = []
        for a1, a2 in ARCH_PAIRS:
            s1 = membership[a1] & boot_ids
            s2 = membership[a2] & boot_ids
            pw.append(jaccard(s1, s2))
        boot_means.append(np.mean(pw))

    ci_lo = float(np.percentile(boot_means, 2.5))
    ci_hi = float(np.percentile(boot_means, 97.5))
    return mean_j, ci_lo, ci_hi


def load_benchmark_data(bench_name, bench_cfg):
    data = {}
    for arch in ARCHS:
        if bench_name == "lambada":
            pure_path = LAMBADA_PATHS[arch]["pure"]
            hyb_path = LAMBADA_PATHS[arch]["h3-1"]
            pure_samples = load_jsonl(pure_path)
            hyb_samples = load_jsonl(hyb_path)

            ll_pure, acc_pure, did_pure = extract_lambada(pure_samples)
            ll_hyb, acc_hyb, did_hyb = extract_lambada(hyb_samples)

            assert np.array_equal(did_pure, did_hyb), f"doc_id mismatch: {arch} lambada"

            p_pure = np.exp(ll_pure)
            p_hyb = np.exp(ll_hyb)

            data[arch] = (p_pure, acc_pure, p_hyb, acc_hyb, did_pure)
        else:
            bench_dir = bench_name
            pure_dir = MULTICHOICE_DIR_MAP[arch]["pure"]
            hyb_dir = MULTICHOICE_DIR_MAP[arch]["h3-1"]

            pure_path = f"{BASE_CLEAN}/{bench_dir}/{pure_dir}/samples/{bench_cfg['sample_file']}"
            hyb_path = f"{BASE_CLEAN}/{bench_dir}/{hyb_dir}/samples/{bench_cfg['sample_file']}"

            pure_samples = load_jsonl(pure_path)
            hyb_samples = load_jsonl(hyb_path)

            metric = bench_cfg["metric"]
            p_pure, acc_pure, did_pure = extract_multichoice(pure_samples, metric)
            p_hyb, acc_hyb, did_hyb = extract_multichoice(hyb_samples, metric)

            assert np.array_equal(did_pure, did_hyb), f"doc_id mismatch: {arch} {bench_name}"

            data[arch] = (p_pure, acc_pure, p_hyb, acc_hyb, did_pure)

    return data


def compute_continuous_jaccard(data, tau):
    helped_sets = {}
    hurt_sets = {}
    n_helped = {}
    n_hurt = {}

    for arch in ARCHS:
        p_pure, acc_pure, p_hyb, acc_hyb, doc_ids = data[arch]
        dp = p_hyb - p_pure

        helped_mask = (dp > tau) & (acc_hyb == 1)
        hurt_mask = (dp < -tau) & (acc_pure == 1)

        helped_sets[arch] = set(doc_ids[helped_mask])
        hurt_sets[arch] = set(doc_ids[hurt_mask])
        n_helped[arch] = int(helped_mask.sum())
        n_hurt[arch] = int(hurt_mask.sum())

    j_helped_mean, j_helped_lo, j_helped_hi = bootstrap_jaccard(helped_sets)
    j_hurt_mean, j_hurt_lo, j_hurt_hi = bootstrap_jaccard(hurt_sets)

    return {
        "J_helped_mean": round(j_helped_mean, 6),
        "J_helped_ci": [round(j_helped_lo, 6), round(j_helped_hi, 6)],
        "J_hurt_mean": round(j_hurt_mean, 6),
        "J_hurt_ci": [round(j_hurt_lo, 6), round(j_hurt_hi, 6)],
        "n_helped": [n_helped[a] for a in ARCHS],
        "n_hurt": [n_hurt[a] for a in ARCHS],
    }


def main():
    results = {}

    for bench_name, bench_cfg in BENCHMARKS.items():
        print(f"\n{'='*60}")
        print(f"Benchmark: {bench_name}")
        print(f"{'='*60}")

        try:
            data = load_benchmark_data(bench_name, bench_cfg)
        except FileNotFoundError as e:
            print(f"  SKIPPED: {e}")
            continue

        bench_results = {}
        for tau in TAUS:
            tau_key = f"tau_{tau:.2f}"
            res = compute_continuous_jaccard(data, tau)
            bench_results[tau_key] = res
            print(f"  tau={tau:.2f}: J_helped={res['J_helped_mean']:.4f} [{res['J_helped_ci'][0]:.4f}, {res['J_helped_ci'][1]:.4f}]  "
                  f"J_hurt={res['J_hurt_mean']:.4f} [{res['J_hurt_ci'][0]:.4f}, {res['J_hurt_ci'][1]:.4f}]  "
                  f"n_helped={res['n_helped']}  n_hurt={res['n_hurt']}")

        results[bench_name] = bench_results

    if "lambada" in results and "tau_0.00" in results["lambada"]:
        t0 = results["lambada"]["tau_0.00"]
        print(f"\n--- Validation ---")
        print(f"LAMBADA tau=0.0: J_helped={t0['J_helped_mean']:.4f}, J_hurt={t0['J_hurt_mean']:.4f}")
        print(f"Known binary:  J_helped~0.10, J_hurt~0.09 at h3-1")

    out_path = "/root/entrainment_gated_ft/results/e2_continuous_jaccard.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
