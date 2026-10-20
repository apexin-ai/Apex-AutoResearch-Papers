# analysis mitigation diagnostics real run

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mitigation_diagnostics_real_run_20260514T124019_result.json`
- **Structured JSON:** [`217850e1c6fe87f72c54.json`](../../sessions/21/217850e1c6fe87f72c54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，所有三项分析均成功执行。以下是实际计算结果：

---

### 分析 1: 近重复度分析 (Contriever embeddings)

每代 N=977 样本：

| 阈值 ε | Gen 1 | Gen 4 | Gen 7 |
|--------|-------|-------|-------|
| 0.95 | 14 (1.4%) | 19 (1.9%) | 22 (2.3%) |
| 0.90 | 19 (1.9%) | 39 (4.0%) | 40 (4.1%) |
| 0.85 | 29 (3.0%) | 47 (4.8%) | 54 (5.5%) |
| 0.80 | 33 (3.4%) | 51 (5.2%) | 60 (6.1%) |
| 0.70 | 46 (4.7%) | 69 (7.1%) | 87 (8.9%) |

趋势：近重复比例随代数增加（Gen1 1.4%→Gen4 1.9%→Gen7 2.3% at ε=0.95）

---

### 分析 2: Gen-0 PPL 分布

| 代 | Mean | Median | P10 | P25 | P75 | P90 | P95 | P99 |
|----|------|--------|-----|-----|-----|-----|-----|-----|
| Gen 1 | 2.0 | 1.8 | 1.3 | 1.5 | 2.2 | 2.8 | 3.2 | 4.4 |
| Gen 4 | 1.4 | 1.4 | 1.2 | 1.3 | 1.5 | 1.7 | 1.8 | 2.1 |
| Gen 7 | 1.4 | 1.4 | 1.2 | 1.3 | 1.5 | 1.8 | 1.9 | 2.1 |

分布漂移：
- Gen1→Gen4: mean shift **-0.5**, KS stat=0.492 (p=0.0000) — 显著收窄
- Gen4→Gen7: mean shift **-0.0**, KS stat=0.089 (p=0.0009) — 基本稳定

---

### 分析 3: RGDS 选中 vs 拒绝 PPL 对比

**Gen 4:**
- Selected (N=488): mean PPL=1.31, median=1.28, P90=1.51
- Rejected (N=489): mean PPL=1.51, median=1.47, P90=1.79
- 差异: -0.20, t=-17.40, p=0.0000, **Cohen's d=-1.11**

**Gen 7:**
- Selected (N=488): mean PPL=1.18, median=1.16, P90=1.32
- Rejected (N=489): mean PPL=1.34, median=1.28, P90=1.59
- 差异: -0.15, t=-14.66, p=0.0000, **Cohen's d=-0.94**

RGDS 强烈偏向选中低 PPL 样本（Cohen's d > 0.9，效应量大），确认其作为质量过滤器有效将高困惑度样本排除。

---
