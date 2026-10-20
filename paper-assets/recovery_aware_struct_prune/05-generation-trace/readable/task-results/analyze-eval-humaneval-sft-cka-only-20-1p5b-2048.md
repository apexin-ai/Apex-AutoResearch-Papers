# analyze eval humaneval sft cka only 20 1p5b 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_humaneval_sft_cka_only_20_1p5b_2048_20260519T132820_result.json`
- **Structured JSON:** [`8bfc86c90225c3de2ca6.json`](../../sessions/8b/8bfc86c90225c3de2ca6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

## 结果

| 指标 | 值 |
|------|-----|
| **pass@1** | **0.61% (1/164)** |
| median_response_length | 2048 (打满上限) |
| avg_response_length | 1968.76 |

## 根因分析

1.5B SFT CKA-only 模型在 HumanEval 上**生成自然语言推理文本而非代码**。几乎所有 163 个失败样本都是 SyntaxError——输出内容是 "Okay, I need to write a Python function..." 或 "The function checks if..." 这类解释性文字，而非可执行的 Python 代码。

模型在 2048 token 内耗尽全部预算在推理文本上，无法生成有效代码补全。

## 跨尺度对比

| 模型 | pass@1 | 通过数 |
|------|--------|--------|
| 7B SFT CKA-only | 20.12% | 33/164 |
| 7B GRPO CKA-only | 20.12% | 33/164 |
| **1.5B SFT CKA-only** | **0.61%** | **1/164** |
| 7B GRPO Standard | 10.98% | 18/164 |
| 7B GRPO RASP | 10.98% | 18/164 |

## 结论

1.5B SFT CKA-only 模型无法支撑跨尺度 capability breadth claim。失败原因并非剪枝导致的能力退化，而是 **1.5B 模型容量不足以在 SFT 后维持代码生成格式**——模型退化为生成自然语言解释而非代码。这表明跨尺度对比需要考虑基座模型的 code generation baseline，1.5B 尺度下 SFT 可能根本无法激活结构化代码输出能力。

---
