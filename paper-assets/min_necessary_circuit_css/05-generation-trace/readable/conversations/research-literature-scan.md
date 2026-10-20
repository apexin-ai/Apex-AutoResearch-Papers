# research literature scan

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_research_literature-scan_20260512T230501.jsonl`
- **Structured JSON:** [`370a835bbc9cdfa2b41c.json`](../../sessions/37/370a835bbc9cdfa2b41c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-12T23:09:04.569462+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T23:09:04.569827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T23:09:04.570026+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-12T23:09:04.570167+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T23:09:04.570290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"circuit discovery\" AND (\"consensus\" OR \"ensemble\" OR \"aggregation\" OR \"multi-method\") arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"circuit discovery\" AND (\"consensus\" OR \"ensemble\" OR \"aggregation\" OR \"multi-method\") arXiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T23:09:04.570409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"mechanistic interpretability\" AND (\"stability\" OR \"robustness\" OR \"cross-method\") arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"mechanistic interpretability\" AND (\"stability\" OR \"robustness\" OR \"cross-method\") arXiv 2026"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T23:09:04.570522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS circuit discovery arXiv 2603.00523 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS circuit discovery arXiv 2603.00523 2026"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T23:09:04.570632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"edge pruning\" circuit mechanistic interpretability 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"edge pruning\" circuit mechanistic interpretability 2026 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T23:09:04.570794+00:00_

Web search results for query: ""circuit discovery" AND ("consensus" OR "ensemble" OR "aggregation" OR "multi-method") arXiv 2026"

Links: [{"title":"Consensus learning: A novel decentralised ensemble learning paradigm","url":"https://arxiv.org/html/2402.16157"},{"title":"Adaptive Consensus Gradients Aggregation for Scaled Distributed Training","url":"https://arxiv.org/html/2411.03742v1"},{"title":"Convergence Speed in Distributed Consensus and Averaging | SIAM Journal on Control and Optimization","url":"https://epubs.siam.org/doi/10.1137/060678324"},{"title":"A Survey on Consensus Algorithms of Blockchain Based on DAG","url":"https://dl.acm.org/doi/fullHtml/10.1145/3688225.3688232"},{"title":"Machine Learning Nov 2024","url":"https://arxiv.org/list/cs.LG/2024-11?skip=0&show=2000"},{"title":"Artificial Intelligence Jul 2025","url":"https://arxiv.org/list/cs.AI/2025-07?skip=2325&show=2000"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=450&show=2000"},{"title":"Consensus-based Recursive Multi-Output Gaussian Process","url":"https://arxiv.org/html/2604.10146v1"},{"title":"[2408.05446] Ensemble everything everywhere: Multi-scale aggregation for adversarial robustness","url":"https://arxiv.org/abs/2408.05446"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=200&show=1000"}]

Based on my search results, I found several papers related to consensus, ensemble methods, and aggregation approaches, though I did not find papers specifically about "circuit discovery" combined with these terms on arXiv from 2026.

The search returned relevant papers on related topics:

1. **Consensus Learning**: A decentralized ensemble learning paradigm where participants exchange predictions and update them using a local aggregation function, governed by a consensus protocol aiming to guide the network towards a common output.

2. **Consensus-based Approaches**: A Consensus Recursive Multi-Output Gaussian Process (CRMG
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T23:09:04.570979+00:00_

Web search results for query: ""mechanistic interpretability" AND ("stability" OR "robustness" OR "cross-method") arXiv 2026"

Links: [{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/html/2602.11180v1"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v1"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models","url":"https://arxiv.org/html/2502.17516v1"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks","url":"https://arxiv.org/html/2511.19265v1"},{"title":"[2602.11180] Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/abs/2602.11180"}]

Based on the search results, here are several recent arXiv papers (2026) on mechanistic interpretability addressing stability, robustness, and cross-method concerns:

## Key Papers Found

### 1. **Certified Circuits: Stability Guarantees for Mechanistic Circuits**
This work introduces Certified Circuits, a framework providing provable stability guarantees for circuit discovery by combining deletion-based randomized smoothing with per-neuron abstention, certifying that 
…[truncated 1641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T23:09:04.571150+00:00_

Web search results for query: "CIRCUS circuit discovery arXiv 2603.00523 2026"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Automatic Discovery of Visual Circuits","url":"https://arxiv.org/html/2404.14349v1"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations | OpenReview","url":"https://openreview.net/forum?id=2Jyb1yu3nN"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"}]

Based on the search results, here's information about the CIRCUS paper (arXiv 2603.00523):

CIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.

Mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle "on
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T23:09:04.571317+00:00_

Web search results for query: ""edge pruning" circuit mechanistic interpretability 2026 arXiv"

Links: [{"title":"Prune, Interpret, Evaluate (PIE ): A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution","url":"https://arxiv.org/html/2604.16889"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/html/2602.11180v1"},{"title":"Multi-Granular Node Pruning for Circuit Discovery","url":"https://arxiv.org/html/2512.10903"},{"title":"Finding Transformer Circuits with Edge Pruning","url":"https://arxiv.org/html/2406.16778v1"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG","url":"https://arxiv.org/html/2510.00845v2"},{"title":"[2510.03282] Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/abs/2510.03282"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://ar5iv.labs.arxiv.org/html/2304.14997"},{"title":"Finding Transformer Circuits With Edge Pruning | OpenReview","url":"https://openreview.net/forum?id=8oSY3rA9jY"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"}]

Based on the search results, I found several recent arXiv papers on edge pruning and circuit mechanistic interpretability from 2025-2026:

## Key Papers Found:

1. **PIE Framework (2026)** - Prune, Interpret, Evaluate (PIE), a CLT-native framework designed to resolve the efficiency bottleneck in mechanistic interpretability. The framework identifies sparse subsets of Cross-Layer Transcoder (CLT) features causally relevant to a task by pruning, allowing interpretation budgets to be allocated where th
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T23:09:04.571490+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.22968 \"Certified Circuits\" stability guarantees mechanistic circuits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.22968 \"Certified Circuits\" stability guarantees mechanistic circuits"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T23:09:04.571610+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.16823 \"Formal Mechanistic Interpretability\" automated circuit discovery provable guarantees"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.16823 \"Formal Mechanistic Interpretability\" automated circuit discovery provable guarantees"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T23:09:04.571745+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.16889 PIE \"cross-layer transcoder\" circuit discovery pruning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.16889 PIE \"cross-layer transcoder\" circuit discovery pruning 2026"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T23:09:04.571868+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"cross-method\" OR \"multi-method\" circuit discovery interpretability combining methods 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"cross-method\" OR \"multi-method\" circuit discovery interpretability combining methods 2026"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T23:09:04.571981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mondorf \"edge attribution patching\" \"edge pruning\" circuit combination BlackboxNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mondorf \"edge attribution patching\" \"edge pruning\" circuit combination BlackboxNLP 2025"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T23:09:04.572116+00:00_

Web search results for query: "arXiv 2602.16823 "Formal Mechanistic Interpretability" automated circuit discovery provable guarantees"

Links: [{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823"},{"title":"(PDF) Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://www.researchgate.net/publication/400970365_Formal_Mechanistic_Interpretability_Automated_Circuit_Discovery_with_Provable_Guarantees"},{"title":"Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/pdf/2602.16823"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"[PDF] Towards Automated Circuit Discovery for Mechanistic Interpretability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Automated-Circuit-Discovery-for-Mechanistic-Conmy-Mavor-Parker/eefbd8b384a58f464827b19e30a6920ba976def9"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | FAR.AI","url":"https://www.far.ai/research/towards-automated-circuit-discovery-for-mechanistic-interpretability"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Paper-Conference.pdf"}]

I found the paper you're searching for! Here's the informati
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T23:09:04.572294+00:00_

Web search results for query: "arXiv 2604.16889 PIE "cross-layer transcoder" circuit discovery pruning 2026"

Links: [{"title":"[2604.16889] Prune, Interpret, Evaluate: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution","url":"https://arxiv.org/abs/2604.16889"},{"title":"Prune, Interpret, Evaluate (PIE ): A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution","url":"https://arxiv.org/html/2604.16889"},{"title":"Transcoders Find Interpretable LLM Feature Circuits","url":"https://arxiv.org/html/2406.11944v1"},{"title":"Functional Faithfulness in the Wild: Circuit Discovery with Differentiable Computation Graph Pruning","url":"https://arxiv.org/html/2407.03779v1/"},{"title":"Transcoders Find Interpretable LLM Feature Circuits Jacob Dunefsky∗","url":"https://arxiv.org/pdf/2406.11944"},{"title":"Multi-Granular Node Pruning for Circuit Discovery","url":"https://arxiv.org/html/2512.10903"},{"title":"Attribution-Guided Pruning for Insight and Control: Circuit Discovery and Targeted Correction in Small-scale LLMs","url":"https://arxiv.org/html/2506.13727"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"[2512.10903] Multi-Granular Node Pruning for Circuit Discovery","url":"https://arxiv.org/abs/2512.10903"},{"title":"Protein Circuit Tracing via Cross-layer Transcoders","url":"https://arxiv.org/html/2602.12026v1"}]

Based on the search results, I found the paper you're looking for:

The paper introduces PIE, the first CLT-native end-to-end framework connecting Pruning, automatic Interpretation, and interpretation Evaluation, enabling systematic measurement of behavioral fidelity and downstream interpretability under pruning. 

The paper addresses the fact that existing feature-interpretation pipelines typically operate on uniformly sampled units, but only a small fract
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T23:09:04.572462+00:00_

Web search results for query: "arXiv 2602.22968 "Certified Circuits" stability guarantees mechanistic circuits"

Links: [{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"[2602.22968] Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/abs/2602.22968"},{"title":"AI Research Roundup: Agent Behavioral Contracts, Autonomous Memory, and Certified Circuits | Awesome Agents","url":"https://awesomeagents.ai/science/agent-contracts-autonomous-memory-certified-circuits/"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731v1"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"}]

Based on the search results, here's what I found about arXiv paper 2602.22968:

## Certified Circuits: Stability Guarantees for Mechanistic Circuits

Certified Circuits provide provable stability guarantees for circuit discovery. The framework wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component inclusion decisions are invariant to bounded edit-distance perturbations of the concept d
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T23:09:04.572622+00:00_

Web search results for query: ""cross-method" OR "multi-method" circuit discovery interpretability combining methods 2026"

Links: [{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936v2"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"SCALABLE CIRCUIT LEARNING FOR INTERPRETING LARGE ...","url":"https://openreview.net/pdf/5ce96be0d1afcc4c78a52d8749cd9c6efe17852a.pdf"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"ICLR Poster Circuit Insights: Towards Interpretability Beyond Activations","url":"https://iclr.cc/virtual/2026/poster/10011755"},{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"}]

I found several relevant results on circuit discovery and interpretability methods from 2026. Here are the key findings:

## Recent Developments in Circuit Discovery Methods

Recent work proposes WeightLens and CircuitLens, two complementary methods that go beyond activation-based analysis. CircuitLens captures how feature activations arise from interact
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T23:09:04.572822+00:00_

Web search results for query: "Mondorf "edge attribution patching" "edge pruning" circuit combination BlackboxNLP 2025"

Links: [{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.31/"},{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/accepted_papers/"},{"title":"[PDF] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BlackboxNLP-2025-MIB-Shared-Task:-Exploring-for-Mondorf-Wang/6de77c59381b74de6e6f554c3f6e12690d6628e8"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP (2025) - ACL Anthology","url":"https://aclanthology.org/events/blackboxnlp-2025/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/html/2510.25786"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"}]

I found search results for the Mondorf et al. paper on ensemble strategies for circuit localization at BlackboxNLP 2025. Here's w
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T23:09:04.572995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.24731 \"circuit stability\" \"language model generalization\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.24731 \"circuit stability\" \"language model generalization\" 2026"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-12T23:09:04.573119+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.16740 \"attention-head stability\" \"circuit universality\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.16740 \"attention-head stability\" \"circuit universality\" 2026"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T23:09:04.573233+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS \"stability ensembles\" circuit consensus follow-up v2 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS \"stability ensembles\" circuit consensus follow-up v2 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T23:09:04.573374+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"circuit discovery\" \"agreement\" OR \"concordance\" OR \"voting\" interpretability methods 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"circuit discovery\" \"agreement\" OR \"concordance\" OR \"voting\" interpretability methods 2026 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T23:09:04.573529+00:00_

Web search results for query: "arXiv 2505.24731 "circuit stability" "language model generalization" 2026"

Links: [{"title":"[2505.24731] Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/abs/2505.24731"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"Circuit Stability Characterizes Language Model ...","url":"https://arxiv.org/pdf/2505.24731"},{"title":"Circuit Stability Characterizes Language Model ...","url":"https://aclanthology.org/2025.acl-long.442.pdf"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=2050&show=2000"},{"title":"GitHub - alansun17904/circuit-stability: [ACL '25] Circuit Stability Characterizes Language Model Generalization","url":"https://github.com/alansun17904/circuit-stability"},{"title":"Circuit Stability Characterizes Language Model Generalization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.442/"},{"title":"Algorithmic Phase Transitions in Language Models:","url":"https://arxiv.org/pdf/2412.07386"},{"title":"LLM Circuit Analyses Are Consistent Across Training and Scale Curt Tigges","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf"},{"title":"Algorithmic Phase Transitions in Language Models: A Mechanistic Case Study of Arithmetic","url":"https://arxiv.org/html/2412.07386v1"}]

I found the paper! Here are the search results for arXiv 2505.24731:

## Paper Overview

"Circuit Stability Characterizes Language Model Generalization" is authored by Alan Sun and was submitted on May 30, 2025.

## Key Concept

Circuit stability refers to a model's ability to apply a consistent reasoning process—its circuit—across various inputs. The paper introduces circuit stability as a new way to assess model performance, inspired by recent developments in mechanistic interpretability.

## Main Contributions

Th
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T23:09:04.573690+00:00_

Web search results for query: "CIRCUS "stability ensembles" circuit consensus follow-up v2 2026"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Solana announces their next event will follow Consensus ...","url":"https://www.facebook.com/coindesk/posts/solana-announces-their-next-event-will-follow-consensus-2026-from-hong-kong-to-m/1362409929258089/"},{"title":"Generalized String-Stability Criteria for Consensus Protocols","url":"https://arxiv.org/html/2604.21329v1"},{"title":"Fixed-time leader-following speed consensus control for multi-PMSMs based on multi-agent systems consensus | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-18061-3"},{"title":"Model-free adaptive consensus design for a class of unknown heterogeneous nonlinear multi-agent systems with packet dropouts | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-73959-8"},{"title":"Machine Learning Nov 2024","url":"https://arxiv.org/list/cs.LG/2024-11?skip=0&show=2000"},{"title":"Regional consensus of switched positive multi-agent systems with multiple equilibria | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-86296-1"},{"title":"Log in to EasyChair for ICCS 2026","url":"https://easychair.org/account/signin?l=79040894748625862.1778459738.1a191881"},{"title":"2026 IEEE International Symposium on Circuits and Systems | IEEE CASS","url":"https://ieee-cas.org/event/conference/2026-ieee-international-symposium-circuits-and-systems"}]

I found relevant results for your search query. The top results are about the CIRCUS paper:

CIRCUS addresses the problem that mechanistic circuit discovery is sensitive to arbitrary analyst choices, and reframes it as an uncertainty-quantification problem. The method constructs an ensembl
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T23:09:04.573885+00:00_

Web search results for query: ""circuit discovery" "agreement" OR "concordance" OR "voting" interpretability methods 2026 arXiv"

Links: [{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/html/2510.14936v2"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees | OpenReview","url":"https://openreview.net/forum?id=Timsb74vIY"},{"title":"The Computational Complexity of Circuit Discovery for Inner Interpretability","url":"https://arxiv.org/html/2410.08025"},{"title":"[2510.14936] Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/abs/2510.14936"},{"title":"SCALABLE CIRCUIT LEARNING FOR INTERPRETING LARGE ...","url":"https://openreview.net/pdf/5ce96be0d1afcc4c78a52d8749cd9c6efe17852a.pdf"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/html/2601.14004v1"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"}]

Based on the web search results, I found several relevant papers on circuit discovery and interpretability methods from 2026 on arXiv:

## Key 2026 Papers on Circuit Discovery

**1. Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees**
Automated circuit discovery is a central tool in mechanistic interpretability for identifying the internal components of neural ne
…[truncated 1434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T23:09:04.574065+00:00_

Web search results for query: "arXiv 2602.16740 "attention-head stability" "circuit universality" 2026"

Links: [{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"[2602.16740] Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/abs/2602.16740"},{"title":"Machine Learning arXiv on X: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok https://t.co/NymJkSIUw6 [𝚌𝚜.𝙻𝙶 𝚌𝚜.𝙰𝙸] https://t.co/JAcAQlIyVg\" / X","url":"https://x.com/Memoirs/status/2027962347445239968/photo/1"},{"title":"[2602.18849] Exact Attention Sensitivity and the Geometry of Transformer Stability","url":"https://arxiv.org/abs/2602.18849"},{"title":"Inferring Functionality of Attention Heads from their Parameters","url":"https://arxiv.org/html/2412.11965v1"},{"title":"Exact Attention Sensitivity and the Geometry of Transformer Stability","url":"https://arxiv.org/html/2602.18849"},{"title":"Selective Synchronization Attention","url":"https://arxiv.org/html/2602.14445"},{"title":"Attention Mechanisms in Neural Networks A Comprehensive Mathematical Treatment From Theory to Implementation","url":"https://arxiv.org/html/2601.03329v1"},{"title":"Which Attention Heads Matter for In-Context Learning?","url":"https://arxiv.org/html/2502.14010v1"},{"title":"Attention is All You Need: A Paradigm Shift in Natural ...","url":"https://www.linkedin.com/pulse/attention-all-you-need-paradigm-shift-natural-anil-a-kuriakose-acdsc"}]

I found the arXiv paper 2602.16740 for you. Here's what I found:

## Paper Overview

The paper is titled "Quantifying LLM Attention-Head Stability: Implications for Circuit Universality" by Karan Bali, Jack Stanley, Praneet Suresh, and Danilo Bzdok, and was submitted on February 17, 2026.

## Main Research Question

The paper addresses a concern in mechanistic interp
…[truncated 1340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T23:09:04.574263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BlackboxNLP 2025 MIB shared task circuit localization entries results combining methods"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BlackboxNLP 2025 MIB shared task circuit localization entries results combining methods"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T23:09:04.574390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GIM \"gradient interaction\" mechanistic interpretability benchmark circuit discovery 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GIM \"gradient interaction\" mechanistic interpretability benchmark circuit discovery 2026 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T23:09:04.574540+00:00_

Web search results for query: "BlackboxNLP 2025 MIB shared task circuit localization entries results combining methods"

Links: [{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"[2511.18409] Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/abs/2511.18409"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.31/"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"BlackboxNLP 2025","url":"https://blackboxnlp.github.io/2025/"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.32/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"},{"title":"[PDF] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BlackboxNLP-2025-MIB-Shared-Task:-Exploring-for-Mondorf-Wang/6de77c59381b74de6e6f554c3f6e12690d6628e8"}]

Based on the search results, here's what I found about the BlackboxNLP 2025 MIB shared task circuit localizati
…[truncated 1465 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T23:09:04.574731+00:00_

Web search results for query: "GIM "gradient interaction" mechanistic interpretability benchmark circuit discovery 2026 arXiv"

Links: [{"title":"Corti introduces GIM: Benchmark-leading method for understanding AI model behavior | Corti","url":"https://www.corti.ai/stories/gim-a-new-standard-for-mechanistic-interpretability"},{"title":"GIM: Improved Interpretability for Large Language Models","url":"https://arxiv.org/html/2505.17630"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis","url":"https://arxiv.org/html/2510.00845"},{"title":"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification","url":"https://arxiv.org/html/2502.06852v1"},{"title":"InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques","url":"https://arxiv.org/html/2407.14494v1"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"}]

Based on the search results, I found relevant information about GIM (Gradient Interaction Modifications) and mechanistic interpretability:

## Key Findings

**GIM (Gradient Interaction Modifications):** GIM is a gradient-based method that achieves the highest known accuracy for identifying which components in a model are responsible for specific behaviors. As of today, this is the w
…[truncated 1223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T23:09:04.574899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2511.18409 \"Findings BlackboxNLP 2025 shared task\" circuit localization methods teams"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2511.18409 \"Findings BlackboxNLP 2025 shared task\" circuit localization methods teams"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-12T23:09:04.575019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.25786 \"Improving Circuit Faithfulness\" \"Better Edge Selection\" BlackboxNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.25786 \"Improving Circuit Faithfulness\" \"Better Edge Selection\" BlackboxNLP"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-12T23:09:04.575162+00:00_

Web search results for query: "arXiv 2511.18409 "Findings BlackboxNLP 2025 shared task" circuit localization methods teams"

Links: [{"title":"[2511.18409] Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/abs/2511.18409"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Request PDF","url":"https://www.researchgate.net/publication/397423880_BlackboxNLP-2025_MIB_Shared_Task_Exploring_Ensemble_Strategies_for_Circuit_Localization_Methods"},{"title":"[2510.06811] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/abs/2510.06811"},{"title":"Findings of the BlackboxNLP 2025 Shared Task:","url":"https://www.arxiv.org/pdf/2511.18409"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"[PDF] BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BlackboxNLP-2025-MIB-Shared-Task:-Exploring-for-Mondorf-Wang/6de77c59381b74de6e6f554c3f6e12690d6628e8"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.31/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811v1"},{"title":"MCML - BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://mcml.ai/publications/mwg+25/"}]

Based on the search results for arXiv 2511.18409, here's what I found:

## Overview

The paper is titled 
…[truncated 1747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T23:09:04.575326+00:00_

Web search results for query: "arXiv 2510.25786 "Improving Circuit Faithfulness" "Better Edge Selection" BlackboxNLP"

Links: [{"title":"Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/pdf/2510.25786"},{"title":"[2510.25786] BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/abs/2510.25786"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/html/2510.25786"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409"},{"title":"Improving Circuit Faithfulness via Better Edge Selection","url":"https://aclanthology.org/2025.blackboxnlp-1.29.pdf"},{"title":"Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms","url":"https://arxiv.org/html/2403.17806v2"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection - ACL Anthology","url":"https://aclanthology.org/2025.blackboxnlp-1.29/"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://arxiv.org/html/2510.03282v1"},{"title":"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification","url":"https://arxiv.org/html/2502.06852v1"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811"}]

I found the paper! Here's information about arXiv 2510.25786:

## BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection

The paper addresses one of the main challenges in mechanistic interpretability: circuit discovery, which involves determining which parts of a model perform a given task.

### Key Contributions

The authors propose three key improvements to circuit discovery: Firs
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T23:09:04.575550+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "literature_map.yaml",
  "content": "# Literature Map — structfuse-context (cross-method circuit consensus)\n# Last updated: 2026-05-12\n\n- arxiv_id: \"2603.00523\"\n  title: \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\"\n  authors: \"Unknown (arXiv 2603.00523v2)\"\n  year: 2026\n  category: \"direct-competitor\"\n  role: \"Primary competitor — intra-method stability scoring\"\n  summary: >\n    Constructs ensemble of attribution graphs by pruning a single raw attribution\n    run under multiple threshold configurations. Assigns per-edge stability score\n    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.\n    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.\n    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).\n  relevance_to_css: >\n    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE\n    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask\n    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.\n    v2 update (2026-03-20) is same paper, no separate follow-up found.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.06811\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n  authors: \"Mondorf, Wang et al.\"\n  year: 2025\n  category: \"direct-competitor\"\n  role: \"Limited cross-method ensembling (EAP-IG + Edge Pruning)\"\n  summary: >\n    Explores parallel ensembling (averaging/min/max of attribution scores across methods)\n    and sequential ensembling (EAP-IG warm-start → Edge Pruning refinement).\n    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.\n    Workshop short paper at BlackboxNLP 2025.\n  relevance_to_css: >\n    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both\n    gradient-based edge attribution methods from the same algorithmic family.\n    No causal/mask-based methods included. Simple score aggregation (avg/min/max),\n    no principled consensus framework. CSS goes beyond by spanning algorithm families\n    and providing binary consensus with confidence scoring.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.22968\"\n  title: \"Certified Circuits: Stability Guarantees for Mechanistic Circuits\"\n  authors: \"Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Stability via data subsampling (complementary orthogonal axis)\"\n  summary: >\n    Wraps any black-box circuit discovery algorithm with randomized data subsampling\n    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component\n    inclusion is invariant to bounded dataset edit-distance perturbations. Certified\n    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.\n  relevance_to_css: >\n    Complementary: addresses data stability (same method, different data subsets).\n    CSS addresses method stability (same data, different algorithms). Could combine:\n    run CSS consensus then certify the consensus circuit's data-robustness.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16823\"\n  title: \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n  authors: \"Itamar Hadad, Guy Katz, Shahaf Bassan\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Formal verification for circuit discovery (ICLR 2026)\"\n  summary: >\n    Integrates neural network verification tools into circuit discovery. Provides\n    provable guarantees over continuous input domains: (i) input-domain robustness,\n    (ii) patching-domain robustness, (iii) family of minimality guarantees\n    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.\n  relevance_to_css: >\n    Orthogonal: provides theoretical guarantees for a single discovery method.\n    CSS is empirical cross-method consensus. Could use formal methods to verify\n    that CSS consensus circuits satisfy minimality/faithfulness properties.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2604.16889\"\n  title: \"PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\"\n  authors: \"Qinhao Chen, Linyang He, Nima Mesgarani\"\n  year: 2026\n  category: \"method-component\"\n  role: \"New circuit discovery method (CLT-native, could be input to CSS)\"\n  summary: >\n    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores\n    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware\n    reranking. Evaluated with KL-divergence behavior retention and FADE-style interpretation metrics.\n  relevance_to_css: >\n    Potential new method to include in CSS ensemble. As CLT/transcoder methods become\n    standard, CSS should demonstrate it can incorporate them alongside traditional\n    edge-level methods. Not a competitor.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16740\"\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  category: \"evaluation\"\n  role: \"Cross-seed stability analysis (motivates need for robust circuits)\"\n  summary: >\n    Quantifies attention head similarity across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models\n    show stronger mid-depth divergence. AdamW increases head stability for deeper models.\n  relevance_to_css: >\n    Motivational: shows circuits can be seed-dependent, strengthening the argument\n    that consensus across methods (not just seeds) is needed for robust circuit claims.\n    Citable as motivation in related work.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.00845\"\n  title: \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Statistical stability framework for circuit discovery\"\n  summary: >\n    Argues interpretability methods should be viewed as statistical estimators subject to\n    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits\n    are often reported without quantification of statistical stability or uncertainty.\n  relevance_to_css: >\n    Strong motivation paper for CSS. If a single method has high variance, cross-method\n    consensus provides a principled way to identify edges that are stable regardless of\n    estimation noise. Citable as framing/motivation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.25786\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\"\n  authors: \"Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Bootstrapping for edge consistency + ILP selection\"\n  summary: >\n    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,\n    (2) ratio-based selection for strong positive edges, (3) integer linear programming\n    formulation replacing greedy selection. Yields more faithful circuits on MIB.\n  relevance_to_css: >\n    Bootstrapping for intra-method edge consistency is related to CSS's stability concept\n    but limited to single method. The ILP selection idea could inspire CSS's consensus\n    aggregation mechanism.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.24731\"\n  title: \"Circuit Stability Characterizes Language Model Generalization\"\n  authors: \"Alan Sun\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Circuit stability predicts generalization (ACL 2025)\"\n  summary: >\n    Circuit stability = model applying consistent circuit across inputs. Through case studies\n    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional\n    generalization. Stability can be induced via chain-of-thought prompting.\n  relevance_to_css: >\n    Downstream application: if CSS consensus circuits are more stable (by construction),\n    they may better predict generalization. Potential evaluation angle for CSS paper.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2511.18409\"\n  title: \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n  authors: \"Shared Task Organizers\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Benchmark and evaluation framework for circuit localization\"\n  summary: >\n    Two tracks: circuit localization (causally influential components) and causal variable\n    localization (mapping activations to interpretable features). Three teams, eight methods.\n    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.\n  relevance_to_css: >\n    MIB benchmark could be used to evaluate CSS. The finding that ensembles help validates\n    the general direction. But no team did true cross-family consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.17630\"\n  title: \"GIM: Improved Interpretability for Large Language Models\"\n  authors: \"Corti team\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Top-performing gradient method on MIB benchmark\"\n  summary: >\n    Gradient Interaction Modifications — gradient-based circuit discovery method.\n    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods\n    in early layers; Integrated Gradients better in middle/late layers.\n  relevance_to_css: >\n    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance\n    differences across methods further motivates cross-method consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2502.06852\"\n  title: \"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Improved gradient-based circuit discovery (fixes EAP saturation)\"\n  summary: >\n    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient\n    propagation fix for more accurate edge importance scoring.\n  relevance_to_css: >\n    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows\n    intra-family variation — but CSS's value is cross-family agreement.\n  discovered_date: \"2026-05-12\"\n\n# ============================================================\n# NOVELTY ASSESSMENT (as of 2026-05-12)\n# ============================================================\n# No paper found that performs TRUE cross-method consensus spanning\n# different algorithm families (gradient-based vs mask-learning vs\n# causal intervention). Specifically:\n#\n# - CIRCUS: intra-method (threshold variation within single algorithm)\n# - Mondorf et al.: EAP-IG + EP (both gradient-family)\n# - Nikankin et al.: bootstrapping within single method\n# - Certified Circuits: data perturbation stability (single method)\n#\n# CSS's core novelty — binary consensus across algorithm families\n# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)\n# with principled cross-family agreement scoring — REMAINS UNCLAIMED.\n# ============================================================\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "literature_map.yaml",
    "content": "# Literature Map — structfuse-context (cross-method circuit consensus)\n# Last updated: 2026-05-12\n\n- arxiv_id: \"2603.00523\"\n  title: \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\"\n  authors: \"Unknown (arXiv 2603.00523v2)\"\n  year: 2026\n  category: \"direct-competitor\"\n  role: \"Primary competitor — intra-method stability scoring\"\n  summary: >\n    Constructs ensemble of attribution graphs by pruning a single raw attribution\n    run under multiple threshold configurations. Assigns per-edge stability score\n    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.\n    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.\n    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).\n  relevance_to_css: >\n    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE\n    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask\n    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.\n    v2 update (2026-03-20) is same paper, no separate follow-up found.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.06811\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n  authors: \"Mondorf, Wang et al.\"\n  year: 2025\n  category: \"direct-competitor\"\n  role: \"Limited cross-method ensembling (EAP-IG + Edge Pruning)\"\n  summary: >\n    Explores parallel ensembling (averaging/min/max of attribution scores across methods)\n    and sequential ensembling (EAP-IG warm-start → Edge Pruning refinement).\n    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.\n    Workshop short paper at BlackboxNLP 2025.\n  relevance_to_css: >\n    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both\n    gradient-based edge attribution methods from the same algorithmic family.\n    No causal/mask-based methods included. Simple score aggregation (avg/min/max),\n    no principled consensus framework. CSS goes beyond by spanning algorithm families\n    and providing binary consensus with confidence scoring.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.22968\"\n  title: \"Certified Circuits: Stability Guarantees for Mechanistic Circuits\"\n  authors: \"Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Stability via data subsampling (complementary orthogonal axis)\"\n  summary: >\n    Wraps any black-box circuit discovery algorithm with randomized data subsampling\n    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component\n    inclusion is invariant to bounded dataset edit-distance perturbations. Certified\n    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.\n  relevance_to_css: >\n    Complementary: addresses data stability (same method, different data subsets).\n    CSS addresses method stability (same data, different algorithms). Could combine:\n    run CSS consensus then certify the consensus circuit's data-robustness.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16823\"\n  title: \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n  authors: \"Itamar Hadad, Guy Katz, Shahaf Bassan\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Formal verification for circuit discovery (ICLR 2026)\"\n  summary: >\n    Integrates neural network verification tools into circuit discovery. Provides\n    provable guarantees over continuous input domains: (i) input-domain robustness,\n    (ii) patching-domain robustness, (iii) family of minimality guarantees\n    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.\n  relevance_to_css: >\n    Orthogonal: provides theoretical guarantees for a single discovery method.\n    CSS is empirical cross-method consensus. Could use formal methods to verify\n    that CSS consensus circuits satisfy minimality/faithfulness properties.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2604.16889\"\n  title: \"PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\"\n  authors: \"Qinhao Chen, Linyang He, Nima Mesgarani\"\n  year: 2026\n  category: \"method-component\"\n  role: \"New circuit discovery method (CLT-native, could be input to CSS)\"\n  summary: >\n    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores\n    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware\n    reranking. Evaluated with KL-divergence behavior retention and FADE-style interpretation metrics.\n  relevance_to_css: >\n    Potential new method to include in CSS ensemble. As CLT/transcoder methods become\n    standard, CSS should demonstrate it can incorporate them alongside traditional\n    edge-level methods. Not a competitor.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16740\"\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  category: \"evaluation\"\n  role: \"Cross-seed stability analysis (motivates need for robust circuits)\"\n  summary: >\n    Quantifies attention head similarity across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models\n    show stronger mid-depth divergence. AdamW increases head stability for deeper models.\n  relevance_to_css: >\n    Motivational: shows circuits can be seed-dependent, strengthening the argument\n    that consensus across methods (not just seeds) is needed for robust circuit claims.\n    Citable as motivation in related work.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.00845\"\n  title: \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Statistical stability framework for circuit discovery\"\n  summary: >\n    Argues interpretability methods should be viewed as statistical estimators subject to\n    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits\n    are often reported without quantification of statistical stability or uncertainty.\n  relevance_to_css: >\n    Strong motivation paper for CSS. If a single method has high variance, cross-method\n    consensus provides a principled way to identify edges that are stable regardless of\n    estimation noise. Citable as framing/motivation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.25786\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\"\n  authors: \"Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Bootstrapping for edge consistency + ILP selection\"\n  summary: >\n    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,\n    (2) ratio-based selection for strong positive edges, (3) integer linear programming\n    formulation replacing greedy selection. Yields more faithful circuits on MIB.\n  relevance_to_css: >\n    Bootstrapping for intra-method edge consistency is related to CSS's stability concept\n    but limited to single method. The ILP selection idea could inspire CSS's consensus\n    aggregation mechanism.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.24731\"\n  title: \"Circuit Stability Characterizes Language Model Generalization\"\n  authors: \"Alan Sun\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Circuit stability predicts generalization (ACL 2025)\"\n  summary: >\n    Circuit stability = model applying consistent circuit across inputs. Through case studies\n    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional\n    generalization. Stability can be induced via chain-of-thought prompting.\n  relevance_to_css: >\n    Downstream application: if CSS consensus circuits are more stable (by construction),\n    they may better predict generalization. Potential evaluation angle for CSS paper.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2511.18409\"\n  title: \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n  authors: \"Shared Task Organizers\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Benchmark and evaluation framework for circuit localization\"\n  summary: >\n    Two tracks: circuit localization (causally influential components) and causal variable\n    localization (mapping activations to interpretable features). Three teams, eight methods.\n    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.\n  relevance_to_css: >\n    MIB benchmark could be used to evaluate CSS. The finding that ensembles help validates\n    the general direction. But no team did true cross-family consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.17630\"\n  title: \"GIM: Improved Interpretability for Large Language Models\"\n  authors: \"Corti team\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Top-performing gradient method on MIB benchmark\"\n  summary: >\n    Gradient Interaction Modifications — gradient-based circuit discovery method.\n    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods\n    in early layers; Integrated Gradients better in middle/late layers.\n  relevance_to_css: >\n    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance\n    differences across methods further motivates cross-method consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2502.06852\"\n  title: \"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Improved gradient-based circuit discovery (fixes EAP saturation)\"\n  summary: >\n    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient\n    propagation fix for more accurate edge importance scoring.\n  relevance_to_css: >\n    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows\n    intra-family variation — but CSS's value is cross-family agreement.\n  discovered_date: \"2026-05-12\"\n\n# ============================================================\n# NOVELTY ASSESSMENT (as of 2026-05-12)\n# ============================================================\n# No paper found that performs TRUE cross-method consensus spanning\n# different algorithm families (gradient-based vs mask-learning vs\n# causal intervention). Specifically:\n#\n# - CIRCUS: intra-method (threshold variation within single algorithm)\n# - Mondorf et al.: EAP-IG + EP (both gradient-family)\n# - Nikankin et al.: bootstrapping within single method\n# - Certified Circuits: data perturbation stability (single method)\n#\n# CSS's core novelty — binary consensus across algorithm families\n# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)\n# with principled cross-family agreement scoring — REMAINS UNCLAIMED.\n# ============================================================\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T23:09:04.575826+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_map.yaml' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T23:09:04.575984+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T23:09:04.576109+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
logs
memory.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-12T23:09:04.576224+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T23:09:04.576339+00:00_

__pycache__
_project
analysis
analyze_mvp_results.py
css.py
deploy_phase2.sh
eap_ig_scoring.py
edge_pruning_scoring.py
ifr_scoring.py
manifest.yaml
model_adapter.py
mvp_status_report_20260512.md
phase2_configs.yaml
related_work_notes.md
run_circus.py
run_phase2_experiment.py
structfuse-mvp
test_css.py
test_eap_ig_scoring.py
test_edge_pruning_scoring.py
test_ifr_scoring.py
test_run_circus_fixes.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-12T23:09:04.576487+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml",
  "content": "# Literature Map — structfuse-context (cross-method circuit consensus)\n# Last updated: 2026-05-12\n\n- arxiv_id: \"2603.00523\"\n  title: \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\"\n  authors: \"Unknown (arXiv 2603.00523v2)\"\n  year: 2026\n  category: \"direct-competitor\"\n  role: \"Primary competitor — intra-method stability scoring\"\n  summary: >\n    Constructs ensemble of attribution graphs by pruning a single raw attribution\n    run under multiple threshold configurations. Assigns per-edge stability score\n    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.\n    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.\n    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).\n  relevance_to_css: >\n    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE\n    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask\n    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.\n    v2 update (2026-03-20) is same paper, no separate follow-up found.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.06811\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n  authors: \"Mondorf, Wang et al.\"\n  year: 2025\n  category: \"direct-competitor\"\n  role: \"Limited cross-method ensembling (EAP-IG + Edge Pruning)\"\n  summary: >\n    Explores parallel ensembling (averaging/min/max of attribution scores across methods)\n    and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement).\n    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.\n    Workshop short paper at BlackboxNLP 2025.\n  relevance_to_css: >\n    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both\n    gradient-based edge attribution methods from the same algorithmic family.\n    No causal/mask-based methods included. Simple score aggregation (avg/min/max),\n    no principled consensus framework. CSS goes beyond by spanning algorithm families\n    and providing binary consensus with confidence scoring.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.22968\"\n  title: \"Certified Circuits: Stability Guarantees for Mechanistic Circuits\"\n  authors: \"Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Stability via data subsampling (complementary orthogonal axis)\"\n  summary: >\n    Wraps any black-box circuit discovery algorithm with randomized data subsampling\n    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component\n    inclusion is invariant to bounded dataset edit-distance perturbations. Certified\n    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.\n  relevance_to_css: >\n    Complementary: addresses data stability (same method, different data subsets).\n    CSS addresses method stability (same data, different algorithms). Could combine:\n    run CSS consensus then certify the consensus circuit's data-robustness.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16823\"\n  title: \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n  authors: \"Itamar Hadad, Guy Katz, Shahaf Bassan\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Formal verification for circuit discovery (ICLR 2026)\"\n  summary: >\n    Integrates neural network verification tools into circuit discovery. Provides\n    provable guarantees over continuous input domains: (i) input-domain robustness,\n    (ii) patching-domain robustness, (iii) family of minimality guarantees\n    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.\n  relevance_to_css: >\n    Orthogonal: provides theoretical guarantees for a single discovery method.\n    CSS is empirical cross-method consensus. Could use formal methods to verify\n    that CSS consensus circuits satisfy minimality/faithfulness properties.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2604.16889\"\n  title: \"PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\"\n  authors: \"Qinhao Chen, Linyang He, Nima Mesgarani\"\n  year: 2026\n  category: \"method-component\"\n  role: \"New circuit discovery method (CLT-native, could be input to CSS)\"\n  summary: >\n    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores\n    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware\n    reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n  relevance_to_css: >\n    Potential new method to include in CSS ensemble. As CLT/transcoder methods become\n    standard, CSS should demonstrate it can incorporate them alongside traditional\n    edge-level methods. Not a competitor.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16740\"\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  category: \"evaluation\"\n  role: \"Cross-seed stability analysis (motivates need for robust circuits)\"\n  summary: >\n    Quantifies attention head similarity across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models\n    show stronger mid-depth divergence. AdamW increases head stability for deeper models.\n  relevance_to_css: >\n    Motivational: shows circuits can be seed-dependent, strengthening the argument\n    that consensus across methods (not just seeds) is needed for robust circuit claims.\n    Citable as motivation in related work.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.00845\"\n  title: \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Statistical stability framework for circuit discovery\"\n  summary: >\n    Argues interpretability methods should be viewed as statistical estimators subject to\n    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits\n    are often reported without quantification of statistical stability or uncertainty.\n  relevance_to_css: >\n    Strong motivation paper for CSS. If a single method has high variance, cross-method\n    consensus provides a principled way to identify edges that are stable regardless of\n    estimation noise. Citable as framing/motivation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.25786\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\"\n  authors: \"Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Bootstrapping for edge consistency + ILP selection\"\n  summary: >\n    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,\n    (2) ratio-based selection for strong positive edges, (3) integer linear programming\n    formulation replacing greedy selection. Yields more faithful circuits on MIB.\n  relevance_to_css: >\n    Bootstrapping for intra-method edge consistency is related to CSS stability concept\n    but limited to single method. ILP selection idea could inspire CSS aggregation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.24731\"\n  title: \"Circuit Stability Characterizes Language Model Generalization\"\n  authors: \"Alan Sun\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Circuit stability predicts generalization (ACL 2025)\"\n  summary: >\n    Circuit stability = model applying consistent circuit across inputs. Through case studies\n    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional\n    generalization. Stability can be induced via chain-of-thought prompting.\n  relevance_to_css: >\n    Downstream application: if CSS consensus circuits are more stable (by construction),\n    they may better predict generalization. Potential evaluation angle for CSS paper.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2511.18409\"\n  title: \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n  authors: \"Shared Task Organizers\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Benchmark and evaluation framework for circuit localization\"\n  summary: >\n    Two tracks: circuit localization (causally influential components) and causal variable\n    localization (mapping activations to interpretable features). Three teams, eight methods.\n    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.\n  relevance_to_css: >\n    MIB benchmark could be used to evaluate CSS. Finding that ensembles help validates\n    the general direction. But no team did true cross-family consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.17630\"\n  title: \"GIM: Improved Interpretability for Large Language Models\"\n  authors: \"Corti team\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Top-performing gradient method on MIB benchmark\"\n  summary: >\n    Gradient Interaction Modifications — gradient-based circuit discovery method.\n    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods\n    in early layers; Integrated Gradients better in middle/late layers.\n  relevance_to_css: >\n    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance\n    differences across methods further motivates cross-method consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2502.06852\"\n  title: \"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Improved gradient-based circuit discovery (fixes EAP saturation)\"\n  summary: >\n    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient\n    propagation fix for more accurate edge importance scoring.\n  relevance_to_css: >\n    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows\n    intra-family variation — CSS's value is cross-family agreement, not intra-family.\n  discovered_date: \"2026-05-12\"\n\n# ============================================================\n# NOVELTY ASSESSMENT (as of 2026-05-12)\n# ============================================================\n# No paper found that performs TRUE cross-method consensus spanning\n# different algorithm families (gradient-based vs mask-learning vs\n# causal intervention). Specifically:\n#\n# - CIRCUS: intra-method (threshold variation within single algorithm)\n# - Mondorf et al.: EAP-IG + EP (both gradient-family)\n# - Nikankin et al.: bootstrapping within single method\n# - Certified Circuits: data perturbation stability (single method)\n#\n# CSS's core novelty — binary consensus across algorithm families\n# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)\n# with principled cross-family agreement scoring — REMAINS UNCLAIMED\n# as of 2026-05-12.\n# ============================================================\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml",
    "content": "# Literature Map — structfuse-context (cross-method circuit consensus)\n# Last updated: 2026-05-12\n\n- arxiv_id: \"2603.00523\"\n  title: \"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles\"\n  authors: \"Unknown (arXiv 2603.00523v2)\"\n  year: 2026\n  category: \"direct-competitor\"\n  role: \"Primary competitor — intra-method stability scoring\"\n  summary: >\n    Constructs ensemble of attribution graphs by pruning a single raw attribution\n    run under multiple threshold configurations. Assigns per-edge stability score\n    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.\n    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.\n    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).\n  relevance_to_css: >\n    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE\n    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask\n    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.\n    v2 update (2026-03-20) is same paper, no separate follow-up found.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.06811\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods\"\n  authors: \"Mondorf, Wang et al.\"\n  year: 2025\n  category: \"direct-competitor\"\n  role: \"Limited cross-method ensembling (EAP-IG + Edge Pruning)\"\n  summary: >\n    Explores parallel ensembling (averaging/min/max of attribution scores across methods)\n    and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement).\n    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.\n    Workshop short paper at BlackboxNLP 2025.\n  relevance_to_css: >\n    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both\n    gradient-based edge attribution methods from the same algorithmic family.\n    No causal/mask-based methods included. Simple score aggregation (avg/min/max),\n    no principled consensus framework. CSS goes beyond by spanning algorithm families\n    and providing binary consensus with confidence scoring.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.22968\"\n  title: \"Certified Circuits: Stability Guarantees for Mechanistic Circuits\"\n  authors: \"Alaa Anani, Tobias Lorenz, Bernt Schiele, Mario Fritz, Jonas Fischer\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Stability via data subsampling (complementary orthogonal axis)\"\n  summary: >\n    Wraps any black-box circuit discovery algorithm with randomized data subsampling\n    (1000 subsamples) + per-neuron vote aggregation. Certifies that circuit component\n    inclusion is invariant to bounded dataset edit-distance perturbations. Certified\n    circuits: 91% higher accuracy, 45% fewer neurons vs baselines on ImageNet.\n  relevance_to_css: >\n    Complementary: addresses data stability (same method, different data subsets).\n    CSS addresses method stability (same data, different algorithms). Could combine:\n    run CSS consensus then certify the consensus circuit's data-robustness.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16823\"\n  title: \"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees\"\n  authors: \"Itamar Hadad, Guy Katz, Shahaf Bassan\"\n  year: 2026\n  category: \"method-component\"\n  role: \"Formal verification for circuit discovery (ICLR 2026)\"\n  summary: >\n    Integrates neural network verification tools into circuit discovery. Provides\n    provable guarantees over continuous input domains: (i) input-domain robustness,\n    (ii) patching-domain robustness, (iii) family of minimality guarantees\n    (quasi-, local-, subset-, cardinal-minimality). Published at ICLR 2026.\n  relevance_to_css: >\n    Orthogonal: provides theoretical guarantees for a single discovery method.\n    CSS is empirical cross-method consensus. Could use formal methods to verify\n    that CSS consensus circuits satisfy minimality/faithfulness properties.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2604.16889\"\n  title: \"PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\"\n  authors: \"Qinhao Chen, Linyang He, Nima Mesgarani\"\n  year: 2026\n  category: \"method-component\"\n  role: \"New circuit discovery method (CLT-native, could be input to CSS)\"\n  summary: >\n    First CLT-native end-to-end framework. Feature Attribution Patching (FAP) scores\n    CLT features by gradient-weighted write contributions. FAP-Synergy adds synergy-aware\n    reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n  relevance_to_css: >\n    Potential new method to include in CSS ensemble. As CLT/transcoder methods become\n    standard, CSS should demonstrate it can incorporate them alongside traditional\n    edge-level methods. Not a competitor.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2602.16740\"\n  title: \"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality\"\n  authors: \"Karan Bali, Jack Stanley, Praneet Suresh, Danilo Bzdok\"\n  year: 2026\n  category: \"evaluation\"\n  role: \"Cross-seed stability analysis (motivates need for robust circuits)\"\n  summary: >\n    Quantifies attention head similarity across independently initialized training runs.\n    Middle-layer heads are least stable yet most representationally distinct. Deeper models\n    show stronger mid-depth divergence. AdamW increases head stability for deeper models.\n  relevance_to_css: >\n    Motivational: shows circuits can be seed-dependent, strengthening the argument\n    that consensus across methods (not just seeds) is needed for robust circuit claims.\n    Citable as motivation in related work.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.00845\"\n  title: \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis of EAP-IG\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Statistical stability framework for circuit discovery\"\n  summary: >\n    Argues interpretability methods should be viewed as statistical estimators subject to\n    variance/robustness questions. Systematic stability analysis of EAP-IG. Shows circuits\n    are often reported without quantification of statistical stability or uncertainty.\n  relevance_to_css: >\n    Strong motivation paper for CSS. If a single method has high variance, cross-method\n    consensus provides a principled way to identify edges that are stable regardless of\n    estimation noise. Citable as framing/motivation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2510.25786\"\n  title: \"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection\"\n  authors: \"Yaniv Nikankin, Dana Arad, Itay Itzhak, Anja Reusch, Adi Simhi, Gal Kesten-Pomeranz, Yonatan Belinkov\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Bootstrapping for edge consistency + ILP selection\"\n  summary: >\n    Three improvements: (1) bootstrapping to identify edges with consistent attribution scores,\n    (2) ratio-based selection for strong positive edges, (3) integer linear programming\n    formulation replacing greedy selection. Yields more faithful circuits on MIB.\n  relevance_to_css: >\n    Bootstrapping for intra-method edge consistency is related to CSS stability concept\n    but limited to single method. ILP selection idea could inspire CSS aggregation.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.24731\"\n  title: \"Circuit Stability Characterizes Language Model Generalization\"\n  authors: \"Alan Sun\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Circuit stability predicts generalization (ACL 2025)\"\n  summary: >\n    Circuit stability = model applying consistent circuit across inputs. Through case studies\n    on arithmetic and Boolean evaluation, shows stability predicts length/structural/compositional\n    generalization. Stability can be induced via chain-of-thought prompting.\n  relevance_to_css: >\n    Downstream application: if CSS consensus circuits are more stable (by construction),\n    they may better predict generalization. Potential evaluation angle for CSS paper.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2511.18409\"\n  title: \"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models\"\n  authors: \"Shared Task Organizers\"\n  year: 2025\n  category: \"evaluation\"\n  role: \"Benchmark and evaluation framework for circuit localization\"\n  summary: >\n    Two tracks: circuit localization (causally influential components) and causal variable\n    localization (mapping activations to interpretable features). Three teams, eight methods.\n    Ensemble and regularization strategies most effective. Evaluation via faithfulness curves.\n  relevance_to_css: >\n    MIB benchmark could be used to evaluate CSS. Finding that ensembles help validates\n    the general direction. But no team did true cross-family consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2505.17630\"\n  title: \"GIM: Improved Interpretability for Large Language Models\"\n  authors: \"Corti team\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Top-performing gradient method on MIB benchmark\"\n  summary: >\n    Gradient Interaction Modifications — gradient-based circuit discovery method.\n    Tops HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods\n    in early layers; Integrated Gradients better in middle/late layers.\n  relevance_to_css: >\n    Strong single-method baseline to include in CSS ensemble. Layer-dependent performance\n    differences across methods further motivates cross-method consensus.\n  discovered_date: \"2026-05-12\"\n\n- arxiv_id: \"2502.06852\"\n  title: \"EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\"\n  authors: \"Unknown\"\n  year: 2025\n  category: \"method-component\"\n  role: \"Improved gradient-based circuit discovery (fixes EAP saturation)\"\n  summary: >\n    Addresses gradient saturation in Edge Attribution Patching. Proposes gradient\n    propagation fix for more accurate edge importance scoring.\n  relevance_to_css: >\n    Another gradient-family method variant. Existence of EAP, EAP-IG, EAP-GP shows\n    intra-family variation — CSS's value is cross-family agreement, not intra-family.\n  discovered_date: \"2026-05-12\"\n\n# ============================================================\n# NOVELTY ASSESSMENT (as of 2026-05-12)\n# ============================================================\n# No paper found that performs TRUE cross-method consensus spanning\n# different algorithm families (gradient-based vs mask-learning vs\n# causal intervention). Specifically:\n#\n# - CIRCUS: intra-method (threshold variation within single algorithm)\n# - Mondorf et al.: EAP-IG + EP (both gradient-family)\n# - Nikankin et al.: bootstrapping within single method\n# - Certified Circuits: data perturbation stability (single method)\n#\n# CSS's core novelty — binary consensus across algorithm families\n# (e.g., EAP-IG vs ACDC vs subnetwork probing vs edge pruning)\n# with principled cross-family agreement scoring — REMAINS UNCLAIMED\n# as of 2026-05-12.\n# ============================================================\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T23:09:04.576767+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan_20260512T230501",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-12T23:09:04.576938+00:00_

文献扫描完成。结果写入 `artifacts/literature_map.yaml`（13篇论文）。

**截至 2026-05-12，未发现新的 cross-method circuit consensus 工作。** 核心发现：

| 论文 | 做了什么 | 为什么不是我们的 novelty |
|------|---------|------------------------|
| CIRCUS (2603.00523v2) | intra-method threshold variation ensemble | 单一算法内变阈值，不跨算法族 |
| Mondorf et al. (2510.06811) | EAP-IG + EP 平行/串行 ensemble | 仅 gradient-family 内组合 |
| Certified Circuits (2602.22968) | 数据扰动稳定性认证 | 单方法 + data axis，非 method axis |
| Nikankin et al. (2510.25786) | 单方法 bootstrapping | 同上 |

**CSS 的 cross-algorithm-family consensus（gradient vs mask vs causal）在当前文献中无人做过，novelty 成立。**

CIRCUS 无 v2/follow-up（v2 只是同篇 minor update，2026-03-20）。

值得关注的新工作：
- Formal MI (ICLR 2026) — 可用于验证 consensus circuit 的 minimality
- PIE (2604.16889) — CLT-native 新方法，可纳入 CSS ensemble
- GIM — MIB benchmark 第一，作为强 baseline 纳入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-scan_20260512T230501"
}
```

</details>

---
