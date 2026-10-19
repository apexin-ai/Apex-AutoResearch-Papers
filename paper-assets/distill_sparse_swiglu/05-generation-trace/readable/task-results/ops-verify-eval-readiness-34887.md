# ops verify eval readiness 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-eval-readiness-34887_20260518T173758_result.json`
- **Structured JSON:** [`0b5bf59307111a111e73.json`](../../sessions/0b/0b5bf59307111a111e73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the report:

---

## Eval 环境就绪状态 (westd-34887)

### 1. Eval 环境: **就绪 (Y)**

- **Eval 脚本**: 15+ eval 脚本存在于 `/root/distill_sparse_swiglu/src/`，当前正在使用 `benchmark_eval.py`
- **HF_HUB_OFFLINE**: **不在源代码中**，而是在启动命令中通过环境变量设置 (`export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`)。当前运行的两个 eval 进程已正确设置
- **HF Cache**: `/root/autodl-tmp/.hf_cache/hub/` 包含所有需要的模型和数据集:
  - 模型: Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-14B
  - 数据集: wikitext, ai2_arc, winogrande, mmlu, gsm8k, c4, SlimPajama-6B
- **本地模型副本**: `/root/autodl-tmp/models/` 有 llama-3.1-8b, mistral-7b, qwen2.5-14b

### 2. GPU 状态: **两卡均在跑 eval**

| GPU | 任务 | 内存 | 进度 |
|-----|------|------|------|
| cuda:0 | `kl_sparsity35_s42_eval_teal` | 55371/97887 MiB | GSM8K generate_until ~37% |
| cuda:1 | `kl_sparsity45_s42_eval_teal` | 55371/97887 MiB | GSM8K generate_until ~39% |

两卡正在跑 benchmark_eval (wikitext2, arc_challenge, winogrande, mmlu, gsm8k)，预计还需 ~20-30 分钟完成 GSM8K。

### 3. Checkpoint 清单 (westd-34887)

| Sparsity | Checkpoint | Seeds |
|----------|-----------|-------|
| 30% | `kl_sparsity30_s42_v3`, `kl_30pct_s123`, `kl_30pct_s456`, `kl_sparsity30_s123`, `kl_sparsity30_s456` | 42/123/456 |
| 35% | `kl_sparsity35_s42` | 42 |
| 45% | `kl_sparsity45_s42` | 42 |
| 50% | `kl_50pct_s123`, `kl_50pct_s456`, `mvp_kl_norm_v2_s42/s123/s456` | 42/123/456 |
| 70% | `kl_sparsity70_s42` | 42 |
| BCE variants | `mvp_bce_s42/s123/s456`, `bce_isocompute_v2_s42`, `bce_isocompute_v3_s42/s123/s456` | multi |
| Compensation | `kl_comp_30pct_s42`, `kl_comp_30pct_s123` | 42/123 |
| Mistral | `mistral_kl_s42`, `mistral_kl30_s42`, `mistral_kl70_s42` | 42 |
| Qwen-14B | `qwen14b_kl30_s42`, `qwen14b_bce30_s42` | 42 |
| Ablation | `tau_ablation_fixed01`, `tau_ablation_fixed05`, `c3_coupling_oracle_s42`, `ste_baseline_s42` | 42 |

**缺少 25% 和 40% sparsity 的 checkpoint。**

### 4. c1_ablation_bce_kl_targets_s123: **实际已成功完成**

- 在 **westd-41718** 上运行（非 34887）
- Registry 标记为 `failed`，原因: `"startup recovery: process dead, no active cron monitor"` — 这是监控系统的误报
- **实际训练完成**: 1000 步，876.8s
- **Checkpoint 存在**: `westd-41718:/root/distill_sparse_swiglu/checkpoints/c1_ablation_bce_kl_targets_s123/predictor_bce_kl_targets.pt` (145MB)
- **结果**: WikiText-2 PPL = **11.71** (sparsity 0.500)，KL reference PPL = 11.79，BCE reference PPL = 22.51
- 结论: BCEwithKLtargets (11.71) ≈ KL (11.79)，成功复现 C1 causal ablation hypothesis

### 5. 需要的修复

- **无阻塞项**: eval 环境就绪，当前两个 eval 已在运行
- **Registry 更正**: c1_s123 应从 `failed` 更新为 `succeeded`
- **HF_HUB_OFFLINE 位置**: 未硬编码在脚本中，依赖启动命令传入。不影响功能但建议注意

---
