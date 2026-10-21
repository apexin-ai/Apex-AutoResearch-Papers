# analysis exp 018v2 full sgs walker s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018v2_full_sgs_walker_s1_20260516T171908_result.json`
- **Structured JSON:** [`2a8a836a6b93bdbfa437.json`](../../sessions/2a/2a8a836a6b93bdbfa437.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**exp_018v2_full_sgs_walker_s1 — Conclusion: NEGATIVE (但有重要部分成功)**

| 指标 | 值 |
|------|-----|
| eval_return peak | 499.6 @ 75K |
| eval_return final | 448.3 @ 105K |
| NVE peak | **1.66×** @ 95K (超过 1.5× 阈值) |
| NVE final | 1.34× @ 105K |
| NVE mean (45K-105K) | 1.23× |
| CIVO reduction vs 008d | **79%** (excess NVE 从 3.12 降到 0.66) |
| Late collapse | 有 (112K train_return 降到 11-108) |

**核心发现**: Full-SGS 将 CIVO 大幅降低 79%，证明 obs decoder gradient 是 CIVO 的**主要**驱动因素。但未完全消除——NVE 在 95K 仍有 1.66× 的瞬时尖峰，且末尾出现不稳定。C5("obs decoder gradient 是 CIVO sole root cause") 部分支持但不完全成立，可能存在次要的 CIVO 机制。

已更新：registry (status=DONE, conclusion=negative, metrics), nve_trajectories.csv, 分析报告已注册为 artifact。

---
