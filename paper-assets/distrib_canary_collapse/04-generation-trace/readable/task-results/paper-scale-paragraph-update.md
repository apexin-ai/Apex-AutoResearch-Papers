# paper scale paragraph update

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_scale_paragraph_update_20260518T032731_result.json`
- **Structured JSON:** [`cd3125050fac91f9419e.json`](../../sessions/cd/cd3125050fac91f9419e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 修改文件及位置

| 文件 | 位置 | 修改类型 |
|------|------|---------|
| `experiments.tex` | L370-376 `\paragraph{Scale generalization.}` | 重写段落 |
| `experiments.tex` | L356-359 Table 7 footnote | 新增一行脚注 |
| `discussion.tex` | L33 (Short time-series constraint 段落内) | 插入 1 句 |

### 2. Scale 段落全文

```latex
\paragraph{Scale generalization.}
Scaling from 410M to 1.4B parameters (3.4$\times$) preserves majority consensus
($K{\geq}4/5$ in 5/8 pairs): the lead-lag signal persists across model scale.
Of the three non-consensus pairs, two target perplexity
(token\_entropy$\to$perplexity, $K{=}1$; ECE$\to$perplexity, $K{=}2$), a channel
that also fails to reach $K{\geq}4$ in the 410M Baseline due to the shared-trend
artifact identified by the first-differencing diagnostic (\S\ref{sec:method_sensitivity}).
The sole scale-specific miss is token\_entropy$\to$distinct\_3 ($K{=}3/5$), where
permutation Granger forward significance falls just short of threshold ($p{=}0.053$);
excluding perplexity pairs, Scale consensus reaches 5/6.
Threshold onset detection achieves 8/8 at this scale, and permutation Granger reverse
significance is 0/8 (the only condition without ECE reverse leakage, likely because the
larger model's reduced variance suppresses borderline reverse signals).
Toda--Yamamoto yields 0/8 significant pairs: at $T{=}10$ generations, ADF integration
order estimates become unstable across conditions (token\_entropy shifts from $I(0)$ to
$I(1)$ relative to the Baseline), and the resulting loss of residual degrees of freedom
renders the procedure uninformative (\S\ref{sec:consensus_validation}).
The consensus framework absorbs this single-method failure by design.
```

旧段落错误已修正：原文称"two token\_entropy pairs"落入非共识，实际是 3 对（遗漏了 ece→ppl）。

### 3. TY limitation — 修改

在 discussion.tex "Short time-series constraint" 段落的 FNR 句后插入 1 句：

> Scale amplifies this limitation: in Pythia-1.4B, ADF integration order estimates become unstable (token\_entropy shifts from I(0) to I(1)) and increased downstream variance degrades signal-to-noise ratios, so Toda--Yamamoto yields 0/8 significance at this scale while the consensus framework still maintains K≥4/5 in 5/8 pairs.

### 4. Table 7 脚注 — 已添加

新增一行：
> Canary→perplexity pairs do not reach K≥4 in any condition; these are shared-trend artifacts eliminated by first-differencing (§method\_sensitivity).

### 5. 编译结果

0 errors, 26 pages, `main.pdf` 489907 bytes.

---
