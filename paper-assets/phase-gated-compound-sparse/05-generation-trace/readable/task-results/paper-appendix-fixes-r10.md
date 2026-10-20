# paper appendix fixes r10

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_fixes_r10_20260516T035040_result.json`
- **Structured JSON:** [`f9a053a88497fe634098.json`](../../sessions/f9/f9a053a88497fe634098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three fixes are complete and the paper compiles cleanly. Here's a summary of changes:

### 修改摘要

**修改文件 (7 个)：**

**1. NT samples — `appendix_robustness.tex`**
- 新增 `\subsection{Non-Think Token Quality Under Compound Sparsity}` (label: `app:nt-samples`)
- 两个 illustrative examples：Example 1 展示 answer tokens 在 s=0.25 下 PPL 近基线 (1.2×)、thinking tokens 4.8× 膨胀；Example 2 展示 s=0.30 下 severity 穿透 phase boundary
- 明确标注 non-think = `&lt;think>` 标签外的最终输出 token

**2. Pilot CI — `appendix_moved.tex` + `appendix_disc_analysis.tex`**
- `appendix_moved.tex`: profiling subset table caption 增加说明"preliminary table does not include per-condition bootstrap CIs"，指向 Table 2 (n=496 CIs) 和 Table 7 (permutation CIs)。表后新增段落列出确认后的 n=496 CIs
- `appendix_disc_analysis.tex`: GSM8K section 新增 `\paragraph{Power analysis for random conditions.}`，引用 c9 数据：min detectable d=0.40, max observed |d|=0.164, QW importance d≈0.63 power>0.99

**3. G metric downgrade — 6 个文件**
- `background.tex`: G 定义处改为 "auxiliary descriptive ratio that illustrates..."
- `methodology.tex`: "complementary ratio perspective" → "auxiliary illustrative ratio"
- `results.tex`: "complementary ratio perspective" → "auxiliary illustrative perspective"；answer-region 段删除 `($G \approx 1$)` 引用
- `limitations.tex`: 加 "auxiliary ratio" 修饰
- `appendix_robustness.tex`: G table caption 重写为 "serves as an auxiliary visualization... primary statistical evidence is provided by $\Delta$"；body text "Strong phase modulation is specific to" → "The $G$ values illustrate that..."，末尾加 "should be interpreted as a descriptive ratio rather than an independent statistical test"；outlier section 加 "(auxiliary illustration of phase concentration)"
- `appendix_moved.tex`: profiling subset caption 加 "serve as an auxiliary illustration"；"explaining $G \approx 1$" → "consistent with $G \approx 1$"

---
