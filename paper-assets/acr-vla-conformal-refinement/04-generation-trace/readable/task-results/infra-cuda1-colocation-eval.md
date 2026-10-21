# infra cuda1 colocation eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cuda1-colocation-eval_20260513T214253_result.json`
- **Structured JSON:** [`4fcbccd0bb1edaa1313c.json`](../../sessions/4f/4fcbccd0bb1edaa1313c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是分析报告。

---

## cuda:1 叠加任务评估报告

### 1. 当前状态

| 指标 | 值 |
|------|-----|
| GPU util | 8-10% |
| VRAM 占用 | 555 MiB / 24,564 MiB (2.3%) |
| 进程 | PID 78520, CRM train K=10 |
| 训练进度 | **epoch 32/50** (非之前报告的 ~20/50) |

全机 GPU 概览：

| GPU | Util | VRAM | 任务 |
|-----|------|------|------|
| 0 | 11% | 1423 MiB | eval-spatial-v5-full |
| 1 | 8% | 555 MiB | CRM train K=10 |
| 2 | 18% | 1423 MiB | eval-reconvla-spatial-v1 |
| 3 | 23% | 1541 MiB | precompute-k5 (object) |

### 2. CRM 训练剩余时间

训练进程 PID 94479/94480 于 05:41 启动，截至 05:44 已完成 31 个 epoch。

- 每 epoch 耗时：≈ **6 秒**（337K MLP + 26737 样本 + bs=32，计算量极小）
- 剩余 18 个 epoch → **约 2 分钟完成**

### 3. K=5 Precompute 状态

正在 cuda:3 上跑，object 部分 9100/14570，**约 22 分钟后完成**。spatial 部分已跑完并合并。不需要在 cuda:1 上再跑一份。

### 4. 缓存现状

| Cache | 状态 |
|-------|------|
| `crm_cache/` (K=10) | 已完成 |
| `crm_cache_k5/` | 进行中（~22min 完成）|
| `crm_cache_k3/` | **不存在** |
| `crm_cache_k20/` | **不存在** |

### 5. 结论：**不建议叠加，但建议接力**

**原因：** CRM 训练将在 ~2 分钟内完成，叠加任务的启动开销就已经超过这个窗口。"叠加"的前提不成立。

**建议：** CRM 训练完成后，cuda:1 将完全空闲（24 GB），此时直接启动 **K=3 precompute** 或 **K=20 precompute**（各 ~35 min, ~1.5 GB VRAM），无需担心 CUDA context 冲突。

优先级建议：K=3 > K=20（K=3 是消融实验的下界，对论文 table 更有价值；K=20 的收益递减可能不大）。若时间允许，K=3 完成后紧接 K=20，cuda:1 可在 ~70 分钟内串完两个。

---
