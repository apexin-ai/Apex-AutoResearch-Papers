# analysis func error patterns

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_func-error-patterns_20260517T080634_result.json`
- **Structured JSON:** [`03dfd613453c085e7f3a.json`](../../sessions/03/03dfd613453c085e7f3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

### 关键数字

| | CLS (seed0) | CWM (seed123) | Oracle Ensemble |
|---|---|---|---|
| Accuracy | 87.78% | 87.30% | **89.84%** |

- **Error overlap**: 68.8% (192/279 errors shared)
- **Complementarity**: 31.2% (87/279 instances only one formulation gets right)
- **Agreement rate**: 95.4%

### By Mutation Type — formulation 什么时候重要

| Mutation | n | CLS | CWM | Oracle | Complementarity |
|---|---|---|---|---|---|
| **return_value** | 402 | 97.5% | 98.0% | 98.8% | **61.5%** (最高) |
| **variable_swap** | 85 | **94.1%** | 88.2% | 94.1% | 50.0% |
| **original** | 398 | 86.4% | 87.2% | 89.7% | 35.9% |
| **operator_swap** | 298 | 86.2% | 86.9% | 88.9% | 29.8% |
| **off_by_one** | 671 | 82.4% | 80.8% | 84.4% | 26.1% |
| **boundary_removal** | 36 | 91.7% | 91.7% | 91.7% | 0.0% (完全相同) |

### Cross-seed validation (4 pairs)

Oracle 89.8-90.3%, complementarity 31-40% — patterns stable.

### 意外发现

1. **Formulation 差异很小** — CLS 和 CWM 在 func-level 上 95.4% 的 instances 给出相同结果，oracle ensemble 仅提升 ~2pp。这说明在 func-level 任务上，formulation choice 影响有限。
2. **variable_swap 是 CLS 的优势区** — CLS 比 CWM 高 5.9pp，且 CWM 在此类 mutation 上没有任何独占正确的 instance (cwm_only=0)。
3. **boundary_removal 完全一致** — 两种 formulation 的预测完全相同，error overlap=100%。
4. **return_value 最高互补性** — 虽然两者都很强 (>97%), 但犯的错几乎不重叠 (complementarity=61.5%)。
5. **对 D116 framing 的含义**：func-level 上 formulation 的影响集中在特定 mutation type (variable_swap, return_value), 但总体互补性有限。design space 差异更可能在 repo-level (更复杂场景) 上凸显。

---
