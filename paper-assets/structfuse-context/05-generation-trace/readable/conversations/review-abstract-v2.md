# review abstract v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_review_abstract-v2_20260515T134237.jsonl`
- **Structured JSON:** [`00bcdd0c60bde2389b84.json`](../../sessions/00/00bcdd0c60bde2389b84.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T13:44:49.495227+00:00_

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
  "session": "worker_review_abstract-v2_20260515T134237",
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

_source line 2 · 2026-05-15T13:44:49.495555+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:44:49.495801+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "structfuse-context",
  "file": "paper/abstract_v2.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "structfuse-context",
    "file": "paper/abstract_v2.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T13:44:49.495951+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'paper/abstract_v2.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T13:44:49.496080+00:00_

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
  "session": "worker_review_abstract-v2_20260515T134237",
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

_source line 6 · 2026-05-15T13:44:49.496318+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md\", \"content\": \"# Paper Framing — StructFuse\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3)\\n\\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \\\"slow and ineffective\\\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\\n\\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\\n\\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a 
…[truncated 13048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:44:49.496475+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "structfuse-context",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "structfuse-context",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:44:49.497167+00:00_

&lt;persisted-output>
Output too large (53.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/ea0b1c3c-58ff-4308-85e3-16d8ebb03157/tool-results/toolu_01E3uRnKhGRxgnFxVTB94yws.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeou
…[truncated 315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:44:49.497389+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/abstract_v2.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/abstract_v2.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:44:49.497523+00:00_

artifacts/_project/paper/abstract_v2.md
artifacts/paper_drafts/abstract_v2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:44:49.497663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/ea0b1c3c-58ff-4308-85e3-16d8ebb03157/tool-results/toolu_01E3uRnKhGRxgnFxVTB94yws.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-structfuse-context/ea0b1c3c-58ff-4308-85e3-16d8ebb03157/tool-results/toolu_01E3uRnKhGRxgnFxVTB94yws.txt"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:44:49.498311+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"m1_reextract_v2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:00:20.578Z\", \"updated_at\": \"2026-05-15T13:04:50.192Z\", \"hypothesis\": \"M1 重提取 v2：恢复 28,276 个因运行时瞬态文件系统故障失败的 instances（82 repos）。CodeQL pack 已修复，端到端测试通过。预期将训练数据从 15,897 提升至 ~44,173。D022 批准。\", \"parent\": \"m1_extraction\", \"spec\": {\"command\": \"bash scripts/rerun_m1_failed.sh (4 CPU workers, CodeQL 2-hop, pack installed)\", \"server\": \"bjb1-42106\", \"data_path\": \"/root/autodl-tmp/structfuse/full_m1_data/\", \"data_count\": 28276, \"model_name\": \"N/A (CodeQL extraction)\", \"seed\": \"N/A\", \"log_path\": \"/root/runs/structfuse-context/m1_reextract_v2.log\", \"checkpoint_source\": \"rerun of m1_extraction failed instances (v2, CodeQL fixed)\", \"eval_data\": \"N/A\"}, \"notes\": \"moto CodeQL call_graph.ql timeout (NOT OOM): directCallEdge predicate exceeds 300s timeout on every instance (exit code 33). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated failure — 1/4 workers stuck on moto (~5min/instance, ~38h total), other 3 workers process pydicom/conan/MONAI normally. DB creation succeeded; bounded_dataflow.ql unaffected.\", \"metrics\": {\"all_jsonl_lines\": 44173, \"last_checked\": \"2026-05-15T20:57 CST\", \"remaining_repos\": [\"Project-MONAI/MONAI (350/524, 66.8%)\", \"getmoto/moto (100/536, 18.7%)\"], \"processes_alive\": 5, \"details\": \"batch_extract.py (4 workers) + CodeQL running on MONAI and moto repos\", \"note\": \"actual output path: /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\", \"issue\": \"CodeQL call_graph on moto consistently fails (exit 33, timeout on directCallEdge predicate). 536 moto instances all fail call_graph, fallback to embedding-distance. Isolated to 1/4 workers.\", \"eta_cst\": \"2026-05-15T22:00\"}}, \"m2_full_starcoder_resumed\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:44:19.253Z\
…[truncated 52492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:44:49.498507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v2.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/abstract_v2.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:44:49.498669+00:00_

1	# Abstract
2	
3	**What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry**
4	
5	Hard negative mining is critical for training contrastive code retrievers, yet the field lacks systematic understanding of which mining strategies work and why. Prior work argues that non-differentiable embedding negatives are ineffective compared to gradient-based alternatives, but this claim has not been evaluated under controlled conditions in structural code retrieval settings. Meanwhile, code's rich structural properties—call graphs, data-flow dependencies—remain entirely unexploited for negative selection.
6	
7	We conduct a controlled comparison of three hard negative mining strategies for repository-level code retrieval: random sampling, static embedding-distance mining, and dataflow-aware mining guided by inter-procedural data-flow analysis. To enable this study, we build a CodeQL-based extraction pipeline that scales to 123 repositories with 0% analysis timeout, making structure-grounded negative mining practically feasible. All experiments use identical training pipelines across two decoder-only encoders (Qwen2.5-Coder-3B and StarCoder2-3B) with three random seeds each, enabling analysis of strategy–encoder interactions.
8	
9	We report two findings. First, static embedding-distance mining provides a reliable retrieval improvement over random baselines (+X.X pp Recall@1 averaged across encoders and seeds) at zero additional computational cost, establishing a strong baseline for future work. Second, as a preliminary observation, dataflow-aware negatives do not consistently outperform embedding mining but exhibit an encoder-dependent interaction pattern: negative difficulty margin analysis suggests that encoder representation geometry—specifically, the degree of embedding space saturation—may mediate strategy effectiveness. All improvements are training-time interventions with zero inference overhead.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_review_abstract-v2_20260515T134237",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T13:44:49.498972+00:00_

## 审查结果: NEEDS_REVISION

### 问题清单 (按严重程度)

**1. [MAJOR] 缺少下游任务评估（SWE-bench）信号**

Abstract 完全没有提及 downstream task evaluation。paper_framing 已列此为 reviewer 最大攻击面之一（plan_003），当前状态 QUEUED。对于一篇以"systematic study"定位的论文，只报告 R@1 而不展示"检索改进是否转化为实际 bug 修复"会被 reviewer 要求 major revision。

建议：在 findings 段末尾加一句 SWE-bench 结果的占位（e.g., "Downstream evaluation on SWE-bench Lite confirms that retrieval gains translate to end-to-end repair performance (+Y.Y% resolve rate)."），待 plan_003 完成后填入。如果最终不跑 SWE-bench，则需要显式声明 scope 限于 retrieval。

**2. [MAJOR] "reliable" 断言缺乏完整证据支撑**

当前 M2 full-scale 数据：
- Qwen: random 3 seeds 完成 (0.5527/0.5554/0.6009), embedding 仅 s43 完成 (0.5606, +0.52pp vs random s43), s44 运行中
- StarCoder: random s42 完成 (0.4604), 其余均在运行中，embedding 0/3 完成

"reliable" 一词要求跨 seed + 跨 encoder 一致性。目前只有 1 个 full-scale seed 的 embedding-random delta (+0.52pp)，且 effect size 相比 pilot (+1.6–2.0pp) 大幅缩水。如果剩余 seeds 不一致，"reliable" 将被 reviewer 直接否定。

建议：保留占位写法，但在 M2 全部完成前不要固化 "reliable" 措辞。备选弱化："provides a consistent improvement in pilot experiments and initial full-scale runs"。

**3. [MAJOR] "entirely unexploited" 过强**

"code's rich structural properties—call graphs, data-flow dependencies—remain **entirely** unexploited for negative selection" — ARISE（paper_framing 已列出）使用 intra-procedural data-flow。虽然 ARISE 用于 inference 而非 training-time negative mining，但 reviewer 可能引用它来挑战 "entirely"。

建议：改为 "remain largely unexploited for training-time negative selection"。

**4. [MINOR] "zero additional computational cost" 与 "zero inference overhead" 混用**

第三段用了两个不同的 cost claim：
- "at zero additional computational cost" — embedding mining 需要计算 pretrained embeddings（一次性开销），并非严格的 zero cost
- "zero inference overhead" — 正确，训练时干预不影响推理

两者含义不同，前者更容易被 reviewer 攻击。

建议：统一为 "at negligible additional cost (a single forward pass over the corpus)" 或删除前半句、只保留末句 "zero inference overhead"。

**5. [MINOR] BM25 baseline 缺位**

Abstract 引用 CoCoHaNeRe（gradient-based vs non-differentiable）作为对手，但 plan_018（BM25 negative baseline）仅完成 Phase 1（数据生成），Phase 2（训练对比）未开始。Abstract 当前未提及 BM25。如果最终论文需要 BM25 baseline 来回应 CoCoHaNeRe，abstract 应至少留出空间。

建议：如果 plan_018 Phase 2 会在提交前完成，在 method 段加 "and BM25-ranked negatives as a lexical baseline"（4 strategies 而非 3）。否则保持现状。

**6. [MINOR] 字数 OK，结构缺 significance 收尾**

~232 词，在 150-250 范围内。四要素中 Problem→Method→Results 完整，但 Impact/Significance 偏弱。末句 "All improvements are training-time interventions with zero inference overhead" 是技术细节，不是 significance statement。

建议：末句改为 broader impact，如 "These findings provide practitioners with an actionable, zero-overhead baseline for hard negative mining and a diagnostic framework (representation geometry) for selecting strategies without exhaustive experimentation."

### 总结

Abstract 整体结构清晰、claim 恰当地 hedged（Claim 2 标注为 preliminary observation）、数字占位合理。主要问题是：(1) 缺下游评估信号，(2) "reliable" 需要完整 M2 数据确认，(3) "entirely unexploited" 过强。建议待 M2 runs 全部完成（Qwen ~May 17, StarCoder ~May 20）后，用实际数字填入并根据 effect size 调整措辞强度，再进行 v3 修订。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_review_abstract-v2_20260515T134237"
}
```

</details>

---
