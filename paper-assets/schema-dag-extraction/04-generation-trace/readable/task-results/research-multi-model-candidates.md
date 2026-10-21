# research multi model candidates

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_multi-model-candidates_20260515T031845_result.json`
- **Structured JSON:** [`174e8ded6dff82cde126.json`](../../sessions/17/174e8ded6dff82cde126.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。结论：

**推荐 Top-2:**

1. **LLaMA-3.3-70B-Instruct-FP8** (`nvidia/Llama-3.3-70B-Instruct-FP8`) — 不同 family（Meta），能力与 Qwen3-32B 对等，vLLM guided decoding 完全支持。FP8 ~70GB，98GB 单卡可跑但需独占（停掉 Qwen3）。

2. **Phi-4 (14B)** (`microsoft/phi-4`) — 不同 family（Microsoft），仅 ~14-28GB VRAM，可与 Qwen3 并行。如果 type confusability 在小模型上也成立，反而增强论证。

**排除:** Mistral-Large-2 (123B FP8 ~130GB 超出)、DeepSeek-V3 (671B 太大)、DeepSeek-V2-Lite (guided decoding 兼容性不确定 + NER 能力存疑)。

报告已写入 artifacts 并注册。

---
