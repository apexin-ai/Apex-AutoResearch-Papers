# analysis codellama tokenizer analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama_tokenizer_analysis_20260518T120927_result.json`
- **Structured JSON:** [`c576bc9425cc83d44074.json`](../../sessions/c5/c576bc9425cc83d44074.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。现在合并两轮分析结果，输出完整报告。

---

# Tokenization 统计分析报告：CodeLlama vs 其他 3 模型 (tail-2048)

## 1. 基础 Tokenizer 特性

| Model | Vocab Size | Chars/Token (mean) | Chat Template Overhead | Content Budget (2048-OH) |
|---|---|---|---|---|
| **Qwen-7B** | 151,643 | 3.03 | 32 tokens | 2016 |
| **Qwen-1.5B** | 151,643 | 3.03 | 32 tokens | 2016 |
| **CodeLlama-13B** | 32,016 | 2.49 | 12 tokens | 2036 |
| **DeepSeek-6.7B** | 32,000 | 2.29 | 72 tokens | 1976 |

Qwen 的 151K 大词表使其每个 token 编码 3.03 个字符，显著优于 CodeLlama (2.49) 和 DeepSeek (2.29)。

## 2. Raw Token 数统计（tokenize 原始 input+output，无 chat template）

| Model | Mean | Median | Max | P90 | P99 |
|---|---|---|---|---|---|
| **Qwen-7B** | 1929 | 2018 | 2018 | 2018 | 2018 |
| **Qwen-1.5B** | 1929 | 2018 | 2018 | 2018 | 2018 |
| **CodeLlama-13B** | 2341 | 2488 | 2635 | 2555 | 2582 |
| **DeepSeek-6.7B** | 2551 | 2734 | 2911 | 2831 | 2873 |

**关键发现**：tail-2048 数据是按 Qwen tokenizer 截取的（Qwen max=2018，完美适配 2048 limit）。同一文本用 CodeLlama 编码后 **1.21x 膨胀**，DeepSeek **1.32x 膨胀**。

## 3. 训练时实际截断分析（考虑 label-preserving truncation）

训练代码 `to_chat_text` 实现了 **label-preserving truncation**：先计算 chat template + label 的 overhead，然后截断 input content 以适配 budget，label（pass/fail）**永远不会丢失**。

### 截断率与内容损失

| Model | % Samples Truncated | Avg Tokens Lost | Avg Content Retained | Min Retained |
|---|---|---|---|---|
| **Qwen-7B** | 94.2% | 1.0 | **100.0%** | 100.0% |
| **Qwen-1.5B** | 94.2% | 1.0 | **100.0%** | 100.0% |
| **CodeLlama-13B** | 94.7% | 412.1 | **83.3%** | 77.4% |
| **DeepSeek-6.7B** | 94.9% | 691.7 | **74.4%** | 68.0% |

Qwen 虽然 94.2% 的样本触发截断，但只截掉 ~1 token（数据本身就按 Qwen 裁剪到 ~2017 tokens）。CodeLlama 平均丢失 412 tokens（保留 83.3%），DeepSeek 丢失 692 tokens（保留 74.4%）。

### 内容保留分布

| Model | <50% | 50-70% | 70-80% | 80-90% | 90-95% | 95-100% | 100% |
|---|---|---|---|---|---|---|---|
| Qwen-7B | 0 | 0 | 0 | 0 | 0 | 5569 | 341 |
| Qwen-1.5B | 0 | 0 | 0 | 0 | 0 | 5569 | 341 |
| CodeLlama-13B | 0 | 0 | 785 | **4321** | 455 | 35 | 314 |
| DeepSeek-6.7B | 0 | **719** | **3999** | 844 | 21 | 27 | 300 |

CodeLlama 大部分样本保留 80-90%；DeepSeek 大部分在 70-80%。

## 4. 最终序列长度（截断+chat template 后）

| Model | Mean | Median | Max | >2048 |
|---|---|---|---|---|
| Qwen-7B | 1959.2 | 2048 | 2048 | 0 |
| Qwen-1.5B | 1959.2 | 2048 | 2048 | 0 |
| CodeLlama-13B | 1959.2 | 2047 | 2047 | 0 |
| DeepSeek-6.7B | 1963.2 | 2048 | 2048 | 0 |

所有模型最终序列都在 2048 以内，label-preserving truncation 正常工作。

## 5. Label Token 特性

| Model | "pass" tokens | "fail" tokens | Label Fraction in Sequence |
|---|---|---|---|
| Qwen-7B | 1 (`[6385]`) | 1 (`[18403]`) | 0.051% |
| Qwen-1.5B | 1 (`[6385]`) | 1 (`[18403]`) | 0.051% |
| CodeLlama-13B | 1 (`[1209]`) | 1 (`[4418]`) | 0.051% |
| DeepSeek-6.7B | 1 (`[4805]`) | 1 (`[16156]`) | 0.051% |

所有模型都将 pass/fail 编码为单 token。Label 仅占序列的 0.051%，这意味着使用 `label_only_loss` 时，每个 2048-token 序列中只有 1 个 token 贡献梯度。

## 6. Chat Template 格式

```
Qwen:      <|im_start|>system\n...<|im_end|>\n<|im_start|>user\n{input}<|im_end|>\n<|im_start|>assistant\n{label}<|im_end|>
DeepSeek:  <｜begin▁of▁sentence｜>{system_prompt}\n### Instruction:\n{input}\n### Response:\n{label}  (72 tokens overhead)
CodeLlama: &lt;s>[INST] {input} [/INST] {label} &lt;/s>  (12 tokens overhead, 最简洁)
```

## 7. 核心结论

### Tokenization 不能完全解释 CodeLlama tail-2048 的失败

这是本分析最重要的发现：

1. **DeepSeek 截断更严重却表现正常**：DeepSeek 仅保留 74.4% 内容（丢失 692 tokens），远差于 CodeLlama 的 83.3%（丢失 412 tokens），但 DeepSeek 在 tail-2048 上表现正常 (95-97.9%)。这排除了"内容截断导致信息丢失"作为 CodeLlama 失败的唯一解释。

2. **Tokenizer 效率差异是系统性的但非致命的**：CodeLlama 的 32K 词表 vs Qwen 的 151K 词表导致 1.21x token 膨胀，但 DeepSeek 同样是 32K 词表且膨胀更大 (1.32x)，仍然能学。

3. **截断方向的影响**：训练默认 `truncation_side="right"`，即截掉 input 的右侧（trace 末尾）。对 tail-2048 数据（本身是 full trace 的尾部），再截右侧意味着丢失 trace 的最后部分。但这对 CodeLlama 和 DeepSeek 的影响类似。

### 可能的真实原因（需进一步验证）

既然 tokenization/truncation 不是 root cause，CodeLlama tail-2048 的灾难性失败可能源于：

- **模型架构/预训练差异**：CodeLlama (Llama-2 based) 在代码理解的 representation 质量上可能不如 Qwen/DeepSeek，特别是在 trace 被大量截断后，剩余信息不足以让 CodeLlama 学到判别模式
- **LoRA 适配性**：相同的 LoRA 配置对不同架构的效果可能差异很大
- **Label-only loss 的稀疏梯度问题**：每个 2048-token 序列中只有 1 个 token (0.051%) 贡献梯度，对 CodeLlama 这样的大模型来说，梯度信号可能过于稀疏，学习率/步数需要调整
- **截断后的内容可辨别性**：虽然 CodeLlama 保留了 83% 的 trace 内容，但丢失的 17% 可能恰好包含 pass/fail 判定的关键信号（如最后的 assertion 结果），而 CodeLlama 的编码方式可能更集中地将这些关键信息放在被截断的区域

### 论文 Discussion 建议

可以这样 frame：tokenization efficiency 差异 (1.21x-1.32x token inflation) 对内容保留有 measurable impact，但 DeepSeek 的 counter-example 表明 truncation 不是 sufficient explanation。CodeLlama 的失败更可能是 model capability 与 truncation 的 compound effect，需要更大的 max_length 或更 aggressive 的数据适配来弥补。

---
