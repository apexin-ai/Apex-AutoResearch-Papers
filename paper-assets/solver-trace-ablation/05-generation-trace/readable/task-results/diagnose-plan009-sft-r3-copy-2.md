# diagnose plan009 sft r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan009-sft-r3_20260514T114053_result.json`
- **Structured JSON:** [`a6f1d2f9cb98377e4b27.json`](../../sessions/a6/a6f1d2f9cb98377e4b27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 根因分析

崩溃原因是 **W&B API key 未配置**。模型加载、数据加载均成功，在 `trainer.train()` 启动时 W&B callback 尝试初始化登录，抛出异常：

```
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
```

与 OOM/GPU 无关，纯粹是 W&B 认证问题。

### 额外观察

日志中有一行值得注意：
> `The model is already on multiple devices. Skipping the move to device specified in args.`

说明 `device_map='auto'` 仍然生效，模型被分散到多个 GPU。虽然这次崩溃原因是 W&B，但 **即使修好 W&B，r2 的 OOM 问题仍会复现**。当前 GPU 状态：GPU0 占用 96664/97887 MiB，GPU1 占用 48090/97887 MiB。

### 修复建议

需要修两个问题：

1. **W&B 认证**：训练命令前加 `export WANDB_API_KEY=[REDACTED] W&B logging，加 `--report_to none` 参数（或 `export WANDB_MODE=disabled`）

2. **device_map 跨 GPU 问题未真正修复**：`train_sft.py` 第 195 行附近加载模型时 `device_map='auto'` 会把模型分到多卡。需要改为 `device_map={'': f'cuda:{gpu_id}'}` 或 `device_map=None` 后手动 `.to(device)`，确保模型只在 `CUDA_VISIBLE_DEVICES` 指定的单卡上。

### 是否需要改代码

需要改 `scripts/train_sft.py`：
- 检查模型加载处的 `device_map` 参数，改为单卡绑定
- 可选：加 `report_to` 参数支持，或在脚本内设 `WANDB_MODE`

要我读取 `train_sft.py` 源码定位具体修改位置吗？

---
