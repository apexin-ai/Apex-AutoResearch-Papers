# analysis a052 s42 fp32 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a052_s42_fp32_5method_20260521T070055_result.json`
- **Structured JSON:** [`3ee46a10de25918e5762.json`](../../sessions/3e/3ee46a10de25918e5762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**α=0.52 s42 fp32 — D102 5method 分析结果**

| 指标 | 值 |
|------|------|
| PermG fwd (FDR) | **3/8** |
| PermG rev (FDR) | 0/8 |
| DiffXCorr fwd (FDR) | 5/8 |
| ThresholdOnset 3sigma | **0/8** |
| TY fwd | 1/8 |
| K≥3 | **0/8** |
| K≥4 | 0/8 |

关键发现：PermG 存在方向性不对称（3 fwd / 0 rev），确认 α=0.52 已在 α_c 以上有因果信号。但 3sigma threshold onset 全部为 None（信号幅度不足 3σ），导致 K 投票无法积累到 ≥3。

旧 registry 的 threshold_onset_3sigma=8/8、K≥3=6/8 来自 pre-D102 分析（使用非 3sigma 阈值），已修正。Conclusion 维持 **success**（PermG > 0/8）。

---
