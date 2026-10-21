# writing r34 r38 fixes

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 155
- **Recorded user turns:** 8
- **Tool calls:** 51
- **Original source:** `logs/workers/worker_writing_r34_r38_fixes_20260521T083937.log`
- **Structured JSON:** [`cc1ccbf7512d5abd0057.json`](../../sessions/cc/cc1ccbf7512d5abd0057.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
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
    "Write"
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
  "uuid": "5e326bf3-4d1e-404c-8017-dd00866078c2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1779363000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5332d2d1-5a3d-4c40-825f-8e98fd7a2ca1",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down the 7 tasks and start working on them. First, I need to understand the file structure and then tackle each item.

Let me start by reading the relevant files in parallel to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "233348f0-2bb4-490c-bfd9-485b21978b18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUDEFmdbSjmqZzSxexXERc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14516
      },
      "output_tokens": 20,
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

I'll work through the 7 reviewer feedback items. Let me start by reading the relevant files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "42dfa424-d59e-4546-8d1b-041e36e12022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUDEFmdbSjmqZzSxexXERc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14516
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01FoXYVGvSdzCTiQkCPwapGv`</summary>

```json
{
  "description": "Read all paper source files",
  "subagent_type": "Explore",
  "prompt": "I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. \n\nPlease read the following files in full:\n1. results.tex\n2. method.tex\n3. appendix_qlora.tex\n4. related_work.tex\n5. references.bib\n6. introduction.tex\n7. main.tex\n\nAlso glob for any fig1-related Python files in `artifacts/_project/chart/` under `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`.\n\nAnd grep across all .tex files in `docs/paper/` for:\n- \"recursive generation depth\"\n- \"DDR\"\n- \"6-gen\"\n- \"aaronson\"\n- \"ordinal\"\n- \"$+$11.6\" or \"+11.6\"\n- \"QLoRA\" or \"qlora\"\n\nReport all findings with file paths, line numbers, and surrounding context."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "d9ea3c4f-fea9-46d9-9b32-877091ce02dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUDEFmdbSjmqZzSxexXERc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14516
      },
      "output_tokens": 20,
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

### System

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Read all paper source files",
  "task_type": "local_agent",
  "prompt": "I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. \n\nPlease read the following files in full:\n1. results.tex\n2. method.tex\n3. appendix_qlora.tex\n4. related_work.tex\n5. references.bib\n6. introduction.tex\n7. main.tex\n\nAlso glob for any fig1-related Python files in `artifacts/_project/chart/` under `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`.\n\nAnd grep across all .tex files in `docs/paper/` for:\n- \"recursive generation depth\"\n- \"DDR\"\n- \"6-gen\"\n- \"aaronson\"\n- \"ordinal\"\n- \"$+$11.6\" or \"+11.6\"\n- \"QLoRA\" or \"qlora\"\n\nReport all findings with file paths, line numbers, and surrounding context.",
  "uuid": "cc39f933-3b91-4da7-ac40-d70d7982a371",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

## Round 1

121 recorded events

### User

_source line 8 · 2026-05-21T08:39:52.548Z_

I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. 

Please read the following files in full:
1. results.tex
2. method.tex
3. appendix_qlora.tex
4. related_work.tex
5. references.bib
6. introduction.tex
7. main.tex

Also glob for any fig1-related Python files in `artifacts/_project/chart/` under `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`.

And grep across all .tex files in `docs/paper/` for:
- "recursive generation depth"
- "DDR"
- "6-gen"
- "aaronson"
- "ordinal"
- "$+$11.6" or "+11.6"
- "QLoRA" or "qlora"

Report all findings with file paths, line numbers, and surrounding context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c6d96a66-cc69-44e6-a695-ac834f62fd95"
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_019iysGfVomFHY9vsi1aYHDt`</summary>

```json
{
  "pattern": "**/fig1*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "f22f4761-aeac-4a42-9e6f-ab49b5865aed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUDEFmdbSjmqZzSxexXERc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14516
      },
      "output_tokens": 20,
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

_source line 10 · 2026-05-21T08:39:52.936Z_

<details><summary>↩ Tool result · `toolu_019iysGfVomFHY9vsi1aYHDt`</summary>

```text
artifacts/_project/chart/fig1_ddr_v2.py
artifacts/_project/chart/fig1_combined_v1.py
artifacts/_project/chart/fig1_ddr_v3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "18f2bedd-facb-4f9f-accf-24ebbe7e440b",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/chart/fig1_ddr_v2.py",
      "artifacts/_project/chart/fig1_combined_v1.py",
      "artifacts/_project/chart/fig1_ddr_v3.py"
    ],
    "durationMs": 6,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01J2cfqhdy8DmPdYPY29YPMU`</summary>

```json
{
  "pattern": "**/fig_ddr*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e1badd07-3b47-4aa4-8cb9-c9453526bf05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUDEFmdbSjmqZzSxexXERc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14516
      },
      "output_tokens": 20,
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

_source line 12 · 2026-05-21T08:39:53.415Z_

<details><summary>↩ Tool result · `toolu_01J2cfqhdy8DmPdYPY29YPMU`</summary>

```text
artifacts/_project/chart/fig_ddr_scatter.py
artifacts/_project/chart/fig_ddr_trajectory_v2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "7f8b7d01-e868-43ae-a1c7-e60ea8d7f00f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/chart/fig_ddr_scatter.py",
      "artifacts/_project/chart/fig_ddr_trajectory_v2.py"
    ],
    "durationMs": 5,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/results.tex",
  "usage": {
    "total_tokens": 17211,
    "tool_uses": 1,
    "duration_ms": 1902
  },
  "last_tool_name": "Read",
  "uuid": "7a5213cb-e917-43c3-8efe-0e69ad0c2e0d",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01CrgYpQRinaYfeifx4XqYoF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e65cbbd4-ba9c-4a16-b1c3-53ca62af377b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 15 · 2026-05-21T08:39:54.464Z_

<details><summary>↩ Tool result · `toolu_01CrgYpQRinaYfeifx4XqYoF`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94), inflating the 3-class metric.
9	We therefore adopt \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\,=\,0.028), with the primary difficulty concentrated at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
11	Note that CIs above reflect bootstrap sampling variability; the cross-generator range (9.1\,pp) captures the distinct and larger uncertainty of generator selection.
12	
13	\paragraph{Cross-model generalization.}
14	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under 5-generator LOGO.\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\,=\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
15	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
16	A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
18	
19	\paragraph{Length confound control.}
20	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\ref{app:length}).
21	
22	\paragraph{Seed-sharing control.}
23	Seed-level demeaning (F1\,=\,0.701) and an independent-seed experiment with disjoint seed pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.
24	
25	\begin{table}[t]
26	\centering
27	\footnotesize
28	\resizebox{\columnwidth}{!}{%
29	\begin{tabular}{llcccc}
30	\toprule
31	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-cl F1}$^{\dagger}$ \\
32	\midrule
33	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
34	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
35	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
36	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
37	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
38	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
39	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
40	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
41	\midrule
42	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
43	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
44	\bottomrule
45	\end{tabular}}
46	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\,=\,0.028, IQR\,=\,[0.692, 0.714]. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
47	\label{tab:logo-results}
48	\end{table}
49	
50	\subsection{Differential Depth Response}
51	\label{sec:results-differential}
52	
53	\begin{figure*}[t]
54	\centering
55	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
56	\caption{Feature trajectories across generation depth. \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the differential depth response (DDR).}
57	\label{fig:ddr-trajectory}
58	\end{figure*}
59	
60	Not all distributional properties respond equally to recursive generation.
61	Figure~\ref{fig:ddr-trajectory} reveals a striking dichotomy that holds across all eight generators: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.
62	We term this asymmetry the \emph{differential depth response} (DDR).
63	The primary partition is binary: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields silhouette\,=\,0.660 (Appendix~\ref{app:ddr-validation}), cleanly separating three \emph{drifting} features ($|\rho| > 0.60$, $d{=}0.76$--$1.17$) from four \emph{non-drifting} ones ($d \leq 0.55$); higher $k$ degrades cluster quality ($k{=}3$: silhouette\,=\,0.532).
64	A domain-informed refinement resolves entropy std as a sole \emph{intermediate} member ($d{=}0.55$, $|\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\% vs.\ $>$15\% for drifting features).
65	Convergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\S\ref{sec:results-differential}, Quantification).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	Pooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\ref{fig:feature-drift}):
75	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.64$, TTR $\rho = -0.63$, entropy mean $\rho = -0.60$),
76	while non-drifting features remain near-zero (tail decay $|\rho| = 0.04$; per-depth distributions in Appendix~\ref{app:feature-distributions}).
77	The six-fold magnitude gap between drifting ($|\rho| > 0.60$) and non-drifting features ($|\rho| \leq 0.16$) defines the DDR partition.
78	Within the non-drifting group, entropy std ($|\rho| = 0.16$, $d{=}0.55$) shows a substantial level shift despite low monotonicity, distinguishing it from the three near-stationary features ($d < 0.10$); this refinement is stable across $d$ thresholds in $[0.56, 0.75]$ (Appendix~\ref{app:ddr-validation}).
79	
80	\paragraph{Quantification.}
81	Convergence across parametric and non-parametric effect-size measures confirm the split.
82	Cohen's $d$ \cite{cohen1988statistical} shows a ${\geq}7\times$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary features ($d \leq 0.08$); KS statistics, Glass's $\Delta$, Cliff's $\delta$, and CV shift all corroborate (Appendix~\ref{app:ddr-validation}).
83	Four features fall cleanly into drifting or non-drifting groups.
84	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1 vs.\ gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1 ($|\rho|{=}0.40$); tail decay is \emph{weakly stationary}, passing TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).
85	Entropy std ($d{=}0.55$, $|\rho|{=}0.16$) is the sole intermediate member.
86	\paragraph{Validation.}
87	The drifting/non-drifting boundary is validated by convergent evidence: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields a clean separation (silhouette\,=\,0.660), invariant across threshold choices $\varepsilon \in [0.10, 0.75]$; crucially, per-generator split analysis recovers the identical partition in all eight hold-out generators independently (per-generator silhouette range 0.505--0.760; Appendix~\ref{app:ddr-validation}).
88	Per-generator TOST equivalence testing ($\varepsilon{=}|d|{<}0.20$, following Cohen's~\citeyearpar{cohen1988statistical} conventional threshold; gen-1 vs.\ gen-2+) confirms near-stationarity for entropy min (8/8 pass) and entropy max (6/8); tail decay passes for only 4/8, with $|d|{=}0.10$--$0.22$ spanning the boundary.
89	A permutation test ($n{=}10{,}000$) confirms the three-vs-four split is non-random ($p{=}0.030$; fixed-label silhouette\,=\,0.660 vs.\ null mean\,=\,0.46); exhaustive enumeration of all $\binom{7}{3}{=}35$ possible splits ranks this partition first (Appendix~\ref{app:ddr-validation}).
90	Reclassifying either boundary feature as intermediate preserves the core drifting/non-drifting split and leaves classification unchanged.
91	
92	\paragraph{Feature complementarity.}
93	The full 7-feature set (F1\,=\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
94	PCA confirms the three drifting features share a single latent dimension (92.3\% variance; Appendix~\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\,pp, confirming that DDR's contribution is identifying \emph{which} distributional properties drift, not classification per se.
95	TTR and hapax ratio ($r = 0.97$) are both retained for marginal LOFO gains despite feature masking \cite{strobl_conditional_2008} (Appendix~\ref{app:lofo}).
96	
97	\paragraph{Cross-family reference models.}
98	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Appendix~\ref{app:cross-ref}), bounding the same-family affinity effect; depth features are robust to reference model choice, though residual same-family proximity may inflate Pythia-family F1 by up to 1.3\,pp.
99	
100	\paragraph{Temperature and prompt-type sensitivity.}
101	All four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp binary F1); low-temperature improvement is family-dependent ($+7$--$9$\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen; Appendix~\ref{app:sampling-sensitivity}).
102	Continuation chains show the strongest drift (F1\,=\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\,=\,0.753; Appendix~\ref{app:prompt-type}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\ref{app:ddr-temp-stability}).
103	
104	
105	\subsection{Comparison with Detection Baselines}
106	\label{sec:results-baselines}
107	
108	Existing detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
109	
110	\begin{table}[t]
111	\centering
112	\footnotesize
113	\begin{tabular}{lcccc}
114	\toprule
115	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
116	\midrule
117	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
118	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
119	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
120	\midrule
121	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
122	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
123	LD-Score              & 1 & 0.630 & 0.675 & --- \\
124	Binoculars            & 1 & 0.411 & 0.539 & --- \\
125	\bottomrule
126	\end{tabular}
127	\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}
128	\label{tab:baselines}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
134	\caption{LOGO binary F1 vs.\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at 2.4$\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}
135	\label{fig:baseline-ci}
136	\end{figure}
137	
138	The 7-feature ensemble surpasses all individual baselines in 3-class F1 ($\Delta$\,=\,6.7--36.3\,pp; Figure~\ref{fig:baseline-ci}) and the pure 4-detector ensemble in binary F1 (0.705 vs.\ 0.700).
139	Adding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4$\times$ the inference cost.
140	This result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses (\S\ref{sec:discussion}).
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "4a42263c-535c-4fe4-a73f-226e2116e634"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 17216,
    "tool_uses": 2,
    "duration_ms": 2094
  },
  "last_tool_name": "Read",
  "uuid": "e5a7bc95-70a1-47f8-81a9-e0c56d5b5642",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01XHh4kfqcFqWWgRQcnrwMdZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "3ffaef17-4e21-422c-b9a4-b09c362ef517",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 18 · 2026-05-21T08:39:54.648Z_

<details><summary>↩ Tool result · `toolu_01XHh4kfqcFqWWgRQcnrwMdZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
8	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
9	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:generation}
13	
14	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
15	This selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
16	
17	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
18	The same pool of seed passages serves as gen-0 for all generators.
19	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
20	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
21	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
22	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
23	We generate up to depth~4 to empirically confirm convergence: 5-class analysis shows adjacent depths 2--4 become indistinguishable (F1\,$\approx$\,0.27; Appendix~\ref{app:finer-depth}), motivating the gen-2+ class collapse.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
26	
27	\subsection{Feature Extraction}
28	\label{sec:features}
29	
30	The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
31	This dual-view design enables the location/shape decomposition that constitutes our primary finding.
32	We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
33	Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
34	
35	We extract seven distributional features per text (Table~\ref{tab:features}), selected to provide principled coverage of the NLL distribution---location (mean), spread (std), extremes (max, min), and tail structure (decay)---complemented by two reference-free surface diversity measures.
36	We evaluated six additional NLL statistics (median, 90th percentile, IQR, CV, skewness, kurtosis) as candidate features; all exhibit $|r| > 0.65$ with existing features and yield no classification gain when added ($\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
37	
38	\begin{table}[t]
39	\centering
40	\footnotesize
41	\begin{tabular}{llp{3.8cm}}
42	\toprule
43	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
44	\midrule
45	entropy\_mean & Ref.\ NLL & Central tendency of token surprise \\
46	entropy\_std  & Ref.\ NLL & Spread of token surprise \\
47	entropy\_max  & Ref.\ NLL & Maximum token surprise \\
48	entropy\_min  & Ref.\ NLL & Minimum token surprise \\
49	tail\_decay   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
50	\midrule
51	TTR           & Surface & Type-token ratio \\
52	hapax\_ratio  & Surface & Proportion of hapax legomena \\
53	\bottomrule
54	\end{tabular}
55	\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}
56	\label{tab:features}
57	\end{table}
58	
59	\paragraph{Reference-model features.}
60	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
61	We use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.
62	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
63	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay---the slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.
64	
65	\paragraph{Surface features.}
66	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
67	
68	\paragraph{Feature complementarity.}
69	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
70	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
71	
72	\subsection{Evaluation Protocol}
73	\label{sec:evaluation}
74	
75	\paragraph{Cross-validation.}
76	To evaluate generalization, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.
77	LOGO holds out individual generators but does not isolate family effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
78	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
79	
80	\paragraph{Classifier.}
81	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
82	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power resides in the features, not the classifier.
83	
84	\paragraph{Metrics and statistical testing.}
85	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap CIs ($n{=}1{,}000$).
86	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
87	
88	\paragraph{Baselines.}
89	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
90	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
91	
92	\paragraph{Length confound control.}
93	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "68d6fda5-100c-4a3d-8338-91e6c39843e7"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/appendix_qlora.tex",
  "usage": {
    "total_tokens": 17221,
    "tool_uses": 3,
    "duration_ms": 2535
  },
  "last_tool_name": "Read",
  "uuid": "b3df1bdd-db2f-4e40-9f8c-44bb6e06fa39",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_019i3mY14Gvq87YdGhkEisjr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "80e2d4c4-9510-4726-abf6-fd724f486dce",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 21 · 2026-05-21T08:39:55.089Z_

<details><summary>↩ Tool result · `toolu_019i3mY14Gvq87YdGhkEisjr`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[ht]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "1c57a41d-ed13-4d1c-8365-e53f225195db"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/related_work.tex",
  "usage": {
    "total_tokens": 17226,
    "tool_uses": 4,
    "duration_ms": 2743
  },
  "last_tool_name": "Read",
  "uuid": "527c6f5b-7a46-4f23-808a-06138db7127b",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_019rfvz1HcKSy2LxpbW3DoMz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "58d69c23-e260-4822-9ac7-b8ce8c098bb6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 24 · 2026-05-21T08:39:55.297Z_

<details><summary>↩ Tool result · `toolu_019rfvz1HcKSy2LxpbW3DoMz`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, geometric invariants \cite{intrinsic_dim_detection}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
9	Several recent efforts move beyond the binary boundary---collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
10	Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \cite{uchendu_attribution,munir_looking_glass}.
11	
12	\subsection{Model Collapse and Iterative Generation}
13	\label{sec:related-collapse}
14	
15	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,briesch_self_consuming,seddik_synthetic_data}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}.
16	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \citet{schaeffer_collapse_position} identify eight distinct definitions of ``collapse,'' most tied to retraining dynamics.
17	We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
18	Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
19	We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
20	The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
21	
22	\subsection{Vocabulary Diversity and Stylometry}
23	\label{sec:related-diversity}
24	
25	Declining lexical diversity in LLM text is documented in both training \cite{curious_decline} and deployment settings \cite{writing_diversity}; MAUVE \cite{mauve} provides a divergence-based metric for quantifying this distributional gap.
26	Our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \cite{nucleus_sampling} constitutes a drifting component of DDR.
27	
28	\subsection{Data Quality and Provenance}
29	\label{sec:related-provenance}
30	
31	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
32	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
33	Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
34	\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "09c97bae-6437-441e-bd96-ed25b1fa7c18"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 17231,
    "tool_uses": 5,
    "duration_ms": 2957
  },
  "last_tool_name": "Read",
  "uuid": "469055fb-0ef9-4c66-b29f-85f730214f26",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01TrR8ND26veZrS6PkFaRLkE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "2d00ea9c-f471-428a-bc66-c1e9e4bcab69",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 17236,
    "tool_uses": 6,
    "duration_ms": 3169
  },
  "last_tool_name": "Read",
  "uuid": "b40dc942-7f79-4a58-9fd4-2a4e2a186b26",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01QVh46urg3UDr1bkb264nV8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "6dd9ca73-7ba9-4b49-8079-af2fc2ce3338",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 29 · 2026-05-21T08:39:55.781Z_

<details><summary>↩ Tool result · `toolu_01TrR8ND26veZrS6PkFaRLkE`</summary>

```text
1	% ===== Data Provenance / Contamination =====
2	
3	% ===== Statistics =====
4	
5	@book{cohen1988statistical,
6	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
7	  author = {Cohen, Jacob},
8	  edition = {2nd},
9	  publisher = {Lawrence Erlbaum Associates},
10	  year = {1988},
11	}
12	
13	% ===== Detection =====
14	
15	@inproceedings{detectgpt,
16	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
17	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
18	  booktitle = {Proceedings of the International Conference on Machine Learning},
19	  year = {2023},
20	}
21	
22	@inproceedings{gltr,
23	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
24	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
25	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
26	  year = {2019},
27	}
28	
29	@inproceedings{dna_gpt,
30	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
31	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
32	  booktitle = {Proceedings of the International Conference on Learning Representations},
33	  year = {2024},
34	}
35	
36	@inproceedings{binoculars,
37	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
38	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
39	  booktitle = {Proceedings of the International Conference on Machine Learning},
40	  year = {2024},
41	}
42	
43	@inproceedings{fast_detectgpt,
44	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
45	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
46	  booktitle = {Proceedings of the International Conference on Learning Representations},
47	  year = {2024},
48	}
49	
50	@article{ld_score,
51	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
52	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
53	  journal = {arXiv preprint arXiv:2605.01647},
54	  year = {2026},
55	}
56	
57	@inproceedings{diveye,
58	  title = {{Diversity Boosts AI-Generated Text Detection}},
59	  author = {Basani, Advik Raj and Chen, Pin-Yu},
60	  booktitle = {Proceedings of the International Conference on Learning Representations},
61	  year = {2026},
62	  eprint = {2509.18880},
63	  archiveprefix = {arXiv},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{intrinsic_dim_detection,
96	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
97	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2023},
100	}
101	
102	@inproceedings{grover,
103	  title = {{Defending Against Neural Fake News}},
104	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
105	  booktitle = {Advances in Neural Information Processing Systems},
106	  year = {2019},
107	}
108	
109	@article{release_strategies,
110	  title = {{Release Strategies and the Social Impacts of Language Models}},
111	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
112	  journal = {arXiv preprint arXiv:1908.09203},
113	  year = {2019},
114	}
115	
116	@inproceedings{beyond_binary,
117	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
118	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
119	  booktitle = {Proceedings of the ACM Web Conference},
120	  year = {2025},
121	}
122	
123	@inproceedings{semeval2024_task8,
124	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
125	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
126	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
127	  year = {2024},
128	}
129	
130	% ===== Model Collapse =====
131	
132	@inproceedings{self_consuming_mad,
133	  title = {{Self-Consuming Generative Models Go MAD}},
134	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
135	  booktitle = {Proceedings of the International Conference on Learning Representations},
136	  year = {2024},
137	}
138	
139	@article{curse_of_recursion,
140	  title = {{AI models collapse when trained on recursively generated data}},
141	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
142	  journal = {Nature},
143	  volume = {631},
144	  pages = {755--759},
145	  year = {2024},
146	}
147	
148	@inproceedings{strong_model_collapse,
149	  title = {{Strong Model Collapse}},
150	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
151	  booktitle = {Proceedings of the International Conference on Learning Representations},
152	  year = {2025},
153	}
154	
155	@inproceedings{model_collapse_avoidable,
156	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
157	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
158	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
159	  year = {2024},
160	}
161	
162	@inproceedings{schaeffer_collapse_position,
163	  title = {{Position: Model Collapse Does Not Mean What You Think}},
164	  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
165	  booktitle = {Proceedings of the International Conference on Machine Learning},
166	  year = {2025},
167	  eprint = {2503.03150},
168	  archiveprefix = {arXiv},
169	}
170	
171	@inproceedings{drayson_detection_prevents_collapse,
172	  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},
173	  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
174	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
175	  year = {2025},
176	  eprint = {2502.15654},
177	  archiveprefix = {arXiv},
178	}
179	
180	@article{seddik_synthetic_data,
181	  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
182	  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
183	  journal = {arXiv preprint arXiv:2404.05090},
184	  year = {2024},
185	}
186	
187	% ===== Fine-tuning =====
188	
189	@inproceedings{qlora,
190	  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
191	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
192	  booktitle = {Advances in Neural Information Processing Systems},
193	  year = {2023},
194	}
195	
196	% ===== Data Quality =====
197	
198	% ===== (orphan entries removed: fineweb, dolma) =====
199	
200	@inproceedings{dsir,
201	  title = {{Data Selection for Language Models via Importance Resampling}},
202	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
203	  booktitle = {Advances in Neural Information Processing Systems},
204	  year = {2023},
205	}
206	
207	@inproceedings{qurating,
208	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
209	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
210	  booktitle = {Proceedings of the International Conference on Machine Learning},
211	  year = {2024},
212	}
213	
214	@inproceedings{ccnet,
215	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
216	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
217	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
218	  year = {2020},
219	}
220	
221	% ===== Watermarking =====
222	
223	@inproceedings{watermark_llm,
224	  title = {{A Watermark for Large Language Models}},
225	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
226	  booktitle = {Proceedings of the International Conference on Machine Learning},
227	  year = {2023},
228	}
229	
230	@article{synthid_text,
231	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
232	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
233	  journal = {Nature},
234	  volume = {634},
235	  pages = {818--823},
236	  year = {2024},
237	}
238	
239	@misc{aaronson_watermark,
240	  title = {{Watermarking GPT Outputs}},
241	  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
242	  year = {2022},
243	  note = {Blog post},
244	  url = {https://scottaaronson.blog/?p=6823},
245	}
246	
247	@article{chainwash,
248	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
249	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
250	  journal = {arXiv preprint arXiv:2605.05503},
251	  year = {2026},
252	}
253	
254	% ===== Vocabulary Diversity =====
255	
256	@inproceedings{curious_decline,
257	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
258	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
259	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
260	  year = {2024},
261	}
262	
263	@inproceedings{writing_diversity,
264	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
265	  author = {Padmakumar, Vishakh and He, He},
266	  booktitle = {Proceedings of the International Conference on Learning Representations},
267	  year = {2024},
268	}
269	
270	@inproceedings{nucleus_sampling,
271	  title = {{The Curious Case of Neural Text Degeneration}},
272	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
273	  booktitle = {Proceedings of the International Conference on Learning Representations},
274	  year = {2020},
275	}
276	
277	% ===== Stylometry =====
278	
279	@article{stamatatos_survey,
280	  title = {{A Survey of Modern Authorship Attribution Methods}},
281	  author = {Stamatatos, Efstathios},
282	  journal = {Journal of the American Society for Information Science and Technology},
283	  volume = {60},
284	  number = {3},
285	  pages = {538--556},
286	  year = {2009},
287	}
288	
289	@article{koppel_authorship,
290	  title = {{Computational Methods in Authorship Attribution}},
291	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
292	  journal = {Journal of the American Society for Information Science and Technology},
293	  volume = {60},
294	  number = {1},
295	  pages = {9--26},
296	  year = {2009},
297	}
298	
299	@inproceedings{uchendu_attribution,
300	  title = {{Authorship Attribution for Neural Text Generation}},
301	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
302	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
303	  year = {2020},
304	}
305	
306	@inproceedings{munir_looking_glass,
307	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
308	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
309	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
310	  year = {2021},
311	}
312	
313	@article{briesch_self_consuming,
314	  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
315	  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
316	  journal = {arXiv preprint arXiv:2311.16822},
317	  year = {2023},
318	}
319	
320	% ===== Iterative Generation =====
321	
322	@inproceedings{broken_telephone,
323	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
324	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
325	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
326	  year = {2025},
327	}
328	
329	@article{markovian_chains,
330	  title = {{Markovian Generation Chains in Large Language Models}},
331	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
332	  journal = {arXiv preprint arXiv:2603.11228},
333	  year = {2026},
334	}
335	
336	@inproceedings{attractor_cycles,
337	  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},
338	  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
339	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
340	  year = {2025},
341	  eprint = {2502.15208},
342	  archiveprefix = {arXiv},
343	}
344	
345	% ===== Membership Inference =====
346	
347	@inproceedings{min_k_percent,
348	  title = {{Detecting Pretraining Data from Large Language Models}},
349	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
350	  booktitle = {Proceedings of the International Conference on Learning Representations},
351	  year = {2024},
352	}
353	
354	@article{koike_mia_detection,
355	  title = {{Machine Text Detectors are Membership Inference Attacks}},
356	  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},
357	  journal = {arXiv preprint arXiv:2510.19492},
358	  year = {2025},
359	}
360	
361	% ===== Survey =====
362	
363	@article{wu_survey_2025,
364	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
365	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
366	  journal = {Computational Linguistics},
367	  publisher = {MIT Press},
368	  year = {2025},
369	}
370	
371	@inproceedings{jawahar_survey,
372	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
373	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
374	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
375	  year = {2020},
376	}
377	
378	% ===== Models =====
379	
380	@inproceedings{pythia,
381	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
382	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
383	  booktitle = {Proceedings of the International Conference on Machine Learning},
384	  year = {2023},
385	}
386	
387	@inproceedings{olmo,
388	  title = {{OLMo: Accelerating the Science of Language Models}},
389	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
390	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
391	  year = {2024},
392	}
393	
394	@article{qwen3,
395	  title = {{Qwen3 Technical Report}},
396	  author = {{Qwen Team}},
397	  journal = {arXiv preprint arXiv:2505.09388},
398	  year = {2025},
399	}
400	
401	@inproceedings{ghostbuster,
402	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
403	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
404	  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
405	  year = {2024},
406	}
407	
408	@article{two_birds,
409	  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},
410	  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},
411	  journal = {arXiv preprint arXiv:2508.14190},
412	  year = {2025},
413	}
414	
415	@inproceedings{beyond_final_actor,
416	  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},
417	  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},
418	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
419	  year = {2026},
420	}
421	
422	% ===== Machine Learning =====
423	
424	@article{gutierrez_ordinal_survey,
425	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
426	  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
427	  journal = {IEEE Transactions on Knowledge and Data Engineering},
428	  volume = {28},
429	  number = {1},
430	  pages = {127--146},
431	  year = {2016},
432	}
433	
434	@article{coral_ordinal,
435	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
436	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
437	  journal = {Pattern Recognition Letters},
438	  volume = {140},
439	  pages = {325--331},
440	  year = {2020},
441	}
442	
443	@inproceedings{frank_hall_ordinal,
444	  title = {{A Simple Approach to Ordinal Classification}},
445	  author = {Frank, Eibe and Hall, Mark},
446	  booktitle = {Proceedings of the European Conference on Machine Learning},
447	  year = {2001},
448	}
449	
450	@article{corn_ordinal,
451	  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
452	  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
453	  journal = {Pattern Analysis and Applications},
454	  volume = {26},
455	  pages = {941--955},
456	  year = {2023},
457	}
458	
459	@inproceedings{kasa_ordinality_nlp,
460	  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
461	  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
462	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
463	  year = {2024},
464	}
465	
466	@inproceedings{xgboost,
467	  title = {{XGBoost: A Scalable Tree Boosting System}},
468	  author = {Chen, Tianqi and Guestrin, Carlos},
469	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
470	  year = {2016},
471	}
472	
473	@article{lakens_equivalence,
474	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
475	  author = {Lakens, Dani{\"e}l},
476	  journal = {Social Psychological and Personality Science},
477	  volume = {8},
478	  number = {4},
479	  pages = {355--362},
480	  year = {2017},
481	}
482	
483	% ===== Generator Model References =====
484	
485	@article{llama3,
486	  title = {{The Llama 3 Herd of Models}},
487	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
488	  journal = {arXiv preprint arXiv:2407.21783},
489	  year = {2024},
490	}
491	
492	@article{mistral7b,
493	  title = {{Mistral 7B}},
494	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
495	  journal = {arXiv preprint arXiv:2310.06825},
496	  year = {2023},
497	}
498	
499	@article{strobl_conditional_2008,
500	  title = {Conditional Variable Importance for Random Forests},
501	  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},
502	  journal = {BMC Bioinformatics},
503	  volume = {9},
504	  pages = {307},
505	  year = {2008},
506	}
507	
508	% --- Entries from Paper Agent (docs/paper) ---
509	
510	@inproceedings{dolma,
511	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
512	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
513	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
514	  year = {2024},
515	}
516	
517	
518	@inproceedings{fineweb,
519	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
520	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
521	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
522	  year = {2024},
523	}
524	
525	
526	@inproceedings{mapping_llm_science,
527	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
528	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
529	  booktitle = {Proceedings of the Conference on Language Modeling},
530	  year = {2024},
531	}
532	
533	
534	@inproceedings{monitoring_ai_review,
535	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
536	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
537	  booktitle = {Proceedings of the International Conference on Machine Learning},
538	  year = {2024},
539	}
540	
541	% ===== Stylometry =====
542	
543	
544	
545	@inproceedings{raid,
546	  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
547	  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
548	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
549	  year = {2024},
550	  address = {Bangkok, Thailand},
551	  publisher = {Association for Computational Linguistics},
552	  pages = {12463--12492},
553	}
554	
555	% ===== Distribution Quality =====
556	
557	@inproceedings{mauve,
558	  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},
559	  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},
560	  booktitle = {Advances in Neural Information Processing Systems},
561	  year = {2021},
562	}
563	
564	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "d6db34b3-feba-4cb9-a831-608b449bf17a"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T08:39:55.723Z_

<details><summary>↩ Tool result · `toolu_01QVh46urg3UDr1bkb264nV8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	AI text detection asks a single binary question---\emph{human or machine?}---and recent methods answer it with increasing reliability \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Yet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{recursive depths}---an estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.
6	While most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.
7	Knowing \emph{how many times} text has been recursively generated matters for data provenance \cite{ccnet,dsir} and model collapse analysis \cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.
8	
9	Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}.
10	We introduce \emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\,/\,gen-1\,/\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).
11	We term this location/shape asymmetry the \emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.
12	Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
13	
14	As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
15	
16	Our contributions:
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\,=\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---DDR identifies \emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.
19	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.
20	\end{enumerate}
21	A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "693333a2-0fae-486c-aa21-89a3f612561b"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 17241,
    "tool_uses": 7,
    "duration_ms": 3378
  },
  "last_tool_name": "Read",
  "uuid": "795e97d8-ddf4-49a2-9147-fb682fc06f06",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01WyF41sgEzGEcwi9L4tKr91`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "37548ae6-ed9a-43cf-a4e2-980a5c6cf5f9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 33 · 2026-05-21T08:39:55.933Z_

<details><summary>↩ Tool result · `toolu_01WyF41sgEzGEcwi9L4tKr91`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\subsection{Candidate Feature Screening}
69	\label{app:feature-candidate}
70	\input{appendix_feature_candidates}
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	
76	\section{Classifier Sensitivity}
77	\label{app:classifier}
78	\input{appendix_classifier}
79	\FloatBarrier
80	
81	\section{Robustness to Text Perturbation}
82	\label{app:human-edit}
83	\input{appendix_human_edit}
84	
85	\section{Cross-Domain Generalization}
86	\label{app:domain}
87	\input{appendix_domain}
88	
89	\section{Instruction-Tuned Model Analysis}
90	\label{app:instruct}
91	\input{appendix_instruct}
92	
93	\section{Error Analysis of Binary Classification}
94	\label{app:error-analysis}
95	\input{appendix_error_analysis}
96	
97	\section{Downstream Utility}
98	\label{app:downstream}
99	\input{appendix_downstream}
100	
101	\section{Cross-Model Chain Per-Class Detail}
102	\label{app:cross-model-detail}
103	\input{appendix_cross_model_detail}
104	
105	\section{Feature Distribution Analysis}
106	\label{app:feature-distributions}
107	\input{appendix_feature_distributions}
108	
109	\section{Cross-Temperature Transfer}
110	\label{app:cross-temp}
111	\input{appendix_cross_temp}
112	\FloatBarrier
113	
114	\section{Feature Ablation}
115	\label{app:ablation-table}
116	\input{appendix_ablation}
117	
118	\input{appendix_feature_correlation}
119	
120	\section{Cross-Family Reference Models}
121	\label{app:cross-ref}
122	\input{table4}
123	
124	\input{appendix_seed_control}
125	
126	\input{appendix_tost}
127	\FloatBarrier
128	
129	\input{appendix_tost_bootstrap}
130	
131	\section{DDR Partition Validation}
132	\label{app:ddr-validation}
133	\input{appendix_ddr_validation}
134	\FloatBarrier
135	
136	\section{Generator Subset Summary}
137	\label{app:gen-subsets-section}
138	\input{appendix_generator_subsets}
139	
140	\input{appendix_qualitative_examples}
141	
142	\section{Cross-Generator Transfer Analysis}
143	\label{app:transfer}
144	\input{appendix_transfer}
145	\FloatBarrier
146	
147	\section{Supplementary DDR Characterization}
148	\label{app:ddr-supplement}
149	
150	\subsection{Partition Stability Across Temperatures}
151	\label{app:ddr-temp-stability}
152	\input{appendix_temperature_stability}
153	
154	\subsection{Per-Feature Convergence Dynamics}
155	\label{app:convergence}
156	\input{appendix_convergence}
157	\FloatBarrier
158	
159	\subsection{DDR Causality Analysis}
160	\label{app:ddr-causality}
161	\input{appendix_ddr_causality}
162	
163	\subsection{Decoding Strategy Robustness}
164	\label{app:decoding-strategy}
165	\input{appendix_decoding_strategy}
166	
167	\input{appendix_9gen_scale}
168	
169	\subsection{Comparison with Concurrent Iterative-Generation Studies}
170	\label{app:iterative-comparison}
171	\input{appendix_iterative_comparison}
172	
173	\subsection{Token-Level NLL Distribution}
174	\label{app:nll-distribution}
175	\input{appendix_nll_distribution}
176	
177	\end{document}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "1d9e7b86-2cf3-43ae-8b5f-44ced95c538c"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0514_3/p…",
  "usage": {
    "total_tokens": 17246,
    "tool_uses": 8,
    "duration_ms": 3584
  },
  "last_tool_name": "Glob",
  "uuid": "92311e7c-3ff2-4dc0-8626-ed5ad8c118ec",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_01DrTVezSoUSbuNbGYdPQZcU`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "6e29f4c3-5d73-43cc-8f21-8f8619dffe70",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L2ALFukETcqeTXWun6n5ip",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17198,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17198,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 36 · 2026-05-21T08:39:56.144Z_

<details><summary>↩ Tool result · `toolu_01DrTVezSoUSbuNbGYdPQZcU`</summary>

```text
artifacts/_project/chart/fig1_ddr_v2.py
artifacts/_project/chart/fig1_combined_v1.py
artifacts/_project/chart/fig1_ddr_v3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "8b7d1a97-8249-4ee5-87da-2084bae0abfb"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for recursive generation depth",
  "usage": {
    "total_tokens": 42380,
    "tool_uses": 9,
    "duration_ms": 7120
  },
  "last_tool_name": "Grep",
  "uuid": "ff5199c0-1218-48f6-8900-964f8c8daf26",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01JK9SNTTUbJgjyiDR6P2BGf`</summary>

```json
{
  "pattern": "recursive generation depth",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "ca941af8-d57d-45b7-bd7c-51392b9d1e8d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 39 · 2026-05-21T08:39:59.690Z_

<details><summary>↩ Tool result · `toolu_01JK9SNTTUbJgjyiDR6P2BGf`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "5b19b15e-1712-4334-8557-9082caa1b670"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for DDR",
  "usage": {
    "total_tokens": 42381,
    "tool_uses": 10,
    "duration_ms": 7547
  },
  "last_tool_name": "Grep",
  "uuid": "6bc5f856-a035-4966-bb5e-d0ed1a6e1d6d",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mmunk34dV2Y9Trdd2hnZ5b`</summary>

```json
{
  "pattern": "DDR",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "9be32c4c-e1d4-4df8-bab7-0582bfbf0f0d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-21T08:40:00.112Z_

<details><summary>↩ Tool result · `toolu_01Mmunk34dV2Y9Trdd2hnZ5b`</summary>

```text
&lt;persisted-output>
Output too large (40.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/toolu_01Mmunk34dV2Y9Trdd2hnZ5b.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-24-
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "861face8-084f-4d58-af55-81a427715c1a"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for 6-gen",
  "usage": {
    "total_tokens": 42382,
    "tool_uses": 11,
    "duration_ms": 8172
  },
  "last_tool_name": "Grep",
  "uuid": "caf2611f-3978-47c5-b289-d11e4bedcf96",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Grep · `toolu_01Bc1vMZTZ6qHDP9d82UtMw7`</summary>

```json
{
  "pattern": "6-gen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "4e6d0f6b-ac04-4c90-978e-69d1f2fcb29b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-21T08:40:00.736Z_

<details><summary>↩ Tool result · `toolu_01Bc1vMZTZ6qHDP9d82UtMw7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-3-\paragraph{Setup.}
docs/paper/appendix_qlora.tex:4:We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-5-For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-6-All results use the same LOGO protocol as the main experiments.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
--
docs/paper/appendix_cross_temp.tex:1:Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-2-We evaluate four train$\rightarrow$test temperature conditions using Qwen3-1.7B data regenerated at $t{=}1.0$ (remaining five generators retain $t{=}0.7$).\footnote{The $t{=}1.0$ data uses top-$p{=}0.95$ (vs.\ $p{=}0.9$ for other configurations); this difference may contribute to the observed degradation beyond the temperature effect alone.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-3-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-5-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-6-\includegraphics[width=\columnwidth]{fig_appendix_cross_temp.pdf}
docs/paper/appendix_cross_temp.tex:7:[Omitted long matching line]
docs/paper/appendix_cross_temp.tex-8-\label{fig:cross-temp}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_cross_temp.tex-9-\end{figure}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-15-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-16-\end{tabular}}
docs/paper/appendix_confusion_matrix.tex:17:\caption{Aggregated 3-class confusion matrix from 6-generator LOGO evaluation ($N=27{,}529$). Each cell shows count and row-normalized percentage. Gen-0 is near-perfectly identified. Gen-1 errors are asymmetric: misclassification as gen-2+ (18.8\%) is 3$\times$ more frequent than as gen-0 (6.2\%). Gen-1 text already carries detectable recursive distortion.}
docs/paper/appendix_confusion_matrix.tex-18-\label{tab:confusion}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-19-\end{table}
--
docs/paper/appendix_lofo.tex:1:We complement the permutation importance analysis (\S\ref{sec:results-differential}) with a leave-one-feature-out ablation. Each row drops one of the seven features and re-evaluates the full 6-gen LOGO protocol; $\Delta$ is the change relative to the full 7-feature ensemble (F1\,=\,0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-3-\begin{table}[ht]
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-19-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-20-\end{tabular}
docs/paper/appendix_lofo.tex:21:\caption{Leave-one-feature-out ablation (6-gen LOGO). Each row drops one feature and re-evaluates with the LOGO protocol. Sorted by impact magnitude.}
docs/paper/appendix_lofo.tex-22-\label{tab:lofo}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_lofo.tex-23-\end{table}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-4-[Omitted long context line]
docs/paper/abstract.tex-5-Where prior work on iterative generation documents \emph{what converges}, the novel observation here is \emph{what is preserved}: shape invariance under the same process that compresses location provides the stable reference needed for depth estimation without per-generator calibration.
docs/paper/abstract.tex:6:As a proof of concept, a lightweight 7-feature ensemble exploiting DDR achieves leak-free binary F1\,=\,0.694 (gen-1 vs.\ gen-2+, effective resolution: three depth classes) under leave-one-generator-out evaluation, surpassing individual baselines and matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end classifier recovers substantially more (F1\,=\,0.905, 6-gen LOGO), establishing the analytical framework---not the specific features---as the primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-7-The signal attenuates under instruction tuning; current applicability is restricted to base models.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex-8-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-1-To verify that the depth signal resides in the features rather than the classifier,
docs/paper/appendix_classifier.tex:2:we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest
docs/paper/appendix_classifier.tex-3-in place of XGBoost (Table~\ref{tab:alt-classifier}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-4-All other settings (the same 7 features, 3-class labels, and class-balanced downsampling) are
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-7-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-8-\centering
docs/paper/appendix_classifier.tex:9:\caption{LOGO macro-F1 across three classifiers. Each column shows the held-out generator F1. (6-generator LOGO; 3-class.)}
docs/paper/appendix_classifier.tex-10-\label{tab:alt-classifier}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-11-\small
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-67-\noindent\begin{minipage}{\columnwidth}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-68-\scriptsize $^{\ast}$OLMo temperature experiments use OLMo-2-0425-1B (April 2025 release); the original OLMo-2-1B-hf weights are no longer publicly available.\par\vspace{1pt}
docs/paper/appendix_classifier.tex:69:$^{\dagger}$Pythia-2.8B and Qwen3-1.7B use 6-generator LOGO (pre-expansion); OLMo-2-1B and Qwen3-0.6B use 8-generator LOGO. Within-model comparisons are unaffected.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-70-\end{minipage}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-71-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-85-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-86-\includegraphics[width=\columnwidth]{fig_appendix_per_gen.pdf}
docs/paper/appendix_classifier.tex:87:\caption{Per-generator LOGO performance. (a) 8-generator binary and 3-class F1, sorted by binary F1. Dashed lines: pool average. (b) 6-generator LOGO detail heatmap showing the performance spread across model families.}
docs/paper/appendix_classifier.tex-88-\label{fig:per-gen}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-89-\end{figure}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-15-
docs/paper/introduction.tex-16-Our contributions:
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
docs/paper/discussion.tex:18:Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
docs/paper/discussion.tex-19-Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-20-Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "8bc0933f-43df-4672-8728-ba05a568334d"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for aaronson",
  "usage": {
    "total_tokens": 42383,
    "tool_uses": 12,
    "duration_ms": 8604
  },
  "last_tool_name": "Grep",
  "uuid": "53bd1e78-db27-497b-9821-93ab3c20e799",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01ECmSCSogQipdREXvbnKjMy`</summary>

```json
{
  "pattern": "aaronson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "bac7bb08-6a93-4471-bf83-e023f6458778",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-21T08:40:01.168Z_

<details><summary>↩ Tool result · `toolu_01ECmSCSogQipdREXvbnKjMy`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-31-Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
docs/paper/related_work.tex:32:Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-33-Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-34-\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-237-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-238-
docs/paper/references.bib:239:@misc{aaronson_watermark,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-240-  title = {{Watermarking GPT Outputs}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-241-  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-242-  year = {2022},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-243-  note = {Blog post},
docs/paper/references.bib:244:  url = {https://scottaaronson.blog/?p=6823},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-245-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-246-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e441a6e3-c482-4d95-a4ec-98659fd35eeb"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for ordinal",
  "usage": {
    "total_tokens": 42384,
    "tool_uses": 13,
    "duration_ms": 9233
  },
  "last_tool_name": "Grep",
  "uuid": "4f1605da-585d-4f54-aeef-d2adbcb0ffaa",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_015HzzAcW3WCRYcE1qCzwaaa`</summary>

```json
{
  "pattern": "ordinal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "57fd5280-277e-4ba8-92ab-b046b462fdd1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 51 · 2026-05-21T08:40:01.795Z_

<details><summary>↩ Tool result · `toolu_015HzzAcW3WCRYcE1qCzwaaa`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-7-The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, geometric invariants \cite{intrinsic_dim_detection}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
docs/paper/related_work.tex:8:RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-9-[Omitted long context line]
docs/paper/related_work.tex:10:Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \cite{uchendu_attribution,munir_looking_glass}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-12-\subsection{Model Collapse and Iterative Generation}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-31-Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-32-Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
docs/paper/related_work.tex:33:Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-34-\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-166-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-167-Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
docs/paper/appendix_ddr_validation.tex:168:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-169-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-170-\begin{table}[ht]
--
docs/paper/appendix_confusion_matrix.tex:1:Table~\ref{tab:confusion} reports the aggregated confusion matrix from the original six-generator subset (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B) under leave-one-generator-out (LOGO) evaluation, collapsed to three ordinal classes: gen-0 (human), gen-1 (first-generation), and gen-2+ (depth $\geq$ 2).
docs/paper/appendix_confusion_matrix.tex-2-The later-added Llama-3.2-3B and Mistral-7B-v0.3 are evaluated in the full 8-generator LOGO results (Table~\ref{tab:logo-results}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-3-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-28-\paragraph{Feature subset degradation.}
docs/paper/appendix_human_edit.tex-29-Table~\ref{tab:feature-degrade} compares perturbation robustness of the full 7-feature ensemble against an entropy-only subset (5 reference-model features).
docs/paper/appendix_human_edit.tex:30:The higher unperturbed binary F1 of the entropy-only subset (0.833 vs.\ 0.695) reflects the strong discriminability of reference-model features for the coarse binary task (gen-1 vs.\ gen-2+); however, lexical features are essential for the finer-grained ordinal task (3-class F1: 0.737 vs.\ 0.688) and provide greater robustness under perturbation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-31-At 20\% replacement, the 7-feature ensemble surpasses entropy-only on binary F1 (0.591 vs.\ 0.569), despite starting from a lower baseline.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_human_edit.tex-32-Random word replacement drastically alters per-token context and makes entropy features (computed over the full token sequence) extremely sensitive to noise.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-80-\paragraph{Classifier.}
docs/paper/method.tex-81-We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
docs/paper/method.tex:82:Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power resides in the features, not the classifier.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-83-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-84-\paragraph{Metrics and statistical testing.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-29-confirming that discriminative power originates in the entropy and lexical features,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-30-not in classifier capacity.
docs/paper/appendix_classifier.tex:31:Ordinal-specific methods (CORAL \cite{coral_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, which confirms that 3-class granularity provides insufficient resolution for ranking-aware losses to improve over standard multiclass classification.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-32-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_classifier.tex-33-\subsection*{Sampling Sensitivity Analysis}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-8-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-9-Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}.
docs/paper/introduction.tex:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-11-We term this location/shape asymmetry the \emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-17-\begin{enumerate}[nosep,leftmargin=*]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-18-[Omitted long context line]
docs/paper/introduction.tex:19:    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-20-\end{enumerate}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-21-A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-422-% ===== Machine Learning =====
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-423-
docs/paper/references.bib:424:@article{gutierrez_ordinal_survey,
docs/paper/references.bib-425-  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-426-  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-432-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-433-
docs/paper/references.bib:434:@article{coral_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-435-  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-436-  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-441-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-442-
docs/paper/references.bib:443:@inproceedings{frank_hall_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-444-  title = {{A Simple Approach to Ordinal Classification}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-445-  author = {Frank, Eibe and Hall, Mark},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-448-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-449-
docs/paper/references.bib:450:@article{corn_ordinal,
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-451-  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-452-  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-457-}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-458-
docs/paper/references.bib:459:@inproceedings{kasa_ordinality_nlp,
docs/paper/references.bib-460-  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-461-  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-48-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-49-\paragraph{Classifier comparison.}
docs/paper/appendix_finer_depth.tex:50:To verify that 5-class degradation reflects feature-level limitations rather than classifier choice, we evaluate four alternatives under the same protocol: HistGradientBoosting (macro F1\,=\,0.501, 95\% bootstrap CI [0.496, 0.506]), random forest (0.476), logistic regression (0.447), and Frank-Hall ordinal reduction (0.451).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_finer_depth.tex-51-All classifiers perform comparably to the default XGBoost ensemble (0.501), indicating that classifier capacity is not the bottleneck.
docs/paper/appendix_finer_depth.tex-52-The gen-2/gen-3 boundary is the primary failure mode across all methods: these two classes are effectively inseparable with the current feature set. This establishes 3-class granularity as the practical ceiling for surface and entropy features.
docs/paper/appendix_finer_depth.tex:53:At the 3-class level, ordinal-specific methods (CORAL ordinal regression, Frank-Hall reduction) similarly fail to improve over multiclass XGBoost (\S\ref{sec:results}), which confirms that the bottleneck is feature separability across all granularities, not the modeling of label ordinality.
--
docs/paper/results.tex-106-\label{sec:results-baselines}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-107-
docs/paper/results.tex:108:Existing detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-109-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-110-\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "61451ae7-c3c9-470d-80ac-d4a39ccedc04"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for \\$\\+\\$11\\.6|\\+11\\.6",
  "usage": {
    "total_tokens": 42385,
    "tool_uses": 14,
    "duration_ms": 9863
  },
  "last_tool_name": "Grep",
  "uuid": "52fe334e-7fda-45da-b1aa-dc57d864c030",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_011MR4BJaBFrCiAd3pDQJtYh`</summary>

```json
{
  "pattern": "\\$\\+\\$11\\.6|\\+11\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "726467d1-fdf5-400e-aa60-22a9bca0a1c7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 54 · 2026-05-21T08:40:02.424Z_

<details><summary>↩ Tool result · `toolu_011MR4BJaBFrCiAd3pDQJtYh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-26-On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "67a94ecd-ee8b-4a5b-8522-87e1c469ca3a"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Searching for QLoRA|qlora",
  "usage": {
    "total_tokens": 42386,
    "tool_uses": 15,
    "duration_ms": 10389
  },
  "last_tool_name": "Grep",
  "uuid": "3c27a15e-4c5d-4876-860d-4a62f6849bff",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_01HyoVyRjLbTj3d4f4vFtTuw`</summary>

```json
{
  "pattern": "QLoRA|qlora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "234ced8e-b7e2-4891-af19-00736dc8bed1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NEYRNUhV5eTU1YVxETjjFM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25128,
      "cache_read_input_tokens": 17198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25128,
        "ephemeral_1h_input_tokens": 0
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

_source line 57 · 2026-05-21T08:40:02.957Z_

<details><summary>↩ Tool result · `toolu_01HyoVyRjLbTj3d4f4vFtTuw`</summary>

```text
docs/paper/appendix_qlora.tex:1:To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-2-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-3-\paragraph{Setup.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-9-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-10-\small
docs/paper/appendix_qlora.tex:11:\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
docs/paper/appendix_qlora.tex:12:\label{tab:qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-13-\resizebox{\linewidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-14-\begin{tabular}{lccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-17-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-18-XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
docs/paper/appendix_qlora.tex:19:QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-20-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-21-\end{tabular}}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-24-\paragraph{Results.}
docs/paper/appendix_qlora.tex:25:QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
docs/paper/appendix_qlora.tex:26:On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
docs/paper/appendix_qlora.tex-27-The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex-28-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-58-\input{appendix_finer_depth}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-59-
docs/paper/main.tex:60:\section{End-to-End Depth Classification (QLoRA)}
docs/paper/main.tex:61:\label{app:qlora}
docs/paper/main.tex:62:\input{appendix_qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-63-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-64-\section{Leave-One-Feature-Out Analysis}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex-4-Recursive generation in base models imprints a systematic distributional signature---central-tendency features drift with depth while shape features remain stable---a dichotomy we term differential depth response (DDR), validated across eight generators from five families.
docs/paper/conclusion.tex-5-This enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: inference-chain drift compresses location while preserving shape, whereas retraining erodes both.
docs/paper/conclusion.tex:6:Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)---and frontier scale, where preliminary evidence suggests attenuated but persistent effects.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
docs/paper/discussion.tex:18:Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
docs/paper/discussion.tex-19-Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
docs/paper/discussion.tex:20:Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
docs/paper/discussion.tex-21-Cross-domain evaluation (News, Academic, Code; $t{=}1.0$) yields binary F1\,=\,0.74--0.75 but degraded 3-class F1 (0.62--0.65; Appendix~\ref{app:domain}), with temperature and domain effects confounded.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-22-Our generation chains use open-ended continuation prompts; real-world recursive pipelines---instruction-following chains, multi-turn dialogues, mixed-model editing---may attenuate, restructure, or introduce confounds not present in controlled chains.
--
docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-70-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-71-\paragraph{End-to-end instruct classification.}
docs/paper/appendix_instruct.tex:72:To test whether depth signal persists at the token level despite summary-statistic degradation, we apply the QLoRA end-to-end classifier (Appendix~\ref{app:qlora}) to instruction-tuned data using within-model 5-fold stratified CV (Table~\ref{tab:instruct-qlora}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-73-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-74-\begin{table}[ht]
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-75-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-76-\small
docs/paper/appendix_instruct.tex:77:\caption{End-to-end QLoRA vs.\ XGBoost on instruction-tuned data (within-model 5-fold CV, Qwen3-0.6B backbone). Base QLoRA rows shown for reference only; instruct sets ($N{\approx}4.4$--$5.0$K) are approximately twice the base sets ($N{\approx}2.3$K), so cross-condition comparison is confounded by training set size.}
docs/paper/appendix_instruct.tex:78:\label{tab:instruct-qlora}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-79-\resizebox{\linewidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-80-\begin{tabular}{lccccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-82-& \multicolumn{2}{c}{\textbf{3-class F1}} & & \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-83-\cmidrule(lr){2-3}
docs/paper/appendix_instruct.tex:84:\textbf{Model} & XGB & QLoRA & $\boldsymbol{\Delta}$ & \textbf{$N$} \\
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-85-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-86-OLMo-2-1B-Inst   & 0.575 & 0.888\,$\pm$\,0.007 & $+$31.3\,pp & 4{,}429 \\
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-93-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-94-
docs/paper/appendix_instruct.tex:95:The XGBoost-to-QLoRA gap on the same instruct data is substantial ($+$17.5 to $+$31.3\,pp), indicating that depth signal persists at the token level under instruction tuning but is inaccessible to the seven summary statistics; the degradation reported in Table~\ref{tab:instruct} reflects a feature-level limitation rather than signal absence.
docs/paper/appendix_instruct.tex:96:Note that instruct samples are approximately twice the base count used here (Table~\ref{tab:instruct-qlora}), so the instruct-vs-base QLoRA comparison is confounded by training set size; the meaningful comparison is QLoRA-vs-XGBoost on the same instruct data.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-97-All results use within-model 5-fold CV, not cross-generator LOGO, limiting generalization claims.
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-12-Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex-15-
docs/paper/introduction.tex-16-Our contributions:
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-187-% ===== Fine-tuning =====
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-188-
docs/paper/references.bib:189:@inproceedings{qlora,
docs/paper/references.bib:190:  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-191-  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib-192-  booktitle = {Advances in Neural Information Processing Systems},
--
docs/paper/appendix_generator_subsets.tex-13-Main LOGO (Table~\ref{tab:logo-results}) & 8 & All: Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B, Llama, Mistral \\
docs/paper/appendix_generator_subsets.tex-14-Cross-model chains (Table~\ref{tab:cross-ref}) & 5 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B \\
docs/paper/appendix_generator_subsets.tex:15:QLoRA (Table~\ref{tab:qlora}) & 6 & Py-2.8B/1B, OLMo, Qw-1.7B/0.6B/8B \\
docs/paper/appendix_generator_subsets.tex-16-Temperature ablation (Table~\ref{tab:sampling-ablation}) & 4 & Py-2.8B, OLMo, Qw-1.7B/0.6B \\
docs/paper/appendix_generator_subsets.tex-17-Prompt-type (Appendix~\ref{app:prompt-type}) & 1 & Py-2.8B only \\
--
docs/paper/results.tex-15-Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
docs/paper/results.tex-16-A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
docs/paper/results.tex:17:An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex-19-\paragraph{Length confound control.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "49980e33-bed7-4899-967e-719c7775e408"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/toolu_01Mmunk34dV2Y9Trdd2hnZ5b.txt",
  "usage": {
    "total_tokens": 61712,
    "tool_uses": 16,
    "duration_ms": 14210
  },
  "last_tool_name": "Read",
  "uuid": "38574977-0b54-40c1-9345-279533f79c9c",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_015LqTsV6fCZjqq8Nu1iNiLe`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/toolu_01Mmunk34dV2Y9Trdd2hnZ5b.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "bf96f909-2482-4f23-b623-cb1ac4b25302",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014j1yHFq47yoGUwyAA91LQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 19324,
      "cache_read_input_tokens": 42326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19324,
        "ephemeral_1h_input_tokens": 0
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

_source line 60 · 2026-05-21T08:40:07.208Z_

<details><summary>↩ Tool result · `toolu_015LqTsV6fCZjqq8Nu1iNiLe`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-17-We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
2	docs/paper/related_work.tex-18-Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
3	docs/paper/related_work.tex:19:We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
4	docs/paper/related_work.tex-20-The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
5	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-21-
6	--
7	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-24-
8	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-25-Declining lexical diversity in LLM text is documented in both training \cite{curious_decline} and deployment settings \cite{writing_diversity}; MAUVE \cite{mauve} provides a divergence-based metric for quantifying this distributional gap.
9	docs/paper/related_work.tex:26:Our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \cite{nucleus_sampling} constitutes a drifting component of DDR.
10	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-27-
11	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex-28-\subsection{Data Quality and Provenance}
12	--
13	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-31-
14	docs/paper/appendix_dataset_stats.tex-32-Figure~\ref{fig:violin} shows the full distribution of each feature across five generation depths (0--4), pooled across all eight generators ($N$\,=\,37{,}058).
15	docs/paper/appendix_dataset_stats.tex:33:The violin plots confirm the DDR pattern: drifting features (entropy mean, TTR, hapax ratio) show progressive narrowing and location shift, while shape features (entropy max, tail decay) maintain approximately constant distributions across depths.
16	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-34-
17	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_dataset_stats.tex-35-\begin{figure*}[!htbp]
18	--
19	docs/paper/appendix_feature_distributions.tex:1:\subsection*{DDR Trend Lines}
20	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-2-
21	docs/paper/appendix_feature_distributions.tex-3-Figure~\ref{fig:ddr-trends} shows the per-feature depth trend (mean across all samples at each depth) with individual generator traces overlaid.
22	docs/paper/appendix_feature_distributions.tex:4:The consistent downward trajectories for drifting features across all generators confirm that DDR is a universal property of recursive generation.
23	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-5-Shape features exhibit flat trajectories regardless of generator, with near-zero $R^2$ for the linear fit.
24	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-6-
25	--
26	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-8-\centering
27	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-9-\includegraphics[width=\textwidth]{fig_appendix_ddr_trends.pdf}
28	docs/paper/appendix_feature_distributions.tex:10:\caption{Per-feature depth trends. Bold line: pooled mean ($\pm$1.96\,SE shading) across all generators, colored by DDR zone (blue: drifting, wine: intermediate, amber: near-stationary). Thin traces: individual generators. Spearman $\rho$ and linear $R^2$ are annotated per panel.}
29	docs/paper/appendix_feature_distributions.tex-11-\label{fig:ddr-trends}
30	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_distributions.tex-12-\vspace{-0.5em}
31	--
32	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-1-\subsection*{Data-Driven Clustering}
33	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-2-
34	docs/paper/appendix_ddr_validation.tex:3:To assess the DDR partition structure and determine whether the drifting/non-drifting split is data-driven, we apply $k$-means clustering ($k \in \{2,3,4,5\}$) to the seven features in standardized $(|\rho|, d)$ space (Table~\ref{tab:clustering}).
35	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-4-
36	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-5-\begin{table}[ht]
37	--
38	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-22-The primary drifting/non-drifting split ($k{=}2$, silhouette\,=\,0.660) is the strongest cluster structure.
39	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-23-At $k{=}3$, entropy min forms its own cluster rather than joining the near-stationary group because its pooled $|\rho|{=}0.40$ (driven by the gen-0/gen-1 boundary) places it far from other near-stationary features in $\rho$ space.
40	docs/paper/appendix_ddr_validation.tex:24:The 3/1/3 DDR partition resolves this by using the gen-1 vs.\ gen-2+ Cohen's $d$ ($d{=}0.03$) to place entropy min in the near-stationary group, a domain-informed refinement that unsupervised clustering cannot recover from pooled statistics alone.
41	docs/paper/appendix_ddr_validation.tex:25:At $k{=}4$ (silhouette\,=\,0.571), entropy std separates from the near-stationary group, consistent with its intermediate DDR classification.
42	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-26-
43	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-27-\paragraph{Exhaustive partition enumeration.}
44	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-28-To confirm that the three-vs-four split is optimal rather than incidental, we enumerate all $\binom{7}{3}{=}35$ possible ways to assign three features to a ``drifting'' group and the remaining four to ``non-drifting,'' computing the silhouette score for each partition in standardized $(|\rho|, d)$ space.
45	docs/paper/appendix_ddr_validation.tex:29:The observed DDR partition (\{entropy mean, TTR, hapax ratio\}) achieves the highest silhouette (0.660), with a gap of 0.18 to the second-ranked split; 20 of 35 partitions produce negative silhouette scores.
46	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-30-
47	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-31-\paragraph{Per-generator replication.}
48	--
49	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-47-\begin{tabular}{llccc}
50	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-48-\toprule
51	docs/paper/appendix_ddr_validation.tex:49:\textbf{DDR Zone} & \textbf{Feature} & $\boldsymbol{\varepsilon{=}0.15}$ & $\boldsymbol{\varepsilon{=}0.20}$ & $\boldsymbol{\varepsilon{=}0.25}$ \\
52	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-50-\midrule
53	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-51-\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 0/8 & 0/8 & 0/8 \\
54	--
55	docs/paper/appendix_ddr_validation.tex-86-\label{app:epsilon-sweep}
56	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-87-
57	docs/paper/appendix_ddr_validation.tex:88:The DDR partition classifies features as non-stationary ($d \geq \varepsilon$) or stationary ($d < \varepsilon$) based on pooled Cohen's $d$ (\S\ref{sec:results-differential}).
58	docs/paper/appendix_ddr_validation.tex-89-Table~\ref{tab:epsilon-sweep} reports the critical $\varepsilon$ at which each feature's classification changes; the three drifting and three near-stationary features maintain their classification for all $\varepsilon \in [0.10, 0.75]$.
59	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-90-
60	--
61	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-97-\begin{tabular}{llcc}
62	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-98-\toprule
63	docs/paper/appendix_ddr_validation.tex:99:\textbf{DDR Zone} & \textbf{Feature} & \textbf{Pooled $d$} & \textbf{Stationary at $\varepsilon >$} \\
64	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-100-\midrule
65	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-101-\multirow{3}{*}{Drifting} & $\bar{H}$ (ent.\ mean) & 1.17 & 1.17 \\
66	--
67	docs/paper/appendix_ddr_validation.tex-118-\label{app:holdout-split}
68	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-119-
69	docs/paper/appendix_ddr_validation.tex:120:To confirm the DDR partition is not an artifact of the specific generator pool, we split the eight generators into disjoint selection (4) and validation (4) sets, compute per-subset pooled $(|\rho|, d)$, and check whether all seven features receive the same zone assignment in both subsets.
70	docs/paper/appendix_ddr_validation.tex-121-We evaluate two complementary splits to avoid dependence on a single partition:
71	docs/paper/appendix_ddr_validation.tex-122-Split~A selects \{Pythia-2.8B, Qwen3-1.7B, OLMo, Mistral\} (validation: Pythia-1B, Qwen3-0.6B, Qwen3-8B, Llama);
72	--
73	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-126-\centering
74	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-127-\small
75	docs/paper/appendix_ddr_validation.tex:128:\caption{Holdout split validation of the DDR partition. Selection (sel) and validation (val) $|\rho|$ and $d$ for two disjoint 4/4 generator splits. Zone assignment is identical across all four subsets for every feature.}
76	docs/paper/appendix_ddr_validation.tex-129-\label{tab:holdout-split}
77	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-130-\resizebox{\linewidth}{!}{%
78	--
79	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-166-
80	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-167-Levene tests reject equal variance between gen-1 and gen-2+ for drifting features ($p < 10^{-10}$; variance ratios 1.86--2.21).
81	docs/paper/appendix_ddr_validation.tex:168:To verify that the DDR partition is robust to this heteroscedasticity, we supplement pooled Cohen's $d$ with Glass's $\Delta$ (using the gen-1 standard deviation as denominator) and Cliff's $\delta$ (a non-parametric ordinal effect size; Table~\ref{tab:effect-sizes}).
82	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-169-
83	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_validation.tex-170-\begin{table}[ht]
84	--
85	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-129-\input{appendix_tost_bootstrap}
86	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-130-
87	docs/paper/main.tex:131:\section{DDR Partition Validation}
88	docs/paper/main.tex-132-\label{app:ddr-validation}
89	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-133-\input{appendix_ddr_validation}
90	--
91	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-145-\FloatBarrier
92	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-146-
93	docs/paper/main.tex:147:\section{Supplementary DDR Characterization}
94	docs/paper/main.tex-148-\label{app:ddr-supplement}
95	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-149-
96	--
97	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-157-\FloatBarrier
98	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-158-
99	docs/paper/main.tex:159:\subsection{DDR Causality Analysis}
100	docs/paper/main.tex-160-\label{app:ddr-causality}
101	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex-161-\input{appendix_ddr_causality}
102	--
103	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-20-
104	docs/paper/appendix_confusion_matrix.tex-21-Figure~\ref{fig:confusion-heatmap} provides a heatmap visualization of the confusion matrix.
105	docs/paper/appendix_confusion_matrix.tex:22:The row-normalized view highlights near-perfect gen-0 classification (99.4\% recall), gen-1 confusion primarily with gen-2+ (18.8\%) rather than gen-0 (6.2\%), and gen-2+ misclassification predominantly into gen-1 (23.3\%), consistent with DDR predictions.
106	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-23-
107	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_confusion_matrix.tex-24-\begin{figure}[H]
108	--
109	docs/paper/appendix_feature_candidates.tex-1-To verify that the seven retained features are not an arbitrary subset, we screened six additional NLL-distributional statistics as candidate features: median, 90th percentile (p90), interquartile range (IQR), coefficient of variation (CV), skewness, and kurtosis.
110	docs/paper/appendix_feature_candidates.tex:2:Table~\ref{tab:candidate-features} reports their DDR coordinates, classification impact, and correlation with retained features.
111	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-3-
112	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-4-\begin{table}[ht]
113	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-5-\centering
114	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-6-\small
115	docs/paper/appendix_feature_candidates.tex:7:\caption{Candidate feature screening. All six candidates fall in the drifting DDR zone and correlate strongly ($|r| > 0.65$) with existing features. Adding any combination to the baseline degrades or leaves unchanged LOGO 3-class F1; LOFO $\Delta > 0$ indicates that removing the candidate \emph{improves} classification.}
116	docs/paper/appendix_feature_candidates.tex-8-\label{tab:candidate-features}
117	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-9-\resizebox{\linewidth}{!}{%
118	--
119	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-26-Adding all six to the 6-feature baseline\footnote{Tail decay requires full-vocabulary logits unavailable in the token-NLL subset used for this analysis; we report 6-feature baselines for fair comparison.} reduces 3-class LOGO F1 from 0.733 to 0.722, consistent with overfitting from redundant inputs.
120	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_feature_candidates.tex-27-LOFO analysis on the extended 12-feature set confirms that removing skewness ($+$0.010), median ($+$0.008), or IQR ($+$0.007) \emph{improves} classification, indicating these features inject noise rather than signal.
121	docs/paper/appendix_feature_candidates.tex:28:The retained seven features span three complementary DDR zones (drifting, intermediate, near-stationary) and two modalities (reference-model NLL, surface lexical diversity); additional distributional statistics provide no incremental information.
122	--
123	docs/paper/conclusion.tex-2-\label{sec:conclusion}
124	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex-3-
125	docs/paper/conclusion.tex:4:Recursive generation in base models imprints a systematic distributional signature---central-tendency features drift with depth while shape features remain stable---a dichotomy we term differential depth response (DDR), validated across eight generators from five families.
126	docs/paper/conclusion.tex-5-This enables cross-generator depth classification (leak-free binary F1\,=\,0.694; end-to-end: 0.905) and provides an analytical lens complementary to model collapse: inference-chain drift compresses location while preserving shape, whereas retraining erodes both.
127	docs/paper/conclusion.tex:6:Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)---and frontier scale, where preliminary evidence suggests attenuated but persistent effects.
128	--
129	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-41-A plausible explanation is that Gemma-2's first-generation continuations occupy a region of feature space highly similar to human-written text (gen-0), causing systematic misclassification of gen-1 as gen-0 or gen-2+.
130	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-42-This constitutes an architecture-specific generalization limitation rather than a systemic failure of the depth fingerprinting approach.
131	docs/paper/appendix_9gen_scale.tex:43:Several architectural differences may explain this behavior: (a)~Gemma-2's distinct attention mechanism and SentencePiece tokenizer with a larger vocabulary may produce first-generation continuations whose feature-space signature closely resembles human text, causing systematic gen-0/gen-1 confusion; (b)~this anomaly does not affect DDR's validity for the remaining eight generators, where per-generator F1 shifts by at most 0.011 upon Gemma inclusion.
132	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-44-
133	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-45-\paragraph{Scale effect.}
134	--
135	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-48-
136	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-49-\paragraph{14B-parameter evidence.}
137	docs/paper/appendix_9gen_scale.tex:50:Preliminary evidence from a 14.7B generator (Qwen3-14B-Base) confirms that the DDR partition persists at larger scale: Cohen's $d$ for drifting features remains in the large-effect range ($d{=}0.78$--$1.12$), though Spearman $|\rho|$ attenuates by 21--35\%, with entropy mean falling just below the drifting threshold ($|\rho|{=}0.39 < 0.40$, $d{=}0.78$).
138	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_9gen_scale.tex-51-This scale-dependent signal compression is consistent with larger models producing more self-typical outputs that narrow inter-depth contrasts; the partition structure is preserved even as absolute effect sizes compress.
139	--
140	docs/paper/discussion.tex-13-Depth-aware filtering can serve as a prophylactic against model collapse \cite{drayson_detection_prevents_collapse}, though depth-stratified curation does not yet improve downstream training (TOST equivalence at $\varepsilon{=}{\pm}2\%$; Appendix~\ref{app:downstream}); the primary value lies in provenance, not training improvement.
141	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-14-
142	docs/paper/discussion.tex:15:DDR is mechanistically distinct from model collapse \cite{curse_of_recursion,strong_model_collapse}: retraining erodes tail coverage by updating weights, whereas inference-chain drift at fixed parameters shifts only location, leaving shape stable.
143	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-16-Prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---but not what is \emph{preserved}; this complementary observation enables depth detection without per-generator calibration.
144	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-17-The decomposition itself---identifying which distributional properties carry cross-generator depth signal---constitutes the analytical contribution, independent of whether shape stability originates from sampling truncation or deeper autoregressive properties.
145	docs/paper/discussion.tex-18-Three depth classes represent the practical resolution ceiling (5-class F1\,$\approx$\,0.50; Appendix~\ref{app:finer-depth}); QLoRA recovers more signal (F1\,=\,0.905, 6-gen LOGO; Appendix~\ref{app:qlora}), reflecting token-order patterns that aggregate statistics miss.
146	docs/paper/discussion.tex:19:Instruction-tuned models substantially compress DDR structure (silhouette 0.660$\to$0.372; entropy-mean $\rho$ reverses sign; 3-class F1 degrades 3.7--19.9\,pp), with model-dependent heterogeneity ruling out a uniform mechanism (Appendix~\ref{app:instruct}).
147	docs/paper/discussion.tex:20:Yet QLoRA recovers to 0.89--0.91 on instruct data, confirming that depth signal persists at the token-sequence level beyond DDR's summary-statistic decomposition.
148	docs/paper/discussion.tex-21-Cross-domain evaluation (News, Academic, Code; $t{=}1.0$) yields binary F1\,=\,0.74--0.75 but degraded 3-class F1 (0.62--0.65; Appendix~\ref{app:domain}), with temperature and domain effects confounded.
149	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex-22-Our generation chains use open-ended continuation prompts; real-world recursive pipelines---instruction-following chains, multi-turn dialogues, mixed-model editing---may attenuate, restructure, or introduce confounds not present in controlled chains.
150	--
151	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-28-  & Open-ended continuation (no meaning-preserving constraint)
152	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-29-  & Token-level NLL statistics (location, scale, shape) + lexical diversity
153	docs/paper/appendix_iterative_comparison.tex:30:  & Depth classification + DDR decomposition into generator \& depth effects
154	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-31-  & 0.6--8B (8 models)
155	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-32-  & 5
156	--
157	docs/paper/appendix_iterative_comparison.tex-38-Table~\ref{tab:iterative-comparison} compares this work with two concurrent studies on iterative LLM generation.
158	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_iterative_comparison.tex-39-All three examine how repeated inference transforms text, but differ in the chain operator (meaning-preserving vs.\ open-ended), the analytic lens (factuality decay, convergence dynamics, vs.\ distributional decomposition), and the downstream goal.
159	docs/paper/appendix_iterative_comparison.tex:40:Our continuation-chain setting, which imposes no semantic-preservation constraint, permits richer depth signal and enables the location/shape decomposition that defines DDR.
160	--
161	docs/paper/appendix_ddr_causality.tex:1:This appendix validates the causal predictive power of DDR features through three complementary analyses: permutation importance, Granger causality, and feature intervention.
162	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-2-
163	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-3-\paragraph{Permutation Importance.}
164	--
165	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-54-\paragraph{Key Findings.}
166	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-55-\begin{enumerate}[nosep,leftmargin=*]
167	docs/paper/appendix_ddr_causality.tex:56:\item \textbf{Drifting dominance.} The $5.5\times$ permutation-importance gap confirms that drifting features (entropy\_mean, ttr, hapax\_ratio) are the primary depth signal carriers, consistent with the DDR partition derived from convergence analysis (\S\ref{sec:results-differential}).
168	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-57-
169	docs/paper/appendix_ddr_causality.tex-58-\item \textbf{Entropy\_min lacks causal direction.} Beyond its small effect size (F1 drop\,=\,0.019), entropy\_min is the only feature without significant Granger causality ($p$\,=\,0.375). This strengthens the near-stationary classification: the feature is neither marginally important nor temporally predictive.
170	--
171	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-60-\item \textbf{Entropy\_max asymmetry.} Entropy\_max ranks fourth in permutation importance (F1 drop\,=\,0.070) but produces the largest degradation in the counterfactual intervention ($-$2.0\,pp), indicating that it provides unique signal not redundant with other features; its causal contribution exceeds its marginal importance.
172	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-61-
173	docs/paper/appendix_ddr_causality.tex:62:\item \textbf{Mistral heterogeneity.} In per-generator Granger tests, Mistral-7B shows non-significant hapax\_ratio and ttr ($p > 0.4$), though Fisher combination across generators remains significant. This generator-specific attenuation partly explains Mistral's lowest LOGO F1 (0.605) and suggests that DDR fingerprints are weaker in models with heavier repetition penalties.
174	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_ddr_causality.tex-63-\end{enumerate}
175	--
176	docs/paper/method.tex-30-The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
177	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-31-This dual-view design enables the location/shape decomposition that constitutes our primary finding.
178	docs/paper/method.tex:32:We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
179	docs/paper/method.tex-33-Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
180	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-34-
181	--
182	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-53-\bottomrule
183	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-54-\end{tabular}
184	docs/paper/method.tex:55:\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}
185	docs/paper/method.tex-56-\label{tab:features}
186	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-57-\end{table}
187	--
188	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-67-
189	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-68-\paragraph{Feature complementarity.}
190	docs/paper/method.tex:69:These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
191	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-70-TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
192	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex-71-
193	--
194	docs/paper/appendix_convergence.tex:1:This appendix visualizes per-feature convergence trajectories across generation depth, complementing the DDR analysis in \S\ref{sec:results-differential}.
195	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_convergence.tex-2-
196	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_convergence.tex-3-\begin{figure}[H]
197	--
198	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-50-Three-generator instruct LOGO yields binary F1\,=\,0.487, indicating weak cross-generator transfer under instruction tuning.
199	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-51-
200	docs/paper/appendix_instruct.tex:52:\paragraph{DDR structure under instruction tuning.}
201	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-53-$k{=}2$ clustering in $(|\rho|, d)$ space on pooled instruct features yields silhouette\,=\,0.372 (vs.\ 0.660 for base models), indicating that the clean drifting/non-drifting partition is substantially compressed.
202	docs/paper/appendix_instruct.tex-54-The compression is model-dependent: OLMo-Instruct shows near-zero $|\rho|$ for TTR and hapax (0.006, 0.025), while Qwen instruct models retain moderate correlations ($|\rho|{=}0.48$--$0.53$).
203	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-55-Cross-condition transfer is near chance in both directions (base$\rightarrow$instruct binary F1\,=\,0.490; instruct$\rightarrow$base F1\,=\,0.454), with the asymmetry ($-$0.036) suggesting that instruct-trained features generalize even less to base distributions than the reverse.
204	docs/paper/appendix_instruct.tex:56:These results indicate that instruction tuning compresses the feature-space structure underlying DDR rather than simply reversing feature directions (Figure~\ref{fig:instruct-ddr}).
205	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-57-
206	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-58-\begin{figure}[ht]
207	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-59-\centering
208	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-60-\includegraphics[width=\linewidth]{fig_appendix_instruct_ddr.pdf}
209	docs/paper/appendix_instruct.tex:61:\caption{DDR partition under base (left) vs.\ instruction-tuned (right) models. Bars show pooled $|d|$; markers show individual generators. Base models exhibit a clean drifting/non-drifting separation (silhouette\,=\,0.660); instruction tuning compresses all features toward zero, collapsing the partition (silhouette\,=\,0.372). Entropy max shifts from near-stationary to intermediate under instruct, while formerly drifting features (hapax, TTR) lose most of their effect size.}
210	docs/paper/appendix_instruct.tex-62-\label{fig:instruct-ddr}
211	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-63-\end{figure}
212	--
213	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-67-To test this, we replace the reference with Qwen3-0.6B-Instruct and recompute all features on the two instruct generators.
214	docs/paper/appendix_instruct.tex-68-The hypothesis is partially rejected: Qwen3-1.7B-Instruct shows mixed changes (entropy max $d$: $0.51 \to 0.08$, becoming near-stationary; entropy std $d$: $1.07 \to 1.51$, increasing), while OLMo-Instruct loses nearly all depth signal (entropy mean $d$: $1.33 \to 0.02$; tail decay $d$: $0.60 \to 0.06$).
215	docs/paper/appendix_instruct.tex:69:The model-dependent heterogeneity rules out reference mismatch as a universal explanation for instruct DDR degradation, supporting the interpretation that alignment fundamentally reshapes the generation dynamics rather than introducing a correctable measurement artifact.
216	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-70-
217	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_instruct.tex-71-\paragraph{End-to-end instruct classification.}
218	--
219	docs/paper/appendix_temperature_stability.tex:1:To assess whether the DDR three-way partition generalizes beyond the default temperature ($\tau{=}0.7$), we computed per-feature Cohen's $d$ (generation~1 vs.\ generation~2+) at $\tau \in \{0.5, 0.7, 0.9\}$ for all four generators in the temperature ablation (12 conditions total; Table~\ref{tab:ddr-temp-stability}).
220	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_temperature_stability.tex-2-
221	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_temperature_stability.tex-3-\begin{table}[ht]
222	--
223	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-3-\paragraph{Error asymmetry.}
224	docs/paper/appendix_error_analysis.tex-4-Errors are heavily asymmetric: 86.2\% are false negatives (gen-2+ predicted as gen-1) and only 13.8\% are false positives (gen-1 predicted as gen-2+).
225	docs/paper/appendix_error_analysis.tex:5:The classifier systematically under-predicts depth, consistent with the DDR pattern: shallow gen-2+ samples that have not yet accumulated sufficient distributional drift are indistinguishable from gen-1.
226	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-6-
227	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-7-\paragraph{Per-depth error rates.}
228	--
229	docs/paper/appendix_error_analysis.tex-39-In contrast, shape features show no discriminating power: entropy\_max ($p = 0.584$) and tail\_decay ($p = 0.653$).
230	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_error_analysis.tex-40-Misclassified gen-2+ samples have systematically higher TTR (0.464 vs.\ 0.302 for correct) and entropy\_mean (2.26 vs.\ 1.57); these samples retain gen-1-like lexical diversity and have not undergone the distributional convergence characteristic of deeper generations.
231	docs/paper/appendix_error_analysis.tex:41:This is consistent with the DDR pattern (\S\ref{sec:results-differential}): errors concentrate where depth-accumulated drift is insufficient, and shape features (which are near-stationary by design) provide no additional discriminative signal for error correction.
232	--
233	docs/paper/appendix_tost.tex-5-We adopt Cohen's conventional small effect size ($d{=}0.20$) \cite{cohen1988statistical} as the smallest effect of practical significance (SESOI): effects below this threshold are unlikely to be practically meaningful for depth discrimination.
234	docs/paper/appendix_tost.tex-6-LOFO analysis independently supports this choice: removing any near-stationary feature changes classification F1 by $\leq$1.5\,pp (Appendix~\ref{app:lofo}), linking the statistical threshold to classification irrelevance.
235	docs/paper/appendix_tost.tex:7:Sensitivity analysis at $\varepsilon \in \{0.15, 0.20, 0.25\}$ confirms the partition is robust to the bound choice (see DDR Validation appendix).
236	docs/paper/appendix_tost.tex-8-Table~\ref{tab:tost-per-gen} reports observed $|d|$; \checkmark{} marks features for which the TOST null hypothesis (non-equivalence) is rejected at $\alpha = 0.05$.
237	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-9-
238	--
239	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-11-All drifting and intermediate features fail equivalence uniformly, with $|d|$ ranging from 0.23 (entropy std, Mistral) to 1.40 (entropy mean, Pythia-1B).
240	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-12-The partition is robust at the individual-generator level, with entropy min as the most consistently stationary feature.
241	docs/paper/appendix_tost.tex:13:Figure~\ref{fig:ddr-scatter} visualizes the DDR partition in ($|\rho|$, $d$) space, showing a clear gap between the three groups.
242	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-14-
243	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-15-\begin{table}[ht]
244	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-16-\centering
245	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-17-\footnotesize
246	docs/paper/appendix_tost.tex:18:\caption{Per-generator TOST equivalence ($\varepsilon{=}|d|{<}0.20$, gen-1 vs.\ gen-2+). Observed $|d|$; \checkmark{} = equivalent ($p_{\mathrm{TOST}} < 0.05$). Features grouped by DDR partition.}
247	docs/paper/appendix_tost.tex-19-\label{tab:tost-per-gen}
248	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-20-\resizebox{\columnwidth}{!}{%
249	--
250	/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_tost.tex-42-\centering
251	
252	[Showing results with pagination = limit: 250]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e46947a8-3755-4227-a777-913083ea422a"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad94135ba66be0aed",
  "tool_use_id": "toolu_01FoXYVGvSdzCTiQkCPwapGv",
  "status": "completed",
  "output_file": "",
  "summary": "Read all paper source files",
  "usage": {
    "total_tokens": 75658,
    "tool_uses": 16,
    "duration_ms": 40038
  },
  "uuid": "073c08d5-1814-494d-9b54-8b0026ed46a7",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool result

_source line 62 · 2026-05-21T08:40:32.589Z_

<details><summary>↩ Tool result · `toolu_01FoXYVGvSdzCTiQkCPwapGv`</summary>

````text
Perfect! Now I have all the information. Let me compile the comprehensive findings report.

## COMPREHENSIVE FINDINGS REPORT

### FILES READ (Full Content)

I have successfully read all 7 requested files in full:

1. **results.tex** - 141 lines: Contains results section with depth classification performance metrics, differential depth response analysis, and baseline comparisons
2. **method.tex** - 94 lines: Documents task formulation, generation chain construction, feature extraction methodology, and evaluation protocol
3. **appendix_qlora.tex** - 36 lines: Details QLoRA end-to-end depth classification experiments with setup, results, and hyperparameter robustness analysis
4. **related_work.tex** - 35 lines: Covers related work in AI-generated text detection, model collapse, vocabulary diversity, stylometry, and data provenance
5. **references.bib** - 563 lines: Complete bibliography with 80+ citations covering detection methods, model collapse, fine-tuning, watermarking, and model papers
6. **introduction.tex** - 22 lines: Introduces depth fingerprinting concept, DDR principle, and key contributions
7. **main.tex** - 178 lines: Master document with structure, document class configuration, and appendix organization

### FIG1-RELATED PYTHON FILES FOUND

Located in `artifacts/_project/chart/`:
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v2.py`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_combined_v1.py`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v3.py`

### GREP SEARCH FINDINGS

#### 1. "recursive generation depth" - **NO MATCHES FOUND**

#### 2. "DDR" - **Extensive Matches (40+ occurrences)**

Key findings across the paper:

- **Results.tex Line 17**: "An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO (+11.6pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution."

- **Method.tex Line 32**: "We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification (+11.6pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition."

- **Introduction.tex Line 10**: Document defines DDR as "location/shape asymmetry" that is "a structural property of fixed-parameter autoregressive sampling"

- **Related Work.tex Line 19**: "DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration."

- **Discussion.tex Line 15-20**: Multiple references to DDR's mechanistic distinctness from model collapse and its structure under instruction tuning (silhouette compression 0.660→0.372)

- **Appendix references**: DDR Partition Validation (app:ddr-validation), DDR Causality Analysis (app:ddr-causality), Supplementary DDR Characterization (app:ddr-supplement), DDR Trends in feature distributions, Temperature stability of DDR partition

#### 3. "6-gen" - **Multiple Matches**

- **Appendix_qlora.tex Line 4**: "Evaluated on the original 6-generator subset; XGBoost 3-class F1=0.789"
- **Appendix_qlora.tex Line 25**: "QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO"
- **Appendix_cross_temp.tex Line 1**: "Figure~\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline"
- **Appendix_lofo.tex Line 1**: "Leave-one-feature-out ablation (6-gen LOGO)"
- **Appendix_confusion_matrix.tex Line 17**: "Aggregated 3-class confusion matrix from 6-generator LOGO evaluation (N=27,529)"
- **Appendix_classifier.tex Line 2**: "we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest"

#### 4. "aaronson" - **2 Matches**

- **Related_work.tex Line 32**: "Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches."

- **References.bib Line 239-244**: 
```bibtex
@misc{aaronson_watermark,
  title = {{Watermarking GPT Outputs}},
  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
  year = {2022},
  note = {Blog post},
  url = {https://scottaaronson.blog/?p=6823},
}
```

#### 5. "ordinal" - **8 Matches**

- **Related_work.tex Line 8**: "RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation."

- **Related_work.tex Line 10**: "Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task"

- **Related_work.tex Line 19**: "DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration."

- **Related_work.tex Line 33**: "Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth."

- **Method.tex Line 82**: "Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance"

- **Introduction.tex Line 19**: "We define generation depth classification as an ordinal prediction task"

- **References.bib**: Multiple ordinal-related entries (gutierrez_ordinal_survey, coral_ordinal, frank_hall_ordinal, corn_ordinal, kasa_ordinality_nlp)

#### 6. "$+$11.6" or "+11.6" - **3 Matches**

- **Results.tex Line 17**: "An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO ($+$11.6\,pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora})"

- **Method.tex Line 32**: "end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora})"

- **Appendix_qlora.tex Line 25**: "QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789)."

#### 7. "QLoRA" or "qlora" - **23 Matches**

Primary occurrences:
- **Appendix_qlora.tex**: Entire section dedicated to QLoRA experiments (36 lines)
- **Results.tex Line 17**: Main results mention of QLoRA performance
- **Method.tex Line 32**: Reference to QLoRA improving classification by +11.6pp
- **Introduction.tex Line 14**: "an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora})"
- **Discussion.tex Line 18**: "QLoRA recovers more signal (F1=0.905, 6-gen LOGO; Appendix~\ref{app:qlora})"
- **Discussion.tex Line 20**: "Yet QLoRA recovers to 0.89--0.91 on instruct data"
- **Conclusion.tex Line 6**: "Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)"
- **References.bib Line 189-193**: QLoRA citation (Dettmers et al., NeurIPS 2023)
- **Appendix_instruct.tex**: Multiple references to QLoRA performance on instruction-tuned models

### SUMMARY STATISTICS

- **Total files read**: 7 papers/documents (418 total lines)
- **Total grep patterns searched**: 7 queries
- **Patterns with matches**: 6/7 (all except "recursive generation depth")
- **Total DDR mentions**: 40+ occurrences across multiple files
- **QLoRA mentions**: 23 occurrences
- **6-gen references**: 12+ mentions
- **Ordinal classification references**: 8 matches
- **"Aaronson watermark" references**: 2 matches (cited work)
- **+11.6pp improvement references**: 3 critical mentions

The paper extensively documents differential depth response (DDR) as the core contribution, with QLoRA as an important validation experiment showing that end-to-end neural classifiers can recover deeper signal (0.905 F1) beyond the handcrafted features (0.789-0.694 F1 range).
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c854b664-0454-46a5-b50f-0de3f642b880",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to read multiple files from the paper source directory. The base path is `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/`. \n\nPlease read the following files in full:\n1. results.tex\n2. method.tex\n3. appendix_qlora.tex\n4. related_work.tex\n5. references.bib\n6. introduction.tex\n7. main.tex\n\nAlso glob for any fig1-related Python files in `artifacts/_project/chart/` under `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`.\n\nAnd grep across all .tex files in `docs/paper/` for:\n- \"recursive generation depth\"\n- \"DDR\"\n- \"6-gen\"\n- \"aaronson\"\n- \"ordinal\"\n- \"$+$11.6\" or \"+11.6\"\n- \"QLoRA\" or \"qlora\"\n\nReport all findings with file paths, line numbers, and surrounding context.",
    "agentId": "ad94135ba66be0aed",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information. Let me compile the comprehensive findings report.\n\n## COMPREHENSIVE FINDINGS REPORT\n\n### FILES READ (Full Content)\n\nI have successfully read all 7 requested files in full:\n\n1. **results.tex** - 141 lines: Contains results section with depth classification performance metrics, differential depth response analysis, and baseline comparisons\n2. **method.tex** - 94 lines: Documents task formulation, generation chain construction, feature extraction methodology, and evaluation protocol\n3. **appendix_qlora.tex** - 36 lines: Details QLoRA end-to-end depth classification experiments with setup, results, and hyperparameter robustness analysis\n4. **related_work.tex** - 35 lines: Covers related work in AI-generated text detection, model collapse, vocabulary diversity, stylometry, and data provenance\n5. **references.bib** - 563 lines: Complete bibliography with 80+ citations covering detection methods, model collapse, fine-tuning, watermarking, and model papers\n6. **introduction.tex** - 22 lines: Introduces depth fingerprinting concept, DDR principle, and key contributions\n7. **main.tex** - 178 lines: Master document with structure, document class configuration, and appendix organization\n\n### FIG1-RELATED PYTHON FILES FOUND\n\nLocated in `artifacts/_project/chart/`:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v2.py`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_combined_v1.py`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v3.py`\n\n### GREP SEARCH FINDINGS\n\n#### 1. \"recursive generation depth\" - **NO MATCHES FOUND**\n\n#### 2. \"DDR\" - **Extensive Matches (40+ occurrences)**\n\nKey findings across the paper:\n\n- **Results.tex Line 17**: \"An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO (+11.6pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.\"\n\n- **Method.tex Line 32**: \"We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification (+11.6pp, 6-gen LOGO; Appendix~\\ref{app:qlora}) but obscure the decomposition.\"\n\n- **Introduction.tex Line 10**: Document defines DDR as \"location/shape asymmetry\" that is \"a structural property of fixed-parameter autoregressive sampling\"\n\n- **Related Work.tex Line 19**: \"DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.\"\n\n- **Discussion.tex Line 15-20**: Multiple references to DDR's mechanistic distinctness from model collapse and its structure under instruction tuning (silhouette compression 0.660→0.372)\n\n- **Appendix references**: DDR Partition Validation (app:ddr-validation), DDR Causality Analysis (app:ddr-causality), Supplementary DDR Characterization (app:ddr-supplement), DDR Trends in feature distributions, Temperature stability of DDR partition\n\n#### 3. \"6-gen\" - **Multiple Matches**\n\n- **Appendix_qlora.tex Line 4**: \"Evaluated on the original 6-generator subset; XGBoost 3-class F1=0.789\"\n- **Appendix_qlora.tex Line 25**: \"QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO\"\n- **Appendix_cross_temp.tex Line 1**: \"Figure~\\ref{fig:cross-temp} shows cross-temperature transfer results for the 6-generator LOGO pipeline\"\n- **Appendix_lofo.tex Line 1**: \"Leave-one-feature-out ablation (6-gen LOGO)\"\n- **Appendix_confusion_matrix.tex Line 17**: \"Aggregated 3-class confusion matrix from 6-generator LOGO evaluation (N=27,529)\"\n- **Appendix_classifier.tex Line 2**: \"we repeat the 6-generator LOGO evaluation using Logistic Regression and Random Forest\"\n\n#### 4. \"aaronson\" - **2 Matches**\n\n- **Related_work.tex Line 32**: \"Proactive watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \\cite{chainwash}, motivating passive approaches.\"\n\n- **References.bib Line 239-244**: \n```bibtex\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Jan Hendrik},\n  year = {2022},\n  note = {Blog post},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n```\n\n#### 5. \"ordinal\" - **8 Matches**\n\n- **Related_work.tex Line 8**: \"RAID \\cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.\"\n\n- **Related_work.tex Line 10**: \"Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task\"\n\n- **Related_work.tex Line 19**: \"DDR isolates what converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.\"\n\n- **Related_work.tex Line 33**: \"Our NLL-based analysis connects to \\citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.\"\n\n- **Method.tex Line 82**: \"Alternative classifiers (CORAL \\cite{coral_ordinal}, CORN \\cite{corn_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) yield comparable performance\"\n\n- **Introduction.tex Line 19**: \"We define generation depth classification as an ordinal prediction task\"\n\n- **References.bib**: Multiple ordinal-related entries (gutierrez_ordinal_survey, coral_ordinal, frank_hall_ordinal, corn_ordinal, kasa_ordinality_nlp)\n\n#### 6. \"$+$11.6\" or \"+11.6\" - **3 Matches**\n\n- **Results.tex Line 17**: \"An end-to-end QLoRA classifier achieves 3-class F1=0.905 under 6-generator LOGO ($+$11.6\\,pp vs. the same-subset XGBoost baseline of 0.789; Appendix~\\ref{app:qlora})\"\n\n- **Method.tex Line 32**: \"end-to-end neural features improve classification ($+$11.6\\,pp, 6-gen LOGO; Appendix~\\ref{app:qlora})\"\n\n- **Appendix_qlora.tex Line 25**: \"QLoRA achieves 3-class LOGO F1=0.905 (±0.003) under 6-generator LOGO, a +11.6\\,pp improvement over the same-subset XGBoost baseline (0.789).\"\n\n#### 7. \"QLoRA\" or \"qlora\" - **23 Matches**\n\nPrimary occurrences:\n- **Appendix_qlora.tex**: Entire section dedicated to QLoRA experiments (36 lines)\n- **Results.tex Line 17**: Main results mention of QLoRA performance\n- **Method.tex Line 32**: Reference to QLoRA improving classification by +11.6pp\n- **Introduction.tex Line 14**: \"an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\\ref{app:qlora})\"\n- **Discussion.tex Line 18**: \"QLoRA recovers more signal (F1=0.905, 6-gen LOGO; Appendix~\\ref{app:qlora})\"\n- **Discussion.tex Line 20**: \"Yet QLoRA recovers to 0.89--0.91 on instruct data\"\n- **Conclusion.tex Line 6**: \"Current boundaries are instruction tuning---where alignment compresses DDR structure while token-level signal persists (QLoRA 0.89--0.91)\"\n- **References.bib Line 189-193**: QLoRA citation (Dettmers et al., NeurIPS 2023)\n- **Appendix_instruct.tex**: Multiple references to QLoRA performance on instruction-tuned models\n\n### SUMMARY STATISTICS\n\n- **Total files read**: 7 papers/documents (418 total lines)\n- **Total grep patterns searched**: 7 queries\n- **Patterns with matches**: 6/7 (all except \"recursive generation depth\")\n- **Total DDR mentions**: 40+ occurrences across multiple files\n- **QLoRA mentions**: 23 occurrences\n- **6-gen references**: 12+ mentions\n- **Ordinal classification references**: 8 matches\n- **\"Aaronson watermark\" references**: 2 matches (cited work)\n- **+11.6pp improvement references**: 3 critical mentions\n\nThe paper extensively documents differential depth response (DDR) as the core contribution, with QLoRA as an important validation experiment showing that end-to-end neural classifiers can recover deeper signal (0.905 F1) beyond the handcrafted features (0.789-0.694 F1 range)."
      }
    ],
    "totalDurationMs": 40039,
    "totalTokens": 78100,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 61650,
      "output_tokens": 2498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13946
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2498,
          "cache_read_input_tokens": 61650,
          "cache_creation_input_tokens": 13946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13946,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 8,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a comprehensive overview. Let me now read specific files I need to check and modify. Let me process each task:

**2a. R34-W3: QLoRA 6-gen subset 标注** - The grep results show that:
- `results.tex` line 17: already has "6-generator LOGO" and "+11.6pp vs. the same-subset XGBoost baseline"
- `method.tex` line 32: already has "6-gen LOGO"
- `appendix_qlora.tex` line 4 and 25: already has "6-generator subset" and "6-generator LOGO" and "same-subset XGBoost baseline"


This task is already complete.

**2b. R38-W3: 术语一致性** - "recursive generation depth" has no matches so it's already clean, but I need to examine DDR usage more carefully and check the Table 7 caption in `appendix_qlora.tex` along with the LoRA configuration consistency.

**2c. R37-M1: Figure 1/2 颜色一致性** - I need to read the Python source files for fig1 and fig2 to verify the color consistency.

**2d. R37-M3: aaronson_watermark bib** - Still need to address this item.

**2e. R37-R2: ordinal regression 引用** - I need to find and add the Diaz & Karampatziakis paper.

**2f. R35-M5: Bib first_author 修复** - I need to check the references.bib file for arXiv entries that need author fixes.

**2g. R34-V1: Float 位置优化** - I need to review the table and figure placements.

Now I'm going to read through the specific files I need to examine.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "3f09052b-8ff1-4b75-a850-cbeb181a8ea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 64_

Good overview. Let me now read the specific files I need to check and modify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "42ff9955-7aff-4f32-8ee5-307fe26b85fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01XzbmHBQo98mgocxMqecZc4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "aba542fc-96ca-4b14-b954-3cceaa4b5125",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 66 · 2026-05-21T08:40:44.352Z_

<details><summary>↩ Tool result · `toolu_01XzbmHBQo98mgocxMqecZc4`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Depth Classification Performance}
5	\label{sec:results-classification}
6	
7	The 7-feature ensemble achieves 3-class LOGO F1\,=\,0.762 (95\% CI [0.758, 0.766]; $N$\,=\,37{,}058) across eight generators from five families (Table~\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\,pp capturing generator selection uncertainty.
8	Because gen-0 seeds are shared across generators (\S\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\,$\approx$\,0.94), inflating the 3-class metric.
9	We therefore adopt \textbf{leak-free binary F1} (gen-1 vs.\ gen-2+)\,=\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.
10	Per-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\,=\,0.028), with the primary difficulty concentrated at the gen-1\,/\,gen-2+ boundary (Appendix~\ref{app:confusion}).
11	Note that CIs above reflect bootstrap sampling variability; the cross-generator range (9.1\,pp) captures the distinct and larger uncertainty of generator selection.
12	
13	\paragraph{Cross-model generalization.}
14	Cross-model chains (randomly selected generator per step) yield binary F1\,=\,0.830 (95\% CI [.818, .841]) under 5-generator LOGO.\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\,=\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}
15	Single-generator transfer (Appendix~\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\,=\,0.810; LOFO yields 0.686.
16	A scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\leq$0.013; \S\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\ref{app:domain}).
17	An end-to-end QLoRA classifier achieves 3-class F1\,=\,0.905 under 6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789; Appendix~\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.
18	
19	\paragraph{Length confound control.}
20	Length-matched subsampling yields binary F1\,=\,0.724 (vs.\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\ref{app:length}).
21	
22	\paragraph{Seed-sharing control.}
23	Seed-level demeaning (F1\,=\,0.701) and an independent-seed experiment with disjoint seed pools (F1\,=\,0.680; Appendix~\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.
24	
25	\begin{table}[t]
26	\centering
27	\footnotesize
28	\resizebox{\columnwidth}{!}{%
29	\begin{tabular}{llcccc}
30	\toprule
31	\textbf{Model} & \textbf{Family} & \textbf{Params} & \textbf{Bin F1} & \textbf{95\% CI} & \textbf{3-cl F1}$^{\dagger}$ \\
32	\midrule
33	Pythia-2.8B     & Pythia  & 2.8B & \textbf{0.724} & [.707, .742] & 0.798 \\
34	Pythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \textbf{0.806} \\
35	Qwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\
36	Llama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\
37	OLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\
38	Qwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\
39	Qwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\
40	Mistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\
41	\midrule
42	\multicolumn{3}{l}{\textbf{Average (8-gen LOGO)}} & \textbf{0.694} & [.688, .700] & \textbf{0.762} \\
43	\multicolumn{3}{l}{\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\
44	\bottomrule
45	\end{tabular}}
46	\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\% CIs, $n$\,=\,1000). Binary F1 (gen-1 vs.\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\,=\,0.028, IQR\,=\,[0.692, 0.714]. $^{\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\S\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\,=\,0.680; Appendix~\ref{app:seed-control}).}
47	\label{tab:logo-results}
48	\end{table}
49	
50	\subsection{Differential Depth Response}
51	\label{sec:results-differential}
52	
53	\begin{figure*}[t]
54	\centering
55	\includegraphics[width=\textwidth]{fig_ddr_trajectory.pdf}
56	\caption{Feature trajectories across generation depth. \textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\rho| > 0.59$). \textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the differential depth response (DDR).}
57	\label{fig:ddr-trajectory}
58	\end{figure*}
59	
60	Not all distributional properties respond equally to recursive generation.
61	Figure~\ref{fig:ddr-trajectory} reveals a striking dichotomy that holds across all eight generators: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.
62	We term this asymmetry the \emph{differential depth response} (DDR).
63	The primary partition is binary: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields silhouette\,=\,0.660 (Appendix~\ref{app:ddr-validation}), cleanly separating three \emph{drifting} features ($|\rho| > 0.60$, $d{=}0.76$--$1.17$) from four \emph{non-drifting} ones ($d \leq 0.55$); higher $k$ degrades cluster quality ($k{=}3$: silhouette\,=\,0.532).
64	A domain-informed refinement resolves entropy std as a sole \emph{intermediate} member ($d{=}0.55$, $|\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\% vs.\ $>$15\% for drifting features).
65	Convergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\S\ref{sec:results-differential}, Quantification).
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
70	\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}
71	\label{fig:feature-drift}
72	\end{figure}
73	
74	Pooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\ref{fig:feature-drift}):
75	drifting features show substantial monotonic trends (hapax ratio $\rho = -0.64$, TTR $\rho = -0.63$, entropy mean $\rho = -0.60$),
76	while non-drifting features remain near-zero (tail decay $|\rho| = 0.04$; per-depth distributions in Appendix~\ref{app:feature-distributions}).
77	The six-fold magnitude gap between drifting ($|\rho| > 0.60$) and non-drifting features ($|\rho| \leq 0.16$) defines the DDR partition.
78	Within the non-drifting group, entropy std ($|\rho| = 0.16$, $d{=}0.55$) shows a substantial level shift despite low monotonicity, distinguishing it from the three near-stationary features ($d < 0.10$); this refinement is stable across $d$ thresholds in $[0.56, 0.75]$ (Appendix~\ref{app:ddr-validation}).
79	
80	\paragraph{Quantification.}
81	Convergence across parametric and non-parametric effect-size measures confirm the split.
82	Cohen's $d$ \cite{cohen1988statistical} shows a ${\geq}7\times$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary features ($d \leq 0.08$); KS statistics, Glass's $\Delta$, Cliff's $\delta$, and CV shift all corroborate (Appendix~\ref{app:ddr-validation}).
83	Four features fall cleanly into drifting or non-drifting groups.
84	Entropy min and tail decay are \emph{boundary features}: entropy min is near-stationary for gen-1 vs.\ gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1 ($|\rho|{=}0.40$); tail decay is \emph{weakly stationary}, passing TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).
85	Entropy std ($d{=}0.55$, $|\rho|{=}0.16$) is the sole intermediate member.
86	\paragraph{Validation.}
87	The drifting/non-drifting boundary is validated by convergent evidence: $k{=}2$ clustering in standardized $(|\rho|, d)$ space yields a clean separation (silhouette\,=\,0.660), invariant across threshold choices $\varepsilon \in [0.10, 0.75]$; crucially, per-generator split analysis recovers the identical partition in all eight hold-out generators independently (per-generator silhouette range 0.505--0.760; Appendix~\ref{app:ddr-validation}).
88	Per-generator TOST equivalence testing ($\varepsilon{=}|d|{<}0.20$, following Cohen's~\citeyearpar{cohen1988statistical} conventional threshold; gen-1 vs.\ gen-2+) confirms near-stationarity for entropy min (8/8 pass) and entropy max (6/8); tail decay passes for only 4/8, with $|d|{=}0.10$--$0.22$ spanning the boundary.
89	A permutation test ($n{=}10{,}000$) confirms the three-vs-four split is non-random ($p{=}0.030$; fixed-label silhouette\,=\,0.660 vs.\ null mean\,=\,0.46); exhaustive enumeration of all $\binom{7}{3}{=}35$ possible splits ranks this partition first (Appendix~\ref{app:ddr-validation}).
90	Reclassifying either boundary feature as intermediate preserves the core drifting/non-drifting split and leaves classification unchanged.
91	
92	\paragraph{Feature complementarity.}
93	The full 7-feature set (F1\,=\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \approx 0$; Appendix~\ref{app:ablation-table}).
94	PCA confirms the three drifting features share a single latent dimension (92.3\% variance; Appendix~\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\,pp, confirming that DDR's contribution is identifying \emph{which} distributional properties drift, not classification per se.
95	TTR and hapax ratio ($r = 0.97$) are both retained for marginal LOFO gains despite feature masking \cite{strobl_conditional_2008} (Appendix~\ref{app:lofo}).
96	
97	\paragraph{Cross-family reference models.}
98	Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Appendix~\ref{app:cross-ref}), bounding the same-family affinity effect; depth features are robust to reference model choice, though residual same-family proximity may inflate Pythia-family F1 by up to 1.3\,pp.
99	
100	\paragraph{Temperature and prompt-type sensitivity.}
101	All four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\,pp binary F1); low-temperature improvement is family-dependent ($+7$--$9$\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen; Appendix~\ref{app:sampling-sensitivity}).
102	Continuation chains show the strongest drift (F1\,=\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\,=\,0.753; Appendix~\ref{app:prompt-type}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\ref{app:ddr-temp-stability}).
103	
104	
105	\subsection{Comparison with Detection Baselines}
106	\label{sec:results-baselines}
107	
108	Existing detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\ref{tab:baselines}).
109	
110	\begin{table}[t]
111	\centering
112	\footnotesize
113	\begin{tabular}{lcccc}
114	\toprule
115	\textbf{Method} & \textbf{Feat.} & \textbf{3-cl F1} & \textbf{Bin F1} & \textbf{ms/text} \\
116	\midrule
117	4-det.\ + surface     & 6 & \textbf{0.795} & \textbf{0.708} & 22.8 \\
118	4-detector ens.\      & 4 & 0.785 & 0.700 & 22.8 \\
119	7-feature (ours)      & 7 & 0.774 & 0.705 & \textbf{9.7} \\
120	\midrule
121	Avg-LogProb           & 1 & 0.707 & 0.673 & --- \\
122	FastDetectGPT         & 1 & 0.660 & 0.569 & --- \\
123	LD-Score              & 1 & 0.630 & 0.675 & --- \\
124	Binoculars            & 1 & 0.411 & 0.539 & --- \\
125	\bottomrule
126	\end{tabular}
127	\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}
128	\label{tab:baselines}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.pdf}
134	\caption{LOGO binary F1 vs.\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at 2.4$\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}
135	\label{fig:baseline-ci}
136	\end{figure}
137	
138	The 7-feature ensemble surpasses all individual baselines in 3-class F1 ($\Delta$\,=\,6.7--36.3\,pp; Figure~\ref{fig:baseline-ci}) and the pure 4-detector ensemble in binary F1 (0.705 vs.\ 0.700).
139	Adding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4$\times$ the inference cost.
140	This result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses (\S\ref{sec:discussion}).
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e9cb6375-047c-4698-bdf5-c3d17b509364",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nThe 7-feature ensemble achieves 3-class LOGO F1\\,=\\,0.762 (95\\% CI [0.758, 0.766]; $N$\\,=\\,37{,}058) across eight generators from five families (Table~\\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\\,pp capturing generator selection uncertainty.\nBecause gen-0 seeds are shared across generators (\\S\\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\\,$\\approx$\\,0.94), inflating the 3-class metric.\nWe therefore adopt \\textbf{leak-free binary F1} (gen-1 vs.\\ gen-2+)\\,=\\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.\nPer-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\\,=\\,0.028), with the primary difficulty concentrated at the gen-1\\,/\\,gen-2+ boundary (Appendix~\\ref{app:confusion}).\nNote that CIs above reflect bootstrap sampling variability; the cross-generator range (9.1\\,pp) captures the distinct and larger uncertainty of generator selection.\n\n\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield binary F1\\,=\\,0.830 (95\\% CI [.818, .841]) under 5-generator LOGO.\\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\\,=\\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}\nSingle-generator transfer (Appendix~\\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\\,=\\,0.810; LOFO yields 0.686.\nA scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\\leq$0.013; \\S\\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\\ref{app:domain}).\nAn end-to-end QLoRA classifier achieves 3-class F1\\,=\\,0.905 under 6-generator LOGO ($+$11.6\\,pp vs.\\ the same-subset XGBoost baseline of 0.789; Appendix~\\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.\n\n\\paragraph{Length confound control.}\nLength-matched subsampling yields binary F1\\,=\\,0.724 (vs.\\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\\ref{app:length}).\n\n\\paragraph{Seed-sharing control.}\nSeed-level demeaning (F1\\,=\\,0.701) and an independent-seed experiment with disjoint seed pools (F1\\,=\\,0.680; Appendix~\\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{Params} & \\textbf{Bin F1} & \\textbf{95\\% CI} & \\textbf{3-cl F1}$^{\\dagger}$ \\\\\n\\midrule\nPythia-2.8B     & Pythia  & 2.8B & \\textbf{0.724} & [.707, .742] & 0.798 \\\\\nPythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \\textbf{0.806} \\\\\nQwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\\\\nLlama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\\\\nOLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\\\\nQwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\\\\nQwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\\\\nMistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Average (8-gen LOGO)}} & \\textbf{0.694} & [.688, .700] & \\textbf{0.762} \\\\\n\\multicolumn{3}{l}{\\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\\% CIs, $n$\\,=\\,1000). Binary F1 (gen-1 vs.\\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\\,=\\,0.028, IQR\\,=\\,[0.692, 0.714]. $^{\\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\\S\\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\\,=\\,0.680; Appendix~\\ref{app:seed-control}).}\n\\label{tab:logo-results}\n\\end{table}\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_ddr_trajectory.pdf}\n\\caption{Feature trajectories across generation depth. \\textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\\rho| > 0.59$). \\textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the differential depth response (DDR).}\n\\label{fig:ddr-trajectory}\n\\end{figure*}\n\nNot all distributional properties respond equally to recursive generation.\nFigure~\\ref{fig:ddr-trajectory} reveals a striking dichotomy that holds across all eight generators: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.\nWe term this asymmetry the \\emph{differential depth response} (DDR).\nThe primary partition is binary: $k{=}2$ clustering in standardized $(|\\rho|, d)$ space yields silhouette\\,=\\,0.660 (Appendix~\\ref{app:ddr-validation}), cleanly separating three \\emph{drifting} features ($|\\rho| > 0.60$, $d{=}0.76$--$1.17$) from four \\emph{non-drifting} ones ($d \\leq 0.55$); higher $k$ degrades cluster quality ($k{=}3$: silhouette\\,=\\,0.532).\nA domain-informed refinement resolves entropy std as a sole \\emph{intermediate} member ($d{=}0.55$, $|\\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\\% vs.\\ $>$15\\% for drifting features).\nConvergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\\S\\ref{sec:results-differential}, Quantification).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nPooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\\ref{fig:feature-drift}):\ndrifting features show substantial monotonic trends (hapax ratio $\\rho = -0.64$, TTR $\\rho = -0.63$, entropy mean $\\rho = -0.60$),\nwhile non-drifting features remain near-zero (tail decay $|\\rho| = 0.04$; per-depth distributions in Appendix~\\ref{app:feature-distributions}).\nThe six-fold magnitude gap between drifting ($|\\rho| > 0.60$) and non-drifting features ($|\\rho| \\leq 0.16$) defines the DDR partition.\nWithin the non-drifting group, entropy std ($|\\rho| = 0.16$, $d{=}0.55$) shows a substantial level shift despite low monotonicity, distinguishing it from the three near-stationary features ($d < 0.10$); this refinement is stable across $d$ thresholds in $[0.56, 0.75]$ (Appendix~\\ref{app:ddr-validation}).\n\n\\paragraph{Quantification.}\nConvergence across parametric and non-parametric effect-size measures confirm the split.\nCohen's $d$ \\cite{cohen1988statistical} shows a ${\\geq}7\\times$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary features ($d \\leq 0.08$); KS statistics, Glass's $\\Delta$, Cliff's $\\delta$, and CV shift all corroborate (Appendix~\\ref{app:ddr-validation}).\nFour features fall cleanly into drifting or non-drifting groups.\nEntropy min and tail decay are \\emph{boundary features}: entropy min is near-stationary for gen-1 vs.\\ gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1 ($|\\rho|{=}0.40$); tail decay is \\emph{weakly stationary}, passing TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).\nEntropy std ($d{=}0.55$, $|\\rho|{=}0.16$) is the sole intermediate member.\n\\paragraph{Validation.}\nThe drifting/non-drifting boundary is validated by convergent evidence: $k{=}2$ clustering in standardized $(|\\rho|, d)$ space yields a clean separation (silhouette\\,=\\,0.660), invariant across threshold choices $\\varepsilon \\in [0.10, 0.75]$; crucially, per-generator split analysis recovers the identical partition in all eight hold-out generators independently (per-generator silhouette range 0.505--0.760; Appendix~\\ref{app:ddr-validation}).\nPer-generator TOST equivalence testing ($\\varepsilon{=}|d|{<}0.20$, following Cohen's~\\citeyearpar{cohen1988statistical} conventional threshold; gen-1 vs.\\ gen-2+) confirms near-stationarity for entropy min (8/8 pass) and entropy max (6/8); tail decay passes for only 4/8, with $|d|{=}0.10$--$0.22$ spanning the boundary.\nA permutation test ($n{=}10{,}000$) confirms the three-vs-four split is non-random ($p{=}0.030$; fixed-label silhouette\\,=\\,0.660 vs.\\ null mean\\,=\\,0.46); exhaustive enumeration of all $\\binom{7}{3}{=}35$ possible splits ranks this partition first (Appendix~\\ref{app:ddr-validation}).\nReclassifying either boundary feature as intermediate preserves the core drifting/non-drifting split and leaves classification unchanged.\n\n\\paragraph{Feature complementarity.}\nThe full 7-feature set (F1\\,=\\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \\approx 0$; Appendix~\\ref{app:ablation-table}).\nPCA confirms the three drifting features share a single latent dimension (92.3\\% variance; Appendix~\\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\\,pp, confirming that DDR's contribution is identifying \\emph{which} distributional properties drift, not classification per se.\nTTR and hapax ratio ($r = 0.97$) are both retained for marginal LOFO gains despite feature masking \\cite{strobl_conditional_2008} (Appendix~\\ref{app:lofo}).\n\n\\paragraph{Cross-family reference models.}\nAlternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Appendix~\\ref{app:cross-ref}), bounding the same-family affinity effect; depth features are robust to reference model choice, though residual same-family proximity may inflate Pythia-family F1 by up to 1.3\\,pp.\n\n\\paragraph{Temperature and prompt-type sensitivity.}\nAll four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\\,pp binary F1); low-temperature improvement is family-dependent ($+7$--$9$\\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen; Appendix~\\ref{app:sampling-sensitivity}).\nContinuation chains show the strongest drift (F1\\,=\\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\\,=\\,0.753; Appendix~\\ref{app:prompt-type}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\\ref{app:ddr-temp-stability}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\nExisting detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\\ref{tab:baselines}).\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Feat.} & \\textbf{3-cl F1} & \\textbf{Bin F1} & \\textbf{ms/text} \\\\\n\\midrule\n4-det.\\ + surface     & 6 & \\textbf{0.795} & \\textbf{0.708} & 22.8 \\\\\n4-detector ens.\\      & 4 & 0.785 & 0.700 & 22.8 \\\\\n7-feature (ours)      & 7 & 0.774 & 0.705 & \\textbf{9.7} \\\\\n\\midrule\nAvg-LogProb           & 1 & 0.707 & 0.673 & --- \\\\\nFastDetectGPT         & 1 & 0.660 & 0.569 & --- \\\\\nLD-Score              & 1 & 0.630 & 0.675 & --- \\\\\nBinoculars            & 1 & 0.411 & 0.539 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}\n\\label{tab:baselines}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.pdf}\n\\caption{LOGO binary F1 vs.\\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at 2.4$\\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nThe 7-feature ensemble surpasses all individual baselines in 3-class F1 ($\\Delta$\\,=\\,6.7--36.3\\,pp; Figure~\\ref{fig:baseline-ci}) and the pure 4-detector ensemble in binary F1 (0.705 vs.\\ 0.700).\nAdding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4$\\times$ the inference cost.\nThis result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses (\\S\\ref{sec:discussion}).\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01Xe81ASUPZLw4oKUcs4U1Wh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "f04d6da4-17a3-4bfa-9b79-5f351c998e9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 68 · 2026-05-21T08:40:44.817Z_

<details><summary>↩ Tool result · `toolu_01Xe81ASUPZLw4oKUcs4U1Wh`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, we predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).
8	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic autoregressive generation.
9	Depths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\S\ref{sec:results-differential}).
10	
11	\subsection{Generation Chain Construction}
12	\label{sec:generation}
13	
14	We construct generation chains using eight generators spanning five model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}, \textbf{Llama} (Llama-3.2-3B) \cite{llama3}, and \textbf{Mistral} (Mistral-7B-v0.3) \cite{mistral7b}.
15	This selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
16	
17	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
18	The same pool of seed passages serves as gen-0 for all generators.
19	We use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.
20	In LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.
21	We address this with a supplementary binary evaluation excluding gen-0 entirely (\S\ref{sec:results-baselines}).
22	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
23	We generate up to depth~4 to empirically confirm convergence: 5-class analysis shows adjacent depths 2--4 become indistinguishable (F1\,$\approx$\,0.27; Appendix~\ref{app:finer-depth}), motivating the gen-2+ class collapse.
24	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
25	After filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.
26	
27	\subsection{Feature Extraction}
28	\label{sec:features}
29	
30	The seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).
31	This dual-view design enables the location/shape decomposition that constitutes our primary finding.
32	We deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora}) but obscure the decomposition.
33	Cross-group ablation (\S\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\ref{app:lofo}) confirm that both feature groups contribute independently.
34	
35	We extract seven distributional features per text (Table~\ref{tab:features}), selected to provide principled coverage of the NLL distribution---location (mean), spread (std), extremes (max, min), and tail structure (decay)---complemented by two reference-free surface diversity measures.
36	We evaluated six additional NLL statistics (median, 90th percentile, IQR, CV, skewness, kurtosis) as candidate features; all exhibit $|r| > 0.65$ with existing features and yield no classification gain when added ($\Delta$F1\,$\leq$\,$-0.011$; Appendix~\ref{app:feature-candidate}).
37	
38	\begin{table}[t]
39	\centering
40	\footnotesize
41	\begin{tabular}{llp{3.8cm}}
42	\toprule
43	\textbf{Feature} & \textbf{Source} & \textbf{Measures} \\
44	\midrule
45	entropy\_mean & Ref.\ NLL & Central tendency of token surprise \\
46	entropy\_std  & Ref.\ NLL & Spread of token surprise \\
47	entropy\_max  & Ref.\ NLL & Maximum token surprise \\
48	entropy\_min  & Ref.\ NLL & Minimum token surprise \\
49	tail\_decay   & Ref.\ NLL & Log-prob decay slope (ranks 100--1K) \\
50	\midrule
51	TTR           & Surface & Type-token ratio \\
52	hapax\_ratio  & Surface & Proportion of hapax legomena \\
53	\bottomrule
54	\end{tabular}
55	\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\S\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}
56	\label{tab:features}
57	\end{table}
58	
59	\paragraph{Reference-model features.}
60	A held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.
61	We use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.
62	Although Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\S\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\leq$0.013 across Pythia, OLMo, and Qwen references).
63	From the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\_decay---the slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.
64	
65	\paragraph{Surface features.}
66	Two features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\_ratio).
67	
68	\paragraph{Feature complementarity.}
69	These features exhibit a \emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\S\ref{sec:results-differential}; pairwise correlations in Appendix~\ref{sec:appendix-feature-correlation}).
70	TTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.
71	
72	\subsection{Evaluation Protocol}
73	\label{sec:evaluation}
74	
75	\paragraph{Cross-validation.}
76	To evaluate generalization, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.
77	LOGO holds out individual generators but does not isolate family effects; \textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\,=\,0.686; \S\ref{sec:results-classification}).
78	Generator subsets vary across experiments (Appendix~\ref{app:gen-subsets-section}).
79	
80	\paragraph{Classifier.}
81	We use XGBoost \cite{xgboost} throughout ($n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\ref{tab:baselines}.
82	Alternative classifiers (CORAL \cite{coral_ordinal}, CORN \cite{corn_ordinal}, Frank-Hall \cite{frank_hall_ordinal}) yield comparable performance (Appendix~\ref{app:classifier}); discriminative power resides in the features, not the classifier.
83	
84	\paragraph{Metrics and statistical testing.}
85	The primary metric is \textbf{macro-averaged F1} over the three depth classes, with 95\% bootstrap CIs ($n{=}1{,}000$).
86	All $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.
87	
88	\paragraph{Baselines.}
89	We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
90	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.
91	
92	\paragraph{Length confound control.}
93	Since TTR and hapax\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\S\ref{sec:results-classification}; Appendix~\ref{app:length}).
94	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "12c25c23-ea4c-4163-b48b-c65cb7ab1504",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, we predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$: human-written ($d{=}0$), first-generation LLM output ($d{=}1$), or text produced by two or more recursive LLM generations ($d{=}2{+}$).\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$ (human corpus), $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic autoregressive generation.\nDepths beyond 2 are merged into $2{+}$ because feature convergence compresses inter-class margins at deeper levels (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using eight generators spanning five model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}, \\textbf{Llama} (Llama-3.2-3B) \\cite{llama3}, and \\textbf{Mistral} (Mistral-7B-v0.3) \\cite{mistral7b}.\nThis selection spans parameter scales from 0.6B to 8B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nThe same pool of seed passages serves as gen-0 for all generators.\nWe use shared seeds across generators so that cross-generator comparisons control for input content and isolate the effect of the generation model from source text variation.\nIn LOGO evaluation, gen-0 samples from the held-out generator's chains also appear (with the same text) in the training generators' chains, creating a potential train--test overlap for the gen-0 class.\nWe address this with a supplementary binary evaluation excluding gen-0 entirely (\\S\\ref{sec:results-baselines}).\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nWe generate up to depth~4 to empirically confirm convergence: 5-class analysis shows adjacent depths 2--4 become indistinguishable (F1\\,$\\approx$\\,0.27; Appendix~\\ref{app:finer-depth}), motivating the gen-2+ class collapse.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nAfter filtering chain breaks and passages too short for feature extraction, 37{,}058 texts remain across all depths (Appendix~\\ref{app:dataset-stats}); depths 2--4 are collapsed into $2{+}$.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features operationalize two complementary views of distributional drift: reference-model features capture how the token-level NLL distribution shifts relative to a fixed model (location and shape statistics), while surface features capture how lexical diversity contracts under recursive generation (type-token statistics).\nThis dual-view design enables the location/shape decomposition that constitutes our primary finding.\nWe deliberately use interpretable distributional statistics so that the DDR partition remains transparent and mechanistically informative; end-to-end neural features improve classification ($+$11.6\\,pp, 6-gen LOGO; Appendix~\\ref{app:qlora}) but obscure the decomposition.\nCross-group ablation (\\S\\ref{sec:results-differential}) and leave-one-feature-out analysis (Appendix~\\ref{app:lofo}) confirm that both feature groups contribute independently.\n\nWe extract seven distributional features per text (Table~\\ref{tab:features}), selected to provide principled coverage of the NLL distribution---location (mean), spread (std), extremes (max, min), and tail structure (decay)---complemented by two reference-free surface diversity measures.\nWe evaluated six additional NLL statistics (median, 90th percentile, IQR, CV, skewness, kurtosis) as candidate features; all exhibit $|r| > 0.65$ with existing features and yield no classification gain when added ($\\Delta$F1\\,$\\leq$\\,$-0.011$; Appendix~\\ref{app:feature-candidate}).\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\begin{tabular}{llp{3.8cm}}\n\\toprule\n\\textbf{Feature} & \\textbf{Source} & \\textbf{Measures} \\\\\n\\midrule\nentropy\\_mean & Ref.\\ NLL & Central tendency of token surprise \\\\\nentropy\\_std  & Ref.\\ NLL & Spread of token surprise \\\\\nentropy\\_max  & Ref.\\ NLL & Maximum token surprise \\\\\nentropy\\_min  & Ref.\\ NLL & Minimum token surprise \\\\\ntail\\_decay   & Ref.\\ NLL & Log-prob decay slope (ranks 100--1K) \\\\\n\\midrule\nTTR           & Surface & Type-token ratio \\\\\nhapax\\_ratio  & Surface & Proportion of hapax legomena \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Seven distributional features. Reference features use Pythia-410M per-token NLL; surface features require no reference model. DDR analysis (\\S\\ref{sec:results-differential}) reveals that the first three drift with depth while the last four remain stable.}\n\\label{tab:features}\n\\end{table}\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than all generators) computes per-token negative log-likelihood (NLL) for each text.\nWe use ``entropy'' as shorthand for token-level NLL throughout, following convention in prior detection work; these are point-wise NLL values, not Shannon entropy of the full distribution.\nAlthough Pythia-410M shares the GPT-NeoX architecture with two of the eight generators, cross-family reference model experiments (\\S\\ref{sec:results-differential}) confirm that depth features are not reference-specific (LOGO F1 varies by $\\leq$0.013 across Pythia, OLMo, and Qwen references).\nFrom the resulting NLL sequence, we extract five statistics: mean, standard deviation, maximum, and minimum of the token-level NLL, plus tail\\_decay---the slope of the vocabulary-level averaged log-probability distribution in the mid-rank region (ranks 100--1000), capturing how steeply probability mass decays beyond high-frequency tokens.\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model: type-token ratio (TTR) and the proportion of words appearing exactly once (hapax\\_ratio).\n\n\\paragraph{Feature complementarity.}\nThese features exhibit a \\emph{differential depth response} (DDR), separating into drifting and non-drifting groups (\\S\\ref{sec:results-differential}; pairwise correlations in Appendix~\\ref{sec:appendix-feature-correlation}).\nTTR and hapax ratio are strongly correlated ($r = 0.97$); both are retained for marginal LOFO gains.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation over all eight generators.\nLOGO holds out individual generators but does not isolate family effects; \\textbf{Leave-One-Family-Out (LOFO)} addresses this by holding out entire model families (binary F1\\,=\\,0.686; \\S\\ref{sec:results-classification}).\nGenerator subsets vary across experiments (Appendix~\\ref{app:gen-subsets-section}).\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} throughout ($n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, learning rate $0.1$), with identical hyperparameters across all methods in Table~\\ref{tab:baselines}.\nAlternative classifiers (CORAL \\cite{coral_ordinal}, CORN \\cite{corn_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) yield comparable performance (Appendix~\\ref{app:classifier}); discriminative power resides in the features, not the classifier.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, with 95\\% bootstrap CIs ($n{=}1{,}000$).\nAll $p$-values are two-sided with Bonferroni correction within each family of simultaneous tests.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation to ensure a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify depth signal is not a length artifact via length-matched subsampling that equalizes length distributions across depth classes (\\S\\ref{sec:results-classification}; Appendix~\\ref{app:length}).\n",
      "numLines": 94,
      "startLine": 1,
      "totalLines": 94
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01A6KnaNroaqf9ffyvUJNqYb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "d104891d-14c1-4ae2-9ef3-ae14587ecef9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 70 · 2026-05-21T08:40:45.140Z_

<details><summary>↩ Tool result · `toolu_01A6KnaNroaqf9ffyvUJNqYb`</summary>

```text
1	To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \cite{qlora}.
2	
3	\paragraph{Setup.}
4	We fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\,=\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}
5	For 3-class evaluation, we collapse predictions into gen-0\,/\,gen-1\,/\,gen-2+ post hoc.
6	All results use the same LOGO protocol as the main experiments.
7	
8	\begin{table}[ht]
9	\centering
10	\small
11	\caption{QLoRA end-to-end depth classification vs.\ XGBoost on handcrafted features, under LOGO evaluation.}
12	\label{tab:qlora}
13	\resizebox{\linewidth}{!}{%
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Method} & \textbf{5-class F1} & \textbf{3-class F1} & \textbf{Per-class F1 (5-class)} \\
17	\midrule
18	XGBoost (7 features) & 0.501 $\pm$ 0.038 & 0.789 & --- \\
19	QLoRA (Qwen3-0.6B)   & 0.583 $\pm$ 0.010 & 0.905 $\pm$ 0.003 & 0.999\,/\,0.796\,/\,0.413\,/\,0.259\,/\,0.447 \\
20	\bottomrule
21	\end{tabular}}
22	\end{table}
23	
24	\paragraph{Results.}
25	QLoRA achieves 3-class LOGO F1\,=\,0.905 ($\pm$0.003) under 6-generator LOGO, a +11.6\,pp improvement over the same-subset XGBoost baseline (0.789).
26	On 5-class evaluation, QLoRA reaches F1\,=\,0.583 ($\pm$0.010) vs.\ 0.501 for XGBoost (+8.2\,pp), with the largest gains at gen-1 (0.796 vs.\ 0.634) and gen-2 (0.413 vs.\ 0.268).
27	The gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\,=\,0.259), consistent with the feature-level analysis in \S\ref{sec:discussion}.
28	
29	\paragraph{Hyperparameter robustness.}
30	A second run with LoRA rank 32 and seed 123 yields 5-class F1\,=\,0.587 ($\pm$0.005) and 3-class F1\,=\,0.905 ($\pm$0.004), which confirms stability across hyperparameter and seed variation ($\Delta < 1$\,pp on both metrics).
31	
32	\paragraph{Implications.}
33	The substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.
34	End-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.
35	This confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "ac16c4fc-4806-46f7-9e47-8885492740e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/appendix_qlora.tex",
      "content": "To assess whether depth signal extends beyond handcrafted features, we fine-tune a pretrained language model end-to-end as a depth classifier using QLoRA \\cite{qlora}.\n\n\\paragraph{Setup.}\nWe fine-tune Qwen3-0.6B-Base with LoRA rank 16, learning rate $2 \\times 10^{-4}$, and 3 epochs, framing depth estimation as 5-class sequence classification (gen-0 through gen-4).\\footnote{Evaluated on the original 6-generator subset; XGBoost 3-class F1\\,=\\,0.789. We expect 8-generator training to further improve given additional diversity; the comparison direction is preserved.}\nFor 3-class evaluation, we collapse predictions into gen-0\\,/\\,gen-1\\,/\\,gen-2+ post hoc.\nAll results use the same LOGO protocol as the main experiments.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{QLoRA end-to-end depth classification vs.\\ XGBoost on handcrafted features, under LOGO evaluation.}\n\\label{tab:qlora}\n\\resizebox{\\linewidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{5-class F1} & \\textbf{3-class F1} & \\textbf{Per-class F1 (5-class)} \\\\\n\\midrule\nXGBoost (7 features) & 0.501 $\\pm$ 0.038 & 0.789 & --- \\\\\nQLoRA (Qwen3-0.6B)   & 0.583 $\\pm$ 0.010 & 0.905 $\\pm$ 0.003 & 0.999\\,/\\,0.796\\,/\\,0.413\\,/\\,0.259\\,/\\,0.447 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Results.}\nQLoRA achieves 3-class LOGO F1\\,=\\,0.905 ($\\pm$0.003) under 6-generator LOGO, a +11.6\\,pp improvement over the same-subset XGBoost baseline (0.789).\nOn 5-class evaluation, QLoRA reaches F1\\,=\\,0.583 ($\\pm$0.010) vs.\\ 0.501 for XGBoost (+8.2\\,pp), with the largest gains at gen-1 (0.796 vs.\\ 0.634) and gen-2 (0.413 vs.\\ 0.268).\nThe gen-2/gen-3 boundary remains the primary failure mode (gen-3 F1\\,=\\,0.259), consistent with the feature-level analysis in \\S\\ref{sec:discussion}.\n\n\\paragraph{Hyperparameter robustness.}\nA second run with LoRA rank 32 and seed 123 yields 5-class F1\\,=\\,0.587 ($\\pm$0.005) and 3-class F1\\,=\\,0.905 ($\\pm$0.004), which confirms stability across hyperparameter and seed variation ($\\Delta < 1$\\,pp on both metrics).\n\n\\paragraph{Implications.}\nThe substantial 3-class improvement demonstrates that raw token embeddings contain depth signal beyond what summary statistics capture; the seven handcrafted features are a strong but lossy compression of the full distributional information.\nEnd-to-end fine-tuning exploits token-level patterns (e.g., positional regularities, n-gram repetitions) that aggregate features cannot represent.\nThis confirms that the depth signal documented in our main analysis is real and exploitable beyond engineered features, while the handcrafted approach retains practical advantages: interpretability, computational efficiency (no GPU inference), and the ability to reveal the differential depth response pattern that motivates the task formulation.\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01MBTXEJDTWcL1Lqbg3YMDFU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "cce8a9d3-4619-4aee-9ab5-c7eb8d0dd143",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 72 · 2026-05-21T08:40:45.659Z_

<details><summary>↩ Tool result · `toolu_01MBTXEJDTWcL1Lqbg3YMDFU`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{AI-Generated Text Detection}
5	\label{sec:related-detection}
6	
7	The detection literature spans statistical tests \cite{gltr,grover,release_strategies}, zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \cite{diveye}, geometric invariants \cite{intrinsic_dim_detection}, and learned classifiers \cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \citet{wu_survey_2025} and \citet{jawahar_survey} for surveys.
8	RAID \cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.
9	Several recent efforts move beyond the binary boundary---collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}, creator-editor modes \cite{beyond_final_actor}, multi-generator attribution \cite{semeval2024_task8}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.52--0.71; Table~\ref{tab:baselines}) \cite{paraphrase_evades,detection_possibilities}.
10	Our contribution is orthogonal: ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \cite{uchendu_attribution,munir_looking_glass}.
11	
12	\subsection{Model Collapse and Iterative Generation}
13	\label{sec:related-collapse}
14	
15	Self-consuming generative models progressively lose distributional coverage \cite{self_consuming_mad,curse_of_recursion,briesch_self_consuming,seddik_synthetic_data}, though data mixing mitigates collapse \cite{model_collapse_avoidable,strong_model_collapse}.
16	These studies address \emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \citet{schaeffer_collapse_position} identify eight distinct definitions of ``collapse,'' most tied to retraining dynamics.
17	We study \emph{inference chains} where parameters are fixed and only the input distribution evolves.
18	Two concurrent works are most directly relevant: \citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.
19	We study \emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \emph{that} and \emph{why} convergence occurs, DDR isolates \emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.
20	The independent convergence of all three approaches on ${\sim}$3 distinguishable depth classes---via Markovian dynamics \cite{markovian_chains}, information-theoretic loss \cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\ref{tab:iterative-comparison} in Appendix~\ref{app:iterative-comparison} provides a structured comparison).
21	
22	\subsection{Vocabulary Diversity and Stylometry}
23	\label{sec:related-diversity}
24	
25	Declining lexical diversity in LLM text is documented in both training \cite{curious_decline} and deployment settings \cite{writing_diversity}; MAUVE \cite{mauve} provides a divergence-based metric for quantifying this distributional gap.
26	Our surface features (TTR, hapax ratio) are classical stylometric measures \cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \cite{nucleus_sampling} constitutes a drifting component of DDR.
27	
28	\subsection{Data Quality and Provenance}
29	\label{sec:related-provenance}
30	
31	Scalable data curation relies on quality signals \cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.
32	Proactive watermarking \cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \cite{chainwash}, motivating passive approaches.
33	Our NLL-based analysis connects to \citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.
34	\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "87dfa864-8dec-4dc0-bbf8-47049b51cc7b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{AI-Generated Text Detection}\n\\label{sec:related-detection}\n\nThe detection literature spans statistical tests \\cite{gltr,grover,release_strategies}, zero-shot scoring \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \\cite{diveye}, geometric invariants \\cite{intrinsic_dim_detection}, and learned classifiers \\cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \\citet{wu_survey_2025} and \\citet{jawahar_survey} for surveys.\nRAID \\cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.\nSeveral recent efforts move beyond the binary boundary---collaboration roles \\cite{beyond_binary}, joint detection-attribution \\cite{two_birds}, creator-editor modes \\cite{beyond_final_actor}, multi-generator attribution \\cite{semeval2024_task8}---but all taxonomize by \\emph{source} or \\emph{production mode}, not recursive generation \\emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\\,=\\,0.52--0.71; Table~\\ref{tab:baselines}) \\cite{paraphrase_evades,detection_possibilities}.\nOur contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \\cite{uchendu_attribution,munir_looking_glass}.\n\n\\subsection{Model Collapse and Iterative Generation}\n\\label{sec:related-collapse}\n\nSelf-consuming generative models progressively lose distributional coverage \\cite{self_consuming_mad,curse_of_recursion,briesch_self_consuming,seddik_synthetic_data}, though data mixing mitigates collapse \\cite{model_collapse_avoidable,strong_model_collapse}.\nThese studies address \\emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \\citet{schaeffer_collapse_position} identify eight distinct definitions of ``collapse,'' most tied to retraining dynamics.\nWe study \\emph{inference chains} where parameters are fixed and only the input distribution evolves.\nTwo concurrent works are most directly relevant: \\citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \\citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \\citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.\nWe study \\emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \\emph{that} and \\emph{why} convergence occurs, DDR isolates \\emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.\nThe independent convergence of all three approaches on ${\\sim}$3 distinguishable depth classes---via Markovian dynamics \\cite{markovian_chains}, information-theoretic loss \\cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\\ref{tab:iterative-comparison} in Appendix~\\ref{app:iterative-comparison} provides a structured comparison).\n\n\\subsection{Vocabulary Diversity and Stylometry}\n\\label{sec:related-diversity}\n\nDeclining lexical diversity in LLM text is documented in both training \\cite{curious_decline} and deployment settings \\cite{writing_diversity}; MAUVE \\cite{mauve} provides a divergence-based metric for quantifying this distributional gap.\nOur surface features (TTR, hapax ratio) are classical stylometric measures \\cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \\cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \\cite{nucleus_sampling} constitutes a drifting component of DDR.\n\n\\subsection{Data Quality and Provenance}\n\\label{sec:related-provenance}\n\nScalable data curation relies on quality signals \\cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.\nProactive watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \\cite{chainwash}, motivating passive approaches.\nOur NLL-based analysis connects to \\citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.\n\\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_017L3SBnbpJyimJM9q6ebG42`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "67af3a80-97c3-4f1c-8c94-7ee47bc104c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 74 · 2026-05-21T08:40:46.968Z_

<details><summary>↩ Tool result · `toolu_017L3SBnbpJyimJM9q6ebG42`</summary>

```text
1	% ===== Data Provenance / Contamination =====
2	
3	% ===== Statistics =====
4	
5	@book{cohen1988statistical,
6	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
7	  author = {Cohen, Jacob},
8	  edition = {2nd},
9	  publisher = {Lawrence Erlbaum Associates},
10	  year = {1988},
11	}
12	
13	% ===== Detection =====
14	
15	@inproceedings{detectgpt,
16	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
17	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
18	  booktitle = {Proceedings of the International Conference on Machine Learning},
19	  year = {2023},
20	}
21	
22	@inproceedings{gltr,
23	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
24	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
25	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
26	  year = {2019},
27	}
28	
29	@inproceedings{dna_gpt,
30	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
31	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
32	  booktitle = {Proceedings of the International Conference on Learning Representations},
33	  year = {2024},
34	}
35	
36	@inproceedings{binoculars,
37	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
38	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
39	  booktitle = {Proceedings of the International Conference on Machine Learning},
40	  year = {2024},
41	}
42	
43	@inproceedings{fast_detectgpt,
44	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
45	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
46	  booktitle = {Proceedings of the International Conference on Learning Representations},
47	  year = {2024},
48	}
49	
50	@article{ld_score,
51	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
52	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
53	  journal = {arXiv preprint arXiv:2605.01647},
54	  year = {2026},
55	}
56	
57	@inproceedings{diveye,
58	  title = {{Diversity Boosts AI-Generated Text Detection}},
59	  author = {Basani, Advik Raj and Chen, Pin-Yu},
60	  booktitle = {Proceedings of the International Conference on Learning Representations},
61	  year = {2026},
62	  eprint = {2509.18880},
63	  archiveprefix = {arXiv},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{intrinsic_dim_detection,
96	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
97	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2023},
100	}
101	
102	@inproceedings{grover,
103	  title = {{Defending Against Neural Fake News}},
104	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
105	  booktitle = {Advances in Neural Information Processing Systems},
106	  year = {2019},
107	}
108	
109	@article{release_strategies,
110	  title = {{Release Strategies and the Social Impacts of Language Models}},
111	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
112	  journal = {arXiv preprint arXiv:1908.09203},
113	  year = {2019},
114	}
115	
116	@inproceedings{beyond_binary,
117	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
118	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
119	  booktitle = {Proceedings of the ACM Web Conference},
120	  year = {2025},
121	}
122	
123	@inproceedings{semeval2024_task8,
124	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
125	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
126	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
127	  year = {2024},
128	}
129	
130	% ===== Model Collapse =====
131	
132	@inproceedings{self_consuming_mad,
133	  title = {{Self-Consuming Generative Models Go MAD}},
134	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
135	  booktitle = {Proceedings of the International Conference on Learning Representations},
136	  year = {2024},
137	}
138	
139	@article{curse_of_recursion,
140	  title = {{AI models collapse when trained on recursively generated data}},
141	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
142	  journal = {Nature},
143	  volume = {631},
144	  pages = {755--759},
145	  year = {2024},
146	}
147	
148	@inproceedings{strong_model_collapse,
149	  title = {{Strong Model Collapse}},
150	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
151	  booktitle = {Proceedings of the International Conference on Learning Representations},
152	  year = {2025},
153	}
154	
155	@inproceedings{model_collapse_avoidable,
156	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
157	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
158	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
159	  year = {2024},
160	}
161	
162	@inproceedings{schaeffer_collapse_position,
163	  title = {{Position: Model Collapse Does Not Mean What You Think}},
164	  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
165	  booktitle = {Proceedings of the International Conference on Machine Learning},
166	  year = {2025},
167	  eprint = {2503.03150},
168	  archiveprefix = {arXiv},
169	}
170	
171	@inproceedings{drayson_detection_prevents_collapse,
172	  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},
173	  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
174	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
175	  year = {2025},
176	  eprint = {2502.15654},
177	  archiveprefix = {arXiv},
178	}
179	
180	@article{seddik_synthetic_data,
181	  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
182	  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
183	  journal = {arXiv preprint arXiv:2404.05090},
184	  year = {2024},
185	}
186	
187	% ===== Fine-tuning =====
188	
189	@inproceedings{qlora,
190	  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},
191	  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
192	  booktitle = {Advances in Neural Information Processing Systems},
193	  year = {2023},
194	}
195	
196	% ===== Data Quality =====
197	
198	% ===== (orphan entries removed: fineweb, dolma) =====
199	
200	@inproceedings{dsir,
201	  title = {{Data Selection for Language Models via Importance Resampling}},
202	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
203	  booktitle = {Advances in Neural Information Processing Systems},
204	  year = {2023},
205	}
206	
207	@inproceedings{qurating,
208	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
209	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
210	  booktitle = {Proceedings of the International Conference on Machine Learning},
211	  year = {2024},
212	}
213	
214	@inproceedings{ccnet,
215	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
216	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
217	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
218	  year = {2020},
219	}
220	
221	% ===== Watermarking =====
222	
223	@inproceedings{watermark_llm,
224	  title = {{A Watermark for Large Language Models}},
225	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
226	  booktitle = {Proceedings of the International Conference on Machine Learning},
227	  year = {2023},
228	}
229	
230	@article{synthid_text,
231	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
232	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
233	  journal = {Nature},
234	  volume = {634},
235	  pages = {818--823},
236	  year = {2024},
237	}
238	
239	@misc{aaronson_watermark,
240	  title = {{Watermarking GPT Outputs}},
241	  author = {Aaronson, Scott and Kirchner, Jan Hendrik},
242	  year = {2022},
243	  note = {Blog post},
244	  url = {https://scottaaronson.blog/?p=6823},
245	}
246	
247	@article{chainwash,
248	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
249	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
250	  journal = {arXiv preprint arXiv:2605.05503},
251	  year = {2026},
252	}
253	
254	% ===== Vocabulary Diversity =====
255	
256	@inproceedings{curious_decline,
257	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
258	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
259	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
260	  year = {2024},
261	}
262	
263	@inproceedings{writing_diversity,
264	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
265	  author = {Padmakumar, Vishakh and He, He},
266	  booktitle = {Proceedings of the International Conference on Learning Representations},
267	  year = {2024},
268	}
269	
270	@inproceedings{nucleus_sampling,
271	  title = {{The Curious Case of Neural Text Degeneration}},
272	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
273	  booktitle = {Proceedings of the International Conference on Learning Representations},
274	  year = {2020},
275	}
276	
277	% ===== Stylometry =====
278	
279	@article{stamatatos_survey,
280	  title = {{A Survey of Modern Authorship Attribution Methods}},
281	  author = {Stamatatos, Efstathios},
282	  journal = {Journal of the American Society for Information Science and Technology},
283	  volume = {60},
284	  number = {3},
285	  pages = {538--556},
286	  year = {2009},
287	}
288	
289	@article{koppel_authorship,
290	  title = {{Computational Methods in Authorship Attribution}},
291	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
292	  journal = {Journal of the American Society for Information Science and Technology},
293	  volume = {60},
294	  number = {1},
295	  pages = {9--26},
296	  year = {2009},
297	}
298	
299	@inproceedings{uchendu_attribution,
300	  title = {{Authorship Attribution for Neural Text Generation}},
301	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
302	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
303	  year = {2020},
304	}
305	
306	@inproceedings{munir_looking_glass,
307	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
308	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
309	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
310	  year = {2021},
311	}
312	
313	@article{briesch_self_consuming,
314	  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
315	  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
316	  journal = {arXiv preprint arXiv:2311.16822},
317	  year = {2023},
318	}
319	
320	% ===== Iterative Generation =====
321	
322	@inproceedings{broken_telephone,
323	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
324	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
325	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
326	  year = {2025},
327	}
328	
329	@article{markovian_chains,
330	  title = {{Markovian Generation Chains in Large Language Models}},
331	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
332	  journal = {arXiv preprint arXiv:2603.11228},
333	  year = {2026},
334	}
335	
336	@inproceedings{attractor_cycles,
337	  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},
338	  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
339	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
340	  year = {2025},
341	  eprint = {2502.15208},
342	  archiveprefix = {arXiv},
343	}
344	
345	% ===== Membership Inference =====
346	
347	@inproceedings{min_k_percent,
348	  title = {{Detecting Pretraining Data from Large Language Models}},
349	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
350	  booktitle = {Proceedings of the International Conference on Learning Representations},
351	  year = {2024},
352	}
353	
354	@article{koike_mia_detection,
355	  title = {{Machine Text Detectors are Membership Inference Attacks}},
356	  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},
357	  journal = {arXiv preprint arXiv:2510.19492},
358	  year = {2025},
359	}
360	
361	% ===== Survey =====
362	
363	@article{wu_survey_2025,
364	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
365	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
366	  journal = {Computational Linguistics},
367	  publisher = {MIT Press},
368	  year = {2025},
369	}
370	
371	@inproceedings{jawahar_survey,
372	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
373	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
374	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
375	  year = {2020},
376	}
377	
378	% ===== Models =====
379	
380	@inproceedings{pythia,
381	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
382	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
383	  booktitle = {Proceedings of the International Conference on Machine Learning},
384	  year = {2023},
385	}
386	
387	@inproceedings{olmo,
388	  title = {{OLMo: Accelerating the Science of Language Models}},
389	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
390	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
391	  year = {2024},
392	}
393	
394	@article{qwen3,
395	  title = {{Qwen3 Technical Report}},
396	  author = {{Qwen Team}},
397	  journal = {arXiv preprint arXiv:2505.09388},
398	  year = {2025},
399	}
400	
401	@inproceedings{ghostbuster,
402	  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
403	  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
404	  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},
405	  year = {2024},
406	}
407	
408	@article{two_birds,
409	  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},
410	  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},
411	  journal = {arXiv preprint arXiv:2508.14190},
412	  year = {2025},
413	}
414	
415	@inproceedings{beyond_final_actor,
416	  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},
417	  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},
418	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
419	  year = {2026},
420	}
421	
422	% ===== Machine Learning =====
423	
424	@article{gutierrez_ordinal_survey,
425	  title = {{Ordinal Regression Methods: Survey and Experimental Study}},
426	  author = {Guti{\'e}rrez, Pedro Antonio and P{\'e}rez-Ortiz, Mar{\'i}a and S{\'a}nchez-Monedero, Javier and Fern{\'a}ndez-Navarro, Francisco and Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
427	  journal = {IEEE Transactions on Knowledge and Data Engineering},
428	  volume = {28},
429	  number = {1},
430	  pages = {127--146},
431	  year = {2016},
432	}
433	
434	@article{coral_ordinal,
435	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
436	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
437	  journal = {Pattern Recognition Letters},
438	  volume = {140},
439	  pages = {325--331},
440	  year = {2020},
441	}
442	
443	@inproceedings{frank_hall_ordinal,
444	  title = {{A Simple Approach to Ordinal Classification}},
445	  author = {Frank, Eibe and Hall, Mark},
446	  booktitle = {Proceedings of the European Conference on Machine Learning},
447	  year = {2001},
448	}
449	
450	@article{corn_ordinal,
451	  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},
452	  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},
453	  journal = {Pattern Analysis and Applications},
454	  volume = {26},
455	  pages = {941--955},
456	  year = {2023},
457	}
458	
459	@inproceedings{kasa_ordinality_nlp,
460	  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},
461	  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},
462	  booktitle = {Findings of the Association for Computational Linguistics: ACL},
463	  year = {2024},
464	}
465	
466	@inproceedings{xgboost,
467	  title = {{XGBoost: A Scalable Tree Boosting System}},
468	  author = {Chen, Tianqi and Guestrin, Carlos},
469	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
470	  year = {2016},
471	}
472	
473	@article{lakens_equivalence,
474	  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},
475	  author = {Lakens, Dani{\"e}l},
476	  journal = {Social Psychological and Personality Science},
477	  volume = {8},
478	  number = {4},
479	  pages = {355--362},
480	  year = {2017},
481	}
482	
483	% ===== Generator Model References =====
484	
485	@article{llama3,
486	  title = {{The Llama 3 Herd of Models}},
487	  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},
488	  journal = {arXiv preprint arXiv:2407.21783},
489	  year = {2024},
490	}
491	
492	@article{mistral7b,
493	  title = {{Mistral 7B}},
494	  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},
495	  journal = {arXiv preprint arXiv:2310.06825},
496	  year = {2023},
497	}
498	
499	@article{strobl_conditional_2008,
500	  title = {Conditional Variable Importance for Random Forests},
501	  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},
502	  journal = {BMC Bioinformatics},
503	  volume = {9},
504	  pages = {307},
505	  year = {2008},
506	}
507	
508	% --- Entries from Paper Agent (docs/paper) ---
509	
510	@inproceedings{dolma,
511	  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},
512	  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},
513	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
514	  year = {2024},
515	}
516	
517	
518	@inproceedings{fineweb,
519	  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},
520	  author = {Penedo, Guilherme and Kydl{\'\i}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
521	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
522	  year = {2024},
523	}
524	
525	
526	@inproceedings{mapping_llm_science,
527	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
528	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
529	  booktitle = {Proceedings of the Conference on Language Modeling},
530	  year = {2024},
531	}
532	
533	
534	@inproceedings{monitoring_ai_review,
535	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
536	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
537	  booktitle = {Proceedings of the International Conference on Machine Learning},
538	  year = {2024},
539	}
540	
541	% ===== Stylometry =====
542	
543	
544	
545	@inproceedings{raid,
546	  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},
547	  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
548	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
549	  year = {2024},
550	  address = {Bangkok, Thailand},
551	  publisher = {Association for Computational Linguistics},
552	  pages = {12463--12492},
553	}
554	
555	% ===== Distribution Quality =====
556	
557	@inproceedings{mauve,
558	  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},
559	  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},
560	  booktitle = {Advances in Neural Information Processing Systems},
561	  year = {2021},
562	}
563	
564	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "ad5bd806-30d5-47e4-9760-5eedc87ec012",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
      "content": "% ===== Data Provenance / Contamination =====\n\n% ===== Statistics =====\n\n@book{cohen1988statistical,\n  title = {{Statistical Power Analysis for the Behavioral Sciences}},\n  author = {Cohen, Jacob},\n  edition = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1988},\n}\n\n% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2026},\n  eprint = {2509.18880},\n  archiveprefix = {arXiv},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{intrinsic_dim_detection,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n@inproceedings{schaeffer_collapse_position,\n  title = {{Position: Model Collapse Does Not Mean What You Think}},\n  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2025},\n  eprint = {2503.03150},\n  archiveprefix = {arXiv},\n}\n\n@inproceedings{drayson_detection_prevents_collapse,\n  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},\n  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  eprint = {2502.15654},\n  archiveprefix = {arXiv},\n}\n\n@article{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  journal = {arXiv preprint arXiv:2404.05090},\n  year = {2024},\n}\n\n% ===== Fine-tuning =====\n\n@inproceedings{qlora,\n  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},\n  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Data Quality =====\n\n% ===== (orphan entries removed: fineweb, dolma) =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Jan Hendrik},\n  year = {2022},\n  note = {Blog post},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {3},\n  pages = {538--556},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {1},\n  pages = {9--26},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n@article{briesch_self_consuming,\n  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal = {arXiv preprint arXiv:2311.16822},\n  year = {2023},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n@inproceedings{attractor_cycles,\n  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},\n  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n  eprint = {2502.15208},\n  archiveprefix = {arXiv},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{koike_mia_detection,\n  title = {{Machine Text Detectors are Membership Inference Attacks}},\n  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},\n  journal = {arXiv preprint arXiv:2510.19492},\n  year = {2025},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n@inproceedings{ghostbuster,\n  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{two_birds,\n  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},\n  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},\n  journal = {arXiv preprint arXiv:2508.14190},\n  year = {2025},\n}\n\n@inproceedings{beyond_final_actor,\n  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},\n  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2026},\n}\n\n% ===== Machine Learning =====\n\n@article{gutierrez_ordinal_survey,\n  title = {{Ordinal Regression Methods: Survey and Experimental Study}},\n  author = {Guti{\\'e}rrez, Pedro Antonio and P{\\'e}rez-Ortiz, Mar{\\'i}a and S{\\'a}nchez-Monedero, Javier and Fern{\\'a}ndez-Navarro, Francisco and Herv{\\'a}s-Mart{\\'i}nez, C{\\'e}sar},\n  journal = {IEEE Transactions on Knowledge and Data Engineering},\n  volume = {28},\n  number = {1},\n  pages = {127--146},\n  year = {2016},\n}\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@article{corn_ordinal,\n  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},\n  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},\n  journal = {Pattern Analysis and Applications},\n  volume = {26},\n  pages = {941--955},\n  year = {2023},\n}\n\n@inproceedings{kasa_ordinality_nlp,\n  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},\n  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year = {2024},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n\n@article{lakens_equivalence,\n  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},\n  author = {Lakens, Dani{\\\"e}l},\n  journal = {Social Psychological and Personality Science},\n  volume = {8},\n  number = {4},\n  pages = {355--362},\n  year = {2017},\n}\n\n% ===== Generator Model References =====\n\n@article{llama3,\n  title = {{The Llama 3 Herd of Models}},\n  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n}\n\n@article{mistral7b,\n  title = {{Mistral 7B}},\n  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},\n  journal = {arXiv preprint arXiv:2310.06825},\n  year = {2023},\n}\n\n@article{strobl_conditional_2008,\n  title = {Conditional Variable Importance for Random Forests},\n  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},\n  journal = {BMC Bioinformatics},\n  volume = {9},\n  pages = {307},\n  year = {2008},\n}\n\n% --- Entries from Paper Agent (docs/paper) ---\n\n@inproceedings{dolma,\n  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},\n  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n\n@inproceedings{fineweb,\n  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  author = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year = {2024},\n}\n\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n\n\n@inproceedings{raid,\n  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},\n  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2024},\n  address = {Bangkok, Thailand},\n  publisher = {Association for Computational Linguistics},\n  pages = {12463--12492},\n}\n\n% ===== Distribution Quality =====\n\n@inproceedings{mauve,\n  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},\n  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2021},\n}\n\n",
      "numLines": 564,
      "startLine": 1,
      "totalLines": 564
    }
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01NuYbaTqRWxGMXJ7HuE3CQq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c60d1836-d46b-4fec-8395-c736ff37d5b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 76 · 2026-05-21T08:40:47.100Z_

<details><summary>↩ Tool result · `toolu_01NuYbaTqRWxGMXJ7HuE3CQq`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	AI text detection asks a single binary question---\emph{human or machine?}---and recent methods answer it with increasing reliability \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Yet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{recursive depths}---an estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.
6	While most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.
7	Knowing \emph{how many times} text has been recursively generated matters for data provenance \cite{ccnet,dsir} and model collapse analysis \cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.
8	
9	Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}.
10	We introduce \emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\,/\,gen-1\,/\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).
11	We term this location/shape asymmetry the \emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.
12	Where concurrent work characterizes \emph{that} and \emph{why} convergence occurs \cite{broken_telephone,markovian_chains}, DDR isolates \emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.
13	
14	As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\,=\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.
15	
16	Our contributions:
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\,=\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \emph{what converges}---diversity loss \cite{curious_decline}, attractor dynamics \cite{markovian_chains}---DDR identifies \emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.
19	    \item \textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.
20	\end{enumerate}
21	A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c99111b3-d02f-45c2-b53e-bc9083231af8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nAI text detection asks a single binary question---\\emph{human or machine?}---and recent methods answer it with increasing reliability \\cite{detectgpt,fast_detectgpt,binoculars,ld_score}.\nYet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \\cite{dolma,fineweb} and seed further generation, text accumulates at varying \\emph{recursive depths}---an estimated 7--17\\% of recent scientific publications already contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.\nWhile most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.\nKnowing \\emph{how many times} text has been recursively generated matters for data provenance \\cite{ccnet,dsir} and model collapse analysis \\cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.\n\nDistributional compression under recursive generation is well-documented \\cite{curious_decline,broken_telephone,markovian_chains}.\nWe introduce \\emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\\,/\\,gen-1\\,/\\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).\nWe term this location/shape asymmetry the \\emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \\cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.\nWhere concurrent work characterizes \\emph{that} and \\emph{why} convergence occurs \\cite{broken_telephone,markovian_chains}, DDR isolates \\emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.\n\nAs a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\\,=\\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\\,=\\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \\emph{what converges}---diversity loss \\cite{curious_decline}, attractor dynamics \\cite{markovian_chains}---DDR identifies \\emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.\n    \\item \\textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.\n\\end{enumerate}\nA proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_011jqAeeVgMhR9J1T34yL823`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "7aa29474-614a-4e8c-b922-e6ddc8af3239",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xJQDTSC7CM6tCrVfrM5hu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 136,
      "cache_creation_input_tokens": 3142,
      "cache_read_input_tokens": 26357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3142
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

_source line 78 · 2026-05-21T08:40:47.262Z_

<details><summary>↩ Tool result · `toolu_011jqAeeVgMhR9J1T34yL823`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	
18	\graphicspath{{../chart/}}
19	
20	\title{Depth Fingerprinting: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{abstract}
28	
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{results}
33	
34	\input{discussion}
35	\input{conclusion}
36	\input{limitations}
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	
43	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
44	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
45	
46	\input{appendix_dataset_stats}
47	
48	\section{Length Confound Analysis}
49	\label{app:length}
50	\input{appendix_length}
51	
52	\section{Prompt Type Generalization}
53	\label{app:prompt-type}
54	\input{appendix_prompt_type}
55	
56	\section{Finer-Grained Depth Classification}
57	\label{app:finer-depth}
58	\input{appendix_finer_depth}
59	
60	\section{End-to-End Depth Classification (QLoRA)}
61	\label{app:qlora}
62	\input{appendix_qlora}
63	
64	\section{Leave-One-Feature-Out Analysis}
65	\label{app:lofo}
66	\input{appendix_lofo}
67	
68	\subsection{Candidate Feature Screening}
69	\label{app:feature-candidate}
70	\input{appendix_feature_candidates}
71	
72	\section{Confusion Matrix}
73	\label{app:confusion}
74	\input{appendix_confusion_matrix}
75	
76	\section{Classifier Sensitivity}
77	\label{app:classifier}
78	\input{appendix_classifier}
79	\FloatBarrier
80	
81	\section{Robustness to Text Perturbation}
82	\label{app:human-edit}
83	\input{appendix_human_edit}
84	
85	\section{Cross-Domain Generalization}
86	\label{app:domain}
87	\input{appendix_domain}
88	
89	\section{Instruction-Tuned Model Analysis}
90	\label{app:instruct}
91	\input{appendix_instruct}
92	
93	\section{Error Analysis of Binary Classification}
94	\label{app:error-analysis}
95	\input{appendix_error_analysis}
96	
97	\section{Downstream Utility}
98	\label{app:downstream}
99	\input{appendix_downstream}
100	
101	\section{Cross-Model Chain Per-Class Detail}
102	\label{app:cross-model-detail}
103	\input{appendix_cross_model_detail}
104	
105	\section{Feature Distribution Analysis}
106	\label{app:feature-distributions}
107	\input{appendix_feature_distributions}
108	
109	\section{Cross-Temperature Transfer}
110	\label{app:cross-temp}
111	\input{appendix_cross_temp}
112	\FloatBarrier
113	
114	\section{Feature Ablation}
115	\label{app:ablation-table}
116	\input{appendix_ablation}
117	
118	\input{appendix_feature_correlation}
119	
120	\section{Cross-Family Reference Models}
121	\label{app:cross-ref}
122	\input{table4}
123	
124	\input{appendix_seed_control}
125	
126	\input{appendix_tost}
127	\FloatBarrier
128	
129	\input{appendix_tost_bootstrap}
130	
131	\section{DDR Partition Validation}
132	\label{app:ddr-validation}
133	\input{appendix_ddr_validation}
134	\FloatBarrier
135	
136	\section{Generator Subset Summary}
137	\label{app:gen-subsets-section}
138	\input{appendix_generator_subsets}
139	
140	\input{appendix_qualitative_examples}
141	
142	\section{Cross-Generator Transfer Analysis}
143	\label{app:transfer}
144	\input{appendix_transfer}
145	\FloatBarrier
146	
147	\section{Supplementary DDR Characterization}
148	\label{app:ddr-supplement}
149	
150	\subsection{Partition Stability Across Temperatures}
151	\label{app:ddr-temp-stability}
152	\input{appendix_temperature_stability}
153	
154	\subsection{Per-Feature Convergence Dynamics}
155	\label{app:convergence}
156	\input{appendix_convergence}
157	\FloatBarrier
158	
159	\subsection{DDR Causality Analysis}
160	\label{app:ddr-causality}
161	\input{appendix_ddr_causality}
162	
163	\subsection{Decoding Strategy Robustness}
164	\label{app:decoding-strategy}
165	\input{appendix_decoding_strategy}
166	
167	\input{appendix_9gen_scale}
168	
169	\subsection{Comparison with Concurrent Iterative-Generation Studies}
170	\label{app:iterative-comparison}
171	\input{appendix_iterative_comparison}
172	
173	\subsection{Token-Level NLL Distribution}
174	\label{app:nll-distribution}
175	\input{appendix_nll_distribution}
176	
177	\end{document}
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a2ccb667-936e-4e97-97c8-2af5f745d5d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.tex",
      "content": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{placeins}\n\\usepackage{multirow}\n\\usepackage{float}\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Classifying Recursive Generation Depth\\\\in Base-Model LLM Text}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\n\\noindent\\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).\nMain paper results (\\S\\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).\n\n\\input{appendix_dataset_stats}\n\n\\section{Length Confound Analysis}\n\\label{app:length}\n\\input{appendix_length}\n\n\\section{Prompt Type Generalization}\n\\label{app:prompt-type}\n\\input{appendix_prompt_type}\n\n\\section{Finer-Grained Depth Classification}\n\\label{app:finer-depth}\n\\input{appendix_finer_depth}\n\n\\section{End-to-End Depth Classification (QLoRA)}\n\\label{app:qlora}\n\\input{appendix_qlora}\n\n\\section{Leave-One-Feature-Out Analysis}\n\\label{app:lofo}\n\\input{appendix_lofo}\n\n\\subsection{Candidate Feature Screening}\n\\label{app:feature-candidate}\n\\input{appendix_feature_candidates}\n\n\\section{Confusion Matrix}\n\\label{app:confusion}\n\\input{appendix_confusion_matrix}\n\n\\section{Classifier Sensitivity}\n\\label{app:classifier}\n\\input{appendix_classifier}\n\\FloatBarrier\n\n\\section{Robustness to Text Perturbation}\n\\label{app:human-edit}\n\\input{appendix_human_edit}\n\n\\section{Cross-Domain Generalization}\n\\label{app:domain}\n\\input{appendix_domain}\n\n\\section{Instruction-Tuned Model Analysis}\n\\label{app:instruct}\n\\input{appendix_instruct}\n\n\\section{Error Analysis of Binary Classification}\n\\label{app:error-analysis}\n\\input{appendix_error_analysis}\n\n\\section{Downstream Utility}\n\\label{app:downstream}\n\\input{appendix_downstream}\n\n\\section{Cross-Model Chain Per-Class Detail}\n\\label{app:cross-model-detail}\n\\input{appendix_cross_model_detail}\n\n\\section{Feature Distribution Analysis}\n\\label{app:feature-distributions}\n\\input{appendix_feature_distributions}\n\n\\section{Cross-Temperature Transfer}\n\\label{app:cross-temp}\n\\input{appendix_cross_temp}\n\\FloatBarrier\n\n\\section{Feature Ablation}\n\\label{app:ablation-table}\n\\input{appendix_ablation}\n\n\\input{appendix_feature_correlation}\n\n\\section{Cross-Family Reference Models}\n\\label{app:cross-ref}\n\\input{table4}\n\n\\input{appendix_seed_control}\n\n\\input{appendix_tost}\n\\FloatBarrier\n\n\\input{appendix_tost_bootstrap}\n\n\\section{DDR Partition Validation}\n\\label{app:ddr-validation}\n\\input{appendix_ddr_validation}\n\\FloatBarrier\n\n\\section{Generator Subset Summary}\n\\label{app:gen-subsets-section}\n\\input{appendix_generator_subsets}\n\n\\input{appendix_qualitative_examples}\n\n\\section{Cross-Generator Transfer Analysis}\n\\label{app:transfer}\n\\input{appendix_transfer}\n\\FloatBarrier\n\n\\section{Supplementary DDR Characterization}\n\\label{app:ddr-supplement}\n\n\\subsection{Partition Stability Across Temperatures}\n\\label{app:ddr-temp-stability}\n\\input{appendix_temperature_stability}\n\n\\subsection{Per-Feature Convergence Dynamics}\n\\label{app:convergence}\n\\input{appendix_convergence}\n\\FloatBarrier\n\n\\subsection{DDR Causality Analysis}\n\\label{app:ddr-causality}\n\\input{appendix_ddr_causality}\n\n\\subsection{Decoding Strategy Robustness}\n\\label{app:decoding-strategy}\n\\input{appendix_decoding_strategy}\n\n\\input{appendix_9gen_scale}\n\n\\subsection{Comparison with Concurrent Iterative-Generation Studies}\n\\label{app:iterative-comparison}\n\\input{appendix_iterative_comparison}\n\n\\subsection{Token-Level NLL Distribution}\n\\label{app:nll-distribution}\n\\input{appendix_nll_distribution}\n\n\\end{document}\n",
      "numLines": 178,
      "startLine": 1,
      "totalLines": 178
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of all the files. Let me process each task:

**2a. R34-W3: QLoRA 6-gen subset 标注** — Already present in all three locations:
- `results.tex` line 17: "6-generator LOGO ($+$11.6\,pp vs.\ the same-subset XGBoost baseline of 0.789"
- `method.tex` line 32: "($+$11.6\,pp, 6-gen LOGO; Appendix~\ref{app:qlora})"


- `appendix_qlora.tex` lines 4 and 25 also contain the same metrics — this is complete.

**2b. R38-W3: 术语一致性** — Checking terminology consistency. "Recursive generation depth" doesn't appear anywhere, so that's already clean. For DDR usage, it's consistently applied as "DDR partition" throughout the paper.

Now examining the QLoRA configuration details in Table 7 — the caption describes "end-to-end depth classification vs. XGBoost on handcrafted features," while the setup specifies "LoRA rank 16, learning rate $2 \times 10^{-4}$, and 3 epochs," and the hyperparameter robustness section mentions "LoRA rank 32" — need to verify these configurations align properly across sections. The appendix labels this as `app:qlora` and describes the LoRA setup with rank 16 for the main experiment and rank 32 for robustness testing, but neither alpha nor target modules are specified. Since the task asks me to flag missing information and add it if needed, I should note that these standard LoRA hyperparameters are absent from the documentation. The caption and description are consistent since neither mentions rank, alpha, or target modules, but the setup is incomplete—it's missing alpha and target modules specifications. Now I'm checking the color consistency between Figure 1 and Figure 2 by looking at how they're described in the results and then verifying against the actual Python source files. The watermark bibliography entry is already properly tagged as a blog post.

I need to track down the Diaz and Karampatziakis 2019 citation on soft labels for ordinal regression and add it to the bibliography. I'm also going through several arXiv entries to see which ones have been formally published—checking the recent ones from 2026 first since they're unlikely to be published yet, then working backward through 2024 and 2023 entries to see if any have official publication records. Looking at the publication status more carefully — Llama 3 and Mistral 7B are both technical reports that typically remain on arXiv rather than being formally published at conferences. For the bibliography check, I should focus on identifying the obviously published papers rather than doing exhaustive searches on each one, since the task specifies I don't need to WebSearch every entry. wait, looking more carefully:
- `release_strategies` (2019) is arXiv — this is a policy paper, probably never published at a venue
- `qwen3` is labeled `journal = {arXiv preprint}` — it's a tech report, fine as arXiv
- `llama3` is labeled `journal = {arXiv preprint}` — fine as tech report

For the 2023-2025 entries specifically:
- `briesch_self_consuming` (2023): "Large Language Models Suffer From Their Own Output" — I'll need to check
- `koike_mia_detection` (2025): "Machine Text Detectors are Membership Inference Attacks" — could be at ACL/EMNLP
- `seddik_synthetic_data` (2024): might be at a venue now
- `two_birds` (2025): arXiv:2508.14190 — very recent (2025-08), likely not yet published

The `markovian_chains` entry from 2026 is too recent to have venue publication. For the well-known papers like llama3 and mistral7b, I should verify whether they've moved from arXiv to formal venues — the llama3 paper with arXiv:2407.21783 appears to be a preprint that hasn't been formally published yet. The real issue I'm looking for is catching cases where a paper actually appeared at a conference like NeurIPS 2024 but is still cited as arXiv, so I need to check entries like `seddik_synthetic_data` more carefully.

Let me start with the practical tasks: checking the Python files for color consistency, searching for the ordinal regression paper, and reviewing the bibliography entries more thoroughly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "25f6e422-b172-45ad-904c-e01719c9e325",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvWFs3fatjmVVmkrfY52UJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24836,
      "cache_read_input_tokens": 29499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24836
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

_source line 80_

Now let me check the figure source files and search for the ordinal regression citation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c850686a-14aa-44ec-b1fc-d20fc3d7d23d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvWFs3fatjmVVmkrfY52UJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24836,
      "cache_read_input_tokens": 29499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24836
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

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_01B1PsBRZWhSALpdVjMTjFhV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v3.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "99d964cf-d1e8-4aee-b8ed-7f330a29fc73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvWFs3fatjmVVmkrfY52UJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24836,
      "cache_read_input_tokens": 29499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24836
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

_source line 82 · 2026-05-21T08:41:46.604Z_

<details><summary>↩ Tool result · `toolu_01B1PsBRZWhSALpdVjMTjFhV`</summary>

```text
1	"""Figure 1: Differential Depth Response — redesigned as strip/forest plot.
2	Wong colorblind-safe palette, diamond grand means, per-generator dots."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import matplotlib.patches as mpatches
7	import numpy as np
8	import json
9	
10	# ── Data ──
11	with open('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/rebuttal/spearman_per_generator.json') as f:
12	    data = json.load(f)
13	
14	features = [
15	    ('hapax_ratio',   r'Hapax ratio',                      'drifting',     0.76),
16	    ('ttr',           r'TTR',                               'drifting',     0.88),
17	    ('entropy_mean',  r'$\bar{H}$ (entropy mean)',          'drifting',     1.17),
18	    ('entropy_std',   r'$\sigma_H$ (entropy std)',          'intermediate', 0.55),
19	    ('entropy_min',   r'$H_{\min}$ (entropy min)',          'near-stat',    0.016),
20	    ('entropy_max',   r'$H_{\max}$ (entropy max)',          'near-stat',    0.08),
21	    ('tail_decay',    r'Tail decay',                        'near-stat',    0.08),
22	]
23	
24	generators = list(data.keys())
25	gen_short = ['Py-1B', 'Py-2.8B', 'OLMo', 'Qw-0.6B', 'Qw-1.7B', 'Qw-8B', 'Llama', 'Mistral']
26	
27	# ── Style ── (Wong colorblind-safe from Nature Methods)
28	C_DRIFT  = '#0072B2'   # blue
29	C_INTERM = '#882255'   # wine/mauve (Tol palette)
30	C_STAT   = '#E69F00'   # amber
31	C_BG_DRIFT  = '#0072B2'
32	C_BG_INTERM = '#882255'
33	C_BG_STAT   = '#E69F00'
34	
35	zone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'near-stat': C_STAT}
36	
37	plt.rcParams.update({
38	    'font.family': 'serif',
39	    'font.serif': ['DejaVu Serif'],
40	    'font.size': 8,
41	    'axes.labelsize': 9,
42	    'xtick.labelsize': 7.5,
43	    'ytick.labelsize': 8,
44	    'figure.dpi': 300,
45	    'savefig.dpi': 300,
46	    'savefig.bbox': 'tight',
47	    'savefig.pad_inches': 0.04,
48	    'mathtext.fontset': 'cm',
49	})
50	
51	n = len(features)
52	y_pos = np.arange(n)[::-1]
53	
54	fig, ax = plt.subplots(figsize=(3.25, 2.6))
55	
56	# ── Zone background shading ──
57	# Order: [0]=hapax, [1]=TTR, [2]=ent_mean, [3]=ent_std, [4]=ent_min, [5]=ent_max, [6]=tail
58	zone_ranges = {
59	    'drifting':     (y_pos[2] - 0.42, y_pos[0] + 0.42),
60	    'intermediate': (y_pos[3] - 0.42, y_pos[3] + 0.42),
61	    'near-stat':    (y_pos[6] - 0.42, y_pos[4] + 0.42),
62	}
63	for zone, (ylo, yhi) in zone_ranges.items():
64	    ax.axhspan(ylo, yhi, color=zone_color[zone], alpha=0.045, zorder=0)
65	
66	# ── Separator lines between zones ──
67	sep1 = (y_pos[2] + y_pos[3]) / 2
68	sep2 = (y_pos[3] + y_pos[4]) / 2
69	ax.axhline(sep1, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)
70	ax.axhline(sep2, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)
71	
72	# ── Zero line ──
73	ax.axvline(0, color='#bbbbbb', linewidth=0.6, linestyle='-', zorder=1)
74	
75	# ── Per-generator dots + grand mean diamond ──
76	gen_markers = ['o', 's', '^', 'D', 'v', 'P', 'X', '*']
77	np.random.seed(42)
78	
79	for i, (feat_key, label, zone, d_val) in enumerate(features):
80	    yi = y_pos[i]
81	    c = zone_color[zone]
82	
83	    vals = [data[g][feat_key] for g in generators]
84	    grand_mean = np.mean(vals)
85	
86	    jitter = np.linspace(-0.18, 0.18, len(vals))
87	
88	    for j, (v, gm) in enumerate(zip(vals, gen_markers)):
89	        ax.scatter(v, yi + jitter[j], marker='o', s=12,
90	                   color=c, alpha=0.40, edgecolors='none', zorder=3,
91	                   linewidths=0)
92	
93	    # Grand mean: diamond marker with white edge
94	    ax.scatter(grand_mean, yi, marker='D', s=45, color=c,
95	               edgecolors='white', linewidths=0.7, zorder=5)
96	
97	    # Thin connecting line from min to max (range)
98	    ax.plot([min(vals), max(vals)], [yi, yi],
99	            color=c, linewidth=0.9, alpha=0.30, zorder=2, solid_capstyle='round')
100	
101	# ── Y-axis labels ──
102	ax.set_yticks(y_pos)
103	ax.set_yticklabels([f[1] for f in features], fontsize=7)
104	
105	# ── X-axis ──
106	ax.set_xlabel(r'Spearman $\rho$ with generation depth', fontsize=8)
107	ax.set_xlim(-0.82, 0.22)
108	ax.set_ylim(-0.55, n - 0.45)
109	
110	# ── Axis styling ──
111	ax.spines['top'].set_visible(False)
112	ax.spines['right'].set_visible(False)
113	ax.spines['left'].set_visible(False)
114	ax.spines['bottom'].set_color('#999999')
115	ax.spines['bottom'].set_linewidth(0.5)
116	ax.tick_params(axis='y', length=0)
117	ax.tick_params(axis='x', length=3, width=0.5, color='#999999')
118	
119	# ── Zone labels on right margin ──
120	zone_info = [
121	    ('drifting',     (y_pos[0] + y_pos[2]) / 2,  'Drifting',         r'$d = 0.76$–$1.17$'),
122	    ('intermediate', y_pos[3],                     'Intermediate',     r'$d = 0.55$'),
123	    ('near-stat',    (y_pos[4] + y_pos[6]) / 2,   'Near-stationary',  r'$d < 0.10$'),
124	]
125	for zone, ym, lbl, sub in zone_info:
126	    ax.text(0.20, ym + 0.15, lbl, fontsize=5.5, color=zone_color[zone],
127	            fontweight='bold', va='bottom', ha='right', style='italic')
128	    ax.text(0.20, ym - 0.15, sub, fontsize=5, color=zone_color[zone],
129	            va='top', ha='right')
130	
131	# ── Legend ──
132	legend_elements = [
133	    plt.scatter([], [], marker='o', s=14, color='#666', alpha=0.5,
134	                edgecolors='none', label='Per-generator'),
135	    plt.scatter([], [], marker='D', s=50, color='#666',
136	                edgecolors='white', linewidths=0.8, label='Grand mean'),
137	]
138	leg = ax.legend(handles=legend_elements, loc='lower left',
139	                fontsize=5.5, frameon=True, framealpha=0.9,
140	                edgecolor='#dddddd', fancybox=False,
141	                handletextpad=0.3, borderpad=0.4,
142	                bbox_to_anchor=(0.0, 0.0))
143	leg.get_frame().set_linewidth(0.4)
144	
145	plt.tight_layout()
146	
147	out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
148	fig.savefig(f'{out}/fig1_differential_response.pdf', format='pdf')
149	fig.savefig(f'{out}/fig1_differential_response.png', format='png')
150	print(f'Saved to {out}/')
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "dfb04abb-6bca-4cbd-88b4-f34054676c11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig1_ddr_v3.py",
      "content": "\"\"\"Figure 1: Differential Depth Response — redesigned as strip/forest plot.\nWong colorblind-safe palette, diamond grand means, per-generator dots.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nimport numpy as np\nimport json\n\n# ── Data ──\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/rebuttal/spearman_per_generator.json') as f:\n    data = json.load(f)\n\nfeatures = [\n    ('hapax_ratio',   r'Hapax ratio',                      'drifting',     0.76),\n    ('ttr',           r'TTR',                               'drifting',     0.88),\n    ('entropy_mean',  r'$\\bar{H}$ (entropy mean)',          'drifting',     1.17),\n    ('entropy_std',   r'$\\sigma_H$ (entropy std)',          'intermediate', 0.55),\n    ('entropy_min',   r'$H_{\\min}$ (entropy min)',          'near-stat',    0.016),\n    ('entropy_max',   r'$H_{\\max}$ (entropy max)',          'near-stat',    0.08),\n    ('tail_decay',    r'Tail decay',                        'near-stat',    0.08),\n]\n\ngenerators = list(data.keys())\ngen_short = ['Py-1B', 'Py-2.8B', 'OLMo', 'Qw-0.6B', 'Qw-1.7B', 'Qw-8B', 'Llama', 'Mistral']\n\n# ── Style ── (Wong colorblind-safe from Nature Methods)\nC_DRIFT  = '#0072B2'   # blue\nC_INTERM = '#882255'   # wine/mauve (Tol palette)\nC_STAT   = '#E69F00'   # amber\nC_BG_DRIFT  = '#0072B2'\nC_BG_INTERM = '#882255'\nC_BG_STAT   = '#E69F00'\n\nzone_color = {'drifting': C_DRIFT, 'intermediate': C_INTERM, 'near-stat': C_STAT}\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif'],\n    'font.size': 8,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 7.5,\n    'ytick.labelsize': 8,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.04,\n    'mathtext.fontset': 'cm',\n})\n\nn = len(features)\ny_pos = np.arange(n)[::-1]\n\nfig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n# ── Zone background shading ──\n# Order: [0]=hapax, [1]=TTR, [2]=ent_mean, [3]=ent_std, [4]=ent_min, [5]=ent_max, [6]=tail\nzone_ranges = {\n    'drifting':     (y_pos[2] - 0.42, y_pos[0] + 0.42),\n    'intermediate': (y_pos[3] - 0.42, y_pos[3] + 0.42),\n    'near-stat':    (y_pos[6] - 0.42, y_pos[4] + 0.42),\n}\nfor zone, (ylo, yhi) in zone_ranges.items():\n    ax.axhspan(ylo, yhi, color=zone_color[zone], alpha=0.045, zorder=0)\n\n# ── Separator lines between zones ──\nsep1 = (y_pos[2] + y_pos[3]) / 2\nsep2 = (y_pos[3] + y_pos[4]) / 2\nax.axhline(sep1, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)\nax.axhline(sep2, color='#cccccc', linewidth=0.5, linestyle='-', zorder=1)\n\n# ── Zero line ──\nax.axvline(0, color='#bbbbbb', linewidth=0.6, linestyle='-', zorder=1)\n\n# ── Per-generator dots + grand mean diamond ──\ngen_markers = ['o', 's', '^', 'D', 'v', 'P', 'X', '*']\nnp.random.seed(42)\n\nfor i, (feat_key, label, zone, d_val) in enumerate(features):\n    yi = y_pos[i]\n    c = zone_color[zone]\n\n    vals = [data[g][feat_key] for g in generators]\n    grand_mean = np.mean(vals)\n\n    jitter = np.linspace(-0.18, 0.18, len(vals))\n\n    for j, (v, gm) in enumerate(zip(vals, gen_markers)):\n        ax.scatter(v, yi + jitter[j], marker='o', s=12,\n                   color=c, alpha=0.40, edgecolors='none', zorder=3,\n                   linewidths=0)\n\n    # Grand mean: diamond marker with white edge\n    ax.scatter(grand_mean, yi, marker='D', s=45, color=c,\n               edgecolors='white', linewidths=0.7, zorder=5)\n\n    # Thin connecting line from min to max (range)\n    ax.plot([min(vals), max(vals)], [yi, yi],\n            color=c, linewidth=0.9, alpha=0.30, zorder=2, solid_capstyle='round')\n\n# ── Y-axis labels ──\nax.set_yticks(y_pos)\nax.set_yticklabels([f[1] for f in features], fontsize=7)\n\n# ── X-axis ──\nax.set_xlabel(r'Spearman $\\rho$ with generation depth', fontsize=8)\nax.set_xlim(-0.82, 0.22)\nax.set_ylim(-0.55, n - 0.45)\n\n# ── Axis styling ──\nax.spines['top'].set_visible(False)\nax.spines['right'].set_visible(False)\nax.spines['left'].set_visible(False)\nax.spines['bottom'].set_color('#999999')\nax.spines['bottom'].set_linewidth(0.5)\nax.tick_params(axis='y', length=0)\nax.tick_params(axis='x', length=3, width=0.5, color='#999999')\n\n# ── Zone labels on right margin ──\nzone_info = [\n    ('drifting',     (y_pos[0] + y_pos[2]) / 2,  'Drifting',         r'$d = 0.76$–$1.17$'),\n    ('intermediate', y_pos[3],                     'Intermediate',     r'$d = 0.55$'),\n    ('near-stat',    (y_pos[4] + y_pos[6]) / 2,   'Near-stationary',  r'$d < 0.10$'),\n]\nfor zone, ym, lbl, sub in zone_info:\n    ax.text(0.20, ym + 0.15, lbl, fontsize=5.5, color=zone_color[zone],\n            fontweight='bold', va='bottom', ha='right', style='italic')\n    ax.text(0.20, ym - 0.15, sub, fontsize=5, color=zone_color[zone],\n            va='top', ha='right')\n\n# ── Legend ──\nlegend_elements = [\n    plt.scatter([], [], marker='o', s=14, color='#666', alpha=0.5,\n                edgecolors='none', label='Per-generator'),\n    plt.scatter([], [], marker='D', s=50, color='#666',\n                edgecolors='white', linewidths=0.8, label='Grand mean'),\n]\nleg = ax.legend(handles=legend_elements, loc='lower left',\n                fontsize=5.5, frameon=True, framealpha=0.9,\n                edgecolor='#dddddd', fancybox=False,\n                handletextpad=0.3, borderpad=0.4,\n                bbox_to_anchor=(0.0, 0.0))\nleg.get_frame().set_linewidth(0.4)\n\nplt.tight_layout()\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'\nfig.savefig(f'{out}/fig1_differential_response.pdf', format='pdf')\nfig.savefig(f'{out}/fig1_differential_response.png', format='png')\nprint(f'Saved to {out}/')\n",
      "numLines": 151,
      "startLine": 1,
      "totalLines": 151
    }
  }
}
```

</details>

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_01NpVLVcXyMjKfWzC7tp6M7R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig_ddr_trajectory_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "aff0b7fc-ed9f-4679-8d31-5584e2f3ee61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvWFs3fatjmVVmkrfY52UJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24836,
      "cache_read_input_tokens": 29499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24836
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

_source line 84 · 2026-05-21T08:41:47.061Z_

<details><summary>↩ Tool result · `toolu_01NpVLVcXyMjKfWzC7tp6M7R`</summary>

```text
1	"""Figure 1: DDR trajectory — 2×2 panel showing drifting vs stationary features.
2	Wong colorblind-safe palette, diamond grand means, per-generator thin lines."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import numpy as np
7	import pandas as pd
8	
9	DATA = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/data/features_all_models.csv'
10	df = pd.read_csv(DATA)
11	
12	plt.rcParams.update({
13	    'font.family': 'serif',
14	    'font.serif': ['DejaVu Serif'],
15	    'font.size': 8,
16	    'axes.labelsize': 8,
17	    'xtick.labelsize': 7,
18	    'ytick.labelsize': 7,
19	    'figure.dpi': 300,
20	    'savefig.dpi': 300,
21	    'savefig.bbox': 'tight',
22	    'savefig.pad_inches': 0.04,
23	    'mathtext.fontset': 'cm',
24	})
25	
26	# Wong colorblind-safe palette (8 colors)
27	PALETTE = [
28	    '#0072B2',  # blue  — Pythia-2.8B
29	    '#56B4E9',  # sky   — Pythia-1B
30	    '#009E73',  # green — OLMo
31	    '#E69F00',  # amber — Qwen-0.6B
32	    '#D55E00',  # vermillion — Qwen-1.7B
33	    '#CC79A7',  # pink  — Qwen-8B
34	    '#F0E442',  # yellow — Llama (darkened below)
35	    '#882255',  # wine  — Mistral
36	]
37	
38	GENERATORS = [
39	    ('pythia-2.8b',      'Py-2.8B',   PALETTE[0]),
40	    ('pythia-1b',        'Py-1B',     PALETTE[1]),
41	    ('olmo-2-1b',        'OLMo',      PALETTE[2]),
42	    ('qwen3-0.6b',       'Qw-0.6B',   PALETTE[3]),
43	    ('qwen3-1.7b',       'Qw-1.7B',   PALETTE[4]),
44	    ('qwen3-8b',         'Qw-8B',     PALETTE[5]),
45	    ('llama-3.2-3b',     'Llama',     '#999900'),  # darkened yellow for visibility
46	    ('mistral-7b-v0.3',  'Mistral',   PALETTE[7]),
47	]
48	
49	C_DRIFT_MEAN = '#0072B2'   # blue — grand mean for drifting panels
50	C_STAT_MEAN  = '#E69F00'   # amber — grand mean for stationary panels
51	
52	features = [
53	    ('entropy_mean', r'Entropy Mean ($\bar{H}$)',  'drifting'),
54	    ('hapax_ratio',  r'Hapax Ratio',               'drifting'),
55	    ('entropy_max',  r'Entropy Max ($H_{\max}$)',   'stationary'),
56	    ('tail_decay',   r'Tail Decay',                 'stationary'),
57	]
58	
59	depths = sorted(df['depth'].unique())
60	
61	fig, axes = plt.subplots(2, 2, figsize=(6.8, 4.0), sharex=True)
62	panel_labels = ['(a)', '(b)', '(c)', '(d)']
63	
64	for idx, (feat, label, zone) in enumerate(features):
65	    ax = axes[idx // 2][idx % 2]
66	    c_mean = C_DRIFT_MEAN if zone == 'drifting' else C_STAT_MEAN
67	
68	    all_means = []
69	    for gen_name, gen_short, gen_color in GENERATORS:
70	        sub = df[df['model_name'] == gen_name]
71	        means = sub.groupby('depth')[feat].mean().reindex(depths)
72	        all_means.append(means.values)
73	        ax.plot(depths, means.values,
74	                color=gen_color, linewidth=0.8, alpha=0.5,
75	                marker='o', markersize=2.5, markeredgewidth=0, zorder=2)
76	
77	    grand = np.mean(all_means, axis=0)
78	    ax.plot(depths, grand,
79	            color=c_mean, linewidth=1.4, alpha=0.85, zorder=4)
80	    ax.scatter(depths, grand,
81	               color=c_mean, marker='D', s=30,
82	               edgecolors='white', linewidths=0.6, zorder=5)
83	
84	    # Spearman rho annotation
85	    from scipy.stats import spearmanr
86	    all_depth_vals = []
87	    all_feat_vals = []
88	    for gen_name, _, _ in GENERATORS:
89	        sub = df[df['model_name'] == gen_name]
90	        all_depth_vals.extend(sub['depth'].values)
91	        all_feat_vals.extend(sub[feat].values)
92	    rho, _ = spearmanr(all_depth_vals, all_feat_vals)
93	    ax.text(0.97, 0.95, rf'$\rho = {rho:.3f}$',
94	            transform=ax.transAxes, fontsize=6.5,
95	            va='top', ha='right', color='#555',
96	            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
97	                      edgecolor='#ddd', linewidth=0.4, alpha=0.9))
98	
99	    ax.set_title(f'{panel_labels[idx]} {label}', fontsize=8, pad=4,
100	                 loc='left', fontweight='normal')
101	
102	    ax.spines['top'].set_visible(False)
103	    ax.spines['right'].set_visible(False)
104	    ax.spines['left'].set_color('#999')
105	    ax.spines['left'].set_linewidth(0.5)
106	    ax.spines['bottom'].set_color('#999')
107	    ax.spines['bottom'].set_linewidth(0.5)
108	    ax.tick_params(length=3, width=0.5, color='#999')
109	    ax.set_xticks(depths)
110	
111	    if idx >= 2:
112	        ax.set_xlabel('Generation Depth', fontsize=7.5)
113	
114	# Suppress x labels on top row
115	for ax in axes[0]:
116	    ax.xaxis.set_tick_params(labelbottom=False)
117	
118	# Row group labels
119	fig.text(0.005, 0.73, 'Drifting', fontsize=7.5, fontweight='bold',
120	         color='#0072B2', rotation=90, va='center', ha='left')
121	fig.text(0.005, 0.30, 'Stationary', fontsize=7.5, fontweight='bold',
122	         color='#E69F00', rotation=90, va='center', ha='left')
123	
124	# Legend: generators + grand mean
125	from matplotlib.lines import Line2D
126	handles = []
127	for _, gen_short, gen_color in GENERATORS:
128	    handles.append(Line2D([0], [0], color=gen_color, linewidth=0.8,
129	                          alpha=0.6, marker='o', markersize=2.5,
130	                          markeredgewidth=0, label=gen_short))
131	handles.append(Line2D([0], [0], color='#0072B2', linewidth=0, marker='D',
132	                       markersize=5, markeredgecolor='white',
133	                       markeredgewidth=0.6, label='Grand Mean'))
134	
135	fig.legend(handles=handles, loc='lower center', ncol=5,
136	           fontsize=5.5, frameon=True, framealpha=0.95,
137	           edgecolor='#ddd', fancybox=False,
138	           handletextpad=0.3, columnspacing=1.0,
139	           bbox_to_anchor=(0.5, -0.02))
140	
141	plt.tight_layout(rect=[0.03, 0.06, 1, 1])
142	plt.subplots_adjust(hspace=0.25, wspace=0.28)
143	
144	out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'
145	fig.savefig(f'{out}/fig_ddr_trajectory.pdf', format='pdf')
146	fig.savefig(f'{out}/fig_ddr_trajectory.png', format='png')
147	print(f'Saved trajectory figure to {out}/')
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "db49369d-d061-4330-8a75-dd96f941d7bc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart/fig_ddr_trajectory_v2.py",
      "content": "\"\"\"Figure 1: DDR trajectory — 2×2 panel showing drifting vs stationary features.\nWong colorblind-safe palette, diamond grand means, per-generator thin lines.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\nDATA = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/data/features_all_models.csv'\ndf = pd.read_csv(DATA)\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif'],\n    'font.size': 8,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.04,\n    'mathtext.fontset': 'cm',\n})\n\n# Wong colorblind-safe palette (8 colors)\nPALETTE = [\n    '#0072B2',  # blue  — Pythia-2.8B\n    '#56B4E9',  # sky   — Pythia-1B\n    '#009E73',  # green — OLMo\n    '#E69F00',  # amber — Qwen-0.6B\n    '#D55E00',  # vermillion — Qwen-1.7B\n    '#CC79A7',  # pink  — Qwen-8B\n    '#F0E442',  # yellow — Llama (darkened below)\n    '#882255',  # wine  — Mistral\n]\n\nGENERATORS = [\n    ('pythia-2.8b',      'Py-2.8B',   PALETTE[0]),\n    ('pythia-1b',        'Py-1B',     PALETTE[1]),\n    ('olmo-2-1b',        'OLMo',      PALETTE[2]),\n    ('qwen3-0.6b',       'Qw-0.6B',   PALETTE[3]),\n    ('qwen3-1.7b',       'Qw-1.7B',   PALETTE[4]),\n    ('qwen3-8b',         'Qw-8B',     PALETTE[5]),\n    ('llama-3.2-3b',     'Llama',     '#999900'),  # darkened yellow for visibility\n    ('mistral-7b-v0.3',  'Mistral',   PALETTE[7]),\n]\n\nC_DRIFT_MEAN = '#0072B2'   # blue — grand mean for drifting panels\nC_STAT_MEAN  = '#E69F00'   # amber — grand mean for stationary panels\n\nfeatures = [\n    ('entropy_mean', r'Entropy Mean ($\\bar{H}$)',  'drifting'),\n    ('hapax_ratio',  r'Hapax Ratio',               'drifting'),\n    ('entropy_max',  r'Entropy Max ($H_{\\max}$)',   'stationary'),\n    ('tail_decay',   r'Tail Decay',                 'stationary'),\n]\n\ndepths = sorted(df['depth'].unique())\n\nfig, axes = plt.subplots(2, 2, figsize=(6.8, 4.0), sharex=True)\npanel_labels = ['(a)', '(b)', '(c)', '(d)']\n\nfor idx, (feat, label, zone) in enumerate(features):\n    ax = axes[idx // 2][idx % 2]\n    c_mean = C_DRIFT_MEAN if zone == 'drifting' else C_STAT_MEAN\n\n    all_means = []\n    for gen_name, gen_short, gen_color in GENERATORS:\n        sub = df[df['model_name'] == gen_name]\n        means = sub.groupby('depth')[feat].mean().reindex(depths)\n        all_means.append(means.values)\n        ax.plot(depths, means.values,\n                color=gen_color, linewidth=0.8, alpha=0.5,\n                marker='o', markersize=2.5, markeredgewidth=0, zorder=2)\n\n    grand = np.mean(all_means, axis=0)\n    ax.plot(depths, grand,\n            color=c_mean, linewidth=1.4, alpha=0.85, zorder=4)\n    ax.scatter(depths, grand,\n               color=c_mean, marker='D', s=30,\n               edgecolors='white', linewidths=0.6, zorder=5)\n\n    # Spearman rho annotation\n    from scipy.stats import spearmanr\n    all_depth_vals = []\n    all_feat_vals = []\n    for gen_name, _, _ in GENERATORS:\n        sub = df[df['model_name'] == gen_name]\n        all_depth_vals.extend(sub['depth'].values)\n        all_feat_vals.extend(sub[feat].values)\n    rho, _ = spearmanr(all_depth_vals, all_feat_vals)\n    ax.text(0.97, 0.95, rf'$\\rho = {rho:.3f}$',\n            transform=ax.transAxes, fontsize=6.5,\n            va='top', ha='right', color='#555',\n            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',\n                      edgecolor='#ddd', linewidth=0.4, alpha=0.9))\n\n    ax.set_title(f'{panel_labels[idx]} {label}', fontsize=8, pad=4,\n                 loc='left', fontweight='normal')\n\n    ax.spines['top'].set_visible(False)\n    ax.spines['right'].set_visible(False)\n    ax.spines['left'].set_color('#999')\n    ax.spines['left'].set_linewidth(0.5)\n    ax.spines['bottom'].set_color('#999')\n    ax.spines['bottom'].set_linewidth(0.5)\n    ax.tick_params(length=3, width=0.5, color='#999')\n    ax.set_xticks(depths)\n\n    if idx >= 2:\n        ax.set_xlabel('Generation Depth', fontsize=7.5)\n\n# Suppress x labels on top row\nfor ax in axes[0]:\n    ax.xaxis.set_tick_params(labelbottom=False)\n\n# Row group labels\nfig.text(0.005, 0.73, 'Drifting', fontsize=7.5, fontweight='bold',\n         color='#0072B2', rotation=90, va='center', ha='left')\nfig.text(0.005, 0.30, 'Stationary', fontsize=7.5, fontweight='bold',\n         color='#E69F00', rotation=90, va='center', ha='left')\n\n# Legend: generators + grand mean\nfrom matplotlib.lines import Line2D\nhandles = []\nfor _, gen_short, gen_color in GENERATORS:\n    handles.append(Line2D([0], [0], color=gen_color, linewidth=0.8,\n                          alpha=0.6, marker='o', markersize=2.5,\n                          markeredgewidth=0, label=gen_short))\nhandles.append(Line2D([0], [0], color='#0072B2', linewidth=0, marker='D',\n                       markersize=5, markeredgecolor='white',\n                       markeredgewidth=0.6, label='Grand Mean'))\n\nfig.legend(handles=handles, loc='lower center', ncol=5,\n           fontsize=5.5, frameon=True, framealpha=0.95,\n           edgecolor='#ddd', fancybox=False,\n           handletextpad=0.3, columnspacing=1.0,\n           bbox_to_anchor=(0.5, -0.02))\n\nplt.tight_layout(rect=[0.03, 0.06, 1, 1])\nplt.subplots_adjust(hspace=0.25, wspace=0.28)\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'\nfig.savefig(f'{out}/fig_ddr_trajectory.pdf', format='pdf')\nfig.savefig(f'{out}/fig_ddr_trajectory.png', format='png')\nprint(f'Saved trajectory figure to {out}/')\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011G6aan65RXRryimLf8sU9Y`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a3a570af-0315-4bd9-8fec-a40be47456fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvWFs3fatjmVVmkrfY52UJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24836,
      "cache_read_input_tokens": 29499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24836
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

_source line 86 · 2026-05-21T08:41:47.381Z_

<details><summary>↩ Tool result · `toolu_011G6aan65RXRryimLf8sU9Y`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "455d1c8e-6055-4b37-88a8-bec0c3c0c168",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have the figure source files and WebSearch is loaded. Let me analyze what I've found so far and proceed with the remaining tasks.

**Color consistency check (2c):**
- Figure 1 (`fig1_ddr_v3.py`): 
  - Drifting = `#0072B2` (blue) ✓
  - Intermediate = `#882255` (wine) ✓  
  - Near-stationary = `#E69F00` (amber) ✓
- Figure 2 (`fig_ddr_trajectory_v2.py`):
  - Grand mean drifting = `#0072B2` (blue) ✓
  - Grand mean stationary = `#E69F00` (amber) ✓
  - Individual generators use different colors from Wong palette

The color scheme is consistent across both figures—blue for drifting and amber for stationary—and the figure captions in results.tex align with these choices.

Now I'm searching for the ordinal regression paper and verifying the bibliography entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "5e0dad96-c865-4c89-9057-cf94679d59ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrhV4JQtUuMVUP6gF2EDK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8566,
      "cache_read_input_tokens": 54335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8566
      },
      "output_tokens": 19,
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

_source line 88_

Color check is consistent between figures. Now searching for the ordinal regression citation and checking bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "69045f59-a31a-402c-ad65-43836a799bb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrhV4JQtUuMVUP6gF2EDK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8566,
      "cache_read_input_tokens": 54335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8566
      },
      "output_tokens": 19,
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

_source line 89_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4WJSfX96ZL3t6NFNEfrUL`</summary>

```json
{
  "query": "Diaz Karampatziakis 2019 Soft Labels Ordinal Regression CVPR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "cc56959c-d182-4669-9600-9fe4c9e68f18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrhV4JQtUuMVUP6gF2EDK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8566,
      "cache_read_input_tokens": 54335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8566
      },
      "output_tokens": 19,
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

_source line 90_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QutHo6446rH3gMSpSB1CVb`</summary>

```json
{
  "query": "Llama 3 herd of models published venue conference 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "8efc7b6b-ea59-4e26-9f80-a2101fc082c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrhV4JQtUuMVUP6gF2EDK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8566,
      "cache_read_input_tokens": 54335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8566
      },
      "output_tokens": 19,
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

_source line 91_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EWW28FxXuMLi3kLyp61GyL`</summary>

```json
{
  "query": "Mistral 7B Jiang 2023 published venue conference proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "62e972e8-0f9f-4907-8061-a03538317f49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrhV4JQtUuMVUP6gF2EDK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8566,
      "cache_read_input_tokens": 54335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8566
      },
      "output_tokens": 19,
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

_source line 92 · 2026-05-21T08:42:03.121Z_

<details><summary>↩ Tool result · `toolu_01EWW28FxXuMLi3kLyp61GyL`</summary>

```text
Web search results for query: "Mistral 7B Jiang 2023 published venue conference proceedings"

Links: [{"title":"[PDF] Mistral 7B | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mistral-7B-Jiang-Sablayrolles/db633c6b1c286c0386f0078d8a2e6224e03a6227"},{"title":"Mistral 7B for Argument Reasoning in Civil Procedure","url":"https://aclanthology.org/2024.semeval-1.24.pdf"},{"title":"Mistral 7B","url":"https://bibbase.org/network/publication/jiang-sablayrolles-mensch-bamford-chaplot-casas-bressand-lengyel-etal-mistral7b-2023"},{"title":"[2310.06825] Mistral 7B","url":"https://arxiv.org/abs/2310.06825"},{"title":"Mistral 7B | BibSonomy","url":"https://www.bibsonomy.org/bibtex/8f3889cfa5f3ce6e7d9c6db646399276"},{"title":"dblp: Mistral 7B.","url":"https://dblp.org/rec/journals/corr/abs-2310-06825.html"},{"title":"Mistral 7B","url":"https://arxiv.org/pdf/2310.06825"},{"title":"Mistral 7B - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231006825J/abstract"},{"title":"Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L.R., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T. and El Sayed, W. (2023) Mistral 7B. arXiv preprint arXiv2310.06825. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3652712"},{"title":"Paper page - Mistral 7B","url":"https://huggingface.co/papers/2310.06825"}]

Based on the search results, the Mistral 7B paper by Jiang et al. was published in ArXiv in 2023. More specifically, the paper was submitted on October 10, 2023, with the arXiv identifier arXiv2310.06825.

The paper was not published in a traditional conference proceedings venue, but rather as an arXiv preprint, which is a common publication method for machine learning research papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "34850f6d-1774-4df2-8bef-784e92bf74e0",
  "tool_use_result": {
    "query": "Mistral 7B Jiang 2023 published venue conference proceedings",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KpZuNeYNqmm9wks1GEjFSv",
        "content": [
          {
            "title": "[PDF] Mistral 7B | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Mistral-7B-Jiang-Sablayrolles/db633c6b1c286c0386f0078d8a2e6224e03a6227"
          },
          {
            "title": "Mistral 7B for Argument Reasoning in Civil Procedure",
            "url": "https://aclanthology.org/2024.semeval-1.24.pdf"
          },
          {
            "title": "Mistral 7B",
            "url": "https://bibbase.org/network/publication/jiang-sablayrolles-mensch-bamford-chaplot-casas-bressand-lengyel-etal-mistral7b-2023"
          },
          {
            "title": "[2310.06825] Mistral 7B",
            "url": "https://arxiv.org/abs/2310.06825"
          },
          {
            "title": "Mistral 7B | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/8f3889cfa5f3ce6e7d9c6db646399276"
          },
          {
            "title": "dblp: Mistral 7B.",
            "url": "https://dblp.org/rec/journals/corr/abs-2310-06825.html"
          },
          {
            "title": "Mistral 7B",
            "url": "https://arxiv.org/pdf/2310.06825"
          },
          {
            "title": "Mistral 7B - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv231006825J/abstract"
          },
          {
            "title": "Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L.R., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T. and El Sayed, W. (2023) Mistral 7B. arXiv preprint arXiv2310.06825. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3652712"
          },
          {
            "title": "Paper page - Mistral 7B",
            "url": "https://huggingface.co/papers/2310.06825"
          }
        ]
      },
      "Based on the search results, the Mistral 7B paper by Jiang et al. was published in ArXiv in 2023. More specifically, the paper was submitted on October 10, 2023, with the arXiv identifier arXiv2310.06825.\n\nThe paper was not published in a traditional conference proceedings venue, but rather as an arXiv preprint, which is a common publication method for machine learning research papers."
    ],
    "durationSeconds": 4.5375170039999935
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-21T08:42:03.967Z_

<details><summary>↩ Tool result · `toolu_01QutHo6446rH3gMSpSB1CVb`</summary>

```text
Web search results for query: "Llama 3 herd of models published venue conference 2024"

Links: [{"title":"The Llama 3 Herd of Models (2024) | Abhimanyu Dubey | 458 Citations","url":"https://scispace.com/papers/the-llama-3-herd-of-models-3uvee5wnnadv"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://liweinlp.com/wp-content/uploads/2024/07/meta.pdf"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"The Llama 3 Herd of Models | Snorkel AI","url":"https://snorkel.ai/research-paper/the-llama-3-herd-of-models/"},{"title":"The Llama 3 Herd of Models | Research - AI at Meta","url":"https://ai.meta.com/research/publications/the-llama-3-herd-of-models/"},{"title":"Breaking Down Meta's Llama 3 Herd of Models - Arize AI","url":"https://arize.com/blog/breaking-down-meta-llama-3/"},{"title":"dblp: The Llama 3 Herd of Models.","url":"https://dblp.org/rec/journals/corr/abs-2407-21783.html"},{"title":"The Llama 3 Herd of Models | Request PDF","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"}]

Based on the search results, here's what I found about the Llama 3 Herd of Models:

The paper "The Llama 3 Herd of Models" was published on arXiv on July 31, 2024, with the arXiv identifier 2407.21783. It was authored by the Llama Team at AI @ Meta.

The paper presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage, with the largest model being a dense Transformer with 405B parameters and a context window of up to 128K tokens.

However, the search results indicate this was published as an arXiv paper rather than at a traditional academic conference venue. The paper was released on arXiv in July 2024, making it an online technical preprint rather than a conference proceedings paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "333a5ddf-84a4-445a-b509-b050d27f1e94",
  "tool_use_result": {
    "query": "Llama 3 herd of models published venue conference 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NXzCrZTDLoGPN75v3ZanFS",
        "content": [
          {
            "title": "The Llama 3 Herd of Models (2024) | Abhimanyu Dubey | 458 Citations",
            "url": "https://scispace.com/papers/the-llama-3-herd-of-models-3uvee5wnnadv"
          },
          {
            "title": "The Llama 3 Herd of Models Llama Team, AI @ Meta1",
            "url": "https://liweinlp.com/wp-content/uploads/2024/07/meta.pdf"
          },
          {
            "title": "The Llama 3 Herd of Models Llama Team, AI @ Meta1",
            "url": "https://arxiv.org/pdf/2407.21783"
          },
          {
            "title": "[2407.21783] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783"
          },
          {
            "title": "The Llama 3 Herd of Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"
          },
          {
            "title": "The Llama 3 Herd of Models | Snorkel AI",
            "url": "https://snorkel.ai/research-paper/the-llama-3-herd-of-models/"
          },
          {
            "title": "The Llama 3 Herd of Models | Research - AI at Meta",
            "url": "https://ai.meta.com/research/publications/the-llama-3-herd-of-models/"
          },
          {
            "title": "Breaking Down Meta's Llama 3 Herd of Models - Arize AI",
            "url": "https://arize.com/blog/breaking-down-meta-llama-3/"
          },
          {
            "title": "dblp: The Llama 3 Herd of Models.",
            "url": "https://dblp.org/rec/journals/corr/abs-2407-21783.html"
          },
          {
            "title": "The Llama 3 Herd of Models | Request PDF",
            "url": "https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"
          }
        ]
      },
      "Based on the search results, here's what I found about the Llama 3 Herd of Models:\n\nThe paper \"The Llama 3 Herd of Models\" was published on arXiv on July 31, 2024, with the arXiv identifier 2407.21783. It was authored by the Llama Team at AI @ Meta.\n\nThe paper presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage, with the largest model being a dense Transformer with 405B parameters and a context window of up to 128K tokens.\n\nHowever, the search results indicate this was published as an arXiv paper rather than at a traditional academic conference venue. The paper was released on arXiv in July 2024, making it an online technical preprint rather than a conference proceedings paper."
    ],
    "durationSeconds": 5.978789512999996
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T08:42:04.388Z_

<details><summary>↩ Tool result · `toolu_01T4WJSfX96ZL3t6NFNEfrUL`</summary>

```text
Web search results for query: "Diaz Karampatziakis 2019 Soft Labels Ordinal Regression CVPR"

Links: [{"title":"Soft Labels for Ordinal Regression - CVF Open Access","url":"https://openaccess.thecvf.com/content_CVPR_2019/html/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.html"},{"title":"Soft Labels for Ordinal Regression","url":"https://www.computer.org/csdl/proceedings-article/cvpr/2019/329300e733/1gyr8A2OoRW"},{"title":"Soft Labels for Ordinal Regression | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8953836/"},{"title":"Ordinal Regression Research Based on Dual Loss Function—An Example on Lumbar Vertebra Classification in CT Images","url":"https://www.mdpi.com/2075-4418/15/23/2949"},{"title":"Calibration of ordinal regression networks","url":"https://arxiv.org/html/2410.15658v1"},{"title":"Soft Labels for Ordinal Regression","url":"https://openaccess.thecvf.com/content_CVPR_2019/papers/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.pdf"},{"title":"Soft Labels for Ordinal Regression","url":"https://www.researchgate.net/publication/338511937_Soft_Labels_for_Ordinal_Regression"},{"title":"Soft Labels for Ordinal Regression - Reading Collections","url":"https://owen-liuyuxuan.github.io/papers_reading_sharing.github.io/other_categories/depth_completion/OrdinalRegression/"},{"title":"Facial expression intensity estimation using label-distribution-learning-enhanced ordinal regression | Multimedia Systems","url":"https://link.springer.com/article/10.1007/s00530-023-01219-2"},{"title":"Classifying Phonotrauma Severity from Vocal Fold Images with Soft Ordinal Regression","url":"https://arxiv.org/pdf/2511.09702"}]

Based on the search results, I found information about this paper:

## "Soft Labels for Ordinal Regression" - Diaz & Marathe (2019)

The paper was authored by Raul Diaz and Amit Marathe and was published in the Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) in June 2019.

**Main Contribution:**
The method converts data labels into soft probability distributions that pair well with common categorical loss functions such as cross-entropy, and constrains ordinal relationships among categories by incorporating metric penalties into ground truth label representations, allowing deep neural networks to automatically learn intraclass and interclass relationships without any explicit modification of the network architecture.

**Applications:**
The approach was demonstrated to be effective using off-the-shelf classification and segmentation networks in four scenarios: image quality ranking, age estimation, horizon line regression, and monocular depth estimation.

The paper addresses the fundamental problem that ordinal regression attempts to solve classification problems in which categories are not independent but rather follow a natural order, and it is crucial to classify each class correctly while learning adequate interclass ordinal relationships.

The full paper is available through the Computer Vision Foundation's open access repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "86febf7e-28fe-496e-ba54-f84aa860a41d",
  "tool_use_result": {
    "query": "Diaz Karampatziakis 2019 Soft Labels Ordinal Regression CVPR",
    "results": [
      {
        "tool_use_id": "srvtoolu_019dAM1WG5CkL4msar5enfQA",
        "content": [
          {
            "title": "Soft Labels for Ordinal Regression - CVF Open Access",
            "url": "https://openaccess.thecvf.com/content_CVPR_2019/html/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.html"
          },
          {
            "title": "Soft Labels for Ordinal Regression",
            "url": "https://www.computer.org/csdl/proceedings-article/cvpr/2019/329300e733/1gyr8A2OoRW"
          },
          {
            "title": "Soft Labels for Ordinal Regression | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/8953836/"
          },
          {
            "title": "Ordinal Regression Research Based on Dual Loss Function—An Example on Lumbar Vertebra Classification in CT Images",
            "url": "https://www.mdpi.com/2075-4418/15/23/2949"
          },
          {
            "title": "Calibration of ordinal regression networks",
            "url": "https://arxiv.org/html/2410.15658v1"
          },
          {
            "title": "Soft Labels for Ordinal Regression",
            "url": "https://openaccess.thecvf.com/content_CVPR_2019/papers/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.pdf"
          },
          {
            "title": "Soft Labels for Ordinal Regression",
            "url": "https://www.researchgate.net/publication/338511937_Soft_Labels_for_Ordinal_Regression"
          },
          {
            "title": "Soft Labels for Ordinal Regression - Reading Collections",
            "url": "https://owen-liuyuxuan.github.io/papers_reading_sharing.github.io/other_categories/depth_completion/OrdinalRegression/"
          },
          {
            "title": "Facial expression intensity estimation using label-distribution-learning-enhanced ordinal regression | Multimedia Systems",
            "url": "https://link.springer.com/article/10.1007/s00530-023-01219-2"
          },
          {
            "title": "Classifying Phonotrauma Severity from Vocal Fold Images with Soft Ordinal Regression",
            "url": "https://arxiv.org/pdf/2511.09702"
          }
        ]
      },
      "Based on the search results, I found information about this paper:\n\n## \"Soft Labels for Ordinal Regression\" - Diaz & Marathe (2019)\n\nThe paper was authored by Raul Diaz and Amit Marathe and was published in the Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) in June 2019.\n\n**Main Contribution:**\nThe method converts data labels into soft probability distributions that pair well with common categorical loss functions such as cross-entropy, and constrains ordinal relationships among categories by incorporating metric penalties into ground truth label representations, allowing deep neural networks to automatically learn intraclass and interclass relationships without any explicit modification of the network architecture.\n\n**Applications:**\nThe approach was demonstrated to be effective using off-the-shelf classification and segmentation networks in four scenarios: image quality ranking, age estimation, horizon line regression, and monocular depth estimation.\n\nThe paper addresses the fundamental problem that ordinal regression attempts to solve classification problems in which categories are not independent but rather follow a natural order, and it is crucial to classify each class correctly while learning adequate interclass ordinal relationships.\n\nThe full paper is available through the Computer Vision Foundation's open access repository."
    ],
    "durationSeconds": 6.866714243000024
  }
}
```

</details>

---

### Assistant

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
OK, results:

1. **Diaz & Karampatziakis 2019** - Actually the paper is by Raul Diaz and Amit Marathe (NOT Karampatziakis). Published at CVPR 2019. Let me correct the bib entry.

2. **Llama 3** - Still arXiv preprint, not formally published at a conference. Keep as is.

3. **Mistral 7B** - Still arXiv preprint, not formally published. Keep as is.

Let me now check a few more potentially published papers:


- `seddik_synthetic_data` (2024)
- `briesch_self_consuming` (2023)
- `koike_mia_detection` (2025)

Looking at the recent entries, most of the 2026 papers are still arXiv preprints, so those stay as is. The 2025 entries like `koike_mia_detection` also appear to be preprints based on the arXiv identifiers.

Now I need to verify whether some of the older papers have been formally published. The `two_birds` paper from 2025, `seddik_synthetic_data` from 2024, and `briesch_self_consuming` from 2023 all have arXiv identifiers and might have found their way into actual venues by now. The `release_strategies` paper from 2019 is a known OpenAI policy paper that likely never went through formal peer review, so I'll leave that one as an arXiv entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "23589d22-44c0-4def-94e8-174abfcc1f8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9b4G4f8PC3VzWk936H9P1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1635,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 62901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 96_

The Diaz paper is actually by Diaz & Marathe (not Karampatziakis). Let me check the remaining arXiv entries that might have been formally published.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "de7b6b3c-96a1-4fcf-bba9-39394c111a32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9b4G4f8PC3VzWk936H9P1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1635,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 62901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 97_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RY8Q34irNB6w8CVzCJs48n`</summary>

```json
{
  "query": "seddik \"How Bad is Training on Synthetic Data\" 2024 published venue NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a3f38729-cb79-488a-ae9d-c905506b4848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9b4G4f8PC3VzWk936H9P1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1635,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 62901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 98_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019wHdoTwLwY5AR27QT2PHHS`</summary>

```json
{
  "query": "briesch \"Large Language Models Suffer From Their Own Output\" 2023 published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e459a4d9-8e60-40e3-a63e-9883731b79ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9b4G4f8PC3VzWk936H9P1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1635,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 62901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 99_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FVpVG46zQg6XmZDRUgSbjb`</summary>

```json
{
  "query": "koike \"Machine Text Detectors are Membership Inference Attacks\" 2025 published venue ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "95fb383c-28c4-4f24-84fa-842376d204f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9b4G4f8PC3VzWk936H9P1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1635,
      "cache_creation_input_tokens": 1412,
      "cache_read_input_tokens": 62901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1412
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

_source line 100 · 2026-05-21T08:42:23.267Z_

<details><summary>↩ Tool result · `toolu_019wHdoTwLwY5AR27QT2PHHS`</summary>

```text
Web search results for query: "briesch "Large Language Models Suffer From Their Own Output" 2023 published venue conference"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"[Submitted on 28 Nov 2023 (v1), last revised 17 Jun 2024 (this version, v2)]","url":"https://arxiv.org/pdf/2311.16822"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output:","url":"https://arxiv.org/pdf/2311.16822v1"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop" is by Martin Briesch and 2 other authors. The co-authors are Dominik Sobania and Franz Rothlauf from Johannes Gutenberg University, Mainz, Germany.

However, based on the search results, this appears to be a research paper published on arXiv rather than at a traditional conference. The paper was published in 2023 as an arXiv preprint (abs/2311.16822). The search results do not indicate that this paper was published at a specific conference venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "aa3dd094-a4f6-4248-ac18-79b6c4fe7593",
  "tool_use_result": {
    "query": "briesch \"Large Language Models Suffer From Their Own Output\" 2023 published venue conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y66nrZD4pQamNtpadoyBNv",
        "content": [
          {
            "title": "[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/abs/2311.16822"
          },
          {
            "title": "[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/abs/2311.16822v2"
          },
          {
            "title": "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://arxiv.org/html/2311.16822v2"
          },
          {
            "title": "[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"
          },
          {
            "title": "[Submitted on 28 Nov 2023 (v1), last revised 17 Jun 2024 (this version, v2)]",
            "url": "https://arxiv.org/pdf/2311.16822"
          },
          {
            "title": "[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop",
            "url": "https://ar5iv.labs.arxiv.org/html/2311.16822"
          },
          {
            "title": "Large Language Models Suffer From Their Own Output:",
            "url": "https://arxiv.org/pdf/2311.16822v1"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\" is by Martin Briesch and 2 other authors. The co-authors are Dominik Sobania and Franz Rothlauf from Johannes Gutenberg University, Mainz, Germany.\n\nHowever, based on the search results, this appears to be a research paper published on arXiv rather than at a traditional conference. The paper was published in 2023 as an arXiv preprint (abs/2311.16822). The search results do not indicate that this paper was published at a specific conference venue."
    ],
    "durationSeconds": 4.673606345000008
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-21T08:42:24.428Z_

<details><summary>↩ Tool result · `toolu_01FVpVG46zQg6XmZDRUgSbjb`</summary>

```text
Web search results for query: "koike "Machine Text Detectors are Membership Inference Attacks" 2025 published venue ACL EMNLP"

Links: [{"title":"[2510.19492] Machine Text Detectors are Membership Inference Attacks","url":"https://arxiv.org/abs/2510.19492"},{"title":"Machine Text Detectors are Membership Inference Attacks - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/62620ac8-49a3-4f3c-bc95-d4a650e1cbe0"},{"title":"Machine Text Detectors are Membership Inference Attacks","url":"https://arxiv.org/html/2510.19492"},{"title":"Preprint. MACHINE TEXT DETECTORS ARE MEMBERSHIP INFERENCE ATTACKS","url":"https://arxiv.org/pdf/2510.19492"},{"title":"Ryuto Koike - PhD at Science Tokyo | Prev: UPenn | AI safety and security | ryuryukke.github.io | LinkedIn","url":"https://www.linkedin.com/in/ryuto-koike/"},{"title":"MAGE: Machine-generated Text Detection in the Wild | Request PDF","url":"https://www.researchgate.net/publication/384198450_MAGE_Machine-generated_Text_Detection_in_the_Wild"},{"title":"[Literature Review] Machine Text Detectors are Membership Inference Attacks","url":"https://www.themoonlight.io/en/review/machine-text-detectors-are-membership-inference-attacks"},{"title":"Synthetic Data Can Mislead Evaluations: Membership Inference as Machine   Text Detection","url":"https://arxiv.org/pdf/2501.11786"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Machine Text Detectors are Membership Inference Attacks" was authored by Ryuto Koike and 3 other authors, with versions dated October 22, 2025 and February 10, 2026.

The full author list includes Ryuto Koike, Liam Dugan, Masahiro Kaneko, Chris Callison-Burch, and Naoaki Okazaki.

The paper demonstrates the transferability between membership inference attacks (MIAs) and machine-generated text detection, showing how methods originally developed for one task perform on the other.

However, the search results show this paper is currently available as a preprint on arXiv (paper ID 2510.19492) rather than at a published venue. I did not find evidence in the search results that it has been published at ACL or EMNLP. The paper appears to still be in preprint status as of February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e457f6f8-23af-4c2a-b4bf-5a139f890900",
  "tool_use_result": {
    "query": "koike \"Machine Text Detectors are Membership Inference Attacks\" 2025 published venue ACL EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RKuptMQhSXqUD7jEdjtLTX",
        "content": [
          {
            "title": "[2510.19492] Machine Text Detectors are Membership Inference Attacks",
            "url": "https://arxiv.org/abs/2510.19492"
          },
          {
            "title": "Machine Text Detectors are Membership Inference Attacks - Paper Details",
            "url": "https://www.chatpaper.ai/dashboard/paper/62620ac8-49a3-4f3c-bc95-d4a650e1cbe0"
          },
          {
            "title": "Machine Text Detectors are Membership Inference Attacks",
            "url": "https://arxiv.org/html/2510.19492"
          },
          {
            "title": "Preprint. MACHINE TEXT DETECTORS ARE MEMBERSHIP INFERENCE ATTACKS",
            "url": "https://arxiv.org/pdf/2510.19492"
          },
          {
            "title": "Ryuto Koike - PhD at Science Tokyo | Prev: UPenn | AI safety and security | ryuryukke.github.io | LinkedIn",
            "url": "https://www.linkedin.com/in/ryuto-koike/"
          },
          {
            "title": "MAGE: Machine-generated Text Detection in the Wild | Request PDF",
            "url": "https://www.researchgate.net/publication/384198450_MAGE_Machine-generated_Text_Detection_in_the_Wild"
          },
          {
            "title": "[Literature Review] Machine Text Detectors are Membership Inference Attacks",
            "url": "https://www.themoonlight.io/en/review/machine-text-detectors-are-membership-inference-attacks"
          },
          {
            "title": "Synthetic Data Can Mislead Evaluations: Membership Inference as Machine   Text Detection",
            "url": "https://arxiv.org/pdf/2501.11786"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper \"Machine Text Detectors are Membership Inference Attacks\" was authored by Ryuto Koike and 3 other authors, with versions dated October 22, 2025 and February 10, 2026.\n\nThe full author list includes Ryuto Koike, Liam Dugan, Masahiro Kaneko, Chris Callison-Burch, and Naoaki Okazaki.\n\nThe paper demonstrates the transferability between membership inference attacks (MIAs) and machine-generated text detection, showing how methods originally developed for one task perform on the other.\n\nHowever, the search results show this paper is currently available as a preprint on arXiv (paper ID 2510.19492) rather than at a published venue. I did not find evidence in the search results that it has been published at ACL or EMNLP. The paper appears to still be in preprint status as of February 2026."
    ],
    "durationSeconds": 5.469280117999995
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-21T08:42:24.986Z_

<details><summary>↩ Tool result · `toolu_01RY8Q34irNB6w8CVzCJs48n`</summary>

```text
Web search results for query: "seddik "How Bad is Training on Synthetic Data" 2024 published venue NeurIPS ICML"

Links: [{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/html/2502.07164v1"},{"title":"Why AI needs real human data, not just synthetic inputs | Prolific","url":"https://www.prolific.com/resources/synthetic-data-vs-human-data-why-ai-needs-a-human-intelligence-layer-to-succeed"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"How Bad is Training on Synthetic Data? A Statistical ...","url":"https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"Preprint MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA:","url":"https://www.researchgate.net/publication/384886872_Maximizing_the_Potential_of_Synthetic_Data_Insights_from_Random_Matrix_Theory/fulltext/670c8bd2dc91726ad3900444/Maximizing-the-Potential-of-Synthetic-Data-Insights-from-Random-Matrix-Theory.pdf"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"Mohamed El Amine Seddik (Researcher at TII): Papers, h-index, Citations & Profile | Bohrium","url":"https://www.bohrium.com/en/scholar/50i98892/Mohamed_El_Amine_Seddik"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory","url":"https://arxiv.org/pdf/2410.08942"}]

Based on the search results, I found information about the paper you're looking for:

"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" was published in the First Conference on Language Modeling in 2024. 

The paper was authored by Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Abdelkader Debbah.

To clarify the published venue: the paper was published as a conference paper at COLM 2024 (Conference on Language Modeling). The search results show this is the correct venue rather than NeurIPS or ICML. The paper was initially posted on arXiv in April 2024 before being published at the COLM conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "92771ee3-c412-4cd8-b43a-130a60f31183",
  "tool_use_result": {
    "query": "seddik \"How Bad is Training on Synthetic Data\" 2024 published venue NeurIPS ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ULeR3aMkkE9Qrj5Cx1GDVx",
        "content": [
          {
            "title": "Does Training on Synthetic Data Make Models Less Robust?",
            "url": "https://arxiv.org/html/2502.07164v1"
          },
          {
            "title": "Why AI needs real human data, not just synthetic inputs | Prolific",
            "url": "https://www.prolific.com/resources/synthetic-data-vs-human-data-why-ai-needs-a-human-intelligence-layer-to-succeed"
          },
          {
            "title": "[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/abs/2404.05090"
          },
          {
            "title": "MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical ...",
            "url": "https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"
          },
          {
            "title": "Preprint MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA:",
            "url": "https://www.researchgate.net/publication/384886872_Maximizing_the_Potential_of_Synthetic_Data_Insights_from_Random_Matrix_Theory/fulltext/670c8bd2dc91726ad3900444/Maximizing-the-Potential-of-Synthetic-Data-Insights-from-Random-Matrix-Theory.pdf"
          },
          {
            "title": "HOW TO PREVENT MODEL COLLAPSE IN SELF- ...",
            "url": "https://openreview.net/pdf?id=WttfQGwpES"
          },
          {
            "title": "Mohamed El Amine Seddik (Researcher at TII): Papers, h-index, Citations & Profile | Bohrium",
            "url": "https://www.bohrium.com/en/scholar/50i98892/Mohamed_El_Amine_Seddik"
          },
          {
            "title": "Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory",
            "url": "https://arxiv.org/pdf/2410.08942"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\" was published in the First Conference on Language Modeling in 2024. \n\nThe paper was authored by Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Abdelkader Debbah.\n\nTo clarify the published venue: the paper was published as a conference paper at COLM 2024 (Conference on Language Modeling). The search results show this is the correct venue rather than NeurIPS or ICML. The paper was initially posted on arXiv in April 2024 before being published at the COLM conference."
    ],
    "durationSeconds": 7.277934101000021
  }
}
```

</details>

---

### Assistant

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
OK, findings:

1. **seddik_synthetic_data** — Appears to have been published at COLM 2024. But wait, looking more carefully at the search results, I see one result mentioning "MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA" (a different paper), and one linking to openreview.net that might be for the actual paper. Let me check: the search result says "published in the First Conference on Language Modeling in 2024" but I'm not 100% sure this is correct. The arxiv page (2404.05090) shows it's still an arXiv paper. Let me look at the search results more carefully...
   
The OpenReview link suggests there might be a published version, and the search result explicitly states it was published at COLM 2024. If that's accurate, I should update the entry from an arXiv article to an inproceedings entry for COLM 2024. I notice the existing bibliography already has another paper, `model_collapse_avoidable`, listed as a COLM 2024 conference paper, so I can follow that same format.

For the other entries, I'm being practical about this — I'll focus on the ones I can clearly verify. The `briesch_self_consuming` and `koike_mia_detection` papers still appear to be arXiv preprints with no conference publications found. The main one worth double-checking is `seddik_synthetic_data` since the search results point to an OpenReview version that might correspond to a conference publication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a440c9d9-729e-4300-a433-2a42980e4798",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNT2VihtkurreA3MYoyP3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1321,
      "cache_creation_input_tokens": 3304,
      "cache_read_input_tokens": 64313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3304
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

_source line 104_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAHiHafQRpTArHz4nHuCUZ`</summary>

```json
{
  "query": "seddik \"How Bad is Training on Synthetic Data\" COLM 2024 conference language modeling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "aa9ac3ec-d052-45c5-b50a-8bf330fe37cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNT2VihtkurreA3MYoyP3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1321,
      "cache_creation_input_tokens": 3304,
      "cache_read_input_tokens": 64313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3304
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

_source line 105 · 2026-05-21T08:42:47.844Z_

<details><summary>↩ Tool result · `toolu_01SAHiHafQRpTArHz4nHuCUZ`</summary>

```text
Web search results for query: "seddik "How Bad is Training on Synthetic Data" COLM 2024 conference language modeling"

Links: [{"title":"How Bad is Training on Synthetic Data? A Statistical ...","url":"https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"},{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/html/2502.07164v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"},{"title":"MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"HOW TO PREVENT MODEL COLLAPSE IN SELF- ...","url":"https://openreview.net/pdf?id=WttfQGwpES"},{"title":"Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory","url":"https://arxiv.org/pdf/2410.08942"}]

I found the paper you're looking for! Here are the key details:

## Paper Information

"How Bad is Training on Synthetic Data?" was published as a conference paper at COLM 2024.

**Authors:** Mohamed El Amine Seddik (Technology Innovation Institute, Abu Dhabi), Suei-Wen Chen (NYU Abu Dhabi), Soufiane Hayou (Simons Institute, Berkeley), Pierre Youssef (NYU Abu Dhabi), and Merouane Debbah (Khalifa University of Science and Technology)

## Paper Summary

The paper analyzes the phenomenon of model collapse, which refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. This recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial (real) distribution.

**Key Findings:**

The paper demonstrates that model collapse cannot be avoided when training solely on synthetic data. However, when mixing both real and synthetic data, the researchers provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.

The paper is available on OpenReview (the COLM 2024 platform) and on arXiv (arxiv.org/abs/2404.05090).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b03a1ef7-8bd6-4168-8ae8-417f89db159d",
  "tool_use_result": {
    "query": "seddik \"How Bad is Training on Synthetic Data\" COLM 2024 conference language modeling",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QhtYELV1TCk8RtiVe5rcoV",
        "content": [
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical ...",
            "url": "https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"
          },
          {
            "title": "[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse",
            "url": "https://arxiv.org/abs/2404.05090"
          },
          {
            "title": "Does Training on Synthetic Data Make Models Less Robust?",
            "url": "https://arxiv.org/html/2502.07164v1"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2404.05090v1"
          },
          {
            "title": "[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"
          },
          {
            "title": "How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview",
            "url": "https://openreview.net/forum?id=t3z6UlV09o"
          },
          {
            "title": "MAXIMIZING THE POTENTIAL OF SYNTHETIC DATA",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf"
          },
          {
            "title": "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"
          },
          {
            "title": "HOW TO PREVENT MODEL COLLAPSE IN SELF- ...",
            "url": "https://openreview.net/pdf?id=WttfQGwpES"
          },
          {
            "title": "Maximizing the Potential of Synthetic Data: Insights from Random Matrix   Theory",
            "url": "https://arxiv.org/pdf/2410.08942"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n## Paper Information\n\n\"How Bad is Training on Synthetic Data?\" was published as a conference paper at COLM 2024.\n\n**Authors:** Mohamed El Amine Seddik (Technology Innovation Institute, Abu Dhabi), Suei-Wen Chen (NYU Abu Dhabi), Soufiane Hayou (Simons Institute, Berkeley), Pierre Youssef (NYU Abu Dhabi), and Merouane Debbah (Khalifa University of Science and Technology)\n\n## Paper Summary\n\nThe paper analyzes the phenomenon of model collapse, which refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. This recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial (real) distribution.\n\n**Key Findings:**\n\nThe paper demonstrates that model collapse cannot be avoided when training solely on synthetic data. However, when mixing both real and synthetic data, the researchers provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided.\n\nThe paper is available on OpenReview (the COLM 2024 platform) and on arXiv (arxiv.org/abs/2404.05090)."
    ],
    "durationSeconds": 8.578261916999995
  }
}
```

</details>

---

### Assistant

_source line 106_

<details><summary>Logged reasoning block</summary>

```text
OK, confirmed: `seddik_synthetic_data` was published at COLM 2024. I should update this entry.

Now let me also check if `two_birds` (2025, arXiv:2508.14190) has been published somewhere, since it's a 2025 paper that could have been accepted. Wait, arXiv:2508 would be August 2025 submission. Given the current date is May 2026, it could have been published. But the task says not to WebSearch every entry. Let me skip the marginal ones and focus on what I found.

Summary of all tasks:


I'm going through the remaining items to verify consistency. The QLoRA 6-gen subset annotation is already present everywhere, so that's confirmed. For the terminology consistency check, I'm verifying that "recursive generation depth" doesn't appear elsewhere, DDR usage is consistent throughout, and I'm noting a discrepancy in the appendix where the LoRA configuration mentions rank 16 but lacks alpha and target module specifications. Now I'm examining the figure-related items. Now I need to verify the float placement for Table 1 and Figure 2, then make the key edits: adding the Diaz & Marathe citation for ordinal regression, updating the seddik_synthetic_data entry from arXiv to COLM 2024, flagging the missing LoRA configuration details, and checking the float specifiers in the document. I've confirmed the correct authors are Raul Diaz and Amit Marathe from the CVPR 2019 paper on soft labels for ordinal regression. The best place to cite this is in the related work section where ordinal regression methods are discussed, since it directly relates to the ordinal nature of depth classification.

Writing bibtex entries...

Now I'm checking the float positioning in the results file to ensure tables and figures are properly placed with the correct placement specifiers. Looking at where the display items actually appear in the document flow, Table 2 from the method section would likely land on page 3 where the method begins, but Table 1 and Figure 2 from results come much later. The task specifically requires Table 1 and Figure 2 to appear within the first three pages, so I need to figure out how to move those earlier in the document. I need to compile the paper locally to verify the float positions work correctly, so let me start making the edits: adding the Diaz & Marathe bibliography entry, citing it in the related work section, updating the Seddik reference to COLM 2024, and then checking how Table 1 positions itself in the results section with its current `[t]` specifier.

For the display item requirement in the first three pages, the features table in method.tex already has `[t]` positioning, and Figure 2 (fig:feature-drift) is in results.tex around line 67—I should verify whether these will naturally fall within the first three pages or if I need to adjust their placement to meet that constraint. then compile and see what happens. Let me also check the introduction—it currently has no floats, and the task mentions adding a figure reference before `\input{method}`. I'm second-guessing what this means though. Adding a `\ref{}` citation won't actually move where LaTeX places the figure, since float placement depends on where the `\begin{figure}` environment appears in the source code, not where it's referenced. Maybe they mean inserting an actual figure environment, but that seems redundant. Let me re-read the task more carefully.

For the first approach about Table 1, I need to change its float specifier from `[t]` to something that forces it onto page 2. But Table 1 is in results.tex, so moving it earlier in the source would be necessary. Looking at main.tex, the features table in method.tex already uses `[t]` at line 38. In the two-column ACL format, page 1 has the title and abstract with the intro starting, page 2 continues the intro and related work, and page 3 follows. I should probably just compile first to see the current layout, then make adjustments as needed.

Actually, the task says to make all changes first before compiling. The features table in method.tex is the best candidate for appearing in the first three pages, so I'll change it to `[!t]` to force it to the top of its page. Moving Table 1 earlier would require either physically relocating it to an earlier section or using LaTeX tricks like `\afterpage`, which seems riskier. The safest approach is to make the text edits now and then compile to check the result.

Let me go through all the edits I need to make. I see the robustness paragraph mentions LoRA rank 32 with seed 123, so that's one configuration documented. The Table 7 caption doesn't specify hyperparameters, so there's no inconsistency there—but the description is still missing alpha and target modules values. Since I don't have the actual experimental parameters, I'll flag these as missing rather than guessing, and proceed with the edits I can confidently make.

Now I'm thinking through the table numbering in the LaTeX source. The features table in method.tex is positioned early in the document, so depending on how LaTeX orders the floats, it might end up as Table 1 or Table 2 in the final output. I need to check the actual compilation to see where everything lands. There's a mismatch between what the task describes and what I'm finding in the document structure. The task refers to "Table 1 (`tab:logo-results`)" but based on the section order, the features table should be Table 1 and the LOGO results table should be Table 2. Regardless of this discrepancy, the core objective is clear—I need to ensure the display item fits within the first three pages—so I'll proceed with the edits and verify by compiling.

I'm making three key changes: adding the missing Diaz citation to the bibliography, incorporating it into the related work section, and potentially adjusting float specifiers in the results if needed after compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e49a7736-a98b-44ea-bd37-7b2bb3cd0b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9jGhw8CkQTD9YoLwH5P8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 67617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 107_

Now I have all the information I need. Let me make the edits. Starting with the bib entries and citation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "210661a8-fea6-4a8d-b71d-e62ce6666ab4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9jGhw8CkQTD9YoLwH5P8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 67617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 108_

<details open><summary>🔧 Tool call — Edit · `toolu_01WBnjwDcxePnAcYya8dDoJq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "@article{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  journal = {arXiv preprint arXiv:2404.05090},\n  year = {2024},\n}",
  "new_string": "@inproceedings{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "387f9351-6647-4e95-8bb8-9b48aaefcb04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9jGhw8CkQTD9YoLwH5P8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 67617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 109 · 2026-05-21T08:44:26.993Z_

<details><summary>↩ Tool result · `toolu_01WBnjwDcxePnAcYya8dDoJq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c721a2f8-fdf3-41b8-9c6a-aef09df65b62",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "oldString": "@article{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  journal = {arXiv preprint arXiv:2404.05090},\n  year = {2024},\n}",
    "newString": "@inproceedings{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}",
    "originalFile": "% ===== Data Provenance / Contamination =====\n\n% ===== Statistics =====\n\n@book{cohen1988statistical,\n  title = {{Statistical Power Analysis for the Behavioral Sciences}},\n  author = {Cohen, Jacob},\n  edition = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1988},\n}\n\n% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2026},\n  eprint = {2509.18880},\n  archiveprefix = {arXiv},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{intrinsic_dim_detection,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n@inproceedings{schaeffer_collapse_position,\n  title = {{Position: Model Collapse Does Not Mean What You Think}},\n  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2025},\n  eprint = {2503.03150},\n  archiveprefix = {arXiv},\n}\n\n@inproceedings{drayson_detection_prevents_collapse,\n  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},\n  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  eprint = {2502.15654},\n  archiveprefix = {arXiv},\n}\n\n@article{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  journal = {arXiv preprint arXiv:2404.05090},\n  year = {2024},\n}\n\n% ===== Fine-tuning =====\n\n@inproceedings{qlora,\n  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},\n  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Data Quality =====\n\n% ===== (orphan entries removed: fineweb, dolma) =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Jan Hendrik},\n  year = {2022},\n  note = {Blog post},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {3},\n  pages = {538--556},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {1},\n  pages = {9--26},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n@article{briesch_self_consuming,\n  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal = {arXiv preprint arXiv:2311.16822},\n  year = {2023},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n@inproceedings{attractor_cycles,\n  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},\n  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n  eprint = {2502.15208},\n  archiveprefix = {arXiv},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{koike_mia_detection,\n  title = {{Machine Text Detectors are Membership Inference Attacks}},\n  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},\n  journal = {arXiv preprint arXiv:2510.19492},\n  year = {2025},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n@inproceedings{ghostbuster,\n  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{two_birds,\n  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},\n  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},\n  journal = {arXiv preprint arXiv:2508.14190},\n  year = {2025},\n}\n\n@inproceedings{beyond_final_actor,\n  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},\n  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2026},\n}\n\n% ===== Machine Learning =====\n\n@article{gutierrez_ordinal_survey,\n  title = {{Ordinal Regression Methods: Survey and Experimental Study}},\n  author = {Guti{\\'e}rrez, Pedro Antonio and P{\\'e}rez-Ortiz, Mar{\\'i}a and S{\\'a}nchez-Monedero, Javier and Fern{\\'a}ndez-Navarro, Francisco and Herv{\\'a}s-Mart{\\'i}nez, C{\\'e}sar},\n  journal = {IEEE Transactions on Knowledge and Data Engineering},\n  volume = {28},\n  number = {1},\n  pages = {127--146},\n  year = {2016},\n}\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@article{corn_ordinal,\n  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},\n  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},\n  journal = {Pattern Analysis and Applications},\n  volume = {26},\n  pages = {941--955},\n  year = {2023},\n}\n\n@inproceedings{kasa_ordinality_nlp,\n  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},\n  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year = {2024},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n\n@article{lakens_equivalence,\n  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},\n  author = {Lakens, Dani{\\\"e}l},\n  journal = {Social Psychological and Personality Science},\n  volume = {8},\n  number = {4},\n  pages = {355--362},\n  year = {2017},\n}\n\n% ===== Generator Model References =====\n\n@article{llama3,\n  title = {{The Llama 3 Herd of Models}},\n  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n}\n\n@article{mistral7b,\n  title = {{Mistral 7B}},\n  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},\n  journal = {arXiv preprint arXiv:2310.06825},\n  year = {2023},\n}\n\n@article{strobl_conditional_2008,\n  title = {Conditional Variable Importance for Random Forests},\n  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},\n  journal = {BMC Bioinformatics},\n  volume = {9},\n  pages = {307},\n  year = {2008},\n}\n\n% --- Entries from Paper Agent (docs/paper) ---\n\n@inproceedings{dolma,\n  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},\n  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n\n@inproceedings{fineweb,\n  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  author = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year = {2024},\n}\n\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n\n\n@inproceedings{raid,\n  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},\n  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2024},\n  address = {Bangkok, Thailand},\n  publisher = {Association for Computational Linguistics},\n  pages = {12463--12492},\n}\n\n% ===== Distribution Quality =====\n\n@inproceedings{mauve,\n  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},\n  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2021},\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 177,
        "oldLines": 10,
        "newStart": 177,
        "newLines": 10,
        "lines": [
          "   archiveprefix = {arXiv},",
          " }",
          " ",
          "-@article{seddik_synthetic_data,",
          "+@inproceedings{seddik_synthetic_data,",
          "   title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},",
          "   author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},",
          "-  journal = {arXiv preprint arXiv:2404.05090},",
          "+  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},",
          "   year = {2024},",
          " }",
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

_source line 110_

<details open><summary>🔧 Tool call — Edit · `toolu_01MgSqAjnMYLoggobvHVLX7r`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "old_string": "@inproceedings{kasa_ordinality_nlp,",
  "new_string": "@inproceedings{diaz_soft_labels_ordinal,\n  title = {{Soft Labels for Ordinal Regression}},\n  author = {Diaz, Raul and Marathe, Amit},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  year = {2019},\n}\n\n@inproceedings{kasa_ordinality_nlp,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b153f92c-af48-4bcd-9ec2-fcf8ec970849",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9jGhw8CkQTD9YoLwH5P8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2828,
      "cache_read_input_tokens": 67617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2828
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

_source line 111 · 2026-05-21T08:44:28.580Z_

<details><summary>↩ Tool result · `toolu_01MgSqAjnMYLoggobvHVLX7r`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e0d4eca2-c1f9-48c4-9280-7c4b56954c36",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "oldString": "@inproceedings{kasa_ordinality_nlp,",
    "newString": "@inproceedings{diaz_soft_labels_ordinal,\n  title = {{Soft Labels for Ordinal Regression}},\n  author = {Diaz, Raul and Marathe, Amit},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},\n  year = {2019},\n}\n\n@inproceedings{kasa_ordinality_nlp,",
    "originalFile": "% ===== Data Provenance / Contamination =====\n\n% ===== Statistics =====\n\n@book{cohen1988statistical,\n  title = {{Statistical Power Analysis for the Behavioral Sciences}},\n  author = {Cohen, Jacob},\n  edition = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year = {1988},\n}\n\n% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2026},\n  eprint = {2509.18880},\n  archiveprefix = {arXiv},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{intrinsic_dim_detection,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n@inproceedings{schaeffer_collapse_position,\n  title = {{Position: Model Collapse Does Not Mean What You Think}},\n  author = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2025},\n  eprint = {2503.03150},\n  archiveprefix = {arXiv},\n}\n\n@inproceedings{drayson_detection_prevents_collapse,\n  title = {{Machine-Generated Text Detection Prevents Language Model Collapse}},\n  author = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  eprint = {2502.15654},\n  archiveprefix = {arXiv},\n}\n\n@inproceedings{seddik_synthetic_data,\n  title = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  author = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n% ===== Fine-tuning =====\n\n@inproceedings{qlora,\n  title = {{QLoRA: Efficient Finetuning of Quantized LLMs}},\n  author = {Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n% ===== Data Quality =====\n\n% ===== (orphan entries removed: fineweb, dolma) =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Jan Hendrik},\n  year = {2022},\n  note = {Blog post},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {3},\n  pages = {538--556},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  volume = {60},\n  number = {1},\n  pages = {9--26},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n@article{briesch_self_consuming,\n  title = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  author = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal = {arXiv preprint arXiv:2311.16822},\n  year = {2023},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n@inproceedings{attractor_cycles,\n  title = {{Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing}},\n  author = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n  eprint = {2502.15208},\n  archiveprefix = {arXiv},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{koike_mia_detection,\n  title = {{Machine Text Detectors are Membership Inference Attacks}},\n  author = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki},\n  journal = {arXiv preprint arXiv:2510.19492},\n  year = {2025},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n@inproceedings{ghostbuster,\n  title = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  author = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  booktitle = {Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{two_birds,\n  title = {{Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text}},\n  author = {Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan},\n  journal = {arXiv preprint arXiv:2508.14190},\n  year = {2025},\n}\n\n@inproceedings{beyond_final_actor,\n  title = {{Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection}},\n  author = {Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2026},\n}\n\n% ===== Machine Learning =====\n\n@article{gutierrez_ordinal_survey,\n  title = {{Ordinal Regression Methods: Survey and Experimental Study}},\n  author = {Guti{\\'e}rrez, Pedro Antonio and P{\\'e}rez-Ortiz, Mar{\\'i}a and S{\\'a}nchez-Monedero, Javier and Fern{\\'a}ndez-Navarro, Francisco and Herv{\\'a}s-Mart{\\'i}nez, C{\\'e}sar},\n  journal = {IEEE Transactions on Knowledge and Data Engineering},\n  volume = {28},\n  number = {1},\n  pages = {127--146},\n  year = {2016},\n}\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@article{corn_ordinal,\n  title = {{Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities}},\n  author = {Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian},\n  journal = {Pattern Analysis and Applications},\n  volume = {26},\n  pages = {941--955},\n  year = {2023},\n}\n\n@inproceedings{kasa_ordinality_nlp,\n  title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},\n  author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL},\n  year = {2024},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n\n@article{lakens_equivalence,\n  title = {{Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses}},\n  author = {Lakens, Dani{\\\"e}l},\n  journal = {Social Psychological and Personality Science},\n  volume = {8},\n  number = {4},\n  pages = {355--362},\n  year = {2017},\n}\n\n% ===== Generator Model References =====\n\n@article{llama3,\n  title = {{The Llama 3 Herd of Models}},\n  author = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year = {2024},\n}\n\n@article{mistral7b,\n  title = {{Mistral 7B}},\n  author = {Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others},\n  journal = {arXiv preprint arXiv:2310.06825},\n  year = {2023},\n}\n\n@article{strobl_conditional_2008,\n  title = {Conditional Variable Importance for Random Forests},\n  author = {Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim},\n  journal = {BMC Bioinformatics},\n  volume = {9},\n  pages = {307},\n  year = {2008},\n}\n\n% --- Entries from Paper Agent (docs/paper) ---\n\n@inproceedings{dolma,\n  title = {{Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research}},\n  author = {Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n\n@inproceedings{fineweb,\n  title = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  author = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year = {2024},\n}\n\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n\n\n@inproceedings{raid,\n  title = {{RAID}: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors},\n  author = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2024},\n  address = {Bangkok, Thailand},\n  publisher = {Association for Computational Linguistics},\n  pages = {12463--12492},\n}\n\n% ===== Distribution Quality =====\n\n@inproceedings{mauve,\n  title = {{MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers}},\n  author = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2021},\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 456,
        "oldLines": 6,
        "newStart": 456,
        "newLines": 13,
        "lines": [
          "   year = {2023},",
          " }",
          " ",
          "+@inproceedings{diaz_soft_labels_ordinal,",
          "+  title = {{Soft Labels for Ordinal Regression}},",
          "+  author = {Diaz, Raul and Marathe, Amit},",
          "+  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},",
          "+  year = {2019},",
          "+}",
          "+",
          " @inproceedings{kasa_ordinality_nlp,",
          "   title = {{Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques}},",
          "   author = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa},"
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

_source line 112_

<details open><summary>🔧 Tool call — Edit · `toolu_01CBDp4pZrfhVd2T4qMRV8Ch`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
  "old_string": "Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task",
  "new_string": "Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,diaz_soft_labels_ordinal,coral_ordinal,kasa_ordinality_nlp} as a task"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b7df07ae-b616-45d0-ad38-c7858e5079b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ep9yh2rsiPmoNjTZEc8EnV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5235,
      "cache_read_input_tokens": 70445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5235
      },
      "output_tokens": 69,
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

_source line 113 · 2026-05-21T08:44:33.339Z_

<details><summary>↩ Tool result · `toolu_01CBDp4pZrfhVd2T4qMRV8Ch`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "d75b2739-8d1d-4a47-8c49-0fe4d3a3b2a1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/related_work.tex",
    "oldString": "Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task",
    "newString": "Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,diaz_soft_labels_ordinal,coral_ordinal,kasa_ordinality_nlp} as a task",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{AI-Generated Text Detection}\n\\label{sec:related-detection}\n\nThe detection literature spans statistical tests \\cite{gltr,grover,release_strategies}, zero-shot scoring \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \\cite{diveye}, geometric invariants \\cite{intrinsic_dim_detection}, and learned classifiers \\cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \\citet{wu_survey_2025} and \\citet{jawahar_survey} for surveys.\nRAID \\cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.\nSeveral recent efforts move beyond the binary boundary---collaboration roles \\cite{beyond_binary}, joint detection-attribution \\cite{two_birds}, creator-editor modes \\cite{beyond_final_actor}, multi-generator attribution \\cite{semeval2024_task8}---but all taxonomize by \\emph{source} or \\emph{production mode}, not recursive generation \\emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\\,=\\,0.52--0.71; Table~\\ref{tab:baselines}) \\cite{paraphrase_evades,detection_possibilities}.\nOur contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \\cite{uchendu_attribution,munir_looking_glass}.\n\n\\subsection{Model Collapse and Iterative Generation}\n\\label{sec:related-collapse}\n\nSelf-consuming generative models progressively lose distributional coverage \\cite{self_consuming_mad,curse_of_recursion,briesch_self_consuming,seddik_synthetic_data}, though data mixing mitigates collapse \\cite{model_collapse_avoidable,strong_model_collapse}.\nThese studies address \\emph{training-loop} degradation where parameter updates erode tail coverage; indeed, \\citet{schaeffer_collapse_position} identify eight distinct definitions of ``collapse,'' most tied to retraining dynamics.\nWe study \\emph{inference chains} where parameters are fixed and only the input distribution evolves.\nTwo concurrent works are most directly relevant: \\citet{broken_telephone} analyze paraphrasing and translation chains, documenting progressive information loss, while \\citet{markovian_chains} demonstrate attractor dynamics that bound distinguishable depth to approximately three classes; \\citet{attractor_cycles} provide complementary evidence that LLM outputs converge to cyclic attractor states under repeated generation.\nWe study \\emph{non-paraphrastic continuation} chains, where the absence of semantic anchoring permits richer depth signal, and offer a complementary decomposition: where these works characterize \\emph{that} and \\emph{why} convergence occurs, DDR isolates \\emph{what} converges (NLL location) from what is preserved (NLL shape), enabling ordinal classification without per-generator calibration.\nThe independent convergence of all three approaches on ${\\sim}$3 distinguishable depth classes---via Markovian dynamics \\cite{markovian_chains}, information-theoretic loss \\cite{broken_telephone}, and distributional feature compression (this work)---points to a shared resolution ceiling in recursive text generation (Table~\\ref{tab:iterative-comparison} in Appendix~\\ref{app:iterative-comparison} provides a structured comparison).\n\n\\subsection{Vocabulary Diversity and Stylometry}\n\\label{sec:related-diversity}\n\nDeclining lexical diversity in LLM text is documented in both training \\cite{curious_decline} and deployment settings \\cite{writing_diversity}; MAUVE \\cite{mauve} provides a divergence-based metric for quantifying this distributional gap.\nOur surface features (TTR, hapax ratio) are classical stylometric measures \\cite{stamatatos_survey,koppel_authorship}; we repurpose them from generator identity \\cite{uchendu_attribution} to the depth dimension, where their monotonic decline under top-$p$ sampling \\cite{nucleus_sampling} constitutes a drifting component of DDR.\n\n\\subsection{Data Quality and Provenance}\n\\label{sec:related-provenance}\n\nScalable data curation relies on quality signals \\cite{dsir,qurating,ccnet}; generation depth offers a complementary provenance axis.\nProactive watermarking \\cite{watermark_llm,synthid_text,aaronson_watermark} embeds identifiable patterns but degrades across multi-step chains \\cite{chainwash}, motivating passive approaches.\nOur NLL-based analysis connects to \\citet{min_k_percent} (probability-tail membership inference) but extends from binary membership to full distributional decomposition for ordinal depth.\n\\citet{koike_mia_detection} formalize this connection from the opposite direction, showing that detection scores implicitly perform membership inference, underscoring the shared statistical basis of detection and provenance.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " The detection literature spans statistical tests \\cite{gltr,grover,release_strategies}, zero-shot scoring \\cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, surprisal diversity \\cite{diveye}, geometric invariants \\cite{intrinsic_dim_detection}, and learned classifiers \\cite{ghostbuster,feat_aug_transformer,reliable_detection,ld_score}; see \\citet{wu_survey_2025} and \\citet{jawahar_survey} for surveys.",
          " RAID \\cite{raid} benchmarks binary detection across generators and attacks; we extend the task from binary to ordinal depth estimation.",
          " Several recent efforts move beyond the binary boundary---collaboration roles \\cite{beyond_binary}, joint detection-attribution \\cite{two_birds}, creator-editor modes \\cite{beyond_final_actor}, multi-generator attribution \\cite{semeval2024_task8}---but all taxonomize by \\emph{source} or \\emph{production mode}, not recursive generation \\emph{depth}; repurposing their scores as depth predictors reveals high cross-generator variance (binary F1\\,=\\,0.52--0.71; Table~\\ref{tab:baselines}) \\cite{paraphrase_evades,detection_possibilities}.",
          "-Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \\cite{uchendu_attribution,munir_looking_glass}.",
          "+Our contribution is orthogonal: ordinal depth classification \\cite{gutierrez_ordinal_survey,diaz_soft_labels_ordinal,coral_ordinal,kasa_ordinality_nlp} as a task, and the finding that combining drifting and stationary features yields consistent cross-generator performance where individual detection scores show high variance \\cite{uchendu_attribution,munir_looking_glass}.",
          " ",
          " \\subsection{Model Collapse and Iterative Generation}",
          " \\label{sec:related-collapse}"
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

_source line 114_

Now let me copy the modified files to artifacts and compile to check float positions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "1a12bd96-9be2-4041-a3de-82f4ef98cb1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KyPXwRVvApbDonwHmdnyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 75680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 115_

<details open><summary>🔧 Tool call — Bash · `toolu_013Hxp1KkJdYnDRbqb5kwcCz`</summary>

```json
{
  "command": "cp docs/paper/references.bib artifacts/_project/paper/ && cp docs/paper/related_work.tex artifacts/_project/paper/",
  "description": "Copy modified files to artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "da91a8b8-bc83-46f7-a228-e46282c9b6aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KyPXwRVvApbDonwHmdnyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 75680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 116 · 2026-05-21T08:44:37.618Z_

<details><summary>↩ Tool result · `toolu_013Hxp1KkJdYnDRbqb5kwcCz`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "43e1d7d4-7ffb-45b6-89d3-ede7b79524db",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01QS1BSgBf1NwCszqZkkKKx3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "5a979113-e9b5-435e-ad81-eec64b1049d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UytRejkXVs2iTeUHWSz6Bp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 139,
      "cache_read_input_tokens": 75971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 139
      },
      "output_tokens": 68,
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

_source line 118 · 2026-05-21T08:44:42.559Z_

<details><summary>↩ Tool result · `toolu_01QS1BSgBf1NwCszqZkkKKx3`</summary>

```text
pdfTeX warning (dest): name{table.caption.129} has been referenced but does not
 exist, replaced by a fixed one

&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/cou
rier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (36 pages, 2625625 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "1082ab6c-80b9-49be-91e5-38b1da4681b1",
  "tool_use_result": {
    "stdout": "pdfTeX warning (dest): name{table.caption.129} has been referenced but does not\n exist, replaced by a fixed one\n\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cmextra/cmmib9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/cou\nrier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (36 pages, 2625625 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — Bash · `toolu_018mpN84SNbZAfoJuafTCqAZ`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -20",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a689dd3e-76bf-4106-a1e3-6bb0fd50a6a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNq2dPvxkTjGrSZGVZf2au",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 76110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1132
      },
      "output_tokens": 66,
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

_source line 120 · 2026-05-21T08:44:46.981Z_

<details><summary>↩ Tool result · `toolu_018mpN84SNbZAfoJuafTCqAZ`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "856c482e-2e92-4a41-b00c-03de742baf6f",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Bash · `toolu_01VwmBwdp4FJT4YLkGDHYrqz`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Two more pdflatex passes for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "0974ed88-dc27-4f8d-a685-9855efb3c09c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7x2ajaGVr5gGByKUWcnwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 77242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 154
      },
      "output_tokens": 70,
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

_source line 122 · 2026-05-21T08:44:53.390Z_

<details><summary>↩ Tool result · `toolu_01VwmBwdp4FJT4YLkGDHYrqz`</summary>

```text
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on main.pdf (36 pages, 2625454 bytes).
Transcript written on main.log.
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on main.pdf (36 pages, 2625310 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "d20c06dc-6114-40a7-884b-6d0097a5f93d",
  "tool_use_result": {
    "stdout": "mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on main.pdf (36 pages, 2625454 bytes).\nTranscript written on main.log.\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on main.pdf (36 pages, 2625310 bytes).\nTranscript written on main.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 123_

<details><summary>Logged reasoning block</summary>

```text
Good, compiled successfully with 36 pages. Now let me check the PDF to see what's on the first 3 pages, particularly display items. Let me check for warnings about undefined references or float placement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "95139675-cc33-4890-81df-6cfd5cffed3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufgRFRHawyZSzQvaw2i7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 77396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 10,
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

_source line 124_

Compiled successfully. Let me check the PDF layout to verify float positions on the first pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "75312da4-1aab-4c35-84c9-73ff56e7d8d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufgRFRHawyZSzQvaw2i7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 77396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 10,
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

_source line 125_

<details open><summary>🔧 Tool call — Bash · `toolu_011bfnvVFAko5dkfd7B11jGo`</summary>

```json
{
  "command": "grep -n \"Warning.*Float\" main.log | head -10; echo \"---\"; grep -n \"tab:features\\|tab:logo-results\\|fig:ddr-trajectory\\|fig:feature-drift\\|fig:baseline-ci\" main.log | head -20",
  "description": "Check float placement warnings in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "2b12bc2c-2654-4aca-bccd-8f2a19095e69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufgRFRHawyZSzQvaw2i7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 77396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 10,
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

_source line 126 · 2026-05-21T08:45:00.025Z_

<details><summary>↩ Tool result · `toolu_011bfnvVFAko5dkfd7B11jGo`</summary>

```text
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b99ef560-7a8b-4274-a35d-fbc855e6eb04",
  "tool_use_result": {
    "stdout": "---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Read · `toolu_01Hyd86HRnKYVgEDtuKwusXB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "bff490cb-533b-4c30-a456-e438dc428f1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DufgRFRHawyZSzQvaw2i7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 77396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
      },
      "output_tokens": 10,
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

_source line 128 · 2026-05-21T08:45:00.774Z_

<details><summary>↩ Tool result · `toolu_01Hyd86HRnKYVgEDtuKwusXB`</summary>

```text
PDF pages extracted: 3 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf (2.5MB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "8accf82a-5cb6-40ae-81d3-1e6ea13a65f0",
  "tool_use_result": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
      "originalSize": 2625310,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/pdf-d5497e92-eb3a-4af2-8c3e-10afdc2ff614",
      "count": 3
    }
  }
}
```

</details>

---

## Round 2

1 recorded events

### User

_source line 129 · 2026-05-21T08:45:00.772Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e3d65d2f-c5fb-4aa2-bc9b-000000000000",
  "isSynthetic": true
}
```

</details>

---

## Round 3

1 recorded events

### User

_source line 130 · 2026-05-21T08:45:00.772Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e3d65d2f-c5fb-4aa2-bc9b-000000000001",
  "isSynthetic": true
}
```

</details>

---

## Round 4

18 recorded events

### User

_source line 131 · 2026-05-21T08:45:00.772Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "e3d65d2f-c5fb-4aa2-bc9b-000000000002",
  "isSynthetic": true
}
```

</details>

---

### Assistant

_source line 132_

<details><summary>Logged reasoning block</summary>

```text
I can see the PDF pages. Let me analyze:

**Page 1**: Abstract + start of Introduction. No display items (tables/figures).
**Page 2**: End of Introduction + Related Work (sections 2.1, 2.2). No display items.
**Page 3**: End of Related Work (2.3, 2.4) + Method (3.1, 3.2, 3.3). No display items yet.

So the first 3 pages have NO display items at all. The features table and other figures must appear on page 4 or later. This confirms the task's concern about 2g.


The citations look good now—Diaz and Marathe appear correctly as "Diaz and Marathe, 2019" and Seddik shows as "Seddik et al., 2024". For task 2g, I need to get a display item onto the first three pages. The features table is positioned with `[t]` placement in section 3.3, which starts on page 3, so it should float to the top of page 4 unless I adjust its placement.

I could move the table definition earlier in method.tex before section 3.2, change the float specifiers to force earlier placement, or move a different display item instead. Looking at the line numbers, section 3.1 starts around line 224, section 3.2 around line 234, and section 3.3 around line 272 where the table is defined, so it'll naturally appear where that section begins. I could also try using `[!t]` or `[!ht]` to be more aggressive about placement, but I'm concerned about moving the table before §3.1 since it references content from that section—it would feel out of order. Let me stick with modifying method.tex since that's allowed, and see if a more forceful placement option helps. Looking at the PDF layout more carefully, I see the table is currently in the right column of page 3, and with the `[t]` placement it would float to page 4. To keep it on page 3, I'd need to move the table definition much earlier—probably to the introduction or related work sections. Since I can modify those files, I have some flexibility here to reposition the table and get it to stay on the current page.

The cleanest approach is to place the table definition at the very beginning of the method section with a `[!t]` specifier to force it to the top of page 3, which respects the paper's structure while controlling the float placement more precisely. or page 3. The cleanest fix is to define the table early in the related_work.tex file with top placement, which would position it at the top of page 2 where Related Work begins. Alternatively, I could move the table to appear right after the Method section heading, though that would likely push it to page 4 instead. The real constraint is that pages 1-3 are already packed with text, so getting a display item on those pages requires either moving a float definition into the Introduction or Related Work source, or trimming content elsewhere to shift the layout. I'm realizing the core issue: pages 1-3 are already densely packed with text, so adding a table means I need to push content to page 4. If I place the table at the start of method.tex with `[!t]`, LaTeX should position it at the top of page 4 since page 3's top is already occupied by Related Work. Let me just implement this approach and see how it renders.

Actually, looking back at the task more carefully—it's asking me to get Table 1 (the LOGO results table in results.tex) onto page 2, which would require moving it to introduction.tex or related_work.tex. That feels thematically wrong. The second option suggests adding a forward reference in the intro to influence LaTeX's placement, though I'm not sure how effective that would be.

Let me think about this differently: maybe I should just move one of the existing tables or figures from method.tex to an earlier section, or accept that the first three pages are text-heavy and report that finding instead. I'm considering whether to use the two-column table format instead, though that might disrupt the layout. The more practical approach seems to be moving the table definition to the beginning of the Method section so LaTeX places it at the top of page 4, but I'm realizing this might not actually change its position since it's already on that page in the current structure. I'll compile and check if this placement works. If the table still ends up on page 4, then I'll need to report that achieving the desired page placement requires more substantial restructuring beyond just adjusting float specifiers.

Actually, moving the features table to the beginning of the method section might help—shifting it earlier in the source could push it onto page 2. I could try placing it right after the method section header, or even at the end of the related work section if needed. Let me test moving the table to the start of method.tex first and see how much space that recovers. I'm realizing the table placement strategy — putting it at the end of introduction.tex means it'll be the first float processed and land at the top of page 2, which actually works well since it gives readers an early overview of the features. The forward reference to §4.2 is acceptable in this context. Since introduction.tex is fair game to modify, I'll move the table there and remove it from the Feature Extraction subsection.

But I'm second-guessing whether the features table is the right choice — maybe I should put the DDR strip plot figure instead, since the introduction already discusses DDR and the location/shape asymmetry. Let me check what Figure 1 actually contains in the results section.

Looking at the figure definition, it's a single-column DDR strip plot that's central to the paper's conceptual story. Moving it to the introduction would work well since many papers place their key conceptual figure there. The reference in results.tex would still point backward correctly, which is fine. I need to think through whether the introduction text would support this placement though. I'm realizing the introduction is quite short at just 22 lines, and line 10 has the perfect spot to reference the figure right after the DDR definition. But I should be cautious about moving figures around since the director has already made edits—that could create conflicts. Instead, I'll focus on adjusting the float specifiers and keeping the structural changes minimal.

Actually, looking at the task again, it's giving me two concrete options: either change Table 1's positioning to page 2, or insert a figure reference at the end of the introduction before the related work section. For the second option, I should move the feature-drift figure from results.tex to the end of introduction.tex and add a brief reference in the intro text itself. This way the figure lands on page 2 as intended, and I can keep the textual reference in results.tex as well.

But wait—there are actually two DDR-related figures in results.tex: the full-width trajectory plot (a figure* environment) and the strip plot (a regular figure environment). Since figure* floats behave differently in two-column layout, I need to check which one actually becomes Figure 1 in the compiled PDF based on source order.

Looking at the practical solution: I could move the strip plot figure to the end of introduction.tex and reference it there, which would place the DDR overview on page 2. I need to be careful about which files I'm allowed to modify—introduction.tex should be fine, but I should avoid touching abstract.tex, discussion.tex, and conclusion.tex.

Let me think through the edits I need to make: I'll add a reference to the figure in introduction.tex at the appropriate spot in the DDR description, then move the figure environment itself to the end of that file. Actually, placing the figure at the end of introduction.tex with the `[t]` placement option should work fine—it'll float to the top of page 2, right where the introduction concludes. The caption needs some trimming though, so I'm condensing it to focus on the key findings about drifting versus non-drifting features and their depth sensitivity patterns.

For results.tex, I need to remove the figure environment entirely but keep the text reference to `Figure~\ref{fig:feature-drift}` since the label will still be valid from the moved figure. I should also check that the reference text mentioning the DDR trajectory aligns with what's now in the introduction.

Moving the feature-drift figure to the introduction actually improves the numbering: it becomes Figure 1 (DDR overview), the trajectory figure becomes Figure 2, and the baseline comparison becomes Figure 3—a cleaner progression than the current ordering. I'm realizing the figure numbering will shift based on how LaTeX places floats—`figure*` environments go to the next page while regular `figure` environments can stay on the current page, so the source order might not match the output order. After moving the feature-drift figure to the introduction, it should become Figure 1, with the ddr-trajectory and baseline-ci figures shifting to Figure 2 and 3 respectively. Since the references use `\ref{}` commands, they'll update automatically. Now I need to make the actual edits: move the figure to the end of introduction.tex, remove it from results.tex lines 67-72, and add a reference to it in the introduction text.

But I should verify the text flow in results.tex after removing those lines—checking if the paragraph starting at line 60 still connects properly to line 74 when the figure is gone.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "18fa471c-acbc-48b6-b057-f39f71b5edfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2NpoRhyzoH4P3MXoHTC5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 77900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 133_

Pages 1-3 have no display items — all text. I'll move the DDR overview figure (fig:feature-drift) to the introduction to get a figure on page 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "226a6666-8f7b-4f00-bcbc-07499bb3a21e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2NpoRhyzoH4P3MXoHTC5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 77900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 134_

<details open><summary>🔧 Tool call — Edit · `toolu_01KGesRKWpbEaf3w3EBAxdAo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "We term this location/shape asymmetry the \\emph{differential depth response} (DDR)---a structural property",
  "new_string": "We term this location/shape asymmetry the \\emph{differential depth response} (DDR; Figure~\\ref{fig:feature-drift})---a structural property"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "63d6b59c-dae1-44f0-99f2-a569dc04a981",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2NpoRhyzoH4P3MXoHTC5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 77900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 135 · 2026-05-21T08:47:37.904Z_

<details><summary>↩ Tool result · `toolu_01KGesRKWpbEaf3w3EBAxdAo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "3987148a-a0b4-4277-9921-87bf7007d647",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "oldString": "We term this location/shape asymmetry the \\emph{differential depth response} (DDR)---a structural property",
    "newString": "We term this location/shape asymmetry the \\emph{differential depth response} (DDR; Figure~\\ref{fig:feature-drift})---a structural property",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nAI text detection asks a single binary question---\\emph{human or machine?}---and recent methods answer it with increasing reliability \\cite{detectgpt,fast_detectgpt,binoculars,ld_score}.\nYet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \\cite{dolma,fineweb} and seed further generation, text accumulates at varying \\emph{recursive depths}---an estimated 7--17\\% of recent scientific publications already contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.\nWhile most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.\nKnowing \\emph{how many times} text has been recursively generated matters for data provenance \\cite{ccnet,dsir} and model collapse analysis \\cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.\n\nDistributional compression under recursive generation is well-documented \\cite{curious_decline,broken_telephone,markovian_chains}.\nWe introduce \\emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\\,/\\,gen-1\\,/\\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).\nWe term this location/shape asymmetry the \\emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \\cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.\nWhere concurrent work characterizes \\emph{that} and \\emph{why} convergence occurs \\cite{broken_telephone,markovian_chains}, DDR isolates \\emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.\n\nAs a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\\,=\\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\\,=\\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \\emph{what converges}---diversity loss \\cite{curious_decline}, attractor dynamics \\cite{markovian_chains}---DDR identifies \\emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.\n    \\item \\textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.\n\\end{enumerate}\nA proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " Distributional compression under recursive generation is well-documented \\cite{curious_decline,broken_telephone,markovian_chains}.",
          " We introduce \\emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\\,/\\,gen-1\\,/\\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).",
          "-We term this location/shape asymmetry the \\emph{differential depth response} (DDR)---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \\cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.",
          "+We term this location/shape asymmetry the \\emph{differential depth response} (DDR; Figure~\\ref{fig:feature-drift})---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \\cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.",
          " Where concurrent work characterizes \\emph{that} and \\emph{why} convergence occurs \\cite{broken_telephone,markovian_chains}, DDR isolates \\emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.",
          " ",
          " As a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\\,=\\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features."
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

_source line 136_

<details open><summary>🔧 Tool call — Edit · `toolu_017agNDGmNdBH7rJy3w9ChYM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.",
  "new_string": "A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "6b497773-ca53-4d2c-881b-1d9b7946493f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2NpoRhyzoH4P3MXoHTC5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 77900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 137 · 2026-05-21T08:47:42.140Z_

<details><summary>↩ Tool result · `toolu_017agNDGmNdBH7rJy3w9ChYM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "716a7c40-536d-42b2-8cc7-ee87db78bfce",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "oldString": "A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.",
    "newString": "A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nAI text detection asks a single binary question---\\emph{human or machine?}---and recent methods answer it with increasing reliability \\cite{detectgpt,fast_detectgpt,binoculars,ld_score}.\nYet this framing elides a richer structure emerging on the open web: as LLM outputs re-enter training corpora \\cite{dolma,fineweb} and seed further generation, text accumulates at varying \\emph{recursive depths}---an estimated 7--17\\% of recent scientific publications already contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}---and each generation cycle pushes distributional properties further from both the human source and the first-generation predecessor.\nWhile most deployed LLM outputs use instruction-tuned models, base-model generation pipelines remain prevalent in synthetic data production, pre-training corpus construction, and recursive data augmentation; we accordingly scope this study to base (pretrained) models.\nKnowing \\emph{how many times} text has been recursively generated matters for data provenance \\cite{ccnet,dsir} and model collapse analysis \\cite{curse_of_recursion,strong_model_collapse}, yet no current method moves beyond the binary boundary.\n\nDistributional compression under recursive generation is well-documented \\cite{curious_decline,broken_telephone,markovian_chains}.\nWe introduce \\emph{depth fingerprinting}---classifying text by ordinal generation depth (gen-0\\,/\\,gen-1\\,/\\,gen-2+)---and decompose this compression into structurally distinct components: across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency (mean entropy, lexical diversity) drifts monotonically with depth while its shape (entropy extremes, tail structure) remains an order of magnitude more stable ($d{=}0.76$--$1.17$ vs.\\ $d < 0.10$; convergence across parametric and non-parametric effect-size measures confirms this partition).\nWe term this location/shape asymmetry the \\emph{differential depth response} (DDR; Figure~\\ref{fig:feature-drift})---a structural property of fixed-parameter autoregressive sampling that is mechanistically distinct from the tail-coverage erosion in model collapse \\cite{curse_of_recursion} and analytically informative independent of both the specific mechanism and classification accuracy.\nWhere concurrent work characterizes \\emph{that} and \\emph{why} convergence occurs \\cite{broken_telephone,markovian_chains}, DDR isolates \\emph{what} converges from what is preserved, and leverages the stationary shape component for cross-generator depth prediction without per-generator calibration.\n\nAs a proof of concept, a lightweight 7-feature ensemble informed by DDR achieves leak-free binary F1\\,=\\,0.694 under leave-one-generator-out evaluation, matching multi-detector ensembles at $2.4\\times$ lower cost; an end-to-end QLoRA classifier reaches 0.905 (6-gen LOGO; Appendix~\\ref{app:qlora}), confirming that the depth signal extends well beyond handcrafted features.\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Empirical decomposition (DDR).} Clustering-based validation ($k{=}2$, silhouette\\,=\\,0.660) confirms that inference-chain drift separates into a drifting location component ($d{=}0.76$--$1.17$) and a stable shape component ($d < 0.10$). Where prior work documents \\emph{what converges}---diversity loss \\cite{curious_decline}, attractor dynamics \\cite{markovian_chains}---DDR identifies \\emph{what is preserved}: shape invariance provides the cross-generator reference needed for depth detection without per-generator calibration.\n    \\item \\textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.\n\\end{enumerate}\nA proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 3,
        "newStart": 19,
        "newLines": 10,
        "lines": [
          "     \\item \\textbf{Task formulation and evaluation suite.} We define generation depth classification as an ordinal prediction task and construct a controlled dataset of 37K texts from eight generators across five families (0.6B--8B), with leave-one-generator-out cross-validation as the primary evaluation protocol.",
          " \\end{enumerate}",
          " A proof-of-concept classifier and systematic boundary mapping across temperature, prompt type, instruction tuning, and model scale establish where DDR-based detection succeeds and where it fails.",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}",
          "+\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}",
          "+\\label{fig:feature-drift}",
          "+\\end{figure}"
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

_source line 138_

<details open><summary>🔧 Tool call — Edit · `toolu_01SphjVjmk8PGmQdUzmbUB7u`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nPooled",
  "new_string": "Pooled"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "21b3a6bd-dc5f-4623-9f85-3ca179051209",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsgppvSrLWNq9FKaPPB1fc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8466,
      "cache_read_input_tokens": 82116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8466
      },
      "output_tokens": 69,
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

_source line 139 · 2026-05-21T08:47:48.197Z_

<details><summary>↩ Tool result · `toolu_01SphjVjmk8PGmQdUzmbUB7u`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "4bd58c80-7c59-4908-8252-bfe6f3dab9ef",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "oldString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nPooled",
    "newString": "Pooled",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nThe 7-feature ensemble achieves 3-class LOGO F1\\,=\\,0.762 (95\\% CI [0.758, 0.766]; $N$\\,=\\,37{,}058) across eight generators from five families (Table~\\ref{tab:logo-results}), with cross-generator F1 spread of 9.1\\,pp capturing generator selection uncertainty.\nBecause gen-0 seeds are shared across generators (\\S\\ref{sec:generation}), gen-0 classification is near-perfect (per-class F1\\,$\\approx$\\,0.94), inflating the 3-class metric.\nWe therefore adopt \\textbf{leak-free binary F1} (gen-1 vs.\\ gen-2+)\\,=\\,0.694 (CI [0.688, 0.700]) as the primary metric throughout: it excludes gen-0 entirely and is unaffected by seed sharing.\nPer-generator binary F1 ranges from 0.633 (Mistral-7B) to 0.724 (Pythia-2.8B; SD\\,=\\,0.028), with the primary difficulty concentrated at the gen-1\\,/\\,gen-2+ boundary (Appendix~\\ref{app:confusion}).\nNote that CIs above reflect bootstrap sampling variability; the cross-generator range (9.1\\,pp) captures the distinct and larger uncertainty of generator selection.\n\n\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield binary F1\\,=\\,0.830 (95\\% CI [.818, .841]) under 5-generator LOGO.\\footnote{5-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-0.6B/1.7B); generator-level LOGO with bootstrap CIs ($n$\\,=\\,2{,}000). Not directly comparable to 8-generator LOGO due to differing subsets.}\nSingle-generator transfer (Appendix~\\ref{app:transfer}) confirms the signal is not a mixed-chain artifact: classifiers trained on one generator transfer to all others with mean binary F1\\,=\\,0.810; LOFO yields 0.686.\nA scale effect emerges: Pythia achieves the highest F1 (0.718--0.724) while larger models degrade (Mistral-7B: 0.633), partly reflecting same-family affinity with the Pythia-410M reference (cross-reference spread $\\leq$0.013; \\S\\ref{sec:results-differential}); cross-domain signal persists with variation (Appendix~\\ref{app:domain}).\nAn end-to-end QLoRA classifier achieves 3-class F1\\,=\\,0.905 under 6-generator LOGO ($+$11.6\\,pp vs.\\ the same-subset XGBoost baseline of 0.789; Appendix~\\ref{app:qlora}), confirming that richer token-level representations capture additional depth signal; on instruct data, QLoRA recovers to 0.89--0.91 within-model (Appendix~\\ref{app:instruct}), establishing the empirical decomposition---not the specific classifier---as DDR's primary contribution.\n\n\\paragraph{Length confound control.}\nLength-matched subsampling yields binary F1\\,=\\,0.724 (vs.\\ 0.770 unmatched); a random-subsample control confirms the drop reflects deconfounding, not sample-size reduction (Appendix~\\ref{app:length}).\n\n\\paragraph{Seed-sharing control.}\nSeed-level demeaning (F1\\,=\\,0.701) and an independent-seed experiment with disjoint seed pools (F1\\,=\\,0.680; Appendix~\\ref{app:seed-control}) both confirm the classifier captures generative degradation, not seed-specific content.\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{Params} & \\textbf{Bin F1} & \\textbf{95\\% CI} & \\textbf{3-cl F1}$^{\\dagger}$ \\\\\n\\midrule\nPythia-2.8B     & Pythia  & 2.8B & \\textbf{0.724} & [.707, .742] & 0.798 \\\\\nPythia-1B       & Pythia  & 1.0B & 0.718 & [.700, .735] & \\textbf{0.806} \\\\\nQwen3-1.7B     & Qwen    & 1.7B & 0.709 & [.693, .726] & 0.772 \\\\\nLlama-3.2-3B   & Llama   & 3.2B & 0.697 & [.680, .713] & 0.775 \\\\\nOLMo-2-1B      & OLMo    & 1.5B & 0.695 & [.679, .711] & 0.781 \\\\\nQwen3-8B       & Qwen    & 8.2B & 0.692 & [.674, .708] & 0.714 \\\\\nQwen3-0.6B     & Qwen    & 0.6B & 0.691 & [.673, .709] & 0.780 \\\\\nMistral-7B     & Mistral & 7.0B & 0.633 & [.617, .648] & 0.682 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textbf{Average (8-gen LOGO)}} & \\textbf{0.694} & [.688, .700] & \\textbf{0.762} \\\\\n\\multicolumn{3}{l}{\\textbf{LOFO (family-level)}} & 0.686 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{8-generator LOGO macro-F1 for the 7-feature ensemble (bootstrap 95\\% CIs, $n$\\,=\\,1000). Binary F1 (gen-1 vs.\\ gen-2+) is the primary metric; it excludes gen-0 entirely and is unaffected by seed sharing. Cross-generator binary F1: SD\\,=\\,0.028, IQR\\,=\\,[0.692, 0.714]. $^{\\dagger}$3-class F1 carries upward bias because gen-0 seeds are shared across generators (\\S\\ref{sec:generation}); independent-seed controls confirm the depth signal (F1\\,=\\,0.680; Appendix~\\ref{app:seed-control}).}\n\\label{tab:logo-results}\n\\end{table}\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_ddr_trajectory.pdf}\n\\caption{Feature trajectories across generation depth. \\textbf{Top row (drifting)}: entropy mean and hapax ratio decline monotonically across all eight generators ($|\\rho| > 0.59$). \\textbf{Bottom row (stationary)}: entropy max and tail decay remain flat ($|\\rho| < 0.07$). Colored lines: individual generators; diamonds: cross-generator mean (blue for drifting, amber for stationary). This dichotomy defines the differential depth response (DDR).}\n\\label{fig:ddr-trajectory}\n\\end{figure*}\n\nNot all distributional properties respond equally to recursive generation.\nFigure~\\ref{fig:ddr-trajectory} reveals a striking dichotomy that holds across all eight generators: central-tendency features (entropy mean, TTR, hapax ratio) decline monotonically with depth, while shape features (entropy max, tail decay, entropy min) remain flat.\nWe term this asymmetry the \\emph{differential depth response} (DDR).\nThe primary partition is binary: $k{=}2$ clustering in standardized $(|\\rho|, d)$ space yields silhouette\\,=\\,0.660 (Appendix~\\ref{app:ddr-validation}), cleanly separating three \\emph{drifting} features ($|\\rho| > 0.60$, $d{=}0.76$--$1.17$) from four \\emph{non-drifting} ones ($d \\leq 0.55$); higher $k$ degrades cluster quality ($k{=}3$: silhouette\\,=\\,0.532).\nA domain-informed refinement resolves entropy std as a sole \\emph{intermediate} member ($d{=}0.55$, $|\\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\\% vs.\\ $>$15\\% for drifting features).\nConvergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\\S\\ref{sec:results-differential}, Quantification).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nPooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\\ref{fig:feature-drift}):\ndrifting features show substantial monotonic trends (hapax ratio $\\rho = -0.64$, TTR $\\rho = -0.63$, entropy mean $\\rho = -0.60$),\nwhile non-drifting features remain near-zero (tail decay $|\\rho| = 0.04$; per-depth distributions in Appendix~\\ref{app:feature-distributions}).\nThe six-fold magnitude gap between drifting ($|\\rho| > 0.60$) and non-drifting features ($|\\rho| \\leq 0.16$) defines the DDR partition.\nWithin the non-drifting group, entropy std ($|\\rho| = 0.16$, $d{=}0.55$) shows a substantial level shift despite low monotonicity, distinguishing it from the three near-stationary features ($d < 0.10$); this refinement is stable across $d$ thresholds in $[0.56, 0.75]$ (Appendix~\\ref{app:ddr-validation}).\n\n\\paragraph{Quantification.}\nConvergence across parametric and non-parametric effect-size measures confirm the split.\nCohen's $d$ \\cite{cohen1988statistical} shows a ${\\geq}7\\times$ gap between drifting ($d{=}0.76$--$1.17$) and near-stationary features ($d \\leq 0.08$); KS statistics, Glass's $\\Delta$, Cliff's $\\delta$, and CV shift all corroborate (Appendix~\\ref{app:ddr-validation}).\nFour features fall cleanly into drifting or non-drifting groups.\nEntropy min and tail decay are \\emph{boundary features}: entropy min is near-stationary for gen-1 vs.\\ gen-2+ ($d{=}0.016$) but sensitive at gen-0/gen-1 ($|\\rho|{=}0.40$); tail decay is \\emph{weakly stationary}, passing TOST for only 4/8 generators ($|d|{=}0.10$--$0.22$).\nEntropy std ($d{=}0.55$, $|\\rho|{=}0.16$) is the sole intermediate member.\n\\paragraph{Validation.}\nThe drifting/non-drifting boundary is validated by convergent evidence: $k{=}2$ clustering in standardized $(|\\rho|, d)$ space yields a clean separation (silhouette\\,=\\,0.660), invariant across threshold choices $\\varepsilon \\in [0.10, 0.75]$; crucially, per-generator split analysis recovers the identical partition in all eight hold-out generators independently (per-generator silhouette range 0.505--0.760; Appendix~\\ref{app:ddr-validation}).\nPer-generator TOST equivalence testing ($\\varepsilon{=}|d|{<}0.20$, following Cohen's~\\citeyearpar{cohen1988statistical} conventional threshold; gen-1 vs.\\ gen-2+) confirms near-stationarity for entropy min (8/8 pass) and entropy max (6/8); tail decay passes for only 4/8, with $|d|{=}0.10$--$0.22$ spanning the boundary.\nA permutation test ($n{=}10{,}000$) confirms the three-vs-four split is non-random ($p{=}0.030$; fixed-label silhouette\\,=\\,0.660 vs.\\ null mean\\,=\\,0.46); exhaustive enumeration of all $\\binom{7}{3}{=}35$ possible splits ranks this partition first (Appendix~\\ref{app:ddr-validation}).\nReclassifying either boundary feature as intermediate preserves the core drifting/non-drifting split and leaves classification unchanged.\n\n\\paragraph{Feature complementarity.}\nThe full 7-feature set (F1\\,=\\,0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar $p \\approx 0$; Appendix~\\ref{app:ablation-table}).\nPCA confirms the three drifting features share a single latent dimension (92.3\\% variance; Appendix~\\ref{sec:appendix-feature-correlation}); replacing them with PC1 costs only 1.1\\,pp, confirming that DDR's contribution is identifying \\emph{which} distributional properties drift, not classification per se.\nTTR and hapax ratio ($r = 0.97$) are both retained for marginal LOFO gains despite feature masking \\cite{strobl_conditional_2008} (Appendix~\\ref{app:lofo}).\n\n\\paragraph{Cross-family reference models.}\nAlternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Appendix~\\ref{app:cross-ref}), bounding the same-family affinity effect; depth features are robust to reference model choice, though residual same-family proximity may inflate Pythia-family F1 by up to 1.3\\,pp.\n\n\\paragraph{Temperature and prompt-type sensitivity.}\nAll four tested generators degrade at $t{=}0.9$ ($-9.3$ to $-26.0$\\,pp binary F1); low-temperature improvement is family-dependent ($+7$--$9$\\,pp for Pythia/OLMo at $t{=}0.5$, negligible for Qwen; Appendix~\\ref{app:sampling-sensitivity}).\nContinuation chains show the strongest drift (F1\\,=\\,0.781), with cross-prompt-type transfer confirming shared signal (LOPTO F1\\,=\\,0.753; Appendix~\\ref{app:prompt-type}); the DDR partition hierarchy is preserved across temperatures despite absolute effect-size compression (Appendix~\\ref{app:ddr-temp-stability}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\nExisting detection methods target binary real-vs-synthetic classification; we test whether their continuous scores incidentally encode recursive depth by repurposing four detection scores as ordinal depth predictors under identical XGBoost and LOGO conditions (Table~\\ref{tab:baselines}).\n\n\\begin{table}[t]\n\\centering\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Feat.} & \\textbf{3-cl F1} & \\textbf{Bin F1} & \\textbf{ms/text} \\\\\n\\midrule\n4-det.\\ + surface     & 6 & \\textbf{0.795} & \\textbf{0.708} & 22.8 \\\\\n4-detector ens.\\      & 4 & 0.785 & 0.700 & 22.8 \\\\\n7-feature (ours)      & 7 & 0.774 & 0.705 & \\textbf{9.7} \\\\\n\\midrule\nAvg-LogProb           & 1 & 0.707 & 0.673 & --- \\\\\nFastDetectGPT         & 1 & 0.660 & 0.569 & --- \\\\\nLD-Score              & 1 & 0.630 & 0.675 & --- \\\\\nBinoculars            & 1 & 0.411 & 0.539 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth classification (8-gen LOGO, pooled evaluation; slightly higher than per-generator macro average in Table~\\ref{tab:logo-results}). Identical XGBoost configuration. 7-feature: one 410M model (905\\,MB); 4-det ensembles: two models, 1.4B params (2{,}868\\,MB). Individual detection scores (N/A) share the reference-model forward pass; per-method timing is not separately profiled.}\n\\label{tab:baselines}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.pdf}\n\\caption{LOGO binary F1 vs.\\ inference cost in ms/text (8-gen pooled). The 7-feature ensemble (one 410M reference model) matches multi-detector ensembles (two models, 1.4B total) at 2.4$\\times$ lower cost; individual detectors vary widely when repurposed for depth. Inference costs measured on a single NVIDIA RTX 5090.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nThe 7-feature ensemble surpasses all individual baselines in 3-class F1 ($\\Delta$\\,=\\,6.7--36.3\\,pp; Figure~\\ref{fig:baseline-ci}) and the pure 4-detector ensemble in binary F1 (0.705 vs.\\ 0.700).\nAdding DDR's surface features to the four detectors yields the highest binary F1 (0.708), marginally above the 7-feature set at 2.4$\\times$ the inference cost.\nThis result underscores that DDR's primary contribution is not classification performance---where multi-detector ensembles match or marginally exceed it---but the decomposition of depth signal into location-sensitive and shape-stable components, a structural distinction absent from both binary detection methods and model collapse analyses (\\S\\ref{sec:discussion}).\n",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 13,
        "newStart": 64,
        "newLines": 6,
        "lines": [
          " A domain-informed refinement resolves entropy std as a sole \\emph{intermediate} member ($d{=}0.55$, $|\\rho|{=}0.16$), distinct from the three near-stationary features ($d < 0.10$; CV shift $<$3\\% vs.\\ $>$15\\% for drifting features).",
          " Convergence across parametric and non-parametric effect-size measures confirms this partition, establishing that the location/shape asymmetry reflects distributional structure rather than feature-selection artifact (\\S\\ref{sec:results-differential}, Quantification).",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}",
          "-\\caption{Differential depth response (DDR). Diamonds: cross-generator means; dots: per-generator values. Drifting features (blue; $|\\rho| > 0.60$, $d{=}0.76$--$1.17$) show strong monotonic depth sensitivity; non-drifting features remain stable. Entropy std (wine; $d{=}0.55$) is an intermediate member; non-drifting features (amber; $d < 0.10$) show negligible drift. Entropy min ($|\\rho|{=}0.40$ pooled; gen-0/gen-1 sensitive) and tail decay (TOST 4/8) are boundary features within this group.}",
          "-\\label{fig:feature-drift}",
          "-\\end{figure}",
          "-",
          " Pooled class-balanced Spearman correlations with depth confirm the binary split (Figure~\\ref{fig:feature-drift}):",
          " drifting features show substantial monotonic trends (hapax ratio $\\rho = -0.64$, TTR $\\rho = -0.63$, entropy mean $\\rho = -0.60$),",
          " while non-drifting features remain near-zero (tail decay $|\\rho| = 0.04$; per-depth distributions in Appendix~\\ref{app:feature-distributions})."
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

_source line 140_

Now copy all modified files to artifacts and recompile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "dcdb171a-b278-4552-b12d-2ccc17c943aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EA547HGMnug2t1ZeYcxDVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 90582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

_source line 141_

<details open><summary>🔧 Tool call — Bash · `toolu_01QAM5JRAGnqG6GaUksjNKWi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint && cp docs/paper/introduction.tex docs/paper/results.tex docs/paper/references.bib docs/paper/related_work.tex artifacts/_project/paper/",
  "description": "Copy all modified files to artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "94df0ac7-ea05-46d9-bf18-156dae9a016f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EA547HGMnug2t1ZeYcxDVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 90582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

_source line 142 · 2026-05-21T08:47:59.953Z_

<details><summary>↩ Tool result · `toolu_01QAM5JRAGnqG6GaUksjNKWi`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "a59ab3f0-4427-4dcf-86ff-0cfe945d41e1",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 143_

<details open><summary>🔧 Tool call — Bash · `toolu_01TdjRfvxR5SuLbQkjgJKXXj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Output\" | tail -10 && bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep \"Output\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep \"Output\"",
  "description": "Full compile cycle",
  "timeout": 180000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c4243ad5-5845-4604-a516-85c0d6241b8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1NQGYNd7aMEux95AwKJyY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 91007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 172
      },
      "output_tokens": 60,
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

### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bm96vkk3l",
  "tool_use_id": "toolu_01TdjRfvxR5SuLbQkjgJKXXj",
  "description": "Full compile cycle",
  "task_type": "local_bash",
  "uuid": "ad524bf3-caba-47c2-96c9-aa813520cc43",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### System

_source line 145_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bm96vkk3l",
  "tool_use_id": "toolu_01TdjRfvxR5SuLbQkjgJKXXj",
  "status": "completed",
  "output_file": "",
  "summary": "Full compile cycle",
  "uuid": "8d65dd71-0807-4762-b5b6-98cf9832fafe",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994"
}
```

---

### Tool result

_source line 146 · 2026-05-21T08:48:09.939Z_

<details><summary>↩ Tool result · `toolu_01TdjRfvxR5SuLbQkjgJKXXj`</summary>

```text
LaTeX Warning: `!h' float specifier changed to `!ht'.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
Output written on main.pdf (36 pages, 2627237 bytes).
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Output written on main.pdf (36 pages, 2627074 bytes).
Output written on main.pdf (36 pages, 2627074 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "6d1e2bae-f1ef-4e82-8fe1-ffc44d0e7185",
  "tool_use_result": {
    "stdout": "LaTeX Warning: `!h' float specifier changed to `!ht'.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\nOutput written on main.pdf (36 pages, 2627237 bytes).\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nOutput written on main.pdf (36 pages, 2627074 bytes).\nOutput written on main.pdf (36 pages, 2627074 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Read · `toolu_016nZwqyUXZG79hniaP8WV9V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "aad12047-aef4-4f9d-a60d-da601d55414a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMkVeo5dr6YvzxhCPEApWa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 91179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
      },
      "output_tokens": 65,
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

_source line 148 · 2026-05-21T08:48:13.508Z_

<details><summary>↩ Tool result · `toolu_016nZwqyUXZG79hniaP8WV9V`</summary>

```text
PDF pages extracted: 4 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf (2.5MB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "30c82d3e-b7c9-4832-abc1-a933dc224d87",
  "tool_use_result": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
      "originalSize": 2627074,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/f0729576-0a0b-4639-9730-0c3f60cce994/tool-results/pdf-eeb0722c-5da7-46c0-9113-53caf9806724",
      "count": 4
    }
  }
}
```

</details>

---

## Round 5

1 recorded events

### User

_source line 149 · 2026-05-21T08:48:13.507Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b136ce45-35af-4a5f-9c66-000000000000",
  "isSynthetic": true
}
```

</details>

---

## Round 6

1 recorded events

### User

_source line 150 · 2026-05-21T08:48:13.507Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b136ce45-35af-4a5f-9c66-000000000001",
  "isSynthetic": true
}
```

</details>

---

## Round 7

1 recorded events

### User

_source line 151 · 2026-05-21T08:48:13.507Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b136ce45-35af-4a5f-9c66-000000000002",
  "isSynthetic": true
}
```

</details>

---

## Round 8

4 recorded events

### User

_source line 152 · 2026-05-21T08:48:13.507Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "b136ce45-35af-4a5f-9c66-000000000003",
  "isSynthetic": true
}
```

</details>

---

### Assistant

_source line 153_

<details><summary>Logged reasoning block</summary>

```text
Figure 1 (DDR strip plot) now appears on page 2, right in the introduction section. The "Diaz and Marathe, 2019" citation is visible on page 2 line 148-149. The Seddik citation on page 2/3 shows correctly. Table 1 (features) appears on page 4.

This looks good. The first display item is now on page 2 as desired.

Let me now compile a summary of all 7 tasks:

**2a. R34-W3: QLoRA 6-gen subset 标注** — Already present in all three locations. No changes needed.


**2b. R38-W3: 术语一致性** — "recursive generation depth" has no matches in the paper. DDR usage is consistent throughout. The appendix_qlora.tex file has consistent table captions and config, though LoRA alpha and target modules aren't specified in the setup description, which I should flag.
**2c. R37-M1: Figure 1/2 颜色一致性** — Both figures use the same color scheme with blue for drifting and amber for stationary, and the captions align properly.
**2d. R37-M3** —

Checking the aaronson_watermark entry, which already has the blog post note tagged correctly.

**2e. R37-R2: ordinal regression 引用** — I've added the Diaz & Marathe CVPR 2019 reference on ordinal regression to the bibliography and cited it in the related work section. The user's suggested author name was incorrect; Marathe is the actual co-author.

**2f. R35-M5: Bib first_author 修复** — Updated the seddik_synthetic_data entry from an arXiv preprint to the published COLM 2024 version. The other entries like llama3, mistral7b, and several others remain as arXiv preprints, which is correct.

**2g. R34-V1: Float 位置优化** — I've relocated the feature-drift figure from results.tex to introduction.tex so it appears earlier in the document on page 2, and added the corresponding reference in the introduction text. Modified introduction.tex, results.tex, related_work.tex, and references.bib as needed while leaving abstract.tex, discussion.tex, and conclusion.tex untouched. The document compiles cleanly at 36 pages with no errors, and I'm now syncing all the modified files to the artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "4e73a32f-f2dd-4185-a72b-a1872a238c30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSjW6ZurdknHo4QzLKYp3E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 91675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5231
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

_source line 154_

Figure 1 now appears on page 2. All edits compile cleanly (36 pages, no errors).

## Status Report

| Task | Status | Detail |
|------|--------|--------|
| **2a** R34-W3: QLoRA 6-gen 标注 | **已存在** | results.tex, method.tex, appendix_qlora.tex 均已有 "6-gen LOGO" + "same-subset XGBoost baseline" 说明 |
| **2b** R38-W3: 术语一致性 | **已存在/FLAG** | "recursive generation depth" 无匹配(clean)；DDR 用法一致；**FLAG**: appendix_qlora.tex 缺少 LoRA alpha 和 target modules，需补充实验值 |
| **2c** R37-M1: Figure 颜色一致性 | **已一致** | Fig 1 和 Fig 2 均用 blue=#0072B2(drifting)、amber=#E69F00(stationary)，caption 描述匹配 |
| **2d** R37-M3: aaronson bib | **已存在** | 已有 `note = {Blog post}`，无需修改 |
| **2e** R37-R2: ordinal regression 引用 | **已修改** | 添加 Diaz & Marathe (CVPR 2019) 到 references.bib，引用添加到 related_work.tex §2.1。注意：原建议的 "Karampatziakis" 是错误的，实际共同作者是 Amit Marathe |
| **2f** R35-M5: Bib 修复 | **已修改** | `seddik_synthetic_data` 从 arXiv → COLM 2024。llama3/mistral7b/briesch/koike 确认仍为 arXiv preprint |
| **2g** R34-V1: Float 位置 | **已修改** | fig:feature-drift 从 results.tex 移至 introduction.tex，Figure 1 现在出现在第 2 页 |

**修改的文件** (已同步到 artifacts/_project/paper/):
- `introduction.tex` — 添加 DDR 图 + Figure ref
- `results.tex` — 移除重复的 figure 环境
- `related_work.tex` — 添加 diaz_soft_labels_ordinal 引用
- `references.bib` — 新增 Diaz entry, 更新 Seddik 为 COLM 2024

**待人工补充**: appendix_qlora.tex 的 LoRA alpha 值和 target modules（需实验记录）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "uuid": "c34615ac-9bf7-4015-97ef-9e0132150055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GSjW6ZurdknHo4QzLKYp3E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 91675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5231
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

### Task result

_source line 155_

Figure 1 now appears on page 2. All edits compile cleanly (36 pages, no errors).

## Status Report

| Task | Status | Detail |
|------|--------|--------|
| **2a** R34-W3: QLoRA 6-gen 标注 | **已存在** | results.tex, method.tex, appendix_qlora.tex 均已有 "6-gen LOGO" + "same-subset XGBoost baseline" 说明 |
| **2b** R38-W3: 术语一致性 | **已存在/FLAG** | "recursive generation depth" 无匹配(clean)；DDR 用法一致；**FLAG**: appendix_qlora.tex 缺少 LoRA alpha 和 target modules，需补充实验值 |
| **2c** R37-M1: Figure 颜色一致性 | **已一致** | Fig 1 和 Fig 2 均用 blue=#0072B2(drifting)、amber=#E69F00(stationary)，caption 描述匹配 |
| **2d** R37-M3: aaronson bib | **已存在** | 已有 `note = {Blog post}`，无需修改 |
| **2e** R37-R2: ordinal regression 引用 | **已修改** | 添加 Diaz & Marathe (CVPR 2019) 到 references.bib，引用添加到 related_work.tex §2.1。注意：原建议的 "Karampatziakis" 是错误的，实际共同作者是 Amit Marathe |
| **2f** R35-M5: Bib 修复 | **已修改** | `seddik_synthetic_data` 从 arXiv → COLM 2024。llama3/mistral7b/briesch/koike 确认仍为 arXiv preprint |
| **2g** R34-V1: Float 位置 | **已修改** | fig:feature-drift 从 results.tex 移至 introduction.tex，Figure 1 现在出现在第 2 页 |

**修改的文件** (已同步到 artifacts/_project/paper/):
- `introduction.tex` — 添加 DDR 图 + Figure ref
- `results.tex` — 移除重复的 figure 环境
- `related_work.tex` — 添加 diaz_soft_labels_ordinal 引用
- `references.bib` — 新增 Diaz entry, 更新 Seddik 为 COLM 2024

**待人工补充**: appendix_qlora.tex 的 LoRA alpha 值和 target modules（需实验记录）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 544445,
  "duration_api_ms": 561434,
  "num_turns": 38,
  "stop_reason": "end_turn",
  "session_id": "f0729576-0a0b-4639-9730-0c3f60cce994",
  "total_cost_usd": 2.0659046499999993,
  "usage": {
    "input_tokens": 3116,
    "cache_creation_input_tokens": 85065,
    "cache_read_input_tokens": 1294166,
    "output_tokens": 23206,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 85065,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 1453,
        "cache_read_input_tokens": 91675,
        "cache_creation_input_tokens": 5231,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5231
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 82053,
      "outputTokens": 6554,
      "cacheReadInputTokens": 121174,
      "cacheCreationInputTokens": 75596,
      "webSearchRequests": 7,
      "costUSD": 0.2914354,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3116,
      "outputTokens": 23206,
      "cacheReadInputTokens": 1294166,
      "cacheCreationInputTokens": 85065,
      "webSearchRequests": 0,
      "costUSD": 1.7744692499999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e0bbdfec-73a6-4c6f-9510-90869f120fd0"
}
```

</details>

---
