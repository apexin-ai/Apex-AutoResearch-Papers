# review experiments v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_review_experiments-v1_20260515T140139.jsonl`
- **Structured JSON:** [`eeedc0cc8db25ac47346.json`](../../sessions/ee/eeedc0cc8db25ac47346.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-15T14:04:42.003484+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T14:04:42.004031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T14:04:42.004331+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper/experiments_v1.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "paper/experiments_v1.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T14:04:42.004670+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments_v1.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T14:04:42.004911+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T14:04:42.005323+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a 
…[truncated 13048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T14:04:42.005582+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "structfuse-context",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "structfuse-context",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T14:04:42.006643+00:00_

&lt;persisted-output>
Output too large (53.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3fdfc3ae-29d4-40a0-a3c5-60e981fc7935/tool-results/toolu_01MNg1GapZZt8M6gsfrqx4jX.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeou
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:04:42.006922+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "experiment_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "experiment_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T14:04:42.007555+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:04:42.007853+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*experiments_v1*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*experiments_v1*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T14:04:42.008078+00:00_

artifacts/_project/paper/experiments_v1_054f8d.md
artifacts/_project/paper/experiments_v1_eccca0.md
artifacts/_project/paper/experiments_v1_bcd130.md
artifacts/_project/paper/experiments_v1_d4b180.md
artifacts/_project/paper/experiments_v1.md
artifacts/paper_drafts/experiments_v1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T14:04:42.008310+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*experiment_plan*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T14:04:42.008547+00:00_

logs/workers/worker_knowledge_experiment_plan_20260512T102157.log
logs/workers/worker_knowledge_experiment_plan_20260512T102157_result.json
experiment_plan.lock
logs/workers/worker_knowledge_update_experiment_plan_20260514T025324.log
logs/workers/worker_knowledge_update_experiment_plan_20260514T025324_result.json
experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T14:04:42.008845+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3fdfc3ae-29d4-40a0-a3c5-60e981fc7935/tool-results/toolu_01MNg1GapZZt8M6gsfrqx4jX.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3fdfc3ae-29d4-40a0-a3c5-60e981fc7935/tool-results/toolu_01MNg1GapZZt8M6gsfrqx4jX.txt"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:04:42.009918+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeout on directCallEdge predicate). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated to 1/4 workers.\", \"eta_cst\": \"2026-05-15T22:00\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\
…[truncated 52492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:04:42.010250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T14:04:42.010809+00:00_

1	# §4 Experiments
2	
3	## §4.1 Experimental Setup
4	
5	**Dataset.** We construct a code retrieval dataset from SWE-smith \cite{yang2025swesmith}, a large-scale collection of synthetic Python bug-fix instances derived from real-world GitHub repositories. After excluding repositories with failed clones, 44,173 instances across 123 repositories remain. Our structural extraction pipeline (\S3.2) produces inter-procedural data-flow graphs for 15,897 instances (36.0\%); of these, 14,288 yield resolvable positive files and are retained for training. Per-seed stratified splits produce $\sim$11,300 training and $\sim$3,000 validation instances, preserving repository-level distribution across partitions.
6	
7	**Encoders.** We select two 3B-parameter decoder-only code models representing distinct pretraining paradigms: **Qwen2.5-Coder-3B** \cite{hui2024qwen25coder} (Fill-in-the-Middle on curated multilingual code) and **StarCoder2-3B** \cite{lozhkov2024starcoder2} (multi-task FIM on The Stack v2). These encoders exhibit markedly different pretrained representation geometries: Qwen operates in a near-saturated similarity regime (mean positive cosine similarity 0.986), while StarCoder maintains healthy separation (0.798). This divergence enables examination of whether mining strategy effectiveness interacts with encoder properties---a core question of our study.
8	
9	**Training.** All fine-tuning details follow \S3.4: LoRA ($r{=}16$, $\alpha{=}32$) on $W_q$/$W_v$, InfoNCE with learnable $\tau$, AdamW ($\text{lr}{=}2{\times}10^{-5}$). Seed 42 trains for 3 epochs without early stopping to provide a full overfitting diagnostic curve; seeds 43 and 44 train for 2 epochs with early stopping (patience 2, evaluated every 500 steps).\footnote{The 3-epoch seed-42 runs enable analysis of post-peak degradation (\S4.3.3); all checkpoint selection uses the same dual-checkpoint protocol regardless of epoch count.} We maintain dual checkpoints per run: $\theta^*_{\text{loss}}$ (best validation
…[truncated 13793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T14:04:42.011084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T14:04:42.011388+00:00_

1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
5	    vs gold statistics'
6	  priority: P0
7	  gpu_budget_hours: 0
8	  deps: []
9	  registry_id: m1_extraction
10	  mvp_registry_id: mvp_p1_codeql_feasibility
11	- id: plan_002
12	  claim: 1
13	  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
14	    3 seeds each, Qwen2.5-Coder-3B LoRA'
15	  priority: P0
16	  gpu_budget_hours: 200
17	  deps:
18	  - plan_001
19	  registry_id: m2_embed_verify
20	  mvp_registry_id: mvp_p2b_contrastive_training
21	  full_registry_ids: ["m2_full_qwen", "m2_full_starcoder"]
22	- id: plan_003
23	  claim: 1
24	  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
25	    checkpoint, Qwen3.6-27B agent'
26	  priority: P0
27	  gpu_budget_hours: 40
28	  deps:
29	  - plan_002
30	  notes: 'eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos
31	    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.'
32	- id: plan_004
33	  claim: 1
34	  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
35	    LLM agent'
36	  priority: P1
37	  gpu_budget_hours: 15
38	  deps:
39	  - plan_002
40	  notes: 'eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via
41	    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting
42	    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs —
43	    dream reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but
44	    not RepoBench-R) across all 3 tiers.'
45	- id: plan_005
46	  claim: 2
47	  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
48	    negatives 何时最有害'
49	  priority: P1
50	  gpu_budget_hours: 5
51	  deps:
52	  - plan_002
53	  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:
54	    repo size 
…[truncated 5991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T14:04:42.012923+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T14:04:42.013238+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ROADMAP.md\", \"content\": \"# StructFuse — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:58 UTC | 更新原因: D052 Scenario C/D 应急方案 + D053 plan_005 升 P0\\n\\n## 核心方向\\nEmbedding-distance mining reliably improves contrastive code retrieval at zero additional cost (D049 软化 framing). BM25 baseline empirically closes CoCoHaNeRe correction argument. Structure-grounded negatives conditional on representation saturation (n=2, exploratory per D035). 详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（post-MVP）+ 审稿进行中\\n- **Qwen (cuda:0)**: embed_s44 running. embed_s43 done: best_by_R@1=0.5606, Δ+0.52pp\\n- **StarCoder (cuda:1)**: random_s43 done (R@1=0.4912), random_s44 running → 后续 embed×3 + dataflow×3\\n- **M2 ETA**: Qwen ~May 17 21:00 CST, StarCoder ~May 20 01:00 CST\\n- **BM25 Phase 2**: tmux watcher 就绪，M2 完成后自动触发\\n- **m1_reextract_v2**: ~90.5% done, ETA May 15 19:00 CST\\n- **写作**: Intro v1 ✅ PASS | Method v1 ✅ PASS | Related Work v1 ✅ PASS | Abstract v2 待审 | Experiments v1 待审 | Conclusion v1 待审\\n- **已完成**: plan_017 ✅ | plan_018 Phase 1 ✅ | neg_difficulty 可视化 ✅ | K/checkpoint 文档 ✅\\n\\n## ⚠️ Claim 1 Delta 状况 (D048→D049→D052)\\n- s43 best_by_R@1: Δ+0.52pp | Fixed-checkpoint 均值 ~0.82pp\\n- s44: embed 仍在跑，暂无最终 delta\\n- D052 应急方案已定义：Scenario C (Δ<0.5pp/CI跨零) → fixed-checkpoint + pool=50；Scenario D (Δ≈0) → 叙事重心转 Claim 2+3\\n- **翻盘点**: pool=50 评估（pool=8 噪声 ±0.5pp 与 delta 同阶）\\n\\n## Post-M2 优先级 (D035, D053)\\n| Priority | Plan | Description | GPU hours | 状态 |\\n|----------|------|-------------|-----------|------|\\n| **P0** | D045 | 统计分析: best_by_R@1 + leave-one-out + seed variance | 0h (分析) | M2完成后 |\\n| **P0** | pool=50 | 重新评估所有 best checkpoint (D042/D048) | ~2h | M2完成后 |\\n| **P0** | plan_005 | 分层分析 (Claim 2 定量支撑, D053 升级) | 0h (分析) | M2完成后 |\\n| **P0** | plan_018 P2 | BM25 训练 Qwen+StarCoder | 15h | watcher 自动触发 |\\n| **P0** | plan_003 | SWE-
…[truncated 2669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T140139",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T14:04:42.013686+00:00_

All data collected. Let me compile the review.

---

## 审查结果: NEEDS_REVISION

### 问题清单 (按严重程度)

**1. [CRITICAL] 草稿 >70% 是 TBD 占位符，不具备审查实质内容的条件**

18 个 M2 runs 仅完成 ~6 个（Qwen: random×3 + embed_s43 done, embed_s44 running; StarCoder: random_s42 done, random_s43 done, random_s44 running）。Main Results 两张表中仅填入 4 个 Qwen 值和 1 个 StarCoder 值。所有 mean、CI、delta 均为 X.XX。Claim 1 的核心证据（embedding > random across seeds and encoders）目前只有 1 个完整 seed 比较（Qwen s43: 0.5606 vs 0.5554, Δ+0.52pp）。**无法对 claim-evidence 对齐做出实质判断。**

建议：M2 全部完成后重新提交审查。当前版本仅作为结构模板评估。

**2. [CRITICAL] Claim 3（CodeQL scalability）在 Experiments 中完全缺失**

plan_006 在 registry 中标记为 DONE，有详细 metrics（0% timeout, 78% Z%, 123/131 repos），但 experiments_v1.md 没有任何对应的 subsection 或 table。Claim 3 是 paper_framing.md 的三个 core claims 之一，实验章节必须有对应证据。

建议：添加 §4.3.x "Structural Extraction Scalability" subsection，报告 timeout rate, Z% by repo tier, coverage。

**3. [CRITICAL] Seed 44 outlier 未做统计处理，存在 inflate mean 的风险**

Qwen random_s44 R@1=0.6009，比 s42/s43（0.5527/0.5554）高出 ~4.5pp。3-seed mean 会被严重拉高。如果 embedding_s44 也偶然较高（当前 eval@500 R@1=0.5942），mean delta 可能完全由 seed variance 驱动而非策略效应。草稿 §4.3.2 承认了这一点但全部 TBD。

建议：报告 median 和 leave-one-out 分析作为 primary robustness check。若排除 s44 后 embedding > random 仍成立，才能支撑 "reliable"。D051 已经要求 mean ± std，但 std 可能比 treatment effect 还大。

**4. [MAJOR] 缺少 plan_005 分层分析 subsection**

ROADMAP D053 已将 plan_005 升级为 P0（Claim 2 唯一定量支撑），experiment_plan.yaml 列出 5 维分层分析，但 experiments_v1.md 没有对应 subsection。Claim 2（dataflow × geometry interaction）在草稿中仅靠 §4.3.5 neg difficulty 的 pretrained-space 分析支撑，没有 training R@1 分层数据。

建议：添加 §4.3.x "Stratified Analysis" subsection。

**5. [MAJOR] "zero additional computational cost" claim 未提供计量支撑**

Claim 1 反复说 "zero additional computational cost over random sampling"，但草稿从未量化各策略的 mining time。Embedding-distance mining 需要先跑一遍 encoder forward pass 计算所有文件的 embedding，这不是零成本。

建议：报告各策略的 mining wall-clock time（random: 0, BM25: X min, embedding: X min, dataflow: X min CodeQL + X min BM25）。如果 embedding mining 的一次性成本远小于训练时间，可以说 "negligible additional cost"，但不能说 "zero"。

**6. [MAJOR] 数字一致性问题：StarCoder pos_sim 文本 vs 表格不一致**

§4.1 line 7: "StarCoder maintains healthy separation (0.798)"
Table 5 line 161: StarCoder random pos_sim = 0.799

Registry ground truth: 0.7985。两者都是合理的四舍五入，但同一篇论文中不一致会引发 reviewer 质疑。

建议：统一为 0.80 或 0.799。

**7. [MAJOR] §4.3.5 interpretive language 过强**

- Line 171: "embedding-distance negatives occupy **precisely the region** where the encoder is most uncertain" — "precisely" 暗示精确定位，实际是宽泛的 distributional pattern
- Line 171: "providing **maximal** gradient signal" — 未经证明。gradient signal 没有被测量

建议：改为 "negatives drawn from the high-similarity tail of the pretrained distribution, where the encoder has least separation" 和 "providing stronger gradient signal"。

**8. [MAJOR] BM25 overlap 87.1% 未讨论**

plan_018 Phase 1 数据显示 BM25 vs embedding negatives 的 overlap = 87.1%。这意味着两种策略在 87% 的 negative 选择上完全一致，策略差异主要来自 13% 的不同。这对 "different strategies explore different dimensions of difficulty" 的叙事是严重挑战。草稿未提及此 finding。

建议：在 §4.3.4 或 §4.4 Discussion 中报告 overlap 率，讨论其对策略区分度的 implication。特别是 small repos（<50 files）overlap 更高（66.8% top-7 Jaccard），说明策略差异仅在大 repo 中有意义。

**9. [MINOR] s42 regime 不一致未充分说明**

s42 跑 3 epochs 无 early stopping，s43/s44 跑 2 epochs 有 early stopping。脚注提到是为了 "overfitting diagnostic curve"，但这意味着 s42 的 best_by_R@1 checkpoint 搜索范围比其他 seed 大 50%（4242 vs 2816 steps），引入 checkpoint selection bias。

建议：在 §4.3.1 或 Limitations 中明确说明这一 confound。D047 已标记需要 s42 重跑（2-epoch regime），建议优先执行。

**10. [MINOR] Pool 构造细节缺失**

§4.1 说 "Pool-based retrieval with pool size 50 (1 positive + 49 negatives)" 但未说明 49 个 negatives 如何从 repo 中采样。是随机？按距离？同 repo 内？跨 repo？

建议：补充 pool 构造协议。

**11. [MINOR] 无 pretrained baseline（zero-shot retrieval）**

所有策略都是 contrastive fine-tuning 后的结果。缺少 pretrained encoder 直接做 retrieval 的 baseline，无法说明 fine-tuning 本身的价值。

建议：添加 "Pretrained (no fine-tuning)" 行到 Table 1/2。

**12. [MINOR] §4.4 Limitations 用 plan 编号**

Line 190: "Sensitivity to pool size at evaluation time will be reported in §4.3.6 (pending plan_019 completion)" — plan_019 是内部编号，不应出现在论文中。

建议：删除所有 plan_NNN 引用。

### 修改建议

1. **等 M2 完成**后填入所有数字，重新提交审查
2. **添加 3 个缺失 subsection**: CodeQL scalability (Claim 3), Stratified analysis (Claim 2), Pretrained baseline
3. **量化 mining cost**: 一个表格比较各策略的 data preparation wall-clock time
4. **统一数字精度**: 全文采用一致的小数位数规则（建议 3 位）
5. **弱化 interpretive language**: §4.3.5 中的 "precisely"/"maximal" → "approximately"/"stronger"
6. **报告 BM25-embedding overlap**: 在 Discussion 中讨论策略重叠率的 implication
7. **处理 s44 outlier**: 报告 median + leave-one-out + 排除 s44 后的 robustness check
8. **清理 plan 编号**: 论文中不应出现内部 tracking ID

### 审稿攻击面预演

| 攻击点 | 严重度 | 预期 reviewer 措辞 | 防御准备 |
|--------|--------|-------------------|----------|
| **Effect size 仅 +0.52pp**（s43）| 致命 | "The improvement is within noise range. Is this practically meaningful?" | 需 3-seed mean + CI 证明显著性；若 CI 跨零则 Claim 1 需大幅 reframe |
| **Seed 44 outlier** | 高 | "Seed 44 inflates your means. Report median or exclude it." | Leave-one-out table showing ranking holds; per-seed val difficulty check (D050) |
| **Pool=50 太小** | 高 | "Real repos have hundreds of files. Does your finding hold at pool=200+?" | plan_019 必须完成并报告 |
| **只有 2 个 encoder** | 中 | "n=2 is anecdotal. You need ≥3 for any geometry interaction claim." | 已在 Claim 2 用 "exploratory observation" 降级，但 reviewer 可能仍嫌不够 |
| **36% structural coverage → 64% fallback** | 中 | "Your dataflow strategy is really 36% dataflow + 64% embedding. You're testing a diluted mixture." | plan_005 分层分析必须显示 dataflow-rich 子集有更大差异 |
| **无 downstream task** | 高 | "R@1 improvement doesn't mean anything if it doesn't help fix bugs." | plan_003 SWE-bench 必须完成 |
| **BM25 训练 baseline 缺失** | 高 | "You claim CoCoHaNeRe's BM25-proxy caused harm but don't train with BM25 negatives yourself." | plan_018 Phase 2 必须完成 |
| **"Zero cost" 未证明** | 中 | "Embedding mining requires a forward pass over the corpus. That's not zero cost." | 量化 mining time 并改措辞为 "negligible" |

**最危险场景**: 3-seed Qwen mean embedding-random delta < 1pp 且 CI 跨零。此时 Claim 1 的 "reliable improvement" 不成立，需要启动 D052 Scenario C/D 应急方案。当前唯一完成的 seed (s43) delta 仅 +0.52pp，这个风险是真实存在的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_experiments-v1_20260515T140139"
}
```

</details>

---
