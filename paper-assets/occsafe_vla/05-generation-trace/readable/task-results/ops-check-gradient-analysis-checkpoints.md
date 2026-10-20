# ops check gradient analysis checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_gradient_analysis_checkpoints_20260524T094437_result.json`
- **Structured JSON:** [`e3d478f3dce46003b595.json`](../../sessions/e3/e3d478f3dce46003b595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

只有 `dataset_statistics.json`，尚未产出任何 checkpoint。

## 汇总：6 条件 checkpoint 可用性

| # | 条件 | 状态 | 位置 |
|---|------|------|------|
| 1 | **Vanilla_s0** | ✅ 可用 | 34685: `/root/autodl-tmp/checkpoints/vanilla_retrain_s0/.../50000_chkpt` |
| 2 | **Full OCC_s0** | ✅ 可用 | 34685: `/root/autodl-tmp/checkpoints/full_occ_retrain_s0/.../50000_chkpt` |
| 3 | **Detach BN_s0** | ⏳ 重训中 | 10894: `ablation_occ_detach_s0_retrain/` — 目前仅有 dataset_statistics.json，尚无 checkpoint 产出 |
| 4 | **Detach+LN_s0** | ✅ 可用 | 34685 & 10894 均有: `.../detach_ln_s0/.../50000_chkpt` |
| 5 | **Random OCC_s0** | ❌ 缺失 | 两台服务器仅有 **s2**（`ablation_random_occ_s2`），**s0 不存在，需重训** |
| 6 | **Depth_s0** | ❌ 缺失 | 两台服务器均无任何 depth checkpoint，**需重训** |

**需要行动：**
- **Random OCC_s0** 和 **Depth_s0** 都需要从头重训（seed 42）
- **Detach BN_s0** 正在训练但刚开始，需等待完成后传到 34685

---
