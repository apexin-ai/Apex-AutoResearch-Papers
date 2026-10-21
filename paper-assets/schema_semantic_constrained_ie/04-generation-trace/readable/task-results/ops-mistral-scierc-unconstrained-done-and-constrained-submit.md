# ops mistral scierc unconstrained done and constrained submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mistral_scierc_unconstrained_done_and_constrained_submit_20260516T052319_result.json`
- **Structured JSON:** [`b6e1696fa4a8878f52de.json`](../../sessions/b6/b6e1696fa4a8878f52de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## w6_mistral_scierc_unconstrained — DONE

| 指标 | 值 |
|------|-----|
| Total samples | 551 |
| Parse fail rate | 0.00% |
| **E_P / E_R / E_F1** | 0.2402 / 0.3156 / **0.2728** |
| **R_P / R_R / R_F1** | 0.0295 / 0.0483 / **0.0366** |
| ET_pct (非法实体类型) | 1.50% |
| RV_pct (非法关系类型) | 0.00% |
| DR_pct (悬空关系) | **56.94%** |

关键发现：Mistral-7B unconstrained 的 R_F1 极低（0.037），超过一半的预测关系引用了不在实体列表中的实体（DR=57%），说明模型生成的关系和实体之间严重不一致。

## w6_mistral_scierc_constrained — RUNNING

- 服务器: westd-16980, GPU 0
- PID: 334606, tmux session: `w6_mistral_scierc_constrained`
- 已完成 11/551 样本，xgrammar 正常工作
- 预计耗时 ~30-35 分钟（与 unconstrained 类似）

---
