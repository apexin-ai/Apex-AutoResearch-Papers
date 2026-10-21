# code d146 oom verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-oom-verify_20260519T145726_result.json`
- **Structured JSON:** [`0210bed2b1ab816160c3.json`](../../sessions/02/0210bed2b1ab816160c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**训练未启动，不是 OOM 问题，而是启动命令本身失败。**

### 详情

| 项目 | 状态 |
|------|------|
| Config batch_size | **未修改** — 仍是 `per_device_batch_size: 4`（预期改为 2） |
| Config accumulation | `gradient_accumulation_steps: 4`（正确） |
| GPU 显存 | 0 MiB / 97887 MiB — 空闲，无进程 |
| 训练进度 | **从未开始** — step 0/500 |
| 错误 | `bash: line 1: --config: command not found`，EXIT_CODE=127 |

### 根因分析

`d146_pipeline.sh` 脚本本身正确（`$PYTHON $SCRIPT_PY --config ...`），python3 和 train_grpo.py 也都存在。但日志显示 `$PYTHON` 和 `$SCRIPT_PY` 变量未展开，导致命令变成了裸 `--config ...`。

推测：tmux session 不是通过 `bash d146_pipeline.sh` 启动的，而是逐行发送命令，变量定义行未被执行或在不同 shell 上下文中丢失。

### 需要修复两件事

1. **Config 未改**：`per_device_batch_size` 仍为 4，需改为 2
2. **启动方式**：用 `bash /root/solver-trace-ablation/scripts/d146_pipeline.sh` 整体执行脚本，而非拆行发送

---
