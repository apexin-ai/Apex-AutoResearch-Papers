"""Gate comparison: Direction-Aware vs Strict Bidirectional NLI gate for BT.

Re-computes bidirectional NLI (forward + backward) for formality & verbosity
counterfactual pairs, then compares BT P(style) under:
  - Strict gate:     min(NLI_fwd, NLI_bwd) >= 0.90
  - Direction-aware: appropriate single direction >= 0.90
    (verbosity: fwd for compression, bwd for expansion;
     formality: max(fwd, bwd) — either direction sufficient)
"""

import json
import logging
import sys

import choix
import numpy as np
import torch
from transformers import pipeline as hf_pipeline

logger = logging.getLogger(__name__)

NLI_MODEL = "/root/autodl-tmp/models/nli-deberta-v3-large/"
THRESHOLD = 0.90
N_BOOT = 10_000
SEED = 42
BATCH_SIZE = 16
DATA_DIR = "/root/causal_style_decomp_judge/data"
HIGH, LOW = 0, 1

AXES = {
    "formality": {
        "verified": f"{DATA_DIR}/verified_32b.jsonl",
        "pairwise": f"{DATA_DIR}/pairwise_results_qwen32b_formality.jsonl",
        "style_field": "original_formality",
        "high_style": "formal",
        "pref_t1": "trial1_prefers_formal",
        "pref_t2": "trial2_prefers_formal",
    },
    "verbosity": {
        "verified": f"{DATA_DIR}/verified_verbosity.jsonl",
        "pairwise": f"{DATA_DIR}/pairwise_results_qwen32b_verbosity.jsonl",
        "style_field": "original_verbosity",
        "high_style": "verbose",
        "pref_t1": "trial1_prefers_verbose",
        "pref_t2": "trial2_prefers_verbose",
    },
}


# ── Data ──────────────────────────────────────────────────────────────

def load_data(cfg):
    """Join verified texts with pairwise judge preferences by id."""
    with open(cfg["verified"]) as f:
        verified = {}
        for line in f:
            if line.strip():
                r = json.loads(line)
                verified[r["id"]] = r
    with open(cfg["pairwise"]) as f:
        pairwise = [json.loads(l) for l in f if l.strip()]
    merged = []
    for p in pairwise:
        v = verified.get(p["id"])
        if v is None:
            logger.warning("Pair %s not in verified data, skipping", p["id"])
            continue
        rec = {**v}
        rec.update(p)
        merged.append(rec)
    logger.info("Loaded %d merged records", len(merged))
    return merged


# ── NLI ───────────────────────────────────────────────────────────────

def compute_nli(nli_pipe, originals, counterfactuals, batch_size):
    """Return (forward, backward) NLI entailment scores for all pairs."""
    def _scores(a_list, b_list):
        inputs = [{"text": a, "text_pair": b} for a, b in zip(a_list, b_list)]
        out = []
        for i in range(0, len(inputs), batch_size):
            batch = inputs[i:i + batch_size]
            res = nli_pipe(
                batch, top_k=None,
                tokenizer_kwargs={"truncation": True, "padding": True, "max_length": 512},
            )
            for r in res:
                scores = {x["label"].lower(): x["score"] for x in r}
                out.append(scores.get("entailment", 0.0))
        return out

    logger.info("Forward NLI (original → counterfactual)...")
    fwd = _scores(originals, counterfactuals)
    logger.info("Backward NLI (counterfactual → original)...")
    bwd = _scores(counterfactuals, originals)
    return fwd, bwd


# ── Gates ─────────────────────────────────────────────────────────────

def apply_gates(records, fwd, bwd, cfg):
    """Annotate each record with strict and direction-aware gate outcomes."""
    for i, rec in enumerate(records):
        rec["nli_fwd"] = fwd[i]
        rec["nli_bwd"] = bwd[i]

        rec["nli_strict"] = min(fwd[i], bwd[i])
        rec["pass_strict"] = rec["nli_strict"] >= THRESHOLD

        if cfg["style_field"] == "original_verbosity":
            if rec.get("original_verbosity") == "verbose":
                rec["nli_da"] = fwd[i]
            else:
                rec["nli_da"] = bwd[i]
        else:
            rec["nli_da"] = max(fwd[i], bwd[i])

        rec["pass_da"] = rec["nli_da"] >= THRESHOLD
        rec["pass_extra"] = rec["pass_da"] and not rec["pass_strict"]


# ── BT ────────────────────────────────────────────────────────────────

def pair_comps(rec, cfg):
    """Extract BT comparisons for one pair from judge preferences."""
    c = []
    if rec.get("trial1_choice") in ("A", "B"):
        c.append((HIGH, LOW) if rec.get(cfg["pref_t1"]) else (LOW, HIGH))
    if rec.get("trial2_choice") in ("A", "B"):
        c.append((HIGH, LOW) if rec.get(cfg["pref_t2"]) else (LOW, HIGH))
    return c


def fit_bt(comps):
    params = choix.ilsr_pairwise(2, comps, alpha=0.01)
    return params[HIGH] - params[LOW]


def bt_p(s):
    return 1.0 / (1.0 + np.exp(-s))


def bt_analysis(recs, cfg, label):
    """BT fit + pair-level bootstrap CI for a filtered subset."""
    comps, groups = [], {}
    for r in recs:
        c = pair_comps(r, cfg)
        if c:
            comps.extend(c)
            groups[r["id"]] = c
    if len(comps) < 2:
        return None

    prob = bt_p(fit_bt(comps))
    rng = np.random.RandomState(SEED)
    ids = list(groups.keys())
    n = len(ids)
    boot = []
    for _ in range(N_BOOT):
        idx = rng.choice(n, size=n, replace=True)
        b = []
        for j in idx:
            b.extend(groups[ids[j]])
        try:
            boot.append(bt_p(fit_bt(b)))
        except Exception:
            pass
    boot = np.array(boot)
    ci = np.percentile(boot, [2.5, 97.5])
    n_below = int(np.sum(boot < 0.5))
    pval = n_below / len(boot) if len(boot) else 1.0

    return {
        "label": label,
        "n_pairs": len(groups),
        "n_comps": len(comps),
        "bt": round(prob, 4),
        "ci": [round(ci[0], 4), round(ci[1], 4)],
        "pval": pval,
    }


def paired_bootstrap_delta(records, cfg):
    """Paired bootstrap: ΔP(style) = P_DA − P_strict per resample."""
    rng = np.random.RandomState(SEED)
    n = len(records)
    pc = [pair_comps(r, cfg) for r in records]
    sm = [r["pass_strict"] for r in records]
    dm = [r["pass_da"] for r in records]

    deltas = []
    for _ in range(N_BOOT):
        idx = rng.choice(n, size=n, replace=True)
        cs, cd = [], []
        for j in idx:
            if sm[j]:
                cs.extend(pc[j])
            if dm[j]:
                cd.extend(pc[j])
        try:
            if len(cs) >= 2 and len(cd) >= 2:
                deltas.append(bt_p(fit_bt(cd)) - bt_p(fit_bt(cs)))
        except Exception:
            pass
    return np.array(deltas)


# ── Per-axis analysis ─────────────────────────────────────────────────

def run_axis(name, records, cfg, nli_pipe):
    origs = [r["original_text"] for r in records]
    cfs = [r["counterfactual_text"] for r in records]

    logger.info("[%s] Computing bidirectional NLI (%d pairs)...", name, len(records))
    fwd, bwd = compute_nli(nli_pipe, origs, cfs, BATCH_SIZE)
    apply_gates(records, fwd, bwd, cfg)

    nt = len(records)
    ns = sum(r["pass_strict"] for r in records)
    nd = sum(r["pass_da"] for r in records)
    ne = sum(r["pass_extra"] for r in records)
    high = cfg["high_style"]

    print(f"\n{'='*70}")
    print(f"  {name.upper()} — Gate Comparison")
    print(f"{'='*70}")
    print(f"  Total pairs:          {nt}")
    print(f"  Strict bidir gate:    {ns}/{nt} ({100*ns/nt:.0f}%)")
    print(f"  Direction-aware gate: {nd}/{nt} ({100*nd/nt:.0f}%)")
    print(f"  Extra (DA only):      {ne} ({100*ne/nt:.0f}%)")

    r_strict = bt_analysis(
        [r for r in records if r["pass_strict"]], cfg, "Strict",
    )
    r_da = bt_analysis(
        [r for r in records if r["pass_da"]], cfg, "Direction-Aware",
    )
    r_extra = bt_analysis(
        [r for r in records if r["pass_extra"]], cfg, "Extra Only",
    )

    for tag, res in [
        ("Strict Bidirectional", r_strict),
        ("Direction-Aware", r_da),
        ("Extra Pairs Only", r_extra),
    ]:
        print(f"\n  ─── {tag} ───")
        if res is None:
            print(f"  Insufficient data")
            continue
        print(f"  n={res['n_pairs']} pairs, {res['n_comps']} comparisons")
        print(f"  BT P({high}): {res['bt']:.4f}  CI [{res['ci'][0]:.4f}, {res['ci'][1]:.4f}]")
        if tag != "Extra Pairs Only":
            pv = res["pval"]
            s = f"p < {1/N_BOOT}" if pv == 0 else f"p = {pv:.4f}"
            print(f"  {s}")

    if r_strict and r_da:
        print(f"\n  ─── Difference Test (paired bootstrap, {N_BOOT} iter) ───")
        deltas = paired_bootstrap_delta(records, cfg)
        obs = r_da["bt"] - r_strict["bt"]
        ci_d = np.percentile(deltas, [2.5, 97.5])
        z = ci_d[0] <= 0 <= ci_d[1]
        print(f"  Observed ΔP({high}): {obs:+.4f} (DA − strict)")
        print(f"  Bootstrap 95% CI:  [{ci_d[0]:+.4f}, {ci_d[1]:+.4f}]")
        print(
            f"  Contains 0: "
            f"{'Yes → no significant difference' if z else 'No → significant difference'}"
        )
        return {"strict": r_strict, "da": r_da, "extra": r_extra,
                "delta_obs": obs, "delta_ci": ci_d.tolist(), "no_diff": z}

    return {"strict": r_strict, "da": r_da, "extra": r_extra}


# ── Main ──────────────────────────────────────────────────────────────

def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
    )

    logger.info("Loading NLI model from %s", NLI_MODEL)
    nli_pipe = hf_pipeline("text-classification", model=NLI_MODEL, device=0)

    results = {}
    for name, cfg in AXES.items():
        records = load_data(cfg)
        results[name] = run_axis(name, records, cfg, nli_pipe)

    print(f"\n{'='*70}")
    print(f"  SUMMARY")
    print(f"{'='*70}")
    for name in AXES:
        r = results[name]
        high = AXES[name]["high_style"]
        if r.get("strict") and r.get("da"):
            s, d = r["strict"], r["da"]
            delta = r.get("delta_obs", 0)
            ci = r.get("delta_ci", [0, 0])
            nd = r.get("no_diff", True)
            print(
                f"  {name}: strict P({high})={s['bt']:.4f} (n={s['n_pairs']}), "
                f"DA P({high})={d['bt']:.4f} (n={d['n_pairs']}), "
                f"Δ={delta:+.4f} CI [{ci[0]:+.4f}, {ci[1]:+.4f}] "
                f"→ {'no diff' if nd else 'DIFF'}"
            )
    print()


if __name__ == "__main__":
    main()
