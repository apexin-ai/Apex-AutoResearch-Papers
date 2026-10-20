# research evidence cost literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 91
- **Recorded user turns:** 0
- **Tool calls:** 45
- **Original source:** `logs/chats/worker_research_evidence-cost-literature_20260516T041839.jsonl`
- **Structured JSON:** [`6e42f8fadc6bf8eea09c.json`](../../sessions/6e/6e42f8fadc6bf8eea09c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

91 recorded events

### Tool call

_source line 1 · 2026-05-16T04:24:15.207913+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__append_idea",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T04:24:15.208450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T04:24:15.208763+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T04:24:15.209357+00:00_

Error: result (102,344 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T04:24:15.209607+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"rationale generation\" NLP \"task performance\" degradation trade-off"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"rationale generation\" NLP \"task performance\" degradation trade-off"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T04:24:15.209812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"evidence generation\" \"relation extraction\" performance cost trade-off"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"evidence generation\" \"relation extraction\" performance cost trade-off"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T04:24:15.209979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"chain-of-thought\" extraction \"accuracy trade-off\" information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"chain-of-thought\" extraction \"accuracy trade-off\" information extraction"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T04:24:15.210562+00:00_

Web search results for query: ""chain-of-thought" extraction "accuracy trade-off" information extraction"

Links: [{"title":"ARCHE: A Novel Task to Evaluate LLMs on Latent Reasoning Chain Extraction","url":"https://arxiv.org/html/2511.12485"},{"title":"Teaching RAG to Think: Chain-of-Thought Retrieval Guide - GeekyAnts","url":"https://geekyants.com/blog/teaching-your-rag-system-to-think-a-guide-to-chain-of-thought-retrieval"},{"title":"Chain-of-thought reasoning meets RAG: Rationale-guided retrieval systems explained | We Love Open Source • All Things Open","url":"https://allthingsopen.org/articles/chain-of-thought-reasoning-rag-rationale-guided-retrieval"},{"title":"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.153/"},{"title":"Knowledge Graph Efficient Construction: Embedding Chain-of-Thought into LLMs","url":"https://www.vldb.org/workshops/2024/proceedings/LLM+KG/LLM+KG-4.pdf"},{"title":"[2311.05922] Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction","url":"https://arxiv.org/abs/2311.05922"},{"title":"Unveiling the Key Factors for Distilling Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2502.18001v1"},{"title":"Invoice Information Extraction: Methods and Performance Evaluation","url":"https://arxiv.org/html/2510.15727v1"},{"title":"Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf"},{"title":"Evaluating chain-of-thought monitorability | OpenAI","url":"https://openai.com/index/evaluating-chain-of-thought-monitorability/"}]

I found several relevant research findings on chain-of-thought extraction and accuracy trade-offs in information extraction. Here are the key findings:

## Trade-off Between Coverage and Accuracy

Research on latent reasoning chain extraction shows 
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T04:24:15.210836+00:00_

Web search results for query: ""rationale generation" NLP "task performance" degradation trade-off"

Links: [{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 1074–1084","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"Degradation of Multi-Task Prompting Across Six NLP Tasks and LLM Families","url":"https://www.mdpi.com/2079-9292/14/21/4349"},{"title":"Automatic Transmission for LLM Tiers: Optimizing Cost and ...","url":"https://aclanthology.org/2025.findings-acl.873.pdf"},{"title":"The Pitfalls of Reasoning for Instruction-Following in LLMs","url":"https://openreview.net/pdf/057301f0efb5252bc107372a0fda3e9e277ad744.pdf"},{"title":"Controlling Bias Exposure for Fair Interpretable Predictions","url":"https://aclanthology.org/2022.findings-emnlp.431.pdf"},{"title":"Recursive Decomposition of Logical Thoughts: Framework for","url":"https://www.jair.org/index.php/jair/article/download/18562/27208"},{"title":"Why is constrained neural language generation particularly ...","url":"https://openreview.net/pdf?id=Vwgjk5ysWn"},{"title":"ConDABench: Interactive Evaluation of Language Models for Data Analysis","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/ADA__Benchmark___Evaluation.pdf"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"},{"title":"Published as a conference paper at ICLR 2025 LLM UNLEARNING VIA LOSS ADJUSTMENT","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf"}]

I found relevant research on your topic. Here are the key findings from the search results:

## Performance Degradation Trade-offs in NLP

There exists a trade-off between structural compliance and task accuracy, as demonstrated when models generate incorrect answers when forced to comply with a structured JSON format, despite producing correct answers in unconstr
…[truncated 1485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T04:24:15.211026+00:00_

Web search results for query: ""evidence generation" "relation extraction" performance cost trade-off"

Links: [{"title":"Evaluating Generative Language Models in Information Extraction as Subjective Question Correction","url":"https://arxiv.org/html/2404.03532v1"},{"title":"Self-Aligned Evidence Extraction for Retrieval-Augmented ...","url":"https://aclanthology.org/2024.emnlp-main.178.pdf"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3674501"},{"title":"Advanced technology-driven few-shot relation extraction: Challenges, opportunities, and future outlook - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197626009875"},{"title":"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://arxiv.org/html/2404.03098v1"},{"title":"Few-Shot Relation Extraction Based on Prompt Learning: A Taxonomy, Survey, Challenges and Future Directions | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3746281"},{"title":"Best Vision-enabled LLMs for Data Extraction: Cost-Performance Benchmark | by Vasyl Rakivnenko | Legal Design and Innovation | Medium","url":"https://medium.com/legal-design-and-innovation/best-vision-enabled-llms-for-data-extraction-cost-performance-benchmark-b62fe7bc5430"},{"title":"Graph Retrieval-Augmented Generation","url":"https://www.emergentmind.com/topics/graph-retrieval-augmented-generation-rag"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Comparison of pipeline, sequence-to-sequence, and GPT models for end-to-end relation extraction: experiments with the rare disease use-case","url":"https://arxiv.org/html/2311.13729"}]

I've performed a web search for "evidence
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T04:24:15.211217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T04:24:15.211423+00:00_

File content (46117 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T04:24:15.211555+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"cost of faithfulness\" information extraction explanation generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"cost of faithfulness\" information extraction explanation generation"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T04:24:15.211677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"explanation generation\" \"performance degradation\" NLP classification extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"explanation generation\" \"performance degradation\" NLP classification extraction"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T04:24:15.211794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"faithful information extraction\" cost overhead evidence rationale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"faithful information extraction\" cost overhead evidence rationale"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T04:24:15.211933+00:00_

Web search results for query: ""cost of faithfulness" information extraction explanation generation"

Links: [{"title":"Robust Explanation for Free or At the Cost of Faithfulness","url":"https://proceedings.mlr.press/v202/tan23a/tan23a.pdf"},{"title":"FaithLens: Faithfulness in AI Analysis","url":"https://www.emergentmind.com/topics/faithlens"},{"title":"Towards Faithful Model Explanation in NLP: A Survey | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/50/2/657/119158/Towards-Faithful-Model-Explanation-in-NLP-A-Survey"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham","url":"https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf"},{"title":"Towards Faithful Model Explanation in NLP: A Survey","url":"https://arxiv.org/html/2209.11326v4"},{"title":"FRIC: a framework for feature importance explanations and evaluation in span-level NLP | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-025-11628-1"},{"title":"Towards Faithful Model Explanation in NLP: A Survey | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2335"},{"title":"Towards Faithful Model Explanation in NLP: A Survey Qing Lyu","url":"https://veronica320.github.io/WPE2/survey.pdf"},{"title":"[2304.11633] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633"},{"title":"Towards Transparent Reasoning: What Drives Faithfulness in Large Language Models?","url":"https://arxiv.org/html/2510.24236v2"}]

Based on the web search results, here's what I found about the "cost of faithfulness" in relation to information extraction and explanation generation:

## Key Findings

**Robustness-Faithfulness Trade-off:**
Research shows there exists a robustness
…[truncated 1375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T04:24:15.212302+00:00_

Web search results for query: ""faithful information extraction" cost overhead evidence rationale"

Links: [{"title":"Exploring Faithful Rationale for Multi-Hop Fact Verification via Salience-Aware","url":"https://ojs.aaai.org/index.php/AAAI/article/download/26591/26363"},{"title":"Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2507.15586"},{"title":"[1603.07954] Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning","url":"https://arxiv.org/abs/1603.07954"},{"title":"[2304.11633] Evaluating ChatGPT’s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://ar5iv.labs.arxiv.org/html/2304.11633"},{"title":"[PDF] Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Information-Extraction-by-Acquiring-with-Narasimhan-Yala/ac50801574f7c97f1cf8f6718a9ff2b3e18c2dc6"},{"title":"Improving Information Extraction by Acquiring External Evidence with","url":"https://arxiv.org/pdf/1603.07954"},{"title":"Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning by Adam Yala | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Information-Extraction-by-Acquiring-with-Yala/ed36db843648474d087582c12e4652f83fd7cf8d"},{"title":"Millions of dollars are up for grabs because courts can't figure out if eDiscovery costs are recoverable","url":"https://www.logikcull.com/blog/millions-dollars-hang-courts-cant-figure-e-discovery-costs-recoverable"},{"title":"(PDF) Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning","url":"https://www.researchgate.net/publication/311990525_Improving_Information_Extraction_by_Acquiring_External_Evidence_with_Reinforcement_Learning"},{"title":"6. Data Coding and Da
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T04:24:15.212498+00:00_

Web search results for query: ""explanation generation" "performance degradation" NLP classification extraction"

Links: [{"title":"Degradation of Multi-Task Prompting Across Six NLP Tasks and LLM Families","url":"https://www.mdpi.com/2079-9292/14/21/4349"},{"title":"NLP Model Evaluation - Metrics, Benchmarks, and Beyond | Deconvolute Labs","url":"https://deconvoluteai.com/blog/evaluating-nlp-models"},{"title":"Towards Explainable NLP: A Generative Explanation Framework for Text Classification | Request PDF","url":"https://www.researchgate.net/publication/335783945_Towards_Explainable_NLP_A_Generative_Explanation_Framework_for_Text_Classification"},{"title":"Everything you need to know about model monitoring for natural language processing","url":"https://www.arthur.ai/blog/nlp-model-monitoring-with-arthur"},{"title":"Degradation stage classification via interpretable feature learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S027861252100100X"},{"title":"Text Classification Algorithms: Key Concepts and Applications in NLP","url":"https://innerview.co/blog/text-classification-algorithms-unlocking-the-power-of-nlp"},{"title":"A Generative Explanation Framework for Text Classification","url":"https://aclanthology.org/P19-1560.pdf"},{"title":"NLP Model Metrics. Evaluating the performance of Natural… | by Sujatha Mudadla | Medium","url":"https://medium.com/@sujathamudadla1213/nlp-model-metrics-b3fa32373269"},{"title":"More than Metrics: A Complete Guide to NLP Testing | deepset Blog","url":"https://www.deepset.ai/blog/more-than-metrics-how-to-test-an-nlp-system"},{"title":"What Is NLP (Natural Language Processing)? | IBM","url":"https://www.ibm.com/think/topics/natural-language-processing"}]

Based on the search results, here are the key findings regarding explanation generation, performance degradation, and NLP classification/extraction:

## Performance Degradation in Multi-Task NLP Systems

Performance degradation is not uniform acr
…[truncated 1623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T04:24:15.212741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "document-level relation extraction evidence sentence supporting evidence joint extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "document-level relation extraction evidence sentence supporting evidence joint extraction"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T04:24:15.212889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model performance\" \"explanation plausibility\" trade-off text classification human rationales"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model performance\" \"explanation plausibility\" trade-off text classification human rationales"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T04:24:15.213010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "rationale extraction \"hurts performance\" \"main task\" multitask learning NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "rationale extraction \"hurts performance\" \"main task\" multitask learning NLP"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T04:24:15.213125+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DocRE evidence supporting sentences ATLOP DREEAM document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DocRE evidence supporting sentences ATLOP DREEAM document relation extraction"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T04:24:15.213305+00:00_

Web search results for query: ""model performance" "explanation plausibility" trade-off text classification human rationales"

Links: [{"title":"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://arxiv.org/html/2404.03098v1"},{"title":"[2404.03098] Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://arxiv.org/abs/2404.03098"},{"title":"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.262/"},{"title":"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales | OpenReview","url":"https://openreview.net/forum?id=jIGRm4Yisp"},{"title":"(PDF) Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://www.researchgate.net/publication/379599633_Exploring_the_Trade-off_Between_Model_Performance_and_Explanation_Plausibility_of_Text_Classifiers_Using_Human_Rationales"},{"title":"[Literature Review] Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://www.themoonlight.io/en/review/exploring-the-trade-off-between-model-performance-and-explanation-plausibility-of-text-classifiers-using-human-rationales"},{"title":"Exploring the Trade-off Between Model Performance and ...","url":"https://visualdslab.com/papers/PlausibleNLPExplanations/"},{"title":"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales","url":"https://aclanthology.org/2024.findings-naacl.262.xml"},{"title":"Can human clinical rationales improve the performance and explainability of clinical text classification model
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T04:24:15.213524+00:00_

Web search results for query: "rationale extraction "hurts performance" "main task" multitask learning NLP"

Links: [{"title":"Rationalization for explainable NLP: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10560994/"},{"title":"Rationalization for Explainable NLP: A Survey","url":"https://arxiv.org/pdf/2301.08912"},{"title":"Frontiers | Rationalization for explainable NLP: a survey","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1225093/full"},{"title":"Rationale-Driven Multi-Task Learning","url":"https://www.emergentmind.com/topics/rationale-driven-multi-task-learning"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview","url":"https://arxiv.org/html/2109.09138v2"},{"title":"Multi-Task Learning in ML: Optimization & Use Cases [Overview]","url":"https://www.v7labs.com/blog/multi-task-learning-guide"},{"title":"Multi-task learning for natural language processing in the 2020s: Where are we going? - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0167865520302087"},{"title":"When Multi-Task Learning Works -- And When It Doesn't","url":"https://hazyresearch.stanford.edu/multi-task-learning"},{"title":"A Survey of Multi-task Learning in Natural Language ...","url":"https://aclanthology.org/2023.eacl-main.66.pdf"},{"title":"What is Multi-task Learning in NLP?","url":"https://www.activeloop.ai/resources/glossary/multi-task-learning-in-nlp/"}]

Based on the search results, I found relevant information about rationale extraction and its relationship to task performance in NLP:

## Key Finding

A desideratum for rationale extraction is that it should not hurt task performance. This represents a recognized challenge in the field—maintaining performance on the main task while also generating rationales for explainability.

## Context on Rationale Extraction

Rationalization can be divided into two major groups: abstractive and extractive, where extractive ra
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T04:24:15.213707+00:00_

Web search results for query: "document-level relation extraction evidence sentence supporting evidence joint extraction"

Links: [{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"},{"title":"A Comprehensive Survey of Document-level Relation Extraction (2016-2023)","url":"https://web3.arxiv.org/pdf/2309.16396v2"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283v1"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"(PDF) Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"}]

Based on the search results, here's what I found about document-level relation extraction with evidence sentence supporting evidence and joint extraction:

## Overview

Document-level re
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T04:24:15.213878+00:00_

Web search results for query: "DocRE evidence supporting sentences ATLOP DREEAM document relation extraction"

Links: [{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2302.08675"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"Semantic-guided attention and adaptive gating for document-level relation extraction | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-78051-9"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"(PDF) DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/368652592_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"ACME-RE: Adaptive Context Memory and Evidence-guided Relation","url":"https://openreview.net/pdf?id=wY1u4cLz3C"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v1"}]

Based on the search results, I found comprehensive information about the topics you're interested in:

## DocRE, Evidence, and Key Methods

Document-level relation extraction (DocR
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T04:24:15.214064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-explaining\" model \"performance cost\" \"task accuracy\" NLP joint training rationale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-explaining\" model \"performance cost\" \"task accuracy\" NLP joint training rationale"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T04:24:15.214192+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM \"relation extraction\" \"generate evidence\" \"supporting evidence\" seq2seq generative DocRE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM \"relation extraction\" \"generate evidence\" \"supporting evidence\" seq2seq generative DocRE"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T04:24:15.214337+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"pitfalls of reasoning\" \"chain of thought\" hurts performance instruction following LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"pitfalls of reasoning\" \"chain of thought\" hurts performance instruction following LLM"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T04:24:15.214456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Robust Explanation for Free or At the Cost of Faithfulness\" Tan ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Robust Explanation for Free or At the Cost of Faithfulness\" Tan ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T04:24:15.214598+00:00_

Web search results for query: ""self-explaining" model "performance cost" "task accuracy" NLP joint training rationale"

Links: [{"title":"Rationalization for explainable NLP: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10560994/"},{"title":"Understanding Multi-Task Learning in NLP Evaluation","url":"https://moldstud.com/articles/p-understanding-multi-task-learning-in-nlp-evaluation"},{"title":"Frontiers | From outputs to insights: a survey of rationalization approaches for explainable text classification","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1363531/full"},{"title":"Frontiers | Rationalization for explainable NLP: a survey","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1225093/full"},{"title":"Self-supervised and Supervised Joint Training for Resource ...","url":"http://proceedings.mlr.press/v139/cheng21b/cheng21b.pdf"},{"title":"LARGE LANGUAGE MODEL CASCADES WITH MIX","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf"},{"title":"Joint Pipeline Training: Achieving Parameter-Efficient Task-Aware Compression with Differential Learning Rates | by Micheal Bee | Medium","url":"https://medium.com/@mbonsign/learning-token-encodings-during-training-achieves-equivalent-performance-with-dramatic-memory-50af27790803"},{"title":"A JOINT MANY-TASK MODEL","url":"https://openreview.net/pdf?id=SJZAb5cel"},{"title":"NLP Model Evaluation - Metrics, Benchmarks, and Beyond | Deconvolute Labs","url":"https://deconvoluteai.com/blog/evaluating-nlp-models"},{"title":"Explainability for Large Language Models: A Survey | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/full/10.1145/3639372"}]

Based on the web search results, I found relevant information about self-explaining models, their performance costs, task accuracy, and joint training approaches in NLP. Her
…[truncated 1826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T04:24:15.214798+00:00_

Web search results for query: ""Robust Explanation for Free or At the Cost of Faithfulness" Tan ICML 2023"

Links: [{"title":"Robust Explanation for Free or At the Cost of Faithfulness","url":"https://proceedings.mlr.press/v202/tan23a/tan23a.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Zeren+Tan+and+Yang+Tian.+2023.+Robust+Explanation+for+Free+or+At+the+Cost+of+Faithfulness.+In+International+Conference+on+Machine+Learning%2C+ICML+2023%2C+23--29+July+2023%2C+Honolulu%2C+Hawaii%2C+USA+%28Proceedings+of+Machine+Learning+Research%2C+Vol.+202%29%2C+Andreas+Krause%2C+Emma+Brunskill%2C+Kyunghyun+Cho%2C+Barbara+Engelhardt%2C+Sivan+Sabato%2C+and+Jonathan+Scarlett+%28Eds.%29.+PMLR%2C+33534--33562.+https%3A%2F%2Fproceedings.mlr.press%2Fv202%2Ftan23a.html"},{"title":"[Quick Review] Improving Interpretation Faithfulness for Vision Transformers","url":"https://liner.com/review/improving-interpretation-faithfulness-for-vision-transformers"},{"title":"ICML 2023 Papers","url":"https://icml.cc/virtual/2023/papers.html"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"Counterfactual Explanations in ICML 2023 | by Kyosuke Morita | Medium","url":"https://medium.com/@kyosuke1029/counterfactual-explanations-in-icml-2023-134588863304"},{"title":"Downloads 2022","url":"https://icml.cc/Downloads/2022"},{"title":"ICML 2023 Orals","url":"https://icml.cc/virtual/2023/events/oral"},{"title":"Downloads 2023","url":"https://icml.cc/Downloads/2023"},{"title":"ICML 2023 Schedule","url":"https://icml.cc/virtual/2023/calendar"}]

I found the paper! Here's information about "Robust Explanation for Free or At the Cost of Faithfulness" by Tan et al., ICML 2023:

## Overview

This paper investigates explanation methods for machine learning models' trustworthiness, addresses their vulnerability to adversarial perturbations, and examines when robust explanations are necessary and what they cost.

## Key Findings

The paper proves that the robustness
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T04:24:15.215067+00:00_

Web search results for query: "LLM "relation extraction" "generate evidence" "supporting evidence" seq2seq generative DocRE"

Links: [{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143v1"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"[Literature Review] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.themoonlight.io/en/review/llm-with-relation-classifier-for-document-level-relation-extraction"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3674501"}]

Based on the search results, here are some key findings related to your query about LLMs for relation extraction with evidence generation and seq2seq approaches in DocRE:

## Key Research Areas

A no
…[truncated 1400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T04:24:15.215372+00:00_

Web search results for query: ""pitfalls of reasoning" "chain of thought" hurts performance instruction following LLM"

Links: [{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse","url":"https://arxiv.org/html/2410.21333v1"},{"title":"When Chain-of-Thought Hurts Performance | by Zaina Haider | Jan, 2026 | Medium","url":"https://medium.com/@thekzgroupllc/when-chain-of-thought-hurts-performance-52e30b5d456e"},{"title":"How to teach chain of thought reasoning to your LLM","url":"https://invisibletech.ai/blog/how-to-teach-chain-of-thought-reasoning-to-your-llm"},{"title":"Towards a Typology of Strange LLM Chains-of-Thought","url":"https://www.lesswrong.com/posts/qgvSMwRrdqoDMJJnD/towards-a-typology-of-strange-llm-chains-of-thought"},{"title":"Technical Report: The Decreasing Value of Chain of Thought in Prompting - Wharton Generative AI Labs","url":"https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse | OpenReview","url":"https://openreview.net/forum?id=J3gzdbYZxS"},{"title":"Chain-of-thought can hurt performance on tasks where thinking makes humans worse | Hacker News","url":"https://news.ycombinator.com/item?id=41999340"},{"title":"Prompt Engineering: Chain of Thought & LLM Performance | by Ria Kulshrestha | Medium | Data Science Collective","url":"https://medium.com/data-science-collective/so-you-think-you-can-prompt-b3384664bafc"},{"title":"Why Chain of Thought Fails in Clinical Text Understanding","url":"https://arxiv.org/html/2509.21933v1"},{"title":"When More is Less: Understanding Chain-of-Thought Length in LLMs","url":"https://arxiv.org/html/2502.07266v1"}]

Based on the search results, here's what recent research shows about the pitfalls of chain-of-thought reasoning and how it can hurt LLM performance:

## Key Findings on CoT Performance Degrad
…[truncated 1899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T04:24:15.215657+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mind Your Step\" chain-of-thought reduce performance \"thinking makes humans worse\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mind Your Step\" chain-of-thought reduce performance \"thinking makes humans worse\" 2024"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T04:24:15.215843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DREEAM evidence prediction \"relation F1\" improvement DocRED evidence supervision attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DREEAM evidence prediction \"relation F1\" improvement DocRED evidence supervision attention"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T04:24:15.216020+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"joint evidence\" \"relation extraction\" performance drop F1 decrease trade-off multitask"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"joint evidence\" \"relation extraction\" performance drop F1 decrease trade-off multitask"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T04:24:15.216193+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generative information extraction SFT \"evidence\" \"faithfulness\" LLM fine-tuning performance penalty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generative information extraction SFT \"evidence\" \"faithfulness\" LLM fine-tuning performance penalty"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T04:24:15.216446+00:00_

Web search results for query: ""Mind Your Step" chain-of-thought reduce performance "thinking makes humans worse" 2024"

Links: [{"title":"[2410.21333] Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse","url":"https://arxiv.org/abs/2410.21333"},{"title":"ICML Poster Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse","url":"https://icml.cc/virtual/2025/poster/45714"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse | OpenReview","url":"https://openreview.net/forum?id=rpbzBXdo4x"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse","url":"https://arxiv.org/html/2410.21333v1"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.21333v2"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mind-your-step-by-step-chain-thought"},{"title":"Mind your step (by step): Chain-of-thought can reduce performance on tasks where thinking makes humans worse. | Concepts & Cognition Lab","url":"https://cognition.princeton.edu/publications/mind-your-step-step-chain-thought-can-reduce-performance-tasks-where-thinking-makes"},{"title":"GitHub - JiayiGeng/CoT_overthinking: Code repo for paper: Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse","url":"https://github.com/JiayiGeng/CoT_overthinking"},{"title":"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse - Princeton University","url":"https://collaborate.princeton.edu/en/publications/mind-your-step-by-step-ch
…[truncated 1742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T04:24:15.216732+00:00_

Web search results for query: "DREEAM evidence prediction "relation F1" improvement DocRED evidence supervision attention"

Links: [{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.eacl-main.145/"},{"title":"GitHub - YoumiMa/dreeam: source code for {D}ocument-level {R}elation {E}xtraction with {E}vidence-guided {A}ttention {M}echanism · GitHub","url":"https://github.com/YoumiMa/dreeam"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2302.08675"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction | Computer Speech and Language","url":"https://dl.acm.org/doi/10.1016/j.csl.2024.101728"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://paperreading.club/page?id=152339"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"(PDF) DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/368652592_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"[PDF] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/51237757750c4618bf114ff329dacb9c997b771a"
…[truncated 1712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T04:24:15.217021+00:00_

Web search results for query: ""joint evidence" "relation extraction" performance drop F1 decrease trade-off multitask"

Links: [{"title":"Multi-task learning for few-shot biomedical relation extraction | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-023-10484-6"},{"title":"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/1/117/113094/It-Takes-Two-Flints-to-Make-a-Fire-Multitask"},{"title":"Multi-task Learning for Joint Entity and Relation Extraction on Open-domain | Proceedings of the 2024 6th Asia Conference on Machine Learning and Computing","url":"https://dl.acm.org/doi/10.1145/3690771.3690790"},{"title":"90% F1 Score in Relational Triple Extraction: Is it Real ?","url":"https://aclanthology.org/2023.genbench-1.1.pdf"},{"title":"Harnessing multi-task learning to improve overlapping relation extraction | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07533-y"},{"title":"Frontiers | A Relational Adaptive Neural Model for Joint Entity and Relation Extraction","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2021.635492/full"},{"title":"1 A Comprehensive Survey on Relation Extraction: Recent","url":"https://arxiv.org/pdf/2306.02051"},{"title":"Improving relation extraction by multi-task learning","url":"https://www.researchgate.net/publication/343864565_Improving_relation_extraction_by_multi-task_learning"},{"title":"Joint entity and relation extraction combined with multi-module feature information enhancement | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-024-01518-9"},{"title":"90% F1 Score in Relational Triple Extraction: Is it Real ?","url":"https://arxiv.org/pdf/2302.09887"}]

Based on the search r
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T04:24:15.217312+00:00_

Web search results for query: "generative information extraction SFT "evidence" "faithfulness" LLM fine-tuning performance penalty"

Links: [{"title":"Supervised Fine-Tuning (SFT) for LLMs - GeeksforGeeks","url":"https://www.geeksforgeeks.org/artificial-intelligence/supervised-fine-tuning-sft-for-llms/"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"AI Large Language Models and Supervised Fine Tuning - Black Hills Information Security, Inc.","url":"https://www.blackhillsinfosec.com/ai-large-language-models-and-supervised-fine-tuning/"},{"title":"Understanding and Using Supervised Fine-Tuning (SFT) for Language Models","url":"https://cameronrwolfe.substack.com/p/understanding-and-using-supervised"},{"title":"Supervised Fine-Tuning Dataset for AI & LLM Models | Shaip","url":"https://www.shaip.com/generative-ai/fine-tuning-solutions/"},{"title":"Supervised Fine-Tuning · Hugging Face","url":"https://huggingface.co/learn/llm-course/chapter11/3"},{"title":"The Comprehensive Guide to Fine-tuning LLM | by Sunil Rao | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/comprehensive-guide-to-fine-tuning-llm-4a8fd4d0e0af"},{"title":"Master Gemini SFT. Diagnose & fix fine-tuning challenges | Google Cloud Blog","url":"https://cloud.google.com/blog/products/ai-machine-learning/master-gemini-sft"},{"title":"Supervised fine-tuning (SFT) — Klu","url":"https://klu.ai/glossary/supervised-fine-tuning"}]

I've performed a web search for your query about generative information extraction, SFT, evidence, faithfulness, and LLM fine-tuning performance penalties.

The search results reveal relevant findings on related topics, particularly from recent research on SFT and fine-tuning trade-offs:

**
…[truncated 1327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T04:24:15.217606+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"It Takes Two Flints to Make a Fire\" multitask relation explanation classifiers Computational Linguistics 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"It Takes Two Flints to Make a Fire\" multitask relation explanation classifiers Computational Linguistics 2023"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T04:24:15.217795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "E2GRE \"Entity and Evidence Guided\" DocRED relation extraction evidence F1 joint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "E2GRE \"Entity and Evidence Guided\" DocRED relation extraction evidence F1 joint"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T04:24:15.217968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CDER \"Collaborative Evidence Retrieval\" document relation extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CDER \"Collaborative Evidence Retrieval\" document relation extraction 2025"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T04:24:15.218134+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking hurts\" \"reasoning tax\" LLM performance cost explanation generation overhead 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking hurts\" \"reasoning tax\" LLM performance cost explanation generation overhead 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T04:24:15.218362+00:00_

Web search results for query: "E2GRE "Entity and Evidence Guided" DocRED relation extraction evidence F1 joint"

Links: [{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"(PDF) Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283v1"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail","url":"https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | DeepAI","url":"https://deepai.org/publication/entity-and-evidence-guided-relation-extraction-for-docred"},{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.catalyzex.com/paper/arxiv:2008.12283"},{"title":"Entity and Evidence Guided Document-Level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2021.repl4nlp-1.30/"}]

Based on the web search results, here's what I found about E2GRE:

## E2GRE: Entity and Evidence Guided Relation Extraction for DocRED

E2GRE (Entity and Evidence Guided Relation Extraction) is a joint training framework p
…[truncated 1293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T04:24:15.218623+00:00_

Web search results for query: ""It Takes Two Flints to Make a Fire" multitask relation explanation classifiers Computational Linguistics 2023"

Links: [{"title":"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/1/117/113094/It-Takes-Two-Flints-to-Make-a-Fire-Multitask"},{"title":"[2204.11424] It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers","url":"https://arxiv.org/abs/2204.11424"},{"title":"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers - ACL Anthology","url":"https://aclanthology.org/2023.cl-1.3/"},{"title":"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10333739-takes-two-flints-make-fire-multitask-learning-neural-relation-explanation-classifiers"},{"title":"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers | DeepAI","url":"https://deepai.org/publication/it-takes-two-flints-to-make-a-fire-multitask-learning-of-neural-relation-and-explanation-classifiers"},{"title":"Computational Linguistics, Volume 49, Issue 1 - March 2023 - ACL Anthology","url":"https://aclanthology.org/volumes/2023.cl-1/"},{"title":"releases/cl2022-twoflints at master · clulab/releases","url":"https://github.com/clulab/releases/tree/master/cl2022-twoflints"},{"title":"[PDF] On the Importance of Delexicalization for Fact Verification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Importance-of-Delexicalization-for-Fact-Suntwal-Mithun/9609183790546396d6c549b65bdb62a76fcafc03"},{"title":"CiteSeerX","url":"https://citeseerx.ist.psu.edu/search_result?query=It+Takes+Two+Flints+to+Make+a+Fire:+Multitask+Learning+of+Neural+Relation+and+Explanation+Classifiers."},{
…[truncated 1683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T04:24:15.218877+00:00_

Web search results for query: "CDER "Collaborative Evidence Retrieval" document relation extraction 2025"

Links: [{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"},{"title":"CDER: Collaborative Evidence Retrieval for Document- ...","url":"https://www.researchgate.net/publication/382280635_CDER_Collaborative_Evidence_Retrieval_for_Document-Level_Relation_Extraction"},{"title":"khaitran22 (Khai Tran) · GitHub","url":"https://github.com/khaitran22"},{"title":"publications | Khai Tran - GitHub Pages","url":"https://khaitran22.github.io/publications/"},{"title":"CDER: Collaborative evidence retrieval for document-level ...","url":"https://espace.library.uq.edu.au/view/UQ:f699039"},{"title":"Document-Level Relation Extraction with Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/363410025_Document-Level_Relation_Extraction_with_Reconstruction"}]

Based on the search results, here's what I found about CDER:

## Overview

Document-level Relation Extraction (DocRE) involves identifying relations between entities across multiple sentences in a document, with ev
…[truncated 1377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T04:24:15.219149+00:00_

Web search results for query: ""thinking hurts" "reasoning tax" LLM performance cost explanation generation overhead 2024 2025"

Links: [{"title":"Scaling for Reasoning: How Thinking Tokens Are Rewriting LLM Performance Rules","url":"https://leapnonprofit.org/scaling-for-reasoning-how-thinking-tokens-are-rewriting-llm-performance-rules"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"},{"title":"The 2025 LLM Revolution: How Reasoning Models, Falling Costs, and New Architectures Are Changing AI | Efficient Coder","url":"https://www.xugj520.cn/en/archives/2025-llm-revolution-reasoning-models.html"},{"title":"Increasing the Thinking Budget is Not All You Need","url":"https://arxiv.org/html/2512.19585v1"},{"title":"the-illusion-of-thinking.pdf","url":"https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf"},{"title":"LLMs Can Reason Faster Only If We Let Them - People","url":"https://people.cs.vt.edu/~naren/papers/LLMs_Faster_ICML25.pdf"},{"title":"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/html/2605.00136v1"},{"title":"State of Reasoning LLMs: The New Era of “Thinking” Machines | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/state-of-reasoning-llms-the-new-era-of-thinking-machines-f241b1a3096d"},{"title":"Can LLMs Identify Tax Abuse?","url":"https://arxiv.org/html/2508.20097v1"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

Based on the search results, here's what I found about "thinking hurts" and the reasoning tax in LLM performance:

## The Core Problem: "Thinking Hurts" on Simple Tasks

On simple tasks, thinking hurts—for example, factual recall accuracy drops by 2.4-3.8% because the model wastes tokens overthinking questions like 'What's the capital of France?' Translation and classification tasks see no benefit, 
…[truncated 1402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T04:24:15.219451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"rationalization\" \"explainable NLP\" survey \"should not hurt task performance\" extractive rationale 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"rationalization\" \"explainable NLP\" survey \"should not hurt task performance\" extractive rationale 2023"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T04:24:15.219671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoRE LLM document relation extraction generative \"end-to-end\" evidence 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoRE LLM document relation extraction generative \"end-to-end\" evidence 2024"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T04:24:15.219855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Chain of Thought with Explicit Evidence Reasoning\" few-shot relation extraction CoTER 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Chain of Thought with Explicit Evidence Reasoning\" few-shot relation extraction CoTER 2023"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T04:24:15.220077+00:00_

Web search results for query: "AutoRE LLM document relation extraction generative "end-to-end" evidence 2024"

Links: [{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-demos.20/"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"(PDF) AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://www.researchgate.net/publication/384197797_AutoRE_Document-Level_Relation_Extraction_with_Large_Language_Models"},{"title":"[PDF] Large language models for generative information extraction: a survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-language-models-for-generative-information-a-Xu-Chen/351a2d50b4aff8e9754dc7074dd589b10a7465d4"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"AutoRE: Document-Level Relation Extraction with Large ...","url":"https://aclanthology.org/2024.acl-demos.20.pdf"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"}]

Based on the search results, here's what I found about AutoRE:

## AutoRE: Document-Level Relation Extraction with Large Language Models

AutoRE is an end-to-end DocRE model that adopts a novel RE extraction paradigm named R
…[truncated 1520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T04:24:15.220414+00:00_

Web search results for query: ""Chain of Thought with Explicit Evidence Reasoning" few-shot relation extraction CoTER 2023"

Links: [{"title":"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.153/"},{"title":"[2311.05922] Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction","url":"https://arxiv.org/abs/2311.05922"},{"title":"Chain of Thought with Explicit Evidence Reasoning for Few ...","url":"https://aclanthology.org/2023.findings-emnlp.153.pdf"},{"title":"[2311.05922v2] Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction","url":"https://arxiv.org/abs/2311.05922v2"},{"title":"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=sthusQGkef"},{"title":"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction","url":"https://arxiv.org/html/2311.05922v3"},{"title":"Papers with Code - Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction","url":"https://paperswithcode.com/paper/chain-of-thought-with-explicit-evidence"},{"title":"arXiv Computation and Language Research Summaries for November 10, 2023","url":"https://www.linkedin.com/pulse/ep-47-november-10-2023-brad-edwards-xdstc?trk=article-ssr-frontend-pulse_more-articles_related-content-card"},{"title":"arXiv:2311.03734v1 [cs.CL] 7 Nov 2023","url":"https://arxiv.org/pdf/2311.03734"},{"title":"Chain of Thought with Explicit Evidence Reasoning for Few ...","url":"https://openreview.net/pdf?id=sthusQGkef"}]

Based on the search results, I found comprehensive information about the research paper you're looking for:

## Chain of Thought with Explicit Evidence Reasoning (CoT-ER) for Few-shot Relation Extraction

CoT-ER is a novel approach for few-shot relation extraction using large language models, standing for "chain-of-thou
…[truncated 1274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T04:24:15.220784+00:00_

Web search results for query: ""rationalization" "explainable NLP" survey "should not hurt task performance" extractive rationale 2023"

Links: [{"title":"Frontiers | Rationalization for explainable NLP: a survey","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1225093/full"},{"title":"Rationalization for explainable NLP: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10560994/"},{"title":"Rationalization for Explainable NLP: A Survey","url":"https://arxiv.org/pdf/2301.08912"},{"title":"Rationalization for explainable NLP: a survey - Illinois Experts","url":"https://experts.illinois.edu/en/publications/rationalization-for-explainable-nlp-a-survey"},{"title":"Rationalization for explainable NLP: a survey - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37818431/"},{"title":"[PDF] Rationalization for explainable NLP: a survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Rationalization-for-explainable-NLP:-a-survey-Gurrapu-Kulkarni/1cdfa7c3465943a295f8df2d2097c4bb3e222426"},{"title":"(PDF) Rationalization for explainable NLP: a survey","url":"https://www.researchgate.net/publication/375400968_Rationalization_for_explainable_NLP_a_survey"},{"title":"[2301.08912] Rationalization for Explainable NLP: A Survey","url":"https://arxiv.org/abs/2301.08912"},{"title":"Frontiers | From outputs to insights: a survey of rationalization approaches for explainable text classification","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1363531/full"},{"title":"From outputs to insights: a survey of rationalization approaches for explainable text classification - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11300430/"}]

I found a comprehensive 2023 survey on rationalization for explainable NLP. Here are the key findings from the search results:

## Overview

Rationalization is an emerging explainable technique for NLP applications that provides explan
…[truncated 1337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T04:24:15.221036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Revisiting Relation Extraction\" \"era of Large Language Models\" Wadhwa 2023 ACL GPT evidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Revisiting Relation Extraction\" \"era of Large Language Models\" Wadhwa 2023 ACL GPT evidence"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-16T04:24:15.221173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"explain then predict\" vs \"predict then explain\" NLP performance accuracy comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"explain then predict\" vs \"predict then explain\" NLP performance accuracy comparison"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T04:24:15.221353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GLiDRE\" generalist lightweight document relation extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GLiDRE\" generalist lightweight document relation extraction 2025"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T04:24:15.221518+00:00_

Web search results for query: ""Revisiting Relation Extraction" "era of Large Language Models" Wadhwa 2023 ACL GPT evidence"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"[2305.05003] Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/abs/2305.05003"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"dblp: Somin Wadhwa","url":"https://dblp.org/pid/265/5925.html"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"},{"title":"[Quick Review] Revisiting Relation Extraction in the era of Large Language Models","url":"https://liner.com/review/revisiting-relation-extraction-in-era-large-language-models"}]

I found the paper you were looking for! Here are the key details about the paper:

## Publication Information

The paper "Revisiting Relation Extraction in the era of Large Language Models" was authored by Somin Wadhwa, Silvio 
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-16T04:24:15.221809+00:00_

Web search results for query: ""GLiDRE" generalist lightweight document relation extraction 2025"

Links: [{"title":"[2508.00757] GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/abs/2508.00757"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757v2"},{"title":"GitHub - robinarmingaud/glidre: Zero and Few-shot document level relation extraction / ⚠️ Development moved to: https://github.com/cea-list-lasti/glidre","url":"https://github.com/robinarmingaud/glidre"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250800757A/abstract"},{"title":"(PDF) GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/394262622_GLiDRE_Generalist_Lightweight_model_for_Document-level_Relation_Extraction"},{"title":"GitHub - jackboyla/GLiREL: Generalist and Lightweight Model for Relation Extraction (Extract any relationship types from text) · GitHub","url":"https://github.com/jackboyla/GLiREL"},{"title":"Paper page - GLiClass: Generalist Lightweight Model for Sequence Classification Tasks","url":"https://huggingface.co/papers/2508.07662"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/392505146_GLiREL_-_Generalist_Model_for_Zero-Shot_Relation_Extraction"},{"title":"GLiDRE : Modèle généraliste pour l'extraction de relations à l'échelle de documents - Archive ouverte HAL","url":"https://hal.science/hal-04918406"},{"title":"GLiClass: Generalist Lightweight Model for Sequence Classification Tasks","url":"https://arxiv.org/html/2508.07662v1"}]

Based on the search results, here's what I found about GLiDRE:

## Overview

GLiDRE is a new compact model for document-level relation extraction, designed to work efficiently in
…[truncated 1311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T04:24:15.222105+00:00_

Web search results for query: ""explain then predict" vs "predict then explain" NLP performance accuracy comparison"

No links found.

The search returned no results. Let me try a different search query:

Links: [{"title":"Language Models Perform Reasoning via Chain of Thought","url":"https://research.google/blog/language-models-perform-reasoning-via-chain-of-thought/"},{"title":"[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models","url":"https://arxiv.org/abs/2201.11903"},{"title":"Applying large language models and chain-of-thought for automatic scoring - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666920X24000146"},{"title":"How to teach chain of thought reasoning to your LLM","url":"https://invisibletech.ai/blog/how-to-teach-chain-of-thought-reasoning-to-your-llm"},{"title":"Chain-of-Thought Prompting — Improve Accuracy by Getting LLMs to Reason | Width.ai","url":"https://www.width.ai/post/chain-of-thought-prompting"},{"title":"What is chain of thought (CoT) prompting? | IBM","url":"https://www.ibm.com/think/topics/chain-of-thoughts"},{"title":"What Makes a Good Reasoning Chain? Uncovering ...","url":"https://aclanthology.org/2025.emnlp-main.329.pdf"},{"title":"Chain of Thought Prompting for Intent Classification using ...","url":"https://nlp.cs.aueb.gr/theses/Capstone_Thesis_Report.pdf"},{"title":"Chain-of-thought prompting elicits reasoning in large language models | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3602070"},{"title":"Comprehensive Guide to Chain-of-Thought Prompting | Mercity Research","url":"https://www.mercity.ai/blog-post/guide-to-chain-of-thought-prompting/"}]

Let me try another search specifically focused on the comparison between explanation-first and prediction-first approaches:

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2601.04208"},{"title":"Task-Structured Curricu
…[truncated 5366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T04:24:15.222371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T04:24:15.222530+00:00_

File content (46117 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T04:24:15.222656+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
  "description": "Read first 100 lines of literature_map.yaml dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt",
    "description": "Read first 100 lines of literature_map.yaml dump"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T04:24:15.222872+00:00_

&lt;persisted-output>
Output too large (124.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/b5bjfl8vt.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\
…[truncated 294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T04:24:15.223052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt | python3 -c \"\nimport sys, json\ndata = json.load(sys.stdin)\ncontent = data['result']\n# Extract category lines\nfor line in content.split('\\\\n'):\n    if 'Category' in line and '===' in line:\n        print(line.strip())\n\"",
  "description": "Extract category headers from literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt | python3 -c \"\nimport sys, json\ndata = json.load(sys.stdin)\ncontent = data['result']\n# Extract category lines\nfor line in content.split('\\\\n'):\n    if 'Category' in line and '===' in line:\n        print(line.strip())\n\"",
    "description": "Extract category headers from literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T04:24:15.223294+00:00_

&lt;persisted-output>
Output too large (122KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/b5v3u17i2.txt

Preview (first 2KB):
{"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml", "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（div
…[truncated 292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T04:24:15.223530+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\nfor line in content.split('\\n'):\n    stripped = line.strip()\n    if stripped.startswith('# === Category'):\n        print(stripped)\n\"",
  "description": "Extract category headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\nfor line in content.split('\\n'):\n    stripped = line.strip()\n    if stripped.startswith('# === Category'):\n        print(stripped)\n\"",
    "description": "Extract category headers"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T04:24:15.223804+00:00_

# === Category 1: Reward Diversity / Reward Shaping for RL Stability ===
# === Category 2: Mode Collapse Prevention in GRPO/RLHF ===
# === Category 3: Contrastive Rewards in RL ===
# === Category 4: Evidence-Based Rewards in IE/NLP ===
# === Category 5: Multi-Objective RL for Text Generation ===
# === Category 6: RSFT Methodology & Theory ===
# === Category 7: RL for Information Extraction ===
# === Category 8: Recent LLM-based DocRE Methods ===
# === Category 9: Evidence Generation & Task Performance Trade-off ===
# === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===
# === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===
# === Category 12: Reranking / Verification as Bridge ===
# === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===
# === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===
# === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===
# === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===
# === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===
# === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===
# === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===
# === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===
# === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===
# === Category 22: Faithfulness Cost in NLP (Direction 2) ===
# === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===
# === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===
# === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===
# === Category 7: Evidence-based DocRE (Expanded) ===
# === Category 8: Faithfulness in Structured Output / Evidence Quality ===
# === Category 9: RLHF/GRPO for Structured Tasks (Expanded) ===
# === Category 10: QLoRA vs Full Fine-tuning (Expanded) ===
# === Category 11: Multi-task Learning Trade-offs in IE (Expanded) ===
# 
…[truncated 1293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T04:24:15.224003+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\nlines = content.split('\\n')\n# Find titles in categories 9, 11, 22, 35\nin_target = False\nfor line in lines:\n    stripped = line.strip()\n    if stripped.startswith('# === Category'):\n        # Check if it's a target category\n        for cat in ['Category 9:', 'Category 11:', 'Category 22:', 'Category 35:']:\n            if cat in stripped:\n                in_target = True\n                print(f'\\n{stripped}')\n                break\n        else:\n            in_target = False\n    elif in_target and stripped.startswith('- title:'):\n        print(f'  {stripped}')\n\"",
  "description": "List existing papers in target categories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\nlines = content.split('\\n')\n# Find titles in categories 9, 11, 22, 35\nin_target = False\nfor line in lines:\n    stripped = line.strip()\n    if stripped.startswith('# === Category'):\n        # Check if it's a target category\n        for cat in ['Category 9:', 'Category 11:', 'Category 22:', 'Category 35:']:\n            if cat in stripped:\n                in_target = True\n                print(f'\\n{stripped}')\n                break\n        else:\n            in_target = False\n    elif in_target and stripped.startswith('- title:'):\n        print(f'  {stripped}')\n\"",
    "description": "List existing papers in target categories"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T04:24:15.224154+00:00_

# === Category 9: Evidence Generation & Task Performance Trade-off ===
  - title: "Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse"
  - title: "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion"
  - title: "Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales"
  - title: "The Decreasing Value of Chain of Thought in Prompting"

# === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===
  - title: "Correctness is not Faithfulness in RAG Attributions"
  - title: "Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering"
  - title: "Towards Faithful Model Explanation in NLP: A Survey"

# === Category 22: Faithfulness Cost in NLP (Direction 2) ===
  - title: "Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks"
  - title: "Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models"
  - title: "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps"

# === Category 9: RLHF/GRPO for Structured Tasks (Expanded) ===
  - title: "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models"
  - title: "E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization"
  - title: "RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs"
  - title: "Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning"

# === Category 11: Multi-task Learning Trade-offs in IE (Expanded) ===
  - title: "C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction"
  - title: "Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via 
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T04:24:15.224346+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\n# Check for specific paper titles\npapers_to_check = [\n    'Two Flints', 'Robust Explanation for Free', 'Rationalization for Explainable',\n    'CoT-ER', 'Chain of Thought with Explicit Evidence', 'E2GRE', 'Entity and Evidence Guided',\n    'DREEAM', 'CDER', 'AutoRE', 'Revisiting Relation Extraction', 'GLiDRE',\n    'ChatGPT.*Information Extraction', 'Evaluating ChatGPT'\n]\nfor p in papers_to_check:\n    import re\n    if re.search(p, content, re.IGNORECASE):\n        print(f'FOUND: {p}')\n    else:\n        print(f'NOT FOUND: {p}')\n\"",
  "description": "Check which papers are already in literature_map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\n# Check for specific paper titles\npapers_to_check = [\n    'Two Flints', 'Robust Explanation for Free', 'Rationalization for Explainable',\n    'CoT-ER', 'Chain of Thought with Explicit Evidence', 'E2GRE', 'Entity and Evidence Guided',\n    'DREEAM', 'CDER', 'AutoRE', 'Revisiting Relation Extraction', 'GLiDRE',\n    'ChatGPT.*Information Extraction', 'Evaluating ChatGPT'\n]\nfor p in papers_to_check:\n    import re\n    if re.search(p, content, re.IGNORECASE):\n        print(f'FOUND: {p}')\n    else:\n        print(f'NOT FOUND: {p}')\n\"",
    "description": "Check which papers are already in literature_map"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T04:24:15.224489+00:00_

NOT FOUND: Two Flints
NOT FOUND: Robust Explanation for Free
NOT FOUND: Rationalization for Explainable
NOT FOUND: CoT-ER
NOT FOUND: Chain of Thought with Explicit Evidence
NOT FOUND: E2GRE
NOT FOUND: Entity and Evidence Guided
FOUND: DREEAM
FOUND: CDER
FOUND: AutoRE
NOT FOUND: Revisiting Relation Extraction
FOUND: GLiDRE
NOT FOUND: ChatGPT.*Information Extraction
NOT FOUND: Evaluating ChatGPT

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T04:24:15.224662+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T04:24:15.224834+00:00_

_project
ced_eval_commands.md
ced_stabilizer_literature_survey.md
cuda3_diagnostic.md
d024_literature_survey.md
diag_mvp2_grpo_flatnli_r3.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dream_reports
dreeam_evif1_alignment_report.md
edcr_analysis.md
edcr_analysis_r2b.md
edcr_diagnostic_table.md
eval_plan_014_no_evidence_r2_analysis.md
eval_progress_20260516.md
eval_progress_check_0515.md
eval_script_audit.md
eval_status_check.md
experiment_summary_table.md
freige
gap_analysis_w3.md
grpo_forgetting_dynamics.pdf
grpo_forgetting_dynamics.png
kl_analysis_report.md
literature_quantization_rl.md
literature_survey_evidence_overhead.md
manifest.yaml
metrics_summary.csv
metrics_summary_table.md
mvp2_eval_rsft_r2b_maxtok1536_r2
paired_ttest_analysis.py
paper
paper_evidence_table.md
paper_main_tables_draft.md
paper_metrics_table.md
plan_001_flat_nli_seed45
plan_003
plan_003_edcr_cross_method_table.md
plan_003_edcr_diagnostic
plan_003_edcr_diagnostic.md
plan_009
plan_009_dynamics_data.json
plan_009_dynamics_figure
plan_009_forgetting_data.csv
plan_009_forgetting_data_v5.csv
plan_009_forgetting_figure
plan_009_grpo_forgetting
plan_012_dpo_ced
plan_012_dpo_ced_1ep_analysis.md
process_check_report.md
reeval_commands.md
related_work_gap_analysis.md
related_work_survey
rsft_gen_progress_check.md
rsft_pipeline_commands.md
status_check_loop4.md
topk_ablation_lit_review.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-16T04:24:15.224987+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/evidence_cost_literature_scan.md",
  "content": "# Evidence Cost Literature Scan\n**Date**: 2026-05-16\n**Objective**: 搜索 \"evidence generation cost in information extraction\" 相关文献，评估 FREIGE 发现的新颖性。\n\n## FREIGE 的核心发现\n- No-evidence SFT: rel_f1 = 0.4876\n- Evidence SFT: rel_f1 = 0.4106\n- **Evidence tax**: -7.7 F1 points (generative SFT, DocRE, LLM fine-tuning)\n\n## 搜索结论\n\n### 新颖性评估: **高度新颖**\n\n**没有任何现有工作在以下组合条件下量化过 evidence 对主任务的性能代价：**\n1. Generative (seq2seq) evidence 生成（非 extractive attention supervision）\n2. Document-level relation extraction（非 sentence-level）\n3. LLM SFT fine-tuning（非 prompting）\n4. 明确量化 evidence 导致的 rel_f1 下降\n\n### 与现有工作的关键区别\n\n| 工作 | 设定 | Evidence 对 RE 的影响 | 与 FREIGE 的差异 |\n|------|------|---------------------|-----------------|\n| DREEAM (Ma+, EACL 2023) | Encoder-based, attention supervision | **帮助** RE (+2 F1) | 非生成式；evidence 是 attention 监督信号 |\n| E2GRE (Huang+, 2021) | Encoder-based, joint prediction | **帮助** RE | 非生成式；evidence 是 auxiliary classification head |\n| Two Flints (Tang & Surdeanu, CL 2023) | Extractive rationale + RE classification | **帮助** RE (+4% F1) | Sentence-level；extractive 非 generative |\n| Resck+ (NAACL 2024 Findings) | Text classification + rationale plausibility | **微弱影响** (negligible) | Classification 非 extraction；非 seq2seq |\n| Mind Your Step (Geng+, 2024/ICML 2025) | CoT prompting | **有害** (up to -36.3%) | Prompting 非 SFT；非 IE task |\n| CoT-ER (EMNLP 2023 Findings) | Few-shot prompting with evidence for RE | **帮助** RE | Prompting 非 SFT；sentence-level |\n| Rationalization Survey (Gurrapu+, 2023) | Survey | 列为 desiderata: \"should not hurt\" | 仅声明不应有害，未量化 |\n\n### 核心洞察\n\n**Encoder-based discriminative 模型**中，evidence 作为 attention supervision 或 auxiliary task 通常**帮助** RE（DREEAM、E2GRE、CDER、Two Flints）。这是因为 evidence 信号引导模型聚焦相关 context，属于 implicit knowledge injection。\n\n**Generative LLM SFT** 中，要求模型同时生成 evidence 和 relation 是一个**更困难的任务**——模型必须在有限的 output capacity 中分配 token budget 给两个子任务。FREIGE 的 -7.7 F1 量化了这个 \"faithfulness tax\"，这在文献中是首次。\n\n## 找到的新论文（需加入 literature_map.yaml）\n\n### 1. It Takes Two Flints to Make a Fire (Direct Competitor)\n- **Authors**: Zheng Tang, Mihai Surdeanu\n- **Year**: 2023\n- **Venue**: Computational Linguistics, Vol. 49, Issue 1\n- **URL**: https://aclanthology.org/2023.cl-1.3/\n- **Key Finding**: Joint training of RE classifier + explanation sequence labeler. Joint training HELPS RE (+~4% F1 on CoNLL04). Explanation classifier operates on extractive features.\n- **Role**: direct_competitor\n- **Critical Difference**: Sentence-level, extractive, discriminative model. 与 FREIGE 的 generative DocRE 设定相反——他们发现 joint 有益，我们发现 joint 有害。这个对比强化了我们的 contribution。\n\n### 2. Robust Explanation for Free or At the Cost of Faithfulness\n- **Authors**: Zeren Tan, Yang Tian\n- **Year**: 2023\n- **Venue**: ICML 2023\n- **URL**: https://proceedings.mlr.press/v202/tan23a.html\n- **Key Finding**: 首次理论证明 robustness-faithfulness trade-off 存在。Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness 需牺牲 faithfulness。\n- **Role**: theoretical_foundation\n- **Relevance**: 提供了 \"faithfulness 有代价\" 的理论框架，虽然研究对象是 post-hoc explanation 而非 generative evidence。\n\n### 3. Rationalization for Explainable NLP: A Survey\n- **Authors**: Sai Gurrapu et al.\n- **Year**: 2023\n- **Venue**: Frontiers in AI\n- **URL**: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full\n- **Key Finding**: 首个 NLP rationalization 综述。列出 desiderata: \"rationale extraction should not hurt task performance\"。将 rationalization 分为 extractive 和 abstractive 两类。\n- **Role**: background_survey\n- **Relevance**: 明确了 \"不应损害主任务\" 是学界共识/期望，但没有论文系统量化违反这一 desiderata 的程度。FREIGE 的发现直接挑战了这一假设。\n\n### 4. Chain of Thought with Explicit Evidence Reasoning for Few-shot RE (CoT-ER)\n- **Authors**: Xilai Yin et al.\n- **Year**: 2023\n- **Venue**: EMNLP 2023 Findings\n- **URL**: https://aclanthology.org/2023.findings-emnlp.153/\n- **Key Finding**: 用 LLM 先生成 evidence，再 CoT 推理做 few-shot RE。与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。\n- **Role**: related_method\n- **Relevance**: 在 prompting 设定下 evidence+CoT 有益。与 SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是 SFT 训练 specific 的问题。\n\n### 5. Entity and Evidence Guided Relation Extraction for DocRED (E2GRE)\n- **Authors**: Kevin Huang et al.\n- **Year**: 2021\n- **Venue**: RepL4NLP @ ACL 2021\n- **URL**: https://aclanthology.org/2021.repl4nlp-1.30/\n- **Key Finding**: Joint evidence prediction + relation extraction for DocRED。利用 pretrained LM attention 作为 evidence 特征，joint training 在 RE 和 evidence prediction 上均有增益。\n- **Role**: direct_competitor\n- **Relevance**: DocRE 上 joint evidence+RE 的先驱。但使用 encoder-based discriminative 模型，evidence 是 binary classification 而非 text generation。他们发现 joint 有益，与 FREIGE 相反。\n\n### 6. Revisiting Relation Extraction in the era of Large Language Models\n- **Authors**: Somin Wadhwa, Silvio Amir, Byron Wallace\n- **Year**: 2023\n- **Venue**: ACL 2023\n- **URL**: https://aclanthology.org/2023.acl-long.868/\n- **Key Finding**: GPT-3 few-shot 在 RE 上接近 SOTA。Seq2seq 大模型在 RE 上有竞争力但评估需要 human evaluation（exact match 低估性能）。\n- **Role**: background\n- **Relevance**: 建立了 LLM-based generative RE 的 baseline context。\n\n## 总结\n\n| 结论 | 详情 |\n|------|------|\n| 直接竞品 | **无**——没有论文在 generative SFT + DocRE 设定下量化 evidence cost |\n| 间接对比 | Two Flints (sentence-level, extractive → 有益), E2GRE (encoder-based → 有益), CoT-ER (prompting → 有益) |\n| 理论支撑 | Tan & Tian ICML 2023 (faithfulness 有理论代价), Rationalization Survey (desiderata: 不应有害) |\n| 新颖性确认 | FREIGE 首次在 generative SFT DocRE 中量化 evidence tax (-7.7 F1) |\n| Framing 建议 | \"文献中 evidence 通常被认为有益（DREEAM, E2GRE, Two Flints）或至少无害（Rationalization Survey desiderata）。FREIGE 揭示了一个被忽视的现象：在 generative LLM SFT 中，faithfulness 有可量化的代价。\" |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/evidence_cost_literature_scan.md",
    "content": "# Evidence Cost Literature Scan\n**Date**: 2026-05-16\n**Objective**: 搜索 \"evidence generation cost in information extraction\" 相关文献，评估 FREIGE 发现的新颖性。\n\n## FREIGE 的核心发现\n- No-evidence SFT: rel_f1 = 0.4876\n- Evidence SFT: rel_f1 = 0.4106\n- **Evidence tax**: -7.7 F1 points (generative SFT, DocRE, LLM fine-tuning)\n\n## 搜索结论\n\n### 新颖性评估: **高度新颖**\n\n**没有任何现有工作在以下组合条件下量化过 evidence 对主任务的性能代价：**\n1. Generative (seq2seq) evidence 生成（非 extractive attention supervision）\n2. Document-level relation extraction（非 sentence-level）\n3. LLM SFT fine-tuning（非 prompting）\n4. 明确量化 evidence 导致的 rel_f1 下降\n\n### 与现有工作的关键区别\n\n| 工作 | 设定 | Evidence 对 RE 的影响 | 与 FREIGE 的差异 |\n|------|------|---------------------|-----------------|\n| DREEAM (Ma+, EACL 2023) | Encoder-based, attention supervision | **帮助** RE (+2 F1) | 非生成式；evidence 是 attention 监督信号 |\n| E2GRE (Huang+, 2021) | Encoder-based, joint prediction | **帮助** RE | 非生成式；evidence 是 auxiliary classification head |\n| Two Flints (Tang & Surdeanu, CL 2023) | Extractive rationale + RE classification | **帮助** RE (+4% F1) | Sentence-level；extractive 非 generative |\n| Resck+ (NAACL 2024 Findings) | Text classification + rationale plausibility | **微弱影响** (negligible) | Classification 非 extraction；非 seq2seq |\n| Mind Your Step (Geng+, 2024/ICML 2025) | CoT prompting | **有害** (up to -36.3%) | Prompting 非 SFT；非 IE task |\n| CoT-ER (EMNLP 2023 Findings) | Few-shot prompting with evidence for RE | **帮助** RE | Prompting 非 SFT；sentence-level |\n| Rationalization Survey (Gurrapu+, 2023) | Survey | 列为 desiderata: \"should not hurt\" | 仅声明不应有害，未量化 |\n\n### 核心洞察\n\n**Encoder-based discriminative 模型**中，evidence 作为 attention supervision 或 auxiliary task 通常**帮助** RE（DREEAM、E2GRE、CDER、Two Flints）。这是因为 evidence 信号引导模型聚焦相关 context，属于 implicit knowledge injection。\n\n**Generative LLM SFT** 中，要求模型同时生成 evidence 和 relation 是一个**更困难的任务**——模型必须在有限的 output capacity 中分配 token budget 给两个子任务。FREIGE 的 -7.7 F1 量化了这个 \"faithfulness tax\"，这在文献中是首次。\n\n## 找到的新论文（需加入 literature_map.yaml）\n\n### 1. It Takes Two Flints to Make a Fire (Direct Competitor)\n- **Authors**: Zheng Tang, Mihai Surdeanu\n- **Year**: 2023\n- **Venue**: Computational Linguistics, Vol. 49, Issue 1\n- **URL**: https://aclanthology.org/2023.cl-1.3/\n- **Key Finding**: Joint training of RE classifier + explanation sequence labeler. Joint training HELPS RE (+~4% F1 on CoNLL04). Explanation classifier operates on extractive features.\n- **Role**: direct_competitor\n- **Critical Difference**: Sentence-level, extractive, discriminative model. 与 FREIGE 的 generative DocRE 设定相反——他们发现 joint 有益，我们发现 joint 有害。这个对比强化了我们的 contribution。\n\n### 2. Robust Explanation for Free or At the Cost of Faithfulness\n- **Authors**: Zeren Tan, Yang Tian\n- **Year**: 2023\n- **Venue**: ICML 2023\n- **URL**: https://proceedings.mlr.press/v202/tan23a.html\n- **Key Finding**: 首次理论证明 robustness-faithfulness trade-off 存在。Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness 需牺牲 faithfulness。\n- **Role**: theoretical_foundation\n- **Relevance**: 提供了 \"faithfulness 有代价\" 的理论框架，虽然研究对象是 post-hoc explanation 而非 generative evidence。\n\n### 3. Rationalization for Explainable NLP: A Survey\n- **Authors**: Sai Gurrapu et al.\n- **Year**: 2023\n- **Venue**: Frontiers in AI\n- **URL**: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full\n- **Key Finding**: 首个 NLP rationalization 综述。列出 desiderata: \"rationale extraction should not hurt task performance\"。将 rationalization 分为 extractive 和 abstractive 两类。\n- **Role**: background_survey\n- **Relevance**: 明确了 \"不应损害主任务\" 是学界共识/期望，但没有论文系统量化违反这一 desiderata 的程度。FREIGE 的发现直接挑战了这一假设。\n\n### 4. Chain of Thought with Explicit Evidence Reasoning for Few-shot RE (CoT-ER)\n- **Authors**: Xilai Yin et al.\n- **Year**: 2023\n- **Venue**: EMNLP 2023 Findings\n- **URL**: https://aclanthology.org/2023.findings-emnlp.153/\n- **Key Finding**: 用 LLM 先生成 evidence，再 CoT 推理做 few-shot RE。与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。\n- **Role**: related_method\n- **Relevance**: 在 prompting 设定下 evidence+CoT 有益。与 SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是 SFT 训练 specific 的问题。\n\n### 5. Entity and Evidence Guided Relation Extraction for DocRED (E2GRE)\n- **Authors**: Kevin Huang et al.\n- **Year**: 2021\n- **Venue**: RepL4NLP @ ACL 2021\n- **URL**: https://aclanthology.org/2021.repl4nlp-1.30/\n- **Key Finding**: Joint evidence prediction + relation extraction for DocRED。利用 pretrained LM attention 作为 evidence 特征，joint training 在 RE 和 evidence prediction 上均有增益。\n- **Role**: direct_competitor\n- **Relevance**: DocRE 上 joint evidence+RE 的先驱。但使用 encoder-based discriminative 模型，evidence 是 binary classification 而非 text generation。他们发现 joint 有益，与 FREIGE 相反。\n\n### 6. Revisiting Relation Extraction in the era of Large Language Models\n- **Authors**: Somin Wadhwa, Silvio Amir, Byron Wallace\n- **Year**: 2023\n- **Venue**: ACL 2023\n- **URL**: https://aclanthology.org/2023.acl-long.868/\n- **Key Finding**: GPT-3 few-shot 在 RE 上接近 SOTA。Seq2seq 大模型在 RE 上有竞争力但评估需要 human evaluation（exact match 低估性能）。\n- **Role**: background\n- **Relevance**: 建立了 LLM-based generative RE 的 baseline context。\n\n## 总结\n\n| 结论 | 详情 |\n|------|------|\n| 直接竞品 | **无**——没有论文在 generative SFT + DocRE 设定下量化 evidence cost |\n| 间接对比 | Two Flints (sentence-level, extractive → 有益), E2GRE (encoder-based → 有益), CoT-ER (prompting → 有益) |\n| 理论支撑 | Tan & Tian ICML 2023 (faithfulness 有理论代价), Rationalization Survey (desiderata: 不应有害) |\n| 新颖性确认 | FREIGE 首次在 generative SFT DocRE 中量化 evidence tax (-7.7 F1) |\n| Framing 建议 | \"文献中 evidence 通常被认为有益（DREEAM, E2GRE, Two Flints）或至少无害（Rationalization Survey desiderata）。FREIGE 揭示了一个被忽视的现象：在 generative LLM SFT 中，faithfulness 有可量化的代价。\" |\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-16T04:24:15.225197+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/evidence_cost_literature_scan.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-16T04:24:15.225373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\n# Get last 30 lines\nlines = content.split('\\n')\nfor i, line in enumerate(lines[-30:], len(lines)-30):\n    print(f'{i}: {line}')\n\"",
  "description": "View last 30 lines of literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2680448a-1368-49f1-9df3-fb8974b6cca5/tool-results/mcp-agent-ml-research-read_project_file-1778905135738.txt') as f:\n    data = json.load(f)\ncontent = json.loads(data['result'])['data']['content']\n# Get last 30 lines\nlines = content.split('\\n')\nfor i, line in enumerate(lines[-30:], len(lines)-30):\n    print(f'{i}: {line}')\n\"",
    "description": "View last 30 lines of literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-16T04:24:15.225513+00:00_

2208:     venue: arXiv 2602.11201
2209:     url: https://arxiv.org/abs/2602.11201
2210:     category: faithfulness_decay
2211:     role: related_analysis
2212:     key_finding: >
2213:       提出 Normalized Logit Difference Decay (NLDD) 度量 CoT 推理步骤的 faithfulness。
2214:       发现 Reasoning Horizon (k*) 在链长度的 70-85% 处，超过后推理 token 对最终答案几乎无影响。
2215:       模型可以编码正确的内部表征但完全无法完成任务——accuracy alone does not reveal faithfulness。
2216:     relevance_to_freige: >
2217:       与 FREIGE C1 (faithfulness cost) 和 C4 (EDCR 诊断) 相关：
2218:       faithfulness decay 现象说明模型内部表征和外部输出之间存在系统性偏差，
2219:       EDCR 的 evidence-relation consistency 诊断本质上在检测类似的 faithfulness decay——
2220:       当 evidence 与 relation 预测 decouple 时，模型的 reasoning chain 变得 unfaithful。
2221: 
2222:   - title: "The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input"
2223:     authors: Google DeepMind
2224:     year: 2025
2225:     venue: arXiv 2501.03200
2226:     url: https://arxiv.org/abs/2501.03200
2227:     category: faithfulness_decay
2228:     role: background
2229:     key_finding: >
2230:       大规模 benchmark 评估 LLM 在长文档中的 grounding 能力。860 public + 859 private 样例，
2231:       要求生成完全 grounded 在提供文档中的长文本回复。使用多 judge 聚合评分缓解评估偏差。
2232:       当前最佳模型 faithfulness 得分 ~0.88，说明 grounding 仍是显著挑战。
2233:     relevance_to_freige: >
2234:       FACTS Grounding 是 faithfulness 评估的重要 benchmark，验证了 FREIGE 的核心前提：
2235:       即使最强 LLM 在 grounding 任务上也远未完美（~12% failure rate），
2236:       这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。
2237:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-16T04:24:15.225677+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "description": "Check literature_map.yaml location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "description": "Check literature_map.yaml location"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-16T04:24:15.225799+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-16T04:24:15.225914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": "2220",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "offset": "2220",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-16T04:24:15.226043+00:00_

2220	      EDCR 的 evidence-relation consistency 诊断本质上在检测类似的 faithfulness decay——
2221	      当 evidence 与 relation 预测 decouple 时，模型的 reasoning chain 变得 unfaithful。
2222	
2223	  - title: "The FACTS Grounding Leaderboard: Benchmarking LLMs' Ability to Ground Responses to Long-Form Input"
2224	    authors: Google DeepMind
2225	    year: 2025
2226	    venue: arXiv 2501.03200
2227	    url: https://arxiv.org/abs/2501.03200
2228	    category: faithfulness_decay
2229	    role: background
2230	    key_finding: >
2231	      大规模 benchmark 评估 LLM 在长文档中的 grounding 能力。860 public + 859 private 样例，
2232	      要求生成完全 grounded 在提供文档中的长文本回复。使用多 judge 聚合评分缓解评估偏差。
2233	      当前最佳模型 faithfulness 得分 ~0.88，说明 grounding 仍是显著挑战。
2234	    relevance_to_freige: >
2235	      FACTS Grounding 是 faithfulness 评估的重要 benchmark，验证了 FREIGE 的核心前提：
2236	      即使最强 LLM 在 grounding 任务上也远未完美（~12% failure rate），
2237	      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。
2238	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-16T04:24:15.226188+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "old_string": "      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。",
  "new_string": "      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。\n\n  # === Category 36: Evidence Cost in Generative IE (NEW - 2026-05-16 evidence cost scan) ===\n\n  - title: \"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers\"\n    authors: Zheng Tang, Mihai Surdeanu\n    year: 2023\n    venue: Computational Linguistics, Vol. 49, Issue 1\n    url: https://aclanthology.org/2023.cl-1.3/\n    category: evidence_cost_generative_ie\n    role: direct_competitor\n    key_finding: >\n      Joint training of relation classifier + explanation sequence labeler (extractive rationale)。\n      Joint training 不仅不损害 RE，反而提升 ~4% F1 on CoNLL04。\n      Explanation classifier 操作在 extractive features 上，保证 faithfulness。\n    relevance_to_freige: >\n      最直接的对比论文。与 FREIGE 形成关键对照：\n      Two Flints 在 sentence-level extractive discriminative 设定下发现 joint evidence+RE 有益；\n      FREIGE 在 document-level generative SFT 设定下发现 joint evidence+RE 有害 (-7.7 F1)。\n      这个差异揭示了 generative vs discriminative、sentence vs document level 的关键区别。\n\n  - title: \"Robust Explanation for Free or At the Cost of Faithfulness\"\n    authors: Zeren Tan, Yang Tian\n    year: 2023\n    venue: ICML 2023\n    url: https://proceedings.mlr.press/v202/tan23a.html\n    category: evidence_cost_generative_ie\n    role: theoretical_foundation\n    key_finding: >\n      首次理论证明 robustness-faithfulness trade-off 存在。\n      Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness\n      需牺牲 faithfulness。对 SmoothGrad 等 6 种方法验证了该 trade-off。\n    relevance_to_freige: >\n      提供 \"faithfulness 有代价\" 的理论框架。虽然研究 post-hoc explanation 而非 generative evidence，\n      但核心洞察一致：追求可解释性/忠实性可能需要牺牲其他性能维度。\n      FREIGE 的 evidence tax 是这一理论在 generative IE 中的实证体现。\n\n  - title: \"Rationalization for Explainable NLP: A Survey\"\n    authors: Sai Gurrapu et al.\n    year: 2023\n    venue: Frontiers in AI\n    url: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full\n    category: evidence_cost_generative_ie\n    role: background_survey\n    key_finding: >\n      首个 NLP rationalization 综述。列出 desiderata: \"rationale extraction should not hurt task performance\"。\n      将 rationalization 分为 extractive 和 abstractive 两类，覆盖 2007-2023 文献。\n      识别了 attention-based rationale 中 noisy rationale 和 prediction accuracy 之间的 trade-off。\n    relevance_to_freige: >\n      明确了 \"不应损害主任务\" 是学界共识 desiderata。但没有论文系统量化违反这一 desiderata 的程度。\n      FREIGE 的 -7.7 F1 evidence tax 直接挑战了这一假设，证明在 generative SFT 中该 desiderata 不成立。\n\n  - title: \"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction\"\n    authors: Xilai Yin et al.\n    year: 2023\n    venue: EMNLP 2023 Findings\n    url: https://aclanthology.org/2023.findings-emnlp.153/\n    category: evidence_cost_generative_ie\n    role: related_method\n    key_finding: >\n      CoT-ER: 用 LLM 先生成 task-specific evidence，再 CoT 推理做 few-shot RE。\n      0% training data 下与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。\n    relevance_to_freige: >\n      在 prompting 设定下 evidence+CoT 对 RE 有益。\n      与 FREIGE SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是\n      SFT 训练 specific 的问题（output format 约束 vs prompting 引导）。\n\n  - title: \"Entity and Evidence Guided Relation Extraction for DocRED\"\n    authors: Kevin Huang et al.\n    year: 2021\n    venue: RepL4NLP @ ACL 2021\n    url: https://aclanthology.org/2021.repl4nlp-1.30/\n    category: evidence_cost_generative_ie\n    role: direct_competitor\n    key_finding: >\n      E2GRE: DocRE 上首个 joint evidence prediction + relation extraction 框架。\n      利用 entity-guided input 和 pretrained LM attention 作为 evidence 特征。\n      Joint training 在 RE 和 evidence prediction 上均有增益，达到 DocRED leaderboard SOTA。\n    relevance_to_freige: >\n      DocRE 上 joint evidence+RE 的先驱工作。但使用 encoder-based discriminative 模型，\n      evidence 是 binary sentence classification（非 text generation）。\n      他们发现 joint 有益，与 FREIGE generative 设定下的发现相反——\n      核心区别在于 discriminative attention supervision vs generative output format constraint。\n\n  - title: \"Revisiting Relation Extraction in the era of Large Language Models\"\n    authors: Somin Wadhwa, Silvio Amir, Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    category: evidence_cost_generative_ie\n    role: background\n    key_finding: >\n      系统评估 GPT-3 和 Flan-T5 在标准 RE 任务上的表现。\n      Few-shot GPT-3 接近 SOTA，但 exact match 低估 generative RE 性能，需 human evaluation。\n      建立了 LLM-based generative RE 的 evaluation methodology。\n    relevance_to_freige: >\n      建立了 LLM generative RE 的 baseline context，验证了 seq2seq RE 的可行性。\n      FREIGE 在此基础上进一步探索了加入 evidence 生成后的性能变化。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "old_string": "      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。",
    "new_string": "      这证明 evidence-grounded IE 中 faithfulness 约束确实会带来 performance cost (C1)。\n\n  # === Category 36: Evidence Cost in Generative IE (NEW - 2026-05-16 evidence cost scan) ===\n\n  - title: \"It Takes Two Flints to Make a Fire: Multitask Learning of Neural Relation and Explanation Classifiers\"\n    authors: Zheng Tang, Mihai Surdeanu\n    year: 2023\n    venue: Computational Linguistics, Vol. 49, Issue 1\n    url: https://aclanthology.org/2023.cl-1.3/\n    category: evidence_cost_generative_ie\n    role: direct_competitor\n    key_finding: >\n      Joint training of relation classifier + explanation sequence labeler (extractive rationale)。\n      Joint training 不仅不损害 RE，反而提升 ~4% F1 on CoNLL04。\n      Explanation classifier 操作在 extractive features 上，保证 faithfulness。\n    relevance_to_freige: >\n      最直接的对比论文。与 FREIGE 形成关键对照：\n      Two Flints 在 sentence-level extractive discriminative 设定下发现 joint evidence+RE 有益；\n      FREIGE 在 document-level generative SFT 设定下发现 joint evidence+RE 有害 (-7.7 F1)。\n      这个差异揭示了 generative vs discriminative、sentence vs document level 的关键区别。\n\n  - title: \"Robust Explanation for Free or At the Cost of Faithfulness\"\n    authors: Zeren Tan, Yang Tian\n    year: 2023\n    venue: ICML 2023\n    url: https://proceedings.mlr.press/v202/tan23a.html\n    category: evidence_cost_generative_ie\n    role: theoretical_foundation\n    key_finding: >\n      首次理论证明 robustness-faithfulness trade-off 存在。\n      Robust model 可免费获得 robust explanation；non-robust model 提升 explanation robustness\n      需牺牲 faithfulness。对 SmoothGrad 等 6 种方法验证了该 trade-off。\n    relevance_to_freige: >\n      提供 \"faithfulness 有代价\" 的理论框架。虽然研究 post-hoc explanation 而非 generative evidence，\n      但核心洞察一致：追求可解释性/忠实性可能需要牺牲其他性能维度。\n      FREIGE 的 evidence tax 是这一理论在 generative IE 中的实证体现。\n\n  - title: \"Rationalization for Explainable NLP: A Survey\"\n    authors: Sai Gurrapu et al.\n    year: 2023\n    venue: Frontiers in AI\n    url: https://www.frontiersin.org/articles/10.3389/frai.2023.1225093/full\n    category: evidence_cost_generative_ie\n    role: background_survey\n    key_finding: >\n      首个 NLP rationalization 综述。列出 desiderata: \"rationale extraction should not hurt task performance\"。\n      将 rationalization 分为 extractive 和 abstractive 两类，覆盖 2007-2023 文献。\n      识别了 attention-based rationale 中 noisy rationale 和 prediction accuracy 之间的 trade-off。\n    relevance_to_freige: >\n      明确了 \"不应损害主任务\" 是学界共识 desiderata。但没有论文系统量化违反这一 desiderata 的程度。\n      FREIGE 的 -7.7 F1 evidence tax 直接挑战了这一假设，证明在 generative SFT 中该 desiderata 不成立。\n\n  - title: \"Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction\"\n    authors: Xilai Yin et al.\n    year: 2023\n    venue: EMNLP 2023 Findings\n    url: https://aclanthology.org/2023.findings-emnlp.153/\n    category: evidence_cost_generative_ie\n    role: related_method\n    key_finding: >\n      CoT-ER: 用 LLM 先生成 task-specific evidence，再 CoT 推理做 few-shot RE。\n      0% training data 下与 fully-supervised SOTA 竞争力相当（FewRel 1.0/2.0）。\n    relevance_to_freige: >\n      在 prompting 设定下 evidence+CoT 对 RE 有益。\n      与 FREIGE SFT 设定下 evidence 有害形成对比——说明 evidence cost 可能是\n      SFT 训练 specific 的问题（output format 约束 vs prompting 引导）。\n\n  - title: \"Entity and Evidence Guided Relation Extraction for DocRED\"\n    authors: Kevin Huang et al.\n    year: 2021\n    venue: RepL4NLP @ ACL 2021\n    url: https://aclanthology.org/2021.repl4nlp-1.30/\n    category: evidence_cost_generative_ie\n    role: direct_competitor\n    key_finding: >\n      E2GRE: DocRE 上首个 joint evidence prediction + relation extraction 框架。\n      利用 entity-guided input 和 pretrained LM attention 作为 evidence 特征。\n      Joint training 在 RE 和 evidence prediction 上均有增益，达到 DocRED leaderboard SOTA。\n    relevance_to_freige: >\n      DocRE 上 joint evidence+RE 的先驱工作。但使用 encoder-based discriminative 模型，\n      evidence 是 binary sentence classification（非 text generation）。\n      他们发现 joint 有益，与 FREIGE generative 设定下的发现相反——\n      核心区别在于 discriminative attention supervision vs generative output format constraint。\n\n  - title: \"Revisiting Relation Extraction in the era of Large Language Models\"\n    authors: Somin Wadhwa, Silvio Amir, Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    category: evidence_cost_generative_ie\n    role: background\n    key_finding: >\n      系统评估 GPT-3 和 Flan-T5 在标准 RE 任务上的表现。\n      Few-shot GPT-3 接近 SOTA，但 exact match 低估 generative RE 性能，需 human evaluation。\n      建立了 LLM-based generative RE 的 evaluation methodology。\n    relevance_to_freige: >\n      建立了 LLM generative RE 的 baseline context，验证了 seq2seq RE 的可行性。\n      FREIGE 在此基础上进一步探索了加入 evidence 生成后的性能变化。"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-16T04:24:15.226742+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-16T04:24:15.226942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-16T04:24:15.227079+00:00_

1	# Literature Map for faith-evidence-ie (FREIGE)
2	# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
3	# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion)
4	
5	papers:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-16T04:24:15.227206+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "old_string": "# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion)",
  "new_string": "# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion; +6 papers from evidence cost literature scan)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "old_string": "# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion)",
    "new_string": "# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan; +15 papers from 2026-05-16 incremental scan; +9 papers from Related Work targeted expansion; +6 papers from evidence cost literature scan)"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-16T04:24:15.227660+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-cost-literature_20260516T041839",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 91 · 2026-05-16T04:24:15.227862+00:00_

搜索完成。结果总结：

## 新颖性评估：高度新颖

**没有任何现有论文在 "generative SFT + DocRE" 设定下量化过 evidence 对 rel_f1 的代价。**

### 关键对比

现有工作（DREEAM、E2GRE、Two Flints）都在 **encoder-based discriminative** 模型中研究 evidence，且一致发现 evidence **帮助** RE。原因是 evidence 作为 attention supervision 引导模型聚焦相关 context。

FREIGE 的设定根本不同：**generative LLM SFT** 要求模型在输出中同时生成 evidence + relation，这是一个更难的任务——模型必须在有限 output capacity 中分配 token budget。-7.7 F1 的 evidence tax 在文献中是首次量化。

### 已加入 literature_map.yaml（Category 36，6 篇）

| 论文 | Role | 核心差异 |
|------|------|---------|
| Two Flints (Tang & Surdeanu, CL 2023) | direct_competitor | Sentence-level extractive → joint 有益 (+4% F1) |
| Robust Explanation (Tan & Tian, ICML 2023) | theoretical_foundation | 理论证明 faithfulness 有代价 |
| Rationalization Survey (Gurrapu+, 2023) | background_survey | Desiderata: "不应有害"，FREIGE 直接反驳 |
| CoT-ER (Yin+, EMNLP 2023 Findings) | related_method | Prompting 下 evidence 有益，与 SFT 对比 |
| E2GRE (Huang+, RepL4NLP 2021) | direct_competitor | DocRE joint evidence+RE 先驱，encoder-based → 有益 |
| Revisiting RE (Wadhwa+, ACL 2023) | background | LLM generative RE baseline |

详细报告已写入 `artifacts/evidence_cost_literature_scan.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_evidence-cost-literature_20260516T041839"
}
```

</details>

---
