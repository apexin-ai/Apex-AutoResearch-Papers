# fix d041 rollback constraint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_fix_d041-rollback-constraint_20260515T022107.log`
- **Structured JSON:** [`a1c2667c52def94f6b11.json`](../../sessions/a1/a1c2667c52def94f6b11.json)

## Before a recorded user message

44 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "eda70eef-d51f-4323-a5dd-15e35fd03218",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778825400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "68c48ed6-8920-4499-98f7-972154f27710",
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the three files that need to be modified to understand the current state and identify the incorrect changes that need to be reverted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "acfccf40-62ae-42e5-9247-2e359a881dc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuUwehNCpaNiS1kwZRFWXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11991
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

Let我先读取三个需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "43c0f0b4-29b3-49f3-a1a8-708efd05d022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuUwehNCpaNiS1kwZRFWXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11991
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_015carBJV4cztDWChZU4UrRo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "86775fab-3c17-4a1b-8c48-d3f05f48287c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuUwehNCpaNiS1kwZRFWXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11991
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T02:21:20.514Z_

<details><summary>↩ Tool result · `toolu_015carBJV4cztDWChZU4UrRo`</summary>

```text
1	# §3 Method
2	
3	## §3.1 Problem Formulation
4	
5	We address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\mathcal{F} = \{f_1, f_2, \ldots, f_N\}$. The gold set $\mathcal{F}^+_q \subset \mathcal{F}$ denotes the files modified in the ground-truth patch.
6	
7	We formulate this as a contrastive learning problem. Let $E_\theta$ be a pretrained encoder parameterized by $\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:
8	
9	$$\text{sim}(E_\theta(q), E_\theta(f^+)) \gg \text{sim}(E_\theta(q), E_\theta(f^-))$$
10	
11	where $\text{sim}(\cdot, \cdot)$ denotes cosine similarity.
12	
13	The quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.
14	
15	## §3.2 Structural Information Extraction
16	
17	### CodeQL Bounded Data-Flow Analysis
18	
19	We use CodeQL \cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:
20	
21	- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.
22	- **Data-flow graph**: inter-procedural data-flow paths $\mathcal{P} = \{(v_{\text{src}}, v_1, \ldots, v_{\text{sink}})\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.
23	
24	### File-Level Reachability
25	
26	From the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \mathcal{F}$ and an edge $(f_i, f_j) \in E$ exists if and only if at least one data-flow path in $\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.
27	
28	A key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.
29	
30	At full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].
31	
32	### Beniget Fallback
33	
34	For repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].
35	
36	### Coverage Statistics
37	
38	The extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:
39	
40	| Metric | Value |
41	|--------|-------|
42	| Timeout rate | 0% (all repository tiers) |
43	| Repository coverage | 123/131 (93.9%) |
44	| Structural data rate | 34% of instances |
45	| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |
46	
47	The 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.
48	
49	## §3.3 Structure-Aware Negative Mining
50	
51	We compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.
52	
53	### Random Negatives
54	
55	For each query $q$, we sample $K$ negatives uniformly at random from $\mathcal{F} \setminus \mathcal{F}^+_q$:
56	
57	$$f^-_{\text{rand}} \sim \text{Uniform}(\mathcal{F} \setminus \mathcal{F}^+_q), \quad |\{f^-_{\text{rand}}\}| = K$$
58	
59	This baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.
60	
61	### Embedding-Distance Negatives
62	
63	We compute embeddings for all files and queries using $E_{\theta_0}$ (before fine-tuning) and build a FAISS index \cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:
64	
65	$$f^-_{\text{embed}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q}{\text{argtop-}K}\ \text{sim}(E_{\theta_0}(q), E_{\theta_0}(f))$$
66	
67	These negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\theta_0}$ and avoids the instability and computational overhead of online re-mining \cite{xiong2021ance}.
68	
69	### Dataflow-Aware Negatives
70	
71	This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
72	
73	$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
74	
75	where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:
76	
77	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \in \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
78	
79	These files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.
80	
81	For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
82	
83	### Difficulty Gradient
84	
85	The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
86	
87	### Relationship to BM25 Baselines
88	
89	In addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].
90	
91	## §3.4 Contrastive Fine-tuning
92	
93	### InfoNCE Loss
94	
95	We train with InfoNCE loss \cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\{f^-_1, \ldots, f^-_K\}$:
96	
97	$$\mathcal{L} = -\log \frac{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau)}{\exp(\text{sim}(E_\theta(q), E_\theta(f^+)) / \tau) + \sum_{k=1}^{K} \exp(\text{sim}(E_\theta(q), E_\theta(f^-_k)) / \tau)}$$
98	
99	where $\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].
100	
101	### LoRA Fine-tuning Setup
102	
103	We fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}—using LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.
104	
105	Each encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].
106	
107	Training uses AdamW with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
108	
109	### Dual Checkpoint Strategy
110	
111	We observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\theta^*_{\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].
112	
113	### Early Stopping
114	
115	The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].
116	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
117	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "54354e31-8c11-4978-a993-0b7a0e5f7a32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
      "numLines": 117,
      "startLine": 1,
      "totalLines": 117
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Dwh6LucB7cJTGLpoeTPqwD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "e5d00de5-ceb6-466e-b92f-603702ab9e8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuUwehNCpaNiS1kwZRFWXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11991
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T02:21:20.975Z_

<details><summary>↩ Tool result · `toolu_01Dwh6LucB7cJTGLpoeTPqwD`</summary>

```text
1	# 1. Introduction
2	
3	Code retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \cite{liu2024repobench}, fault localization \cite{chen2025locagent}, and automated program repair \cite{jimenez2024swebench}.
4	Contrastive learning has become the dominant paradigm for training dense code retrievers \cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \cite{chen2020simclr,xiong2021ance}.
5	Despite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.
6	As retrieval scales to repository-level settings with hundreds of candidate files \cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.
7	
8	Existing negative selection approaches span a broad spectrum but leave a critical gap.
9	Random negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \cite{karpukhin2020dpr}.
10	Embedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.
11	CoCoHaNeRe \cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.
12	Meanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.
13	Notably, files that are close in embedding space may be structurally connected through shared data-flow paths \cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
20	Our experiments on CodeSearchNet \cite{husain2019codesearchnet} yield three principal findings.
21	First, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \cite{fan2025cocohanere}.
22	Second, as an \textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\ ${\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).
23	Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
24	
25	Our contributions are as follows:
26	\begin{enumerate}
27	\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.
28	\item \textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.
29	\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.
30	\end{enumerate}
31	
32	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
33	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "268ca940-5c4d-4b6b-ae0b-1142d5ffb34a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_013i56p86UdT4GC34pqmqCwd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "62b6c164-1c19-4499-98e3-5595950edd9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuUwehNCpaNiS1kwZRFWXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11991,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11991
      },
      "output_tokens": 25,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T02:21:21.200Z_

<details><summary>↩ Tool result · `toolu_013i56p86UdT4GC34pqmqCwd`</summary>

```text
1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct our training corpus from SWE-smith \cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \placeholder{34.3%} [pending recalc]. The remaining \placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.
6	
7	For each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.
8	
9	**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \in \{1, 5, 10\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\theta^*_{\text{R@1}}$), as discussed in §3.3.
10	
11	**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \cite{fan2025cocohanere}.
12	
13	## §4.2 Implementation Details
14	
15	**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} and **StarCoder2-3B** \cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.
16	
17	**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\tau = 0.07$, AdamW optimizer with learning rate $2 \times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.
18	
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
24	
25	## §4.3 Results
26	
27	### Main Results
28	
29	Table 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\pm$ standard deviation over three seeds.
30	
31	**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.
32	
33	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
34	|---|---|---|---|---|---|---|
35	| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |
36	| BM25 (no training) | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{X.XX} |
37	| Random | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
38	| BM25-mined | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
39	| Embedding-distance | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
40	| Dataflow-aware | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} | \placeholder{X.XX±X.XX} |
41	
42	**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\placeholder{+X.X}pp and \placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.
43	
44	### Pilot Validation
45	
46	Prior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.
47	
48	**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.
49	
50	| Strategy | Qwen R@1 | StarCoder R@1 |
51	|---|---|---|
52	| Random | 0.5357 | 0.4922 |
53	| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |
54	| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |
55	
56	The pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.
57	
58	### Ablations
59	
60	**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\in \{50, 100, 200, 500\}$.
61	
62	**Table 3: R@1 by pool size.**
63	
64	| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\Delta$ | SC Emb. | SC Rand. | SC $\Delta$ |
65	|---|---|---|---|---|---|---|
66	| 50 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
67	| 100 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
68	| 200 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
69	| 500 | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{+X.X} |
70	
71	**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.
72	
73	| Strategy | Qwen R@1 (s42) |
74	|---|---|
75	| Static embedding-distance | \placeholder{X.XX} |
76	| Dynamic (epoch re-mining) | \placeholder{X.XX} |
77	
78	### Downstream Evaluation
79	
80	**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).
81	
82	| Retriever | Resolve Rate |
83	|---|---|
84	| BM25 | \placeholder{X.X%} |
85	| Random-trained | \placeholder{X.X%} |
86	| Embedding-trained (Qwen) | \placeholder{X.X%} |
87	
88	## §4.4 Analysis
89	
90	### Representation Geometry and Negative Difficulty
91	
92	A central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.
93	
94	**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\_sim − neg\_sim.
95	
96	| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |
97	|---|---|---|---|---|---|---|
98	| | pos\_sim | neg\_sim | margin | pos\_sim | neg\_sim | margin |
99	| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |
100	| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |
101	| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |
102	
103	Several patterns emerge from Table 4:
104	
105	**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\times$ larger margins across all strategies, indicating a more separable pretrained space.
106	
107	**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.
108	
109	**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.
110	
111	### Stratified Analysis
112	
113	We stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.
114	
115	**Table 5: R@1 stratified by structural data availability.**
116	
117	| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\Delta$ | SC (Emb.) | SC (DF) | $\Delta$ |
118	|---|---|---|---|---|---|---|---|
119	| Rich dataflow ($\geq$5 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
120	| Sparse dataflow (1–4 edges) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
121	| No structural data (fallback) | \placeholder{N} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} | \placeholder{X.XX} | \placeholder{X.XX} | \placeholder{±X.X} |
122	
123	Confound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.
124	
125	### CodeQL Scalability
126	
127	We report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).
128	
129	&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->
130	**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.
131	
132	| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |
133	|---|---|---|---|---|---|
134	| Small (<50 inst.) | 18 | 500 | 0% | \placeholder{81.0%} [pending recalc] | 0.0% |
135	| Medium (50–200) | 36 | 4,096 | 0% | \placeholder{47.2%} [pending recalc] | 50.0% |
136	| Large (200–500) | 40 | 13,628 | 0% | \placeholder{34.3%} [pending recalc] | 85.7% |
137	| XLarge (500+) | 29 | 25,949 | 0% | \placeholder{31.4%} [pending recalc] | 96.0% |
138	| **Total** | **123** | **44,173** | **0%** | **\placeholder{34.3%} [pending recalc]** | — |
139	
140	The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.
141	
142	&lt;!-- Claim 2 wording fix: 2026-05-15 -->
143	&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "f3b910ea-6f41-48e0-9aea-92b11f4af8ad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
      "numLines": 144,
      "startLine": 1,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I need to identify the incorrect changes in each file. Let me analyze each file:

### method_v1.md

Line 77: `$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \in \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$`

This says `f ∈ R_G(q)` - which means selecting from structurally **connected** files. 

But wait, looking at the actual implementation, the code filters for files NOT in the connected set, so it's selecting disconnected files. The paper's original notation with `f ∈ R_G(q)` appears to be the error—it should be `f ∉ R_G(q)` to match what the code actually does. The descriptions on lines 79 and 85 that say "connected" should indeed be "disconnected" to align with the implementation.

Now I'm going through the three files to identify all the places where this notation and terminology need to be corrected. In method_v1.md, the mathematical notation and descriptions of structural connectivity need to be flipped. The introduction_v2.md file has similar issues where it describes selecting from structurally connected files when it should say disconnected.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "68ab1648-ad18-4921-8080-69f63d508def",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 13_

找到了所有需要修正的位置。三个文件中都有被错误翻转的约束方向。开始修改。

**method_v1.md** 有3处需要改，**introduction_v2.md** 有1处，**experiments_v1.md** 有1处。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "333afdc9-33fb-4cb6-9cb4-695ebf217c43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_01UoGfG3vmnDDNLYdheAW4yY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
  "new_string": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "6abe3157-21ce-460b-b53a-ca877235271d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T02:21:47.544Z_

<details><summary>↩ Tool result · `toolu_01UoGfG3vmnDDNLYdheAW4yY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "01f12e3f-d992-46a8-807e-0113a7691fc5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
    "newString": "$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 9,
        "newStart": 74,
        "newLines": 9,
        "lines": [
          " ",
          " where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:",
          " ",
          "-$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\in \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$",
          "+$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$",
          " ",
          "-These files are structurally connected to the gold files in the data-flow graph (structurally plausible) and exhibit high BM25 lexical similarity with the query (hard to distinguish). They share inter-procedural data-flow connections with the gold files yet are not part of the actual fix. By training the encoder to distinguish these structurally proximate but non-gold files from true positives, we aim to push the embedding space toward capturing fine-grained functional distinctions beyond surface-level similarity.",
          "+These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.",
          " ",
          " For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_011V4DZAGJq4i5QXs8ave29e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query.",
  "new_string": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "bf35729b-d85f-41b7-a392-e22e10f0d9a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T02:21:49.890Z_

<details><summary>↩ Tool result · `toolu_011V4DZAGJq4i5QXs8ave29e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "5734d27b-cd82-42f8-8aba-14e0e9844697",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query.",
    "newString": "Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query.",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 7,
        "lines": [
          " ",
          " ### Difficulty Gradient",
          " ",
          "-The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are both structurally connected and lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
          "+The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).",
          " ",
          " ### Relationship to BM25 Baselines",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01RStGQnPGRZTiNg5Sjv3Vyq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "bf564301-4261-41c1-b71d-5fa869f6605f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T02:21:51.358Z_

<details><summary>↩ Tool result · `toolu_01RStGQnPGRZTiNg5Sjv3Vyq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "6702f58a-35fb-4dff-b4e2-c5a8a8bb651e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
    "oldString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "newString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->",
    "originalFile": "# §3 Method\n\n## §3.1 Problem Formulation\n\nWe address the task of **repo-level code retrieval for bug fixing**: given a natural-language bug report or issue description $q$, retrieve the top-$k$ most relevant source files from a repository's file set $\\mathcal{F} = \\{f_1, f_2, \\ldots, f_N\\}$. The gold set $\\mathcal{F}^+_q \\subset \\mathcal{F}$ denotes the files modified in the ground-truth patch.\n\nWe formulate this as a contrastive learning problem. Let $E_\\theta$ be a pretrained encoder parameterized by $\\theta$. We learn an embedding space where the similarity between a query $q$ and its gold files exceeds the similarity to non-gold files:\n\n$$\\text{sim}(E_\\theta(q), E_\\theta(f^+)) \\gg \\text{sim}(E_\\theta(q), E_\\theta(f^-))$$\n\nwhere $\\text{sim}(\\cdot, \\cdot)$ denotes cosine similarity.\n\nThe quality of the learned embedding space depends critically on the selection of negative files $f^-$ during training. We systematically compare three negative mining strategies—random, embedding-distance, and dataflow-aware—and analyze how their effectiveness interacts with the encoder's pretrained representation geometry.\n\n## §3.2 Structural Information Extraction\n\n### CodeQL Bounded Data-Flow Analysis\n\nWe use CodeQL \\cite{codeql2019} to perform scope-bounded inter-procedural data-flow analysis on each repository. We define taint-tracking queries with a bounded analysis depth (2-hop) that trace data flow from designated sources to sinks across function call boundaries. This produces two complementary structural views:\n\n- **Call graph**: function-level call relationships within and across files, capturing which functions invoke which others.\n- **Data-flow graph**: inter-procedural data-flow paths $\\mathcal{P} = \\{(v_{\\text{src}}, v_1, \\ldots, v_{\\text{sink}})\\}$, where each node $v_i$ is annotated with its enclosing file. These paths trace how data propagates through function parameters, return values, and shared state across call boundaries.\n\n### File-Level Reachability\n\nFrom the extracted data-flow paths, we construct a file-level structural connectivity graph $G = (V, E)$, where $V = \\mathcal{F}$ and an edge $(f_i, f_j) \\in E$ exists if and only if at least one data-flow path in $\\mathcal{P}$ traverses both $f_i$ and $f_j$. Two files are **connected** if data flows between them across call boundaries; otherwise they are **disconnected**.\n\nA key design property is that $G$ is **externally fixed**: it is computed once from the repository's static structure and does not update during encoder training. This makes the structural signal immune to representation drift \\cite{xiong2021ance}, a known issue in dynamic negative mining where the mining distribution shifts as the encoder updates.\n\nAt full scale, 78% of files connected in $G$ are non-gold files (structurally related but not in the patch), providing a rich pool for structure-grounded negative mining [Source: paper_framing, plan_006].\n\n### Beniget Fallback\n\nFor repositories where CodeQL database creation fails (e.g., unsupported build configurations or missing dependencies), we employ beniget—a lightweight Python def-use chain analyzer—as a fallback. Beniget operates directly on the AST without requiring a compiled CodeQL database, providing partial structural information at lower computational cost. Across the full dataset, CodeQL succeeded on 15,133 instances and beniget contributed an additional 764 instances via fallback [Source: m1_extraction registry].\n\n### Coverage Statistics\n\nThe extraction pipeline achieves the following at full scale (131 repositories, 44,173 instances attempted) [Source: m1_extraction and plan_006 registries]:\n\n| Metric | Value |\n|--------|-------|\n| Timeout rate | 0% (all repository tiers) |\n| Repository coverage | 123/131 (93.9%) |\n| Structural data rate | 34% of instances |\n| Connected-not-gold rate (Z%) | 78% overall; median 96% for repositories with 500+ instances |\n\nThe 0% timeout rate confirms the tractability of bounded inter-procedural analysis at scale. The structural data rate of 34% reflects transient filesystem failures during batch extraction rather than fundamental limitations of the analysis; a re-extraction pass is expected to recover the majority of failed instances (§6). The high Z% in large repositories indicates that structural connectivity provides a rich negative mining signal precisely where lexical ambiguity is greatest.\n\n## §3.3 Structure-Aware Negative Mining\n\nWe compare three negative mining strategies spanning a spectrum from uninformed to structure-grounded selection. All mining is **static**: negatives are computed once before training from the frozen pretrained encoder $E_{\\theta_0}$ and the fixed structural graph $G$, and are not refreshed during fine-tuning.\n\n### Random Negatives\n\nFor each query $q$, we sample $K$ negatives uniformly at random from $\\mathcal{F} \\setminus \\mathcal{F}^+_q$:\n\n$$f^-_{\\text{rand}} \\sim \\text{Uniform}(\\mathcal{F} \\setminus \\mathcal{F}^+_q), \\quad |\\{f^-_{\\text{rand}}\\}| = K$$\n\nThis baseline provides unbiased but typically easy negatives, as randomly chosen files are unlikely to share topical or structural similarity with the query.\n\n### Embedding-Distance Negatives\n\nWe compute embeddings for all files and queries using $E_{\\theta_0}$ (before fine-tuning) and build a FAISS index \\cite{johnson2021faiss} over file embeddings. For each query $q$, we select the $K$ non-gold files with highest cosine similarity in the pretrained embedding space:\n\n$$f^-_{\\text{embed}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q}{\\text{argtop-}K}\\ \\text{sim}(E_{\\theta_0}(q), E_{\\theta_0}(f))$$\n\nThese negatives occupy the region of the embedding space where the pretrained encoder is most uncertain, forcing the fine-tuned model to learn finer distinctions. This approach requires only a single forward pass through $E_{\\theta_0}$ and avoids the instability and computational overhead of online re-mining \\cite{xiong2021ance}.\n\n### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n\nIn addition to the three primary strategies, we evaluate BM25-mined negatives as a supplementary comparison. BM25 negatives are constructed by indexing all repository files with Okapi BM25 \\cite{robertson2009bm25} and selecting the top-$K$ highest-scoring non-gold files per query. This provides a lexical-overlap baseline that grounds our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}, which argues that non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods. At the top-7 level (matching training $K$), BM25 and embedding-distance negatives diverge substantially for medium and large repositories (Jaccard overlap 0.30–0.38), indicating that the two approaches select meaningfully different negatives despite high overlap at the full candidate level [Source: plan_018 registry].\n\n## §3.4 Contrastive Fine-tuning\n\n### InfoNCE Loss\n\nWe train with InfoNCE loss \\cite{karpukhin2020dpr}. For a query $q$ with positive file $f^+$ and a set of $K$ negatives $\\{f^-_1, \\ldots, f^-_K\\}$:\n\n$$\\mathcal{L} = -\\log \\frac{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau)}{\\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^+)) / \\tau) + \\sum_{k=1}^{K} \\exp(\\text{sim}(E_\\theta(q), E_\\theta(f^-_k)) / \\tau)}$$\n\nwhere $\\tau$ is a learnable temperature parameter initialized to 0.07 and $K = 7$ negatives per query [Source: m2_full_qwen registry].\n\n### LoRA Fine-tuning Setup\n\nWe fine-tune two decoder-only pretrained code models—Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}—using LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of each attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. The base model weights remain frozen; only the LoRA adapters and projection head are updated.\n\nEach encoder produces fixed-dimensional representations via mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled hidden state to a 256-dimensional embedding space [Source: m2_full_qwen registry].\n\nTraining uses AdamW with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\n### Dual Checkpoint Strategy\n\nWe observe that validation loss and retrieval metrics (Recall@1) do not always select the same checkpoint, particularly for StarCoder2-3B. We therefore maintain two checkpoints throughout training: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1). Final evaluation uses $\\theta^*_{\\text{R@1}}$, and we report both to enable analysis of the loss–metric disagreement [Source: D036 decision].\n\n### Early Stopping\n\nThe initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 113,
        "oldLines": 4,
        "newStart": 113,
        "newLines": 4,
        "lines": [
          " ### Early Stopping",
          " ",
          " The initial seed ($s_{42}$) trains for 3 epochs to provide a complete overfitting curve; subsequent seeds ($s_{43}$, $s_{44}$) train for 2 epochs with early stopping (patience = 2 evaluation cycles, evaluated every 500 steps) based on validation loss. This design was informed by observed overfitting after epoch 1 in $s_{42}$ runs [Source: D026 decision].",
          "-&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01NXRYpkcaBaxqp41Wt2yh2Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
  "new_string": "dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "b8fe18f7-643f-4ba8-8f53-e9ea0c2f86ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T02:21:52.778Z_

<details><summary>↩ Tool result · `toolu_01NXRYpkcaBaxqp41Wt2yh2Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "34702aa6-e375-4841-84ac-2d7fb1e029ed",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
    "newString": "dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.",
          " Using CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.",
          "-We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally connected files ranked by BM25.",
          "+We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.",
          " All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.",
          " ",
          " Our experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_014C2CTXUSZqsTMfdrUyPEc7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "2b27c9e9-8f31-489c-b2db-da55b3a1ffe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T02:21:54.194Z_

<details><summary>↩ Tool result · `toolu_014C2CTXUSZqsTMfdrUyPEc7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "34640b33-fa49-44a1-8ddf-6a3b435ef880",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
    "oldString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "newString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->",
    "originalFile": "# 1. Introduction\n\nCode retrieval---identifying relevant source files given a query such as a bug report or natural language description---underpins critical software engineering workflows including IDE-assisted completion \\cite{liu2024repobench}, fault localization \\cite{chen2025locagent}, and automated program repair \\cite{jimenez2024swebench}.\nContrastive learning has become the dominant paradigm for training dense code retrievers \\cite{jain2021contracode,li2022coderetriever}, where the quality of negative examples critically determines the learned representation \\cite{chen2020simclr,xiong2021ance}.\nDespite this sensitivity, the choice of negative mining strategy in code retrieval receives surprisingly little systematic attention: most systems adopt random in-batch negatives \\cite{karpukhin2020dpr} or a single hard negative heuristic without controlled comparison.\nAs retrieval scales to repository-level settings with hundreds of candidate files \\cite{jimenez2024swebench,reddy2025swerank}, the margin between effective and ineffective negative selection is amplified, making this gap increasingly consequential.\n\nExisting negative selection approaches span a broad spectrum but leave a critical gap.\nRandom negatives are widely used yet risk being trivially distinguishable from positives, providing weak training signal \\cite{karpukhin2020dpr}.\nEmbedding-distance hard negatives, selected as nearest neighbors in a frozen embedding space \\cite{xiong2021ance}, increase difficulty but may introduce false negatives---semantically related examples incorrectly treated as negatives.\nCoCoHaNeRe \\cite{fan2025cocohanere} argues that non-differentiable embedding negatives are ``slow and ineffective'' compared to gradient-based alternatives, yet does not evaluate simple static embedding-distance mining in structural code retrieval settings.\nMeanwhile, code possesses rich structural information---call graphs, data-flow dependencies, type hierarchies---that could inform negative selection but remains entirely unexploited for this purpose.\nNotably, files that are close in embedding space may be structurally connected through shared data-flow paths \\cite{guo2021graphcodebert}, making them poor candidates for hard negatives; filtering such pairs could yield genuinely informative training signal.\n\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n\nOur experiments on CodeSearchNet \\cite{husain2019codesearchnet} yield three principal findings.\nFirst, static embedding-distance negatives consistently improve retrieval over random baselines (+[TBD] pp Recall@1 for Qwen, +[TBD] pp for StarCoder across [TBD] seeds), directly challenging the premise that gradient-based mining mechanisms are necessary for effective code search \\cite{fan2025cocohanere}.\nSecond, as an \\textbf{exploratory observation}, dataflow-aware negatives do not consistently outperform embedding-distance mining but exhibit encoder-dependent interaction patterns: negative difficulty margin analysis suggests that the pretrained embedding space's degree of saturation (positive-pair similarity $>0.98$ for Qwen vs.\\ ${\\sim}0.80$ for StarCoder) may mediate strategy effectiveness, providing a candidate mechanistic hypothesis for when different strategies should be preferred (an exploratory finding from two encoders; pending multi-seed confirmation).\nThird, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.\n\nOur contributions are as follows:\n\\begin{enumerate}\n\\item The first systematic empirical comparison of negative mining strategies for contrastive code retrieval, demonstrating that simple static embedding-distance mining consistently improves performance across encoders with distinct representation geometries, without requiring gradient-based mechanisms.\n\\item \\textbf{[Exploratory observation]} An analysis revealing that structure-grounded (dataflow) negatives interact with encoder representation geometry, with negative difficulty margin analysis providing mechanistic evidence for this interaction and a testable prediction for when structural mining should be most beneficial.\n\\item A scalable pipeline for scope-bounded inter-procedural data-flow extraction via CodeQL, enabling structure-aware negative mining for contrastive code retrieval training across large-scale repositories.\n\\end{enumerate}\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 4,
        "newStart": 30,
        "newLines": 4,
        "lines": [
          " \\end{enumerate}",
          " ",
          " &lt;!-- Claim 2 wording fix: 2026-05-15 -->",
          "-&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01CXKtPzskFZVQSzD1RQ6R7t`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
  "new_string": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "0ead3870-acdc-4178-afbe-748860b8b84b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T02:21:56.551Z_

<details><summary>↩ Tool result · `toolu_01CXKtPzskFZVQSzD1RQ6R7t`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "765143cf-2fc6-4207-9f7e-8b3acb9a5db4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
    "newString": "Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4).",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " ",
          " For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).",
          " ",
          "-**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally connected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.",
          "+**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.",
          " ",
          " **Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01NVmUNC3CY6szJeYRBAGzxC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "old_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
  "new_string": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "e31fd149-9c0b-4337-b617-44c77911df89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhShK8bWYFJjSb3z2bN1MH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10299,
      "cache_read_input_tokens": 23438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10299
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T02:21:57.654Z_

<details><summary>↩ Tool result · `toolu_01NVmUNC3CY6szJeYRBAGzxC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "984b4e87-f135-4347-a260-071d2971595a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
    "oldString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
    "newString": "&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->",
    "originalFile": "# §4 Experiments\n\n## §4.1 Experimental Setup\n\n**Dataset.** We construct our training corpus from SWE-smith \\cite{yang2025swesmith}, a large-scale dataset of real-world GitHub bug-fix commits. Starting from 5,029 task instances spanning 131 unique (repository, commit) pairs, each task corresponds to a single bug-fix commit; we expand each task by treating every gold file as a separate training instance, yielding 44,173 training instances total (since many tasks involve multiple gold files). We run the StructFuse extraction pipeline (§3.2) to obtain inter-procedural data-flow graphs via CodeQL. After filtering for clone/checkout failures and extraction errors, we retain \\placeholder{15,133} [pending recalc] instances with structural data across 123 repositories, yielding a structural coverage rate of \\placeholder{34.3%} [pending recalc]. The remaining \\placeholder{65.7%} [pending recalc] of instances lack structural connectivity data due to transient filesystem failures during batch extraction; a re-extraction pass (in progress) is expected to recover the majority of these instances, and we discuss data efficiency implications in §6.\n\nFor each random seed, we perform a per-repository stratified split to produce approximately 11,300 training and 3,000 validation instances. Each instance consists of an issue description (query), one or more gold files (positives), and strategy-specific negatives (§3.4). The per-seed split ensures that no repository appears exclusively in one partition, preserving the distribution of repository sizes and structural properties.\n\n**Evaluation Protocol.** We evaluate retrieval performance using Recall@$k$ ($k \\in \\{1, 5, 10\\}$) and Mean Reciprocal Rank (MRR), computed over a candidate pool of size 50 (1 positive + 49 negatives sampled per query). During training, $K = 7$ negatives are used per query. We report results as mean $\\pm$ standard deviation across three random seeds (42, 43, 44). For all comparisons, we use the checkpoint selected by best validation Recall@1 ($\\theta^*_{\\text{R@1}}$), as discussed in §3.3.\n\n**Baselines.** Our core experiment compares three contrastive negative mining strategies—random, embedding-distance, and dataflow-aware (§3.4)—across two encoders and three seeds (3 × 3 × 2 = 18 runs). We additionally include two BM25-based comparisons reported separately from the core matrix: (1) a BM25 retrieval baseline using Okapi BM25 \\cite{robertson2009bm25} to rank candidate files by lexical overlap with the query, providing a non-neural reference point; and (2) BM25-mined negatives as a supplementary contrastive training strategy to ground our comparison against the gradient-based premise of CoCoHaNeRe \\cite{fan2025cocohanere}.\n\n## §4.2 Implementation Details\n\n**Encoders.** We select two decoder-only pretrained code models with distinct pretraining regimes and representation geometries: **Qwen2.5-Coder-3B** \\cite{hui2024qwen25coder} and **StarCoder2-3B** \\cite{li2023starcoder}. Qwen2.5-Coder-3B is trained primarily with Fill-in-the-Middle (FIM) on a curated multilingual code corpus, while StarCoder2-3B uses a multi-task objective including FIM on The Stack v2. As we show in §4.4, these models exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (mean positive cosine similarity 0.798). This divergence enables us to study how representation geometry may mediate the effectiveness of different negative mining strategies.\n\n**Fine-Tuning Configuration.** Both encoders are fine-tuned with LoRA \\cite{hu2022lora} applied to the query and value projection matrices ($W_q$, $W_v$) of every attention layer, with rank $r = 16$, scaling factor $\\alpha = 32$, and dropout 0.05. We apply mean pooling over non-padding positions of the last hidden layer, followed by L2 normalization. A two-layer MLP projection head (Linear→GELU→Linear) maps the pooled representation to a 256-dimensional embedding. Training uses InfoNCE loss with learnable temperature initialized at $\\tau = 0.07$, AdamW optimizer with learning rate $2 \\times 10^{-5}$, weight decay 0.01, cosine annealing schedule with 10% linear warmup, and gradient clipping at max norm 1.0. Input sequences are truncated to 2,048 tokens. Batch size is 8 with gradient checkpointing enabled.\n\nFor the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.\n\n## §4.3 Results\n\n### Main Results\n\nTable 1 presents the main retrieval results across three negative mining strategies and two encoders. Each cell reports mean $\\pm$ standard deviation over three seeds.\n\n**Table 1: Retrieval performance by negative mining strategy and encoder.** Pool size = 50. Best per-encoder results in **bold**.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | R@1 | R@5 | MRR | R@1 | R@5 | MRR |\n| BM25 (no training) | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{X.XX} |\n| Random | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| BM25-mined | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Embedding-distance | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n| Dataflow-aware | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} | \\placeholder{X.XX±X.XX} |\n\n**Key observations.** (1) Embedding-distance mining consistently improves over random negatives across both encoders (\\placeholder{+X.X}pp and \\placeholder{+X.X}pp R@1 for Qwen and StarCoder respectively), confirming that simple static embedding-distance mining provides meaningful training signal without gradient-based mechanisms. (2) Dataflow-aware negatives show encoder-dependent effects: \\placeholder{description of interaction pattern based on final results}. (3) All contrastive strategies substantially outperform the BM25 retrieval baseline, demonstrating the value of learned representations for repo-level code retrieval.\n\n### Pilot Validation\n\nPrior to the full multi-seed experiment, we conducted single-seed pilot runs on a 24-repository subset (~3,300 instances) to validate the pipeline and obtain early signal on strategy differentiation. Pilot results (Table 2) show consistent patterns with the full-scale experiment.\n\n**Table 2: Pilot results (single seed, 24-repo subset, R@1 checkpoint).** Pool size = 50.\n\n| Strategy | Qwen R@1 | StarCoder R@1 |\n|---|---|---|\n| Random | 0.5357 | 0.4922 |\n| Embedding-distance | 0.5557 (+2.0pp) | 0.5078 (+1.6pp) |\n| Dataflow-aware | 0.5436 (+0.8pp) | 0.4869 (−0.5pp) |\n\nThe pilot established two findings, with patterns expected to be confirmed at full scale (pending M2 full results): (i) embedding-distance mining yields consistent improvement across both encoders, and (ii) the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder.\n\n### Ablations\n\n**Pool Size Sensitivity.** To assess whether strategy rankings are robust to evaluation-time candidate pool size, we evaluate best checkpoints at pool sizes $\\in \\{50, 100, 200, 500\\}$.\n\n**Table 3: R@1 by pool size.**\n\n| Pool Size | Qwen Emb. | Qwen Rand. | Qwen $\\Delta$ | SC Emb. | SC Rand. | SC $\\Delta$ |\n|---|---|---|---|---|---|---|\n| 50 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 100 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 200 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n| 500 | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{+X.X} |\n\n**Dynamic Mining Control.** To isolate the effect of static vs. dynamic negative mining, we compare our static embedding-distance strategy against an epoch-level re-mining variant that recomputes embeddings and re-mines negatives at the start of each epoch.\n\n| Strategy | Qwen R@1 (s42) |\n|---|---|\n| Static embedding-distance | \\placeholder{X.XX} |\n| Dynamic (epoch re-mining) | \\placeholder{X.XX} |\n\n### Downstream Evaluation\n\n**SWE-bench Lite.** To validate that retrieval improvements translate to downstream task performance, we integrate the trained retriever into an LLM-based repair agent and evaluate on SWE-bench Lite (300 instances).\n\n| Retriever | Resolve Rate |\n|---|---|\n| BM25 | \\placeholder{X.X%} |\n| Random-trained | \\placeholder{X.X%} |\n| Embedding-trained (Qwen) | \\placeholder{X.X%} |\n\n## §4.4 Analysis\n\n### Representation Geometry and Negative Difficulty\n\nA central question is *why* embedding-distance mining helps while dataflow-aware mining shows encoder-dependent effects. We analyze this through the lens of **negative difficulty**: the mean cosine similarity between each query and its assigned negatives in the pretrained embedding space. Higher negative similarity implies harder negatives—the encoder must learn finer distinctions to separate positives from negatives.\n\n**Table 4: Negative difficulty analysis (pretrained encoders, 2048-token context).** Margin = pos\\_sim − neg\\_sim.\n\n| Strategy | Qwen2.5-Coder-3B | | | StarCoder2-3B | | |\n|---|---|---|---|---|---|---|\n| | pos\\_sim | neg\\_sim | margin | pos\\_sim | neg\\_sim | margin |\n| Random | 0.986 | 0.911 | 0.074 | 0.799 | 0.605 | 0.194 |\n| Embedding-distance | 0.986 | 0.969 | 0.017 | 0.808 | 0.741 | 0.067 |\n| Dataflow-aware | 0.986 | 0.956 | 0.029 | 0.801 | 0.682 | 0.119 |\n\nSeveral patterns emerge from Table 4:\n\n**Saturation asymmetry.** Qwen's pretrained space is near-saturated: positive cosine similarity exceeds 0.98 regardless of strategy, leaving a maximum margin of only 0.074. StarCoder maintains 2.6–4.1$\\times$ larger margins across all strategies, indicating a more separable pretrained space.\n\n**Difficulty gradient.** Both encoders follow the expected ordering: embedding-distance negatives are hardest (smallest margin), followed by dataflow-aware, then random. However, the *magnitude* of margin compression differs: embedding-distance mining reduces Qwen's margin from 0.074 to 0.017 (77% reduction), while StarCoder's margin drops from 0.194 to 0.067 (65% reduction). The steeper relative compression for Qwen suggests that in saturated spaces, even small increases in negative difficulty push the encoder close to its representational capacity.\n\n**Mechanistic hypothesis.** Based on our two-encoder comparison, we hypothesize the following mechanism. When the pretrained space is saturated, the encoder has limited room to separate positives from any category of hard negatives. Embedding-distance negatives provide a direct optimization target: they occupy precisely the region where the encoder is uncertain. Dataflow-aware negatives, while structurally informative, target a subset of the hard-negative space that may not align with the encoder's most informative gradient direction. In the well-separated StarCoder space, both strategies have sufficient room to be effective; in Qwen's saturated space, the additional structural constraint of dataflow-aware mining may exclude some of the most useful hard negatives.\n\n### Stratified Analysis\n\nWe stratify results by structural data availability to assess whether the dataflow-aware strategy's effectiveness depends on the richness of the underlying CodeQL graph.\n\n**Table 5: R@1 stratified by structural data availability.**\n\n| Stratum | Instances | Qwen (Emb.) | Qwen (DF) | $\\Delta$ | SC (Emb.) | SC (DF) | $\\Delta$ |\n|---|---|---|---|---|---|---|---|\n| Rich dataflow ($\\geq$5 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| Sparse dataflow (1–4 edges) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n| No structural data (fallback) | \\placeholder{N} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} | \\placeholder{X.XX} | \\placeholder{X.XX} | \\placeholder{±X.X} |\n\nConfound analysis reveals that rich-dataflow instances are heavily concentrated in large repositories (99.3% in large/xlarge tiers), while small repositories have no rich-dataflow instances. We therefore control for pool size and repository size when comparing strategies across strata to isolate the independent effect of structural data richness.\n\n### CodeQL Scalability\n\nWe report extraction-time statistics to support the practicality of the pipeline at scale (Claim 3).\n\n&lt;!-- PENDING: Table 6 所有数值将在 m1_reextract_v2 完成后从实际数据一次性重算。不再手动调数字。 -->\n**Table 6: CodeQL extraction scalability by repository tier [PENDING RECALC].** Repositories are tiered by their instance count in the expanded dataset.\n\n| Tier | Repos | Instances | Timeout Rate | Structural Coverage | Z% (median) |\n|---|---|---|---|---|---|\n| Small (<50 inst.) | 18 | 500 | 0% | \\placeholder{81.0%} [pending recalc] | 0.0% |\n| Medium (50–200) | 36 | 4,096 | 0% | \\placeholder{47.2%} [pending recalc] | 50.0% |\n| Large (200–500) | 40 | 13,628 | 0% | \\placeholder{34.3%} [pending recalc] | 85.7% |\n| XLarge (500+) | 29 | 25,949 | 0% | \\placeholder{31.4%} [pending recalc] | 96.0% |\n| **Total** | **123** | **44,173** | **0%** | **\\placeholder{34.3%} [pending recalc]** | — |\n\nThe pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n",
    "structuredPatch": [
      {
        "oldStart": 140,
        "oldLines": 4,
        "newStart": 140,
        "newLines": 4,
        "lines": [
          " The pipeline achieves 0% timeout rate across all repository tiers. Structural coverage [pending recalc] (proportion of instances with CodeQL data-flow output) decreases with repository size, reflecting the combinatorial complexity of inter-procedural analysis in large codebases. Conversely, the connected-not-gold rate (Z%)—the proportion of structurally connected files that are non-gold—increases with repository size, reaching a median of 96% for repositories with 500+ instances. This indicates that larger repositories provide richer pools for structure-grounded negative mining. Of the 123 repositories, \\placeholder{104} [pending recalc] produce at least one training pair with inter-file structural connectivity; the remaining \\placeholder{19} [pending recalc] contribute instances to training but lack cross-file dataflow edges (their dataflow-aware negatives fall back to embedding-distance selection). The re-extraction pass currently in progress is expected to substantially improve structural coverage across all tiers.",
          " ",
          " &lt;!-- Claim 2 wording fix: 2026-05-15 -->",
          "-&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->",
          "+&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15; 回滚约束方向 2026-05-15 -->"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 28_

验证修改结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "e27d70ef-9390-4f85-9fb4-2c71e2beb286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwNfQysrYNypXAf6RH2gbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 33737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01WkC2ZHS14dncDfN52rGyCT`</summary>

```json
{
  "pattern": "f ∈ R_G|f \\\\in \\\\mathcal\\{R\\}_G|structurally connected.*files.*ranked|structurally connected non-gold",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "74bf3d0f-8e80-4c02-9cb4-48824cffc84c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwNfQysrYNypXAf6RH2gbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 33737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T02:22:05.321Z_

<details><summary>↩ Tool result · `toolu_01WkC2ZHS14dncDfN52rGyCT`</summary>

```text
artifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.
artifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\% timeout rate and [TBD]\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "1cc80cfc-05a0-41e2-8e6e-426baea5fc0e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/paper_drafts/introduction_v1.md:30:3. We develop and validate a scope-bounded inter-procedural data-flow extraction pipeline using CodeQL \\cite{github2019codeql} that operates at scale (123 repositories, 0% timeout rate, 78% structurally connected non-gold rate), enabling structure-grounded negative mining for contrastive training of code retrievers.\nartifacts/paper_drafts/introduction_v2.md:23:Third, our CodeQL-based extraction pipeline scales reliably to [TBD] repositories with 0\\% timeout rate and [TBD]\\% structurally connected non-gold rate, demonstrating that inter-procedural data-flow analysis is practically feasible for training-time negative mining at scale.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01CGvRLhh3ECedM3uAqufk3q`</summary>

```json
{
  "pattern": "f \\\\notin \\\\mathcal\\{R\\}_G|structurally disconnected|structurally \\*\\*disconnected\\*\\*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "734b201b-aed5-4533-a5f3-e7f6b4c1d511",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwNfQysrYNypXAf6RH2gbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 33737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T02:22:06.726Z_

<details><summary>↩ Tool result · `toolu_01CGvRLhh3ECedM3uAqufk3q`</summary>

```text
artifacts/paper_drafts/method_v1.md:77:$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
artifacts/paper_drafts/method_v1.md:79:These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.
artifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]
artifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]
artifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
artifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what "structurally disconnected but textually similar" means concretely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "0840d2c0-df17-4cc5-8f78-b84db582224e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/paper_drafts/method_v1.md:77:$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\nartifacts/paper_drafts/method_v1.md:79:These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.\nartifacts/paper_drafts/method_v1.md:85:[Omitted long matching line]\nartifacts/paper_drafts/experiments_v1.md:21:[Omitted long matching line]\nartifacts/paper_drafts/introduction_v2.md:17:We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.\nartifacts/paper_drafts/figure_design_v1.md:49:**Purpose**: Make the 3 strategies intuitive. Directly supports §3.4 and helps readers understand what \"structurally disconnected but textually similar\" means concretely.",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01JMtuMD7K886zaYm1TvGrmK`</summary>

```json
{
  "pattern": "sim\\(E_\\\\theta_?0|embedding distance.*排序|argtop.*sim\\(E",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "b1584b3f-5a98-415b-ab3e-bc6cb2257f58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DwNfQysrYNypXAf6RH2gbP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3002,
      "cache_read_input_tokens": 33737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3002
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T02:22:08.711Z_

<details><summary>↩ Tool result · `toolu_01JMtuMD7K886zaYm1TvGrmK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "c33dc1c8-a170-4d0a-a42e-2ce59f4b572e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
The grep results show:

1. **No `f ∈ R_G` or `f \in \mathcal{R}_G` left** — the constraint has been correctly flipped to `f \notin \mathcal{R}_G(q)`.

2. **"structurally connected non-gold" still appears** in:
   - `introduction_v1.md` line 30 — but this is a different file (v1, not v2), and the context is about "structurally connected non-gold rate" which is a coverage statistic (Z%), not about the negative selection constraint. This refers to the proportion of connected files that are non-gold, which is a different concept. 
   - `introduction_v2.md` line 23 — same thing, "structurally connected non-gold rate" is the Z% metric describing what fraction of structurally connected files are non-gold. This is the correct usage.

3. **"structurally disconnected" appears correctly** in method_v1.md (lines 77, 79, 85), experiments_v1.md (line 21), and introduction_v2.md (line 17).

4. **No `sim(E_θ0)` or embedding distance sorting** — BM25 ranking is preserved as it should be.

The "structurally connected non-gold rate" in the introduction files is specifically the Z% metric measuring what percentage of structurally connected files are non-gold—this is distinct from the negative selection constraint and shouldn't be modified. Now I need to check the full context around these modified sections to ensure everything flows correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "48cb264a-b1f5-434a-b9ed-7362a452c628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RxYdmdQXWpt6muXMJQF5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 36_

验证通过。快速确认关键区域上下文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "98b4534d-048a-45ec-8092-681c2065a8ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RxYdmdQXWpt6muXMJQF5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_018QmCFzHC2yRFRG4UTwrG4e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
  "offset": 69,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "9497e534-65d2-4de2-8b71-b2491b29a824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RxYdmdQXWpt6muXMJQF5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T02:22:26.798Z_

<details><summary>↩ Tool result · `toolu_018QmCFzHC2yRFRG4UTwrG4e`</summary>

```text
69	### Dataflow-Aware Negatives
70	
71	This strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\mathcal{F}^+_q$, define the reachability set:
72	
73	$$\mathcal{R}_G(q) = \{f \in \mathcal{F} : \exists f^+ \in \mathcal{F}^+_q,\ (f^+, f) \in E^*\}$$
74	
75	where $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:
76	
77	$$f^-_{\text{df}} = \underset{f \in \mathcal{F} \setminus \mathcal{F}^+_q :\ f \notin \mathcal{R}_G(q)}{\text{argtop-}K}\ \text{BM25}(q, f)$$
78	
79	These files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.
80	
81	For instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).
82	
83	### Difficulty Gradient
84	
85	The three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).
86	
87	### Relationship to BM25 Baselines
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "816ef985-00bb-41b7-8077-80e747264745",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/method_v1.md",
      "content": "### Dataflow-Aware Negatives\n\nThis strategy combines BM25 ranking with structural reachability filtering. For query $q$ with gold files $\\mathcal{F}^+_q$, define the reachability set:\n\n$$\\mathcal{R}_G(q) = \\{f \\in \\mathcal{F} : \\exists f^+ \\in \\mathcal{F}^+_q,\\ (f^+, f) \\in E^*\\}$$\n\nwhere $E^*$ denotes the 2-hop bounded reachability in $G$. The dataflow-aware negatives are:\n\n$$f^-_{\\text{df}} = \\underset{f \\in \\mathcal{F} \\setminus \\mathcal{F}^+_q :\\ f \\notin \\mathcal{R}_G(q)}{\\text{argtop-}K}\\ \\text{BM25}(q, f)$$\n\nThese files are structurally **disconnected** from the gold files in the data-flow graph (no inter-procedural data-flow path reaches them) yet exhibit high BM25 lexical similarity with the query (hard to distinguish on surface). By training the encoder to distinguish these lexically similar but structurally unreachable files from true positives, we aim to push the embedding space toward capturing functional distinctions that surface-level similarity misses.\n\nFor instances lacking structural connectivity data (~66% of training data), the dataflow-aware strategy falls back to embedding-distance mining, ensuring consistent negative count across all instances. We analyze the fallback stratum separately in stratified evaluation (§5).\n\n### Difficulty Gradient\n\nThe three strategies impose an expected difficulty ordering. Random negatives are easiest (low similarity, no structural constraint). Embedding-distance negatives are hardest (highest pretrained similarity, no structural constraint). Dataflow-aware negatives apply structural filtering via CodeQL reachability and rank candidates by BM25, selecting files that are structurally disconnected yet lexically similar to the query. We quantify this ordering empirically via the *negative difficulty* metric: the mean cosine similarity between each query and its assigned negatives in the pretrained space (§5).\n\n### Relationship to BM25 Baselines\n",
      "numLines": 20,
      "startLine": 69,
      "totalLines": 117
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_013uFkdpTEd1hdqrgahVkqUK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
  "offset": 14,
  "limit": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "2606b734-96f6-4653-9018-904aa5d29869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RxYdmdQXWpt6muXMJQF5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T02:22:27.634Z_

<details><summary>↩ Tool result · `toolu_013uFkdpTEd1hdqrgahVkqUK`</summary>

```text
14	
15	We present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.
16	Using CodeQL \cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.
17	We compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.
18	All experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \cite{hui2024qwen25coder} and StarCoder2-3B \cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "39dbe798-a18d-400d-9c2d-fcd5af0f68cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v2.md",
      "content": "\nWe present a systematic study of hard negative mining strategies for contrastive code retrieval, introducing structure-aware negative selection guided by inter-procedural data-flow analysis.\nUsing CodeQL \\cite{github2019codeql}, we extract scope-bounded data-flow graphs that capture taint propagation paths across function boundaries within repositories, then leverage these graphs to identify structurally connected file pairs.\nWe compare three strategies under controlled conditions: (1) random sampling, (2) static embedding-distance mining via FAISS \\cite{johnson2021faiss} nearest-neighbor lookup, and (3) dataflow-aware mining that selects negatives from structurally **disconnected** files ranked by BM25.\nAll experiments use identical training pipelines, evaluation protocols, and multiple random seeds across two decoder-only encoders---Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} and StarCoder2-3B \\cite{li2023starcoder}---which differ in pretraining corpora and representation geometry, enabling analysis of strategy--encoder interactions.\n",
      "numLines": 6,
      "startLine": 14,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01NCL3gnGrUdiSJWDQ4a6cEt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
  "offset": 19,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "5ac23992-2bc4-46dc-8dc8-5661cf306e2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RxYdmdQXWpt6muXMJQF5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1100,
      "cache_read_input_tokens": 36739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1100
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T02:22:28.772Z_

<details><summary>↩ Tool result · `toolu_01NCL3gnGrUdiSJWDQ4a6cEt`</summary>

```text
19	For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\theta^*_{\text{loss}}$ (minimum validation loss) and $\theta^*_{\text{R@1}}$ (maximum validation Recall@1).
20	
21	**Negative Mining.** Embedding-distance negatives are mined using FAISS \cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.
22	
23	**Hardware.** All experiments are conducted on a single node with 2$\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\times$ 3 seeds $\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "c5c1fe25-053c-4875-994a-1b30ced40648",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md",
      "content": "For the initial seed (s42), we train for 3 epochs to obtain a full overfitting curve; subsequent seeds (s43, s44) train for 2 epochs with early stopping (patience 2 evaluations) based on validation loss. Evaluation is performed every 500 steps. We maintain dual checkpoints: $\\theta^*_{\\text{loss}}$ (minimum validation loss) and $\\theta^*_{\\text{R@1}}$ (maximum validation Recall@1).\n\n**Negative Mining.** Embedding-distance negatives are mined using FAISS \\cite{johnson2021faiss} over frozen pretrained embeddings. BM25 negatives are mined by indexing all repository files with Okapi BM25 and selecting the top-$K$ highest-scoring non-gold files per query. Dataflow-aware negatives use the CodeQL-derived structural connectivity graph to identify structurally disconnected non-gold files, then rank them by BM25 to select the top-$K$ negatives (§3.4). All mining is **static**—performed once before training and not refreshed.\n\n**Hardware.** All experiments are conducted on a single node with 2$\\times$ NVIDIA RTX PRO 6000 (96 GB VRAM each). Qwen and StarCoder training chains run on separate GPUs in parallel. Each run (single strategy, single seed, single encoder) requires approximately 5–7 hours; the core experiment matrix (3 strategies $\\times$ 3 seeds $\\times$ 2 encoders = 18 runs) completes in approximately 120 GPU-hours. BM25-mined negative runs are conducted separately and reported as a supplementary comparison.",
      "numLines": 5,
      "startLine": 19,
      "totalLines": 144
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

修改完成，验证结果：

| 检查项 | 状态 |
|--------|------|
| `f ∈ R_G` 作为 negative 选择约束 | 已消除（改为 `f \notin R_G(q)`） |
| "structurally connected" 作为 negative 描述 | 已改为 "structurally disconnected"（3个文件共5处） |
| BM25 排序 | 保留不变（无 `sim(E_θ0)` 回退） |
| D041 标记追加 | 3个文件均已追加 `回滚约束方向 2026-05-15` |

注：`introduction_v2.md:23` 中 "structurally connected non-gold rate" 是 Z% 统计指标（描述 connected 文件中 non-gold 的比例），不是 negative 选择方向，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "uuid": "0ea1ac37-0c82-4c01-a1ac-b2eae58f0ac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01765PV7MNMA7UYXMEvhT8yN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 37839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2078
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 44_

修改完成，验证结果：

| 检查项 | 状态 |
|--------|------|
| `f ∈ R_G` 作为 negative 选择约束 | 已消除（改为 `f \notin R_G(q)`） |
| "structurally connected" 作为 negative 描述 | 已改为 "structurally disconnected"（3个文件共5处） |
| BM25 排序 | 保留不变（无 `sim(E_θ0)` 回退） |
| D041 标记追加 | 3个文件均已追加 `回滚约束方向 2026-05-15` |

注：`introduction_v2.md:23` 中 "structurally connected non-gold rate" 是 Z% 统计指标（描述 connected 文件中 non-gold 的比例），不是 negative 选择方向，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 82850,
  "duration_api_ms": 83892,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "e920ab01-1271-44ad-8b0a-ec36c281cbe3",
  "total_cost_usd": 0.3518485,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 28470,
    "cache_read_input_tokens": 143200,
    "output_tokens": 4029,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28470,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 257,
        "cache_read_input_tokens": 37839,
        "cache_creation_input_tokens": 2078,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2078
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1461,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001551,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4029,
      "cacheReadInputTokens": 143200,
      "cacheCreationInputTokens": 28470,
      "webSearchRequests": 0,
      "costUSD": 0.3502975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ba18e727-eb9d-4b84-ba24-8e27be0b5321"
}
```

</details>

---
