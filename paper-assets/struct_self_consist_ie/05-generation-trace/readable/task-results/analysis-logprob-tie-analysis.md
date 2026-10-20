# analysis logprob tie analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_logprob_tie_analysis_20260515T071401_result.json`
- **Structured JSON:** [`f6287a428cc0aebf5ebc.json`](../../sessions/f6/f6287a428cc0aebf5ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 register_artifact 工具可用。报告已写入 `artifacts/logprob_tie_analysis.md`。

---

## 分析结果摘要

### Tie 问题严重

- Median logprob range 仅 **0.041**（8 个样本间 mean_logprob 最大差异）
- **ε=0.05 时 60% instance 是 tied**，ε=0.1 时 84% tied
- 大部分 instance 上 logprob selection 退化为近随机

### Non-tied 子集上 logprob 有效

| 子集 | N | LP-best vs Greedy | p-value |
|------|---|-------------------|---------|
| range ≥ 0.05 | 222 (40%) | **+0.027** | **0.010** |
| range ≥ 0.1 | 90 (16%) | +0.035 | 0.079 |

在 non-tied 子集上 logprob 甚至**优于 SJ** (0.6133 vs 0.6066)。

### SJ 优势来自 spread 而非 signal quality

- SJ 仅 12.5% tied vs logprob 60% tied
- 两者一致性仅 14.3% → 捕获不同维度
- Within-instance ρ 随 logprob spread 从 0.08 增长到 0.39

### 结论

**Ties 是 logprob 表现差的充分解释**。Logprob 包含有效质量信号 (ρ≈0.39 when spread)，但被数值压缩限制。SJ 胜出因为离散 Jaccard 天然有更大区分度，不是因为更好的信号。两者组合潜力大。

---
