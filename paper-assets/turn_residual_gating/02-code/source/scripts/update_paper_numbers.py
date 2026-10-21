#!/usr/bin/env python3
"""Update hardcoded paper numbers from multi-seed evaluation results.

Usage:
    python scripts/update_paper_numbers.py --summary results.json --dry-run
    python scripts/update_paper_numbers.py --summary results.json --apply
    python scripts/update_paper_numbers.py --results-dir eval_results/ --dry-run

Summary JSON format:
    {
      "tg":     {"tf_gar_ours": [...], "ar_gar_ours": [...], "gap_ratio": [...]},
      "pcgrad": {"tf_gar_ours": [...], "ar_gar_ours": [...], "gap_ratio": [...]},
      "ug":     {"tf_gar_ours": [...], "ar_gar_ours": [...], "gap_ratio": [...]},
      "lo":     {"tf_gar_ours": [...], "ar_gar_ours": [...], "gap_ratio": [...]},
      "base":   {"ar_gar_ours": [...]},
      "ss":     {"tf_gar_ours": [...], "ar_gar_ours": [...], "gap_ratio": [...], "ar_ppl": [...]}
    }

Results-dir format: eval_{condition}_s{seed}.json files, each with at minimum
tf_gar_ours, ar_gar_ours (floats); gap_ratio computed automatically if absent.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
PAPER_DIR = PROJECT_DIR / "paper" / "sections"

TEX_FILES = ["abstract.tex", "introduction.tex", "experiments.tex", "discussion.tex"]


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def mean_std(values):
    a = np.array(values, dtype=float)
    return float(a.mean()), float(a.std(ddof=0))


def fmt_ms(values, f=".3f"):
    """$0.318\\pm0.052$  — omit ±std when it rounds to zero."""
    m, s = mean_std(values)
    if float(f"{s:{f}}") == 0:
        return f"${m:{f}}$"
    return f"${m:{f}}\\pm{s:{f}}$"


def fmt_gap_ms(values, f=".1f"):
    """$25.3\\pm4.2\\times$  — omit ±std when it rounds to zero."""
    m, s = mean_std(values)
    if float(f"{s:{f}}") == 0:
        return f"${m:{f}}\\times$"
    return f"${m:{f}}\\pm{s:{f}}\\times$"


# ---------------------------------------------------------------------------
# Input loaders
# ---------------------------------------------------------------------------

def load_summary(path):
    with open(path) as f:
        return json.load(f)


def load_results_dir(dirpath):
    """Scan eval_{cond}_s{seed}.json or {cond}_s{seed}.json files."""
    summary = defaultdict(lambda: defaultdict(list))
    pat = re.compile(r"(?:eval_)?(\w+?)_s(\d+)\.json$")

    for fpath in sorted(Path(dirpath).glob("*.json")):
        m = pat.search(fpath.name)
        if not m:
            print(f"  [skip] {fpath.name}", file=sys.stderr)
            continue
        cond = m.group(1)
        with open(fpath) as f:
            d = json.load(f)
        for key in ("tf_gar_ours", "ar_gar_ours", "ar_ppl", "gap_ratio",
                     "tf_gar_dongre", "ar_gar_dongre"):
            if key in d:
                summary[cond][key].append(d[key])
        if "gap_ratio" not in d:
            tf = d.get("tf_gar_ours", 0)
            ar = d.get("ar_gar_ours", 0)
            if ar > 0:
                summary[cond]["gap_ratio"].append(tf / ar)
    return dict(summary)


# ---------------------------------------------------------------------------
# Replacement engine
# ---------------------------------------------------------------------------

class Rule:
    def __init__(self, files, old, new, desc, *, use_regex=False):
        self.files = files if isinstance(files, list) else [files]
        self.old = old
        self.new = new
        self.desc = desc
        self.use_regex = use_regex

    def apply(self, filename, content):
        if filename not in self.files:
            return content, 0
        if self.use_regex:
            new_content, n = re.subn(self.old, self.new, content)
        else:
            n = content.count(self.old)
            new_content = content.replace(self.old, self.new) if n > 0 else content
        return new_content, n


def build_rules(data):
    rules = []
    ALL = list(TEX_FILES)
    main_conds = [c for c in ("tg", "pcgrad", "ug", "lo") if c in data]

    # Per-condition means
    ar_means, tf_means = {}, {}
    for c in main_conds:
        v = data[c].get("ar_gar_ours", [])
        if v:
            ar_means[c] = mean_std(v)[0]
        v = data[c].get("tf_gar_ours", [])
        if v:
            tf_means[c] = mean_std(v)[0]

    tg = data.get("tg", {})
    ss = data.get("ss", {})
    tg_ar = tg.get("ar_gar_ours", [])
    tg_tf = tg.get("tf_gar_ours", [])
    tg_gap = tg.get("gap_ratio", [])
    ss_ar = ss.get("ar_gar_ours", [])
    ss_gap = ss.get("gap_ratio", [])
    tg_ar_m = mean_std(tg_ar)[0] if tg_ar else 0.016
    tg_gap_m = mean_std(tg_gap)[0] if tg_gap else 31

    # Files that contain these patterns (not discussion.tex)
    AR_GAP_FILES = ["abstract.tex", "introduction.tex", "experiments.tex"]

    # ── 1. AR GAR range: 0.015--0.025 ────────────────────────────
    if len(ar_means) >= 2:
        lo, hi = min(ar_means.values()), max(ar_means.values())
        new = f"{lo:.3f}--{hi:.3f}"
        if new != "0.015--0.025":
            rules.append(Rule(AR_GAP_FILES, "0.015--0.025", new,
                              f"AR GAR range -> {new}"))

    # ── 2. Gap range: 20--33×  ────────────────────────────────────
    if ar_means:
        gaps = [0.50 / v for v in ar_means.values() if v > 0]
        glo, ghi = int(round(min(gaps))), int(round(max(gaps)))
        old = "20--33$\\times$"
        new = f"{glo}--{ghi}$\\times$"
        if old != new:
            rules.append(Rule(AR_GAP_FILES, old, new,
                              f"Gap range -> {glo}--{ghi}x"))

    # ── 3. TF spread: 0.75\,pp ───────────────────────────────────
    if len(tf_means) >= 2:
        spread = (max(tf_means.values()) - min(tf_means.values())) * 100
        sp = f"{spread:.2f}"
        if sp != "0.75":
            rules.append(Rule(
                ["experiments.tex"],
                "0.75 percentage points (pp)",
                f"{sp} percentage points (pp)",
                f"TF spread -> {sp} pp"))
            rules.append(Rule(
                ["experiments.tex", "introduction.tex"],
                "0.75\\,pp",
                f"{sp}\\,pp",
                f"TF spread -> {sp}\\,pp"))

    # ── 4. SS improvement: 0.016 to 0.318 (20×) ─────────────────
    if ss_ar and ss_gap:
        ss_ar_m = mean_std(ss_ar)[0]
        ss_gap_m = mean_std(ss_gap)[0]
        imp = ss_ar_m / tg_ar_m if tg_ar_m > 0 else 20

        old = "0.016 to 0.318 (20$\\times$)"
        new = f"{tg_ar_m:.3f} to {ss_ar_m:.3f} ({imp:.0f}$\\times$)"
        if old != new:
            rules.append(Rule(
                ["introduction.tex", "discussion.tex"], old, new,
                f"SS before->after -> {new}"))

    # ── 5. SS gap compression: ${{\\sim}}$31$\\times$ gap to 1.57$\\times$ ─
    if ss_gap:
        ss_gap_m = mean_std(ss_gap)[0]
        old = "${\\sim}$31$\\times$ gap to 1.57$\\times$"
        new = f"${{\\sim}}${tg_gap_m:.0f}$\\times$ gap to {ss_gap_m:.2f}$\\times$"
        if old != new:
            rules.append(Rule(
                ["introduction.tex", "discussion.tex"], old, new,
                f"SS gap compression -> ~{tg_gap_m:.0f}x to {ss_gap_m:.2f}x"))

    # ── 6. SS gap compression (no "gap"): from ~31× to 1.57× ────
    if ss_gap:
        ss_gap_m = mean_std(ss_gap)[0]
        old = "${\\sim}$31$\\times$ to 1.57$\\times$"
        new = f"${{\\sim}}${tg_gap_m:.0f}$\\times$ to {ss_gap_m:.2f}$\\times$"
        if old != new:
            rules.append(Rule(
                ["introduction.tex"], old, new,
                f"SS gap compression (alt) -> ~{tg_gap_m:.0f}x to {ss_gap_m:.2f}x"))

    # ── 7. Abstract standalone: 1.57$\\times$ ────────────────────
    if ss_gap:
        ss_gap_m = mean_std(ss_gap)[0]
        old = "1.57$\\times$"
        new = f"{ss_gap_m:.2f}$\\times$"
        if old != new:
            rules.append(Rule(
                ["abstract.tex"], old, new,
                f"Abstract SS gap -> {ss_gap_m:.2f}x"))

    # ── 8. Discussion: second seed sentence ──────────────────────
    if ss_ar and ss_gap and len(ss_ar) >= 2:
        n = len(ss_ar)
        old = ("A second seed yields AR GAR\\,=\\,0.418 "
               "(gap 1.20$\\times$); systematic ablation is deferred.")
        new = (f"Across {n} seeds, AR GAR\\,=\\,{fmt_ms(ss_ar)} "
               f"(gap {fmt_gap_ms(ss_gap, '.2f')}).")
        rules.append(Rule(
            ["discussion.tex"], old, new,
            f"Discussion: 2nd seed -> {n}-seed mean+/-std"))

    # ── 9. (single seed) → (N seeds) ─────────────────────────────
    if ss_gap and len(ss_gap) >= 2:
        n = len(ss_gap)
        rules.append(Rule(
            ["abstract.tex", "introduction.tex", "discussion.tex"],
            "(single seed)",
            f"({n} seeds)",
            f"(single seed) -> ({n} seeds)"))
        rules.append(Rule(
            ["introduction.tex"],
            "(single seed;",
            f"({n} seeds;",
            f"(single seed; -> ({n} seeds;"))

    # ── 10. TG multi-seed: TF GAR mean±std ───────────────────────
    if tg_tf and len(tg_tf) >= 2:
        old = "$0.504\\pm0.001$"
        new = fmt_ms(tg_tf)
        if old != new:
            rules.append(Rule(
                ["experiments.tex"], old, new,
                f"TG TF GAR -> {new}"))

    # ── 11. TG multi-seed: AR GAR mean±std ───────────────────────
    if tg_ar and len(tg_ar) >= 2:
        old = "$0.016\\pm0.001$"
        new = fmt_ms(tg_ar)
        if old != new:
            rules.append(Rule(
                ["experiments.tex"], old, new,
                f"TG AR GAR -> {new}"))

    # ── 12. TG multi-seed: gap range ─────────────────────────────
    if tg_gap and len(tg_gap) >= 2:
        m, _ = mean_std(tg_gap)
        lo, hi = min(tg_gap), max(tg_gap)
        old = "${\\sim}$31$\\times$ (range 30.5--32.1$\\times$)"
        new = (f"${{\\sim}}${m:.0f}$\\times$ "
               f"(range {lo:.1f}--{hi:.1f}$\\times$)")
        if old != new:
            rules.append(Rule(
                ["experiments.tex"], old, new,
                f"TG gap -> ~{m:.0f}x ({lo:.1f}--{hi:.1f})"))

    # ── 13. Table 1 AR column values (regex) ─────────────────────
    old_ar = {
        "base": "0.012", "tg": "0.016", "pcgrad": "0.015",
        "ug": "0.015", "lo": "0.025",
    }
    row_re = {
        "base":   r"(Base\s+&.*&\s*)0\.012(\s*\\\\)",
        "tg":     r"(ThreadGate\s+&.*&\s*)0\.016(\s*\\\\)",
        "pcgrad": r"(\\;\+\\,PCGrad\s+&.*&\s*)0\.015(\s*\\\\)",
        "ug":     r"(Uniform\s+Gate\s+&.*&\s*)0\.015(\s*\\\\)",
        "lo":     r"(LoRA-only\s+&.*&\s*)\\textbf\{0\.025\}(\s*\\\\)",
    }
    for cond in ["base"] + list(main_conds):
        vals = data.get(cond, {}).get("ar_gar_ours", [])
        if not vals:
            continue
        new_v = f"{mean_std(vals)[0]:.3f}"
        if new_v == old_ar.get(cond):
            continue
        pat = row_re.get(cond)
        if not pat:
            continue
        if cond == "lo":
            repl = rf"\g<1>\\textbf{{{new_v}}}\g<2>"
        else:
            repl = rf"\g<1>{new_v}\g<2>"
        rules.append(Rule(
            ["experiments.tex"], pat, repl,
            f"Table 1 {cond} AR -> {new_v}", use_regex=True))

    # ── 14. Table caption: N=5 → N=50 ────────────────────────────
    old_n = "$N$\\,=\\,5 ten-turn generated"
    new_n = "$N$\\,=\\,50"
    rules.append(Rule(
        ["experiments.tex"], old_n, new_n,
        "Table caption: N=5 ten-turn -> N=50"))

    return rules


# ---------------------------------------------------------------------------
# Apply
# ---------------------------------------------------------------------------

def apply_rules(rules, paper_dir, dry_run=True):
    files_needed = set()
    for r in rules:
        files_needed.update(r.files)

    total_applied = 0
    matched_log = []
    unmatched_log = []

    for fname in sorted(files_needed):
        fpath = paper_dir / fname
        if not fpath.exists():
            print(f"  [warn] {fname} not found", file=sys.stderr)
            continue

        content = fpath.read_text()
        original = content

        for rule in rules:
            if fname not in rule.files:
                continue
            content, n = rule.apply(fname, content)
            if n > 0:
                total_applied += n
                matched_log.append(f"  [OK]   {fname}: {rule.desc} ({n}x)")
            else:
                unmatched_log.append(f"  [MISS] {fname}: {rule.desc}")

        if content != original:
            if dry_run:
                print(f"  {fname}: changes pending (dry-run)")
            else:
                fpath.write_text(content)
                print(f"  {fname}: UPDATED")
        else:
            print(f"  {fname}: no changes")

    print()
    for line in matched_log:
        print(line)
    if unmatched_log:
        print()
        for line in unmatched_log:
            print(line)

    return total_applied


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(
        description="Update hardcoded paper numbers from multi-seed eval results.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--summary", help="Path to summary JSON file")
    g.add_argument("--results-dir", help="Dir with eval_{cond}_s{seed}.json files")
    p.add_argument("--paper-dir", default=str(PAPER_DIR),
                   help=f"Paper sections directory (default: {PAPER_DIR})")
    m = p.add_mutually_exclusive_group()
    m.add_argument("--dry-run", action="store_true", default=True,
                   help="Print changes without writing (default)")
    m.add_argument("--apply", action="store_true",
                   help="Apply changes to .tex files")
    args = p.parse_args()

    if args.apply:
        args.dry_run = False

    paper_dir = Path(args.paper_dir)
    if not paper_dir.exists():
        print(f"Error: {paper_dir} not found", file=sys.stderr)
        sys.exit(1)

    # Load data
    if args.summary:
        data = load_summary(args.summary)
        print(f"Loaded: {args.summary}")
    else:
        data = load_results_dir(args.results_dir)
        print(f"Loaded: {args.results_dir}")

    # Print summary
    print(f"Conditions: {', '.join(sorted(data.keys()))}")
    for cond in sorted(data.keys()):
        metrics = data[cond]
        parts = []
        for k in sorted(metrics.keys()):
            v = metrics[k]
            if isinstance(v, list) and v:
                m, s = mean_std(v)
                parts.append(f"{k}={m:.4f}+/-{s:.4f}(n={len(v)})")
        if parts:
            print(f"  {cond}: {', '.join(parts)}")

    # Build rules
    rules = build_rules(data)
    n_rules = sum(len(r.files) for r in rules)
    print(f"\n{len(rules)} rules -> {n_rules} file-level replacements")

    # Apply
    mode = "DRY RUN" if args.dry_run else "APPLYING"
    print(f"\n{'='*60}\n  {mode}\n{'='*60}\n")

    applied = apply_rules(rules, paper_dir, dry_run=args.dry_run)

    print(f"\n{'='*60}")
    print(f"  {applied} replacements applied")
    if args.dry_run:
        print(f"  (dry-run -- no files written)")
        print(f"  Run with --apply to write changes")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
