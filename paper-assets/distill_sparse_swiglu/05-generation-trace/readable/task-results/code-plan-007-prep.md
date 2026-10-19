# code plan 007 prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_007_prep_20260516T015954_result.json`
- **Structured JSON:** [`fe4ab6db7ede47e528d0.json`](../../sessions/fe/fe4ab6db7ede47e528d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。以下是完整分析。

---

## 代码审查结果

### 现有脚本

| 脚本 | 用途 | `--gpu` | 适用条件 |
|------|------|---------|---------|
| `lm_eval_sparse.py` | 加载 predictor → TEAL global mask → lm-eval | **无（硬编码 cuda:0）** | KL/STE/BCE（需要 predictor） |
| `lm_eval_teal.py` | 训练无关的 activation-magnitude masking → lm-eval | ✅ | vanilla TEAL |
| `benchmark_eval.py` | 通用脚本，支持所有模式 | ✅ | 全部（predictor / baseline / dense） |

### Checkpoint 验证

全部存在且 key 兼容（`ckpt["predictors"]`）：

| Condition | Checkpoint 路径 | 文件名 |
|-----------|---------------|--------|
| KL 50% (已完成) | `checkpoints/mvp_kl_norm_v2_s42/` | `predictor_kl_normalized.pt` |
| KL 30% | `checkpoints/kl_sparsity30_s42_v3/` | `predictor_kl_normalized.pt` |
| KL 70% | `checkpoints/kl_sparsity70_s42/` | `predictor_kl_normalized.pt` |
| STE 50% | `checkpoints/ste_baseline_s42/` | `predictor_kl_normalized.pt` |
| BCE iso-compute 50% | `checkpoints/bce_isocompute_v2_s42/` | `predictor_bce.pt` |
| TEAL 50% | 无需 checkpoint | — |
| WINA 50% | 无需 checkpoint | — |

### 当前 GPU 状态

- **GPU 0** (PID 191340): `lm_eval_sparse.py` — **KL 30%** 正在跑 → `results/lm_eval_kl_30pct`
- **GPU 1** (PID 190835): `lm_eval_teal.py` — **TEAL 50%** 正在跑 → `results/lm_eval_teal_50pct`

### 关键问题

1. **`lm_eval_sparse.py` 硬编码 `cuda:0`** — 无法利用双 GPU 并行跑两个 predictor 条件。解决方案：后续条件改用 `benchmark_eval.py`（有 `--gpu` 参数），或加 `CUDA_VISIBLE_DEVICES` 环境变量。
2. **WINA 无专用 lm-eval 脚本** — `benchmark_eval.py --baseline_mode wina` 可直接支持。
3. **few-shot 一致性**：`lm_eval_sparse.py` 的 `--num_fewshot` 默认 None（用 lm-eval task 自带默认值），`benchmark_eval.py` 显式设置了 ARC-c=25, WG=5, MMLU=5, GSM8K=8。GSM8K 可能有差异（lm-eval 默认可能是 5-shot vs benchmark_eval 的 8-shot）。建议统一使用 `benchmark_eval.py`。

---

## 执行计划

推荐统一用 `benchmark_eval.py`（`--sparsity_mode teal_global`），有 `--gpu` 支持且标准化 few-shot。

### 当前正在跑（Round 1，预计还需 ~30-40 min）

| GPU | 条件 | 状态 |
|-----|------|------|
| 0 | KL 30% | 🔄 运行中 |
| 1 | TEAL 50% | 🔄 运行中 |

### Round 2（Round 1 完成后）

```bash
# KL 70% — GPU 0
cd /root/distill_sparse_swiglu && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python -u src/benchmark_eval.py \
  --exp_id kl_70pct_s42 \
  --checkpoint checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global \
  --sparsity_target 0.7 \
  --tasks arc_challenge,winogrande,mmlu,gsm8k \
  --gpu 0 \
  > results/lm_eval_kl_70pct.log 2>&1 &

# STE 50% — GPU 1
CUDA_VISIBLE_DEVICES=1 nohup python -u src/benchmark_eval.py \
  --exp_id ste_50pct_s42 \
  --checkpoint checkpoints/ste_baseline_s42/predictor_kl_normalized.pt \
  --sparsity_mode teal_global \
  --sparsity_target 0.5 \
  --tasks arc_challenge,winogrande,mmlu,gsm8k \
  --gpu 0 \
  > results/lm_eval_ste_50pct.log 2>&1 &
```

### Round 3（Round 2 完成后）

```bash
# BCE iso-compute 50% — GPU 0
CUDA_VISIBLE_DEVICES=0 nohup python -u src/benchmark_eval.py \
  --exp_id bce_isocompute_50pct_s42 \
  --checkpoint checkpoints/bce_isocompute_v2_s42/predictor_bce.pt \
  --sparsity_mode teal_global \
  --sparsity_target 0.5 \
  --tasks arc_challenge,winogrande,mmlu,gsm8k \
  --gpu 0 \
  > results/lm_eval_bce_50pct.log 2>&1 &

# WINA 50% — GPU 1
CUDA_VISIBLE_DEVICES=1 nohup python -u src/benchmark_eval.py \
  --exp_id wina_50pct \
  --baseline_mode wina \
  --sparsity_target 0.5 \
  --tasks arc_challenge,winogrande,mmlu,gsm8k \
  --gpu 0 \
  > results/lm_eval_wina_50pct.log 2>&1 &
```

### 汇总表

| # | 条件 | 脚本 | 关键参数 | Checkpoint | 预计时间 |
|---|------|------|---------|-----------|---------|
| 1 | KL 30% | lm_eval_sparse.py | `--sparsity_target 0.3` | `kl_sparsity30_s42_v3/predictor_kl_normalized.pt` | ~50 min (运行中) |
| 2 | TEAL 50% | lm_eval_teal.py | `--sparsity_target 0.5` | 无需 | ~50 min (运行中) |
| 3 | KL 70% | benchmark_eval.py | `--sparsity_mode teal_global --sparsity_target 0.7` | `kl_sparsity70_s42/predictor_kl_normalized.pt` | ~50 min |
| 4 | STE 50% | benchmark_eval.py | `--sparsity_mode teal_global --sparsity_target 0.5` | `ste_baseline_s42/predictor_kl_normalized.pt` | ~50 min |
| 5 | BCE 50% | benchmark_eval.py | `--sparsity_mode teal_global --sparsity_target 0.5` | `bce_isocompute_v2_s42/predictor_bce.pt` | ~50 min |
| 6 | WINA 50% | benchmark_eval.py | `--baseline_mode wina --sparsity_target 0.5` | 无需 | ~50 min |

**注意**：`CUDA_VISIBLE_DEVICES` + `--gpu 0` 组合确保每个任务用正确的物理 GPU。Round 2-3 的 4 个任务总计 ~100 min（双 GPU 并行），加上 Round 1 剩余时间，全部完成预计 ~2.5 小时。DDL 前（5/25）绰绰有余。

---
