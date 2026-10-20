# research second vla survey

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_second_vla_survey_20260519T162116_result.json`
- **Structured JSON:** [`b7449864dd6d84d22ef7.json`](../../sessions/b7/b7449864dd6d84d22ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `artifacts/second_vla_survey.md`。

**核心结论**:

**Top-1: OpenVLA-Phi3V** (`furonghuang-lab/openvla_phi3v`) — Phi-3-Vision backbone, 与 OpenVLA 使用完全相同的训练配方和 256-bin action tokenization，唯一变量是 backbone 从 Llama-2 换成 Phi-3。适配工作量极低（~2-3 天），变量控制最干净。

**Top-2: SpatialVLA** (`IPEC-COMMUNITY/spatialvla-4b-224-pt`) — PaLiGemma2/Gemma-2 backbone，完全独立的团队和框架，autoregressive discrete action tokens。覆盖第三个 LLM 家族。适配 ~4-5 天。

**Top-3: NORA** (`declare-lab/nora`) — Qwen-2.5-VL-3B backbone，3B 最小最快，但 FAST+ 变长 tokenizer 增加分析难度。

**推荐策略**: 先做 OpenVLA-Phi3V（快速出结果，控制变量最干净），若 reviewer 仍嫌不够，再加 SpatialVLA（覆盖 Llama-2 / Phi-3 / Gemma-2 三个 LLM 家族）。可选用 π₀ 做负对照（cross-attention 架构，预测不会出现 L1 routing）。

---
