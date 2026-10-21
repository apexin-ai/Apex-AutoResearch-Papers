# diagnose phase1 r3 failure

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1-r3-failure_20260513T202119_result.json`
- **Structured JSON:** [`076ba0522e73978f2527.json`](../../sessions/07/076ba0522e73978f2527.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnose_phase1_r3.md`。

**根因**: 启动命令缺少 `CUDA_VISIBLE_DEVICES`，两个 GRPO 进程都加载到 GPU 0，单卡 96GB 容纳不下两套完整训练状态（~132-142 GB），在 step 25 时 GPU 显存耗尽被驱动 SIGKILL。

**三轮失败链**: r1 config 解析 bug → r2 wandb 认证问题 → r3 GPU 隔离缺失导致显存 OOM。

**最关键修复**: 启动时加 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离两个实验到不同 GPU。建议同时开 `gradient_checkpointing=True` 留安全余量。

---
