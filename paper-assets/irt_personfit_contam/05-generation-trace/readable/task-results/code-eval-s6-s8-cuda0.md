# code eval s6 s8 cuda0

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-s6-s8-cuda0_20260521T082927_result.json`
- **Structured JSON:** [`74cc2a03040a05f65c91.json`](../../sessions/74/74cc2a03040a05f65c91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s7 尚未 eval。汇总已有结果：

## Eval 结果汇总

| Condition | Accuracy | lz* | theta_mle | n_items |
|-----------|----------|-----|-----------|---------|
| clean_s1 | 0.6787 | 9.468 | -0.0987 | 14042 |
| clean_s2 | 0.6789 | 7.054 | -0.0842 | 14042 |
| clean_s3 | 0.6783 | 9.529 | -0.1068 | 14042 |
| clean_s4 | 0.6786 | 8.967 | -0.1092 | 14042 |
| clean_s5 | 0.6787 | 8.532 | -0.0875 | 14042 |
| clean_s6 | 0.6771 | 8.245 | -0.1036 | 14042 |
| clean_s7 | — | — | — | 未跑 |
| **clean_s8** | **0.6768** | **9.111** | **-0.1035** | **14042** |

**汇总统计（s1-s6, s8，共 7 seeds）：**
- Accuracy: 0.6768 ~ 0.6789，均值 ≈ 0.6782，极差 0.0021
- lz*: 7.054 ~ 9.529，均值 ≈ 8.701
- theta_mle: -0.1092 ~ -0.0842，均值 ≈ -0.0991

s7 checkpoint 存在但未 eval。需要我继续在 cuda:0 上跑 s7 吗？

---
