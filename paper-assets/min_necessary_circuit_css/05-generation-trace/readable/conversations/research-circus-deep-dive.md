# research circus deep dive

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_research_circus_deep_dive_20260512T221843.jsonl`
- **Structured JSON:** [`171df9ab784cf4c115c0.json`](../../sessions/17/171df9ab784cf4c115c0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-12T22:22:15.628029+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-12T22:22:15.628385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T22:22:15.628581+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS circuit discovery stability arXiv 2603.00523"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS circuit discovery stability arXiv 2603.00523"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T22:22:15.628757+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS \"config-bagging\" circuit discovery consensus stability scoring 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS \"config-bagging\" circuit discovery consensus stability scoring 2026"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T22:22:15.628903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T22:22:15.629026+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/related_work_notes.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-12T22:22:15.629148+00:00_

artifacts/related_work_notes.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-12T22:22:15.629308+00:00_

Web search results for query: "CIRCUS circuit discovery stability arXiv 2603.00523"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"[2602.16823] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"[2602.16823v1] Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/abs/2602.16823v1"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/html/2602.16823v1"},{"title":"Automated Circuit Discovery with Provable Guarantees","url":"https://arxiv.org/pdf/2602.16823"},{"title":"Automatic Discovery of Visual Circuits","url":"https://arxiv.org/html/2404.14349v1"}]

Based on the search results, here is information about the paper arXiv 2603.00523:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score (the fraction of configurations that retain it), and extracts a strict-consensus circuit consisting only of edges that appear in all views.

**The Core Problem:**
Mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionari
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T22:22:15.629504+00:00_

Web search results for query: "CIRCUS "config-bagging" circuit discovery consensus stability scoring 2026"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Generalized String-Stability Criteria for Consensus Protocols","url":"https://arxiv.org/html/2604.21329v1"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Circus 2026 — AI & Experimentation Conference — London","url":"https://speero.com/circus"},{"title":"Configuration — Circus 0.17.2 documentation - Read the Docs","url":"https://circus.readthedocs.io/en/latest/for-ops/configuration/"},{"title":"Circuit Insights - 2026 IEEE CICC","url":"https://www.ieee-cicc.org/circuit-insights/"},{"title":"ConsCS: Effective and Efficient Verification of Circom Circuits (ICSE 2025 - Research Track) - ICSE 2025","url":"https://conf.researchr.org/details/icse-2025/icse-2025-research-track/189/ConsCS-Effective-and-Efficient-Verification-of-Circom-Circuits"},{"title":"Circos: An information aesthetic for comparative genomics","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2752132/"},{"title":"ConsCS: Effective and Efficient Verification of Circom Circuits | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00200"}]

Based on the search results, I found relevant information about CIRCUS:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS addresses the problem that mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, often yielding brittle "one-shot" explanations with no principled notion of uncertainty. The method reframes circuit
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T22:22:15.629688+00:00_

Web search results for query: "arXiv 2603.00523 CIRCUS per-edge stability mechanistic interpretability"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Certified Circuits: Stability Guarantees for Mechanistic Circuits","url":"https://arxiv.org/html/2602.22968"},{"title":"Quantifying LLM Attention-Head Stability: Implications for Circuit Universality","url":"https://arxiv.org/html/2602.16740"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731"},{"title":"[2603.30002] Tracking Equivalent Mechanistic Interpretations Across Neural Networks","url":"https://arxiv.org/abs/2603.30002"},{"title":"Circuit Stability Characterizes Language Model ...","url":"https://aclanthology.org/2025.acl-long.442.pdf"},{"title":"Mechanistic Interpretability for AI Safety A Review","url":"https://arxiv.org/html/2404.14082v2"},{"title":"Beyond Accuracy: Introducing a Symbolic-Mechanistic Approach to Interpretable Evaluation","url":"https://arxiv.org/html/2603.23517"},{"title":"Mechanistic Interpretability Needs Philosophy","url":"https://arxiv.org/html/2506.18852v1"}]

Based on the search results, I found detailed information about arXiv paper 2603.00523.

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

CIRCUS reframes circuit discovery as a problem of uncertainty over explanations, pruning one attribution graph under multiple configurations and assigning each edge an empirical inclusion frequency s(e)∈[0,1] measuring how robustly it survives across the configuration family.

### Key Problem Addressed

A critical issue is that circuit discovery results depend on arbitrary analyst choices: two different pruning thresholds yield two different circuits, with no principled way to tell whi
…[truncated 1113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-12T22:22:15.629894+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.00523",
  "prompt": "Extract the full abstract, author list, and any methodology details visible on this page. What models and tasks are evaluated? What circuit discovery methods are used (EAP, ACDC, Edge Pruning, etc.)? Does CIRCUS compare across different circuit discovery algorithms?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2603.00523",
    "prompt": "Extract the full abstract, author list, and any methodology details visible on this page. What models and tasks are evaluated? What circuit discovery methods are used (EAP, ACDC, Edge Pruning, etc.)? Does CIRCUS compare across different circuit discovery algorithms?"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T22:22:15.630032+00:00_

# CIRCUS Paper Summary

## Full Abstract
"Every mechanistic circuit carries an invisible asterisk: it reflects not just the model's computation, but the analyst's choice of pruning threshold. Change that choice and the circuit changes, yet current practice treats a single pruned subgraph as ground truth with no way to distinguish robust structure from threshold artifacts. We introduce CIRCUS, which reframes circuit discovery as a problem of uncertainty over explanations. CIRCUS prunes one attribution graph under B configurations, assigns each edge an empirical inclusion frequency s(e) in [0,1] measuring how robustly it survives across the configuration family, and extracts a consensus circuit of edges present in every view. This yields a principled core/contingent/noise decomposition (analogous to posterior model-inclusion indicators in Bayesian variable selection) that separates robust structure from threshold-sensitive artifacts, with negligible overhead. On Gemma-2-2B and Llama-3.2-1B, consensus circuits are 40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power, consistently outperform influence-ranked and random baselines, and are confirmed causally relevant by activation patching."

## Author
Swapnil Parekh

## Models & Tasks Evaluated
- Gemma-2-2B
- Llama-3.2-1B

## Methodology Details
CIRCUS prunes a single attribution graph across multiple pruning threshold configurations, computing empirical edge inclusion frequencies. It extracts consensus circuits and decomposes results into robust core/contingent/noise categories. Evaluation employs activation patching for causal validation.

## Circuit Discovery Comparison
The page does not specify which circuit discovery algorithms (EAP, ACDC, etc.) CIRCUS compares against, though it benchmarks against influence-ranked and random baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-12T22:22:15.630167+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2603.00523",
  "prompt": "Extract ALL methodology details from the CIRCUS paper. Specifically I need:\n\n1. STABILITY MEASUREMENT: What exactly varies across the ensemble? Is it pruning thresholds, random seeds, data subsets, or something else? What is \"config-bagging\" precisely? How many configurations B are used?\n\n2. CONSENSUS MECHANISM: What is the mathematical formula for the stability score s(e)? Is it binary voting or continuous averaging? How is the consensus circuit extracted - what threshold is used?\n\n3. MODELS AND TASKS: List all models (GPT-2, Llama, Gemma, etc.) and all tasks (IOI, Greater-Than, etc.) used in experiments.\n\n4. CIRCUIT DISCOVERY METHODS: Which underlying circuit discovery method(s) does CIRCUS use? EAP? ACDC? Edge Pruning? Does it compare across DIFFERENT circuit discovery algorithms, or only vary parameters within ONE algorithm?\n\n5. FAITHFULNESS EVALUATION: What metrics are used to evaluate circuit quality? KL divergence? Logit diff? How does CIRCUS prove consensus is better than single runs?\n\n6. CORE/CONTINGENT/NOISE DECOMPOSITION: How are these three categories defined mathematically?\n\nBe extremely detailed and include any formulas or specific numbers mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2603.00523",
    "prompt": "Extract ALL methodology details from the CIRCUS paper. Specifically I need:\n\n1. STABILITY MEASUREMENT: What exactly varies across the ensemble? Is it pruning thresholds, random seeds, data subsets, or something else? What is \"config-bagging\" precisely? How many configurations B are used?\n\n2. CONSENSUS MECHANISM: What is the mathematical formula for the stability score s(e)? Is it binary voting or continuous averaging? How is the consensus circuit extracted - what threshold is used?\n\n3. MODELS AND TASKS: List all models (GPT-2, Llama, Gemma, etc.) and all tasks (IOI, Greater-Than, etc.) used in experiments.\n\n4. CIRCUIT DISCOVERY METHODS: Which underlying circuit discovery method(s) does CIRCUS use? EAP? ACDC? Edge Pruning? Does it compare across DIFFERENT circuit discovery algorithms, or only vary parameters within ONE algorithm?\n\n5. FAITHFULNESS EVALUATION: What metrics are used to evaluate circuit quality? KL divergence? Logit diff? How does CIRCUS prove consensus is better than single runs?\n\n6. CORE/CONTINGENT/NOISE DECOMPOSITION: How are these three categories defined mathematically?\n\nBe extremely detailed and include any formulas or specific numbers mentioned."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T22:22:15.630297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T22:22:15.630498+00:00_

1	# Circuit Discovery Related Work Notes (2024-2026)
2	
3	> 调研日期：2026-05-12 | 项目：structfuse-context
4	> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？
5	
6	---
7	
8	## 1. 方法一致性比较（Novelty 关键）
9	
10	**结论：没有论文以"跨方法一致性分析"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。
11	
12	### 直接比较多方法的论文
13	
14	| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |
15	|------|----------|----------|---------------------|
16	| Conmy et al. "Towards Automated Circuit Discovery" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |
17	| Syed et al. "Attribution Patching Outperforms Automated Circuit Discovery" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |
18	| Bhaskar et al. "Finding Transformer Circuits with Edge Pruning" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |
19	| Hsu et al. "CD-T" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |
20	| Edin et al. "GIM" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |
21	| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |
22	
23	### 最接近"一致性分析"的论文
24	
25	**Hanna et al. "Have Faith in Faithfulness: Going Beyond Circuit Overlap" (2024, arXiv 2403.17806)**
26	- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大
27	- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价
28	- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究
29	
30	**Méloux et al. "Mechanistic Interpretability as Statistical Estimation: A Variance Analysis" (2025, arXiv 2510.00845)**
31	- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561
32	- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等
33	- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法
34	
35	**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**
36	
37	---
38	
3
…[truncated 7344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T22:22:15.630690+00:00_

# CIRCUS Methodology: Comprehensive Extraction

## 1. STABILITY MEASUREMENT

**What Varies:** "Config-bagging" varies **pruning thresholds** (node and edge cumulative-influence cutoffs), not random seeds or data subsets. The method applies B different threshold configurations to a **single attribution graph** without retraining.

**Config-Bagging Definition:** A deterministic design set of pruning configurations {πb} where each πb specifies node and edge thresholds. The paper uses B=25 (5×5 grid) for stability analysis and B=9 non-nested configurations for main evaluation. B=3 is used in some nested-config experiments.

**Critical Design Principle—Non-Nesting:** Configurations must cross thresholds in **opposite directions** to avoid degeneracy. Nested configs (where E(1)⊆E(2)⊆...⊆E(B)) cause consensus to equal the tightest single view. Non-nested examples: "(0.6,0.99)" retains few nodes but many edges; "(0.9,0.95)" does the opposite.

## 2. CONSENSUS MECHANISM

**Stability Score Formula:**
```
s(e) = (1/B) × Σ[b=1 to B] 𝟙[e ∈ E(b)]
```

This is **binary voting with continuous averaging**: each edge receives a frequency s(e)∈[0,1] representing the proportion of the B views in which it appears.

**Consensus Circuit Extraction:**
```
Cτ = {e : s(e) ≥ τ}
```

The paper primarily reports **strict consensus** with τ=1 (edges present in **every view**), though τ<1 permits exploratory larger sets.

**Threshold Rationale:** τ=1 yields an "all-views circuit"; the paper notes this is the "data-driven operating point" because C₁ remains within ~2% influence-retained (IR) of best single configs.

## 3. MODELS AND TASKS

**Models:**
- Gemma-2-2B
- Llama-3.2-1B

**Tasks/Behaviors:**
- Short factoid completions: capitals, arithmetic, trivia
- Paper explicitly states: "Prompts are short factoid completions (capitals, arithmetic, trivia); generalization to more complex behaviors (reasoning, in-context learning) remains open."

**Dataset Scale:**
- Gemma: 50 prompts
- Llama: 20 promp
…[truncated 2695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T22:22:15.630906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS \"Swapnil Parekh\" circuit consensus github code repository 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS \"Swapnil Parekh\" circuit consensus github code repository 2026"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T22:22:15.631032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"2603.00523\" citing papers OR follow-up stability ensemble circuit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"2603.00523\" citing papers OR follow-up stability ensemble circuit"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T22:22:15.631176+00:00_

Web search results for query: "CIRCUS "Swapnil Parekh" circuit consensus github code repository 2026"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Swapnil Parekh – AI","url":"https://swapnilparekh.github.io/"},{"title":"Swapnil Srivastava — Full Stack Engineer","url":"https://swapnilsparsh.github.io/"},{"title":"swapnilsparsh (Swapnil Srivastava) · GitHub","url":"https://github.com/swapnilsparsh"},{"title":"Swapnil Parekh - Intuit | LinkedIn","url":"https://www.linkedin.com/in/swapnil-parekh/"},{"title":"swapagarwal (Swapnil Agarwal) · GitHub","url":"https://github.com/swapagarwal"},{"title":"Swapnil Joshi & Manasi Parekh Ke Saath Movie Talk, Bharela Ringan Batata Nu Shaak Aur Fajeto! - YouTube","url":"https://www.youtube.com/watch?v=ONhbc_6ayV4"},{"title":"circuit-simulator · GitHub Topics · GitHub","url":"https://github.com/topics/circuit-simulator"},{"title":"GitHub - midas-research/data-free-uats","url":"https://github.com/midas-research/data-free-uats"},{"title":"Swapnil Mishra","url":"https://s-mishra.github.io/"}]

Based on the search results, I found information about the CIRCUS research:

CIRCUS is a paper titled "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles" by Swapnil Parekh, which was submitted on February 28, 2026.

The method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a stability score, and extracts a strict-consensus circuit consisting only of edges that appear in all views, producing a threshold-robust "core" circuit while explicitly surfacing contingent alternatives.

On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40x smaller than the union of all configurations while retaining comparable influence-flow explanatory power.

The paper is available on arXiv (arxiv.org/abs/2603.00523). However, the search results did no
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T22:22:15.631344+00:00_

Web search results for query: ""2603.00523" citing papers OR follow-up stability ensemble circuit"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"Stability-Weighted Ensemble Feature Importance for Financial Applications by Hamid R. Arian, Seyed Alireza Mousavizade, Luis A. Seco :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4905824"},{"title":"ELAVL1 primarily couples mRNA stability with the 3 - UTRs ...","url":"https://www.cell.com/cell-reports/pdf/S2211-1247(21)00523-4.pdf"},{"title":"3600 Market Street, 6th Floor Philadelphia, PA 19104-2688 U.S.","url":"https://www.siam.org/media/kuib0myo/ds25_abstracts.pdf"},{"title":"i POWER SYSTEM DYNAMICS AND STABILITY Peter W. Sauer and M. A. Pai","url":"https://courses.physics.illinois.edu/ece576/sp2018/Sauer%20and%20Pai%20book%20-%20Jan%202007.pdf"},{"title":"Chapter 6 Stability and nonlinear dynamics in thyristor and diode circuits","url":"https://iandobson.ece.iastate.edu/PAPERS/dobsonPEchapter01.pdf"},{"title":"Top arXiv papers","url":"https://scirate.com/?archive=quant-ph&date=2026-03-03&page=22&range=1"},{"title":"Definition and Classification of Power System Stability","url":"https://home.engineering.iastate.edu/~jdm/ee554/TermsDefinitions2004.pdf"},{"title":"Power System Stability and Control - Prabha Kundur ( ...","url":"https://dl.poweren.ir/downloads/PowerEn/Book/2019/Jun/Power%20System%20Stability%20and%20Control%20-%20Prabha%20Kundur%20(PowerEn.ir).pdf"}]

Based on the search results, I found the paper you're looking for:

The paper with ID 2603.00523 is titled "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles" by Swapnil Parekh, submitted on February 28, 2026.

**Overview of the paper:**

The paper addresses how mechanistic circuit discovery is se
…[truncated 828 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T22:22:15.631512+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://swapnilparekh.github.io/",
  "prompt": "Look for any GitHub links, code repositories, or project pages related to CIRCUS or circuit discovery. Also note the author's affiliation and other publications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://swapnilparekh.github.io/",
    "prompt": "Look for any GitHub links, code repositories, or project pages related to CIRCUS or circuit discovery. Also note the author's affiliation and other publications."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T22:22:15.631635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS circuit discovery \"cross-layer transcoders\" OR \"attribution graph\" EAP ACDC \"single method\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS circuit discovery \"cross-layer transcoders\" OR \"attribution graph\" EAP ACDC \"single method\" 2026"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T22:22:15.631779+00:00_

# Response: GitHub Links and CIRCUS-Related Content

Based on the web page content provided, I found **no references to CIRCUS or circuit discovery projects**, and **no GitHub repository links** are displayed on this portfolio page.

## What I Found:

**GitHub Profile Link:**
The page includes a GitHub icon link at the bottom (to https://github.com/SwapnilDreams100), but no specific repositories or projects are listed.

**Author Information:**
Swapnil Parekh identifies as an "AI Scientist" specializing in mechanistic interpretability, adversarial robustness, and agentic systems. His most relevant publication for circuit-related work appears to be:

- "The Parliament in the Model: How Neural Circuits Reach Consensus" (April 2024), which discusses how "specific computational subgraphs, attention heads, MLP layers, residual stream connections" operate within language models.

**Affiliation:**
No institutional affiliation is mentioned on this page.

## Conclusion:

To locate CIRCUS-related code or circuit discovery projects, you would need to visit his GitHub profile directly or contact the author, as this portfolio page doesn't enumerate specific repositories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T22:22:15.631944+00:00_

Web search results for query: "CIRCUS circuit discovery "cross-layer transcoders" OR "attribution graph" EAP ACDC "single method" 2026"

Links: [{"title":"Attribution Patching Outperforms Automated Circuit Discovery Aaquib Syed","url":"https://openreview.net/pdf?id=tiLbFR4bJW"},{"title":"Automatic Circuit Discovery","url":"https://sidn.baulab.info/autocircuits/"},{"title":"Discovering Transformer Circuits via a Hybrid Attribution and Pruning Framework","url":"https://www.arxiv.org/pdf/2510.03282"},{"title":"Circuit Tracing: Revealing Computational Graphs in Language Models","url":"https://transformer-circuits.pub/2025/attribution-graphs/methods.html"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://aclanthology.org/2024.blackboxnlp-1.25.pdf"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"Sparse Crosscoders for Cross-Layer Features and Model Diffing","url":"https://transformer-circuits.pub/2024/crosscoders/index.html"},{"title":"Cross-Layer Transcoders (CLTs)","url":"https://www.emergentmind.com/topics/cross-layer-transcoders-clts"},{"title":"Circuit Tracing with the Qwen3 Cross-Layer Transcoders — BluelightAI","url":"https://www.bluelightai.com/blog/circuit-tracing-with-qwen3/"},{"title":"Circuit Tracing: A Step Closer to Understanding Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/circuit-tracing-a-step-closer-to-understanding-large-language-models/"}]

Based on the web search results, I found relevant information about the topics you searched for. Here's what I found:

## Circuit Discovery Methods

EAP outperforms all previous methods for circuit discovery, since it is competitive with ACDC on recovering circuits while significantly reducing the computational demand. ACDC recursively applies activation patching—replacing activations with those from "cor
…[truncated 1222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T22:22:15.632126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "offset": "155"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "offset": "155"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T22:22:15.632260+00:00_

155	4. **非唯一性问题 (ICLR 2025 "Everything Everywhere All at Once")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。
156	
157	#### 🎯 差异化建议
158	
159	- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。
160	- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。
161	- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。
162	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T22:22:15.632415+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

````json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "old_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。",
  "new_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n\n---\n\n## 1b. CIRCUS 深度分析\n\n> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)\n> 作者：Swapnil Parekh\n> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）\n\n### 方法细节\n\n**Stability 测量机制：变化剪枝阈值，不变种子/数据。**\n\nCIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。\n\n**Config-bagging 参数：**\n- B=25（5×5 grid）用于 stability 分析\n- B=9（non-nested configurations）用于主实验评估\n- B=3 用于嵌套配置消融实验\n- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置\n\n**Consensus 公式：**\n\nstability score（per-edge inclusion frequency）：\n```\ns(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]\n```\n\nconsensus circuit 提取：\n```\nC_τ = {e : s(e) ≥ τ}\n```\n\n主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。\n\n**Core/Contingent/Noise 分类：**\n| 类别 | 定义 | 含义 |\n|------|------|------|\n| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |\n| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |\n| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |\n\n类比 Bayesian variable selection 中的 posterior model-inclusion indicators。\n\n### 实验设置\n\n**模型：**\n- Gemma-2-2B\n- Llama-3.2-1B\n\n**任务：**\n- Short factoid completions：capitals, arithmetic, trivia\n- 数据规模：50 prompts (Gemma), 20 prompts (Llama)\n- 论文明确承认局限：\"generalization to more complex behaviors (reasoning, in-context learning) remains open\"\n\n**使用的 circuit discovery 方法：仅一种。**\n- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）\n- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}\n- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法\n- **不跨方法比较**\n\n### Faithfulness 评估\n\n**Metrics：**\n\n1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。\n\n2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。\n\n3. **Activation Patching（因果验证）**：\n   - Patch C₁ 节点激活从 source prompt → target prompt\n   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6\n   - p=0.0004 (Wilcoxon signed-rank)\n   - Consensus = oracle 的 57%，random = 20%\n\n4. **Win-rate**：\n   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9\n   - vs random: 37/50 (Gemma), 20/20 (Llama)\n\n**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。\n\n### 跨方法比较\n\n**CIRCUS 没有做跨方法比较。** 这是确认的事实：\n- 仅使用 CLT attribution graphs 一种 pipeline\n- 变化的是该 pipeline 内的剪枝阈值配置\n- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法\n- **这是 CSS 的核心差异点**\n\n### CSS vs CIRCUS 精确差异表\n\n| 维度 | CIRCUS | CSS (ours) |\n|------|--------|-----------|\n| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |\n| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |\n| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |\n| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |\n| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |\n| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |\n| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |\n| **任务类型** | Short factoid completions | 待定 |\n| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |\n| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |\n| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |\n\n### 关键论点：为何 cross-method > intra-method\n\n1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近\"重要边\"。阈值变化只探索同一视角的灵敏度。\n2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。\n3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道\"哪些结构是方法无关的\"，CSS 回答的是不同的问题。\n4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "old_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。",
    "new_string": "- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n\n---\n\n## 1b. CIRCUS 深度分析\n\n> 论文：CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles (arXiv 2603.00523, 2026.02.28)\n> 作者：Swapnil Parekh\n> 代码：未公开（GitHub: SwapnilDreams100，未找到 CIRCUS 仓库）\n\n### 方法细节\n\n**Stability 测量机制：变化剪枝阈值，不变种子/数据。**\n\nCIRCUS 对**单一 attribution graph**（由 cross-layer transcoders 生成的归因图）施加 B 组不同的剪枝配置 {π₁, ..., πB}，每组配置指定不同的 node threshold 和 edge threshold（cumulative-influence cutoffs）。**不涉及**随机种子变化或数据子集变化。\n\n**Config-bagging 参数：**\n- B=25（5×5 grid）用于 stability 分析\n- B=9（non-nested configurations）用于主实验评估\n- B=3 用于嵌套配置消融实验\n- **关键设计约束——non-nesting**：配置必须在不同维度上交叉变化（如 (0.6, 0.99) 保留少 node 多 edge，(0.9, 0.95) 相反），避免 E(1)⊆E(2)⊆...⊆E(B) 导致 consensus 退化为最严格单配置\n\n**Consensus 公式：**\n\nstability score（per-edge inclusion frequency）：\n```\ns(e) = (1/B) × Σ_{b=1}^{B} 𝟙[e ∈ E(b)]\n```\n\nconsensus circuit 提取：\n```\nC_τ = {e : s(e) ≥ τ}\n```\n\n主实验使用 **strict consensus τ=1**（边必须在所有配置中存在）。τ<1 可用于探索性分析。\n\n**Core/Contingent/Noise 分类：**\n| 类别 | 定义 | 含义 |\n|------|------|------|\n| Core | s(e) = 1 | 所有配置都保留，鲁棒结构 |\n| Contingent | 0.5 ≤ s(e) < 1 | 多数配置保留，替代路径 |\n| Noise | s(e) < 0.5 | 少数配置保留，阈值敏感伪影 |\n\n类比 Bayesian variable selection 中的 posterior model-inclusion indicators。\n\n### 实验设置\n\n**模型：**\n- Gemma-2-2B\n- Llama-3.2-1B\n\n**任务：**\n- Short factoid completions：capitals, arithmetic, trivia\n- 数据规模：50 prompts (Gemma), 20 prompts (Llama)\n- 论文明确承认局限：\"generalization to more complex behaviors (reasoning, in-context learning) remains open\"\n\n**使用的 circuit discovery 方法：仅一种。**\n- 底层方法：cross-layer transcoders (CLTs) 生成的 attribution graphs（引用 Ameisen et al. 2025, Hanna et al. 2025）\n- 节点 = learned features（CLT 特征），边 = features 间的直接因果效应，权重 W ∈ ℝ^{|E|}\n- **不使用** EAP, ACDC, Edge Pruning 或其他传统 circuit discovery 方法\n- **不跨方法比较**\n\n### Faithfulness 评估\n\n**Metrics：**\n\n1. **Influence Retained (IR)**：IR(S) = Φ(S)/Φ(E)，其中 Φ(S) = Σ|w_e| 为子图绝对边权之和。衡量通过子图 S 的总归因影响比例。\n\n2. **KL Divergence（per-logit）**：D_KL(p_E || p_S)，consensus 达到 0.0010±0.0008 vs union-pruned 0.40±1.74（20 prompts, 17/20 wins）。\n\n3. **Activation Patching（因果验证）**：\n   - Patch C₁ 节点激活从 source prompt → target prompt\n   - Recovery: consensus 19.4 vs random 6.8 vs matched controls 1.6\n   - p=0.0004 (Wilcoxon signed-rank)\n   - Consensus = oracle 的 57%，random = 20%\n\n4. **Win-rate**：\n   - vs union-pruned: 47/50 (Gemma), 19/20 (Llama) with B=9\n   - vs random: 37/50 (Gemma), 20/20 (Llama)\n\n**关键结论：** strict consensus circuit ~40× smaller than union，但保持 comparable influence-flow 解释力。overhead 仅 5.5%（<1ms consensus 构建）。\n\n### 跨方法比较\n\n**CIRCUS 没有做跨方法比较。** 这是确认的事实：\n- 仅使用 CLT attribution graphs 一种 pipeline\n- 变化的是该 pipeline 内的剪枝阈值配置\n- 不涉及 EAP, ACDC, Edge Pruning, SP 等任何其他 circuit discovery 算法\n- **这是 CSS 的核心差异点**\n\n### CSS vs CIRCUS 精确差异表\n\n| 维度 | CIRCUS | CSS (ours) |\n|------|--------|-----------|\n| **变化什么** | 单方法内的剪枝阈值 (node/edge cutoffs) | 算法族 (gradient/mask/causal 等不同范式) |\n| **底层方法数** | 1 种 (CLT attribution graphs) | K=3+ 种根本不同的算法 (如 EAP, ACDC, EP) |\n| **稳定性来源** | Intra-method: 阈值鲁棒性 (Rashomon set) | Cross-method: 算法族间一致性 (不同 inductive bias) |\n| **聚合方式** | 连续 stability score s(e)∈[0,1] + strict consensus τ=1 | 二值投票 (K 方法中 ≥ threshold 方法包含 edge) |\n| **输入** | 单次 attribution run 的一张归因图 | 每种方法独立运行产出的 K 张电路图 |\n| **计算开销** | 极低 (5.5% overhead, 不需重新计算归因) | 需要运行 K 种不同算法 (各自完整 pipeline) |\n| **模型规模** | Gemma-2-2B, Llama-3.2-1B | 待定 |\n| **任务类型** | Short factoid completions | 待定 |\n| **core claim** | 阈值变化下的鲁棒核心 vs 阈值敏感伪影 | 跨算法族共识比单方法更鲁棒、更可信 |\n| **方法间差异分析** | ❌ 不分析 | ✅ Pairwise Jaccard matrix / agreement heatmap |\n| **taxonomy 基础** | 同方法不同参数的 inclusion frequency | 不同方法的 agreement count |\n\n### 关键论点：为何 cross-method > intra-method\n\n1. **不同 inductive bias**：EAP 基于梯度归因，ACDC 基于 activation patching（因果干预），EP 基于可微剪枝。它们从根本不同的角度逼近\"重要边\"。阈值变化只探索同一视角的灵敏度。\n2. **信息正交性**：跨方法共识的边同时被梯度信号、因果干预和优化剪枝确认，信息量远大于同方法不同阈值。\n3. **实用价值**：如果研究者只有一种方法，CIRCUS 有用；如果研究者想知道\"哪些结构是方法无关的\"，CSS 回答的是不同的问题。\n4. **Méloux et al. 的启示**：单方法内 Jaccard 仅 0.561，说明 intra-method 变异已经很大。跨方法共识可能提供更稳定的 core（或发现更大的分歧——这本身也是重要发现）。"
  }
}
````

</details>

---

### Tool result

_source line 28 · 2026-05-12T22:22:15.632684+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T22:22:15.632861+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "related_work_notes_v2",
  "type": "report",
  "description": "Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "tags": "['literature', 'CIRCUS', 'novelty', 'related-work']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "related_work_notes_v2",
    "type": "report",
    "description": "Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation",
    "project": "structfuse-context",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "tags": "['literature', 'CIRCUS', 'novelty', 'related-work']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T22:22:15.633007+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_114feb\", \"name\": \"related_work_notes_v2\", \"type\": \"report\", \"description\": \"Related work notes with CIRCUS deep analysis (Section 1b) - detailed method comparison, stability scoring mechanism, cross-method gap confirmation\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes_114feb.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:21:54.490118+00:00\", \"tags\": [\"literature\", \"CIRCUS\", \"novelty\", \"related-work\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circus_deep_dive_20260512T221843",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-12T22:22:15.633182+00:00_

## Q5 结论（最关键）：CIRCUS **没有**做跨方法比较

CIRCUS 只使用一种底层方法（CLT attribution graphs），变化的是剪枝阈值配置，不涉及 EAP/ACDC/EP 等不同 circuit discovery 算法。这确认了 CSS 的核心差异点。

## CSS vs CIRCUS 精确差异

| 维度 | CIRCUS | CSS (ours) |
|------|--------|-----------|
| 变化什么 | 单方法内剪枝阈值 | 不同算法族 (gradient/mask/causal) |
| 方法数 | 1 种 (CLT attribution) | K=3+ 种根本不同算法 |
| 稳定性来源 | Intra-method 阈值鲁棒性 | Cross-method 算法间一致性 |
| 聚合方式 | 连续 s(e)∈[0,1] + strict τ=1 | 二值投票 ≥ threshold |
| 计算开销 | 极低 (5.5%) | 需运行 K 种完整 pipeline |
| 跨方法分析 | 不做 | Pairwise Jaccard / agreement matrix |

**核心论点**：CIRCUS 回答"这条边对阈值选择鲁棒吗？"，CSS 回答"这条边是算法无关的吗？"。不同算法有不同 inductive bias（梯度 vs 因果干预 vs 可微剪枝），跨方法共识的信息正交性远高于阈值变化。

## 其他要点

- **模型/任务**：Gemma-2-2B + Llama-3.2-1B，仅 short factoid completions（capitals, arithmetic, trivia），50/20 prompts
- **Consensus 公式**：s(e) = (1/B)Σ𝟙[e∈E(b)]，B=9 主实验，strict consensus τ=1
- **Faithfulness**：IR + KL divergence + activation patching (p=0.0004)，consensus ~40× smaller than union 但保持解释力
- **GitHub 仓库**：未公开

已追加到 `artifacts/related_work_notes.md` Section 1b。

Sources:
- [CIRCUS paper (arXiv)](https://arxiv.org/abs/2603.00523)
- [CIRCUS HTML full text](https://arxiv.org/html/2603.00523)
- [Swapnil Parekh's page](https://swapnilparekh.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_circus_deep_dive_20260512T221843"
}
```

</details>

---
