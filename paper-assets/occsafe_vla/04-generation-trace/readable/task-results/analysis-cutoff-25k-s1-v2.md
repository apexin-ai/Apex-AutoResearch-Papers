# analysis cutoff 25k s1 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cutoff_25k_s1_v2_20260526T225939_result.json`
- **Structured JSON:** [`b1ebb69fd782940728f9.json`](../../sessions/b1/b1ebb69fd782940728f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## cutoff_25k_s1_v2 分析结果

**Conclusion: success**

### Final Metrics (step 50000)
- action_loss: **0.0439**
- occ_loss: **0.0121**
- depth_loss: 0.0000

### Checkpoint
`/root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt`

(另有 30000 和 40000 中间 checkpoint)

### 与 parent (cutoff_25k_s0) 对比

| Metric | s0 (seed 42) | s1_v2 (seed 43) |
|--------|-------------|-----------------|
| action_loss | 0.0718 | **0.0439** |
| occ_loss | 0.0106 | 0.0121 |

- action_loss 显著低于 parent（0.0439 vs 0.0718），seed 间存在较大方差
- occ_loss 接近 parent（0.0121 vs 0.0106），说明 cutoff 行为一致
- OCC cutoff 行为符合预期：25K 时 occ_loss=0.0088（OCC ON 阶段最低点），cutoff 后 occ_loss 回升至 0.0140 (40K)，最终稳定在 0.0121 (50K)

### W&B
未检测到此实验的 W&B run（WANDB_MODE=disabled）。

---
