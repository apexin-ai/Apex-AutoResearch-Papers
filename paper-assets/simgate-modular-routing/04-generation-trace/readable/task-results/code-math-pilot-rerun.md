# code math pilot rerun

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_math-pilot-rerun_20260515T091050_result.json`
- **Structured JSON:** [`5d16fed81dfd9a7af08a.json`](../../sessions/5d/5d16fed81dfd9a7af08a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 1. 重跑 Pilot 50 (sandbox 修复后)

| 指标 | 旧 pilot (buggy) | 重跑 (fixed) |
|------|------------------|--------------|
| Internal acc | 80.0% | 76.0% |
| Code acc | 72.0% | 72.0% |
| Empty output rate | **32%** | **2.6%** |
| Code exec rate | 82% | 78% |

Sandbox fix (auto_print_last_expr) 生效，empty output 从 32% 降到 2.6%。

### 2. Clean N=300 完整统计

| 指标 | 值 | 95% CI |
|------|-----|--------|
| Internal acc | 81.0% | [76.7%, 85.3%] |
| Code acc | 76.7% | [72.0%, 81.3%] |
| **Diff (int − code)** | **+4.3%** | **[0.0%, +8.7%]** |

- Bootstrap P(diff≤0) = 0.032
- McNemar exact p = 0.079
- Level 4 gap: +2.0%, Level 5 gap: +6.8%

Labels: no_preference=253, internal_preferred=30, det_preferred=17

### 3. CI 是否排除 0？

**否。** 95% CI 下界恰好为 0.000，未严格排除 0。McNemar p=0.079 也不显著。趋势一致（internal > code）但未达统计显著。

### 4. vs N=250 对比

| | N=250 (clean) | N=300 (clean) |
|--|---------------|---------------|
| Diff | +4.4% | +4.3% |
| CI | [−0.4%, +9.2%] | [0.0%, +8.7%] |

方向稳定，CI 略微收窄但仍含 0。加入修复后的 pilot 50 题没有改变结论方向。

---
