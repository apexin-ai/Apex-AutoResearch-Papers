# code urgent phase2 results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_urgent_phase2_results_20260522T235931_result.json`
- **Structured JSON:** [`8bcffd00ea4e5005b611.json`](../../sessions/8b/8bcffd00ea4e5005b611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 Phase 2 Cross-Scoring 均已完成，GPU 空闲。结果如下：

---

## Gemma-27B (C4) — Qwen Cross-Scored

| Pair | Self-Scored | Cross-Scored (Qwen) | Δ |
|------|------------|---------------------|------|
| 0v1 | **0.9695** | **0.8874** | −0.0821 |
| 1v2 | **0.6196** | 0.5894 | −0.0302 |
| 2v3 | 0.5388 | 0.5150 | −0.0238 |
| 3v4 | 0.5069 | 0.5059 | −0.0010 |
| 4v5 | 0.5124 | 0.5107 | −0.0017 |

**K\* (θ=0.60):**
- Self-scored: K\* = **2** (0v1=0.97, 1v2=0.62 ≥ 0.60; 2v3=0.54 < 0.60)
- Cross-scored: K\* = **1** (0v1=0.89 ≥ 0.60; 1v2=0.59 < 0.60)

Cross-scoring 使 0v1 降了 8.2pp，1v2 跌破阈值，K\* 从 2 降到 1。

---

## Gemma-2B 10K — Qwen Cross-Scored

| Pair | Self-Scored | Cross-Scored (Qwen) | Δ |
|------|------------|---------------------|------|
| 0v1 | **0.9817** | **0.9534** | −0.0283 |
| 1v2 | **0.6430** | **0.6099** | −0.0331 |
| 2v3 | 0.5550 | 0.5409 | −0.0141 |
| 3v4 | 0.5173 | 0.5174 | +0.0001 |
| 4v5 | 0.5101 | 0.5159 | +0.0058 |

**K\* (θ=0.60):**
- Self-scored: K\* = **2** (0v1=0.98, 1v2=0.64 ≥ 0.60; 2v3=0.56 < 0.60)
- Cross-scored: K\* = **2** (0v1=0.95, 1v2=0.61 ≥ 0.60; 2v3=0.54 < 0.60)

Cross-scoring 整体衰减较温和（0v1 降 2.8pp，1v2 降 3.3pp），K\* 保持 2 不变。

---

### 小结

| 实验 | Self K\* | Cross K\* | 变化 |
|------|---------|----------|------|
| Gemma-27B C4 | 2 | **1** | ↓1 |
| Gemma-2B 10K | 2 | **2** | 不变 |

Gemma-27B 的 cross-scoring 衰减显著，1v2 从 0.62 跌到 0.59 刚好落在阈值下方（borderline）。Gemma-2B 10K 的 cross-scoring 虽也有衰减但 1v2 仍以 0.61 守住阈值。

---
