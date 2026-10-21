# paper research cluster3 prompt

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_paper_research_cluster3_prompt_20260521T183830.jsonl`
- **Structured JSON:** [`493ac9fa70ad3ac0dc79.json`](../../sessions/49/493ac9fa70ad3ac0dc79.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-21T18:41:41.573068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:41:41.573480+00:00_

1	meta:
2	  last_updated: "2026-05-21T12:00:00Z"
3	  total_papers: 18
4	
5	categories:
6	  - key: "gtheory_evaluation"
7	    name: "G-Theory & Evaluation Variance"
8	    narrative: "Applying Generalizability Theory and variance decomposition to LLM evaluation reliability"
9	  - key: "infrastructure_variance"
10	    name: "Infrastructure-Induced Variance"
11	    narrative: "Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference"
12	  - key: "prompt_sensitivity"
13	    name: "Prompt Sensitivity & Methodological Variance"
14	    narrative: "Prompt phrasing, seed, temperature, and ordering as variance sources"
15	  - key: "evaluation_methodology"
16	    name: "Evaluation Methodology"
17	    narrative: "Scoring artifacts, benchmark design, and evaluation protocol considerations"
18	
19	papers:
20	  mesting2026hidden:
21	    title: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"
22	    authors:
23	      - "Messing, S."
24	    year: 2026
25	    venue: "arXiv"
26	    url: "https://arxiv.org/abs/2604.11581"
27	    category: "gtheory_evaluation"
28	    role: "direct-competitor"
29	    relevance: "Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology."
30	    verified: true
31	    added_by: "director"
32	    added_at: "2026-05-20T14:00:00Z"
33	
34	  brittlebench2026:
35	    title: "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity"
36	    authors: []
37	    year: 2026
38	    venue: "arXiv"
39	    url: "https://arxiv.org/abs/2603.13285"
40	    category: "prompt_sensitivity"
41	    role: "direct-competitor"
42	    relevance: "Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single per
…[truncated 11742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:41:41.573703+00:00_

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
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
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

_source line 4 · 2026-05-21T18:41:41.573845+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:41:41.573987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brittlebench Quantifying LLM Robustness Prompt Sensitivity arXiv 2603.13285"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brittlebench Quantifying LLM Robustness Prompt Sensitivity arXiv 2603.13285"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T18:41:41.574133+00:00_

Web search results for query: "Brittlebench Quantifying LLM Robustness Prompt Sensitivity arXiv 2603.13285"

Links: [{"title":"[2603.13285] Brittlebench: Quantifying LLM robustness via prompt sensitivity","url":"https://arxiv.org/abs/2603.13285"},{"title":"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity","url":"https://arxiv.org/pdf/2603.13285"},{"title":"What Did I Do Wrong? Quantifying LLMs’ Sensitivity and Consistency to Prompt Engineering","url":"https://arxiv.org/html/2406.12334v1"},{"title":"[2406.12334] What Did I Do Wrong? Quantifying LLMs’ Sensitivity and Consistency to Prompt Engineering","url":"https://ar5iv.labs.arxiv.org/html/2406.12334v1"},{"title":"Towards LLMs Robustness to Changes in Prompt Format Styles","url":"https://arxiv.org/pdf/2504.06969"},{"title":"Towards LLMs Robustness to Changes in Prompt Format Styles","url":"https://arxiv.org/html/2504.06969v1"}]

The search results successfully retrieved information about the Brittlebench paper (arXiv 2603.13285). Here's what I found:

## Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity

This work introduces a theoretical framework for quantifying model sensitivity to prompt variants, or brittleness, that can enable disentangling data-induced difficulty from prompt-related variability.

**Key Problem Addressed:**
Existing evaluation methods largely rely on clean, static benchmarks, which can overestimate true model performance by failing to capture the noise and variability inherent in real-world user inputs. This is especially true for language models, which can face human-generated text queries containing mistakes, typos, or alternative ways of phrasing the same question.

**Methodology:**
The Brittlebench evaluation pipeline holistically evaluates the sensitivity of frontier models. Brittlebench applies a taxonomy of semantics-preserving perturbations on existing benchmarks, measuring model robustness by decomposing the variance of prompt sensitivity and the inherent 
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:41:41.574284+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hua \"Flaw or Artifact\" Rethinking Prompt Sensitivity Evaluating LLMs EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hua \"Flaw or Artifact\" Rethinking Prompt Sensitivity Evaluating LLMs EMNLP 2025"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T18:41:41.574450+00:00_

Web search results for query: "Hua "Flaw or Artifact" Rethinking Prompt Sensitivity Evaluating LLMs EMNLP 2025"

Links: [{"title":"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1006/"},{"title":"[2509.01790] Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs","url":"https://arxiv.org/abs/2509.01790"},{"title":"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs","url":"https://paperreading.club/page?id=335127"},{"title":"Artifact or Flaw? Rethinking Prompt Sensitivity in Evaluating LLMs | OpenReview","url":"https://openreview.net/forum?id=frH3KtOZPC"},{"title":"Paper page - Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs","url":"https://huggingface.co/papers/2509.01790"},{"title":"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs | Request PDF","url":"https://www.researchgate.net/publication/397420296_Flaw_or_Artifact_Rethinking_Prompt_Sensitivity_in_Evaluating_LLMs"},{"title":"Artifact or Flaw? Rethinking Prompt Sensitivity in Evaluating LLMs","url":"https://openreview.net/pdf?id=frH3KtOZPC"},{"title":"Prompt architecture induces methodological artifacts in large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036937/"},{"title":"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs","url":"https://arxiv.org/pdf/2509.01790"}]

I found the paper you were searching for! Here are the details:

**Paper Title:** Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs

**Authors:** Andong Hua, Kenan Tang, Chenhe Gu, Jindong Gu, Eric Wong, and Yao Qin

**Conference:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 19889–19899, Suzhou, China

**Main Findings:** Modern large language models are more robust to prompt templates than previously believed, and prompt sensitivity may be more an artifact of evaluation than a flaw in the m
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:41:41.574607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bui \"Assessing Macro Micro Effects Random Seeds Fine-Tuning Large Language Models\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bui \"Assessing Macro Micro Effects Random Seeds Fine-Tuning Large Language Models\" 2025"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T18:41:41.574760+00:00_

Web search results for query: "Bui "Assessing Macro Micro Effects Random Seeds Fine-Tuning Large Language Models" 2025"

Links: [{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-short.3/"},{"title":"[2503.07329] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://arxiv.org/abs/2503.07329"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://www.researchgate.net/publication/402605825_Assessing_the_Macro_and_Micro_Effects_of_Random_Seeds_on_Fine-Tuning_Large_Language_Models"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://arxiv.org/html/2503.07329v2"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models | OpenReview","url":"https://openreview.net/forum?id=SnJh6fszp5"},{"title":"[PDF] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Assessing-the-Macro-and-Micro-Effects-of-Random-on-Zhou-Savova/f59cbffc46a6b0376f1b296fce2332658ae45818"},{"title":"[Literature Review] Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://www.themoonlight.io/en/review/assessing-the-macro-and-micro-effects-of-random-seeds-on-fine-tuning-large-language-models"},{"title":"(PDF) Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://www.researchgate.net/publication/389748545_Assessing_the_Macro_and_Micro_Effects_of_Random_Seeds_on_Fine-Tuning_Large_Language_Models"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning","url":"https://arxiv.org/pdf/2503.07329"}]

Based on the search results, I found the paper you're
…[truncated 1493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T18:41:41.574900+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Same Prompt Different Outcomes\" Evaluating Reproducibility Data Analysis LLMs arXiv 2602.14349"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Same Prompt Different Outcomes\" Evaluating Reproducibility Data Analysis LLMs arXiv 2602.14349"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:41:41.575039+00:00_

Web search results for query: ""Same Prompt Different Outcomes" Evaluating Reproducibility Data Analysis LLMs arXiv 2602.14349"

Links: [{"title":"[2602.14349] Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs","url":"https://arxiv.org/abs/2602.14349"},{"title":"Evaluating the Reproducibility of Data Analysis by LLMs","url":"https://arxiv.org/pdf/2602.14349"},{"title":"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMsWe thank Monica Alexander and Jamie Stafford for helpful suggestions. We gratefully acknowledge the financial support of the Data Sciences Institute at the University of Toronto and NSERC Alliance. Cui conducted this analysis while working at the Investigative Journalism Foundation (IJF) and we gratefully acknowledge the IJF for providing the appointments database. Contact: rohan.alexander@utoronto.ca.","url":"https://arxiv.org/html/2602.14349"},{"title":"AIRepr: An Analyst-Inspector Framework for Evaluating Reproducibility of LLMs in Data Science","url":"https://arxiv.org/pdf/2502.16395"},{"title":"Jagged competencies: Measuring the reliability of generative AI in academic research - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0148296325006277"},{"title":"AIRepr: An Analyst-Inspector Framework for Evaluating ...","url":"https://aclanthology.org/2025.findings-emnlp.539.pdf"},{"title":"A statistical framework for evaluating the repeatability and reproducibility of large language models","url":"https://www.medrxiv.org/content/10.1101/2025.08.06.25333170.full.pdf"},{"title":"A statistical framework for evaluating the repeatability and reproducibility of large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12637745/"}]

I found the paper! Here's information about arXiv paper 2602.14349:

**Title:** Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs

**Authors:** Jiaxin Cui and Rohan Alexander

…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T18:41:41.575182+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sclar \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sclar \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T18:41:41.575322+00:00_

Web search results for query: "Sclar "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" ICLR 2024"

Links: [{"title":"ICLR Poster Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://iclr.cc/virtual/2024/poster/18650"},{"title":"[2310.11324v2] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324v2"},{"title":"[2310.11324] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt   Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/pdf/2310.11324"},{"title":"Understanding the effects of iterative prompting on truthfulness | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693094"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10520219-quantifying-language-models-sensitivity-spurious-features-prompt-design-how-learned-start-worrying-about-prompt-formatting"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://blog.athina.ai/quantifying-language-models-sensitivity-to-spurious-features-in-prompt-design-or-how-i-learned-to-start-worrying-about-prompt-formatting"},{"title":"[PDF] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | Semantic Scho
…[truncated 2082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T18:41:41.575481+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "answer option ordering effect multiple choice LLM evaluation benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "answer option ordering effect multiple choice LLM evaluation benchmark 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T18:41:41.575619+00:00_

Web search results for query: "answer option ordering effect multiple choice LLM evaluation benchmark 2024 2025"

Links: [{"title":"Do Large Language Models Plan Answer Positions? Position Bias in Multiple-Choice Question Generation","url":"https://arxiv.org/html/2605.01846"},{"title":"Multiple-Choice Questions are Efficient and Robust LLM Evaluators","url":"https://arxiv.org/html/2405.11966v4"},{"title":"[2308.11483] Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions","url":"https://arxiv.org/abs/2308.11483"},{"title":"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.130/"},{"title":"Large Language Models Sensitivity to The Order of Options in   Multiple-Choice Questions","url":"https://arxiv.org/pdf/2308.11483"},{"title":"Order Matters: Assessing LLM Sensitivity in Multiple-Choice Tasks - Megagon","url":"https://megagon.ai/order-matters-llm-sensitiv-mult-choice-tsks/"},{"title":"Large Language Models Are Not Robust Multiple Choice Selectors","url":"https://arxiv.org/pdf/2309.03882"}]

Based on the search results, here's what research has found about answer option ordering effects in multiple-choice LLM evaluation benchmarks:

## Key Findings

LLMs exhibit systematic position biases, disproportionately favoring certain answer positions. Research demonstrates a considerable performance gap of approximately 13% to 75% in LLMs on different benchmarks when answer options are reordered, even when using demonstrations in a few-shot setting.

## Position Bias Mechanisms

This sensitivity arises when LLMs are uncertain about the prediction between the top-2/3 choices, and specific options placements may favor certain predictions between those top choices depending on the question caused by positional bias. LLMs exhibit selection bias when answering MCQs, often preferring specific option identifiers such as "Option A" due to token-le
…[truncated 890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T18:41:41.575785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pezeshkpour Hruschka \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\" NAACL 2024 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pezeshkpour Hruschka \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\" NAACL 2024 authors"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T18:41:41.575935+00:00_

Web search results for query: "Pezeshkpour Hruschka "Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions" NAACL 2024 authors"

Links: [{"title":"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.130/"},{"title":"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions | CiNii Research","url":"https://cir.nii.ac.jp/crid/1360870768893229184"},{"title":"Large Language Models Sensitivity to The Order of Options ...","url":"https://aclanthology.org/2024.findings-naacl.130.pdf"},{"title":"[PDF] Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Sensitivity-to-The-Order-of-Pezeshkpour-Hruschka/fd81018bc72b030545a2d3f3010f3758ec4d48c3"},{"title":"Large Language Models Sensitivity to The Order of Options in   Multiple-Choice Questions","url":"https://arxiv.org/pdf/2308.11483"},{"title":"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions | Request PDF","url":"https://www.researchgate.net/publication/382633315_Large_Language_Models_Sensitivity_to_The_Order_of_Options_in_Multiple-Choice_Questions"},{"title":"Order Matters: Assessing LLM Sensitivity in Multiple-Choice Tasks - Megagon","url":"https://megagon.ai/order-matters-llm-sensitiv-mult-choice-tsks/"},{"title":"Order Matters: Assessing LLM Sensitivity in Multiple-Choice Tasks | by Megagon Labs | Medium","url":"https://megagonlabs.medium.com/order-matters-assessing-llm-sensitivity-in-multiple-choice-tasks-43bf4f3740f4"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Large+language+models+sensitivity+to+the+order+of+options+in+multiple-choice+questions&amp=&author=P+Pezeshkpour&amp=&author=E+Hruschka"},{"title":"[2308.11483] Large Language Models Sensitivity to The Ord
…[truncated 615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T18:41:41.576083+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brittlebench arXiv 2603.13285 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brittlebench arXiv 2603.13285 authors full list"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:41:41.576217+00:00_

Web search results for query: "Brittlebench arXiv 2603.13285 authors full list"

Links: [{"title":"[2603.13285] Brittlebench: Quantifying LLM robustness via prompt sensitivity","url":"https://arxiv.org/abs/2603.13285"},{"title":"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity","url":"https://arxiv.org/html/2603.13285"},{"title":"Brittlebench: Quantifying LLM robustness via prompt sensitivity","url":"https://arxiv.org/pdf/2603.13285"},{"title":"A 3D benchmark problem for crack propagation in brittle fracture","url":"https://arxiv.org/pdf/1910.06691"},{"title":"Cracking double-blind review: Authorship attribution with deep learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313031/"}]

Based on the search results, the full list of authors for the Brittlebench arXiv paper (2603.13285) is:

1. Angelika Romanou
2. Mark Ibrahim
3. Candace Ross
4. Chantal Shaib
5. Kerem Oktar
6. Samuel J. Bell
7. Anaelia Ovalle
8. Jesse Dodge
9. Antoine Bosselut
10. Koustuv Sinha
11. Adina Williams


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T18:41:41.576341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sclar Choi Tsvetkov Suhr \"quantifying language models sensitivity spurious features prompt design\" ICLR 2024 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sclar Choi Tsvetkov Suhr \"quantifying language models sensitivity spurious features prompt design\" ICLR 2024 DOI"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T18:41:41.576510+00:00_

Web search results for query: "Sclar Choi Tsvetkov Suhr "quantifying language models sensitivity spurious features prompt design" ICLR 2024 DOI"

Links: [{"title":"ICLR Poster Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://iclr.cc/virtual/2024/poster/18650"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf"},{"title":"[2310.11324v2] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324v2"},{"title":"[2310.11324] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10520219-quantifying-language-models-sensitivity-spurious-features-prompt-design-how-learned-start-worrying-about-prompt-formatting"},{"title":"Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/html/2310.11324v2"},{"title":"Assessing and Understanding the Prompt Sensitivity of LLMs","url":"https://aclanthology.org/2024.findings-emnlp.108.pdf"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | OpenReview","url":"https://openreview.net/forum?id=RIu5lyNXjT"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt   Design or: How I learned to start worrying about prompt formatting","
…[truncated 1525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T18:41:41.576703+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors:\n      - \"Romanou, A.\"\n      - \"Ibrahim, M.\"\n      - \"Ross, C.\"\n      - \"Shaib, C.\"\n      - \"Oktar, K.\"\n      - \"Bell, S.J.\"\n      - \"Ovalle, A.\"\n      - \"Dodge, J.\"\n      - \"Bosselut, A.\"\n      - \"Sinha, K.\"\n      - \"Williams, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors:\n      - \"Romanou, A.\"\n      - \"Ibrahim, M.\"\n      - \"Ross, C.\"\n      - \"Shaib, C.\"\n      - \"Oktar, K.\"\n      - \"Bell, S.J.\"\n      - \"Ovalle, A.\"\n      - \"Dodge, J.\"\n      - \"Bosselut, A.\"\n      - \"Sinha, K.\"\n      - \"Williams, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T18:41:41.576906+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T18:41:41.577042+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, A.\"\n      - \"Tang, K.\"\n      - \"Gu, C.\"\n      - \"Gu, J.\"\n      - \"Wong, E.\"\n      - \"Qin, Y.\"\n    year: 2025\n    venue: \"EMNLP 2025\"\n    url: \"https://aclanthology.org/2025.emnlp-main.1006/\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, A.\"\n      - \"Tang, K.\"\n      - \"Gu, C.\"\n      - \"Gu, J.\"\n      - \"Wong, E.\"\n      - \"Qin, Y.\"\n    year: 2025\n    venue: \"EMNLP 2025\"\n    url: \"https://aclanthology.org/2025.emnlp-main.1006/\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T18:41:41.577242+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T18:41:41.577409+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, N.T.\"\n      - \"Savova, G.\"\n      - \"Wang, L.\"\n    year: 2025\n    venue: \"IJCNLP-AACL 2025\"\n    url: \"https://aclanthology.org/2025.ijcnlp-short.3/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, N.T.\"\n      - \"Savova, G.\"\n      - \"Wang, L.\"\n    year: 2025\n    venue: \"IJCNLP-AACL 2025\"\n    url: \"https://aclanthology.org/2025.ijcnlp-short.3/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T18:41:41.577608+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T18:41:41.577740+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors:\n      - \"Cui, J.\"\n      - \"Alexander, R.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors:\n      - \"Cui, J.\"\n      - \"Alexander, R.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T18:41:41.577934+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T18:41:41.578071+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "offset": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "offset": "300"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T18:41:41.578205+00:00_

300	    verified: true
301	    added_by: "worker"
302	    added_at: "2026-05-21T00:00:00Z"
303	
304	  shanmugavelu2024floating:
305	    title: "Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications"
306	    authors:
307	      - "Shanmugavelu, S."
308	      - "Taillefumier, M."
309	      - "Culver, C."
310	      - "Hernandez, O."
311	      - "Coletti, M."
312	      - "Sedova, A."
313	    year: 2024
314	    venue: "SC'24 Workshops (IEEE)"
315	    url: "https://arxiv.org/abs/2408.05148"
316	    doi: "10.1109/SCW63240.2024.00028"
317	    category: "infrastructure_variance"
318	    role: "background"
319	    relevance: "Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference."
320	    verified: true
321	    added_by: "worker"
322	    added_at: "2026-05-21T12:00:00Z"
323	
324	  zhang2025tbik:
325	    title: "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch"
326	    authors:
327	      - "Zhang, Z."
328	      - "Ding, X."
329	      - "Yuan, J."
330	      - "Liu, R."
331	      - "Mao, H."
332	      - "Xing, J."
333	      - "Liu, Z."
334	    year: 2025
335	    venue: "arXiv"
336	    url: "https://arxiv.org/abs/2511.17826"
337	    category: "infrastructure_variance"
338	    role: "method-component"
339	    relevance: "Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design."
340	    verified: true
341	    added_by: "worker"
342	    added_at: "2026-05-21T12:00:00Z"
343	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T18:41:41.578378+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    added_at: \"2026-05-21T12:00:00Z\"",
  "new_string": "    added_at: \"2026-05-21T12:00:00Z\"\n\n  sclar2024formatting:\n    title: \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying About Prompt Formatting\"\n    authors:\n      - \"Sclar, M.\"\n      - \"Choi, Y.\"\n      - \"Tsvetkov, Y.\"\n      - \"Suhr, A.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    url: \"https://arxiv.org/abs/2310.11324\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 76 accuracy points swing from formatting choices (LLaMA-2-13B). Proposes FORMATSPREAD for evaluating prompt format sensitivity. Demonstrates that even meaning-preserving formatting changes drastically alter benchmark rankings. Seminal prompt sensitivity work our paper builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  pezeshkpour2024ordering:\n    title: \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\"\n    authors:\n      - \"Pezeshkpour, P.\"\n      - \"Hruschka, E.\"\n    year: 2024\n    venue: \"NAACL 2024 Findings\"\n    url: \"https://aclanthology.org/2024.findings-naacl.130/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    added_at: \"2026-05-21T12:00:00Z\"",
    "new_string": "    added_at: \"2026-05-21T12:00:00Z\"\n\n  sclar2024formatting:\n    title: \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying About Prompt Formatting\"\n    authors:\n      - \"Sclar, M.\"\n      - \"Choi, Y.\"\n      - \"Tsvetkov, Y.\"\n      - \"Suhr, A.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    url: \"https://arxiv.org/abs/2310.11324\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 76 accuracy points swing from formatting choices (LLaMA-2-13B). Proposes FORMATSPREAD for evaluating prompt format sensitivity. Demonstrates that even meaning-preserving formatting changes drastically alter benchmark rankings. Seminal prompt sensitivity work our paper builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  pezeshkpour2024ordering:\n    title: \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\"\n    authors:\n      - \"Pezeshkpour, P.\"\n      - \"Hruschka, E.\"\n    year: 2024\n    venue: \"NAACL 2024 Findings\"\n    url: \"https://aclanthology.org/2024.findings-naacl.130/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T18:41:41.578558+00:00_

&lt;tool_use_error>Found 2 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: "2026-05-21T12:00:00Z"&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T18:41:41.578696+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"",
  "new_string": "  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  sclar2024formatting:\n    title: \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying About Prompt Formatting\"\n    authors:\n      - \"Sclar, M.\"\n      - \"Choi, Y.\"\n      - \"Tsvetkov, Y.\"\n      - \"Suhr, A.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    url: \"https://arxiv.org/abs/2310.11324\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 76 accuracy points swing from formatting choices (LLaMA-2-13B). Proposes FORMATSPREAD for evaluating prompt format sensitivity. Demonstrates that even meaning-preserving formatting changes drastically alter benchmark rankings. Seminal prompt sensitivity work our paper builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  pezeshkpour2024ordering:\n    title: \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\"\n    authors:\n      - \"Pezeshkpour, P.\"\n      - \"Hruschka, E.\"\n    year: 2024\n    venue: \"NAACL 2024 Findings\"\n    url: \"https://aclanthology.org/2024.findings-naacl.130/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"",
    "new_string": "  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  sclar2024formatting:\n    title: \"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying About Prompt Formatting\"\n    authors:\n      - \"Sclar, M.\"\n      - \"Choi, Y.\"\n      - \"Tsvetkov, Y.\"\n      - \"Suhr, A.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    url: \"https://arxiv.org/abs/2310.11324\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 76 accuracy points swing from formatting choices (LLaMA-2-13B). Proposes FORMATSPREAD for evaluating prompt format sensitivity. Demonstrates that even meaning-preserving formatting changes drastically alter benchmark rankings. Seminal prompt sensitivity work our paper builds upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\"\n\n  pezeshkpour2024ordering:\n    title: \"Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions\"\n    authors:\n      - \"Pezeshkpour, P.\"\n      - \"Hruschka, E.\"\n    year: 2024\n    venue: \"NAACL 2024 Findings\"\n    url: \"https://aclanthology.org/2024.findings-naacl.130/\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents 13-75% performance gap from answer option reordering in MC benchmarks. Shows LLMs exhibit systematic positional bias favoring certain option identifiers. Demonstrates option ordering as a methodological variance source our G-study framework captures.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T18:41:41.578920+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T18:41:41.579062+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  total_papers: 18",
  "new_string": "  total_papers: 20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  total_papers: 18",
    "new_string": "  total_papers: 20"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T18:41:41.579237+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-21T18:41:41.579407+00:00_

Cluster 3 完成，6 篇全部 verified：

| bibtex_key | 状态 | 变更 |
|---|---|---|
| `brittlebench2026` | verified | 补全 11 位作者 |
| `hua2025flaw` | verified | 作者从 1→6 人，补 ACL Anthology URL |
| `bui2025seeds` | verified | 作者从 1→3 人，venue 更正为 IJCNLP-AACL 2025 |
| `sameprompt2026` | verified | 补全作者 Cui & Alexander |
| `sclar2024formatting` | **新增** | Sclar et al. ICLR 2024，76pt accuracy swing from formatting |
| `pezeshkpour2024ordering` | **新增** | Pezeshkpour & Hruschka NAACL 2024 Findings，MC 选项顺序敏感性 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_cluster3_prompt_20260521T183830"
}
```

</details>

---
