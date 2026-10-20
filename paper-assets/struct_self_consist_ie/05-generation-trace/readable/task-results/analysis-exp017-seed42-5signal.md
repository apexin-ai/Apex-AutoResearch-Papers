# analysis exp017 seed42 5signal

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp017_seed42_5signal_20260514T194345_result.json`
- **Structured JSON:** [`546366da48c477c8bd98.json`](../../sessions/54/546366da48c477c8bd98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。seed42 N=16 的 5 信号评估结果：

**Full split (2756 instances)**:
| Signal | ρ | AUROC | ECE |
|--------|------|-------|------|
| SJ | 0.464 | 0.739 | 0.113 |
| FK | 0.457 | 0.736 | 0.107 |
| EM | 0.461 | 0.739 | 0.108 |
| voting_conf | 0.455 | 0.741 | 0.084 |
| logprob | 0.306 | 0.759 | 0.129 |

**Conditional split (2642 instances)**:
| Signal | ρ | AUROC | ECE |
|--------|------|-------|------|
| SJ | 0.460 | 0.757 | 0.085 |
| FK | 0.452 | 0.753 | 0.081 |
| EM | 0.462 | 0.759 | 0.076 |
| voting_conf | 0.398 | 0.729 | 0.074 |
| logprob | 0.319 | 0.802 | 0.092 |

N=8→N=16 结构信号 ρ 提升 +0.02~0.03，logprob 不变（Δ≈0）。Registry 已更新为 DONE/success，报告保存在 `output/exp_017_llama_conll_n16/all_signals_report.json`。

---
