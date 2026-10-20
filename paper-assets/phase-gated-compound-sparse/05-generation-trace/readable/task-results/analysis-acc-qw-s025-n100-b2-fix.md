# analysis acc qw s025 n100 b2 fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s025_n100_b2_fix_20260515T230327_result.json`
- **Structured JSON:** [`22a310e20d3f327726f9.json`](../../sessions/22/22a310e20d3f327726f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

### acc_qw_s025_n100_b2_fix (importance_s025)
- **accuracy: 17/50 = 34.0%**
- null_count: 9 (18%)
- truncated_count: 3 (6%) — 其中 3 个 truncated 同时也是 null
- wrong_count: 24 (48%)
- correct_count: 17 (34%)
- gen_length: min=74, max=8192, mean=1044, median=535
- **对比原 batch2 (2048): accuracy 34% → 34%，无变化**

null 的 9 个 problem:
`prealgebra/951`, `prealgebra/572`(truncated), `intermediate_algebra/956`, `intermediate_algebra/279`(truncated), `prealgebra/1233`(truncated), `intermediate_algebra/207`, `algebra/2253`, `algebra/1035`, `prealgebra/105`

### acc_qw_s020_n100_b2_fix (importance_s020，同类对比)
- **accuracy: 23/50 = 46.0%**
- null_count: 3 (6%)
- truncated_count: 1 (2%)
- wrong_count: 24 (48%)

### 异常/注意事项
- s025 fix 的 accuracy 与原 batch2 (2048) 完全一致（都是 17/50 = 34%），说明 max_new_tokens 从 2048→8192 对 s025 没有帮助。虽然有 3 个 truncated 问题获得了更多生成空间，但答案提取仍然失败（null），最终正确数不变。
- s025 的 null rate (18%) 远高于 s020 (6%)，说明更激进的稀疏化导致更多答案提取失败。
- s020 (46%) 显著优于 s025 (34%)，wrong_count 相同 (24)，差距主要来自 s025 更多的 null（9 vs 3）。

---
