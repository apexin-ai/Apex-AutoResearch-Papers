# analysis exp 025 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_025_bootstrap_ci_20260516T190329_result.json`
- **Structured JSON:** [`1ea81b712faffa5c2bc5.json`](../../sessions/1e/1ea81b712faffa5c2bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 结果

| Pair | AUC | 95% CI | Perm p | CI lower > 0.60? |
|------|-----|--------|--------|-------------------|
| 0v1 | 0.9876 | [0.9851, 0.9900] | 0.0001 | **PASS** |
| 1v2 | 0.8047 | [0.7934, 0.8162] | 0.0001 | **PASS** |
| **2v3** | **0.6544** | **[0.6401, 0.6688]** | **0.0001** | **PASS** |
| 3v4 | 0.5500 | [0.5340, 0.5657] | 0.0001 | FAIL |
| 4v5 | 0.5284 | [0.5122, 0.5443] | 0.0010 | FAIL |

**K\*\_CI = 3**。2v3 CI lower = 0.6401 > 0.60 已确认，permutation p < 0.001 全部显著。Registry 已更新 bootstrap_ci 字段。

---
