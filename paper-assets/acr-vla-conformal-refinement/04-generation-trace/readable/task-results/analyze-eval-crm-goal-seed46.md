# analyze eval crm goal seed46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-goal-seed46_20260519T235724_result.json`
- **Structured JSON:** [`a450eebcabb636f35a6d.json`](../../sessions/a4/a450eebcabb636f35a6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是分析摘要：

---

## CRM Goal OOD 综合分析

### 两个实验结果

| Seed | CRM SR | 状态 |
|------|--------|------|
| seed44-r2 | **64%** | metrics 已补充 |
| seed46 | **72%** | 新完成，已注册 |

### CRM Goal OOD 汇总 (n=4)

| Seed | SR |
|------|----|
| 42 | 67% |
| 43 | 72% |
| 44 | 64% |
| 46 | 72% |
| **平均** | **68.8% ± 3.9%** |

（seed45-r2 标记 failed，不计入）

### 与 VLA-only baseline 对比

| 方法 | 平均 SR | n | Std |
|------|---------|---|-----|
| VLA-only | 69.4% | 5 | ±3.7% |
| CRM obs_only | 68.8% | 4 | ±3.9% |

### 结论

**CRM 在 Goal OOD 上效果中性。** 68.8% vs 69.4%，差异 -0.6pp，远在噪声范围内。CRM 仅在 Object+Spatial 训练，未能对 Goal suite 产生正向迁移，也未造成退化。这符合预期——Goal 任务的 action distribution 与训练分布差异较大，CRM 的校正信号不 informative。

---
