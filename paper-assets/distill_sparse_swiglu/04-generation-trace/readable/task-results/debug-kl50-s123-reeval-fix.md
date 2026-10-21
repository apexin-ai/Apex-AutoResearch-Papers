# debug kl50 s123 reeval fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_kl50_s123_reeval_fix_20260517T185153_result.json`
- **Structured JSON:** [`a0038fbdd58ce17f0601.json`](../../sessions/a0/a0038fbdd58ce17f0601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已成功完成，无需修复。**

诊断结果：

1. **第一次运行失败**（`/root/runs/distill_sparse_swiglu/kl50_global_s123_reeval.log` on westd-41718）：
   - `FileNotFoundError: '/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt'`
   - 原因：实验提交到 westd-41718 但 checkpoint 只在 westd-34887（已记录为 M009）

2. **Retry 已成功**（`/root/distill_sparse_swiglu/logs/kl50_global_s123_reeval.log` on westd-41718）：
   - checkpoint 被 scp 过去后重跑成功
   - 结果已保存到 `/root/distill_sparse_swiglu/results/benchmark/kl50_global_s123_reeval/results.json`

3. **Registry 状态**：`status: DONE`, `conclusion: success`，metrics 已填入：

| Metric | 值 |
|---|---|
| wikitext2_ppl | 11.7184 |
| arc_challenge_acc_norm | 0.3635 |
| winogrande_acc | 0.6109 |
| mmlu_acc | 0.2834 |
| gsm8k_exact_match | 0.0258 |

Registry 的 `failure_reason` 字段残留了第一次失败的信息（`EXIT_CODE=1`），但 `conclusion: success` 和 metrics 表明 retry 已成功。ROADMAP 中的 `kl50_global_s123_reeval 失败诊断 + 修复重跑` 任务可以标记完成——数据已可用于 Table 2 Row 6 修正。

需要我清理 registry 的 failure_reason 字段或更新 ROADMAP 吗？

---
