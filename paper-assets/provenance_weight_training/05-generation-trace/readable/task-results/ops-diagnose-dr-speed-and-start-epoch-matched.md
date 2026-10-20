# ops diagnose dr speed and start epoch matched

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_dr_speed_and_start_epoch_matched_20260518T081529_result.json`
- **Structured JSON:** [`b1ec3c2387f84a7893c6.json`](../../sessions/b1/b1ec3c2387f84a7893c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== D&R 诊断 ===

seed123 命令 (PID 13576, cuda:0):
  python training/pretrain_weighted.py
    --data_path data/scored_data_filtered_q05.jsonl
    --eval_data_path data/human/eval_holdout.jsonl    ← 多出
    --eval_steps 500                                   ← 多出
    --use_wandb --wandb_project provenance-weight-training  ← 多出
    --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4
    --learning_rate 5e-5 --max_length 2048 --bf16 --seed 123
    (其余参数与 seed42 一致)

seed456 命令 (PID 13654, cuda:1):
  完全相同，只是 --seed 456

差异（vs seed42）:
  1. --eval_data_path data/human/eval_holdout.jsonl (67,823 eval 样本)
  2. --eval_steps 500
  3. --use_wandb (offline 模式)
  核心训练参数全部一致（data_path、bf16、batch_size、grad_accum、max_length、lr、num_train_tokens）

根因：--eval_data_path + --eval_steps 500
  显存：加载 67K eval 样本 → +29GB（70GB vs 41GB）
  速度：每 500 步跑一轮 eval，67823 samples / batch 8 = 8477 eval batches，
        每轮 eval 耗时 ~38 min（3.7 batch/s）。6103 训练步共触发 ~12 次 eval，
        纯 eval 开销 ~7.6h。有效速度从 ~55 steps/min 降至 ~11 steps/min。
  （日志中 X/8477 的进度条是 eval 进度条，不是训练进度条，训练总步数仍是 6103）

显存: cuda:0 70,237 MiB, cuda:1 70,237 MiB

建议: Kill 并去掉 --eval_data_path、--eval_steps、--use_wandb 三个参数后重启。
      训练结果不受影响（eval 不影响模型权重），只是浪费了大量时间在 eval 上。
      seed123 当前训练进度约 step 500-1000/6103（大部分时间在跑 eval）。

=== epoch-matched ===
PID: 20387
cuda:2 显存: 41,757 MiB ✓（与 seed42 正常值一致）
进度: step 5/2533（刚启动，预热中）
tmux session: detect_remove_q05_epoch_matched_seed42
Registry: RUNNING
```

---
