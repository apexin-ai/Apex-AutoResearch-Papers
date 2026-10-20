# code gsm8k dryrun verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k_dryrun_verify_20260515T223001_result.json`
- **Structured JSON:** [`7ef825780884cd494915.json`](../../sessions/7e/7ef825780884cd494915.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复验证通过。** 结果汇总：

1. **无 TypeError** — 脚本完整运行结束，`bootstrap_interaction_index` 返回 dict 的修复生效
2. **输出文件** — `profiling_results.json` (29KB) 已生成
3. **Bootstrap 统计量完整** — `interaction_index` 包含 `mean`, `ci_low`, `ci_high`, `median`, `median_ci_low`, `median_ci_high`, `winsorized_mean`, `skewness`, `outlier_count` 等字段，均正常填充

示例输出（`high_sparsity` @ sparsity=0.25）：
- mean=+3.056, 95%CI=[-0.400, +5.328]
- median=+4.026, winsorized_mean=+3.201, skewness=-0.808

注意：`mid_sparsity` 的 CI 为 nan，因为只有 1 个 segment 无法做 bootstrap，这是预期行为（dry-run 只有 2 个问题数据量极少）。Verdict 为 FAIL 也是因为样本量不足，不影响代码正确性判断。

---
