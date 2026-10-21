# analysis null fpr s43 s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_null_fpr_s43_s44_20260520T080200_result.json`
- **Structured JSON:** [`269fb281a677c1a0ec39.json`](../../sessions/26/269fb281a677c1a0ec39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。从 JSON summary 中提取各 method 的 forward significant pair 数：

## α=0.0 Null FPR 三 seed 汇总

| Method | s42 | s43 | s44 | Total | 平均 FPR |
|--------|-----|-----|-----|-------|---------|
| PermG (FDR) | 0/8 | 0/8 | 0/8 | 0/24 | **0.000** |
| diff_xcorr (FDR) | 4/8 | 2/8 | 3/8 | 9/24 | **0.375** |
| threshold (3σ) | 3/8 | 1/8 | 2/8 | 6/24 | **0.250** |
| TY Granger | 1/8 | 1/8 | 0/8 | 2/24 | **0.083** |
| K≥3 consensus | 1/8 | 0/8 | 1/8 | 2/24 | **0.083** |

关键发现：
- **PermG** 是唯一 null FPR = 0 的方法，三 seed 无一假阳性
- **diff_xcorr** FPR 最高（37.5%），作为独立方法不可靠
- **threshold** FPR = 25%，同样偏高
- **TY** 和 **K≥3** FPR ≈ 8.3%，接近名义 α=0.05 水平，尚可接受
- s44 的 K≥3 假阳性来自 token_entropy→mauve（naive+diff+threshold 3/5 投票），说明 consensus 机制对 null 的抑制并非完美

---
