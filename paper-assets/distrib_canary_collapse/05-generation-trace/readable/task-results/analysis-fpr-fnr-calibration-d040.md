# analysis fpr fnr calibration d040

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fpr-fnr-calibration-d040_20260515T155510_result.json`
- **Structured JSON:** [`6febcf36758e4432f8c3.json`](../../sessions/6f/6febcf36758e4432f8c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出摘要：

**FPR 表（α=0.0 null control, 8 pairs, seed=42）**

| K (method threshold) | FPR | 假阳性 pairs |
|---|---|---|
| ≥1/5 | 1.000 | 8/8 |
| ≥2/5 | 0.750 | 6/8 |
| ≥3/5 | 0.375 | 3/8 |
| ≥4/5 | 0.000 | 0/8 |
| ≥5/5 | 0.000 | 0/8 |

**FNR 关键行（α=1.0, 对 6 个 ground truth ROBUST pairs）**
- K=4, S=3（推荐配置）: FNR_robust = 0.0（6/6 全部检出）
- K=5, S=3: FNR_robust = 0.5（只检出 3/6）
- K=5, S=4: FNR_robust = 0.667（只检出 2/6）

**推荐配置 4/5 methods, 3/4 seeds** 在可用数据上实现完美分离：FPR=0, FNR_robust=0。降至 3/5 会引入 FPR=0.375。

文件已写入 `artifacts/D040/data/fpr_fnr_calibration.json` 并注册为 `art_20260515_e63a07`。

---
