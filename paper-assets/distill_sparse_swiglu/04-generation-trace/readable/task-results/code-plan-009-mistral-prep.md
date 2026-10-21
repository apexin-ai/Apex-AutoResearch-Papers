# code plan 009 mistral prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_009_mistral_prep_20260516T022828_result.json`
- **Structured JSON:** [`e8093c40b1e0fe80ed2f.json`](../../sessions/e8/e8093c40b1e0fe80ed2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完美，checkpoint 中保存了完整训练 args。现在全部信息已齐备，整理产出。

---

## 调查结果

### 关键发现：Mistral KL downstream eval 已经跑过一次

日志 `logs/eval_mistral_kl_downstream.log` 显示该 eval **已完成**，结果：
- MMLU ≈ **0.2758**（dense: 0.6244，降幅 56%）
- GSM8K ≈ **0.0076**（dense: 0.3654，几乎归零）

结果被后续 `mistral_dense` 运行覆盖了（results.json 只剩 dense 数据）。registry 标记为 "failed" 可能是因为结果极差。如果要重跑，建议先排查结果是否属实。

### 所有路径已验证

| 资源 | 路径 | 状态 |
|------|------|------|
| Mistral 模型 | `/root/autodl-tmp/models/mistral-7b/` | OK (14GB, 32层, hidden=4096) |
| KL s42 checkpoint | `checkpoints/mistral_kl_s42/predictor_kl_normalized.pt` | OK (145MB, 32层×bottleneck128) |
| eval_benchmark.py 条件 | `mistral_kl_s42` (mode=predictor) | 已配置 |
| setup_env.sh | `/root/distill_sparse_swiglu/setup_env.sh` | OK |

---

## 命令 1：Mistral KL Downstream Eval（重跑）

```bash
source /root/distill_sparse_swiglu/setup_env.sh
cd /root/distill_sparse_swiglu

CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/eval_benchmark.py \
  --condition mistral_kl_s42 \
  --tasks all \
  --skip_ppl \
  --gpu 0 \
  --output_dir results/plan_009_mistral_kl_downstream \
  > logs/eval_mistral_kl_downstream_v2.log 2>&1
```

预计耗时 ~55 分钟（基于上次 3324s），占 1 GPU。

---

## 命令 2：Mistral KL 额外 seed 训练

原始 s42 训练参数（从 checkpoint args 提取）：

```
loss_type=kl_normalized, num_steps=1000, batch_size=4, seq_len=2048,
lr=1e-3, sparsity_target=0.5, lambda_max=1000, gradient_checkpointing=True,
dataset=wikitext-103, relaxation=gumbel, tau_start=1.0, tau_end=0.1
```

### Seed 123（GPU 0）
```bash
source /root/distill_sparse_swiglu/setup_env.sh
cd /root/distill_sparse_swiglu

CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py \
  --model_name_or_path /root/autodl-tmp/models/mistral-7b \
  --loss_type kl_normalized \
  --num_steps 1000 \
  --batch_size 4 \
  --seq_len 2048 \
  --lr 1e-3 \
  --seed 123 \
  --sparsity_target 0.5 \
  --gpu 0 \
  --log_every 10 \
  --gradient_checkpointing \
  --lambda_max 1000.0 \
  --dataset wikitext-103 \
  --output_dir checkpoints/mistral_kl_s123 \
  --wandb_run_name mistral_kl_s123
```

### Seed 456（GPU 1）
```bash
source /root/distill_sparse_swiglu/setup_env.sh
cd /root/distill_sparse_swiglu

CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python src/train.py \
  --model_name_or_path /root/autodl-tmp/models/mistral-7b \
  --loss_type kl_normalized \
  --num_steps 1000 \
  --batch_size 4 \
  --seq_len 2048 \
  --lr 1e-3 \
  --seed 456 \
  --sparsity_target 0.5 \
  --gpu 0 \
  --log_every 10 \
  --gradient_checkpointing \
  --lambda_max 1000.0 \
  --dataset wikitext-103 \
  --output_dir checkpoints/mistral_kl_s456 \
  --wandb_run_name mistral_kl_s456
```

两个 seed 可并行跑在 cuda:0 / cuda:1 上（注意 `CUDA_VISIBLE_DEVICES` 控制物理 GPU，`--gpu 0` 映射为该可见设备内的第 0 号）。

---

## 需要 Director 决策

上次 Mistral KL downstream eval 结果极差（MMLU 0.28 / GSM8K 0.008），远超 PPL 退化预期。可能原因：
1. **属实**：Mistral 的 sparse predictor 在 downstream 上退化比 PPL 更严重
2. **eval bug**：predictor mask 应用逻辑在 Mistral 上有问题（虽然代码是模型无关的）
3. **数据问题**：offline 模式下 dataset 缓存不完整

是否直接重跑，还是先诊断上次结果？

---
