# analysis edcr partial correlation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_partial_correlation_20260525T012215_result.json`
- **Structured JSON:** [`ee02e4be585f00e8d0d8.json`](../../sessions/ee/ee02e4be585f00e8d0d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰。关键发现：

**EDCR ↔ F1 partial correlation（控制 relation frequency 后）全部显著：**

| Model | Raw r | Partial r (ctrl freq) | p-value |
|-------|------:|-----:|------:|
| Qwen3-8B RSFT | -0.712 | **-0.675** | 3.9e-13 *** |
| Qwen3-1.7B RSFT | -0.664 | **-0.636** | 2.2e-11 *** |
| Llama-3.1-8B RSFT | -0.601 | **-0.562** | 1.0e-08 *** |

控制 frequency + avg_evi_count 后仍然显著（r ∈ [-0.65, -0.51], 全部 p < 1e-7）。

**Robustness checks：**
- 排除 F1=0 的 relation 后仍高度显著（r ∈ [-0.66, -0.52]）
- EDCR_tp（仅 TP 三元组的 evidence）控制 freq 后变弱（r ≈ -0.13 ~ -0.25），8B 模型 p=0.02 显著，其余两个 n.s.。说明 EDCR 的预测力主要来自整体 evidence 模式（含 FP 预测），而非仅 TP 子集

**结论**：EDCR 在控制 relation frequency 后仍与 per-relation F1 强负相关，支持论文声称 EDCR 是 evidence grounding 质量的可靠指标。脚本和结果已保存到服务器。

---
