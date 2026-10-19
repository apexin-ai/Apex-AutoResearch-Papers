# ops fix m2 wandb resubmit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-m2-wandb-resubmit_20260513T015530_result.json`
- **Structured JSON:** [`523af2a9569a47745076.json`](../../sessions/52/523af2a9569a47745076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，汇报如下：

---

### 1. 错误原因

`train.py:275` 调用 `accelerator.init_trackers()` → `wandb.init()` 时，服务器上无 wandb API key（无 `.netrc`，无 `WANDB_API_KEY` 环境变量），导致 `wandb.errors.UsageError: No API key configured`。

### 2. 修复内容

- 在 `run_m2_early_pilot.sh` 的 `set -e` 后插入两行：
  - `export WANDB_MODE=offline` — 跳过 API key 验证，日志写本地
  - `export WANDB_DIR=/root/autodl-tmp/structfuse/wandb_logs/` — 日志存数据盘
- 创建了 `/root/autodl-tmp/structfuse/wandb_logs/` 目录
- 清理了残留的 `m2_early_pilot` tmux session（`hgate-dpo003-merged` 保留未动）

### 3. Wrapper 脚本最终版本

```bash
#!/bin/bash
# M2 Early Pilot: 3 strategies × 1 seed (42) sequential training
# Data: partial M1 (24 repos), model: Qwen2.5-Coder-3B LoRA
set -e
export WANDB_MODE=offline
export WANDB_DIR=/root/autodl-tmp/structfuse/wandb_logs/

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

DATA_DIR="/root/autodl-tmp/structfuse/m2_early_pilot_data"
OUT_BASE="/root/autodl-tmp/structfuse/checkpoints/m2_early_pilot"
MODEL="Qwen/Qwen2.5-Coder-3B"

declare -A STRATEGY_MAP
STRATEGY_MAP[random]="random"
STRATEGY_MAP[embedding]="embedding_distance"
STRATEGY_MAP[dataflow]="dataflow_aware"

for TAG in random embedding dataflow; do
    STRATEGY="${STRATEGY_MAP[$TAG]}"
    # ... 训练命令（参数未改动）...
    # dataflow 策略额外带 --dataflow-graph-file
    # 每个策略完成后清理中间 checkpoint
done
```

### 4. 就绪状态

- 脚本已修复，`WANDB_MODE=offline` 生效
- 旧 tmux session 已清理
- 训练参数未改动
- 可以重新提交

---
