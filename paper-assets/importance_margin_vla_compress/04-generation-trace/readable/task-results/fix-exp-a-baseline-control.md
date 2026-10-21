# fix exp a baseline control

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_a_baseline_control_20260518T123634_result.json`
- **Structured JSON:** [`222788742d5d987b0a99.json`](../../sessions/22/222788742d5d987b0a99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动，正在运行。

**总结：**

| 项目 | 内容 |
|---|---|
| **失败原因** | `wandb.init()` 尝试在线登录但服务器没有配置 WANDB API key，抛出 `UsageError: No API key configured` |
| **修复** | 命令中添加 `WANDB_MODE=offline` 环境变量，跳过登录 |
| **exp_id** | `train_baseline_control_100k_v2` |
| **状态** | 已启动，step=50 正常训练中，loss=0.0481，sps=2.9 |

---
