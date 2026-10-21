# analysis llama olmo paradox

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-olmo-paradox_20260522T233657_result.json`
- **Structured JSON:** [`d4b23d56a47b05ab94c0.json`](../../sessions/d4/d4b23d56a47b05ab94c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact already written to disk. Analysis complete.

**写入**: `artifacts/llama_olmo_paradox_analysis.md`

**核心结论**：三个 moderating factors 共同解释悖论——

1. **Pre-training data volume（主因）**：LLaMA 15T vs OLMo 4.7T，3× 数据差距使 LLaMA 的表征更"固化"，LoRA 的低秩扰动（仅 0.52% 可训练参数）不足以改变其 benchmark 行为
2. **Two-stage training（次因）**：OLMo-2 有 843B token 的 annealing 阶段，模型被设计为可通过后期训练吸收新知识，对 LoRA SFT 天然更 receptive
3. **GQA vs MHA（次因）**：LLaMA 的 GQA（8 KV heads）使 KV projection 的 LoRA 参数比 OLMo-2 的 MHA（32 KV heads）少 60%，限制了注意力模式的可调整性

建议 Discussion 措辞已包含在文件末尾，强调 baseline ability 不是唯一决定因素，contamination susceptibility 由 training history + architecture + capacity 联合决定。

---
