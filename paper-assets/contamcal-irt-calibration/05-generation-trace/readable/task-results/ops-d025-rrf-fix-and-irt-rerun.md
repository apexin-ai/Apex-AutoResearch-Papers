# ops d025 rrf fix and irt rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d025_rrf_fix_and_irt_rerun_20260517T002046_result.json`
- **Structured JSON:** [`99ee6b6b76baabab2094.json`](../../sessions/99/99ee6b6b76baabab2094.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**执行结果：**
- `SKIP_PATTERNS` 已添加 `"old_alpha16"`，所有 alpha16 变体均被排除
- `load_eval_results` benchmark 检测从 first-model 改为 all-models union
- d025 RRF v2 重新生成: `/root/autodl-tmp/exp003/rrf_d025_v2/` (7 respondents, Llama MMLU 3/3 信号)
- Cross-family RRF v3: `/root/autodl-tmp/exp003/rrf_cross_family_v3/` (34 models, Llama 含 MMLU)
- Cross-family IRT v3: `/root/autodl-tmp/exp006/results_cross_family_irt_v3/` (3 benchmarks 完整)

**核心结论：** ARC γ 的 family-specificity 是最强的实证发现（Qwen-only 0.73 显著 → cross-family 0.00 消失），MMLU γ 跨 family 稳定 (~0.7 但 CI 含 0)，GSM8K 无信号。

---
