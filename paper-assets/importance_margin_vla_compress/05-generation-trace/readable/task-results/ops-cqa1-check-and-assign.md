# ops cqa1 check and assign

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-check-and-assign_20260520T131653_result.json`
- **Structured JSON:** [`2b7aba13227232f94db1.json`](../../sessions/2b/2b7aba13227232f94db1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 状态汇报

### GPU 状态

| GPU | 显存占用 | 状态 | 进程 |
|-----|---------|------|------|
| 0 | 1 MiB / 24564 MiB | **空闲** | — |
| 1 | 1 MiB / 24564 MiB | **空闲** | — |
| 2 | 4537 MiB | 运行中 | X-VLA k=0.7 seed43 (PID 868193) |
| 3 | 4064 MiB | 运行中 | X-VLA k=0.5 seed43 (PID 894197) |

**2 个 GPU 空闲 (cuda:0, cuda:1)**，但因为 RTX 4090D 只有 24GB，无法跑 OpenVLA 7B eval。

---

### X-VLA seed43 k=0.9（已完成）

**Overall SR: 97.6% (488/500)**

---

### X-VLA seed43 k=0.7（接近完成）

当前进度：Task 9/9（最后一个 task），Ep 9/50，目前 9/9 全 SUCCESS。

已完成 task 的 per-task SR：

| Task | Description | SR |
|------|------------|-----|
| 0 | alphabet soup | 49/50 (98.0%) |
| 1 | cream cheese | 0/50 (0.0%) |
| 2 | salad dressing | 50/50 (100.0%) |
| 3 | bbq sauce | 42/50 (84.0%) |
| 4 | ketchup | 17/50 (34.0%) |
| 5 | tomato sauce | 47/50 (94.0%) |
| 6 | butter | 9/50 (18.0%) |
| 7 | milk | 36/50 (72.0%) |
| 8 | chocolate pudding | 1/50 (2.0%) |
| 9 | orange juice | 运行中 (9/9 SUCCESS) |

**暂估 overall SR: ~55-58%**（tasks 0-8 合计 251/450 = 55.8%，Task 9 大概率高 SR）

---

### X-VLA seed43 k=0.5（仍在运行）

当前进度：Task 7 Ep 19/50，还剩 Task 7（31 eps）、Task 8、Task 9。

已完成 task 的 per-task SR：

| Task | Description | SR |
|------|------------|-----|
| 0 | alphabet soup | 28/50 (56.0%) |
| 1 | cream cheese | 3/50 (6.0%) |
| 2 | salad dressing | 38/50 (76.0%) |
| 3 | bbq sauce | 37/50 (74.0%) |
| 4 | ketchup | 20/50 (40.0%) |
| 5 | tomato sauce | 28/50 (56.0%) |
| 6 | butter | 1/50 (2.0%) |
| 7 | milk | 运行中 |

**暂估 overall SR: ~40-45%**（tasks 0-6 合计 155/350 = 44.3%）

---

### 关键发现

对比 k=0.9 (97.6%)，k=0.7 和 k=0.5 性能显著下降：
- **Task 1 (cream cheese)** 和 **Task 6 (butter)** 在 k=0.7/k=0.5 下几乎完全崩溃（0-2%），但 k=0.9 下分别为 100% 和 100%
- **Task 8 (chocolate pudding)** k=0.7 仅 2%（k=0.9 为 96%）
- 降幅非线性：k=0.9→k=0.7 从 97.6% 骤降至 ~56%，说明某些 vision tokens 对特定 task 至关重要

k=0.7 预计约 15 分钟内完成，k=0.5 约 40-50 分钟。

---
