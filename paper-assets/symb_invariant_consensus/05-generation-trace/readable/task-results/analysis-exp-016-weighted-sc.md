# analysis exp 016 weighted sc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json`
- **Structured JSON:** [`37031b3e81fa4eac4039.json`](../../sessions/37/37031b3e81fa4eac4039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-016 完成。结果汇总：

| Method | Accuracy | vs SC (p) | vs SICA (p) |
|--------|----------|-----------|-------------|
| **SICA** (ref) | **76.49%** (615) | — | — |
| **SC / Uniform** | **76.24%** (613) | — | 0.855 |
| Inv-length-weighted | 76.74% (617) | 0.453 | 0.864 |
| Length-weighted | 75.25% (605) | 0.153 | 0.066 |
| Constraint-count (=length) | 75.25% (605) | 0.153 | 0.066 |

**结论**：
- 所有加权变体 vs SC/SICA 均不显著（p > 0.05）
- Length-weighting 反而伤害性能（-1pp），长 trace 略微不可靠
- Inverse-length 有微弱正向效果（+0.5pp），但远非显著
- 简单加权投票不能替代 SICA，同时也确认 SICA 本身相对 SC 的优势也不显著

产出已注册：报告 `art_20260516_c7cc07`，数据 `art_20260516_7eef43`。脚本在服务器 `scripts/weighted_sc_baseline.py`。

---
