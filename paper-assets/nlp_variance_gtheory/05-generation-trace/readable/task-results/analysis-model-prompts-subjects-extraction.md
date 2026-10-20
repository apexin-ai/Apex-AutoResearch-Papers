# analysis model prompts subjects extraction

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_model_prompts_subjects_extraction_20260522T035444_result.json`
- **Structured JSON:** [`abd53173cfa996530f74.json`](../../sessions/ab/abd53173cfa996530f74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是三项结果。

---

## 任务 2: 完整 8 模型列表

来源：`src/config/model_paths.py`

| # | Display Name | HuggingFace Model ID | 参数量 | 本地路径（ModelScope 下载） |
|---|---|---|---|---|
| 1 | Llama-3.1-8B | `meta-llama/Llama-3.1-8B-Instruct` | 8B | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| 2 | Gemma-2-9B | `google/gemma-2-9b-it` | 9B | `/root/autodl-tmp/.hf_cache/LLM-Research/gemma-2-9b-it` |
| 3 | Mistral-7B-v0.3 | `mistralai/Mistral-7B-Instruct-v0.3` | 7B | `/root/autodl-tmp/.hf_cache/LLM-Research/Mistral-7B-Instruct-v0___3` |
| 4 | Qwen3-8B | `Qwen/Qwen3-8B` | 8B | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` |
| 5 | Yi-1.5-9B | `01-ai/Yi-1.5-9B-Chat` | 9B | `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B-Chat` |
| 6 | OLMo-2-7B | `allenai/OLMo-2-1124-7B-Instruct` | 7B | `/root/autodl-tmp/.hf_cache/allenai/OLMo-2-1124-7B-Instruct` |
| 7 | InternLM2.5-7B | `internlm/internlm2_5-7b-chat` | 7B | `/root/autodl-tmp/.hf_cache/Shanghai_AI_Laboratory/internlm2_5-7b-chat` |
| 8 | DeepSeek-7B | `deepseek-ai/deepseek-llm-7b-chat` | 7B | `/root/autodl-tmp/.hf_cache/deepseek-ai/deepseek-llm-7b-chat` |

**注意**：`cross_model_gstudy_8model.json` 显示实际分析分两组——`common_models`（6 个，排除 OLMo-2-7B 和 Yi-1.5-9B）和 `all_models`（8 个）。排除原因可能是这两个模型在部分 benchmark 上数据不完整。

---

## 任务 3: Prompt 模板（6 × 5 benchmarks）

来源：`src/data/prompt_templates.py` + `src/inference/benchmark_utils.py`

每个 benchmark 有 6 个语义等价但表面形式不同的 prompt 变体（Brittlebench-style surface perturbation），用于测量 prompt wording 作为 G-theory facet 的贡献。

### MC 类：MMLU（4 选项固定）

**Template 1** — 经典 Harness 格式
```
The following are multiple choice questions (with answers) about {subject}.

{question}
A. {A}
B. {B}
C. {C}
D. {D}
Answer:
```

**Template 2** — "Question:" 前缀 + 行内选项
```
Answer the following {subject} questions by selecting the correct option.

Question: {question}
(A) {A}  (B) {B}  (C) {C}  (D) {D}
Correct answer:
```

**Template 3** — Q/A 简写 + 缩进选项
```
Below are {subject} multiple-choice problems. Pick the right letter.

Q: {question}
  A) {A}
  B) {B}
  C) {C}
  D) {D}
A:
```

**Template 4** — 列表符号 + 指令式
```
Answer the following {subject} question by selecting A, B, C, or D.

{question}
- A. {A}
- B. {B}
- C. {C}
- D. {D}
Answer:
```

**Template 5** — "exam question" 框架 + verbose 选项
```
Below is a {subject} exam question with four possible answers. Choose the correct one.

{question}
Option A: {A}
Option B: {B}
Option C: {C}
Option D: {D}
Correct:
```

**Template 6** — 极简 + "Your answer"
```
Question ({subject}):
{question}
Choices:
(A) {A} (B) {B} (C) {C} (D) {D}
Your answer:
```

### MC 类：ARC-Challenge / HellaSwag

结构与 MMLU 相同的 6 个变体模式（system instruction + choice layout + answer cue 三维变化），但：
- **ARC**：system 改为 science 相关指令（"Answer the following science question" 等）
- **HellaSwag**：system 改为 continuation/coherence 指令（"Choose the most plausible continuation" 等）
- 两者都支持可变长度选项（3-5 个），通过 `choice_style` 动态格式化（`vertical_dot` / `inline_paren` / `indented_paren` / `bulleted` / `verbose` / `compact`，分别对应 Template 1-6）

### FF 类：GSM8K（Chain-of-Thought）

**Template 1**
```
Solve the following math problem step by step.

Q: {question}
A: Let's think step by step.
```

**Template 2**
```
Answer the following math word problem. Show your work.

Question: {question}
Solution:
```

**Template 3**
```
Solve each problem below. Write your reasoning, then give the final answer after ####.

Problem: {question}
Reasoning:
```

**Template 4**
```
You are a math tutor. Solve the problem and show your steps.

{question}
Steps:
```

**Template 5**
```
Work through this math question carefully.

Q: {question}
Work:
```

**Template 6**
```
Math problem:

{question}
Let's solve this step by step.
```

### FF 类：MATH（\boxed{} 格式）

与 GSM8K 结构平行，6 个变体，区别是 system 指令要求答案放在 `\boxed{}` 中（而非 `####`），query 结尾也相应调整。

---

## 任务 5: MMLU Subject 选择

来源：`src/data/sample_mmlu.py`

### 10 个 Subject 完整列表

| # | Subject | MMLU Category | Items |
|---|---------|---------------|-------|
| 1 | `abstract_algebra` | STEM | 20 |
| 2 | `college_physics` | STEM | 20 |
| 3 | `high_school_mathematics` | STEM | 20 |
| 4 | `computer_security` | STEM | 20 |
| 5 | `world_religions` | Humanities | 20 |
| 6 | `philosophy` | Humanities | 20 |
| 7 | `us_foreign_policy` | Social Science | 20 |
| 8 | `international_law` | Social Science / Professional | 20 |
| 9 | `professional_medicine` | Professional | 20 |
| 10 | `clinical_knowledge` | Professional | 20 |

**总计**：10 subjects × 20 items = **200 items**

### 选择标准

**Purposive stratified sampling**（人为选定，非随机），覆盖 MMLU 的 4 大 domain：
- STEM（4 个）：abstract_algebra, college_physics, high_school_mathematics, computer_security
- Humanities（2 个）：world_religions, philosophy
- Social Science（2 个）：us_foreign_policy, international_law
- Professional（2 个）：professional_medicine, clinical_knowledge

代码 docstring 原文："Subjects span STEM, humanities, social science, professional, and legal domains."

每个 subject 内部从 `cais/mmlu` test split 中随机抽 20 题（`seed=42`，等量分配 `items_per_subject = n_items // n_subjects`）。

---
