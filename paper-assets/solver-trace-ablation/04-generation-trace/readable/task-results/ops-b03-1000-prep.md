# ops b03 1000 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_b03-1000-prep_20260515T085623_result.json`
- **Structured JSON:** [`52401f9a9ef188dff09a.json`](../../sessions/52/52401f9a9ef188dff09a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

### 检查结果

**Checkpoint 不存在。** `/root/autodl-tmp/outputs/exp1_isr_b03_s42/` 目录不存在，需从 base model 训练。

**GPU 状态：**
- GPU 0: 空闲 (0 MiB, 0%)
- GPU 1: 占用中 (80355 MiB, 89%)

**reward_mode 注意：** 你的命令模板用了 `--reward_mode execution_sta`，但 exp1_isr_b03 系列实际使用的是 `additive_bonus`（见 `grpo_additive_bonus.yaml`）。`--beta` 参数的帮助文档也明确说 "used with additive_bonus mode"。应该用 `additive_bonus`。

### 提交命令（GPU 0，从 base model 开始，1000 步）

```bash
export CUDA_VISIBLE_DEVICES=0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/solver-trace-ablation

python3 scripts/train_grpo.py \
  --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --reward_mode additive_bonus \
  --output_dir /root/autodl-tmp/outputs/exp1_isr_b03_s42_1000 \
  --num_steps 1000 \
  --beta 0.3 \
  --seed 42 \
  --no_wandb
```

**C002 合规**：用 `export CUDA_VISIBLE_DEVICES=0`，不是 inline 赋值。提交后需 `nvidia-smi` 确认只占 GPU 0。

---
