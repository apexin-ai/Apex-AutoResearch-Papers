# analysis test eval 4b rsft s44 no evi r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_4b_rsft_s44_no_evi_r2_20260523T134349_result.json`
- **Structured JSON:** [`e6d6e36515ed9abd45f3.json`](../../sessions/e6/e6d6e36515ed9abd45f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**s44 no-evi ign_f1 = 0.2671**，evidence tax = **+1.46pp**（vs with-evi 0.2525）。

**3-seed 汇总：**

| Seed | No-evi | With-evi | Tax |
|------|--------|----------|-----|
| s42 | 0.2652 | 0.2501 | +1.51pp |
| s43 | 0.2702 | 0.2503 | +1.99pp |
| s44 | 0.2671 | 0.2525 | +1.46pp |
| **Mean** | **0.2675±0.0025** | **0.2510±0.0013** | **+1.65±0.29pp** |

3 个 seed 一致显示正的 evidence tax，去掉 evidence 输出后 RE F1 平均提升 1.65pp。Registry 已更新，报告已注册。

---
