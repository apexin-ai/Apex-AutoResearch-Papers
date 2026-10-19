# research r1 8b model variant check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r1_8b_model_variant_check_20260519T221613_result.json`
- **Structured JSON:** [`172cdbb66c348f23380c.json`](../../sessions/17/172cdbb66c348f23380c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。

## 结论

| 项目 | 完整模型 ID |
|------|------------|
| **HarmThoughts `r1-8b`** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |
| **AdvBench trace 生成** | `deepseek-ai/DeepSeek-R1-Distill-Llama-8B` |

**两者一致。** HarmThoughts README 明确列出四个模型：OpenThinker-7B, **DeepSeek-R1-Distill-Llama-8B**, DeepSeek-R1-Distill-Qwen-32B, QwQ-32B。

服务器上实际下载的模型 config.json 也确认架构是 `LlamaForCausalLM`（Llama 3.1 基座，32层，hidden_size=4096）。

附注：`src/reasoningshield_explore.py` 中 `"r1-8b": "DeepSeek-R1-Distill-Qwen-8B"` 的映射是**错误的**（且针对的是 ReasoningShield 数据集，不是 HarmThoughts）。实际上不存在 "DeepSeek-R1-Distill-Qwen-8B" 这个模型，Qwen 系列最近的是 7B 版本。该映射不影响我们的实验代码，因为 HarmThoughts 和 AdvBench 的处理流程都没有引用它。

---
