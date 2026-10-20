# diagnose exp16 multi llm

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp16_multi_llm_20260519T203301_result.json`
- **Structured JSON:** [`ec8dbf9709d62e9bf4e4.json`](../../sessions/ec/ec8dbf9709d62e9bf4e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，以下是完整报告。

---

## exp16_multi_llm 诊断报告

### 失败直接原因

**两个独立问题叠加：**

#### 问题 1：W&B API Key 未配置（致命错误）

服务器上没有 `WANDB_API_KEY` 环境变量，也没有 `~/.wandb` 登录凭证。任何使用 `--use_wandb` 的脚本在 `wandb.init()` 时立即崩溃。

**原始报错（来自 `exp16_gpu0_recovery.log`）：**
```
File "/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/wandb_init.py", line 1530, in init
    wi.maybe_login(init_settings)
  File "/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/wandb_init.py", line 200, in maybe_login
    wandb_login._login(
  ...
  File "/root/miniconda3/lib/python3.12/site-packages/wandb/sdk/lib/wbauth/authenticate.py", line 139, in authenticate_session
    raise UsageError(
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

**受影响组件**：`exp16_gpu0_recovery.sh`（MLM 管线）在 MLM DAPT seed=42 完成后，GRU classifier 阶段因 `--use_wandb` 崩溃。后续 seed 123/456 全部未执行。

#### 问题 2：Cron 监控误判

原始 9-class 管线（PID 293493）的提交命令**遗漏了 `--use_wandb` 参数**，训练实际上在正常运行，但 Cron 系统因检测不到 W&B metrics 而判定为 "failed"。

### 各子任务状态

| 子任务 | 日志路径 | 状态 | 备注 |
|--------|----------|------|------|
| vanilla 3 seeds | `~/runs/.../exp16_vanilla_train.log` | **完成** (exit 0) | Val Acc 最高 0.8649 |
| 9-class 原始管线 | `~/runs/.../exp16_9class_train.log` | **仍在运行** (PID 293493) | seed 42/123 完成，456 进行中；无 W&B |
| 9-class GPU1 恢复 | `logs/exp16_gpu1_recovery.log` | **完成** | 设了 `WANDB_MODE=disabled`，正常 |
| MLM GPU0 恢复 | `logs/exp16_gpu0_recovery.log` | **崩溃** | DAPT seed=42 完成，GRU 阶段 wandb 报错 |
| Llama 数据生成 | `~/runs/.../exp16_llama_*.log` | **完成** (exit 0) | |

### 训练质量警告

GRU classifier 训练显示异常模式——**train loss 从 epoch 2 开始归零**，val acc 锁定在 0.9865：

```
Epoch 1/20 | Train Loss: 0.0978 | Val Loss: 0.0318 | Val Acc: 0.9865
Epoch 2/20 | Train Loss: 0.0000 | Val Loss: 0.1118 | Val Acc: 0.9865
...
Epoch 20/20 | Train Loss: 0.0000 | Val Loss: 0.1562 | Val Acc: 0.9865
```

这可能意味着：9-class DAPT 特征太强导致 GRU 分类器 1 个 epoch 即完全拟合，后续 19 个 epoch 纯过拟合（val loss 持续上升）。不一定是 bug，但值得关注。

### 修复建议

1. **MLM 管线修复**：`exp16_gpu0_recovery.sh` 需要加 `export WANDB_MODE=disabled`（和 GPU1 恢复脚本一样），然后重新运行。目前 MLM 的 3 seeds GRU classifier 阶段全部缺失。
2. **9-class 原始管线**：无需干预，正在正常运行，等 seed 456 完成即可。
3. **W&B 长期修复**：在服务器上配置 `WANDB_API_KEY`，或在所有训练脚本中默认 `WANDB_MODE=offline`。

---
