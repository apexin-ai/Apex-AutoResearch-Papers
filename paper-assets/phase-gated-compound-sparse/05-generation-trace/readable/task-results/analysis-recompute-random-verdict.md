# analysis recompute random verdict

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recompute-random-verdict_20260514T072533_result.json`
- **Structured JSON:** [`2323f4c5408abceaf043.json`](../../sessions/23/2323f4c5408abceaf043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 重算结果

| 实验 | 旧 verdict | 新 verdict | median II (high/mid/low) | median CI 重叠 |
|------|-----------|-----------|--------------------------|---------------|
| **s015** | PASS | **FAIL** | +0.093 / +0.097 / +0.103 | 完全重叠 |
| **s020** | PASS | **FAIL** | +0.292 / +0.350 / +0.276 | 完全重叠 |
| **s025** | PASS | **FAIL** | +0.818 / +0.932 / +1.363 | 完全重叠 |
| **s030** | N/A(新) | **FAIL** | +2.503 / +2.592 / +4.041 | 完全重叠 |

**根因**：旧 verdict 基于 mean CI，而 random masking 数据极端偏斜（skewness -5 到 -16），少数 outlier segment 将 mean 拉偏导致虚假 CI non-overlap。切换到 median CI 后，三个 phase 的 median II 值高度接近（无结构化 gradient），CI 完全重叠 → 正确判定 FAIL。

**注意**：首次重算脚本将 JSON 中的 mean/ci_low/ci_high 从 segment-level bootstrap 更新为了 problem-level bootstrap。median/median_ci_low/median_ci_high 和 pass_fail verdict 均正确。perplexity、phase_stats、per_problem_ii 原始数据未受影响。

---
