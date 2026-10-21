# fix grpo path and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grpo_path_and_launch_20260514T170649_result.json`
- **Structured JSON:** [`1d79664e748f4e4f1009.json`](../../sessions/1d/1d79664e748f4e4f1009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GRPO rasp_20 启动成功：

- **GPU 0**: python 进程 PID 221271，已占用 12488MiB 显存
- 模型加载完成，正在准备 GSM8K 数据集
- GPU 1 eval 不受影响（PID 217541，12286MiB）

**完成总结**：
1. 修复了 `run_grpo_v4.sh` 的 `MODEL_PATH` → `/root/autodl-tmp/pruned_${METHOD}_${SPARSITY}`
2. 修复了 `OUTPUT_DIR` → `/root/autodl-tmp/recovered_${METHOD}_${SPARSITY}`
3. GRPO rasp_20 训练已在 cuda:0 上启动，日志：`~/runs/recovery_aware_struct_prune/grpo_rasp_20.log`

---
