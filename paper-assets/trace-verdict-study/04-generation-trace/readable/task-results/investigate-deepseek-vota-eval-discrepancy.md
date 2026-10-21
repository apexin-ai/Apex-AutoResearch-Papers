# investigate deepseek vota eval discrepancy

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_deepseek_vota_eval_discrepancy_20260515T222754_result.json`
- **Structured JSON:** [`45351ad41cb2c88a178d.json`](../../sessions/45/45351ad41cb2c88a178d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部调查完成。以下是结论。

---

## 调查结论

### 根因

`evaluate.py` v2 的 content-aware truncation 从 **右侧** 截断 `input_text`（保留前 N tokens），这摧毁了输入末尾的问题后缀 `"Does this code pass all tests? Answer: "`。

**核心数据：**

| | DeepSeek tokenizer | Qwen tokenizer |
|---|---|---|
| VOTA 样本平均 token 数 | 2759 | 1908 |
| 超过 2048 的样本比例 | **1091/1190 (91.7%)** | **0/1190 (0%)** |
| 最大 token 数 | 2951 | 2045 |

这就是为什么 Qwen 结果不变（99.41%）但 DeepSeek 崩塌的原因——Qwen tokenizer 更高效，所有样本都在 2048 以内，truncation 从未触发。

### 截断 vs 非截断准确率

| 分组 | 样本数 | 准确率 |
|---|---|---|
| **不需要截断** (≤2048) | 99 | **100.0%** |
| **需要截断** (>2048) | 1091 | **8.3%** |

模型在不截断时完美运行。截断后输出的是垃圾 token（"these" 414次, "this" 226次, "given" 154次…）——这些是代码/trace 内容的续写，模型根本不知道自己该回答 pass/fail。

### 84.45% vs 16%——哪个对？

**84.45% 更能代表模型真实能力**。原始 eval（`bootstrap_compare.py`）发送完整输入，模型看到完整问题，给出有效的 pass/fail 预测。虽然输入 >2048 超出训练 max_length，但 DeepSeek Coder 6.7B 原生支持 16K context，这不是严重问题。

**16% 是 truncation bug 的产物**，不代表模型质量。

### 训练也有同样的问题

`train_sft.py` 的 `to_chat_text()` 使用同样的右截断——91.7% 的 DeepSeek 训练样本也丢失了问题后缀。模型主要从 8.3% 未截断样本 + 全序列 loss 中学到的 pass/fail 分类能力。这解释了为什么 DeepSeek 是 84.45% 而非 Qwen 的 99.41%。

### 建议下一步

1. **修复 evaluate.py**：把右截断改为 **trace-only 截断**，保留输入开头（code+test）和结尾（question）。`train_sft.py` 已有 `truncate_traces()` 函数可复用：
   ```python
   TRACE_MARKER = "Execution trace:\n"
   SUFFIX = "\n\nDoes this code pass all tests? Answer: "
   # 只截断 trace 部分，保留 code + question
   ```

2. **如果重新训练 DeepSeek**：使用 `--max_trace_tokens` 参数进行 trace-only 截断，或用 `--label_only_loss` 模式（使用 `to_prompt_completion`，不会截断 question）。当前训练对 91.7% 的样本效果很差。

3. **当前**：以 84.45% 作为 DeepSeek VOTA 的正式结果，标注 train/eval max_length mismatch 为已知局限。

---
