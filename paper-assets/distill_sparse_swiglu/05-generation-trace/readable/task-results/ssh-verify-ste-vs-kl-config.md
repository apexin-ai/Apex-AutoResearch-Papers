# ssh verify ste vs kl config

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_ste_vs_kl_config_20260520T183822_result.json`
- **Structured JSON:** [`8f38d01de3a3b2bc2999.json`](../../sessions/8f/8f38d01de3a3b2bc2999.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已收集。以下是对比结果：

---

## 训练配置对比：STE 30% vs KL+Gumbel 30%

来源：两个 checkpoint 中保存的 `vars(args)`（westd-41718）

| 参数 | STE 30% s42 | KL+Gumbel 30% s42 v3 | 一致？ |
|------|-------------|----------------------|--------|
| **model_name_or_path** | llama-3.1-8b | llama-3.1-8b | ✅ |
| **loss_type** | kl_normalized | kl_normalized | ✅ |
| **relaxation** | **ste** | **gumbel** | ❌ 有意差异 |
| **num_steps** | 1000 | 1000 | ✅ |
| **batch_size** | 4 | 4 | ✅ |
| **seq_len** | 2048 | 2048 | ✅ |
| **lr** | 1e-3 | 1e-3 | ✅ |
| **seed** | 42 | 42 | ✅ |
| **sparsity_target** | 0.3 | 0.3 | ✅ |
| **lambda_max** | 5000.0 | 5000.0 | ✅ |
| **kl_temperature** | 1.0 | 1.0 | ✅ |
| **tau_start** | 1.0 | 1.0 | ✅ |
| **tau_end** | 0.1 | 0.1 | ✅ |
| **warmup_steps** | 100 | 100 | ✅ |
| **dataset** | wikitext-103 | wikitext-103 | ✅ |
| **gradient_accumulation_steps** | 1 | 1 | ✅ |
| **gradient_checkpointing** | true | true | ✅ |
| **bottleneck_dim** | 128 | *(缺失，旧版代码)* | ✅ 实际相同 |
| **sparsity_reg_weight** | 0.1 | 0.1 | ✅ |
| **trainable params** | 75,960,320 | 75,960,320 | ✅ |

**结论：训练超参完全一致，唯一差异是 `--relaxation ste` vs `gumbel`（有意的实验变量）。**

注意：`kl_sparsity30_s42.log` 日志文件显示 `cap=1000`，那是旧版 run（非 v3）。v3 checkpoint 确认 `lambda_max=5000`。

---

## Eval 配置对比

| 参数 | STE eval (`ste_30_s42_eval`) | KL+Gumbel eval (`d030_kl30_uniform`) | 一致？ |
|------|------------------------------|--------------------------------------|--------|
| **checkpoint** | ste_30_s42/predictor_kl_normalized.pt | kl_sparsity30_s42_v3/predictor_kl_normalized.pt | — |
| **sparsity_mode** | teal_global | teal_global | ✅ |
| **allocation** | uniform | uniform | ✅ |
| **sparsity_target** | 0.3 | 0.3 | ✅ |
| **seq_len** | 2048 | 2048 | ✅ |
| **calibration_samples** | 32 | 32 | ✅ |
| **batch_size** | 8 | 8 | ✅ |
| **bottleneck_size** | 128 | 128 | ✅ |
| **tasks** | wikitext2, arc, winogrande, mmlu, gsm8k, **hellaswag, piqa** | wikitext2, arc, winogrande, mmlu, gsm8k | ⚠️ STE 多 2 个 task |

**Eval 差异**：STE eval 包含 7 个 task（含 hellaswag + piqa），KL+Gumbel eval 只有 5 个。评估框架配置本身一致。

---
