# investigate cka checkpoint exists

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_cka_checkpoint_exists_20260525T113852_result.json`
- **Structured JSON:** [`d2ead054d451523ee3b7.json`](../../sessions/d2/d2ead054d451523ee3b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### (a) 原始 checkpoint: 已删除，不可恢复

`ablation_occ_detach_s0` 的 checkpoint 目录在**两台服务器上都不存在**：
- westd-10894: `/root/autodl-tmp/checkpoints/ablation_occ_detach_s0/` → **No such file or directory**
- westd-34685: 无任何 detach 相关 checkpoint 目录

### (b) Retrain checkpoint: 存在

路径: `westd-10894:/root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt/`
- 完整模型（4 shard, ~15GB）+ LoRA adapter + action_head/occ_head/proprio_projector
- 时间戳: May 25 10:19

### (c) CKA 分析结果对比

**原始分析（灾难性漂移）— westd-34685:**
- 路径: `/root/autodl-tmp/analysis/cka/cka_results.json`
- 日期: May 24 07:57
- Condition 名: `"Detach OCC"`
- DINOv2 mean ≈ **0.539**, min ≈ 0.448
- SigLIP mean ≈ **0.312**, min ≈ 0.223
- **无 run log**，无法确认用了哪个 checkpoint 路径

**Retrain 分析（无漂移）— westd-10894:**
- 路径: `/root/autodl-tmp/analysis/cka_same_seed/cka_results.json`
- 日期: May 25 13:02
- Condition 名: `"Detach+BN"`
- DINOv2 mean ≈ **0.964**, min ≈ 0.889
- SigLIP mean ≈ **0.953**, min ≈ 0.829
- Run log **明确确认**用的是 `ablation_occ_detach_s0_retrain/.../50000_chkpt`

### (d) CKA 脚本

- 位置: `/root/occsafe_vla/analysis/cka_analysis.py`
- **无硬编码路径**，通过 `--checkpoint_paths` CLI 参数传入
- 原始分析在 westd-34685 上执行时没有保存 log，所以无法回溯当时用了哪个具体路径

### 结论

**原始 checkpoint 已被删除，无法重新分析。** CKA 数据矛盾无法通过重新跑原始 checkpoint 来解决。两个可能方向：
1. 原始训练本身可能有 bug（如 resume 导致的 batch_idx 重计数问题，见 C002 约束），retrain 修复了这个问题
2. 原始 checkpoint 可能是一个不完整或损坏的保存

---
