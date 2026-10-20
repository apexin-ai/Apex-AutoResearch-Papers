# analysis phase diagram t10 a075 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t10_a075_s43_fp32_20260522T064055_result.json`
- **Structured JSON:** [`b6a157caafc0ebe44c12.json`](../../sessions/b6/b6a157caafc0ebe44c12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PermG=6/8，与 s42 完全一致。**

| | s42 | s43 |
|---|---|---|
| **PermG (FDR) fwd** | **6/8** | **6/8** |
| DiffXCorr fwd | 6/8 | 7/8 |
| Threshold 3σ | 0/8 | 0/8 |
| TY Granger | 2/8 | 0/8 |
| K≥3 robust | 6/8 | 4/8 |

- 训练正常完成，EXIT_CODE=0，gen_0–gen_10 完整
- Final loss=0.1734，gen_10 ppl=77.82
- K≥3 从 6/8 降至 4/8，原因是 te→d2/d3 各丢一个 naive_xcorr vote（边界效应），核心 PermG 信号不受影响
- **结论：T=10 α=0.75 的 6/8 ceiling 是 seed-robust 的**

分析已写入 `artifacts/D102_t10_a075_s43_analysis.md` 并注册。

---
