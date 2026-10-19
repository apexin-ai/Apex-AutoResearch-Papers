# ops s2 l01 sdf loss check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s2_l01_sdf_loss_check_20260524T045005_result.json`
- **Structured JSON:** [`28311e3d306da1c867bd.json`](../../sessions/28/28311e3d306da1c867bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## s2_l01 SDF Loss 追踪

### 当前状态
所有 4 个 run 均在正常训练中，当前 step ~23.3K / 30K (78%)。

### SDF Loss 历史

| Step 范围 | s2_l01 SDF | s2_l005 SDF | s1_l005 SDF | s1_l01 SDF | 其他均值 | 倍数 |
|-----------|-----------|------------|------------|-----------|---------|------|
| ~7K (之前) | ~0.065 | ~0.035 | ~0.035 | ~0.035 | ~0.035 | 1.86x |
| ~19K | ~0.065 | ~0.034 | ~0.034 | ~0.034 | ~0.034 | 1.91x |
| ~23.3K (当前) | **~0.067** | ~0.033 | ~0.033 | ~0.033 | **~0.033** | **2.03x** |

### 趋势判断

- **收敛/发散/持续**: **持续偏高，完全平坦**。s2_l01 的 SDF loss 从 step 7K 到 23K 一直锁定在 0.06-0.07 区间，无任何收敛趋势。
- **与其他 run 差距变化**: **轻微扩大**（1.86x → 2.03x），因为其他 run 从 0.035 缓慢收敛到 0.033，而 s2_l01 纹丝不动。
- **是否需要干预**: **No**
  - SDF loss 稳定不发散，action loss 和 ee loss 与其他 run 量级一致
  - 已完成 78%（22+ 小时），kill 浪费计算资源且不会获得新信息
  - 这很可能是 sigma=2 + lambda=0.1 组合的固有特性（SDF loss 权重高但 sigma 大导致 SDF 目标更模糊），最终需要看下游任务性能差异来判断这个配置是否有价值
  - 建议让它跑完，在 30K 时做完整的下游评估对比

---
