# research alt small models 2025

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_alt_small_models_2025_20260518T182125_result.json`
- **Structured JSON:** [`dabeb6ce573395c16713.json`](../../sessions/da/dabeb6ce573395c16713.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是按推荐度排序的候选列表。

---

## 候选模型列表

### 1. Qwen3-1.7B-Base ⭐ 首选推荐

| 项目 | 信息 |
|------|------|
| HuggingFace ID | `Qwen/Qwen3-1.7B-Base` |
| 参数量 | 1.7B |
| 发布日期 | 2025-04-28 |
| 许可证 | Apache 2.0 |
| 纯文本 decoder-only | 是 |
| Base 版本 | 是 |
| Tokenizer | Qwen 自研, vocab ~151K |
| 训练数据 | 18T tokens (119 languages) |
| 上下文 | 32K |

**推荐理由**: 参数量适中(1.7B)，训练数据充足(18T tokens)，Apache 2.0 完全开源，性能超越 Qwen2.5-3B。对 iterative model collapse 实验来说，1.7B 训练迭代速度比 3B 快约 40%，是最佳平衡点。

---

### 2. Qwen3-0.6B-Base

| 项目 | 信息 |
|------|------|
| HuggingFace ID | `Qwen/Qwen3-0.6B-Base` |
| 参数量 | 0.6B |
| 发布日期 | 2025-04-28 |
| 许可证 | Apache 2.0 |
| 纯文本 decoder-only | 是 |
| Base 版本 | 是 |
| Tokenizer | 同 Qwen3 系列, vocab ~151K |
| 训练数据 | 18T tokens |
| 上下文 | 32K |

**适用场景**: 需要更快实验迭代速度的场景。作为 ablation 或 pilot 实验的低成本选择。

---

### 3. SmolLM3-3B-Base

| 项目 | 信息 |
|------|------|
| HuggingFace ID | `HuggingFaceTB/SmolLM3-3B-Base` |
| 参数量 | 3B |
| 发布日期 | 2025-07-08 |
| 许可证 | Apache 2.0 |
| 纯文本 decoder-only | 是 (GQA + NoPE) |
| Base 版本 | 是 |
| Tokenizer | SentencePiece, vocab 128K |
| 训练数据 | 11.2T tokens |
| 上下文 | 64K (YARN 扩展至 128K) |

**适用场景**: 如需接近 Gemma 4 E2B 的参数规模(~3B vs 5.1B)。缺点是 3B 在 iterative 实验中训练成本更高。

---

### 4. OLMo-2-0425-1B

| 项目 | 信息 |
|------|------|
| HuggingFace ID | `allenai/OLMo-2-0425-1B` |
| 参数量 | 1.1B |
| 发布日期 | 2025-05-01 |
| 许可证 | Apache 2.0 |
| 纯文本 decoder-only | 是 |
| Base 版本 | 是 |
| Tokenizer | GPT-NeoX 系列 |
| 训练数据 | 大规模 (OLMo-mix-1124, 5T+ family) |
| 上下文 | 4K (默认) |

**特点**: 完全开源（数据+代码+权重+中间 checkpoint），可复现性最强。缺点是上下文窗口较短，性能可能弱于 Qwen3 同规模。

---

### 5. Gemma 3 1B PT

| 项目 | 信息 |
|------|------|
| HuggingFace ID | `google/gemma-3-1b-pt` |
| 参数量 | 1B |
| 发布日期 | 2025-03 |
| 许可证 | **Gemma Terms of Use**（非 Apache 2.0，有商用限制） |
| 纯文本 decoder-only | 是 (1B 版本为纯文本) |
| Base 版本 | 是 (pt = pretrained) |
| Tokenizer | SentencePiece, vocab 256K |
| 训练数据 | 2T tokens |
| 上下文 | 32K |

**注意**: Gemma 3 仍使用 Google 自定义许可证（有商用限制和 MAU 门槛），Gemma 4 才切换到 Apache 2.0。如果许可证不是硬性要求，这个模型是 Gemma 家族内最佳替代。

---

## 排除的模型

| 模型 | 排除原因 |
|------|----------|
| Gemma 4 E2B | 多模态 (text+vision+audio), 5.1B，无纯文本 base 版 |
| Phi-4-mini | 3.8B 略超范围，**无 base 版本**（仅 instruct/reasoning） |
| Llama 3.2 1B/3B | 2024-09 发布，早于 2025-01 截止线 |
| Qwen3.5 小模型 | 尚未发布（目前仅有 27B+） |

---

## 建议

对于 iterative model collapse 实验，**`Qwen/Qwen3-1.7B-Base`** 是最佳选择：
- Apache 2.0 无限制
- 1.7B 参数在单卡上训练迭代快
- 18T tokens 预训练确保起始质量高
- 纯文本 decoder-only base model，无 instruction tuning 干扰

如需更小的 pilot 实验用 `Qwen3-0.6B-Base`，需更大模型用 `SmolLM3-3B-Base`。

Sources:
- [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base)
- [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)
- [Qwen3 Blog](https://qwenlm.github.io/blog/qwen3/)
- [SmolLM3-3B-Base](https://huggingface.co/HuggingFaceTB/SmolLM3-3B-Base)
- [SmolLM3 Blog](https://huggingface.co/blog/smollm3)
- [OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)
- [Gemma 3 1B PT](https://huggingface.co/google/gemma-3-1b-pt)
- [Gemma 4 Apache 2.0 License](https://www.mindstudio.ai/blog/gemma-4-apache-2-license-commercial-use)
- [Gemma 4 HuggingFace Blog](https://huggingface.co/blog/gemma4)

---
