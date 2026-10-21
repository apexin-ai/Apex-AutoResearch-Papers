# analysis alpha sweep a048 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a048_s42_fp32_20260521T061354_result.json`
- **Structured JSON:** [`3d29b492a8f8a04b96eb.json`](../../sessions/3d/3d29b492a8f8a04b96eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE(success)，artifact 已注册。

## 结果摘要

| 指标 | 值 |
|------|-----|
| **PermG_fwd** | **0/8** |
| PermG_rev | 0/8 |
| DiffXCorr_fwd | 1/8 |
| DiffXCorr_rev | 1/8 |
| threshold_onset_3sigma | 0/8 |
| TY_fwd | 3/8 (C003: 低α下不可靠) |
| **K_ge3** | **1/8** |
| K_ge4 | 0/8 |
| robust_pairs | ece→distinct_1 (naive,diff,ty) |

**Drift**: distinct_2 −46.3%, distinct_3 −45.8%, ece +799.6% — 退化明显但 PermG 检测不到前导信号。

**结论**: α=0.48 PermG 0/8（盲区），与 α=0.45 一致。相变点 α_c 收窄至 **(0.48, 0.50)**，宽度从 0.05 缩至 0.02。α=0.48 处退化信号强度不足以被 permutation Granger 捕获，相变非常陡峭。

---
