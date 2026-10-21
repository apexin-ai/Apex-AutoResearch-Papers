# analysis pythia1b c4 s43 v2 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia1b_c4_s43_v2_5method_20260521T074525_result.json`
- **Structured JSON:** [`951439c71d4cb891a78d.json`](../../sessions/95/951439c71d4cb891a78d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。`generalize_pythia1b_c4_a100_s43_v2` → **DONE (success)**。

### 结果汇总

| 指标 | 值 |
|------|-----|
| PermG_fwd (FDR) | **8/8** |
| PermG_rev (FDR) | 0/8 |
| DiffXCorr_fwd (FDR) | 8/8 |
| DiffXCorr_rev (FDR) | 8/8 |
| Threshold_onset_3sigma | 0/8 |
| TY_fwd | 1/8 |
| **K≥3** | **8/8** |
| K≥4 | 1/8 |

与 parent s42（PermG 8/8, K≥3 6/8）对比，s43 v2 的 K≥3 从 6/8 提升到 8/8，信号更强。PermG 方向性清晰（forward 8/8, reverse 0/8），确认 canary → downstream 因果方向。

---
