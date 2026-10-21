# ops prep cutoff evals and gradient check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_cutoff_evals_and_gradient_check_20260524T080620_result.json`
- **Structured JSON:** [`019ef37bbf8e6891458a.json`](../../sessions/01/019ef37bbf8e6891458a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan written. Here's the full report:

---

## 1. Cutoff Eval Plan

**Checkpoint status**: 50000_chkpt **不存在**，两个实验当前都在 ~40k steps，等待训练完成。

完成后 checkpoint 路径：
- `cutoff_15k_s0`: `/root/autodl-tmp/checkpoints/cutoff_15k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- `cutoff_45k_s0`: `/root/autodl-tmp/checkpoints/cutoff_45k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`

**Eval 在 westd-34685 直接跑** — LIBERO 已装在 conda env `occsafe` 中，无需跨服务器传输。当前 5 个 GPU 空闲 (2,3,5,7,8)，两个 eval 可并行。完整命令已写入 `/tmp/cutoff_eval_plan.txt`。

---

## 2. 梯度分析就绪状态

**三个 checkpoint 全部就绪且完整：**

| Checkpoint | 路径 | safetensors | 附加组件 |
|---|---|---|---|
| Vanilla (s42) | `vanilla_retrain_s0/.../50000_chkpt` | 4/4 | action_head, proprio_projector |
| Full OCC (s42) | `full_occ_retrain_s0/.../50000_chkpt` | 4/4 | action_head, proprio_projector, **occ_head** |
| Detach LN (s42) | `detach_ln_s0/.../50000_chkpt` | 4/4 | action_head, proprio_projector, **occ_head** |

**梯度分析脚本**: `/root/occsafe_vla/analysis/gradient_analysis.py` — 已存在，支持 `--condition_type occ --occ_detach true/false`。辅助绘图脚本 `plot_gradient_figure.py` 和 `plot_gradient_paper.py` 也在。

**可以立即启动**，空闲 GPU 充足。

---
