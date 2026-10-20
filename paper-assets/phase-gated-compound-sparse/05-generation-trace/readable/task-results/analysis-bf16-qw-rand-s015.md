# analysis bf16 qw rand s015

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_qw_rand_s015_20260514T081651_result.json`
- **Structured JSON:** [`dd1aec8777ad9a705023.json`](../../sessions/dd/dd1aec8777ad9a705023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已全部更新。

**bf16_qw_rand_s015 结果总结：**

| Phase | Median II | Median CI | PPL(both) |
|-------|-----------|-----------|-----------|
| high  | 0.138     | [0.10, 0.21] | 4.21 |
| mid   | 0.219     | [-0.00, 0.66] | 4.61 |
| low   | 0.188     | [0.10, 0.31] | 5.48 |

- **Verdict: FAIL** — median CIs 完全重叠，无结构化 phase gradient
- **Conclusion: success** — 确认假设：random masking 不产生 phase-dependent compound interaction
- 50 problems, 52888 tokens, 0.5 GPU-hours

---
