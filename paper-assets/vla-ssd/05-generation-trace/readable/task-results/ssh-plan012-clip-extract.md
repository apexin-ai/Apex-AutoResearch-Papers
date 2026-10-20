# ssh plan012 clip extract

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan012-clip-extract_20260516T013043_result.json`
- **Structured JSON:** [`c21e076db4a6197a3f80.json`](../../sessions/c2/c21e076db4a6197a3f80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**特征提取**：10/10 任务完成，63728 帧，354s，180 fps。每个文件 50 trajectories，cls_token + patch_mean shape (T, 1024) float16。

**RSA 结果**：

| Model | Peak RSA | CI95 |
|-------|---------|------|
| SigLIP + projector | 0.615 | — |
| **CLIP ViT-L/14** | **0.557** | [0.442, 0.660] |
| SigLIP only | 0.488 | — |
| Trained VLA | 0.488 | — |
| Untrained VLA | 0.485 | — |
| DINO | 0.388 | — |

**结论**：CLIP RSA=0.557，远高于 DINO (0.388)，接近 SigLIP+projector (0.615)。Action-relevant representational structure 是 VL pretrained encoders 的通用属性，非 SigLIP 独有。CLIP 和 SigLIP 都显著优于 vision-only 的 DINO，确认 VL pretraining 是关键因素。Projector 仍有额外增益 (0.615 vs 0.557)。

Registry 已更新为 DONE，artifact 已注册。

---
