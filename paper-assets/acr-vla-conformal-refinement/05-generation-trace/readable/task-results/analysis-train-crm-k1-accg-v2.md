# analysis train crm k1 accg v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_train-crm-k1-accg-v2_20260517T180340_result.json`
- **Structured JSON:** [`63b75d07a860171be077.json`](../../sessions/63/63b75d07a860171be077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B tool 有问题，但已有足够信息得出结论。

---

## 实验结果总结: `train-crm-k1-accg-object-seed42-v2`

### Conclusion: **FAILED**

**根因**: W&B API key 未在 bjb2-28827 上配置，`wandb.init()` 抛出 `UsageError: No API key configured`，训练循环从未启动。

### 执行进度

| 阶段 | 状态 |
|------|------|
| 特征预计算 | 完成 (72507 samples, 5043.9s) |
| 数据加载 | 完成 (65223 cached, train=58701, val=6522) |
| 模型初始化 | 完成 (MultiScaleCRM: 327,522 params) |
| W&B init | **崩溃** |
| 训练循环 | 未执行 |

### 关键 Metrics

- **final val_loss**: N/A (训练未开始)
- **train_loss**: N/A
- **best epoch**: N/A

### Checkpoint

- **checkpoint_path**: 无。服务器上未找到任何 `.pt` / `.pth` 文件。

### 与 Parent 对比

无法对比 — 没有产出任何训练结果。Parent (fallback) val_loss=0.006505 仍为当前最优。

### 是否可用于后续 eval

**否。** 需要先修复 W&B 登录问题后重新训练。

### 修复方案

在 bjb2-28827 上执行 `wandb login` 配置 API key，或在训练命令中设置环境变量 `WANDB_API_KEY=[REDACTED]

---
