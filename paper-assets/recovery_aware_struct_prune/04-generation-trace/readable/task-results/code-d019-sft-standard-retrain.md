# code d019 sft standard retrain

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d019-sft-standard-retrain_20260515T075735_result.json`
- **Structured JSON:** [`74a9e16cb1a7d6827325.json`](../../sessions/74/74a9e16cb1a7d6827325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，loss 会在 epoch 1 结束时保存到 trainer_state.json。

## 产出报告

**1. SFT 训练脚本和完整命令**
- 脚本：`/root/recovery_aware_struct_prune/src/sft_recovery.py`
- 命令：
```
python src/sft_recovery.py \
  --model_path /root/autodl-tmp/pruned_standard_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 \
  --gpu 1 \
  --num_train_epochs 2 \
  --learning_rate 2e-5 \
  --batch_size 1 \
  --gradient_accumulation_steps 8 \
  --max_seq_length 2048 \
  --logging_steps 10 \
  --seed 42
```
- 参数来源：从 `sft_rasp_20/training_args.bin` 反向确认（epochs=2, lr=2e-5, batch=1, grad_acc=8, cosine scheduler, seed=42）

**2. 训练启动确认**
- tmux session: `sft_standard_20_retrain`
- PID: 239077
- GPU: cuda:1 (00000000:C8:00.0)，占用 12622 MiB
- 数据集：7473 samples（GSM8K full train，从缓存加载）
- 总步数：1870（935 steps/epoch × 2 epochs）

**3. 初始 loss**
- 不可见：`report_to="none"` 导致 loss 不输出到日志。训练无报错，进度条正常推进，视为正常运行。

**4. 预计完成时间**
- 当前速度：~4.5 s/step
- 预计总时长：~2h 20min
- 预计完成：约 **18:30 UTC**（比任务预估的 37-40 min 慢很多，可能原始训练在不同 GPU 或不同 batch 配置下进行）

**注意**：GPU 0 上有另一个实验 `grpo_stage2_rasp_20_v3`（PID 233489, 41GB），两个实验互不干扰。

---
