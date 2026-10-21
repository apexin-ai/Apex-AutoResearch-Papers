# exp fewrel contamination check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewrel_contamination_check_20260516T122940_result.json`
- **Structured JSON:** [`2be712c9067701d0caff.json`](../../sessions/2b/2be712c9067701d0caff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

## FewRel Contamination Check 结果

| 指标 | 值 |
|------|-----|
| Train-origin (64 rels) mean acc | **74.3%** |
| Val-origin (16 rels) mean acc | **83.1%** |
| Δ (train − val) | **−8.8 pp** |
| Mann-Whitney U | 356, p=0.061 |
| Welch's t | −2.28, p=0.030 |
| Cohen's d | −0.54 |

**结论：无 contamination 证据。** 

关键 defense 论点：
1. Mann-Whitney p=0.061 > 0.05（非参数检验不显著）
2. **方向完全反转**——val-origin types 准确率反而更高。如果 contamination 存在，train-origin 应该更高
3. Val-origin types 更高的可能解释：FewRel val split 的 16 个 relations 本身语义更明确/可区分（如 "position played on team", "military rank", "constellation"）

这是对 Reviewer W-W5 Q3 的强有力反驳。结果保存在 `/root/schema-dag-extraction/artifacts/fewrel_contamination_check/results.json`，基于 19 个 80-rel 实验（比之前的 2 个实验统计功效大幅提升）。

---
