# harvest goal crm s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_goal-crm-s47_20260524T120138_result.json`
- **Structured JSON:** [`7bda97b038c7d482ed1d.json`](../../sessions/7b/7bda97b038c7d482ed1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个完成实验已更新 registry。汇报如下：

## 收割结果

### 已完成（3 个，均 success）

| 实验 | GPU | SR | 详情 |
|------|-----|-----|------|
| **eval-supp-goal-crm-norm005-s47** | cuda:1 | **82.0%** (164/200) | crm_obs_only, norm=0.05 |
| **eval-supp-goal-adapt-tau025-s47** | cuda:0 | **82.0%** (164/200) | adaptive_conformal_crm, tau=0.25, trigger_rate=8.87%, mean_unc=0.148 |
| **eval-supp-goal-k2mean-s47** | cuda:2 | **82.5%** (165/200) | vla_only, baseline_mode=mean |

### 仍在运行（2 个）

| 实验 | GPU | 状态 |
|------|-----|------|
| **eval-supp-obj-reconvla-s47** | cuda:4 (1911 MiB) | Object benchmark 进行中，正在跑 pick_up 系列任务 |
| **eval-supp-long-k2mean-s47-r2** | cuda:5 (4303 MiB) | Long-horizon benchmark 进行中，已过 KITCHEN_SCENE4 |

### 服务器 GPU 状态

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 1901 MiB | 残留（adapt 已结束） |
| 1 | 1 MiB | 空闲 |
| 2 | 1 MiB | 空闲 |
| 3 | 1 MiB | 空闲 |
| 4 | 1911 MiB | obj-reconvla 运行中 |
| 5 | 4303 MiB | long-k2mean 运行中 |

GPU 0/1/2/3 已空闲，可用于新任务。

---
