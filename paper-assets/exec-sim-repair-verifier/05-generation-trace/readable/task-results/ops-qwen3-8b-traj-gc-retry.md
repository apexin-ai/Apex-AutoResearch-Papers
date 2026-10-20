# ops qwen3 8b traj gc retry

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen3-8b-traj-gc-retry_20260518T225738_result.json`
- **Structured JSON:** [`997e73ac14e9cd2814e3.json`](../../sessions/99/997e73ac14e9cd2814e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### gradient_checkpointing 原始状态
- **已启用** (`gradient_checkpointing=True`，第 188 行)
- 说明 v1 (seq8192) 在 gc 开启状态下就 OOM 了，gc+seq8192 在单卡 5090 (32GB) 上不可行

### v2 (gc=True + seq4096) 训练状态
**已完成**，GPU 0 当前空闲 (0MiB)。训练结果：

| 指标 | 值 |
|---|---|
| 总步数 | 147 (3 epochs × 49 steps) |
| train loss (step 50) | 1.4515 |
| train loss (step 100) | 0.1455 |
| grad_norm (step 100) | 0.269 |
| eval_loss | **NaN** (所有 epoch) |
| checkpoints | checkpoint-98, checkpoint-147, best/ |

### 问题
1. **eval_loss=NaN** — 所有 3 个 epoch 的 eval_loss 都是 NaN，导致 `best_metric=Infinity`，`best_model_checkpoint=null`。`best/` 目录存在但可能不是基于有效 metric 选出来的。这需要排查 eval 数据处理逻辑。
2. **无需代码修改** — gc 已经是 True，seq4096 已经跑完。

### 最终确定的配置
- `gradient_checkpointing=True`
- `max_seq_length=4096`

### 最终训练命令（供主 Agent 用 submit_training_job 提交）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python train_traj_verifier.py --data_dir data/swebench_full/ --model_name /root/autodl-tmp/models/Qwen/Qwen3-8B --output_dir /root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/ --run_name qwen3-8b-traj-repo --seed 42 --max_seq_length 4096 --batch_size 1 --grad_accumulation 8 --lr 2e-4 --epochs 3 --lora_rank 16 --lora_alpha 32 --no_wandb
```

### 建议主 Agent 关注
- v2 训练已完成，无需重新提交，除非要清掉 output_dir 重跑
- **eval_loss=NaN 需要调查**：可能是 eval 数据 tokenization 问题（label 全 -100 导致 loss 计算返回 NaN），会影响 best checkpoint 选择的可靠性
- 如果需要重跑 seq8192，可能需要 QLoRA (4-bit 量化) 或双卡并行，单卡 5090 gc+seq8192 无法 fit

---
