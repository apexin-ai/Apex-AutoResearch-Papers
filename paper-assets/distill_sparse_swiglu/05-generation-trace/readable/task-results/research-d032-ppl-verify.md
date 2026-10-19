# research d032 ppl verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d032_ppl_verify_20260516T050247_result.json`
- **Structured JSON:** [`f5e7b0c7b59c531757bd.json`](../../sessions/f5/f5e7b0c7b59c531757bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D032 完成。

**确认数据污染存在：** `kl_sparsity30_s42_v3` 的 `teal_sparse_ppl` 被 Mistral 的值错误覆盖。

| 实验 | 模型 | Sparsity | Registry 旧值 | 日志真实值 | 状态 |
|------|------|----------|-------------|-----------|------|
| mistral_kl_s42 | Mistral-7B | 50% | 8.98 | **8.98** | 正确 |
| kl_sparsity30_s42_v3 | Llama-3.1-8B | 28.5% | ~~8.98~~ | **13.63** | 已修正 |

已执行：
1. 从原始日志 (`eval_mistral_kl_s42.log`, `eval_kl_sparsity30_s42_v3.log`) 独立验证两个实验的真实 PPL
2. 修正 `kl_sparsity30_s42_v3` 的顶层残留字段 `teal_sparse_ppl`: 8.98 → 13.63（`metrics.teal_sparse_ppl` 已在之前的 D032 修复中被改为 13.63）
3. 报告已注册为 artifact `art_20260516_1aed77`

---
