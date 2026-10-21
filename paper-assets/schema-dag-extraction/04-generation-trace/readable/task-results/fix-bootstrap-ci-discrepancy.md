# fix bootstrap ci discrepancy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bootstrap_ci_discrepancy_20260516T022039_result.json`
- **Structured JSON:** [`cf4c1afe1287aacc03b2.json`](../../sessions/cf/cf4c1afe1287aacc03b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are on the server only. The task is complete. Here's the summary:

---

## 结果

### 差异原因
`bootstrap_ci.json`（80-pool）使用**固定分位边界**（从原始数据计算一次 Q25/Q75，bootstrap 在固定 Q1/Q4 组内重采样），而 `three_way_comparison.py` 使用**重计算分位边界**（每次 bootstrap resample 重新计算 Q25/Q75，组成员随 resample 变化）。固定边界更保守，CI 更宽。

### 统一后的三方 Δ CI（fixed boundary, B=10000）

| Group | Δ(Q4-Q1) | 95% CI | Crosses zero? |
|---|---|---|---|
| 16-rel independent | −7.42pp | [−9.40, −5.54] | No |
| 80-pool → 16-sub | −3.92pp | [−8.17, +0.38] | **Yes** |
| 80-rel controlled | +0.35pp | [−7.11, +8.33] | Yes |

### 对比原始值（re-computed boundary）

| Group | Original CI | Unified CI | 变化 |
|---|---|---|---|
| 16-rel | [−9.45, −4.49] | [−9.40, −5.54] | 略窄，仍显著 |
| 80-pool 16-sub | **[−8.62, −0.16]** | **[−8.17, +0.38]** | **跨零了** |
| 80-rel | [−9.38, +7.55] | [−7.11, +8.33] | 跨零不变 |

16-rel 不存在两个文件 CI 不一致的问题（两者都用 re-computed boundary，结果一致），但统一到 fixed boundary 后 CI 从 [−9.45, −4.49] 变为 [−9.40, −5.54]，差异很小，结论不变。

结果已保存到 `artifacts/three_way_comparison/results_unified.json`。

---
