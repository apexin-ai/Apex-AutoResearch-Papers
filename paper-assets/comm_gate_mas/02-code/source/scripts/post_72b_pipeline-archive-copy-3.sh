#!/usr/bin/env bash
# Post-72B completion pipeline: fill macros → compile PDF → guardrail check.
# Run from project root after oracle_qwen72b_n500 finishes.
#
# Usage:
#   bash scripts/post_72b_pipeline.sh
#   bash scripts/post_72b_pipeline.sh --dry-run   # preview without writing

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

SEED_JSON="outputs/oracle_qwen72b_n500/seed_42.json"
MACRO_TEX="artifacts/paper/72b_macros.tex"
PAPER_DIR="artifacts/paper"
DRY_RUN=""

if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN="--dry-run"
    echo "=== DRY RUN MODE ==="
fi

echo "============================================================"
echo "  Post-72B Pipeline"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================================"

# --- Step 1: Check seed_42.json exists ---
echo ""
echo "[1/6] Checking experiment output..."
if [[ ! -f "$SEED_JSON" ]]; then
    echo "ERROR: $SEED_JSON not found. Is the experiment finished?"
    exit 1
fi
echo "  Found: $SEED_JSON ($(wc -c < "$SEED_JSON") bytes)"

# --- Step 2: Fill macros ---
echo ""
echo "[2/6] Filling 72B LaTeX macros..."
python src/fill_72b_macros.py "$SEED_JSON" $DRY_RUN
FILL_EXIT=$?
if [[ $FILL_EXIT -ne 0 ]]; then
    echo "ERROR: fill_72b_macros.py failed (exit $FILL_EXIT)"
    exit 1
fi

# --- Step 3: Verify macro file and add \input if needed ---
echo ""
echo "[3/6] Verifying macro integration..."
if [[ -z "$DRY_RUN" ]]; then
    if [[ ! -f "$MACRO_TEX" ]]; then
        echo "ERROR: $MACRO_TEX was not created"
        exit 1
    fi
    echo "  Macro file: $MACRO_TEX"
    cat "$MACRO_TEX"

    # Check if main.tex already has \input{72b_macros}
    if grep -q '\\input{72b_macros}' "$PAPER_DIR/main.tex"; then
        echo "  main.tex already includes \\input{72b_macros}"
    else
        echo "  Adding \\input{72b_macros} to main.tex after placeholder block..."
        sed -i.bak '/^\\newcommand{\\qwenSevenTwoBN}/a\
\\input{72b_macros}' "$PAPER_DIR/main.tex"
        rm -f "$PAPER_DIR/main.tex.bak"
        echo "  Done. \\input{72b_macros} added."
    fi
else
    echo "  [dry-run] Skipping file verification"
fi

# --- Step 4: Compile PDF ---
echo ""
echo "[4/6] Compiling PDF with tectonic..."
if [[ -z "$DRY_RUN" ]]; then
    cd "$PAPER_DIR"
    TECTONIC_OUT=$(tectonic main.tex 2>&1) || true
    cd "$PROJECT_ROOT"

    if [[ -f "$PAPER_DIR/main.pdf" ]]; then
        echo "  Compilation: PASS"
        PDF_SIZE=$(wc -c < "$PAPER_DIR/main.pdf")
        echo "  PDF size: $PDF_SIZE bytes"
    else
        echo "  Compilation: FAIL"
        echo "$TECTONIC_OUT"
        exit 1
    fi

    # Check for errors in output
    if echo "$TECTONIC_OUT" | grep -qi "error"; then
        echo "  WARNING: tectonic reported errors:"
        echo "$TECTONIC_OUT" | grep -i "error"
    fi
else
    echo "  [dry-run] Skipping compilation"
fi

# --- Step 5: Check page count ---
echo ""
echo "[5/6] Checking page count..."
if [[ -z "$DRY_RUN" ]] && [[ -f "$PAPER_DIR/main.pdf" ]]; then
    PAGE_COUNT=$(python -c "
try:
    import subprocess
    r = subprocess.run(['pdfinfo', '$PAPER_DIR/main.pdf'], capture_output=True, text=True)
    for line in r.stdout.splitlines():
        if line.startswith('Pages:'):
            print(line.split(':')[1].strip())
            break
except Exception:
    # Fallback: use PyPDF2 or count via strings
    import struct, re
    with open('$PAPER_DIR/main.pdf', 'rb') as f:
        content = f.read()
    # Count /Type /Page entries (rough estimate)
    pages = len(re.findall(rb'/Type\s*/Page[^s]', content))
    print(pages)
" 2>/dev/null || echo "UNKNOWN")

    echo "  Total pages: $PAGE_COUNT"

    # NeurIPS: 9 pages main body (references + appendix unlimited)
    # We can't easily detect where main body ends from page count alone
    if [[ "$PAGE_COUNT" != "UNKNOWN" ]] && [[ "$PAGE_COUNT" -gt 50 ]]; then
        echo "  WARNING: Unusually high page count. Check for compilation issues."
    fi
    echo "  Note: Verify main body ≤ 9 pages manually (references start on page 10)."
else
    echo "  [dry-run] Skipping page check"
fi

# --- Step 6: Guardrail summary ---
echo ""
echo "[6/6] 72B Statistical Summary"
echo "============================================================"
if [[ -f "$SEED_JSON" ]]; then
    python -c "
import json
data = json.load(open('$SEED_JSON'))
n = data['num_tasks'] - data.get('num_skipped', 0)
bl = data['baseline']['correct'] / n * 100
pr = data['oracle_pruned']['correct'] / n * 100
delta = pr - bl
p = data['mcnemar']['p_value']
supp = data['oracle_pruned']['suppression_rate']
b = data['mcnemar']['b_oracle_only']
c = data['mcnemar']['c_baseline_only']

import math
if b + c > 0:
    se = math.sqrt((b + c - (b - c)**2 / n)) / n
    ci_lo, ci_hi = (delta/100 - 1.96 * se) * 100, (delta/100 + 1.96 * se) * 100
else:
    ci_lo = ci_hi = 0.0

sign = '+' if delta >= 0 else ''
print(f'  Model:      Qwen2.5-72B-Instruct-AWQ')
print(f'  Dataset:    GSM8K (N={n})')
print(f'  Baseline:   {bl:.1f}%')
print(f'  Pruned:     {pr:.1f}%')
print(f'  Delta:      {sign}{delta:.1f} pp')
print(f'  95% CI:     [{ci_lo:+.1f}, {ci_hi:+.1f}] pp')
print(f'  McNemar p:  {p:.4f}')
print(f'  Suppression:{supp:.1f}%')
print(f'  Skipped:    {data.get(\"num_skipped\", 0)}')
print()
if abs(delta) <= 3.0 and p >= 0.1:
    print('  *** SCENARIO A: Safe to fill macros. Scale-invariant framing holds. ***')
else:
    reasons = []
    if abs(delta) > 3.0: reasons.append(f'|Delta|={abs(delta):.1f}pp > 3pp')
    if p < 0.1: reasons.append(f'p={p:.3f} < 0.1')
    print(f'  *** SCENARIO B (CONTINGENCY-B): {\", \".join(reasons)} ***')
    print(f'  *** Must activate CONTINGENCY-B narrative rewrite before submission! ***')
"
fi
echo "============================================================"
echo "Done. Review the summary above before submitting."
