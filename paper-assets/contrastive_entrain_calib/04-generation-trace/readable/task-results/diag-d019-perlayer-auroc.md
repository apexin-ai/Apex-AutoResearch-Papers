# diag d019 perlayer auroc

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d019-perlayer-auroc_20260518T233807_result.json`
- **Structured JSON:** [`28a798d45eca0eb42c6b.json`](../../sessions/28/28a798d45eca0eb42c6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## BASE MODEL (no LoRA)

| Layer | \|\|h\|\| mean | dot AUROC | cos AUROC |
|------:|------:|------:|------:|
| 19 | 103.9 | 0.7850 | 0.7925 |
| 20 | 114.0 | 0.8000 | 0.7975 |
| 24 | 264.6 | 0.7775 | 0.7850 |
| 27 | 411.0 | 0.7900 | 0.7875 |
| 32 | 829.3 | 0.7975 | 0.7975 |
| 33 | 978.1 | 0.7925 | 0.7925 |
| 35 | 1038.5 | **0.8050** | **0.8025** |

- Cross-layer mean cos AUROC: **0.8100**
- Best single-layer: L35 dot=0.8050, cos=0.8025

## EXP-002 (checkpoint-500)

| Layer | \|\|h\|\| mean | dot AUROC | cos AUROC |
|------:|------:|------:|------:|
| 19 | 108.8 | 0.8000 | 0.7975 |
| 20 | 120.9 | 0.7850 | 0.7825 |
| 24 | 267.6 | 0.7775 | 0.7750 |
| 27 | 419.2 | 0.7925 | 0.7950 |
| 32 | 856.2 | 0.8225 | **0.8225** |
| 33 | 1001.3 | **0.8250** | **0.8250** |
| 35 | 1183.5 | 0.8200 | 0.8200 |

- Cross-layer mean dot AUROC: **0.8200**
- Best single-layer: L33 dot=0.8250, cos=0.8250

## BASE vs EXP-002 COMPARISON

| Layer | Base cos | Exp cos | Delta |
|------:|------:|------:|------:|
| 19 | 0.7925 | 0.7975 | +0.0050 |
| 20 | 0.7975 | 0.7825 | -0.0150 |
| 24 | 0.7850 | 0.7750 | -0.0100 |
| 27 | 0.7875 | 0.7950 | +0.0075 |
| 32 | 0.7975 | 0.8225 | **+0.0250** |
| 33 | 0.7925 | 0.8250 | **+0.0325** |
| 35 | 0.8025 | 0.8200 | +0.0175 |

## 关键发现

1. **所有 7 层在 base 和 exp-002 上都有信号**（cosine AUROC 0.77-0.83），没有"噪声层"。
2. **训练没有退化信号**：没有任何层 cosine AUROC 下降超过 0.05。深层（L32/33/35）反而小幅提升。
3. **\|\|h\|\| 范围确认 norm 问题**：L19=104 vs L35=1039/1184，跨层 10x 差距。dot product 直接平均时深层完全主导。
4. **Best layer 从 L35(base) 移到 L33(exp-002)**，AUROC 0.8250。
5. **Scenario A**：所有层 cosine AUROC > 0.75，建议 R1 改用 cosine similarity 而非 raw dot product，避免 norm 主导问题。

---
