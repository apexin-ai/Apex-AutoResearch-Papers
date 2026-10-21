# investigate humaneval sft cka only zero pass

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_humaneval_sft_cka_only_zero_pass_20260519T043957_result.json`
- **Structured JSON:** [`3c40fc301ff2cc6cfe8c.json`](../../sessions/3c/3c40fc301ff2cc6cfe8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**Pass@1 = 0% 是真实结果，不是 bug。**

### 根因

SFT CKA-only 20% 模型在收到代码题时，完全进入数学推理模式，生成冗长的自然语言解释而非 Python 代码。3 个诊断样本的表现：

| 题目 | 输出内容 | 是否有代码 |
|------|---------|-----------|
| HumanEval/0 | 纯自然语言分析"how do I generate all possible pairs" | 无，512 tokens 全是推理 |
| HumanEval/2 | 先推理，后输出 broken code（字符串拼接垃圾） | 有但完全错误 |
| HumanEval/4 | 纯自然语言描述 MAD 计算步骤 | 无，512 tokens 全是推理 |

模型行为：GSM8K SFT 将生成分布重度偏移到数学推理风格，面对代码 prompt 时仍在 `&lt;think>` 中做 step-by-step 分析，要么从不输出代码（撞 max_new_tokens），要么输出 broken code。

### 对比数据

| 模型 | HumanEval Pass@1 | 备注 |
|------|-----------------|------|
| Unpruned | 45.12% | baseline |
| **GRPO CKA-only 20%** | **35.00%** (前20题) | GRPO 保留了代码能力 |
| SFT Standard 20% | 11.59% | 至少能生成代码 |
| SFT RASP 20% | 10.37% | 类似 |
| **SFT CKA-only 20%** | **0.00%** (前69题) | 完全丧失代码能力 |

### 解读

CKA-only 剪枝 + GSM8K SFT 的组合导致代码能力彻底坍塌。CKA-only 在 GSM8K 上是最好的方法（64.37%），但代价是完全牺牲了 cross-task generalization。GRPO CKA-only 没有这个问题（前 20 题 35%），说明 GRPO 的 RL 训练方式比 SFT 更好地保持了通用能力。

评测可以等其跑完，最终结果大概率仍是 0% 或极接近 0%。

---
