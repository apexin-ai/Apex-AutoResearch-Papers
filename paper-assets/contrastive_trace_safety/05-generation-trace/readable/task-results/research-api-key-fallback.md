# research api key fallback

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_api_key_fallback_20260518T202806_result.json`
- **Structured JSON:** [`ba8e142d8c3a6e8c6412.json`](../../sessions/ba/ba8e142d8c3a6e8c6412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/api_key_fallback_eval.md`。

核心发现:

1. **服务器上所有 instruction-tuned LLM (QwQ-32B, R1-32B, R1-8B, OT-7B) 都是被研究模型**, 用它们做标注存在 circular concern
2. **推荐方案: Groq 免费 tier 的 Qwen3-32B** — 非被研究模型, 32B reasoning quality, 免费即用, 60-90 分钟可完成 100 条标注
3. **备选: Google AI Studio (Gemini 2.5 Flash)** — 完全不同的 model family, 零 circular risk
4. 等 Claude API key 可以并行推进, 到了就追加一轮验证

---
