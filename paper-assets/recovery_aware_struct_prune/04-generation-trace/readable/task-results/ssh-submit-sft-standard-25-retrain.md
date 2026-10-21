# ssh submit sft standard 25 retrain

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_sft_standard_25_retrain_20260523T163018_result.json`
- **Structured JSON:** [`cddaffe3ae0ac6f61e8c.json`](../../sessions/cd/cddaffe3ae0ac6f61e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已确认启动成功。

**汇总：**

| 项目 | 值 |
|------|-----|
| 完整命令 | `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu_id 0 --num_epochs 2 --lr 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --logging_steps 10` |
| PID | 148228 |
| tmux session | `sft_standard_25_retrain` |
| GPU 0 占用 | 86% util, 12769 MiB |
| 日志 | `~/runs/recovery_aware_struct_prune/sft_standard_25_retrain.log`（tee 缓冲延迟，内容会逐步刷出） |
| 输出目录 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25` |
| 服务器 | westd-32935 cuda:0 |

---
