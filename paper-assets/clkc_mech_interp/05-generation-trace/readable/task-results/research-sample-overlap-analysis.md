# research sample overlap analysis

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sample-overlap-analysis_20260524T152022_result.json`
- **Structured JSON:** [`c07ac3262601f603ac9c.json`](../../sessions/c0/c07ac3262601f603ac9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在完全理解了。差异的主要原因是：各模型的 data prep 脚本**独立从完整 ConflictQA 数据集随机采样 2000 条**（默认 seed=42 但可能在不同时间/参数执行），然后各自 verify。

最终结果如下：

---

```
ConflictQA 三模型样本集重叠度分析
============================================================

数据来源: ConflictQA-popQA-chatgpt (同一份 HuggingFace 数据集)
数据流水线: 各模型独立采样 → verification → balance & split

样本集大小（verify 后）:
  Llama-3.1-8B:  1600 samples (1499 unique questions)
  Gemma-2-9B:    1368 samples (666 unique questions)
  Qwen3-8B:      1418 samples (708 unique questions)

两两重叠（问题级）:
  Llama ∩ Gemma:  108 (占Llama 7.2%, 占Gemma 16.2%)
  Llama ∩ Qwen:   134 (占Llama 8.9%, 占Qwen 18.9%)
  Gemma ∩ Qwen:   165 (占Gemma 24.8%, 占Qwen 23.3%)

三模型共同: 23 questions (占最小集Gemma 3.5%)

各自独有:
  Llama only: 1280
  Gemma only: 416
  Qwen only:  432

差异来源（两重因素叠加）:
  1. 采样差异: 各模型的 prepare_data 脚本独立从 ConflictQA 全集
     随机采样 ~2000 条（种子/时间不同），起始问题集已不同
     - Llama 与本地 raw_sampled 重叠仅 39.8%
     - Gemma 与本地 raw_sampled 重叠仅 53.6%
     - Qwen 100% 来自 raw_sampled（用的是 verify_parametric_knowledge.py）
  2. Verification 过滤: 各模型 parametric knowledge 不同，
     同一问题是否通过 verification 因模型而异
```

**结论**: 重叠极低（三模型共同仅 23 个问题），主因是数据准备流水线各自独立采样，而非仅仅是 verification 差异。如果审稿人关心跨模型可比性，需要强调论文的 claim 是「同一现象在不同模型上独立复现」，而非「同一组问题在三个模型上表现如何」。

---
