# code temporal label model

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_temporal-label-model_20260514T170841_result.json`
- **Structured JSON:** [`29691f14803b163e08f8.json`](../../sessions/29/29691f14803b163e08f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Registry 状态修复**
- `tlm-probe-comparison`: PREPARING → DONE ✓
- `temporal-label-model`: 新建并注册为 DONE ✓（含 spec、metrics、conclusion=success）

**Artifacts 注册** (3/3)
- `tlm_analysis` — TWV/HMM 按 confidence 的 agreement/flip 分析
- `probe_comparison` — MV/TWV/HMM 三组 probe 交叉评估结果
- `tlm_run_summary` — 流水线运行摘要

**最终结果**

| Method | Self F1 | MV-c2 F1 | MV-c2 Acc |
|--------|---------|----------|-----------|
| MV     | 0.8468  | 0.8946   | 0.9116    |
| TWV    | 0.8107  | **0.9003** | **0.9157** |
| HMM    | 0.9657  | 0.7502   | 0.7879    |

TWV 在 conf≥2 交叉评估上超过 MV baseline +0.57pp F1，直接支持 Claim 1。HMM 因 file_diff emission 主导导致过度预测 stagnation，可在论文中作为对比讨论。

---
