# launch exp 012

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_exp_012_20260520T033036_result.json`
- **Structured JSON:** [`d0d4874ea0cb35de9816.json`](../../sessions/d0/d0d4874ea0cb35de9816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_012 状态汇报：

- **状态**: 进程存活，已在正常训练中
- **PID**: 385711（bash），385721（python, GPU 进程）
- **GPU**: cuda:0，占用 19036 MiB
- **tmux session**: `exp_012` 存在
- **训练进度**: 生成阶段 8960/35000 samples，正在推进
- **Registry**: 已从 PREPARING → RUNNING 更新

无需重启，进程一直在跑，只是 registry 状态未同步。padding_side 警告是 HuggingFace 的常规警告，不影响训练。

---
