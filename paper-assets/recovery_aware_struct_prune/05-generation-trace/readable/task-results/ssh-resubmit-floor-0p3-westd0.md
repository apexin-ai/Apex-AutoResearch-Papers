# ssh resubmit floor 0p3 westd0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_resubmit_floor_0p3_westd0_20260523T092224_result.json`
- **Structured JSON:** [`58af6937ce4b124612e4.json`](../../sessions/58/58af6937ce4b124612e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已成功恢复运行。

**汇报**：
- **清理**: 删除了不完整的 `grpo_cka_only_20_floor_0.3/` (4.8GB 截断的 model.safetensors)
- **SKIP**: Prune 和 SFT 自动跳过（产出完好）
- **当前步骤**: Step 3/4 GRPO 训练已启动 (PID 120758, `train_grpo_v5.py`)，GPU 0 上运行
- **PID**: tmux session PID 120742, 训练进程 PID 120758
- **exp_id**: `floor_ablation_0p3_cka_only_20_v2`

GRPO 100 steps 完成后会自动进入 Step 4/4 GSM8K eval。

---
