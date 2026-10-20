# ops check cwm8b progress and cuda0 task

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cwm8b-progress-and-cuda0-task_20260515T234348_result.json`
- **Structured JSON:** [`0af8402f5c25484dc403.json`](../../sessions/0a/0af8402f5c25484dc403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 任务 1: CWM 8B 训练进度（repo-level-cwm-8b-conda-v5）

| 指标 | 值 |
|------|-----|
| 训练步数 | **~6100 / 6633** (92%) |
| 当前状态 | 正在跑 validation（5071/9335，54%） |
| 速度 | ~12s/step（训练），~9.8 it/s（验证） |
| 最新 train loss | **0.0035** (epoch 2.74) → 稳定下降 |
| 最新 eval loss | **0.5161** (epoch 2.71) |
| 预估剩余 | ~2小时（含剩余训练步 + 验证轮） |

**Loss 趋势**: 0.0056 (ep 2.37) → 0.0053 (ep 2.40) → 0.0035 (ep 2.74)，持续下降，正常。

### 任务 2: CWM 8B ckpt-400 test eval 进度

| 指标 | 值 |
|------|-----|
| 进度 | **5040 / 9784** (51.5%) |
| running_acc | **64.8%** |
| 速度 | ~8.4 samples/min |
| 预估剩余 | ~9.4 小时 |
| 恢复样本 | 359 resumed + 4681 new |

### 任务 3: cuda:0 空闲任务建议

**GPU 状态**:
| GPU | 利用率 | 显存 |
|-----|--------|------|
| **0** | **0%** | **0 / 32607 MiB (空闲)** |
| **1** | **0%** | **0 / 32607 MiB (空闲)** |
| 2 | 96% | 21059 / 32607 MiB |
| 3 | 89% | 22527 / 32607 MiB |

**Option A — CWM 4B seed123 val sweep**: 
- checkpoints 可用: ckpt-200, 300, 400, 500, 600（共 5 个）
- 已完成 eval: 仅 `cls_seed123_ckpt200`
- **还有 4 个 checkpoint 待 eval，适合在 cuda:0 上批量跑**

**Option B — 补跑 ckpt-5600/5800**:
- 未找到任何 5600/5800 相关的 JSON 结果或运行进程
- 未找到对应 checkpoint 目录

**建议: Option A**。seed123 有 4 个未 eval 的 checkpoint（300-600），GPU 0+1 都空闲，可以并行跑两个 eval。Option B 的 checkpoint 不存在或路径不明确。

---
