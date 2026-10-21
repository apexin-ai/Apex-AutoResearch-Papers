# code r17 weighted mean downstream

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_weighted_mean_downstream_20260523T115014_result.json`
- **Structured JSON:** [`6030b5fffc83d54a4e6d.json`](../../sessions/60/6030b5fffc83d54a4e6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出：

- **脚本**: `artifacts/r17_evidence/weighted_mean_downstream.py`
- **报告**: `artifacts/r17_evidence/weighted_mean_downstream.md`
- **JSON**: `artifacts/r17_evidence/weighted_mean_downstream.json`

关键结果：

| Metric | Uncorrected (3918 C) | Weighted-mean (1690 C) |
|--------|-----:|-----:|
| ρ | 0.9965 | 0.9988 |
| τ | 0.9600 | 0.9785 |
| Flip rate | 2.00% | 1.08% |
| Avg \|rank disp\| | 74.67 | 39.36 |
| Mean score shift | +2.116 pp | +1.772 pp |
| Cohort differential | −0.291 pp | −0.101 pp |

三个定性结论在 DEFF 校正下全部成立：(1) C%=13.5% 远超 ~5% null；(2) 排名近乎完美保留（ρ>0.998）；(3) 两个 cohort 均有正 score shift，cohort differential 在校正后从 −0.29 缩小到 −0.10 pp，方向一致。校正使分析更保守（C items 减少 57%），但不反转任何发现。

---
