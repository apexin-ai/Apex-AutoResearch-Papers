#!/usr/bin/env python3
"""
Registry Data Mining Analysis
Extracts, categorizes, and statistically analyzes all experiment data from
the ACR-VLA Conformal Refinement project registry.

Output: registry_data_mining.md in the same directory.
"""
import json
import re
import sys
import math
import warnings
from collections import defaultdict
from pathlib import Path
import numpy as np
from scipy import stats

warnings.filterwarnings("ignore")

REGISTRY_FILE = "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-bbd03d76/303e4c8b-71ee-4731-b54d-1b505d6124d2/tool-results/mcp-agent-ml-research-read_registry-1780104379527.txt"
OUTPUT_FILE = "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/registry_data_mining.md"

# ─── Load Registry ───────────────────────────────────────────────────────────
with open(REGISTRY_FILE) as f:
    raw = json.load(f)
inner = json.loads(raw["result"])
exps = inner["data"]["experiments"]

# ─── Parse helpers ───────────────────────────────────────────────────────────
def parse_cmd(cmd):
    params = {}
    if not cmd:
        return params
    for match in re.finditer(r'--(\w+)\s+([^\s]+)', cmd):
        params[match.group(1)] = match.group(2)
    return params

def normalize_sr(val):
    """Normalize SR to 0-1 scale. Values > 1 are assumed to be percentages."""
    if val is None or val == "N/A":
        return None
    try:
        v = float(val)
        if v > 1.0:
            v = v / 100.0
        return round(v, 4)
    except (ValueError, TypeError):
        return None

def normalize_tr(val):
    """Normalize trigger_rate to 0-1 scale."""
    if val is None or val == "N/A":
        return None
    try:
        v = float(val)
        if v > 1.0:
            v = v / 100.0
        return round(v, 4)
    except (ValueError, TypeError):
        return None

def detect_model(exp_id, params):
    """Detect VLA model: smolvla or pi05."""
    model_param = params.get("model", "").lower().strip('"')
    if "pi0" in model_param or "pi05" in exp_id.lower():
        return "pi05"
    if "smolvla" in model_param or "smolvla" in exp_id.lower():
        return "smolvla"
    # Default: check for pi05 indicators in the experiment name
    if any(x in exp_id.lower() for x in ["pi05", "pi0.5", "pi-05"]):
        return "pi05"
    return "smolvla"  # default assumption

def detect_suite(params, exp_id):
    """Detect benchmark suite."""
    bench = params.get("benchmark", "").lower().strip('"')
    # Normalize long_horizon -> long
    if bench in ("long_horizon", "long"):
        return "long"
    if bench in ("object", "goal", "spatial"):
        return bench
    # Fallback: infer from experiment ID
    eid = exp_id.lower()
    if "long" in eid:
        return "long"
    if "object" in eid or "obj" in eid:
        return "object"
    if "goal" in eid:
        return "goal"
    if "spatial" in eid:
        return "spatial"
    return None

def get_sr(metrics):
    """Extract success rate from metrics dict."""
    for key in ["SR", "success_rate", "overall_success_rate", "overall_sr"]:
        if key in metrics:
            return normalize_sr(metrics[key])
    return None

def get_tr(metrics):
    """Extract trigger rate from metrics dict."""
    if "trigger_rate" in metrics:
        return normalize_tr(metrics["trigger_rate"])
    return None

def classify_condition(params, exp_id):
    """
    Classify experiment into condition.
    Returns (condition_name, is_valid) tuple.
    """
    mode = params.get("mode", "").lower().strip('"')
    K_raw = params.get("K", "").strip('"')
    tau_raw = params.get("conformal_threshold", "").strip('"')

    try:
        K = int(K_raw) if K_raw else None
    except ValueError:
        K = None
    try:
        tau = float(tau_raw) if tau_raw else None
    except ValueError:
        tau = None

    # VLA-only
    if mode == "vla_only":
        return "vla-only", True

    # CRM always-on: mode=adaptive_conformal_crm with tau<=0.01, K=2
    if mode == "adaptive_conformal_crm" and tau is not None and tau <= 0.01 and K == 2:
        return "crm-always-on", True

    # CRM always-on: mode=crm_obs_only with K=2 (these are also CRM always-on)
    if mode == "crm_obs_only" and K == 2:
        return "crm-always-on", True

    # Adaptive: mode=adaptive_conformal_crm, tau=0.25, K=2
    if mode == "adaptive_conformal_crm" and tau is not None and abs(tau - 0.25) < 0.001 and K == 2:
        return "adaptive", True

    # Also handle K=None cases for adaptive with tau=0.25 if experiment name suggests K=2
    # (some experiments have K missing from command but K=2 is implied)

    return "other", False

def is_duplicate_or_stale(exp_id, exp_data, params):
    """
    Identify experiments to skip:
    - Old eval format (SR values like 0.12 for object => old task set)
    - Dry runs
    - k2mean experiments (vla_only with K=2 action averaging, separate analysis)
    - Experiments with 0 SR that look like failures
    - Experiments with N/A SR
    """
    eid = exp_id.lower()

    # Skip dry runs
    if "dryrun" in eid or "dry-run" in eid:
        return True

    # Skip k2mean variants (these use action averaging, not standard VLA-only)
    if "k2mean" in eid:
        return True

    # Skip wrapper variants that might use different eval pipelines
    # Actually keep wrapper variants, they seem to be the correct eval pipeline

    # Skip openvla experiments (different model entirely)
    if "openvla" in eid:
        return True

    # Skip lto-split experiments (subset benchmarks)
    if "lto-split" in eid:
        return True

    # Skip experiments without a valid suite
    suite = detect_suite(params, exp_id)
    if suite is None:
        return True

    return False

def pick_best_run(exp_list):
    """
    When multiple runs exist for the same (model, suite, condition, seed),
    pick the latest one (by updated_at or experiment naming convention).
    Prefer experiments with trigger_rate data.
    Prefer experiments with '-r2', '-r3', '-r4' suffixes (later reruns).
    """
    if len(exp_list) == 1:
        return exp_list[0]

    # Sort by: has trigger_rate (True first), then by rerun number (higher first), then by updated_at
    def sort_key(item):
        eid, e = item
        has_tr = get_tr(e.get("metrics", {})) is not None
        # Extract rerun number - only match -r\d at end of name or before next hyphen section
        rerun = 0
        for m in re.finditer(r'-r(\d+)(?:-|$)', eid):
            # Skip server name patterns like bjb1-r2, cqa1-r3
            prefix = eid[:m.start()]
            if prefix.endswith(('bjb1', 'bjb2', 'cqa1', 'westd', '4090')):
                continue
            rerun = max(rerun, int(m.group(1)))
        # Parse updated_at
        updated = e.get("updated_at", "")
        return (has_tr, rerun, updated)

    sorted_list = sorted(exp_list, key=sort_key, reverse=True)
    return sorted_list[0]


# ─── Main extraction ─────────────────────────────────────────────────────────
records = []
# Group by (model, suite, condition, seed) to handle duplicates
groups = defaultdict(list)

for exp_id, e in exps.items():
    # Only include success or negative conclusions with metrics
    if e.get("conclusion") not in ("success", "negative"):
        continue
    if not e.get("metrics"):
        continue

    spec = e.get("spec", {})
    cmd = spec.get("command", "")
    params = parse_cmd(cmd)

    # Classify condition
    condition, is_valid = classify_condition(params, exp_id)
    if not is_valid:
        continue

    # Skip duplicates and stale experiments
    if is_duplicate_or_stale(exp_id, e, params):
        continue

    # Extract key fields
    model = detect_model(exp_id, params)
    suite = detect_suite(params, exp_id)
    seed = params.get("seed", "").strip('"')
    sr = get_sr(e.get("metrics", {}))
    tr = get_tr(e.get("metrics", {}))

    if sr is None or sr == 0:
        # Skip experiments with 0 or missing SR (likely failed or stale)
        continue

    if suite is None:
        continue

    # Additional validation: skip SmolVLA experiments with suspiciously low SR
    # that suggest old eval pipeline (before task set was standardized)
    if model == "smolvla":
        if suite == "object" and sr < 0.5:
            continue  # Old task set had much lower SR
        if suite == "spatial" and sr < 0.5:
            continue  # Old task set
        if suite == "goal" and sr < 0.5:
            continue  # Old task set
        if suite == "long" and sr < 0.3:
            continue  # Even long shouldn't be this low with correct eval

    key = (model, suite, condition, seed)
    groups[key].append((exp_id, e, sr, tr, condition))

# Deduplicate
for key, exp_list in groups.items():
    model, suite, condition, seed = key
    # Prepare list for pick_best_run
    candidates = [(eid, e_data) for eid, e_data, sr, tr, cond in exp_list]
    best_eid, best_e = pick_best_run(candidates)

    # Re-extract SR and TR from best
    sr = get_sr(best_e.get("metrics", {}))
    tr = get_tr(best_e.get("metrics", {}))

    if sr is not None and sr > 0:
        records.append({
            "exp_id": best_eid,
            "model": model,
            "suite": suite,
            "condition": condition,
            "seed": seed,
            "SR": sr,
            "trigger_rate": tr,
            "conclusion": best_e.get("conclusion"),
        })

print(f"Total valid records after dedup: {len(records)}")

# Sort records
records.sort(key=lambda r: (r["model"], r["suite"], r["condition"], r["seed"]))

# ─── Step 3: Group and compute means ─────────────────────────────────────────
grouped = defaultdict(list)
for r in records:
    key = (r["model"], r["suite"], r["condition"])
    grouped[key].append(r)

summary = {}
for key, recs in grouped.items():
    srs = [r["SR"] for r in recs]
    trs = [r["trigger_rate"] for r in recs if r["trigger_rate"] is not None]
    summary[key] = {
        "n": len(recs),
        "mean_sr": np.mean(srs),
        "std_sr": np.std(srs, ddof=1) if len(srs) > 1 else 0,
        "min_sr": np.min(srs),
        "max_sr": np.max(srs),
        "srs": srs,
        "mean_tr": np.mean(trs) if trs else None,
        "std_tr": np.std(trs, ddof=1) if len(trs) > 1 else None,
        "trs": trs,
        "seeds": [r["seed"] for r in recs],
    }

# ─── Step 4: Effect analysis ─────────────────────────────────────────────────
def cohens_d(group1, group2):
    """Compute Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return None, None, None
    m1, m2 = np.mean(group1), np.mean(group2)
    s1, s2 = np.std(group1, ddof=1), np.std(group2, ddof=1)
    # Pooled std
    sp = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    if sp == 0:
        return float("inf") if m2 != m1 else 0, None, None
    d = (m2 - m1) / sp
    # 95% CI for difference in means
    se = sp * math.sqrt(1/n1 + 1/n2)
    t_crit = stats.t.ppf(0.975, n1 + n2 - 2)
    ci_low = (m2 - m1) - t_crit * se
    ci_high = (m2 - m1) + t_crit * se
    return d, ci_low, ci_high

def effect_analysis(model, suite, summary):
    """Compute pairwise effect sizes for a given model x suite."""
    results = {}
    vla_key = (model, suite, "vla-only")
    crm_key = (model, suite, "crm-always-on")
    adapt_key = (model, suite, "adaptive")

    comparisons = [
        ("CRM-always-on vs VLA-only", crm_key, vla_key),
        ("Adaptive vs VLA-only", adapt_key, vla_key),
        ("Adaptive vs CRM-always-on", adapt_key, crm_key),
    ]

    for label, key_a, key_b in comparisons:
        if key_a in summary and key_b in summary:
            srs_a = summary[key_a]["srs"]
            srs_b = summary[key_b]["srs"]
            delta = np.mean(srs_a) - np.mean(srs_b)
            d, ci_low, ci_high = cohens_d(srs_b, srs_a)
            # Welch's t-test
            if len(srs_a) >= 2 and len(srs_b) >= 2:
                t_stat, p_val = stats.ttest_ind(srs_a, srs_b, equal_var=False)
            else:
                t_stat, p_val = None, None
            results[label] = {
                "delta": delta,
                "d": d,
                "ci_low": ci_low,
                "ci_high": ci_high,
                "t_stat": t_stat,
                "p_val": p_val,
                "n_a": len(srs_a),
                "n_b": len(srs_b),
            }
    return results

# ─── Step 5: Trigger rate analysis ───────────────────────────────────────────
trigger_data = defaultdict(list)
for r in records:
    if r["trigger_rate"] is not None:
        trigger_data[(r["model"], r["suite"], r["condition"])].append(r)

# Correlation between trigger_rate and SR delta
def trigger_correlation_analysis(model, records, summary):
    """Per-suite correlation between trigger_rate and adaptive SR improvement."""
    results = {}
    # For adaptive experiments with trigger rates, correlate TR with SR
    for suite in ["object", "spatial", "goal", "long"]:
        adapt_key = (model, suite, "adaptive")
        vla_key = (model, suite, "vla-only")

        if adapt_key not in summary or vla_key not in summary:
            continue

        vla_mean = summary[vla_key]["mean_sr"]
        adapt_recs = [r for r in records
                      if r["model"] == model and r["suite"] == suite
                      and r["condition"] == "adaptive" and r["trigger_rate"] is not None]

        if len(adapt_recs) < 3:
            continue

        trs = [r["trigger_rate"] for r in adapt_recs]
        srs = [r["SR"] for r in adapt_recs]
        deltas = [r["SR"] - vla_mean for r in adapt_recs]

        # Pearson
        if len(trs) >= 3:
            r_pearson, p_pearson = stats.pearsonr(trs, srs)
            r_spearman, p_spearman = stats.spearmanr(trs, srs)
        else:
            r_pearson, p_pearson = None, None
            r_spearman, p_spearman = None, None

        results[suite] = {
            "n": len(adapt_recs),
            "mean_tr": np.mean(trs),
            "std_tr": np.std(trs, ddof=1) if len(trs) > 1 else 0,
            "r_pearson": r_pearson,
            "p_pearson": p_pearson,
            "r_spearman": r_spearman,
            "p_spearman": p_spearman,
            "trs": trs,
            "srs": srs,
        }
    return results

# ─── Step 6: Cross-seed variance analysis ────────────────────────────────────
def variance_analysis(model, suite, summary):
    """Compare variance across conditions using Levene's test."""
    results = {}
    conditions = ["vla-only", "crm-always-on", "adaptive"]
    srs_by_cond = {}
    for cond in conditions:
        key = (model, suite, cond)
        if key in summary and summary[key]["n"] >= 3:
            srs_by_cond[cond] = summary[key]["srs"]

    if len(srs_by_cond) < 2:
        return None

    # Pairwise Levene's tests
    cond_list = list(srs_by_cond.keys())
    for i in range(len(cond_list)):
        for j in range(i+1, len(cond_list)):
            c1, c2 = cond_list[i], cond_list[j]
            s1, s2 = srs_by_cond[c1], srs_by_cond[c2]
            if len(s1) >= 2 and len(s2) >= 2:
                lev_stat, lev_p = stats.levene(s1, s2)
                f_ratio = np.var(s1, ddof=1) / np.var(s2, ddof=1) if np.var(s2, ddof=1) > 0 else float("inf")
                results[f"{c1} vs {c2}"] = {
                    "var_1": np.var(s1, ddof=1),
                    "var_2": np.var(s2, ddof=1),
                    "f_ratio": f_ratio,
                    "levene_stat": lev_stat,
                    "levene_p": lev_p,
                    "n1": len(s1),
                    "n2": len(s2),
                }
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# Generate Report
# ═══════════════════════════════════════════════════════════════════════════════
lines = []
def w(s=""):
    lines.append(s)

w("# Registry Data Mining Report")
w(f"**Generated**: 2026-05-30 | **Total registry experiments**: {len(exps)} | **Valid records (after filtering & dedup)**: {len(records)}")
w()
w("## Filtering Criteria")
w()
w("- **Conclusion**: `success` or `negative` (both are valid data)")
w("- **Metrics**: Must have non-zero SR")
w("- **VLA-only**: `mode=vla_only`, no K/tau requirements")
w("- **CRM always-on**: `mode=adaptive_conformal_crm` with `tau≤0.01, K=2` OR `mode=crm_obs_only` with `K=2`")
w("- **Adaptive**: `mode=adaptive_conformal_crm` with `tau=0.25, K=2`")
w("- **Excluded**: ablations (K≠2 for CRM modes, tau≠0.25 for adaptive), k2mean, dry runs, old eval pipeline (SR<0.5 for SmolVLA Object/Spatial/Goal), OpenVLA, LTO-split")
w("- **Deduplication**: When multiple runs exist for same (model, suite, condition, seed), kept latest run with trigger_rate data preferred")
w()

# ─── Section 1: Raw Data Table ───────────────────────────────────────────────
w("## 1. Raw Data Table")
w()
w("| # | Experiment ID | Model | Suite | Condition | Seed | SR | Trigger Rate | Conclusion |")
w("|---|---|---|---|---|---|---|---|---|")
for i, r in enumerate(records, 1):
    tr_str = f"{r['trigger_rate']:.4f}" if r["trigger_rate"] is not None else "—"
    w(f"| {i} | `{r['exp_id']}` | {r['model']} | {r['suite']} | {r['condition']} | {r['seed']} | {r['SR']:.4f} | {tr_str} | {r['conclusion']} |")
w()

# ─── Section 2: Summary Table ────────────────────────────────────────────────
w("## 2. Summary Table (Mean ± Std)")
w()
w("| Model | Suite | Condition | N | Mean SR | Std SR | Min SR | Max SR | Mean TR | Std TR |")
w("|---|---|---|---|---|---|---|---|---|---|")
for key in sorted(summary.keys()):
    model, suite, condition = key
    s = summary[key]
    tr_mean = f"{s['mean_tr']:.4f}" if s["mean_tr"] is not None else "—"
    tr_std = f"{s['std_tr']:.4f}" if s["std_tr"] is not None else "—"
    w(f"| {model} | {suite} | {condition} | {s['n']} | {s['mean_sr']:.4f} | {s['std_sr']:.4f} | {s['min_sr']:.4f} | {s['max_sr']:.4f} | {tr_mean} | {tr_std} |")
w()

# ─── Section 3: Effect Size Analysis ─────────────────────────────────────────
w("## 3. Effect Size Analysis Per Suite")
w()

for model in ["smolvla", "pi05"]:
    w(f"### {model.upper()}")
    w()

    # Degradation ranking
    degradation = []

    for suite in ["object", "spatial", "goal", "long"]:
        effects = effect_analysis(model, suite, summary)
        if not effects:
            continue

        w(f"#### {suite.capitalize()}")
        w()
        w("| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |")
        w("|---|---|---|---|---|---|---|---|")

        for label, eff in effects.items():
            d_str = f"{eff['d']:.3f}" if eff["d"] is not None else "—"
            ci_str = f"[{eff['ci_low']:.4f}, {eff['ci_high']:.4f}]" if eff["ci_low"] is not None else "—"
            t_str = f"{eff['t_stat']:.3f}" if eff["t_stat"] is not None else "—"
            p_str = f"{eff['p_val']:.4f}" if eff["p_val"] is not None else "—"
            if eff["p_val"] is not None and eff["p_val"] < 0.001:
                p_str = f"{eff['p_val']:.2e}"
            w(f"| {label} | {eff['delta']:+.4f} | {d_str} | {ci_str} | {t_str} | {p_str} | {eff['n_a']} | {eff['n_b']} |")

            # Track degradation for CRM-always-on vs VLA-only
            if "CRM-always-on vs VLA-only" in label:
                degradation.append((suite, eff["delta"]))
        w()

    # Degradation ranking
    if degradation:
        degradation.sort(key=lambda x: x[1])
        w(f"**Degradation severity ranking ({model})**: ", )
        ranking = " > ".join([f"{s} ({d:+.4f})" for s, d in degradation])
        w(ranking)
        w()

# ─── Section 4: Trigger Rate Analysis ────────────────────────────────────────
w("## 4. Trigger Rate Analysis")
w()

for model in ["smolvla", "pi05"]:
    w(f"### {model.upper()} Trigger Rate Distribution")
    w()

    # Per-condition trigger rate stats
    w("| Suite | Condition | N (with TR) | Mean TR | Std TR | Min TR | Max TR |")
    w("|---|---|---|---|---|---|---|")
    for suite in ["object", "spatial", "goal", "long"]:
        for cond in ["crm-always-on", "adaptive"]:
            key = (model, suite, cond)
            recs_with_tr = [r for r in records
                           if r["model"] == model and r["suite"] == suite
                           and r["condition"] == cond and r["trigger_rate"] is not None]
            if recs_with_tr:
                trs = [r["trigger_rate"] for r in recs_with_tr]
                w(f"| {suite} | {cond} | {len(trs)} | {np.mean(trs):.4f} | {np.std(trs, ddof=1) if len(trs) > 1 else 0:.4f} | {np.min(trs):.4f} | {np.max(trs):.4f} |")
    w()

    # Correlation analysis
    tr_corr = trigger_correlation_analysis(model, records, summary)
    if tr_corr:
        w(f"### {model.upper()} Trigger Rate × SR Correlation (Adaptive only)")
        w()
        w("| Suite | N | Mean TR | Pearson r | Pearson p | Spearman ρ | Spearman p |")
        w("|---|---|---|---|---|---|---|")
        for suite, tc in sorted(tr_corr.items()):
            r_p = f"{tc['r_pearson']:.4f}" if tc["r_pearson"] is not None else "—"
            p_p = f"{tc['p_pearson']:.4f}" if tc["p_pearson"] is not None else "—"
            r_s = f"{tc['r_spearman']:.4f}" if tc["r_spearman"] is not None else "—"
            p_s = f"{tc['p_spearman']:.4f}" if tc["p_spearman"] is not None else "—"
            w(f"| {suite} | {tc['n']} | {tc['mean_tr']:.4f} | {r_p} | {p_p} | {r_s} | {p_s} |")
        w()

# ─── Section 5: Cross-Seed Variance Analysis ─────────────────────────────────
w("## 5. Cross-Seed Variance Analysis")
w()

for model in ["smolvla", "pi05"]:
    w(f"### {model.upper()}")
    w()

    has_results = False
    for suite in ["object", "spatial", "goal", "long"]:
        var_results = variance_analysis(model, suite, summary)
        if var_results:
            has_results = True
            w(f"#### {suite.capitalize()}")
            w()
            w("| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |")
            w("|---|---|---|---|---|---|")
            for label, vr in var_results.items():
                w(f"| {label} | {vr['var_1']:.6f} | {vr['var_2']:.6f} | {vr['f_ratio']:.3f} | {vr['levene_stat']:.3f} | {vr['levene_p']:.4f} |")
            w()

    if not has_results:
        w("Insufficient data (need ≥3 seeds per condition for variance testing).")
        w()

# ─── Section 6: Key Findings ─────────────────────────────────────────────────
w("## 6. Key Findings Summary")
w()

# Compute key findings programmatically
findings = []

# Finding 1: CRM degradation pattern
for model in ["smolvla", "pi05"]:
    degradations = []
    for suite in ["object", "spatial", "goal", "long"]:
        vla_key = (model, suite, "vla-only")
        crm_key = (model, suite, "crm-always-on")
        if vla_key in summary and crm_key in summary:
            delta = summary[crm_key]["mean_sr"] - summary[vla_key]["mean_sr"]
            degradations.append((suite, delta))

    if degradations:
        worst = min(degradations, key=lambda x: x[1])
        best = max(degradations, key=lambda x: x[1])
        avg_deg = np.mean([d for _, d in degradations])
        findings.append(
            f"**{model.upper()} CRM always-on degradation**: Average Δ = {avg_deg:+.4f}. "
            f"Worst: {worst[0]} ({worst[1]:+.4f}). Best: {best[0]} ({best[1]:+.4f})."
        )

# Finding 2: Adaptive recovery
for model in ["smolvla", "pi05"]:
    recoveries = []
    for suite in ["object", "spatial", "goal", "long"]:
        vla_key = (model, suite, "vla-only")
        adapt_key = (model, suite, "adaptive")
        crm_key = (model, suite, "crm-always-on")
        if vla_key in summary and adapt_key in summary:
            delta_vs_vla = summary[adapt_key]["mean_sr"] - summary[vla_key]["mean_sr"]
            recoveries.append((suite, delta_vs_vla))
        if crm_key in summary and adapt_key in summary:
            recovery = summary[adapt_key]["mean_sr"] - summary[crm_key]["mean_sr"]

    if recoveries:
        avg_rec = np.mean([d for _, d in recoveries])
        pos_suites = [s for s, d in recoveries if d > 0]
        neg_suites = [s for s, d in recoveries if d < 0]
        findings.append(
            f"**{model.upper()} Adaptive vs VLA-only**: Average Δ = {avg_rec:+.4f}. "
            f"Positive in: {', '.join(pos_suites) if pos_suites else 'none'}. "
            f"Negative in: {', '.join(neg_suites) if neg_suites else 'none'}."
        )

# Finding 3: Trigger rate patterns
for model in ["smolvla", "pi05"]:
    tr_by_suite = {}
    for suite in ["object", "spatial", "goal", "long"]:
        adapt_key = (model, suite, "adaptive")
        if adapt_key in summary and summary[adapt_key]["mean_tr"] is not None:
            tr_by_suite[suite] = summary[adapt_key]["mean_tr"]
    if tr_by_suite:
        sorted_tr = sorted(tr_by_suite.items(), key=lambda x: x[1], reverse=True)
        tr_strs = [f"{s}: {v:.3f}" for s, v in sorted_tr]
        findings.append(f"**{model.upper()} Trigger rates (adaptive)**: {', '.join(tr_strs)}")

# Finding 4: Variance patterns
for model in ["smolvla", "pi05"]:
    high_var_cond = []
    for suite in ["object", "spatial", "goal", "long"]:
        for cond in ["vla-only", "crm-always-on", "adaptive"]:
            key = (model, suite, cond)
            if key in summary and summary[key]["n"] >= 3:
                high_var_cond.append((suite, cond, summary[key]["std_sr"]))
    if high_var_cond:
        highest = max(high_var_cond, key=lambda x: x[2])
        lowest = min(high_var_cond, key=lambda x: x[2])
        findings.append(
            f"**{model.upper()} Variance**: Highest std: {highest[0]}/{highest[1]} (σ={highest[2]:.4f}). "
            f"Lowest std: {lowest[0]}/{lowest[1]} (σ={lowest[2]:.4f})."
        )

for i, finding in enumerate(findings, 1):
    w(f"{i}. {finding}")

w()

# ─── Section 7: Detailed condition breakdowns ────────────────────────────────
w("## 7. Condition Summary Pivot Table")
w()
w("### SR by Model × Suite × Condition")
w()
w("| Model | Suite | VLA-only (N, μ±σ) | CRM-always-on (N, μ±σ) | Adaptive (N, μ±σ) | Δ(CRM-VLA) | Δ(Adp-VLA) | Δ(Adp-CRM) |")
w("|---|---|---|---|---|---|---|---|")

for model in ["smolvla", "pi05"]:
    for suite in ["object", "spatial", "goal", "long"]:
        cells = []
        means = {}
        for cond in ["vla-only", "crm-always-on", "adaptive"]:
            key = (model, suite, cond)
            if key in summary:
                s = summary[key]
                cells.append(f"{s['n']}, {s['mean_sr']:.3f}±{s['std_sr']:.3f}")
                means[cond] = s["mean_sr"]
            else:
                cells.append("—")

        d_crm_vla = f"{means.get('crm-always-on', 0) - means.get('vla-only', 0):+.3f}" if "crm-always-on" in means and "vla-only" in means else "—"
        d_adp_vla = f"{means.get('adaptive', 0) - means.get('vla-only', 0):+.3f}" if "adaptive" in means and "vla-only" in means else "—"
        d_adp_crm = f"{means.get('adaptive', 0) - means.get('crm-always-on', 0):+.3f}" if "adaptive" in means and "crm-always-on" in means else "—"

        w(f"| {model} | {suite} | {cells[0]} | {cells[1]} | {cells[2]} | {d_crm_vla} | {d_adp_vla} | {d_adp_crm} |")

w()

# Write output
output_text = "\n".join(lines)
with open(OUTPUT_FILE, "w") as f:
    f.write(output_text)

print(f"\nReport written to: {OUTPUT_FILE}")
print(f"Total lines: {len(lines)}")

# Print summary to stdout
print("\n=== Quick Summary ===")
for key in sorted(summary.keys()):
    model, suite, cond = key
    s = summary[key]
    print(f"  {model}/{suite}/{cond}: N={s['n']}, μ={s['mean_sr']:.4f}±{s['std_sr']:.4f}")
