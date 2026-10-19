# code advbench reclassify phase2 v2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_advbench_reclassify_phase2_v2_20260522T135840_result.json`
- **Structured JSON:** [`b87742a7b9b0e4c81f06.json`](../../sessions/b8/b87742a7b9b0e4c81f06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 v2 完成。结果汇总：

---

### 1. JB/Safe 分布

| | v1 | v2 |
|--|---|---|
| Total traces | 520 | 520 |
| JB | (原始分类) | **159** |
| Safe | (原始分类) | **361** |
| JB rate | — | **30.6%** |
| Reclassified | — | 271 traces |

---

### 2. 5-Metric Layer Selection 表

| Metric | Best Layer | Window | Depth% | Score |
|--------|-----------|--------|--------|-------|
| Bal. accuracy | L9 | W15 | 29.0% | 0.7331 |
| Precision | L21 | W15 | 67.7% | 0.7279 |
| Inv. FPR | L21 | W15 | 67.7% | 0.1944 |
| CR-composite | L3 | W5 | 9.7% | 0.2991 |
| AUROC | L11 | W15 | 35.5% | 0.8053 |
| Crossing rate | L0 | W5 | 0.0% | 0.4519 |

---

### 3. v1 vs v2 对比

| | v1 | v2 | 变化 |
|--|---|---|---|
| CR-composite best | **L9** (29.0%) | **L3** (9.7%) | 向更浅层偏移 |
| Precision best | **L22** (71.0%) | **L21** (67.7%) | 基本不变 |
| **Divergence** | **42pp** | **58pp** | **+16pp，偏差加剧** |

关键发现：修正 trace 分类器后，divergence 从 42pp **扩大到 58pp**。CR-composite 最优层从 L9 大幅下移到 L3（更浅），而 Precision 最优层基本稳定在 L21-22（深层）。这说明 v1 的分类噪声实际上**掩盖了**一部分 layer selection bias——清洗标签后，crossing-rate 主导的 composite 指标更加偏向浅层，与 precision/FPR 等判别性指标的分歧更大。Bias replication 结论不变且更强。

---
