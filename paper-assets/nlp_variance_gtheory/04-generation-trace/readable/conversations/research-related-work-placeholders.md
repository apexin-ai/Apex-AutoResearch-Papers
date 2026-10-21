# research related work placeholders

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_research_related_work_placeholders_20260520T210242.jsonl`
- **Structured JSON:** [`9b026168fd0f03555dae.json`](../../sessions/9b/9b026168fd0f03555dae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-20T21:04:11.351479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T21:04:11.351822+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T21:04:11.352052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T21:04:11.352288+00:00_

1	# Related Work — Structured Notes
2	
3	> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。
4	
5	## (a) G-theory & Variance Decomposition in NLP/ML
6	
7	### [Mesting et al., 2026] — Hidden Measurement Error in LLM Pipelines
8	- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估，交叉分解 5 个 facets（item/prompt/temperature/judge model/replication）；发现 judge 选择贡献 43.8% 方差，prompt×judge 交互贡献 12.4%；标准 95% CI 实际覆盖率仅 79%，标准 CI 遗漏 40-60% 不确定性
9	- **方法**: 在 AILuminate、MMLU、Chatbot Arena 上对多个 LLM 进行全交叉 G-study，用 REML 估计方差分量，D-study 指导评估设计优化（如 3 个 judge 可降低 38% SE）
10	- **与本工作的关系**: extends — 我们直接继承其 TEE 框架和 REML 方法论，是最近的方法论前驱；但其 facets 完全限于方法论层面，未涉及 infrastructure
11	- **我们的差异化**: 我们将 G-theory 框架扩展到 infrastructure facets（precision/hardware/batch），实现 infrastructure × methodology 的联合交叉分解，这是 Mesting 未触及的维度
12	
13	### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition
14	- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量
15	- **方法**: 提出基于语义层次的方差分解框架，将 prompt 变异按语义保持程度分级
16	- **与本工作的关系**: complements — 提供了 prompt 方差的细粒度语义分解，其 articulation 分量对应我们框架中 prompt paraphrase facet
17	- **我们的差异化**: Kunievsky 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的全交叉设计；我们的框架同时容纳 prompt 和 infrastructure facets
18	
19	### [Nalisnick et al., 2024] — GeneralizIT: G-theory Software for ML
20	- **核心发现**: 为 ML 场景提供 G-theory 计算工具包（Python），简化 REML 估计和 D-study 设计流程
21	- **方法**: Python 实现 G-theory 核心计算，包括方差分量估计和 D-study 投影
22	- **与本工作的关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现
23	- **我们的差异化**: GeneralizIT 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget
24	
25	## (b) Infrastructure Variance
26	
27	### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance
28	- **核心发现**: BF16 推理导致高达 9% 的 accuracy 标准差和 9,000-token 的回复长度偏移，FP32 接近 0%；推理模型（reasoning models）受影响最大；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存
29	- **方法**: 系统性测试不同 GPU 数量、类型、精度配置下的 LLM 推理输出变异，对比 FP32/BF16/FP16 的准确率和生成长度差异
30	- *
…[truncated 3515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T21:04:11.352566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bui 2025 seed sensitivity LLM fine-tuning variance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bui 2025 seed sensitivity LLM fine-tuning variance"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T21:04:11.352755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Same Prompt Different Outcomes\" 2026 LLM reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Same Prompt Different Outcomes\" 2026 LLM reproducibility"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T21:04:11.352912+00:00_

Web search results for query: "Bui 2025 seed sensitivity LLM fine-tuning variance"

Links: [{"title":"[2503.07329] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://arxiv.org/abs/2503.07329"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://arxiv.org/html/2503.07329v2"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning","url":"https://openreview.net/pdf?id=hWYXNwJV5Y"},{"title":"[Literature Review] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://www.themoonlight.io/en/review/assessing-the-macro-and-micro-effects-of-random-seeds-on-fine-tuning-large-language-models"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models | OpenReview","url":"https://openreview.net/forum?id=SnJh6fszp5"},{"title":"[PDF] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Assessing-the-Macro-and-Micro-Effects-of-Random-on-Zhou-Savova/f59cbffc46a6b0376f1b296fce2332658ae45818"},{"title":"The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior","url":"https://arxiv.org/html/2512.12066v2"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning","url":"https://arxiv.org/pdf/2503.07329"},{"title":"Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency","url":"https://arxiv.org/pdf/2506.17209"}]

Based on the search results, I found the relevant paper by Bui et al. on seed sensitivity in LLM fine-tuning variance:

The paper "Assessing the Macro and Micro Effects of Random Seeds on Fine-Tunin
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T21:04:11.353083+00:00_

Web search results for query: ""Same Prompt Different Outcomes" 2026 LLM reproducibility"

Links: [{"title":"[2602.14349] Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs","url":"https://arxiv.org/abs/2602.14349"},{"title":"Non-Deterministic LLM Prompts in 2026: A Practical Guide","url":"https://futureagi.com/blog/non-deterministic-llm-prompts-2025/"},{"title":"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMsWe thank Monica Alexander and Jamie Stafford for helpful suggestions. We gratefully acknowledge the financial support of the Data Sciences Institute at the University of Toronto and NSERC Alliance. Cui conducted this analysis while working at the Investigative Journalism Foundation (IJF) and we gratefully acknowledge the IJF for providing the appointments database. Contact: rohan.alexander@utoronto.ca.","url":"https://arxiv.org/html/2602.14349"},{"title":"Same Prompt, Different Outcomes: Evaluating","url":"https://arxiv.org/pdf/2602.14349"},{"title":"Reproducibility: Is your AI project doomed? | TechTarget","url":"https://www.techtarget.com/searchenterpriseai/post/Reproducibility-Is-your-AI-project-doomed"},{"title":"Reflections on the Reproducibility of Commercial LLM ...","url":"https://arxiv.org/pdf/2510.25506"},{"title":"When “Better” Prompts Hurt: Evaluation-Driven Iteration for LLM Applications A Framework with Reproducible Local Experiments","url":"https://arxiv.org/html/2601.22025v1"}]

Based on the search results, I found the research paper and related information about LLM reproducibility in 2026:

## Key Finding: "Same Prompt, Different Outcomes" Research

A systematic study evaluates the reproducibility of data analysis conducted by Large Language Models, testing two prompting strategies, six models, and four temperature settings, with ten independent executions per configuration, yielding 480 total attempts. The researchers assessed completion, concordance, validity, and
…[truncated 977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T21:04:11.353252+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T21:04:11.353374+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:04:11.353532+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.07329",
  "prompt": "Extract: 1) Full author list 2) Which models were fine-tuned (e.g. RoBERTa, LLaMA, etc.) 3) Which datasets/benchmarks were used (e.g. GLUE tasks) 4) Fine-tuning method (full fine-tune, LoRA, etc.) 5) Key metrics used (accuracy, F1, consistency, RTES variance, etc.) 6) Main quantitative findings about seed sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2503.07329",
    "prompt": "Extract: 1) Full author list 2) Which models were fine-tuned (e.g. RoBERTa, LLaMA, etc.) 3) Which datasets/benchmarks were used (e.g. GLUE tasks) 4) Fine-tuning method (full fine-tune, LoRA, etc.) 5) Key metrics used (accuracy, F1, consistency, RTES variance, etc.) 6) Main quantitative findings about seed sensitivity"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T21:04:11.353653+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.14349",
  "prompt": "Extract: 1) Full author list and year 2) Specific evaluation tasks/benchmarks used 3) Which LLM models were tested 4) Evaluation metrics (accuracy, BLEU, concordance, etc.) 5) The two prompting strategies mentioned 6) Main quantitative findings about reproducibility variance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.14349",
    "prompt": "Extract: 1) Full author list and year 2) Specific evaluation tasks/benchmarks used 3) Which LLM models were tested 4) Evaluation metrics (accuracy, BLEU, concordance, etc.) 5) The two prompting strategies mentioned 6) Main quantitative findings about reproducibility variance"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T21:04:11.353776+00:00_

# Paper Analysis: Random Seeds in LLM Fine-Tuning

Based on the arXiv page content provided, here's what can be extracted:

## 1) Full Author List
Nghia Bui, Guergana Savova, and Lijing Wang

## 2) Models Fine-Tuned
**Not specified** in the provided content. The abstract and metadata do not identify which specific LLM architectures were evaluated.

## 3) Datasets/Benchmarks Used
The study employed "the GLUE and SuperGLUE benchmarks" for systematic evaluation across multiple tasks.

## 4) Fine-Tuning Method
**Not specified** in the available content. The methodology section describing fine-tuning approach is not included in this page excerpt.

## 5) Key Metrics Used
- Accuracy and F1 (macro-level)
- Mean and variance calculations (to quantify performance fluctuations)
- **Consistency**: "a novel metric, measuring the stability of individual predictions across runs"

## 6) Main Quantitative Findings
The abstract indicates "significant variance at both macro and micro levels," emphasizing the necessity for "careful consideration of random seeds in fine-tuning and evaluation." However, specific numerical results are not provided in this excerpt.

**Note:** The full paper PDF would contain detailed findings, model specifications, and complete methodology details not visible on this abstract page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T21:04:11.353916+00:00_

# Research Paper Extraction: LLM Data Analysis Reproducibility

**1) Authors and Year:**
Jiaxin Cui and Rohan Alexander (2026)

**2) Evaluation Tasks/Benchmarks:**
The abstract doesn't specify particular benchmarks. The study evaluated LLM performance on data analysis tasks using a systematic experimental design rather than named benchmark datasets.

**3) LLM Models Tested:**
Six models were evaluated, but the abstract does not identify them by name.

**4) Evaluation Metrics:**
The authors assessed four key dimensions: "completion, concordance, validity, and consistency" of analytical attempts. Specific numerical metrics (accuracy, BLEU scores) aren't mentioned in the abstract.

**5) Prompting Strategies:**
Two strategies were compared, but the abstract doesn't describe what differentiated them.

**6) Main Quantitative Findings:**
The study conducted "480 total attempts" across configurations (6 models × 2 prompting strategies × 4 temperature settings × 10 executions). The research found "considerable variation in the analytical results even for consistent configurations," indicating that reproducibility is problematic—suggesting researchers using LLMs for analysis should "run multiple times independently and the distribution of results considered."

*Note: The abstract provides limited methodological detail; the full paper would contain specifics on models, strategies, and metrics.*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T21:04:11.354069+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2503.07329v2",
  "prompt": "Extract the following specific details: 1) Which LLM models were fine-tuned (e.g. RoBERTa-base, RoBERTa-large, LLaMA, GPT-2, etc.)? 2) Fine-tuning method: was it full fine-tuning, LoRA, adapter, or something else? 3) How many random seeds were tested? 4) List specific GLUE/SuperGLUE tasks used with their quantitative results - especially the RTES variance=18.22 finding and consistency scores. 5) Any other key quantitative findings about seed sensitivity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2503.07329v2",
    "prompt": "Extract the following specific details: 1) Which LLM models were fine-tuned (e.g. RoBERTa-base, RoBERTa-large, LLaMA, GPT-2, etc.)? 2) Fine-tuning method: was it full fine-tuning, LoRA, adapter, or something else? 3) How many random seeds were tested? 4) List specific GLUE/SuperGLUE tasks used with their quantitative results - especially the RTES variance=18.22 finding and consistency scores. 5) Any other key quantitative findings about seed sensitivity."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T21:04:11.354187+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2602.14349",
  "prompt": "Extract: 1) Which 6 specific LLM models were tested? 2) What are the two prompting strategies? 3) What specific data analysis tasks were used (datasets, analysis types)? 4) The four temperature settings. 5) Specific quantitative results for completion rate, concordance, validity, consistency. 6) Key findings about which factors (model, temperature, prompt strategy) contributed most to variance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2602.14349",
    "prompt": "Extract: 1) Which 6 specific LLM models were tested? 2) What are the two prompting strategies? 3) What specific data analysis tasks were used (datasets, analysis types)? 4) The four temperature settings. 5) Specific quantitative results for completion rate, concordance, validity, consistency. 6) Key findings about which factors (model, temperature, prompt strategy) contributed most to variance."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T21:04:11.354309+00:00_

# Research Summary: Random Seeds in LLM Fine-Tuning

## Models Tested
Two pretrained language models were evaluated:
- **RoBERTa-large** (~350M parameters) with full fine-tuning
- **Llama3.2-3B** (~3.21B parameters) with LoRA fine-tuning

## Fine-Tuning Methods
1. **RoBERTa-large**: Full fine-tuning across all parameters
2. **Llama3.2-3B**: Parameter-efficient LoRA fine-tuning, updating approximately 2.3 million parameters

## Random Seeds
The study tested **10 randomly chosen seeds**: 42, 52, 62, 72, 82, 92, 102, 112, 122, and 132.

## GLUE/SuperGLUE Results

### Key Variance Findings (RoBERTa-large):
- **RTES**: Variance of 16.67 (high sensitivity)
- **COPA**: Variance of 16.83 (highest variance)
- **MultiRC**: Variance of 13.30
- **Stable tasks**: QQP (0.06), QNLI (0.38), SST2 (0.55)

### Consistency Scores (RoBERTa-large):
- High consistency: SST2 (96.83%), QNLI (95.64%), QQP (95.57%)
- Low consistency: COPA (64.88%), RTES (70.05%)

### Critical Finding
Figure 1 demonstrates the core issue: two models with identical 60% accuracy showed only 20% overlapping individual predictions, illustrating significant "micro-level" instability despite stable "macro-level" performance.

## Additional Key Quantitative Insights
- Llama3.2-3B with LoRA exhibited "significantly lower variance across most tasks" compared to RoBERTa-large
- Training dataset size showed weak negative correlation (-0.3918) with variance and moderate positive correlation (0.4257) with consistency

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T21:04:11.354493+00:00_

# LLM Data Analysis Reproducibility Study: Key Findings

## 1) Six LLM Models Tested
The study evaluated models from three providers:
- **Anthropic**: Claude Haiku 4.5, Claude Opus 4.6
- **OpenAI**: GPT-5-mini, GPT-5.2
- **Google**: Gemini Flash 3, Gemini Pro 3

## 2) Two Prompting Strategies

**Multi-step approach**: Five sequential prompts, each generating individual Python scripts executed in order. An error at any stage prevents subsequent steps from running.

**Single-step approach**: One comprehensive prompt generating a complete pipeline script. The model creates internally consistent code as a unified unit, reducing error propagation.

## 3) Data Analysis Tasks

The task involved analyzing Canadian government appointment records from New Brunswick (2013-2024):
- Step 1: Consolidate 12 annual CSV files
- Step 2: Identify reappointment patterns via name-position-organization matching
- Step 3: Aggregate to organization-year summaries
- Step 4: Perform OLS regression (reappointment rate vs. total appointments)
- Step 5: Generate scatter plot with regression line

The dataset contained 3,718 appointment records across 43 organizations.

## 4) Four Temperature Settings
0.0, 0.3, 0.7, and 1.0 (lower values favor more probable tokens; GPT-5-mini only used default temperature of 1.0)

## 5) Quantitative Results

| Metric | Key Findings |
|--------|--------------|
| **Completion** | Single-step: consistently high rates; Multi-step: substantially lower due to error propagation (e.g., Gemini Flash 3: 100% single-step vs. 0% multi-step) |
| **Concordance** | Steps 2-3 showed lowest concordance with human analysis; Steps 4-5 higher; many LLM reappointment rate estimates were systematically lower |
| **Validity** | "high for almost all configurations" across steps |
| **Consistency** | "considerable variation in analytical results even for consistent configurations"; t-statistics remained near zero in most cases but some single-step configurations produced values suggesti
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T21:04:11.354681+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
  "old_string": "- **方法**: 多温度多模型重复实验设计 [需补充：具体评估任务和指标]",
  "new_string": "- **方法**: 在加拿大政府任命记录数据集（3,718 条记录）上，使用 6 个模型（Claude Haiku 4.5、Claude Opus 4.6、GPT-5-mini、GPT-5.2、Gemini Flash 3、Gemini Pro 3）× 2 种 prompting 策略（multi-step 分步 vs. single-step 一次性）× 4 个温度（0.0/0.3/0.7/1.0）× 10 次重复，共 480 次执行；评估指标为 completion（完成率）、concordance（与人工分析一致性）、validity（有效性）、consistency（跨运行一致性）；发现 prompting 策略是主导方差源，数据预处理步骤产生最大分析分歧，即使 T=0 也存在非确定性"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
    "old_string": "- **方法**: 多温度多模型重复实验设计 [需补充：具体评估任务和指标]",
    "new_string": "- **方法**: 在加拿大政府任命记录数据集（3,718 条记录）上，使用 6 个模型（Claude Haiku 4.5、Claude Opus 4.6、GPT-5-mini、GPT-5.2、Gemini Flash 3、Gemini Pro 3）× 2 种 prompting 策略（multi-step 分步 vs. single-step 一次性）× 4 个温度（0.0/0.3/0.7/1.0）× 10 次重复，共 480 次执行；评估指标为 completion（完成率）、concordance（与人工分析一致性）、validity（有效性）、consistency（跨运行一致性）；发现 prompting 策略是主导方差源，数据预处理步骤产生最大分析分歧，即使 T=0 也存在非确定性"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T21:04:11.354829+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T21:04:11.354957+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
  "old_string": "- **方法**: [需补充：具体微调设置、模型、数据集]",
  "new_string": "- **方法**: 对 RoBERTa-large（全参数微调）和 Llama3.2-3B（LoRA，~2.3M 可训练参数）在 GLUE/SuperGLUE 基准上以 10 个随机种子（42–132）重复微调；宏观指标为 accuracy/F1 的均值和方差，微观指标为自定义 consistency（跨种子个体预测稳定性）；RoBERTa-large 方差极端分化——COPA 方差 16.83、RTE 方差 16.67，而 QQP 仅 0.06；LoRA 微调的 Llama 在多数任务上方差显著低于全参数微调"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
    "old_string": "- **方法**: [需补充：具体微调设置、模型、数据集]",
    "new_string": "- **方法**: 对 RoBERTa-large（全参数微调）和 Llama3.2-3B（LoRA，~2.3M 可训练参数）在 GLUE/SuperGLUE 基准上以 10 个随机种子（42–132）重复微调；宏观指标为 accuracy/F1 的均值和方差，微观指标为自定义 consistency（跨种子个体预测稳定性）；RoBERTa-large 方差极端分化——COPA 方差 16.83、RTE 方差 16.67，而 QQP 仅 0.06；LoRA 微调的 Llama 在多数任务上方差显著低于全参数微调"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T21:04:11.355098+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_placeholders_20260520T210242",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T21:04:11.355242+00:00_

两处 `[需补充]` 已替换：

1. **Bui et al., 2025** — 补全为：RoBERTa-large（全参数微调）+ Llama3.2-3B（LoRA）在 GLUE/SuperGLUE 上以 10 种子重复；COPA 方差 16.83、RTE 方差 16.67（高敏感），QQP 仅 0.06（稳定）；LoRA 微调方差显著低于全参数微调。

2. **Same Prompt, Different Outcomes (Cui & Alexander, 2026)** — 补全为：6 模型（Claude/GPT-5/Gemini 系列）× 2 prompting 策略 × 4 温度 × 10 重复，共 480 次；在政府任命记录数据分析任务上评估 completion/concordance/validity/consistency 四维指标；prompting 策略为主导方差源，T=0 下仍存在非确定性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related_work_placeholders_20260520T210242"
}
```

</details>

---
