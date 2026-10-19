# check scienceworld sft pid

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scienceworld_sft_pid_20260524T221456_result.json`
- **Structured JSON:** [`0bda0c3a547c72d1af57.json`](../../sessions/0b/0bda0c3a547c72d1af57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

| 项目 | 值 |
|------|-----|
| **PID** | 168770 |
| **运行时长** | ~2:45（启动于 May 25 06:12） |
| **tmux session** | `scienceworld_sft_bjb1` |
| **GPU 占用** | cuda:0, 550 MiB |
| **W&B run ID** | **无** — 脚本 `sft_train_v3.py` 设置了 `report_to="none"`，未对接 W&B |
| **output_dir** | `/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/`（当前为空，尚未保存 checkpoint） |

训练命令：
```
python scripts/sft_train_v3.py \
  --model_path /root/autodl-tmp/models/Qwen/Qwen3-1___7B \
  --data_path data/scienceworld_sft_train.jsonl \
  --val_path data/scienceworld_sft_val.jsonl \
  --output_dir /root/autodl-tmp/checkpoints/scienceworld_sft_bjb1 \
  --num_train_epochs 2 --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 16 --learning_rate 5e-6 \
  --lr_scheduler_type cosine --max_seq_length 16384 \
  --warmup_ratio 0.05 --save_steps 112 --seed 42
```

`RAGEN/wandb/run-20260524_161721-33j24s39` 是昨天的旧 run（ID: `33j24s39`），与当前 SFT 训练无关。

---
