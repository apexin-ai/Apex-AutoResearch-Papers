# ssh unified action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unified-action-probe_20260516T020715_result.json`
- **Structured JSON:** [`d5d72c47eac1a7197144.json`](../../sessions/d5/d5d72c47eac1a7197144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。统一超参 action probe 结果：

| Model | mean_R² | overall_R² | epochs |
|---|---|---|---|
| **vla_last_preaction_L19** | **0.6711** | **0.7234** | 9 |
| dino_cls | 0.6343 | 0.7012 | 17 |
| projector | 0.6298 | 0.6992 | 22 |
| vla_image_mean_L19 | 0.5986 | 0.6770 | 26 |
| clip_cls | 0.5866 | 0.6602 | 21 |

**Bootstrap pairwise (n=10000)**:
- projector ≈ dino_cls (p=0.557, NS)
- projector > clip_cls (Δ=+0.043, p<0.001)
- dino_cls > clip_cls (Δ=+0.048, p<0.001)
- projector > vla_image_mean_L19 (Δ=+0.031, p<0.001)
- vla_last_preaction_L19 > projector (Δ=+0.041, p=0.002)

**修正确认**: 之前 DINO 在不同超参下得到 0.712 和 0.814 两个不可比数字，现在统一为 0.634。CLIP 之前在宽松超参下 0.814，现在 0.587 — 差距主要来自超参差异（100ep→50ep、patience10→5、batch512→256）和 target shift（a_t→a_{t+1}）。

**产出**:
- 脚本: `/root/vla-ssd/scripts/unified_action_probe.py`
- 结果 JSON: `/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json`
- 旧脚本已移至: `/root/vla-ssd/scripts/run_clip_action_probe.py`, `run_clip_action_probe_final.py`
- Registry `plan_012_clip_vit_control` metrics 已更新

---
