# analysis a065 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a065_5method_20260521T005951_result.json`
- **Structured JSON:** [`689e270d48ff86e79e7f.json`](../../sessions/68/689e270d48ff86e79e7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved. Here's the summary:

## α=0.65 s42 fp32 — 5-Method Lead-Lag Analysis

### Summary Counts
| Method | Fwd Sig | Rev Sig |
|--------|---------|---------|
| PermG FDR | 0/8 | 0/8 |
| DiffXCorr FDR | 6/8 | 6/8 |
| ThresholdOnset (3sigma) | 0/8 | — |
| TY Granger | 4/8 | — |
| **Robust (K≥3)** | **1/8** | — |

### Per-Pair Consensus
| Pair | K | Methods |
|------|---|---------|
| TE→D1 | 1/5 | diff |
| TE→D2 | 1/5 | diff |
| TE→D3 | 2/5 | diff, ty |
| TE→mauve | 0/5 | — |
| **ECE→D1** | **3/5** | **naive, diff, ty** |
| ECE→D2 | 2/5 | diff, ty |
| ECE→D3 | 1/5 | diff |
| ECE→mauve | 2/5 | naive, ty |

### Key Observations
- **唯一 robust pair: ECE→distinct_1** (K=3, naive+diff+ty 一致显著，TY F=1939.9 p=0.0005)
- PermG 全灭 (FDR 后 0/8)，尽管 raw p-values 有 3 pairs <0.05（ECE→D1/D2/D3），FDR 校正后均 >0.05
- ThresholdOnset 全灭 — canary onset 在 gen 1-2 但 downstream 无 3sigma 突破
- DiffXCorr FDR 6/8 显著但 symmetric (fwd=rev)，方向性弱
- α=0.65 位于 sync dip 区间，K≥3 仅 1/8 与预期吻合

---
