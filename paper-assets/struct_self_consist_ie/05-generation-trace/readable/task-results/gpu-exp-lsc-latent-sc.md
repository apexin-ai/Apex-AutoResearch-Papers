# gpu exp lsc latent sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_lsc_latent_sc_20260520T163017_result.json`
- **Structured JSON:** [`b5df5ded1f4b0e4a1be2.json`](../../sessions/b5/b5df5ded1f4b0e4a1be2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果为 **negative**。

## 结果摘要

| Method | F1 |
|--------|-----|
| Greedy | 0.7793 |
| LP Selection | 0.7845 |
| **Centroid Selection (A)** | **0.7593** ❌ |
| Majority Vote | 0.8366 |
| **Latent Entity Conf (B)** | **0.8385** (~= MV) |
| Oracle | 0.8668 |

**关键发现：**
- **Centroid selection (0.7593) 比 LP selection (0.7845) 还差**，head-to-head W100/L218/T1671
- Latent entity confidence (0.8385) 仅比 majority vote (0.8366) 高 +0.19pp，几乎无增益
- LP vs Latent Spearman ρ=0.518（中等相关）— hidden states 确实提供了 LP 之外的部分独立信号，但这些信号不足以改善 selection
- Entity match rate 99.45% — pipeline 本身工作正常
- 507s (8.5min) 完成 2000 instances × 8 samples

**结论：** 假设"hidden states 绕过 LP 压缩提供更好的 discriminative ranking"在技术上成立（ρ=0.518 说明两者不完全相关），但 latent signal 的判别力不足以超越已有 baselines。Centroid selection 尤其差，说明 mean-pooled entity fingerprint 的相似性不能有效区分好/坏 samples。

---
