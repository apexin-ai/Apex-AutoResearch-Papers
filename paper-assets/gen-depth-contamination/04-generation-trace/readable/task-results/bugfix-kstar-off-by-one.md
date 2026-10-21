# bugfix kstar off by one

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_kstar-off-by-one_20260519T203108_result.json`
- **Structured JSON:** [`dac8d011b66202fe9adc.json`](../../sessions/da/dac8d011b66202fe9adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

## 修复汇总

**4 个文件，6 处 K* 计算逻辑**，全部有相同的 off-by-one bug：

| 服务器 | 文件 | 行号 | 修改 |
|--------|------|------|------|
| westd-42896 | `run_deberta_c4.py` | L202, L206 | `k_star = -1` → `0`, `k_star = k` → `k + 1` |
| cqa1-22115 | `run_deberta_upperbound.py` | L159, L161 | `kstar = -1` → `0`, `kstar = k` → `k + 1` |
| cqa1-22115 | `run_deberta_cross_transfer.py` | L207, L210 | 同上 |
| cqa1-22115 | `analyze_deberta_results.py` | L118/L121 (`pairwise_auc_bootstrap`), L143/L147 (`lgbm_kstar`) | 同上，两个函数都修复 |

**验证**：用已知数据（1v2 CI_lower=0.6696 > 0.60, 2v3 CI_lower=0.5814 < 0.60），修复后 K\*=2（旧代码报 K\*=1）。

---
