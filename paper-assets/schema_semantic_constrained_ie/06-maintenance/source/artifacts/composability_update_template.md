# Composability Update Template — DocRED FT Results

> Generated 2026-05-16. Fill placeholders when constrained eval completes.
> **RUNNING experiments:** `w5_qwen_docred_lora_constrained_eval`, `w5_llama_docred_lora_constrained_eval`

---

## Placeholder Legend

| Placeholder | Meaning |
|-------------|---------|
| `{QWEN_DR_S1}` | Qwen DocRED FT+S1 DR% |
| `{QWEN_CF_S1}` | Qwen DocRED FT+S1 CF% |
| `{QWEN_RF1_S1}` | Qwen DocRED FT+S1 R-F1 (x100) |
| `{QWEN_EF1_S1}` | Qwen DocRED FT+S1 E-F1 (x100) |
| `{QWEN_DDR_S1}` | Qwen DocRED FT+S1 relative DR reduction vs FT-U (compute: (0.76-{QWEN_DR_S1})/0.76*100) |
| `{QWEN_PF_S1}` | Qwen DocRED FT+S1 parse_fail_rate% |
| `{LLAMA_DR_S1}` | Llama DocRED FT+S1 DR% |
| `{LLAMA_CF_S1}` | Llama DocRED FT+S1 CF% |
| `{LLAMA_RF1_S1}` | Llama DocRED FT+S1 R-F1 (x100) |
| `{LLAMA_EF1_S1}` | Llama DocRED FT+S1 E-F1 (x100) |
| `{LLAMA_DDR_S1}` | Llama DocRED FT+S1 relative DR reduction vs FT-U (compute: (0.49-{LLAMA_DR_S1})/0.49*100) |
| `{LLAMA_PF_S1}` | Llama DocRED FT+S1 parse_fail_rate% |

## Known Numbers (from registry, fill directly)

| Metric | Qwen FT-U | Llama FT-U |
|--------|-----------|------------|
| DR% | 0.76 | 0.49 |
| RV% | 0.27 | 0.15 |
| ET% | 0 | 0 |
| CF% | 0.12 | **MISSING** (not in registry; likely ~0) |
| R-F1 | 40.86 | 43.72 |
| E-F1 | 82.15 | 83.93 |
| parse_fail% | 7.11 | 2.3 |

> **Action needed:** Llama FT-U CF% not recorded in registry. When constrained eval finishes, also check if the unconstrained eval log has CF. If unavailable, use 0 (consistent with SciERC FT-U pattern where CF=0 for both models).

---

## Update #1 [P0]: Table 5 — Add DocRED block

**File:** `artifacts/_project/paper/section5_scierc_draft.tex`
**Location:** lines 159-199 (table `tab:composability`)

### Current table structure (lines 164-188)

```latex
\begin{tabular}{@{}lll rrrr r@{}}
\toprule
\textbf{Model} & \textbf{Setting} & \textbf{Mode}
  & \textbf{DR\,$\downarrow$} & \textbf{CF}
  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
  & \textbf{$\Delta$DR} \\
\midrule
\multirow{4}{*}{Qwen3-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
\midrule
\multirow{4}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
\bottomrule
\end{tabular}
```

### Target: Add Dataset column + DocRED LoRA block

**Option A (recommended): Add a "Dataset" column, restructure into two panels**

Replace the entire table body (lines 159-199) with:

```latex
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llll rrrr r@{}}
\toprule
\textbf{Dataset} & \textbf{Model} & \textbf{Setting} & \textbf{Mode}
  & \textbf{DR\,$\downarrow$} & \textbf{CF}
  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
  & \textbf{$\Delta$DR} \\
\midrule
\multirow{8}{*}{\rotatebox[origin=c]{90}{SciERC}}
& \multirow{4}{*}{Qwen3-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
& & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
& & \cmidrule(l){3-9}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
& & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
\cmidrule(l){2-9}
& \multirow{4}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
& & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
& & \cmidrule(l){3-9}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
& & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
\midrule
\multirow{4}{*}{\rotatebox[origin=c]{90}{DocRED}}
& \multirow{2}{*}{Qwen3-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.76 & 0.12 & 40.86 & 82.15 & --- \\
& & & Full S1    & {QWEN_DR_S1} & {QWEN_CF_S1} & {QWEN_RF1_S1} & {QWEN_EF1_S1} & $\downarrow${QWEN_DDR_S1}\% \\
\cmidrule(l){2-9}
& \multirow{2}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.49 & 0    & 43.72 & 83.93 & --- \\
& & & Full S1    & {LLAMA_DR_S1} & {LLAMA_CF_S1} & {LLAMA_RF1_S1} & {LLAMA_EF1_S1} & $\downarrow${LLAMA_DDR_S1}\% \\
\bottomrule
\end{tabular}}%
```

> **Note:** DocRED panel only includes LoRA rows (ZS DocRED already in Table cross-model). If ZS DocRED rows are also wanted, replicate from cross-model table data.

**Option B (minimal): Keep current structure, append DocRED LoRA rows after Llama \bottomrule**

Insert before `\bottomrule` (line 188):

```latex
\midrule
\multicolumn{8}{l}{\textit{DocRED (998 documents)}} \\
\midrule
\multirow{2}{*}{Qwen3-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.76 & 0.12 & 40.86 & 82.15 & --- \\
  & & Full S1    & {QWEN_DR_S1} & {QWEN_CF_S1} & {QWEN_RF1_S1} & {QWEN_EF1_S1} & $\downarrow${QWEN_DDR_S1}\% \\
\midrule
\multirow{2}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.49 & 0    & 43.72 & 83.93 & --- \\
  & & Full S1    & {LLAMA_DR_S1} & {LLAMA_CF_S1} & {LLAMA_RF1_S1} & {LLAMA_EF1_S1} & $\downarrow${LLAMA_DDR_S1}\% \\
```

### Caption update (line 190-198)

**Current:**
```latex
\caption{Composability matrix on SciERC (551 documents):
zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
for Qwen3-8B and Llama-3.1-8B.
$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
For both models, fine-tuning alone leaves residual DR (1--2\%);
adding S1 reduces it to $\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp.
F1\,$\times$100.
Evaluation is limited to one dataset and one fine-tuning method (LoRA).}
```

**Target:**
```latex
\caption{Composability matrix on SciERC (551 documents) and DocRED (998 documents):
zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
for Qwen3-8B and Llama-3.1-8B.
$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
Fine-tuning alone leaves residual DR ($\leq$2\%);
adding S1 reduces it to $\leq$\,{MAX_RESIDUAL_DR}\% with R-F1 change within $\pm${MAX_RF1_DELTA}\,pp on both datasets.
F1\,$\times$100.}
```

> `{MAX_RESIDUAL_DR}` = max of (0, 0.09, {QWEN_DR_S1}, {LLAMA_DR_S1})
> `{MAX_RF1_DELTA}` = max absolute R-F1 delta across all FT rows

---

## Update #2 [P0]: Delete "DocRED not reported" from Limitations

**File:** `artifacts/_project/paper/main.tex`
**Location:** line 70

### Current (line 70):
```latex
Composability with fine-tuned models is validated on SciERC with both Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.09\%, R-F1 loss $<$0.1\,pp), but evaluation is limited to one dataset and one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\%) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
```

### Target:
```latex
Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,{MAX_RESIDUAL_DR}\%, R-F1 change within $\pm${MAX_RF1_DELTA}\,pp), though evaluation covers one fine-tuning method (LoRA); residual CF under fine-tuning ({MIN_FT_CF}\%--{MAX_FT_CF}\%) traces to schema-level type ambiguity rather than enforcement failure.
```

> `{MIN_FT_CF}` = min of (0.46, 1.18, {QWEN_CF_S1}, {LLAMA_CF_S1})
> `{MAX_FT_CF}` = max of same set

### Also update line 76:

**Current:**
```latex
Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
```

**Target:**
```latex
Validation with larger scales (70B+) and non-English ontologies remains to be explored.
```

> Remove "fine-tuned models" since now validated on two datasets.

---

## Update #3 [P1]: Composability paragraph — add DocRED evidence

**File:** `artifacts/_project/paper/section5_scierc_draft.tex`
**Location:** lines 125-157

### Current line 127 (experiment scope):
```latex
Table~\ref{tab:composability} presents the composability matrix on SciERC for both Qwen3-8B and Llama-3.1-8B (zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1), testing whether OntoCoDec composes with task-specific fine-tuning across model families.
```

### Target:
```latex
Table~\ref{tab:composability} presents the composability matrix on SciERC and DocRED for both Qwen3-8B and Llama-3.1-8B, testing whether OntoCoDec composes with task-specific fine-tuning across model families and ontology scales.
```

### Insert after line 143 (after Llama SciERC paragraph, before "Across both models"):

```latex

On DocRED, fine-tuning yields even lower baseline violations than SciERC: Qwen DR drops from 18.46\% (zero-shot) to 0.76\%, Llama from 26.07\% to 0.49\%.
% w5_qwen_docred_lora_unconstrained_eval: DR=0.0076, R-F1=0.4086, E-F1=0.8215
% w5_llama_docred_lora_unconstrained_eval: DR=0.0049, R-F1=0.4372, E-F1=0.8393
Adding OntoCoDec reduces DR further (Qwen 0.76\%\,$\to$\,{QWEN_DR_S1}\%, Llama 0.49\%\,$\to$\,{LLAMA_DR_S1}\%) with R-F1 change of {QWEN_RF1_DELTA}\,pp (Qwen) and {LLAMA_RF1_DELTA}\,pp (Llama).
% w5_qwen_docred_lora_constrained_eval: DR={QWEN_DR_S1_RAW}, R-F1={QWEN_RF1_S1_RAW}, E-F1={QWEN_EF1_S1_RAW}
% w5_llama_docred_lora_constrained_eval: DR={LLAMA_DR_S1_RAW}, R-F1={LLAMA_RF1_S1_RAW}, E-F1={LLAMA_EF1_S1_RAW}
```

> `{QWEN_RF1_DELTA}` = {QWEN_RF1_S1} - 40.86, formatted as +/-X.XX
> `{LLAMA_RF1_DELTA}` = {LLAMA_RF1_S1} - 43.72, formatted as +/-X.XX

### Current line 145-146:
```latex
Across both models, fine-tuned + S1 yields DR\,$\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp, consistently validating Claim~3 on SciERC across two model families: fine-tuning and OntoCoDec compose along orthogonal axes---fine-tuning improves extraction quality, OntoCoDec guarantees ontological compliance.
We evaluate on one dataset and one fine-tuning method (LoRA), so we do not claim composability holds universally.
```

### Target:
```latex
Across both models and both datasets, fine-tuned + S1 yields DR\,$\leq$\,{MAX_RESIDUAL_DR}\% with R-F1 change within $\pm${MAX_RF1_DELTA}\,pp, validating Claim~3 across two model families and two ontology scales: fine-tuning and OntoCoDec compose along orthogonal axes---fine-tuning improves extraction quality, OntoCoDec guarantees ontological compliance.
We evaluate with one fine-tuning method (LoRA), so we do not claim composability holds universally across all adaptation methods.
```

### Current line 149 (CF under FT):
```latex
First, CF interference drops substantially under fine-tuning for both models: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp,
```

### Target (append DocRED CF data):
```latex
First, CF interference drops substantially under fine-tuning for both models on SciERC: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp;
on DocRED: Qwen from $+$2.47\,pp to $+${QWEN_CF_DELTA}\,pp, Llama from $+$11.85\,pp to $+${LLAMA_CF_DELTA}\,pp,
```

> `{QWEN_CF_DELTA}` = {QWEN_CF_S1} - 0.12 (DocRED ZS CF: Qwen=0.10→2.57, so delta=2.47; FT: 0.12→{QWEN_CF_S1})
> `{LLAMA_CF_DELTA}` = {LLAMA_CF_S1} - 0 (DocRED ZS CF: Llama=0.17→12.02, so delta=11.85; FT: ~0→{LLAMA_CF_S1})

---

## Update #4 [P1]: Table caption "one dataset" caveat

**File:** `artifacts/_project/paper/section5_scierc_draft.tex`
**Location:** line 197

### Current:
```
Evaluation is limited to one dataset and one fine-tuning method (LoRA).}
```

### Target:
```
Evaluation covers two datasets and one fine-tuning method (LoRA).}
```

(Already covered in Update #1 caption rewrite above — listed separately for checklist tracking.)

---

## Update #5 [P1]: main.tex line 69 — ZS-only claim needs softening

**File:** `artifacts/_project/paper/main.tex`
**Location:** line 69

### Current:
```latex
Results cover two 8B-class models under zero-shot prompting, where relation F1 remains around 8\% compared to $\sim$50\% for fine-tuned systems.
```

### Target:
```latex
Under zero-shot prompting, relation F1 remains around 8\% compared to $\sim$50\% for fine-tuned systems; composability with LoRA fine-tuning is validated on both datasets (Table~\ref{tab:composability}).
```

---

## Update #6 [P2]: Appendix CF-DR trade-off — optional DocRED FT evidence

**File:** `artifacts/_project/paper/appendix_discussion.tex`
**Location:** line 74

### Current:
```latex
(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
```

### Target (if DocRED FT CF is also low):
```latex
(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning reduces CF by 88\% on SciERC (9.90\%\,$\to$\,1.18\%) and by {DOCRED_CF_REDUCTION}\% on DocRED (2.57\%\,$\to$\,{QWEN_CF_S1}\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
```

> `{DOCRED_CF_REDUCTION}` = (2.57 - {QWEN_CF_S1}) / 2.57 * 100 (Qwen ZS S1 CF=2.57)

---

## Derived Quantities Cheat Sheet

When results arrive, compute these before filling the template:

```python
# After loading metrics from registry:
# qwen_s1 = registry["w5_qwen_docred_lora_constrained_eval"]["metrics"]
# llama_s1 = registry["w5_llama_docred_lora_constrained_eval"]["metrics"]

# DR reduction
QWEN_DDR_S1 = round((0.76 - qwen_s1["DR_pct"]) / 0.76 * 100)
LLAMA_DDR_S1 = round((0.49 - llama_s1["DR_pct"]) / 0.49 * 100)

# R-F1 delta
QWEN_RF1_DELTA = round(qwen_s1["R_F1"] - 40.86, 2)  # format as +/-
LLAMA_RF1_DELTA = round(llama_s1["R_F1"] - 43.72, 2)

# E-F1 delta
QWEN_EF1_DELTA = round(qwen_s1["E_F1"] - 82.15, 2)
LLAMA_EF1_DELTA = round(llama_s1["E_F1"] - 83.93, 2)

# CF delta (FT-U → FT-S1)
QWEN_CF_DELTA = round(qwen_s1["CF_pct"] - 0.12, 2)
LLAMA_CF_DELTA = round(llama_s1["CF_pct"] - 0, 2)  # Llama FT-U CF ~0

# Cross-dataset summary stats
MAX_RESIDUAL_DR = max(0, 0.09, qwen_s1["DR_pct"], llama_s1["DR_pct"])
MAX_RF1_DELTA = max(abs(QWEN_RF1_DELTA), abs(LLAMA_RF1_DELTA), 0.09, 0.02)
MIN_FT_CF = min(0.46, 1.18, qwen_s1["CF_pct"], llama_s1["CF_pct"])
MAX_FT_CF = max(0.46, 1.18, qwen_s1["CF_pct"], llama_s1["CF_pct"])
```

---

## Conditional Adjustments

### If DocRED FT DR residual is high (> 0.5%)
- The "no F1 cost" claim in the composability paragraph needs nuance
- Add: "On DocRED, residual DR after FT+S1 ({X}%) is higher than SciERC (0/0.09%), consistent with the tighter ontology ($\bar{\tau}$=0.842) limiting constraint enforcement even after fine-tuning."
- Limitations line 70: change "DR≤X%" to appropriate range

### If DocRED FT DR residual is very low (< 0.1%)
- Strong result — the claim generalizes cleanly
- Consider adding: "Fine-tuning effectively resolves the dual-factor limitation: with near-zero baseline RV, constraint tightness no longer limits DR enforcement."

### If DocRED FT+S1 R-F1 drops significantly (> 0.5pp)
- Cannot claim "zero F1 cost" for DocRED
- Reframe as: "R-F1 cost is modest ({X}pp) and concentrated in..."
- Check per-relation breakdown for explanation

### If DocRED FT+S1 CF is high (> 2%)
- Llama DocRED ZS CF was 12.02%, so FT CF might still be elevated
- Update Limitations CF range accordingly
- Investigate whether CF traces to MISC type (analogous to Generic on SciERC)

---

## File Inventory

| File | Exists | Editable | Updates Needed |
|------|--------|----------|----------------|
| `artifacts/_project/paper/section5_scierc_draft.tex` | YES | YES | #1 (Table 5), #3 (text), #4 (caption) |
| `artifacts/_project/paper/main.tex` | YES | YES | #2 (Limitations L70), #5 (L69) |
| `artifacts/_project/paper/appendix_discussion.tex` | YES | YES | #6 (CF-DR, optional) |
| `artifacts/_project/paper/section5_crossmodel_draft.tex` | YES | ref only | ZS DocRED numbers source |
| `artifacts/_project/paper/paper_tables_draft.tex` | YES | low priority | TBD placeholders (not in main.tex \input) |

## Missing Data Flag

- **Llama DocRED FT-U CF%**: Not in registry (`w5_llama_docred_lora_unconstrained_eval` has no `CF_pct` field). Use 0 unless evaluation log shows otherwise. This affects CF delta computation for Llama DocRED.
