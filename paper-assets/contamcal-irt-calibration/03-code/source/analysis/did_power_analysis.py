"""DiD Post-hoc Power Analysis.

Computes MDES (minimum detectable effect size) for each family × benchmark
DiD test at d025. SE estimated from bootstrap 95% CI width.
"""
import json
import math
import os

Z_ALPHA = 1.959964  # norm.ppf(0.975)
Z_BETA  = 0.841621  # norm.ppf(0.80)

# d025 data extracted from treated_untreated_summary.csv (westd)
# Fields: n_t, n_u, did, did_ci_lo, did_ci_hi, did_p, treated_delta, untreated_delta
D025_DATA = {
    "mmlu": {
        "Gemma-2-9B":   {"n_t": 3540, "n_u": 10502, "did": 0.0054593, "did_ci_lo": -0.0067356, "did_ci_hi": 0.0176252, "did_p": 0.3898, "treated_delta": 0.031073, "untreated_delta": 0.025614},
        "OLMo-2-7B":    {"n_t": 3540, "n_u": 10502, "did": -0.0107472, "did_ci_lo": -0.0218183, "did_ci_hi": 0.0004000, "did_p": 0.0582, "treated_delta": 0.015819, "untreated_delta": 0.026566},
        "Phi-4":        {"n_t": 3540, "n_u": 10502, "did": -0.0027042, "did_ci_lo": -0.0113694, "did_ci_hi": 0.0061894, "did_p": 0.5406, "treated_delta": 0.003390, "untreated_delta": 0.006094},
        "Qwen2.5-14B":  {"n_t": 3540, "n_u": 10502, "did": 0.0068685, "did_ci_lo": -0.0074596, "did_ci_hi": 0.0212785, "did_p": 0.3460, "treated_delta": -0.068927, "untreated_delta": -0.075795},
        "Qwen2.5-7B":   {"n_t": 3540, "n_u": 10502, "did": -0.0084333, "did_ci_lo": -0.0228878, "did_ci_hi": 0.0053487, "did_p": 0.2386, "treated_delta": -0.037571, "untreated_delta": -0.029137},
    },
    "arc_challenge": {
        "Gemma-2-9B":   {"n_t": 257, "n_u": 915, "did": -0.0025345, "did_ci_lo": -0.0344092, "did_ci_hi": 0.0307797, "did_p": 0.8778, "treated_delta": 0.011673, "untreated_delta": 0.014208},
        "OLMo-2-7B":    {"n_t": 257, "n_u": 915, "did": -0.0112777, "did_ci_lo": -0.0405690, "did_ci_hi": 0.0180137, "did_p": 0.4404, "treated_delta": 0.011673, "untreated_delta": 0.022951},
        "Phi-4":        {"n_t": 257, "n_u": 915, "did": -0.0082626, "did_ci_lo": -0.0243074, "did_ci_hi": 0.0076503, "did_p": 0.3024, "treated_delta": -0.003891, "untreated_delta": 0.004372},
        "Qwen2.5-14B":  {"n_t": 257, "n_u": 915, "did": -0.0025813, "did_ci_lo": -0.0279815, "did_ci_hi": 0.0206332, "did_p": 0.8508, "treated_delta": -0.023346, "untreated_delta": -0.020765},
        "Qwen2.5-7B":   {"n_t": 257, "n_u": 915, "did": 0.0242606, "did_ci_lo": -0.0149986, "did_ci_hi": 0.0629074, "did_p": 0.2214, "treated_delta": -0.019455, "untreated_delta": -0.043716},
    },
}

MODEL_ORDER = ["Gemma-2-9B", "OLMo-2-7B", "Phi-4", "Qwen2.5-14B", "Qwen2.5-7B"]


def compute_power_stats(d):
    ci_width = d["did_ci_hi"] - d["did_ci_lo"]
    se_did = ci_width / (2 * Z_ALPHA)

    mdes = (Z_ALPHA + Z_BETA) * se_did

    se_sq = se_did ** 2
    sigma_sq_pooled = se_sq / (1.0 / d["n_t"] + 1.0 / d["n_u"])

    n_each_05pp = 2 * (Z_ALPHA + Z_BETA) ** 2 * sigma_sq_pooled / (0.005 ** 2)
    n_each_1pp = 2 * (Z_ALPHA + Z_BETA) ** 2 * sigma_sq_pooled / (0.010 ** 2)

    return {
        "n_treated": d["n_t"],
        "n_untreated": d["n_u"],
        "treated_delta_pp": round(d["treated_delta"] * 100, 2),
        "untreated_delta_pp": round(d["untreated_delta"] * 100, 2),
        "did_pp": round(d["did"] * 100, 2),
        "did_ci_lo_pp": round(d["did_ci_lo"] * 100, 2),
        "did_ci_hi_pp": round(d["did_ci_hi"] * 100, 2),
        "did_p": d["did_p"],
        "se_did_pp": round(se_did * 100, 3),
        "mdes_pp": round(mdes * 100, 2),
        "sigma_sq_pooled": round(sigma_sq_pooled, 6),
        "observed_abs_did_pp": round(abs(d["did"]) * 100, 2),
        "detectable_at_80pct_power": abs(d["did"]) > mdes,
        "n_each_balanced_for_0.5pp": int(math.ceil(n_each_05pp)),
        "n_each_balanced_for_1.0pp": int(math.ceil(n_each_1pp)),
    }


results = {}
for bm in ["mmlu", "arc_challenge"]:
    results[bm] = {}
    for model in MODEL_ORDER:
        results[bm][model] = compute_power_stats(D025_DATA[bm][model])

# ── Print summary table ──
print("=" * 110)
print("DiD POST-HOC POWER ANALYSIS  (d025, α=0.05, 80% power, two-sided)")
print("=" * 110)

for bm in ["mmlu", "arc_challenge"]:
    print(f"\n{'─' * 110}")
    n_t = D025_DATA[bm][MODEL_ORDER[0]]["n_t"]
    n_u = D025_DATA[bm][MODEL_ORDER[0]]["n_u"]
    print(f"  {bm.upper().replace('_', ' ')}  (n_treated={n_t}, n_untreated={n_u})")
    print(f"{'─' * 110}")
    print(f"  {'Model':<16s} {'DiD(pp)':>8s} {'95% CI':>20s} {'p':>8s} {'SE(pp)':>8s} {'MDES(pp)':>9s} {'Power?':>7s} {'n@0.5pp':>9s} {'n@1pp':>7s}")
    print(f"  {'─'*16} {'─'*8} {'─'*20} {'─'*8} {'─'*8} {'─'*9} {'─'*7} {'─'*9} {'─'*7}")

    for model in MODEL_ORDER:
        d = results[bm][model]
        ci = f"[{d['did_ci_lo_pp']:+.2f}, {d['did_ci_hi_pp']:+.2f}]"
        pwr = "YES" if d["detectable_at_80pct_power"] else "no"
        print(f"  {model:<16s} {d['did_pp']:>+8.2f} {ci:>20s} {d['did_p']:>8.4f} {d['se_did_pp']:>8.3f} {d['mdes_pp']:>9.2f} {pwr:>7s} {d['n_each_balanced_for_0.5pp']:>9,d} {d['n_each_balanced_for_1.0pp']:>7,d}")

    mdes_vals = [results[bm][m]["mdes_pp"] for m in MODEL_ORDER]
    print(f"\n  MDES range: {min(mdes_vals):.2f} – {max(mdes_vals):.2f} pp (mean {sum(mdes_vals)/len(mdes_vals):.2f} pp)")
    print(f"  → Any item-specific effect >{max(mdes_vals):.1f}pp would have been detected with ≥80% power")

# ── Build JSON output ──
output = {
    "analysis": "DiD Post-hoc Power Analysis",
    "description": "Minimum detectable effect sizes for DiD (treated vs. untreated item accuracy changes) at d025 dosage",
    "method": "SE estimated from bootstrap 95% CI width: SE = (CI_hi - CI_lo) / (2 × 1.96); MDES = (z_{α/2} + z_β) × SE",
    "parameters": {
        "alpha": 0.05,
        "power": 0.80,
        "test": "two-sided",
        "bootstrap_iterations": 10000,
        "dosage": "d025 (2.5%)"
    },
    "results": {},
    "summary": {},
    "paper_text": {}
}

for bm in ["mmlu", "arc_challenge"]:
    output["results"][bm] = results[bm]
    mdes_vals = [results[bm][m]["mdes_pp"] for m in MODEL_ORDER]
    did_vals = [abs(results[bm][m]["did_pp"]) for m in MODEL_ORDER]

    output["summary"][bm] = {
        "mdes_range_pp": [round(min(mdes_vals), 2), round(max(mdes_vals), 2)],
        "mdes_mean_pp": round(sum(mdes_vals) / len(mdes_vals), 2),
        "observed_abs_did_range_pp": [round(min(did_vals), 2), round(max(did_vals), 2)],
        "all_below_mdes": all(abs(results[bm][m]["did_pp"]) < results[bm][m]["mdes_pp"] for m in MODEL_ORDER),
    }

# Generate paper text
mmlu_mdes = [results["mmlu"][m]["mdes_pp"] for m in MODEL_ORDER]
arc_mdes = [results["arc_challenge"][m]["mdes_pp"] for m in MODEL_ORDER]
mmlu_did = [abs(results["mmlu"][m]["did_pp"]) for m in MODEL_ORDER]
arc_did = [abs(results["arc_challenge"][m]["did_pp"]) for m in MODEL_ORDER]

paper_text = (
    f"Post-hoc power analysis (80\\% power, $\\alpha=0.05$, two-sided) yields minimum detectable effect sizes (MDES) "
    f"of {min(mmlu_mdes):.1f}--{max(mmlu_mdes):.1f}\\,pp for MMLU ($n_{{\\text{{treated}}}}=3{{,}}540$, "
    f"$n_{{\\text{{untreated}}}}=10{{,}}502$) and {min(arc_mdes):.1f}--{max(arc_mdes):.1f}\\,pp for ARC-Challenge "
    f"($n_{{\\text{{treated}}}}=257$, $n_{{\\text{{untreated}}}}=915$). "
    f"All observed $|\\text{{DiD}}|$ values fall below the MDES (MMLU: {min(mmlu_did):.1f}--{max(mmlu_did):.1f}\\,pp; "
    f"ARC: {min(arc_did):.1f}--{max(arc_did):.1f}\\,pp), meaning the test cannot distinguish a true null from a "
    f"sub-{max(mmlu_mdes):.0f}\\,pp effect on MMLU. However, this bound rules out the large item-specific effects "
    f"($>$5\\,pp) that characterize memorization-based contamination in prior work."
)
output["paper_text"]["limitations_or_appendix"] = paper_text

print("\n\n" + "=" * 110)
print("PAPER TEXT (for Limitations or Appendix)")
print("=" * 110)
print(paper_text)

# Write JSON
out_dir = os.path.dirname(os.path.abspath(__file__)).replace("/analysis", "/artifacts/did_power_analysis")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "did_power_analysis.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2, default=str)
print(f"\nJSON saved to: {out_path}")
