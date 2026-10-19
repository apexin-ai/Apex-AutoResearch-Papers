# review experiments v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_review_experiments-v1_20260515T134308.jsonl`
- **Structured JSON:** [`2ee2c023196ed280f930.json`](../../sessions/2e/2ee2c023196ed280f930.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-15T13:47:34.372940+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
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

_source line 2 · 2026-05-15T13:47:34.373288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:47:34.373457+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
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

_source line 4 · 2026-05-15T13:47:34.373621+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/experiments_v1.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:47:34.373767+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
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

_source line 6 · 2026-05-15T13:47:34.374021+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a 
…[truncated 13048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:47:34.374195+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "structfuse-context",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "structfuse-context",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:47:34.374878+00:00_

&lt;persisted-output>
Output too large (53.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3d71ee37-20db-413a-b9a1-717587d4a7ef/tool-results/toolu_012D4gVpTL6c3gYvs6N15Hhp.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeou
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:47:34.375091+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
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

_source line 10 · 2026-05-15T13:47:34.375232+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:47:34.375386+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*experiments*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*experiments*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:47:34.375528+00:00_

artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
logs/workers/worker_ssh_all_experiments_progress_check_20260514T000504.log
logs/workers/worker_ssh_all_experiments_progress_check_20260514T000504_result.json
artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
logs/workers/worker_write_experiments-skeleton_20260514T225046.log
logs/chats/worker_write_experiments-skeleton_20260514T225046.lock
logs/chats/worker_write_experiments-skeleton_20260514T225046.jsonl
logs/workers/worker_write_experiments-skeleton_20260514T225046_result.json
artifacts/_project/paper/experiments_v1_054f8d.md
logs/workers/worker_fix_experiments-v1-warnings_20260514T225801.log
logs/workers/worker_fix_experiments-v1-warnings_20260514T225801_result.json
artifacts/_project/paper/experiments_v1_eccca0.md
logs/workers/worker_fix_experiments-v1-round2_20260514T230518.log
logs/workers/worker_fix_experiments-v1-round2_20260514T230518_result.json
artifacts/_project/paper/experiments_v1_bcd130.md
artifacts/_project/paper/experiments_v1_d4b180.md
artifacts/_project/paper/experiments_v1.md
logs/workers/worker_fix_experiments-v1-placeholders_20260515T031409.log
logs/chats/worker_fix_experiments-v1-placeholders_20260515T031409.lock
logs/chats/worker_fix_experiments-v1-placeholders_20260515T031409.jsonl
logs/workers/worker_fix_experiments-v1-placeholders_20260515T031409_result.json
logs/workers/worker_fix_experiments-v1-plac
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:47:34.375707+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
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

_source line 14 · 2026-05-15T13:47:34.375840+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:47:34.375963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3d71ee37-20db-413a-b9a1-717587d4a7ef/tool-results/toolu_012D4gVpTL6c3gYvs6N15Hhp.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/3d71ee37-20db-413a-b9a1-717587d4a7ef/tool-results/toolu_012D4gVpTL6c3gYvs6N15Hhp.txt"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:47:34.376650+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeout on directCallEdge predicate). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated to 1/4 workers.\", \"eta_cst\": \"2026-05-15T22:00\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\
…[truncated 52492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:47:34.376874+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/experiments_v1.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:47:34.377104+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T13:47:34.377272+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:47:34.377459+00:00_

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
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T13:47:34.377721+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "14.?288",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Grep",
  "tool_args": {
    "pattern": "14.?288",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T13:47:34.377889+00:00_

Found 39 files
logs/workers/worker_review_experiments-v1_20260515T134308.log
logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer.jsonl
logs/chats/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director.jsonl
decisions.yaml
logs/chats/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_paper_agent.jsonl
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_20260515T125358_974829.jsonl
artifacts/paper_drafts/experiments_v1.md
logs/workers/worker_writing_experiments-v1-skeleton_20260515T102528.log
logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260515T041145_721590.jsonl
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260515T041127_259791.jsonl
logs/workers/worker_fix_experiments-v1-placeholders_20260515T035615_result.json
logs/workers/worker_fix_experiments-v1-placeholders_20260515T035615.log
logs/workers/worker_fix_experiments-v1-placeholders_20260515T031409_result.json
logs/chats/worker_fix_experiments-v1-placeholders_20260515T031409.jsonl
logs/workers/worker_fix_experiments-v1-placeholders_20260515T031409.log
logs/workers/worker_fix_d042-data-pipeline-numbers_20260515T021433_result.json
logs/workers/worker_fix_d042-data-pipeline-numbers_20260515T021433.log
artifacts/_project/paper/experiment_setup_v1.md
artifacts/paper_drafts/experiment_setup_v1.md
logs/workers/worker_fix_d041-method-drafts_20260515T020954.log
logs/workers/worker_fix_claim2-wording-critical_20260515T020243.log
logs/workers/worker_write_method-and-setup-draft_20260515T015255.log
logs/workers/worker_fix_repo-count-clarification_20260514T231412.log
logs/workers/worker_fix_gpu_resume_with_bm25_20260514T175853.log
logs/workers/worker_code_plan_018_bm25_mining_20260514T163941.log
logs/chats/worker_check_training_progress_loop5_20260514T080030.jsonl
logs/workers/worker_check_training_progress_loop5_20260514T080030.log
logs/chats/archive/feishu_group_oc_a824c537c71f24fe2c80800ab4d82d39_reviewer_20260514T075838_38669
…[truncated 855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T13:47:34.378057+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "14.?288",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Grep",
  "tool_args": {
    "pattern": "14.?288",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T13:47:34.378194+00:00_

843-  summary: 实现 pool=50 独立评估替代当前 pool=8；删除 R@10 报告；数据管道数字等 M1v2 完成后统一重算
844-  rationale: 'Reviewer critical: 当前 eval pool=8（1+7 negatives），论文误写 pool=50。pool=8
845:    下 R@10 恒为 1.0 无意义，R@1 区分度也受质疑。实现 pool=50 独立评估只需推理（不重训练），在已保存 checkpoints 上跑即可。数据管道数字（15133/15897/14288）存在多处不一致，根因是
846-    M1 reextract v2 尚未完成，完成后全链路重算一次统一。'
847-  related_experiments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_experiments-v1_20260515T134308",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T13:47:34.378435+00:00_

All data collected. Here's the review:

---

## 审查结果: NEEDS_REVISION

### 问题清单 (按严重程度)

**1. [CRITICAL] Seed 方差远大于 treatment effect，统计力不足**

唯一完成的配对比较 (Qwen embedding_s43 vs random_s43) treatment effect = +0.52pp，而 random 策略内部的跨 seed 方差高达 4.82pp（s44=0.6009 vs s42=0.5527）。Treatment effect 仅为 seed 方差的 ~1/9。草稿声称将报告 "bootstrap 95% confidence intervals for all pairwise comparisons"，但 n=3 seeds 在这个方差水平下 CI 几乎必然跨零。

草稿 §4.3.2 提到了 s44 异常但未量化这个比值，也未讨论对 Claim 1 ("reliable improvement") 的影响。reviewer 会立刻指出：你声称的 "reliable" improvement 在统计上无法与噪声区分。

**建议**: 在 §4.3.2 显式报告 treatment effect vs seed variance 的比值。在 Discussion 中坦诚讨论统计力限制。考虑是否需要增加 seed 数量（paper_framing 的 contingency plan 应提前考虑这一场景）。

---

**2. [MAJOR] StarCoder random_s43 数据已就绪但草稿仍为 placeholder**

Registry 显示 `m2_full_starcoder_resumed` 的 `random_s43` 已完成 (best_R@1=0.4912, early_stopped step 2500)，但 Table 1 StarCoder 面板中 random_s43 仍为 X.XX。同时 `random_s44` 的 eval@500 R@1=0.4848 也已可用（虽然未完成，不应填入正式表格）。

**建议**: 更新 StarCoder random_s43 = 0.4912。

---

**3. [MAJOR] 数据管道数字 14,288 已被 D042 标记为待重算**

§4.1 声称 "14,288 yield resolvable positive files"。decisions.yaml D042 明确指出 "数据管道数字（15133/15897/14288）存在多处不一致，根因是 M1 reextract v2 尚未完成，完成后全链路重算一次统一"。我通过 plan_018 metrics 交叉验证 14,288 = 各 seed 的 train+val 之和（s42: 11,308+2,980=14,288; s43: 11,236+3,052=14,288; s44: 11,264+3,024=14,288），当前数值本身一致。但 M1v2 完成后（ETA 今晚 22:00 CST）若重建训练数据，此数字可能变化。

**建议**: 确认当前 M2 训练数据是否基于 pre-M1v2 数据。如果是，明确说明；如果 M1v2 数据将用于后续训练，标记为 provisional。

---

**4. [MAJOR] Claim 3（CodeQL 可扩展性）在实验章节无专属小节**

paper_framing 列出 Claim 3: "Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline"，关键证据 (0% timeout, 78% Z%, 123/131 repos) 来自 plan_006_scalability。但 §4 中仅在 §4.1 Dataset 段落提及了部分数字，没有 dedicated analysis。plan_006 的 tier-wise scalability 数据（small/medium/large/xlarge）完全未出现。

**建议**: 增加 §4.3.x "Structural Extraction Scalability" 小节，或在 §4.1 扩展报告 plan_006 关键指标。

---

**5. [MAJOR] BM25 baseline (§4.3.4) 和 Pool Size Sensitivity (§4.3.6) 完全是 placeholder**

plan_018 Phase 2（GPU 训练）仍为 QUEUED，plan_019 未启动。Dream 审稿三档一致认定缺 BM25 baseline 是 "#1 structural gap"。这两个小节的完成对论文可投稿性是 blocking dependency。

**状态确认**: Phase 1 (CPU mining) 已完成，BM25 数据已就绪。这不是草稿问题而是实验进度问题，但草稿应明确标注 blocking 依赖。

---

**6. [MAJOR] 无统计检验规范**

§4.1 Seeds 段落说 "We report bootstrap 95% confidence intervals for all pairwise comparisons"，但未指定 bootstrap 方法细节（resample unit 是什么？seed-level resampling n=3 还是 instance-level？bootstrap iterations 数量？）。n=3 seeds 的 seed-level bootstrap CI 几乎无统计意义。如果用 instance-level bootstrap（在 val set ~3K instances 上），需要说明 instance 间非独立性（同 repo 的 instances 相关）。

**建议**: 明确 bootstrap 的 resampling unit 和方法。如果是 seed-level，坦诚承认 n=3 的限制。

---

**7. [MINOR] 训练/验证集大小应报告精确范围**

§4.1 写 "~11,300 training and ~3,000 validation"。实际各 seed 不同: train 11,236–11,308, val 2,980–3,052。建议改为 "11,236–11,308 training and 2,980–3,052 validation instances (varying by seed due to stratified splitting)"。

---

**8. [MINOR] RepoBench-R 引用 placeholder**

§4.4 Limitations: `\cite{[TBD: key]}` 需补充。RepoBench 原始论文: Liu et al., 2023.

---

**9. [MINOR] §4.3.5 neg_difficulty 分析与训练结果的桥接缺失**

neg_difficulty table 数据完整且经 registry 验证全部正确（3 位小数均匹配）。但该分析旨在解释 strategy × encoder interaction，而 interaction 的训练证据（dataflow 结果）全部是 placeholder。当前该节是 self-contained 的 pretrained-space 分析，但与 §4.2 的因果连接完全依赖于尚未产出的 dataflow 训练数据。

**建议**: 在 §4.3.5 开头增加一句前向引用，明确该分析的解释力取决于 §4.2 的完整结果。

---

**10. [MINOR] margin compression 百分比方向性表述可能误导**

§4.3.5: "embedding-distance mining reduces Qwen's margin by 77% (0.074→0.017) versus 65% for StarCoder (0.194→0.067)"。数学正确（(0.074-0.017)/0.074=77%），但 "reduces margin" 的表述暗示这是坏事。在 hard negative mining 语境下，更小的 margin = 更难的 negatives = 更强的训练信号。建议改为更中性的表述，如 "compresses the margin"。

---

### 数字准确性审计

| 草稿数字 | Registry 来源 | 状态 |
|---|---|---|
| 44,173 instances | m1_extraction: 50,869-6,696 skip = 44,173 | ✅ |
| 123 repositories | m1_extraction: repos_with_output=123 | ✅ |
| 15,897 (36.0%) | m1_extraction: 15,133+764=15,897, rate=0.36 | ✅ |
| 14,288 | plan_018: 各 seed train+val=14,288 | ✅ (D042 待确认) |
| ~11,300 train / ~3,000 val | plan_018: 11,236-11,308 / 2,980-3,052 | ✅ (约数) |
| Qwen random s42=0.5527 | m2_full_qwen: random_s42 best_R@1=0.5527 | ✅ |
| Qwen random s43=0.5554 | m2_full_qwen: random_s43 best_R@1=0.5554 | ✅ |
| Qwen random s44=0.6009 | m2_full_qwen_continued: random_s44 best_R@1=0.6009 | ✅ |
| Qwen embed s43=0.5606 | m2_full_qwen_continued: embedding_s43 best_R@1=0.5606 | ✅ |
| StarCoder random s42=0.4604 | m2_full_starcoder: random_s42 best_R@1=0.4604 | ✅ |
| neg_difficulty 全表 (12 cells) | neg_difficulty_analysis: qwen_2048 + starcoder_2048 | ✅ (全部匹配) |
| pos_sim Qwen=0.986 | 0.9855 → 0.986 (3dp rounding) | ✅ |
| pos_sim StarCoder=0.798 | 0.7985 → 0.799 (草稿写0.799, framing写0.798) | ⚠️ 微小不一致 |
| margin ratio 2.6–4.1× | registry sc_qwen_margin_ratio_2048: 2.61–4.07 | ✅ |

pos_sim StarCoder: §4.1 写 "0.798"，§4.3.5 Table 写 "0.799"。Registry 值 0.7985 四舍五入到 3dp = 0.799。§4.1 的 0.798 不准确。

---

### 修改建议（优先级排序）

1. **[必须]** 在 §4.3.2 或 Discussion 中量化 seed variance vs treatment effect，讨论统计力。这决定了 Claim 1 的 "reliable" 措辞是否站得住脚。
2. **[必须]** 更新 StarCoder random_s43 = 0.4912。
3. **[必须]** 确认 14,288 在 M1v2 完成后是否仍有效，或标记为 provisional。
4. **[强烈建议]** 为 Claim 3 增加 scalability analysis 小节。
5. **[强烈建议]** 明确 bootstrap CI 方法论（resampling unit, 是否 cluster by repo）。
6. **[建议]** 统一 StarCoder pos_sim: §4.1 的 0.798 → 0.799。
7. **[建议]** 精确化 train/val 数量描述。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_experiments-v1_20260515T134308"
}
```

</details>

---
