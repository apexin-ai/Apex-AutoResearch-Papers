# analysis get 204 eval results

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_get_204_eval_results_20260515T001652_result.json`
- **Structured JSON:** [`f85d694b565145b5be86.json`](../../sessions/f8/f85d694b565145b5be86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。205 样本（比预期多 1，可能有重复），193 条有效（双侧都成功执行）。

## MVP v4 全量评估结果

### All samples (both executed, N=193)

| 指标 | 结果 | 阈值 | 判定 |
|------|------|------|------|
| **C1** disagree_rate | **39.9%** (77/193) | >=10% | **PASS** |
| **C2** diagnostic_rate | **87.0%** (67/77) | >=40% | **PASS** |
| **C3** error_types | **3 types** | >=2 | **PASS** |
| **C4** targeted_vs_blind | **+7.2pp** (T:61/97 B:54/97) | >5pp | **PASS** |
| **C5** localization | **85.4%** (35/41) | >=60% | **PASS** |

### Excluding GT=Unknown (N=127)

| 指标 | 结果 | 阈值 | 判定 |
|------|------|------|------|
| **C1** disagree_rate | **35.4%** (45/127) | >=10% | **PASS** |
| **C2** diagnostic_rate | **84.4%** (38/45) | >=40% | **PASS** |
| **C3** error_types | **2 types** | >=2 | **PASS** |
| **C4** targeted_vs_blind | **-1.7pp** (T:34/59 B:35/59) | >5pp | **FAIL** |
| **C5** localization | **89.3%** (25/28) | >=60% | **PASS** |

### 总结

**MVP RESULT: 5/5 PASS → PROCEED**（All-mode 全过）。

Excl-Unknown 模式下 C4 FAIL（targeted 修复率反而低于 blind 1.7pp），但主判定基于 All-mode，整体通过。

repair_only.py 仍在运行，结果文件尚未生成。

---
