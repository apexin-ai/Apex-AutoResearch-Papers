# research paper research

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_research_paper-research_20260515T020141.jsonl`
- **Structured JSON:** [`bb8ddd3fb593151e5f0a.json`](../../sessions/bb/bb8ddd3fb593151e5f0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T02:05:13.780814+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T02:05:13.781207+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T02:05:13.781373+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T02:05:13.781540+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'recursive_gen_depth_est'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T02:05:13.781709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model collapse\" recursive training 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model collapse\" recursive training 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T02:05:13.781840+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"text generation detection\" depth estimation recursive 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"text generation detection\" depth estimation recursive 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T02:05:13.781995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"recursive fine-tuning\" degradation synthetic data 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"recursive fine-tuning\" degradation synthetic data 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T02:05:13.782119+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AI-generated text\" provenance attribution generation depth 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AI-generated text\" provenance attribution generation depth 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T02:05:13.782400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"synthetic data\" iterative training quality degradation LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"synthetic data\" iterative training quality degradation LLM 2026 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T02:05:13.782615+00:00_

Web search results for query: ""model collapse" recursive training 2026 arXiv"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/html/2412.17646v1"},{"title":"A theoretical basis for model collapse in recursive training Research supported by a grant from Google Research Asia","url":"https://arxiv.org/html/2506.09401v4"},{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/html/2605.07724"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"[2506.09401] A theoretical basis for model collapse in recursive training","url":"https://arxiv.org/abs/2506.09401"},{"title":"A THEORETICAL BASIS FOR MODEL COLLAPSE IN RECURSIVE TRAINING","url":"https://arxiv.org/html/2506.09401v1"},{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"}]

I've found several relevant papers and research on model collapse and recursive training. Here are the key findings:

## Key Research on Model Collapse in Recursive Training

**Main Phenomenon:**
Indiscriminately training generative artificial intelligence on real and generated content can lead to a collapse in the ability of the models to generate diverse high-quality output.

**Recent ArXiv Papers (2026):**

1. **"A theoretica
…[truncated 1204 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T02:05:13.782826+00:00_

Web search results for query: ""recursive fine-tuning" degradation synthetic data 2026 arXiv"

Links: [{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning","url":"https://arxiv.org/html/2511.01490v1"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-TuningAccepted to Findings of the Association for Computational Linguistics (ACL 2026).","url":"https://arxiv.org/html/2511.01490"},{"title":"PSK@EEUCA 2026: Fine-Tuning Large Language Models with Synthetic Data Augmentation for Multi-Class Toxicity Detection in Gaming Chat","url":"https://arxiv.org/html/2605.07201"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory","url":"https://arxiv.org/html/2410.08942"},{"title":"[2505.13811] Context-Free Synthetic Data Mitigates Forgetting","url":"https://arxiv.org/abs/2505.13811"},{"title":"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training","url":"https://arxiv.org/html/2509.04796v1"},{"title":"[2601.01689] Mitigating Longitudinal Performance Degradation in Child Face Recognition Using Synthetic Data","url":"https://arxiv.org/abs/2601.01689"},{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/html/2605.07724"},{"title":"AIDE: Task-Specific Fine Tuning with Attribute Guided MultI-Hop Data Expansion","url":"https://arxiv.org/html/2412.06136v1"},{"title":"Think Less, Label Better: Multi-Stage Domain-Grounded Synthetic Data Generation for Fine-Tuning Large Language Models in Telecommunications","url":"https://arxiv.org/html/2509.25736v1"}]

I found several relevant arXiv papers on recursive fine-tuning, synthetic data degradation, and related topics from 2025-2026. Here are the key findings:

## Most Relevant Papers

**1. "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursi
…[truncated 1809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T02:05:13.783032+00:00_

Web search results for query: ""text generation detection" depth estimation recursive 2026 arXiv"

Links: [{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v1"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692v1"},{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"More Than Generation: Unifying Generation and Depth Estimation via Text-to-Image Diffusion Models","url":"https://arxiv.org/html/2510.23574v1"},{"title":"[2603.23146v1] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146v1"},{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"}]

Based on the search results, I found several recent arXiv papers on text generation detection from 2026, though the specific combination of all your query terms doesn't appear in a single paper. Here are the most relevant findings:

## Key Papers on AI-Generated Text Detection (2026)

**DivEye - Diversity Boosts AI-Generated Text Detection**

Published in Transactions on Machine Learning Research (02/2026), DivEye is a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-bas
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T02:05:13.783293+00:00_

Web search results for query: ""synthetic data" iterative training quality degradation LLM 2026 arXiv"

Links: [{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-TuningAccepted to Findings of the Association for Computational Linguistics (ACL 2026).","url":"https://arxiv.org/html/2511.01490"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning","url":"https://arxiv.org/html/2511.01490v1"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631v1"},{"title":"[2510.01631] Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/abs/2510.01631"},{"title":"Towards Active Synthetic Data Generation for Finetuning Language Models","url":"https://arxiv.org/html/2512.00884"},{"title":"Demystifying Synthetic Data in LLM Pre-training:","url":"https://arxiv.org/pdf/2510.01631"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"Scaling Laws of Synthetic Data for Language Models","url":"https://arxiv.org/html/2503.19551v3"},{"title":"On the Diversity of Synthetic Data and its Impact on Training Large Language Models","url":"https://arxiv.org/html/2410.15226v2"}]

I found several highly relevant arXiv papers from 2025-2026 on synthetic data, iterative training, and quality degradation in LLMs. Here are the key findings:

## Main Research Findings

**Model Collapse and Iterative Training:**

Model collapse refers to the degradation of some aspect of a model's output
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T02:05:13.783506+00:00_

Web search results for query: ""AI-generated text" provenance attribution generation depth 2026 arXiv"

Links: [{"title":"[2601.00218] Unknown Aware AI-Generated Content Attribution","url":"https://arxiv.org/abs/2601.00218"},{"title":"Unknown Aware AI-Generated Content Attribution Ellie Thieu UW–Madison","url":"https://arxiv.org/pdf/2601.00218"},{"title":"[2501.02406] A Training-free Method for LLM Text Attribution","url":"https://arxiv.org/abs/2501.02406"},{"title":"A Faceted Proposal for Transparent Attribution of AI-Assisted Text Production","url":"https://arxiv.org/html/2604.25346v1"},{"title":"Unknown Aware AI-Generated Content Attribution","url":"https://arxiv.org/html/2601.00218v1"},{"title":"Toward Reliable Provenance in AI-Generated Content: Text, Images, and Code | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/toward-reliable-provenance-in-ai-generated-content-text-images-and-code-9ebe8c57ceae"},{"title":"A Practical Synthesis of Detecting AI-Generated Textual, ...","url":"https://arxiv.org/pdf/2504.02898"},{"title":"Document Attribution: Examining Citation Relationships using Large Language Models","url":"https://arxiv.org/html/2505.06324.pdf"},{"title":"[2603.15034] Interpretable Predictability-Based AI Text Detection: A Replication Study","url":"https://arxiv.org/abs/2603.15034"},{"title":"[2509.13365] The Provenance Problem: LLMs and the Breakdown of Citation Norms","url":"https://arxiv.org/abs/2509.13365"}]

I've performed a web search for "AI-generated text provenance attribution 2026 arXiv" and found several relevant research papers. Here are the key findings:

## Recent arXiv Papers on AI-Generated Text Provenance and Attribution (2026)

### LLM Text Attribution
Verifying the provenance of content is crucial to the functioning of many organizations, e.g., educational institutions, social media platforms, and firms. A training-free method for LLM text attribution paper addresses how this problem is becoming increasingly chal
…[truncated 1232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T02:05:13.783701+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "detect generation depth recursive LLM synthetic data statistical features perplexity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "detect generation depth recursive LLM synthetic data statistical features perplexity 2026"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T02:05:13.783835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"model collapse\" detection \"how many\" generations iterations depth estimation arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"model collapse\" detection \"how many\" generations iterations depth estimation arXiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T02:05:13.784010+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.10531 \"From Collapse to Improvement\" iterative training contaminated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.10531 \"From Collapse to Improvement\" iterative training contaminated"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T02:05:13.784183+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.07724 \"Curated Synthetic Data Doesn't Have to Collapse\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.07724 \"Curated Synthetic Data Doesn't Have to Collapse\" 2026"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T02:05:13.784336+00:00_

Web search results for query: ""model collapse" detection "how many" generations iterations depth estimation arXiv 2026"

Links: [{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"[2510.16657] Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence","url":"https://arxiv.org/abs/2510.16657"},{"title":"Escaping Model Collapse via Synthetic Data Verification:","url":"https://arxiv.org/pdf/2510.16657"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/html/2412.17646v1"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"}]

Based on the search results, I found several relevant papers on model collapse detection and analysis. Here are the key findings:

## Recent Research on Model Collapse

Model collapse is a phenomenon in which recursive iteratio
…[truncated 1500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T02:05:13.784525+00:00_

Web search results for query: "detect generation depth recursive LLM synthetic data statistical features perplexity 2026"

Links: [{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-TuningAccepted to Findings of the Association for Computational Linguistics (ACL 2026).","url":"https://arxiv.org/html/2511.01490"},{"title":"Models - Perplexity","url":"https://docs.perplexity.ai/docs/sonar/models"},{"title":"LLMDet: A Third Party Large Language Models Generated Text Detection Tool","url":"https://arxiv.org/pdf/2305.15004"},{"title":"Stack More LLM’s: Efficient Detection of Machine-Generated Texts via Perplexity Approximation | Doklady Mathematics","url":"https://link.springer.com/article/10.1134/S1064562424602075"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Not all tokens are created equal: Perplexity Attention Weighted Networks for AI-generated text detection - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S156625352500538X"},{"title":"Low-Perplexity LLM-Generated Sequences and Where To Find Them","url":"https://arxiv.org/html/2507.01844v1"},{"title":"Investigating Efficacy of Perplexity in Detecting LLM-Generated Code","url":"https://arxiv.org/html/2412.16525v1"},{"title":"The Science of Detecting LLM-Generated Text – Communications of the ACM","url":"https://cacm.acm.org/research/the-science-of-detecting-llm-generated-text/"}]

Based on the web search results, I found several relevant papers and research related to detecting LLM-generated synthetic data and measuring perplexity. Here's what the search uncovered:

## Key Findings:

**Synthetic Data and Model Collapse:**
Model collapse is a degenerative process affecting generations of learned generative models, in which the dat
…[truncated 1837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T02:05:13.784707+00:00_

Web search results for query: "arXiv 2602.10531 "From Collapse to Improvement" iterative training contaminated"

Links: [{"title":"[2602.10531] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/html/2602.10531"},{"title":"[2602.10531v1] From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources","url":"https://arxiv.org/abs/2602.10531v1"},{"title":"From Collapse to Improvement: Statistical Perspectives on the Evolutionary","url":"https://arxiv.org/pdf/2602.10531"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065v1"},{"title":"When Models Don’t Collapse: On the Consistency of Iterative MLE","url":"https://arxiv.org/html/2505.19046v1"},{"title":"The Value of Variance: Mitigating Debate Collapse in Multi-Agent...","url":"https://arxiv.org/abs/2602.07186"},{"title":"A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula","url":"https://arxiv.org/html/2602.10014"},{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Reinforcement","url":"https://arxiv.org/html/2406.07515v1"}]

I found the paper! Here's information about arXiv 2602.10531:

**Title:** "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"

**Authors:** Soham Bakshi and Sunrit Chakraborty

**Key Findings:**

The 
…[truncated 1176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T02:05:13.785027+00:00_

Web search results for query: "arXiv 2605.07724 "Curated Synthetic Data Doesn't Have to Collapse" 2026"

Links: [{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/html/2605.07724"},{"title":"[2605.07724] Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/abs/2605.07724"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713v4"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI | by Alexander Watson | TDS Archive | Medium","url":"https://medium.com/data-science/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai-7cd380208d14"},{"t
…[truncated 1306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T02:05:13.785250+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "predict number of recursive generations synthetic text forensics \"generation count\" LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "predict number of recursive generations synthetic text forensics \"generation count\" LLM 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T02:05:13.785396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.18880 DivEye surprisal diversity AI text detection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.18880 DivEye surprisal diversity AI text detection 2026"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T02:05:13.785680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.13692 \"Breaking the Generator Barrier\" disentangled AI text detection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.13692 \"Breaking the Generator Barrier\" disentangled AI text detection 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T02:05:13.785816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"machine-generated text\" \"model collapse\" prevention detection filter 2026 arXiv 2502.15654"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"machine-generated text\" \"model collapse\" prevention detection filter 2026 arXiv 2502.15654"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T02:05:13.786018+00:00_

Web search results for query: "arXiv 2509.18880 DivEye surprisal diversity AI text detection 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.researchgate.net/publication/395771470_Diversity_Boosts_AI-Generated_Text_Detection"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"}]

I found comprehensive information about the arXiv paper 2509.18880. Here's what I discovered:

## Overview

DivEye is a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. It is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs.

## Key Features

DivEye extracts diversity-based features from token-level surprisal patterns. The feature set captures token-level surprisal patterns across multip
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T02:05:13.786210+00:00_

Web search results for query: "predict number of recursive generations synthetic text forensics "generation count" LLM 2025 2026"

Links: [{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Synthetic Data Generation Using Large Language Models","url":"https://arxiv.org/pdf/2503.14023"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v1"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"Generation of Programmatic Rules for Document Forgery ...","url":"https://arxiv.org/pdf/2512.19228"},{"title":"GitHub - ahmad-alismail/LLM_based_Synthetic_Data_Generation: A curated and continuously updated collection of papers, tools, and datasets on synthetic data generation using LLMs and agentic workflows.","url":"https://github.com/ahmad-alismail/LLM_based_Synthetic_Data_Generation"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Synthetic Data in the Era of LLMs","url":"https://synth-data-acl.github.io/"},{"title":"Large language models in digital forensics: capabilities, challenges and future directions - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666281725001830"}]

Based on the search results, I found relevant information about recursive generations of synthetic text and LLMs. Here are the key findings:

## Model Collapse and Recursive Generations

Learning from data produced by other models causes 'model collapse'—a degenerative process whereby, over time, models forget the true underlying data distribution. Over tim
…[truncated 1328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T02:05:13.786406+00:00_

Web search results for query: ""machine-generated text" "model collapse" prevention detection filter 2026 arXiv 2502.15654"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"[2507.15654] On Ward Numbers and Increasing Schröder Trees","url":"https://arxiv.org/abs/2507.15654"},{"title":"arXiv:2502.15654v5 [cs.CL] 19 May 2025","url":"https://arxiv.org/pdf/2502.15654"},{"title":"[2308.15654] Injective edge colorings of degenerate graphs and the oriented chromatic number","url":"https://arxiv.org/abs/2308.15654"},{"title":"arXiv:2307.15654v1 [quant-ph] 28 Jul 2023","url":"https://arxiv.org/pdf/2307.15654"},{"title":"[2501.15654] People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text","url":"https://arxiv.org/abs/2501.15654"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.15654"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2309.15654"},{"title":"[2502.15646] Predicting gene essentiality and drug response from perturbation screens in preclinical cancer models with LEAP: Layered Ensemble of Autoencoders and Predictors","url":"https://arxiv.org/abs/2502.15646"}]

I found the paper you're looking for! Here's what the search revealed about arXiv paper 2502.15654:

The paper is titled "Machine-generated text detection prevents language model collapse".

**Key findings:**

As Large Language Models become increasingly prevalent, their generated outputs are proliferating across the web, and since online data is the primary resource for LLM pre-training, subsequent models could be trained on an unknown portion of synthetic samples.

This could lead to model collapse, a degenerative process whereby LLMs reinforce their own errors, reduce output diversity, and ultimately yield declining performance.

…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T02:05:13.786582+00:00_

Web search results for query: "arXiv 2604.13692 "Breaking the Generator Barrier" disentangled AI text detection 2026"

Links: [{"title":"[2604.13692v1] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692v1"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692v1"},{"title":"[2604.13692] Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/abs/2604.13692"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"Explainable Disentangled Representation Learning for Generalizable","url":"https://arxiv.org/pdf/2604.21300"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"},{"title":"Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/html/2410.08113v1"},{"title":"Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/html/2604.21300"},{"title":"[2604.21300] Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI","url":"https://arxiv.org/abs/2604.21300"},{"title":"[2603.23146v1] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146v1"}]

I found the paper! Here's what the search results show about arXiv 2604.13692:

## "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection"

The paper was submitted on April 15, 2026 by authors Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, and Xiuli Bi from Chongqing University of Posts and Telecommunications, Chin
…[truncated 1504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T02:05:13.786767+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.16065 \"Can Generative AI Survive Data Contamination\" recursive training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.16065 \"Can Generative AI Survive Data Contamination\" recursive training 2026"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T02:05:13.786931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"text genealogy\" OR \"model genealogy\" OR \"generation lineage\" synthetic AI text tracing 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"text genealogy\" OR \"model genealogy\" OR \"generation lineage\" synthetic AI text tracing 2026 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T02:05:13.787071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.23146 \"Why AI-Generated Text Detection Fails\" explainable 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.23146 \"Why AI-Generated Text Detection Fails\" explainable 2026"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T02:05:13.787252+00:00_

Web search results for query: "arXiv 2602.16065 "Can Generative AI Survive Data Contamination" recursive training 2026"

Links: [{"title":"[2602.16065] Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/abs/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training","url":"https://arxiv.org/html/2602.16065"},{"title":"Can Generative Artificial Intelligence Survive Data ...","url":"https://arxiv.org/pdf/2602.16065"},{"title":"Rethinking Data Protection in the (Generative) Artificial Intelligence Era","url":"https://arxiv.org/html/2507.03034v4"},{"title":"AI-generated data contamination erodes pathological variability and diagnostic reliability | Research Square","url":"https://www.researchsquare.com/article/rs-8753102/v1"},{"title":"Retrieval Collapses When AI Pollutes the Web","url":"https://arxiv.org/html/2602.16136"},{"title":"AI-generated data contamination erodes pathological variability and diagnostic reliability | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344383v1.full"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Model Collapse and the Right to Uncontaminated Human-Generated Data - Harvard Journal of Law & Technology","url":"https://jolt.law.harvard.edu/digest/model-collapse-and-the-right-to-uncontaminated-human-generated-data"},{"title":"A Closer Look at the Existing Risks of Generative AI: Mapping the Who, What, and How of Real-World Incidents","url":"https://arxiv.org/html/2505.22073v2"}]

I found the paper you requested! Here's what I discovered:

## arXiv 2602.16065 - "Can Generative Artificial Intelligence Survive Data Contamination?"

The paper was submitted on February 17, 2026, and is authored by Kevin Wang, Hongqian Niu, and Didong Li.

### Main Focus

The paper addresses h
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T02:05:13.787445+00:00_

Web search results for query: ""text genealogy" OR "model genealogy" OR "generation lineage" synthetic AI text tracing 2026 arXiv"

Links: [{"title":"The Best Uses of AI for Genealogists - Legacy Family Tree Webinars","url":"https://familytreewebinars.com/webinar/the-best-uses-of-ai-for-genealogists"},{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v1"},{"title":"A Genealogist's Guide to Artificial Intelligence (2026)","url":"https://www.aboutdarwin.com/a-genealogists-guide-to-artificial-intelligence/"},{"title":"Synthetic Data Generation with Large Language Models for Text","url":"https://arxiv.org/pdf/2310.07849"},{"title":"AI and Genealogy: Advancements You Can Use • FamilySearch","url":"https://www.familysearch.org/en/blog/ai-developments-genealogy"},{"title":"A Genealogist's Guide to Artificial Intelligence - Family Tree Magazine","url":"https://familytreemagazine.com/resources/software/ai-and-genealogy/"},{"title":"Ancestors and Algorithms: AI for Genealogy","url":"https://ancestorsandai.buzzsprout.com/"},{"title":"How AI will change genealogy in 2026 - Chronicle Makers","url":"https://denyseallen.substack.com/p/how-ai-will-change-genealogy-2026"},{"title":"Which AI Tool Is Best for Genealogy in 2025? ChatGPT vs Claude vs Gemini vs Perplexity","url":"https://denyseallen.substack.com/p/ai-tool-comparison-genealogy-2025"},{"title":"Generative AI for Synthetic Data Generation: Methods, ...","url":"https://arxiv.org/pdf/2403.04190"}]

Based on the search results, I found relevant information about synthetic data generation using AI, though the results focus more on genealogy applications and synthetic text generation rather than specifically on "text genealogy" or "model genealogy" as a research field. Here's what I found:

## Synthetic Data Generation with Large Language Models

Recent advances in generative AI – particularly LLMs like Claude 3.7 Sonnet, DeepSeek's R1, Meta's Llam
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T02:05:13.787626+00:00_

Web search results for query: "arXiv 2603.23146 "Why AI-Generated Text Detection Fails" explainable 2026"

Links: [{"title":"[2603.23146] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146"},{"title":"[2603.23146v1] Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/abs/2603.23146v1"},{"title":"Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy","url":"https://arxiv.org/html/2603.23146"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection","url":"https://arxiv.org/html/2604.13692v1"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods","url":"https://arxiv.org/html/2406.15583v1"},{"title":"The Problems with AI Detectors: False Positives and False Negatives - Generative AI Detection Tools - Guides at University of San Diego Legal Research Center","url":"https://lawlibguides.sandiego.edu/c.php?g=1443311&p=10721367"},{"title":"AI Detectors Fail Diverse Student Populations: A Mathematical Framing of Structural Detection Limits","url":"https://arxiv.org/html/2603.20254"}]

I found the paper! Here's what I discovered:

The paper arXiv:2603.23146 is titled "Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy" by Shushanta Pudasaini, Luis Miralles-Pechuán, David Lillis, and Marisa Llorens Salvador, submitted on March 24, 2026 with the latest version from April 22, 2026.

**Key Findings:**

The paper addresses how the widespre
…[truncated 1185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T02:05:13.787816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"recursive depth\" OR \"generation depth\" OR \"iteration count\" predict classify synthetic text perplexity surprisal arXiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"recursive depth\" OR \"generation depth\" OR \"iteration count\" predict classify synthetic text perplexity surprisal arXiv 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T02:05:13.787975+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2412.17646 \"Rate of Model Collapse\" recursive training 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2412.17646 \"Rate of Model Collapse\" recursive training 2024"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T02:05:13.788777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.16499 \"model collapse\" generalization memorization 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.16499 \"model collapse\" generalization memorization 2025"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T02:05:13.789135+00:00_

Web search results for query: "arXiv 2412.17646 "Rate of Model Collapse" recursive training 2024"

Links: [{"title":"[2412.17646] Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/abs/2412.17646"},{"title":"Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/html/2412.17646"},{"title":"Rate of Model Collapse in Recursive Training - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241217646T/abstract"},{"title":"[Literature Review] Rate of Model Collapse in Recursive Training","url":"https://www.themoonlight.io/en/review/rate-of-model-collapse-in-recursive-training"},{"title":"(PDF) Rate of Model Collapse in Recursive Training","url":"https://www.researchgate.net/publication/387350343_Rate_of_Model_Collapse_in_Recursive_Training"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v2"},{"title":"A theoretical basis for model collapse in recursive training Research supported by a grant from Google Research Asia","url":"https://arxiv.org/html/2506.09401"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"}]

I found the paper you were looking for. Here's what I can tell you about arXiv 2412.17646:

## "Rate of Model Collapse in Recursive Training"

**Paper Details:**
- Authors: Ananda Theertha Suresh, Andrew Thangaraj, and Aditya Nanda Kishore Khandavally
- Submitted on December 23, 2024

**Research Focus:**
As models are recursively trained on generated data from previous rounds, their ability to capture the nuances of the original human-generated data may degrade, often referred to as model collapse.

**Main Con
…[truncated 741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T02:05:13.789438+00:00_

Web search results for query: ""recursive depth" OR "generation depth" OR "iteration count" predict classify synthetic text perplexity surprisal arXiv 2025 2026"

Links: [{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Teaching Pretrained Language Models to Think Deeper with Retrofitted Recurrence","url":"https://arxiv.org/html/2511.07384v1"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-TuningAccepted to Findings of the Association for Computational Linguistics (ACL 2026).","url":"https://arxiv.org/html/2511.01490"},{"title":"Decoding Game: On Minimax Optimality of Heuristic Text Generation Strategies","url":"https://arxiv.org/html/2410.03968v1"},{"title":"Thinking Deeper, Not Longer: Depth-Recurrent Transformers for Compositional Generalization","url":"https://arxiv.org/html/2603.21676"},{"title":"Advancing Search-Augmented Language Models","url":"https://research.perplexity.ai/articles/advancing-search-augmented-language-models"},{"title":"ResearchRubrics: A Benchmark of Prompts and Rubrics For Evaluating Deep Research Agents","url":"https://arxiv.org/html/2511.07685v1"},{"title":"LoopFormer: Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation","url":"https://arxiv.org/html/2602.11451v1"},{"title":"[2507.01844] Low-Perplexity LLM-Generated Sequences and Where To Find Them","url":"https://arxiv.org/abs/2507.01844"}]

The search has returned several relevant papers from arXiv published in 2025-2026. Here's a summary of what I found:

## Key Papers Found:

### 1. **DivEye: Diversity Boosts AI-Generated Text Detection** (September 2025)
This paper proposes DivEye, a detection framework that captures how unpredictability fluctuates across text using surprisal-based features, built on the observation that fluctuations 
…[truncated 1700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T02:05:13.789730+00:00_

Web search results for query: "arXiv 2509.16499 "model collapse" generalization memorization 2025"

Links: [{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"[2509.16499] A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/abs/2509.16499"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://shilianghe007.github.io/model-collapse/index.html"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"A Closer Look at Model Collapse","url":"https://arxiv.org/pdf/2509.16499"},{"title":"NeurIPS Poster A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119754"},{"title":"Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study","url":"https://arxiv.org/html/2602.16601v1"},{"title":"Flatness is Necessary, Neural Collapse is Not: Rethinking Generalization via Grokking","url":"https://arxiv.org/html/2509.17738"},{"title":"Generalization vs. Memorization in Autoregressive Deep Learning: Or, Examining Temporal Decay of Gradient Coherence","url":"https://arxiv.org/html/2509.00024"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1200&show=2000"}]

Based on the search results, here's what I found about arXiv paper 2509.16499:

## Paper Overview

The paper addresses model collapse—a phenomenon in which recursive iterations of training on synthetic data lead to performance degradation in diffusion models.

## Main Contribution

The paper identifies a transition from generalization to memorization during model collapse in dif
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T02:05:13.790066+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T02:05:13.790270+00:00_

_project
atlas
atlas_v1_analysis
atlas_v2
baseline_diveye.py
baseline_perplexity_regression.py
baseline_zero_shot_llm.py
baselines.py
dcol_002_oom_diagnosis.md
dcol_code
dcol_deberta_002
dcol_feature_mlp.py
diveye_citation_audit.md
dream_reports
eval_d1d3.py
feature_importance_consistency_analysis.md
manifest.yaml
olmo_temp09_001
pythia_topk50_001

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T02:05:13.790490+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md",
  "content": "# Literature Scan: Recursive Generation Depth Estimation\n**Date:** 2026-05-15  \n**Scope:** 2026 Jan–May (arXiv / published), plus late-2025 papers accepted at 2026 venues  \n**Focus:** Is anyone doing recursive generation depth/iteration count estimation?\n\n---\n\n## Executive Summary\n\n**No direct competitor found.** No paper specifically addresses the problem of predicting how many recursive model→data→model iterations a text has undergone. The niche remains open.\n\nKey developments in adjacent areas:\n- Model collapse theory has advanced significantly (3 new theoretical papers in Feb 2026)\n- AI text detection community is moving toward surprisal-diversity features (DivEye) and generator-agnostic methods — both relevant as method components\n- Provenance/attribution work focuses on \"which model generated this\" rather than \"how many generations deep\"\n\n---\n\n## Papers by Relevance\n\n### METHOD-COMPONENT (directly usable techniques)\n\n#### 1. DivEye: Diversity Boosts AI-Generated Text Detection\n- **arXiv:** 2509.18880 | **Venue:** TMLR Feb 2026, ICLR 2026\n- **Authors:** Basani & Chen (IBM)\n- **Summary:** Uses token-level surprisal diversity features (distributional moments, first-order shifts, second-order dynamics) to detect AI text. Outperforms zero-shot detectors by up to 33.2%.\n- **Relation:** Our project uses similar statistical features (perplexity, surprisal). DivEye's higher-order surprisal statistics could be strong features for depth regression. Their feature set is a natural baseline/component. **Already cited in project — verify feature overlap with our implementation.**\n\n#### 2. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\n- **arXiv:** 2604.13692 | **Date:** Apr 2026\n- **Authors:** Pu, Cheng, Yuan, Wu, Bi (Chongqing Univ.)\n- **Summary:** Disentangles AI-detection semantics from generator-specific artifacts via dual-bottleneck + perturbation regularization. Aims for cross-generator generalization.\n- **Relation:** If we want depth estimation to generalize across different base models, their disentanglement approach could inform our feature design. The \"generator-agnostic detection signal\" is analogous to what we need for \"depth-agnostic-to-model\" estimation.\n\n#### 3. Machine-Generated Text Detection Prevents Language Model Collapse\n- **arXiv:** 2502.15654 | **Date:** Feb 2025 (updated May 2025)\n- **Authors:** (multiple)\n- **Summary:** Shows that filtering synthetic data via MGT detection before retraining mitigates collapse. Analyzes text characteristics at each model generation and their similarity to human references.\n- **Relation:** They analyze per-generation text characteristics — similar signal space to ours. Difference: they use detection as a filter, we use it for depth regression. Their per-generation analysis may contain useful signal characterization.\n\n#### 4. Why AI-Generated Text Detection Fails: Evidence from Explainable AI\n- **arXiv:** 2603.23146 | **Date:** Mar 2026\n- **Authors:** Pudasaini et al.\n- **Summary:** Despite F1=0.9734 in-domain, detection degrades severely under distribution shift. Most discriminative features are also most shift-sensitive.\n- **Relation:** **Important caveat for our approach.** If surface statistical features are domain-fragile for binary detection, they may be even more fragile for ordinal depth regression. We should test cross-domain robustness explicitly.\n\n---\n\n### BACKGROUND (model collapse dynamics — informs what signals exist at each depth)\n\n#### 5. From Collapse to Improvement: Statistical Perspectives on Iterative Training\n- **arXiv:** 2602.10531 | **Date:** Feb 2026\n- **Authors:** Bakshi & Chakraborty\n- **Summary:** Proves that iterative training on contaminated data (mixture of real + synthetic) can *improve* performance if sufficient fresh real data is mixed in. Analyzes how mixture weights and sample size control long-term trajectory.\n- **Relation:** Directly relevant to understanding the signal landscape. If some depth levels actually *improve* (not degrade), our regression target may be non-monotonic. Their theoretical framework helps predict when depth signals are strong vs. weak.\n\n#### 6. Can Generative AI Survive Data Contamination? Theoretical Guarantees\n- **arXiv:** 2602.16065 | **Date:** Feb 2026\n- **Authors:** Wang, Niu, Li\n- **Summary:** Extends model collapse theory beyond Gaussian/discrete to more realistic distribution families. Provides guarantees under contaminated recursive training.\n- **Relation:** Provides stronger theoretical grounding for why our depth signal should exist in realistic settings (not just toy distributions).\n\n#### 7. Curated Synthetic Data Doesn't Have to Collapse\n- **arXiv:** 2605.07724 | **Date:** May 2026\n- **Authors:** Falahati, Amiri, Larson, Golab\n- **Summary:** Pluralistic curation (multiple reward functions) prevents collapse. Converged distribution satisfies weighted Nash bargaining.\n- **Relation:** If curated recursive training doesn't collapse, the statistical drift we rely on for depth detection may not manifest. This defines a harder case for our method — curated pipelines may produce depth-invariant text.\n\n#### 8. Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\n- **arXiv:** 2511.01490 | **Venue:** ACL 2026 Findings\n- **Authors:** (multiple)\n- **Summary:** Multi-source synthetic data reduces distribution collapse. Measures perplexity, Self-BLEU-3, lexical diversity within/across responses.\n- **Relation:** Their diversity metrics (Self-BLEU, lexical diversity) are candidate features for our depth predictor. Their finding that source diversity modulates collapse rate means our model needs to be robust to source-diversity variation.\n\n#### 9. Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\n- **arXiv:** 2509.04796 | **Date:** Sep 2025\n- **Summary:** Defines three-stage knowledge collapse: factual accuracy degrades while surface fluency persists. Domain-specific training delays collapse 15×.\n- **Relation:** Key insight: surface fluency is not a reliable depth signal; factual accuracy is. Our features should capture factual degradation, not just stylistic shifts. Suggests incorporating factual consistency metrics.\n\n---\n\n### PROVENANCE/ATTRIBUTION (related problem, different angle)\n\n#### 10. Unknown Aware AI-Generated Content Attribution\n- **arXiv:** 2601.00218 | **Date:** Jan 2026\n- **Summary:** Attribution framework handling unknown generators. Assigns content to known models or flags as unknown.\n- **Relation:** They solve \"which model?\" — we solve \"how many iterations?\" Complementary problems. Their open-set recognition approach could inform how we handle unknown base models.\n\n#### 11. Explainable Disentangled Representation for Authorship Attribution in the Era of GenAI\n- **arXiv:** 2604.21300 | **Date:** Apr 2026\n- **Summary:** Disentangled representations for authorship attribution across human and AI authors.\n- **Relation:** Authorship attribution at the model level is adjacent to depth attribution. Their disentanglement framework could extend to depth as an additional latent factor.\n\n#### 12. A Faceted Proposal for Transparent Attribution of AI-Assisted Text\n- **arXiv:** 2604.25346 | **Date:** Apr 2026\n- **Summary:** Multi-faceted attribution model covering Form, Generation, Evaluation, Intent, Control, Traceability.\n- **Relation:** Their \"Traceability\" facet is closest to our depth problem. Their framework could position our work as solving one specific facet of a broader attribution problem.\n\n---\n\n### EVALUATION (benchmarks/methods)\n\n#### 13. Interpretable Predictability-Based AI Text Detection: A Replication Study\n- **arXiv:** 2603.15034 | **Date:** Mar 2026\n- **Summary:** Replicates and extends predictability-based detection systems from AuTexTification 2023.\n- **Relation:** Provides a reproducibility baseline for predictability-based methods. Useful for sanity-checking our feature pipeline.\n\n---\n\n## Key Takeaways for the Project\n\n1. **No competitor for depth regression.** Binary detection (human vs. AI) and source attribution (which model) are crowded. Ordinal depth estimation remains novel.\n\n2. **DivEye's surprisal features are the closest method overlap.** Ensure we cite it properly and demonstrate that our depth-regression features go beyond their binary classification features.\n\n3. **Model collapse theory now shows non-monotonic dynamics** (paper #5). Our depth signal may not increase linearly — important for regression model design (consider non-linear targets).\n\n4. **Curated/diverse recursive training weakens depth signal** (papers #7, #8). This should be discussed as a limitation and tested as a hard case.\n\n5. **Factual degradation > stylistic degradation as depth signal** (paper #9). Consider adding factual consistency features beyond perplexity/surprisal.\n\n6. **Detection features are domain-fragile** (paper #4). Cross-domain evaluation is essential for credibility.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md",
    "content": "# Literature Scan: Recursive Generation Depth Estimation\n**Date:** 2026-05-15  \n**Scope:** 2026 Jan–May (arXiv / published), plus late-2025 papers accepted at 2026 venues  \n**Focus:** Is anyone doing recursive generation depth/iteration count estimation?\n\n---\n\n## Executive Summary\n\n**No direct competitor found.** No paper specifically addresses the problem of predicting how many recursive model→data→model iterations a text has undergone. The niche remains open.\n\nKey developments in adjacent areas:\n- Model collapse theory has advanced significantly (3 new theoretical papers in Feb 2026)\n- AI text detection community is moving toward surprisal-diversity features (DivEye) and generator-agnostic methods — both relevant as method components\n- Provenance/attribution work focuses on \"which model generated this\" rather than \"how many generations deep\"\n\n---\n\n## Papers by Relevance\n\n### METHOD-COMPONENT (directly usable techniques)\n\n#### 1. DivEye: Diversity Boosts AI-Generated Text Detection\n- **arXiv:** 2509.18880 | **Venue:** TMLR Feb 2026, ICLR 2026\n- **Authors:** Basani & Chen (IBM)\n- **Summary:** Uses token-level surprisal diversity features (distributional moments, first-order shifts, second-order dynamics) to detect AI text. Outperforms zero-shot detectors by up to 33.2%.\n- **Relation:** Our project uses similar statistical features (perplexity, surprisal). DivEye's higher-order surprisal statistics could be strong features for depth regression. Their feature set is a natural baseline/component. **Already cited in project — verify feature overlap with our implementation.**\n\n#### 2. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\n- **arXiv:** 2604.13692 | **Date:** Apr 2026\n- **Authors:** Pu, Cheng, Yuan, Wu, Bi (Chongqing Univ.)\n- **Summary:** Disentangles AI-detection semantics from generator-specific artifacts via dual-bottleneck + perturbation regularization. Aims for cross-generator generalization.\n- **Relation:** If we want depth estimation to generalize across different base models, their disentanglement approach could inform our feature design. The \"generator-agnostic detection signal\" is analogous to what we need for \"depth-agnostic-to-model\" estimation.\n\n#### 3. Machine-Generated Text Detection Prevents Language Model Collapse\n- **arXiv:** 2502.15654 | **Date:** Feb 2025 (updated May 2025)\n- **Authors:** (multiple)\n- **Summary:** Shows that filtering synthetic data via MGT detection before retraining mitigates collapse. Analyzes text characteristics at each model generation and their similarity to human references.\n- **Relation:** They analyze per-generation text characteristics — similar signal space to ours. Difference: they use detection as a filter, we use it for depth regression. Their per-generation analysis may contain useful signal characterization.\n\n#### 4. Why AI-Generated Text Detection Fails: Evidence from Explainable AI\n- **arXiv:** 2603.23146 | **Date:** Mar 2026\n- **Authors:** Pudasaini et al.\n- **Summary:** Despite F1=0.9734 in-domain, detection degrades severely under distribution shift. Most discriminative features are also most shift-sensitive.\n- **Relation:** **Important caveat for our approach.** If surface statistical features are domain-fragile for binary detection, they may be even more fragile for ordinal depth regression. We should test cross-domain robustness explicitly.\n\n---\n\n### BACKGROUND (model collapse dynamics — informs what signals exist at each depth)\n\n#### 5. From Collapse to Improvement: Statistical Perspectives on Iterative Training\n- **arXiv:** 2602.10531 | **Date:** Feb 2026\n- **Authors:** Bakshi & Chakraborty\n- **Summary:** Proves that iterative training on contaminated data (mixture of real + synthetic) can *improve* performance if sufficient fresh real data is mixed in. Analyzes how mixture weights and sample size control long-term trajectory.\n- **Relation:** Directly relevant to understanding the signal landscape. If some depth levels actually *improve* (not degrade), our regression target may be non-monotonic. Their theoretical framework helps predict when depth signals are strong vs. weak.\n\n#### 6. Can Generative AI Survive Data Contamination? Theoretical Guarantees\n- **arXiv:** 2602.16065 | **Date:** Feb 2026\n- **Authors:** Wang, Niu, Li\n- **Summary:** Extends model collapse theory beyond Gaussian/discrete to more realistic distribution families. Provides guarantees under contaminated recursive training.\n- **Relation:** Provides stronger theoretical grounding for why our depth signal should exist in realistic settings (not just toy distributions).\n\n#### 7. Curated Synthetic Data Doesn't Have to Collapse\n- **arXiv:** 2605.07724 | **Date:** May 2026\n- **Authors:** Falahati, Amiri, Larson, Golab\n- **Summary:** Pluralistic curation (multiple reward functions) prevents collapse. Converged distribution satisfies weighted Nash bargaining.\n- **Relation:** If curated recursive training doesn't collapse, the statistical drift we rely on for depth detection may not manifest. This defines a harder case for our method — curated pipelines may produce depth-invariant text.\n\n#### 8. Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\n- **arXiv:** 2511.01490 | **Venue:** ACL 2026 Findings\n- **Authors:** (multiple)\n- **Summary:** Multi-source synthetic data reduces distribution collapse. Measures perplexity, Self-BLEU-3, lexical diversity within/across responses.\n- **Relation:** Their diversity metrics (Self-BLEU, lexical diversity) are candidate features for our depth predictor. Their finding that source diversity modulates collapse rate means our model needs to be robust to source-diversity variation.\n\n#### 9. Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\n- **arXiv:** 2509.04796 | **Date:** Sep 2025\n- **Summary:** Defines three-stage knowledge collapse: factual accuracy degrades while surface fluency persists. Domain-specific training delays collapse 15×.\n- **Relation:** Key insight: surface fluency is not a reliable depth signal; factual accuracy is. Our features should capture factual degradation, not just stylistic shifts. Suggests incorporating factual consistency metrics.\n\n---\n\n### PROVENANCE/ATTRIBUTION (related problem, different angle)\n\n#### 10. Unknown Aware AI-Generated Content Attribution\n- **arXiv:** 2601.00218 | **Date:** Jan 2026\n- **Summary:** Attribution framework handling unknown generators. Assigns content to known models or flags as unknown.\n- **Relation:** They solve \"which model?\" — we solve \"how many iterations?\" Complementary problems. Their open-set recognition approach could inform how we handle unknown base models.\n\n#### 11. Explainable Disentangled Representation for Authorship Attribution in the Era of GenAI\n- **arXiv:** 2604.21300 | **Date:** Apr 2026\n- **Summary:** Disentangled representations for authorship attribution across human and AI authors.\n- **Relation:** Authorship attribution at the model level is adjacent to depth attribution. Their disentanglement framework could extend to depth as an additional latent factor.\n\n#### 12. A Faceted Proposal for Transparent Attribution of AI-Assisted Text\n- **arXiv:** 2604.25346 | **Date:** Apr 2026\n- **Summary:** Multi-faceted attribution model covering Form, Generation, Evaluation, Intent, Control, Traceability.\n- **Relation:** Their \"Traceability\" facet is closest to our depth problem. Their framework could position our work as solving one specific facet of a broader attribution problem.\n\n---\n\n### EVALUATION (benchmarks/methods)\n\n#### 13. Interpretable Predictability-Based AI Text Detection: A Replication Study\n- **arXiv:** 2603.15034 | **Date:** Mar 2026\n- **Summary:** Replicates and extends predictability-based detection systems from AuTexTification 2023.\n- **Relation:** Provides a reproducibility baseline for predictability-based methods. Useful for sanity-checking our feature pipeline.\n\n---\n\n## Key Takeaways for the Project\n\n1. **No competitor for depth regression.** Binary detection (human vs. AI) and source attribution (which model) are crowded. Ordinal depth estimation remains novel.\n\n2. **DivEye's surprisal features are the closest method overlap.** Ensure we cite it properly and demonstrate that our depth-regression features go beyond their binary classification features.\n\n3. **Model collapse theory now shows non-monotonic dynamics** (paper #5). Our depth signal may not increase linearly — important for regression model design (consider non-linear targets).\n\n4. **Curated/diverse recursive training weakens depth signal** (papers #7, #8). This should be discussed as a limitation and tested as a hard case.\n\n5. **Factual degradation > stylistic degradation as depth signal** (paper #9). Consider adding factual consistency features beyond perplexity/surprisal.\n\n6. **Detection features are domain-fragile** (paper #4). Cross-domain evaluation is essential for credibility.\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T02:05:13.790844+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T02:05:13.791074+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T02:05:13.791293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T02:05:13.791475+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T02:05:13.792451+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T02:05:13.792650+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/manifest.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/manifest.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T02:05:13.792812+00:00_

artifacts/manifest.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T02:05:13.793022+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T02:05:13.793312+00:00_

1	- id: art_20260514_005bbe
2	  name: atlas_analysis_scripts
3	  type: intermediate
4	  description: Atlas 分析脚本套件，dry-run 验证通过。多模型分析等各 pipeline 完成后启用。
5	  path: projects/recursive_gen_depth_est/artifacts/_project/intermediate/atlas_analysis_readme.md
6	  url: null
7	  project: recursive_gen_depth_est
8	  exp_id: null
9	  skill: ''
10	  created_at: '2026-05-14T16:14:36.739250+00:00'
11	  tags:
12	  - atlas
13	  - analysis
14	  - visualization
15	- id: art_20260514_3a51b7
16	  name: dcol_feature_based_train
17	  type: intermediate
18	  description: Feature-based DCOL 训练框架 (plan_004)。19维特征输入，N-pair contrastive loss
19	    + CE，dry-run 2 epoch 73.9% acc。
20	  path: projects/recursive_gen_depth_est/artifacts/_project/intermediate/dcol_feature_based_readme.md
21	  url: null
22	  project: recursive_gen_depth_est
23	  exp_id: null
24	  skill: ''
25	  created_at: '2026-05-14T16:24:14.366830+00:00'
26	  tags:
27	  - dcol
28	  - training
29	  - plan_004
30	- id: art_20260514_9b5f1e
31	  name: dcol_e2e_deberta_code
32	  type: intermediate
33	  description: End-to-end DeBERTa DCOL 训练框架 (plan_008 预研)。dcol_dataset.py + dcol_trainer.py
34	    + dcol_eval.py + run_dcol_training.sh，共 1199 行。Dry-run 通过。
35	  path: projects/recursive_gen_depth_est/artifacts/_project/intermediate/dcol_e2e_deberta_readme.md
36	  url: null
37	  project: recursive_gen_depth_est
38	  exp_id: null
39	  skill: ''
40	  created_at: '2026-05-14T16:31:55.628522+00:00'
41	  tags:
42	  - dcol
43	  - deberta
44	  - plan_008
45	- id: art_20260514_11e780
46	  name: baseline_battery_code
47	  type: intermediate
48	  description: 5 个 baseline 评估脚本 (plan_009)：PPL regression / CE-MLP / CORAL / DivEye
49	    / RF。Dry-run 全部通过，结果保存在 results/baselines/。
50	  path: projects/recursive_gen_depth_est/artifacts/_project/intermediate/baseline_battery_readme.md
51	  url: null
52	  project: recursive_gen_depth_est
53	  exp_id: null
54	  skill: ''
55	  created_at: '2026-05-14T16:33:26.656420+00:00'
56	  tags:
57	  - baseline
58	  - e
…[truncated 7931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T02:05:13.793576+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml",
  "old_string": "  - atlas\n  - v2\n  - results",
  "new_string": "  - atlas\n  - v2\n  - results\n- id: art_20260515_lit_scan\n  name: literature_scan_20260515\n  type: report\n  description: 'Literature scan 2026 Jan-May: 13 papers surveyed, no direct competitor\n    found for recursive depth estimation. Key findings on DivEye features, non-monotonic\n    collapse dynamics, domain fragility of detection features.'\n  path: projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md\n  url: null\n  project: recursive_gen_depth_est\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-15T12:00:00.000000+00:00'\n  tags:\n  - literature\n  - survey\n  - 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml",
    "old_string": "  - atlas\n  - v2\n  - results",
    "new_string": "  - atlas\n  - v2\n  - results\n- id: art_20260515_lit_scan\n  name: literature_scan_20260515\n  type: report\n  description: 'Literature scan 2026 Jan-May: 13 papers surveyed, no direct competitor\n    found for recursive depth estimation. Key findings on DivEye features, non-monotonic\n    collapse dynamics, domain fragility of detection features.'\n  path: projects/recursive_gen_depth_est/artifacts/literature_scan_20260515.md\n  url: null\n  project: recursive_gen_depth_est\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-15T12:00:00.000000+00:00'\n  tags:\n  - literature\n  - survey\n  - 2026"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T02:05:13.793844+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-research_20260515T020141",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T02:05:13.794121+00:00_

文献扫描完成。报告已写入 `artifacts/literature_scan_20260515.md`。

核心结论：

1. **无直接竞争者。** 没有人在做"递归生成深度/代数检测"。二分类检测（human vs AI）和来源归因（哪个模型）很拥挤，但序数深度回归仍是空白。

2. **最相关的方法工作：**
   - **DivEye** (TMLR/ICLR 2026) — surprisal 多样性特征，与我们的特征空间高度重叠，应作为 baseline 引用
   - **Breaking the Generator Barrier** (Apr 2026) — generator-agnostic 检测思路，可借鉴其解耦框架
   - **Why Detection Fails** (Mar 2026) — 检测特征在 domain shift 下严重退化，**对我们是重要警示**

3. **模型坍塌理论的新进展：**
   - **From Collapse to Improvement** (Feb 2026) — 混合真实数据时，迭代训练可以改善而非退化，意味着我们的深度信号可能**非单调**
   - **Curated Synthetic Data Doesn't Collapse** (May 2026) — 精心 curate 的递归训练不坍塌，这是我们方法的 hard case

4. **Knowledge Collapse** (Sep 2025) 指出表面流畅度在各深度保持不变，事实准确性才退化 — 建议考虑加入事实一致性特征。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper-research_20260515T020141"
}
```

</details>

---
