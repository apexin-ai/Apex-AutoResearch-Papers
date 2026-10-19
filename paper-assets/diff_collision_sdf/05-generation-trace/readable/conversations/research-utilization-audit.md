# research utilization audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 36
- **Original source:** `logs/chats/worker_research_utilization_audit_20260528T191058.jsonl`
- **Structured JSON:** [`376b08860f4c0a43f032.json`](../../sessions/37/376b08860f4c0a43f032.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

73 recorded events

### Tool call

_source line 1 · 2026-05-28T19:22:07.875202+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T19:22:07.875578+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T19:22:07.875765+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'conclusion': 'success'}",
  "project": "diff_collision_sdf",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'conclusion': 'success'}",
    "project": "diff_collision_sdf",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T19:22:07.876369+00:00_

Error: result (123,641 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T19:22:07.876592+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T19:22:07.876733+00:00_

docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/archive/analysis_claim2.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/contingency_claim3.tex
docs/paper/experimental_framework.tex
docs/paper/related_work.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/claim3.tex
docs/paper/claim1.tex
docs/paper/abstract.tex
docs/paper/claim2.tex
docs/paper/discussion.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T19:22:07.876905+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Parse registry experiments",
  "prompt": "You need to extract a structured summary of all experiments from a large JSON file.\n\nThe file is at: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt\n\nIt's JSON with schema: {result: string}. The `result` field contains the actual registry data (likely JSON-encoded string or text).\n\nYour task:\n1. Probe the structure with jq (type/length/keys)\n2. Extract ALL experiments with conclusion=\"success\"\n3. For each experiment, extract:\n   - exp_id\n   - hypothesis (brief, 1 line)\n   - key metrics (CAR%, TSR%, dfCAR%, p-value, or whatever metrics are recorded)\n   - tags or category if available\n   - any notes about what makes this experiment unique\n\nOutput a complete, structured list of ALL success experiments. Do NOT truncate or summarize — I need every single one. Format as a markdown table or structured list.\n\nUse python if jq is insufficient for parsing. The file may have nested JSON (a JSON string inside a JSON object).\n\nWrite the full output to /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Agent",
  "tool_args": {
    "description": "Parse registry experiments",
    "prompt": "You need to extract a structured summary of all experiments from a large JSON file.\n\nThe file is at: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt\n\nIt's JSON with schema: {result: string}. The `result` field contains the actual registry data (likely JSON-encoded string or text).\n\nYour task:\n1. Probe the structure with jq (type/length/keys)\n2. Extract ALL experiments with conclusion=\"success\"\n3. For each experiment, extract:\n   - exp_id\n   - hypothesis (brief, 1 line)\n   - key metrics (CAR%, TSR%, dfCAR%, p-value, or whatever metrics are recorded)\n   - tags or category if available\n   - any notes about what makes this experiment unique\n\nOutput a complete, structured list of ALL success experiments. Do NOT truncate or summarize — I need every single one. Format as a markdown table or structured list.\n\nUse python if jq is insufficient for parsing. The file may have nested JSON (a JSON string inside a JSON object).\n\nWrite the full output to /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-28T19:22:07.877097+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt",
    "description": "Check file size"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T19:22:07.877224+00:00_

125618 /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-28T19:22:07.877345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nprint('Outer keys:', list(outer.keys()))\nprint('Type of result:', type(outer['result']))\nresult_str = outer['result']\nprint('First 500 chars:', result_str[:500])\n\"\n",
  "description": "Probe outer JSON structure and result field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\nprint('Outer keys:', list(outer.keys()))\nprint('Type of result:', type(outer['result']))\nresult_str = outer['result']\nprint('First 500 chars:', result_str[:500])\n\"\n",
    "description": "Probe outer JSON structure and result field"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T19:22:07.877511+00:00_

Outer keys: ['result']
Type of result: &lt;class 'str'>
First 500 chars: {"success": true, "data": {"experiments": {"eval_multiseed_sdf_l01_s0_eseed99": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-28T09:10:44.274Z", "updated_at": "2026-05-28T10:40:38.065Z", "hypothesis": "Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=99. Extends 5-way battery to 7-way, proving SDF redundancy is robust across eval seeds.", "parent": "reeval_sdf_s0_l01_30k", "spec": {"command": "eval completed", "server": "westd-35807", "gpu": ["cuda:3"], "pid": "85399",

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T19:22:07.877659+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract paper numerical data",
  "prompt": "You need to read all the paper tex files and extract every specific numerical result cited in the paper.\n\nThe paper tex files are in: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/\n\nRead these files (all of them, not the archive/ or _archive/ ones):\n- introduction.tex\n- claim1.tex\n- claim2.tex  \n- claim3.tex\n- discussion.tex\n- appendix.tex\n- method.tex\n- abstract.tex\n- experimental_framework.tex\n- related_work.tex\n- contingency_claim3.tex\n\nFor each file, extract:\n1. Every specific numerical value mentioned (percentages, p-values, counts, etc.)\n2. The context of each number (what metric it represents, what condition/task)\n3. Any experiment IDs explicitly referenced (look for patterns like E001, exp_id, or experiment identifiers)\n4. Any table data with specific numbers\n5. Any figure references that cite specific data points\n\nAlso look for:\n- References to specific experimental conditions (e.g., task names, ablation conditions)\n- Any mention of baselines or comparison methods with numbers\n- Statistical test results\n\nFormat the output as a structured document organized by tex file, with each numerical reference listed with its full context.\n\nWrite the complete output to /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract paper numerical data",
    "prompt": "You need to read all the paper tex files and extract every specific numerical result cited in the paper.\n\nThe paper tex files are in: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/\n\nRead these files (all of them, not the archive/ or _archive/ ones):\n- introduction.tex\n- claim1.tex\n- claim2.tex  \n- claim3.tex\n- discussion.tex\n- appendix.tex\n- method.tex\n- abstract.tex\n- experimental_framework.tex\n- related_work.tex\n- contingency_claim3.tex\n\nFor each file, extract:\n1. Every specific numerical value mentioned (percentages, p-values, counts, etc.)\n2. The context of each number (what metric it represents, what condition/task)\n3. Any experiment IDs explicitly referenced (look for patterns like E001, exp_id, or experiment identifiers)\n4. Any table data with specific numbers\n5. Any figure references that cite specific data points\n\nAlso look for:\n- References to specific experimental conditions (e.g., task names, ablation conditions)\n- Any mention of baselines or comparison methods with numbers\n- Statistical test results\n\nFormat the output as a structured document organized by tex file, with each numerical reference listed with its full context.\n\nWrite the complete output to /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T19:22:07.877823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T19:22:07.877959+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{fig_overview_pb}
6	\caption{Overview of three findings. \textbf{(a)}~Action-collapsed safety: Pi0+A1 reports 91.5\% CAR, but 99.6\% of safe episodes have displacement ${<}\,0.1$\,mm; dfCAR drops to ${\approx}\,0$\%. \textbf{(b)}~EE-only SDF fails: SDF gradient repels the end-effector but rotates unmonitored arm links into obstacles; all oracle variants underperform unrefined baselines (73--77\% vs.\ 82--83\%). \textbf{(c)}~Data drives safety: collision-free demonstrations account for $+$26\,pp CAR; SDF supervision adds only $+$2.3\,pp ($p = 0.131$, n.s.).}
7	\label{fig:overview}
8	\end{figure*}
9	
10	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{action-collapsed safety} (colloquially, ``fake safety''): \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.
…[truncated 2362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T19:22:07.878105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T19:22:07.878221+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance. We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, revealing that over 99\% of safe episodes in Pi0-family models are action-collapse artifacts. We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance: ground-truth oracle refinement reduces CAR below unrefined baselines by redistributing collisions to unmonitored arm links, and SDF training supervision shows no statistically significant benefit beyond collision-free demonstrations alone. These findings suggest that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T19:22:07.878355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T19:22:07.878509+00:00_

1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\,=\,7); the reported $\pm$ values reflect variance across training seeds, not evaluation stochasticity. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone. Pi0+A1 LoRA weights were not loaded due to a parameter-name mismatch; only auxiliary heads were trained.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
29	
30	Standard CAR con
…[truncated 1895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T19:22:07.878657+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nprint('Top-level keys:', list(data.keys()))\nprint('data[data] keys:', list(data['data'].keys()))\nexperiments = data['data']['experiments']\nprint('Total experiments:', len(experiments))\n# Show all statuses\nstatuses = {}\nfor k, v in experiments.items():\n    s = v.get('status','?')\n    statuses[s] = statuses.get(s,0) + 1\nprint('Status counts:', statuses)\n\"\n",
  "description": "Parse inner JSON, count experiments and status distribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nprint('Top-level keys:', list(data.keys()))\nprint('data[data] keys:', list(data['data'].keys()))\nexperiments = data['data']['experiments']\nprint('Total experiments:', len(experiments))\n# Show all statuses\nstatuses = {}\nfor k, v in experiments.items():\n    s = v.get('status','?')\n    statuses[s] = statuses.get(s,0) + 1\nprint('Status counts:', statuses)\n\"\n",
    "description": "Parse inner JSON, count experiments and status distribution"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T19:22:07.878783+00:00_

Top-level keys: ['success', 'data', 'error', 'metadata']
data[data] keys: ['experiments', 'count', 'total', 'baseline']
Total experiments: 72
Status counts: {'DONE': 72}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T19:22:07.878904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T19:22:07.879026+00:00_

1	\section{The Action-Collapsed Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}).\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields greater CAR inflation. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, and dfCAR equals raw CAR (28.5\%). The displacement distribution is sharply bimodal (Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Action-collapse decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm. Pi0+A1 dfCAR$\,\approx\,$0: only 3/732 safe episodes exceed the threshold.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular*}{\linewidth}{l@{\extracolsep{\fill}}ccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Collapsed (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0 \\
18	\midrule
19	Pi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\
20	\bottomrule
21	\end{tabular*}
22	\end{table}
23	
24	\begin{figure}[t]
25	\centering
26	\includegraphics[width=\columnwidth]{fig_tsr_car_scatter.pdf}
27	\caption{CAR inflation fro
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T19:22:07.879166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T19:22:07.879289+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Collapsed (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes; the net effect is one collision traded for another. The A3 learned SDF never triggers refinement (0 steps per episode).
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=\columnwidth]{fig_oracle_bar.pdf}
31	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines des
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T19:22:07.879449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T19:22:07.879592+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ af
…[truncated 2777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T19:22:07.879755+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Look at one experiment in full to understand schema\nfirst_key = list(experiments.keys())[0]\nprint(json.dumps(experiments[first_key], indent=2))\n\"\n",
  "description": "Inspect full schema of one experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Look at one experiment in full to understand schema\nfirst_key = list(experiments.keys())[0]\nprint(json.dumps(experiments[first_key], indent=2))\n\"\n",
    "description": "Inspect full schema of one experiment"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T19:22:07.879885+00:00_

{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-28T09:10:44.274Z",
  "updated_at": "2026-05-28T10:40:38.065Z",
  "hypothesis": "Multi-eval-seed robustness: SDF \u03bb=0.01 s0 30K with eval_seed=99. Extends 5-way battery to 7-way, proving SDF redundancy is robust across eval seeds.",
  "parent": "reeval_sdf_s0_l01_30k",
  "spec": {
    "command": "eval completed",
    "server": "westd-35807",
    "gpu": [
      "cuda:3"
    ],
    "pid": "85399",
    "log_path": "~/runs/diff_collision_sdf/eval_multiseed_sdf_l01_s0_eseed99.log",
    "submitted_at": "2026-05-28T09:11:32.469Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "safelibero_object",
    "data_count": 200,
    "model_name": "a1_sdf_pi05_object_pudding_seed0_l01",
    "seed": 99,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000",
    "eval_data": "safelibero_object_levelII",
    "wall_clock_seconds": 5345.6,
    "gpu_hours": 1.48
  },
  "conclusion": "success",
  "metrics": {
    "avg_CAR": 0.57,
    "avg_TSR": 0.465,
    "eval_seed": 99,
    "n_episodes": 50,
    "suite": "safelibero_object"
  },
  "checkpoint_path": "/root/autodl-tmp/eval_results/eval_multiseed_sdf_l01_s0_eseed99.json",
  "completed_at": "2026-05-28T10:40:38.065Z"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T19:22:07.880014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T19:22:07.880138+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation on SafeLIBERO is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{fig5_lambda_curve}
8	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\times$ loss-weight range.}
9	\label{fig:lambda_car}
10	\end{figure}
11	\paragraph{Why EE-only SDF fails.}
12	Two independent causes explain the null result. \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$, CAR remains within the null distribution ($p = 0.131$). \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \emph{reduces} CAR by 5--10\,pp (\S\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
13	
14	\paragraph{Implications for evaluation.}
15	dfCAR corrects action-collapse contamination using only EE positio
…[truncated 1759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T19:22:07.880283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T19:22:07.880493+00:00_

1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Action-collapse rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed 
…[truncated 23508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T19:22:07.880656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T19:22:07.880798+00:00_

1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, 
…[truncated 4583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T19:22:07.880943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T19:22:07.881072+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates barrier functions into diffusion denoising but does not learn intrinsic collision awareness. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, with sign indicating free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li2024cdf} and CSSDF-Net~\cite{chen2026cssdfnet} extend SDFs to configuration space for manipulation planning. RDF~\cite{li2024rdf} represents robot geometry as composable per
…[truncated 1703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T19:22:07.881217+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T19:22:07.881361+00:00_

1	% contingency_claim3.tex — Three pre-written §6.3 paragraphs for λ=0.1 results.
2	% NOT \input'd into main.tex. Copy the matching scenario into claim3.tex
3	% when results arrive. Replace {MEAN}, {S0}, {S1} with actual numbers.
4	%
5	% Scenario selection (D033 thresholds):
6	%   B: CAR mean ≤ 57%    → full redundancy confirmed
7	%   C: CAR mean 57–60%   → inconclusive, flag 2/3 seeds
8	%   A: CAR mean > 60%    → dose-response evidence
9	%
10	% Also includes discussion + abstract patch bullets at the end.
11	
12	
13	%% ====================================================================
14	%% SCENARIO B — Full redundancy (CAR ≤ 57%)
15	%% ====================================================================
16	
17	% --- claim3 §6.3 paragraph ---
18	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
19	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
20	
21	
22	%% ====================================================================
23	%% SCENARIO C — Inconclusive / gray zone (CAR 57–60%)
24	%% ====================================================================
25	
26	% --- claim3 §6.3 paragraph ---
27	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
28	At $\lambda = 0.1$, CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), representing a suggestive 
…[truncated 4686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T19:22:07.881600+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Check all conclusion values\nconclusions = {}\nfor k, v in experiments.items():\n    c = v.get('conclusion','NONE')\n    conclusions[c] = conclusions.get(c,0) + 1\nprint('Conclusion counts:', conclusions)\n\n# Also look at what metrics keys exist across all experiments\nall_metric_keys = set()\nfor k, v in experiments.items():\n    m = v.get('metrics', {})\n    all_metric_keys.update(m.keys())\nprint('All metric keys seen:', sorted(all_metric_keys))\n\"\n",
  "description": "Check conclusion values and all metric keys across experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Check all conclusion values\nconclusions = {}\nfor k, v in experiments.items():\n    c = v.get('conclusion','NONE')\n    conclusions[c] = conclusions.get(c,0) + 1\nprint('Conclusion counts:', conclusions)\n\n# Also look at what metrics keys exist across all experiments\nall_metric_keys = set()\nfor k, v in experiments.items():\n    m = v.get('metrics', {})\n    all_metric_keys.update(m.keys())\nprint('All metric keys seen:', sorted(all_metric_keys))\n\"\n",
    "description": "Check conclusion values and all metric keys across experiments"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T19:22:07.881749+00:00_

Conclusion counts: {'success': 72}
All metric keys seen: ['CAR', 'CAR_avg', 'CAR_task0', 'CAR_task1', 'CAR_task2', 'CAR_task3', 'TSR', 'action_loss', 'analysis', 'avg_CAR', 'avg_TSR', 'avg_ee_disp', 'avg_it_per_sec', 'avg_max_ee_disp', 'avg_max_ee_displacement', 'avg_max_obstacle_displacement', 'best_loss', 'best_loss_step', 'best_step', 'car', 'checkpoint_step', 'collision_threshold', 'conclusion', 'dfCAR', 'dfCAR_100mm', 'dfCAR_stable_range_mm', 'displacement_avg', 'displacement_task0', 'displacement_task1', 'displacement_task2', 'displacement_task3', 'ee_disp', 'ee_disp_range', 'ee_loss', 'eikonal', 'eval_seed', 'fake_safe_pct', 'fake_safe_rate_ee', 'final_action_loss', 'final_ee_loss', 'final_loss', 'final_loss_action', 'final_loss_ee', 'final_loss_sdf', 'final_lr', 'final_sdf_loss', 'frozen', 'frozen_ee', 'frozen_episodes', 'frozen_pct', 'frozen_rate', 'frozen_rate_ee', 'frozen_rate_obs', 'grad_norm', 'lr_final', 'max_dfCAR_variation_2_to_200mm', 'mean', 'mean_displacement', 'min_displacement_m', 'n_active_equals_n_total_at_200mm', 'n_episodes', 'n_models', 'n_refine', 'n_thresholds', 'note', 'obstacle_disp', 'overall_CAR', 'overall_TSR', 'per_task', 'per_task_car', 'per_task_tsr', 'real_safety', 'scenario', 'seed', 'source', 'step', 'steps_completed', 'suite', 'task0_CAR', 'task0_TSR', 'task0_disp', 'task0_ee_disp', 'task0_max_disp', 'task0_obs_frozen_pct', 'task0_orange_juice', 'task0_safe_ee_disp', 'task1_CAR', 'task1_TSR', 'task1_chocolate_pudding', 'task1_disp', 'task1_ee_disp', 'task1_max_disp', 'task1_safe_ee_disp', 'task2_CAR', 'task2_TSR', 'task2_disp', 'task2_ee_disp', 'task2_fake_safety', 'task2_max_disp', 'task2_milk', 'task2_obs_frozen_pct', 'task2_safe_ee_disp', 'task3_CAR', 'task3_TSR', 'task3_bbq_sauce', 'task3_disp', 'task3_ee_disp', 'task3_max_disp', 'task3_safe_ee_disp', 'time_per_step', 'total_episodes', 'total_loss', 'total_steps', 'training_hours', 'training_time_h', 'tsr', 'vram_mib', 'wall_clock_hours', 'wall_time_hours']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-28T19:22:07.881887+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T19:22:07.882014+00:00_

__pycache__
_project
a3_lora_fix_result.json
abc_scenario_patches.md
analysis_m022_norm_stats_root_cause.md
analysis_m026_m027_m028_gradient_refine_diagnosis.md
analyze_d012_results.py
analyze_displacement.py
claim3_data_summary.md
comprehensive_fix_report.txt
diagnose_eval_a3_v11_object.md
diagnose_l01_failures.md
disk_cleanup_report.md
drafts
dream_reports
dual_narrative_templates.md
emergency_cleanup_report.md
eval_a3_v11_object
eval_batch_20270527.md
eval_collision_enhancement_plan.md
eval_commands_d012.md
eval_commands_d012_final.md
eval_openvla_safelibero.py
eval_pi05_safelibero.py
eval_pi05_safelibero_object_v11
eval_prep_l01_high.md
eval_readiness_westd35807.md
eval_safelibero.py
eval_safelibero_openvla.py
fallback_2seed.pdf
fig1_teaser.pdf
fig1_teaser.png
fig1_teaser_design.md
fig1_teaser_v1.png
fig1_teaser_v2.png
fig1_teaser_v3.png
fig1_teaser_v4.png
fig1_teaser_v5.png
fig5_lambda_data.csv
fig5_lambda_stepwise.csv
fig_pertask_car_fingerprint.pdf
fig_pertask_car_fingerprint.png
fig_pertask_car_fingerprint.py
figure1_teaser_design.md
figures
final_draft_post_review.pdf
final_scenario_b_3seed.pdf
fix_a1.py
fix_a3.py
kg3_gradient_toy_test.py
literature_review.md
lora_baseline_launch_checklist.md
manifest.yaml
method_draft.md
metric_definitions.md
openvla_eval_prep.md
paper_data_summary.md
paper_draft.pdf
paper_switch.py
permutation_test.py
permutation_test_results.txt
phase2_fix_report.md
pi05_a1_sdf_feasibility_report.md
pi05_collision_analysis_report.md
plot_fig1_teaser.py
pre_s2_paper.pdf
prep_spatial_a1.md
reeval_comparison.json
reeval_comparison.py
reeval_comparison.tex
reference_audit_report.md
related_work_outline.md
related_work_survey.md
remaining_train_status.md
report_a1_integration.md
report_action_scale_fix.md
report_baseline_fix.md
report_baseline_prep.md
report_data_pipeline.md
report_env_setup_kg1_kg2.md
report_eval_tsr_zero_fix.md
report_kg3_gradient_test.md
report_openpi_deploy.md
report_pi05_object_collision_analysis.md
report_pi0_baseline_f
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-28T19:22:07.882164+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Print all experiments with their full content for inspection\nfor exp_id, exp in experiments.items():\n    print(f'=== {exp_id} ===')\n    print(json.dumps(exp, indent=2))\n    print()\nEOF\n",
  "description": "Dump all 72 experiments in full"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Print all experiments with their full content for inspection\nfor exp_id, exp in experiments.items():\n    print(f'=== {exp_id} ===')\n    print(json.dumps(exp, indent=2))\n    print()\nEOF\n",
    "description": "Dump all 72 experiments in full"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T19:22:07.882300+00:00_

&lt;persisted-output>
Output too large (130.8KB). Full output saved to: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/bcdzrg55b.txt

Preview (first 2KB):
=== eval_multiseed_sdf_l01_s0_eseed99 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-28T09:10:44.274Z",
  "updated_at": "2026-05-28T10:40:38.065Z",
  "hypothesis": "Multi-eval-seed robustness: SDF \u03bb=0.01 s0 30K with eval_seed=99. Extends 5-way battery to 7-way, proving SDF redundancy is robust across eval seeds.",
  "parent": "reeval_sdf_s0_l01_30k",
  "spec": {
    "command": "eval completed",
    "server": "westd-35807",
    "gpu": [
      "cuda:3"
    ],
    "pid": "85399",
    "log_path": "~/runs/diff_collision_sdf/eval_multiseed_sdf_l01_s0_eseed99.log",
    "submitted_at": "2026-05-28T09:11:32.469Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "safelibero_object",
    "data_count": 200,
    "model_name": "a1_sdf_pi05_object_pudding_seed0_l01",
    "seed": 99,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000",
    "eval_data": "safelibero_object_levelII",
    "wall_clock_seconds": 5345.6,
    "gpu_hours": 1.48
  },
  "conclusion": "success",
  "metrics": {
    "avg_CAR": 0.57,
    "avg_TSR": 0.465,
    "eval_seed": 99,
    "n_episodes": 50,
    "suite": "safelibero_object"
  },
  "checkpoint_path": "/root/autodl-tmp/eval_results/eval_multiseed_sdf_l01_s0_eseed99.json",
  "completed_at": "2026-05-28T10:40:38.065Z"
}

=== eval_multiseed_sdf_l01_s0_eseed0 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-28T09:10:43.152Z",
  "updated_at": "2026-05-28T10:40:36.941Z",
  "hypothesis": "Multi-eval-seed robustness: SDF \u03bb=0.01 s0 30K with eval_seed=0. Extends 5-way battery to 7-way, proving SDF redundancy is robus
…[truncated 294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-28T19:22:07.882479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/bcdzrg55b.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/bcdzrg55b.txt"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T19:22:07.882615+00:00_

File content (59466 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T19:22:07.882743+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Print list of all exp_ids sorted by created_at\nsorted_exps = sorted(experiments.items(), key=lambda x: x[1].get('created_at',''))\nfor exp_id, exp in sorted_exps:\n    print(exp_id)\nEOF\n",
  "description": "List all experiment IDs sorted by creation time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Print list of all exp_ids sorted by created_at\nsorted_exps = sorted(experiments.items(), key=lambda x: x[1].get('created_at',''))\nfor exp_id, exp in sorted_exps:\n    print(exp_id)\nEOF\n",
    "description": "List all experiment IDs sorted by creation time"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-28T19:22:07.882871+00:00_

baseline_spatial_bowl_s0_v2
baseline_object_pudding_s0_v2
a3_gradient_spatial_bowl_s0
a3_gradient_object_pudding_s0
baseline_lora_spatial_bowl_s0
baseline_lora_object_pudding_s0
a1_lora_object_pudding_s0
a1_lora_spatial_bowl_s0
eval_a1_lora_object_v11
eval_pi05_safelibero_object_v11_s2
eval_pi05_safelibero_object_v11_s1
train_pi05_a1_obj_s0_l01
train_pi05_a1_obj_s0_l005
train_pi05_a1_obj_s1_l005
train_pi05_a1_obj_s1_l01
train_pi05_a1_obj_s2_l005
train_pi05_a1_obj_s2_l01
train_pi05_lora_baseline_s0
train_pi05_lora_baseline_s1
eval_pi05_a1_30k_s0_l005
eval_pi05_a1_30k_s0_l01
train_pi05_a1_spatial_bowl_s0_l005
eval_pi05_a1_30k_s1_l005_v2
eval_pi05_a1_30k_s2_l005_v2
eval_pi05_a1_30k_s1_l01_v2
eval_pi05_a1_30k_s2_l01_v2
eval_pi05_a1_30k_s1_l005_v3
eval_pi05_a1_30k_s2_l005_v3
eval_pi05_a1_best_s0_l005
eval_pi05_a1_best_s2_l005_10k
eval_pi05_a1_30k_s0_l005_r4
eval_pi05_a1_best_s1_l005_16k
eval_pi05_a1_30k_s1_l005_disp
eval_pi05_a1_30k_s0_l01_disp
train_pi05_phase2_lambda0_s2
train_pi05_a1_obj_s0_l01_high
train_pi05_a1_obj_s1_l01_high
eval_lora_baseline_30k_s0_v2
eval_lora_baseline_30k_s1_v2
eval_pi05_baseline_reeval_disp
eval_lora_baseline_30k_s0_reeval
reeval_sdf_s0_l01_30k
reeval_lora_s1_30k
reeval_sdf_s0_l005_30k
reeval_sdf_s1_l005_30k
reeval_sdf_s2_l005_30k
reeval_sdf_s1_l01_30k
reeval_sdf_s2_l01_30k
eval_phase2_lambda0_s2
train_spatial_bowl_lora_control_s0
reeval_lora_s0_30k_v2
train_pi05_a1_obj_s2_l01_high
analysis_threshold_sensitivity
eval_stepwise_s0_l1_22k
train_pi05_lora_baseline_s2_resume
eval_stepwise_s0_l1_26k_v2
eval_pi05_a1_30k_s0_l01_high
eval_pi05_a1_30k_s1_l01_high
train_phase2_lambda0_extra_seed
eval_lora_s2_30k_v2
eval_spatial_bowl_lora_ctrl_s0
eval_pi05_a1_30k_s2_l01_high
eval_multiseed_lora_s0_eseed42
eval_multiseed_lora_s0_eseed123
eval_multiseed_sdf_l01_s0_eseed42
eval_multiseed_sdf_l01_s0_eseed123
eval_multiseed_sdf_l01_s0_eseed256
eval_spatial_bowl_lora_ctrl_s0_v2
eval_multiseed_lora_s0_eseed0
eval_multiseed_lora_s0_eseed99
eval_multiseed_sdf_l01
…[truncated 44 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-28T19:22:07.883023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Sort by created_at\nsorted_exps = sorted(experiments.items(), key=lambda x: x[1].get('created_at',''))\n\n# For each, print key fields compactly\nfor exp_id, exp in sorted_exps:\n    metrics = exp.get('metrics', {})\n    spec = exp.get('spec', {})\n    tags = exp.get('tags', [])\n    category = exp.get('category', exp.get('type', ''))\n    hypothesis = exp.get('hypothesis', '')\n    conclusion = exp.get('conclusion', '')\n    parent = exp.get('parent', '')\n    created_at = exp.get('created_at', '')\n    \n    # Key performance metrics\n    key_metrics = {}\n    for k in ['avg_CAR','avg_TSR','CAR','TSR','car','tsr','dfCAR','dfCAR_100mm',\n              'dfCAR_stable_range_mm','overall_CAR','overall_TSR',\n              'task0_CAR','task1_CAR','task2_CAR','task3_CAR',\n              'task0_TSR','task1_TSR','task2_TSR','task3_TSR',\n              'best_loss','final_loss','best_step','steps_completed',\n              'n_episodes','n_models','eval_seed','seed',\n              'frozen_pct','frozen_rate','fake_safe_pct','fake_safe_rate_ee',\n              'frozen_rate_ee','frozen_rate_obs',\n              'max_dfCAR_variation_2_to_200mm','n_active_equals_n_total_at_200mm',\n              'collision_threshold','displacement_avg','mean_displacement',\n              'analysis','note','conclusion']:\n        if k in metrics:\n            key_metrics[k] = metrics[k]\n    \n    print(f'EXP_ID: {exp_id}')\n    print(f'  CREATED: {created_at}')\n    print(f'  CONCLUSION: {conclusion}')\n    print(f'  PARENT: {parent}')\n    print(f'  TAGS: {tags}')\n    print(f'  CATEGORY: {category}')\n    print(f'  HYPOTHESIS: {hypothesis}')\n    print(f'  METRICS: {json.dumps(key_metrics)}')\n    # spec extras\n    for k in ['data_path','model_name','checkpoint_source','eval_data','lambda','seed','best_step']:\n        if k in spec:\n            print(f'  SPEC.{k}: {spec[k]}')\n    print()\nEOF\n",
  "description": "Extract all experiment key data in compact format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport json\n\nfpath = '/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/mcp-agent-ml-research-read_registry-1779995474942.txt'\n\nwith open(fpath) as f:\n    outer = json.load(f)\n\ndata = json.loads(outer['result'])\nexperiments = data['data']['experiments']\n\n# Sort by created_at\nsorted_exps = sorted(experiments.items(), key=lambda x: x[1].get('created_at',''))\n\n# For each, print key fields compactly\nfor exp_id, exp in sorted_exps:\n    metrics = exp.get('metrics', {})\n    spec = exp.get('spec', {})\n    tags = exp.get('tags', [])\n    category = exp.get('category', exp.get('type', ''))\n    hypothesis = exp.get('hypothesis', '')\n    conclusion = exp.get('conclusion', '')\n    parent = exp.get('parent', '')\n    created_at = exp.get('created_at', '')\n    \n    # Key performance metrics\n    key_metrics = {}\n    for k in ['avg_CAR','avg_TSR','CAR','TSR','car','tsr','dfCAR','dfCAR_100mm',\n              'dfCAR_stable_range_mm','overall_CAR','overall_TSR',\n              'task0_CAR','task1_CAR','task2_CAR','task3_CAR',\n              'task0_TSR','task1_TSR','task2_TSR','task3_TSR',\n              'best_loss','final_loss','best_step','steps_completed',\n              'n_episodes','n_models','eval_seed','seed',\n              'frozen_pct','frozen_rate','fake_safe_pct','fake_safe_rate_ee',\n              'frozen_rate_ee','frozen_rate_obs',\n              'max_dfCAR_variation_2_to_200mm','n_active_equals_n_total_at_200mm',\n              'collision_threshold','displacement_avg','mean_displacement',\n              'analysis','note','conclusion']:\n        if k in metrics:\n            key_metrics[k] = metrics[k]\n    \n    print(f'EXP_ID: {exp_id}')\n    print(f'  CREATED: {created_at}')\n    print(f'  CONCLUSION: {conclusion}')\n    print(f'  PARENT: {parent}')\n    print(f'  TAGS: {tags}')\n    print(f'  CATEGORY: {category}')\n    print(f'  HYPOTHESIS: {hypothesis}')\n    print(f'  METRICS: {json.dumps(key_metrics)}')\n    # spec extras\n    for k in ['data_path','model_name','checkpoint_source','eval_data','lambda','seed','best_step']:\n        if k in spec:\n            print(f'  SPEC.{k}: {spec[k]}')\n    print()\nEOF\n",
    "description": "Extract all experiment key data in compact format"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T19:22:07.883169+00:00_

&lt;persisted-output>
Output too large (43.6KB). Full output saved to: /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/byu337djy.txt

Preview (first 2KB):
EXP_ID: baseline_spatial_bowl_s0_v2
  CREATED: 2026-05-19T22:40:19.501Z
  CONCLUSION: success
  PARENT: 
  TAGS: []
  CATEGORY: 
  HYPOTHESIS: Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison
  METRICS: {"best_loss": 0.00316, "final_loss": 0.0032, "steps_completed": 30000}
  SPEC.data_path: /root/autodl-tmp/colliforce_data/safelibero_spatial
  SPEC.model_name: pi0_base (full-FT, no LoRA)
  SPEC.seed: 0

EXP_ID: baseline_object_pudding_s0_v2
  CREATED: 2026-05-19T22:40:22.370Z
  CONCLUSION: success
  PARENT: 
  TAGS: []
  CATEGORY: 
  HYPOTHESIS: Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%
  METRICS: {"final_loss": 0.005, "steps_completed": 30000}

EXP_ID: a3_gradient_spatial_bowl_s0
  CREATED: 2026-05-20T02:51:33.071Z
  CONCLUSION: success
  PARENT: 
  TAGS: []
  CATEGORY: 
  HYPOTHESIS: SDF gradient-guided action refinement during training (A3) improves collision avoidance on spatial_bowl Level II — training with lambda_refine SDF gradient loss teaches the model to generate actions that respect obstacle geometry, expecting CAR improvement over baseline with TSR drop <10%. Directly comparable to AEGIS (CAR 86%, TSR 88%) on same task.
  METRICS: {"best_loss": 0.01552, "steps_completed": 30000}

EXP_ID: a3_gradient_object_pudding_s0
  CREATED: 2026-05-20T02:51:33.509Z
  CONCLUSION: success
  PARENT: 
  TAGS: []
  CATEGORY: 
  HYPOTHESIS: SDF gradient-guided action refinement during training (A3) improves collision avoidance on object_pudding Level I — same A3 architecture on a different collision scenario, expecting CA
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-28T19:22:07.883317+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/byu337djy.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/ec6abf35-41f7-4fc6-8d02-58f048a66f4f/tool-results/byu337djy.txt"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-28T19:22:07.883623+00:00_

1	EXP_ID: baseline_spatial_bowl_s0_v2
2	  CREATED: 2026-05-19T22:40:19.501Z
3	  CONCLUSION: success
4	  PARENT: 
5	  TAGS: []
6	  CATEGORY: 
7	  HYPOTHESIS: Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison
8	  METRICS: {"best_loss": 0.00316, "final_loss": 0.0032, "steps_completed": 30000}
9	  SPEC.data_path: /root/autodl-tmp/colliforce_data/safelibero_spatial
10	  SPEC.model_name: pi0_base (full-FT, no LoRA)
11	  SPEC.seed: 0
12	
13	EXP_ID: baseline_object_pudding_s0_v2
14	  CREATED: 2026-05-19T22:40:22.370Z
15	  CONCLUSION: success
16	  PARENT: 
17	  TAGS: []
18	  CATEGORY: 
19	  HYPOTHESIS: Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%
20	  METRICS: {"final_loss": 0.005, "steps_completed": 30000}
21	
22	EXP_ID: a3_gradient_spatial_bowl_s0
23	  CREATED: 2026-05-20T02:51:33.071Z
24	  CONCLUSION: success
25	  PARENT: 
26	  TAGS: []
27	  CATEGORY: 
28	  HYPOTHESIS: SDF gradient-guided action refinement during training (A3) improves collision avoidance on spatial_bowl Level II — training with lambda_refine SDF gradient loss teaches the model to generate actions that respect obstacle geometry, expecting CAR improvement over baseline with TSR drop <10%. Directly comparable to AEGIS (CAR 86%, TSR 88%) on same task.
29	  METRICS: {"best_loss": 0.01552, "steps_completed": 30000}
30	
31	EXP_ID: a3_gradient_object_pudding_s0
32	  CREATED: 2026-05-20T02:51:33.509Z
33	  CONCLUSION: success
34	  PARENT: 
35	  TAGS: []
36	  CATEGORY: 
37	  HYPOTHESIS: SDF gradient-guided action refinement during training (A3) improves collision avoidance on object_pudding Level I — same A3 architecture on a different collision scenario, expecting CAR improvement over baseline. Directly comparable to AEGIS (CAR 32%, TSR 92%) on same task.
38	  METRICS: {"best_loss": 0.01439, "final_loss": 0.01898, "steps_completed":
…[truncated 45909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-28T19:22:07.883797+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/ 2>/dev/null || echo \"DIR NOT EXISTS\"",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/ 2>/dev/null || echo \"DIR NOT EXISTS\"",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-28T19:22:07.883932+00:00_

__pycache__
_project
a3_lora_fix_result.json
abc_scenario_patches.md
analysis_m022_norm_stats_root_cause.md
analysis_m026_m027_m028_gradient_refine_diagnosis.md
analyze_d012_results.py
analyze_displacement.py
claim3_data_summary.md
comprehensive_fix_report.txt
diagnose_eval_a3_v11_object.md
diagnose_l01_failures.md
disk_cleanup_report.md
drafts
dream_reports
dual_narrative_templates.md
emergency_cleanup_report.md
eval_a3_v11_object
eval_batch_20270527.md
eval_collision_enhancement_plan.md
eval_commands_d012.md
eval_commands_d012_final.md
eval_openvla_safelibero.py
eval_pi05_safelibero.py
eval_pi05_safelibero_object_v11
eval_prep_l01_high.md
eval_readiness_westd35807.md
eval_safelibero.py
eval_safelibero_openvla.py
fallback_2seed.pdf
fig1_teaser.pdf
fig1_teaser.png
fig1_teaser_design.md
fig1_teaser_v1.png
fig1_teaser_v2.png
fig1_teaser_v3.png
fig1_teaser_v4.png
fig1_teaser_v5.png
fig5_lambda_data.csv
fig5_lambda_stepwise.csv
fig_pertask_car_fingerprint.pdf
fig_pertask_car_fingerprint.png
fig_pertask_car_fingerprint.py
figure1_teaser_design.md
figures
final_draft_post_review.pdf
final_scenario_b_3seed.pdf
fix_a1.py
fix_a3.py
kg3_gradient_toy_test.py
literature_review.md
lora_baseline_launch_checklist.md
manifest.yaml
method_draft.md
metric_definitions.md
openvla_eval_prep.md
paper_data_summary.md
paper_draft.pdf
paper_switch.py
permutation_test.py
permutation_test_results.txt
phase2_fix_report.md
pi05_a1_sdf_feasibility_report.md
pi05_collision_analysis_report.md
plot_fig1_teaser.py
pre_s2_paper.pdf
prep_spatial_a1.md
reeval_comparison.json
reeval_comparison.py
reeval_comparison.tex
reference_audit_report.md
related_work_outline.md
related_work_survey.md
remaining_train_status.md
report_a1_integration.md
report_action_scale_fix.md
report_baseline_fix.md
report_baseline_prep.md
report_data_pipeline.md
report_env_setup_kg1_kg2.md
report_eval_tsr_zero_fix.md
report_kg3_gradient_test.md
report_openpi_deploy.md
report_pi05_object_collision_analysis.md
report_pi0_baseline_f
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-28T19:22:07.884141+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md",
  "content": "# Paper Numerical References — diff_collision_sdf\n\nExtracted from all tex files in `/docs/paper/`. Organized by file. Covers all specific numerical values, table data, statistical results, and experiment references.\n\n---\n\n## abstract.tex\n\n| Value | Context |\n|-------|---------|\n| >99% | Fraction of safe episodes in Pi0-family models that are action-collapse artifacts (as revealed by dfCAR) |\n\nNo experiment IDs. No table data. Single quantitative claim supporting the dfCAR finding.\n\n---\n\n## introduction.tex\n\n### Figure Caption Data (fig_overview_pb)\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1 reported |\n| 99.6% | Fraction of safe episodes with displacement < 0.1 mm | Pi0+A1 |\n| <0.1 mm | Displacement threshold | 99.6% of safe Pi0+A1 episodes |\n| ≈0% | dfCAR | Pi0+A1 after displacement filtering |\n| 73–77% | CAR range | All EE-only oracle SDF variants |\n| 82–83% | CAR range | Unrefined baselines |\n| +26 pp | CAR gain | From collision-free demonstrations |\n| +2.3 pp | Additional CAR gain | From SDF supervision |\n| p = 0.131 | Statistical test (n.s.) | SDF supervision additional benefit |\n\n### Figure Caption Data (fig1_teaser)\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1 before dfCAR filtering |\n| ≈0% | dfCAR | Pi0+A1 after filtering |\n| 288 mm | Minimum displacement | All safe Pi0.5 episodes |\n\n### Body Text\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1, 800 episodes |\n| 800 | Total episodes | Pi0+A1 evaluation |\n| 732 | Collision-free episodes | Pi0+A1 out of 800 |\n| 99.6% | Fraction with displacement < 0.1 mm | Of the 732 collision-free Pi0+A1 episodes |\n| 0% | TSR | Pi0+A1 across all 800 episodes |\n| 100+ | Number of experiments | Total span of the investigation |\n| 6000+ | Evaluation episodes | Total span of the investigation |\n| ≈0% | dfCAR | Pi0+A1 after displacement filtering |\n| 3/732 | Safe episodes surviving dfCAR threshold | Pi0+A1 |\n| 71.5% | TSR | Pi0.5 |\n| 28.5% | CAR | Pi0.5 |\n| 288 mm | Minimum displacement | All Pi0.5 safe episodes |\n| 73.1–76.9% | CAR range | Oracle SDF variants (ground-truth) |\n| 82–83% | CAR range | Unrefined baselines |\n| ~26 pp | CAR gain | LoRA fine-tuning on Pi0.5 with collision-free demos |\n| p > 0.05 | Statistical significance | SDF supervision, λ ∈ {0.01, 0.1} |\n| >99% | Pi0 safe episodes that are artifacts | dfCAR diagnosis |\n\n### Trainable Parameter Counts (Table 1 / tab:configurations)\n\n| Configuration | Trainable Params |\n|---------------|-----------------|\n| Pi0 Full-FT | ~2.5B |\n| Pi0 LoRA | ~33.5M |\n| Pi0+A1 (SDF aux) | ~658K |\n| Pi0+A3 (learned SDF) | ~34.2M |\n| Pi0.5 (pre-trained) | 0 |\n| Pi0.5 LoRA | ~33.5M |\n| Pi0.5+A1 (SDF aux), λ ∈ {0.005, 0.01, 0.1} | ~34.2M |\n\n---\n\n## method.tex\n\n### Benchmark and Models\n\n| Value | Context |\n|-------|---------|\n| ~2.5B | Pi0 parameter count |\n| 50 | Episodes per task per configuration |\n| 200 | Total episodes per configuration (4 tasks × 50) |\n| 3 | Seeds for Pi0.5 multi-seed runs |\n| 600 | Episodes for Pi0.5 multi-seed runs |\n| seed = 7 | Fixed evaluation seed for all experiments |\n| τ_d = 0.1 mm | Displacement threshold for dfCAR |\n| 1 μm | Upper bound of action-collapsed episode cluster |\n| 200 mm | Lower bound of active episode cluster |\n| 2–200 mm | Range of τ_d values yielding identical dfCAR results |\n| λ ∈ {0.005, 0.01, 0.1} | SDF loss weight range tested |\n| 0 pp | TSR for Pi0+A1 (TSR = 0%; LoRA loading failure) |\n\n---\n\n## claim1.tex (Section: The Action-Collapsed Safety Problem)\n\n### Table: tab:fake_safety — Action-collapse decomposition on SafeLIBERO\n\n| Method | Episodes | CAR (%) | TSR (%) | Collapsed (%) | dfCAR (%) |\n|--------|----------|---------|---------|---------------|-----------|\n| Pi0 Full-FT | 200 | 83.0 | 0.5 | 99.4 | ≈0 |\n| Pi0 LoRA | 200 | 82.0 | 0.0 | ~99 | ≈0 |\n| Pi0+A1 (SDF) | 800 | 91.5 | 0.0 | 99.6 | ≈0 |\n| Pi0.5 | 200 | 28.5 | 71.5 | 0.0 | 28.5 |\n\n### Figure Caption (fig_tsr_car_scatter)\n\n| Value | Context |\n|-------|---------|\n| 82–91 pp | CAR inflation gap (reported vs dfCAR) for Pi0-family models |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| >99% | Fraction of collision-free episodes that are action-collapse artifacts in every Pi0 configuration |\n| 91.5% | Raw CAR for Pi0+A1 (highest among Pi0 configs) |\n| 0% (TSR) | Pi0+A1 TSR — parameter-name mismatch prevents LoRA loading |\n| 200 mm | Minimum displacement of safe Pi0.5 episodes |\n| 28.5% | dfCAR for Pi0.5, equals raw CAR |\n| 82–91 pp | Pi0-family CAR inflation gaps |\n| 3/732 | Pi0+A1 safe episodes exceeding τ_d = 0.1 mm threshold |\n\n---\n\n## claim2.tex (Section: End-Effector-Only SDF Cannot Ensure Full-Body Safety)\n\n### Table: tab:oracle — Oracle SDF refinement results\n\n| Method | CAR (%) | Collapsed (%) | Refines/ep |\n|--------|---------|---------------|-----------|\n| LoRA baseline (no refine) | 82.0 | 99.4 | -- |\n| Full-FT baseline (no refine) | 83.0 | -- | -- |\n| Oracle-adaptive (GT, dyn. α) | 75.0 | 98.3 | 14.2 |\n| Oracle-fixed (GT, α=0.005) | 73.1 | 98.3 | 14.8 |\n| Oracle-feature (GT, feat. space) | 76.9 | 96.7 | 241.7 |\n| A3 learned SDF | 77.1 | -- | 0.0 |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| 76.9% | Best oracle CAR (Oracle-feature) |\n| 5.1 pp | Gap: best oracle below LoRA baseline (82.0% – 76.9%) |\n| 82.0% | LoRA baseline CAR |\n| +9 pp | Oracle refinement improvement on the one task where EE is primary collision body |\n| 0 | Refinement steps per episode for A3 learned SDF |\n\n---\n\n## claim3.tex (Section: Avoidance Source Diagnosis)\n\n### Table: tab:avoidance_source — Avoidance source attribution on SafeLIBERO\n\n| Method | Seeds | TSR (%) | CAR (%) | EE Disp (m) |\n|--------|-------|---------|---------|-------------|\n| Pi0.5 baseline | 1 | 71.5 | 28.5 | 0.367 |\n| LoRA-only (no SDF) | 3 | 51.5 ± 0.0 | 54.67 ± 2.02 | 0.391 |\n| LoRA+SDF λ=0.005 | 3 | 54.0 ± 3.0 | 54.5 ± 2.29 | 0.387 |\n| LoRA+SDF λ=0.01 | 3 | 53.8 ± 1.5 | 56.33 ± 1.61 | 0.389 |\n| LoRA+SDF λ=0.1 | 3 | 50.2 ± 3.9 | 57.00 ± 2.18 | 0.394 |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| ~26 pp | CAR gain from collision-free demonstrations (28.5% → 54.67%) |\n| 20× | Range of loss weight tested (λ from 0.005 to 0.1) |\n| 30K | Training checkpoint used for all evaluations |\n| 0% | Action-collapsed rate for all fine-tuned models |\n| >0.37 m | Minimum EE displacement for all fine-tuned models |\n| 57.5% | CAR for Phase 2 ablation (λ=0 after step 5K), 18K checkpoint, single seed s2 |\n| 18K | Checkpoint for Phase 2 ablation (13K steps of Phase 2 training) |\n| 5K | Steps at which λ set to 0 in Phase 2 ablation |\n| 57.00% | CAR for λ=0.1 (3-seed mean) |\n| 54.67% | CAR for LoRA-only (3-seed mean) |\n| p = 0.131 | Two-tailed permutation test, λ=0.1 vs null |\n| p > 0.05 | SDF conditions at λ ∈ {0.01, 0.1}, no significant benefit |\n| ~2.3 pp | Observed effect size (SDF vs LoRA-only) |\n| 5.0 pp | Minimum detectable effect (MDE) at 80% power, n=3, α=0.05 |\n| ~18–20 pp | TSR degradation from fine-tuning (71.5% → 51.5–54.0%) |\n| 0.39 | SSR/TSR ratio for Pi0.5 baseline |\n| 0.51–0.60 | SSR/TSR ratio range for fine-tuned models |\n| 3 seeds per group | Statistical design |\n| σ ≈ 2.0 pp | LoRA cross-seed standard deviation |\n| 84 permutations = C(9,3) | Null B permutation count |\n| p = 0.300 | Null A (LoRA-only seeds only), λ=0.1 |\n| 20 permutations = C(6,3) | Null A permutation count |\n\n### λ=0.1 Individual Seeds\n\n| Seed | CAR (%) |\n|------|---------|\n| s0 | 58.0 |\n| s1 | 58.5 |\n| s2 | 54.5 |\n\n### Matched Evaluation Seeds (paired comparison)\n\n| Paired eval seed | λ=0.1 vs LoRA advantage |\n|-----------------|-------------------------|\n| Seed 1 | +1.5 pp |\n| Seed 2 | +2.5 pp |\n| Seed 3 | +5.5 pp |\n| Cross-seed std (λ=0.1) | σ = 0.9 pp |\n| Cross-seed std (LoRA) | σ = 2.0 pp |\n\n---\n\n## discussion.tex (Section: Discussion and Conclusion / Limitations)\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| 100+ | Experiments conducted across two VLA model families |\n| 6000+ | Total evaluation episodes |\n| ~26 pp | CAR gain from collision-free demonstrations |\n| 5–10 pp | CAR reduction from oracle SDF refinement (EE-only, below baselines) |\n| p = 0.131 | λ=0.1, within null distribution |\n| ~4000× | Parameter range over which dfCAR quantifies contamination |\n| n=3 | Seeds per condition (statistical limitation) |\n| MDE ≈ 5 pp | Minimum detectable effect at 80% power |\n\n---\n\n## experimental_framework.tex\n\n### Benchmark and Evaluation Protocol\n\n| Value | Context |\n|-------|---------|\n| 50 | Episodes per task |\n| 200 | Total episodes per configuration |\n| 3 | Seeds for Pi0.5 multi-seed runs |\n| 600 | Episodes per multi-seed configuration |\n| τ_d = 0.1 mm | dfCAR displacement threshold |\n| 1 μm | Upper cluster boundary (action-collapsed episodes) |\n| 200 mm | Lower cluster boundary (active episodes) |\n| 2–200 mm | Range of τ_d yielding identical filtering |\n| [2, 200] mm | Robust τ_d range |\n\n### Model Parameter Counts\n\n| Model | Params |\n|-------|--------|\n| Pi0 | ~3B |\n| Pi0.5 | ~3.5B |\n| LoRA baseline | ~33.5M trainable |\n| SDF Decoder (A1) | ~395K params |\n| EE Extractor (A1) | ~263K params |\n\n### Oracle Evaluation\n\n| Value | Context |\n|-------|---------|\n| 160 | Oracle evaluation episodes (4 tasks × 40) |\n| α = 0.005 | Fixed step size for Oracle-fixed |\n\n---\n\n## related_work.tex\n\nNo specific experimental numbers cited. Qualitative comparisons only.\n\n---\n\n## appendix.tex\n\n### Appendix: Displacement Distribution (sec:appendix_displacement)\n\n| Value | Context |\n|-------|---------|\n| <1 μm | Pi0-family episode displacement cluster |\n| >200 mm | Pi0.5 episode displacement cluster |\n| [2, 200] mm | τ_d range yielding identical dfCAR |\n\n### Appendix: Displacement Threshold Sensitivity (tab:threshold_sensitivity)\n\nAction-collapse rate (% episodes with d_max < τ_d):\n\n| τ_d | A1-LoRA (Pi0) | Pi0.5 Baseline | Pi0.5+A1 (SDF aux) |\n|-----|---------------|----------------|---------------------|\n| 0.001 mm (1 μm) | 73.9% | 0.0% | 0.0% |\n| 0.1 mm | 99.6% | 0.0% | 0.0% |\n| 1.0 mm | 100.0% | 0.0% | 0.0% |\n| 10 mm | 100.0% | 0.0% | 0.0% |\n\n| Value | Context |\n|-------|---------|\n| 73.9% | A1-LoRA collapse rate even at τ_d = 1 μm |\n| 1–10 mm | Typical action magnitudes in manipulation tasks |\n\n### Table: tab:dfcar_threshold — dfCAR (%) across displacement thresholds (fine-tuned Pi0.5, n=200 per seed)\n\n| Condition | 2 mm | 5 mm | 10 mm | 20 mm | 50 mm | 100 mm | 200 mm | 300 mm |\n|-----------|------|------|-------|-------|-------|--------|--------|--------|\n| LoRA s0 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 |\n| LoRA s1 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 |\n| SDF λ=0.005 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.1 |\n| SDF λ=0.005 s1 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 |\n| SDF λ=0.005 s2 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.3 |\n| SDF λ=0.01 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 |\n| SDF λ=0.01 s1 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.1 |\n| SDF λ=0.01 s2 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.0 |\n\nNote: At τ_d = 300 mm, 0–2 episodes per seed fall below threshold (displacement 200–300 mm), causing ≤0.5 pp deviation.\n\n### Appendix: Per-Task TSR Breakdown (tab:per_task_tsr)\n\nPer-task TSR (%) at 30K steps (Baseline = seed-7 re-eval, LoRA/SDF = 3-seed means):\n\n| Task | Pi0.5 Base | LoRA-only | SDF λ=0.005 | SDF λ=0.01 |\n|------|-----------|-----------|-------------|------------|\n| Orange Juice | 74.0 | 30.0 | 33.3 | 24.7 |\n| Chocolate Pudding | 80.0 | 70.7 | 78.0 | 76.7 |\n| Milk | 66.0 | 44.7 | 35.3 | 48.7 |\n| BBQ Sauce | 66.0 | 60.7 | 69.3 | 65.3 |\n| Mean | 71.5 | 51.5 | 54.0 | 53.8 |\n\n### Appendix: Per-Task CAR Breakdown (tab:per_task_car)\n\nPer-task CAR (%) at 30K steps (OJ=Orange Juice, CP=Chocolate Pudding):\n\n| Condition | OJ | CP | Milk | BBQ | Agg. |\n|-----------|----|----|------|-----|------|\n| LoRA s0 | 56 | 74 | 70 | 26 | 56.5 |\n| LoRA s1 | 54 | 68 | 72 | 16 | 52.5 |\n| LoRA s2 | 56 | 76 | 62 | 26 | 55.0 |\n| SDF λ=0.005 (3-seed) | 54.0 | 72.7 | 71.3 | 20.0 | 54.5 |\n| SDF λ=0.01 (3-seed) | 57.3 | 72.7 | 72.0 | 23.3 | 56.3 |\n| SDF λ=0.1 s0 | 60 | 74 | 68 | 30 | 58.0 |\n| SDF λ=0.1 s1 | 66 | 72 | 70 | 26 | 58.5 |\n| SDF λ=0.1 s2 | 56 | 76 | 70 | 16 | 54.5 |\n| SDF λ=0.1 (3-seed) | 60.7 | 74.0 | 69.3 | 24.0 | 57.0 |\n\nAdditional displacement data for λ=0.1 seed 1:\n- avg_max_obstacle_displacement = 0.0553 m\n- Per-task: OJ=0.033 m, CP=0.055 m, Milk=0.041 m, BBQ=0.093 m\n\n### Appendix: Safe Success Rate (tab:ssr)\n\n| Condition | TSR (%) | CAR (%) | SSR (%) | SSR/TSR |\n|-----------|---------|---------|---------|---------|\n| Pi0.5 baseline | 71.5 | 28.5 | 28.0 | 0.39 |\n| LoRA-only (3 seeds) | 51.5 | 54.67 | 27.7 | 0.54 |\n| SDF λ=0.005 (3 seeds) | 54.0 | 54.5 | 27.8 | 0.51 |\n| SDF λ=0.01 (3 seeds) | 53.8 | 56.33 | 30.2 | 0.56 |\n| SDF λ=0.1 (3 seeds) | 50.2 | 57.00 | 30.2 | 0.60 |\n\n### Appendix: Per-Task Oracle Analysis (tab:oracle_pertask)\n\nPer-task CAR (%) for oracle refinement (evaluated on 160 episodes, 4 tasks × 40):\n\n| Method | Task 0 (OJ) | Task 1 (CP) | Task 2 (Milk) | Task 3 (BBQ) | Aggregate |\n|--------|-------------|-------------|---------------|--------------|-----------|\n| LoRA baseline | 96.0 | 46.0 | 98.0 | 88.0 | 82.0 |\n| Oracle-adaptive | 82.5 | 55.0 | 77.5 | 85.0 | 75.0 |\n| Oracle-fixed | 85.0 | 50.0 | 77.5 | 80.0 | 73.1 |\n| Oracle-feature | 90.0 | 47.5 | 82.5 | 87.5 | 76.9 |\n\nKey per-task observations:\n- Task 1 (Chocolate Pudding): only task where EE is primary collision body; Oracle-adaptive improves from 46.0% to 55.0% (+9 pp)\n- Task 0 (Orange Juice): Oracle-adaptive degrades from 96.0% to 82.5% (-13.5 pp)\n- Task 2 (Milk): Oracle-adaptive degrades from 98.0% to 77.5% (-20.5 pp)\n\nOracle-feature firing statistics:\n- 241.7 refinements/episode (vs 14.2 for Cartesian variants — 17× more steps)\n- Gradient magnitudes: 0.004–0.006 (vs 0.18–0.49 for Cartesian variants — 2 orders of magnitude smaller)\n- A3 learned SDF: 0 steps/episode (never triggers)\n\n### Appendix: Null Distribution for SDF Loss Weight Analysis (sec:appendix_null)\n\nNull pool (Null B): 6 per-seed CAR measurements from LoRA-only + λ=0.005:\n- 56.5% (LoRA s0, re-evaluated), 52.5% (LoRA s1), 55.0% (LoRA s2)\n- 57.0% (λ=0.005 s0), 54.0% (λ=0.005 s1), 52.5% (λ=0.005 s2)\n- Null mean: 54.58%, Null std: 1.93% (Bessel-corrected, n-1=5)\n\n| Test | Value |\n|------|-------|\n| λ=0.01 mean | 56.33%, within 0.9σ of null (p > 0.1) |\n| λ=0.1 mean (3 seeds: 58.0, 58.5, 54.5) | 57.00% |\n| Two-tailed permutation p (λ=0.1, Null B) | 0.131 (= 11/84) |\n| One-tailed permutation p (λ=0.1, Null B) | 0.071 (= 6/84) |\n| Total permutations (Null B) | C(9,3) = 84 |\n| Combinations meeting mean ≥ 57.00 | 6 |\n| Significance threshold α | 0.05 |\n\nNull A (LoRA-only seeds only: {56.5, 52.5, 55.0}):\n- C(6,3) = 20 permutations\n- λ=0.1: one-tailed p = 3/20 = 0.150, two-tailed p = 6/20 = 0.300\n- λ=0.01: one-tailed p = 4/20 = 0.200, two-tailed p = 8/20 = 0.400\n- Under Null B: λ=0.01 one-tailed p = 10/84 ≈ 0.119, two-tailed p = 22/84 ≈ 0.262\n\nPhase 2 ablation (λ=0 from step 5K):\n- CAR = 57.5% at 18K checkpoint (13K steps Phase 2, single seed s2)\n- Within null range → no lasting behavioral effect from SDF\n\n### Appendix: Step-wise Checkpoint Analysis for λ=0.1 (tab:stepwise_lambda01)\n\nPer-seed CAR (%) at training checkpoints (200 episodes each):\n\n| Checkpoint | Seed 0 | Seed 1 | Seed 2 | Mean |\n|------------|--------|--------|--------|------|\n| 16K steps | 55.5 | 56.0 | -- | 55.75 |\n| 20K steps | 55.0 | 56.0 | -- | 55.5 |\n| 22K steps | 60.5 | 56.5 | -- | 58.5 |\n| 24K steps | 52.5 | -- | -- | -- |\n| 26K steps | 53.5 | -- | -- | -- |\n| 28K steps | 54.5 | -- | -- | -- |\n| 30K steps | 58.0 | 58.5 | 54.5 | 57.00 |\n\nSeed 0 checkpoint-to-checkpoint fluctuation range: 52.5–60.5% (8 pp spread)\nBinomial noise (n=50 per task, p≈0.5): σ ≈ 7 pp per task\n\n### Appendix: Oracle SDF Refinement Details (sec:appendix_oracle)\n\n| Value | Context |\n|-------|---------|\n| 160 | Total oracle evaluation episodes (4 tasks × 40) |\n| α = 0.005 | Fixed step size for Oracle-fixed |\n| 241.7 | Refinements per episode for Oracle-feature |\n| 14.2 | Refinements per episode for Cartesian variants |\n| 0.004–0.006 | Gradient magnitudes in feature space (Oracle-feature) |\n| 0.18–0.49 | Gradient magnitudes in action/Cartesian space |\n\n### Appendix: Cross-Scene Validation (tab:spatial_bowl)\n\nScene: spatial_bowl (moka pot, wine bottle, milk carton, red coffee mug, yellow book obstacles)\nSingle training seed (seed 0), single eval seed (seed 7), 200 episodes, 30K checkpoint.\n\n| Condition | CAR (%) | TSR (%) |\n|-----------|---------|---------|\n| LoRA-only | 12.0 | 49.0 |\n| SDF λ=0.005 | 11.5 | 51.5 |\n\n| Value | Context |\n|-------|---------|\n| -0.5 pp | CAR difference (SDF vs LoRA-only) on spatial_bowl |\n| 11–12% | CAR range on spatial_bowl |\n| 54–57% | CAR range on object_pudding (for comparison) |\n\n### Appendix: Evaluation Seed Robustness (tab:eval_seed_robustness)\n\nAggregate CAR and TSR (%) across evaluation seeds (200 episodes each):\n\n| Condition | Seed 0 CAR | Seed 7 CAR | Seed 42 CAR | Seed 99 CAR | Seed 123 CAR | Mean±Std CAR |\n|-----------|-----------|-----------|------------|------------|-------------|-------------|\n| LoRA s0 | 53.0 | 56.5 | 56.5 | 57.5 | 53.0 | 55.3±2.1 |\n| SDF λ=0.01 s0 | 52.5 | 57.0 | -- | 57.0 | -- | 55.5±2.6 |\n| SDF λ=0.1 s0 | -- | 58.0 | 59.0 | -- | 58.5 | 58.1±0.9 |\n\nTSR across evaluation seeds:\n\n| Condition | Seed 0 TSR | Seed 7 TSR | Seed 42 TSR | Seed 99 TSR | Seed 123 TSR | Mean±Std TSR |\n|-----------|-----------|-----------|------------|------------|-------------|-------------|\n| LoRA s0 | 55.5 | 51.5 | 46.0 | 52.0 | 50.5 | 51.1±3.4 |\n| SDF λ=0.01 s0 | 48.5 | 52.5 | -- | 46.5 | -- | 49.2±3.1 |\n| SDF λ=0.1 s0 | -- | 47.0 | 52.5 | -- | 53.5 | 50.3±3.2 |\n\nKey comparisons:\n- LoRA s0 CAR range across 5 seeds: 53.0–57.5%, std=2.1 pp\n- SDF λ=0.01 s0 mean CAR: 55.5% vs LoRA 55.3% (near-identical)\n- SDF λ=0.1 s0 mean CAR: 58.1%, difference from LoRA = 2.8 pp (<1.3σ, non-significant)\n\nPer-task CAR for LoRA s0 across 5 evaluation seeds (tab:eval_seed_car_detail):\n\n| Eval seed | OJ | CP | Milk | BBQ | Agg. |\n|-----------|----|----|----|-----|------|\n| 0 | 46 | 70 | 74 | 22 | 53.0 |\n| 7 | 56 | 74 | 70 | 26 | 56.5 |\n| 42 | 60 | 70 | 68 | 28 | 56.5 |\n| 99 | 58 | 76 | 66 | 30 | 57.5 |\n| 123 | 52 | 74 | 66 | 20 | 53.0 |\n| Mean±Std | 54.4±5.5 | 72.8±2.7 | 68.8±3.3 | 25.2±4.1 | 55.3±2.1 |\n\n### Appendix: Training Details (sec:appendix_training)\n\nArchitecture:\n- LoRA rank (vision/PaliGemma): 16, α=16\n- LoRA rank (action expert): 32, α=32\n- SDF Decoder: 4-layer MLP, hidden dim 256, input = pooled suffix features (1024-d) + query points (3-d)\n- EE Extractor: 2-layer MLP, 1024→256→3\n\nTraining schedule:\n- Phase 1: steps 0–5000 (backbone/LoRA frozen, only SDF decoder + EE extractor trained)\n- Phase 2: steps 5000–30000 (LoRA unfrozen, 100-step gradient warmup ramp)\n\nHyperparameter table (tab:hyperparams):\n\n| Parameter | Value |\n|-----------|-------|\n| Base model | Pi0.5 (OpenPi, ~3.5B parameters) |\n| Optimizer | AdamW |\n| Learning rate | 2.5×10⁻⁵ (cosine decay to lr/10) |\n| Warmup steps | 1000 |\n| Batch size | 32 |\n| Total steps | 30000 |\n| λ_sdf | {0.005, 0.01, 0.1} |\n| λ_ee | 0.01 |\n| SDF query points per step | 64 |\n| SDF clamp δ | 0.05 m |\n| Eikonal weight | 0.1 |\n| LoRA rank (vision) | 16 |\n| LoRA rank (action) | 32 |\n| Phase 1 duration | 5000 steps |\n\nEvaluation protocol:\n- Max timesteps per episode: 300\n- Action trajectory length: 50 steps (flow matching)\n- Execute first 5 steps before replanning\n- Camera rotation: 180° for Pi0.5 (corrects TSR from ~5% to ~52%)\n- Oracle variants: 40 episodes per task (160 total), single seed\n- Standard: 50 episodes per task (200 total)\n\nSDF ground truth:\n- Voxel grid: 64³\n- Query points per training step: 64 (randomly sampled)\n\nComputational resources:\n- GPU: NVIDIA RTX PRO 6000 (96 GB)\n- Phase 1 (5K steps): ~6 hours on single GPU\n- Phase 2 (25K steps): ~32 hours\n- Evaluation (200 episodes): ~4 hours\n- Total budget across 100+ experiments: ~700 GPU-hours\n\n---\n\n## contingency_claim3.tex\n\nThis file is NOT included in main.tex (contingency/planning file only). It contains template paragraphs for three λ=0.1 scenarios with placeholder values {MEAN}, {S0}, {S1}, {DELTA}. Key reference values from the scenario framing:\n\n| Value | Context |\n|-------|---------|\n| 54.5% | Null distribution mean referenced in Scenario B/C templates |\n| 2.15 pp | Null distribution σ referenced in Scenario B/C templates |\n| Scenario B threshold | CAR mean ≤ 57% → full redundancy confirmed |\n| Scenario C threshold | CAR mean 57–60% → inconclusive |\n| Scenario A threshold | CAR mean > 60% → dose-response evidence |\n\nNote: The actual paper uses the Scenario C/B result (λ=0.1 mean = 57.00%, p=0.131, within null, non-significant).\n\n---\n\n## Summary: Key Numbers Across All Files\n\n### Primary Result Numbers\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Pi0+A1 raw CAR | 91.5% | claim1, introduction |\n| Pi0+A1 dfCAR | ≈0% (3/732 episodes survive) | claim1, introduction |\n| Pi0+A1 action-collapse rate | 99.6% | claim1 |\n| Pi0 Full-FT raw CAR | 83.0% | claim1 |\n| Pi0 Full-FT action-collapse rate | 99.4% | claim1 |\n| Pi0 LoRA raw CAR | 82.0% | claim1 |\n| Pi0 LoRA action-collapse rate | ~99% | claim1 |\n| Pi0.5 baseline CAR | 28.5% | claim1, claim3 |\n| Pi0.5 baseline TSR | 71.5% | claim1, claim3 |\n| Pi0.5 baseline dfCAR | 28.5% (= raw CAR) | claim1 |\n| Best oracle CAR | 76.9% (Oracle-feature) | claim2 |\n| Worst oracle CAR | 73.1% (Oracle-fixed) | claim2 |\n| Oracle gap vs LoRA baseline | −5.1 pp (best oracle) to −8.9 pp (worst) | claim2 |\n| LoRA-only CAR (fine-tuned Pi0.5) | 54.67% ± 2.02 | claim3 |\n| LoRA+SDF λ=0.1 CAR | 57.00% ± 2.18 | claim3 |\n| SDF vs LoRA delta | ~2.3 pp | claim3 |\n| p-value (λ=0.1 vs null, two-tailed) | 0.131 | claim3, appendix |\n| CAR gain from demonstrations | ~26 pp | claim3, discussion |\n| spatial_bowl SDF vs LoRA delta | -0.5 pp | appendix |\n\n### Experiment IDs Referenced\nNo explicit experiment IDs (e.g., E001, exp_id patterns) appear in any of the tex files. Experiments are referenced by configuration name (LoRA s0/s1/s2, SDF λ=X sY) and checkpoint step (16K, 20K, 22K, 24K, 26K, 28K, 30K).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md",
    "content": "# Paper Numerical References — diff_collision_sdf\n\nExtracted from all tex files in `/docs/paper/`. Organized by file. Covers all specific numerical values, table data, statistical results, and experiment references.\n\n---\n\n## abstract.tex\n\n| Value | Context |\n|-------|---------|\n| >99% | Fraction of safe episodes in Pi0-family models that are action-collapse artifacts (as revealed by dfCAR) |\n\nNo experiment IDs. No table data. Single quantitative claim supporting the dfCAR finding.\n\n---\n\n## introduction.tex\n\n### Figure Caption Data (fig_overview_pb)\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1 reported |\n| 99.6% | Fraction of safe episodes with displacement < 0.1 mm | Pi0+A1 |\n| <0.1 mm | Displacement threshold | 99.6% of safe Pi0+A1 episodes |\n| ≈0% | dfCAR | Pi0+A1 after displacement filtering |\n| 73–77% | CAR range | All EE-only oracle SDF variants |\n| 82–83% | CAR range | Unrefined baselines |\n| +26 pp | CAR gain | From collision-free demonstrations |\n| +2.3 pp | Additional CAR gain | From SDF supervision |\n| p = 0.131 | Statistical test (n.s.) | SDF supervision additional benefit |\n\n### Figure Caption Data (fig1_teaser)\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1 before dfCAR filtering |\n| ≈0% | dfCAR | Pi0+A1 after filtering |\n| 288 mm | Minimum displacement | All safe Pi0.5 episodes |\n\n### Body Text\n\n| Value | Metric | Condition |\n|-------|--------|-----------|\n| 91.5% | CAR | Pi0+A1, 800 episodes |\n| 800 | Total episodes | Pi0+A1 evaluation |\n| 732 | Collision-free episodes | Pi0+A1 out of 800 |\n| 99.6% | Fraction with displacement < 0.1 mm | Of the 732 collision-free Pi0+A1 episodes |\n| 0% | TSR | Pi0+A1 across all 800 episodes |\n| 100+ | Number of experiments | Total span of the investigation |\n| 6000+ | Evaluation episodes | Total span of the investigation |\n| ≈0% | dfCAR | Pi0+A1 after displacement filtering |\n| 3/732 | Safe episodes surviving dfCAR threshold | Pi0+A1 |\n| 71.5% | TSR | Pi0.5 |\n| 28.5% | CAR | Pi0.5 |\n| 288 mm | Minimum displacement | All Pi0.5 safe episodes |\n| 73.1–76.9% | CAR range | Oracle SDF variants (ground-truth) |\n| 82–83% | CAR range | Unrefined baselines |\n| ~26 pp | CAR gain | LoRA fine-tuning on Pi0.5 with collision-free demos |\n| p > 0.05 | Statistical significance | SDF supervision, λ ∈ {0.01, 0.1} |\n| >99% | Pi0 safe episodes that are artifacts | dfCAR diagnosis |\n\n### Trainable Parameter Counts (Table 1 / tab:configurations)\n\n| Configuration | Trainable Params |\n|---------------|-----------------|\n| Pi0 Full-FT | ~2.5B |\n| Pi0 LoRA | ~33.5M |\n| Pi0+A1 (SDF aux) | ~658K |\n| Pi0+A3 (learned SDF) | ~34.2M |\n| Pi0.5 (pre-trained) | 0 |\n| Pi0.5 LoRA | ~33.5M |\n| Pi0.5+A1 (SDF aux), λ ∈ {0.005, 0.01, 0.1} | ~34.2M |\n\n---\n\n## method.tex\n\n### Benchmark and Models\n\n| Value | Context |\n|-------|---------|\n| ~2.5B | Pi0 parameter count |\n| 50 | Episodes per task per configuration |\n| 200 | Total episodes per configuration (4 tasks × 50) |\n| 3 | Seeds for Pi0.5 multi-seed runs |\n| 600 | Episodes for Pi0.5 multi-seed runs |\n| seed = 7 | Fixed evaluation seed for all experiments |\n| τ_d = 0.1 mm | Displacement threshold for dfCAR |\n| 1 μm | Upper bound of action-collapsed episode cluster |\n| 200 mm | Lower bound of active episode cluster |\n| 2–200 mm | Range of τ_d values yielding identical dfCAR results |\n| λ ∈ {0.005, 0.01, 0.1} | SDF loss weight range tested |\n| 0 pp | TSR for Pi0+A1 (TSR = 0%; LoRA loading failure) |\n\n---\n\n## claim1.tex (Section: The Action-Collapsed Safety Problem)\n\n### Table: tab:fake_safety — Action-collapse decomposition on SafeLIBERO\n\n| Method | Episodes | CAR (%) | TSR (%) | Collapsed (%) | dfCAR (%) |\n|--------|----------|---------|---------|---------------|-----------|\n| Pi0 Full-FT | 200 | 83.0 | 0.5 | 99.4 | ≈0 |\n| Pi0 LoRA | 200 | 82.0 | 0.0 | ~99 | ≈0 |\n| Pi0+A1 (SDF) | 800 | 91.5 | 0.0 | 99.6 | ≈0 |\n| Pi0.5 | 200 | 28.5 | 71.5 | 0.0 | 28.5 |\n\n### Figure Caption (fig_tsr_car_scatter)\n\n| Value | Context |\n|-------|---------|\n| 82–91 pp | CAR inflation gap (reported vs dfCAR) for Pi0-family models |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| >99% | Fraction of collision-free episodes that are action-collapse artifacts in every Pi0 configuration |\n| 91.5% | Raw CAR for Pi0+A1 (highest among Pi0 configs) |\n| 0% (TSR) | Pi0+A1 TSR — parameter-name mismatch prevents LoRA loading |\n| 200 mm | Minimum displacement of safe Pi0.5 episodes |\n| 28.5% | dfCAR for Pi0.5, equals raw CAR |\n| 82–91 pp | Pi0-family CAR inflation gaps |\n| 3/732 | Pi0+A1 safe episodes exceeding τ_d = 0.1 mm threshold |\n\n---\n\n## claim2.tex (Section: End-Effector-Only SDF Cannot Ensure Full-Body Safety)\n\n### Table: tab:oracle — Oracle SDF refinement results\n\n| Method | CAR (%) | Collapsed (%) | Refines/ep |\n|--------|---------|---------------|-----------|\n| LoRA baseline (no refine) | 82.0 | 99.4 | -- |\n| Full-FT baseline (no refine) | 83.0 | -- | -- |\n| Oracle-adaptive (GT, dyn. α) | 75.0 | 98.3 | 14.2 |\n| Oracle-fixed (GT, α=0.005) | 73.1 | 98.3 | 14.8 |\n| Oracle-feature (GT, feat. space) | 76.9 | 96.7 | 241.7 |\n| A3 learned SDF | 77.1 | -- | 0.0 |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| 76.9% | Best oracle CAR (Oracle-feature) |\n| 5.1 pp | Gap: best oracle below LoRA baseline (82.0% – 76.9%) |\n| 82.0% | LoRA baseline CAR |\n| +9 pp | Oracle refinement improvement on the one task where EE is primary collision body |\n| 0 | Refinement steps per episode for A3 learned SDF |\n\n---\n\n## claim3.tex (Section: Avoidance Source Diagnosis)\n\n### Table: tab:avoidance_source — Avoidance source attribution on SafeLIBERO\n\n| Method | Seeds | TSR (%) | CAR (%) | EE Disp (m) |\n|--------|-------|---------|---------|-------------|\n| Pi0.5 baseline | 1 | 71.5 | 28.5 | 0.367 |\n| LoRA-only (no SDF) | 3 | 51.5 ± 0.0 | 54.67 ± 2.02 | 0.391 |\n| LoRA+SDF λ=0.005 | 3 | 54.0 ± 3.0 | 54.5 ± 2.29 | 0.387 |\n| LoRA+SDF λ=0.01 | 3 | 53.8 ± 1.5 | 56.33 ± 1.61 | 0.389 |\n| LoRA+SDF λ=0.1 | 3 | 50.2 ± 3.9 | 57.00 ± 2.18 | 0.394 |\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| ~26 pp | CAR gain from collision-free demonstrations (28.5% → 54.67%) |\n| 20× | Range of loss weight tested (λ from 0.005 to 0.1) |\n| 30K | Training checkpoint used for all evaluations |\n| 0% | Action-collapsed rate for all fine-tuned models |\n| >0.37 m | Minimum EE displacement for all fine-tuned models |\n| 57.5% | CAR for Phase 2 ablation (λ=0 after step 5K), 18K checkpoint, single seed s2 |\n| 18K | Checkpoint for Phase 2 ablation (13K steps of Phase 2 training) |\n| 5K | Steps at which λ set to 0 in Phase 2 ablation |\n| 57.00% | CAR for λ=0.1 (3-seed mean) |\n| 54.67% | CAR for LoRA-only (3-seed mean) |\n| p = 0.131 | Two-tailed permutation test, λ=0.1 vs null |\n| p > 0.05 | SDF conditions at λ ∈ {0.01, 0.1}, no significant benefit |\n| ~2.3 pp | Observed effect size (SDF vs LoRA-only) |\n| 5.0 pp | Minimum detectable effect (MDE) at 80% power, n=3, α=0.05 |\n| ~18–20 pp | TSR degradation from fine-tuning (71.5% → 51.5–54.0%) |\n| 0.39 | SSR/TSR ratio for Pi0.5 baseline |\n| 0.51–0.60 | SSR/TSR ratio range for fine-tuned models |\n| 3 seeds per group | Statistical design |\n| σ ≈ 2.0 pp | LoRA cross-seed standard deviation |\n| 84 permutations = C(9,3) | Null B permutation count |\n| p = 0.300 | Null A (LoRA-only seeds only), λ=0.1 |\n| 20 permutations = C(6,3) | Null A permutation count |\n\n### λ=0.1 Individual Seeds\n\n| Seed | CAR (%) |\n|------|---------|\n| s0 | 58.0 |\n| s1 | 58.5 |\n| s2 | 54.5 |\n\n### Matched Evaluation Seeds (paired comparison)\n\n| Paired eval seed | λ=0.1 vs LoRA advantage |\n|-----------------|-------------------------|\n| Seed 1 | +1.5 pp |\n| Seed 2 | +2.5 pp |\n| Seed 3 | +5.5 pp |\n| Cross-seed std (λ=0.1) | σ = 0.9 pp |\n| Cross-seed std (LoRA) | σ = 2.0 pp |\n\n---\n\n## discussion.tex (Section: Discussion and Conclusion / Limitations)\n\n### Body Text\n\n| Value | Context |\n|-------|---------|\n| 100+ | Experiments conducted across two VLA model families |\n| 6000+ | Total evaluation episodes |\n| ~26 pp | CAR gain from collision-free demonstrations |\n| 5–10 pp | CAR reduction from oracle SDF refinement (EE-only, below baselines) |\n| p = 0.131 | λ=0.1, within null distribution |\n| ~4000× | Parameter range over which dfCAR quantifies contamination |\n| n=3 | Seeds per condition (statistical limitation) |\n| MDE ≈ 5 pp | Minimum detectable effect at 80% power |\n\n---\n\n## experimental_framework.tex\n\n### Benchmark and Evaluation Protocol\n\n| Value | Context |\n|-------|---------|\n| 50 | Episodes per task |\n| 200 | Total episodes per configuration |\n| 3 | Seeds for Pi0.5 multi-seed runs |\n| 600 | Episodes per multi-seed configuration |\n| τ_d = 0.1 mm | dfCAR displacement threshold |\n| 1 μm | Upper cluster boundary (action-collapsed episodes) |\n| 200 mm | Lower cluster boundary (active episodes) |\n| 2–200 mm | Range of τ_d yielding identical filtering |\n| [2, 200] mm | Robust τ_d range |\n\n### Model Parameter Counts\n\n| Model | Params |\n|-------|--------|\n| Pi0 | ~3B |\n| Pi0.5 | ~3.5B |\n| LoRA baseline | ~33.5M trainable |\n| SDF Decoder (A1) | ~395K params |\n| EE Extractor (A1) | ~263K params |\n\n### Oracle Evaluation\n\n| Value | Context |\n|-------|---------|\n| 160 | Oracle evaluation episodes (4 tasks × 40) |\n| α = 0.005 | Fixed step size for Oracle-fixed |\n\n---\n\n## related_work.tex\n\nNo specific experimental numbers cited. Qualitative comparisons only.\n\n---\n\n## appendix.tex\n\n### Appendix: Displacement Distribution (sec:appendix_displacement)\n\n| Value | Context |\n|-------|---------|\n| <1 μm | Pi0-family episode displacement cluster |\n| >200 mm | Pi0.5 episode displacement cluster |\n| [2, 200] mm | τ_d range yielding identical dfCAR |\n\n### Appendix: Displacement Threshold Sensitivity (tab:threshold_sensitivity)\n\nAction-collapse rate (% episodes with d_max < τ_d):\n\n| τ_d | A1-LoRA (Pi0) | Pi0.5 Baseline | Pi0.5+A1 (SDF aux) |\n|-----|---------------|----------------|---------------------|\n| 0.001 mm (1 μm) | 73.9% | 0.0% | 0.0% |\n| 0.1 mm | 99.6% | 0.0% | 0.0% |\n| 1.0 mm | 100.0% | 0.0% | 0.0% |\n| 10 mm | 100.0% | 0.0% | 0.0% |\n\n| Value | Context |\n|-------|---------|\n| 73.9% | A1-LoRA collapse rate even at τ_d = 1 μm |\n| 1–10 mm | Typical action magnitudes in manipulation tasks |\n\n### Table: tab:dfcar_threshold — dfCAR (%) across displacement thresholds (fine-tuned Pi0.5, n=200 per seed)\n\n| Condition | 2 mm | 5 mm | 10 mm | 20 mm | 50 mm | 100 mm | 200 mm | 300 mm |\n|-----------|------|------|-------|-------|-------|--------|--------|--------|\n| LoRA s0 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 | 56.5 |\n| LoRA s1 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 |\n| SDF λ=0.005 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.1 |\n| SDF λ=0.005 s1 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 | 54.0 |\n| SDF λ=0.005 s2 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.5 | 52.3 |\n| SDF λ=0.01 s0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 | 57.0 |\n| SDF λ=0.01 s1 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 | 57.1 |\n| SDF λ=0.01 s2 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.5 | 54.0 |\n\nNote: At τ_d = 300 mm, 0–2 episodes per seed fall below threshold (displacement 200–300 mm), causing ≤0.5 pp deviation.\n\n### Appendix: Per-Task TSR Breakdown (tab:per_task_tsr)\n\nPer-task TSR (%) at 30K steps (Baseline = seed-7 re-eval, LoRA/SDF = 3-seed means):\n\n| Task | Pi0.5 Base | LoRA-only | SDF λ=0.005 | SDF λ=0.01 |\n|------|-----------|-----------|-------------|------------|\n| Orange Juice | 74.0 | 30.0 | 33.3 | 24.7 |\n| Chocolate Pudding | 80.0 | 70.7 | 78.0 | 76.7 |\n| Milk | 66.0 | 44.7 | 35.3 | 48.7 |\n| BBQ Sauce | 66.0 | 60.7 | 69.3 | 65.3 |\n| Mean | 71.5 | 51.5 | 54.0 | 53.8 |\n\n### Appendix: Per-Task CAR Breakdown (tab:per_task_car)\n\nPer-task CAR (%) at 30K steps (OJ=Orange Juice, CP=Chocolate Pudding):\n\n| Condition | OJ | CP | Milk | BBQ | Agg. |\n|-----------|----|----|------|-----|------|\n| LoRA s0 | 56 | 74 | 70 | 26 | 56.5 |\n| LoRA s1 | 54 | 68 | 72 | 16 | 52.5 |\n| LoRA s2 | 56 | 76 | 62 | 26 | 55.0 |\n| SDF λ=0.005 (3-seed) | 54.0 | 72.7 | 71.3 | 20.0 | 54.5 |\n| SDF λ=0.01 (3-seed) | 57.3 | 72.7 | 72.0 | 23.3 | 56.3 |\n| SDF λ=0.1 s0 | 60 | 74 | 68 | 30 | 58.0 |\n| SDF λ=0.1 s1 | 66 | 72 | 70 | 26 | 58.5 |\n| SDF λ=0.1 s2 | 56 | 76 | 70 | 16 | 54.5 |\n| SDF λ=0.1 (3-seed) | 60.7 | 74.0 | 69.3 | 24.0 | 57.0 |\n\nAdditional displacement data for λ=0.1 seed 1:\n- avg_max_obstacle_displacement = 0.0553 m\n- Per-task: OJ=0.033 m, CP=0.055 m, Milk=0.041 m, BBQ=0.093 m\n\n### Appendix: Safe Success Rate (tab:ssr)\n\n| Condition | TSR (%) | CAR (%) | SSR (%) | SSR/TSR |\n|-----------|---------|---------|---------|---------|\n| Pi0.5 baseline | 71.5 | 28.5 | 28.0 | 0.39 |\n| LoRA-only (3 seeds) | 51.5 | 54.67 | 27.7 | 0.54 |\n| SDF λ=0.005 (3 seeds) | 54.0 | 54.5 | 27.8 | 0.51 |\n| SDF λ=0.01 (3 seeds) | 53.8 | 56.33 | 30.2 | 0.56 |\n| SDF λ=0.1 (3 seeds) | 50.2 | 57.00 | 30.2 | 0.60 |\n\n### Appendix: Per-Task Oracle Analysis (tab:oracle_pertask)\n\nPer-task CAR (%) for oracle refinement (evaluated on 160 episodes, 4 tasks × 40):\n\n| Method | Task 0 (OJ) | Task 1 (CP) | Task 2 (Milk) | Task 3 (BBQ) | Aggregate |\n|--------|-------------|-------------|---------------|--------------|-----------|\n| LoRA baseline | 96.0 | 46.0 | 98.0 | 88.0 | 82.0 |\n| Oracle-adaptive | 82.5 | 55.0 | 77.5 | 85.0 | 75.0 |\n| Oracle-fixed | 85.0 | 50.0 | 77.5 | 80.0 | 73.1 |\n| Oracle-feature | 90.0 | 47.5 | 82.5 | 87.5 | 76.9 |\n\nKey per-task observations:\n- Task 1 (Chocolate Pudding): only task where EE is primary collision body; Oracle-adaptive improves from 46.0% to 55.0% (+9 pp)\n- Task 0 (Orange Juice): Oracle-adaptive degrades from 96.0% to 82.5% (-13.5 pp)\n- Task 2 (Milk): Oracle-adaptive degrades from 98.0% to 77.5% (-20.5 pp)\n\nOracle-feature firing statistics:\n- 241.7 refinements/episode (vs 14.2 for Cartesian variants — 17× more steps)\n- Gradient magnitudes: 0.004–0.006 (vs 0.18–0.49 for Cartesian variants — 2 orders of magnitude smaller)\n- A3 learned SDF: 0 steps/episode (never triggers)\n\n### Appendix: Null Distribution for SDF Loss Weight Analysis (sec:appendix_null)\n\nNull pool (Null B): 6 per-seed CAR measurements from LoRA-only + λ=0.005:\n- 56.5% (LoRA s0, re-evaluated), 52.5% (LoRA s1), 55.0% (LoRA s2)\n- 57.0% (λ=0.005 s0), 54.0% (λ=0.005 s1), 52.5% (λ=0.005 s2)\n- Null mean: 54.58%, Null std: 1.93% (Bessel-corrected, n-1=5)\n\n| Test | Value |\n|------|-------|\n| λ=0.01 mean | 56.33%, within 0.9σ of null (p > 0.1) |\n| λ=0.1 mean (3 seeds: 58.0, 58.5, 54.5) | 57.00% |\n| Two-tailed permutation p (λ=0.1, Null B) | 0.131 (= 11/84) |\n| One-tailed permutation p (λ=0.1, Null B) | 0.071 (= 6/84) |\n| Total permutations (Null B) | C(9,3) = 84 |\n| Combinations meeting mean ≥ 57.00 | 6 |\n| Significance threshold α | 0.05 |\n\nNull A (LoRA-only seeds only: {56.5, 52.5, 55.0}):\n- C(6,3) = 20 permutations\n- λ=0.1: one-tailed p = 3/20 = 0.150, two-tailed p = 6/20 = 0.300\n- λ=0.01: one-tailed p = 4/20 = 0.200, two-tailed p = 8/20 = 0.400\n- Under Null B: λ=0.01 one-tailed p = 10/84 ≈ 0.119, two-tailed p = 22/84 ≈ 0.262\n\nPhase 2 ablation (λ=0 from step 5K):\n- CAR = 57.5% at 18K checkpoint (13K steps Phase 2, single seed s2)\n- Within null range → no lasting behavioral effect from SDF\n\n### Appendix: Step-wise Checkpoint Analysis for λ=0.1 (tab:stepwise_lambda01)\n\nPer-seed CAR (%) at training checkpoints (200 episodes each):\n\n| Checkpoint | Seed 0 | Seed 1 | Seed 2 | Mean |\n|------------|--------|--------|--------|------|\n| 16K steps | 55.5 | 56.0 | -- | 55.75 |\n| 20K steps | 55.0 | 56.0 | -- | 55.5 |\n| 22K steps | 60.5 | 56.5 | -- | 58.5 |\n| 24K steps | 52.5 | -- | -- | -- |\n| 26K steps | 53.5 | -- | -- | -- |\n| 28K steps | 54.5 | -- | -- | -- |\n| 30K steps | 58.0 | 58.5 | 54.5 | 57.00 |\n\nSeed 0 checkpoint-to-checkpoint fluctuation range: 52.5–60.5% (8 pp spread)\nBinomial noise (n=50 per task, p≈0.5): σ ≈ 7 pp per task\n\n### Appendix: Oracle SDF Refinement Details (sec:appendix_oracle)\n\n| Value | Context |\n|-------|---------|\n| 160 | Total oracle evaluation episodes (4 tasks × 40) |\n| α = 0.005 | Fixed step size for Oracle-fixed |\n| 241.7 | Refinements per episode for Oracle-feature |\n| 14.2 | Refinements per episode for Cartesian variants |\n| 0.004–0.006 | Gradient magnitudes in feature space (Oracle-feature) |\n| 0.18–0.49 | Gradient magnitudes in action/Cartesian space |\n\n### Appendix: Cross-Scene Validation (tab:spatial_bowl)\n\nScene: spatial_bowl (moka pot, wine bottle, milk carton, red coffee mug, yellow book obstacles)\nSingle training seed (seed 0), single eval seed (seed 7), 200 episodes, 30K checkpoint.\n\n| Condition | CAR (%) | TSR (%) |\n|-----------|---------|---------|\n| LoRA-only | 12.0 | 49.0 |\n| SDF λ=0.005 | 11.5 | 51.5 |\n\n| Value | Context |\n|-------|---------|\n| -0.5 pp | CAR difference (SDF vs LoRA-only) on spatial_bowl |\n| 11–12% | CAR range on spatial_bowl |\n| 54–57% | CAR range on object_pudding (for comparison) |\n\n### Appendix: Evaluation Seed Robustness (tab:eval_seed_robustness)\n\nAggregate CAR and TSR (%) across evaluation seeds (200 episodes each):\n\n| Condition | Seed 0 CAR | Seed 7 CAR | Seed 42 CAR | Seed 99 CAR | Seed 123 CAR | Mean±Std CAR |\n|-----------|-----------|-----------|------------|------------|-------------|-------------|\n| LoRA s0 | 53.0 | 56.5 | 56.5 | 57.5 | 53.0 | 55.3±2.1 |\n| SDF λ=0.01 s0 | 52.5 | 57.0 | -- | 57.0 | -- | 55.5±2.6 |\n| SDF λ=0.1 s0 | -- | 58.0 | 59.0 | -- | 58.5 | 58.1±0.9 |\n\nTSR across evaluation seeds:\n\n| Condition | Seed 0 TSR | Seed 7 TSR | Seed 42 TSR | Seed 99 TSR | Seed 123 TSR | Mean±Std TSR |\n|-----------|-----------|-----------|------------|------------|-------------|-------------|\n| LoRA s0 | 55.5 | 51.5 | 46.0 | 52.0 | 50.5 | 51.1±3.4 |\n| SDF λ=0.01 s0 | 48.5 | 52.5 | -- | 46.5 | -- | 49.2±3.1 |\n| SDF λ=0.1 s0 | -- | 47.0 | 52.5 | -- | 53.5 | 50.3±3.2 |\n\nKey comparisons:\n- LoRA s0 CAR range across 5 seeds: 53.0–57.5%, std=2.1 pp\n- SDF λ=0.01 s0 mean CAR: 55.5% vs LoRA 55.3% (near-identical)\n- SDF λ=0.1 s0 mean CAR: 58.1%, difference from LoRA = 2.8 pp (<1.3σ, non-significant)\n\nPer-task CAR for LoRA s0 across 5 evaluation seeds (tab:eval_seed_car_detail):\n\n| Eval seed | OJ | CP | Milk | BBQ | Agg. |\n|-----------|----|----|----|-----|------|\n| 0 | 46 | 70 | 74 | 22 | 53.0 |\n| 7 | 56 | 74 | 70 | 26 | 56.5 |\n| 42 | 60 | 70 | 68 | 28 | 56.5 |\n| 99 | 58 | 76 | 66 | 30 | 57.5 |\n| 123 | 52 | 74 | 66 | 20 | 53.0 |\n| Mean±Std | 54.4±5.5 | 72.8±2.7 | 68.8±3.3 | 25.2±4.1 | 55.3±2.1 |\n\n### Appendix: Training Details (sec:appendix_training)\n\nArchitecture:\n- LoRA rank (vision/PaliGemma): 16, α=16\n- LoRA rank (action expert): 32, α=32\n- SDF Decoder: 4-layer MLP, hidden dim 256, input = pooled suffix features (1024-d) + query points (3-d)\n- EE Extractor: 2-layer MLP, 1024→256→3\n\nTraining schedule:\n- Phase 1: steps 0–5000 (backbone/LoRA frozen, only SDF decoder + EE extractor trained)\n- Phase 2: steps 5000–30000 (LoRA unfrozen, 100-step gradient warmup ramp)\n\nHyperparameter table (tab:hyperparams):\n\n| Parameter | Value |\n|-----------|-------|\n| Base model | Pi0.5 (OpenPi, ~3.5B parameters) |\n| Optimizer | AdamW |\n| Learning rate | 2.5×10⁻⁵ (cosine decay to lr/10) |\n| Warmup steps | 1000 |\n| Batch size | 32 |\n| Total steps | 30000 |\n| λ_sdf | {0.005, 0.01, 0.1} |\n| λ_ee | 0.01 |\n| SDF query points per step | 64 |\n| SDF clamp δ | 0.05 m |\n| Eikonal weight | 0.1 |\n| LoRA rank (vision) | 16 |\n| LoRA rank (action) | 32 |\n| Phase 1 duration | 5000 steps |\n\nEvaluation protocol:\n- Max timesteps per episode: 300\n- Action trajectory length: 50 steps (flow matching)\n- Execute first 5 steps before replanning\n- Camera rotation: 180° for Pi0.5 (corrects TSR from ~5% to ~52%)\n- Oracle variants: 40 episodes per task (160 total), single seed\n- Standard: 50 episodes per task (200 total)\n\nSDF ground truth:\n- Voxel grid: 64³\n- Query points per training step: 64 (randomly sampled)\n\nComputational resources:\n- GPU: NVIDIA RTX PRO 6000 (96 GB)\n- Phase 1 (5K steps): ~6 hours on single GPU\n- Phase 2 (25K steps): ~32 hours\n- Evaluation (200 episodes): ~4 hours\n- Total budget across 100+ experiments: ~700 GPU-hours\n\n---\n\n## contingency_claim3.tex\n\nThis file is NOT included in main.tex (contingency/planning file only). It contains template paragraphs for three λ=0.1 scenarios with placeholder values {MEAN}, {S0}, {S1}, {DELTA}. Key reference values from the scenario framing:\n\n| Value | Context |\n|-------|---------|\n| 54.5% | Null distribution mean referenced in Scenario B/C templates |\n| 2.15 pp | Null distribution σ referenced in Scenario B/C templates |\n| Scenario B threshold | CAR mean ≤ 57% → full redundancy confirmed |\n| Scenario C threshold | CAR mean 57–60% → inconclusive |\n| Scenario A threshold | CAR mean > 60% → dose-response evidence |\n\nNote: The actual paper uses the Scenario C/B result (λ=0.1 mean = 57.00%, p=0.131, within null, non-significant).\n\n---\n\n## Summary: Key Numbers Across All Files\n\n### Primary Result Numbers\n\n| Metric | Value | Source |\n|--------|-------|--------|\n| Pi0+A1 raw CAR | 91.5% | claim1, introduction |\n| Pi0+A1 dfCAR | ≈0% (3/732 episodes survive) | claim1, introduction |\n| Pi0+A1 action-collapse rate | 99.6% | claim1 |\n| Pi0 Full-FT raw CAR | 83.0% | claim1 |\n| Pi0 Full-FT action-collapse rate | 99.4% | claim1 |\n| Pi0 LoRA raw CAR | 82.0% | claim1 |\n| Pi0 LoRA action-collapse rate | ~99% | claim1 |\n| Pi0.5 baseline CAR | 28.5% | claim1, claim3 |\n| Pi0.5 baseline TSR | 71.5% | claim1, claim3 |\n| Pi0.5 baseline dfCAR | 28.5% (= raw CAR) | claim1 |\n| Best oracle CAR | 76.9% (Oracle-feature) | claim2 |\n| Worst oracle CAR | 73.1% (Oracle-fixed) | claim2 |\n| Oracle gap vs LoRA baseline | −5.1 pp (best oracle) to −8.9 pp (worst) | claim2 |\n| LoRA-only CAR (fine-tuned Pi0.5) | 54.67% ± 2.02 | claim3 |\n| LoRA+SDF λ=0.1 CAR | 57.00% ± 2.18 | claim3 |\n| SDF vs LoRA delta | ~2.3 pp | claim3 |\n| p-value (λ=0.1 vs null, two-tailed) | 0.131 | claim3, appendix |\n| CAR gain from demonstrations | ~26 pp | claim3, discussion |\n| spatial_bowl SDF vs LoRA delta | -0.5 pp | appendix |\n\n### Experiment IDs Referenced\nNo explicit experiment IDs (e.g., E001, exp_id patterns) appear in any of the tex files. Experiments are referenced by configuration name (LoRA s0/s1/s2, SDF λ=X sY) and checkpoint step (16K, 20K, 22K, 24K, 26K, 28K, 30K).\n"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-28T19:22:07.884516+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-28T19:22:07.884692+00:00_

Done. The file is written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md`.

Summary of what was extracted across all 11 tex files:

**Scope:** All numerical values organized by file, then by table/figure/body-text context. Each entry includes the metric, value, and condition/experiment.

**Key findings from extraction:**

- No explicit experiment IDs (E001-style) appear anywhere in the tex files. Experiments are identified by configuration name (e.g., "LoRA s0", "SDF λ=0.005 s2") and checkpoint step.
- `contingency_claim3.tex` is a planning/contingency file not included in main.tex; it uses `{MEAN}`, `{S0}`, `{S1}`, `{DELTA}` placeholders. The actual results correspond to Scenario B/C (λ=0.1 mean = 57.00%, p=0.131).
- The document contains ~15 tables with fully extracted per-cell data, including per-task breakdowns (4 tasks: Orange Juice, Chocolate Pudding, Milk, BBQ Sauce) across CAR/TSR/SSR metrics and all seed/checkpoint combinations.
- Statistical test results are fully captured: permutation test p-values under both Null A (LoRA-only seeds) and Null B (pooled LoRA+λ=0.005), with exact permutation counts.
- The 700 GPU-hour compute budget and all hyperparameters (AdamW, lr=2.5×10⁻⁵, batch 32, 30K steps, 64³ voxel grid) are included in the training details section.
agentId: ae012885e5adc38a7 (use SendMessage with to: 'ae012885e5adc38a7' to continue this agent)
&lt;usage>total_tokens: 50800
tool_uses: 13
duration_ms: 198203&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-28T19:22:07.884909+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
  "content": "# Registry Success Experiments — Complete Summary\n\nAll 72 experiments have `conclusion=success`. Sorted by `created_at`.\n\n---\n\n## Group 1 — Early Baselines (pi0 full-FT, pi0+LoRA, A3 gradient refine) [May 19–21]\n\n### 1. `baseline_spatial_bowl_s0_v2`\n- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison\n- **Metrics:** best_loss=0.00316, final_loss=0.0032, steps_completed=30000\n- **Unique:** Full-FT (no LoRA) pi0 base; spatial_bowl scene; reference baseline\n\n### 2. `baseline_object_pudding_s0_v2`\n- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%\n- **Metrics:** final_loss=0.005, steps_completed=30000\n- **Unique:** Full-FT (no LoRA) pi0 base; object_pudding scene; reference baseline\n\n### 3. `a3_gradient_spatial_bowl_s0`\n- **Hypothesis:** SDF gradient-guided action refinement during training (A3) on spatial_bowl Level II — expects CAR improvement over baseline with TSR drop <10%; comparable to AEGIS (CAR 86%, TSR 88%)\n- **Metrics:** best_loss=0.01552, steps_completed=30000\n- **Unique:** A3 architecture (SDF gradient loss at train time); spatial_bowl scene\n\n### 4. `a3_gradient_object_pudding_s0`\n- **Hypothesis:** SDF gradient-guided action refinement (A3) on object_pudding Level I — comparable to AEGIS (CAR 32%, TSR 92%)\n- **Metrics:** best_loss=0.01439, final_loss=0.01898, steps_completed=30000\n- **Unique:** A3 architecture; object_pudding scene; model `pi0+A3_gradient_refine`\n\n### 5. `baseline_lora_spatial_bowl_s0`\n- **Hypothesis:** LoRA fine-tuned pi0 baseline on spatial_bowl (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3\n- **Metrics:** best_loss=0.00876, steps_completed=30000\n- **Unique:** LoRA baseline (no collision loss); spatial_bowl; parameter-matched reference for A3\n\n### 6. `baseline_lora_object_pudding_s0`\n- **Hypothesis:** LoRA fine-tuned pi0 baseline on object_pudding (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3\n- **Metrics:** best_loss=0.0124, steps_completed=30000\n- **Unique:** LoRA baseline (no collision loss); object_pudding; parameter-matched reference for A3\n\n### 7. `a1_lora_object_pudding_s0`\n- **Hypothesis:** A1 SDF auxiliary task with LoRA injection (rank 16/32) on object_pudding — Phase 1 SDF warmup (frozen LoRA), Phase 2 joint training; expects CAR improvement over LoRA baseline with TSR drop <10%\n- **Metrics:** best_loss=0.01326, final_loss=0.0184, steps_completed=30000\n- **Unique:** A1 architecture; two-phase training (SDF warmup then joint); model `pi0+LoRA+SDF_aux`\n\n### 8. `a1_lora_spatial_bowl_s0`\n- **Hypothesis:** A1 SDF auxiliary task with LoRA injection on spatial_bowl — Phase 1 SDF warmup, Phase 2 joint; expects CAR improvement over LoRA baseline with TSR drop <10%\n- **Metrics:** best_loss=0.01431, steps_completed=30000\n- **Unique:** A1 architecture on spatial_bowl scene\n\n---\n\n## Group 2 — Pi0.5 Baselines and Initial A1 Diagnosis [May 22]\n\n### 9. `eval_a1_lora_object_v11`\n- **Hypothesis:** A1 (SDF auxiliary loss + LoRA, no runtime refinement) eval on safelibero_object — tests whether SDF auxiliary training signal alone improves CAR over LoRA baseline\n- **Metrics:** TSR=0, n_episodes=200, displacement_avg=0.0027\n- **Unique:** First A1 eval; TSR=0 flagged action collapse; critical diagnostic\n\n### 10. `eval_pi05_safelibero_object_v11_s2`\n- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 2): confirm CAR=28% is stable across seeds\n- **Metrics:** CAR=27.5%, TSR=75.0%, mean_displacement=0.132\n- **Unique:** Pi0.5 pretrained checkpoint (no fine-tune); seed 2 replication\n\n### 11. `eval_pi05_safelibero_object_v11_s1`\n- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 1): confirm CAR=28% is stable\n- **Metrics:** CAR=25.0%, TSR=76.0%, mean_displacement=0.153\n- **Unique:** Pi0.5 pretrained checkpoint; seed 1 replication\n\n---\n\n## Group 3 — Pi0.5+A1 Training Sweep (3 seeds × 2 lambdas) [May 23–24]\n\n### 12. `train_pi05_a1_obj_s0_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 0 — restarted after P0 checkpoint collision fix; tests whether stronger SDF signal produces real collision avoidance or action collapse\n- **Metrics:** best_loss=0.00801, steps_completed=30000\n- **Unique:** Pi0.5 backbone; λ=0.01; seed 0; restart after checkpoint fix\n\n### 13. `train_pi05_a1_obj_s0_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 0 — conservative SDF signal\n- **Metrics:** best_loss=0.007861, steps_completed=30000\n- **Unique:** Pi0.5 backbone; λ=0.005; seed 0\n\n### 14. `train_pi05_a1_obj_s1_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 1 — multi-seed replication of conservative lambda\n- **Metrics:** best_loss=0.01143, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.005; seed 1\n\n### 15. `train_pi05_a1_obj_s1_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 1 — multi-seed replication of stronger lambda\n- **Metrics:** best_loss=0.01168, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.01; seed 1\n\n### 16. `train_pi05_a1_obj_s2_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 2 — third seed for statistical significance\n- **Metrics:** best_loss=0.00874, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.005; seed 2\n\n### 17. `train_pi05_a1_obj_s2_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 2 — third seed for statistical significance of higher SDF signal\n- **Metrics:** best_loss=0.00911, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.01; seed 2\n\n### 18. `train_pi05_lora_baseline_s0`\n- **Hypothesis:** LoRA baseline (no SDF) on object_pudding 30K steps — attribution control; if CAR ≈ Pi0.5 baseline (~27%), confirms ColliForce improvement is from SDF not LoRA\n- **Metrics:** best_loss=0.01025, final_loss=0.01343, best_step=24000\n- **Unique:** Pi0.5+LoRA-only control; seed 0; Claim 4 SDF attribution\n\n### 19. `train_pi05_lora_baseline_s1`\n- **Hypothesis:** LoRA baseline (no SDF) seed 1 on object_pudding — second seed for LoRA-only attribution control\n- **Metrics:** best_loss=0.0113, final_loss=0.01408, best_step=14000\n- **Unique:** Pi0.5+LoRA-only control; seed 1\n\n---\n\n## Group 4 — 30K Eval Matrix (3 seeds × 2 lambdas) [May 25]\n\n### 20. `eval_pi05_a1_30k_s0_l005`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.005): completes 3-seed coverage for conservative lambda\n- **Metrics:** avg_CAR=50%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=42%, task2_CAR=86%, task3_CAR=14%, task0_TSR=2%, task1_TSR=20%, n_episodes=200\n- **Unique:** First corrected eval with fixed checkpoint path; low TSR (old eval bug later discovered)\n\n### 21. `eval_pi05_a1_30k_s0_l01`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.01): completes 3-seed coverage for stronger lambda\n- **Metrics:** avg_CAR=53%, avg_TSR=5.5%, task0_CAR=68%, task1_CAR=46%, task2_CAR=86%, task3_CAR=12%, task0_TSR=2%, task1_TSR=20%, n_episodes=200 (note: old script, no max_ee_displacement)\n- **Unique:** λ=0.01; note flags old script version\n\n### 22. `train_pi05_a1_spatial_bowl_s0_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss on spatial_bowl (λ=0.005, seed 0) — tests cross-scene generalization; bilateral obstacles\n- **Metrics:** best_loss=0.01063, final_loss=0.0137, best_step=28000\n- **Unique:** Cross-scene generalization to spatial_bowl; bilateral obstacle geometry\n\n### 23. `eval_pi05_a1_30k_s1_l005_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) corrected re-run with verified 30K checkpoint path\n- **Metrics:** avg_CAR=52.5%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=40%, task2_CAR=94%, task3_CAR=18%, n_episodes=200\n- **Unique:** v2 correction of checkpoint path bug; seed 1\n\n### 24. `eval_pi05_a1_30k_s2_l005_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) corrected re-run — third seed for statistical significance\n- **Metrics:** avg_CAR=54.5%, avg_TSR=9.5%, task0_CAR=62%, task1_CAR=44%, task2_CAR=90%, task3_CAR=22%, n_episodes=200\n- **Unique:** Third seed; corrected checkpoint path\n\n### 25. `eval_pi05_a1_30k_s1_l01_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.01) corrected re-run with lora_baseline model type\n- **Metrics:** avg_CAR=52.5%, avg_TSR=7.5%, task0_CAR=54%, task1_CAR=48%, task2_CAR=94%, task3_CAR=14%, n_episodes=200\n- **Unique:** λ=0.01; corrected model_type parameter; seed 1\n\n### 26. `eval_pi05_a1_30k_s2_l01_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.01) — completes the 3-seed × 2-lambda eval matrix\n- **Metrics:** avg_CAR=53%, avg_TSR=7.5%, task0_CAR=62%, task1_CAR=42%, task2_CAR=88%, task3_CAR=20%, n_episodes=200\n- **Unique:** Completes the full 3×2 matrix; seed 2; λ=0.01\n\n### 27. `eval_pi05_a1_30k_s1_l005_v3`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) rerun with correct --output_path to preserve per-episode displacement data (v2 JSON was overwritten by concurrent evals)\n- **Metrics:** avg_CAR=51.5%, avg_TSR=4%, task0_CAR=54%, task1_CAR=48%, task2_CAR=88%, task3_CAR=16%, n_episodes=200\n- **Unique:** v3 fix for output path collision; first eval with displacement data preserved\n\n### 28. `eval_pi05_a1_30k_s2_l005_v3`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) rerun with correct --output_path; v2 JSON was overwritten\n- **Metrics:** avg_CAR=53%, avg_TSR=9%, task0_CAR=60%, task1_CAR=46%, task2_CAR=86%, task3_CAR=20%, n_episodes=200\n- **Unique:** v3 fix; seed 2; displacement data preserved\n\n### 29. `eval_pi05_a1_best_s0_l005`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed0, λ=0.005) at best-loss checkpoint (step 26000) — completes 3-seed best-checkpoint coverage\n- **Metrics:** avg_CAR=54.5%, avg_TSR=52%, task0_CAR=50%, task1_CAR=74%, task2_CAR=68%, task3_CAR=26%, n_episodes=50, eval_seed=7, collision_threshold=0.001\n- **Unique:** Best-loss checkpoint (step 26000) not final; task-level breakdown; eval_seed=7\n\n### 30. `eval_pi05_a1_best_s2_l005_10k`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed2, λ=0.005, step 10K) — evaluates the sweet-spot checkpoint before action collapse\n- **Metrics:** avg_CAR=55.5%, avg_TSR=9%, task0_CAR=68%, task1_CAR=44%, task2_CAR=92%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0; analysis: \"ALL episodes have high EE displacement (0.39–0.58m). Zero fake safety. 10K best shows genuine collision avoidance.\"\n- **Unique:** Pre-collapse checkpoint; zero fake-safe episodes; analysis confirms genuine avoidance\n\n### 31. `eval_pi05_a1_30k_s0_l005_r4`\n- **Hypothesis:** Pi0.5+A1 30K eval retry (seed0, λ=0.005) — re-run with fixed eval script to get displacement data\n- **Metrics:** avg_CAR=47%, avg_TSR=7.5%, task0_CAR=58%, task1_CAR=38%, task2_CAR=76%, task3_CAR=16%, n_episodes=200 (note: old script, no max_ee_displacement)\n- **Unique:** Retry with fixed script; old script note still present; seed 0\n\n### 32. `eval_pi05_a1_best_s1_l005_16k`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed1, λ=0.005, step 16000) — best-loss checkpoint vs 30K final\n- **Metrics:** avg_CAR=53%, avg_TSR=6.5%, task0_CAR=58%, task1_CAR=50%, task2_CAR=88%, task3_CAR=16%, n_episodes=200, fake_safe_pct=0\n- **Unique:** Best-loss checkpoint at step 16K; zero fake-safe episodes\n\n### 33. `eval_pi05_a1_30k_s1_l005_disp`\n- **Hypothesis:** Displacement fix verification — rerun s1_l005_30k eval to confirm max_ee_displacement field is correctly output\n- **Metrics:** avg_CAR=54%, avg_TSR=4%, task0_CAR=54%, task1_CAR=58%, task2_CAR=92%, task3_CAR=12%, n_episodes=200, fake_safe_pct=0\n- **Unique:** Explicitly validates displacement field fix; zero fake-safe\n\n### 34. `eval_pi05_a1_30k_s0_l01_disp`\n- **Hypothesis:** Pi0.5+A1 30K displacement eval (seed0, λ=0.01) — re-run with fixed eval script to get max_ee_displacement; tests for 30K action collapse\n- **Metrics:** avg_CAR=52.5%, avg_TSR=6.5%, task0_CAR=76%, task1_CAR=32%, task2_CAR=84%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0\n- **Unique:** λ=0.01; displacement-aware eval; zero fake-safe\n\n---\n\n## Group 5 — Phase 2 Ablation, High-Lambda Training [May 25–26]\n\n### 35. `train_pi05_phase2_lambda0_s2`\n- **Hypothesis:** Phase 2 λ=0 ablation (seed2): resume from seed2 l005 best (10K) checkpoint with SDF loss disabled — tests whether early SDF-encoded collision awareness persists in LoRA weights\n- **Metrics:** best_loss=0.00651, best_step=4000\n- **Unique:** Ablation of SDF loss after warmup; resume from 10K; seed 2; tests LoRA weight retention\n\n### 36. `train_pi05_a1_obj_s0_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed0, 30K) — tests faster collision avoidance learning vs earlier over-avoidance onset\n- **Metrics:** (empty — training only)\n- **Unique:** High lambda=0.1; seed 0; paired with seed 1 for error bars\n\n### 37. `train_pi05_a1_obj_s1_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed1, 30K) — second seed for lambda=0.1 error bars\n- **Metrics:** (empty — training only)\n- **Unique:** High lambda=0.1; seed 1\n\n---\n\n## Group 6 — Rotation Fix Re-evals (LoRA Baseline) [May 26]\n\n### 38. `eval_lora_baseline_30k_s0_v2`\n- **Hypothesis:** LoRA baseline (no SDF) 30K eval on object_pudding seed 0 (v2, base env fix) — expects CAR ≈ Pi0.5 baseline (~27%); critical for Claim 4 SDF attribution\n- **Metrics:** avg_CAR=54.5%, avg_TSR=8.5%, dfCAR_100mm=54.5%, n_episodes=200, frozen_pct=0\n- **Unique:** Surprising high CAR~54.5% (vs expected ~27%); dfCAR_100mm introduced; first dfCAR datapoint\n\n### 39. `eval_lora_baseline_30k_s1_v2`\n- **Hypothesis:** LoRA baseline (no SDF) 30K eval seed 1 (v2, base env fix) — second seed for LoRA-only attribution\n- **Metrics:** avg_CAR=56%, avg_TSR=4%, dfCAR_100mm=56%, n_episodes=200, frozen_pct=0\n- **Unique:** Consistently high LoRA CAR; challenges SDF attribution claim; dfCAR_100mm\n\n### 40. `eval_pi05_baseline_reeval_disp`\n- **Hypothesis:** Pi0.5 base model (no LoRA, no SDF) re-eval with fixed eval script on object_pudding 200ep — obtain EE displacement data for dfCAR baseline comparison\n- **Metrics:** (empty — results pending or logged elsewhere)\n- **Unique:** Raw pi0.5 model re-eval; displacement data for dfCAR analysis\n\n### 41. `eval_lora_baseline_30k_s0_reeval`\n- **Hypothesis:** Re-eval LoRA-only s0 (30K) with fixed eval_safelibero.py (180° image rotation added) — if TSR remains ~6–8%, catastrophic forgetting is real; if TSR >30%, eval bug artifact\n- **Metrics:** CAR=56.5%, TSR=51.5%\n- **Unique:** Critical rotation fix applied; TSR jumped from ~8% to 51.5%, confirming earlier TSR collapse was eval bug\n\n---\n\n## Group 7 — Full Re-eval Batch with Rotation Fix (SDF + LoRA) [May 26]\n\n### 42. `reeval_sdf_s0_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s0 (30K) with fixed eval_safelibero.py (180° rotation) — verify TSR collapse is real or eval bug\n- **Metrics:** car=57%, tsr=52.5%, fake_safe_rate_ee=0, frozen_rate_ee=0, frozen_rate_obs=55.5%\n- **Unique:** First corrected SDF re-eval; frozen_rate_obs=55.5% (obstacle motionless, NOT fake safety); note distinguishes paper definition vs script definition\n\n### 43. `reeval_lora_s1_30k`\n- **Hypothesis:** Re-eval LoRA-only s1 (30K) with fixed eval — second seed for LoRA-only attribution baseline; expected TSR ~50%\n- **Metrics:** car=52.5%, tsr=51.5%, fake_safe_rate_ee=0, frozen_rate_ee=0\n- **Unique:** LoRA-only seed 1; confirms rotation fix recovers TSR\n\n### 44. `reeval_sdf_s0_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s0 (30K) with rotation fix — corrected SDF attribution data\n- **Metrics:** car=57%, tsr=55.5%, fake_safe_rate_ee=0, frozen_rate_ee=0\n- **Unique:** λ=0.005; seed 0; corrected\n\n### 45. `reeval_sdf_s1_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s1 (30K) with rotation fix\n- **Metrics:** CAR=54%, TSR=50.5%\n- **Unique:** λ=0.005; seed 1; corrected\n\n### 46. `reeval_sdf_s2_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s2 (30K) with rotation fix — third seed for λ=0.005\n- **Metrics:** CAR=52.5%, TSR=56%\n- **Unique:** λ=0.005; seed 2; corrected\n\n### 47. `reeval_sdf_s1_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s1 (30K) with rotation fix — second seed for λ=0.01\n- **Metrics:** CAR=57.5%, TSR=55.5%\n- **Unique:** λ=0.01; seed 1; corrected\n\n### 48. `reeval_sdf_s2_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s2 (30K) with rotation fix — third seed for λ=0.01\n- **Metrics:** CAR=54.5%, TSR=53.5%\n- **Unique:** λ=0.01; seed 2; corrected; completes 3-seed λ=0.01 re-eval\n\n---\n\n## Group 8 — Phase 2 λ=0 Eval, LoRA Spatial Bowl, Reeval s0, High-Lambda Training [May 26]\n\n### 49. `eval_phase2_lambda0_s2`\n- **Hypothesis:** Phase 2 LoRA unfrozen training with λ=0 (no SDF loss) seed 2 should achieve baseline-level TSR on safelibero_object — control for SDF-augmented models\n- **Metrics:** (empty — eval results not recorded in metrics field)\n- **Unique:** Phase 2 ablation control; λ=0; tests task retention after SDF warmup removed\n\n### 50. `train_spatial_bowl_lora_control_s0`\n- **Hypothesis:** LoRA-only baseline (without SDF collision loss) on spatial_bowl — safety-violation rate should remain high at pre-training level, establishing the gap SDF training aims to close\n- **Metrics:** (empty — training only)\n- **Unique:** LoRA control for spatial_bowl scene; establishes control arm for cross-scene generalization\n\n### 51. `reeval_lora_s0_30k_v2`\n- **Hypothesis:** Re-eval LoRA-only s0 30K with confirmed rotation-fixed script (seed=7) — previous reeval was from buggy version; second reliable LoRA-only seed for Claim 3 mean±std\n- **Metrics:** CAR=57%, TSR=46%\n- **Unique:** Uses eval_seed=7; explicit confirmation of rotation fix; second reliable LoRA seed\n\n### 52. `train_pi05_a1_obj_s2_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed2, 30K) — third seed for 3-seed statistical power for A/B/C scenario determination\n- **Metrics:** best_loss=0.0104, final_loss=0.0104, best_step=30000\n- **Unique:** High lambda=0.1; seed 2; third seed; final checkpoint = best checkpoint (no early plateau)\n\n---\n\n## Group 9 — dfCAR Analysis, Stepwise Eval, LoRA Baseline Seed 2 [May 26–27]\n\n### 53. `analysis_threshold_sensitivity`\n- **Hypothesis:** dfCAR threshold τ_d is robust across [2, 200] mm — bimodal displacement gap (collapsed <0.1mm vs active >270mm) means any threshold in this range produces identical dfCAR values\n- **Metrics:** dfCAR_stable_range_mm=\"[2, 200]\", n_models=8, max_dfCAR_variation_2_to_200mm=0, n_active_equals_n_total_at_200mm=true; conclusion: \"dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold\"\n- **Unique:** Analysis experiment (no training/eval); validates dfCAR metric robustness; uses threshold_sensitivity_v2.csv; 8 models tested\n\n### 54. `eval_stepwise_s0_l1_22k`\n- **Hypothesis:** Step-wise eval of Pi0.5+A1 SDF λ=0.1 (seed 0) at 22K checkpoint — third point in step-wise CAR curve (16K: 55.5%, 20K: 55%, 22K: this)\n- **Metrics:** CAR=60.5%, TSR=45.5%, eval_seed=7, frozen_pct=0\n- **Unique:** Step-wise curve point at 22K; λ=0.1; peak CAR in curve\n\n### 55. `train_pi05_lora_baseline_s2_resume`\n- **Hypothesis:** Resume LoRA baseline seed2 training from checkpoint 22000 to 30000 — original run killed by 24h tmux timeout at step 22364\n- **Metrics:** final_loss=0.0117\n- **Unique:** Resume from tmux-killed checkpoint; seed 2; enables 3v3 statistical comparison\n\n### 56. `eval_stepwise_s0_l1_26k_v2`\n- **Hypothesis:** The 24K frozen episodes (29.5%) were caused by missing --pi05 flag in eval, not SDF training degradation; re-running 26K eval with --pi05 should eliminate frozen episodes\n- **Metrics:** CAR=53.5%, TSR=53%, dfCAR=53.5%, frozen_rate=0\n- **Unique:** Diagnoses eval bug (missing --pi05 flag); dfCAR introduced; frozen_rate corrected to 0\n\n---\n\n## Group 10 — High-Lambda (λ=0.1) 3-Seed Eval, LoRA Seed 2 Eval, Spatial Bowl Control [May 27–28]\n\n### 57. `eval_pi05_a1_30k_s0_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed0 30K checkpoint — based on stepwise curve (16K–28K CAR ~52.5–60.5%, mean ~55.1%), expects Scenario B (CAR ≤ 57%, SDF redundant)\n- **Metrics:** CAR=58%, TSR=47%, dfCAR=58%, frozen_rate=0\n- **Unique:** λ=0.1; seed 0; 30K; dfCAR=CAR (zero frozen); A/B/C scenario determination\n\n### 58. `eval_pi05_a1_30k_s1_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed1 30K — combined with s0 CAR=58.0% determines A/B/C scenario\n- **Metrics:** CAR=58.5%, TSR=49%, dfCAR=58.5%, frozen_rate=0\n- **Unique:** λ=0.1; seed 1; dfCAR=CAR; seeds 0+1 both at ~58% → Scenario C gray zone\n\n### 59. `train_phase2_lambda0_extra_seed`\n- **Hypothesis:** Phase 2 Stage 1 with seed0 and λ_sdf=0.005 for 10K steps — viable checkpoint for Stage 2 lambda-0 training on object_pudding\n- **Metrics:** (empty — training only)\n- **Unique:** Extra seed for Phase 2 ablation; seed 0; 10K stage 1\n\n### 60. `eval_lora_s2_30k_v2`\n- **Hypothesis:** LoRA baseline seed2 at 30K steps — establishes 3-seed null distribution variance for statistical comparison with SDF-augmented models\n- **Metrics:** overall_CAR=55%, overall_TSR=51.5%\n- **Unique:** Uses `overall_CAR`/`overall_TSR` key names; seed 2; completes 3-seed LoRA null distribution\n\n### 61. `eval_spatial_bowl_lora_ctrl_s0`\n- **Hypothesis:** LoRA baseline (no SDF) on spatial_bowl at 30K steps — high TSR but low CAR, confirming collision avoidance requires explicit SDF training signal\n- **Metrics:** avg_CAR=15.5%, avg_TSR=50%; note: \"v1 old pipeline, superseded by v2\"\n- **Unique:** spatial_bowl scene; LoRA control arm; CAR=15.5% vs object_pudding ~56%; note flags pipeline issue\n\n---\n\n## Group 11 — λ=0.1 Seed 2 Eval, Multi-Eval-Seed Robustness Battery [May 28]\n\n### 62. `eval_pi05_a1_30k_s2_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed2 30K — third seed to complete 3-seed statistical power; s0=58%, s1=58.5%, s2 determines final A/B/C scenario\n- **Metrics:** car=54.5%, tsr=54.5%\n- **Unique:** λ=0.1; seed 2; uses lowercase `car`/`tsr` keys; 3-seed mean ≈ 57%; confirms Scenario B/C boundary\n\n### 63. `eval_multiseed_lora_s0_eseed42`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=42 — tests whether LoRA CAR (~56.5% at eval_seed=7) is stable across eval seeds; part of 5-way battery\n- **Metrics:** avg_CAR=56.5%, avg_TSR=46%, n_episodes=50, eval_seed=42\n- **Unique:** 50-episode eval; eval_seed sweep; part of 5-way → 7-way battery\n\n### 64. `eval_multiseed_lora_s0_eseed123`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=123\n- **Metrics:** avg_CAR=53%, avg_TSR=50.5%, n_episodes=50, eval_seed=123\n- **Unique:** eval_seed=123; part of 5-way battery\n\n### 65. `eval_multiseed_sdf_l01_s0_eseed42`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=42 — tests whether SDF CAR (~58.0% at eval_seed=7) remains non-significant vs LoRA across eval seeds\n- **Metrics:** avg_CAR=59%, avg_TSR=52.5%, n_episodes=50, eval_seed=42\n- **Unique:** SDF λ=0.1; eval_seed=42; 5-way battery arm\n\n### 66. `eval_multiseed_sdf_l01_s0_eseed123`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=123\n- **Metrics:** avg_CAR=58.5%, avg_TSR=53.5%, n_episodes=50, eval_seed=123\n- **Unique:** SDF λ=0.1; eval_seed=123; 5-way battery arm\n\n### 67. `eval_multiseed_sdf_l01_s0_eseed256`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=256 — third SDF eval seed for symmetric 3v3 comparison vs LoRA\n- **Metrics:** avg_CAR=57%, avg_TSR=48%, n_episodes=50, eval_seed=256\n- **Unique:** eval_seed=256; symmetric 3v3 SDF vs LoRA comparison\n\n### 68. `eval_spatial_bowl_lora_ctrl_s0_v2`\n- **Hypothesis:** Re-evaluate LoRA-only control on safelibero_spatial with consistent eval pipeline — confirms SDF redundancy across scenes\n- **Metrics:** avg_CAR=12%, avg_TSR=49%, n_episodes=50, eval_seed=7\n- **Unique:** Corrected v2 pipeline for spatial_bowl; avg_CAR=12% (vs 15.5% in v1); confirms spatial_bowl pattern\n\n### 69. `eval_multiseed_lora_s0_eseed0`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=0 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=53%, avg_TSR=55.5%, n_episodes=50, eval_seed=0\n- **Unique:** eval_seed=0; extends battery to 7-way\n\n### 70. `eval_multiseed_lora_s0_eseed99`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=99 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=57.5%, avg_TSR=52%, n_episodes=50, eval_seed=99\n- **Unique:** eval_seed=99; 7-way battery complete for LoRA\n\n### 71. `eval_multiseed_sdf_l01_s0_eseed0`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=0 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=52.5%, avg_TSR=48.5%, n_episodes=50, eval_seed=0\n- **Unique:** SDF λ=0.01 (not λ=0.1); eval_seed=0; 7-way extension\n\n### 72. `eval_multiseed_sdf_l01_s0_eseed99`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=99 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=57%, avg_TSR=46.5%, n_episodes=50, eval_seed=99\n- **Unique:** SDF λ=0.01; eval_seed=99; 7-way battery complete for SDF\n\n---\n\n## Summary Table — Eval Experiments with Performance Metrics\n\n| exp_id | CAR (%) | TSR (%) | dfCAR (%) | n_ep | eval_seed | λ | seed | Scene |\n|--------|---------|---------|-----------|------|-----------|---|------|-------|\n| eval_pi05_safelibero_object_v11_s2 | 27.5 | 75.0 | — | 200 | 2 | — | 0 | object |\n| eval_pi05_safelibero_object_v11_s1 | 25.0 | 76.0 | — | 200 | 1 | — | 1 | object |\n| eval_pi05_a1_30k_s0_l005 | 50.0 | 5.5 | — | 200 | 0 | 0.005 | 0 | object |\n| eval_pi05_a1_30k_s0_l01 | 53.0 | 5.5 | — | 200 | 0 | 0.01 | 0 | object |\n| eval_pi05_a1_30k_s1_l005_v2 | 52.5 | 5.5 | — | 200 | 0 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s2_l005_v2 | 54.5 | 9.5 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_30k_s1_l01_v2 | 52.5 | 7.5 | — | 200 | 0 | 0.01 | 1 | object |\n| eval_pi05_a1_30k_s2_l01_v2 | 53.0 | 7.5 | — | 200 | 0 | 0.01 | 2 | object |\n| eval_pi05_a1_30k_s1_l005_v3 | 51.5 | 4.0 | — | 200 | 0 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s2_l005_v3 | 53.0 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_best_s0_l005 | 54.5 | 52.0 | — | 50 | 7 | 0.005 | 0 | object |\n| eval_pi05_a1_best_s2_l005_10k | 55.5 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_30k_s0_l005_r4 | 47.0 | 7.5 | — | 200 | 0 | 0.005 | 0 | object |\n| eval_pi05_a1_best_s1_l005_16k | 53.0 | 6.5 | — | 200 | 1 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s1_l005_disp | 54.0 | 4.0 | — | 200 | 1 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s0_l01_disp | 52.5 | 6.5 | — | 200 | 0 | 0.01 | 0 | object |\n| eval_lora_baseline_30k_s0_v2 | 54.5 | 8.5 | 54.5 | 200 | 0 | LoRA-only | 0 | object |\n| eval_lora_baseline_30k_s1_v2 | 56.0 | 4.0 | 56.0 | 200 | 1 | LoRA-only | 1 | object |\n| eval_lora_baseline_30k_s0_reeval | 56.5 | 51.5 | — | — | 7 | LoRA-only | 0 | object |\n| reeval_sdf_s0_l01_30k | 57.0 | 52.5 | — | 200 | 0 | 0.01 | 0 | object |\n| reeval_lora_s1_30k | 52.5 | 51.5 | — | 200 | 1 | LoRA-only | 1 | object |\n| reeval_sdf_s0_l005_30k | 57.0 | 55.5 | — | 200 | 0 | 0.005 | 0 | object |\n| reeval_sdf_s1_l005_30k | 54.0 | 50.5 | — | 200 | 1 | 0.005 | 1 | object |\n| reeval_sdf_s2_l005_30k | 52.5 | 56.0 | — | 200 | 2 | 0.005 | 2 | object |\n| reeval_sdf_s1_l01_30k | 57.5 | 55.5 | — | 200 | 1 | 0.01 | 1 | object |\n| reeval_sdf_s2_l01_30k | 54.5 | 53.5 | — | 200 | 2 | 0.01 | 2 | object |\n| reeval_lora_s0_30k_v2 | 57.0 | 46.0 | — | — | 7 | LoRA-only | 0 | object |\n| eval_stepwise_s0_l1_22k | 60.5 | 45.5 | — | — | 7 | 0.1 | 0 | object |\n| eval_stepwise_s0_l1_26k_v2 | 53.5 | 53.0 | 53.5 | — | 7 | 0.1 | 0 | object |\n| eval_pi05_a1_30k_s0_l01_high | 58.0 | 47.0 | 58.0 | — | 7 | 0.1 | 0 | object |\n| eval_pi05_a1_30k_s1_l01_high | 58.5 | 49.0 | 58.5 | — | 7 | 0.1 | 1 | object |\n| eval_lora_s2_30k_v2 | 55.0 | 51.5 | — | — | 7 | LoRA-only | 2 | object |\n| eval_spatial_bowl_lora_ctrl_s0 | 15.5 | 50.0 | — | — | 7 | LoRA-only | 0 | spatial |\n| eval_pi05_a1_30k_s2_l01_high | 54.5 | 54.5 | — | — | 7 | 0.1 | 2 | object |\n| eval_multiseed_lora_s0_eseed42 | 56.5 | 46.0 | — | 50 | 42 | LoRA-only | 0 | object |\n| eval_multiseed_lora_s0_eseed123 | 53.0 | 50.5 | — | 50 | 123 | LoRA-only | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed42 | 59.0 | 52.5 | — | 50 | 42 | 0.1 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed123 | 58.5 | 53.5 | — | 50 | 123 | 0.1 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed256 | 57.0 | 48.0 | — | 50 | 256 | 0.1 | 0 | object |\n| eval_spatial_bowl_lora_ctrl_s0_v2 | 12.0 | 49.0 | — | 50 | 7 | LoRA-only | 0 | spatial |\n| eval_multiseed_lora_s0_eseed0 | 53.0 | 55.5 | — | 50 | 0 | LoRA-only | 0 | object |\n| eval_multiseed_lora_s0_eseed99 | 57.5 | 52.0 | — | 50 | 99 | LoRA-only | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed0 | 52.5 | 48.5 | — | 50 | 0 | 0.01 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed99 | 57.0 | 46.5 | — | 50 | 99 | 0.01 | 0 | object |\n\n---\n\n## Key Findings Across All 72 Experiments\n\n1. **All 72 experiments have `conclusion=success`** — no failures in registry.\n2. **Eval bug (180° image rotation):** Early evals (Groups 3–4) showed TSR ~4–10%, later corrected by rotation fix which recovered TSR to ~50–56%.\n3. **SDF redundancy (Scenario B/C):** After rotation fix, CAR for SDF-augmented models (λ=0.005/0.01/0.1) is ~52–58%, indistinguishable from LoRA-only baseline (~52–57%). This is the central finding.\n4. **dfCAR metric:** Introduced in Group 6 to filter action-collapse episodes. For all rotation-fixed evals, frozen_rate=0 and dfCAR=CAR (no collapsed episodes exist).\n5. **dfCAR threshold sensitivity:** Perfectly invariant across τ_d ∈ [2, 200] mm for all 8 model-seed combinations (`analysis_threshold_sensitivity`).\n6. **Multi-eval-seed battery:** 7 eval seeds tested for both LoRA-only and SDF λ=0.01/0.1; SDF CAR consistently overlaps LoRA CAR range across all seeds.\n7. **Spatial bowl scene:** LoRA-only CAR=12–15.5%, much lower than object_pudding (~54–57%), indicating scene-specific difficulty.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
    "content": "# Registry Success Experiments — Complete Summary\n\nAll 72 experiments have `conclusion=success`. Sorted by `created_at`.\n\n---\n\n## Group 1 — Early Baselines (pi0 full-FT, pi0+LoRA, A3 gradient refine) [May 19–21]\n\n### 1. `baseline_spatial_bowl_s0_v2`\n- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison\n- **Metrics:** best_loss=0.00316, final_loss=0.0032, steps_completed=30000\n- **Unique:** Full-FT (no LoRA) pi0 base; spatial_bowl scene; reference baseline\n\n### 2. `baseline_object_pudding_s0_v2`\n- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%\n- **Metrics:** final_loss=0.005, steps_completed=30000\n- **Unique:** Full-FT (no LoRA) pi0 base; object_pudding scene; reference baseline\n\n### 3. `a3_gradient_spatial_bowl_s0`\n- **Hypothesis:** SDF gradient-guided action refinement during training (A3) on spatial_bowl Level II — expects CAR improvement over baseline with TSR drop <10%; comparable to AEGIS (CAR 86%, TSR 88%)\n- **Metrics:** best_loss=0.01552, steps_completed=30000\n- **Unique:** A3 architecture (SDF gradient loss at train time); spatial_bowl scene\n\n### 4. `a3_gradient_object_pudding_s0`\n- **Hypothesis:** SDF gradient-guided action refinement (A3) on object_pudding Level I — comparable to AEGIS (CAR 32%, TSR 92%)\n- **Metrics:** best_loss=0.01439, final_loss=0.01898, steps_completed=30000\n- **Unique:** A3 architecture; object_pudding scene; model `pi0+A3_gradient_refine`\n\n### 5. `baseline_lora_spatial_bowl_s0`\n- **Hypothesis:** LoRA fine-tuned pi0 baseline on spatial_bowl (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3\n- **Metrics:** best_loss=0.00876, steps_completed=30000\n- **Unique:** LoRA baseline (no collision loss); spatial_bowl; parameter-matched reference for A3\n\n### 6. `baseline_lora_object_pudding_s0`\n- **Hypothesis:** LoRA fine-tuned pi0 baseline on object_pudding (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3\n- **Metrics:** best_loss=0.0124, steps_completed=30000\n- **Unique:** LoRA baseline (no collision loss); object_pudding; parameter-matched reference for A3\n\n### 7. `a1_lora_object_pudding_s0`\n- **Hypothesis:** A1 SDF auxiliary task with LoRA injection (rank 16/32) on object_pudding — Phase 1 SDF warmup (frozen LoRA), Phase 2 joint training; expects CAR improvement over LoRA baseline with TSR drop <10%\n- **Metrics:** best_loss=0.01326, final_loss=0.0184, steps_completed=30000\n- **Unique:** A1 architecture; two-phase training (SDF warmup then joint); model `pi0+LoRA+SDF_aux`\n\n### 8. `a1_lora_spatial_bowl_s0`\n- **Hypothesis:** A1 SDF auxiliary task with LoRA injection on spatial_bowl — Phase 1 SDF warmup, Phase 2 joint; expects CAR improvement over LoRA baseline with TSR drop <10%\n- **Metrics:** best_loss=0.01431, steps_completed=30000\n- **Unique:** A1 architecture on spatial_bowl scene\n\n---\n\n## Group 2 — Pi0.5 Baselines and Initial A1 Diagnosis [May 22]\n\n### 9. `eval_a1_lora_object_v11`\n- **Hypothesis:** A1 (SDF auxiliary loss + LoRA, no runtime refinement) eval on safelibero_object — tests whether SDF auxiliary training signal alone improves CAR over LoRA baseline\n- **Metrics:** TSR=0, n_episodes=200, displacement_avg=0.0027\n- **Unique:** First A1 eval; TSR=0 flagged action collapse; critical diagnostic\n\n### 10. `eval_pi05_safelibero_object_v11_s2`\n- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 2): confirm CAR=28% is stable across seeds\n- **Metrics:** CAR=27.5%, TSR=75.0%, mean_displacement=0.132\n- **Unique:** Pi0.5 pretrained checkpoint (no fine-tune); seed 2 replication\n\n### 11. `eval_pi05_safelibero_object_v11_s1`\n- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 1): confirm CAR=28% is stable\n- **Metrics:** CAR=25.0%, TSR=76.0%, mean_displacement=0.153\n- **Unique:** Pi0.5 pretrained checkpoint; seed 1 replication\n\n---\n\n## Group 3 — Pi0.5+A1 Training Sweep (3 seeds × 2 lambdas) [May 23–24]\n\n### 12. `train_pi05_a1_obj_s0_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 0 — restarted after P0 checkpoint collision fix; tests whether stronger SDF signal produces real collision avoidance or action collapse\n- **Metrics:** best_loss=0.00801, steps_completed=30000\n- **Unique:** Pi0.5 backbone; λ=0.01; seed 0; restart after checkpoint fix\n\n### 13. `train_pi05_a1_obj_s0_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 0 — conservative SDF signal\n- **Metrics:** best_loss=0.007861, steps_completed=30000\n- **Unique:** Pi0.5 backbone; λ=0.005; seed 0\n\n### 14. `train_pi05_a1_obj_s1_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 1 — multi-seed replication of conservative lambda\n- **Metrics:** best_loss=0.01143, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.005; seed 1\n\n### 15. `train_pi05_a1_obj_s1_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 1 — multi-seed replication of stronger lambda\n- **Metrics:** best_loss=0.01168, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.01; seed 1\n\n### 16. `train_pi05_a1_obj_s2_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 2 — third seed for statistical significance\n- **Metrics:** best_loss=0.00874, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.005; seed 2\n\n### 17. `train_pi05_a1_obj_s2_l01`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 2 — third seed for statistical significance of higher SDF signal\n- **Metrics:** best_loss=0.00911, steps_completed=30000\n- **Unique:** Pi0.5; λ=0.01; seed 2\n\n### 18. `train_pi05_lora_baseline_s0`\n- **Hypothesis:** LoRA baseline (no SDF) on object_pudding 30K steps — attribution control; if CAR ≈ Pi0.5 baseline (~27%), confirms ColliForce improvement is from SDF not LoRA\n- **Metrics:** best_loss=0.01025, final_loss=0.01343, best_step=24000\n- **Unique:** Pi0.5+LoRA-only control; seed 0; Claim 4 SDF attribution\n\n### 19. `train_pi05_lora_baseline_s1`\n- **Hypothesis:** LoRA baseline (no SDF) seed 1 on object_pudding — second seed for LoRA-only attribution control\n- **Metrics:** best_loss=0.0113, final_loss=0.01408, best_step=14000\n- **Unique:** Pi0.5+LoRA-only control; seed 1\n\n---\n\n## Group 4 — 30K Eval Matrix (3 seeds × 2 lambdas) [May 25]\n\n### 20. `eval_pi05_a1_30k_s0_l005`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.005): completes 3-seed coverage for conservative lambda\n- **Metrics:** avg_CAR=50%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=42%, task2_CAR=86%, task3_CAR=14%, task0_TSR=2%, task1_TSR=20%, n_episodes=200\n- **Unique:** First corrected eval with fixed checkpoint path; low TSR (old eval bug later discovered)\n\n### 21. `eval_pi05_a1_30k_s0_l01`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.01): completes 3-seed coverage for stronger lambda\n- **Metrics:** avg_CAR=53%, avg_TSR=5.5%, task0_CAR=68%, task1_CAR=46%, task2_CAR=86%, task3_CAR=12%, task0_TSR=2%, task1_TSR=20%, n_episodes=200 (note: old script, no max_ee_displacement)\n- **Unique:** λ=0.01; note flags old script version\n\n### 22. `train_pi05_a1_spatial_bowl_s0_l005`\n- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss on spatial_bowl (λ=0.005, seed 0) — tests cross-scene generalization; bilateral obstacles\n- **Metrics:** best_loss=0.01063, final_loss=0.0137, best_step=28000\n- **Unique:** Cross-scene generalization to spatial_bowl; bilateral obstacle geometry\n\n### 23. `eval_pi05_a1_30k_s1_l005_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) corrected re-run with verified 30K checkpoint path\n- **Metrics:** avg_CAR=52.5%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=40%, task2_CAR=94%, task3_CAR=18%, n_episodes=200\n- **Unique:** v2 correction of checkpoint path bug; seed 1\n\n### 24. `eval_pi05_a1_30k_s2_l005_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) corrected re-run — third seed for statistical significance\n- **Metrics:** avg_CAR=54.5%, avg_TSR=9.5%, task0_CAR=62%, task1_CAR=44%, task2_CAR=90%, task3_CAR=22%, n_episodes=200\n- **Unique:** Third seed; corrected checkpoint path\n\n### 25. `eval_pi05_a1_30k_s1_l01_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.01) corrected re-run with lora_baseline model type\n- **Metrics:** avg_CAR=52.5%, avg_TSR=7.5%, task0_CAR=54%, task1_CAR=48%, task2_CAR=94%, task3_CAR=14%, n_episodes=200\n- **Unique:** λ=0.01; corrected model_type parameter; seed 1\n\n### 26. `eval_pi05_a1_30k_s2_l01_v2`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.01) — completes the 3-seed × 2-lambda eval matrix\n- **Metrics:** avg_CAR=53%, avg_TSR=7.5%, task0_CAR=62%, task1_CAR=42%, task2_CAR=88%, task3_CAR=20%, n_episodes=200\n- **Unique:** Completes the full 3×2 matrix; seed 2; λ=0.01\n\n### 27. `eval_pi05_a1_30k_s1_l005_v3`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) rerun with correct --output_path to preserve per-episode displacement data (v2 JSON was overwritten by concurrent evals)\n- **Metrics:** avg_CAR=51.5%, avg_TSR=4%, task0_CAR=54%, task1_CAR=48%, task2_CAR=88%, task3_CAR=16%, n_episodes=200\n- **Unique:** v3 fix for output path collision; first eval with displacement data preserved\n\n### 28. `eval_pi05_a1_30k_s2_l005_v3`\n- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) rerun with correct --output_path; v2 JSON was overwritten\n- **Metrics:** avg_CAR=53%, avg_TSR=9%, task0_CAR=60%, task1_CAR=46%, task2_CAR=86%, task3_CAR=20%, n_episodes=200\n- **Unique:** v3 fix; seed 2; displacement data preserved\n\n### 29. `eval_pi05_a1_best_s0_l005`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed0, λ=0.005) at best-loss checkpoint (step 26000) — completes 3-seed best-checkpoint coverage\n- **Metrics:** avg_CAR=54.5%, avg_TSR=52%, task0_CAR=50%, task1_CAR=74%, task2_CAR=68%, task3_CAR=26%, n_episodes=50, eval_seed=7, collision_threshold=0.001\n- **Unique:** Best-loss checkpoint (step 26000) not final; task-level breakdown; eval_seed=7\n\n### 30. `eval_pi05_a1_best_s2_l005_10k`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed2, λ=0.005, step 10K) — evaluates the sweet-spot checkpoint before action collapse\n- **Metrics:** avg_CAR=55.5%, avg_TSR=9%, task0_CAR=68%, task1_CAR=44%, task2_CAR=92%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0; analysis: \"ALL episodes have high EE displacement (0.39–0.58m). Zero fake safety. 10K best shows genuine collision avoidance.\"\n- **Unique:** Pre-collapse checkpoint; zero fake-safe episodes; analysis confirms genuine avoidance\n\n### 31. `eval_pi05_a1_30k_s0_l005_r4`\n- **Hypothesis:** Pi0.5+A1 30K eval retry (seed0, λ=0.005) — re-run with fixed eval script to get displacement data\n- **Metrics:** avg_CAR=47%, avg_TSR=7.5%, task0_CAR=58%, task1_CAR=38%, task2_CAR=76%, task3_CAR=16%, n_episodes=200 (note: old script, no max_ee_displacement)\n- **Unique:** Retry with fixed script; old script note still present; seed 0\n\n### 32. `eval_pi05_a1_best_s1_l005_16k`\n- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed1, λ=0.005, step 16000) — best-loss checkpoint vs 30K final\n- **Metrics:** avg_CAR=53%, avg_TSR=6.5%, task0_CAR=58%, task1_CAR=50%, task2_CAR=88%, task3_CAR=16%, n_episodes=200, fake_safe_pct=0\n- **Unique:** Best-loss checkpoint at step 16K; zero fake-safe episodes\n\n### 33. `eval_pi05_a1_30k_s1_l005_disp`\n- **Hypothesis:** Displacement fix verification — rerun s1_l005_30k eval to confirm max_ee_displacement field is correctly output\n- **Metrics:** avg_CAR=54%, avg_TSR=4%, task0_CAR=54%, task1_CAR=58%, task2_CAR=92%, task3_CAR=12%, n_episodes=200, fake_safe_pct=0\n- **Unique:** Explicitly validates displacement field fix; zero fake-safe\n\n### 34. `eval_pi05_a1_30k_s0_l01_disp`\n- **Hypothesis:** Pi0.5+A1 30K displacement eval (seed0, λ=0.01) — re-run with fixed eval script to get max_ee_displacement; tests for 30K action collapse\n- **Metrics:** avg_CAR=52.5%, avg_TSR=6.5%, task0_CAR=76%, task1_CAR=32%, task2_CAR=84%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0\n- **Unique:** λ=0.01; displacement-aware eval; zero fake-safe\n\n---\n\n## Group 5 — Phase 2 Ablation, High-Lambda Training [May 25–26]\n\n### 35. `train_pi05_phase2_lambda0_s2`\n- **Hypothesis:** Phase 2 λ=0 ablation (seed2): resume from seed2 l005 best (10K) checkpoint with SDF loss disabled — tests whether early SDF-encoded collision awareness persists in LoRA weights\n- **Metrics:** best_loss=0.00651, best_step=4000\n- **Unique:** Ablation of SDF loss after warmup; resume from 10K; seed 2; tests LoRA weight retention\n\n### 36. `train_pi05_a1_obj_s0_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed0, 30K) — tests faster collision avoidance learning vs earlier over-avoidance onset\n- **Metrics:** (empty — training only)\n- **Unique:** High lambda=0.1; seed 0; paired with seed 1 for error bars\n\n### 37. `train_pi05_a1_obj_s1_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed1, 30K) — second seed for lambda=0.1 error bars\n- **Metrics:** (empty — training only)\n- **Unique:** High lambda=0.1; seed 1\n\n---\n\n## Group 6 — Rotation Fix Re-evals (LoRA Baseline) [May 26]\n\n### 38. `eval_lora_baseline_30k_s0_v2`\n- **Hypothesis:** LoRA baseline (no SDF) 30K eval on object_pudding seed 0 (v2, base env fix) — expects CAR ≈ Pi0.5 baseline (~27%); critical for Claim 4 SDF attribution\n- **Metrics:** avg_CAR=54.5%, avg_TSR=8.5%, dfCAR_100mm=54.5%, n_episodes=200, frozen_pct=0\n- **Unique:** Surprising high CAR~54.5% (vs expected ~27%); dfCAR_100mm introduced; first dfCAR datapoint\n\n### 39. `eval_lora_baseline_30k_s1_v2`\n- **Hypothesis:** LoRA baseline (no SDF) 30K eval seed 1 (v2, base env fix) — second seed for LoRA-only attribution\n- **Metrics:** avg_CAR=56%, avg_TSR=4%, dfCAR_100mm=56%, n_episodes=200, frozen_pct=0\n- **Unique:** Consistently high LoRA CAR; challenges SDF attribution claim; dfCAR_100mm\n\n### 40. `eval_pi05_baseline_reeval_disp`\n- **Hypothesis:** Pi0.5 base model (no LoRA, no SDF) re-eval with fixed eval script on object_pudding 200ep — obtain EE displacement data for dfCAR baseline comparison\n- **Metrics:** (empty — results pending or logged elsewhere)\n- **Unique:** Raw pi0.5 model re-eval; displacement data for dfCAR analysis\n\n### 41. `eval_lora_baseline_30k_s0_reeval`\n- **Hypothesis:** Re-eval LoRA-only s0 (30K) with fixed eval_safelibero.py (180° image rotation added) — if TSR remains ~6–8%, catastrophic forgetting is real; if TSR >30%, eval bug artifact\n- **Metrics:** CAR=56.5%, TSR=51.5%\n- **Unique:** Critical rotation fix applied; TSR jumped from ~8% to 51.5%, confirming earlier TSR collapse was eval bug\n\n---\n\n## Group 7 — Full Re-eval Batch with Rotation Fix (SDF + LoRA) [May 26]\n\n### 42. `reeval_sdf_s0_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s0 (30K) with fixed eval_safelibero.py (180° rotation) — verify TSR collapse is real or eval bug\n- **Metrics:** car=57%, tsr=52.5%, fake_safe_rate_ee=0, frozen_rate_ee=0, frozen_rate_obs=55.5%\n- **Unique:** First corrected SDF re-eval; frozen_rate_obs=55.5% (obstacle motionless, NOT fake safety); note distinguishes paper definition vs script definition\n\n### 43. `reeval_lora_s1_30k`\n- **Hypothesis:** Re-eval LoRA-only s1 (30K) with fixed eval — second seed for LoRA-only attribution baseline; expected TSR ~50%\n- **Metrics:** car=52.5%, tsr=51.5%, fake_safe_rate_ee=0, frozen_rate_ee=0\n- **Unique:** LoRA-only seed 1; confirms rotation fix recovers TSR\n\n### 44. `reeval_sdf_s0_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s0 (30K) with rotation fix — corrected SDF attribution data\n- **Metrics:** car=57%, tsr=55.5%, fake_safe_rate_ee=0, frozen_rate_ee=0\n- **Unique:** λ=0.005; seed 0; corrected\n\n### 45. `reeval_sdf_s1_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s1 (30K) with rotation fix\n- **Metrics:** CAR=54%, TSR=50.5%\n- **Unique:** λ=0.005; seed 1; corrected\n\n### 46. `reeval_sdf_s2_l005_30k`\n- **Hypothesis:** Re-eval SDF λ=0.005 s2 (30K) with rotation fix — third seed for λ=0.005\n- **Metrics:** CAR=52.5%, TSR=56%\n- **Unique:** λ=0.005; seed 2; corrected\n\n### 47. `reeval_sdf_s1_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s1 (30K) with rotation fix — second seed for λ=0.01\n- **Metrics:** CAR=57.5%, TSR=55.5%\n- **Unique:** λ=0.01; seed 1; corrected\n\n### 48. `reeval_sdf_s2_l01_30k`\n- **Hypothesis:** Re-eval SDF λ=0.01 s2 (30K) with rotation fix — third seed for λ=0.01\n- **Metrics:** CAR=54.5%, TSR=53.5%\n- **Unique:** λ=0.01; seed 2; corrected; completes 3-seed λ=0.01 re-eval\n\n---\n\n## Group 8 — Phase 2 λ=0 Eval, LoRA Spatial Bowl, Reeval s0, High-Lambda Training [May 26]\n\n### 49. `eval_phase2_lambda0_s2`\n- **Hypothesis:** Phase 2 LoRA unfrozen training with λ=0 (no SDF loss) seed 2 should achieve baseline-level TSR on safelibero_object — control for SDF-augmented models\n- **Metrics:** (empty — eval results not recorded in metrics field)\n- **Unique:** Phase 2 ablation control; λ=0; tests task retention after SDF warmup removed\n\n### 50. `train_spatial_bowl_lora_control_s0`\n- **Hypothesis:** LoRA-only baseline (without SDF collision loss) on spatial_bowl — safety-violation rate should remain high at pre-training level, establishing the gap SDF training aims to close\n- **Metrics:** (empty — training only)\n- **Unique:** LoRA control for spatial_bowl scene; establishes control arm for cross-scene generalization\n\n### 51. `reeval_lora_s0_30k_v2`\n- **Hypothesis:** Re-eval LoRA-only s0 30K with confirmed rotation-fixed script (seed=7) — previous reeval was from buggy version; second reliable LoRA-only seed for Claim 3 mean±std\n- **Metrics:** CAR=57%, TSR=46%\n- **Unique:** Uses eval_seed=7; explicit confirmation of rotation fix; second reliable LoRA seed\n\n### 52. `train_pi05_a1_obj_s2_l01_high`\n- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed2, 30K) — third seed for 3-seed statistical power for A/B/C scenario determination\n- **Metrics:** best_loss=0.0104, final_loss=0.0104, best_step=30000\n- **Unique:** High lambda=0.1; seed 2; third seed; final checkpoint = best checkpoint (no early plateau)\n\n---\n\n## Group 9 — dfCAR Analysis, Stepwise Eval, LoRA Baseline Seed 2 [May 26–27]\n\n### 53. `analysis_threshold_sensitivity`\n- **Hypothesis:** dfCAR threshold τ_d is robust across [2, 200] mm — bimodal displacement gap (collapsed <0.1mm vs active >270mm) means any threshold in this range produces identical dfCAR values\n- **Metrics:** dfCAR_stable_range_mm=\"[2, 200]\", n_models=8, max_dfCAR_variation_2_to_200mm=0, n_active_equals_n_total_at_200mm=true; conclusion: \"dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold\"\n- **Unique:** Analysis experiment (no training/eval); validates dfCAR metric robustness; uses threshold_sensitivity_v2.csv; 8 models tested\n\n### 54. `eval_stepwise_s0_l1_22k`\n- **Hypothesis:** Step-wise eval of Pi0.5+A1 SDF λ=0.1 (seed 0) at 22K checkpoint — third point in step-wise CAR curve (16K: 55.5%, 20K: 55%, 22K: this)\n- **Metrics:** CAR=60.5%, TSR=45.5%, eval_seed=7, frozen_pct=0\n- **Unique:** Step-wise curve point at 22K; λ=0.1; peak CAR in curve\n\n### 55. `train_pi05_lora_baseline_s2_resume`\n- **Hypothesis:** Resume LoRA baseline seed2 training from checkpoint 22000 to 30000 — original run killed by 24h tmux timeout at step 22364\n- **Metrics:** final_loss=0.0117\n- **Unique:** Resume from tmux-killed checkpoint; seed 2; enables 3v3 statistical comparison\n\n### 56. `eval_stepwise_s0_l1_26k_v2`\n- **Hypothesis:** The 24K frozen episodes (29.5%) were caused by missing --pi05 flag in eval, not SDF training degradation; re-running 26K eval with --pi05 should eliminate frozen episodes\n- **Metrics:** CAR=53.5%, TSR=53%, dfCAR=53.5%, frozen_rate=0\n- **Unique:** Diagnoses eval bug (missing --pi05 flag); dfCAR introduced; frozen_rate corrected to 0\n\n---\n\n## Group 10 — High-Lambda (λ=0.1) 3-Seed Eval, LoRA Seed 2 Eval, Spatial Bowl Control [May 27–28]\n\n### 57. `eval_pi05_a1_30k_s0_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed0 30K checkpoint — based on stepwise curve (16K–28K CAR ~52.5–60.5%, mean ~55.1%), expects Scenario B (CAR ≤ 57%, SDF redundant)\n- **Metrics:** CAR=58%, TSR=47%, dfCAR=58%, frozen_rate=0\n- **Unique:** λ=0.1; seed 0; 30K; dfCAR=CAR (zero frozen); A/B/C scenario determination\n\n### 58. `eval_pi05_a1_30k_s1_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed1 30K — combined with s0 CAR=58.0% determines A/B/C scenario\n- **Metrics:** CAR=58.5%, TSR=49%, dfCAR=58.5%, frozen_rate=0\n- **Unique:** λ=0.1; seed 1; dfCAR=CAR; seeds 0+1 both at ~58% → Scenario C gray zone\n\n### 59. `train_phase2_lambda0_extra_seed`\n- **Hypothesis:** Phase 2 Stage 1 with seed0 and λ_sdf=0.005 for 10K steps — viable checkpoint for Stage 2 lambda-0 training on object_pudding\n- **Metrics:** (empty — training only)\n- **Unique:** Extra seed for Phase 2 ablation; seed 0; 10K stage 1\n\n### 60. `eval_lora_s2_30k_v2`\n- **Hypothesis:** LoRA baseline seed2 at 30K steps — establishes 3-seed null distribution variance for statistical comparison with SDF-augmented models\n- **Metrics:** overall_CAR=55%, overall_TSR=51.5%\n- **Unique:** Uses `overall_CAR`/`overall_TSR` key names; seed 2; completes 3-seed LoRA null distribution\n\n### 61. `eval_spatial_bowl_lora_ctrl_s0`\n- **Hypothesis:** LoRA baseline (no SDF) on spatial_bowl at 30K steps — high TSR but low CAR, confirming collision avoidance requires explicit SDF training signal\n- **Metrics:** avg_CAR=15.5%, avg_TSR=50%; note: \"v1 old pipeline, superseded by v2\"\n- **Unique:** spatial_bowl scene; LoRA control arm; CAR=15.5% vs object_pudding ~56%; note flags pipeline issue\n\n---\n\n## Group 11 — λ=0.1 Seed 2 Eval, Multi-Eval-Seed Robustness Battery [May 28]\n\n### 62. `eval_pi05_a1_30k_s2_l01_high`\n- **Hypothesis:** Evaluate λ=0.1 seed2 30K — third seed to complete 3-seed statistical power; s0=58%, s1=58.5%, s2 determines final A/B/C scenario\n- **Metrics:** car=54.5%, tsr=54.5%\n- **Unique:** λ=0.1; seed 2; uses lowercase `car`/`tsr` keys; 3-seed mean ≈ 57%; confirms Scenario B/C boundary\n\n### 63. `eval_multiseed_lora_s0_eseed42`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=42 — tests whether LoRA CAR (~56.5% at eval_seed=7) is stable across eval seeds; part of 5-way battery\n- **Metrics:** avg_CAR=56.5%, avg_TSR=46%, n_episodes=50, eval_seed=42\n- **Unique:** 50-episode eval; eval_seed sweep; part of 5-way → 7-way battery\n\n### 64. `eval_multiseed_lora_s0_eseed123`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=123\n- **Metrics:** avg_CAR=53%, avg_TSR=50.5%, n_episodes=50, eval_seed=123\n- **Unique:** eval_seed=123; part of 5-way battery\n\n### 65. `eval_multiseed_sdf_l01_s0_eseed42`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=42 — tests whether SDF CAR (~58.0% at eval_seed=7) remains non-significant vs LoRA across eval seeds\n- **Metrics:** avg_CAR=59%, avg_TSR=52.5%, n_episodes=50, eval_seed=42\n- **Unique:** SDF λ=0.1; eval_seed=42; 5-way battery arm\n\n### 66. `eval_multiseed_sdf_l01_s0_eseed123`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=123\n- **Metrics:** avg_CAR=58.5%, avg_TSR=53.5%, n_episodes=50, eval_seed=123\n- **Unique:** SDF λ=0.1; eval_seed=123; 5-way battery arm\n\n### 67. `eval_multiseed_sdf_l01_s0_eseed256`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=256 — third SDF eval seed for symmetric 3v3 comparison vs LoRA\n- **Metrics:** avg_CAR=57%, avg_TSR=48%, n_episodes=50, eval_seed=256\n- **Unique:** eval_seed=256; symmetric 3v3 SDF vs LoRA comparison\n\n### 68. `eval_spatial_bowl_lora_ctrl_s0_v2`\n- **Hypothesis:** Re-evaluate LoRA-only control on safelibero_spatial with consistent eval pipeline — confirms SDF redundancy across scenes\n- **Metrics:** avg_CAR=12%, avg_TSR=49%, n_episodes=50, eval_seed=7\n- **Unique:** Corrected v2 pipeline for spatial_bowl; avg_CAR=12% (vs 15.5% in v1); confirms spatial_bowl pattern\n\n### 69. `eval_multiseed_lora_s0_eseed0`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=0 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=53%, avg_TSR=55.5%, n_episodes=50, eval_seed=0\n- **Unique:** eval_seed=0; extends battery to 7-way\n\n### 70. `eval_multiseed_lora_s0_eseed99`\n- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=99 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=57.5%, avg_TSR=52%, n_episodes=50, eval_seed=99\n- **Unique:** eval_seed=99; 7-way battery complete for LoRA\n\n### 71. `eval_multiseed_sdf_l01_s0_eseed0`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=0 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=52.5%, avg_TSR=48.5%, n_episodes=50, eval_seed=0\n- **Unique:** SDF λ=0.01 (not λ=0.1); eval_seed=0; 7-way extension\n\n### 72. `eval_multiseed_sdf_l01_s0_eseed99`\n- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=99 — extends 5-way battery to 7-way\n- **Metrics:** avg_CAR=57%, avg_TSR=46.5%, n_episodes=50, eval_seed=99\n- **Unique:** SDF λ=0.01; eval_seed=99; 7-way battery complete for SDF\n\n---\n\n## Summary Table — Eval Experiments with Performance Metrics\n\n| exp_id | CAR (%) | TSR (%) | dfCAR (%) | n_ep | eval_seed | λ | seed | Scene |\n|--------|---------|---------|-----------|------|-----------|---|------|-------|\n| eval_pi05_safelibero_object_v11_s2 | 27.5 | 75.0 | — | 200 | 2 | — | 0 | object |\n| eval_pi05_safelibero_object_v11_s1 | 25.0 | 76.0 | — | 200 | 1 | — | 1 | object |\n| eval_pi05_a1_30k_s0_l005 | 50.0 | 5.5 | — | 200 | 0 | 0.005 | 0 | object |\n| eval_pi05_a1_30k_s0_l01 | 53.0 | 5.5 | — | 200 | 0 | 0.01 | 0 | object |\n| eval_pi05_a1_30k_s1_l005_v2 | 52.5 | 5.5 | — | 200 | 0 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s2_l005_v2 | 54.5 | 9.5 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_30k_s1_l01_v2 | 52.5 | 7.5 | — | 200 | 0 | 0.01 | 1 | object |\n| eval_pi05_a1_30k_s2_l01_v2 | 53.0 | 7.5 | — | 200 | 0 | 0.01 | 2 | object |\n| eval_pi05_a1_30k_s1_l005_v3 | 51.5 | 4.0 | — | 200 | 0 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s2_l005_v3 | 53.0 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_best_s0_l005 | 54.5 | 52.0 | — | 50 | 7 | 0.005 | 0 | object |\n| eval_pi05_a1_best_s2_l005_10k | 55.5 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |\n| eval_pi05_a1_30k_s0_l005_r4 | 47.0 | 7.5 | — | 200 | 0 | 0.005 | 0 | object |\n| eval_pi05_a1_best_s1_l005_16k | 53.0 | 6.5 | — | 200 | 1 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s1_l005_disp | 54.0 | 4.0 | — | 200 | 1 | 0.005 | 1 | object |\n| eval_pi05_a1_30k_s0_l01_disp | 52.5 | 6.5 | — | 200 | 0 | 0.01 | 0 | object |\n| eval_lora_baseline_30k_s0_v2 | 54.5 | 8.5 | 54.5 | 200 | 0 | LoRA-only | 0 | object |\n| eval_lora_baseline_30k_s1_v2 | 56.0 | 4.0 | 56.0 | 200 | 1 | LoRA-only | 1 | object |\n| eval_lora_baseline_30k_s0_reeval | 56.5 | 51.5 | — | — | 7 | LoRA-only | 0 | object |\n| reeval_sdf_s0_l01_30k | 57.0 | 52.5 | — | 200 | 0 | 0.01 | 0 | object |\n| reeval_lora_s1_30k | 52.5 | 51.5 | — | 200 | 1 | LoRA-only | 1 | object |\n| reeval_sdf_s0_l005_30k | 57.0 | 55.5 | — | 200 | 0 | 0.005 | 0 | object |\n| reeval_sdf_s1_l005_30k | 54.0 | 50.5 | — | 200 | 1 | 0.005 | 1 | object |\n| reeval_sdf_s2_l005_30k | 52.5 | 56.0 | — | 200 | 2 | 0.005 | 2 | object |\n| reeval_sdf_s1_l01_30k | 57.5 | 55.5 | — | 200 | 1 | 0.01 | 1 | object |\n| reeval_sdf_s2_l01_30k | 54.5 | 53.5 | — | 200 | 2 | 0.01 | 2 | object |\n| reeval_lora_s0_30k_v2 | 57.0 | 46.0 | — | — | 7 | LoRA-only | 0 | object |\n| eval_stepwise_s0_l1_22k | 60.5 | 45.5 | — | — | 7 | 0.1 | 0 | object |\n| eval_stepwise_s0_l1_26k_v2 | 53.5 | 53.0 | 53.5 | — | 7 | 0.1 | 0 | object |\n| eval_pi05_a1_30k_s0_l01_high | 58.0 | 47.0 | 58.0 | — | 7 | 0.1 | 0 | object |\n| eval_pi05_a1_30k_s1_l01_high | 58.5 | 49.0 | 58.5 | — | 7 | 0.1 | 1 | object |\n| eval_lora_s2_30k_v2 | 55.0 | 51.5 | — | — | 7 | LoRA-only | 2 | object |\n| eval_spatial_bowl_lora_ctrl_s0 | 15.5 | 50.0 | — | — | 7 | LoRA-only | 0 | spatial |\n| eval_pi05_a1_30k_s2_l01_high | 54.5 | 54.5 | — | — | 7 | 0.1 | 2 | object |\n| eval_multiseed_lora_s0_eseed42 | 56.5 | 46.0 | — | 50 | 42 | LoRA-only | 0 | object |\n| eval_multiseed_lora_s0_eseed123 | 53.0 | 50.5 | — | 50 | 123 | LoRA-only | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed42 | 59.0 | 52.5 | — | 50 | 42 | 0.1 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed123 | 58.5 | 53.5 | — | 50 | 123 | 0.1 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed256 | 57.0 | 48.0 | — | 50 | 256 | 0.1 | 0 | object |\n| eval_spatial_bowl_lora_ctrl_s0_v2 | 12.0 | 49.0 | — | 50 | 7 | LoRA-only | 0 | spatial |\n| eval_multiseed_lora_s0_eseed0 | 53.0 | 55.5 | — | 50 | 0 | LoRA-only | 0 | object |\n| eval_multiseed_lora_s0_eseed99 | 57.5 | 52.0 | — | 50 | 99 | LoRA-only | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed0 | 52.5 | 48.5 | — | 50 | 0 | 0.01 | 0 | object |\n| eval_multiseed_sdf_l01_s0_eseed99 | 57.0 | 46.5 | — | 50 | 99 | 0.01 | 0 | object |\n\n---\n\n## Key Findings Across All 72 Experiments\n\n1. **All 72 experiments have `conclusion=success`** — no failures in registry.\n2. **Eval bug (180° image rotation):** Early evals (Groups 3–4) showed TSR ~4–10%, later corrected by rotation fix which recovered TSR to ~50–56%.\n3. **SDF redundancy (Scenario B/C):** After rotation fix, CAR for SDF-augmented models (λ=0.005/0.01/0.1) is ~52–58%, indistinguishable from LoRA-only baseline (~52–57%). This is the central finding.\n4. **dfCAR metric:** Introduced in Group 6 to filter action-collapse episodes. For all rotation-fixed evals, frozen_rate=0 and dfCAR=CAR (no collapsed episodes exist).\n5. **dfCAR threshold sensitivity:** Perfectly invariant across τ_d ∈ [2, 200] mm for all 8 model-seed combinations (`analysis_threshold_sensitivity`).\n6. **Multi-eval-seed battery:** 7 eval seeds tested for both LoRA-only and SDF λ=0.01/0.1; SDF CAR consistently overlaps LoRA CAR range across all seeds.\n7. **Spatial bowl scene:** LoRA-only CAR=12–15.5%, much lower than object_pudding (~54–57%), indicating scene-specific difficulty.\n"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-28T19:22:07.885331+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-28T19:22:07.885522+00:00_

Done. The file is at `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md`.

**What was extracted:**

- All 72 experiments have `conclusion=success` (no failures in registry).
- The file contains:
  - 72 numbered entries grouped into 11 thematic groups (baselines, training sweeps, re-evals, ablations, multi-seed robustness battery, analysis experiments)
  - Each entry: `exp_id`, hypothesis (1 line), key metrics (CAR, TSR, dfCAR, dfCAR_100mm, frozen_rate, fake_safe_rate, best_loss, steps_completed, eval_seed, n_episodes, etc.), unique notes
  - A consolidated performance table for all eval experiments (43 rows) with CAR%, TSR%, dfCAR%, n_episodes, eval_seed, λ, train seed, scene

**Key finding:** After the 180° image rotation eval bug was fixed (Group 6 onward), SDF-augmented models (λ=0.005/0.01/0.1, all 3 seeds) produce CAR ~52–58%, indistinguishable from the LoRA-only baseline (~52–57%), across 7 eval seeds. The `analysis_threshold_sensitivity` experiment confirms dfCAR is perfectly invariant to threshold choice across [2, 200] mm.
agentId: a0bfbd6bb8590d80c (use SendMessage with to: 'a0bfbd6bb8590d80c' to continue this agent)
&lt;usage>total_tokens: 58885
tool_uses: 12
duration_ms: 260338&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-28T19:22:07.885692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-28T19:22:07.885815+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_numerical_references.md"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-28T19:22:07.886065+00:00_

1	# Paper Numerical References — diff_collision_sdf
2	
3	Extracted from all tex files in `/docs/paper/`. Organized by file. Covers all specific numerical values, table data, statistical results, and experiment references.
4	
5	---
6	
7	## abstract.tex
8	
9	| Value | Context |
10	|-------|---------|
11	| >99% | Fraction of safe episodes in Pi0-family models that are action-collapse artifacts (as revealed by dfCAR) |
12	
13	No experiment IDs. No table data. Single quantitative claim supporting the dfCAR finding.
14	
15	---
16	
17	## introduction.tex
18	
19	### Figure Caption Data (fig_overview_pb)
20	
21	| Value | Metric | Condition |
22	|-------|--------|-----------|
23	| 91.5% | CAR | Pi0+A1 reported |
24	| 99.6% | Fraction of safe episodes with displacement < 0.1 mm | Pi0+A1 |
25	| <0.1 mm | Displacement threshold | 99.6% of safe Pi0+A1 episodes |
26	| ≈0% | dfCAR | Pi0+A1 after displacement filtering |
27	| 73–77% | CAR range | All EE-only oracle SDF variants |
28	| 82–83% | CAR range | Unrefined baselines |
29	| +26 pp | CAR gain | From collision-free demonstrations |
30	| +2.3 pp | Additional CAR gain | From SDF supervision |
31	| p = 0.131 | Statistical test (n.s.) | SDF supervision additional benefit |
32	
33	### Figure Caption Data (fig1_teaser)
34	
35	| Value | Metric | Condition |
36	|-------|--------|-----------|
37	| 91.5% | CAR | Pi0+A1 before dfCAR filtering |
38	| ≈0% | dfCAR | Pi0+A1 after filtering |
39	| 288 mm | Minimum displacement | All safe Pi0.5 episodes |
40	
41	### Body Text
42	
43	| Value | Metric | Condition |
44	|-------|--------|-----------|
45	| 91.5% | CAR | Pi0+A1, 800 episodes |
46	| 800 | Total episodes | Pi0+A1 evaluation |
47	| 732 | Collision-free episodes | Pi0+A1 out of 800 |
48	| 99.6% | Fraction with displacement < 0.1 mm | Of the 732 collision-free Pi0+A1 episodes |
49	| 0% | TSR | Pi0+A1 across all 800 episodes |
50	| 100+ | Number of experiments | Total span of the investigation |
51	| 6000+ | Evaluation episodes | Total sp
…[truncated 22419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-28T19:22:07.886371+00:00_

1	# Registry Success Experiments — Complete Summary
2	
3	All 72 experiments have `conclusion=success`. Sorted by `created_at`.
4	
5	---
6	
7	## Group 1 — Early Baselines (pi0 full-FT, pi0+LoRA, A3 gradient refine) [May 19–21]
8	
9	### 1. `baseline_spatial_bowl_s0_v2`
10	- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison
11	- **Metrics:** best_loss=0.00316, final_loss=0.0032, steps_completed=30000
12	- **Unique:** Full-FT (no LoRA) pi0 base; spatial_bowl scene; reference baseline
13	
14	### 2. `baseline_object_pudding_s0_v2`
15	- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%
16	- **Metrics:** final_loss=0.005, steps_completed=30000
17	- **Unique:** Full-FT (no LoRA) pi0 base; object_pudding scene; reference baseline
18	
19	### 3. `a3_gradient_spatial_bowl_s0`
20	- **Hypothesis:** SDF gradient-guided action refinement during training (A3) on spatial_bowl Level II — expects CAR improvement over baseline with TSR drop <10%; comparable to AEGIS (CAR 86%, TSR 88%)
21	- **Metrics:** best_loss=0.01552, steps_completed=30000
22	- **Unique:** A3 architecture (SDF gradient loss at train time); spatial_bowl scene
23	
24	### 4. `a3_gradient_object_pudding_s0`
25	- **Hypothesis:** SDF gradient-guided action refinement (A3) on object_pudding Level I — comparable to AEGIS (CAR 32%, TSR 92%)
26	- **Metrics:** best_loss=0.01439, final_loss=0.01898, steps_completed=30000
27	- **Unique:** A3 architecture; object_pudding scene; model `pi0+A3_gradient_refine`
28	
29	### 5. `baseline_lora_spatial_bowl_s0`
30	- **Hypothesis:** LoRA fine-tuned pi0 baseline on spatial_bowl (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3
31	- **Metrics:** best_loss=0.00876, steps_completed=30000
32	- **Unique:** LoRA baseline (no collision loss); spatial_
…[truncated 29605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-28T19:22:07.886655+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "spatial.*sdf|sdf.*spatial|pi05.*s0.*object.*v11|safelibero.*s0|pi0_full|pi0_lora.*eval|a3.*eval",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Grep",
  "tool_args": {
    "pattern": "spatial.*sdf|sdf.*spatial|pi05.*s0.*object.*v11|safelibero.*s0|pi0_full|pi0_lora.*eval|a3.*eval",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T19:22:07.886802+00:00_

20:- **Hypothesis:** SDF gradient-guided action refinement during training (A3) on spatial_bowl Level II — expects CAR improvement over baseline with TSR drop <10%; comparable to AEGIS (CAR 86%, TSR 88%)
22:- **Unique:** A3 architecture (SDF gradient loss at train time); spatial_bowl scene
45:- **Hypothesis:** A1 SDF auxiliary task with LoRA injection on spatial_bowl — Phase 1 SDF warmup, Phase 2 joint; expects CAR improvement over LoRA baseline with TSR drop <10%
127:- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss on spatial_bowl (λ=0.005, seed 0) — tests cross-scene generalization; bilateral obstacles
283:- **Hypothesis:** LoRA-only baseline (without SDF collision loss) on spatial_bowl — safety-violation rate should remain high at pre-training level, establishing the gap SDF training aims to close
346:- **Hypothesis:** LoRA baseline (no SDF) on spatial_bowl at 30K steps — high TSR but low CAR, confirming collision avoidance requires explicit SDF training signal
385:- **Hypothesis:** Re-evaluate LoRA-only control on safelibero_spatial with consistent eval pipeline — confirms SDF redundancy across scenes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-28T19:22:07.886968+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "stepwise|16k|20k|16000|20000",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Grep",
  "tool_args": {
    "pattern": "stepwise|16k|20k|16000|20000",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/registry_success_summary.md",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-28T19:22:07.887099+00:00_

176:### 32. `eval_pi05_a1_best_s1_l005_16k`
177:- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed1, λ=0.005, step 16000) — best-loss checkpoint vs 30K final
179:- **Unique:** Best-loss checkpoint at step 16K; zero fake-safe episodes
299:## Group 9 — dfCAR Analysis, Stepwise Eval, LoRA Baseline Seed 2 [May 26–27]
306:### 54. `eval_stepwise_s0_l1_22k`
307:- **Hypothesis:** Step-wise eval of Pi0.5+A1 SDF λ=0.1 (seed 0) at 22K checkpoint — third point in step-wise CAR curve (16K: 55.5%, 20K: 55%, 22K: this)
316:### 56. `eval_stepwise_s0_l1_26k_v2`
326:- **Hypothesis:** Evaluate λ=0.1 seed0 30K checkpoint — based on stepwise curve (16K–28K CAR ~52.5–60.5%, mean ~55.1%), expects Scenario B (CAR ≤ 57%, SDF redundant)
428:| eval_pi05_a1_best_s1_l005_16k | 53.0 | 6.5 | — | 200 | 1 | 0.005 | 1 | object |
442:| eval_stepwise_s0_l1_22k | 60.5 | 45.5 | — | — | 7 | 0.1 | 0 | object |
443:| eval_stepwise_s0_l1_26k_v2 | 53.5 | 53.0 | 53.5 | — | 7 | 0.1 | 0 | object |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-28T19:22:07.887316+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/utilization_audit.md",
  "content": "# Experiment Utilization Audit: diff_collision_sdf\n\n**Date:** 2026-05-28\n**Scope:** 72 registry experiments (all conclusion=success) vs. paper tex files\n\n---\n\n## 1. Paper-Referenced Experiments\n\n### 1.1 Claim 1 — Action-Collapse Diagnosis (claim1.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `eval_a1_lora_object_v11` | tab:fake_safety, Pi0+A1 row | CAR=91.5%, TSR=0%, collapsed=99.6% (800 ep aggregate) |\n| `eval_pi05_safelibero_object_v11_s1` | tab:fake_safety, Pi0.5 row | CAR=25% (one of multi-seed) |\n| `eval_pi05_safelibero_object_v11_s2` | tab:fake_safety, Pi0.5 row | CAR=27.5% (one of multi-seed) |\n\n**Note:** Pi0 Full-FT (83%), Pi0 LoRA (82%), and Pi0.5 seed 0 (to get 28.5% mean) results appear in the paper but have **no matching registry experiments** — see §5 Provenance Gaps.\n\n### 1.2 Claim 2 — Oracle SDF Refinement (claim2.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| *(none)* | tab:oracle | Oracle-adaptive 75%, Oracle-fixed 73.1%, Oracle-feature 76.9%, A3 77.1% |\n\n**Note:** All oracle and A3 eval results in claim2 have **no matching registry experiments** — see §5.\n\n### 1.3 Claim 3 — Avoidance Source Attribution (claim3.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `eval_lora_baseline_30k_s0_reeval` | tab:avoidance_source, LoRA s0 | CAR=56.5% |\n| `reeval_lora_s1_30k` | tab:avoidance_source, LoRA s1 | CAR=52.5% |\n| `eval_lora_s2_30k_v2` | tab:avoidance_source, LoRA s2 | CAR=55.0% |\n| `reeval_sdf_s0_l005_30k` | tab:avoidance_source, λ=0.005 s0 | CAR=57.0% |\n| `reeval_sdf_s1_l005_30k` | tab:avoidance_source, λ=0.005 s1 | CAR=54.0% |\n| `reeval_sdf_s2_l005_30k` | tab:avoidance_source, λ=0.005 s2 | CAR=52.5% |\n| `reeval_sdf_s0_l01_30k` | tab:avoidance_source, λ=0.01 s0 | CAR=57.0% |\n| `reeval_sdf_s1_l01_30k` | tab:avoidance_source, λ=0.01 s1 | CAR=57.5% |\n| `reeval_sdf_s2_l01_30k` | tab:avoidance_source, λ=0.01 s2 | CAR=54.5% |\n| `eval_pi05_a1_30k_s0_l01_high` | tab:avoidance_source, λ=0.1 s0 | CAR=58.0% |\n| `eval_pi05_a1_30k_s1_l01_high` | tab:avoidance_source, λ=0.1 s1 | CAR=58.5% |\n| `eval_pi05_a1_30k_s2_l01_high` | tab:avoidance_source, λ=0.1 s2 | CAR=54.5% |\n\nPhase 2 ablation (claim3 body):\n| `train_pi05_phase2_lambda0_s2` | claim3 body text | Phase 2 λ=0 training |\n| `eval_phase2_lambda0_s2` | claim3 body text | CAR=57.5% at 18K (single seed s2) |\n\n### 1.4 Appendix\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `analysis_threshold_sensitivity` | tab:dfcar_threshold | dfCAR invariant across τ_d ∈ [2, 200] mm |\n| `eval_stepwise_s0_l1_22k` | tab:stepwise_lambda01 | 22K: CAR=60.5% |\n| `eval_stepwise_s0_l1_26k_v2` | tab:stepwise_lambda01 | 26K: CAR=53.5% |\n| `eval_multiseed_lora_s0_eseed0` | tab:eval_seed_robustness | LoRA s0 eseed=0: CAR=53.0% |\n| `eval_multiseed_lora_s0_eseed42` | tab:eval_seed_robustness | LoRA s0 eseed=42: CAR=56.5% |\n| `eval_multiseed_lora_s0_eseed99` | tab:eval_seed_robustness | LoRA s0 eseed=99: CAR=57.5% |\n| `eval_multiseed_lora_s0_eseed123` | tab:eval_seed_robustness | LoRA s0 eseed=123: CAR=53.0% |\n| `eval_multiseed_sdf_l01_s0_eseed0` | tab:eval_seed_robustness | SDF λ=0.01 eseed=0: CAR=52.5% |\n| `eval_multiseed_sdf_l01_s0_eseed99` | tab:eval_seed_robustness | SDF λ=0.01 eseed=99: CAR=57.0% |\n| `eval_multiseed_sdf_l01_s0_eseed42` | tab:eval_seed_robustness | SDF λ=0.1 eseed=42: CAR=59.0% |\n| `eval_multiseed_sdf_l01_s0_eseed123` | tab:eval_seed_robustness | SDF λ=0.1 eseed=123: CAR=58.5% |\n| `eval_spatial_bowl_lora_ctrl_s0_v2` | tab:spatial_bowl | LoRA-only spatial: CAR=12.0% |\n\n### 1.5 Training Experiments (indirectly used for hyperparameters/training protocol)\n\n22 training experiments provide training loss data and underpin the appendix training details section:\n`baseline_spatial_bowl_s0_v2`, `baseline_object_pudding_s0_v2`, `a3_gradient_spatial_bowl_s0`, `a3_gradient_object_pudding_s0`, `baseline_lora_spatial_bowl_s0`, `baseline_lora_object_pudding_s0`, `a1_lora_object_pudding_s0`, `a1_lora_spatial_bowl_s0`, `train_pi05_a1_obj_s0_l01`, `train_pi05_a1_obj_s0_l005`, `train_pi05_a1_obj_s1_l005`, `train_pi05_a1_obj_s1_l01`, `train_pi05_a1_obj_s2_l005`, `train_pi05_a1_obj_s2_l01`, `train_pi05_lora_baseline_s0`, `train_pi05_lora_baseline_s1`, `train_pi05_a1_spatial_bowl_s0_l005`, `train_pi05_a1_obj_s0_l01_high`, `train_pi05_a1_obj_s1_l01_high`, `train_pi05_a1_obj_s2_l01_high`, `train_spatial_bowl_lora_control_s0`, `train_pi05_lora_baseline_s2_resume`\n\n**Summary: 51 of 72 experiments are directly or indirectly referenced in the paper.**\n\n---\n\n## 2. Unused Experiments with Potential Value\n\n### 2.1 `eval_multiseed_sdf_l01_s0_eseed256` — 4th eval seed for λ=0.1\n\n- **Data:** CAR=57.0%, TSR=48.0%, 50 episodes, eval_seed=256\n- **Current paper gap:** tab:eval_seed_robustness shows 5 eval seeds for LoRA but only 3 for SDF λ=0.1 (seeds 7, 42, 123). This asymmetry is noticeable.\n- **Recommendation:** **Add to appendix table.** Including eseed=256 would give 4 eval seeds for λ=0.1 (mean CAR = 58.1→57.9%), reducing the asymmetry. Alternatively, add both eseed=0 and eseed=256 for full 5-way symmetry (but eseed=0 eval for λ=0.1 was never run — only for λ=0.01).\n- **Priority: HIGH** — easy win, data already exists.\n\n### 2.2 `reeval_lora_s0_30k_v2` — Run-to-run stochastic variance\n\n- **Data:** LoRA s0, eval_seed=7, CAR=57.0%, TSR=46.0%\n- **Current paper uses:** `eval_lora_baseline_30k_s0_reeval` for the same model/seed giving CAR=56.5%, TSR=51.5%\n- **Significance:** Two runs of the identical model/seed/eval_seed produce 0.5 pp CAR difference and 5.5 pp TSR difference. This quantifies **run-to-run evaluation noise**, which is directly relevant to the MDE discussion (current MDE ≈ 5 pp at n=3).\n- **Recommendation:** Mention in limitations or appendix as evidence that evaluation itself contributes ~0.5–5.5 pp noise, further justifying why 2.3 pp effects are undetectable.\n- **Priority: MEDIUM** — strengthens the statistical argument but requires careful framing.\n\n### 2.3 `train_phase2_lambda0_extra_seed` — 2nd seed for Phase 2 ablation\n\n- **Data:** Phase 2 Stage 1 training (seed 0, λ=0.005, 10K steps)\n- **Current paper gap:** Phase 2 ablation is single-seed (s2 only, CAR=57.5%). This is explicitly flagged as a limitation.\n- **Status:** Training completed, but **no eval experiment registered.** If evaluation was conducted, the data should be added.\n- **Recommendation:** If eval data exists somewhere, add it to claim3 to upgrade Phase 2 ablation from n=1 to n=2.\n- **Priority: HIGH** if eval exists, LOW if eval was never run.\n\n### 2.4 Pre-fix vs post-fix comparison for methodological documentation\n\n- **Available data pairs:**\n  | Model | Pre-fix TSR | Post-fix TSR | Δ |\n  |-------|------------|-------------|---|\n  | SDF λ=0.005 s0 | 5.5% (#20) | 55.5% (#44) | +50 pp |\n  | SDF λ=0.01 s0 | 5.5% (#21) | 52.5% (#42) | +47 pp |\n  | LoRA s0 | 8.5% (#38) | 51.5% (#41) | +43 pp |\n\n- **Recommendation:** Consider a brief appendix paragraph or footnote documenting the 180° image rotation bug and its ~45 pp impact on TSR. This is a valuable cautionary note for the community (VLA evaluation pitfalls).\n- **Priority: LOW** — methodological interest only, not core contribution.\n\n---\n\n## 3. Correctly Excluded Experiments\n\n### 3.1 Pre-rotation-fix evals (12 experiments) — SUPERSEDED\n\nAll performed before the 180° image rotation bug was discovered. TSR values are artifactually low (~4–10% instead of ~50%). CAR values are also unreliable because the policy received incorrectly oriented images.\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_a1_30k_s0_l005` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s0_l01` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s1_l005_v2` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s2_l005_v2` | Pre-fix, TSR=9.5% |\n| `eval_pi05_a1_30k_s1_l01_v2` | Pre-fix, TSR=7.5% |\n| `eval_pi05_a1_30k_s2_l01_v2` | Pre-fix, TSR=7.5% |\n| `eval_pi05_a1_30k_s1_l005_v3` | Pre-fix, TSR=4% |\n| `eval_pi05_a1_30k_s2_l005_v3` | Pre-fix, TSR=9% |\n| `eval_pi05_a1_best_s0_l005` | Pre-fix (eval_seed=7 but old script) |\n| `eval_pi05_a1_30k_s0_l005_r4` | Old script retry |\n| `eval_lora_baseline_30k_s0_v2` | Pre-fix |\n| `eval_lora_baseline_30k_s1_v2` | Pre-fix |\n\n### 3.2 Displacement fix / debugging evals (4 experiments) — INTERMEDIATE\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_a1_best_s2_l005_10k` | Pre-fix, used old eval script. Zero-fake-safe finding is interesting but invalid due to rotation bug. |\n| `eval_pi05_a1_best_s1_l005_16k` | Pre-fix, best-loss checkpoint eval |\n| `eval_pi05_a1_30k_s1_l005_disp` | Displacement field fix verification run |\n| `eval_pi05_a1_30k_s0_l01_disp` | Displacement field fix verification run |\n\n### 3.3 Pipeline v1 / empty metrics (2 experiments) — SUPERSEDED\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_baseline_reeval_disp` | Metrics empty in registry |\n| `eval_spatial_bowl_lora_ctrl_s0` | v1 pipeline, superseded by `_v2` (#68) |\n\n---\n\n## 4. Consistency Cross-Checks\n\n### 4.1 Registry ↔ Paper Value Matches\n\nAll checked values match between registry metrics and paper tables:\n\n| Paper value | Registry source | Match? |\n|-------------|----------------|--------|\n| LoRA s1 CAR=52.5% | reeval_lora_s1_30k: car=52.5% | ✓ |\n| SDF λ=0.005 s0 CAR=57.0% | reeval_sdf_s0_l005_30k: car=57% | ✓ |\n| SDF λ=0.1 s0 CAR=58.0% | eval_pi05_a1_30k_s0_l01_high: CAR=58% | ✓ |\n| SDF λ=0.1 s2 CAR=54.5% | eval_pi05_a1_30k_s2_l01_high: car=54.5% | ✓ |\n| LoRA eseed=42 CAR=56.5% | eval_multiseed_lora_s0_eseed42: avg_CAR=56.5% | ✓ |\n| dfCAR threshold stable [2,200]mm | analysis_threshold_sensitivity | ✓ |\n\n### 4.2 Potential Discrepancy: LoRA s0 value\n\n- Paper tab:avoidance_source uses LoRA-only mean = 54.67% = (56.5 + 52.5 + 55.0) / 3\n- This implies LoRA s0 = 56.5%, from `eval_lora_baseline_30k_s0_reeval`\n- But `reeval_lora_s0_30k_v2` gives 57.0% for the same model/seed/eval_seed\n- The 0.5 pp discrepancy is due to different eval runs (stochastic simulation). Paper consistently uses the earlier run (#41).\n\n---\n\n## 5. Provenance Gaps — Paper Numbers Without Registry Source\n\nThe following paper values have **no matching registry experiment**:\n\n| Paper value | Location | Likely source |\n|-------------|----------|---------------|\n| Pi0 Full-FT: CAR=83.0%, TSR=0.5% | claim1 tab:fake_safety | Evaluated before registry established, or unregistered eval |\n| Pi0 LoRA: CAR=82.0%, TSR=0.0% | claim1 tab:fake_safety | Same — unregistered eval |\n| Pi0.5 baseline: CAR=28.5% (aggregate) | claim1, claim3 | Requires seed 0 eval (registered s1=25%, s2=27.5%; seed 0 not registered) |\n| Oracle-adaptive: CAR=75.0% | claim2 tab:oracle | Oracle evals never registered |\n| Oracle-fixed: CAR=73.1% | claim2 tab:oracle | Oracle evals never registered |\n| Oracle-feature: CAR=76.9% | claim2 tab:oracle | Oracle evals never registered |\n| A3 learned SDF: CAR=77.1% | claim2 tab:oracle | A3 eval never registered |\n| Spatial bowl SDF λ=0.005: CAR=11.5% | appendix tab:spatial_bowl | Eval of trained model #22, eval not registered |\n| Stepwise 16K s0: CAR=55.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 20K s0: CAR=55.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 24K s0: CAR=52.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 28K s0: CAR=54.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 16K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 20K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 22K s1: CAR=56.5% | appendix tab:stepwise | Unregistered eval |\n\n**Total: ~17 data points in the paper without registry provenance.**\n\n---\n\n## 6. Recommendations (Prioritized)\n\n### Priority 1: Add eseed=256 to eval-seed robustness table\n- **Effort:** 5 min (add one row to tab:eval_seed_robustness)\n- **Impact:** Fixes asymmetry (3 vs 5 eval seeds for SDF vs LoRA). New λ=0.1 mean: 58.5→58.1% (4 seeds), further supporting non-significance.\n\n### Priority 2: Check if Phase 2 extra seed was evaluated\n- **Effort:** Check server for eval results of `train_phase2_lambda0_extra_seed` model\n- **Impact:** If available, upgrades Phase 2 ablation from n=1 to n=2, partially addressing a stated limitation.\n\n### Priority 3: Report run-to-run variance in limitations\n- **Effort:** 1 sentence + footnote\n- **Impact:** `reeval_lora_s0_30k_v2` (CAR=57%) vs `eval_lora_baseline_30k_s0_reeval` (CAR=56.5%) demonstrates 0.5 pp CAR and 5.5 pp TSR run-to-run noise. Strengthens the argument that 2.3 pp effects are below noise floor.\n\n### Priority 4: Register provenance gaps\n- **Effort:** Retroactively register the 17 unregistered evals\n- **Impact:** Complete audit trail. Especially important for Pi0/Oracle/A3 results (claim1 & claim2 are foundational).\n\n### Priority 5: Document rotation bug as methodological note\n- **Effort:** 2-3 sentences in appendix\n- **Impact:** Cautionary contribution for VLA evaluation community. 12 pre-fix experiments provide clear evidence of ~45 pp TSR artifact.\n\n### Not recommended:\n- Adding pre-rotation-fix data to the paper (invalid due to eval bug)\n- Adding displacement-fix verification runs (debugging artifacts)\n- Adding v1 pipeline results (superseded)\n\n---\n\n## 7. Summary Statistics\n\n| Category | Count | % of 72 |\n|----------|-------|---------|\n| Directly referenced in paper (eval) | 27 | 37.5% |\n| Indirectly referenced (training) | 22 | 30.6% |\n| Phase 2 ablation | 2 | 2.8% |\n| **Total used** | **51** | **70.8%** |\n| Unused — potentially valuable | 3 | 4.2% |\n| Unused — superseded (pre-fix) | 12 | 16.7% |\n| Unused — debugging/intermediate | 4 | 5.6% |\n| Unused — pipeline v1/empty | 2 | 2.8% |\n| **Total unused** | **21** | **29.2%** |\n\n**Utilization rate: 70.8%.** The 29.2% unused experiments are predominantly pre-rotation-fix evals (57% of unused) that were correctly excluded due to the evaluation bug. Only 3 experiments (4.2% of total) have potential value not currently captured in the paper.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/utilization_audit.md",
    "content": "# Experiment Utilization Audit: diff_collision_sdf\n\n**Date:** 2026-05-28\n**Scope:** 72 registry experiments (all conclusion=success) vs. paper tex files\n\n---\n\n## 1. Paper-Referenced Experiments\n\n### 1.1 Claim 1 — Action-Collapse Diagnosis (claim1.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `eval_a1_lora_object_v11` | tab:fake_safety, Pi0+A1 row | CAR=91.5%, TSR=0%, collapsed=99.6% (800 ep aggregate) |\n| `eval_pi05_safelibero_object_v11_s1` | tab:fake_safety, Pi0.5 row | CAR=25% (one of multi-seed) |\n| `eval_pi05_safelibero_object_v11_s2` | tab:fake_safety, Pi0.5 row | CAR=27.5% (one of multi-seed) |\n\n**Note:** Pi0 Full-FT (83%), Pi0 LoRA (82%), and Pi0.5 seed 0 (to get 28.5% mean) results appear in the paper but have **no matching registry experiments** — see §5 Provenance Gaps.\n\n### 1.2 Claim 2 — Oracle SDF Refinement (claim2.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| *(none)* | tab:oracle | Oracle-adaptive 75%, Oracle-fixed 73.1%, Oracle-feature 76.9%, A3 77.1% |\n\n**Note:** All oracle and A3 eval results in claim2 have **no matching registry experiments** — see §5.\n\n### 1.3 Claim 3 — Avoidance Source Attribution (claim3.tex)\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `eval_lora_baseline_30k_s0_reeval` | tab:avoidance_source, LoRA s0 | CAR=56.5% |\n| `reeval_lora_s1_30k` | tab:avoidance_source, LoRA s1 | CAR=52.5% |\n| `eval_lora_s2_30k_v2` | tab:avoidance_source, LoRA s2 | CAR=55.0% |\n| `reeval_sdf_s0_l005_30k` | tab:avoidance_source, λ=0.005 s0 | CAR=57.0% |\n| `reeval_sdf_s1_l005_30k` | tab:avoidance_source, λ=0.005 s1 | CAR=54.0% |\n| `reeval_sdf_s2_l005_30k` | tab:avoidance_source, λ=0.005 s2 | CAR=52.5% |\n| `reeval_sdf_s0_l01_30k` | tab:avoidance_source, λ=0.01 s0 | CAR=57.0% |\n| `reeval_sdf_s1_l01_30k` | tab:avoidance_source, λ=0.01 s1 | CAR=57.5% |\n| `reeval_sdf_s2_l01_30k` | tab:avoidance_source, λ=0.01 s2 | CAR=54.5% |\n| `eval_pi05_a1_30k_s0_l01_high` | tab:avoidance_source, λ=0.1 s0 | CAR=58.0% |\n| `eval_pi05_a1_30k_s1_l01_high` | tab:avoidance_source, λ=0.1 s1 | CAR=58.5% |\n| `eval_pi05_a1_30k_s2_l01_high` | tab:avoidance_source, λ=0.1 s2 | CAR=54.5% |\n\nPhase 2 ablation (claim3 body):\n| `train_pi05_phase2_lambda0_s2` | claim3 body text | Phase 2 λ=0 training |\n| `eval_phase2_lambda0_s2` | claim3 body text | CAR=57.5% at 18K (single seed s2) |\n\n### 1.4 Appendix\n\n| Registry exp_id | Paper reference | Value used |\n|----------------|----------------|------------|\n| `analysis_threshold_sensitivity` | tab:dfcar_threshold | dfCAR invariant across τ_d ∈ [2, 200] mm |\n| `eval_stepwise_s0_l1_22k` | tab:stepwise_lambda01 | 22K: CAR=60.5% |\n| `eval_stepwise_s0_l1_26k_v2` | tab:stepwise_lambda01 | 26K: CAR=53.5% |\n| `eval_multiseed_lora_s0_eseed0` | tab:eval_seed_robustness | LoRA s0 eseed=0: CAR=53.0% |\n| `eval_multiseed_lora_s0_eseed42` | tab:eval_seed_robustness | LoRA s0 eseed=42: CAR=56.5% |\n| `eval_multiseed_lora_s0_eseed99` | tab:eval_seed_robustness | LoRA s0 eseed=99: CAR=57.5% |\n| `eval_multiseed_lora_s0_eseed123` | tab:eval_seed_robustness | LoRA s0 eseed=123: CAR=53.0% |\n| `eval_multiseed_sdf_l01_s0_eseed0` | tab:eval_seed_robustness | SDF λ=0.01 eseed=0: CAR=52.5% |\n| `eval_multiseed_sdf_l01_s0_eseed99` | tab:eval_seed_robustness | SDF λ=0.01 eseed=99: CAR=57.0% |\n| `eval_multiseed_sdf_l01_s0_eseed42` | tab:eval_seed_robustness | SDF λ=0.1 eseed=42: CAR=59.0% |\n| `eval_multiseed_sdf_l01_s0_eseed123` | tab:eval_seed_robustness | SDF λ=0.1 eseed=123: CAR=58.5% |\n| `eval_spatial_bowl_lora_ctrl_s0_v2` | tab:spatial_bowl | LoRA-only spatial: CAR=12.0% |\n\n### 1.5 Training Experiments (indirectly used for hyperparameters/training protocol)\n\n22 training experiments provide training loss data and underpin the appendix training details section:\n`baseline_spatial_bowl_s0_v2`, `baseline_object_pudding_s0_v2`, `a3_gradient_spatial_bowl_s0`, `a3_gradient_object_pudding_s0`, `baseline_lora_spatial_bowl_s0`, `baseline_lora_object_pudding_s0`, `a1_lora_object_pudding_s0`, `a1_lora_spatial_bowl_s0`, `train_pi05_a1_obj_s0_l01`, `train_pi05_a1_obj_s0_l005`, `train_pi05_a1_obj_s1_l005`, `train_pi05_a1_obj_s1_l01`, `train_pi05_a1_obj_s2_l005`, `train_pi05_a1_obj_s2_l01`, `train_pi05_lora_baseline_s0`, `train_pi05_lora_baseline_s1`, `train_pi05_a1_spatial_bowl_s0_l005`, `train_pi05_a1_obj_s0_l01_high`, `train_pi05_a1_obj_s1_l01_high`, `train_pi05_a1_obj_s2_l01_high`, `train_spatial_bowl_lora_control_s0`, `train_pi05_lora_baseline_s2_resume`\n\n**Summary: 51 of 72 experiments are directly or indirectly referenced in the paper.**\n\n---\n\n## 2. Unused Experiments with Potential Value\n\n### 2.1 `eval_multiseed_sdf_l01_s0_eseed256` — 4th eval seed for λ=0.1\n\n- **Data:** CAR=57.0%, TSR=48.0%, 50 episodes, eval_seed=256\n- **Current paper gap:** tab:eval_seed_robustness shows 5 eval seeds for LoRA but only 3 for SDF λ=0.1 (seeds 7, 42, 123). This asymmetry is noticeable.\n- **Recommendation:** **Add to appendix table.** Including eseed=256 would give 4 eval seeds for λ=0.1 (mean CAR = 58.1→57.9%), reducing the asymmetry. Alternatively, add both eseed=0 and eseed=256 for full 5-way symmetry (but eseed=0 eval for λ=0.1 was never run — only for λ=0.01).\n- **Priority: HIGH** — easy win, data already exists.\n\n### 2.2 `reeval_lora_s0_30k_v2` — Run-to-run stochastic variance\n\n- **Data:** LoRA s0, eval_seed=7, CAR=57.0%, TSR=46.0%\n- **Current paper uses:** `eval_lora_baseline_30k_s0_reeval` for the same model/seed giving CAR=56.5%, TSR=51.5%\n- **Significance:** Two runs of the identical model/seed/eval_seed produce 0.5 pp CAR difference and 5.5 pp TSR difference. This quantifies **run-to-run evaluation noise**, which is directly relevant to the MDE discussion (current MDE ≈ 5 pp at n=3).\n- **Recommendation:** Mention in limitations or appendix as evidence that evaluation itself contributes ~0.5–5.5 pp noise, further justifying why 2.3 pp effects are undetectable.\n- **Priority: MEDIUM** — strengthens the statistical argument but requires careful framing.\n\n### 2.3 `train_phase2_lambda0_extra_seed` — 2nd seed for Phase 2 ablation\n\n- **Data:** Phase 2 Stage 1 training (seed 0, λ=0.005, 10K steps)\n- **Current paper gap:** Phase 2 ablation is single-seed (s2 only, CAR=57.5%). This is explicitly flagged as a limitation.\n- **Status:** Training completed, but **no eval experiment registered.** If evaluation was conducted, the data should be added.\n- **Recommendation:** If eval data exists somewhere, add it to claim3 to upgrade Phase 2 ablation from n=1 to n=2.\n- **Priority: HIGH** if eval exists, LOW if eval was never run.\n\n### 2.4 Pre-fix vs post-fix comparison for methodological documentation\n\n- **Available data pairs:**\n  | Model | Pre-fix TSR | Post-fix TSR | Δ |\n  |-------|------------|-------------|---|\n  | SDF λ=0.005 s0 | 5.5% (#20) | 55.5% (#44) | +50 pp |\n  | SDF λ=0.01 s0 | 5.5% (#21) | 52.5% (#42) | +47 pp |\n  | LoRA s0 | 8.5% (#38) | 51.5% (#41) | +43 pp |\n\n- **Recommendation:** Consider a brief appendix paragraph or footnote documenting the 180° image rotation bug and its ~45 pp impact on TSR. This is a valuable cautionary note for the community (VLA evaluation pitfalls).\n- **Priority: LOW** — methodological interest only, not core contribution.\n\n---\n\n## 3. Correctly Excluded Experiments\n\n### 3.1 Pre-rotation-fix evals (12 experiments) — SUPERSEDED\n\nAll performed before the 180° image rotation bug was discovered. TSR values are artifactually low (~4–10% instead of ~50%). CAR values are also unreliable because the policy received incorrectly oriented images.\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_a1_30k_s0_l005` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s0_l01` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s1_l005_v2` | Pre-fix, TSR=5.5% |\n| `eval_pi05_a1_30k_s2_l005_v2` | Pre-fix, TSR=9.5% |\n| `eval_pi05_a1_30k_s1_l01_v2` | Pre-fix, TSR=7.5% |\n| `eval_pi05_a1_30k_s2_l01_v2` | Pre-fix, TSR=7.5% |\n| `eval_pi05_a1_30k_s1_l005_v3` | Pre-fix, TSR=4% |\n| `eval_pi05_a1_30k_s2_l005_v3` | Pre-fix, TSR=9% |\n| `eval_pi05_a1_best_s0_l005` | Pre-fix (eval_seed=7 but old script) |\n| `eval_pi05_a1_30k_s0_l005_r4` | Old script retry |\n| `eval_lora_baseline_30k_s0_v2` | Pre-fix |\n| `eval_lora_baseline_30k_s1_v2` | Pre-fix |\n\n### 3.2 Displacement fix / debugging evals (4 experiments) — INTERMEDIATE\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_a1_best_s2_l005_10k` | Pre-fix, used old eval script. Zero-fake-safe finding is interesting but invalid due to rotation bug. |\n| `eval_pi05_a1_best_s1_l005_16k` | Pre-fix, best-loss checkpoint eval |\n| `eval_pi05_a1_30k_s1_l005_disp` | Displacement field fix verification run |\n| `eval_pi05_a1_30k_s0_l01_disp` | Displacement field fix verification run |\n\n### 3.3 Pipeline v1 / empty metrics (2 experiments) — SUPERSEDED\n\n| exp_id | Issue |\n|--------|-------|\n| `eval_pi05_baseline_reeval_disp` | Metrics empty in registry |\n| `eval_spatial_bowl_lora_ctrl_s0` | v1 pipeline, superseded by `_v2` (#68) |\n\n---\n\n## 4. Consistency Cross-Checks\n\n### 4.1 Registry ↔ Paper Value Matches\n\nAll checked values match between registry metrics and paper tables:\n\n| Paper value | Registry source | Match? |\n|-------------|----------------|--------|\n| LoRA s1 CAR=52.5% | reeval_lora_s1_30k: car=52.5% | ✓ |\n| SDF λ=0.005 s0 CAR=57.0% | reeval_sdf_s0_l005_30k: car=57% | ✓ |\n| SDF λ=0.1 s0 CAR=58.0% | eval_pi05_a1_30k_s0_l01_high: CAR=58% | ✓ |\n| SDF λ=0.1 s2 CAR=54.5% | eval_pi05_a1_30k_s2_l01_high: car=54.5% | ✓ |\n| LoRA eseed=42 CAR=56.5% | eval_multiseed_lora_s0_eseed42: avg_CAR=56.5% | ✓ |\n| dfCAR threshold stable [2,200]mm | analysis_threshold_sensitivity | ✓ |\n\n### 4.2 Potential Discrepancy: LoRA s0 value\n\n- Paper tab:avoidance_source uses LoRA-only mean = 54.67% = (56.5 + 52.5 + 55.0) / 3\n- This implies LoRA s0 = 56.5%, from `eval_lora_baseline_30k_s0_reeval`\n- But `reeval_lora_s0_30k_v2` gives 57.0% for the same model/seed/eval_seed\n- The 0.5 pp discrepancy is due to different eval runs (stochastic simulation). Paper consistently uses the earlier run (#41).\n\n---\n\n## 5. Provenance Gaps — Paper Numbers Without Registry Source\n\nThe following paper values have **no matching registry experiment**:\n\n| Paper value | Location | Likely source |\n|-------------|----------|---------------|\n| Pi0 Full-FT: CAR=83.0%, TSR=0.5% | claim1 tab:fake_safety | Evaluated before registry established, or unregistered eval |\n| Pi0 LoRA: CAR=82.0%, TSR=0.0% | claim1 tab:fake_safety | Same — unregistered eval |\n| Pi0.5 baseline: CAR=28.5% (aggregate) | claim1, claim3 | Requires seed 0 eval (registered s1=25%, s2=27.5%; seed 0 not registered) |\n| Oracle-adaptive: CAR=75.0% | claim2 tab:oracle | Oracle evals never registered |\n| Oracle-fixed: CAR=73.1% | claim2 tab:oracle | Oracle evals never registered |\n| Oracle-feature: CAR=76.9% | claim2 tab:oracle | Oracle evals never registered |\n| A3 learned SDF: CAR=77.1% | claim2 tab:oracle | A3 eval never registered |\n| Spatial bowl SDF λ=0.005: CAR=11.5% | appendix tab:spatial_bowl | Eval of trained model #22, eval not registered |\n| Stepwise 16K s0: CAR=55.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 20K s0: CAR=55.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 24K s0: CAR=52.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 28K s0: CAR=54.5% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 16K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 20K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |\n| Stepwise 22K s1: CAR=56.5% | appendix tab:stepwise | Unregistered eval |\n\n**Total: ~17 data points in the paper without registry provenance.**\n\n---\n\n## 6. Recommendations (Prioritized)\n\n### Priority 1: Add eseed=256 to eval-seed robustness table\n- **Effort:** 5 min (add one row to tab:eval_seed_robustness)\n- **Impact:** Fixes asymmetry (3 vs 5 eval seeds for SDF vs LoRA). New λ=0.1 mean: 58.5→58.1% (4 seeds), further supporting non-significance.\n\n### Priority 2: Check if Phase 2 extra seed was evaluated\n- **Effort:** Check server for eval results of `train_phase2_lambda0_extra_seed` model\n- **Impact:** If available, upgrades Phase 2 ablation from n=1 to n=2, partially addressing a stated limitation.\n\n### Priority 3: Report run-to-run variance in limitations\n- **Effort:** 1 sentence + footnote\n- **Impact:** `reeval_lora_s0_30k_v2` (CAR=57%) vs `eval_lora_baseline_30k_s0_reeval` (CAR=56.5%) demonstrates 0.5 pp CAR and 5.5 pp TSR run-to-run noise. Strengthens the argument that 2.3 pp effects are below noise floor.\n\n### Priority 4: Register provenance gaps\n- **Effort:** Retroactively register the 17 unregistered evals\n- **Impact:** Complete audit trail. Especially important for Pi0/Oracle/A3 results (claim1 & claim2 are foundational).\n\n### Priority 5: Document rotation bug as methodological note\n- **Effort:** 2-3 sentences in appendix\n- **Impact:** Cautionary contribution for VLA evaluation community. 12 pre-fix experiments provide clear evidence of ~45 pp TSR artifact.\n\n### Not recommended:\n- Adding pre-rotation-fix data to the paper (invalid due to eval bug)\n- Adding displacement-fix verification runs (debugging artifacts)\n- Adding v1 pipeline results (superseded)\n\n---\n\n## 7. Summary Statistics\n\n| Category | Count | % of 72 |\n|----------|-------|---------|\n| Directly referenced in paper (eval) | 27 | 37.5% |\n| Indirectly referenced (training) | 22 | 30.6% |\n| Phase 2 ablation | 2 | 2.8% |\n| **Total used** | **51** | **70.8%** |\n| Unused — potentially valuable | 3 | 4.2% |\n| Unused — superseded (pre-fix) | 12 | 16.7% |\n| Unused — debugging/intermediate | 4 | 5.6% |\n| Unused — pipeline v1/empty | 2 | 2.8% |\n| **Total unused** | **21** | **29.2%** |\n\n**Utilization rate: 70.8%.** The 29.2% unused experiments are predominantly pre-rotation-fix evals (57% of unused) that were correctly excluded due to the evaluation bug. Only 3 experiments (4.2% of total) have potential value not currently captured in the paper.\n"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-28T19:22:07.887643+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/utilization_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-28T19:22:07.887788+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "utilization_audit",
  "type": "report",
  "description": "Cross-comparison of 72 registry success experiments vs paper tex files. Maps each experiment to paper references, identifies 3 unused-but-valuable experiments, 17 provenance gaps, and 5 prioritized recommendations.",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/utilization_audit.md",
  "tags": "['audit', 'paper', 'experiments', 'utilization']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "utilization_audit",
    "type": "report",
    "description": "Cross-comparison of 72 registry success experiments vs paper tex files. Maps each experiment to paper references, identifies 3 unused-but-valuable experiments, 17 provenance gaps, and 5 prioritized recommendations.",
    "project": "diff_collision_sdf",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/utilization_audit.md",
    "tags": "['audit', 'paper', 'experiments', 'utilization']"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-28T19:22:07.887934+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260528_9360ac\", \"name\": \"utilization_audit\", \"type\": \"report\", \"description\": \"Cross-comparison of 72 registry success experiments vs paper tex files. Maps each experiment to paper references, identifies 3 unused-but-valuable experiments, 17 provenance gaps, and 5 prioritized recommendations.\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/utilization_audit.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-28T19:21:52.994152+00:00\", \"tags\": [\"audit\", \"paper\", \"experiments\", \"utilization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_utilization_audit_20260528T191058",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-28T19:22:07.888099+00:00_

审计完成。产出已注册为 `art_20260528_9360ac`。

**核心发现：**

- **利用率 70.8%**（51/72 实验被论文引用），29.2% 未引用的实验中 57% 是因 180° 旋转 bug 被废弃的 pre-fix 评估，属于合理排除。
- **仅 3 个实验有未被利用的价值：**
  1. `eval_multiseed_sdf_l01_s0_eseed256`（λ=0.1 第4个 eval seed，CAR=57%）— 可直接加入 appendix eval-seed 表，修复当前 3 vs 5 的不对称
  2. `reeval_lora_s0_30k_v2`（同一模型重复评估，CAR=57% vs 56.5%）— 量化了 run-to-run 噪声，可支撑 MDE 讨论
  3. `train_phase2_lambda0_extra_seed`（Phase 2 消融第2个 seed）— 如果做过 eval，可将 Phase 2 消融从 n=1 升至 n=2

- **17 个溯源缺口：** 论文中的 Pi0 Full-FT（83%）、Pi0 LoRA（82%）、Oracle 系列、A3、spatial_bowl SDF 评估、以及 stepwise 16K/20K/24K/28K 数据均无对应 registry 实验记录。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_utilization_audit_20260528T191058"
}
```

</details>

---
