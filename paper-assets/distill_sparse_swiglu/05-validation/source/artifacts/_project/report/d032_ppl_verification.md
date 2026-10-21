# D032 数据污染验证报告

## 验证目标
Registry 中 mistral_kl_s42 和 kl_sparsity30_s42_v3 的 teal_sparse_ppl 均为 8.98，高度可疑。

## 日志验证结果

### mistral_kl_s42（Mistral-7B, KL normalized, 50% sparsity）
- 日志文件：`/root/runs/distill_sparse_swiglu/eval_mistral_kl_s42.log`
- 模型：`/root/autodl-tmp/models/mistral-7b/`
- Predictor：`checkpoints/mistral_kl_s42/predictor_kl_normalized.pt`

| 指标 | 日志值 | Registry 值 | 一致？ |
|------|--------|-------------|--------|
| true_dense_ppl | 5.52 | 5.52 | ✓ |
| predictor_hard_mask_ppl | 7.30 | 7.30 | ✓ |
| teal_sparse_ppl | **8.98** | 8.98 | ✓ |
| model_level_sparsity | 0.500 | 0.5 | ✓ |

**结论：mistral_kl_s42 的 8.98 是正确值，无需修改。**

### kl_sparsity30_s42_v3（Llama-3.1-8B, KL normalized, 30% sparsity）
- 日志文件：`/root/runs/distill_sparse_swiglu/eval_kl_sparsity30_s42_v3.log`
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`
- Predictor：`checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt`

| 指标 | 日志值 | Registry 旧值 | 一致？ |
|------|--------|--------------|--------|
| true_dense_ppl | 6.12 | 6.12 | ✓ |
| predictor_hard_mask_ppl | 7.30 | 7.30 | ✓ |
| teal_sparse_ppl | **13.63** | ~~8.98~~ | ✗ 数据污染 |
| model_level_sparsity | 0.490 | 0.3 | — |

**结论：kl_sparsity30_s42_v3 的 teal_sparse_ppl 被 Mistral 的值（8.98）错误覆盖，真实值为 13.63。**

## 污染根因
两个实验的 predictor_hard_mask_ppl 恰好都是 7.30，推测在某次批量写入 registry 时，误将 mistral_kl_s42 的 eval 结果（8.98）写入了 kl_sparsity30_s42_v3 的条目。

## 修复动作
- `kl_sparsity30_s42_v3.metrics.teal_sparse_ppl`：8.98 → **13.63**（已修正）
- `kl_sparsity30_s42_v3.teal_sparse_ppl`（顶层残留字段）：8.98 → **13.63**（已修正）
- `mistral_kl_s42.metrics.teal_sparse_ppl`：8.98（正确，无需修改）

## 正确值汇总

| 实验 | 模型 | Sparsity | true_dense | hard_mask | teal_sparse |
|------|------|----------|-----------|-----------|-------------|
| mistral_kl_s42 | Mistral-7B | 50% | 5.52 | 7.30 | 8.98 |
| kl_sparsity30_s42_v3 | Llama-3.1-8B | 28.5% | 6.12 | 7.30 | 13.63 |
