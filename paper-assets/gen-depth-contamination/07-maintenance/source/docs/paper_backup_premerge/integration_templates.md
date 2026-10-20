# Integration Templates: exp-004 & exp-012

Created: 2026-05-15. Fill [PLACEHOLDER] when results arrive.

---

## 1. exp-004 (7B Cross-Scale) Integration

### 1.1 Registry: exp_004_7b_crossscale (RUNNING)
- Config: Qwen2.5-7B continuation, C4 5K seeds, depth 0-5, scorer=Qwen2.5-1.5B
- Expected output: pairwise AUC per depth pair + bootstrap CI + K*

### 1.2 "≤1.5B" Qualifier Locations (6 sites)

| # | File | Line | Current Text | Scenario A (K*=2) | Scenario B (K*≠2) |
|---|------|------|-------------|-------------------|-------------------|
| 1 | `main.tex` (Abstract) | L36 | `(${\leq}1.5$B scale)` | `($1.5$--$7$B scale)` | keep `(${\leq}1.5$B scale)` |
| 2 | `introduction.tex` | L22 | `at ${\leq}$1.5B scale` | `at $1.5$--$7$B scale` | keep as-is |
| 3 | `main.tex` (Limitations) | L66 | `(1)~model scale ($\leq$1.5B)` | `(1)~model scale ($\leq$7B; tested at 1.5B and 7B)` | keep as-is |
| 4 | `appendix_extended.tex` | L7 | `at the $\leq$1.5B scale` | `at the $\leq$7B scale` | keep as-is |
| 5 | `appendix_extended.tex` | L52 | `Our $\Kempirical = 2$ at $\leq$1.5B` | `Our $\Kempirical = 2$ at $\leq$7B` | keep as-is |
| 6 | `conclusion.tex` | L11 | `scaling to 7B+ models` | `scaling beyond 7B` | keep as-is |

### 1.3 Table 1 (tab:kstar_ci) — Add Qwen-7B Column

File: `experiments_c1.tex` L12-32

**Scenario A (K*=2 confirmed):**
```latex
% Add after \multicolumn{2}{c}{Qwen-cont} in header:
& \multicolumn{2}{c}{Qwen-7B} \\
% Add \cmidrule(lr){10-11}

% Data rows — fill from registry:
0v1 & ... & & ... & & ... & & ... & & [PLACEHOLDER] & \\
1v2 & ... & & ... & & ... & & ... & & [PLACEHOLDER] & [PLACEHOLDER]\rlap{$^*$} \\
2v3 & ... & & ... & & ... & & ... & & [PLACEHOLDER] & [PLACEHOLDER] \\
3v4 & ... & & ... & & ... & & ... & & [PLACEHOLDER] & \\
4v5 & ... & & ... & & ... & & ... & & [PLACEHOLDER] & \\
```

**Scenario B (K*≠2):**
Same column addition, but CI boundaries will show different K*.

### 1.4 Table 2 (tab:setup) — Add Config Row

File: `method.tex` L47-62

```latex
% Add before \bottomrule:
Qwen-7B & Qwen2.5-7B-Instruct & Continuation & 5{,}000 \\
```

Also update L41: `We evaluate four configurations` → `We evaluate five configurations`
And L4-5 in experiments_c1.tex: add `Qwen2.5-7B-Instruct in continuation mode` to the list.

### 1.5 Fig 2 (fig_auc_decay) — Add Qwen-7B Line

File: figure generation script. Add Qwen-7B as 5th solid line with distinct color/marker.

### 1.6 Fig kstar_theta — Add Qwen-7B Line

File: figure generation script. Add 5th curve.

### 1.7 Section Text Templates

#### §4.1 (experiments_c1.tex) — After L43, before L47

**Scenario A:**
```latex
Qwen2.5-7B-Instruct in continuation mode extends this pattern to a larger scale: 1v2 $\auc = [PLACEHOLDER]$ $[[PLACEHOLDER],\,[PLACEHOLDER]]$, with 2v3 falling below $\theta$ ($\auc = [PLACEHOLDER]$), confirming $\Kempirical = 2$ at 7B.
```

**Scenario B (K* > 2):**
```latex
Qwen2.5-7B-Instruct in continuation mode yields 1v2 $\auc = [PLACEHOLDER]$ and 2v3 $\auc = [PLACEHOLDER]$ $[[PLACEHOLDER],\,[PLACEHOLDER]]$---with the 2v3 CI lower bound exceeding $\theta$, giving $\Kempirical = [PLACEHOLDER]$.
The elevated boundary suggests that larger models preserve more generation-specific structure, consistent with scaling law predictions~\cite{dohmatob2024model}.
```

#### Abstract (main.tex L36)

**Scenario A:**
```latex
Across 5 model-mode configurations and 4 decoding strategies ($1.5$--$7$B scale), $\Kempirical{=}2$ ...
```

**Scenario B:**
```latex
Across 5 model-mode configurations and 4 decoding strategies, $\Kempirical{=}2$ at ${\leq}1.5$B scale; at 7B, $\Kempirical{=}[PLACEHOLDER]$, suggesting [PLACEHOLDER] ...
```

#### Introduction (introduction.tex L22)

**Scenario A:**
```latex
\item \textbf{$\Kempirical = 2$ at $\theta{=}0.60$} (Cohen's $h{\approx}0.20$) across 5 model-mode configurations and 4 decoding strategies at $1.5$--$7$B scale, ...
```

**Scenario B:**
```latex
\item \textbf{$\Kempirical = 2$ at $\theta{=}0.60$} (Cohen's $h{\approx}0.20$) across 4 model-mode configurations and 4 decoding strategies at ${\leq}$1.5B scale, ...; a 7B probe yields $\Kempirical = [PLACEHOLDER]$ (Section~\ref{sec:kstar_boundary}).
```

#### Conclusion (conclusion.tex L4-6)

**Scenario A — replace "≤1.5B" implicit scope:**
```latex
$\Kempirical = 2$ at $\theta{=}0.60$ (Cohen's $h{\approx}0.20$) across all tested configurations ($p \leq 0.002$), extending from 1.5B to 7B scale---implying a one-wash laundering effect ...
```

**Scenario B:**
```latex
$\Kempirical = 2$ at $\theta{=}0.60$ at $\leq$1.5B scale; at 7B, $\Kempirical = [PLACEHOLDER]$, suggesting that [PLACEHOLDER].
```

#### Discussion §Scale Considerations (appendix_extended.tex L50-56)

**Scenario A:**
```latex
Our $\Kempirical = 2$ persists from 1.5B to 7B (Qwen-7B continuation: 1v2 $\auc = [PLACEHOLDER]$, 2v3 $\auc = [PLACEHOLDER]$; Table~\ref{tab:kstar_ci}).
The cross-scale consistency strengthens the information-theoretic interpretation: the generation operator's lossy channel property---not model capacity---governs the boundary.
```

**Scenario B:**
```latex
At 7B scale, $\Kempirical = [PLACEHOLDER]$ (Qwen-7B continuation: 1v2 $\auc = [PLACEHOLDER]$, 2v3 $\auc = [PLACEHOLDER]$; Table~\ref{tab:kstar_ci}), exceeding the $\leq$1.5B boundary of $\Kempirical = 2$.
Larger models preserve more generation-specific structure at deeper depths, consistent with scaling law predictions~\cite{dohmatob2024model}; the information bottleneck widens with model capacity.
```

#### Limitations (main.tex L66)

**Scenario A:**
Change `(1)~model scale ($\leq$1.5B)` to `(1)~model scale (tested at 1.5B and 7B; larger scales remain open)`

**Scenario B:**
Keep `(1)~model scale ($\leq$1.5B for $\Kempirical = 2$; 7B yields $\Kempirical = [PLACEHOLDER]$)`

### 1.8 Cascade Checklist (post-fill)

- [ ] Tab 1 numbers match registry exactly
- [ ] Abstract/Intro/Conclusion scale qualifier consistent
- [ ] Fig 2 + Fig kstar_theta regenerated with 7B data
- [ ] Limitations updated
- [ ] Appendix §Scale Considerations updated
- [ ] `check_paper_consistency` passes
- [ ] Page count ≤ 18 (adding a column to Table 1 may push layout)

---

## 2. exp-012 (Binary Confidence) Integration

### 2.1 Registry: exp_012_binary_confidence (QUEUED)
- Method: DivEye log-PPL + Binoculars ratio (observer=Pythia-1.4b, performer=OLMo-1B)
- Metric: Spearman correlation between detector confidence and true depth
- Hypothesis: weak correlation → binary confidence ≠ depth estimation

### 2.2 Insertion Point: New §4.6 "Binary Confidence Does Not Predict Depth"

Place after §4.5 (Neural Probe) in `experiments_c1.tex`, before the `\end` of experiments section.

Rationale: Natural progression — §4.5 shows learned representations can't push K* much deeper; §4.6 shows binary detectors' confidence doesn't even correlate with depth. Together they bracket the claim that depth estimation requires dedicated methods.

### 2.3 Text Template

```latex
%% ====================================================================
\subsection{Binary Detector Confidence and Depth}
\label{sec:binary_confidence}

Binary synthetic text detectors produce a confidence score---but does higher confidence imply deeper generation?
We compute Spearman $\rho$ between detector confidence and true depth for two representative detectors: DivEye~\cite{basani2026diveye} (log-PPL) and Binoculars~\cite{hans2024binoculars} (cross-model perplexity ratio; observer: Pythia-1.4B, performer: OLMo-1B).

DivEye confidence yields $\rho = [PLACEHOLDER]$ ($p = [PLACEHOLDER]$); Binoculars yields $\rho = [PLACEHOLDER]$ ($p = [PLACEHOLDER]$).
[IF weak: Both correlations are weak, confirming that binary detection confidence is not a proxy for generational depth.]
[IF one strong, one weak: DivEye/Binoculars shows [PLACEHOLDER] correlation while [OTHER] shows [PLACEHOLDER], suggesting [PLACEHOLDER].]

This result complements the zero-shot LLM findings (Section~\ref{sec:why_kstar}): frontier LLMs cannot estimate depth via prompting, and binary detectors' confidence scores do not encode depth information either.
Depth estimation requires dedicated statistical features that capture the progressive distributional shift across generations, not merely the binary human-vs-machine distinction.
```

### 2.4 Supporting Evidence Table (if correlations warrant)

```latex
\begin{table}[t]
\centering
\small
\caption{Spearman $\rho$ between binary detector confidence and true generational depth. Neither detector's confidence reliably predicts depth.}
\label{tab:binary_confidence}
\begin{tabular}{lcc}
\toprule
\textbf{Detector} & \textbf{Spearman $\rho$} & $p$ \\
\midrule
DivEye (log-PPL)    & [PLACEHOLDER] & [PLACEHOLDER] \\
Binoculars (PPL ratio) & [PLACEHOLDER] & [PLACEHOLDER] \\
\bottomrule
\end{tabular}
\end{table}
```

Decision: Include table only if there are ≥3 rows of data (e.g., per-model breakdown). If only 2 detectors, report inline.

### 2.5 Cascade Updates

#### Abstract (main.tex)
No change needed — already says "Binary detection methods produce no depth estimate" is motivated in Introduction.

#### Introduction (introduction.tex L11)
Current: `Binary detection methods~\cite{basani2026diveye, zhang2024minkpp, zawalski2026codec} produce no depth estimate.`
Add after: `Moreover, their confidence scores do not correlate with depth (Section~\ref{sec:binary_confidence}), confirming that detection and depth estimation are fundamentally different tasks.`

#### Discussion §Why K*=2 (discussion.tex)
Add paragraph after L18 (convergent failure paragraph):
```latex
Binary detection confidence further confirms this separation: DivEye and Binoculars scores show [weak/negligible] Spearman correlation with true depth ($\rho = [PLACEHOLDER]$ and $[PLACEHOLDER]$), indicating that the confidence axis of binary detectors is orthogonal to the depth dimension.
```

### 2.6 Cascade Checklist (post-fill)

- [ ] New §4.6 compiles cleanly
- [ ] Binoculars citation in references.bib (hans2024binoculars — verify exists)
- [ ] DivEye citation already present (basani2026diveye — verified in intro L11)
- [ ] Introduction cascade sentence added
- [ ] Discussion cascade paragraph added
- [ ] `check_paper_consistency` passes
- [ ] Page count ≤ 18 (new subsection ~0.3 pages; may need to trim if tight)

---

## 3. Page Budget Assessment

Current: 18 pages exactly.

- exp-004 additions: ~0.5 column (Table 1 wider + §4.1 paragraph + scale qualifier changes)
- exp-012 additions: ~0.5-0.7 column (new §4.6 + cascade updates)
- Total: ~1-1.2 columns = ~0.5-0.6 pages

Risk: May push to 19 pages. Mitigation options:
1. Move exp-012 table to appendix (saves ~0.2 col)
2. Compress §4.6 to a paragraph within §4.5 instead of new subsection
3. Tighten §4.1 scale paragraph to 1 sentence
4. Move K*(θ) figure caption text to shorter form
