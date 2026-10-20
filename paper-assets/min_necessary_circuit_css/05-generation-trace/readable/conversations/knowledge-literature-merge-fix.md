# knowledge literature merge fix

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_knowledge_literature-merge-fix_20260513T022004.jsonl`
- **Structured JSON:** [`cc3bd4f2324803196f9d.json`](../../sessions/cc/cc3bd4f2324803196f9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-13T02:22:34.308470+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T02:22:34.308900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T02:22:34.309139+00:00_

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
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
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

_source line 4 · 2026-05-13T02:22:34.309354+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'structfuse-context'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T02:22:34.309543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T02:22:34.309951+00:00_

1	# Related Work Literature Survey for CSS (Cross-method Structural Consensus)
2	
3	> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)
4	
5	---
6	
7	## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability
8	
9	### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
10	- **Authors:** Swapnil Parekh
11	- **Year:** 2026 (arXiv: 2603.00523)
12	- **Venue:** arXiv preprint (Feb 2026)
13	- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
14	- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.
15	
16	### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
17	- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
18	- **Year:** 2026 (arXiv: 2602.22968)
19	- **Venue:** arXiv preprint (Feb 2026)
20	- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component 
…[truncated 17691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T02:22:34.310183+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/literature_map.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T02:22:34.310317+00:00_

artifacts/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T02:22:34.310443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T02:22:34.310643+00:00_

1	# Literature Map — structfuse-context (cross-method circuit consensus)
2	# Last updated: 2026-05-12
3	
4	- arxiv_id: "2603.00523"
5	  title: "CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles"
6	  authors: "Unknown (arXiv 2603.00523v2)"
7	  year: 2026
8	  category: "direct-competitor"
9	  role: "Primary competitor — intra-method stability scoring"
10	  summary: >
11	    Constructs ensemble of attribution graphs by pruning a single raw attribution
12	    run under multiple threshold configurations. Assigns per-edge stability score
13	    (fraction of configs retaining it). Strict-consensus circuit = edges in all views.
14	    ~40x smaller than union on Gemma-2-2B/Llama-3.2-1B while retaining explanatory power.
15	    Consensus nodes beat non-consensus controls in activation patching (p=0.0004).
16	  relevance_to_css: >
17	    CLOSEST competitor but fundamentally intra-method: varies thresholds within ONE
18	    attribution algorithm. Does NOT combine across algorithm families (gradient vs mask
19	    vs causal). CSS's cross-method consensus remains a distinct and unclaimed novelty.
20	    v2 update (2026-03-20) is same paper, no separate follow-up found.
21	  discovered_date: "2026-05-12"
22	
23	- arxiv_id: "2510.06811"
24	  title: "BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods"
25	  authors: "Mondorf, Wang et al."
26	  year: 2025
27	  category: "direct-competitor"
28	  role: "Limited cross-method ensembling (EAP-IG + Edge Pruning)"
29	  summary: >
30	    Explores parallel ensembling (averaging/min/max of attribution scores across methods)
31	    and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement).
32	    Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on MIB leaderboard.
33	    Workshop short paper at BlackboxNLP 2025.
34	  relevance_to_css: >
35	    Closest to cross-method but limited: only combines EAP-IG and Edge Pruning, both
36	    gradient-based e
…[truncated 9931 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T02:22:34.310923+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n---",
  "new_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)\n- **Authors:** Mondorf, Wang et al.\n- **Year:** 2025 (arXiv: 2510.06811)\n- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)\n- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.\n- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).\n\n---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "old_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n---",
    "new_string": "### 1.4 Circuit Tracing: Revealing Computational Graphs in Language Models\n- **Authors:** Anthropic (Dario Amodei team)\n- **Year:** 2025\n- **Venue:** Anthropic Technical Report (March 2025)\n- **Core findings:** Uses cross-layer transcoders to build attribution graphs—graphical representations of computational steps where nodes are features and edges are causal interactions. Open-sourced circuit tracing tools supporting Gemma-2-2B, Llama-3.1-1B, Qwen3-4B.\n- **Relation to CSS:** **互补 (Complementary)**. Provides a different paradigm (feature-level circuits via transcoders vs. component-level circuits). CSS methods operate at edge/component level; circuit tracing works at feature level. Represents a parallel direction worth acknowledging.\n\n### 1.5 Exploring Ensemble Strategies for Circuit Localization Methods (Mondorf et al.)\n- **Authors:** Mondorf, Wang et al.\n- **Year:** 2025 (arXiv: 2510.06811)\n- **Venue:** BlackboxNLP 2025 (Workshop short paper, MIB Shared Task)\n- **Core findings:** Explores parallel ensembling (averaging/min/max of attribution scores across methods) and sequential ensembling (EAP-IG warm-start then Edge Pruning refinement) for circuit localization. Parallel ensemble over all variants achieves best CMD=0.03, CPR=1.83 on the MIB leaderboard.\n- **Relation to CSS:** **直接竞争 (Direct competitor — limited scope)**. The closest existing work to cross-method circuit ensembling, but with critical limitations: (1) **仅限 gradient 族方法**: only combines EAP-IG and Edge Pruning, both gradient-based edge attribution methods from the same algorithmic family — no causal/mask-based methods (e.g., ACDC) included; (2) **Score averaging 而非 binary consensus**: uses simple score aggregation (avg/min/max) rather than principled binary agreement, inheriting score calibration issues across methods with incomparable scales; (3) **无 consensus 理论框架**: no analysis of method agreement patterns, confidence scoring, or consensus circuit properties; (4) **Workshop short paper 规模**: limited evaluation scope compared to CSS's full pipeline. CSS goes beyond by spanning algorithm families (gradient-based vs. iterative patching vs. mask optimization), providing binary consensus with confidence scoring, and analyzing consensus circuit properties (size, faithfulness, robustness).\n\n---"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T02:22:34.311165+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T02:22:34.311314+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n---",
  "new_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\n- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani\n- **Year:** 2026 (arXiv: 2604.16889)\n- **Venue:** arXiv preprint (April 2026)\n- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.\n\n### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\n- **Authors:** arXiv: 2502.06852\n- **Year:** 2025\n- **Venue:** arXiv preprint (Feb 2025)\n- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.\n- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.\n\n### GIM: Improved Interpretability for Large Language Models\n- **Authors:** Corti team\n- **Year:** 2025 (arXiv: 2505.17630)\n- **Venue:** arXiv preprint (May 2025)\n- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.\n- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.\n\n---"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "old_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n---",
    "new_string": "### RelP: Faithful and Efficient Circuit Discovery via Relevance Patching\n- **Authors:** Farnoush Rezaei Jafari et al.\n- **Year:** 2025\n- **Venue:** NeurIPS 2025 MechInterp Workshop (Spotlight)\n- **Core findings:** Replaces gradients in attribution patching with LRP propagation coefficients. For MLP outputs in GPT-2 Large, attribution patching achieves Pearson correlation 0.006 vs. RelP's 0.956 with activation patching ground truth. Faithfulness comparable to IG at lower cost.\n- **Relation to CSS:** **互补 (Complementary)**. Another discovery method with different inductive bias. Documents dramatic differences between methods on the same components—supports CSS's premise.\n\n### PIE: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution\n- **Authors:** Qinhao Chen, Linyang He, Nima Mesgarani\n- **Year:** 2026 (arXiv: 2604.16889)\n- **Venue:** arXiv preprint (April 2026)\n- **Core findings:** First CLT-native end-to-end circuit discovery framework. Feature Attribution Patching (FAP) scores CLT features by gradient-weighted write contributions; FAP-Synergy adds synergy-aware reranking. Evaluated with KL-divergence behavior retention and FADE-style metrics.\n- **Relation to CSS:** **互补 (Complementary)**. Operates at the feature level via cross-layer transcoders rather than at the component/edge level. As CLT/transcoder methods become standard, PIE represents a potential additional discovery method for CSS's ensemble, bridging component-level and feature-level consensus.\n\n### EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification\n- **Authors:** arXiv: 2502.06852\n- **Year:** 2025\n- **Venue:** arXiv preprint (Feb 2025)\n- **Core findings:** Addresses gradient saturation in Edge Attribution Patching by proposing a gradient propagation fix for more accurate edge importance scoring. Improves upon EAP/EAP-IG in faithfulness for circuits where saturation artifacts degrade standard gradient estimates.\n- **Relation to CSS:** **互补 (Complementary)**. Another intra-family gradient variant alongside EAP, EAP-IG. The proliferation of EAP variants (EAP → EAP-IG → EAP-GP) illustrates intra-family variation driven by specific failure modes—CSS's value lies in cross-family agreement that transcends these intra-family fixes.\n\n### GIM: Improved Interpretability for Large Language Models\n- **Authors:** Corti team\n- **Year:** 2025 (arXiv: 2505.17630)\n- **Venue:** arXiv preprint (May 2025)\n- **Core findings:** Gradient Interaction Modifications — gradient-based circuit discovery method that tops the HuggingFace Mechanistic Interpretability Benchmark. Outperforms other methods in early layers; Integrated Gradients performs better in middle/late layers, suggesting layer-dependent method strengths.\n- **Relation to CSS:** **互补 (Complementary)**. Strong single-method baseline. The finding that different gradient methods excel in different layers directly motivates cross-method consensus: no single method dominates across all model components. A potential candidate for inclusion in CSS's method ensemble.\n\n---"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T02:22:34.311551+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T02:22:34.311751+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 5. Distribution-shift robustness is a novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.",
  "new_string": "### 5. Distribution-shift robustness is a planned novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "old_string": "### 5. Distribution-shift robustness is a novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.",
    "new_string": "### 5. Distribution-shift robustness is a planned novel evaluation angle\nNo existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T02:22:34.312067+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T02:22:34.312332+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "### 2. CIRCUS is the primary competitor — positioning is critical\nCIRCUS (Parekh, 2026) is the closest work. Key differentiation:\n- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness\n- **CSS:** uses multiple independent discovery methods → method robustness\n- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).",
  "new_string": "### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical\nTwo closest works, each with distinct limitations:\n- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family\n- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus\n- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus\n- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "old_string": "### 2. CIRCUS is the primary competitor — positioning is critical\nCIRCUS (Parekh, 2026) is the closest work. Key differentiation:\n- **CIRCUS:** varies pruning thresholds within one attribution method → threshold robustness\n- **CSS:** uses multiple independent discovery methods → method robustness\n- CSS argument: method diversity captures a broader space of inductive biases than threshold variation. A threshold ensemble still inherits the blind spots of its single underlying attribution method (e.g., EAP's first-order approximation errors). CSS's methods have structurally different failure modes (gradient-based vs. iterative patching vs. similarity-based).",
    "new_string": "### 2. CIRCUS and Mondorf et al. are the primary competitors — positioning is critical\nTwo closest works, each with distinct limitations:\n- **CIRCUS (Parekh, 2026):** varies pruning thresholds within one attribution method → threshold robustness within a single algorithm family\n- **Mondorf et al. (2510.06811):** ensembles EAP-IG + Edge Pruning via score averaging → cross-method but limited to gradient-family methods only, no binary consensus\n- **CSS:** uses multiple independent discovery methods spanning different algorithm families (gradient-based, iterative patching, mask optimization) → true cross-family method robustness with binary consensus\n- CSS argument: method diversity across algorithm families captures a broader space of inductive biases than either threshold variation (CIRCUS) or intra-family score averaging (Mondorf). CIRCUS inherits the blind spots of its single underlying method; Mondorf stays within the gradient family. CSS's methods have structurally different failure modes, and binary consensus avoids score calibration issues."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T02:22:34.312643+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T02:22:34.312890+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
  "old_string": "4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level",
  "new_string": "4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level\n6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md",
    "old_string": "4. **Consensus/stability approaches** (CIRCUS, Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing) — acknowledge parallel direction, note CSS works at component level",
    "new_string": "4. **Consensus/stability approaches** (CIRCUS, Mondorf et al., Certified Circuits) — position CSS against alternatives\n5. **Feature-level circuits** (Sparse Feature Circuits, Transcoders, Circuit Tracing, PIE) — acknowledge parallel direction, note CSS works at component level\n6. **Method variants and benchmarks** (EAP-GP, GIM, MIB) — contextualize method landscape diversity that motivates cross-family consensus"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T02:22:34.313176+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T02:22:34.313356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T02:22:34.313604+00:00_

1	# Related Work Literature Survey for CSS (Cross-method Structural Consensus)
2	
3	> Generated: 2026-05-13 | Target: EMNLP 2026 Main (ARR deadline 2026-05-25)
4	
5	---
6	
7	## Direction 1: Cross-method Consensus / Ensemble in Mechanistic Interpretability
8	
9	### 1.1 CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles
10	- **Authors:** Swapnil Parekh
11	- **Year:** 2026 (arXiv: 2603.00523)
12	- **Venue:** arXiv preprint (Feb 2026)
13	- **Core findings:** Reframes circuit discovery as an uncertainty-quantification problem. Constructs an ensemble of attribution graphs by pruning a *single* raw attribution run under multiple threshold configurations, assigns each edge a stability score (fraction of configs retaining it), and extracts a strict-consensus circuit (edges appearing in all views). On Gemma-2-2B and Llama-3.2-1B, strict consensus circuits are ~40× smaller than the union while retaining comparable explanatory power. Consensus-identified nodes beat matched non-consensus controls in causal relevance (p=0.0004).
14	- **Relation to CSS:** **直接竞争 (Primary competitor)**. CIRCUS varies pruning thresholds on a single attribution method to build consensus; CSS uses multiple independent discovery methods (EAP-IG, EP, ACDC/IFR). Key differentiators: (1) CSS captures cross-method agreement (different algorithms with different inductive biases), not just threshold robustness within one method; (2) CSS uses binary agreement rather than fractional stability scores; (3) CSS explicitly tests distribution-shift robustness. Must position CSS as complementary/stronger: method diversity > threshold diversity.
15	
16	### 1.2 Certified Circuits: Stability Guarantees for Mechanistic Circuits
17	- **Authors:** Alaa Anani, Tobias Lorenz, Bernt Schiele, et al.
18	- **Year:** 2026 (arXiv: 2602.22968)
19	- **Venue:** arXiv preprint (Feb 2026)
20	- **Core findings:** Wraps any black-box discovery algorithm with randomized data subsampling to certify that circuit component 
…[truncated 22397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-13T02:22:34.313861+00:00_

文件完整且格式正确。总结：

---

### 新增条目（4 篇）

| 论文 | 位置 | 类型 |
|------|------|------|
| **Mondorf et al. (2510.06811)** | §1.5 (Direction 1) | 直接竞争，详细讨论 4 点局限 |
| **PIE (2604.16889)** | Additional Relevant Work | 互补，CLT-native 方法 |
| **EAP-GP (2502.06852)** | Additional Relevant Work | 互补，gradient 族变体 |
| **GIM (2505.17630)** | Additional Relevant Work | 互补，MIB 顶分方法 |

### 修改条目

- **Takeaway #2**: 从仅讨论 CIRCUS 扩展为同时讨论 CIRCUS + Mondorf et al. 两个竞争者
- **Takeaway #6**: 新增第 4 项加入 Mondorf et al.，第 5 项加入 PIE，新增第 6 项 "Method variants and benchmarks"

### Takeaway #5 修改前后

**修改前：**
> Distribution-shift robustness is a novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS's off-diagonal evaluation (train on distribution A, test on distribution B) is a distinctive contribution.

**修改后：**
> Distribution-shift robustness is a **planned** novel evaluation angle — No existing work systematically evaluates whether consensus circuits maintain faithfulness under distribution shift. CSS 计划在 Phase 2 中系统性评估 consensus circuits 在分布偏移下的鲁棒性（off-diagonal evaluation: train on distribution A, test on distribution B），这将成为一个独特的贡献方向（Phase 2 planned, cf. D015）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_literature-merge-fix_20260513T022004"
}
```

</details>

---
