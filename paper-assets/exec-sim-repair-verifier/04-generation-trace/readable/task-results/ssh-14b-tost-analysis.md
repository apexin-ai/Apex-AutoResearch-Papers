# ssh 14b tost analysis

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-tost-analysis_20260523T080227_result.json`
- **Structured JSON:** [`0bf746a92f395852a0ff.json`](../../sessions/0b/0bf746a92f395852a0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B Clustered Bootstrap TOST 结果

| 指标 | 值 |
|------|-----|
| Observed mean diff (CLS−CWM) | **+0.423pp** |
| 95% CI | [−0.455, +1.315]pp |
| Bootstrap SE | 0.458pp |
| TOST 90% CI | [−0.320, +1.176]pp |
| TOST p-value | **0.0006** |
| Equivalent (±2pp) | **YES** |
| Clusters | 114 |
| Total observations | 5,670 (3 seeds × 1,890) |

Per-seed breakdown:
- s42: CLS 89.21% vs CWM 89.26%, diff = −0.05pp
- s123: CLS 90.79% vs CWM 88.99%, diff = +1.80pp
- s456: CLS 89.79% vs CWM 90.26%, diff = −0.48pp

90% CI 完全落在 ±2pp SESOI 内，TOST p=0.0006，等价性成立。结果已保存到 `/root/autodl-tmp/eval_results/14b_tost_bootstrap.json`。

---
