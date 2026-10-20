# analysis exp 082

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-082_20260520T005727_result.json`
- **Structured JSON:** [`98b0ca2ccf4d4b3724f7.json`](../../sessions/98/98b0ca2ccf4d4b3724f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总报告：

---

## exp-082 结果分析：Contrastive × Mistral-7B × FOLIO-204 (seed=123)

### 核心指标

| 指标 | exp-082 (seed=123) | exp-075b (seed=42) | 差异 |
|------|-------------------|-------------------|------|
| SC accuracy | **54.90%** (112/204) | 56.86% (116/204) | -1.96pp |
| Contrastive accuracy | **49.51%** (101/204) | 47.55% (97/204) | +1.96pp |
| **Δ (Contrastive - SC)** | **-5.39pp** | -9.31pp | 缩窄 3.92pp |
| Degenerate count | 35/204 (17.2%) | 41/204 (20.1%) | 减少 6 |
| Pro constraints | 1036 | — | — |
| Con constraints | 920 | — | — |
| Wall time | 206.3 min | — | — |

### Hypothesis 验证

**Rejected.** Δ 差异为 3.92pp，超出 ±2pp 容差。两个 seed 的 SC baseline 本身就差 ~2pp，说明 Mistral-7B 在 FOLIO 上的 sampling variance 较大。

### 关键发现

1. **方向一致**：两个 seed 均为 negative（contrastive < SC），确认 contrastive pipeline 在 Mistral-7B + FOLIO 上系统性地损害准确率
2. **幅度不稳定**：-5.39pp vs -9.31pp，degradation 大小受 seed 影响显著
3. **退化率略降**：35 vs 41，但仍有 17% 的样本因只产生单一候选答案而退化
4. **约束信号弱**：pro/con 比例接近（1036:920），说明约束未能有效区分正确和错误答案
5. **交叉验证 exp-085**（LogiQA, seed=123）：Δ=-2.5pp，同样 negative

### 结论

Contrastive constraint generation 在 Mistral-7B 上跨数据集（FOLIO, LogiQA）、跨 seed（42, 123）**一致为负面**。这不是 seed noise——是方法本身的系统性问题。

---
