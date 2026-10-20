# research exp 001 target data

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp_001_target_data_20260521T231719_result.json`
- **Structured JSON:** [`93c9fbac10c4272ef909.json`](../../sessions/93/93c9fbac10c4272ef909.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/exp001_target_models_data_sources.md`。

---

## 调研结论

### 公开数据可用性

| Benchmark | Prompts | Models w/ outputs | License | 适用性 |
|-----------|---------|-------------------|---------|--------|
| **Arena-Hard v0.1** | 500 | ~28 (HF full) | 未明确 | ⭐ 最适合 — 难度高、模型较新 |
| **WildBench V2** | 1,024 | 64 | Apache 2.0 | ⭐ 次选 — 模型多、许可好 |
| **AlpacaEval 2** | 805 | 228 | CC BY-NC 4.0 | 模型最多，但非商用限制 |
| **MT-Bench** | 80 | 34 | 公开 | 模型偏旧 (2023), multi-turn |
| **Chatbot Arena** | 33K convs | 20 | CC BY-NC, Gated | Pairwise 格式不直接适用 |

### 推荐策略

**Primary benchmark: Arena-Hard v0.1 (500 prompts)**
- 从 HF dataset `lmarena-ai/arena-hard-auto` 下载已有 ~28 models 的 responses
- 对缺失的 frontier 2025-2026 models (GPT-5.5, Claude Opus 4.7, DeepSeek V4 Pro 等) 自行生成
- API 成本 < $5，本地推理 1-2h

### Target Models: 22 个，覆盖 4 个 tier

- **Frontier** (5): GPT-4o, GPT-5.5, Claude Opus 4.7, Gemini 2.5 Pro, DeepSeek V4 Pro
- **Mid** (5): Claude Sonnet 4.6, GPT-4o-mini, Gemini 2.5 Flash, Qwen3-235B-A22B, Mistral Large 3
- **Open Strong** (4): Llama-3.3-70B, Qwen2.5-72B, DeepSeek-V3, Mistral Medium 3.5 (128B)
- **Open Mid/Weak** (8): Llama-3.1-8B, Qwen2.5-7B, Mistral-7B-v0.3, Phi-4, Gemma-2-27B, Llama-3.1-70B, Qwen2.5-14B, Gemma-2-9B

### 关键修正
- ~~GPT-4.5~~ → GPT-5.5 (correct as of May 2026)
- Qwen3-235B 正确 HF ID: `Qwen/Qwen3-235B-A22B-Instruct` (含 A22B 后缀)
- Mistral Large 3: `mistral-large-2512` (675B MoE)
- "Mistral Medium 3" 不存在 → **Mistral Medium 3.5** (128B dense)

---
