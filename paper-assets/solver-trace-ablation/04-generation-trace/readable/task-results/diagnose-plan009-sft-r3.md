# diagnose plan009 sft r3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan009-sft-r3_20260514T114759_result.json`
- **Structured JSON:** [`3ed30dc740a45acbe5d8.json`](../../sessions/3e/3ed30dc740a45acbe5d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结果

**根因**：r3 命令指定了 `--wandb_project` 和 `--wandb_run`，触发 wandb 集成，但服务器上没有配置 wandb API key（无 `.netrc`，无 `WANDB_API_KEY` 环境变量）。训练在 `trainer.train()` → `WandbCallback.on_train_begin` → `wandb.init()` 时抛出 `UsageError: No API key configured`。

**r4 已修复**：r4 日志显示使用了 `WANDB_DISABLED` 环境变量禁用了 wandb，训练正常进行中（已到 step 32/500）。

**错误链**：
1. 模型加载、数据处理均正常完成
2. `trainer.train()` 启动
3. `WandbCallback.on_train_begin` → `wandb.init()` → `_login()` → 找不到 API key → `UsageError`
4. 进程退出，EXIT_CODE=1

无需进一步修复，r4 已绕过此问题。需要更新 registry notes 吗？

---
