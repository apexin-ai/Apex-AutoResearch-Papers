# analysis deepseek tokenizer check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-tokenizer-check_20260517T083521_result.json`
- **Structured JSON:** [`6536092d43d1d51cdeae.json`](../../sessions/65/6536092d43d1d51cdeae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 模型 | Tokenizer 类 | Vocab Size |
|---|---|---|
| **Qwen3-8B** | `Qwen2TokenizerFast` | 151,643 |
| **Qwen3-4B** | `Qwen2TokenizerFast` | 151,643 |
| **DeepSeek-coder-6.7b-instruct** | `LlamaTokenizerFast` | 32,000 |

**编码对比**：Qwen3-8B 和 Qwen3-4B 编码完全一致（共享同一 tokenizer），但与 DeepSeek-coder 完全不同：
- 不同的 tokenizer 类（Qwen2 vs Llama）
- vocab size 差 ~5 倍（151K vs 32K）
- 所有测试字符串的 token ID 和序列长度均不同
- DeepSeek 每个序列都额外加了 BOS token (32013)

**结论**：Qwen3 和 DeepSeek-coder **使用完全不同的 tokenizer**。论文中 "tokenizer-specific" 的表述是准确的——CLS/CWM 模型确实绑定了特定 tokenizer，不能跨模型族复用。

---
