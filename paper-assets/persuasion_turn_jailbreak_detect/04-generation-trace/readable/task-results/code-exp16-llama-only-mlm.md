# code exp16 llama only mlm

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-llama-only-mlm_20260520T000909_result.json`
- **Structured JSON:** [`3549d42dbe5195841d85.json`](../../sessions/35/3549d42dbe5195841d85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已在 GPU 2 上正常运行。

**汇报**:
- **Llama 数据**: 251 jailbreak + 250 benign = 501 条对话
- **Splits**: train 350 (jb=175, bn=175) / val 74 (jb=37, bn=37) / test 77 (jb=39, bn=38)
- **训练脚本**: `scripts/exp16_llama_only_mlm.sh`，Stage 1 MLM DAPT → Stage 2 GRU，seed 42，CUDA_VISIBLE_DEVICES=2
- **tmux session**: `exp16_llama_mlm`
- **GPU 2 状态**: 99% utilization, 20613 MiB 已用，MLM Stage 1 进行中 (Epoch 1, step 100/173, loss 从 11.66 降到 9.36)
- **Checkpoint 输出**: `checkpoints/exp16_llama_only_mlm/`
- **日志**: `logs/exp16_llama_only_mlm.log`

---
