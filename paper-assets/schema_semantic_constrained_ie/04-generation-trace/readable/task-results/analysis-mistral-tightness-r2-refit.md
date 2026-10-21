# analysis mistral tightness r2 refit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_tightness_r2_refit_20260516T175802_result.json`
- **Structured JSON:** [`cdd8ac79e6b278e89796.json`](../../sessions/cd/cdd8ac79e6b278e89796.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/mistral_tightness_r2_analysis.md`。

核心结果：
- **SciERC τ̄ = 0.333**（低 tightness，schema 宽松）
- **DocRED τ̄ = 0.842**（高 tightness，schema 严格）
- **n=4 (Qwen+Llama): R² = 0.538** — 中等线性关系
- **n=6 (加 Mistral): R² = 0.211** — 线性关系崩塌，R² 下降 0.33
- Mistral 残差巨大：SciERC +12.9%（4.7× RMSE），DocRED +26.8%（9.8× RMSE）

结论：τ̄ 只在同一 calibration tier 内有效。Mistral 的高 DR 是 model-level 因素（未经 schema-aware 微调）主导的，schema tightness 是放大器而非根因。论文叙述建议：分层呈现——calibrated models 展示 τ̄ 与 DR 的正相关，Mistral 作为 boundary condition 说明 constrained decoding 在 model-schema misalignment 场景下获益最大。

---
