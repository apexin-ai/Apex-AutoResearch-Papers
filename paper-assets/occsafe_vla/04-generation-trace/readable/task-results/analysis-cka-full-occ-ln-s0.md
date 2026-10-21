# analysis cka full occ ln s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_full_occ_ln_s0_20260525T014618_result.json`
- **Structured JSON:** [`aaf8d9c67c1dd1534621.json`](../../sessions/aa/aaf8d9c67c1dd1534621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**CKA 分析结果 (Full OCC+LN vs Pretrained)**:

| 指标 | DINOv2 | SigLIP |
|------|--------|--------|
| Mean CKA | **0.6404** | **0.9497** |
| Min CKA | 0.2558 | 0.8479 |

**关键发现**: Full OCC+LN 的 DINOv2 表征漂移显著（mean CKA=0.64），远低于 Full OCC BN 的 ~0.96。SigLIP 保持高度相似（0.95）。这说明 LayerNorm 在全梯度流条件下会导致 DINOv2 特征大幅偏离预训练表征，而 BatchNorm 能更好地保持 DINOv2 稳定性。2×2 factorial 表征维度数据完整。

**产出文件**（服务器 westd-10894）:
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_results.json`
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.pdf`
- `/root/autodl-tmp/analysis/cka_full_occ_ln/cka_analysis.png`

---
