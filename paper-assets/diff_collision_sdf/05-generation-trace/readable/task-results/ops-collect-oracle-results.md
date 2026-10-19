# ops collect oracle results

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_oracle_results_20260522T162537_result.json`
- **Structured JSON:** [`3c5bf16713771fa99842.json`](../../sessions/3c/3c5bf16713771fa99842.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

### 结果总结

| | TSR | CAR | refined_count |
|---|---|---|---|
| Baseline (no SDF) | ~0% | **83%** | N/A |
| A3 v11 (no force) | 0% | 74.5% | 0 |
| A3 + force_refine | 0% | **81.2%** | 300/step |

**结论 negative**：
1. force_refine 成功触发了 refinement（每步都 refine），确认正常 A3 中 threshold 阻止了所有 refinement
2. CAR 从 74.5% 恢复到 81.2%（+6.7pp），但仍低于无 SDF 的 baseline 83%
3. **梯度坍缩严重**：绝大多数 episode 的 max_displacement 在 1e-6~1e-10 范围，SDF decoder 输出近常数，梯度几乎为零
4. Task 1 (chocolate_pudding，SDF GT 目标物体) CAR 最差 (57.5%)，是唯一有显著 displacement 的 task（最大 0.35m），说明梯度方向在目标物体附近可能是错的——M024 坐标 bug 可能是原因

---
