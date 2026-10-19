# code plan005 stratified prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 0
- **Tool calls:** 50
- **Original source:** `logs/chats/worker_code_plan005-stratified-prep_20260515T050005.jsonl`
- **Structured JSON:** [`117a370500abb580486e.json`](../../sessions/11/117a370500abb580486e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

101 recorded events

### Tool call

_source line 1 · 2026-05-15T05:09:54.778912+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T05:09:54.779255+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T05:09:54.779433+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "structfuse-context",
  "filters": "{'exp_id': 'plan_005'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "structfuse-context",
    "filters": "{'exp_id': 'plan_005'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T05:09:54.779577+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1305}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T05:09:54.779728+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "decisions.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "decisions.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T05:09:54.780001+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml\", \"content\": \"_next_id: 46\\ndecisions:\\n- id: D001\\n  date: 2026-05-12 09:57 UTC\\n  summary: 'MVP 设计: CodeQL 试点(10 repos) + 迷你对比训练(500 instances) 验证核心假设'\\n  rationale: 13 天 DDL，需要最快速验证核心假设链：(1) CodeQL inter-procedural data-flow 在 Python\\n    repos 上可行（timeout < 30%），(2) data-flow hard negatives 比 random negatives 提升检索\\n    recall。两个 phase 串行，总计约 1 天。通过后立即进入全量数据提取和训练。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-12 10:01 UTC\\n  summary: '采纳 Reviewer 反馈: MVP Phase 2 增加线性分类器 proxy 验证 + 3-seed 训练 + 显式 kill criteria'\\n  rationale: 'Reviewer 指出 Phase 2 原方案（500 instances, ~100 held-out, 2pp gate）统计效力不足，2pp\\n    差异在随机噪声范围内。增加: (1) Phase 2a 线性分类器 proxy 验证解耦特征质量与训练策略；(2) 3-seed 训练要求 ≥2/3 seed\\n    提升；(3) 每个 phase 的 fail→kill/fallback 路径。防止 13 天 DDL 下的沉没成本陷阱。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-12 10:02 UTC\\n  summary: 'H2 验证并入 Phase 1: 提取后立即统计 data-flow 连通文件 vs 不连通文件的 gold patch 覆盖率差异'\\n  rationale: Reviewer 指出 H2（特征区分度）在原 MVP 中无独立验证，Phase 2 失败时无法区分是 H2 还是 H3 问题。零成本 sanity\\n    check（统计连通/不连通文件的 gold patch 覆盖率）可在 Phase 1 提取完后立即执行，不需要训练。这比 Phase 2a 的线性分类器更早给出诊断信号。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-12 11:21 UTC\\n  summary: 'Phase 1 gate PASS: timeout 0%, H2 Fisher p=1.54e-7, 75% instance recall.\\n    进入 Phase 2。'\\n  rationale: 10 repos 中 8 个成功提取（2 个 skip 因 buggy file 路径不存在，非 CodeQL 限制）。timeout rate\\n    0% 远低于 30% 阈值。H2 sanity check：连通文件 gold 覆盖 1.44% vs 不连通 0.00%，Fisher p=1.54e-7。75%\\n    instance recall（6/8 gold file 在连通集）。数据质量问题（路径匹配、skip rate、registry 注册）并行修复，不阻塞\\n    Phase 2。\\n  related_experiments: []\\n  depends_on: []\\n- id: D005\\n  date: 2026-05-12 11:35 UTC\\n  summary: 'CRITICAL: GPU 越界 PID 59170 跑在 GPU 5 而非分配的 cuda:4，立即 kill + 全脚本修复 CUDA_VISIBLE_DEVICES'\\n  ratio
…[truncated 10905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T05:09:54.780186+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T05:09:54.780342+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 296\\ndrwxr-xr-x  3 root root  4096 May 15 10:03 .\\ndrwxr-xr-x 11 root root  4096 May 15 03:34 ..\\ndrwxr-xr-x  2 root root   101 May 14 08:47 __pycache__\\n-rw-r--r--  1 root root  5446 May 15 01:06 analyze_bm25_overlap_stratified.py\\n-rw-r--r--  1 root root 21027 May 15 04:36 analyze_confound.py\\n-rwxr-xr-x  1 root root  3453 May 13 19:47 build_full_m2_data.sh\\n-rw-r--r--  1 root root 21053 May 14 00:39 build_m1_training_data.py\\n-rw-r--r--  1 root root 17398 May 13 12:18 build_m1_training_data.py.bak\\n-rw-r--r--  1 root root  8304 May 14 07:58 build_p2b_data.py\\n-rwxr-xr-x  1 root root  1708 May 13 19:45 clone_repos.sh\\n-rw-r--r--  1 root root  2607 May 12 20:35 collect_p2b_results.py\\n-rw-r--r--  1 root root  5829 May 14 07:58 compute_full_z_percent.py\\n-rw-r--r--  1 root root  2540 May 13 04:02 download_metadata.py\\n-rw-r--r--  1 root root  4049 May 14 07:58 eval_p2b.py\\n-rw-r--r--  1 root root  5689 May 14 07:58 eval_p2b_pooled.py\\n-rw-r--r--  1 root root 20137 May 15 03:38 eval_swebench_e2e.py\\n-rw-r--r--  1 root root  2528 May 13 04:05 fix_metadata.py\\n-rw-r--r--  1 root root  3395 May 13 04:07 fix_metadata_arrow.py\\n-rw-r--r--  1 root root 19067 May 15 09:19 m2_statistical_analysis.py\\n-rwxr-xr-x  1 root root  1884 May 13 18:53 migrate_m1_data.sh\\n-rw-r--r--  1 root root 10467 May 15 01:07 mine_bm25_negatives.py\\n-rw-r--r--  1 root root  7014 May 15 01:07 plot_neg_difficulty.py\\n-rw-r--r--  1 root root 16107 May 15 10:03 plot_per_seed_delta.py\\n-rw-r--r--  1 root root  3906 May 14 03:32 prepare_m1_rerun.py\\n-rwxr-xr-x  1 root root  4134 May 14 03:36 rerun_m1_failed.sh\\n-rw-r--r--  1 root root 11199 May 14 07:58 run_50repo_overlap.py\\n-rw-r--r--  1 root root  1405 May 14 07:58 run_eval_5missing.sh\\n-rwxr-xr-x  1 root root  5205 May 14 07:58 run_eval_all.sh\\n-rwxr-xr-x  1 root root  3816 May 14 07:58 run_eval_p50.sh\\n-rwxr-xr-x  1 root root  5039 May 13 19:48 run_full_m2_
…[truncated 515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T05:09:54.780525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"analyze_stratified*\" -o -name \"evaluate_pool50*\" -o -name \"*stratified*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"analyze_stratified*\" -o -name \"evaluate_pool50*\" -o -name \"*stratified*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T05:09:54.780690+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T05:09:54.780821+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -1 /root/autodl-tmp/structfuse/data/all.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -1 /root/autodl-tmp/structfuse/data/all.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T05:09:54.780944+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"head: cannot open '/root/autodl-tmp/structfuse/data/all.jsonl' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T05:09:54.781059+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T05:09:54.781263+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/memory.md\", \"content\": \"# Inference-Time Graph Methods 文献对比\\n\\n## 对比表\\n\\n| Method | Paper | Venue | Graph Type | Usage Stage | Inter-proc Data-Flow | Task | Scalability | Key Diff from StructFuse |\\n|--------|-------|-------|-----------|-------------|---------------------|------|-------------|--------------------------|\\n| **CodexGraph** | Bridging LLMs and Code Repositories via Code Graph Databases | NAACL 2025 (arXiv:2408.03910) | Code graph DB (MODULE/CLASS/FUNCTION nodes; CONTAINS/INHERITS/USES edges) | Inference-time | No. Static analysis for symbol relations only | General repo-level coding (completion, issue resolution) | CrossCodeEval, SWE-bench, EvoCodeBench | Agent queries graph DB at inference; task-agnostic schema but no data-flow semantics |\\n| **LocAgent** | Graph-Guided LLM Agents for Code Localization | ACL 2025 (arXiv:2503.09089) | Directed heterogeneous graph (code entities + dependency edges) | Inference-time | No. Dependency edges, not data-flow | Fault localization | 92.7% file-level accuracy; SWE-bench +12% Pass@10 | Agent multi-hop graph reasoning at inference; needs fine-tuned 32B model |\\n| **RANGER** | RANGER — Repository-Level Agent for Graph-Enhanced Retrieval | arXiv:2509.25257 (Sep 2025) | Knowledge graph + MCTS traversal | Inference-time | No | Code search, QA, cross-file retrieval, completion | CodeSearchNet, RepoQA, RepoBench, CrossCodeEval | MCTS-guided graph exploration; dual-stage (Cypher + MCTS); higher inference cost due to cross-encoder scoring |\\n| **RepoGraph** | Enhancing AI SE with Repository-level Code Graph | ICLR 2025 (arXiv:2410.14684) | Repo-level code graph (class hierarchy, call graph, file structure) | Inference-time | No. Structural relations only | Software engineering / issue resolution | SWE-bench (+32.8% relative); CrossCodeEval | Plug-in module for existing agents; repo
…[truncated 10547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T05:09:54.781443+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse /root/autodl-tmp -name \"all.jsonl\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse /root/autodl-tmp -name \"all.jsonl\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T05:09:54.781572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T05:09:54.781718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T05:09:54.781843+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/structfuse/data/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T05:09:54.781958+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/experiment_plan*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T05:09:54.782070+00:00_

experiment_plan.lock
experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T05:09:54.782179+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root -name \"all.jsonl\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root -name \"all.jsonl\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T05:09:54.782291+00:00_

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
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
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

_source line 23 · 2026-05-15T05:09:54.782406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T05:09:54.782518+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T05:09:54.782667+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -1 /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -1 /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T05:09:54.783036+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"instance_id\\\": \\\"seatgeek__thefuzz.8a05a3ee.combine_file__18e0miwg\\\", \\\"repo\\\": \\\"swesmith/seatgeek__thefuzz.8a05a3ee\\\", \\\"github_repo\\\": \\\"seatgeek/thefuzz\\\", \\\"base_commit\\\": \\\"8a05a3ee\\\", \\\"buggy_file\\\": \\\"thefuzz/fuzz.py\\\", \\\"buggy_function\\\": \\\"_rapidfuzz_scorer\\\", \\\"gold_patch_files\\\": [\\\"thefuzz/fuzz.py\\\"], \\\"call_graph\\\": [{\\\"target_func\\\": \\\"ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 35, \\\"end_line\\\": 35}, {\\\"target_func\\\": \\\"partial_ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 39, \\\"end_line\\\": 39}, {\\\"target_func\\\": \\\"token_sort_ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 55, \\\"end_line\\\": 55}, {\\\"target_func\\\": \\\"token_set_ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 73, \\\"end_line\\\": 73}, {\\\"target_func\\\": \\\"partial_token_sort_ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 63, \\\"end_line\\\": 63}, {\\\"target_func\\\": \\\"partial_token_set_ratio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 77, \\\"end_line\\\": 77}, {\\\"target_func\\\": \\\"QRatio\\\", \\\"hop_distance\\\": 1, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 88, \\\"end_line\\\": 88}, {\\\"target_func\\\": \\\"UQRatio\\\", \\\"hop_distance\\\": 2, \\\"direction\\\": \\\"caller\\\", \\\"file_path\\\": \\\"thefuzz/fuzz.py\\\", \\\"start_line\\\": 10
…[truncated 8988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T05:09:54.783199+00:00_

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
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T05:09:54.783380+00:00_

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
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T05:09:54.783572+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/analyze_bm25_overlap_stratified.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/analyze_bm25_overlap_stratified.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T05:09:54.783796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Stratified BM25 overlap analysis: compares BM25 top-k negatives against\\n# other mining strategies (random, embedding_distance, dataflow_aware),\\n# stratified by repo size (unique file count).\\n#\\n# Input:  /root/autodl-tmp/structfuse/full_m2_training_data/train_{strategy}_s42.jsonl\\n# Output: /root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\n\\nimport json\\nimport os\\nfrom collections import defaultdict\\n\\nimport numpy as np\\n\\nDATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\nOUT_PATH = \\\"/root/autodl-tmp/structfuse/artifacts/bm25_overlap_stratified.json\\\"\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEED = 42\\nK = 7\\nTIERS = {\\n    \\\"small_lt50\\\": (0, 50),\\n    \\\"medium_50_200\\\": (50, 201),\\n    \\\"large_200plus\\\": (201, float(\\\"inf\\\")),\\n}\\n\\n\\ndef extract_repo(query_id: str) -> str:\\n    iid = query_id.split(\\\"::\\\")[0]\\n    return iid.split(\\\".\\\")[0]\\n\\n\\ndef extract_filepath(full_id: str) -> str:\\n    return full_id.split(\\\"::\\\", 1)[1]\\n\\n\\ndef jaccard(a: set, b: set) -> float:\\n    if not a and not b:\\n        return 1.0\\n    union = a | b\\n    if not union:\\n        return 0.0\\n    return len(a & b) / len(union)\\n\\n\\ndef load_strategy(name: str) -> dict:\\n    path = os.path.join(DATA_DIR, f\\\"train_{name}_s{SEED}.jsonl\\\")\\n    data = {}\\n    with open(path) as f:\\n        for line in f:\\n            d = json.loads(line)\\n            data[d[\\\"query_id\\\"]] = d[\\\"neg_candidates\\\"]\\n    return data\\n\\n\\ndef main():\\n    # 1. Load all strategies\\n    bm25_data = load_strategy(\\\"bm25\\\")\\n    other_data = {s: load_strategy(s) for s in STRATEGIES}\\n\\n    # 2. Build repo file count (union of all file paths across all strategies)\\n    repo_files = defaultdict(set)\\n    for qid, negs in bm25_data.items():\\n        repo = extract_rep
…[truncated 4192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T05:09:54.783954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/m2_statistical_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/m2_statistical_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T05:09:54.784216+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"M2 statistical analysis: compare hard-negative strategies across encoders and seeds.\\n\\nCollects best R@1 from training logs, runs paired t-tests, Wilcoxon,\\nbootstrap CIs, and Cohen's d.  Outputs JSON + Markdown.\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport math\\nimport os\\nimport re\\nimport sys\\nfrom pathlib import Path\\nfrom typing import Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nfrom scipy import stats\\n\\n# ── Configuration ──────────────────────────────────────────────────────\\n\\nENCODERS = [\\\"qwen\\\", \\\"starcoder\\\"]\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSEEDS = [42, 43, 44]\\n\\nCHECKPOINT_BASE = \\\"/root/autodl-tmp/structfuse/checkpoints\\\"\\nOUTPUT_BASE = \\\"/root/autodl-tmp/structfuse/full_m2_outputs\\\"\\n\\n# StarCoder s42 used 3 epochs (others used 2)\\nHETEROGENEITY_NOTES = {\\n    (\\\"starcoder\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"starcoder\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"random\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"embedding_distance\\\", 42): \\\"3 epochs (others: 2)\\\",\\n    (\\\"qwen\\\", \\\"dataflow_aware\\\", 42): \\\"3 epochs (others: 2)\\\",\\n}\\n\\n\\ndef _candidate_dirs(encoder: str, strategy: str, seed: int) -> List[str]:\\n    \\\"\\\"\\\"Return candidate directories to search for a run's output.\\\"\\\"\\\"\\n    enc_short = {\\\"qwen\\\": \\\"qwen\\\", \\\"starcoder\\\": \\\"starcoder\\\"}[encoder]\\n    enc_full = {\\\"qwen\\\": \\\"m2_full_qwen\\\", \\\"starcoder\\\": \\\"m2_full_starcoder\\\"}[encoder]\\n    tag = f\\\"{strategy}_s{seed}\\\"\\n    tag_enc = f\\\"{strategy}_{enc_short}_s{seed}\\\"\\n    return [\\n        f\\\"{OUTP
…[truncated 7463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T05:09:54.784370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/full_m1_data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/full_m1_data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T05:09:54.784583+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Cog-Creators__Red-DiscordBot.33e0eac7.combine_file__041av9lh.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__08222ijt.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__087t8zrv.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__09r9m56h.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__0pgv38lu.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__1saqryqs.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__1tzqbvbn.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__1uip6nek.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__2q6emitb.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__37pg0tud.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__4mst4vlk.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__534o1yuq.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__55bivpbr.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__5nmwjxc8.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__5x7jn623.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__6koxthdy.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__6pbit1uf.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__6qknycp1.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__7xapgtwa.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__7yi8dsns.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__81lxzncn.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__9gfdmym0.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__a31dhzob.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__a8m3r6xb.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__b6sq1hn0.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__clkl76q2.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__cu9qfznh.json\\nCog-Creators__Red-DiscordBot.33e0eac7.combine_file__d97cxah7.json\\nCog-Creators__Red-DiscordBot.33e0eac7.co
…[truncated 6456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T05:09:54.784791+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/full_m2_training_data/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/full_m2_training_data/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T05:09:54.784936+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"dataflow_graph.json\\ntrain_bm25_s42.jsonl\\ntrain_bm25_s43.jsonl\\ntrain_bm25_s44.jsonl\\ntrain_dataflow_aware_s42.jsonl\\ntrain_dataflow_aware_s43.jsonl\\ntrain_dataflow_aware_s44.jsonl\\ntrain_embedding_distance_s42.jsonl\\ntrain_embedding_distance_s43.jsonl\\ntrain_embedding_distance_s44.jsonl\\ntrain_random_s42.jsonl\\ntrain_random_s43.jsonl\\ntrain_random_s44.jsonl\\nval_bm25_s42.jsonl\\nval_bm25_s43.jsonl\\nval_bm25_s44.jsonl\\nval_dataflow_aware_s42.jsonl\\nval_dataflow_aware_s43.jsonl\\nval_dataflow_aware_s44.jsonl\\nval_embedding_distance_s42.jsonl\\nval_embedding_distance_s43.jsonl\\nval_embedding_distance_s44.jsonl\\nval_random_s42.jsonl\\nval_random_s43.jsonl\\nval_random_s44.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T05:09:54.785061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -2 /root/autodl-tmp/structfuse/full_m2_training_data/train_random_s42.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -2 /root/autodl-tmp/structfuse/full_m2_training_data/train_random_s42.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T05:09:54.785360+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"oauthlib__oauthlib.1fd52536.lm_rewrite__e551pdwl::oauthlib/openid/connect/core/grant_types/dispatchers.py\\\", \\\"query_tokens\\\": \\\"import logging\\\\n\\\\nlog = logging.getLogger(__name__)\\\\n\\\\n\\\\nclass Dispatcher:\\\\n    default_grant = None\\\\n    oidc_grant = None\\\\n\\\\n\\\\nclass AuthorizationCodeGrantDispatcher(Dispatcher):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    This is an adapter class that will route simple Authorization Code\\\\n    requests, those that have `response_type=code` and a scope including\\\\n    `openid` to either the `default_grant` or the `oidc_grant` based on\\\\n    the scopes requested.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    def __init__(self, default_grant=None, oidc_grant=None):\\\\n        self.default_grant = default_grant\\\\n        self.oidc_grant = oidc_grant\\\\n\\\\n    def _handler_for_request(self, request):\\\\n        handler = self.default_grant\\\\n\\\\n        if request.scopes and \\\\\\\"openid\\\\\\\" in request.scopes:\\\\n            handler = self.oidc_grant\\\\n\\\\n        log.debug('Selecting handler for request %r.', handler)\\\\n        return handler\\\\n\\\\n    def create_authorization_response(self, request, token_handler):\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"Read scope and route to the designated handler.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        return self._handler_for_request(request).create_authorization_response(request, token_handler)\\\\n\\\\n    def validate_authorization_request(self, request):\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"Read scope and route to the designated handler.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        return self._handler_for_request(request).validate_authorization_request(request)\\\\n\\\\n\\\\nclass ImplicitTokenGrantDispatcher(Dispatcher):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    This is an adapter class that will route simple Authorization\\\\n    requests, those that have `id_token` in `resp
…[truncated 8467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T05:09:54.785519+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/full_m2_outputs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/full_m2_outputs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T05:09:54.785680+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"random_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T05:09:54.785845+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/full_m2_outputs/random_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/full_m2_outputs/random_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T05:09:54.785970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T05:09:54.786087+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T05:09:54.786214+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"m2_full_qwen\\nm2_full_starcoder\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T05:09:54.786331+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T05:09:54.786450+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"embedding_distance_s43\\nrandom_s42\\nrandom_s43\\nrandom_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T05:09:54.786563+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/scripts/eval_p2b_pooled.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/scripts/eval_p2b_pooled.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T05:09:54.786774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nos.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = \\\"4\\\"\\n\\n\\\"\\\"\\\"P2b evaluation with configurable pool_size. Pads negatives from other samples if needed.\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport random\\nimport torch\\nimport torch.nn.functional as F\\nfrom pathlib import Path\\nfrom transformers import AutoTokenizer\\n\\nimport sys\\nsys.path.insert(0, str(Path(__file__).resolve().parent.parent / \\\"training\\\"))\\nfrom contrastive_model import StructFuseEncoder\\n\\n\\ndef load_model(ckpt_dir, model_name, device):\\n    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)\\n    config_path = Path(ckpt_dir) / \\\"training_config.json\\\"\\n    with open(config_path) as f:\\n        cfg = json.load(f)\\n\\n    model = StructFuseEncoder(\\n        model_name=model_name,\\n        proj_dim=cfg.get(\\\"proj_dim\\\", 256),\\n        use_lora=cfg.get(\\\"use_lora\\\", True),\\n        lora_r=cfg.get(\\\"lora_r\\\", 16),\\n        use_fusion_head=cfg.get(\\\"use_fusion_head\\\", False),\\n    )\\n    state_dict = torch.load(Path(ckpt_dir) / \\\"model.pt\\\", map_location=\\\"cpu\\\")\\n    result = model.load_state_dict(state_dict, strict=False)\\n    assert not result.missing_keys, f\\\"Missing keys: {result.missing_keys}\\\"\\n    model = model.to(device).eval()\\n    return model, tokenizer\\n\\n\\ndef encode(model, tokenizer, texts, device, max_len=512, batch_size=16):\\n    all_embs = []\\n    for i in range(0, len(texts), batch_size):\\n        batch_texts = texts[i:i+batch_size]\\n        enc = tokenizer(batch_texts, truncation=True, max_length=max_len,\\n                        padding=True, return_tensors=\\\"pt\\\")\\n        enc = {k: v.to(device) for k, v in enc.items()}\\n        with torch.no_grad():\\n            emb = model.encode(enc[\\\"input_ids\\\"], enc[\\\"attention_mask\\\"])\\n        all_embs.append(emb.cpu())\\n    return torch.cat(all
…[truncated 4451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T05:09:54.786970+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "wc -l /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T05:09:54.787102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2980 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T05:09:54.787222+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "wc -l /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "wc -l /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T05:09:54.787339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/training/contrastive_train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/training/contrastive_train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T05:09:54.787457+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"44173 /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T05:09:54.787584+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/structfuse/training/contrastive_train.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T05:09:54.787726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse/training -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse/training -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T05:09:54.787846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/structfuse/training/train.py\\n/root/structfuse/training/contrastive_model.py\\n/root/structfuse/training/hard_negative_mining.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T05:09:54.787958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "head -3 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "head -3 /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T05:09:54.788216+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"query_id\\\": \\\"pyparsing__pyparsing.533adf47.combine_file__b756s2rd::pyparsing/helpers.py\\\", \\\"query_tokens\\\": \\\"# helpers.py\\\\nimport html.entities\\\\nimport operator\\\\nimport re\\\\nimport sys\\\\nimport typing\\\\n\\\\nfrom . import __diag__\\\\nfrom .core import *\\\\nfrom .util import (\\\\n    _bslash,\\\\n    _flatten,\\\\n    _escape_regex_range_chars,\\\\n    make_compressed_re,\\\\n    replaced_by_pep8,\\\\n)\\\\n\\\\n\\\\n#\\\\n# global helpers\\\\n#\\\\ndef counted_array(\\\\n    expr: ParserElement,\\\\n    int_expr: typing.Optional[ParserElement] = None,\\\\n    *,\\\\n    intExpr: typing.Optional[ParserElement] = None,\\\\n) -> ParserElement:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Helper to define a counted list of expressions.\\\\n\\\\n    This helper defines a pattern of the form::\\\\n\\\\n        integer expr expr expr...\\\\n\\\\n    where the leading integer tells how many expr expressions follow.\\\\n    The matched tokens returns the array of expr tokens as a list - the\\\\n    leading count token is suppressed.\\\\n\\\\n    If ``int_expr`` is specified, it should be a pyparsing expression\\\\n    that produces an integer value.\\\\n\\\\n    Example::\\\\n\\\\n        counted_array(Word(alphas)).parse_string('2 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # in this parser, the leading integer value is given in binary,\\\\n        # '10' indicating that 2 values are in the array\\\\n        binary_constant = Word('01').set_parse_action(lambda t: int(t[0], 2))\\\\n        counted_array(Word(alphas), int_expr=binary_constant).parse_string('10 ab cd ef')  # -> ['ab', 'cd']\\\\n\\\\n        # if other fields must be parsed after the count but before the\\\\n        # list items, give the fields results names and they will\\\\n        # be preserved in the returned ParseResults:\\\\n        count_with_metadata = integer + Word(alphas)(\\\\\\\"type\\\\\\\")\\\\n        typed_arra
…[truncated 7396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T05:09:54.788423+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/training/train.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/training/train.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T05:09:54.788698+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"from __future__ import annotations\\n\\nimport os\\n\\n\\\"\\\"\\\"StructFuse contrastive training entry point.\\n\\nTrains a bi-encoder (Qwen2.5-Coder-3B) with InfoNCE loss, data-flow-weighted\\npositives, and configurable hard-negative mining.  Supports single/multi-GPU\\nvia HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.\\n\\\"\\\"\\\"\\n\\n\\nimport argparse\\nimport sys\\nimport json\\nimport math\\nimport os\\nimport random\\nimport shutil\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List\\n\\nimport numpy as np\\nimport torch\\nfrom torch.utils.data import DataLoader, Dataset\\nfrom transformers import AutoTokenizer, get_cosine_schedule_with_warmup\\n\\nfrom accelerate import Accelerator\\nfrom accelerate.utils import set_seed\\n\\nfrom contrastive_model import StructFuseEncoder\\nfrom hard_negative_mining import build_miner, mine_batch\\n\\n\\n\\ndef _print_flush(*args, **kwargs):\\n    \\\"\\\"\\\"Print with explicit flush for file-redirect compatibility.\\\"\\\"\\\"\\n    kwargs['flush'] = True\\n    print(*args, **kwargs)\\n\\n# ── Dataset ──���───────────────────────────────────────────────────────\\n\\nclass ContrastiveDataset(Dataset):\\n    \\\"\\\"\\\"\\n    Each sample: {query, positive, negatives[], pos_weight, features[]}.\\n\\n    The raw data file is JSONL with fields:\\n        query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance,\\n        neg_candidates (list of file ids), features (dict per candidate).\\n\\n    Negatives are mined dynamically per epoch via `refresh_negatives()`.\\n    \\\"\\\"\\\"\\n\\n    def __init__(\\n        self,\\n        data_path: str,\\n        tokenizer: AutoTokenizer,\\n        max_seq_length: int,\\n        num_negatives: int,\\n        pos_weight_alpha: float,\\n        use_fusion_head: bool,\\n    ):\\n        self.tokenizer = tokenizer\\n        self.max_seq_length = max_seq_length\\n        self.num_neg
…[truncated 7076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T05:09:54.788941+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /root/structfuse/scripts/prepare_stratification_index.py << 'PYEOF'\n\"\"\"Build stratification metadata index from M1 all.jsonl.\n\nReads the full M1 extraction output and computes per-instance and per-repo\nfeatures used for stratified evaluation analysis (plan_005).\n\nOutputs: stratification_index.json with per-instance metadata + repo_stats.\n\nUsage:\n    python prepare_stratification_index.py \\\n        --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n        --output /root/autodl-tmp/structfuse/stratification_index.json\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\n\ndef parse_instance_id_from_query(query_id: str) -> str:\n    return query_id.split(\"::\")[0]\n\n\ndef build_index(m1_path: str) -> dict:\n    repo_files = defaultdict(set)\n    instances = {}\n\n    with open(m1_path) as f:\n        for i, line in enumerate(f):\n            if not line.strip():\n                continue\n            d = json.loads(line)\n            iid = d[\"instance_id\"]\n            repo = d.get(\"repo\", \"\")\n            github_repo = d.get(\"github_repo\", repo)\n            buggy_file = d.get(\"buggy_file\", \"\")\n            gold_files = set(d.get(\"gold_patch_files\", []))\n\n            cg = d.get(\"call_graph\", [])\n            df = d.get(\"dataflow_paths\", [])\n\n            cg_files = set()\n            max_hop = 0\n            for entry in cg:\n                fp = entry.get(\"file_path\", \"\")\n                if fp:\n                    cg_files.add(fp)\n                hop = entry.get(\"hop_distance\", 0)\n                if hop > max_hop:\n                    max_hop = hop\n\n            df_files = set()\n            for entry in df:\n                sf = entry.get(\"source_file\", \"\")\n                kf = entry.get(\"sink_file\", \"\")\n                if sf:\n                    df_files.add(sf)\n                if kf:\n                    df_files.add(kf)\n\n            connected_files = cg_files | df_files\n            connected_not_gold = connected_files - gold_files - {buggy_file}\n            has_z = len(connected_not_gold) > 0\n\n            has_structural = bool(cg or df)\n            extraction_method = d.get(\"extraction_method\", \"none\")\n            inter_proc = d.get(\"inter_procedural\", False)\n\n            all_files = set()\n            all_files.add(buggy_file)\n            all_files.update(gold_files)\n            all_files.update(cg_files)\n            all_files.update(df_files)\n            repo_files[github_repo].update(all_files)\n\n            instances[iid] = {\n                \"repo\": github_repo,\n                \"buggy_file\": buggy_file,\n                \"num_gold_files\": len(gold_files),\n                \"has_structural\": has_structural,\n                \"extraction_method\": extraction_method,\n                \"inter_procedural\": inter_proc,\n                \"num_call_graph_entries\": len(cg),\n                \"num_dataflow_paths\": len(df),\n                \"num_connected_files\": len(connected_files),\n                \"num_connected_not_gold\": len(connected_not_gold),\n                \"has_z\": has_z,\n                \"max_hop_distance\": max_hop,\n            }\n\n            if (i + 1) % 10000 == 0:\n                print(f\"  processed {i+1} instances\", flush=True)\n\n    repo_stats = {}\n    for repo, files in repo_files.items():\n        repo_stats[repo] = {\"file_count\": len(files)}\n\n    for iid, meta in instances.items():\n        repo = meta[\"repo\"]\n        meta[\"repo_file_count\"] = repo_stats.get(repo, {}).get(\"file_count\", 0)\n\n    total = len(instances)\n    structural = sum(1 for m in instances.values() if m[\"has_structural\"])\n    has_z_count = sum(1 for m in instances.values() if m[\"has_z\"])\n\n    summary = {\n        \"total_instances\": total,\n        \"with_structural\": structural,\n        \"with_z\": has_z_count,\n        \"structural_pct\": round(100 * structural / max(total, 1), 1),\n        \"z_pct_conditional\": round(100 * has_z_count / max(structural, 1), 1),\n        \"num_repos\": len(repo_stats),\n    }\n\n    return {\n        \"instances\": instances,\n        \"repo_stats\": repo_stats,\n        \"summary\": summary,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--m1-file\", required=True)\n    parser.add_argument(\"--output\", required=True)\n    args = parser.parse_args()\n\n    print(f\"Building stratification index from {args.m1_file}\", flush=True)\n    index = build_index(args.m1_file)\n\n    Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(index, f, indent=1, ensure_ascii=False)\n\n    s = index[\"summary\"]\n    print(f\"\\nSummary:\", flush=True)\n    print(f\"  Instances: {s['total_instances']}\", flush=True)\n    print(f\"  With structural: {s['with_structural']} ({s['structural_pct']}%)\", flush=True)\n    print(f\"  With Z (connected-not-gold): {s['with_z']} ({s['z_pct_conditional']}% conditional)\", flush=True)\n    print(f\"  Repos: {s['num_repos']}\", flush=True)\n    print(f\"\\nSaved to {args.output}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"prepare_stratification_index.py written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat > /root/structfuse/scripts/prepare_stratification_index.py << 'PYEOF'\n\"\"\"Build stratification metadata index from M1 all.jsonl.\n\nReads the full M1 extraction output and computes per-instance and per-repo\nfeatures used for stratified evaluation analysis (plan_005).\n\nOutputs: stratification_index.json with per-instance metadata + repo_stats.\n\nUsage:\n    python prepare_stratification_index.py \\\n        --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n        --output /root/autodl-tmp/structfuse/stratification_index.json\n\"\"\"\n\nimport argparse\nimport json\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\n\ndef parse_instance_id_from_query(query_id: str) -> str:\n    return query_id.split(\"::\")[0]\n\n\ndef build_index(m1_path: str) -> dict:\n    repo_files = defaultdict(set)\n    instances = {}\n\n    with open(m1_path) as f:\n        for i, line in enumerate(f):\n            if not line.strip():\n                continue\n            d = json.loads(line)\n            iid = d[\"instance_id\"]\n            repo = d.get(\"repo\", \"\")\n            github_repo = d.get(\"github_repo\", repo)\n            buggy_file = d.get(\"buggy_file\", \"\")\n            gold_files = set(d.get(\"gold_patch_files\", []))\n\n            cg = d.get(\"call_graph\", [])\n            df = d.get(\"dataflow_paths\", [])\n\n            cg_files = set()\n            max_hop = 0\n            for entry in cg:\n                fp = entry.get(\"file_path\", \"\")\n                if fp:\n                    cg_files.add(fp)\n                hop = entry.get(\"hop_distance\", 0)\n                if hop > max_hop:\n                    max_hop = hop\n\n            df_files = set()\n            for entry in df:\n                sf = entry.get(\"source_file\", \"\")\n                kf = entry.get(\"sink_file\", \"\")\n                if sf:\n                    df_files.add(sf)\n                if kf:\n                    df_files.add(kf)\n\n            connected_files = cg_files | df_files\n            connected_not_gold = connected_files - gold_files - {buggy_file}\n            has_z = len(connected_not_gold) > 0\n\n            has_structural = bool(cg or df)\n            extraction_method = d.get(\"extraction_method\", \"none\")\n            inter_proc = d.get(\"inter_procedural\", False)\n\n            all_files = set()\n            all_files.add(buggy_file)\n            all_files.update(gold_files)\n            all_files.update(cg_files)\n            all_files.update(df_files)\n            repo_files[github_repo].update(all_files)\n\n            instances[iid] = {\n                \"repo\": github_repo,\n                \"buggy_file\": buggy_file,\n                \"num_gold_files\": len(gold_files),\n                \"has_structural\": has_structural,\n                \"extraction_method\": extraction_method,\n                \"inter_procedural\": inter_proc,\n                \"num_call_graph_entries\": len(cg),\n                \"num_dataflow_paths\": len(df),\n                \"num_connected_files\": len(connected_files),\n                \"num_connected_not_gold\": len(connected_not_gold),\n                \"has_z\": has_z,\n                \"max_hop_distance\": max_hop,\n            }\n\n            if (i + 1) % 10000 == 0:\n                print(f\"  processed {i+1} instances\", flush=True)\n\n    repo_stats = {}\n    for repo, files in repo_files.items():\n        repo_stats[repo] = {\"file_count\": len(files)}\n\n    for iid, meta in instances.items():\n        repo = meta[\"repo\"]\n        meta[\"repo_file_count\"] = repo_stats.get(repo, {}).get(\"file_count\", 0)\n\n    total = len(instances)\n    structural = sum(1 for m in instances.values() if m[\"has_structural\"])\n    has_z_count = sum(1 for m in instances.values() if m[\"has_z\"])\n\n    summary = {\n        \"total_instances\": total,\n        \"with_structural\": structural,\n        \"with_z\": has_z_count,\n        \"structural_pct\": round(100 * structural / max(total, 1), 1),\n        \"z_pct_conditional\": round(100 * has_z_count / max(structural, 1), 1),\n        \"num_repos\": len(repo_stats),\n    }\n\n    return {\n        \"instances\": instances,\n        \"repo_stats\": repo_stats,\n        \"summary\": summary,\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--m1-file\", required=True)\n    parser.add_argument(\"--output\", required=True)\n    args = parser.parse_args()\n\n    print(f\"Building stratification index from {args.m1_file}\", flush=True)\n    index = build_index(args.m1_file)\n\n    Path(args.output).parent.mkdir(parents=True, exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(index, f, indent=1, ensure_ascii=False)\n\n    s = index[\"summary\"]\n    print(f\"\\nSummary:\", flush=True)\n    print(f\"  Instances: {s['total_instances']}\", flush=True)\n    print(f\"  With structural: {s['with_structural']} ({s['structural_pct']}%)\", flush=True)\n    print(f\"  With Z (connected-not-gold): {s['with_z']} ({s['z_pct_conditional']}% conditional)\", flush=True)\n    print(f\"  Repos: {s['num_repos']}\", flush=True)\n    print(f\"\\nSaved to {args.output}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"prepare_stratification_index.py written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T05:09:54.789126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"prepare_stratification_index.py written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T05:09:54.789284+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /root/structfuse/scripts/evaluate_stratified.py << 'PYEOF'\n\"\"\"Per-query evaluation for stratified analysis (plan_005).\n\nEvaluates M2 checkpoints and records per-query results including gold rank,\ncosine similarities, and pool sizes. Supports multiple pool sizes (D038).\n\nOutputs per-query JSONL for downstream analyze_stratified.py.\n\nUsage:\n    # Real eval (GPU):\n    python evaluate_stratified.py \\\n        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42 \\\n        --model-name /root/autodl-tmp/structfuse/models/Qwen2.5-Coder-3B \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --pool-sizes 50 \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag qwen_random_s42\n\n    # Dry-run (no GPU):\n    python evaluate_stratified.py --dry-run \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag dryrun_random_s42\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\n\n\ndef _extract_instance_id(query_id: str) -> str:\n    return query_id.split(\"::\")[0]\n\n\ndef _load_val_data(val_path: str) -> list:\n    samples = []\n    with open(val_path) as f:\n        for line in f:\n            if line.strip():\n                samples.append(json.loads(line))\n    return samples\n\n\ndef _build_global_pool(samples: list) -> dict:\n    pool = {}\n    for s in samples:\n        ct = s.get(\"candidate_tokens\", {})\n        for cid, text in ct.items():\n            if text and cid not in pool:\n                pool[cid] = text\n        pid = s.get(\"pos_id\")\n        pt = s.get(\"pos_tokens\")\n        if pid and pt:\n            pool[pid] = pt\n    return pool\n\n\ndef evaluate_real(samples, global_pool, global_ids, ckpt_dir, model_name,\n                  device, max_seq_len, pool_size, eval_seed):\n    import torch\n    import torch.nn.functional as F\n    from transformers import AutoTokenizer\n\n    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / \"training\"))\n    from contrastive_model import StructFuseEncoder\n\n    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n\n    model = StructFuseEncoder(\n        model_name=model_name,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n    state_dict = torch.load(Path(ckpt_dir) / \"model.pt\", map_location=\"cpu\")\n    result = model.load_state_dict(state_dict, strict=False)\n    assert not result.missing_keys, f\"Missing keys: {result.missing_keys}\"\n    model = model.to(device).eval()\n\n    def encode_batch(texts, batch_size=16):\n        all_embs = []\n        for i in range(0, len(texts), batch_size):\n            bt = texts[i:i+batch_size]\n            enc = tokenizer(bt, truncation=True, max_length=max_seq_len,\n                            padding=True, return_tensors=\"pt\")\n            enc = {k: v.to(device) for k, v in enc.items()}\n            with torch.no_grad():\n                emb = model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            all_embs.append(emb.cpu())\n        return torch.cat(all_embs, dim=0)\n\n    rng = random.Random(eval_seed)\n    results = []\n    target_negs = pool_size - 1\n\n    for idx, s in enumerate(samples):\n        query_id = s.get(\"query_id\", \"\")\n        query_text = s[\"query_tokens\"]\n        pos_text = s[\"pos_tokens\"]\n        pos_id = s.get(\"pos_id\", \"\")\n\n        cand_ids = s.get(\"neg_candidates\", [])\n        cand_tokens = s.get(\"candidate_tokens\", {})\n        neg_texts = [(cid, cand_tokens[cid]) for cid in cand_ids\n                     if cid in cand_tokens and cand_tokens[cid]]\n\n        if len(neg_texts) < target_negs:\n            used = {cid for cid, _ in neg_texts} | {pos_id, query_id}\n            avail = [g for g in global_ids if g not in used]\n            rng.shuffle(avail)\n            for gid in avail:\n                if len(neg_texts) >= target_negs:\n                    break\n                neg_texts.append((gid, global_pool[gid]))\n\n        if len(neg_texts) > target_negs:\n            rng.shuffle(neg_texts)\n            neg_texts = neg_texts[:target_negs]\n\n        if not neg_texts:\n            continue\n\n        pool_texts = [pos_text] + [t for _, t in neg_texts]\n        query_emb = encode_batch([query_text])\n        pool_embs = encode_batch(pool_texts)\n\n        sims = F.cosine_similarity(query_emb, pool_embs, dim=1)\n        ranking = sims.argsort(descending=True)\n        gold_rank = (ranking == 0).nonzero(as_tuple=True)[0].item()\n\n        query_pos_sim = float(sims[0])\n        neg_sims = sims[1:].numpy()\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": gold_rank,\n            \"pool_size\": len(pool_texts),\n            \"query_pos_sim\": round(query_pos_sim, 6),\n            \"mean_neg_sim\": round(float(neg_sims.mean()), 6) if len(neg_sims) > 0 else 0.0,\n            \"max_neg_sim\": round(float(neg_sims.max()), 6) if len(neg_sims) > 0 else 0.0,\n            \"hit_at_1\": gold_rank < 1,\n            \"hit_at_5\": gold_rank < 5,\n            \"hit_at_10\": gold_rank < 10,\n        })\n\n        if (idx + 1) % 200 == 0:\n            r1_so_far = sum(r[\"hit_at_1\"] for r in results) / len(results)\n            print(f\"  [{idx+1}/{len(samples)}] running R@1={r1_so_far:.4f}\", flush=True)\n\n    return results\n\n\ndef evaluate_dryrun(samples, pool_size, eval_seed):\n    rng = np.random.RandomState(eval_seed)\n    results = []\n    for s in samples:\n        query_id = s.get(\"query_id\", \"\")\n        n_negs = min(len(s.get(\"neg_candidates\", [])), pool_size - 1)\n        if n_negs < 1:\n            n_negs = pool_size - 1\n        actual_pool = n_negs + 1\n\n        gold_rank = rng.choice(actual_pool)\n        qp_sim = rng.normal(0.6, 0.15)\n        mn_sim = rng.normal(0.35, 0.1)\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": int(gold_rank),\n            \"pool_size\": actual_pool,\n            \"query_pos_sim\": round(float(np.clip(qp_sim, -1, 1)), 6),\n            \"mean_neg_sim\": round(float(np.clip(mn_sim, -1, 1)), 6),\n            \"max_neg_sim\": round(float(np.clip(mn_sim + 0.15, -1, 1)), 6),\n            \"hit_at_1\": int(gold_rank) < 1,\n            \"hit_at_5\": int(gold_rank) < 5,\n            \"hit_at_10\": int(gold_rank) < 10,\n        })\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--ckpt-dir\", default=None)\n    parser.add_argument(\"--model-name\", default=None)\n    parser.add_argument(\"--val-file\", required=True)\n    parser.add_argument(\"--pool-sizes\", default=\"50\", help=\"Comma-separated pool sizes\")\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--tag\", required=True, help=\"e.g., qwen_random_s42\")\n    parser.add_argument(\"--max-seq-length\", type=int, default=2048)\n    parser.add_argument(\"--device\", default=\"cuda:0\")\n    parser.add_argument(\"--eval-seed\", type=int, default=42)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    pool_sizes = [int(x) for x in args.pool_sizes.split(\",\")]\n    print(f\"Loading val data from {args.val_file}\", flush=True)\n    samples = _load_val_data(args.val_file)\n    print(f\"  {len(samples)} samples loaded\", flush=True)\n\n    if not args.dry_run:\n        global_pool = _build_global_pool(samples)\n        global_ids = list(global_pool.keys())\n        print(f\"  global distractor pool: {len(global_ids)} files\", flush=True)\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    for ps in pool_sizes:\n        print(f\"\\n{'='*50}\", flush=True)\n        print(f\"Evaluating pool_size={ps} tag={args.tag} {'[DRY-RUN]' if args.dry_run else ''}\", flush=True)\n        print(f\"{'='*50}\", flush=True)\n\n        if args.dry_run:\n            results = evaluate_dryrun(samples, ps, args.eval_seed)\n        else:\n            results = evaluate_real(\n                samples, global_pool, global_ids,\n                args.ckpt_dir, args.model_name, args.device,\n                args.max_seq_length, ps, args.eval_seed,\n            )\n\n        total = len(results)\n        r1 = sum(r[\"hit_at_1\"] for r in results) / max(total, 1)\n        r5 = sum(r[\"hit_at_5\"] for r in results) / max(total, 1)\n        r10 = sum(r[\"hit_at_10\"] for r in results) / max(total, 1)\n\n        print(f\"\\nAggregate: R@1={r1:.4f} R@5={r5:.4f} R@10={r10:.4f} (n={total})\", flush=True)\n\n        out_path = out_dir / f\"per_query_{args.tag}_p{ps}.jsonl\"\n        with open(out_path, \"w\") as f:\n            for r in results:\n                f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n        print(f\"Saved: {out_path}\", flush=True)\n\n        summary = {\n            \"tag\": args.tag,\n            \"pool_size\": ps,\n            \"total\": total,\n            \"recall_at_1\": round(r1, 4),\n            \"recall_at_5\": round(r5, 4),\n            \"recall_at_10\": round(r10, 4),\n            \"dry_run\": args.dry_run,\n        }\n        sum_path = out_dir / f\"summary_{args.tag}_p{ps}.json\"\n        with open(sum_path, \"w\") as f:\n            json.dump(summary, f, indent=2)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"evaluate_stratified.py written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat > /root/structfuse/scripts/evaluate_stratified.py << 'PYEOF'\n\"\"\"Per-query evaluation for stratified analysis (plan_005).\n\nEvaluates M2 checkpoints and records per-query results including gold rank,\ncosine similarities, and pool sizes. Supports multiple pool sizes (D038).\n\nOutputs per-query JSONL for downstream analyze_stratified.py.\n\nUsage:\n    # Real eval (GPU):\n    python evaluate_stratified.py \\\n        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42 \\\n        --model-name /root/autodl-tmp/structfuse/models/Qwen2.5-Coder-3B \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --pool-sizes 50 \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag qwen_random_s42\n\n    # Dry-run (no GPU):\n    python evaluate_stratified.py --dry-run \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag dryrun_random_s42\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nfrom pathlib import Path\n\nimport numpy as np\n\n\ndef _extract_instance_id(query_id: str) -> str:\n    return query_id.split(\"::\")[0]\n\n\ndef _load_val_data(val_path: str) -> list:\n    samples = []\n    with open(val_path) as f:\n        for line in f:\n            if line.strip():\n                samples.append(json.loads(line))\n    return samples\n\n\ndef _build_global_pool(samples: list) -> dict:\n    pool = {}\n    for s in samples:\n        ct = s.get(\"candidate_tokens\", {})\n        for cid, text in ct.items():\n            if text and cid not in pool:\n                pool[cid] = text\n        pid = s.get(\"pos_id\")\n        pt = s.get(\"pos_tokens\")\n        if pid and pt:\n            pool[pid] = pt\n    return pool\n\n\ndef evaluate_real(samples, global_pool, global_ids, ckpt_dir, model_name,\n                  device, max_seq_len, pool_size, eval_seed):\n    import torch\n    import torch.nn.functional as F\n    from transformers import AutoTokenizer\n\n    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / \"training\"))\n    from contrastive_model import StructFuseEncoder\n\n    tokenizer = AutoTokenizer.from_pretrained(ckpt_dir, trust_remote_code=True)\n    config_path = Path(ckpt_dir) / \"training_config.json\"\n    with open(config_path) as f:\n        cfg = json.load(f)\n\n    model = StructFuseEncoder(\n        model_name=model_name,\n        proj_dim=cfg.get(\"proj_dim\", 256),\n        use_lora=cfg.get(\"use_lora\", True),\n        lora_r=cfg.get(\"lora_r\", 16),\n        use_fusion_head=cfg.get(\"use_fusion_head\", False),\n    )\n    state_dict = torch.load(Path(ckpt_dir) / \"model.pt\", map_location=\"cpu\")\n    result = model.load_state_dict(state_dict, strict=False)\n    assert not result.missing_keys, f\"Missing keys: {result.missing_keys}\"\n    model = model.to(device).eval()\n\n    def encode_batch(texts, batch_size=16):\n        all_embs = []\n        for i in range(0, len(texts), batch_size):\n            bt = texts[i:i+batch_size]\n            enc = tokenizer(bt, truncation=True, max_length=max_seq_len,\n                            padding=True, return_tensors=\"pt\")\n            enc = {k: v.to(device) for k, v in enc.items()}\n            with torch.no_grad():\n                emb = model.encode(enc[\"input_ids\"], enc[\"attention_mask\"])\n            all_embs.append(emb.cpu())\n        return torch.cat(all_embs, dim=0)\n\n    rng = random.Random(eval_seed)\n    results = []\n    target_negs = pool_size - 1\n\n    for idx, s in enumerate(samples):\n        query_id = s.get(\"query_id\", \"\")\n        query_text = s[\"query_tokens\"]\n        pos_text = s[\"pos_tokens\"]\n        pos_id = s.get(\"pos_id\", \"\")\n\n        cand_ids = s.get(\"neg_candidates\", [])\n        cand_tokens = s.get(\"candidate_tokens\", {})\n        neg_texts = [(cid, cand_tokens[cid]) for cid in cand_ids\n                     if cid in cand_tokens and cand_tokens[cid]]\n\n        if len(neg_texts) < target_negs:\n            used = {cid for cid, _ in neg_texts} | {pos_id, query_id}\n            avail = [g for g in global_ids if g not in used]\n            rng.shuffle(avail)\n            for gid in avail:\n                if len(neg_texts) >= target_negs:\n                    break\n                neg_texts.append((gid, global_pool[gid]))\n\n        if len(neg_texts) > target_negs:\n            rng.shuffle(neg_texts)\n            neg_texts = neg_texts[:target_negs]\n\n        if not neg_texts:\n            continue\n\n        pool_texts = [pos_text] + [t for _, t in neg_texts]\n        query_emb = encode_batch([query_text])\n        pool_embs = encode_batch(pool_texts)\n\n        sims = F.cosine_similarity(query_emb, pool_embs, dim=1)\n        ranking = sims.argsort(descending=True)\n        gold_rank = (ranking == 0).nonzero(as_tuple=True)[0].item()\n\n        query_pos_sim = float(sims[0])\n        neg_sims = sims[1:].numpy()\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": gold_rank,\n            \"pool_size\": len(pool_texts),\n            \"query_pos_sim\": round(query_pos_sim, 6),\n            \"mean_neg_sim\": round(float(neg_sims.mean()), 6) if len(neg_sims) > 0 else 0.0,\n            \"max_neg_sim\": round(float(neg_sims.max()), 6) if len(neg_sims) > 0 else 0.0,\n            \"hit_at_1\": gold_rank < 1,\n            \"hit_at_5\": gold_rank < 5,\n            \"hit_at_10\": gold_rank < 10,\n        })\n\n        if (idx + 1) % 200 == 0:\n            r1_so_far = sum(r[\"hit_at_1\"] for r in results) / len(results)\n            print(f\"  [{idx+1}/{len(samples)}] running R@1={r1_so_far:.4f}\", flush=True)\n\n    return results\n\n\ndef evaluate_dryrun(samples, pool_size, eval_seed):\n    rng = np.random.RandomState(eval_seed)\n    results = []\n    for s in samples:\n        query_id = s.get(\"query_id\", \"\")\n        n_negs = min(len(s.get(\"neg_candidates\", [])), pool_size - 1)\n        if n_negs < 1:\n            n_negs = pool_size - 1\n        actual_pool = n_negs + 1\n\n        gold_rank = rng.choice(actual_pool)\n        qp_sim = rng.normal(0.6, 0.15)\n        mn_sim = rng.normal(0.35, 0.1)\n\n        results.append({\n            \"query_id\": query_id,\n            \"instance_id\": _extract_instance_id(query_id),\n            \"gold_rank\": int(gold_rank),\n            \"pool_size\": actual_pool,\n            \"query_pos_sim\": round(float(np.clip(qp_sim, -1, 1)), 6),\n            \"mean_neg_sim\": round(float(np.clip(mn_sim, -1, 1)), 6),\n            \"max_neg_sim\": round(float(np.clip(mn_sim + 0.15, -1, 1)), 6),\n            \"hit_at_1\": int(gold_rank) < 1,\n            \"hit_at_5\": int(gold_rank) < 5,\n            \"hit_at_10\": int(gold_rank) < 10,\n        })\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--ckpt-dir\", default=None)\n    parser.add_argument(\"--model-name\", default=None)\n    parser.add_argument(\"--val-file\", required=True)\n    parser.add_argument(\"--pool-sizes\", default=\"50\", help=\"Comma-separated pool sizes\")\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--tag\", required=True, help=\"e.g., qwen_random_s42\")\n    parser.add_argument(\"--max-seq-length\", type=int, default=2048)\n    parser.add_argument(\"--device\", default=\"cuda:0\")\n    parser.add_argument(\"--eval-seed\", type=int, default=42)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    args = parser.parse_args()\n\n    pool_sizes = [int(x) for x in args.pool_sizes.split(\",\")]\n    print(f\"Loading val data from {args.val_file}\", flush=True)\n    samples = _load_val_data(args.val_file)\n    print(f\"  {len(samples)} samples loaded\", flush=True)\n\n    if not args.dry_run:\n        global_pool = _build_global_pool(samples)\n        global_ids = list(global_pool.keys())\n        print(f\"  global distractor pool: {len(global_ids)} files\", flush=True)\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    for ps in pool_sizes:\n        print(f\"\\n{'='*50}\", flush=True)\n        print(f\"Evaluating pool_size={ps} tag={args.tag} {'[DRY-RUN]' if args.dry_run else ''}\", flush=True)\n        print(f\"{'='*50}\", flush=True)\n\n        if args.dry_run:\n            results = evaluate_dryrun(samples, ps, args.eval_seed)\n        else:\n            results = evaluate_real(\n                samples, global_pool, global_ids,\n                args.ckpt_dir, args.model_name, args.device,\n                args.max_seq_length, ps, args.eval_seed,\n            )\n\n        total = len(results)\n        r1 = sum(r[\"hit_at_1\"] for r in results) / max(total, 1)\n        r5 = sum(r[\"hit_at_5\"] for r in results) / max(total, 1)\n        r10 = sum(r[\"hit_at_10\"] for r in results) / max(total, 1)\n\n        print(f\"\\nAggregate: R@1={r1:.4f} R@5={r5:.4f} R@10={r10:.4f} (n={total})\", flush=True)\n\n        out_path = out_dir / f\"per_query_{args.tag}_p{ps}.jsonl\"\n        with open(out_path, \"w\") as f:\n            for r in results:\n                f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n        print(f\"Saved: {out_path}\", flush=True)\n\n        summary = {\n            \"tag\": args.tag,\n            \"pool_size\": ps,\n            \"total\": total,\n            \"recall_at_1\": round(r1, 4),\n            \"recall_at_5\": round(r5, 4),\n            \"recall_at_10\": round(r10, 4),\n            \"dry_run\": args.dry_run,\n        }\n        sum_path = out_dir / f\"summary_{args.tag}_p{ps}.json\"\n        with open(sum_path, \"w\") as f:\n            json.dump(summary, f, indent=2)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"evaluate_stratified.py written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T05:09:54.789503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"evaluate_stratified.py written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T05:09:54.789730+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /root/structfuse/scripts/analyze_stratified.py << 'PYEOF'\n\"\"\"Stratified analysis of M2 results (plan_005).\n\nJoins per-query eval results with M1 metadata, groups by 5 stratification\ndimensions, and computes per-stratum R@1 deltas with bootstrap CIs.\n\n5 strata:\n  1. Repo size (small/medium/large)\n  2. Actual eval pool size (quartiles)\n  3. Query-positive similarity (quartiles)\n  4. Structural data availability (has_structural / no_structural)\n  5. Negative difficulty (quartiles of mean_neg_sim)\n\nOutputs: JSON summary, CSV table, PDF plots.\n\nUsage:\n    python analyze_stratified.py \\\n        --results-dir /root/structfuse/results/stratified/per_query \\\n        --index-file /root/autodl-tmp/structfuse/stratification_index.json \\\n        --strategies random,embedding_distance,dataflow_aware \\\n        --encoder qwen --seeds 42,43,44 --pool-size 50 \\\n        --output-dir /root/structfuse/results/stratified\n\n    # Dry-run (uses whatever per_query files exist, or generates mock):\n    python analyze_stratified.py --dry-run \\\n        --output-dir /root/structfuse/results/stratified\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\n\nREPO_SIZE_BINS = {\n    \"small (<50)\": (0, 50),\n    \"medium (50-200)\": (50, 201),\n    \"large (200+)\": (201, float(\"inf\")),\n}\n\n\ndef load_per_query(results_dir, encoder, strategy, seed, pool_size):\n    tag = f\"{encoder}_{strategy}_s{seed}\"\n    path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n    if not path.exists():\n        return None\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    return records\n\n\ndef load_index(index_path):\n    with open(index_path) as f:\n        return json.load(f)\n\n\ndef quartile_bins(values):\n    if not values:\n        return {}\n    arr = np.array(values)\n    q25, q50, q75 = np.percentile(arr, [25, 50, 75])\n    return {\n        \"Q1 (lowest)\": (float(\"-inf\"), q25),\n        \"Q2\": (q25, q50),\n        \"Q3\": (q50, q75),\n        \"Q4 (highest)\": (q75, float(\"inf\")),\n    }\n\n\ndef assign_bin(val, bins):\n    for name, (lo, hi) in bins.items():\n        if lo <= val < hi:\n            return name\n    return list(bins.keys())[-1]\n\n\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\n    rng = np.random.RandomState(seed)\n    arr = np.array(values, dtype=float)\n    n = len(arr)\n    if n < 2:\n        m = float(arr.mean()) if n > 0 else 0.0\n        return {\"mean\": m, \"ci_lower\": m, \"ci_upper\": m, \"n\": n}\n    means = np.array([rng.choice(arr, size=n, replace=True).mean() for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(means, [100 * alpha, 100 * (1 - alpha)])\n    return {\n        \"mean\": round(float(arr.mean()), 6),\n        \"ci_lower\": round(float(lo), 6),\n        \"ci_upper\": round(float(hi), 6),\n        \"n\": n,\n    }\n\n\ndef compute_stratum_metrics(records, strategies, baseline=\"random\"):\n    per_strategy = defaultdict(list)\n    for r in records:\n        per_strategy[r[\"strategy\"]].append(r[\"hit_at_1\"])\n\n    result = {}\n    for s in strategies:\n        vals = per_strategy.get(s, [])\n        result[s] = bootstrap_ci(vals)\n\n    if baseline in result and result[baseline][\"n\"] > 0:\n        base_mean = result[baseline][\"mean\"]\n        for s in strategies:\n            if s != baseline and s in result:\n                result[f\"delta_{s}_vs_{baseline}\"] = round(\n                    result[s][\"mean\"] - base_mean, 6)\n\n    return result\n\n\ndef run_analysis(all_records, index, strategies, baseline=\"random\"):\n    inst_meta = index.get(\"instances\", {})\n\n    for r in all_records:\n        iid = r[\"instance_id\"]\n        meta = inst_meta.get(iid, {})\n        r[\"repo\"] = meta.get(\"repo\", \"unknown\")\n        r[\"repo_file_count\"] = meta.get(\"repo_file_count\", 0)\n        r[\"has_structural\"] = meta.get(\"has_structural\", False)\n        r[\"has_z\"] = meta.get(\"has_z\", False)\n        r[\"extraction_method\"] = meta.get(\"extraction_method\", \"none\")\n\n    # Compute quartile bins from data\n    pool_sizes = [r[\"pool_size\"] for r in all_records]\n    qp_sims = [r[\"query_pos_sim\"] for r in all_records]\n    neg_diffs = [r[\"mean_neg_sim\"] for r in all_records]\n\n    pool_bins = quartile_bins(pool_sizes)\n    sim_bins = quartile_bins(qp_sims)\n    diff_bins = quartile_bins(neg_diffs)\n\n    strata_defs = {\n        \"repo_size\": {\n            \"field\": \"repo_file_count\",\n            \"bins\": REPO_SIZE_BINS,\n            \"type\": \"fixed\",\n        },\n        \"pool_size\": {\n            \"field\": \"pool_size\",\n            \"bins\": pool_bins,\n            \"type\": \"quartile\",\n        },\n        \"query_pos_similarity\": {\n            \"field\": \"query_pos_sim\",\n            \"bins\": sim_bins,\n            \"type\": \"quartile\",\n        },\n        \"structural_availability\": {\n            \"field\": \"has_structural\",\n            \"bins\": {\"with_structural\": True, \"no_structural\": False},\n            \"type\": \"binary\",\n        },\n        \"neg_difficulty\": {\n            \"field\": \"mean_neg_sim\",\n            \"bins\": diff_bins,\n            \"type\": \"quartile\",\n        },\n    }\n\n    results = {}\n    for dim_name, dim_def in strata_defs.items():\n        dim_results = {}\n        field = dim_def[\"field\"]\n        bins = dim_def[\"bins\"]\n        dim_type = dim_def[\"type\"]\n\n        if dim_type == \"binary\":\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, False)\n                for bname, bval in bins.items():\n                    if val == bval:\n                        grouped[bname].append(r)\n                        break\n        else:\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, 0)\n                bname = assign_bin(val, bins)\n                grouped[bname].append(r)\n\n        for bname, brecs in sorted(grouped.items()):\n            metrics = compute_stratum_metrics(brecs, strategies, baseline)\n            metrics[\"count\"] = len(brecs)\n            dim_results[bname] = metrics\n\n        # Weighted aggregate delta\n        total_n = sum(m[\"count\"] for m in dim_results.values())\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in dim_results.items():\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)\n\n        results[dim_name] = {\n            \"bins\": {k: str(v) for k, v in bins.items()},\n            \"strata\": dim_results,\n        }\n\n    return results\n\n\ndef generate_csv(results, output_path):\n    lines = [\"dimension,stratum,count,strategy,r@1_mean,r@1_ci_lower,r@1_ci_upper\"]\n    for dim, data in results.items():\n        for bname, metrics in data[\"strata\"].items():\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                count = metrics[\"count\"]\n                for key, val in metrics.items():\n                    if isinstance(val, dict) and \"mean\" in val:\n                        lines.append(\n                            f\"{dim},{bname},{count},{key},\"\n                            f\"{val['mean']:.4f},{val['ci_lower']:.4f},{val['ci_upper']:.4f}\"\n                        )\n    with open(output_path, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n\n\ndef generate_plots(results, strategies, baseline, output_dir):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        print(\"WARNING: matplotlib not available, skipping plots\", flush=True)\n        return\n\n    for dim, data in results.items():\n        strata = data[\"strata\"]\n        bin_names = [b for b in strata if isinstance(strata[b], dict) and \"count\" in strata[b]]\n        if not bin_names:\n            continue\n\n        fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n\n        # Left: R@1 per strategy per stratum\n        ax = axes[0]\n        x = np.arange(len(bin_names))\n        width = 0.8 / len(strategies)\n        for i, s in enumerate(strategies):\n            means = []\n            errs_lo = []\n            errs_hi = []\n            for b in bin_names:\n                m = strata[b].get(s, {})\n                mean = m.get(\"mean\", 0)\n                ci_lo = m.get(\"ci_lower\", mean)\n                ci_hi = m.get(\"ci_upper\", mean)\n                means.append(mean)\n                errs_lo.append(mean - ci_lo)\n                errs_hi.append(ci_hi - mean)\n            ax.bar(x + i * width, means, width, label=s,\n                   yerr=[errs_lo, errs_hi], capsize=3)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"R@1\")\n        ax.set_title(f\"R@1 by {dim}\")\n        ax.legend(fontsize=7)\n\n        # Right: Delta vs baseline per stratum\n        ax = axes[1]\n        for i, s in enumerate(strategies):\n            if s == baseline:\n                continue\n            deltas = []\n            for b in bin_names:\n                dk = f\"delta_{s}_vs_{baseline}\"\n                deltas.append(strata[b].get(dk, 0) or 0)\n            ax.bar(x + i * width, deltas, width, label=f\"{s} - {baseline}\")\n        ax.axhline(0, color=\"black\", linewidth=0.5)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"Delta R@1\")\n        ax.set_title(f\"Delta vs {baseline} by {dim}\")\n        ax.legend(fontsize=7)\n\n        plt.tight_layout()\n        fig_path = Path(output_dir) / f\"stratified_{dim}.pdf\"\n        plt.savefig(fig_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"  Plot saved: {fig_path}\", flush=True)\n\n\ndef generate_dryrun_data(results_dir, strategies, seeds, pool_size, n_queries=500):\n    rng = np.random.RandomState(2026)\n    Path(results_dir).mkdir(parents=True, exist_ok=True)\n\n    repos = [f\"repo_{i}\" for i in range(20)]\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            if path.exists():\n                continue\n\n            base_r1 = {\"random\": 0.42, \"embedding_distance\": 0.48,\n                       \"dataflow_aware\": 0.51, \"bm25\": 0.45}\n            p_hit = base_r1.get(strategy, 0.45) + rng.normal(0, 0.02)\n\n            with open(path, \"w\") as f:\n                for i in range(n_queries):\n                    repo = rng.choice(repos)\n                    iid = f\"{repo}.{rng.randint(1000, 9999)}.func__{i:04d}\"\n                    hit = rng.random() < p_hit\n                    gold_rank = 0 if hit else rng.randint(1, pool_size)\n                    rec = {\n                        \"query_id\": f\"{iid}::src/file_{i}.py\",\n                        \"instance_id\": iid,\n                        \"gold_rank\": int(gold_rank),\n                        \"pool_size\": pool_size,\n                        \"query_pos_sim\": round(float(rng.normal(0.6, 0.15)), 6),\n                        \"mean_neg_sim\": round(float(rng.normal(0.35, 0.1)), 6),\n                        \"max_neg_sim\": round(float(rng.normal(0.5, 0.1)), 6),\n                        \"hit_at_1\": hit,\n                        \"hit_at_5\": int(gold_rank) < 5,\n                        \"hit_at_10\": int(gold_rank) < 10,\n                    }\n                    f.write(json.dumps(rec) + \"\\n\")\n\n    # Also generate mock index\n    index_path = Path(results_dir).parent / \"mock_stratification_index.json\"\n    if not index_path.exists():\n        instances = {}\n        for strategy in strategies:\n            seed = seeds[0]\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            with open(path) as f2:\n                for line in f2:\n                    r = json.loads(line)\n                    iid = r[\"instance_id\"]\n                    if iid not in instances:\n                        repo = iid.split(\".\")[0]\n                        instances[iid] = {\n                            \"repo\": repo,\n                            \"repo_file_count\": rng.randint(10, 500),\n                            \"has_structural\": bool(rng.random() < 0.34),\n                            \"has_z\": bool(rng.random() < 0.78),\n                            \"extraction_method\": rng.choice([\"codeql\", \"beniget\", \"none\"]),\n                        }\n        mock_index = {\n            \"instances\": instances,\n            \"repo_stats\": {},\n            \"summary\": {\"note\": \"mock data for dry-run\"},\n        }\n        with open(index_path, \"w\") as f2:\n            json.dump(mock_index, f2, indent=1)\n        print(f\"  Mock index written: {index_path}\", flush=True)\n\n    return str(index_path)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--results-dir\", default=None,\n                        help=\"Dir with per_query_*.jsonl files\")\n    parser.add_argument(\"--index-file\", default=None,\n                        help=\"stratification_index.json from prepare_stratification_index.py\")\n    parser.add_argument(\"--strategies\", default=\"random,embedding_distance,dataflow_aware\")\n    parser.add_argument(\"--baseline\", default=\"random\")\n    parser.add_argument(\"--encoder\", default=\"qwen\")\n    parser.add_argument(\"--seeds\", default=\"42,43,44\")\n    parser.add_argument(\"--pool-size\", type=int, default=50)\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--bootstrap-iter\", type=int, default=2000)\n    args = parser.parse_args()\n\n    strategies = args.strategies.split(\",\")\n    seeds = [int(s) for s in args.seeds.split(\",\")]\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    tag_prefix = \"dryrun\" if args.dry_run else args.encoder\n\n    if args.dry_run:\n        results_dir = str(out_dir / \"per_query\")\n        print(\"Generating dry-run mock data...\", flush=True)\n        index_path = generate_dryrun_data(results_dir, strategies, seeds, args.pool_size)\n    else:\n        results_dir = args.results_dir\n        index_path = args.index_file\n\n    if not results_dir or not index_path:\n        print(\"ERROR: --results-dir and --index-file required in real mode\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Loading index from {index_path}\", flush=True)\n    index = load_index(index_path)\n    inst_count = len(index.get(\"instances\", {}))\n    print(f\"  {inst_count} instances in index\", flush=True)\n\n    # Load all per-query results\n    all_records = []\n    loaded = 0\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"{tag_prefix}_{strategy}_s{seed}\"\n            recs = load_per_query(results_dir, tag_prefix, strategy, seed, args.pool_size)\n            if recs is None:\n                print(f\"  WARN: missing {tag} pool={args.pool_size}\", flush=True)\n                continue\n            for r in recs:\n                r[\"strategy\"] = strategy\n                r[\"seed\"] = seed\n            all_records.extend(recs)\n            loaded += 1\n            print(f\"  Loaded {tag}: {len(recs)} queries\", flush=True)\n\n    print(f\"\\nTotal: {len(all_records)} records from {loaded} runs\", flush=True)\n\n    if not all_records:\n        print(\"ERROR: no data loaded\", file=sys.stderr)\n        sys.exit(1)\n\n    # Run analysis\n    print(\"\\nRunning stratified analysis...\", flush=True)\n    results = run_analysis(all_records, index, strategies, args.baseline)\n\n    # Print summary\n    for dim, data in results.items():\n        print(f\"\\n{'='*60}\", flush=True)\n        print(f\"Dimension: {dim}\", flush=True)\n        print(f\"{'='*60}\", flush=True)\n        strata = data[\"strata\"]\n        for bname, metrics in sorted(strata.items()):\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                parts = [f\"  {bname} (n={metrics['count']})\"]\n                for s in strategies:\n                    m = metrics.get(s, {})\n                    if isinstance(m, dict) and \"mean\" in m:\n                        parts.append(f\"  {s}: {m['mean']:.4f} [{m['ci_lower']:.4f}, {m['ci_upper']:.4f}]\")\n                for s in strategies:\n                    if s != args.baseline:\n                        dk = f\"delta_{s}_vs_{args.baseline}\"\n                        d = metrics.get(dk)\n                        if d is not None:\n                            parts.append(f\"  {dk}: {d:+.4f}\")\n                print(\"\\n\".join(parts), flush=True)\n            elif isinstance(metrics, (int, float)):\n                print(f\"  {bname}: {metrics}\", flush=True)\n\n    # Save outputs\n    suffix = \"_dryrun\" if args.dry_run else \"\"\n\n    json_path = out_dir / f\"stratified_results{suffix}.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved: {json_path}\", flush=True)\n\n    csv_path = out_dir / f\"stratified_results{suffix}.csv\"\n    generate_csv(results, csv_path)\n    print(f\"CSV saved: {csv_path}\", flush=True)\n\n    generate_plots(results, strategies, args.baseline, out_dir)\n\n    print(\"\\nDone.\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"analyze_stratified.py written OK\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat > /root/structfuse/scripts/analyze_stratified.py << 'PYEOF'\n\"\"\"Stratified analysis of M2 results (plan_005).\n\nJoins per-query eval results with M1 metadata, groups by 5 stratification\ndimensions, and computes per-stratum R@1 deltas with bootstrap CIs.\n\n5 strata:\n  1. Repo size (small/medium/large)\n  2. Actual eval pool size (quartiles)\n  3. Query-positive similarity (quartiles)\n  4. Structural data availability (has_structural / no_structural)\n  5. Negative difficulty (quartiles of mean_neg_sim)\n\nOutputs: JSON summary, CSV table, PDF plots.\n\nUsage:\n    python analyze_stratified.py \\\n        --results-dir /root/structfuse/results/stratified/per_query \\\n        --index-file /root/autodl-tmp/structfuse/stratification_index.json \\\n        --strategies random,embedding_distance,dataflow_aware \\\n        --encoder qwen --seeds 42,43,44 --pool-size 50 \\\n        --output-dir /root/structfuse/results/stratified\n\n    # Dry-run (uses whatever per_query files exist, or generates mock):\n    python analyze_stratified.py --dry-run \\\n        --output-dir /root/structfuse/results/stratified\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\n\nREPO_SIZE_BINS = {\n    \"small (<50)\": (0, 50),\n    \"medium (50-200)\": (50, 201),\n    \"large (200+)\": (201, float(\"inf\")),\n}\n\n\ndef load_per_query(results_dir, encoder, strategy, seed, pool_size):\n    tag = f\"{encoder}_{strategy}_s{seed}\"\n    path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n    if not path.exists():\n        return None\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    return records\n\n\ndef load_index(index_path):\n    with open(index_path) as f:\n        return json.load(f)\n\n\ndef quartile_bins(values):\n    if not values:\n        return {}\n    arr = np.array(values)\n    q25, q50, q75 = np.percentile(arr, [25, 50, 75])\n    return {\n        \"Q1 (lowest)\": (float(\"-inf\"), q25),\n        \"Q2\": (q25, q50),\n        \"Q3\": (q50, q75),\n        \"Q4 (highest)\": (q75, float(\"inf\")),\n    }\n\n\ndef assign_bin(val, bins):\n    for name, (lo, hi) in bins.items():\n        if lo <= val < hi:\n            return name\n    return list(bins.keys())[-1]\n\n\ndef bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):\n    rng = np.random.RandomState(seed)\n    arr = np.array(values, dtype=float)\n    n = len(arr)\n    if n < 2:\n        m = float(arr.mean()) if n > 0 else 0.0\n        return {\"mean\": m, \"ci_lower\": m, \"ci_upper\": m, \"n\": n}\n    means = np.array([rng.choice(arr, size=n, replace=True).mean() for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    lo, hi = np.percentile(means, [100 * alpha, 100 * (1 - alpha)])\n    return {\n        \"mean\": round(float(arr.mean()), 6),\n        \"ci_lower\": round(float(lo), 6),\n        \"ci_upper\": round(float(hi), 6),\n        \"n\": n,\n    }\n\n\ndef compute_stratum_metrics(records, strategies, baseline=\"random\"):\n    per_strategy = defaultdict(list)\n    for r in records:\n        per_strategy[r[\"strategy\"]].append(r[\"hit_at_1\"])\n\n    result = {}\n    for s in strategies:\n        vals = per_strategy.get(s, [])\n        result[s] = bootstrap_ci(vals)\n\n    if baseline in result and result[baseline][\"n\"] > 0:\n        base_mean = result[baseline][\"mean\"]\n        for s in strategies:\n            if s != baseline and s in result:\n                result[f\"delta_{s}_vs_{baseline}\"] = round(\n                    result[s][\"mean\"] - base_mean, 6)\n\n    return result\n\n\ndef run_analysis(all_records, index, strategies, baseline=\"random\"):\n    inst_meta = index.get(\"instances\", {})\n\n    for r in all_records:\n        iid = r[\"instance_id\"]\n        meta = inst_meta.get(iid, {})\n        r[\"repo\"] = meta.get(\"repo\", \"unknown\")\n        r[\"repo_file_count\"] = meta.get(\"repo_file_count\", 0)\n        r[\"has_structural\"] = meta.get(\"has_structural\", False)\n        r[\"has_z\"] = meta.get(\"has_z\", False)\n        r[\"extraction_method\"] = meta.get(\"extraction_method\", \"none\")\n\n    # Compute quartile bins from data\n    pool_sizes = [r[\"pool_size\"] for r in all_records]\n    qp_sims = [r[\"query_pos_sim\"] for r in all_records]\n    neg_diffs = [r[\"mean_neg_sim\"] for r in all_records]\n\n    pool_bins = quartile_bins(pool_sizes)\n    sim_bins = quartile_bins(qp_sims)\n    diff_bins = quartile_bins(neg_diffs)\n\n    strata_defs = {\n        \"repo_size\": {\n            \"field\": \"repo_file_count\",\n            \"bins\": REPO_SIZE_BINS,\n            \"type\": \"fixed\",\n        },\n        \"pool_size\": {\n            \"field\": \"pool_size\",\n            \"bins\": pool_bins,\n            \"type\": \"quartile\",\n        },\n        \"query_pos_similarity\": {\n            \"field\": \"query_pos_sim\",\n            \"bins\": sim_bins,\n            \"type\": \"quartile\",\n        },\n        \"structural_availability\": {\n            \"field\": \"has_structural\",\n            \"bins\": {\"with_structural\": True, \"no_structural\": False},\n            \"type\": \"binary\",\n        },\n        \"neg_difficulty\": {\n            \"field\": \"mean_neg_sim\",\n            \"bins\": diff_bins,\n            \"type\": \"quartile\",\n        },\n    }\n\n    results = {}\n    for dim_name, dim_def in strata_defs.items():\n        dim_results = {}\n        field = dim_def[\"field\"]\n        bins = dim_def[\"bins\"]\n        dim_type = dim_def[\"type\"]\n\n        if dim_type == \"binary\":\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, False)\n                for bname, bval in bins.items():\n                    if val == bval:\n                        grouped[bname].append(r)\n                        break\n        else:\n            grouped = defaultdict(list)\n            for r in all_records:\n                val = r.get(field, 0)\n                bname = assign_bin(val, bins)\n                grouped[bname].append(r)\n\n        for bname, brecs in sorted(grouped.items()):\n            metrics = compute_stratum_metrics(brecs, strategies, baseline)\n            metrics[\"count\"] = len(brecs)\n            dim_results[bname] = metrics\n\n        # Weighted aggregate delta\n        total_n = sum(m[\"count\"] for m in dim_results.values())\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in dim_results.items():\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)\n\n        results[dim_name] = {\n            \"bins\": {k: str(v) for k, v in bins.items()},\n            \"strata\": dim_results,\n        }\n\n    return results\n\n\ndef generate_csv(results, output_path):\n    lines = [\"dimension,stratum,count,strategy,r@1_mean,r@1_ci_lower,r@1_ci_upper\"]\n    for dim, data in results.items():\n        for bname, metrics in data[\"strata\"].items():\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                count = metrics[\"count\"]\n                for key, val in metrics.items():\n                    if isinstance(val, dict) and \"mean\" in val:\n                        lines.append(\n                            f\"{dim},{bname},{count},{key},\"\n                            f\"{val['mean']:.4f},{val['ci_lower']:.4f},{val['ci_upper']:.4f}\"\n                        )\n    with open(output_path, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n\n\ndef generate_plots(results, strategies, baseline, output_dir):\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n    except ImportError:\n        print(\"WARNING: matplotlib not available, skipping plots\", flush=True)\n        return\n\n    for dim, data in results.items():\n        strata = data[\"strata\"]\n        bin_names = [b for b in strata if isinstance(strata[b], dict) and \"count\" in strata[b]]\n        if not bin_names:\n            continue\n\n        fig, axes = plt.subplots(1, 2, figsize=(14, 5))\n\n        # Left: R@1 per strategy per stratum\n        ax = axes[0]\n        x = np.arange(len(bin_names))\n        width = 0.8 / len(strategies)\n        for i, s in enumerate(strategies):\n            means = []\n            errs_lo = []\n            errs_hi = []\n            for b in bin_names:\n                m = strata[b].get(s, {})\n                mean = m.get(\"mean\", 0)\n                ci_lo = m.get(\"ci_lower\", mean)\n                ci_hi = m.get(\"ci_upper\", mean)\n                means.append(mean)\n                errs_lo.append(mean - ci_lo)\n                errs_hi.append(ci_hi - mean)\n            ax.bar(x + i * width, means, width, label=s,\n                   yerr=[errs_lo, errs_hi], capsize=3)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"R@1\")\n        ax.set_title(f\"R@1 by {dim}\")\n        ax.legend(fontsize=7)\n\n        # Right: Delta vs baseline per stratum\n        ax = axes[1]\n        for i, s in enumerate(strategies):\n            if s == baseline:\n                continue\n            deltas = []\n            for b in bin_names:\n                dk = f\"delta_{s}_vs_{baseline}\"\n                deltas.append(strata[b].get(dk, 0) or 0)\n            ax.bar(x + i * width, deltas, width, label=f\"{s} - {baseline}\")\n        ax.axhline(0, color=\"black\", linewidth=0.5)\n        ax.set_xticks(x + width * (len(strategies) - 1) / 2)\n        ax.set_xticklabels(bin_names, rotation=30, ha=\"right\", fontsize=8)\n        ax.set_ylabel(\"Delta R@1\")\n        ax.set_title(f\"Delta vs {baseline} by {dim}\")\n        ax.legend(fontsize=7)\n\n        plt.tight_layout()\n        fig_path = Path(output_dir) / f\"stratified_{dim}.pdf\"\n        plt.savefig(fig_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"  Plot saved: {fig_path}\", flush=True)\n\n\ndef generate_dryrun_data(results_dir, strategies, seeds, pool_size, n_queries=500):\n    rng = np.random.RandomState(2026)\n    Path(results_dir).mkdir(parents=True, exist_ok=True)\n\n    repos = [f\"repo_{i}\" for i in range(20)]\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            if path.exists():\n                continue\n\n            base_r1 = {\"random\": 0.42, \"embedding_distance\": 0.48,\n                       \"dataflow_aware\": 0.51, \"bm25\": 0.45}\n            p_hit = base_r1.get(strategy, 0.45) + rng.normal(0, 0.02)\n\n            with open(path, \"w\") as f:\n                for i in range(n_queries):\n                    repo = rng.choice(repos)\n                    iid = f\"{repo}.{rng.randint(1000, 9999)}.func__{i:04d}\"\n                    hit = rng.random() < p_hit\n                    gold_rank = 0 if hit else rng.randint(1, pool_size)\n                    rec = {\n                        \"query_id\": f\"{iid}::src/file_{i}.py\",\n                        \"instance_id\": iid,\n                        \"gold_rank\": int(gold_rank),\n                        \"pool_size\": pool_size,\n                        \"query_pos_sim\": round(float(rng.normal(0.6, 0.15)), 6),\n                        \"mean_neg_sim\": round(float(rng.normal(0.35, 0.1)), 6),\n                        \"max_neg_sim\": round(float(rng.normal(0.5, 0.1)), 6),\n                        \"hit_at_1\": hit,\n                        \"hit_at_5\": int(gold_rank) < 5,\n                        \"hit_at_10\": int(gold_rank) < 10,\n                    }\n                    f.write(json.dumps(rec) + \"\\n\")\n\n    # Also generate mock index\n    index_path = Path(results_dir).parent / \"mock_stratification_index.json\"\n    if not index_path.exists():\n        instances = {}\n        for strategy in strategies:\n            seed = seeds[0]\n            tag = f\"dryrun_{strategy}_s{seed}\"\n            path = Path(results_dir) / f\"per_query_{tag}_p{pool_size}.jsonl\"\n            with open(path) as f2:\n                for line in f2:\n                    r = json.loads(line)\n                    iid = r[\"instance_id\"]\n                    if iid not in instances:\n                        repo = iid.split(\".\")[0]\n                        instances[iid] = {\n                            \"repo\": repo,\n                            \"repo_file_count\": rng.randint(10, 500),\n                            \"has_structural\": bool(rng.random() < 0.34),\n                            \"has_z\": bool(rng.random() < 0.78),\n                            \"extraction_method\": rng.choice([\"codeql\", \"beniget\", \"none\"]),\n                        }\n        mock_index = {\n            \"instances\": instances,\n            \"repo_stats\": {},\n            \"summary\": {\"note\": \"mock data for dry-run\"},\n        }\n        with open(index_path, \"w\") as f2:\n            json.dump(mock_index, f2, indent=1)\n        print(f\"  Mock index written: {index_path}\", flush=True)\n\n    return str(index_path)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--results-dir\", default=None,\n                        help=\"Dir with per_query_*.jsonl files\")\n    parser.add_argument(\"--index-file\", default=None,\n                        help=\"stratification_index.json from prepare_stratification_index.py\")\n    parser.add_argument(\"--strategies\", default=\"random,embedding_distance,dataflow_aware\")\n    parser.add_argument(\"--baseline\", default=\"random\")\n    parser.add_argument(\"--encoder\", default=\"qwen\")\n    parser.add_argument(\"--seeds\", default=\"42,43,44\")\n    parser.add_argument(\"--pool-size\", type=int, default=50)\n    parser.add_argument(\"--output-dir\", required=True)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--bootstrap-iter\", type=int, default=2000)\n    args = parser.parse_args()\n\n    strategies = args.strategies.split(\",\")\n    seeds = [int(s) for s in args.seeds.split(\",\")]\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n\n    tag_prefix = \"dryrun\" if args.dry_run else args.encoder\n\n    if args.dry_run:\n        results_dir = str(out_dir / \"per_query\")\n        print(\"Generating dry-run mock data...\", flush=True)\n        index_path = generate_dryrun_data(results_dir, strategies, seeds, args.pool_size)\n    else:\n        results_dir = args.results_dir\n        index_path = args.index_file\n\n    if not results_dir or not index_path:\n        print(\"ERROR: --results-dir and --index-file required in real mode\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Loading index from {index_path}\", flush=True)\n    index = load_index(index_path)\n    inst_count = len(index.get(\"instances\", {}))\n    print(f\"  {inst_count} instances in index\", flush=True)\n\n    # Load all per-query results\n    all_records = []\n    loaded = 0\n    for strategy in strategies:\n        for seed in seeds:\n            tag = f\"{tag_prefix}_{strategy}_s{seed}\"\n            recs = load_per_query(results_dir, tag_prefix, strategy, seed, args.pool_size)\n            if recs is None:\n                print(f\"  WARN: missing {tag} pool={args.pool_size}\", flush=True)\n                continue\n            for r in recs:\n                r[\"strategy\"] = strategy\n                r[\"seed\"] = seed\n            all_records.extend(recs)\n            loaded += 1\n            print(f\"  Loaded {tag}: {len(recs)} queries\", flush=True)\n\n    print(f\"\\nTotal: {len(all_records)} records from {loaded} runs\", flush=True)\n\n    if not all_records:\n        print(\"ERROR: no data loaded\", file=sys.stderr)\n        sys.exit(1)\n\n    # Run analysis\n    print(\"\\nRunning stratified analysis...\", flush=True)\n    results = run_analysis(all_records, index, strategies, args.baseline)\n\n    # Print summary\n    for dim, data in results.items():\n        print(f\"\\n{'='*60}\", flush=True)\n        print(f\"Dimension: {dim}\", flush=True)\n        print(f\"{'='*60}\", flush=True)\n        strata = data[\"strata\"]\n        for bname, metrics in sorted(strata.items()):\n            if isinstance(metrics, dict) and \"count\" in metrics:\n                parts = [f\"  {bname} (n={metrics['count']})\"]\n                for s in strategies:\n                    m = metrics.get(s, {})\n                    if isinstance(m, dict) and \"mean\" in m:\n                        parts.append(f\"  {s}: {m['mean']:.4f} [{m['ci_lower']:.4f}, {m['ci_upper']:.4f}]\")\n                for s in strategies:\n                    if s != args.baseline:\n                        dk = f\"delta_{s}_vs_{args.baseline}\"\n                        d = metrics.get(dk)\n                        if d is not None:\n                            parts.append(f\"  {dk}: {d:+.4f}\")\n                print(\"\\n\".join(parts), flush=True)\n            elif isinstance(metrics, (int, float)):\n                print(f\"  {bname}: {metrics}\", flush=True)\n\n    # Save outputs\n    suffix = \"_dryrun\" if args.dry_run else \"\"\n\n    json_path = out_dir / f\"stratified_results{suffix}.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n    print(f\"\\nJSON saved: {json_path}\", flush=True)\n\n    csv_path = out_dir / f\"stratified_results{suffix}.csv\"\n    generate_csv(results, csv_path)\n    print(f\"CSV saved: {csv_path}\", flush=True)\n\n    generate_plots(results, strategies, args.baseline, out_dir)\n\n    print(\"\\nDone.\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"analyze_stratified.py written OK\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T05:09:54.790023+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_stratified.py written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T05:09:54.790175+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T05:09:54.790310+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T05:09:54.790433+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cd /root/structfuse && python3 scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cd /root/structfuse && python3 scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T05:09:54.790559+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/structfuse && python3 scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.87}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T05:09:54.790699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "which python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "which python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T05:09:54.790821+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T05:09:54.790935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/miniconda3/bin/python*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/miniconda3/bin/python*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T05:09:54.791055+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python\\n/root/miniconda3/bin/python3\\n/root/miniconda3/bin/python3-config\\n/root/miniconda3/bin/python3.1\\n/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T05:09:54.791174+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T05:09:54.791300+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json'\\n\\nStdout:\\n\\nBuilding stratification index from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n  processed 10000 instances\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T05:09:54.791445+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && nohup python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json > /tmp/prep_index.log 2>&1 & echo \"PID=$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && nohup python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json > /tmp/prep_index.log 2>&1 & echo \"PID=$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T05:09:54.791570+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && nohup python scripts/prepare_stratification_index.py --m1-file /root/autodl-tmp/structfuse/full_m1_data/all.jsonl --output /root/autodl-tmp/structfuse/stratification_index.json > /tmp/prep_index.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=728590\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T05:09:54.791735+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /tmp/prep_index.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /tmp/prep_index.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T05:09:54.791857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Building stratification index from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n  processed 10000 instances\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T05:09:54.791971+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /tmp/prep_index.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /tmp/prep_index.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T05:09:54.792093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Building stratification index from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n  processed 10000 instances\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T05:09:54.792206+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /tmp/prep_index.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /tmp/prep_index.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T05:09:54.792324+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Building stratification index from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\\n  processed 10000 instances\\n  processed 20000 instances\\n  processed 30000 instances\\n  processed 40000 instances\\n\\nSummary:\\n  Instances: 44173\\n  With structural: 15153 (34.3%)\\n  With Z (connected-not-gold): 11825 (78.0% conditional)\\n  Repos: 123\\n\\nSaved to /root/autodl-tmp/structfuse/stratification_index.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T05:09:54.792455+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/analyze_stratified.py --dry-run --output-dir /root/structfuse/results/stratified 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/analyze_stratified.py --dry-run --output-dir /root/structfuse/results/stratified 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T05:09:54.792615+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"Generating dry-run mock data...\\n  Mock index written: /root/structfuse/results/stratified/mock_stratification_index.json\\nLoading index from /root/structfuse/results/stratified/mock_stratification_index.json\\n  1500 instances in index\\n  Loaded dryrun_random_s42: 500 queries\\n  Loaded dryrun_random_s43: 500 queries\\n  Loaded dryrun_random_s44: 500 queries\\n  Loaded dryrun_embedding_distance_s42: 500 queries\\n  Loaded dryrun_embedding_distance_s43: 500 queries\\n  Loaded dryrun_embedding_distance_s44: 500 queries\\n  Loaded dryrun_dataflow_aware_s42: 500 queries\\n  Loaded dryrun_dataflow_aware_s43: 500 queries\\n  Loaded dryrun_dataflow_aware_s44: 500 queries\\n\\nTotal: 4500 records from 9 runs\\n\\nRunning stratified analysis...\\nTraceback (most recent call last):\\n  File \\\"/root/structfuse-context/scripts/analyze_stratified.py\\\", line 475, in &lt;module>\\n    main()\\n  File \\\"/root/structfuse-context/scripts/analyze_stratified.py\\\", line 432, in main\\n    results = run_analysis(all_records, index, strategies, args.baseline)\\n              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/structfuse-context/scripts/analyze_stratified.py\\\", line 204, in run_analysis\\n    d = m.get(delta_key, 0) or 0\\n        ^^^^^\\nAttributeError: 'float' object has no attribute 'get'\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.02}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T05:09:54.792797+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat > /tmp/fix_analyze.py << 'PYEOF'\nimport re\n\nwith open(\"/root/structfuse/scripts/analyze_stratified.py\") as f:\n    content = f.read()\n\nold = '''        # Weighted aggregate delta\n        total_n = sum(m[\"count\"] for m in dim_results.values())\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in dim_results.items():\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)'''\n\nnew = '''        # Weighted aggregate delta\n        bin_items = [(b, m) for b, m in dim_results.items()\n                     if isinstance(m, dict) and \"count\" in m]\n        total_n = sum(m[\"count\"] for _, m in bin_items)\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in bin_items:\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)'''\n\ncontent = content.replace(old, new)\nwith open(\"/root/structfuse/scripts/analyze_stratified.py\", \"w\") as f:\n    f.write(content)\nprint(\"Fixed\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /tmp/fix_analyze.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat > /tmp/fix_analyze.py << 'PYEOF'\nimport re\n\nwith open(\"/root/structfuse/scripts/analyze_stratified.py\") as f:\n    content = f.read()\n\nold = '''        # Weighted aggregate delta\n        total_n = sum(m[\"count\"] for m in dim_results.values())\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in dim_results.items():\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)'''\n\nnew = '''        # Weighted aggregate delta\n        bin_items = [(b, m) for b, m in dim_results.items()\n                     if isinstance(m, dict) and \"count\" in m]\n        total_n = sum(m[\"count\"] for _, m in bin_items)\n        for s in strategies:\n            if s == baseline:\n                continue\n            delta_key = f\"delta_{s}_vs_{baseline}\"\n            weighted_sum = 0\n            for bname, m in bin_items:\n                d = m.get(delta_key, 0) or 0\n                w = m[\"count\"] / max(total_n, 1)\n                weighted_sum += d * w\n            dim_results[f\"weighted_{delta_key}\"] = round(weighted_sum, 6)'''\n\ncontent = content.replace(old, new)\nwith open(\"/root/structfuse/scripts/analyze_stratified.py\", \"w\") as f:\n    f.write(content)\nprint(\"Fixed\")\nPYEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /tmp/fix_analyze.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T05:09:54.792935+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Fixed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T05:09:54.793052+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/analyze_stratified.py --dry-run --output-dir /root/structfuse/results/stratified 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/analyze_stratified.py --dry-run --output-dir /root/structfuse/results/stratified 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T05:09:54.793219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Generating dry-run mock data...\\nLoading index from /root/structfuse/results/stratified/mock_stratification_index.json\\n  1500 instances in index\\n  Loaded dryrun_random_s42: 500 queries\\n  Loaded dryrun_random_s43: 500 queries\\n  Loaded dryrun_random_s44: 500 queries\\n  Loaded dryrun_embedding_distance_s42: 500 queries\\n  Loaded dryrun_embedding_distance_s43: 500 queries\\n  Loaded dryrun_embedding_distance_s44: 500 queries\\n  Loaded dryrun_dataflow_aware_s42: 500 queries\\n  Loaded dryrun_dataflow_aware_s43: 500 queries\\n  Loaded dryrun_dataflow_aware_s44: 500 queries\\n\\nTotal: 4500 records from 9 runs\\n\\nRunning stratified analysis...\\n\\n============================================================\\nDimension: repo_size\\n============================================================\\n  large (200+) (n=906)\\n  random: 0.3826 [0.3312, 0.4373]\\n  embedding_distance: 0.4463 [0.3909, 0.5016]\\n  dataflow_aware: 0.5556 [0.4999, 0.6111]\\n  delta_embedding_distance_vs_random: +0.0636\\n  delta_dataflow_aware_vs_random: +0.1729\\n  medium (50-200) (n=468)\\n  random: 0.3841 [0.3113, 0.4636]\\n  embedding_distance: 0.4306 [0.3472, 0.5139]\\n  dataflow_aware: 0.5145 [0.4393, 0.5896]\\n  delta_embedding_distance_vs_random: +0.0464\\n  delta_dataflow_aware_vs_random: +0.1303\\n  small (<50) (n=3126)\\n  random: 0.4499 [0.4200, 0.4807]\\n  embedding_distance: 0.4461 [0.4156, 0.4766]\\n  dataflow_aware: 0.4629 [0.4321, 0.4928]\\n  delta_embedding_distance_vs_random: -0.0038\\n  delta_dataflow_aware_vs_random: +0.0130\\n  weighted_delta_dataflow_aware_vs_random: 0.057429\\n  weighted_delta_embedding_distance_vs_random: 0.015024\\n\\n============================================================\\nDimension: pool_size\\n============================================================\\n  Q4 (highest) (n=4500)\\n  random: 0.4293 [0.4047, 0.4540]\\n  embedding_distance: 0.4447 [0.4200, 0.4707]\\n  dataflow_aware: 0
…[truncated 4165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T05:09:54.793384+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-42106",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/evaluate_stratified.py --dry-run --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl --output-dir /root/structfuse/results/stratified/per_query --tag dryrun_test --pool-sizes 50,100 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python scripts/evaluate_stratified.py --dry-run --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl --output-dir /root/structfuse/results/stratified/per_query --tag dryrun_test --pool-sizes 50,100 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T05:09:54.793522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading val data from /root/autodl-tmp/structfuse/full_m2_training_data/val_random_s42.jsonl\\n  2980 samples loaded\\n\\n==================================================\\nEvaluating pool_size=50 tag=dryrun_test [DRY-RUN]\\n==================================================\\n\\nAggregate: R@1=0.0272 R@5=0.1342 R@10=0.2795 (n=2980)\\nSaved: /root/structfuse/results/stratified/per_query/per_query_dryrun_test_p50.jsonl\\n\\n==================================================\\nEvaluating pool_size=100 tag=dryrun_test [DRY-RUN]\\n==================================================\\n\\nAggregate: R@1=0.0279 R@5=0.1349 R@10=0.2708 (n=2980)\\nSaved: /root/structfuse/results/stratified/per_query/per_query_dryrun_test_p100.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T05:09:54.793682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/structfuse/results/stratified/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/structfuse/results/stratified/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T05:09:54.793817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 360\\ndrwxr-xr-x 3 root root   4096 May 15 13:08 .\\ndrwxr-xr-x 3 root root   4096 May 15 13:08 ..\\n-rw-r--r-- 1 root root 243557 May 15 13:08 mock_stratification_index.json\\ndrwxr-xr-x 2 root root   4096 May 15 13:08 per_query\\n-rw-r--r-- 1 root root  17692 May 15 13:08 stratified_neg_difficulty.pdf\\n-rw-r--r-- 1 root root  16103 May 15 13:08 stratified_pool_size.pdf\\n-rw-r--r-- 1 root root  18322 May 15 13:08 stratified_query_pos_similarity.pdf\\n-rw-r--r-- 1 root root  17082 May 15 13:08 stratified_repo_size.pdf\\n-rw-r--r-- 1 root root   2859 May 15 13:08 stratified_results_dryrun.csv\\n-rw-r--r-- 1 root root  10300 May 15 13:08 stratified_results_dryrun.json\\n-rw-r--r-- 1 root root  15284 May 15 13:08 stratified_structural_availability.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-15T05:09:54.793945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "stat /root/autodl-tmp/structfuse/stratification_index.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "stat /root/autodl-tmp/structfuse/stratification_index.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-15T05:09:54.794073+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File: /root/autodl-tmp/structfuse/stratification_index.json\\n  Size: 19817653  \\tBlocks: 38712      IO Block: 4096   regular file\\nDevice: 900h/2304d\\tInode: 13044059001  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-15 13:08:03.013940385 +0800\\nModify: 2026-05-15 13:08:03.373944073 +0800\\nChange: 2026-05-15 13:08:03.373944073 +0800\\n Birth: 2026-05-15 13:08:03.013940385 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-15T05:09:54.794224+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratification_spec.md",
  "content": "# Plan 005: Stratified Analysis Specification\n\n## Pipeline\n\nThree-stage pipeline, stages 1 & 3 are CPU-only:\n\n1. **`prepare_stratification_index.py`** (CPU, DONE) — parses all.jsonl → `stratification_index.json`\n2. **`evaluate_stratified.py`** (GPU, awaiting M2 checkpoints) — per-query eval with pool_size control\n3. **`analyze_stratified.py`** (CPU) — stratification + bootstrap CI + plots\n\n## 5 Stratification Dimensions\n\n| # | Dimension | Bins | Source | Method |\n|---|-----------|------|--------|--------|\n| 1 | Repo size (file count) | small (<50), medium (50-200), large (200+) | `stratification_index.json` → `repo_file_count` | Fixed thresholds (matches BM25 overlap analysis) |\n| 2 | Eval pool size | Quartiles | Per-query eval output → `pool_size` | Data-driven quartiles |\n| 3 | Query-positive similarity | Quartiles | Per-query eval output → `query_pos_sim` | Data-driven quartiles |\n| 4 | Structural data availability | Binary: with_structural / no_structural | `stratification_index.json` → `has_structural` | Binary (34.3% with / 65.7% without) |\n| 5 | Negative difficulty | Quartiles of mean neg cosine sim | Per-query eval output → `mean_neg_sim` | Data-driven quartiles |\n\n## Pool Size Control (D038)\n\n`evaluate_stratified.py` accepts `--pool-sizes 50,100,200,500` to test strategy ranking stability across pool sizes. Each pool size produces a separate per-query JSONL. Analysis is run independently per pool size.\n\nPadding strategy: when a query has fewer candidates than target pool_size, pad with global distractors from other queries in the same val set (same as `eval_p2b_pooled.py`).\n\n## Data Sources\n\n- **M1 metadata**: `/root/autodl-tmp/structfuse/stratification_index.json` (19MB, 44,173 instances, 123 repos)\n- **Val data**: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (2,980 queries each)\n- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/m2_full_{encoder}/{strategy}_s{seed}/`\n\n## Per-query Output Schema\n\n```json\n{\n  \"query_id\": \"instance_id::file_path\",\n  \"instance_id\": \"repo.commit.mutation__hash\",\n  \"gold_rank\": 0,\n  \"pool_size\": 50,\n  \"query_pos_sim\": 0.712345,\n  \"mean_neg_sim\": 0.351234,\n  \"max_neg_sim\": 0.581234,\n  \"hit_at_1\": true,\n  \"hit_at_5\": true,\n  \"hit_at_10\": true\n}\n```\n\n## Analysis Outputs\n\n- `stratified_results.json` — full results with bootstrap 95% CIs per stratum\n- `stratified_results.csv` — flat table for easy import\n- `stratified_{dimension}.pdf` — bar charts: R@1 per strategy (left), delta vs random (right)\n- Weighted aggregate delta per dimension (accounts for stratum sizes)\n\n## Execution Plan\n\nWhen M2 checkpoints are ready:\n\n```bash\n# Stage 2: per-query eval (GPU, ~30min per run × 18 runs)\nfor encoder in qwen starcoder; do\n  for strategy in random embedding_distance dataflow_aware; do\n    for seed in 42 43 44; do\n      python evaluate_stratified.py \\\n        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_${encoder}/${strategy}_s${seed} \\\n        --model-name /root/autodl-tmp/structfuse/models/${model_path} \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl \\\n        --pool-sizes 50 \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag ${encoder}_${strategy}_s${seed}\n    done\n  done\ndone\n\n# Stage 3: analysis (CPU, <1min)\npython analyze_stratified.py \\\n  --results-dir /root/structfuse/results/stratified/per_query \\\n  --index-file /root/autodl-tmp/structfuse/stratification_index.json \\\n  --strategies random,embedding_distance,dataflow_aware \\\n  --encoder qwen --seeds 42,43,44 --pool-size 50 \\\n  --output-dir /root/structfuse/results/stratified\n```\n\n## Verification\n\n- [x] `prepare_stratification_index.py` — completed, 44,173 instances indexed\n- [x] `evaluate_stratified.py --dry-run` — passed (2,980 queries, multi-pool-size)\n- [x] `analyze_stratified.py --dry-run` — passed (5 dimensions, JSON+CSV+5 PDFs)\n- [ ] Real eval — awaiting M2 checkpoints\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratification_spec.md",
    "content": "# Plan 005: Stratified Analysis Specification\n\n## Pipeline\n\nThree-stage pipeline, stages 1 & 3 are CPU-only:\n\n1. **`prepare_stratification_index.py`** (CPU, DONE) — parses all.jsonl → `stratification_index.json`\n2. **`evaluate_stratified.py`** (GPU, awaiting M2 checkpoints) — per-query eval with pool_size control\n3. **`analyze_stratified.py`** (CPU) — stratification + bootstrap CI + plots\n\n## 5 Stratification Dimensions\n\n| # | Dimension | Bins | Source | Method |\n|---|-----------|------|--------|--------|\n| 1 | Repo size (file count) | small (<50), medium (50-200), large (200+) | `stratification_index.json` → `repo_file_count` | Fixed thresholds (matches BM25 overlap analysis) |\n| 2 | Eval pool size | Quartiles | Per-query eval output → `pool_size` | Data-driven quartiles |\n| 3 | Query-positive similarity | Quartiles | Per-query eval output → `query_pos_sim` | Data-driven quartiles |\n| 4 | Structural data availability | Binary: with_structural / no_structural | `stratification_index.json` → `has_structural` | Binary (34.3% with / 65.7% without) |\n| 5 | Negative difficulty | Quartiles of mean neg cosine sim | Per-query eval output → `mean_neg_sim` | Data-driven quartiles |\n\n## Pool Size Control (D038)\n\n`evaluate_stratified.py` accepts `--pool-sizes 50,100,200,500` to test strategy ranking stability across pool sizes. Each pool size produces a separate per-query JSONL. Analysis is run independently per pool size.\n\nPadding strategy: when a query has fewer candidates than target pool_size, pad with global distractors from other queries in the same val set (same as `eval_p2b_pooled.py`).\n\n## Data Sources\n\n- **M1 metadata**: `/root/autodl-tmp/structfuse/stratification_index.json` (19MB, 44,173 instances, 123 repos)\n- **Val data**: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (2,980 queries each)\n- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/m2_full_{encoder}/{strategy}_s{seed}/`\n\n## Per-query Output Schema\n\n```json\n{\n  \"query_id\": \"instance_id::file_path\",\n  \"instance_id\": \"repo.commit.mutation__hash\",\n  \"gold_rank\": 0,\n  \"pool_size\": 50,\n  \"query_pos_sim\": 0.712345,\n  \"mean_neg_sim\": 0.351234,\n  \"max_neg_sim\": 0.581234,\n  \"hit_at_1\": true,\n  \"hit_at_5\": true,\n  \"hit_at_10\": true\n}\n```\n\n## Analysis Outputs\n\n- `stratified_results.json` — full results with bootstrap 95% CIs per stratum\n- `stratified_results.csv` — flat table for easy import\n- `stratified_{dimension}.pdf` — bar charts: R@1 per strategy (left), delta vs random (right)\n- Weighted aggregate delta per dimension (accounts for stratum sizes)\n\n## Execution Plan\n\nWhen M2 checkpoints are ready:\n\n```bash\n# Stage 2: per-query eval (GPU, ~30min per run × 18 runs)\nfor encoder in qwen starcoder; do\n  for strategy in random embedding_distance dataflow_aware; do\n    for seed in 42 43 44; do\n      python evaluate_stratified.py \\\n        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_${encoder}/${strategy}_s${seed} \\\n        --model-name /root/autodl-tmp/structfuse/models/${model_path} \\\n        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl \\\n        --pool-sizes 50 \\\n        --output-dir /root/structfuse/results/stratified/per_query \\\n        --tag ${encoder}_${strategy}_s${seed}\n    done\n  done\ndone\n\n# Stage 3: analysis (CPU, <1min)\npython analyze_stratified.py \\\n  --results-dir /root/structfuse/results/stratified/per_query \\\n  --index-file /root/autodl-tmp/structfuse/stratification_index.json \\\n  --strategies random,embedding_distance,dataflow_aware \\\n  --encoder qwen --seeds 42,43,44 --pool-size 50 \\\n  --output-dir /root/structfuse/results/stratified\n```\n\n## Verification\n\n- [x] `prepare_stratification_index.py` — completed, 44,173 instances indexed\n- [x] `evaluate_stratified.py --dry-run` — passed (2,980 queries, multi-pool-size)\n- [x] `analyze_stratified.py --dry-run` — passed (5 dimensions, JSON+CSV+5 PDFs)\n- [ ] Real eval — awaiting M2 checkpoints\n"
  }
}
````

</details>

---

### Tool result

_source line 98 · 2026-05-15T05:09:54.794404+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratification_spec.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-15T05:09:54.794532+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan005_stratification_spec",
  "type": "report",
  "description": "Plan 005 分层分析规格文档：5 维分层定义、3 阶段管道、数据源、执行计划",
  "project": "structfuse-context",
  "exp_id": "plan_005",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratification_spec.md",
  "tags": "['stratified_analysis', 'plan_005', 'pipeline']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan005_stratification_spec",
    "type": "report",
    "description": "Plan 005 分层分析规格文档：5 维分层定义、3 阶段管道、数据源、执行计划",
    "project": "structfuse-context",
    "exp_id": "plan_005",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratification_spec.md",
    "tags": "['stratified_analysis', 'plan_005', 'pipeline']"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T05:09:54.794730+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_d1d8e6\", \"name\": \"plan005_stratification_spec\", \"type\": \"report\", \"description\": \"Plan 005 分层分析规格文档：5 维分层定义、3 阶段管道、数据源、执行计划\", \"path\": \"projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": \"plan_005\", \"skill\": \"\", \"created_at\": \"2026-05-15T05:09:44.760930+00:00\", \"tags\": [\"stratified_analysis\", \"plan_005\", \"pipeline\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan005-stratified-prep_20260515T050005",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-15T05:09:54.794913+00:00_

完成。总结：

**已完成**：
- **`prepare_stratification_index.py`** — 已运行，从 44,173 条 all.jsonl 构建了 19MB 元数据索引（34.3% 有结构数据，条件 Z%=78.0%）
- **`evaluate_stratified.py`** — GPU 评估脚本，支持多 pool_size（D038），dry-run 验证通过
- **`analyze_stratified.py`** — 5 维分层分析 + bootstrap CI + PDF 图表，dry-run 验证通过（输出 JSON + CSV + 5 个 PDF）
- **`stratification_index.json`** — 已保存到 `/root/autodl-tmp/structfuse/stratification_index.json`
- **规格文档** — 已注册 artifact

**待 M2 checkpoint**：运行 `evaluate_stratified.py` 对 18 个 run（2 encoder × 3 strategy × 3 seed）生成 per-query 结果，然后 `analyze_stratified.py` 一键出全部分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_plan005-stratified-prep_20260515T050005"
}
```

</details>

---
