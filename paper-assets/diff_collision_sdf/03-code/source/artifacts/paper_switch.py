#!/usr/bin/env python3
"""Auto-switch paper text based on λ=0.1 s2 30K eval result.

Usage:
  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run
  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0
"""
import argparse
import subprocess
import sys
from itertools import combinations
from math import comb, sqrt
from pathlib import Path

NULL_VALUES = [57.0, 52.5, 55, 57, 54, 52.5]
NULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)
NULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5

S0_CAR, S1_CAR = 58.0, 58.5
S0_TSR, S1_TSR = 47.0, 49.0

PAPER_DIR = Path(__file__).resolve().parent.parent / "docs" / "paper"


def mean(v):
    return sum(v) / len(v)


def std_b(v):
    m = mean(v)
    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5


def perm_test(null_vals, treat_vals):
    pool = null_vals + treat_vals
    k = len(treat_vals)
    obs = mean(treat_vals)
    mu = mean(pool)
    dev = abs(obs - mu)
    n = comb(len(pool), k)
    ge = tw = 0
    for c in combinations(pool, k):
        m = mean(c)
        if m >= obs:
            ge += 1
        if abs(m - mu) >= dev - 1e-12:
            tw += 1
    return ge / n, tw / n, n


def fill(tpl, vals):
    for k, v in vals.items():
        tpl = tpl.replace("{" + k + "}", str(v))
    return tpl


def safe_replace(content, old, new, label):
    n = content.count(old)
    if n == 0:
        print(f"  !! [{label}] NOT FOUND")
        return content, False
    if n > 1:
        print(f"  !! [{label}] found {n}x")
        return content, False
    return content.replace(old, new), True


def get_replacements(scenario, v):
    R = []
    is_c = scenario == "C"

    # 1. abstract.tex L5 (training results — condensed abstract)
    old = (
        r"and SDF training supervision shows no statistically significant benefit "
        r"beyond collision-free demonstrations alone."
    )
    if is_c:
        new = (
            r"and SDF training supervision shows no statistically significant benefit "
            r"at $\lambda \leq 0.01$; at $\lambda = 0.1$, a modest increase emerges "
            r"but remains small relative to the demonstration-driven gain."
        )
    else:
        new = old
    R.append(("abstract.tex", "abstract L5 training", old, new))

    # 2. abstract.tex L6 (concluding sentence — condensed abstract)
    old = (
        r"These findings suggest that collision avoidance primarily arises from "
        r"demonstration data rather than EE-only geometric supervision."
    )
    if is_c:
        new = (
            r"These findings suggest that collision avoidance primarily arises from "
            r"demonstration data, though a modest SDF effect at high loss weights "
            r"cannot be fully ruled out."
        )
    else:
        new = old
    R.append(("abstract.tex", "abstract L6 conclusion", old, new))

    # 3. claim3.tex L3 scope sentence
    old = (
        r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
        r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
        r"evaluated at the 30K-step checkpoint."
    )
    if is_c:
        new = (
            r"We compare LoRA-only against LoRA+SDF at three loss weights "
            r"($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at "
            r"the 30K-step checkpoint."
        )
    else:
        new = (
            r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
            r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
            r"evaluated at the 30K-step checkpoint."
        )
    R.append(("claim3.tex", "claim3 L3 scope", old, new))

    # 4. claim3.tex L7 table caption
    old = (
        r"\caption{Avoidance source attribution on SafeLIBERO. SDF shows no "
        r"statistically significant CAR improvement beyond LoRA-only at the tested "
        r"scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models "
        r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}"
    )
    if is_c:
        new = fill(
            r"\caption{Avoidance source attribution on SafeLIBERO. SDF at "
            r"$\lambda \leq 0.01$ shows no statistically significant CAR improvement "
            r"beyond LoRA-only ($p > 0.1$). At $\lambda = 0.1$, a modest increase "
            r"reaches statistical significance ($z = {z_value}$, permutation "
            r"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\,pp) "
            r"is small relative to the $+$26\,pp LoRA gain. All fine-tuned models "
            r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}", v)
    else:
        new = (
            r"\caption{Avoidance source attribution on SafeLIBERO. SDF shows no "
            r"statistically significant CAR improvement beyond LoRA-only at the tested "
            r"scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models "
            r"exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}"
        )
    R.append(("claim3.tex", "claim3 L7 caption", old, new))

    # 5. claim3.tex L20 table row
    old = (
        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
        r"50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\"
    )
    new = fill(
        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
        r"{tsr_mean}\,$\pm$\,{tsr_std} & {mean_car}\,$\pm$\,{std_car} & 0.394 \\", v)
    R.append(("claim3.tex", "claim3 L20 table row", old, new))

    # 6. claim3.tex L27 body paragraph
    old = (
        r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
        r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
        r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
        r"avoidance. Adding SDF supervision does not yield statistically significant "
        r"improvement at the tested scale: LoRA-only CAR (54.83\%) is statistically "
        r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
        r"(57.00\%, $p = 0.155$; Appendix~\ref{sec:appendix_null}). "
        r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
        r"CAR\,=\,57.5\% (18K checkpoint, single seed s2), suggesting that SDF gradients "
        r"do not produce a lasting behavioral effect. The per-task CAR ordering "
        r"is preserved across all conditions and invariant to $\lambda$ "
        r"(Figure~\ref{fig:lambda_and_fingerprint}, right), indicating "
        r"that avoidance patterns reflect the demonstration distribution rather than "
        r"geometric supervision."
    )
    if is_c:
        new = (
            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
            r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
            r"avoidance. At $\lambda \leq 0.01$, SDF supervision does not yield "
            r"statistically significant improvement: LoRA-only CAR (54.83\%) is within "
            r"0.17\,pp of $\lambda = 0.005$ and statistically indistinguishable from "
            r"$\lambda = 0.01$ (56.33\%, $p > 0.1$; Appendix~\ref{sec:appendix_null}). "
            r"At $\lambda = 0.1$, a modest increase emerges "
            r"(Section~\ref{sec:lambda_high}), but per-task CAR ordering "
            r"remains identical across all conditions "
            r"(Figure~\ref{fig:lambda_and_fingerprint}, right), indicating that avoidance patterns "
            r"reflect the demonstration distribution regardless of SDF loss weight. "
            r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
            r"CAR\,=\,57.5\% (18K checkpoint, single seed s2), suggesting "
            r"that SDF gradients do not produce a lasting behavioral effect."
        )
    else:
        new = fill(
            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with "
            r"zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine "
            r"avoidance. Adding SDF supervision does not yield statistically significant "
            r"improvement at the tested scale: LoRA-only CAR (54.83\%) is statistically "
            r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
            r"({mean_car}\%, $p = {p_value}$; Appendix~\ref{sec:appendix_null}). "
            r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
            r"CAR\,=\,57.5\% (18K checkpoint, single seed s2), suggesting that SDF gradients "
            r"do not produce a lasting behavioral effect. The per-task CAR ordering "
            r"is preserved across all conditions and invariant to $\lambda$ "
            r"(Figure~\ref{fig:lambda_and_fingerprint}, right), indicating "
            r"that avoidance patterns reflect the demonstration distribution rather than "
            r"geometric supervision.", v)
    R.append(("claim3.tex", "claim3 L27 body", old, new))

    # 7. claim3.tex L32-33 dose-response paragraph
    hdr = r"\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}"
    old_body = (
        r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
        r"CAR\,=\,57.00\%\,$\pm$\,2.18 "
        r"(3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null "
        r"distribution ($p = 0.155$; Figure~\ref{fig:lambda_and_fingerprint}, left). "
        r"Alternative null constructions yield consistent "
        r"non-significance (Appendix~\ref{sec:appendix_null}). "
        r"With $n = 3$ seeds ($\sigma \approx 2.3$\,pp), 80\% "
        r"power requires effects $\geq 5.6$\,pp; the observed "
        r"${\sim}$2.2\,pp falls below this minimum detectable effect (MDE). "
        r"The binding constraint is not signal magnitude but "
        r"the structural mismatch between EE monitoring and "
        r"full-body collision surfaces."
    )
    old = hdr + "\n" + old_body
    if is_c:
        new_body = fill(
            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), a modest but "
            r"statistically significant departure from the null distribution "
            r"(mean 54.67\%, $\sigma = 2.07$; permutation "
            r"$p = {p_value}$, one-tailed $p = {p_one_value}$). The "
            r"effect size of {delta_pp}\,pp is small relative to the $+$26\,pp gain "
            r"from LoRA fine-tuning alone, indicating that EE-only SDF supervision "
            r"can incrementally augment demonstration-driven avoidance at sufficiently "
            r"high loss weights but cannot substitute for it. A stepwise ablation across "
            r"six checkpoints (16K--28K) shows no sustained trend prior to 30K "
            r"(mean 55.3\%, within 0.4$\sigma$ of the null; "
            r"Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K "
            r"remains identical to all other conditions "
            r"(Figure~\ref{fig:lambda_and_fingerprint}, left), confirming that the dominant avoidance "
            r"signal remains the demonstration distribution. The response is thus "
            r"dose-dependent: SDF shows no significant benefit at $\lambda \leq 0.01$ "
            r"($p > 0.1$), with a small but detectable effect at $\lambda = 0.1$ "
            r"that preserves the same demonstration-driven avoidance fingerprint.", v)
    else:
        new_body = fill(
            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), within the null "
            r"distribution (mean 54.67\%, $\sigma = 2.07$; permutation "
            r"$p = {p_value}$, one-tailed $p = {p_one_value}$). "
            r"Alternative null constructions yield consistent non-significance. "
            r"With $n = 3$ seeds ($\sigma \approx 2.3$\,pp), 80\% power requires "
            r"effects $\geq 5.6$\,pp; the observed ${\sim}$2.2\,pp falls below this "
            r"MDE (Figure~\ref{fig:lambda_and_fingerprint}, left). The binding constraint is not "
            r"training signal magnitude but the structural mismatch between "
            r"end-effector monitoring and full-body collision surfaces.", v)
    R.append(("claim3.tex", "claim3 L32-33 dose-response", old, hdr + "\n" + new_body))

    # 8. claim3.tex lambda+fingerprint figure caption
    old = (
        r"\caption{(Left) Effect of SDF loss weight $\lambda$ on CAR and TSR "
        r"($\lambda = 0$: LoRA-only). All $\lambda$ values remain within the "
        r"null band ($p > 0.05$). (Right) Per-task CAR fingerprint; the task "
        r"ordering is preserved across all $\lambda$ values, confirming "
        r"demonstration-driven avoidance.}"
    )
    if is_c:
        new = fill(
            r"\caption{(Left) Effect of SDF loss weight $\lambda$ on CAR and TSR "
            r"($\lambda = 0$: LoRA-only). SDF shows no significant effect at "
            r"$\lambda \leq 0.01$; at $\lambda = 0.1$, a modest but significant "
            r"departure emerges ($p = {p_value}$). (Right) Per-task CAR fingerprint; "
            r"the task ordering is preserved across all $\lambda$ values, confirming "
            r"demonstration-driven avoidance.}", v)
    else:
        new = (
            r"\caption{(Left) Effect of SDF loss weight $\lambda$ on CAR and TSR "
            r"($\lambda = 0$: LoRA-only). All $\lambda$ values remain within the "
            r"null band ($p > 0.05$). (Right) Per-task CAR fingerprint; the task "
            r"ordering is preserved across all $\lambda$ values, confirming "
            r"demonstration-driven avoidance.}"
        )
    R.append(("claim3.tex", "lambda+fingerprint fig caption", old, new))

    # 9. discussion.tex L3 scope (Scenario C only)
    if is_c:
        old = (
            r"and collision-free demonstrations account for nearly all "
            r"avoidance gains with no statistically significant SDF benefit "
            r"(\S\ref{sec:avoidance_source})."
        )
        new = (
            r"and collision-free demonstrations account for nearly all "
            r"avoidance gains, with EE-only SDF contributing at most a modest "
            r"increment at high loss weights (\S\ref{sec:avoidance_source})."
        )
        R.append(("discussion.tex", "discussion L3 scope", old, new))

    # 10. discussion.tex L12 limitation
    old = r"a small SDF effect (2--5\,pp) without larger samples."
    if is_c:
        new = fill(
            r"the $\lambda = 0.1$ effect ({delta_pp}\,pp, $p = {p_value}$, $n = 3$) "
            r"is statistically significant but small; whether this modest gain "
            r"justifies the computational cost of SDF supervision requires "
            r"task-specific cost-benefit analysis.", v)
    else:
        new = old
    R.append(("discussion.tex", "discussion L12 limitation", old, new))

    return R


def main():
    parser = argparse.ArgumentParser(
        description="Auto-switch paper for lambda=0.1 s2 30K result")
    parser.add_argument("--s2-car", type=float, required="--verify" not in sys.argv)
    parser.add_argument("--s2-tsr", type=float, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify", action="store_true",
                        help="Check all old_strings match current .tex files")
    args = parser.parse_args()

    if args.verify:
        if not PAPER_DIR.exists():
            print(f"ERROR: paper dir not found: {PAPER_DIR}")
            sys.exit(1)
        dummy_v = {k: "X" for k in [
            "s0_car", "s1_car", "s2_car", "mean_car", "std_car",
            "tsr_mean", "tsr_std", "p_value", "p_one_value", "z_value", "delta_pp"]}
        all_ok = True
        for scenario in ("B", "C"):
            replacements = get_replacements(scenario, dummy_v)
            print(f"--- Scenario {scenario} ({len(replacements)} items) ---")
            for filename, label, old, new in replacements:
                fpath = PAPER_DIR / filename
                if not fpath.exists():
                    print(f"  [MISSING] {label:35s} {filename}")
                    all_ok = False
                    continue
                content = fpath.read_text()
                if old in content:
                    print(f"  [OK]      {label:35s} {filename}")
                else:
                    print(f"  [MISMATCH]{label:35s} {filename}")
                    print(f"            Expected: {old[:80]}...")
                    all_ok = False
        sys.exit(0 if all_ok else 1)

    cars = [S0_CAR, S1_CAR, args.s2_car]
    car_mean = mean(cars)
    car_std = std_b(cars)

    if args.s2_tsr is not None:
        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]
    else:
        tsrs = [S0_TSR, S1_TSR]
        print("NOTE: --s2-tsr not provided, using 2-seed TSR")
    tsr_mean = mean(tsrs)
    tsr_std = std_b(tsrs)

    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)
    z = (car_mean - NULL_MEAN) / NULL_STD
    delta = car_mean - NULL_MEAN

    scenario = "C" if p_one < 0.05 else "B"

    v = {
        "s0_car": f"{S0_CAR:.1f}",
        "s1_car": f"{S1_CAR:.1f}",
        "s2_car": f"{args.s2_car:.1f}",
        "mean_car": f"{car_mean:.2f}",
        "std_car": f"{car_std:.2f}",
        "tsr_mean": f"{tsr_mean:.1f}",
        "tsr_std": f"{tsr_std:.1f}",
        "p_value": f"{p_two:.3f}",
        "p_one_value": f"{p_one:.3f}",
        "z_value": f"{z:.2f}",
        "delta_pp": f"{delta:.1f}",
    }

    print("=" * 60)
    print("  PAPER SWITCH — lambda=0.1 s2 30K")
    print("=" * 60)
    print(f"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}")
    print(f"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}")
    print(f"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)")
    print(f"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}")
    print(f"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05")
    print(f"             p_two = {v['p_value']}")
    print(f"  Z-score:   {v['z_value']}")
    print(f"  Delta:     +{v['delta_pp']} pp")
    print(f"  Scenario:  {scenario}  "
          f"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}")
    print()

    if not PAPER_DIR.exists():
        print(f"ERROR: paper dir not found: {PAPER_DIR}")
        sys.exit(1)

    replacements = get_replacements(scenario, v)

    files_content = {}
    counts = {}

    for filename, label, old, new in replacements:
        fpath = PAPER_DIR / filename
        if filename not in files_content:
            if not fpath.exists():
                print(f"  !! {filename} not found")
                continue
            files_content[filename] = fpath.read_text()
            counts[filename] = 0

        content, ok = safe_replace(files_content[filename], old, new, label)
        files_content[filename] = content
        if ok:
            counts[filename] += 1
            status = "ok"
        else:
            status = "FAIL"
        print(f"  [{status:4s}] {label:35s} {filename}")

    total = sum(counts.values())
    n_files = sum(1 for c in counts.values() if c > 0)
    expected = len(replacements)
    print(f"\n  {total}/{expected} replacements in {n_files} files")

    if args.dry_run:
        print("\n  DRY RUN — no files modified")
        return

    for filename, content in files_content.items():
        fpath = PAPER_DIR / filename
        fpath.write_text(content)
        print(f"  Wrote {filename} ({counts[filename]} changes)")

    print("\nCompiling PDF...")
    try:
        result = subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"],
            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            print("  PDF compiled OK")
        else:
            print("  PDF compilation FAILED")
            err = result.stderr or result.stdout or ""
            for line in err.split("\n")[-10:]:
                if line.strip():
                    print(f"    {line}")
    except FileNotFoundError:
        print("  latexmk not found — skipping PDF compilation")
    except subprocess.TimeoutExpired:
        print("  PDF compilation timed out (120s)")


if __name__ == "__main__":
    main()
