# check sft alpha4 20 v2 status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sft_alpha4_20_v2_status_20260521T183312_result.json`
- **Structured JSON:** [`304e13fbbca8f4de8d1a.json`](../../sessions/30/304e13fbbca8f4de8d1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

- **PID**: 401581 → **ALIVE**
- **Python 进程** (PID 401586): 运行 ~3 分钟，CPU 254%，RSS ~2GB
- **训练进度**: 刚启动，模型已加载到 cuda:0 (CUDA_VISIBLE_DEVICES=2)，日志只有 3 行，尚未开始训练 step — 可能正在加载数据集/tokenizer 或初始化 optimizer
- **参数**: `--num_epochs 2 --lr 2e-5 --model_path pruned_alpha4_20 --output_dir sft_alpha4_20`

进程活跃且 CPU 占用正常（254% 表示多核工作中），属于训练前初始化阶段。再等几分钟应该会看到训练 step 日志输出。

---
