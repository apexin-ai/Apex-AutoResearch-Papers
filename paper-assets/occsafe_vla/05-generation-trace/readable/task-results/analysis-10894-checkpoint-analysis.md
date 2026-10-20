# analysis 10894 checkpoint analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_10894_checkpoint_analysis_20260525T104922_result.json`
- **Structured JSON:** [`27df030a00c371d0eaa9.json`](../../sessions/27/27df030a00c371d0eaa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析全部��成（~15min 总用时，GPU 1-2）。核心发现：

---

## 综合分析结果

### 1. 梯度重分配 (Cutoff 15K 最关键发现)

| 模块 | Cutoff 15K vs Vanilla 梯度比 |
|------|---|
| **DINOv2** | **0.14x – 0.33x** (梯度死区) |
| **SigLIP** | **2.0x – 2.8x** (补偿性放大) |

早期 OCC (0-15K) 后切断 → DINOv2 gradient 几乎归零 → 模型被迫通过 SigLIP 学习。

### 2. Feature Rank 坍缩

| Condition | Deep layer eff_rank (block 21) | vs Pretrained 567 |
|---|---|---|
| Vanilla | 547 | 0.96x (正常) |
| Full OCC BN | 538 | 0.95x (正常) |
| **Full OCC LN** | **90** | **0.16x (6x 坍缩)** |
| **Cutoff 15K** | **87** | **0.15x (6x 坍缩)** |

Top-10 PC 在 Cutoff 15K 和 Full OCC LN 中捕获 **98-99%** 方差（正常应为 57%）。

### 3. LoRA 权重悖论

Cutoff 15K 的 DINOv2 LoRA norm 最小 (87.2)，但 CKA drift 最严重 (0.520)。**小权重变化导致灾难性表征漂移。**

### 4. 机制解释

- **Full OCC BN (最佳安全性)**: 持续 OCC → 特征多样性 > pretrained → 空间理解保持
- **Cutoff 15K (最差安全性)**: 早期 OCC 重塑特征 → 切断后梯度死区 → rank 坍缩 + CKA 漂移 → 空间理解丧失
- **Full OCC LN**: LayerNorm 导致 rank 坍缩，但特征仍与 pretrained 对齐 (CKA=0.96) — 集中但正确

---

**输出文件：**
- `gradient_complete/results.json` + `comprehensive_analysis.pdf`
- `lora_weight_analysis/results.json`
- `feature_rank/results.json`
- `checkpoint_analysis_summary.md`

GPU 1-3 现在空闲。如需进一步分析（如 linear probing、cross-condition CKA matrix），可以继续利用剩余 ~9.5h。

---
