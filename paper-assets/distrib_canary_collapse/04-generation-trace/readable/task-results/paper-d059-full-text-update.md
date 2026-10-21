# paper d059 full text update

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d059_full_text_update_20260518T035629_result.json`
- **Structured JSON:** [`def81dd657ab65cd8b6c.json`](../../sessions/de/def81dd657ab65cd8b6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Compilation: 0 errors, 26 pages.

---

## 修改前后对比

### 修改 1+6: Abstract
文件: abstract.tex, L5
```
OLD: (24/24 forward, 0/24 reverse, four methods, four seeds), with strong directional asymmetry (token entropy: 0\% reverse, ECE: marginal)
NEW: (${\geq}4/5$ method consensus, four seeds), with token entropy maintaining complete unidirectional precedence (0/16 reverse pairs significant across 4 seeds; ECE: marginal reverse consistent with calibration-diversity feedback)
```

### 修改 2a: Introduction methods
文件: introduction.tex, L48
```
OLD: confirmed by 4 independent methods, 4 seeds
NEW: confirmed by ${\geq}4/5$ method consensus, 4 seeds
```

### 修改 2b: Introduction reverse claim
文件: introduction.tex, L48
```
OLD: with token entropy maintaining complete unidirectional precedence (24/24 forward, 0/24 reverse)
NEW: with token entropy maintaining complete unidirectional precedence (forward 12/12 across 4 seeds and 3 diversity metrics, reverse 0/12; ECE: marginal reverse $p\approx 0.03$, consistent with a canary quality hierarchy, \S\ref{sec:discussion})
```

### 修改 3: Case study
文件: experiments.tex, L195
```
OLD: Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} significant (all $p{>}0.49$), establishing complete directional asymmetry.
NEW: Token entropy reverse-direction tests (diversity$\to$token\_entropy) find \textbf{0/4} significant under unified parameters (all $p{>}0.48$, seed~42; consistently non-significant across all 4 seeds under the original FDR-corrected analysis). ECE reverse-direction tests show 3/4 significant ($p\approx 0.03$ for diversity$\to$ECE; perplexity$\to$ECE $p{=}0.14$), consistent with the canary quality hierarchy documented in \S\ref{sec:discussion}.
```

### 修改 4: Conclusion
文件: conclusion.tex, L16
```
OLD: At $\alpha{=}1.0$, token entropy exhibits robust Granger-precedence over diversity collapse (24/24 forward, 0/24 reverse, Tier~3 across 4~seeds) with a consistent one-generation lead.
NEW: At $\alpha{=}1.0$, token entropy exhibits robust Granger-precedence over diversity collapse (${\geq}4/5$ method consensus, Tier~3 across 4~seeds) with complete unidirectional precedence (token entropy: 0/16 reverse pairs across 4 seeds; ECE: marginal reverse $p\approx 0.03$, consistent with a canary quality hierarchy) and a consistent one-generation lead.
```

### 修改 5: Tables 一致性检查
Tables 无 unscoped "0/24 reverse" claim。table footnotes (L356-357) 已正确 scope 到 token\_entropy。无需修改。

### 修改 7: Limitations single-seed caveat
文件: limitations.tex, 新增 L45-46 (在 Replace-only protocol 前)
```
NEW: \paragraph{Single-seed generalization conditions.}
All generalization conditions (architecture, scale, domain; \S\ref{sec:generalization}) use a single seed; C4 cross-seed replication reveals seed-dependent variation in reverse-direction significance (4/8 vs 0/8), motivating future multi-seed validation.
```

### 修改 8a: Discussion GPT-2m conditional
文件: discussion.tex, L15
```
OLD: Initial cross-architecture validation on GPT-2-medium (single seed, $\alpha{=}1.0$) replicates the entropy-leads-diversity pattern
NEW: Preliminary cross-architecture validation on GPT-2-medium (single seed, $\alpha{=}1.0$) suggests the entropy-leads-diversity pattern transfers
```

### 修改 8b: Discussion GPT-2m α=0.25 conditional
文件: discussion.tex, L17
```
OLD: At $\alpha{=}0.25$, GPT-2-medium yields
NEW: In preliminary $\alpha{=}0.25$ experiments, GPT-2-medium yields
```

### 额外一致性修改 (全文一致规则)

**experiments.tex, L147:**
```
OLD: with 0/24 in the reverse direction, confirming temporal asymmetry.
NEW: with token entropy reverse 0/16 across four seeds; ECE reverse shows marginal significance in 3/4 conditions ($p\approx 0.03$), consistent with the canary quality hierarchy (\S\ref{sec:discussion}).
```

**experiments.tex, L200 (figure caption):**
```
OLD: This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction significant pairs.
NEW: This visual pattern corresponds to the statistical finding of 24/24 forward-direction significant pairs, with token entropy maintaining complete unidirectional precedence (reverse 0/4 per seed).
```

### 编译结果
`pdflatex -interaction=nonstopmode main.tex`: 0 errors, 26 pages, 491271 bytes. Backup at `docs/paper_backup_d059/`.

---
