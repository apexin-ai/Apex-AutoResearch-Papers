# gpu d066 beam sweep scierc analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_d066_beam_sweep_scierc_analysis_20260520T030447_result.json`
- **Structured JSON:** [`6233e0ef472835051b8f.json`](../../sessions/62/6233e0ef472835051b8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d066 SciERC Beam Sweep 状态

**k=8 constrained 仍在运行**（66/551, ~12%），ETA 约 11:50 CST（~43 分钟后）。其余 7/8 configs 全部完成。

### 7/8 Results Summary

| Config | E-F1 | R-F1 | DR% | CF% | Avg Time |
|--------|------|------|-----|-----|----------|
| k=1 unc | 66.88 | 42.95 | 2.11 | 0.0 | 2.49s |
| k=1 con | 66.88 | 42.95 | 0.0 | 0.5 | 2.93s |
| **k=2 unc** | **67.79** | **44.75** | 1.54 | 0.0 | 2.95s |
| k=2 con | 67.71 | 44.60 | 0.0 | 0.11 | 3.46s |
| k=4 unc | 67.49 | 43.72 | 1.89 | 0.0 | 3.49s |
| k=4 con | 67.22 | 43.60 | 0.0 | 0.0 | 4.07s |
| k=8 unc | 66.40 | 43.17 | 1.77 | 0.0 | 4.19s |
| k=8 con | — | — | — | — | IN PROGRESS |

### 核心发现
- **F1 呈倒 U 型**：k=2 是峰值（E-F1=67.79, R-F1=44.75），k=4/k=8 逐步下降
- **ET%=0, RV%=0**：模型已完全内化 schema 词表
- **DR% 1.5–2.1% unc → 0% con**：constrained decoding 消除所有 domain restriction 违规
- **Constrained F1 成本 ≤0.27pp**，延迟开销 ~17%
- **Pareto optimal: k=2 constrained**

已更新 registry notes + metrics，artifact 已注册。k=8 con 完成后需补充最后一行数据并将 status 改为 DONE。

---
