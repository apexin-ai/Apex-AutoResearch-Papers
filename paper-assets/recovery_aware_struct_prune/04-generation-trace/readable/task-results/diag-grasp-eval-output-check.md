# diag grasp eval output check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grasp-eval-output-check_20260515T152341_result.json`
- **Structured JSON:** [`8191479b62f2be7abdf8.json`](../../sessions/81/8191479b62f2be7abdf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了当前 run 的 log：`results/eval_grasp_n100.log`，进度 71/100，约 25 分钟后完成。

## 汇总

### 1. PID 38120 实际命令
```
python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096
```
- 没有 `--output_path`
- 没有显式 `--seed`

### 2. 结果**不会丢失**
源码分析：
- `--seed` 默认值 = **42**，不传等同于传了 `--seed 42`
- `--output_path` 为 None 时自动回退：`results/eval_pruned_graspune_20_greedy.json`
- 脚本结束时**一定会** `json.dump` 保存完整结果（含 accuracy、stderr、per-example results、eos_stats）

### 3. Log 文件状态
- 当前 run log：`results/eval_grasp_n100.log` — 71/100，~51s/it
- 50-sample checkpoint: accuracy=0.0600, eos_rate=2.00%, avg_len=4018
- 预计 ~25 min 后完成

### 4. SFT 模型确认
`/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20/` 存在，model.safetensors 12.6GB，config.json/tokenizer 齐全。

### 5. GraSP post-SFT eval 命令（待 GraSP eval 完成后执行）
```bash
cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python -u src/eval_gsm8k.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 \
  --max_samples 100 --max_new_tokens 4096 --seed 42 \
  --output_path results/eval_sft_grasp_20_n100.json \
  2>&1 | tee results/eval_sft_grasp_20_n100.log
```

需要我现在准备一个 tmux 命令等 GraSP eval 结束后自动启动 post-SFT eval 吗？

---
