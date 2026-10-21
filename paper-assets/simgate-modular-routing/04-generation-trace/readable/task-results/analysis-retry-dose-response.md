# analysis retry dose response

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retry-dose-response_20260518T124459_result.json`
- **Structured JSON:** [`1aa507516d4037394c9b.json`](../../sessions/1a/1aa507516d4037394c9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 核心结果

| 条件 | Death Rate |
|------|-----------|
| 7B Baseline (N=1) | 51.2% |
| Retry (N=3) | 40.9% |
| **Retry (N=5)** | **43.5%** |
| Reflexion/72B | ~35% |
| Deterministic | 16.3% |

## 结论: **SUCCESS**

- **Plateau confirmed**: N=5 vs N=3 差异 = +2.6pp（<3pp 阈值），且方向相反（N=5 更高）
- **Death dominance 是结构性上限**: agent 平均消耗 4.66/5.0 次 retry 仍无法降低 death rate，说明是重复同样的致死错误
- **与 hypothesis 的偏差**: plateau 水平在 ~42%，高于预测的 35-40%，且未收敛到 reflexion/72B 的 ~35%。但这反而强化核心论点: blind retry 连 reflection-based 方法都不如，问题在于 *how* not *how many times*

**局限**: 实验只跑了 N=5，N=1/2/4 未在同一 run 收集；N=3 reference 来自另一实验。

---
