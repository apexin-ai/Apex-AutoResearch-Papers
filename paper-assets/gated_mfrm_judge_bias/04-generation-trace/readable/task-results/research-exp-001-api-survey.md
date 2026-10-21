# research exp 001 api survey

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_exp_001_api_survey_20260521T230918_result.json`
- **Structured JSON:** [`20f6ef7c05a23a30cc5f.json`](../../sessions/20/20f6ef7c05a23a30cc5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成，结果已写入 `memory.md`。以下是汇总：

## Proprietary Judges

| Judge | Model ID | Input $/1M | Output $/1M | 预估总费用 | 状态 |
|-------|----------|-----------|------------|-----------|------|
| GPT-4o | `gpt-4o` | $2.50 | $10.00 | **$112.50** | ✅ |
| GPT-5.5 | `gpt-5.5` | $5.00 | $30.00 | **$275.00** | ✅ 2026-04-23 发布 |
| Claude Opus 4.7 | `claude-opus-4-7-20250219` | $5.00 | $25.00 | **$250.00** | ✅ |
| Claude Sonnet 4.6 | `claude-sonnet-4-6-20250514` | $3.00 | $15.00 | **$150.00** | ✅ |
| Gemini 2.5 Pro | `gemini-2.5-pro` | $1.25 | $10.00 | **$81.25** | ✅ |
| DeepSeek V4 Pro | `deepseek-v4-pro` | $0.435 (促销) | $0.87 (促销) | **$15.23** | ✅ 促销至5/31 |
| Qwen3-235B-A22B | `qwen3-235b-a22b` | $0.18 (OpenRouter) | $0.54 (OpenRouter) | **$7.20** | ✅ |

**Proprietary 总费用: ~$891** (促销价) / ~$950 (原价)

## Open-Source Judges (4×RTX 6000 = 192GB VRAM)

| Judge | HuggingFace ID | FP16 VRAM | INT8 VRAM | 可行性 |
|-------|---------------|-----------|-----------|--------|
| Llama-3.3-70B | `meta-llama/Llama-3.3-70B-Instruct` | ~140 GB | ~70 GB | ✅ |
| Qwen2.5-72B | `Qwen/Qwen2.5-72B-Instruct` | ~144 GB | ~72 GB | ✅ |
| Mistral-Large 3 | `mistralai/Mistral-Large-3-675B-Instruct-2512` | ~1.35 TB | ~675 GB | ❌ 太大 |

**Mistral-Large 无法本地运行**（675B MoE 需 8×H200）。替代方案：**Mistral Medium 3.5** (`mistralai/Mistral-Medium-3.5-128B`)，FP8 ~128GB 可在 192GB 上运行。

## 关键结论

1. **GPT-5.5 和 DeepSeek V4 Pro 均已发布**，无需替代
2. **总费用 ~$891**（7 个 proprietary judges），可控
3. **DeepSeek 促销 5/31 到期**，建议尽快启动数据收集
4. **需要 5 个 API key**: OpenAI、Anthropic、Google AI、DeepSeek、DashScope（或用 OpenRouter 统一接入）
5. **Mistral 需决策**: 用 Medium 3.5 (128B) 本地跑，还是改用 Mistral API 调 Large 3

Sources:
- [OpenAI API Pricing](https://openai.com/api/pricing/)
- [Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [GPT-5.5 Release](https://openai.com/index/introducing-gpt-5-5/)
- [DeepSeek V4 Preview](https://api-docs.deepseek.com/news/news260424)
- [Mistral Large 3 HuggingFace](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)
- [Mistral Medium 3.5 HuggingFace](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)

---
