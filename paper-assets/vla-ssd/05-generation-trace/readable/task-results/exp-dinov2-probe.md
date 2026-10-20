# exp dinov2 probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dinov2-probe_20260515T071343_result.json`
- **Structured JSON:** [`0c5c68ec125069b82c38.json`](../../sessions/0c/0c5c68ec125069b82c38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，结果符合预期：

| 实验 | Spearman ρ | R² | MAE |
|------|-----------|-----|------|
| **Control D (DINO-V2 temporal distance probe)** | 0.833 | 0.687 | 0.127 |
| **Control A (Oracle)** | 1.000 | 1.000 | 0.000 |

- DINO-V2 只有 1 层特征（cls_token, 1024-dim），单层 ρ=0.833
- Oracle baseline ρ=1.0，完美 ceiling，验证实验流程正确
- 产出分别在 `/root/autodl-tmp/vla-ssd/results/dinov2/temporal_distance/` 和 `/root/autodl-tmp/vla-ssd/results/oracle/oracle/`

---
