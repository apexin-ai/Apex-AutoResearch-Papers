# paper spatial bowl appendix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_spatial-bowl-appendix_20260528T023032_result.json`
- **Structured JSON:** [`4df49779a002c3814728.json`](../../sessions/4d/4df49779a002c3814728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`paper_switch.py` 不存在，跳过验证步骤。

已完成。在 `appendix.tex` 的 Oracle SDF Refinement Details 和 Training Details 之间插入了 `\section{Cross-Scene Validation: spatial\_bowl}`（第 223–246 行），包含：

- 说明 spatial\_bowl 用于跨场景一致性验证
- 表格：LoRA-only CAR=15.5%/TSR=50.0% vs SDF λ=0.005 CAR=17.0%/TSR=53.0%
- 结论：+1.5 pp 差异在 seed 噪声范围内（σ≈1.9 pp），SDF 冗余在跨场景设置下复现
- 简要说明 CAR 整体较低的原因（场景更复杂，5 个密集障碍物）

数据来源：registry 条目 `eval_spatial_bowl_lora_ctrl_s0` 和 `eval_spatial_bowl_sdf_s0_l005_30k`，均为单 seed（train s0, eval seed=7）、200 episodes、30K checkpoint。

---
