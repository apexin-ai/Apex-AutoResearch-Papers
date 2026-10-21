# code dino libero goal prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino-libero-goal-prep_20260515T164518_result.json`
- **Structured JSON:** [`11b1e4c9b4c0077a84d9.json`](../../sessions/11/11b1e4c9b4c0077a84d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Gate **PASS**。结果汇总：

| 指标 | 值 |
|------|-----|
| Mean cosine sim | **0.9600** |
| Min cosine sim | 0.9009 |
| Max cosine sim | 0.9861 |
| Gate (≥ 0.95) | **PASS** |

10 个 LIBERO-Goal task 在 t=0 时视觉高度相似，"同一 scene"假设成立。Min=0.90 说明个别 pair 有轻微差异（可能是桌面物体摆放微调），但整体均值 0.96 远超阈值。

**脚本位置与命令**：

- 视觉 gate：`/root/vla-ssd/scripts/visual_similarity_gate.py`
  ```bash
  python scripts/visual_similarity_gate.py --device cuda:1
  ```
- DINO 特征提取（LIBERO-Goal）：`/root/vla-ssd/scripts/extract_dinov2.py`
  ```bash
  python scripts/extract_dinov2.py \
    --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
    --output_dir /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/ \
    --model_path /root/autodl-tmp/vla-ssd/checkpoints/dinov2-large \
    --gpu 1
  ```
- 结果 JSON：`/root/autodl-tmp/vla-ssd/results/visual_similarity_gate.json`

---
