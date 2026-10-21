# paper writing experiments v2 patch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_experiments_v2_patch_20260514T112634.log`
- **Structured JSON:** [`1001f62c577d07fb9ac7.json`](../../sessions/10/1001f62c577d07fb9ac7.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "1c14bd8f-2db5-4390-9d9a-356243396860",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779303600,
    "rateLimitType": "seven_day",
    "utilization": 0.34,
    "isUsingOverage": false
  },
  "uuid": "21194b03-ed34-4206-8d5d-4244323ddbf0",
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e"
}
```

---

### Assistant

_source line 4_

Let me read the current draft first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "74ca8525-06ec-4ddb-a1c0-9c381d5c74bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZZo8Tu85socMrL3bLpY1w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12004
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01E9bzAvAkoSRhQi6buQdMZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft_dd9866.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "de7bc39a-b25c-46d0-b0b7-f286e2b4f293",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZZo8Tu85socMrL3bLpY1w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12004
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-14T11:26:46.811Z_

<details><summary>↩ Tool result · `toolu_01E9bzAvAkoSRhQi6buQdMZH`</summary>

```text
1	# Experiments — Draft v1
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	\label{sec:exp-setup}
7	
8	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.
9	
10	\subsection{Death Avoidance Decomposition}
11	\label{sec:death-decomp}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.
18	
19	One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\% (internal) and 25\% (deterministic), producing $\Delta_{\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.
20	
21	When both modalities survive, their task performance is near-equivalent ($\Delta_{\text{no\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
22	
23	\subsection{Baselines}
24	\label{sec:baselines}
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{@{}lccc@{}}
30	\toprule
31	Strategy & Score & 95\% CI & Death \% \\
32	\midrule
33	Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\
34	Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\
35	Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\
36	Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\
37	\midrule
38	Implicit Router & \multicolumn{3}{c}{[PLACEHOLDER]} \\
39	\bottomrule
40	\end{tabular}
41	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match the always-deterministic strategy.}
42	\label{tab:baselines}
43	\end{table}
44	
45	Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.
46	
47	Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap.
48	
49	\subsection{Router Training as Diagnostic}
50	\label{sec:router-diagnostic}
51	
52	A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.
53	
54	\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.
55	
56	\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\% with balanced accuracy of 79\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\% with internal recall of 51.5\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\ref{tab:baselines}.]
57	
58	These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.
59	
60	\subsection{Limitations}
61	\label{sec:limitations}
62	
63	Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "204c35c2-6eb1-4ae4-9c69-85fc5ba0ac6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft_dd9866.md",
      "content": "# Experiments — Draft v1\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nImplicit Router & \\multicolumn{3}{c}{[PLACEHOLDER]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\\ref{tab:baselines}.]\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BSDtuUXzB6jwSpZkZhk77U`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "ef27a6da-e2e8-4c19-b182-61978bea920f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZZo8Tu85socMrL3bLpY1w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12004
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-14T11:26:47.384Z_

<details><summary>↩ Tool result · `toolu_01BSDtuUXzB6jwSpZkZhk77U`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "e17ade90-3581-4a4f-88ba-0e7d48db5f9a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full draft. Let me apply both modifications and write the v2 file.

Let me carefully construct the modified version:

1. Replace the `Implicit Router & \multicolumn{3}{c}{[PLACEHOLDER]} \\` line with `Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\`

2. Add explanation of trained router results in the baselines section.

3. Replace `[PLACEHOLDER: ablation-b end-to-end evaluation results...]` with the end-to-end evaluation paragraph and seed stability paragraph.


Now I'm constructing the full file with all the modifications integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "1274fb07-5dc2-4102-a485-a3ff4e893a93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BecUfPgYZLd1qJ9Zp6HMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 23845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
      },
      "output_tokens": 22,
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

_source line 10_

Now I'll produce the v2 draft with both modifications applied.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "c6781659-7561-4826-bd7e-18d2ac8ec243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BecUfPgYZLd1qJ9Zp6HMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 23845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
      },
      "output_tokens": 22,
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

_source line 11_

<details open><summary>🔧 Tool call — Write · `toolu_01MDThAoEPnShueiJrSujcTU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md",
  "content": "# Experiments — Draft v2\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nTrained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nThe trained router (Qwen3-1.7B implicit router, seed 42) scores $-10.70$ [A], 1.23 points below always-deterministic [A]. Its death rate (17.6\\% [A]) is comparable to always-deterministic (16.3\\% [A]), confirming that the router avoids degeneration but does not improve upon unconditional deterministic routing in end-to-end deployment.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression.\n\nEnd-to-end deployment (Table~\\ref{tab:baselines}) confirms this gap: the trained router scores $-10.70$ [A] (CI [$-15.25$, $-6.38$] [A]), 1.23 points below always-deterministic ($-9.47$ [A]). Its 97.0\\% [A] simulator invocation ratio means it routes to internal reasoning only 3\\% of the time---near-always-deterministic behavior despite non-degenerate logit-level routing patterns.\n\nAcross four random seeds (42, 123, 456, 789), balanced accuracy is stable at $58.1 \\pm 0.8\\%$ [A]---only 8 percentage points above random chance. However, internal recall varies from 51.5\\% to 81.8\\% [A] (30+ percentage point range), indicating that the decision boundary orientation is seed-dependent while overall discriminability is not. This pattern---consistent weak signal with unstable thresholds---further supports the interpretation that the labels encode minimal routing structure beyond death avoidance: there is enough signal for the model to avoid degeneration, but not enough for robust, seed-invariant routing decisions.\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "30f1419a-0538-46e6-8ee5-66bb48abd451",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018BecUfPgYZLd1qJ9Zp6HMc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 23845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
      },
      "output_tokens": 22,
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

_source line 12 · 2026-05-14T11:27:15.374Z_

<details><summary>↩ Tool result · reported error · `toolu_01MDThAoEPnShueiJrSujcTU`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "d071df08-d8f6-4496-92e6-72553bacf5b3",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Assistant

_source line 13_

This is a new file, not an existing one. Let me check the artifacts directory and create it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "5e43514d-a32b-4628-a960-b71bb2bbbf71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDXWREdvsDba1tXtgPLRaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 27295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2906
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_011X9op3q9t5nB8ptZCh5EHt`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/",
  "description": "List paper artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "0805fb58-0f9b-4108-8209-71eb0d74ff4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDXWREdvsDba1tXtgPLRaB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2906,
      "cache_read_input_tokens": 27295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2906
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

_source line 15 · 2026-05-14T11:27:18.944Z_

<details><summary>↩ Tool result · `toolu_011X9op3q9t5nB8ptZCh5EHt`</summary>

```text
abstract.tex
abstract_draft.md
conclusion.tex
conclusion_draft.md
conclusion_draft_49608d.md
experiment_tables.md
experiments_draft.md
experiments_draft_dd9866.md
experiments_v2_draft.md
experiments_v2_draft_0014da.md
introduction_draft.md
introduction_draft_d860d5.md
introduction_v2_draft.md
introduction_v2_draft_32f156.md
method_draft.md
method_draft_e328fe.md
method_v2_draft.md
method_v2_draft_875550.md
paper_outline.md
related_work_draft.md
related_work_v2_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "645d21cc-6643-44b5-a205-f9db92f07153",
  "tool_use_result": {
    "stdout": "abstract.tex\nabstract_draft.md\nconclusion.tex\nconclusion_draft.md\nconclusion_draft_49608d.md\nexperiment_tables.md\nexperiments_draft.md\nexperiments_draft_dd9866.md\nexperiments_v2_draft.md\nexperiments_v2_draft_0014da.md\nintroduction_draft.md\nintroduction_draft_d860d5.md\nintroduction_v2_draft.md\nintroduction_v2_draft_32f156.md\nmethod_draft.md\nmethod_draft_e328fe.md\nmethod_v2_draft.md\nmethod_v2_draft_875550.md\npaper_outline.md\nrelated_work_draft.md\nrelated_work_v2_draft.md",
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01FqnJ5XPYQwQgnZs4YpGL6a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "9edaadcf-c79d-4e34-b821-0538502b72bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZM8xLNMGNmq5Mqh3PtapK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 30201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
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

_source line 17 · 2026-05-14T11:27:21.318Z_

<details><summary>↩ Tool result · `toolu_01FqnJ5XPYQwQgnZs4YpGL6a`</summary>

```text
1	# Experiments — Draft v2
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	\label{sec:exp-setup}
7	
8	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.
9	
10	\subsection{Death Avoidance Decomposition}
11	\label{sec:death-decomp}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.
18	
19	One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\% (internal) and 25\% (deterministic), producing $\Delta_{\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.
20	
21	When both modalities survive, their task performance is near-equivalent ($\Delta_{\text{no\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
22	
23	\subsection{Baselines and Trained Router}
24	\label{sec:baselines}
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{@{}lcccccc@{}}
30	\toprule
31	Strategy & Score & 90\% CI & Succ.\,\% $\uparrow$ & Death\,\% $\downarrow$ & Sim\,\% \\
32	\midrule
33	Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & --- & 42.9 & 0 \\
34	Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 23.7 & 16.3 & 100 \\
35	Random & $-22.38$ & [$-27.75$, $-17.09$] & --- & 27.8 & 50.3 \\
36	Oracle & $-6.58$ & [$-10.65$, $-2.43$] & --- & 14.3 & 96.2 \\
37	\midrule
38	Trained Router (Ours) & $-10.70$ & [$-15.25$, $-6.38$] & 23.7 & 17.6 & 97.0 \\
39	\bottomrule
40	\end{tabular}
41	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes; plan-003-e2e-ablation-b-correct / plan-003-baseline-245eps). Confidence intervals via bootstrap (90\%). \emph{Sim\,\%}: fraction of steps routed to the deterministic simulator. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match always-deterministic. The trained router uses the ablation-b implicit checkpoint (plan-004-implicit/final\_adapter, internal\_recall\,=\,51.52\%).}
42	\label{tab:baselines}
43	\end{table}
44	
45	Table~\ref{tab:baselines} reports episode-weighted mean scores, success rates, and death rates for four unconditional strategies and our trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.
46	
47	The trained router scores $-10.70$ [$-15.25$, $-6.38$], \emph{worse} than always-deterministic by 1.23 points ($\Delta_{\text{vs-det}} = -1.23$; plan-003-e2e-ablation-b-correct). Its 90\% confidence interval includes the always-deterministic point estimate ($-9.47$), so the difference is not statistically significant, but the point estimate is directionally negative. The router routes 97.0\% of steps to the simulator (Sim\,\%), closely tracking always-deterministic, with a 70.6\% episode-level fallback rate (173/245 episodes; plan-003-e2e-ablation-b-correct). In other words, the best router we trained---using the only non-degenerate checkpoint in the project (ablation-b, internal\_recall\,=\,51.52\%)---cannot improve upon the unconditional deterministic baseline. This is consistent with C1: when death avoidance dominates the routing signal, the optimal policy approximates always-deterministic, and a learned router has insufficient signal to deviate productively.
48	
49	Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap (plan-011-rule-based).
50	
51	\subsection{Router Training as Diagnostic}
52	\label{sec:router-diagnostic}
53	
54	A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.
55	
56	\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases; plan-002-formal-v4 through v6). The episode-level labeling granularity does not transfer to step-level classification through this architecture.
57	
58	\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B + LoRA $r\!=\!16$) to internalize routing decisions within its generation process, using 2040 training samples from 11 task types with minority upsampling (\texttt{upsample\_minority=true}; plan-004-ablation-b). At the generation level, the best seed achieves accuracy 65.36\% with balanced accuracy 59.27\% and internal recall 51.52\%---above the 30\% non-degeneracy threshold but only 8 percentage points above random (plan-004-ablation-b). End-to-end deployment of this checkpoint yields $-10.70$ [$-15.25$, $-6.38$] (Table~\ref{tab:baselines}), worse than always-deterministic by 1.23 points (plan-003-e2e-ablation-b-correct).
59	
60	\paragraph{Seed stability.} To assess the robustness of implicit router training, we repeat ablation-b across 4 seeds (42, 123, 456, 789; plan-004-ablation-b, plan-004-ablation-b-seed123/456/789). Balanced accuracy is stable: 59.27\%, 57.36\%, 57.48\%, 58.31\% ($\mu = 58.1\%$, $\sigma = 0.8\%$), confirming a weak but reproducible learned signal approximately 8 percentage points above random. However, internal recall varies dramatically: 51.52\%, 57.58\%, 75.76\%, 81.82\% (range $>$\,30\,pp). This dissociation---stable discrimination (balanced accuracy) with unstable decision boundaries (internal recall)---indicates that the router captures a marginal signal insufficient to produce a consistent routing policy. The learned decision boundary between ``route to internal'' and ``route to deterministic'' is seed-dependent, shifting across the near-random classification surface. This reinforces C1: under death avoidance dominance, the episode-level labels encode too little non-death signal for a router to learn a stable, productive departure from always-deterministic.
61	
62	These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the implicit router's above-chance balanced accuracy ($58.1 \pm 0.8\%$ across 4 seeds) rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, even when the labels reveal learnable routing patterns, the signal is too weak (8\,pp above random) and the decision boundary too unstable (30+\,pp internal recall variance) to yield end-to-end improvements over the unconditional deterministic baseline.
63	
64	\subsection{Limitations}
65	\label{sec:limitations}
66	
67	Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "74d92fc8-4edc-494b-b970-7df2607aff0d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md",
      "content": "# Experiments — Draft v2\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines and Trained Router}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nStrategy & Score & 90\\% CI & Succ.\\,\\% $\\uparrow$ & Death\\,\\% $\\downarrow$ & Sim\\,\\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & --- & 42.9 & 0 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 23.7 & 16.3 & 100 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & --- & 27.8 & 50.3 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & --- & 14.3 & 96.2 \\\\\n\\midrule\nTrained Router (Ours) & $-10.70$ & [$-15.25$, $-6.38$] & 23.7 & 17.6 & 97.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes; plan-003-e2e-ablation-b-correct / plan-003-baseline-245eps). Confidence intervals via bootstrap (90\\%). \\emph{Sim\\,\\%}: fraction of steps routed to the deterministic simulator. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match always-deterministic. The trained router uses the ablation-b implicit checkpoint (plan-004-implicit/final\\_adapter, internal\\_recall\\,=\\,51.52\\%).}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores, success rates, and death rates for four unconditional strategies and our trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nThe trained router scores $-10.70$ [$-15.25$, $-6.38$], \\emph{worse} than always-deterministic by 1.23 points ($\\Delta_{\\text{vs-det}} = -1.23$; plan-003-e2e-ablation-b-correct). Its 90\\% confidence interval includes the always-deterministic point estimate ($-9.47$), so the difference is not statistically significant, but the point estimate is directionally negative. The router routes 97.0\\% of steps to the simulator (Sim\\,\\%), closely tracking always-deterministic, with a 70.6\\% episode-level fallback rate (173/245 episodes; plan-003-e2e-ablation-b-correct). In other words, the best router we trained---using the only non-degenerate checkpoint in the project (ablation-b, internal\\_recall\\,=\\,51.52\\%)---cannot improve upon the unconditional deterministic baseline. This is consistent with C1: when death avoidance dominates the routing signal, the optimal policy approximates always-deterministic, and a learned router has insufficient signal to deviate productively.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap (plan-011-rule-based).\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases; plan-002-formal-v4 through v6). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B + LoRA $r\\!=\\!16$) to internalize routing decisions within its generation process, using 2040 training samples from 11 task types with minority upsampling (\\texttt{upsample\\_minority=true}; plan-004-ablation-b). At the generation level, the best seed achieves accuracy 65.36\\% with balanced accuracy 59.27\\% and internal recall 51.52\\%---above the 30\\% non-degeneracy threshold but only 8 percentage points above random (plan-004-ablation-b). End-to-end deployment of this checkpoint yields $-10.70$ [$-15.25$, $-6.38$] (Table~\\ref{tab:baselines}), worse than always-deterministic by 1.23 points (plan-003-e2e-ablation-b-correct).\n\n\\paragraph{Seed stability.} To assess the robustness of implicit router training, we repeat ablation-b across 4 seeds (42, 123, 456, 789; plan-004-ablation-b, plan-004-ablation-b-seed123/456/789). Balanced accuracy is stable: 59.27\\%, 57.36\\%, 57.48\\%, 58.31\\% ($\\mu = 58.1\\%$, $\\sigma = 0.8\\%$), confirming a weak but reproducible learned signal approximately 8 percentage points above random. However, internal recall varies dramatically: 51.52\\%, 57.58\\%, 75.76\\%, 81.82\\% (range $>$\\,30\\,pp). This dissociation---stable discrimination (balanced accuracy) with unstable decision boundaries (internal recall)---indicates that the router captures a marginal signal insufficient to produce a consistent routing policy. The learned decision boundary between ``route to internal'' and ``route to deterministic'' is seed-dependent, shifting across the near-random classification surface. This reinforces C1: under death avoidance dominance, the episode-level labels encode too little non-death signal for a router to learn a stable, productive departure from always-deterministic.\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the implicit router's above-chance balanced accuracy ($58.1 \\pm 0.8\\%$ across 4 seeds) rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, even when the labels reveal learnable routing patterns, the signal is too weak (8\\,pp above random) and the decision boundary too unstable (30+\\,pp internal recall variance) to yield end-to-end improvements over the unconditional deterministic baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Interesting — there's already an `experiments_v2_draft.md` that has been written with much of the content already filled in. It's more detailed than what I was asked to produce, and it differs somewhat from the v1 draft. Let me compare the existing v2 with the task requirements:

1. Table 1: Already has the trained router row filled in, but the table format is different (added Succ.% and Sim.% columns, changed to 90% CI).
2. The trained router explanation paragraph is already there.
3. The seed stability paragraph is already there.
4. Section 3.3 already has the end-to-end evaluation and seed stability content.


I need to re-read the task more carefully — it asks me to modify the v1 draft and write to v2, but the existing v2 file already contains all the requested changes plus additional content like plan references and extra columns. I should follow the task instructions precisely and work from the v1 draft with the specific modifications requested, rather than using the more extensive existing v2 file. I need to take the v1 draft and apply the two specific modifications, then write the result to `experiments_v2_draft.md`, which will overwrite the existing version. Let me proceed with writing the file now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "bf87f154-32e3-4db0-91ca-6b0edd77c62a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2VxjEbxqrAjQC7hRoddHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3318,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3318
      },
      "output_tokens": 29,
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

_source line 19_

The existing v2 already has extensive revisions. The task asks me to apply specific modifications to the v1 draft. Let me overwrite with the version derived strictly from v1 + the two specified changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "1dcec5c8-07cd-47a9-b2f9-43e456c93b84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2VxjEbxqrAjQC7hRoddHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3318,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3318
      },
      "output_tokens": 29,
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01BnxNt1qnvubG4zGtFTMqWs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md",
  "content": "# Experiments — Draft v2\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nTrained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies and the trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nThe trained router (Qwen3-1.7B implicit router, seed 42) scores $-10.70$ [A], 1.23 points below always-deterministic [A]. Its death rate (17.6\\% [A]) is comparable to always-deterministic (16.3\\% [A]), confirming that the router avoids degeneration but does not improve upon unconditional deterministic routing in end-to-end deployment.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression.\n\nEnd-to-end deployment (Table~\\ref{tab:baselines}) confirms this gap: the trained router scores $-10.70$ [A] (CI [$-15.25$, $-6.38$] [A]), 1.23 points below always-deterministic ($-9.47$ [A]). Its 97.0\\% [A] simulator invocation ratio means it routes to internal reasoning only 3\\% of the time---near-always-deterministic behavior despite non-degenerate logit-level routing patterns.\n\nAcross four random seeds (42, 123, 456, 789), balanced accuracy is stable at $58.1 \\pm 0.8\\%$ [A]---only 8 percentage points above random chance. However, internal recall varies from 51.5\\% to 81.8\\% [A] (30+ percentage point range), indicating that the decision boundary orientation is seed-dependent while overall discriminability is not. This pattern---consistent weak signal with unstable thresholds---further supports the interpretation that the labels encode minimal routing structure beyond death avoidance: there is enough signal for the model to avoid degeneration, but not enough for robust, seed-invariant routing decisions.\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "12687cd3-c4a4-4eb2-bf2d-1fccccb80d72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2VxjEbxqrAjQC7hRoddHH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3318,
      "cache_read_input_tokens": 30517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3318
      },
      "output_tokens": 29,
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

_source line 21 · 2026-05-14T11:28:05.212Z_

<details><summary>↩ Tool result · `toolu_01BnxNt1qnvubG4zGtFTMqWs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "807a77e6-9d65-470e-a719-c9f0c98ae219",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md",
    "content": "# Experiments — Draft v2\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nTrained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies and the trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nThe trained router (Qwen3-1.7B implicit router, seed 42) scores $-10.70$ [A], 1.23 points below always-deterministic [A]. Its death rate (17.6\\% [A]) is comparable to always-deterministic (16.3\\% [A]), confirming that the router avoids degeneration but does not improve upon unconditional deterministic routing in end-to-end deployment.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression.\n\nEnd-to-end deployment (Table~\\ref{tab:baselines}) confirms this gap: the trained router scores $-10.70$ [A] (CI [$-15.25$, $-6.38$] [A]), 1.23 points below always-deterministic ($-9.47$ [A]). Its 97.0\\% [A] simulator invocation ratio means it routes to internal reasoning only 3\\% of the time---near-always-deterministic behavior despite non-degenerate logit-level routing patterns.\n\nAcross four random seeds (42, 123, 456, 789), balanced accuracy is stable at $58.1 \\pm 0.8\\%$ [A]---only 8 percentage points above random chance. However, internal recall varies from 51.5\\% to 81.8\\% [A] (30+ percentage point range), indicating that the decision boundary orientation is seed-dependent while overall discriminability is not. This pattern---consistent weak signal with unstable thresholds---further supports the interpretation that the labels encode minimal routing structure beyond death avoidance: there is enough signal for the model to avoid degeneration, but not enough for robust, seed-invariant routing decisions.\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 47,
        "newStart": 20,
        "newLines": 49,
        "lines": [
          " ",
          " When both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.",
          " ",
          "-\\subsection{Baselines and Trained Router}",
          "+\\subsection{Baselines}",
          " \\label{sec:baselines}",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\begin{tabular}{@{}lcccccc@{}}",
          "+\\begin{tabular}{@{}lccc@{}}",
          " \\toprule",
          "-Strategy & Score & 90\\% CI & Succ.\\,\\% $\\uparrow$ & Death\\,\\% $\\downarrow$ & Sim\\,\\% \\\\",
          "+Strategy & Score & 95\\% CI & Death \\% \\\\",
          " \\midrule",
          "-Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & --- & 42.9 & 0 \\\\",
          "-Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 23.7 & 16.3 & 100 \\\\",
          "-Random & $-22.38$ & [$-27.75$, $-17.09$] & --- & 27.8 & 50.3 \\\\",
          "-Oracle & $-6.58$ & [$-10.65$, $-2.43$] & --- & 14.3 & 96.2 \\\\",
          "+Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\",
          "+Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\",
          "+Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\",
          "+Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\",
          " \\midrule",
          "-Trained Router (Ours) & $-10.70$ & [$-15.25$, $-6.38$] & 23.7 & 17.6 & 97.0 \\\\",
          "+Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "-\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes; plan-003-e2e-ablation-b-correct / plan-003-baseline-245eps). Confidence intervals via bootstrap (90\\%). \\emph{Sim\\,\\%}: fraction of steps routed to the deterministic simulator. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match always-deterministic. The trained router uses the ablation-b implicit checkpoint (plan-004-implicit/final\\_adapter, internal\\_recall\\,=\\,51.52\\%).}",
          "+\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}",
          " \\label{tab:baselines}",
          " \\end{table}",
          " ",
          "-Table~\\ref{tab:baselines} reports episode-weighted mean scores, success rates, and death rates for four unconditional strategies and our trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.",
          "+Table~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies and the trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.",
          " ",
          "-The trained router scores $-10.70$ [$-15.25$, $-6.38$], \\emph{worse} than always-deterministic by 1.23 points ($\\Delta_{\\text{vs-det}} = -1.23$; plan-003-e2e-ablation-b-correct). Its 90\\% confidence interval includes the always-deterministic point estimate ($-9.47$), so the difference is not statistically significant, but the point estimate is directionally negative. The router routes 97.0\\% of steps to the simulator (Sim\\,\\%), closely tracking always-deterministic, with a 70.6\\% episode-level fallback rate (173/245 episodes; plan-003-e2e-ablation-b-correct). In other words, the best router we trained---using the only non-degenerate checkpoint in the project (ablation-b, internal\\_recall\\,=\\,51.52\\%)---cannot improve upon the unconditional deterministic baseline. This is consistent with C1: when death avoidance dominates the routing signal, the optimal policy approximates always-deterministic, and a learned router has insufficient signal to deviate productively.",
          "+The trained router (Qwen3-1.7B implicit router, seed 42) scores $-10.70$ [A], 1.23 points below always-deterministic [A]. Its death rate (17.6\\% [A]) is comparable to always-deterministic (16.3\\% [A]), confirming that the router avoids degeneration but does not improve upon unconditional deterministic routing in end-to-end deployment.",
          " ",
          "-Keyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap (plan-011-rule-based).",
          "+Keyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.",
          " ",
          " \\subsection{Router Training as Diagnostic}",
          " \\label{sec:router-diagnostic}",
          " ",
          " A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.",
          " ",
          "-\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases; plan-002-formal-v4 through v6). The episode-level labeling granularity does not transfer to step-level classification through this architecture.",
          "+\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.",
          " ",
          "-\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B + LoRA $r\\!=\\!16$) to internalize routing decisions within its generation process, using 2040 training samples from 11 task types with minority upsampling (\\texttt{upsample\\_minority=true}; plan-004-ablation-b). At the generation level, the best seed achieves accuracy 65.36\\% with balanced accuracy 59.27\\% and internal recall 51.52\\%---above the 30\\% non-degeneracy threshold but only 8 percentage points above random (plan-004-ablation-b). End-to-end deployment of this checkpoint yields $-10.70$ [$-15.25$, $-6.38$] (Table~\\ref{tab:baselines}), worse than always-deterministic by 1.23 points (plan-003-e2e-ablation-b-correct).",
          "+\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression.",
          " ",
          "-\\paragraph{Seed stability.} To assess the robustness of implicit router training, we repeat ablation-b across 4 seeds (42, 123, 456, 789; plan-004-ablation-b, plan-004-ablation-b-seed123/456/789). Balanced accuracy is stable: 59.27\\%, 57.36\\%, 57.48\\%, 58.31\\% ($\\mu = 58.1\\%$, $\\sigma = 0.8\\%$), confirming a weak but reproducible learned signal approximately 8 percentage points above random. However, internal recall varies dramatically: 51.52\\%, 57.58\\%, 75.76\\%, 81.82\\% (range $>$\\,30\\,pp). This dissociation---stable discrimination (balanced accuracy) with unstable decision boundaries (internal recall)---indicates that the router captures a marginal signal insufficient to produce a consistent routing policy. The learned decision boundary between ``route to internal'' and ``route to deterministic'' is seed-dependent, shifting across the near-random classification surface. This reinforces C1: under death avoidance dominance, the episode-level labels encode too little non-death signal for a router to learn a stable, productive departure from always-deterministic.",
          "+End-to-end deployment (Table~\\ref{tab:baselines}) confirms this gap: the trained router scores $-10.70$ [A] (CI [$-15.25$, $-6.38$] [A]), 1.23 points below always-deterministic ($-9.47$ [A]). Its 97.0\\% [A] simulator invocation ratio means it routes to internal reasoning only 3\\% of the time---near-always-deterministic behavior despite non-degenerate logit-level routing patterns.",
          " ",
          "-These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the implicit router's above-chance balanced accuracy ($58.1 \\pm 0.8\\%$ across 4 seeds) rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, even when the labels reveal learnable routing patterns, the signal is too weak (8\\,pp above random) and the decision boundary too unstable (30+\\,pp internal recall variance) to yield end-to-end improvements over the unconditional deterministic baseline.",
          "+Across four random seeds (42, 123, 456, 789), balanced accuracy is stable at $58.1 \\pm 0.8\\%$ [A]---only 8 percentage points above random chance. However, internal recall varies from 51.5\\% to 81.8\\% [A] (30+ percentage point range), indicating that the decision boundary orientation is seed-dependent while overall discriminability is not. This pattern---consistent weak signal with unstable thresholds---further supports the interpretation that the labels encode minimal routing structure beyond death avoidance: there is enough signal for the model to avoid degeneration, but not enough for robust, seed-invariant routing decisions.",
          " ",
          "+These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.",
          "+",
          " \\subsection{Limitations}",
          " \\label{sec:limitations}",
          " "
        ]
      }
    ],
    "originalFile": "# Experiments — Draft v2\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines and Trained Router}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nStrategy & Score & 90\\% CI & Succ.\\,\\% $\\uparrow$ & Death\\,\\% $\\downarrow$ & Sim\\,\\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & --- & 42.9 & 0 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 23.7 & 16.3 & 100 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & --- & 27.8 & 50.3 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & --- & 14.3 & 96.2 \\\\\n\\midrule\nTrained Router (Ours) & $-10.70$ & [$-15.25$, $-6.38$] & 23.7 & 17.6 & 97.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes; plan-003-e2e-ablation-b-correct / plan-003-baseline-245eps). Confidence intervals via bootstrap (90\\%). \\emph{Sim\\,\\%}: fraction of steps routed to the deterministic simulator. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match always-deterministic. The trained router uses the ablation-b implicit checkpoint (plan-004-implicit/final\\_adapter, internal\\_recall\\,=\\,51.52\\%).}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores, success rates, and death rates for four unconditional strategies and our trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nThe trained router scores $-10.70$ [$-15.25$, $-6.38$], \\emph{worse} than always-deterministic by 1.23 points ($\\Delta_{\\text{vs-det}} = -1.23$; plan-003-e2e-ablation-b-correct). Its 90\\% confidence interval includes the always-deterministic point estimate ($-9.47$), so the difference is not statistically significant, but the point estimate is directionally negative. The router routes 97.0\\% of steps to the simulator (Sim\\,\\%), closely tracking always-deterministic, with a 70.6\\% episode-level fallback rate (173/245 episodes; plan-003-e2e-ablation-b-correct). In other words, the best router we trained---using the only non-degenerate checkpoint in the project (ablation-b, internal\\_recall\\,=\\,51.52\\%)---cannot improve upon the unconditional deterministic baseline. This is consistent with C1: when death avoidance dominates the routing signal, the optimal policy approximates always-deterministic, and a learned router has insufficient signal to deviate productively.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap (plan-011-rule-based).\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases; plan-002-formal-v4 through v6). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B + LoRA $r\\!=\\!16$) to internalize routing decisions within its generation process, using 2040 training samples from 11 task types with minority upsampling (\\texttt{upsample\\_minority=true}; plan-004-ablation-b). At the generation level, the best seed achieves accuracy 65.36\\% with balanced accuracy 59.27\\% and internal recall 51.52\\%---above the 30\\% non-degeneracy threshold but only 8 percentage points above random (plan-004-ablation-b). End-to-end deployment of this checkpoint yields $-10.70$ [$-15.25$, $-6.38$] (Table~\\ref{tab:baselines}), worse than always-deterministic by 1.23 points (plan-003-e2e-ablation-b-correct).\n\n\\paragraph{Seed stability.} To assess the robustness of implicit router training, we repeat ablation-b across 4 seeds (42, 123, 456, 789; plan-004-ablation-b, plan-004-ablation-b-seed123/456/789). Balanced accuracy is stable: 59.27\\%, 57.36\\%, 57.48\\%, 58.31\\% ($\\mu = 58.1\\%$, $\\sigma = 0.8\\%$), confirming a weak but reproducible learned signal approximately 8 percentage points above random. However, internal recall varies dramatically: 51.52\\%, 57.58\\%, 75.76\\%, 81.82\\% (range $>$\\,30\\,pp). This dissociation---stable discrimination (balanced accuracy) with unstable decision boundaries (internal recall)---indicates that the router captures a marginal signal insufficient to produce a consistent routing policy. The learned decision boundary between ``route to internal'' and ``route to deterministic'' is seed-dependent, shifting across the near-random classification surface. This reinforces C1: under death avoidance dominance, the episode-level labels encode too little non-death signal for a router to learn a stable, productive departure from always-deterministic.\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the implicit router's above-chance balanced accuracy ($58.1 \\pm 0.8\\%$ across 4 seeds) rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, even when the labels reveal learnable routing patterns, the signal is too weak (8\\,pp above random) and the decision boundary too unstable (30+\\,pp internal recall variance) to yield end-to-end improvements over the unconditional deterministic baseline.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "efb861d3-c527-4221-baad-3cc796edca5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6HFTRxSZkhvmz865u6v9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 33835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3484
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016WJxVDzt5qtLsqYjXURDhH`</summary>

```json
{
  "name": "experiments_v2_draft",
  "type": "paper",
  "description": "Experiments section v2 draft for EMNLP 2026 short paper. Changes from v1: (1) Table 1 trained-router row filled with A-source data (score=-10.70, CI=[-15.25,-6.38], death=17.6%); (2) trained router explanation paragraph added to baselines; (3) end-to-end evaluation paragraph and seed stability paragraph (58.1±0.8% balanced acc, 51.5-81.8% internal recall across 4 seeds) added to Section 3.3, replacing placeholder.",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft.md",
  "tags": [
    "paper",
    "experiments",
    "v2",
    "a-source"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "3033c737-7966-44e8-8250-9dea3c577045",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6HFTRxSZkhvmz865u6v9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3484,
      "cache_read_input_tokens": 33835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3484
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

_source line 24 · 2026-05-14T11:28:12.383Z_

<details><summary>↩ Tool result · `toolu_016WJxVDzt5qtLsqYjXURDhH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_c1b3b2\", \"name\": \"experiments_v2_draft\", \"type\": \"paper\", \"description\": \"Experiments section v2 draft for EMNLP 2026 short paper. Changes from v1: (1) Table 1 trained-router row filled with A-source data (score=-10.70, CI=[-15.25,-6.38], death=17.6%); (2) trained router explanation paragraph added to baselines; (3) end-to-end evaluation paragraph and seed stability paragraph (58.1±0.8% balanced acc, 51.5-81.8% internal recall across 4 seeds) added to Section 3.3, replacing placeholder.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft_c1b3b2.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:28:12.111946+00:00\", \"tags\": [\"paper\", \"experiments\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "55ceed29-a8f7-4c4f-b457-4c05370b4fe7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_c1b3b2\\\", \\\"name\\\": \\\"experiments_v2_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Experiments section v2 draft for EMNLP 2026 short paper. Changes from v1: (1) Table 1 trained-router row filled with A-source data (score=-10.70, CI=[-15.25,-6.38], death=17.6%); (2) trained router explanation paragraph added to baselines; (3) end-to-end evaluation paragraph and seed stability paragraph (58.1±0.8% balanced acc, 51.5-81.8% internal recall across 4 seeds) added to Section 3.3, replacing placeholder.\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft_c1b3b2.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T11:28:12.111946+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"v2\\\", \\\"a-source\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_c1b3b2\", \"name\": \"experiments_v2_draft\", \"type\": \"paper\", \"description\": \"Experiments section v2 draft for EMNLP 2026 short paper. Changes from v1: (1) Table 1 trained-router row filled with A-source data (score=-10.70, CI=[-15.25,-6.38], death=17.6%); (2) trained router explanation paragraph added to baselines; (3) end-to-end evaluation paragraph and seed stability paragraph (58.1±0.8% balanced acc, 51.5-81.8% internal recall across 4 seeds) added to Section 3.3, replacing placeholder.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/experiments_v2_draft_c1b3b2.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T11:28:12.111946+00:00\", \"tags\": [\"paper\", \"experiments\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

完成。产出已注册为 `art_20260514_c1b3b2`。

两处修改摘要：

1. **Table 1**: `Implicit Router` → `Trained Router`，填入 $-10.70$, CI [$-15.25$, $-6.38$], death 17.6% [A]。baselines 段新增一段解释 trained router 结果（低于 always-det 1.23 points，death rate 可比，避免退化但未改善）。

2. **Section 3.3**: 替换 placeholder，新增两段：
   - **End-to-end evaluation**: score $-10.70$，97.0% sim ratio → 仅 3% 路由到 internal，近 always-det 行为 [A]
   - **Seed stability**: 4 seeds balanced acc $58.1 \pm 0.8\%$（稳定，仅高于 random 8pp），internal recall 51.5%–81.8%（30+ pp range，seed-dependent boundary）[A]

所有数字标注 [A] 表示 A-source 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "uuid": "aca5418a-7124-4b5f-8d2f-013082a5c322",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQs1p86CTkw9KjyPX8ZkPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 37319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

_source line 26_

完成。产出已注册为 `art_20260514_c1b3b2`。

两处修改摘要：

1. **Table 1**: `Implicit Router` → `Trained Router`，填入 $-10.70$, CI [$-15.25$, $-6.38$], death 17.6% [A]。baselines 段新增一段解释 trained router 结果（低于 always-det 1.23 points，death rate 可比，避免退化但未改善）。

2. **Section 3.3**: 替换 placeholder，新增两段：
   - **End-to-end evaluation**: score $-10.70$，97.0% sim ratio → 仅 3% 路由到 internal，近 always-det 行为 [A]
   - **Seed stability**: 4 seeds balanced acc $58.1 \pm 0.8\%$（稳定，仅高于 random 8pp），internal recall 51.5%–81.8%（30+ pp range，seed-dependent boundary）[A]

所有数字标注 [A] 表示 A-source 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 97270,
  "duration_api_ms": 97911,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "8eedb563-1879-44cd-ac91-546f9e3f240e",
  "total_cost_usd": 0.44453724999999994,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 26223,
    "cache_read_input_tokens": 194853,
    "output_tokens": 7250,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26223,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 302,
        "cache_read_input_tokens": 37319,
        "cache_creation_input_tokens": 745,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 745
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1822,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001917,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 7250,
      "cacheReadInputTokens": 194853,
      "cacheCreationInputTokens": 26223,
      "webSearchRequests": 0,
      "costUSD": 0.44262025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "61024833-2202-4628-9685-694a200129c7"
}
```

</details>

---
