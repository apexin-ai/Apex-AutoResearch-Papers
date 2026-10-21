# analysis deepseek math integrity

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_math_integrity_20260522T121318_result.json`
- **Structured JSON:** [`77111554161996973ebf.json`](../../sessions/77/77111554161996973ebf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 数据完整性
`deepseek_math.jsonl` **完全完整**：57,600/57,600 行有效，0 null，0 空值。完全交叉设计（1 model × 200 items × 2 temps × 6 prompts × 6 seeds × 4 orderings）。之前分析注明 37,400/57,600 是**错误的**。

### 2. 8-model MATH G-study（已存在）
服务器上已有 `math_8model_verified.json`，包含全部 8 个模型（DeepSeek, Gemma, InternLM, Llama, Mistral, OLMo, Qwen, Yi）的 Henderson I 方差分解：

| Component | % |
|---|---|
| residual | 43.88% |
| item_id | 24.03% |
| model:item_id | 17.28% |
| model | 8.51% |
| prompt_template:item_id | 2.86% |
| model:prompt_template | 1.67% |
| 其余 | < 1% |

**G_item = 0.888**，grand mean accuracy = 0.286。

### 3. 与 7-model 对比
- item_id: 26.48% → 24.03%（-2.45pp）
- 加入 DeepSeek 后 model 相关方差略增，item 方差占比相应下降，但整体结构不变。

### 4. 结论
MATH 可以直接升级为 **8-model 分析**，数据完整无缺失。已保存至本地 artifacts。

---
