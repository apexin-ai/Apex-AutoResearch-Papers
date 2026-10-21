# ops mmlu domain nmodels check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu_domain_nmodels_check_20260517T061107_result.json`
- **Structured JSON:** [`350646784eeb5906a967.json`](../../sessions/35/350646784eeb5906a967.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果明确了。

**每个 domain 的 J = 21**（全部 8 个 domain 一致）。

从 24 个候选模型中被排除的 3 个：
1. `Qwen2.5-3B_d000_s123_aligned` — 无 RRF exposure 条目
2. `Qwen2.5-3B_d000_s42_a32_aligned` — 无 RRF exposure 条目
3. `Qwen2.5-3B_d005_s42_a32_aligned` — 无 RRF exposure 条目

**排除原因**：这 3 个模型在 `/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json` 中没有对应的 RRF（Reciprocal Rank Fusion）exposure 分数，脚本中 `strip_aligned(dirname)` 去掉 `_aligned` 后缀后查 RRF 字典未命中，因此被过滤。本质是这些 checkpoint 在 RRF exposure 计算阶段未被纳入（可能是后续新增的 seed/alpha 变体，RRF 没有重算）。

---
