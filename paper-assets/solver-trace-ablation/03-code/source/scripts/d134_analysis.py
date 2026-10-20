#!/usr/bin/env python3
"""D134 experiment analysis: multi-seed ISR vs Random, 4B GRPO training.
Reads taxonomy data from classify.json, taxonomy.json, or top-level taxonomy files.
Computes summary stats, statistical tests (Fisher, Mann-Whitney, permutation, Bayes Factor),
and BCa bootstrap CIs. Outputs appendix-ready markdown.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import betaln

CONDITION_MAP = [
    ("d134_4b_isr", "ISR"),
    ("d134_4b_random", "RANDOM"),
    ("plan002_additive", "ISR"),
    ("plan018_additive_random", "RANDOM"),
    ("plan018_random", "RANDOM"),
]

MODE_PREFIXES = {
    "d134_only": ["d134_4b"],
    "all": ["d134_4b", "plan002_additive_b01", "plan018_additive_random_b01", "plan018_random"],
}


def parse_args():
    p = argparse.ArgumentParser(description="D134 multi-seed analysis and statistical tests")
    p.add_argument("--data_dir", type=str, default="/root/autodl-tmp/outputs",
                   help="Directory containing experiment outputs")
    p.add_argument("--mode", type=str, default="d134_only", choices=list(MODE_PREFIXES),
                   help="d134_only = matched 5+5 design (default); all = include original seeds")
    p.add_argument("--prefix", type=str, default=None,
                   help="(Legacy) Single prefix filter; overrides mode/prefixes")
    p.add_argument("--prefixes", type=str, default=None,
                   help="Comma-separated prefixes; overrides --mode")
    p.add_argument("--output", type=str, default=None,
                   help="Write markdown summary to this file")
    p.add_argument("--n_perm", type=int, default=10000,
                   help="Number of permutations for permutation test")
    p.add_argument("--n_boot", type=int, default=10000,
                   help="Number of bootstrap resamples for BCa CI")
    p.add_argument("--seed", type=int, default=42,
                   help="Random seed for permutation/bootstrap")
    return p.parse_args()


# --- Data loading ---

def match_condition(name: str) -> str | None:
    best_prefix = ""
    best_cond = None
    for prefix, cond in CONDITION_MAP:
        if name.startswith(prefix) and len(prefix) > len(best_prefix):
            best_prefix = prefix
            best_cond = cond
    return best_cond


def extract_seed(name: str) -> int | None:
    m = re.search(r'_s(\d+)', name)
    return int(m.group(1)) if m else None


def load_eval_results(path: Path) -> dict | None:
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    if "eval_results" in data:
        return data["eval_results"]
    return data


def load_taxonomy_unified(path: Path) -> dict | None:
    with open(path) as f:
        raw = json.load(f)
    t = raw.get("taxonomy", {})
    proved = t.get("proved", 0)
    if proved == 0:
        return None
    h7 = t.get("H7", 0)
    h1 = t.get("H1_exact", 0)
    h8 = t.get("H8", 0)
    genuine = t.get("genuine", 0)
    return {
        "n_total": 100, "n_proved": proved,
        "h7_total_count": h7, "h7_total_rate": h7 / proved,
        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
        "genuine_count": genuine, "genuine_rate": genuine / proved,
        "content_independent_count": 0,
    }


def load_taxonomy_verification(path: Path) -> dict | None:
    with open(path) as f:
        raw = json.load(f)
    proved = raw.get("proved", 0)
    if proved == 0:
        return None
    tax = raw.get("taxonomy", {})
    h7 = tax.get("h7", {}).get("count", 0)
    h1 = tax.get("h1_exact", {}).get("count", 0)
    h8 = tax.get("h8", {}).get("count", 0)
    genuine = tax.get("genuine", {}).get("count", 0)
    return {
        "n_total": raw.get("total", 100), "n_proved": proved,
        "h7_total_count": h7, "h7_total_rate": h7 / proved,
        "h1_strict_count": h1, "h8_conjunction_collapse_count": h8,
        "genuine_count": genuine, "genuine_rate": genuine / proved,
        "content_independent_count": 0,
    }


def discover_runs(data_dir: Path, prefixes: list[str]) -> list[dict]:
    runs = []
    seen = set()
    for entry in sorted(data_dir.iterdir()):
        name = entry.name
        if not any(name.startswith(p) for p in prefixes):
            continue
        cond = match_condition(name)
        seed_val = extract_seed(name)
        if cond is None or seed_val is None:
            continue
        key = (cond, seed_val)
        if key in seen:
            continue
        data = None
        if entry.is_dir():
            for fname in ["classify.json", "taxonomy.json"]:
                data = load_eval_results(entry / fname)
                if data is not None:
                    break
            if data is None:
                continue
        elif entry.is_file():
            if name.endswith("_taxonomy_unified.json"):
                data = load_taxonomy_unified(entry)
            elif name.endswith("_taxonomy_verification.json"):
                data = load_taxonomy_verification(entry)
            if data is None:
                continue
        else:
            continue
        seen.add(key)
        isr_star = None
        if entry.is_dir():
            eval_path = entry / "eval_results.json"
            if eval_path.exists():
                with open(eval_path) as ef:
                    eval_raw = json.load(ef)
                isr_star = eval_raw.get("summary", {}).get("proved_only_mean_isr")
        runs.append({"dir_name": name, "seed": seed_val, "condition": cond,
                      "data": data, "isr_star": isr_star})
    return runs


def compute_row(run: dict) -> dict:
    d = run["data"]
    n_proved = d.get("n_proved", 0)
    n_total = d.get("n_total", 100)
    h7 = d.get("h7_total_count", 0)
    h7_rate = d.get("h7_total_rate", h7 / n_proved if n_proved > 0 else 0.0)
    h1 = d.get("h1_strict_count", 0)
    h8 = d.get("h8_conjunction_collapse_count", 0)
    genuine = d.get("genuine_count", 0)
    genuine_rate = d.get("genuine_rate", genuine / n_proved if n_proved > 0 else 0.0)
    ci = d.get("content_independent_count", 0)
    snh = max(genuine - ci, 0)
    snh_rate = snh / n_proved if n_proved > 0 else 0.0
    return {
        "seed": run["seed"], "condition": run["condition"], "n_total": n_total,
        "PR": n_proved, "H7_count": h7, "H7_rate": h7_rate,
        "H1_count": h1, "H8_count": h8,
        "genuine_count": genuine, "genuine_rate": genuine_rate,
        "CI_count": ci, "SNH_count": snh, "SNH_rate": snh_rate,
        "ISR_star": run.get("isr_star"),
    }


def build_table(runs: list[dict]) -> pd.DataFrame:
    rows = [compute_row(r) for r in runs]
    df = pd.DataFrame(rows)
    df = df.sort_values(["condition", "seed"]).reset_index(drop=True)
    return df


# --- Statistical tests ---

def fisher_h7_domination(df: pd.DataFrame) -> dict:
    results = {}
    for cond in ["ISR", "RANDOM"]:
        sub = df[df["condition"] == cond]
        results[cond] = {
            "n": len(sub),
            "h7_dom": int((sub["H7_rate"] >= 0.5).sum()),
            "not_h7_dom": int((sub["H7_rate"] < 0.5).sum()),
        }
    table = np.array([
        [results["ISR"]["h7_dom"], results["ISR"]["not_h7_dom"]],
        [results["RANDOM"]["h7_dom"], results["RANDOM"]["not_h7_dom"]],
    ])
    odds_ratio, p_value = stats.fisher_exact(table, alternative="greater")

    # 95% exact CI via scipy.stats.contingency
    or_ci_lo, or_ci_hi = np.nan, np.nan
    try:
        ct = stats.contingency.odds_ratio(table)
        ci = ct.confidence_interval(confidence_level=0.95)
        or_ci_lo, or_ci_hi = ci.low, ci.high
    except Exception:
        pass

    return {
        "table": table.tolist(),
        "ISR": results["ISR"],
        "RANDOM": results["RANDOM"],
        "odds_ratio": odds_ratio,
        "or_ci_lo": or_ci_lo,
        "or_ci_hi": or_ci_hi,
        "p_value": p_value,
    }


def permutation_test_genuine(df: pd.DataFrame, n_perm: int = 10000,
                              rng_seed: int = 42) -> dict:
    isr = df[df["condition"] == "ISR"]["genuine_rate"].values
    rand = df[df["condition"] == "RANDOM"]["genuine_rate"].values
    observed = isr.mean() - rand.mean()
    pooled = np.concatenate([isr, rand])
    n_isr = len(isr)
    rng = np.random.default_rng(rng_seed)
    count = 0
    for _ in range(n_perm):
        perm = rng.permutation(pooled)
        if perm[:n_isr].mean() - perm[n_isr:].mean() >= observed:
            count += 1
    return {
        "observed_diff": float(observed),
        "p_value": count / n_perm,
        "n_perm": n_perm,
        "isr_mean": float(isr.mean()),
        "random_mean": float(rand.mean()),
    }


def mannwhitney_h7(df: pd.DataFrame) -> dict:
    isr = df[df["condition"] == "ISR"]["H7_rate"].values
    rand = df[df["condition"] == "RANDOM"]["H7_rate"].values
    n1, n2 = len(isr), len(rand)
    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0 if n1 * n2 > 0 else np.nan
    return {
        "U": float(u_stat),
        "p_value": float(p_value),
        "r_rank_biserial": float(r_rb),
        "isr_median": float(np.median(isr)),
        "random_median": float(np.median(rand)),
    }


def mannwhitney_isr_star(df: pd.DataFrame) -> dict | None:
    isr = df[df["condition"] == "ISR"]["ISR_star"].dropna().values.astype(float)
    rand = df[df["condition"] == "RANDOM"]["ISR_star"].dropna().values.astype(float)
    if len(isr) < 2 or len(rand) < 2:
        return None
    n1, n2 = len(isr), len(rand)
    u_stat, p_value = stats.mannwhitneyu(isr, rand, alternative="greater")
    r_rb = 2.0 * u_stat / (n1 * n2) - 1.0
    return {
        "U": float(u_stat),
        "p_value": float(p_value),
        "r_rank_biserial": float(r_rb),
        "isr_median": float(np.median(isr)),
        "random_median": float(np.median(rand)),
        "isr_mean": float(np.mean(isr)),
        "random_mean": float(np.mean(rand)),
    }


def bca_bootstrap_ci(df: pd.DataFrame, metric: str, n_boot: int = 10000,
                      rng_seed: int = 42) -> dict:
    """BCa 95% CI for per-condition means of a metric."""
    result = {}
    for cond in ["ISR", "RANDOM"]:
        vals = df[df["condition"] == cond][metric].values
        if len(vals) < 2:
            result[cond] = {"mean": float(vals.mean()) if len(vals) else np.nan,
                            "ci_lo": np.nan, "ci_hi": np.nan}
            continue
        res = stats.bootstrap(
            (vals,), np.mean, n_resamples=n_boot,
            confidence_level=0.95, method="BCa",
            random_state=np.random.default_rng(rng_seed),
        )
        result[cond] = {
            "mean": float(vals.mean()),
            "ci_lo": float(res.confidence_interval.low),
            "ci_hi": float(res.confidence_interval.high),
        }
    return result


def bayes_factor_h7_domination(df: pd.DataFrame) -> dict:
    """BF10 for H7-domination rate difference (beta-binomial conjugate).
    H0: ISR and Random share same domination rate.
    H1: independent rates. Prior: Beta(1,1) on each.
    """
    isr_sub = df[df["condition"] == "ISR"]
    rand_sub = df[df["condition"] == "RANDOM"]
    k_isr = int((isr_sub["H7_rate"] >= 0.5).sum())
    n_isr = len(isr_sub)
    k_rand = int((rand_sub["H7_rate"] >= 0.5).sum())
    n_rand = len(rand_sub)
    k_total = k_isr + k_rand
    n_total = n_isr + n_rand

    # log marginal under H0 (shared rate)
    log_m_h0 = betaln(1 + k_total, 1 + n_total - k_total) - betaln(1, 1)
    # log marginal under H1 (independent rates)
    log_m_h1 = (betaln(1 + k_isr, 1 + n_isr - k_isr) - betaln(1, 1)
                + betaln(1 + k_rand, 1 + n_rand - k_rand) - betaln(1, 1))
    log_bf10 = log_m_h1 - log_m_h0
    bf10 = float(np.exp(log_bf10))

    return {
        "k_isr": k_isr, "n_isr": n_isr,
        "k_rand": k_rand, "n_rand": n_rand,
        "bf10": bf10,
        "log_bf10": float(log_bf10),
        "interpretation": _interpret_bf(bf10),
    }


def _interpret_bf(bf: float) -> str:
    if bf > 100:
        return "extreme evidence for H1"
    if bf > 30:
        return "very strong evidence for H1"
    if bf > 10:
        return "strong evidence for H1"
    if bf > 3:
        return "moderate evidence for H1"
    if bf > 1:
        return "anecdotal evidence for H1"
    if bf > 1/3:
        return "anecdotal evidence (inconclusive)"
    if bf > 1/10:
        return "moderate evidence for H0"
    return "strong evidence for H0"


def condition_stats(df: pd.DataFrame) -> pd.DataFrame:
    metrics = ["PR", "H7_rate", "genuine_rate", "SNH_rate"]
    rows = []
    for cond in ["ISR", "RANDOM"]:
        sub = df[df["condition"] == cond]
        row = {"condition": cond, "n_seeds": len(sub)}
        for m in metrics:
            vals = sub[m].values
            row[f"{m}_mean"] = vals.mean()
            row[f"{m}_std"] = vals.std(ddof=1) if len(vals) > 1 else 0.0
        isr_vals = sub["ISR_star"].dropna().values.astype(float)
        row["ISR_star_mean"] = isr_vals.mean() if len(isr_vals) else np.nan
        row["ISR_star_std"] = isr_vals.std(ddof=1) if len(isr_vals) > 1 else 0.0
        rows.append(row)
    return pd.DataFrame(rows)


# --- Formatting ---

def fmt_pct(val: float) -> str:
    return f"{val*100:.1f}\\%"

def fmt_or(val: float) -> str:
    return "$\\infty$" if np.isinf(val) else f"{val:.2f}"

def fmt_ci(lo: float, hi: float) -> str:
    lo_s = f"{lo:.2f}" if not np.isnan(lo) else "0"
    hi_s = "$\\infty$" if np.isinf(hi) or np.isnan(hi) else f"{hi:.2f}"
    return f"[{lo_s}, {hi_s}]"

def fmt_p(p: float) -> str:
    if p < 0.001:
        return "$<$0.001"
    return f"{p:.3f}"

def fmt_mean_std(mean: float, std: float, pct: bool = False) -> str:
    if pct:
        return f"{mean*100:.1f} $\\pm$ {std*100:.1f}\\%"
    return f"{mean:.1f} $\\pm$ {std:.1f}"

def fmt_bca(bca: dict, pct: bool = False) -> str:
    m = bca["mean"]
    lo, hi = bca["ci_lo"], bca["ci_hi"]
    if pct:
        return f"{m*100:.1f}\\% [{lo*100:.1f}, {hi*100:.1f}]"
    return f"{m:.1f} [{lo:.1f}, {hi:.1f}]"


# --- Console output ---

def print_per_seed_table(df: pd.DataFrame):
    print("\n" + "=" * 90)
    print("  PER-SEED RESULTS")
    print("=" * 90)
    cols = ["condition", "seed", "PR", "H7_count", "H7_rate", "H1_count",
            "H8_count", "genuine_count", "genuine_rate", "CI_count", "SNH_count", "SNH_rate",
            "ISR_star"]
    fmt = df[cols].copy()
    for c in ["H7_rate", "genuine_rate", "SNH_rate"]:
        fmt[c] = fmt[c].apply(lambda v: f"{v*100:.1f}%")
    fmt["ISR_star"] = fmt["ISR_star"].apply(lambda v: f"{v:.4f}" if pd.notna(v) else "---")
    print(fmt.to_string(index=False))


def print_condition_stats(cond_df: pd.DataFrame):
    print("\n" + "=" * 90)
    print("  CONDITION-LEVEL STATISTICS (mean +/- SD)")
    print("=" * 90)
    for _, row in cond_df.iterrows():
        n = int(row['n_seeds'])
        print(f"\n  {row['condition']} (n={n} seeds):")
        print(f"    PR:           {row['PR_mean']:.1f} +/- {row['PR_std']:.1f}")
        print(f"    H7 rate:      {row['H7_rate_mean']*100:.1f} +/- {row['H7_rate_std']*100:.1f}%")
        print(f"    Genuine rate: {row['genuine_rate_mean']*100:.1f} +/- {row['genuine_rate_std']*100:.1f}%")
        print(f"    S-NH rate:    {row['SNH_rate_mean']*100:.1f} +/- {row['SNH_rate_std']*100:.1f}%")
        if not np.isnan(row.get('ISR_star_mean', np.nan)):
            print(f"    ISR*:         {row['ISR_star_mean']:.4f} +/- {row['ISR_star_std']:.4f}")


def print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star=None):
    print("\n" + "=" * 90)
    print("  STATISTICAL TESTS")
    print("=" * 90)

    print("\n  1. H7 Domination Fisher Exact Test (H7-dominated = H7% >= 50%)")
    print(f"     ISR:    {fisher['ISR']['h7_dom']} dominated / {fisher['ISR']['n']} seeds")
    print(f"     RANDOM: {fisher['RANDOM']['h7_dom']} dominated / {fisher['RANDOM']['n']} seeds")
    print(f"     Contingency: {fisher['table']}")
    or_str = "inf" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.4f}"
    print(f"     OR = {or_str}, 95% CI = [{fisher['or_ci_lo']:.4f}, {fisher['or_ci_hi']:.4f}]"
          if not np.isnan(fisher['or_ci_lo']) else f"     OR = {or_str}, 95% CI = N/A")
    print(f"     p-value (one-sided, greater): {fisher['p_value']:.4f}")

    print(f"\n  2. Genuine Rate Permutation Test (n_perm={perm['n_perm']})")
    print(f"     ISR mean:    {perm['isr_mean']*100:.2f}%")
    print(f"     RANDOM mean: {perm['random_mean']*100:.2f}%")
    print(f"     Diff: {perm['observed_diff']*100:.2f} pp, p = {perm['p_value']:.4f}")

    print(f"\n  3. H7 Rate Mann-Whitney U Test")
    print(f"     ISR median:    {mw['isr_median']*100:.1f}%")
    print(f"     RANDOM median: {mw['random_median']*100:.1f}%")
    print(f"     U = {mw['U']:.1f}, p = {mw['p_value']:.4f}")
    print(f"     Rank-biserial r = {mw['r_rank_biserial']:.4f}")

    print(f"\n  4. Bayes Factor (H7 Domination, Beta-Binomial)")
    print(f"     ISR:    {bf['k_isr']}/{bf['n_isr']} dominated")
    print(f"     RANDOM: {bf['k_rand']}/{bf['n_rand']} dominated")
    print(f"     BF10 = {bf['bf10']:.4f} ({bf['interpretation']})")

    print(f"\n  5. BCa Bootstrap 95% CI (n_boot resamples)")
    for label, bca in [("H7 rate", bca_h7), ("Genuine rate", bca_gen)]:
        print(f"     {label}:")
        for cond in ["ISR", "RANDOM"]:
            b = bca[cond]
            print(f"       {cond}: {b['mean']*100:.1f}% [{b['ci_lo']*100:.1f}, {b['ci_hi']*100:.1f}]"
                  if not np.isnan(b['ci_lo']) else f"       {cond}: {b['mean']*100:.1f}% [N/A]")

    if mw_isr_star:
        print(f"\n  6. ISR* (Proved-Only Mean ISR) Mann-Whitney U Test")
        print(f"     ISR mean:    {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}")
        print(f"     RANDOM mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}")
        print(f"     U = {mw_isr_star['U']:.1f}, p = {mw_isr_star['p_value']:.4f}")
        print(f"     Rank-biserial r = {mw_isr_star['r_rank_biserial']:.4f}")


# --- Markdown generation (appendix-ready) ---

def generate_markdown(df: pd.DataFrame, cond_df: pd.DataFrame,
                      fisher: dict, perm: dict, mw: dict,
                      bf: dict, bca_h7: dict, bca_gen: dict,
                      mw_isr_star: dict = None) -> str:
    L = []
    L.append("## D134: ISR vs Random Statistical Analysis\n")

    # Per-seed table
    L.append("### Table A1: Per-Seed Hacking Taxonomy (4B Qwen3, 500 steps)\n")
    L.append("| Condition | Seed | PR | H7 | H7\\% | H1 | H8 | Genuine | Gen\\% | CI | S-NH | S-NH\\% | ISR* |")
    L.append("|:----------|-----:|---:|---:|-----:|---:|---:|--------:|------:|---:|-----:|-------:|-----:|")
    for _, r in df.iterrows():
        isr_star_str = f"{r['ISR_star']:.4f}" if pd.notna(r.get('ISR_star')) else "---"
        L.append(
            f"| {r['condition']} | {r['seed']} | {int(r['PR'])} | {int(r['H7_count'])} | "
            f"{r['H7_rate']*100:.1f} | {int(r['H1_count'])} | {int(r['H8_count'])} | "
            f"{int(r['genuine_count'])} | {r['genuine_rate']*100:.1f} | {int(r['CI_count'])} | "
            f"{int(r['SNH_count'])} | {r['SNH_rate']*100:.1f} | {isr_star_str} |"
        )

    # Condition summary with BCa CI
    L.append("\n### Table A2: Condition-Level Summary\n")
    L.append("| Condition | $n$ | PR (mean$\\pm$SD) | H7\\% (mean$\\pm$SD) | H7\\% BCa 95\\% CI | Gen\\% (mean$\\pm$SD) | Gen\\% BCa 95\\% CI |")
    L.append("|:----------|----:|:------------------|:-------------------|:-----------------|:-------------------|:-----------------|")
    for _, r in cond_df.iterrows():
        cond = r["condition"]
        h7_bca = bca_h7.get(cond, {})
        gen_bca = bca_gen.get(cond, {})
        h7_ci = f"[{h7_bca['ci_lo']*100:.1f}, {h7_bca['ci_hi']*100:.1f}]" if h7_bca and not np.isnan(h7_bca.get('ci_lo', np.nan)) else "N/A"
        gen_ci = f"[{gen_bca['ci_lo']*100:.1f}, {gen_bca['ci_hi']*100:.1f}]" if gen_bca and not np.isnan(gen_bca.get('ci_lo', np.nan)) else "N/A"
        L.append(
            f"| {cond} | {int(r['n_seeds'])} | "
            f"{r['PR_mean']:.1f}$\\pm${r['PR_std']:.1f} | "
            f"{r['H7_rate_mean']*100:.1f}$\\pm${r['H7_rate_std']*100:.1f} | "
            f"{h7_ci} | "
            f"{r['genuine_rate_mean']*100:.1f}$\\pm${r['genuine_rate_std']*100:.1f} | "
            f"{gen_ci} |"
        )

    # Statistical tests
    if fisher and perm and mw and bf:
        L.append("\n### Statistical Tests\n")

        # Fisher
        or_str = "$\\infty$" if np.isinf(fisher['odds_ratio']) else f"{fisher['odds_ratio']:.2f}"
        ci_lo = f"{fisher['or_ci_lo']:.2f}" if not np.isnan(fisher['or_ci_lo']) else "0"
        ci_hi = "$\\infty$" if np.isinf(fisher.get('or_ci_hi', np.inf)) or np.isnan(fisher.get('or_ci_hi', np.nan)) else f"{fisher['or_ci_hi']:.2f}"
        L.append("**1. H7 Domination Fisher Exact Test** (threshold: H7$\\geq$50\\% of proved)")
        L.append(f"- ISR: {fisher['ISR']['h7_dom']}/{fisher['ISR']['n']} seeds H7-dominated; "
                 f"Random: {fisher['RANDOM']['h7_dom']}/{fisher['RANDOM']['n']}")
        L.append(f"- OR = {or_str}, 95\\% exact CI = [{ci_lo}, {ci_hi}], "
                 f"$p$ = {fmt_p(fisher['p_value'])}")
        L.append("")

        # Permutation
        L.append(f"**2. Genuine Rate Permutation Test** ($n$ = {perm['n_perm']:,} permutations)")
        L.append(f"- ISR mean: {perm['isr_mean']*100:.2f}\\%, Random mean: {perm['random_mean']*100:.2f}\\%")
        L.append(f"- $\\Delta$ = {perm['observed_diff']*100:.2f} pp, $p$ = {fmt_p(perm['p_value'])}")
        L.append("")

        # Mann-Whitney
        L.append("**3. H7 Rate Mann-Whitney $U$ Test**")
        L.append(f"- ISR median: {mw['isr_median']*100:.1f}\\%, Random median: {mw['random_median']*100:.1f}\\%")
        L.append(f"- $U$ = {mw['U']:.1f}, $p$ = {fmt_p(mw['p_value'])}, "
                 f"rank-biserial $r$ = {mw['r_rank_biserial']:.3f}")
        L.append("")

        # Bayes Factor
        L.append("**4. Bayes Factor** (Beta-Binomial conjugate, prior: Beta(1,1))")
        L.append(f"- $BF_{{10}}$ = {bf['bf10']:.2f} ({bf['interpretation']})")
        L.append(f"- ISR: {bf['k_isr']}/{bf['n_isr']} H7-dominated, "
                 f"Random: {bf['k_rand']}/{bf['n_rand']}")

        if mw_isr_star:
            L.append("")
            L.append("**5. ISR* (Proved-Only Mean ISR) Mann-Whitney $U$ Test**")
            L.append(f"- ISR mean: {mw_isr_star['isr_mean']:.4f}, median: {mw_isr_star['isr_median']:.4f}")
            L.append(f"- Random mean: {mw_isr_star['random_mean']:.4f}, median: {mw_isr_star['random_median']:.4f}")
            L.append(f"- $U$ = {mw_isr_star['U']:.1f}, $p$ = {fmt_p(mw_isr_star['p_value'])}, "
                     f"rank-biserial $r$ = {mw_isr_star['r_rank_biserial']:.3f}")

    return "\n".join(L) + "\n"


# --- Main ---

def main():
    args = parse_args()
    data_dir = Path(args.data_dir)

    if not data_dir.exists():
        print(f"ERROR: data directory {data_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    if args.prefix:
        prefixes = [args.prefix]
    elif args.prefixes:
        prefixes = [p.strip() for p in args.prefixes.split(",")]
    else:
        prefixes = MODE_PREFIXES[args.mode]
    print(f"Mode: {args.mode} | Prefixes: {prefixes}")

    runs = discover_runs(data_dir, prefixes)
    if not runs:
        print(f"ERROR: no runs found in {data_dir} with prefixes {prefixes}", file=sys.stderr)
        sys.exit(1)

    isr_count = sum(1 for r in runs if r["condition"] == "ISR")
    rand_count = sum(1 for r in runs if r["condition"] == "RANDOM")
    print(f"Found {len(runs)} runs: {isr_count} ISR, {rand_count} RANDOM")
    for r in runs:
        print(f"  {r['condition']:6s} s{r['seed']} <- {r['dir_name']}")

    df = build_table(runs)
    print_per_seed_table(df)

    cond_df = condition_stats(df)
    print_condition_stats(cond_df)

    if isr_count < 2 or rand_count < 2:
        print("\nWARNING: need >= 2 seeds per condition for statistical tests, skipping.",
              file=sys.stderr)
        bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
        bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
        if args.output:
            md = generate_markdown(df, cond_df, {}, {}, {}, {}, bca_h7, bca_gen)
            Path(args.output).write_text(md)
            print(f"\nMarkdown written to {args.output}")
        return

    fisher = fisher_h7_domination(df)
    perm = permutation_test_genuine(df, n_perm=args.n_perm, rng_seed=args.seed)
    mw = mannwhitney_h7(df)
    bf = bayes_factor_h7_domination(df)
    bca_h7 = bca_bootstrap_ci(df, "H7_rate", args.n_boot, args.seed)
    bca_gen = bca_bootstrap_ci(df, "genuine_rate", args.n_boot, args.seed)
    mw_isr_star = mannwhitney_isr_star(df)

    print_tests(fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)

    md = generate_markdown(df, cond_df, fisher, perm, mw, bf, bca_h7, bca_gen, mw_isr_star)
    print("\n" + "=" * 90)
    print("  MARKDOWN OUTPUT (appendix-ready)")
    print("=" * 90)
    print(md)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(md)
        print(f"Markdown written to {args.output}")


if __name__ == "__main__":
    main()
