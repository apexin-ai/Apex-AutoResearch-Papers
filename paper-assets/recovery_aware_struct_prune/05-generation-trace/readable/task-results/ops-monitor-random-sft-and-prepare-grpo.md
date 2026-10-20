# ops monitor random sft and prepare grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor_random_sft_and_prepare_grpo_20260517T133115_result.json`
- **Structured JSON:** [`a58abffa72f3f4df9b60.json`](../../sessions/a5/a58abffa72f3f4df9b60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## Random SFT 完成状态

**已完成。** 由 `scoring_ablation_random` tmux session 中的 ablation 脚本执行成功（PID 710113 是一次独立的 OOM 失败尝试，与最终成功的训练无关）。

### 1. 模型路径与 Metrics

| 项目 | 值 |
|---|---|
| **SFT 模型路径** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20` |
| **train_loss** | 0.7516 |
| **训练时长** | ~38.5 min (2312s), 2 epochs, 7473 samples |
| **GSM8K accuracy (post-SFT)** | **60.0%** (120/200, greedy) |
| **EOS rate** | 99.5% |
| **模型文件** | `model.safetensors` 11.3 GB，完整 |

### 2. GRPO 启动就绪状态

| 检查项 | 状态 |
|---|---|
| `src/train_grpo_v5.py` | 存在 |
| 磁盘空间 `/root/autodl-tmp` | 66GB 可用（充足） |
| GPU cuda:1 | 当前仅 13GB 占用（ablation eval 在 cuda:0 跑），可用 |

### 3. 命令修正

提议的 GRPO 命令有两处需修正：

- **`--save_strategy no`**：该参数不是 CLI arg，脚本硬编码为 `save_strategy="steps"`。若要禁用保存，改用 `--save_steps 99999`
- **`--optim adamw_bnb_8bit`**：脚本默认值是 `adamw_8bit`，确认使用哪个

修正后的命令：
```bash
CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20 \
  --gpu 0 \
  --max_completion_length 1024 \
  --beta 0.01 \
  --temperature 0.4 \
  --repetition_penalty 1.15 \
  --format_reward_weight 0.1 \
  --gradient_checkpointing true \
  --optim adamw_8bit \
  --loss_type dapo \
  --learning_rate 1e-6 \
  --max_steps 100 \
  --save_steps 99999 \
  --reward_desert_patience 50 \
  --run_name grpo_random_20
```

### 4. 阻塞问题

- `scoring_ablation_random` tmux session 正在 cuda:0 上跑 `pruned_cka_only_20` 的 eval（进度 ~50%），不影响 cuda:1 上启动 GRPO
- 无其他阻塞

---
