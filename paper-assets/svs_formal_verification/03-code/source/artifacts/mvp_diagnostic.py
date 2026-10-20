#!/usr/bin/env python3
"""MVP diagnostic analysis for SVS formal verification (mvp_003)."""

import json
import math
import sys
from collections import defaultdict
from datetime import datetime

import numpy as np
from scipy import stats


def load_data(path):
    with open(path) as f:
        return json.load(f)


def all_chains(data):
    chains = []
    for p in data:
        gold = p["gold_label"]
        for cv in p["chain_verifications"]:
            cv["_gold"] = gold
            cv["_correct_svs"] = p["correct_svs"]
            cv["_correct_sc"] = p["correct_sc"]
            cv["_chain_correct"] = (cv["answer"] == gold)
            cv["_frate"] = cv["formalized_claims"] / cv["total_claims"] if cv["total_claims"] > 0 else 0.0
            chains.append(cv)
    return chains


def fmt(v, prec=4):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "N/A"
    return f"{v:.{prec}f}"


def ic_stats(ic_values):
    if not ic_values:
        return {"count": 0, "mean": float("nan"), "std": float("nan"),
                "median": float("nan"), "min": float("nan"), "max": float("nan")}
    a = np.array(ic_values)
    return {"count": len(a), "mean": float(np.mean(a)), "std": float(np.std(a, ddof=1)) if len(a) > 1 else 0.0,
            "median": float(np.median(a)), "min": float(np.min(a)), "max": float(np.max(a))}


# ---------- Section 1: Per-label IC distribution ----------

def section1(chains):
    by_label = defaultdict(list)
    for c in chains:
        by_label[c["answer"]].append(c["ic_score"])
    rows = []
    for label in ["True", "False", "Unknown"]:
        s = ic_stats(by_label.get(label, []))
        rows.append((label, s))
    return rows


def print_section1(rows):
    print("\n--- 1. Per-Label IC Distribution ---")
    print(f"{'Label':<9}| {'Count':>5} | {'IC Mean ± Std':>16} | {'Median':>7} | {'Min':>6} | {'Max':>6}")
    print("-" * 68)
    for label, s in rows:
        if s["count"] == 0:
            print(f"{label:<9}| {'0':>5} |  (no chains)")
        else:
            print(f"{label:<9}| {s['count']:>5} | {fmt(s['mean'])} ± {fmt(s['std'])} | {fmt(s['median'])} | {fmt(s['min'])} | {fmt(s['max'])}")


# ---------- Section 2: Formalization rate by label ----------

def section2(chains):
    by_label = defaultdict(list)
    for c in chains:
        by_label[c["answer"]].append(c["_frate"])
    rows = []
    for label in ["True", "False", "Unknown"]:
        vals = by_label.get(label, [])
        if vals:
            a = np.array(vals)
            rows.append((label, len(a), float(np.mean(a)), float(np.std(a, ddof=1)) if len(a) > 1 else 0.0))
        else:
            rows.append((label, 0, float("nan"), float("nan")))
    return rows


def print_section2(rows):
    print("\n--- 2. Formalization Rate by Label ---")
    print(f"{'Label':<9}| {'Count':>5} | {'FRate Mean ± Std':>20}")
    print("-" * 42)
    for label, n, mean, std in rows:
        if n == 0:
            print(f"{label:<9}| {'0':>5} |  (no chains)")
        else:
            print(f"{label:<9}| {n:>5} | {fmt(mean)} ± {fmt(std)}")


# ---------- Section 3: IC vs correctness (P2) ----------

def cohens_d_bootstrap(correct_ic, wrong_ic, n_boot=5000):
    rng = np.random.default_rng(42)
    c = np.array(correct_ic)
    w = np.array(wrong_ic)
    nc, nw = len(c), len(w)
    if nc < 2 or nw < 2:
        return float("nan"), (float("nan"), float("nan"))

    def _d(a, b):
        na, nb = len(a), len(b)
        pooled = math.sqrt(((na - 1) * np.var(a, ddof=1) + (nb - 1) * np.var(b, ddof=1)) / (na + nb - 2))
        if pooled == 0:
            return 0.0
        return (np.mean(a) - np.mean(b)) / pooled

    obs_d = _d(c, w)
    boot_ds = []
    for _ in range(n_boot):
        bc = rng.choice(c, size=nc, replace=True)
        bw = rng.choice(w, size=nw, replace=True)
        boot_ds.append(_d(bc, bw))
    boot_ds = np.array(boot_ds)
    ci_lo = float(np.percentile(boot_ds, 2.5))
    ci_hi = float(np.percentile(boot_ds, 97.5))
    return float(obs_d), (ci_lo, ci_hi)


def section3(chains):
    correct_ic = [c["ic_score"] for c in chains if c["_chain_correct"]]
    wrong_ic = [c["ic_score"] for c in chains if not c["_chain_correct"]]
    d, ci = cohens_d_bootstrap(correct_ic, wrong_ic)
    cs = ic_stats(correct_ic)
    ws = ic_stats(wrong_ic)
    p2_pass = (not math.isnan(d)) and d > 0.15 and ci[0] > 0
    return cs, ws, d, ci, p2_pass


def print_section3(cs, ws, d, ci, p2_pass):
    print("\n--- 3. P2: IC vs Correctness ---")
    print(f"Correct chains: N={cs['count']}, IC={fmt(cs['mean'])} ± {fmt(cs['std'])}")
    print(f"Wrong chains:   N={ws['count']}, IC={fmt(ws['mean'])} ± {fmt(ws['std'])}")
    print(f"Cohen's d = {fmt(d)} [95% CI: {fmt(ci[0])}, {fmt(ci[1])}]")
    print(f"P2 {'PASS' if p2_pass else 'FAIL'}: d > 0.15 and 95% CI excludes 0")


# ---------- Section 4: Cross table label × correctness × IC ----------

def section4(chains):
    table = {}
    for label in ["True", "False", "Unknown"]:
        for correct in [True, False]:
            key = (label, correct)
            vals = [c["ic_score"] for c in chains if c["answer"] == label and c["_chain_correct"] == correct]
            table[key] = ic_stats(vals)
    return table


def print_section4(table):
    print("\n--- 4. Cross Table: Label × Correctness × IC ---")
    print(f"{'Label':<9}| {'Correct':>7} | {'Count':>5} | {'IC Mean ± Std':>16}")
    print("-" * 52)
    for label in ["True", "False", "Unknown"]:
        for correct in [True, False]:
            s = table[(label, correct)]
            tag = "yes" if correct else "no"
            if s["count"] == 0:
                print(f"{label:<9}| {tag:>7} | {'0':>5} |  -")
            else:
                print(f"{label:<9}| {tag:>7} | {s['count']:>5} | {fmt(s['mean'])} ± {fmt(s['std'])}")

    t_wrong = table[("True", False)]
    u_correct = table[("Unknown", True)]
    if t_wrong["count"] > 0 and u_correct["count"] > 0 and not math.isnan(t_wrong["mean"]) and not math.isnan(u_correct["mean"]):
        if t_wrong["mean"] > u_correct["mean"]:
            print("  ⚠ IC(True,wrong) > IC(Unknown,correct): IC may be a label proxy, not correctness signal")
        else:
            print("  ✓ IC(Unknown,correct) ≥ IC(True,wrong): IC tracks correctness, not just label")


# ---------- Section 5: IC inversion cases ----------

def section5(data):
    inversions = [p for p in data if not p["correct_svs"] and p["correct_sc"]]
    return inversions


def print_section5(inversions):
    print(f"\n--- 5. IC Inversion Cases (SVS wrong, SC right): {len(inversions)} ---")
    if not inversions:
        print("  (none)")
        return
    for p in inversions:
        print(f"\n  Problem: {p['problem_id']}")
        print(f"  Gold={p['gold_label']}, SVS={p['selected_answer']}, SC={p['sc_answer']}")
        print(f"  Group scores: {json.dumps({k: round(v, 4) for k, v in p['group_scores'].items()})}")
        by_ans = defaultdict(list)
        for cv in p["chain_verifications"]:
            by_ans[cv["answer"]].append(cv["ic_score"])
        for ans, ics in by_ans.items():
            a = np.array(ics)
            tag = " ← gold" if ans == p["gold_label"] else ""
            print(f"    answer={ans}{tag}: N={len(a)}, IC={np.mean(a):.4f}±{np.std(a, ddof=1):.4f}" if len(a) > 1
                  else f"    answer={ans}{tag}: N=1, IC={a[0]:.4f}")


# ---------- Section 6: FC weight sensitivity ----------

def recompute_svs(data, ic_w, fc_w, cclc_lambda=0.3):
    correct = 0
    for p in data:
        by_answer = defaultdict(list)
        for cv in p["chain_verifications"]:
            cs = ic_w * cv["ic_score"] + fc_w * cv["fc_score"]
            by_answer[cv["answer"]].append(cs)

        # estimate cclc contribution from original data
        orig_by_answer = defaultdict(list)
        for cv in p["chain_verifications"]:
            orig_cs = 0.5 * cv["ic_score"] + 0.5 * cv["fc_score"]
            orig_by_answer[cv["answer"]].append(orig_cs)

        new_group_scores = {}
        for ans, scores in by_answer.items():
            new_mean = sum(scores) / len(scores)
            # back-calculate cclc contribution from original group_score
            if ans in p["group_scores"] and ans in orig_by_answer:
                orig_mean = sum(orig_by_answer[ans]) / len(orig_by_answer[ans])
                cclc_contrib = p["group_scores"][ans] - orig_mean
            else:
                cclc_contrib = 0.0
            new_group_scores[ans] = new_mean + cclc_contrib

        best = max(new_group_scores, key=new_group_scores.get)
        if best == p["gold_label"]:
            correct += 1
    return correct / len(data) if data else 0.0


def section6(data):
    sc_acc = sum(p["correct_sc"] for p in data) / len(data) if data else 0.0
    configs = [
        ("0.0 (pure IC)", 1.0, 0.0),
        ("0.5 (default)", 0.5, 0.5),
        ("1.0 (pure FC)", 0.0, 1.0),
    ]
    rows = []
    for label, ic_w, fc_w in configs:
        acc = recompute_svs(data, ic_w, fc_w)
        rows.append((label, acc, acc - sc_acc))
    return rows, sc_acc


def print_section6(rows, sc_acc):
    print("\n--- 6. FC Weight Sensitivity ---")
    print(f"SC baseline accuracy: {fmt(sc_acc)}")
    print(f"{'fc_weight':<16}| {'SVS Accuracy':>12} | {'Δ vs SC':>8}")
    print("-" * 42)
    for label, acc, delta in rows:
        print(f"{label:<16}| {fmt(acc):>12} | {'+' if delta >= 0 else ''}{fmt(delta):>7}")


# ---------- Section 7: All-SAT proportion ----------

def section7(chains):
    total = len(chains)
    all_sat = [c for c in chains if c["ic_score"] == 1.0]
    n_sat = len(all_sat)
    by_label = defaultdict(lambda: [0, 0])  # [all_sat_count, total_count]
    for c in chains:
        by_label[c["answer"]][1] += 1
        if c["ic_score"] == 1.0:
            by_label[c["answer"]][0] += 1
    return n_sat, total, dict(by_label)


def print_section7(n_sat, total, by_label):
    print("\n--- 7. All-SAT Proportion ---")
    pct = n_sat / total * 100 if total > 0 else 0
    print(f"All-SAT chains: {n_sat}/{total} ({pct:.1f}%)")
    print(f"{'Label':<9}| {'All-SAT':>7} | {'Total':>5} | {'Pct':>6}")
    print("-" * 36)
    for label in ["True", "False", "Unknown"]:
        if label in by_label:
            s, t = by_label[label]
            p = s / t * 100 if t > 0 else 0
            print(f"{label:<9}| {s:>7} | {t:>5} | {p:>5.1f}%")
        else:
            print(f"{label:<9}|       0 |     0 |     -")
    if n_sat == total:
        print("  ⚠ All chains are SAT — PCV provides no discrimination")
    elif n_sat / total > 0.8 if total > 0 else False:
        print(f"  ⚠ {pct:.0f}% all-SAT — PCV discrimination is weak")


# ---------- Summary ----------

def build_summary(s1, s3_d, s3_pass, inversions, s6_rows, n_sat, total_chains):
    findings = []

    # P2 result
    if s3_pass:
        findings.append(f"P2 PASS: Cohen's d = {fmt(s3_d)}, IC distinguishes correct from wrong chains")
    else:
        findings.append(f"P2 FAIL: Cohen's d = {fmt(s3_d)}, IC does NOT reliably distinguish correctness")

    # IC inversion
    findings.append(f"{len(inversions)} IC inversion cases (SVS wrong, SC right)")

    # All-SAT
    sat_pct = n_sat / total_chains * 100 if total_chains > 0 else 0
    findings.append(f"All-SAT rate: {n_sat}/{total_chains} ({sat_pct:.1f}%)")

    # Best fc weight
    best = max(s6_rows, key=lambda x: x[1])
    findings.append(f"Best weight config: fc_weight={best[0]}, accuracy={fmt(best[1])}")

    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python mvp_diagnostic.py <results.json>")
        sys.exit(1)

    path = sys.argv[1]
    data = load_data(path)
    chains = all_chains(data)

    n_problems = len(data)
    n_chains = len(chains)

    print(f"=== SVS MVP Diagnostic Report ===")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Input: {path} ({n_problems} problems, {n_chains} chains)")

    s1 = section1(chains)
    print_section1(s1)

    s2 = section2(chains)
    print_section2(s2)

    cs, ws, d, ci, p2_pass = section3(chains)
    print_section3(cs, ws, d, ci, p2_pass)

    s4 = section4(chains)
    print_section4(s4)

    inversions = section5(data)
    print_section5(inversions)

    s6_rows, sc_acc = section6(data)
    print_section6(s6_rows, sc_acc)

    n_sat, total, by_label = section7(chains)
    print_section7(n_sat, total, by_label)

    findings = build_summary(s1, d, p2_pass, inversions, s6_rows, n_sat, n_chains)
    print("\n=== Summary ===")
    for i, f in enumerate(findings, 1):
        print(f"Key finding {i}: {f}")

    # write JSON report
    report = {
        "date": datetime.now().isoformat(),
        "input_path": path,
        "n_problems": n_problems,
        "n_chains": n_chains,
        "section1_per_label_ic": {label: s for label, s in s1},
        "section2_frate_by_label": {label: {"count": n, "mean": mean, "std": std} for label, n, mean, std in s2},
        "section3_p2": {
            "correct_ic": cs, "wrong_ic": ws,
            "cohens_d": d, "ci_95": list(ci), "p2_pass": p2_pass,
        },
        "section4_cross_table": {f"{label}_{('correct' if correct else 'wrong')}": s for (label, correct), s in s4.items()},
        "section5_inversions": [
            {"problem_id": p["problem_id"], "gold": p["gold_label"],
             "svs": p["selected_answer"], "sc": p["sc_answer"],
             "group_scores": p["group_scores"]}
            for p in inversions
        ],
        "section6_fc_sensitivity": [{"config": label, "accuracy": acc, "delta_vs_sc": delta} for label, acc, delta in s6_rows],
        "section7_all_sat": {"n_sat": n_sat, "total": total, "by_label": by_label},
        "summary": findings,
    }

    out_path = "/root/outputs/mvp_diagnostic_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nFull report written to {out_path}")


if __name__ == "__main__":
    main()
