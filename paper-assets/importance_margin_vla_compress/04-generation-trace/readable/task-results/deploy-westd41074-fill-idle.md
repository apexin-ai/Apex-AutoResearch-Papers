# deploy westd41074 fill idle

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_fill_idle_20260524T193017_result.json`
- **Structured JSON:** [`1c266ce7328ebaf052bc.json`](../../sessions/1c/1c266ce7328ebaf052bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果。

---

## westd-41074 GPU 状态汇报

### 1. 4 个 GPU 实际运行状态

| GPU | 显存 | 利用率 | 运行实验 | 状态 |
|-----|------|--------|---------|------|
| 0 | 10786/97887 MiB | 22% | Random k=0.9 Long seed43 postfix (PID 634833) | RUNNING |
| **1** | **1 MiB** | **0%** | **空闲** — L2norm k=0.85 seed43 v2 已完成 | — |
| 2 | 10780/97887 MiB | 37% | Random k=0.85 Long seed43 postfix (PID 635090) | RUNNING |
| **3** | **1 MiB** | **0%** | **空闲** — L2norm k=0.7 seed43 已完成 | — |

### 2. L2norm seed42 postfix 结果

| 实验 | SR | 状态 |
|------|-----|------|
| L2norm k=0.3 seed42 Long postfix | **36.6%** | DONE (刚完成，结果在 westd-41074) |
| L2norm k=0.5 seed42 Long postfix | — | RUNNING on westd-27271 |

### 3. 新发现的已完成实验（已更新 registry → DONE）

- **L2norm k=0.7 seed43 Long** → SR=62.6%
- **L2norm k=0.85 seed43 Long** → SR=78.6%
- **L2norm k=0.3 seed42 Long** → SR=36.6%

### 4. 部署情况

**没有部署新实验。** 原因：
- 原定目标 Random k=0.3 seed43 postfix 结果已存在 (SR=28.0%, 500 episodes, 有效)
- Random k=0.3 seed42 postfix 也已 DONE (SR=29.6%, westd-38929)
- L2norm k=0.7 seed42 postfix 已 DONE (SR=62.6%, westd-27271)
- 遍历所有 Long dual-seed 矩阵，**全部 k 值×双 seed 都已 DONE 或 RUNNING**，无缺失数据点

GPU0/GPU2 的实验已补录 registry 条目并设为 RUNNING。

**GPU1 和 GPU3 目前空闲，Long dual-seed 曲线无缺口可填。** 如需部署其他实验（如其他 suite 或 attention scoring），请指示。

---
