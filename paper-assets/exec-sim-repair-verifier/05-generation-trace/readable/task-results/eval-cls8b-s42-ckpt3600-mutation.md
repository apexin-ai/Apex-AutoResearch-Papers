# eval cls8b s42 ckpt3600 mutation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt3600-mutation_20260516T011214_result.json`
- **Structured JSON:** [`6be1ba999f8b5a3af6ea.json`](../../sessions/6b/6be1ba999f8b5a3af6ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，artifact 已注册。

## 结果汇总

**CLS 8B s42-resume ckpt-3600 — Per-Mutation-Type Test Accuracy (n=9784)**

| Mutation Type | Correct | Total | Accuracy |
|---|---|---|---|
| gold | 4,459 | 4,633 | **96.24%** |
| mutation_off_by_one | 159 | 183 | **86.89%** |
| mutation_operator_swap | 2,732 | 3,357 | **81.38%** |
| mutation_return_value | 424 | 562 | **75.44%** |
| mutation_boundary_removal | 492 | 1,049 | **46.90%** |
| **OVERALL** | **8,266** | **9,784** | **84.48%** |

关键发现：
- **gold 样本**（真实 patch）识别率极高 96.24%，模型擅长判断正确修复
- **boundary_removal 最难**，仅 46.90%——边界条件移除是最具迷惑性的 mutation
- **off_by_one 出乎意料地高** 86.89%，但样本量小（n=183）
- Overall 84.48% 与已知 test 结果一致

Registry 已更新为 DONE/success，artifact 已注册。

---
