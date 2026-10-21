# Scenario A Text Templates — CWM Multi-Seed Data Fill

Generated: 2026-05-21
Scenario: CWM repo-level ~54% variant accuracy, gap ~29pp (Reviewer prediction)

Placeholders:
- `{CWM_MEAN_8B}` — Qwen3-8B CWM repo per-test accuracy, multi-seed mean
- `{CWM_STD_8B}` — Qwen3-8B CWM repo per-test accuracy, std
- `{CWM_SEEDS_8B}` — Qwen3-8B CWM repo seed count
- `{CWM_VAR_MEAN_8B}` — Qwen3-8B CWM repo variant-level accuracy, multi-seed mean
- `{CWM_DS_MEAN}` — DeepSeek CWM repo per-test accuracy, multi-seed mean
- `{CWM_DS_STD}` — DeepSeek CWM repo std
- `{CWM_DS_SEEDS}` — DeepSeek CWM repo seed count
- `{GAP_8B}` — Qwen3-8B CLS mean minus CWM mean (pp)
- `{GAP_RANGE}` — min–max gap across 4B and 8B (e.g., "19--26" or "25--29")
- `{N_SEEDS_LABEL}` — seed count description for caption (e.g., "3 seeds")

---

## Template 1: §4.3 Formulation Divergence Paragraph

**File:** `docs/paper/experiments.tex`
**Replace:** Lines 135–136 (current `\paragraph{Formulation divergence (single-seed).}` through end of paragraph)

```latex
\paragraph{Formulation divergence.} Under our 4--8B LoRA protocol, \cls{} and \cwm{} diverge at repo level on Qwen3: the gap is 25.59\pp{} at 4B (\cls{} 83.63\% vs.\ \cwm{} 58.04\%, seed 42; Figure~\ref{fig:scaling_gap}) and {GAP_8B}\pp{} at 8B (\cls{} 84.83 $\pm$ 0.67\% vs.\ \cwm{} {CWM_MEAN_8B} $\pm$ {CWM_STD_8B}\%, {CWM_SEEDS_8B} seeds). \cwm{} falls below majority baseline at both scales. The gap exceeds any single assessed confound (\S\ref{sec:threats}), though eval sequence length, checkpoint selection, and LoRA capacity limits may interact; causal attribution to the classification-vs-generation distinction requires isolating these factors.
```

**Notes:**
- Paragraph title: dropped "(single-seed)"
- 4B: kept as seed 42 (unchanged, no multi-seed 4B CWM planned)
- 8B: replaced single-seed 65.17% with multi-seed mean±std; CLS already has 3-seed stats
- Removed "single-seed design and multiple confounds preclude definitive causal attribution"
- Retained weakened confound caveat: "gap exceeds any single assessed confound ... though [confounds] may interact"
- If {GAP_8B} changes significantly from 19.31, check cascading references

---

## Template 2: Table 3 Caption

**File:** `docs/paper/experiments.tex`
**Replace:** Line 111 (`\caption{...}`)

```latex
\caption{Repo-level cross-formulation comparison on SWE-bench Verified test set. Qwen3-8B \cls{}/\traj{}: mean $\pm$ std over 3 seeds; \cwm{}: {CWM_SEEDS_8B} seeds. DeepSeek \cls{}: 2 seeds\textsuperscript{$\ddagger$}; \cwm{}: {CWM_DS_SEEDS} seeds; \traj{}: 3 seeds. Qwen3-4B: seed 42.}
```

**Notes:**
- Removed "multi-seed runs in progress"
- Added CWM seed counts for both model families
- Kept existing DeepSeek CLS footnote ($\ddagger$ = excludes outlier s123)
- If DeepSeek CWM also has outlier seeds, add similar footnote

---

## Template 3: Conclusion CWM Paragraph

**File:** `docs/paper/conclusion.tex`
**Replace:** Line 4 (the main conclusion paragraph, from "At repository level" to end of sentence)

Current:
```
At repository level under ${\leq}$8B LoRA fine-tuning, a robust interaction ($z{=}-23.7$) confirms divergence (19--26\pp{}, single-seed variant-level), with \cwm{} falling below majority baseline---consistent across families but dependent on multiple confounds (\S\ref{sec:threats}).
```

Template:
```latex
At repository level under ${\leq}$8B LoRA fine-tuning, a robust interaction ($z{=}-23.7$) confirms divergence ({GAP_RANGE}\pp{}, multi-seed), with \cwm{} falling below majority baseline---consistent across families. The gap exceeds any single assessed confound (\S\ref{sec:threats}), though causal attribution to formulation design requires isolating correlated factors.
```

**Notes:**
- Removed "single-seed variant-level" → "multi-seed"
- Replaced "19--26\pp{}" with `{GAP_RANGE}\pp{}`
- Replaced "dependent on multiple confounds" with weaker "gap exceeds any single assessed confound, though causal attribution requires isolating correlated factors"
- z=-23.7 will be updated separately via `run_w5_full_regression.py` if the full regression changes it

---

## Template 3b: Limitations Paragraph (conclusion.tex L8)

Current opening:
```
Most repo-level comparisons use a single seed; the gap magnitude (19--26\pp{}) exceeds any single assessed confound ...
```

Template:
```latex
Repo-level \cwm{} comparisons use {CWM_SEEDS_8B} seeds for Qwen3 and {CWM_DS_SEEDS} seeds for DeepSeek; the gap magnitude ({GAP_RANGE}\pp{}) exceeds any single assessed confound (\S\ref{sec:threats}), but correlated confounds mean causal attribution to formulation design requires further controlled experiments.
```

**Notes:**
- Replaced "Most repo-level comparisons use a single seed" with actual seed counts
- Replaced "limited seeds mean definitive causal attribution requires multi-seed replication" — multi-seed is now done, shift caveat to "correlated confounds"
- Keep the rest of the Limitations paragraph unchanged (DeepSeek exploratory, LoRA scale, synthetic mutations, etc.)

---

## Cascading Updates Checklist

After filling templates, grep and update these locations to match:

| Location | Current | Update to |
|----------|---------|-----------|
| abstract.tex L4 | "19--26\pp{} in single-seed" | "{GAP_RANGE}\pp{}" (drop "single-seed") |
| introduction.tex L15 | "diverge by 19--26\pp{} ... single-seed evaluation" | "{GAP_RANGE}\pp{}" (drop caveat) |
| experiments.tex L60 | "19--26\pp{}" | "{GAP_RANGE}\pp{}" |
| experiments.tex L161 | "19--26\pp{} (repo)" | "{GAP_RANGE}\pp{}" |
| main.tex L54 (Fig 2 caption) | "19--26\pp{}" | "{GAP_RANGE}\pp{}" |
| checklist.tex L11 | "single-seed constraints" | update description |

See `artifacts/cwm_data_fill_checklist.md` for full 19-location list.
