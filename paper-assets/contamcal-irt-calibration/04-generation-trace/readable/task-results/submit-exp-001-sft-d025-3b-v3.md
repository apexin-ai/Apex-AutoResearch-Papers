# submit exp 001 sft d025 3B v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_001_sft_d025_3B_v3_20260515T161027_result.json`
- **Structured JSON:** [`e05004785e1f410ee197.json`](../../sessions/e0/e05004785e1f410ee197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **exp_001_sft_d025_3B_v3** 已在 GPU 5 上启动，PID 589763，占用 7698 MiB
- tmux session: `exp001_d025_3B_v3`
- 训练数据: 54133 samples, 3384 steps
- lora-alpha=32, seed=42, lr=5e-5
- 输出目录: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42`
- Registry 已更新为 RUNNING

注意：脚本不接受 `--gpu` 参数（任务描述中有此参数），GPU 选择完全通过 `CUDA_VISIBLE_DEVICES=5` 控制。

---
