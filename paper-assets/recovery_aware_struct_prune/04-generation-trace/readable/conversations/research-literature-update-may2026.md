# research literature update may2026

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/chats/worker_research_literature_update_may2026_20260514T132612.jsonl`
- **Structured JSON:** [`6d2fcbc1995b1c08c464.json`](../../sessions/6d/6d2fcbc1995b1c08c464.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

69 recorded events

### Tool call

_source line 1 · 2026-05-14T13:30:56.511797+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,TodoWrite",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,TodoWrite",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T13:30:56.512134+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T13:30:56.512355+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'in_progress', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'pending', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'pending', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'in_progress', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'pending', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'pending', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T13:30:56.512532+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T13:30:56.512663+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T13:30:56.512949+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml\", \"content\": \"papers:\\n  # === Direct Competitors ===\\n  - id: self_healing_2025\\n    title: \\\"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: direct-competitor\\n    role: \\\"RLVR recovery baseline\\\"\\n    relevance: 9\\n    key_finding: \\\"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\\\"\\n    our_relation: \\\"We extend beyond single sparsity ratio and add CKA-guided pruning selection\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: resp_2025\\n    title: \\\"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\\\"\\n    year: 2025\\n    venue: \\\"arXiv Dec 2025\\\"\\n    category: direct-competitor\\n    role: \\\"Structured pruning for reasoning without recovery\\\"\\n    relevance: 8\\n    key_finding: \\\"GSM8K 81.3% at 40% sparsity via self-reflective importance\\\"\\n    our_relation: \\\"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: grasprune_2026\\n    title: \\\"GRASPrune: Global Gating-based Structural Pruning for LLMs\\\"\\n    year: 2026\\n    venue: \\\"ACL 2026 Main\\\"\\n    category: direct-competitor\\n    role: \\\"SOTA budgeted structural pruning\\\"\\n    relevance: 8\\n    key_finding: \\\"Global gating achieves best structured pruning under budget constraints\\\"\\n    our_relation: \\\"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: opsd_2026\\n    title: \\\"OPSD: One-shot Post-RL Structured Distillation\\\"\\n    year: 2026\\n    venue: \\\"arXiv May 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Post-RL compression via distillation\\\"\\n    relevance: 7\\n    key_finding: \\\"Compress post-RL mode
…[truncated 7647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T13:30:56.513164+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'in_progress', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'pending', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'in_progress', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'pending', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T13:30:56.513339+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T13:30:56.513468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 \"structured pruning\" reasoning LLM",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 \"structured pruning\" reasoning LLM",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T13:30:56.513591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 RLVR pruning OR compression language model",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 RLVR pruning OR compression language model",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T13:30:56.513709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2024 2025 2026 CKA pruning neural network",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2024 2025 2026 CKA pruning neural network",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T13:30:56.513826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2025 2026 \"recovery\" \"structured pruning\" language model",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2025 2026 \"recovery\" \"structured pruning\" language model",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T13:30:56.513949+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 GRPO pruning OR compression LLM",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 GRPO pruning OR compression LLM",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T13:30:56.514066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 \"test-time compute\" pruning language model",
  "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 \"test-time compute\" pruning language model",
    "allowed_domains": "['arxiv.org', 'scholar.google.com', 'semanticscholar.org', 'huggingface.co']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T13:30:56.514208+00:00_

Web search results for query: "arxiv 2026 "structured pruning" reasoning LLM"

Links: [{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/pdf/2603.13418"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.13418"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.08065"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma","url":"https://arxiv.org/pdf/2305.11627"}]

I found several recent arxiv papers (from 2026) related to structured pruning and reasoning LLMs. Here are the key results:

## Recent Papers on Structured Pruning for Reasoning LLMs

1. **STOP: Structured On-Policy Pruning** - This paper uses structured reasoning interfaces and annotation, segmenting traces into semantically coherent reasoning nodes using discourse and formatting rules.

2. **GPrune-LLM: Generalization-Aware Structured Pruning** - Structured pruning is widely used to compress
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T13:30:56.514446+00:00_

Web search results for query: "arxiv 2024 2025 2026 CKA pruning neural network"

Links: [{"title":"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/html/2408.13482v1"},{"title":"[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/abs/2408.13482"},{"title":"arXiv:2506.04513v1 [cs.CV] 4 Jun 2025","url":"https://arxiv.org/pdf/2506.04513"},{"title":"A Survey on Deep Neural Network Pruning","url":"https://arxiv.org/pdf/2308.06767"},{"title":"Integrating Pruning with Quantization for Efficient Deep Neural Networks Compression","url":"https://arxiv.org/html/2509.04244v1"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures","url":"https://arxiv.org/pdf/2504.13296"},{"title":"A Paradigm for Density Discovery in Sparse Neural Networks","url":"https://arxiv.org/pdf/2509.25665"},{"title":"[2101.09671] Pruning and Quantization for Deep Neural Network Acceleration: A Survey","url":"https://arxiv.org/abs/2101.09671"},{"title":"Pruning vs Quantization: Which is Better?","url":"https://arxiv.org/pdf/2307.02973"},{"title":"Pruning and Quantization Impact on Graph Neural Networks","url":"https://arxiv.org/html/2510.22058v1"}]

I found several relevant papers on arXiv related to CKA-based pruning of neural networks. Here are the key findings:

## Recent CKA-Based Pruning Research

**1. MPruner (2024)**
MPruner utilizes layer clustering with the Centered Kernel Alignment (CKA) similarity metric, allowing incorporation of global information from the neural network for more precise and efficient layer-wise pruning. MPruner achieved up to a 50% reduction in parameters and memory usage for CNN and transformer-based models, with minimal to no loss in accuracy.

**2. CKA-Based Pruning Strategy (2025)**
A more recent paper from June 2025 describes using Centered Kernel Alignment (CKA) as a similarity metric to evaluate resulting subnetworks t
…[truncated 706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T13:30:56.514623+00:00_

Web search results for query: "arxiv 2026 RLVR pruning OR compression language model"

Links: [{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"[2601.09694] LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/abs/2601.09694"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/pdf/2601.09694"},{"title":"One-for-All Pruning: A Universal Model for Customized Compression of Large Language Models","url":"https://arxiv.org/html/2505.12216"}]

The web search has returned several relevant results about language model compression, pruning, and related techniques from 2026. Here are the key findings:

## Main Results

**RLVR-related paper:**
A paper titled "Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR" introduces arrol (Accelerating RLVR via online Rollout Pruning), an online rollout pruning
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T13:30:56.514790+00:00_

Web search results for query: "arxiv 2025 2026 "recovery" "structured pruning" language model"

Links: [{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models","url":"https://arxiv.org/html/2510.18030"},{"title":"[2505.22689] SlimLLM: Accurate Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2505.22689"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2507.20749] Investigating Structural Pruning and Recovery Techniques for Compressing Multimodal Large Language Models: An Empirical Study","url":"https://arxiv.org/abs/2507.20749"},{"title":"Investigating Structural Pruning and Recovery Techniques ...","url":"https://arxiv.org/pdf/2507.20749"},{"title":"[2510.07782] RCPU: Rotation-Constrained Error Compensation for Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2510.07782"},{"title":"Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.08065"}]

Based on the search results, I found several recent arXiv papers (2025-2026) on structured pruning of language models with a focus on recovery techniques:

## Key Papers Found:

1. **Structural Pruning of Large Vision Language Models** - Published April 27, 2026 (arxiv 2604.24380), this comprehensive study investigates layerwise and widthwise pruning paired with supervised finetuning and
…[truncated 1249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T13:30:56.514955+00:00_

Web search results for query: "arxiv 2026 "test-time compute" pruning language model"

Links: [{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"ICLR 2026 Test-Time Updates (TTU) Workshop","url":"https://arxiv.org/pdf/2603.19296"},{"title":"[2602.01070] What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/abs/2602.01070"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach","url":"https://arxiv.org/abs/2502.05171"},{"title":"Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference","url":"https://arxiv.org/html/2603.20224"},{"title":"[2603.20224] Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference","url":"https://arxiv.org/abs/2603.20224"}]

Based on the search results, here are the relevant papers on test-time compute, pruning, and language models from arXiv in 2026:

## Key Papers Found:

**1. "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"** (2604.25098)

While current Large Language Models (LLMs) exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), their massive parameter counts and high inference costs have motivated the development of pruning methods that can reduce model size without sacrificing performance. Experiments across four reasoning benchmarks on t
…[truncated 1086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T13:30:56.515126+00:00_

Web search results for query: "arxiv 2026 GRPO pruning OR compression LLM"

Links: [{"title":"[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/abs/2603.04135"},{"title":"Compute Where it Counts: Self Optimizing Language Models","url":"https://arxiv.org/html/2605.10875"},{"title":"Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs","url":"https://arxiv.org/html/2604.05643v2"},{"title":"Compressing Chain-of-Thought in LLMs via Step Entropy","url":"https://arxiv.org/html/2508.03346v1"},{"title":"[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.13418"},{"title":"Making Slow Thinking Faster: Compressing LLM Chain-of-Thought via Step Entropy","url":"https://arxiv.org/html/2508.03346"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.13418"},{"title":"Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization","url":"https://arxiv.org/html/2602.10048"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/pdf/2601.09694"}]

Here are the search results for your query about GRPO, pruning, and LLM compression from arXiv in 2026:

## Key Papers Found:

1. **Dynamic Pruning Policy Optimization (DPPO)** - A framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction, significantly accelerating GRPO training without altering the optimization objective. On Qwen3-4B trained on MATH, DPPO achieves 2.37× training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.

2. **Self-Optimizing Language Models (SOL)** - Each action instantiates a 
…[truncated 1189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T13:30:56.515348+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.13165 STOP structured on-policy pruning reasoning",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.13165 STOP structured on-policy pruning reasoning",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T13:30:56.515493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T13:30:56.515617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.24380 structural pruning vision language models recovery",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.24380 structural pruning vision language models recovery",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T13:30:56.515735+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.24840 \"prune as you generate\" online rollout RLVR",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.24840 \"prune as you generate\" online rollout RLVR",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T13:30:56.515896+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.08065 deterministic differentiable structured pruning LLM",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.08065 deterministic differentiable structured pruning LLM",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T13:30:56.516066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T13:30:56.516213+00:00_

Web search results for query: "arxiv 2604.24380 structural pruning vision language models recovery"

Links: [{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration","url":"https://arxiv.org/html/2404.02424v2"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"Hierarchical Safety Realignment: Lightweight Restoration of Safety in Pruned Large Vision-Language Models","url":"https://arxiv.org/html/2505.16104v1"},{"title":"[2404.02424] Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration","url":"https://arxiv.org/abs/2404.02424"},{"title":"[2604.16557] S-GRPO: Unified Post-Training for Large Vision-Language Models","url":"https://arxiv.org/abs/2604.16557"},{"title":"[2604.09687] Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models","url":"https://arxiv.org/abs/2604.09687"},{"title":"[2604.14629] Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models","url":"https://arxiv.org/abs/2604.14629"}]

Based on the search results, I found the paper you're looking for. arXiv:2604.24380 is titled "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency", with authors Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, and Zeynep 
…[truncated 700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T13:30:56.516469+00:00_

Web search results for query: "arxiv 2605.13165 STOP structured on-policy pruning reasoning"

Links: [{"title":"[2605.13165] STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/abs/2605.13165"},{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning","url":"https://arxiv.org/html/2605.07804v1"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning","url":"https://arxiv.org/html/2604.16029"},{"title":"Structured Pruning for Diverse Best-of-𝑁 Reasoning Optimization","url":"https://arxiv.org/html/2506.03978v1"},{"title":"Post Reasoning: Improving the Performance of Non-Thinking Models at No Cost","url":"https://arxiv.org/html/2605.06165v1"},{"title":"Think Clearly: Improving Reasoning via Redundant Token Pruning","url":"https://arxiv.org/html/2507.08806v1"},{"title":"Think, Prune, Train, Improve: Scaling Reasoning Without Scaling Models","url":"https://arxiv.org/html/2504.18116v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"}]

Based on the search results, I found information about the paper arxiv 2605.13165 on STOP (Structured On-Policy Pruning).

## Overview

STOP (Structured On-policy Pruning) is an on-policy algorithm for analyzing and pruning long-form reasoning traces.

## Problem Being Addressed

Long chain-of-thought (Long CoT) reasoning improves performance on multi-step problems, but it also induces overthinking: models often generate low-yield reasoning that increases inference cost and latency. This inefficiency is especially problematic in low-data fine-tuning regimes, wher
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T13:30:56.516677+00:00_

Web search results for query: "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO"

Links: [{"title":"[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/abs/2603.04135"},{"title":"Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/html/2603.04135"},{"title":"Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models","url":"https://arxiv.org/html/2512.15347v1"},{"title":"A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models","url":"https://arxiv.org/html/2508.01548"},{"title":"OPERA: Online Data Pruning for Efficient Retrieval Model Adaptation","url":"https://arxiv.org/html/2603.17205"},{"title":"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/html/2603.24840"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"Large-scale Dataset Pruning with Dynamic Uncertainty","url":"https://arxiv.org/html/2306.05175v3"},{"title":"[2512.15347] Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models","url":"https://arxiv.org/abs/2512.15347"}]

I found the paper arxiv 2603.04135. Here are the key details:

**Title:** Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization

**Main Contribution:** DPPO is a framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction. By incorporating mathematically derived rescaling factors, DPPO significantly accelerates GRPO training without altering the optimization objective of the full-batch baseline.

**Problem Addressed:** Group Relative Policy Optimization (GRPO) effectively scales L
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T13:30:56.516853+00:00_

Web search results for query: "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures"

Links: [{"title":"[2504.13296] Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis","url":"https://arxiv.org/abs/2504.13296"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures","url":"https://arxiv.org/pdf/2504.13296"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis","url":"https://arxiv.org/html/2504.13296"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=900&show=2000"},{"title":"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/html/2408.13482v1"},{"title":"Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation","url":"https://arxiv.org/html/2601.19794v1"},{"title":"Pruning Everything, Everywhere, All at Once","url":"https://arxiv.org/html/2506.04513"},{"title":"Effective Layer Pruning Through Similarity Metric Perspective","url":"https://arxiv.org/html/2405.17081v2"},{"title":"[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/abs/2408.13482"},{"title":"[2601.19794] Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation","url":"https://arxiv.org/abs/2601.19794"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2504.13296 is titled "Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis". The paper was submitted on April 17, 2025, with a revised version (v2) on July 20, 2025, and is authored by Ganesh Sundaram, Jonas Ulmen, and Daniel Görges.

The paper addresses how comprehensive structured pruning frameworks based on parameter dependency analysis can reduce model si
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T13:30:56.517032+00:00_

Web search results for query: "arxiv 2603.24840 "prune as you generate" online rollout RLVR"

Links: [{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/html/2603.24840"},{"title":"Thinking in Streaming Video","url":"https://arxiv.org/html/2603.12938"},{"title":"Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models","url":"https://arxiv.org/html/2603.12248"},{"title":"Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.01321"},{"title":"Part II: ROLL Flash – Accelerating RLVR and Agentic Training with Asynchrony","url":"https://arxiv.org/html/2510.11345v1"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse","url":"https://arxiv.org/html/2509.25808v1"},{"title":"Reaching Beyond the Mode: RL for Distributional Reasoning in Language Models","url":"https://arxiv.org/html/2603.24844"},{"title":"Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning","url":"https://arxiv.org/html/2603.09803"},{"title":"Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning","url":"https://arxiv.org/html/2602.14338"}]

Based on the search results, I found the arXiv paper 2603.24840. Here's what the paper is about:

## Paper Overview

ARRoL (Accelerating RLVR via online RoLlout Pruning) is an online rollout pruning method that prunes rollouts during generation while explicitly steering the surviving ones more correctness-balanced to enhance learning signals.

## Key Problems Addressed

Methods such as GRPO and DAPO suffer from substantial computational cost since they rely on sampling many rollouts for each prompt. Moreover, in RLVR the relative advantage is often 
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T13:30:56.517199+00:00_

Web search results for query: "arxiv 2603.08065 deterministic differentiable structured pruning LLM"

Links: [{"title":"[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.08065"},{"title":"Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.08065"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.13418"},{"title":"Learnable Permutation for Structured Sparsity on Transformer Models","url":"https://arxiv.org/html/2601.22980"},{"title":"[2603.23985] Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score","url":"https://arxiv.org/abs/2603.23985"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"},{"title":"Systematic Characterization of Minimal Deep Learning Architectures: A Unified Analysis of Convergence, Pruning, and Quantization","url":"https://arxiv.org/html/2601.17987"},{"title":"Greedy Output Approximation: Towards Efficient Structured Pruning for LLMs Without Retraining","url":"https://arxiv.org/html/2407.19126v1"},{"title":"Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score","url":"https://arxiv.org/html/2603.23985"}]

I found the paper! Here's what I can tell you about arXiv 2603.08065:

## Paper Overview

The paper is titled "Deterministic Differentiable Structured Pruning for Large Language Models" and was submitted on March 9, 2026 by authors including Weiyu Huang, Pengle Zhang, Xiaolu Zhang, Jun Zhou, Jun Zhu, and Jianfei Chen.

## Main Contribution

Structured pruning reduces LLM inference cost by removing low-importance architectural components
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T13:30:56.517408+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.27115 task-specific neurons model collapse recovery pruning",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.27115 task-specific neurons model collapse recovery pruning",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T13:30:56.517540+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 \"structured pruning\" LLM reasoning recovery May April new",
  "allowed_domains": "['arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 \"structured pruning\" LLM reasoning recovery May April new",
    "allowed_domains": "['arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T13:30:56.517662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2026 \"functional overlap\" OR \"functional similarity\" pruning LLM",
  "allowed_domains": "['arxiv.org', 'scholar.google.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2026 \"functional overlap\" OR \"functional similarity\" pruning LLM",
    "allowed_domains": "['arxiv.org', 'scholar.google.com']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T13:30:56.517857+00:00_

Web search results for query: "arxiv 2026 "functional overlap" OR "functional similarity" pruning LLM"

Links: [{"title":"[2311.03366] Functional Overlap Reranking for Neural Code Generation","url":"https://arxiv.org/abs/2311.03366"}]

I found one result related to "functional overlap," though it's focused on neural code generation rather than LLM pruning. The search returned:

A paper on functional overlap reranking that quantifies the functional overlap between solution clusters to provide a better ranking strategy for code solutions.

However, this result (arxiv 2311.03366) is from 2023, not 2026, and appears to be about code generation rather than pruning language models. The search query you provided may not have many results available yet, as 2026 papers may still be limited in the arxiv database. If you're looking for more recent work on functional similarity or overlap in LLM pruning specifically, you might try searching with different keywords or without the specific year constraint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T13:30:56.518018+00:00_

Web search results for query: "arxiv 2604.27115 task-specific neurons model collapse recovery pruning"

Links: [{"title":"[2604.27115] Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/abs/2604.27115"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks","url":"https://arxiv.org/html/2604.24637"},{"title":"The Exploration of Neural Collapse under Imbalanced Data","url":"https://arxiv.org/html/2411.17278v1"},{"title":"Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model","url":"https://arxiv.org/html/2506.05801"},{"title":"The Persistence of Neural Collapse Despite Low-Rank Bias: An Analytic Perspective Through Unconstrained Features","url":"https://arxiv.org/html/2410.23169v1"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://arxiv.org/html/2405.17767v1"},{"title":"[2604.24637] Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks","url":"https://arxiv.org/abs/2604.24637"},{"title":"Exploring The Neural Burden In Pruned Models: An Insight Inspired By Neuroscience","url":"https://arxiv.org/html/2407.16716v1"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"}]

Based on the search results, I found the paper you're looking for. Here's what arxiv 2604.27115 is about:

## Paper Overview

The paper is titled "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models", authored by M. K. Khalidi Siam and colleagues from BRAC University.

## Res
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T13:30:56.518189+00:00_

Web search results for query: "arxiv 2026 "structured pruning" LLM reasoning recovery May April new"

Links: [{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/pdf/2603.13418"},{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma","url":"https://arxiv.org/pdf/2305.11627"},{"title":"Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs","url":"https://arxiv.org/html/2604.05643v2"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"}]

Based on the search results, I found several recent arxiv papers from 2026 related to structured pruning, LLM reasoning, and recovery. Here are the most relevant findings:

## Key Papers on Structured Pruning and LLM Reasoning Recovery (2026)

1. **"Structural Pruning of Large Vision Language Models"** (April 2026)
   This paper disentangles the effects of pruning on modality alignment versus core language reasoning, and investigates recovery strategies including supervised finetuning (SFT) of th
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T13:30:56.518472+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'in_progress', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'in_progress', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'pending', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T13:30:56.518648+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T13:30:56.518776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T13:30:56.518987+00:00_

1	papers:
2	  # === Direct Competitors ===
3	  - id: self_healing_2025
4	    title: "Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning"
5	    year: 2025
6	    venue: "under review"
7	    category: direct-competitor
8	    role: "RLVR recovery baseline"
9	    relevance: 9
10	    key_finding: "RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%"
11	    our_relation: "We extend beyond single sparsity ratio and add CKA-guided pruning selection"
12	    arxiv_id: ""
13	
14	  - id: resp_2025
15	    title: "RESP: Self-Reflective Structured Pruning for Reasoning LLMs"
16	    year: 2025
17	    venue: "arXiv Dec 2025"
18	    category: direct-competitor
19	    role: "Structured pruning for reasoning without recovery"
20	    relevance: 8
21	    key_finding: "GSM8K 81.3% at 40% sparsity via self-reflective importance"
22	    our_relation: "No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity"
23	    arxiv_id: ""
24	
25	  - id: grasprune_2026
26	    title: "GRASPrune: Global Gating-based Structural Pruning for LLMs"
27	    year: 2026
28	    venue: "ACL 2026 Main"
29	    category: direct-competitor
30	    role: "SOTA budgeted structural pruning"
31	    relevance: 8
32	    key_finding: "Global gating achieves best structured pruning under budget constraints"
33	    our_relation: "GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top"
34	    arxiv_id: ""
35	
36	  - id: opsd_2026
37	    title: "OPSD: One-shot Post-RL Structured Distillation"
38	    year: 2026
39	    venue: "arXiv May 2026"
40	    category: direct-competitor
41	    role: "Post-RL compression via distillation"
42	    relevance: 7
43	    key_finding: "Compress post-RL model in one shot via structured distillation"
44	    our_relation: "Distillation-based vs our pruning+recovery approach; complementary"
45	    arxiv_id: ""
46	
47	  - id: doing_more_with_less_2026
48	    title: "Doing More With Less: Revisiting the Effectiveness of LLM Prun
…[truncated 7019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T13:30:56.519171+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===",
  "new_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    arxiv_id: \"2603.24840\"\n\n  # === Background / Theory ==="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "old_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===",
    "new_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    arxiv_id: \"2603.24840\"\n\n  # === Background / Theory ==="
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T13:30:56.519417+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T13:30:56.519563+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"",
  "new_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    arxiv_id: \"2604.24380\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "old_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"",
    "new_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    arxiv_id: \"2604.24380\""
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T13:30:56.519767+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T13:30:56.519914+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'in_progress', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'in_progress', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'pending', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T13:30:56.520065+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T13:30:56.520187+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T13:30:56.520326+00:00_

_project
correlation_analysis.py
manifest.yaml
mvp_progress_20260514.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T13:30:56.520470+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md",
  "content": "# Related Work Notes — RASP (Recovery-Aware Structured Pruning)\n\n> Prepared 2026-05-14. Literature map: 24 papers. Target: EMNLP 2026 ARR May 25.\n\n---\n\n## 1. Structured Pruning for LLMs\n\n**Core methods.** LLM-Pruner (Ma et al., 2023) established the structured pruning pipeline for LLMs: dependency-graph-based group identification → importance scoring → one-shot removal → LoRA recovery. GRASPrune [`grasprune_2026`] advances this with global gating under budget constraints, achieving SOTA at ACL 2026 — we use it as our pruning backbone. GPrune-LLM [`gprune_llm_2026`] addresses calibration bias via cross-distribution neuron behavior partitioning. DieT [`diet_2026`] proposes dimension-wise task-specific importance for width pruning at 20–40% sparsity. DDP [`ddp_2026`] introduces deterministic differentiable mask optimization, eliminating the stochastic train-test mismatch of hard-concrete relaxations. Bonsai [`bonsai_2025`] shows competitive gradient-free structured pruning.\n\n**Pruning for reasoning models.** RESP [`resp_2025`] achieves GSM8K 81.3% at 40% structured sparsity via self-reflective importance, but applies no post-pruning recovery. From LLMs to LRMs [`from_llms_to_lrms_2026`] demonstrates that width pruning preserves reasoning better than depth pruning — motivating our width-level focus. Doing More With Less [`doing_more_with_less_2026`] shows that structured pruning significantly degrades test-time scaling (TTS) performance while unstructured pruning can augment it, directly motivating why structured pruning needs a recovery mechanism.\n\n**Usable claims:**\n- Structured pruning degrades reasoning more than general NLP tasks → [`doing_more_with_less_2026`, `resp_2025`]\n- Width pruning > depth pruning for reasoning preservation → [`from_llms_to_lrms_2026`]\n- Global importance scoring outperforms local → [`grasprune_2026`, `gprune_llm_2026`]\n- Current methods lack recovery-awareness in the pruning decision itself → gap we fill\n\n---\n\n## 2. Post-Pruning Recovery\n\n**RLVR recovery.** Self-Healing [`self_healing_2025`] is our primary baseline: RLVR recovers 95%+ reasoning at 25% compression where SFT only reaches ~80%. This is the first work to apply RL-based recovery to pruned reasoning models, but it operates at a single sparsity ratio without predicting recoverability.\n\n**Alternative recovery strategies.** RAC [`rac_2025`] reconstructs chain-of-thought for pruned reasoning models (NeurIPS 2025), showing CoT-targeted recovery works for unstructured/2:4 sparsity. PASER [`paser_2025`] demonstrates that selective training data improves recovery efficiency. PAT [`pat_2025`] co-optimizes pruning mask and fine-tuning jointly (AAAI 2025). The VLM pruning study [`pruning_vlm_recovery_2026`] finds that width pruning + KD recovery outperforms layer pruning + SFT, validating our paradigm choice.\n\n**Scaling and theory.** P² Law [`p2_law_2025`] establishes predictable scaling for recovery compute/data (ACL 2025) — we extend this to RLVR-specific scaling. RL Squeezes, SFT Expands [`rl_squeezes_2026`] (ICLR 2026) provides the theoretical basis: RLVR compresses representations while SFT expands them, explaining why RLVR is the superior recovery mechanism post-pruning.\n\n**Task-specific neuron dynamics.** Task-specific neuron analysis [`task_neurons_2026`] finds that removing just ~10% of task-critical neurons causes complete performance collapse, with a robustness threshold at 15–20%. Fine-tuning substantially recovers performance across pruning levels — supporting the need for recovery-aware pruning that identifies which neurons are critical.\n\n**Usable claims:**\n- RLVR >> SFT for post-pruning recovery → [`self_healing_2025`]\n- RLVR compresses representations (theoretical justification) → [`rl_squeezes_2026`]\n- Recovery compute follows scaling laws → [`p2_law_2025`]\n- Task-specific neurons exist; small removal causes collapse → [`task_neurons_2026`]\n- No prior work predicts recoverability before pruning → gap we fill\n\n---\n\n## 3. CKA in Neural Networks\n\n**Layer-level CKA for pruning.** MPruner [`mpruner_2024`] uses CKA similarity between consecutive layers to identify redundant layers for removal, achieving 50% parameter reduction with minimal accuracy loss. Lachance's thesis [`lachance_thesis_2024`] provides theoretical grounding that CKA layer similarity correlates with pruning recoverability. MIPP [`mipp_2024`] uses mutual information (related to CKA) as a pruning criterion.\n\n**Our extension.** We adapt CKA from layer-level redundancy detection to width-level functional overlap prediction. Specifically, we compute CKA between pre- and post-pruning intermediate representations to predict whether RLVR can recover the pruned model — a novel application of CKA as a recoverability signal rather than an importance signal.\n\n**Usable claims:**\n- CKA identifies redundant layers → [`mpruner_2024`]\n- CKA correlates with recoverability → [`lachance_thesis_2024`]\n- No prior work uses CKA for width-level recoverability prediction → our contribution\n\n---\n\n## 4. RLVR / Reasoning Enhancement\n\n**RLVR foundations.** RL Squeezes [`rl_squeezes_2026`] shows RLVR and SFT have fundamentally different mechanisms (compression vs expansion). Self-Distilled RLVR [`self_distilled_rlvr_2026`] improves RLVR training stability and sample efficiency via self-distillation. OPSD [`opsd_2026`] compresses post-RL models via one-shot structured distillation — a complementary approach to our pruning+recovery pipeline.\n\n**RLVR training efficiency.** DPPO [`dppo_2026`] achieves 2.37× GRPO speedup via importance-sampling-based rollout pruning while preserving unbiased gradients. ARRoL [`arrol_2026`] uses a lightweight quality head to predict and prune low-value rollouts during RLVR generation. Both are complementary to our work — they could accelerate the GRPO recovery phase in RASP.\n\n**Usable claims:**\n- RLVR compresses while SFT expands → [`rl_squeezes_2026`]\n- GRPO training can be accelerated 2× without accuracy loss → [`dppo_2026`, `arrol_2026`]\n- Post-RL distillation is complementary to pruning+recovery → [`opsd_2026`]\n\n---\n\n## 5. Our Positioning: RASP Fills the Gap\n\n### Gap analysis\n\nThe literature reveals a clear gap at the intersection of three directions:\n\n1. **Structured pruning for LLMs** is mature (GRASPrune, GPrune-LLM, Bonsai, DDP) but no method accounts for post-pruning recoverability when making pruning decisions.\n2. **Post-pruning recovery** via RLVR is demonstrated (Self-Healing) but operates as a black-box second stage — the pruning step is unaware of whether the removed structures can be recovered.\n3. **CKA-based analysis** has been applied to layer-level redundancy (MPruner) but never to predict width-level recoverability under RLVR.\n\n### RASP's contribution\n\nRASP bridges these three threads by introducing CKA functional overlap as a predictive signal for RLVR recoverability. Concretely:\n\n- **Before pruning:** We compute CKA overlap between candidate pruning configurations and the full model to estimate how much functional capacity is preserved. High CKA overlap → the pruned model retains the representational substrate that RLVR can rebuild upon.\n- **During pruning:** CKA scores guide which structures to remove, preferring configurations that maximize predicted recoverability at the target sparsity ratio.\n- **After pruning:** RLVR (specifically GRPO) recovers reasoning capability, and we show that CKA-guided pruning requires less recovery compute than importance-only pruning.\n\nThis is distinct from: (a) Self-Healing, which uses RLVR recovery but with standard importance-based pruning; (b) RESP/GRASPrune, which optimize pruning quality without considering recovery; (c) MPruner, which uses CKA for layer redundancy, not width-level recoverability.\n\n### Narrative for Related Work section\n\nWe position RASP as the first method to close the loop between pruning and recovery by making the pruning decision recovery-aware. While prior work treats pruning and recovery as independent stages (prune first, recover later), RASP shows that predicting recoverability — via CKA functional overlap — at the pruning stage yields better final accuracy at the same sparsity ratio and recovery budget. This is analogous to how PAT co-optimizes pruning and tuning, but RASP operates at a higher level: it does not require joint optimization, instead using CKA as a cheap predictive proxy that can be computed before any training begins.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md",
    "content": "# Related Work Notes — RASP (Recovery-Aware Structured Pruning)\n\n> Prepared 2026-05-14. Literature map: 24 papers. Target: EMNLP 2026 ARR May 25.\n\n---\n\n## 1. Structured Pruning for LLMs\n\n**Core methods.** LLM-Pruner (Ma et al., 2023) established the structured pruning pipeline for LLMs: dependency-graph-based group identification → importance scoring → one-shot removal → LoRA recovery. GRASPrune [`grasprune_2026`] advances this with global gating under budget constraints, achieving SOTA at ACL 2026 — we use it as our pruning backbone. GPrune-LLM [`gprune_llm_2026`] addresses calibration bias via cross-distribution neuron behavior partitioning. DieT [`diet_2026`] proposes dimension-wise task-specific importance for width pruning at 20–40% sparsity. DDP [`ddp_2026`] introduces deterministic differentiable mask optimization, eliminating the stochastic train-test mismatch of hard-concrete relaxations. Bonsai [`bonsai_2025`] shows competitive gradient-free structured pruning.\n\n**Pruning for reasoning models.** RESP [`resp_2025`] achieves GSM8K 81.3% at 40% structured sparsity via self-reflective importance, but applies no post-pruning recovery. From LLMs to LRMs [`from_llms_to_lrms_2026`] demonstrates that width pruning preserves reasoning better than depth pruning — motivating our width-level focus. Doing More With Less [`doing_more_with_less_2026`] shows that structured pruning significantly degrades test-time scaling (TTS) performance while unstructured pruning can augment it, directly motivating why structured pruning needs a recovery mechanism.\n\n**Usable claims:**\n- Structured pruning degrades reasoning more than general NLP tasks → [`doing_more_with_less_2026`, `resp_2025`]\n- Width pruning > depth pruning for reasoning preservation → [`from_llms_to_lrms_2026`]\n- Global importance scoring outperforms local → [`grasprune_2026`, `gprune_llm_2026`]\n- Current methods lack recovery-awareness in the pruning decision itself → gap we fill\n\n---\n\n## 2. Post-Pruning Recovery\n\n**RLVR recovery.** Self-Healing [`self_healing_2025`] is our primary baseline: RLVR recovers 95%+ reasoning at 25% compression where SFT only reaches ~80%. This is the first work to apply RL-based recovery to pruned reasoning models, but it operates at a single sparsity ratio without predicting recoverability.\n\n**Alternative recovery strategies.** RAC [`rac_2025`] reconstructs chain-of-thought for pruned reasoning models (NeurIPS 2025), showing CoT-targeted recovery works for unstructured/2:4 sparsity. PASER [`paser_2025`] demonstrates that selective training data improves recovery efficiency. PAT [`pat_2025`] co-optimizes pruning mask and fine-tuning jointly (AAAI 2025). The VLM pruning study [`pruning_vlm_recovery_2026`] finds that width pruning + KD recovery outperforms layer pruning + SFT, validating our paradigm choice.\n\n**Scaling and theory.** P² Law [`p2_law_2025`] establishes predictable scaling for recovery compute/data (ACL 2025) — we extend this to RLVR-specific scaling. RL Squeezes, SFT Expands [`rl_squeezes_2026`] (ICLR 2026) provides the theoretical basis: RLVR compresses representations while SFT expands them, explaining why RLVR is the superior recovery mechanism post-pruning.\n\n**Task-specific neuron dynamics.** Task-specific neuron analysis [`task_neurons_2026`] finds that removing just ~10% of task-critical neurons causes complete performance collapse, with a robustness threshold at 15–20%. Fine-tuning substantially recovers performance across pruning levels — supporting the need for recovery-aware pruning that identifies which neurons are critical.\n\n**Usable claims:**\n- RLVR >> SFT for post-pruning recovery → [`self_healing_2025`]\n- RLVR compresses representations (theoretical justification) → [`rl_squeezes_2026`]\n- Recovery compute follows scaling laws → [`p2_law_2025`]\n- Task-specific neurons exist; small removal causes collapse → [`task_neurons_2026`]\n- No prior work predicts recoverability before pruning → gap we fill\n\n---\n\n## 3. CKA in Neural Networks\n\n**Layer-level CKA for pruning.** MPruner [`mpruner_2024`] uses CKA similarity between consecutive layers to identify redundant layers for removal, achieving 50% parameter reduction with minimal accuracy loss. Lachance's thesis [`lachance_thesis_2024`] provides theoretical grounding that CKA layer similarity correlates with pruning recoverability. MIPP [`mipp_2024`] uses mutual information (related to CKA) as a pruning criterion.\n\n**Our extension.** We adapt CKA from layer-level redundancy detection to width-level functional overlap prediction. Specifically, we compute CKA between pre- and post-pruning intermediate representations to predict whether RLVR can recover the pruned model — a novel application of CKA as a recoverability signal rather than an importance signal.\n\n**Usable claims:**\n- CKA identifies redundant layers → [`mpruner_2024`]\n- CKA correlates with recoverability → [`lachance_thesis_2024`]\n- No prior work uses CKA for width-level recoverability prediction → our contribution\n\n---\n\n## 4. RLVR / Reasoning Enhancement\n\n**RLVR foundations.** RL Squeezes [`rl_squeezes_2026`] shows RLVR and SFT have fundamentally different mechanisms (compression vs expansion). Self-Distilled RLVR [`self_distilled_rlvr_2026`] improves RLVR training stability and sample efficiency via self-distillation. OPSD [`opsd_2026`] compresses post-RL models via one-shot structured distillation — a complementary approach to our pruning+recovery pipeline.\n\n**RLVR training efficiency.** DPPO [`dppo_2026`] achieves 2.37× GRPO speedup via importance-sampling-based rollout pruning while preserving unbiased gradients. ARRoL [`arrol_2026`] uses a lightweight quality head to predict and prune low-value rollouts during RLVR generation. Both are complementary to our work — they could accelerate the GRPO recovery phase in RASP.\n\n**Usable claims:**\n- RLVR compresses while SFT expands → [`rl_squeezes_2026`]\n- GRPO training can be accelerated 2× without accuracy loss → [`dppo_2026`, `arrol_2026`]\n- Post-RL distillation is complementary to pruning+recovery → [`opsd_2026`]\n\n---\n\n## 5. Our Positioning: RASP Fills the Gap\n\n### Gap analysis\n\nThe literature reveals a clear gap at the intersection of three directions:\n\n1. **Structured pruning for LLMs** is mature (GRASPrune, GPrune-LLM, Bonsai, DDP) but no method accounts for post-pruning recoverability when making pruning decisions.\n2. **Post-pruning recovery** via RLVR is demonstrated (Self-Healing) but operates as a black-box second stage — the pruning step is unaware of whether the removed structures can be recovered.\n3. **CKA-based analysis** has been applied to layer-level redundancy (MPruner) but never to predict width-level recoverability under RLVR.\n\n### RASP's contribution\n\nRASP bridges these three threads by introducing CKA functional overlap as a predictive signal for RLVR recoverability. Concretely:\n\n- **Before pruning:** We compute CKA overlap between candidate pruning configurations and the full model to estimate how much functional capacity is preserved. High CKA overlap → the pruned model retains the representational substrate that RLVR can rebuild upon.\n- **During pruning:** CKA scores guide which structures to remove, preferring configurations that maximize predicted recoverability at the target sparsity ratio.\n- **After pruning:** RLVR (specifically GRPO) recovers reasoning capability, and we show that CKA-guided pruning requires less recovery compute than importance-only pruning.\n\nThis is distinct from: (a) Self-Healing, which uses RLVR recovery but with standard importance-based pruning; (b) RESP/GRASPrune, which optimize pruning quality without considering recovery; (c) MPruner, which uses CKA for layer redundancy, not width-level recoverability.\n\n### Narrative for Related Work section\n\nWe position RASP as the first method to close the loop between pruning and recovery by making the pruning decision recovery-aware. While prior work treats pruning and recovery as independent stages (prune first, recover later), RASP shows that predicting recoverability — via CKA functional overlap — at the pruning stage yields better final accuracy at the same sparsity ratio and recovery budget. This is analogous to how PAT co-optimizes pruning and tuning, but RASP operates at a higher level: it does not require joint optimization, instead using CKA as a cheap predictive proxy that can be computed before any training begins.\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T13:30:56.520719+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T13:30:56.520864+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'completed', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'completed', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'in_progress', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T13:30:56.521005+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T13:30:56.521130+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T13:30:56.521245+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T13:30:56.521382+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T13:30:56.521501+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T13:30:56.521614+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact register save project",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact register save project",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T13:30:56.521728+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T13:30:56.521853+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T13:30:56.521962+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T13:30:56.522150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T13:30:56.522373+00:00_

1	- id: art_20260514_40be48
2	  name: model_utils.py
3	  type: intermediate
4	  description: 通用剪枝模型加载函数，处理非均匀 MLP 维度，eval/train/analysis 共用
5	  path: projects/recovery_aware_struct_prune/artifacts/_project/intermediate/model_utils_info.txt
6	  url: null
7	  project: recovery_aware_struct_prune
8	  exp_id: null
9	  skill: ''
10	  created_at: '2026-05-14T06:44:40.783508+00:00'
11	  tags: []
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T13:30:56.522606+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml",
  "old_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []",
  "new_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n- id: art_20260514_rw_notes\n  name: related_work_notes.md\n  type: document\n  description: Related Work 素材笔记，按5个主题组织24篇文献，含可用claims和RASP定位narrative\n  path: projects/recovery_aware_struct_prune/artifacts/related_work_notes.md\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags: [literature, related-work, writing]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml",
    "old_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []",
    "new_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n- id: art_20260514_rw_notes\n  name: related_work_notes.md\n  type: document\n  description: Related Work 素材笔记，按5个主题组织24篇文献，含可用claims和RASP定位narrative\n  path: projects/recovery_aware_struct_prune/artifacts/related_work_notes.md\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags: [literature, related-work, writing]"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T13:30:56.522846+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T13:30:56.523042+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'completed', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read current literature_map.yaml', 'status': 'completed', 'activeForm': 'Reading current literature_map.yaml'}, {'content': 'Search arXiv for new papers (6 keyword groups)', 'status': 'completed', 'activeForm': 'Searching arXiv for new papers'}, {'content': 'Evaluate and add new papers to literature_map.yaml', 'status': 'completed', 'activeForm': 'Evaluating and adding new papers'}, {'content': 'Write related_work_notes.md', 'status': 'completed', 'activeForm': 'Writing related work notes'}, {'content': 'Register artifact', 'status': 'completed', 'activeForm': 'Registering artifact'}]"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T13:30:56.523334+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature_update_may2026_20260514T132612",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-14T13:30:56.523595+00:00_

完成。总结：

### literature_map.yaml 更新（19 → 24 篇）

新增 5 篇论文：

| ID | 标题 | 年份 | 类别 | 相关度 |
|---|---|---|---|---|
| `dppo_2026` | DPPO: Unbiased Dynamic Pruning for GRPO | 2026.03 | method-component | 5 |
| `arrol_2026` | ARRoL: Online Rollout Pruning for RLVR | 2026.03 | method-component | 5 |
| `task_neurons_2026` | Task-Specific Neurons, Model Collapse, and Recovery | 2026.04 | background | 6 |
| `ddp_2026` | Deterministic Differentiable Structured Pruning | 2026.03 | background | 5 |
| `pruning_vlm_recovery_2026` | Structural Pruning of VLMs: Dynamics, Recovery, Data Efficiency | 2026.04 | background | 5 |

**未入选但值得关注的论文：**
- STOP (2605.13165) — 剪裁推理 trace 而非模型权重，与 RASP 问题不同
- UniComp (2602.09130) — 通用压缩评估框架，relevance 4
- SlimLLM (2505.22689) — 结构化剪枝+线性回归恢复，2025 年 5 月，信息不足未入

**搜索未发现的空白：** 无论文同时使用 CKA + width pruning + RLVR recovery，确认 RASP 的 novelty 仍然成立。

### 产出文件
- `literature_map.yaml` — 已更新
- `artifacts/related_work_notes.md` — 5 个 subsection + usable claims + RASP 定位 narrative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature_update_may2026_20260514T132612"
}
```

</details>

---
