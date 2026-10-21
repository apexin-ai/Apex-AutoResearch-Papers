# data nve trajectories figure

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_nve-trajectories-figure_20260516T192934_result.json`
- **Structured JSON:** [`ff63445c37983f0cf07f.json`](../../sessions/ff/ff63445c37983f0cf07f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件：`artifacts/analysis/nve_trajectories_for_figure.json`（已注册 `art_20260516_c91be5`）

**10 个实验的 NVE 轨迹汇总：**

| 实验 | 环境 | Seed | NVE 峰值 | 坍缩起点 |
|------|------|------|---------|---------|
| 008d (trained dt-emb) | Walker | 1 | 4.13×@55K | 55K |
| 008f (no dt-emb) | Walker | 1 | 1.02×@25K | — |
| 009b (trained dt-emb) | Walker | 2 | 2.04×@25K | — (自修正) |
| 009c (no dt-emb) | Walker | 2 | 1.26×@25K | — |
| 016e (SGS partial) | Walker | 1 | 10.42×@95K | 85K |
| 018v2 (SGS full) | Walker | 1 | 4.0×@25K | 112K |
| 015b (frozen dt-emb) | Walker | 1 | 1.45×@55K | — |
| baseline | Walker | 1 | 1.0× | — |
| 010a (baseline) | Cheetah | 1 | 1.0× | — |
| 010b (CIVO trigger) | Cheetah | 1 | 8.65×@65K | 55K |

每个实验包含 5K-105K 每 10K 步的 `nve`、`eval_return`、`value_mean`，以及 baseline v/e ratios 供复现。

---
