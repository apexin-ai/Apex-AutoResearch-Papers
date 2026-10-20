# diagnose probe 001

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_probe_001_20260514T080733_result.json`
- **Structured JSON:** [`b1ddd884ff470c6df886.json`](../../sessions/b1/b1ddd884ff470c6df886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**probe_001 失败原因**：`wandb.errors.UsageError: No API key configured`

- 训练命令含 `--wandb`，触发 `wandb.init()`（train_probe.py:158），但 gpu-5090-2x-2 上未设置 `WANDB_API_KEY`
- 数据加载完全正常：15401/54809 windows（conf≥2），train=10634, val=2943, test=1824，`split_info.json` 已生成
- 仅在 W&B 认证阶段崩溃，训练循环未开始

**修复方案**（任选一）：
1. 重跑时去掉 `--wandb` 标志
2. 训练前 `export WANDB_API_KEY=[REDACTED] `export WANDB_MODE=offline` 离线记录

已更新 registry 的 failure_reason 和 memory.md。

---
