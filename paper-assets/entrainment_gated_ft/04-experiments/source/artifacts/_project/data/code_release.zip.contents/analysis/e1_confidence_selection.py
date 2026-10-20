#!/usr/bin/env python3
"""E1: Confidence-based Architecture Selection"""
import json
import numpy as np
from pathlib import Path

BASE = Path("/root/entrainment_gated_ft")
LM = BASE / "lm_eval_clean"
ARCHS = ["GDN", "RetNet", "HGRN2"]
FULL_NAMES = {"GDN": "GatedDeltaNet", "RetNet": "RetNet", "HGRN2": "HGRN2"}

BENCHMARKS = {
    "lambada": {
        "metric": "acc",
        "pure": {
            "GDN":    LM / "exp007/1.3b/GDN-pure/samples/lambada_openai.jsonl",
            "RetNet": LM / "exp007/1.3b/RetNet-pure/samples/lambada_openai.jsonl",
            "HGRN2":  LM / "exp007/1.3b/HGRN2-pure/samples/lambada_openai.jsonl",
        },
        "hybrid": {
            "GDN":    LM / "1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl",
            "RetNet": LM / "exp007/1.3b/RetNet-h3-1/samples/lambada_openai.jsonl",
            "HGRN2":  LM / "exp007/1.3b/HGRN2-h3-1/samples/lambada_openai.jsonl",
        },
    },
    "hellaswag": {
        "metric": "acc_norm",
        "pure":   {a: LM / f"hellaswag/1.3B-100B-{FULL_NAMES[a]}-pure/samples/hellaswag.jsonl" for a in ARCHS},
        "hybrid": {a: LM / f"hellaswag/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/hellaswag.jsonl" for a in ARCHS},
    },
    "piqa": {
        "metric": "acc",
        "pure":   {a: LM / f"piqa/1.3B-100B-{FULL_NAMES[a]}-pure/samples/piqa.jsonl" for a in ARCHS},
        "hybrid": {a: LM / f"piqa/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/piqa.jsonl" for a in ARCHS},
    },
    "arc_easy": {
        "metric": "acc",
        "pure":   {a: LM / f"arc_easy/1.3B-100B-{FULL_NAMES[a]}-pure/samples/arc_easy.jsonl" for a in ARCHS},
        "hybrid": {a: LM / f"arc_easy/1.3B-100B-{FULL_NAMES[a]}-hybrid-3-1/samples/arc_easy.jsonl" for a in ARCHS},
    },
}


def load_jsonl(path):
    with open(path) as f:
        data = [json.loads(line) for line in f]
    data.sort(key=lambda x: x["doc_id"])
    return data


def get_confidence(sample, metric, benchmark):
    if benchmark == "lambada":
        return sample["resps"][0][0][0]
    resps = [r[0][0] for r in sample["resps"]]
    if metric == "acc_norm":
        endings = sample["doc"]["endings"]
        return max(r / max(len(e), 1) for r, e in zip(resps, endings))
    return max(resps)


def load_data(benchmark):
    cfg = BENCHMARKS[benchmark]
    metric = cfg["metric"]
    data = {"pure_conf": {}, "pure_acc": {}, "hybrid_acc": {}}

    for arch in ARCHS:
        pp, hp = str(cfg["pure"][arch]), str(cfg["hybrid"][arch])
        if not Path(pp).exists() or not Path(hp).exists():
            print(f"  MISSING: {pp} or {hp}")
            return None

        ps = load_jsonl(pp)
        hs = load_jsonl(hp)
        assert [s["doc_id"] for s in ps] == [s["doc_id"] for s in hs], \
            f"doc_id mismatch {benchmark}/{arch}"

        data["pure_conf"][arch] = np.array([get_confidence(s, metric, benchmark) for s in ps])
        data["pure_acc"][arch]  = np.array([int(s[metric]) for s in ps])
        data["hybrid_acc"][arch] = np.array([int(s[metric]) for s in hs])

    ref = [s["doc_id"] for s in load_jsonl(str(cfg["pure"]["GDN"]))]
    for arch in ["RetNet", "HGRN2"]:
        other = [s["doc_id"] for s in load_jsonl(str(cfg["pure"][arch]))]
        assert ref == other, f"Cross-arch mismatch {benchmark}: GDN vs {arch}"

    data["n"] = len(ref)
    return data


# ── Strategies ──

def strat_max_confidence(data, train, test):
    conf  = np.column_stack([data["pure_conf"][a] for a in ARCHS])
    hyb   = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    best  = np.argmax(conf[test], axis=1)
    return float(np.mean(hyb[test][np.arange(len(test)), best]))


def strat_rescue_threshold(data, train, test):
    conf  = np.column_stack([data["pure_conf"][a] for a in ARCHS])
    pure  = np.column_stack([data["pure_acc"][a]  for a in ARCHS])
    hyb   = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    absconf = np.abs(conf)

    tr_abs = absconf[train]
    thresholds = np.linspace(np.percentile(tr_abs, 2), np.percentile(tr_abs, 98), 100)

    best_t, best_a = thresholds[0], -1
    for t in thresholds:
        dec = np.where(tr_abs > t, hyb[train], pure[train])
        a = np.mean(np.sum(dec, axis=1) >= 2)
        if a > best_a:
            best_a, best_t = a, t

    te_abs = absconf[test]
    dec = np.where(te_abs > best_t, hyb[test], pure[test])
    return float(np.mean(np.sum(dec, axis=1) >= 2)), float(best_t)


def strat_confidence_weighted(data, train, test):
    conf = np.column_stack([data["pure_conf"][a] for a in ARCHS])
    hyb  = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    tc   = conf[test]
    th   = hyb[test]
    shifted = tc - np.max(tc, axis=1, keepdims=True)
    w = np.exp(shifted)
    w /= np.sum(w, axis=1, keepdims=True)
    return float(np.mean(np.sum(w * th, axis=1) >= 0.5))


# ── Baselines ──

def bl_mv(data, test):
    hyb = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    return float(np.mean(np.sum(hyb[test], axis=1) >= 2))

def bl_best_single(data, train, test):
    best = max(ARCHS, key=lambda a: np.mean(data["hybrid_acc"][a][train]))
    return float(np.mean(data["hybrid_acc"][best][test])), best

def bl_oracle(data, test):
    hyb = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    return float(np.mean(np.max(hyb[test], axis=1)))

def bl_random(data, test, rng):
    hyb = np.column_stack([data["hybrid_acc"][a] for a in ARCHS])
    n = len(test)
    c = rng.integers(0, 3, size=n)
    return float(np.mean(hyb[test][np.arange(n), c]))


# ── Cross-validation ──

def run_cv(data, n_splits=10, seed=42):
    n = data["n"]
    rng = np.random.default_rng(seed)
    idx = np.arange(n)

    res = {k: [] for k in [
        "max_confidence", "rescue_threshold", "confidence_weighted",
        "majority_vote", "best_single", "oracle", "random"
    ]}
    threshs = []

    for _ in range(n_splits):
        perm = rng.permutation(idx)
        h = n // 2
        tr, te = perm[:h], perm[h:]

        res["max_confidence"].append(strat_max_confidence(data, tr, te))

        ra, rt = strat_rescue_threshold(data, tr, te)
        res["rescue_threshold"].append(ra)
        threshs.append(rt)

        res["confidence_weighted"].append(strat_confidence_weighted(data, tr, te))
        res["majority_vote"].append(bl_mv(data, te))

        ba, _ = bl_best_single(data, tr, te)
        res["best_single"].append(ba)
        res["oracle"].append(bl_oracle(data, te))
        res["random"].append(bl_random(data, te, rng))

    return res, threshs


def main():
    out = {
        "analysis": "e1_confidence_selection",
        "date": "2026-05-22",
        "method": {
            "attention_ratio": "h3-1 (25%)",
            "architectures": ARCHS,
            "cv": "50/50 random split x 10 repeats",
            "confidence_measure": {
                "lambada": "target word loglikelihood",
                "hellaswag": "max char-length-normalized loglikelihood",
                "piqa": "max raw loglikelihood across choices",
                "arc_easy": "max raw loglikelihood across choices",
            },
        },
        "results": {},
    }

    for bm in BENCHMARKS:
        print(f"\n{'='*60}")
        print(f"Benchmark: {bm}")
        print(f"{'='*60}")

        data = load_data(bm)
        if data is None:
            print("  SKIPPED")
            continue

        print(f"  N = {data['n']}")
        for a in ARCHS:
            p = np.mean(data["pure_acc"][a])
            h = np.mean(data["hybrid_acc"][a])
            print(f"  {a:8s}: pure={p:.4f}  h3-1={h:.4f}  delta={h-p:+.4f}")

        cv, threshs = run_cv(data)

        mv_m = np.mean(cv["majority_vote"])
        bs_m = np.mean(cv["best_single"])

        strats = {}
        for s in ["max_confidence", "rescue_threshold", "confidence_weighted"]:
            m, sd = np.mean(cv[s]), np.std(cv[s])
            strats[s] = {
                "mean_acc": round(m, 6),
                "std_acc": round(sd, 6),
                "vs_mv_pp": round((m - mv_m) * 100, 3),
                "vs_best_single_pp": round((m - bs_m) * 100, 3),
            }
            print(f"  {s:25s}: {m:.4f} +/- {sd:.4f}  (vs MV: {(m-mv_m)*100:+.2f}pp)")

        if threshs:
            strats["rescue_threshold"]["mean_threshold"] = round(float(np.mean(threshs)), 4)
            strats["rescue_threshold"]["std_threshold"] = round(float(np.std(threshs)), 4)
            print(f"  rescue threshold: {np.mean(threshs):.3f} +/- {np.std(threshs):.3f}")

        baselines = {}
        for b in ["majority_vote", "best_single", "oracle", "random"]:
            m, sd = np.mean(cv[b]), np.std(cv[b])
            baselines[f"{b}_acc"] = round(m, 6)
            baselines[f"{b}_std"] = round(sd, 6)
            print(f"  {b:15s}: {m:.4f} +/- {sd:.4f}")

        per_arch = {}
        for a in ARCHS:
            per_arch[a] = {
                "pure_acc":   round(float(np.mean(data["pure_acc"][a])), 6),
                "hybrid_acc": round(float(np.mean(data["hybrid_acc"][a])), 6),
            }

        out["results"][bm] = {
            "strategies": strats,
            "baselines": baselines,
            "per_arch": per_arch,
            "n_samples": data["n"],
        }

    # Summary
    print(f"\n{'='*95}")
    print("SUMMARY")
    print(f"{'='*95}")
    hdr = f"{'Benchmark':<12} {'MV':<8} {'BestSgl':<8} {'MaxConf':<15} {'Rescue':<15} {'CW-Vote':<15} {'Oracle':<8}"
    print(hdr)
    print("-" * 95)
    for bm, r in out["results"].items():
        s, b = r["strategies"], r["baselines"]
        print(f"{bm:<12} {b['majority_vote_acc']:.4f}  {b['best_single_acc']:.4f}  "
              f"{s['max_confidence']['mean_acc']:.4f}({s['max_confidence']['vs_mv_pp']:+.1f})  "
              f"{s['rescue_threshold']['mean_acc']:.4f}({s['rescue_threshold']['vs_mv_pp']:+.1f})  "
              f"{s['confidence_weighted']['mean_acc']:.4f}({s['confidence_weighted']['vs_mv_pp']:+.1f})  "
              f"{b['oracle_acc']:.4f}")

    out_path = BASE / "results/e1_confidence_selection.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {out_path}")

    return out


if __name__ == "__main__":
    main()
