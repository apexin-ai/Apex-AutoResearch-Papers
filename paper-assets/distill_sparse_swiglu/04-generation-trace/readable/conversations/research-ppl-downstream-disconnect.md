# research ppl downstream disconnect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_ppl-downstream-disconnect_20260516T015921.jsonl`
- **Structured JSON:** [`aedf780e446bb7399a57.json`](../../sessions/ae/aedf780e446bb7399a57.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T01:59:50.789084+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T01:59:50.789584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T01:59:50.789897+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "perplexity downstream accuracy gap LLM pruning sparsity misleading metric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "tool_args": {
    "query": "perplexity downstream accuracy gap LLM pruning sparsity misleading metric"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T01:59:50.790148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM pruning downstream task degradation perplexity does not predict benchmark performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM pruning downstream task degradation perplexity does not predict benchmark performance"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T01:59:50.790371+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "tool_args": {
    "query": "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T01:59:50.790586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured pruning LLM perplexity proxy metric limitation arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structured pruning LLM perplexity proxy metric limitation arXiv 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T01:59:50.790871+00:00_

Web search results for query: "perplexity downstream accuracy gap LLM pruning sparsity misleading metric"

Links: [{"title":"UniPruning: Unifying Local Metric and Global Feedback for Scalable Sparse LLMs","url":"https://arxiv.org/html/2510.03291"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"Perplexity for LLM Evaluation - Comet","url":"https://www.comet.com/site/blog/perplexity-for-llm-evaluation/"},{"title":"SoLA: Leveraging Soft Activation Sparsity and Low-Rank Decomposition for Large Language Model Compression","url":"https://arxiv.org/html/2604.03258"},{"title":"Towards Extreme Pruning of LLMs with Plug-and-Play Mixed Sparsity","url":"https://arxiv.org/html/2503.11164"},{"title":"Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models","url":"https://arxiv.org/html/2405.20541v1"},{"title":"PERPLEXITY-BASED PRUNING WITH SMALL ...","url":"https://openreview.net/pdf?id=wNseMYxwpq"},{"title":"Perplexity for LLM Evaluation - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/perplexity-for-llm-evaluation/"},{"title":"Efficient Post-Training Pruning of Large Language Models with Statistical Correction","url":"https://arxiv.org/html/2602.07375v1"},{"title":"FASP: Fast and Accurate Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2501.09412"}]

Based on the search results, I found relevant research on the gap between perplexity and downstream accuracy metrics in LLM pruning and sparsity:

## Key Finding

Test set perplexity can be a misleading metric for evaluating the efficacy of data pruning techniques, as interventions that result in significantly higher test set perplexity can still achieve better performance on downstream tasks.

This insight comes from research titled "Perplexed by Perplexity: Perplexity-Based Data Pruning With Small Reference Models," which specifically investigates the disconnect between upstream (perplexity)
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T01:59:50.793374+00:00_

Web search results for query: "LLM pruning downstream task degradation perplexity does not predict benchmark performance"

Links: [{"title":"Frustratingly Easy Task-aware Pruning for Large Language Models","url":"https://arxiv.org/html/2510.22489"},{"title":"When Less is More: Investigating Data Pruning for Pretraining LLMs at Scale","url":"https://openreview.net/pdf?id=XUIYn3jo5T"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/html/2601.09694"},{"title":"Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning","url":"https://arxiv.org/html/2501.14315v2"},{"title":"Is my model perplexed for the right reason? Contrasting LLMs’ Benchmark Behavior with Token-Level Perplexity","url":"https://arxiv.org/html/2603.29396v1"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"DRPruning: Efficient Large Language Model Pruning through Distributionally Robust Optimization","url":"https://arxiv.org/html/2411.14055v1"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"Evaluating the Impact of Compression Techniques on Task-Specific Performance of Large Language Models","url":"https://arxiv.org/html/2409.11233"},{"title":"Multi-dimensional Safety Evaluation of LLM Compression","url":"https://aclanthology.org/2024.findings-emnlp.901.pdf"}]

I found several highly relevant research papers on this topic. Here are the key findings:

## Main Findings

Structured pruning methods experience near-total collapse in factual question-answering performance, with N:M sparsity patterns losing over 97% accuracy on knowledge-intensive tasks even at modest sparsity ratios (25-30%), despite negligible perplexity increases. This disconnect between perplexity and actual task performance underscores the inadequacy of current evaluation metrics and pruning strategies.

W
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T01:59:50.793732+00:00_

Web search results for query: "activation sparsity SwiGLU neuron pruning downstream evaluation catastrophic"

Links: [{"title":"TRAINING-FREE ACTIVATION SPARSITY IN LARGE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf"},{"title":"Post-Training Statistical Calibration for Higher Activation Sparsity","url":"https://arxiv.org/html/2412.07174"},{"title":"SwiGLU Activation in Transformer Models","url":"https://www.emergentmind.com/topics/swiglu-activation"},{"title":"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters","url":"https://arxiv.org/pdf/2406.05955"},{"title":"training-free activation sparsity in large language models","url":"https://www.arxiv.org/pdf/2408.14690"},{"title":"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models","url":"https://arxiv.org/html/2512.12744"},{"title":"First Activations Matter: Training-Free Methods for Dynamic Activation in Large Language Models","url":"https://arxiv.org/html/2408.11393v1"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"Activation Sparsity Opportunities for Compressing General Large Language Models","url":"https://arxiv.org/pdf/2412.12178"},{"title":"Efficient Activation Functions for Sparse LLMs","url":"https://www.emergentmind.com/topics/efficient-activation-functions-for-sparse-llms"}]

I found several relevant research papers on activation sparsity, SwiGLU, neuron pruning, and downstream evaluation. Here's what the search revealed:

## Key Research Findings:

**Activation Sparsity in SwiGLU Models:**

The CATS method enables training-free activation sparsity on SwiGLU-based LLMs by applying magnitude pruning on the output of Wgate, and achieves up to 50% sparsity in Wup and Wdown for Mistral and Llama-2-7B.

However, SwiGLU demonstrates n
…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ppl-downstream-disconnect_20260516T015921",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---
