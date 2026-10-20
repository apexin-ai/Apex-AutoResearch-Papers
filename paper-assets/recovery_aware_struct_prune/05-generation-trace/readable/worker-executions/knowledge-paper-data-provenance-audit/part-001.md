# knowledge paper data provenance audit — Part 1 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

[Transcript overview](../knowledge-paper-data-provenance-audit.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/58/58f6896d6bb5dcb5c414.json)

## Before a recorded user message

## Before a recorded user message

40 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
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
  "uuid": "9d93ebbe-4d3a-4342-a7b5-e293730eae45",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779540000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "baaa688f-46b5-4318-8aff-740875902692",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the tex files and the registry data in parallel. I'll need to:

1. Read all tex files to extract numerical values
2. Read the registry to get experiment data

Let me begin by reading the tex files and the registry simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "eb24b86c-b101-4723-8cfa-bfadc082b886",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13376
      },
      "output_tokens": 23,
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

开始读取论文表格文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "252ffbc5-0dc6-4739-885e-3b72bd933c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13376
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y5j1kkwaxDsWB8g6LctV1Q`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "4875beca-6fa7-4fba-951f-60891b69a9fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWzUGgWUHoVvgZ9iEqHwom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13376,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13376
      },
      "output_tokens": 23,
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

_source line 7 · 2026-05-23T10:47:13.838Z_

<details><summary>↩ Tool result · `toolu_01Y5j1kkwaxDsWB8g6LctV1Q`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

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
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5cdddc68-f2a9-493d-97b7-be75b42bf902",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the tex files and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "694bb490-0561-4fc0-ba1f-39be46ea2ab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01HdnnBWHBin4Smo4agMq37P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "8379e0ee-2e18-4719-8f73-dc325869782e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 10 · 2026-05-23T10:47:18.732Z_

<details><summary>↩ Tool result · `toolu_01HdnnBWHBin4Smo4agMq37P`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\% sparsity under identical configuration (lr $1{\times}10^{-6}$, $\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ & Behavior \\
9	\midrule
10	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} & Active learning \\
11	Random & 0.190 & 0.164 & 0.300 & Stagnation \\
12	Standard & 0.081 & 0.050 & 0.500 & Borderline collapse \\
13	\rasp{} ($\alpha{=}1.0$)$^\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\
14	\bottomrule
15	\multicolumn{5}{l}{\footnotesize $^\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\ref{tab:decoupling}).}
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "9fbd5774-5ae1-4ad9-8251-a8d08d5d6dad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\\% sparsity under identical configuration (lr $1{\\times}10^{-6}$, $\\beta{=}0.01$, $T{=}0.4$, 100 steps). Peak reward = best across 100 training steps. $f_0$: fraction of training batches where all sampled completions receive identical reward (lower = healthier exploration). Best in \\textbf{bold}.}\n\\label{tab:recovery_gradient}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Peak Rew.\\,$\\uparrow$ & Mean Rew.\\,$\\uparrow$ & Min $f_0$\\,$\\downarrow$ & Behavior \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{0.285} & \\textbf{0.125} & Active learning \\\\\nRandom & 0.190 & 0.164 & 0.300 & Stagnation \\\\\nStandard & 0.081 & 0.050 & 0.500 & Borderline collapse \\\\\n\\rasp{} ($\\alpha{=}1.0$)$^\\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\\ref{tab:decoupling}).}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01TtKUFaVuKs4SBgYvh9x2PD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "c21c0207-b64a-4a7e-9871-cd990dc423b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 12 · 2026-05-23T10:47:19.078Z_

<details><summary>↩ Tool result · `toolu_01TtKUFaVuKs4SBgYvh9x2PD`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled GRPO configuration (identical hyperparameters including \texttt{reward\_desert\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\pm$ std over 3 GRPO seeds; \rasp{} uses a single seed. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Model & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
9	\midrule
10	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
11	CKA-only 20\% & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
12	Standard 20\% & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
13	\rasp{} ($\alpha{=}1.0$) 20\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\
14	Random 20\% & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\
17	\bottomrule
18	\multicolumn{5}{l}{\footnotesize $^\dagger$Depth pruning baseline~\citep{shortgpt2024}; removes entire layers.} \\
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "56f9d100-b140-40ba-826b-7887f43f0de4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding). All pruned models use the controlled GRPO configuration (identical hyperparameters including \\texttt{reward\\_desert\\_patience}{$=$}50), evaluated at step 100. CKA-only, Standard, and Random report mean $\\pm$ std over 3 GRPO seeds; \\rasp{} uses a single seed. Best in \\textbf{bold}.}\n\\label{tab:decoupling}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) & Peak Rew. \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only 20\\% & 63.91 & 64.39{\\scriptsize$\\pm$0.19} & $+$0.48 & 0.354 \\\\\nStandard 20\\% & 59.29 & 59.84{\\scriptsize$\\pm$0.38} & $+$0.55 & 0.081 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\\\\nRandom 20\\% & 51.25 & 50.72{\\scriptsize$\\pm$0.15} & $-$0.53 & 0.190 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Depth pruning baseline~\\citep{shortgpt2024}; removes entire layers.} \\\\\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_019Z2SeEokTEq6aoTLjSAQLy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "e3439d2e-7e6d-47b6-8c39-38ad8941b488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 14 · 2026-05-23T10:47:20.214Z_

<details><summary>↩ Tool result · `toolu_019Z2SeEokTEq6aoTLjSAQLy`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "acf0c473-4a7f-4e50-b577-e710d9bc7819",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\n\\label{tab:alpha}\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\alpha$ & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n0.5 & 60.73 & 61.18 & $+$0.45 \\\\\n1.0 & 61.49 & 60.88 & $-$0.61 \\\\\n\\textbf{2.0} & \\textbf{64.97} & \\textbf{66.11} & $+$1.14 \\\\\n3.0 & 64.14 & 63.46 & $-$0.68 \\\\\n4.0 & 61.94 & 62.77 & $+$0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01JYfNfZ59WSJiBbcmQpM6LK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "1b0d25e1-c838-44c4-9fb3-2fd952de759e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 16 · 2026-05-23T10:47:21.182Z_

<details><summary>↩ Tool result · `toolu_01JYfNfZ59WSJiBbcmQpM6LK`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Sparsity cliff at 30\% structured sparsity ($N{=}100$). All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\%.}
4	\label{tab:sparsity_cliff}
5	\begin{tabular}{@{}lcc@{}}
6	\toprule
7	Method & Acc.\,(\%) & EOS Rate\,(\%) \\
8	\midrule
9	Standard & 4 & 5.5 \\
10	\rasp{} ($\alpha{=}1.0$) & 0 & 3.0 \\
11	CKA-only & 0 & --$^\dagger$ \\
12	\bottomrule
13	\multicolumn{3}{@{}l}{\footnotesize $^\dagger$Terminated early after collapse confirmed.}
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "58819d10-7da1-4efd-b7b8-ca79119ee311",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Sparsity cliff at 30\\% structured sparsity ($N{=}100$). All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\\%.}\n\\label{tab:sparsity_cliff}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Acc.\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nStandard & 4 & 5.5 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0 & 3.0 \\\\\nCKA-only & 0 & --$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{3}{@{}l}{\\footnotesize $^\\dagger$Terminated early after collapse confirmed.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01UL3iTDgbJbpJDWL4XmAbsY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "e21dd90d-34bc-4c6a-96fc-56bcb5a38d4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 18 · 2026-05-23T10:47:21.511Z_

<details><summary>↩ Tool result · `toolu_01UL3iTDgbJbpJDWL4XmAbsY`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Inference efficiency at 20\% sparsity. Latency averaged over 100 GSM8K problems. Both pruned configurations remove ${\sim}$1.45B parameters; the latency gap arises from differences in layer-wise sparsity distribution. Best pruned result in \textbf{bold}.}
5	\label{tab:inference}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	Configuration & Latency\,(s) & Speedup\,(\%) & Memory\,(GB) & Mem.\,Red.\,(\%) \\
9	\midrule
10	Dense & 6.682 & -- & 16.22 & -- \\
11	\rasp{} ($\alpha{=}1.0$) 20\% & \textbf{4.156} & \textbf{37.8} & 11.60 & 28.5 \\
12	Standard 20\% & 6.167 & 7.7 & 11.61 & 28.4 \\
13	\bottomrule
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "48379c96-e0e8-4584-bcd0-fd3c294eee88",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table5_inference.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inference efficiency at 20\\% sparsity. Latency averaged over 100 GSM8K problems. Both pruned configurations remove ${\\sim}$1.45B parameters; the latency gap arises from differences in layer-wise sparsity distribution. Best pruned result in \\textbf{bold}.}\n\\label{tab:inference}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & Latency\\,(s) & Speedup\\,(\\%) & Memory\\,(GB) & Mem.\\,Red.\\,(\\%) \\\\\n\\midrule\nDense & 6.682 & -- & 16.22 & -- \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & \\textbf{4.156} & \\textbf{37.8} & 11.60 & 28.5 \\\\\nStandard 20\\% & 6.167 & 7.7 & 11.61 & 28.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01H3Bzo7Hr2kMUL5GwCpCiqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "8c65708c-e6b4-4a37-b2af-1799e282f959",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 20 · 2026-05-23T10:47:22.486Z_

<details><summary>↩ Tool result · `toolu_01H3Bzo7Hr2kMUL5GwCpCiqk`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K. GRPO evaluation available for method comparison; dose-response GRPO follows the same ordering as GSM8K (Table~\ref{tab:alpha}). Best SFT in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{26.8} & 27.4 & $+$0.6 \\
14	Standard & 25.8$^\ddagger$ & 26.4$^\ddagger$ & $+$0.6 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.2 & 22.6 & $+$1.4 \\
16	Random & 14.4 & --- & --- \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\
20	$\alpha{=}2.0$ & 24.0 & 26.2 & $+$2.2 \\
21	$\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\
22	$\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 19.2 & 18.4 & $-$0.8 \\
26	Standard & 14.0 & 12.8 & $-$1.2 \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint. $^\ddagger$Evaluated with earlier answer extraction script; re-evaluation with updated script pending.}
29	\end{tabular}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "ff5fdc8e-46f6-4cc7-9aa6-4d46224e1c79",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). The method ordering (CKA-only $>$ Standard $>$ Random) is preserved from GSM8K. GRPO evaluation available for method comparison; dose-response GRPO follows the same ordering as GSM8K (Table~\\ref{tab:alpha}). Best SFT in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & \\multicolumn{3}{c}{53.0\\,$^\\dagger$} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\nCKA-only & \\textbf{26.8} & 27.4 & $+$0.6 \\\\\nStandard & 25.8$^\\ddagger$ & 26.4$^\\ddagger$ & $+$0.6 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 21.2 & 22.6 & $+$1.4 \\\\\nRandom & 14.4 & --- & --- \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n$\\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\\\\n$\\alpha{=}2.0$ & 24.0 & 26.2 & $+$2.2 \\\\\n$\\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\\\\n$\\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{25\\% sparsity}} \\\\\nCKA-only & 19.2 & 18.4 & $-$0.8 \\\\\nStandard & 14.0 & 12.8 & $-$1.2 \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint. $^\\ddagger$Evaluated with earlier answer extraction script; re-evaluation with updated script pending.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01TVXnyh7JDHF6K4i7V4nybN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "6bf1b10a-7a38-4ad8-993b-c32f48a454af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 22 · 2026-05-23T10:47:22.944Z_

<details><summary>↩ Tool result · `toolu_01TVXnyh7JDHF6K4i7V4nybN`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "82459658-0a6a-4bd0-a700-5b6ccd48a1de",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\\sim}$75\\% code capability loss vs Dense), limiting differentiation (${\\sim}$1\\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\\,pp) but at the 95\\% CI boundary (stderr ${\\approx}$1.55\\,pp).}\n\\label{tab:mbpp}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & -- & 53.48 & -- \\\\\n\\midrule\nCKA-only 20\\% & 12.83 & 14.17 & $+$1.34 \\\\\nStandard 20\\% & 12.03 & 13.10 & $+$1.07 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 11.76 & 13.10 & $+$1.34 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 10.43 & 14.44 & $+$4.01 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Depth pruning; removes entire layers.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01VNzsgbcVYJiqsU7ibFPKk6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "7d13c937-6a02-41df-9f72-483317eee0da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 24 · 2026-05-23T10:47:23.419Z_

<details><summary>↩ Tool result · `toolu_01VNzsgbcVYJiqsU7ibFPKk6`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\begin{tabular}{@{}lcccc@{}}
7	\toprule
8	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
9	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
10	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
11	\midrule
12	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
13	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
14	\rasp{} ($\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\
15	Random & 0.190 & -- & -- & -- \\
16	\bottomrule
17	\end{tabular}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "0e7aee2e-9fe7-47d8-b050-03849219a47d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale validation at 20\\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\\ Table~\\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}\n\\label{tab:cross_scale}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\multirow{2}{*}{Method} & \\multicolumn{2}{c}{7B} & \\multicolumn{2}{c}{1.5B} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Peak Rew. & GSM8K\\,(\\%) & Rew. & GSM8K\\,(\\%) \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{64.39} & \\textbf{0.238} & \\textbf{35.48} \\\\\nStandard & 0.081 & 59.84 & 0.084 & 22.29 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\\\\nRandom & 0.190 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_011Y8Uwono6bxqqbS8SvUReT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "efab2ace-2e87-4b3d-b47f-7f5de1720857",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 26 · 2026-05-23T10:47:24.362Z_

<details><summary>↩ Tool result · `toolu_011Y8Uwono6bxqqbS8SvUReT`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{CKA scoring stability across calibration sizes. Spearman $\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\rho \geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}
5	\label{tab:cka_stability}
6	\begin{tabular}{@{}lcc@{}}
7	\toprule
8	Calibration Sizes & Spearman $\rho$ (min) & Spearman $\rho$ (mean) \\
9	\midrule
10	256 / 512 / 1024 & 0.964 & 0.979 \\
11	\bottomrule
12	\end{tabular}
13	\end{table}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "c785f3dd-6d8b-48fa-8427-8759850d532b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{CKA scoring stability across calibration sizes. Spearman $\\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\\rho \\geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}\n\\label{tab:cka_stability}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nCalibration Sizes & Spearman $\\rho$ (min) & Spearman $\\rho$ (mean) \\\\\n\\midrule\n256 / 512 / 1024 & 0.964 & 0.979 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01846hYg4Xp7aLneCBqsQhos`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "86f94c6e-732d-46ce-86dd-823eb14491bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 28 · 2026-05-23T10:47:24.839Z_

<details><summary>↩ Tool result · `toolu_01846hYg4Xp7aLneCBqsQhos`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.
27	Stage~2 (GRPO): Group Relative Policy Optimization~\citep{shao2024grpo} with learning rate $1{\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.
28	All methods share identical GRPO hyperparameters, including \texttt{reward\_desert\_patience}{$=$}50.
29	Seeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.
30	We repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\ref{tab:decoupling}).
31	CKA-only achieves 64.39\% $\pm$ 0.19\,pp (std across seeds), Standard 59.84\% $\pm$ 0.38\,pp; the 4.55\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\% CI for mean difference: $[3.62, 5.47]$\,pp), confirming that recovery capacity differences are structural rather than stochastic.
32	All experiments run on 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.
33	
34	
35	\subsection{Recovery Capacity Spectrum}
36	\label{sec:recovery_gradient}
37	
38	\input{tables/tab1_recovery_gradient}
39	
40	\begin{figure}[t]
41	    \centering
42	    \includegraphics[width=\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}
43	    \caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}
44	    \label{fig:reward_trajectories}
45	\end{figure}
46	
47	Under identical GRPO hyperparameters, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\gg$ Random $\gg$ Standard $>$ \rasp{} (Table~\ref{tab:recovery_gradient}, Figure~\ref{fig:reward_trajectories}).
48	The pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.
49	
50	\begin{figure}[t]
51	    \centering
52	    \includegraphics[width=\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}
53	    \caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \rasp{} gradient norms remain predominantly near zero.}
54	    \label{fig:collapse_dynamics}
55	\end{figure}
56	
57	CKA-only pruning is the only method that produces active learning under GRPO.
58	Reward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.
59	Random pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.
60	
61	Standard pruning exhibits borderline collapse (Figure~\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \geq 0.500$ throughout, meaning more than half of batches produce no learning signal.
62	\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\%.
63	
64	The 5.8$\times$ peak reward gap between CKA-only (0.354) and \rasp{} (0.061) arises entirely from which structures were removed; parameter budgets and GRPO configurations are identical.
65	
66	
67	\subsection{Reward-Accuracy Decoupling}
68	\label{sec:decoupling}
69	
70	\input{tables/tab2_decoupling}
71	
72	Despite the 4.4$\times$ peak reward gap, GRPO barely moves accuracy: all fine-grained methods at 20\% sparsity change by $|\Delta| < 1$\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \rasp{} $-$0.61\,pp; Table~\ref{tab:decoupling}).
73	We term this \emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.
74	At 20\% sparsity, the four fine-grained criteria show mean $|\Delta| {=} 0.54$\,pp (max $0.61$\,pp); across the full $\alpha$ dose-response spectrum, $|\Delta|$ remains below $1.14$\,pp.
75	
76	The degree of decoupling varies with sparsity.
77	At 15\%, GRPO slightly amplifies the CKA-only advantage: the SFT gap of 5.69\,pp (72.18\% vs 66.49\%) widens to 7.20\,pp under GRPO (72.76\% vs 65.56\%).
78	At 20\%, GRPO adds nothing: the SFT gap of 4.62\,pp is preserved almost exactly (4.55\,pp).
79	The most extreme case is 25\%, where Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\,pp (Appendix~\ref{sec:appendix_cross_sparsity}).
80	Across all four fine-grained criteria at 20\% and 25\%, $|\Delta| < 1$\,pp without exception on GSM8K (Tables~\ref{tab:decoupling},~\ref{tab:cross_sparsity}); dose-response $\alpha$ variations show slightly larger but still small differences (max $1.14$\,pp at $\alpha{=}2.0$; Table~\ref{tab:alpha}).
81	On MATH-500, differences remain within statistical noise ($|\Delta| < 2.5$\,pp with stderr ${\approx}$2\,pp; Appendix~\ref{sec:appendix_math500}).
82	Moderate structural damage (15\%) apparently preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\%) exceeds the threshold where GRPO can improve upon SFT baselines.
83	
84	These results are robust: CKA-only GRPO accuracy varies by only 0.36\,pp across three seeds (64.22--64.58\%; Appendix~\ref{sec:appendix_multiseed}), and extending training to 300 steps leaves accuracy unchanged (CKA-only 64.37\%$\to$64.37\%, Standard 59.44\%$\to$59.29\%).
85	The ranking and decoupling generalize beyond GSM8K: on MATH-500~\citep{hendrycks2021math}, CKA-only ranks highest and Random lowest in SFT accuracy (26.8\% vs 14.4\%), though middle-ranked methods swap positions (Standard 25.8\% $>$ \rasp{} 21.2\%; Appendix~\ref{sec:appendix_math500}), and on MBPP~\citep{austin2021mbpp} all fine-grained GRPO $|\Delta| < 2$\,pp (Appendix~\ref{sec:appendix_mbpp}).
86	\label{sec:ood}
87	ShortGPT~\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\,pp on GSM8K, $+$4.01\,pp on MBPP; Tables~\ref{tab:decoupling},~\ref{tab:mbpp}), unlike the uniformly small deltas of fine-grained methods ($|\Delta| \leq 1.34$\,pp, with the cross-benchmark maximum from MBPP).
88	
89	
90	\subsection{Additional Results}
91	\label{sec:additional_results}
92	
93	\paragraph{Post-SFT accuracy does not predict GRPO outcome.}
94	\label{sec:sft_gradient}
95	Under SFT alone, CKA-only (63.91\%) $>$ \rasp{} (61.49\%) $>$ Standard (59.29\%) $>$ Random (51.25\%), yet under GRPO the \rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).
96	More strikingly, ShortGPT post-SFT (44.73\%) shows GRPO actively harming accuracy ($-$1.36\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\%) with GRPO accuracy 87.64\% ($\Delta{=}{-}0.23$\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\% dense retention).
97	Post-SFT accuracy does not predict GRPO recovery outcome: the spectrum is driven by structural properties of the pruned architecture.
98	
99	\paragraph{Sparsity limits and dose-response.}
100	\label{sec:sparsity_cliff}
101	All methods collapse at 30\% sparsity, validating 20\% as the operating point (Appendix~\ref{sec:appendix_sparsity_cliff}).
102	Pruning reduces parameters by 19\% and memory by ${\sim}$28\% (Appendix~\ref{sec:appendix_inference}).
103	On GSM8K, the CKA coefficient $\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\{0.5, 1.0, 2.0, 3.0, 4.0\}$, peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%) with $|\Delta| \leq 1.14$\,pp at every point; $\alpha{=}1.0$ collapses (peak reward 0.061) while $\alpha{=}4.0$ recovers to 62.77\% (Appendix~\ref{sec:appendix_alpha}).
104	
105	
106	\subsection{Extended Analysis}
107	\label{sec:extended_analysis}
108	
109	\begin{figure}[t]
110	    \centering
111	    \includegraphics[width=\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}
112	    \caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\mu{=}0.62$) yet recovers best; Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) preserve dense fidelity but collapse under RL.}
113	    \label{fig:cka_heatmap}
114	\end{figure}
115	
116	\input{tables/tab5_cross_scale}
117	
118	\paragraph{Representational diversity.}
119	CKA similarity between dense and pruned representations (Figure~\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\mu{=}0.62$), while Standard ($\mu{=}0.90$), Random ($\mu{=}0.92$), and \rasp{} ($\mu{=}0.88$) cluster near 1.0.
120	Preserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.
121	CKA-only concentrates pruning in early layers (L0--9, 72.5\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\ref{sec:appendix_overlap}).
122	Gradient flow analysis corroborates this: CKA-only models exhibit 2.89$\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.
123	
124	\paragraph{Extended training cannot rescue collapse.}
125	Extending GRPO from 100 to 300 steps (Figure~\ref{fig:extended_training}, Appendix~\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.
126	
127	\paragraph{Cross-scale and cross-architecture generalization.}
128	On DeepSeek-R1-Distill-Qwen-1.5B at 20\% sparsity (Table~\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\% $\gg$ \rasp{} 26.16\% $>$ Standard 22.29\%), with reward-accuracy decoupling confirmed at this scale ($|\Delta| < 1$\,pp: CKA-only $-$0.15, Standard $-$0.61\,pp).
129	On Qwen2.5-Math-7B at 20\% sparsity (Table~\ref{tab:cross_arch}, Appendix~\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\% vs Standard's 18.5\%) yet SFT recovers it to 51.50\% $\pm$ 3.53 while Standard remains at 21.00\% $\pm$ 2.88 ($N{=}200$), confirming that recoverability depends on preserved structure, not starting accuracy. GRPO validation on this architecture is left to future work.
130	
131	
132	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "56f612af-cc09-48a2-8cb4-7e759e9b1133",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Base model and evaluation.}\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\\citep{qwen2.5} with GQA~\\citep{ainslie2023gqa} (architecture details in Section~\\ref{sec:prelim}).\nOur primary benchmark is GSM8K~\\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.\nWe report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.\nFor rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).\nThe original unpruned model achieves 90.83\\% on GSM8K (greedy decoding).\n\n\\paragraph{Pruning methods.}\nWe compare four pruning criteria at 20\\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\\sim}$1.45B parameters) with identical per-layer capacity floors (${\\ge}$40\\% retention per layer):\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.\n    \\item \\textbf{Random}: uniform random selection among eligible groups.\n    \\item \\textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\\citep{llmpruner2023}.\n    \\item \\textbf{\\rasp{}} ($\\alpha{=}1.0$): the composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ (Eq.~\\ref{eq:score}), removing structures that are both low-importance and functionally redundant.\n\\end{enumerate}\n\n\\paragraph{Recovery pipeline and hardware.}\nAll four methods undergo matched two-stage recovery.\nStage~1 (SFT warmup): 2 epochs on 7{,}473 GSM8K chain-of-thought examples with teacher forcing (37 minutes), restoring EOS generation and basic format compliance.\nStage~2 (GRPO): Group Relative Policy Optimization~\\citep{shao2024grpo} with learning rate $1{\\times}10^{-6}$, maximum completion length 1{,}024 tokens, KL penalty coefficient $\\beta{=}0.01$, sampling temperature 0.4, DAPO-style clipped loss, and binary reward ($r{=}1$ if correct, $r{=}0$ otherwise), trained for 100 steps on 1{,}000 GSM8K training problems.\nAll methods share identical GRPO hyperparameters, including \\texttt{reward\\_desert\\_patience}{$=$}50.\nSeeds vary at the GRPO stage; pruning calibration and SFT use identical configurations across all methods.\nWe repeat GRPO training with 3 random seeds for CKA-only, Standard, and Random (Table~\\ref{tab:decoupling}).\nCKA-only achieves 64.39\\% $\\pm$ 0.19\\,pp (std across seeds), Standard 59.84\\% $\\pm$ 0.38\\,pp; the 4.55\\,pp gap is robust across seeds (Welch's $t$-test, $p{=}0.0009$, Cohen's $d{=}11.1$; 95\\% CI for mean difference: $[3.62, 5.47]$\\,pp), confirming that recovery capacity differences are structural rather than stochastic.\nAll experiments run on 2$\\times$ NVIDIA RTX PRO 6000 GPUs (94\\,GB VRAM each); pruning variants are trained in parallel on separate GPUs under identical wall-clock conditions.\n\n\n\\subsection{Recovery Capacity Spectrum}\n\\label{sec:recovery_gradient}\n\n\\input{tables/tab1_recovery_gradient}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig2_reward_trajectories.pdf}\n    \\caption{GRPO reward trajectories for four pruning criteria and the unpruned model under identical training configuration ($\\beta{=}0.01$, $T{=}0.4$, 100 steps). CKA-only reaches 0.354 peak reward with an observed recovery event at step 90. Random oscillates between 0.14 and 0.19 (training timed out at step 97; 9 steps shown). Standard peaks at 0.081 before borderline collapse. \\rasp{} peaks at 0.061 (step 50) and declines to 0.010 by step 100.}\n    \\label{fig:reward_trajectories}\n\\end{figure}\n\nUnder identical GRPO hyperparameters, the four pruning criteria produce a clear recovery capacity spectrum: CKA-only $\\gg$ Random $\\gg$ Standard $>$ \\rasp{} (Table~\\ref{tab:recovery_gradient}, Figure~\\ref{fig:reward_trajectories}).\nThe pruning criterion, not training configuration, determines whether the model learns, stagnates, or collapses.\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig3_collapse_dynamics.pdf}\n    \\caption{Training dynamics diagnostics. (a)~$f_0$ (fraction of zero-variance batches): CKA-only stays below 0.35; Standard and \\rasp{} remain in the collapse zone ($f_0 > 0.5$) throughout training. (b)~Gradient norm: Standard exhibits a transient minimum of 0.017 at step 90 before recovering to 2.41 at step 100; \\rasp{} gradient norms remain predominantly near zero.}\n    \\label{fig:collapse_dynamics}\n\\end{figure}\n\nCKA-only pruning is the only method that produces active learning under GRPO.\nReward reaches a peak of 0.354 (mean 0.285) with $f_0$ as low as 0.125, including a recovery event at step 90 where reward rebounds from a transient perturbation.\nRandom pruning produces stagnation: reward oscillates between 0.142 and 0.190 with $f_0$ near 0.33.\n\nStandard pruning exhibits borderline collapse (Figure~\\ref{fig:collapse_dynamics}): reward peaks at 0.081 (step 40) then oscillates near 0.05, with $f_0 \\geq 0.500$ throughout, meaning more than half of batches produce no learning signal.\n\\rasp{} produces full collapse: reward peaks at 0.061 (step 50) then declines to 0.010 by step 100, with $f_0 > 0.675$ and clipped ratio $>$ 90\\%.\n\nThe 5.8$\\times$ peak reward gap between CKA-only (0.354) and \\rasp{} (0.061) arises entirely from which structures were removed; parameter budgets and GRPO configurations are identical.\n\n\n\\subsection{Reward-Accuracy Decoupling}\n\\label{sec:decoupling}\n\n\\input{tables/tab2_decoupling}\n\nDespite the 4.4$\\times$ peak reward gap, GRPO barely moves accuracy: all fine-grained methods at 20\\% sparsity change by $|\\Delta| < 1$\\,pp (CKA-only $+$0.48, Standard $+$0.55, Random $-$0.53, \\rasp{} $-$0.61\\,pp; Table~\\ref{tab:decoupling}).\nWe term this \\emph{reward-accuracy decoupling}: reward trajectory reflects the model's capacity to learn from RL signal, not downstream accuracy.\nAt 20\\% sparsity, the four fine-grained criteria show mean $|\\Delta| {=} 0.54$\\,pp (max $0.61$\\,pp); across the full $\\alpha$ dose-response spectrum, $|\\Delta|$ remains below $1.14$\\,pp.\n\nThe degree of decoupling varies with sparsity.\nAt 15\\%, GRPO slightly amplifies the CKA-only advantage: the SFT gap of 5.69\\,pp (72.18\\% vs 66.49\\%) widens to 7.20\\,pp under GRPO (72.76\\% vs 65.56\\%).\nAt 20\\%, GRPO adds nothing: the SFT gap of 4.62\\,pp is preserved almost exactly (4.55\\,pp).\nThe most extreme case is 25\\%, where Standard's peak reward collapses to 0.008 yet accuracy still changes by only $+$0.99\\,pp (Appendix~\\ref{sec:appendix_cross_sparsity}).\nAcross all four fine-grained criteria at 20\\% and 25\\%, $|\\Delta| < 1$\\,pp without exception on GSM8K (Tables~\\ref{tab:decoupling},~\\ref{tab:cross_sparsity}); dose-response $\\alpha$ variations show slightly larger but still small differences (max $1.14$\\,pp at $\\alpha{=}2.0$; Table~\\ref{tab:alpha}).\nOn MATH-500, differences remain within statistical noise ($|\\Delta| < 2.5$\\,pp with stderr ${\\approx}$2\\,pp; Appendix~\\ref{sec:appendix_math500}).\nModerate structural damage (15\\%) apparently preserves enough capacity for GRPO to differentially benefit CKA-only pruning, while more aggressive pruning (20--25\\%) exceeds the threshold where GRPO can improve upon SFT baselines.\n\nThese results are robust: CKA-only GRPO accuracy varies by only 0.36\\,pp across three seeds (64.22--64.58\\%; Appendix~\\ref{sec:appendix_multiseed}), and extending training to 300 steps leaves accuracy unchanged (CKA-only 64.37\\%$\\to$64.37\\%, Standard 59.44\\%$\\to$59.29\\%).\nThe ranking and decoupling generalize beyond GSM8K: on MATH-500~\\citep{hendrycks2021math}, CKA-only ranks highest and Random lowest in SFT accuracy (26.8\\% vs 14.4\\%), though middle-ranked methods swap positions (Standard 25.8\\% $>$ \\rasp{} 21.2\\%; Appendix~\\ref{sec:appendix_math500}), and on MBPP~\\citep{austin2021mbpp} all fine-grained GRPO $|\\Delta| < 2$\\,pp (Appendix~\\ref{sec:appendix_mbpp}).\n\\label{sec:ood}\nShortGPT~\\citep{shortgpt2024} depth pruning is the sole exception: its GRPO delta is task-dependent ($-$1.36\\,pp on GSM8K, $+$4.01\\,pp on MBPP; Tables~\\ref{tab:decoupling},~\\ref{tab:mbpp}), unlike the uniformly small deltas of fine-grained methods ($|\\Delta| \\leq 1.34$\\,pp, with the cross-benchmark maximum from MBPP).\n\n\n\\subsection{Additional Results}\n\\label{sec:additional_results}\n\n\\paragraph{Post-SFT accuracy does not predict GRPO outcome.}\n\\label{sec:sft_gradient}\nUnder SFT alone, CKA-only (63.91\\%) $>$ \\rasp{} (61.49\\%) $>$ Standard (59.29\\%) $>$ Random (51.25\\%), yet under GRPO the \\rasp{}/Standard ordering reverses (peak 0.081 vs 0.061) and Random outperforms both in peak reward (0.190).\nMore strikingly, ShortGPT post-SFT (44.73\\%) shows GRPO actively harming accuracy ($-$1.36\\,pp), while unstructured pruning achieves the highest post-SFT accuracy (87.87\\%) with GRPO accuracy 87.64\\% ($\\Delta{=}{-}0.23$\\,pp), confirming that pruning criteria are irrelevant when structural damage is minimal (96.5\\% dense retention).\nPost-SFT accuracy does not predict GRPO recovery outcome: the spectrum is driven by structural properties of the pruned architecture.\n\n\\paragraph{Sparsity limits and dose-response.}\n\\label{sec:sparsity_cliff}\nAll methods collapse at 30\\% sparsity, validating 20\\% as the operating point (Appendix~\\ref{sec:appendix_sparsity_cliff}).\nPruning reduces parameters by 19\\% and memory by ${\\sim}$28\\% (Appendix~\\ref{sec:appendix_inference}).\nOn GSM8K, the CKA coefficient $\\alpha$ exhibits an inverted-U pattern in recovery accuracy across $\\{0.5, 1.0, 2.0, 3.0, 4.0\\}$, peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%) with $|\\Delta| \\leq 1.14$\\,pp at every point; $\\alpha{=}1.0$ collapses (peak reward 0.061) while $\\alpha{=}4.0$ recovers to 62.77\\% (Appendix~\\ref{sec:appendix_alpha}).\n\n\n\\subsection{Extended Analysis}\n\\label{sec:extended_analysis}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=\\columnwidth]{figures/paper/fig4_cka_heatmap.pdf}\n    \\caption{Layer-wise CKA similarity between dense and pruned representations (28 layers). CKA-only diverges most from dense ($\\mu{=}0.62$) yet recovers best; Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) preserve dense fidelity but collapse under RL.}\n    \\label{fig:cka_heatmap}\n\\end{figure}\n\n\\input{tables/tab5_cross_scale}\n\n\\paragraph{Representational diversity.}\nCKA similarity between dense and pruned representations (Figure~\\ref{fig:cka_heatmap}) shows CKA-only diverges most from the dense model ($\\mu{=}0.62$), while Standard ($\\mu{=}0.90$), Random ($\\mu{=}0.92$), and \\rasp{} ($\\mu{=}0.88$) cluster near 1.0.\nPreserving dense fidelity through gradient importance appears to retain redundant representations at the expense of the diversity that GRPO exploration requires.\nCKA-only concentrates pruning in early layers (L0--9, 72.5\\% of removed groups) while Standard prunes uniformly, removing late-layer structures that are representationally unique (Appendix~\\ref{sec:appendix_overlap}).\nGradient flow analysis corroborates this: CKA-only models exhibit 2.89$\\times$ mean gradient magnitude versus Standard across 55/56 layer groups ($p{<}0.05$, Wilcoxon; Appendix~\\ref{sec:appendix_gradient}), consistent with diversity preservation enabling stronger RL training signals.\n\n\\paragraph{Extended training cannot rescue collapse.}\nExtending GRPO from 100 to 300 steps (Figure~\\ref{fig:extended_training}, Appendix~\\ref{sec:appendix_extended}), Standard shows zero net improvement (reward 0.054--0.058, $f_0 > 0.5$ throughout), while CKA-only sustains a 5.5$\\times$ gap (0.308 vs 0.056 at step 300). The gap is structural, not a matter of training budget.\n\n\\paragraph{Cross-scale and cross-architecture generalization.}\nOn DeepSeek-R1-Distill-Qwen-1.5B at 20\\% sparsity (Table~\\ref{tab:cross_scale}), the three-method ordering is preserved (CKA-only 35.48\\% $\\gg$ \\rasp{} 26.16\\% $>$ Standard 22.29\\%), with reward-accuracy decoupling confirmed at this scale ($|\\Delta| < 1$\\,pp: CKA-only $-$0.15, Standard $-$0.61\\,pp).\nOn Qwen2.5-Math-7B at 20\\% sparsity (Table~\\ref{tab:cross_arch}, Appendix~\\ref{sec:appendix_cross_arch}), CKA-only causes near-total initial damage (1.0\\% vs Standard's 18.5\\%) yet SFT recovers it to 51.50\\% $\\pm$ 3.53 while Standard remains at 21.00\\% $\\pm$ 2.88 ($N{=}200$), confirming that recoverability depends on preserved structure, not starting accuracy. GRPO validation on this architecture is left to future work.\n\n\n",
      "numLines": 132,
      "startLine": 1,
      "totalLines": 132
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_017Htxet1j85hTfHSE476Cks`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "23648e42-2971-44bb-82a2-bff6fdc66486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 30 · 2026-05-23T10:47:25.789Z_

<details><summary>↩ Tool result · `toolu_017Htxet1j85hTfHSE476Cks`</summary>

```text
1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}
8	\label{tab:hyperparams}
9	\begin{tabular}{@{}lll@{}}
10	\toprule
11	Parameter & SFT & GRPO \\
12	\midrule
13	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
14	Batch size & 1 & 1 \\
15	Gradient accumulation & 8 & 1 \\
16	Max sequence length & 2{,}048 & -- \\
17	Max new tokens & -- & 1{,}024 \\
18	Optimizer & AdamW & AdamW \\
19	Epochs / Steps & 2 epochs & 100 steps \\
20	KL coefficient $\beta$ & -- & 0.01 \\
21	Sampling temperature & -- & 0.4 \\
22	Num generations per prompt & -- & 8 \\
23	Reward & -- & Binary (exact match) \\
24	Loss formulation & Cross-entropy & DAPO-style clipped \\
25	\texttt{reward\_desert\_patience} & -- & 50 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	\section{Algorithm}
31	\label{sec:appendix_algo}
32	
33	\begin{algorithm}[h]
34	\caption{Controlled Pruning Comparison Framework}
35	\label{alg:rasp}
36	\begin{algorithmic}[1]
37	\Require Model $\mathcal{M}$, calibration data $\mathcal{D}_\text{cal}$, target sparsity $s$, scoring criterion $\mathcal{C} \in \{\text{Std}, \text{RASP}, \text{CKA}, \text{Rand}\}$, layer floor $\tau$
38	\Ensure Pruned and recovered model $\mathcal{M}'$
39	\Statex \textit{\% Stage 1: Shared Structural Analysis}
40	\For{each structure $h \in \mathcal{H}$}
41	    \State Compute importance $I(h)$ via Eq.~\eqref{eq:importance}
42	    \State Collect activations $\mathbf{X}_h$ on $\mathcal{D}_\text{cal}$
43	\EndFor
44	\For{each layer $\ell = 1, \ldots, L$}
45	    \For{each structure $h_i$ in layer $\ell$}
46	        \State $F(h_i) \gets \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$
47	    \EndFor
48	\EndFor
49	\Statex \textit{\% Stage 2: Criterion-Specific Scoring}
50	\For{each structure $h \in \mathcal{H}$}
51	    \State $S(h) \gets \mathcal{C}(I(h), F(h))$ \hfill $\triangleright$ Eq.~\ref{eq:standard}, \ref{eq:score}, \ref{eq:cka_only}, or random
52	\EndFor
53	\State Sort $\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\tau$
54	\Statex \textit{\% Stage 3: Identical Two-Stage Recovery}
55	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
56	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ recover reasoning
57	\State \Return $\mathcal{M}'$
58	\end{algorithmic}
59	\end{algorithm}
60	
61	\section{Inference Efficiency}
62	\label{sec:appendix_inference}
63	
64	\begin{table}[h]
65	\centering
66	\small
67	\caption{Inference characteristics at 20\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\% and memory by ${\sim}$28\%, with TTFT improving 18\%. Per-token throughput decreases 19\% (0.81$\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}
68	\label{tab:inference}
69	\begin{tabular}{@{}lcccc@{}}
70	\toprule
71	Configuration & TPS\,(tok/s) & TTFT\,(ms) & Per-token\,(ms) & Params\,(B) \\
72	\midrule
73	Dense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\
74	CKA-only 20\% & 58.3 & 16.4 & 16.7 & 6.16 \\
75	Standard 20\% & 58.2 & 16.4 & 16.7 & 6.16 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	All pruned models achieve ${\sim}$28\% memory reduction from structural parameter removal.
81	TTFT (time to first token) improves by 18\% (20.1$\to$16.4\,ms), reflecting faster prefill with fewer parameters.
82	Per-token throughput decreases by 19\% (72.0$\to$58.3 tok/s, or 13.9$\to$16.7\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.
83	CKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.
84	
85	\section{CKA Coefficient $\alpha$ Ablation}
86	\label{sec:appendix_alpha}
87	
88	\input{tables/table3_alpha}
89	
90	On GSM8K, the dose-response curve across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U pattern peaking at $\alpha{=}2.0$ (SFT 64.97\%, GRPO 66.11\%, $\Delta{=}{+}1.14$\,pp; Table~\ref{tab:alpha}).
91	At $\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\%, GRPO 61.18\%).
92	At $\alpha{=}1.0$ (\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\%, $\Delta{=}{-}0.61$\,pp).
93	$\alpha{=}3.0$ (SFT 64.14\%, GRPO 63.46\%, $\Delta{=}{-}0.68$\,pp) excludes a plateau hypothesis: accuracy drops 2.65\,pp from the $\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.
94	At $\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\% GRPO accuracy (SFT 61.94\%, $\Delta{=}{+}0.83$\,pp) with active GRPO learning (reward 0.146$\to$0.256$\to$0.198).
95	Reward-accuracy decoupling holds at every $\alpha$ value: $|\Delta| \leq 1.14$\,pp across all five points.
96	
97	\section{Extended Training Dynamics}
98	\label{sec:appendix_extended}
99	
100	\begin{figure}[h]
101	    \centering
102	    \includegraphics[width=0.85\columnwidth]{figures/paper/fig5_extended_training.pdf}
103	    \caption{Extended GRPO training (300 steps, 3$\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}
104	    \label{fig:extended_training}
105	\end{figure}
106	
107	\section{MATH-500 Out-of-Distribution Evaluation}
108	\label{sec:appendix_math500}
109	
110	\input{tables/tab_math500}
111	
112	The method ordering CKA-only (26.8\%) $>$ Standard (25.8\%) $>$ \rasp{} (21.2\%) $>$ Random (14.4\%) on MATH-500 SFT is preserved from GSM8K (64.39\% $>$ 59.84\% $>$ 60.88\% $>$ 50.72\%), confirming that the recovery capacity spectrum generalizes across benchmarks.
113	The $\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\sim}$8\,pp across $\alpha$ values, but with stderr ${\approx}$2\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.
114	The inverted-U pattern is validated on GSM8K (Table~\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.
115	
116	\section{MBPP Code Generation}
117	\label{sec:appendix_mbpp}
118	
119	\input{tables/tab_mbpp}
120	
121	MBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\approx}1.7$\,pp).
122	This directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.
123	
124	\section{CKA Scoring Stability}
125	\label{sec:appendix_cka_stability}
126	
127	\input{tables/tab_cka_stability}
128	
129	CKA-based structure rankings are highly stable across calibration data volumes: Spearman $\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.
130	
131	\section{Gradient Signal Analysis}
132	\label{sec:appendix_gradient}
133	
134	We compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}
140	\label{tab:gradient_flow}
141	\begin{tabular}{@{}lcc@{}}
142	\toprule
143	Comparison & Gradient Ratio & Sig.\ Layers \\
144	\midrule
145	CKA-only vs Standard & 2.89$\times$ & 55\,/\,56 \\
146	CKA-only vs \rasp{} & 2.26$\times$ & 56\,/\,56 \\
147	\rasp{} vs Standard & 1.28$\times$ & 45\,/\,56 \\
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	The gradient magnitude hierarchy (CKA-only $\gg$ \rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\% $>$ 60.88\% $>$ 59.84\%), with bootstrap 95\% CIs for all ratios excluding 1.0.
153	This is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.
154	
155	\section{Seed Reproducibility}
156	\label{sec:appendix_seed}
157	
158	CKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\% (seed 42), 64.22\% (seed 123), 64.58\% (seed 456), yielding mean 64.39\% $\pm$ 0.19\,pp.
159	Standard: mean 59.84\% $\pm$ 0.38\,pp across the same 3 seeds.
160	See Table~\ref{tab:multiseed} for the full summary.
161	
162	\section{Sparsity Cliff at 30\%}
163	\label{sec:appendix_sparsity_cliff}
164	
165	\input{tables/table4_sparsity_cliff}
166	
167	All tested methods collapse at 30\% sparsity: Standard retains 4\% accuracy, \rasp{} and CKA-only reach 0\%.
168	This capacity threshold, independent of pruning criterion, validates 20\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.
169	
170	\section{Multi-Seed GRPO Results}
171	\label{sec:appendix_multiseed}
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}
177	\label{tab:multiseed}
178	\begin{tabular}{@{}llccc@{}}
179	\toprule
180	Sparsity & Method & Mean Acc.\,(\%) & Std\,(pp) & Seeds \\
181	\midrule
182	\multirow{4}{*}{20\%} & CKA-only & 64.39 & 0.19 & 3 \\
183	 & Standard & 59.84 & 0.38 & 3 \\
184	 & \rasp{} & 60.88 & -- & 1 \\
185	 & Random & 50.72 & 0.15 & 3 \\
186	\midrule
187	\multirow{2}{*}{15\%} & CKA-only & 72.76 & 0.57 & 3 \\
188	 & Standard & 65.56 & 0.50 & 3 \\
189	\bottomrule
190	\end{tabular}
191	\end{table}
192	
193	At 20\% sparsity, the 4.55\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\%, Standard: 59.44--60.20\%).
194	Standard shows a wider observed range across seeds (0.76\,pp vs 0.36\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.
195	Random (3 seeds: 50.57\%, 50.72\%, 50.87\%; $\sigma{=}0.15$\,pp, observed range 0.30\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\%.
196	All three seeds satisfy GRPO $\leq$ SFT ($\Delta{=}{-}0.68$, $-$0.53, $-$0.38\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.
197	Note: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\% vs.\ 59.29\% for seeds 123/456; $\Delta = 0.08$\,pp).
198	At 15\% sparsity, the gap widens to 7.20\,pp (72.76\% vs 65.56\%, $t{\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\%, Standard: 65.13--65.43\%).
199	
200	\section{Cross-Sparsity Validation}
201	\label{sec:appendix_cross_sparsity}
202	
203	\begin{table}[h]
204	\centering
205	\small
206	\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\% and 20\% GRPO values are mean over 3 seeds (see Tables~\ref{tab:decoupling},~\ref{tab:multiseed}). $^\ddagger$Single seed. Mean $|\Delta| \leq 1$\,pp across all conditions.}
207	\label{tab:cross_sparsity}
208	\begin{tabular}{@{}llccc@{}}
209	\toprule
210	Sparsity & Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
211	\midrule
212	\multirow{2}{*}{15\%} & CKA-only & 72.18 & \textbf{72.76{\scriptsize$\pm$0.57}} & $+$0.58 \\
213	 & Standard & 66.49 & 65.56{\scriptsize$\pm$0.50} & $-$0.93 \\
214	\midrule
215	\multirow{2}{*}{20\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\
216	 & Standard & 59.29 & 59.84 & $+$0.55 \\
217	\midrule
218	\multirow{2}{*}{25\%$^\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\
219	 & Standard & 50.87 & 51.86 & $+$0.99 \\
220	\midrule
221	30\% & All & \multicolumn{3}{c}{Collapse ($\leq$4\%; Table~\ref{tab:sparsity_cliff})} \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	At 15\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\,pp (72.76\% vs 65.56\%), compared to $+$4.55\,pp at 20\%.
227	CKA-only at 15\% (72.76\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\% of original dense model performance (90.83\%).
228	At 25\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\,pp from 15\%$\to$20\%, $-$8.42\,pp from 20\%$\to$25\%), while CKA-only's decline decelerates ($-$8.27\,pp then $-$3.79\,pp).
229	Reward-accuracy decoupling is preserved ($|\Delta| \leq 1$\,pp for both methods) despite Standard's near-zero peak reward (0.008).
230	
231	\section{Cross-Architecture Validation}
232	\label{sec:appendix_cross_arch}
233	
234	\begin{table}[h]
235	\centering
236	\small
237	\caption{Cross-architecture validation on Qwen2.5-Math-7B~\citep{qwen2.5} at 20\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}
238	\label{tab:cross_arch}
239	\begin{tabular}{@{}lccc@{}}
240	\toprule
241	Method & Post-Prune\,(\%) & Post-SFT\,(\%) & EOS Rate\,(\%) \\
242	\midrule
243	CKA-only & 1.0 & \textbf{51.50 $\pm$ 3.53} & 27.0 \\
244	Standard & 18.5 & 21.00 $\pm$ 2.88 & 36.5 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	CKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\% post-prune accuracy vs Standard's 18.5\%), yet SFT recovers CKA-only to 51.50\% while Standard remains at 21.00\%.
250	This post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.
251	EOS rates remain below 40\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\footnote{Preliminary GRPO evaluation yields 48.60\% (243/500), but 83.8\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}
252	
253	\section{Structural Overlap Analysis}
254	\label{sec:appendix_overlap}
255	
256	CKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity.
257	CKA-only concentrates pruning in early layers (L0--9 account for 72.5\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).
258	Standard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).
259	
260	The methods share only partial overlap in which structures they remove.
261	65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.
262	Conversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.
263	
264	This pattern is consistent with the CKA heatmap (Figure~\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.
265	
266	\section{KL Divergence During GRPO Training}
267	\label{sec:appendix_kl}
268	
269	\begin{figure}[t]
270	    \centering
271	    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
272	    \caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}
273	    \label{fig:kl_divergence}
274	\end{figure}
275	
276	\section{Depth-First Pruning Baseline}
277	\label{sec:appendix_depth_first}
278	
279	As a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\% sparsity.
280	Both SFT (${\sim}$10\%) and GRPO (${\sim}$8\%) accuracy are near chance (early-stopped at $N{\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.
281	This baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.
282	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "e6b66703-c02e-407b-8206-43b8c2d0c7d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex",
      "content": "\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Hyperparameter details for SFT warmup and GRPO recovery stages.}\n\\label{tab:hyperparams}\n\\begin{tabular}{@{}lll@{}}\n\\toprule\nParameter & SFT & GRPO \\\\\n\\midrule\nLearning rate & $2 \\times 10^{-5}$ & $1 \\times 10^{-6}$ \\\\\nBatch size & 1 & 1 \\\\\nGradient accumulation & 8 & 1 \\\\\nMax sequence length & 2{,}048 & -- \\\\\nMax new tokens & -- & 1{,}024 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs / Steps & 2 epochs & 100 steps \\\\\nKL coefficient $\\beta$ & -- & 0.01 \\\\\nSampling temperature & -- & 0.4 \\\\\nNum generations per prompt & -- & 8 \\\\\nReward & -- & Binary (exact match) \\\\\nLoss formulation & Cross-entropy & DAPO-style clipped \\\\\n\\texttt{reward\\_desert\\_patience} & -- & 50 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Algorithm}\n\\label{sec:appendix_algo}\n\n\\begin{algorithm}[h]\n\\caption{Controlled Pruning Comparison Framework}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration data $\\mathcal{D}_\\text{cal}$, target sparsity $s$, scoring criterion $\\mathcal{C} \\in \\{\\text{Std}, \\text{RASP}, \\text{CKA}, \\text{Rand}\\}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Shared Structural Analysis}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$ on $\\mathcal{D}_\\text{cal}$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each structure $h_i$ in layer $\\ell$}\n        \\State $F(h_i) \\gets \\frac{1}{|\\mathcal{H}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{h_i}, \\mathbf{X}_{h_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Criterion-Specific Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets \\mathcal{C}(I(h), F(h))$ \\hfill $\\triangleright$ Eq.~\\ref{eq:standard}, \\ref{eq:score}, \\ref{eq:cka_only}, or random\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending; prune lowest up to $s$, subject to $\\tau$\n\\Statex \\textit{\\% Stage 3: Identical Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ recover reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\section{Inference Efficiency}\n\\label{sec:appendix_inference}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Inference characteristics at 20\\% sparsity (single-GPU, no contention). Pruning reduces parameters by 19\\% and memory by ${\\sim}$28\\%, with TTFT improving 18\\%. Per-token throughput decreases 19\\% (0.81$\\times$) due to non-uniform layer widths from full-layer removal that current GPU kernels do not optimize.}\n\\label{tab:inference}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nConfiguration & TPS\\,(tok/s) & TTFT\\,(ms) & Per-token\\,(ms) & Params\\,(B) \\\\\n\\midrule\nDense 7B & 72.0 & 20.1 & 13.9 & 7.62 \\\\\nCKA-only 20\\% & 58.3 & 16.4 & 16.7 & 6.16 \\\\\nStandard 20\\% & 58.2 & 16.4 & 16.7 & 6.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll pruned models achieve ${\\sim}$28\\% memory reduction from structural parameter removal.\nTTFT (time to first token) improves by 18\\% (20.1$\\to$16.4\\,ms), reflecting faster prefill with fewer parameters.\nPer-token throughput decreases by 19\\% (72.0$\\to$58.3 tok/s, or 13.9$\\to$16.7\\,ms per token), consistent with non-uniform layer widths creating computational bottlenecks that current GPU kernels do not optimize away.\nCKA-only and Standard show identical throughput (58.3 vs 58.2 tok/s), confirming that the pruning criterion affects recovery capacity but not inference speed at matched sparsity.\n\n\\section{CKA Coefficient $\\alpha$ Ablation}\n\\label{sec:appendix_alpha}\n\n\\input{tables/table3_alpha}\n\nOn GSM8K, the dose-response curve across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U pattern peaking at $\\alpha{=}2.0$ (SFT 64.97\\%, GRPO 66.11\\%, $\\Delta{=}{+}1.14$\\,pp; Table~\\ref{tab:alpha}).\nAt $\\alpha{=}0.5$, importance still dominates; recovery is low (SFT 60.73\\%, GRPO 61.18\\%).\nAt $\\alpha{=}1.0$ (\\rasp{}), GRPO collapses (peak reward 0.061, accuracy 60.88\\%, $\\Delta{=}{-}0.61$\\,pp).\n$\\alpha{=}3.0$ (SFT 64.14\\%, GRPO 63.46\\%, $\\Delta{=}{-}0.68$\\,pp) excludes a plateau hypothesis: accuracy drops 2.65\\,pp from the $\\alpha{=}2.0$ peak, confirming that the optimum is a true peak rather than a saturation regime.\nAt $\\alpha{=}4.0$, CKA overlap dominates; the model recovers to 62.77\\% GRPO accuracy (SFT 61.94\\%, $\\Delta{=}{+}0.83$\\,pp) with active GRPO learning (reward 0.146$\\to$0.256$\\to$0.198).\nReward-accuracy decoupling holds at every $\\alpha$ value: $|\\Delta| \\leq 1.14$\\,pp across all five points.\n\n\\section{Extended Training Dynamics}\n\\label{sec:appendix_extended}\n\n\\begin{figure}[h]\n    \\centering\n    \\includegraphics[width=0.85\\columnwidth]{figures/paper/fig5_extended_training.pdf}\n    \\caption{Extended GRPO training (300 steps, 3$\\times$ original budget). (a)~Standard reward shows zero net gain (0.054$\\to$0.056); CKA-only oscillates in the 0.22--0.44 range with a 5.5$\\times$ gap at step 300. (b)~Standard $f_0$ remains in the collapse zone ($>$0.5); CKA-only stays below 0.30.}\n    \\label{fig:extended_training}\n\\end{figure}\n\n\\section{MATH-500 Out-of-Distribution Evaluation}\n\\label{sec:appendix_math500}\n\n\\input{tables/tab_math500}\n\nThe method ordering CKA-only (26.8\\%) $>$ Standard (25.8\\%) $>$ \\rasp{} (21.2\\%) $>$ Random (14.4\\%) on MATH-500 SFT is preserved from GSM8K (64.39\\% $>$ 59.84\\% $>$ 60.88\\% $>$ 50.72\\%), confirming that the recovery capacity spectrum generalizes across benchmarks.\nThe $\\alpha$ dose-response effect is not statistically significant on MATH-500: SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values, but with stderr ${\\approx}$2\\,pp per point, attributable to high truncation rates at the 2048-token limit and floor effects at this difficulty level.\nThe inverted-U pattern is validated on GSM8K (Table~\\ref{tab:alpha}); MATH-500 does not resolve the dose-response shape.\n\n\\section{MBPP Code Generation}\n\\label{sec:appendix_mbpp}\n\n\\input{tables/tab_mbpp}\n\nMBPP GRPO deltas are uniformly slightly positive across all fine-grained methods (mean $+$1.25\\,pp), but none are statistically significant at this sample size ($N{=}374$; stderr ${\\approx}1.7$\\,pp).\nThis directional consistency may reflect a weak task-specific GRPO effect at the capability floor rather than a violation of reward-accuracy decoupling.\n\n\\section{CKA Scoring Stability}\n\\label{sec:appendix_cka_stability}\n\n\\input{tables/tab_cka_stability}\n\nCKA-based structure rankings are highly stable across calibration data volumes: Spearman $\\rho$ between rankings from 256, 512, and 1024 calibration samples ranges from 0.964 to 0.979, indicating that the scoring criterion is not sensitive to calibration set size.\n\n\\section{Gradient Signal Analysis}\n\\label{sec:appendix_gradient}\n\nWe compare per-layer gradient magnitudes during early GRPO training ($N{=}200$ GSM8K calibration samples) across three pruning criteria using paired Wilcoxon signed-rank tests.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise gradient magnitude ratios during GRPO training. Ratio: mean gradient magnitude of method A divided by method B across 56 parameter groups (28 layers $\\times$ 2 projections). Significant layers: count where paired Wilcoxon signed-rank $p{<}0.05$.}\n\\label{tab:gradient_flow}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nComparison & Gradient Ratio & Sig.\\ Layers \\\\\n\\midrule\nCKA-only vs Standard & 2.89$\\times$ & 55\\,/\\,56 \\\\\nCKA-only vs \\rasp{} & 2.26$\\times$ & 56\\,/\\,56 \\\\\n\\rasp{} vs Standard & 1.28$\\times$ & 45\\,/\\,56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient magnitude hierarchy (CKA-only $\\gg$ \\rasp{} $>$ Standard) mirrors the recovery capacity hierarchy (GSM8K: 64.39\\% $>$ 60.88\\% $>$ 59.84\\%), with bootstrap 95\\% CIs for all ratios excluding 1.0.\nThis is consistent with diversity preservation enabling stronger training signals during GRPO, though the evidence is correlational: an alternative explanation---that CKA-only retains more functional structure, producing higher initial loss and naturally larger gradients---cannot be ruled out.\n\n\\section{Seed Reproducibility}\n\\label{sec:appendix_seed}\n\nCKA-only GSM8K accuracy across 3 GRPO seeds: 64.37\\% (seed 42), 64.22\\% (seed 123), 64.58\\% (seed 456), yielding mean 64.39\\% $\\pm$ 0.19\\,pp.\nStandard: mean 59.84\\% $\\pm$ 0.38\\,pp across the same 3 seeds.\nSee Table~\\ref{tab:multiseed} for the full summary.\n\n\\section{Sparsity Cliff at 30\\%}\n\\label{sec:appendix_sparsity_cliff}\n\n\\input{tables/table4_sparsity_cliff}\n\nAll tested methods collapse at 30\\% sparsity: Standard retains 4\\% accuracy, \\rasp{} and CKA-only reach 0\\%.\nThis capacity threshold, independent of pruning criterion, validates 20\\% as the operating point and confirms that the recovery capacity spectrum reflects how methods allocate a limited pruning budget.\n\n\\section{Multi-Seed GRPO Results}\n\\label{sec:appendix_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed GRPO results on GSM8K ($N{=}1{,}319$). CKA-only, Standard, and Random each trained with 3 GRPO seeds (42, 123, 456); pruning calibration and SFT are identical across all runs within each sparsity level.}\n\\label{tab:multiseed}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & Mean Acc.\\,(\\%) & Std\\,(pp) & Seeds \\\\\n\\midrule\n\\multirow{4}{*}{20\\%} & CKA-only & 64.39 & 0.19 & 3 \\\\\n & Standard & 59.84 & 0.38 & 3 \\\\\n & \\rasp{} & 60.88 & -- & 1 \\\\\n & Random & 50.72 & 0.15 & 3 \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.76 & 0.57 & 3 \\\\\n & Standard & 65.56 & 0.50 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 20\\% sparsity, the 4.55\\,pp gap between CKA-only and Standard is robust across seeds, with non-overlapping ranges (CKA-only: 64.22--64.58\\%, Standard: 59.44--60.20\\%).\nStandard shows a wider observed range across seeds (0.76\\,pp vs 0.36\\,pp), consistent with borderline-collapse dynamics where small perturbations produce larger outcome variation.\nRandom (3 seeds: 50.57\\%, 50.72\\%, 50.87\\%; $\\sigma{=}0.15$\\,pp, observed range 0.30\\,pp) converges in a narrow band with SFT accuracy seed-independent at 51.25\\%.\nAll three seeds satisfy GRPO $\\leq$ SFT ($\\Delta{=}{-}0.68$, $-$0.53, $-$0.38\\,pp), confirming that reward-accuracy decoupling is reproducible across seeds even for stagnating methods.\nNote: Standard seed 42 was trained from a separately initialized SFT checkpoint (accuracy 59.21\\% vs.\\ 59.29\\% for seeds 123/456; $\\Delta = 0.08$\\,pp).\nAt 15\\% sparsity, the gap widens to 7.20\\,pp (72.76\\% vs 65.56\\%, $t{\\approx}16.4$, $p{<}0.001$), with non-overlapping ranges (CKA-only: 72.10--73.09\\%, Standard: 65.13--65.43\\%).\n\n\\section{Cross-Sparsity Validation}\n\\label{sec:appendix_cross_sparsity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-sparsity validation on DeepSeek-R1-Distill-Qwen-7B. GSM8K accuracy ($N{=}1{,}319$) after SFT warmup and GRPO recovery. 15\\% and 20\\% GRPO values are mean over 3 seeds (see Tables~\\ref{tab:decoupling},~\\ref{tab:multiseed}). $^\\ddagger$Single seed. Mean $|\\Delta| \\leq 1$\\,pp across all conditions.}\n\\label{tab:cross_sparsity}\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nSparsity & Method & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n\\multirow{2}{*}{15\\%} & CKA-only & 72.18 & \\textbf{72.76{\\scriptsize$\\pm$0.57}} & $+$0.58 \\\\\n & Standard & 66.49 & 65.56{\\scriptsize$\\pm$0.50} & $-$0.93 \\\\\n\\midrule\n\\multirow{2}{*}{20\\%} & CKA-only & 63.91 & 64.39 & $+$0.48 \\\\\n & Standard & 59.29 & 59.84 & $+$0.55 \\\\\n\\midrule\n\\multirow{2}{*}{25\\%$^\\ddagger$} & CKA-only & 60.12 & 59.59 & $-$0.53 \\\\\n & Standard & 50.87 & 51.86 & $+$0.99 \\\\\n\\midrule\n30\\% & All & \\multicolumn{3}{c}{Collapse ($\\leq$4\\%; Table~\\ref{tab:sparsity_cliff})} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 15\\% sparsity (3-seed mean), the CKA-only advantage widens to $+$7.20\\,pp (72.76\\% vs 65.56\\%), compared to $+$4.55\\,pp at 20\\%.\nCKA-only at 15\\% (72.76\\%) represents the highest mean accuracy across all experimental conditions, retaining 80.1\\% of original dense model performance (90.83\\%).\nAt 25\\% sparsity (single seed), Standard's SFT accuracy decline accelerates ($-$7.20\\,pp from 15\\%$\\to$20\\%, $-$8.42\\,pp from 20\\%$\\to$25\\%), while CKA-only's decline decelerates ($-$8.27\\,pp then $-$3.79\\,pp).\nReward-accuracy decoupling is preserved ($|\\Delta| \\leq 1$\\,pp for both methods) despite Standard's near-zero peak reward (0.008).\n\n\\section{Cross-Architecture Validation}\n\\label{sec:appendix_cross_arch}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture validation on Qwen2.5-Math-7B~\\citep{qwen2.5} at 20\\% structured sparsity. Accuracy evaluated on GSM8K ($N{=}200$). Post-SFT reports mean $\\pm$ std over multiple SFT runs. EOS rate: fraction of generations that produce a valid end-of-sequence token.}\n\\label{tab:cross_arch}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Post-Prune\\,(\\%) & Post-SFT\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nCKA-only & 1.0 & \\textbf{51.50 $\\pm$ 3.53} & 27.0 \\\\\nStandard & 18.5 & 21.00 $\\pm$ 2.88 & 36.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCKA-only pruning causes near-total initial damage on Qwen2.5-Math-7B (1.0\\% post-prune accuracy vs Standard's 18.5\\%), yet SFT recovers CKA-only to 51.50\\% while Standard remains at 21.00\\%.\nThis post-prune accuracy reversal provides strong evidence that recovery capacity is shaped by preserved network structure rather than starting accuracy.\nEOS rates remain below 40\\% for both methods, indicating that SFT warmup is less effective on this architecture; GRPO validation is deferred to future work.\\footnote{Preliminary GRPO evaluation yields 48.60\\% (243/500), but 83.8\\% of responses were truncated at 2048 tokens, precluding direct comparison with SFT results.}\n\n\\section{Structural Overlap Analysis}\n\\label{sec:appendix_overlap}\n\nCKA-only and Standard pruning produce markedly different removal patterns across the 28 layers of DeepSeek-R1-Distill-Qwen-7B at 20\\% sparsity.\nCKA-only concentrates pruning in early layers (L0--9 account for 72.5\\% of removed MLP groups), preserving nearly all structures in later layers (L16--27).\nStandard distributes removals more uniformly, pruning substantial numbers of groups in late layers (L16--18, L22, L25--26).\n\nThe methods share only partial overlap in which structures they remove.\n65 MLP groups are pruned exclusively by CKA-only (retained by Standard), concentrated in L6--9 and L27---structures that gradient importance scores as important but CKA identifies as redundant with neighboring groups.\nConversely, 46+ groups are pruned exclusively by Standard (retained by CKA-only), concentrated in L16--18, L22, and L25--26---structures that gradient importance scores as unimportant but CKA identifies as representationally unique.\n\nThis pattern is consistent with the CKA heatmap (Figure~\\ref{fig:cka_heatmap}): CKA-only's aggressive early-layer pruning disrupts dense representations (low diagonal CKA, $\\mu{=}0.62$) but preserves diverse late-layer pathways, while Standard's uniform pruning maintains dense fidelity ($\\mu{=}0.90$) at the cost of removing unique computational pathways in later layers.\n\n\\section{KL Divergence During GRPO Training}\n\\label{sec:appendix_kl}\n\n\\begin{figure}[t]\n    \\centering\n    \\includegraphics[width=0.75\\columnwidth]{figures/paper/fig_appendix_kl.pdf}\n    \\caption{KL divergence between the policy and reference model during GRPO training. RASP maintains near-zero KL ($<$0.001), consistent with minimal policy movement during collapse. Random shows the highest KL (${\\sim}$0.004--0.005), indicating more policy exploration. CKA-only and Standard fall between these extremes.}\n    \\label{fig:kl_divergence}\n\\end{figure}\n\n\\section{Depth-First Pruning Baseline}\n\\label{sec:appendix_depth_first}\n\nAs a sanity check, we test whether CKA-only's advantage reflects mere layer-depth bias by constructing a depth-first baseline: synthetic importance scores force removal of late layers first (L18--27: 0.001, L10--17: 0.5, L0--9: 1.0), then standard pruning at 20\\% sparsity.\nBoth SFT (${\\sim}$10\\%) and GRPO (${\\sim}$8\\%) accuracy are near chance (early-stopped at $N{\\approx}50$--88 samples due to conclusive results), confirming that naive depth ordering cannot substitute for criterion-based structure selection.\nThis baseline operates at layer-level granularity (removing entire transformer blocks), unlike CKA-only/Standard/\\rasp{} which prune at MLP channel group level; the granularity difference limits direct comparison with our main results and precludes using this baseline as evidence for the recovery capacity spectrum.\n",
      "numLines": 282,
      "startLine": 1,
      "totalLines": 282
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01AxjZhmB9JdFTPHe5DomWCo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "8d8fd384-cbd2-4d75-98bf-e40cf9e3839b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 32 · 2026-05-23T10:47:26.266Z_

<details><summary>↩ Tool result · `toolu_01AxjZhmB9JdFTPHe5DomWCo`</summary>

```text
1	Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.
2	RLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\@.
3	When pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \emph{reward-accuracy decoupling}: on GSM8K at 20\% sparsity, $|\Delta(\text{GRPO}-\text{SFT})| \leq 0.61$\,pp across all four fine-grained criteria (max $1.34$\,pp including dose-response variations and MBPP), with additional validation at 15\% and 25\%; differences on MATH-500 fall within statistical noise.
4	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$.
5	On DeepSeek-R1-Distill-Qwen-7B, a dose-response analysis across $\alpha \in \{0.5, 1.0, 2.0, 3.0, 4.0\}$ reveals an inverted-U on GSM8K, peaking at $\alpha{=}2.0$ (66.11\%).
6	Under identical GRPO training, four pruning criteria produce a \emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\times$ vs importance-only), while importance-dominated pruning collapses entirely.
7	The spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "0246c699-217b-4457-85be-0ef6ee9575e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex",
      "content": "Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or RLVR) to restore reasoning capabilities.\nRLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\\@.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \\emph{reward-accuracy decoupling}: on GSM8K at 20\\% sparsity, $|\\Delta(\\text{GRPO}-\\text{SFT})| \\leq 0.61$\\,pp across all four fine-grained criteria (max $1.34$\\,pp including dose-response variations and MBPP), with additional validation at 15\\% and 25\\%; differences on MATH-500 fall within statistical noise.\nWe propose Recovery-Aware Structured Pruning (\\rasp{}), which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$.\nOn DeepSeek-R1-Distill-Qwen-7B, a dose-response analysis across $\\alpha \\in \\{0.5, 1.0, 2.0, 3.0, 4.0\\}$ reveals an inverted-U on GSM8K, peaking at $\\alpha{=}2.0$ (66.11\\%).\nUnder identical GRPO training, four pruning criteria produce a \\emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\\times$ vs importance-only), while importance-dominated pruning collapses entirely.\nThe spectrum tracks preserved representational diversity rather than gradient importance, with initial evidence for generality across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B).\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01KJDujeXp4MTkoTCZjaSF94`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "fc3852fa-368d-4796-841a-e5881fe53162",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 34 · 2026-05-23T10:47:26.732Z_

<details><summary>↩ Tool result · `toolu_01KJDujeXp4MTkoTCZjaSF94`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations and MBPP, the maximum is $1.34$\,pp.
8	What matters is not \emph{how} you train after pruning, but \emph{which structures} you remove.
9	
10	This gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	No prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
12	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\alpha{=}2.0$ (66.11\%). SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}
18	\label{fig:dose_response}
19	\end{figure}
20	
21	We present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\citep{kornblith2019cka} via a coefficient $\alpha$ in the pruning score (Figure~\ref{fig:dose_response}).
22	The dose-response curve reveals an inverted-U: recovery peaks at $\alpha{=}2.0$ (66.11\% GRPO on GSM8K~\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.
23	Under identical GRPO~\citep{shao2024grpo} training, four criteria produce a \textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\times$ Standard), Random stagnates, Standard (importance-only;~\citealp{llmpruner2023}) exhibits borderline collapse, and $\alpha{=}1.0$ collapses fully.
24	The ordering tracks preserved representational diversity, not gradient importance.
25	A depth pruning baseline (ShortGPT;~\citealp{shortgpt2024}) is the only method with $|\Delta| > 1$\,pp ($-$1.36\,pp on GSM8K), confirming that pruning granularity interacts with RL trainability.
26	
27	Our contributions are:
28	\begin{enumerate}[nosep,leftmargin=*]
29	    \item \textbf{Reward-accuracy decoupling.} At 20--25\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\Delta| {=} 0.54$\,pp at 20\% (max $0.61$\,pp; $1.34$\,pp including dose-response variations and MBPP). At 15\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\S\ref{sec:decoupling}).
30	    \item \textbf{Recovery capacity spectrum.} We propose \rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\alpha{=}2.0$ (66.11\%). Under identical GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\S\ref{sec:scoring}, \S\ref{sec:recovery_gradient}, \S\ref{sec:extended_analysis}).
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "8c866231-1aa0-4645-b7cd-a5e3039659cb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nReasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.\nThe dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \\citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, significantly outperforming SFT.\nWe show that this hierarchy is an artifact of suboptimal pruning.\nWhen pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\\% sparsity, mean $|\\Delta(\\text{GRPO}-\\text{SFT})| {=} 0.54$\\,pp across the four fine-grained criteria (max $0.61$\\,pp); including dose-response variations and MBPP, the maximum is $1.34$\\,pp.\nWhat matters is not \\emph{how} you train after pruning, but \\emph{which structures} you remove.\n\nThis gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.\nNo prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.\nWe note that \\citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../figures/paper/fig1_dose_response.pdf}\n\\caption{Dose-response curve for the CKA diversity coefficient $\\alpha$ at 20\\% MLP channel sparsity on GSM8K ($N{=}1{,}319$). Recovery accuracy follows an inverted-U, peaking at $\\alpha{=}2.0$ (66.11\\%). SFT and GRPO curves nearly overlap ($|\\Delta| \\leq 1.14$\\,pp at every point), visually demonstrating reward-accuracy decoupling: the pruning criterion, not the recovery paradigm, determines outcome.}\n\\label{fig:dose_response}\n\\end{figure}\n\nWe present a controlled comparison on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% MLP channel sparsity, varying the balance between gradient importance and CKA-based representational diversity~\\citep{kornblith2019cka} via a coefficient $\\alpha$ in the pruning score (Figure~\\ref{fig:dose_response}).\nThe dose-response curve reveals an inverted-U: recovery peaks at $\\alpha{=}2.0$ (66.11\\% GRPO on GSM8K~\\citep{cobbe2021gsm8k}), where importance and diversity reach optimal balance.\nUnder identical GRPO~\\citep{shao2024grpo} training, four criteria produce a \\textbf{recovery capacity spectrum}: CKA-only pruning achieves active learning (peak reward 4.4$\\times$ Standard), Random stagnates, Standard (importance-only;~\\citealp{llmpruner2023}) exhibits borderline collapse, and $\\alpha{=}1.0$ collapses fully.\nThe ordering tracks preserved representational diversity, not gradient importance.\nA depth pruning baseline (ShortGPT;~\\citealp{shortgpt2024}) is the only method with $|\\Delta| > 1$\\,pp ($-$1.36\\,pp on GSM8K), confirming that pruning granularity interacts with RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Reward-accuracy decoupling.} At 20--25\\% sparsity, GRPO and SFT produce near-identical accuracy across all four fine-grained criteria: mean $|\\Delta| {=} 0.54$\\,pp at 20\\% (max $0.61$\\,pp; $1.34$\\,pp including dose-response variations and MBPP). At 15\\%, GRPO can still amplify the CKA-guided advantage ($+$1.51\\,pp differential), but this partial exception reinforces the main pattern: the pruning criterion, not the recovery paradigm, determines outcome (\\S\\ref{sec:decoupling}).\n    \\item \\textbf{Recovery capacity spectrum.} We propose \\rasp{}, which balances gradient importance with CKA-based representational diversity via a coefficient $\\alpha$. A dose-response analysis on GSM8K reveals an inverted-U peaking at $\\alpha{=}2.0$ (66.11\\%). Under identical GRPO training, four criteria produce qualitatively distinct dynamics---from active learning to full collapse---that track preserved diversity, not gradient importance. The spectrum is validated across scales (1.5B) and, via SFT-based recovery, across architectures (Qwen2.5-Math-7B) (\\S\\ref{sec:scoring}, \\S\\ref{sec:recovery_gradient}, \\S\\ref{sec:extended_analysis}).\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01ChPYFWbKVUMQQgs7Agy4XM`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 50,
  "fields": [
    "*"
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
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "3cef34a5-cc1d-4312-991b-6c3c5a83f2e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTRFjV5U2DZDnMEQV3bmJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1748,
      "cache_read_input_tokens": 25217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1748
      },
      "output_tokens": 18,
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

_source line 36 · 2026-05-23T10:47:29.041Z_

<details><summary>↩ Tool result · `toolu_01ChPYFWbKVUMQQgs7Agy4XM`</summary>

```text
Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "37c7d07b-decc-4fab-acab-630a49f85c6e",
  "tool_use_result": {
    "content": "Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"parent\": \"eval_gsm8k_grpo_alpha0p5_20\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.log\", \"completed_at\": \"2026-05-23T10:11:11.002Z\"}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ| comparison.\", \"parent\": \"eval_math500_grpo_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_cka_only_20_2048_v2.log\", \"completed_at\": \"2026-05-23T08:55:58.278Z\"}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"hypothesis\": \"GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.\", \"parent\": \"eval_gsm8k_grpo_alpha3p0_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_alpha3p0_20.log\", \"completed_at\": \"2026-05-23T07:48:50.736Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"hypothesis\": \"GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v3\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:58:52.769Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"hypothesis\": \"GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T04:41:44.783Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T04:41:56.794961+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:44:32.303Z\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"hypothesis\": \"CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishes upper bound for cross-benchmark dose-response curve.\", \"parent\": \"eval_math500_sft_cka_only_20_westb\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:00:43.009Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"hypothesis\": \"GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"reproduce\": {\"finished_at\": \"2026-05-23T03:14:21.897Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:14:37.164633+00:00\"}]}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:16:40.537Z\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"hypothesis\": \"MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 337s/sample (no token limit). Tests whether CKA-only pruning + GRPO recovery generalizes beyond DeepSeek-R1-Distill to Qwen-Math architecture.\", \"parent\": \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:53:37.071Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"hypothesis\": \"α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response curve on MATH-500.\", \"parent\": \"eval_math500_sft_rasp_alpha1p0_20\", \"notes\": \"westb submission failed: model sft_rasp_20_westd not found on westb. Only exists on westd-32935. Waiting for westd:3 (α=4.0, 85%) to free up.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T22:58:10.208Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T22:58:19.219921+00:00\"}]}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:01:03.420Z\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.\", \"parent\": \"eval_math500_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-19T08:54:35.352Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:54:40.855817+00:00\"}]}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:16.850Z\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"hypothesis\": \"α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:18:43.350Z\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"hypothesis\": \"α=3.0 SFT MATH-500 eval @2048. Dose-response \\\"下降段确认点\\\": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Completes 5/5 MATH-500 dose-response.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:12:26.406Z\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"hypothesis\": \"α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}, \"completed_at\": \"2026-05-22T21:22:35.442Z\"}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"hypothesis\": \"α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T20:12:27.595Z\"}, \"failure_reason\": \"cron false positive: process exited normally, result file confirmed by Reviewer (24.0% accuracy)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T20:12:32.633Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T20:12:40.230344+00:00\"}]}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"hypothesis\": \"MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:48:12.480Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:48:17.521Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:48:25.193120+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}, \"notes\": \"Cron 误判 (已知模式): 实验实际完成 1319/1319, acc=50.87%. 与 seed42 (50.57%) 一致, 验证 C1 decoupling. Results: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\"}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\", \"hypothesis\": \"MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。\", \"parent\": \"grpo_random_20_seed123_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 claim is robust across random seeds.\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:22:39.316Z\"}, \"failure_reason\": \"磁盘满: GRPO训练100/100完成但save_pretrained失败 (No space left on device)。westb-23072:/root/autodl-tmp 空间不足。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:22:44.289Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:22:54.301751+00:00\"}]}, \"notes\": \"失败原因: GRPO 训练 100/100 步已完成 (3h02min)，但 save_pretrained 时磁盘满 (No space left on device, os error 28)。保存路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456。W&B run auv9riek 有完整训练 metrics。save_steps=100=max_steps，无中间 checkpoint，需重跑。 | 已有成果: W&B metrics 完整 | 建议: 清理 westb-23072 磁盘后重提交\"}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\", \"hypothesis\": \"MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\", \"hypothesis\": \"MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior log recovery showed ~24.18% from nohup output.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\", \"hypothesis\": \"MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\", \"completed_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"hypothesis\": \"α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.\", \"notes\": \"UNBLOCKED: grpo_rasp_alpha3p0_20_v2 checkpoint-100 完整 (12.3GB). Eval 已启动 PID 43755 on westd:0, 2.8s/sample, ETA ~60 min.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\", \"completed_at\": \"2026-05-22T14:46:15.365Z\"}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"hypothesis\": \"Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.\", \"parent\": \"eval_math500_sft_random_20_v2\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:10:18.359Z\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"hypothesis\": \"α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T12:34:57.027Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:35:05.634Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:35:15.663664+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}, \"log_path\": \"/tmp/eval_gsm8k_sft_alpha3p0.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"notes\": \"Cron 误判。评估 1319/1319 全部完成，accuracy=64.14%。进程因写结果 JSON 时磁盘满 (OSError: No space left on device) 以非零码退出，但所有推理已完成、accuracy 已计算。结果 JSON 未写入磁盘，数据从日志提取。中间进度 ~64.15%@1300 与最终 64.14% 一致。\"}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\", \"hypothesis\": \"Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 decline).\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"hypothesis\": \"Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.\", \"parent\": \"eval_math500_grpo_standard_20_fair_2048\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:19.798Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:27.767Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:38.330160+00:00\"}]}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}, \"notes\": \"Cron 误判。实际正常完成。MATH-500 Accuracy = 0.2640 ± 0.0197 (132/500)。运行时长 ~7h11min。结果文件: /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\"}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:49.435Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:57.919Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:13:16.493425+00:00\"}]}, \"notes\": \"Cron 误判 (已知 pattern: process dead 5× with no sentinel/W&B)。实际 GRPO 训练正常完成 (19:02 CST)。模型保存: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123。WandB run: grpo_sft_random_20 (ID: 1silchcm)。日志: /tmp/mf2_random_seed123_grpo.log\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\", \"hypothesis\": \"α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harms recovery.\", \"parent\": \"grpo_alpha4_20\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:31:57.909Z\", \"notes\": \"GRPO 训练 100/100 steps 完成，但 checkpoint-100/model.safetensors 被截断（7.2GB vs 应有 11.5GB）。原因：westb 数据盘在保存时 100% 满。需要重跑 GRPO。SFT checkpoint-935 完好（11.5GB）。\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"hypothesis\": \"α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:22:49.360Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"hypothesis\": \"α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:20:50.793Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\", \"hypothesis\": \"MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priority.\", \"parent\": \"sft_qwen_math_cka_only_20_v2\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"hypothesis\": \"α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:16.837Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"hypothesis\": \"α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:13.196Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"hypothesis\": \"1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}, \"completed_at\": \"2026-05-22T07:50:22.759Z\"}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"hypothesis\": \"α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.\", \"parent\": \"eval_gsm8k_sft_alpha4_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:47:27.370Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:47:34.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:47:41.693855+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"hypothesis\": \"α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v2\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:30:52.773Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:30:50.611Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:31:04.453494+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}, \"notes\": \"Cron 误判为 failed（进程正常退出但 cron 未检测到 sentinel）。实际完成 1319/1319，accuracy=62.77%。α=4.0 GRPO > Standard GRPO (59.84%) > RASP α=1.0 GRPO (54.43%)。确认 α tuning 有效缓解 RASP collapse。checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100, log_path: /root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log, results_path: /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\"}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T02:58:40.587Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:58:45.343074+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.13, \"correct\": 65, \"n_total\": 500}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\"}}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\", \"hypothesis\": \"Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500\", \"completed_at\": \"2026-05-21T19:22:29.444Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"hypothesis\": \"α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning can mitigate collapse.\", \"parent\": \"sft_alpha4_20_v2\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T19:27:23.228Z\"}, \"sft_alpha4_20_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"hypothesis\": \"α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after full SFT→GRPO→eval pipeline.\", \"parent\": \"sft_alpha4_20_manual\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T18:54:53.481Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:54:59.708620+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"hypothesis\": \"CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data\", \"parent\": \"eval_math500_grpo_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:33:40.068Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"hypothesis\": \"CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency\", \"parent\": \"eval_math500_sft_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:29:10.900Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}, \"notes\": \"Eval completed all 500 problems. Result JSON not saved due to IsADirectoryError (output_path pointed to directory instead of file). Metrics extracted from log.\"}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"hypothesis\": \"Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:40:37.092Z\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"hypothesis\": \"CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"parent\": \"grpo_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:05:38.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:05:47.086682+00:00\"}]}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:09:25.937Z\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"hypothesis\": \"Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。\", \"parent\": \"grpo_standard_25_westb\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\", \"completed_at\": \"2026-05-21T12:37:17.579Z\"}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"hypothesis\": \"CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T10:17:58.203Z\"}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"hypothesis\": \"Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:47:06.620Z\"}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"hypothesis\": \"CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。\", \"parent\": \"grpo_cka_only_25\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"notes\": \"正确 PID=322443 (v3提交)。323174 是重复提交已 kill。\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:17:13.429Z\"}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"hypothesis\": \"Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.\", \"parent\": \"sft_standard_25\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_25.log\"}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"hypothesis\": \"Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。\", \"parent\": \"grpo_random_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\"}, \"sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"hypothesis\": \"Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:50:00.000Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_random_20.log\"}}, \"count\": 50, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9483}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I have all the tex files loaded. The registry data was too large and saved to a file. Let me use agents to parse the registry data and build the provenance table. Let me first load the TodoWrite tool and then launch an agent to parse the registry data.

Let me launch an agent to parse the registry JSON and extract the key fields I need. Meanwhile, I already have all the paper data I need from the tex files.

Let me organize what I have from the paper:

**Table 1 (tab1_recovery_gradient.tex) - Recovery Capacity Spectrum:**
- CKA-only: Peak Rew=0.354, Mean Rew=0.285, Min f0=0.125


- Random: Peak Rew=0.190, Mean Rew=0.164, Min f0=0.300
- Standard: Peak Rew=0.081, Mean Rew=0.050, Min f0=0.500
- RASP (α=1.0): Peak Rew=0.061, Mean Rew=0.031, Min f0=0.675

**Table 2 (tab2_decoupling.tex) - GRPO Responsiveness:**
- Unpruned: SFT=81.27%, GRPO=81.27%, Δ=0.00

, Peak Rew=0.669

Now I'm looking at the performance metrics when applying different pruning strategies at 20% sparsity. The CKA-only approach shows modest gains with GRPO improving by 0.48 points, while standard pruning achieves a 0.55 point improvement despite lower absolute scores. RASP and random pruning both show performance degradation, with RASP dropping 0.61 points and random dropping 0.53 points.

I'm also examining how the α hyperparameter affects the dose-response curve. The results show that α=2.0 produces the strongest improvement at +1.14 points, while α=1.0 and α=3.0 both show degradation. The pattern suggests an optimal sweet spot around α=2.0 for this particular task.

Now looking at the sparsity cliff results, RASP with α=1.0 actually performs worse than the standard approach at 30% sparsity, dropping to 0% accuracy compared to 4% for the baseline. The inference efficiency metrics are more promising though—RASP achieves a 37.8% speedup and 28.5% memory reduction at 20% sparsity, substantially outperforming the standard sparse approach which only gets 7.7% speedup with similar memory savings.

For the MATH-500 benchmark, I'm comparing different pruning methods at 20% sparsity across both SFT and GRPO training regimes. CKA-only performs best with around 26-27% accuracy, while RASP with α=1.0 lags significantly at 21-22%, suggesting the CKA-based selection is more effective for this task. The α dose-response analysis shows that lower α values (0.5) maintain better performance, though the gains from GRPO training are modest across all configurations.

Now looking at the MBPP results, the dense baseline achieves 53.48% accuracy, and at 20% sparsity both CKA-only and standard methods show dramatic drops to around 12-14%, with GRPO providing only marginal improvements of 1-1.3 percentage points.

Examining the cross-scale evaluation, the 7B model with CKA-only pruning reaches a peak reward of 0.354 and 64.39% on GSM8K, substantially outperforming the standard approach which gets 0.081 reward and 59.84% accuracy, while the 1.5B variant achieves 0.238 reward and 35% on GSM8K.

Looking at the stability metrics, the CKA approach shows strong consistency with a minimum Spearman correlation of 0.964 and mean of 0.979. The inference benchmarks reveal that the dense model achieves 72.0 tokens per second with 20.1ms time-to-first-token, while the CKA-only variant trades some throughput (58.3 TPS) for reduced latency and parameter count.

Examining the gradient flow comparisons, CKA-only demonstrates substantially better signal propagation than the standard approach at 2.89× improvement, and the multi-seed results show CKA-only consistently outperforming baselines across different sparsity levels, with the 20% sparsity configuration achieving 64.39±0.19 accuracy across three seeds. Now I'm looking at the cross-architecture results where CKA-only pruning achieves 51.50% post-SFT compared to standard's 21.00%, showing a substantial 30.5 percentage point advantage, alongside the detailed experimental metrics confirming the statistical significance of these improvements across different sparsity levels. Looking at the metrics from the abstract and introduction sections, I'm seeing consistent performance gaps around 0.54pp on average at 20% sparsity, with the peak reward ratio validating at 4.4× and the optimal alpha parameter settling at 2.0. Now I need to map these experimental results back to the registry data to trace which configurations produced these outcomes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "681dc94e-d193-45c6-9100-8afbc71480c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34680
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

_source line 38_

Registry 数据量太大，启动子 agent 解析并提取映射关系。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5c402395-f51b-4356-9a3b-b352bd324d9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34680
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

_source line 39_

<details open><summary>🔧 Tool call — Agent · `toolu_01Nf8X2QpYuR5f2HKgrP8EYj`</summary>

```json
{
  "description": "Parse registry JSON for provenance",
  "prompt": "You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`\n\nThe file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).\n\n**What to extract for each experiment:**\n1. `exp_id`\n2. `status` and `conclusion`\n3. `metrics` (any accuracy, reward, etc.)\n4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`\n5. `created_at` or `updated_at` timestamps\n6. `tags` or any other identifying info\n\n**What I need mapped:**\nI need to match these experiments to paper values. The paper has these key experiments:\n\n**GSM8K 7B 20% sparsity:**\n- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354\n- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081\n- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061\n- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190\n- ShortGPT: SFT=44.73%, GRPO=43.37%\n- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)\n\n**GSM8K 7B α dose-response:**\n- α=0.5: SFT=60.73%, GRPO=61.18%\n- α=1.0: SFT=61.49%, GRPO=60.88%\n- α=2.0: SFT=64.97%, GRPO=66.11%\n- α=3.0: SFT=64.14%, GRPO=63.46%\n- α=4.0: SFT=61.94%, GRPO=62.77%\n\n**GSM8K 7B 15% sparsity:**\n- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)\n- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)\n\n**GSM8K 7B 25% sparsity:**\n- CKA-only: SFT=60.12%, GRPO=59.59%\n- Standard: SFT=50.87%, GRPO=51.86%\n\n**GSM8K 7B 30% sparsity (cliff):**\n- Standard: 4%\n- RASP: 0%\n- CKA-only: 0%\n\n**MATH-500 evaluations:**\n- Dense: 53.0%\n- CKA-only 20%: SFT=26.8%, GRPO=27.4%\n- Standard 20%: SFT=25.8%, GRPO=26.4%\n- RASP 20%: SFT=21.2%, GRPO=22.6%\n- Random 20%: SFT=14.4%\n- α=0.5: SFT=25.4%, GRPO=24.8%\n- α=2.0: SFT=24.0%, GRPO=26.2%\n- α=3.0: SFT=23.2%, GRPO=22.8%\n- α=4.0: SFT=26.6%, GRPO=26.2%\n- CKA-only 25%: SFT=19.2%, GRPO=18.4%\n- Standard 25%: SFT=14.0%, GRPO=12.8%\n\n**MBPP evaluations:**\n- Dense: 53.48%\n- CKA-only 20%: SFT=12.83%, GRPO=14.17%\n- Standard 20%: SFT=12.03%, GRPO=13.10%\n- RASP 20%: SFT=11.76%, GRPO=13.10%\n- ShortGPT 20%: SFT=10.43%, GRPO=14.44%\n\n**1.5B cross-scale:**\n- CKA-only: Rew=0.238, GSM8K=35.48%\n- Standard: Rew=0.084, GSM8K=22.29%\n- RASP: Rew=0.099, GSM8K=26.16%\n\n**Cross-architecture (Qwen2.5-Math-7B):**\n- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%\n- Standard: Post-Prune=18.5%, Post-SFT=21.00%\n\n**Inference efficiency:**\n- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B\n- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB\n- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB\n- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n\n**Gradient flow:**\n- CKA vs Standard: 2.89×, 55/56\n- CKA vs RASP: 2.26×, 56/56\n- RASP vs Standard: 1.28×, 45/56\n\n**Extended training 300 steps:**\n- CKA-only: 64.37%→64.37%\n- Standard: 59.44%→59.29%\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n\n**Instructions:**\n1. First probe the file structure with `jq` to understand the format\n2. Parse the `result` field content\n3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`\n4. Try to match experiments to the paper values above\n5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate\n\nOutput the full results as a structured mapping. Be thorough - I need every experiment matched."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "13dc4679-b6f9-4352-a026-ae226028bf9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QkwLbPSh4kuXK1vujkJ84N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 34680,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34680
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


### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Parse registry JSON for provenance",
  "task_type": "local_agent",
  "prompt": "You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`\n\nThe file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).\n\n**What to extract for each experiment:**\n1. `exp_id`\n2. `status` and `conclusion`\n3. `metrics` (any accuracy, reward, etc.)\n4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`\n5. `created_at` or `updated_at` timestamps\n6. `tags` or any other identifying info\n\n**What I need mapped:**\nI need to match these experiments to paper values. The paper has these key experiments:\n\n**GSM8K 7B 20% sparsity:**\n- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354\n- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081\n- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061\n- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190\n- ShortGPT: SFT=44.73%, GRPO=43.37%\n- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)\n\n**GSM8K 7B α dose-response:**\n- α=0.5: SFT=60.73%, GRPO=61.18%\n- α=1.0: SFT=61.49%, GRPO=60.88%\n- α=2.0: SFT=64.97%, GRPO=66.11%\n- α=3.0: SFT=64.14%, GRPO=63.46%\n- α=4.0: SFT=61.94%, GRPO=62.77%\n\n**GSM8K 7B 15% sparsity:**\n- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)\n- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)\n\n**GSM8K 7B 25% sparsity:**\n- CKA-only: SFT=60.12%, GRPO=59.59%\n- Standard: SFT=50.87%, GRPO=51.86%\n\n**GSM8K 7B 30% sparsity (cliff):**\n- Standard: 4%\n- RASP: 0%\n- CKA-only: 0%\n\n**MATH-500 evaluations:**\n- Dense: 53.0%\n- CKA-only 20%: SFT=26.8%, GRPO=27.4%\n- Standard 20%: SFT=25.8%, GRPO=26.4%\n- RASP 20%: SFT=21.2%, GRPO=22.6%\n- Random 20%: SFT=14.4%\n- α=0.5: SFT=25.4%, GRPO=24.8%\n- α=2.0: SFT=24.0%, GRPO=26.2%\n- α=3.0: SFT=23.2%, GRPO=22.8%\n- α=4.0: SFT=26.6%, GRPO=26.2%\n- CKA-only 25%: SFT=19.2%, GRPO=18.4%\n- Standard 25%: SFT=14.0%, GRPO=12.8%\n\n**MBPP evaluations:**\n- Dense: 53.48%\n- CKA-only 20%: SFT=12.83%, GRPO=14.17%\n- Standard 20%: SFT=12.03%, GRPO=13.10%\n- RASP 20%: SFT=11.76%, GRPO=13.10%\n- ShortGPT 20%: SFT=10.43%, GRPO=14.44%\n\n**1.5B cross-scale:**\n- CKA-only: Rew=0.238, GSM8K=35.48%\n- Standard: Rew=0.084, GSM8K=22.29%\n- RASP: Rew=0.099, GSM8K=26.16%\n\n**Cross-architecture (Qwen2.5-Math-7B):**\n- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%\n- Standard: Post-Prune=18.5%, Post-SFT=21.00%\n\n**Inference efficiency:**\n- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B\n- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB\n- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB\n- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n\n**Gradient flow:**\n- CKA vs Standard: 2.89×, 55/56\n- CKA vs RASP: 2.26×, 56/56\n- RASP vs Standard: 1.28×, 45/56\n\n**Extended training 300 steps:**\n- CKA-only: 64.37%→64.37%\n- Standard: 59.44%→59.29%\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n\n**Instructions:**\n1. First probe the file structure with `jq` to understand the format\n2. Parse the `result` field content\n3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`\n4. Try to match experiments to the paper values above\n5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate\n\nOutput the full results as a structured mapping. Be thorough - I need every experiment matched.",
  "uuid": "f96f0aca-cdde-4262-aa42-703c409101c5",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


## Round 1

## Round 1

41 recorded events


### User

_source line 41 · 2026-05-23T10:48:43.666Z_

You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.

The file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`

The file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).

**What to extract for each experiment:**
1. `exp_id`
2. `status` and `conclusion`
3. `metrics` (any accuracy, reward, etc.)
4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`
5. `created_at` or `updated_at` timestamps
6. `tags` or any other identifying info

**What I need mapped:**
I need to match these experiments to paper values. The paper has these key experiments:

**GSM8K 7B 20% sparsity:**
- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354
- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081
- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061
- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190
- ShortGPT: SFT=44.73%, GRPO=43.37%
- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)

**GSM8K 7B α dose-response:**
- α=0.5: SFT=60.73%, GRPO=61.18%
- α=1.0: SFT=61.49%, GRPO=60.88%
- α=2.0: SFT=64.97%, GRPO=66.11%
- α=3.0: SFT=64.14%, GRPO=63.46%
- α=4.0: SFT=61.94%, GRPO=62.77%

**GSM8K 7B 15% sparsity:**
- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)
- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)

**GSM8K 7B 25% sparsity:**
- CKA-only: SFT=60.12%, GRPO=59.59%
- Standard: SFT=50.87%, GRPO=51.86%

**GSM8K 7B 30% sparsity (cliff):**
- Standard: 4%
- RASP: 0%
- CKA-only: 0%

**MATH-500 evaluations:**
- Dense: 53.0%
- CKA-only 20%: SFT=26.8%, GRPO=27.4%
- Standard 20%: SFT=25.8%, GRPO=26.4%
- RASP 20%: SFT=21.2%, GRPO=22.6%
- Random 20%: SFT=14.4%
- α=0.5: SFT=25.4%, GRPO=24.8%
- α=2.0: SFT=24.0%, GRPO=26.2%
- α=3.0: SFT=23.2%, GRPO=22.8%
- α=4.0: SFT=26.6%, GRPO=26.2%
- CKA-only 25%: SFT=19.2%, GRPO=18.4%
- Standard 25%: SFT=14.0%, GRPO=12.8%

**MBPP evaluations:**
- Dense: 53.48%
- CKA-only 20%: SFT=12.83%, GRPO=14.17%
- Standard 20%: SFT=12.03%, GRPO=13.10%
- RASP 20%: SFT=11.76%, GRPO=13.10%
- ShortGPT 20%: SFT=10.43%, GRPO=14.44%

**1.5B cross-scale:**
- CKA-only: Rew=0.238, GSM8K=35.48%
- Standard: Rew=0.084, GSM8K=22.29%
- RASP: Rew=0.099, GSM8K=26.16%

**Cross-architecture (Qwen2.5-Math-7B):**
- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%
- Standard: Post-Prune=18.5%, Post-SFT=21.00%

**Inference efficiency:**
- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B
- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB
- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB
- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B
- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B

**CKA stability:**
- Spearman ρ min=0.964, mean=0.979

**Gradient flow:**
- CKA vs Standard: 2.89×, 55/56
- CKA vs RASP: 2.26×, 56/56
- RASP vs Standard: 1.28×, 45/56

**Extended training 300 steps:**
- CKA-only: 64.37%→64.37%
- Standard: 59.44%→59.29%

**Unstructured pruning:**
- SFT=87.87%, GRPO=87.64%

**Instructions:**
1. First probe the file structure with `jq` to understand the format
2. Parse the `result` field content
3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`
4. Try to match experiments to the paper values above
5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate

Output the full results as a structured mapping. Be thorough - I need every experiment matched.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "77c6ec19-75aa-4976-9675-22f2bf53eaa0"
}
```

</details>

---


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 16758,
    "tool_uses": 1,
    "duration_ms": 7110
  },
  "last_tool_name": "Bash",
  "uuid": "90da4cc7-406f-4221-aece-130b26ec7fd0",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01RvAAiwjWZviWzQZ3Uq4Q7u`</summary>

```json
{
  "command": "wc -c \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\"",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "dcbd1782-a704-465d-92d5-a99e4e96d685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpNkcBk8QW7vcief7UHJcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16747,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 44 · 2026-05-23T10:48:50.932Z_

<details><summary>↩ Tool result · `toolu_01RvAAiwjWZviWzQZ3Uq4Q7u`</summary>

```text
73390 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "58b8bf33-e51a-4aea-a06c-6ebf638f4f2b"
}
```

</details>

---


### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Peek at file structure",
  "usage": {
    "total_tokens": 16762,
    "tool_uses": 2,
    "duration_ms": 8446
  },
  "last_tool_name": "Bash",
  "uuid": "fdf12f87-fbe0-4cad-89f2-80937dacb32c",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01QfQtzQzoQjLLQvbDJWnyfn`</summary>

```json
{
  "command": "head -c 2000 \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\"",
  "description": "Peek at file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "0e84afd6-3ef9-408c-af5b-d34d75c1785c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpNkcBk8QW7vcief7UHJcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16747,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16747,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 47 · 2026-05-23T10:48:52.163Z_

<details><summary>↩ Tool result · `toolu_01QfQtzQzoQjLLQvbDJWnyfn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"par
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "3427ebfa-1a00-4cd7-a0d2-6acf9d84a659"
}
```

</details>

---


### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Parse JSON and list all experiment IDs",
  "usage": {
    "total_tokens": 18999,
    "tool_uses": 3,
    "duration_ms": 16730
  },
  "last_tool_name": "Bash",
  "uuid": "1675dfa0-2150-47c8-9728-a768164f0801",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01VS7VftsGFzdUCp9tDUK6rV`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint('---')\nfor k in sorted(exps.keys()):\n    print(k)\n\"",
  "description": "Parse JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "e30fee38-7df3-4211-9c36-c9cee4510173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJnNHKS4fWzeUm5q1setJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2235,
      "cache_read_input_tokens": 16747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2235,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-23T10:49:00.496Z_

<details><summary>↩ Tool result · `toolu_01VS7VftsGFzdUCp9tDUK6rV`</summary>

```text
Total experiments: 50
---
eval_gsm8k_grpo_alpha0p5_20
eval_gsm8k_grpo_alpha2p0_20
eval_gsm8k_grpo_alpha3p0_20
eval_gsm8k_grpo_alpha4_20_v3
eval_gsm8k_grpo_cka_only_25_v3
eval_gsm8k_grpo_depth_first_20
eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3
eval_gsm8k_grpo_random_20_seed123_v2
eval_gsm8k_grpo_random_20_seed456
eval_gsm8k_grpo_random_20_v2
eval_gsm8k_grpo_standard_25
eval_gsm8k_sft_alpha0p5_20
eval_gsm8k_sft_alpha2p0_20
eval_gsm8k_sft_alpha3p0_20
eval_gsm8k_sft_alpha4_20_v5
eval_gsm8k_sft_cka_only_25
eval_gsm8k_sft_depth_first_20
eval_gsm8k_sft_random_20
eval_gsm8k_sft_standard_25
eval_math500_grpo_cka_only_20
eval_math500_grpo_cka_only_20_2048_v2
eval_math500_grpo_cka_only_25_v2
eval_math500_grpo_rasp_alpha0p5_20
eval_math500_grpo_rasp_alpha1p0_20
eval_math500_grpo_rasp_alpha2p0_20
eval_math500_grpo_rasp_alpha3p0_20
eval_math500_grpo_rasp_alpha4p0_20
eval_math500_grpo_standard_20_fair_2048_v2
eval_math500_sft_cka_only_20_westd
eval_math500_sft_cka_only_25_v2
eval_math500_sft_qwen_math_cka_only_20
eval_math500_sft_random_20_v3
eval_math500_sft_rasp_alpha0p5_20
eval_math500_sft_rasp_alpha1p0_20_v2
eval_math500_sft_rasp_alpha2p0_20
eval_math500_sft_rasp_alpha3p0_20
eval_math500_sft_rasp_alpha4p0_20
eval_math500_sft_standard_20_1p5b
eval_math500_sft_standard_20_2048_v2
eval_math500_sft_standard_25
grpo_alpha4_20
grpo_qwen_math_cka_only_20
grpo_random_20_seed123
grpo_random_20_seed123_v2
grpo_random_20_seed456
grpo_rasp_alpha3p0_20
grpo_rasp_alpha3p0_20_v2
grpo_standard_25_westb
sft_alpha4_20_v2
sft_random_20
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "f45e8e2c-baee-45d1-b4df-329cba13a61f"
}
```

</details>

---


### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Extract all experiment details",
  "usage": {
    "total_tokens": 20152,
    "tool_uses": 4,
    "duration_ms": 26914
  },
  "last_tool_name": "Bash",
  "uuid": "2aea110c-1cdb-473c-9e05-e1242c1b8e58",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01VkToq2Q53r51KmV5rGbZSB`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','?')\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    server = spec.get('server','?')\n    output_path = spec.get('output_path', e.get('checkpoint_path','?'))\n    log_path = spec.get('log_path','?')\n    command = spec.get('command','?')\n    created = e.get('created_at','?')\n    updated = e.get('updated_at','?')\n    completed = e.get('completed_at','?')\n    hyp = e.get('hypothesis','')\n    parent = e.get('parent','')\n    tags = e.get('tags','')\n    \n    # Format metrics\n    m_parts = []\n    for mk, mv in metrics.items():\n        m_parts.append(f'{mk}={mv}')\n    m_str = ', '.join(m_parts) if m_parts else 'NO_METRICS'\n    \n    print(f'=== {k} ===')\n    print(f'  status={status}, conclusion={conclusion}')\n    print(f'  metrics: {m_str}')\n    print(f'  server={server}')\n    print(f'  output_path={output_path}')\n    print(f'  log_path={log_path}')\n    print(f'  created={created}, updated={updated}, completed={completed}')\n    print(f'  parent={parent}')\n    print(f'  hypothesis={hyp[:200]}')\n    print(f'  command={command[:200] if command != \\\"?\\\" else \\\"?\\\"}')\n    print()\n\" 2>&1",
  "description": "Extract all experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5a13d174-1c7d-4f96-875d-a111da0ae920",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAJbFnmmgXomxiAttxyiYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1117,
      "cache_read_input_tokens": 18982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1117,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 53 · 2026-05-23T10:49:10.670Z_

<details><summary>↩ Tool result · `toolu_01VkToq2Q53r51KmV5rGbZSB`</summary>

```text
&lt;persisted-output>
Output too large (38.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/bsl4yszjb.txt

Preview (first 2KB):
=== eval_gsm8k_grpo_alpha0p5_20 ===
  status=DONE, conclusion=success
  metrics: gsm8k_accuracy=0.6118, gsm8k_correct=807, gsm8k_total=1319
  server=westd-32935
  output_path=?
  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json
  created=2026-05-22T09:28:05.478Z, updated=2026-05-22T09:29:23.350Z, completed=2026-05-22T09:29:13.196Z
  parent=pipeline_alpha0p5_20
  hypothesis=α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.
  command=eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048

=== eval_gsm8k_grpo_alpha2p0_20 ===
  status=DONE, conclusion=success
  metrics: gsm8k_accuracy=0.6611, gsm8k_correct=872, gsm8k_total=1319
  server=westd-32935
  output_path=?
  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json
  created=2026-05-22T09:28:08.089Z, updated=2026-05-22T09:29:24.824Z, completed=2026-05-22T09:29:16.837Z
  parent=pipeline_alpha2p0_20
  hypothesis=α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.
  command=eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048

=== eval_gsm8k_grpo_alpha3p0_20 ===
  status=DONE, conclusion=success
  metrics: gsm8k_accuracy=0.6345, correct=837, total=1319, stderr=0.0133, eos_rate=0.9864, truncated=18, avg_response_length=219.7
  server=westd-32935
  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100
  log_path=/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log
  created=2026-05-22T09:30:06.630Z, updated=2026-05-22T14:47:06.188Z, completed=2026-05-22T14:46:15.365Z
  parent=
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5a2417c0-4de0-44a4-b3cf-0e94fbdaef71"
}
```

</details>

---


### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/bsl4yszjb.txt",
  "usage": {
    "total_tokens": 21824,
    "tool_uses": 5,
    "duration_ms": 30076
  },
  "last_tool_name": "Read",
  "uuid": "27d7390c-b259-4e17-931e-2c16af7f53c0",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01Cw9DeRrTzyna8vUxyZ1M9T`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/bsl4yszjb.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "02da6ee4-0f0e-4b15-b493-eaaa3fba6129",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4hk2NocoBzEr76skmAcDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 20099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1616,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 56 · 2026-05-23T10:49:14.213Z_

<details><summary>↩ Tool result · `toolu_01Cw9DeRrTzyna8vUxyZ1M9T`</summary>

```text
1	=== eval_gsm8k_grpo_alpha0p5_20 ===
2	  status=DONE, conclusion=success
3	  metrics: gsm8k_accuracy=0.6118, gsm8k_correct=807, gsm8k_total=1319
4	  server=westd-32935
5	  output_path=?
6	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json
7	  created=2026-05-22T09:28:05.478Z, updated=2026-05-22T09:29:23.350Z, completed=2026-05-22T09:29:13.196Z
8	  parent=pipeline_alpha0p5_20
9	  hypothesis=α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.
10	  command=eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048
11	
12	=== eval_gsm8k_grpo_alpha2p0_20 ===
13	  status=DONE, conclusion=success
14	  metrics: gsm8k_accuracy=0.6611, gsm8k_correct=872, gsm8k_total=1319
15	  server=westd-32935
16	  output_path=?
17	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json
18	  created=2026-05-22T09:28:08.089Z, updated=2026-05-22T09:29:24.824Z, completed=2026-05-22T09:29:16.837Z
19	  parent=pipeline_alpha2p0_20
20	  hypothesis=α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.
21	  command=eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048
22	
23	=== eval_gsm8k_grpo_alpha3p0_20 ===
24	  status=DONE, conclusion=success
25	  metrics: gsm8k_accuracy=0.6345, correct=837, total=1319, stderr=0.0133, eos_rate=0.9864, truncated=18, avg_response_length=219.7
26	  server=westd-32935
27	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100
28	  log_path=/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log
29	  created=2026-05-22T09:30:06.630Z, updated=2026-05-22T14:47:06.188Z, completed=2026-05-22T14:46:15.365Z
30	  parent=
31	  hypothesis=α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.
32	  command=CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_
33	
34	=== eval_gsm8k_grpo_alpha4_20_v3 ===
35	  status=DONE, conclusion=success
36	  metrics: gsm8k_accuracy=0.6277, gsm8k_accuracy_ci=0.0133, gsm8k_correct=828, gsm8k_total=1319, eos_rate=0.9856, avg_response_length=188.16, natural_eos=1300, truncated=19
37	  server=westd-32935
38	  output_path=?
39	  log_path=/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log
40	  created=2026-05-22T03:49:52.414Z, updated=2026-05-22T05:33:39.349Z, completed=2026-05-22T05:30:50.611Z
41	  parent=eval_gsm8k_grpo_alpha4_20_v2
42	  hypothesis=α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.
43	  command=python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8
44	
45	=== eval_gsm8k_grpo_cka_only_25_v3 ===
46	  status=DONE, conclusion=success
47	  metrics: gsm8k_accuracy=0.5959, correct=786, n_total=1319, eos_rate=0.9818
48	  server=westd-29022
49	  output_path=N/A (eval only)
50	  log_path=~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log
51	  created=2026-05-21T04:56:52.006Z, updated=2026-05-21T08:17:13.429Z, completed=2026-05-21T08:17:13.429Z
52	  parent=grpo_cka_only_25
53	  hypothesis=CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。
54	  command=python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42
55	
56	=== eval_gsm8k_grpo_depth_first_20 ===
57	  status=DONE, conclusion=success
58	  metrics: NO_METRICS
59	  server=westd-32935
60	  output_path=?
61	  log_path=/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log
62	  created=2026-05-22T14:20:41.126Z, updated=2026-05-22T15:18:38.970Z, completed=2026-05-22T15:18:38.970Z
63	  parent=pipeline_depth_first_20
64	  hypothesis=MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior 
65	  command=CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json -
66	
67	=== eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3 ===
68	  status=DONE, conclusion=success
69	  metrics: accuracy=0.486, correct=243, total=500, stderr=0.0224, truncated_pct=0.838, natural_eos_pct=0.162, avg_response_length=1766.5
70	  server=westb-23072
71	  output_path=?
72	  log_path=~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log
73	  created=2026-05-22T15:12:46.181Z, updated=2026-05-23T02:53:37.071Z, completed=2026-05-23T02:53:37.071Z
74	  parent=eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2
75	  hypothesis=MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 
76	  command=bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_awa
77	
78	=== eval_gsm8k_grpo_random_20_seed123_v2 ===
79	  status=DONE, conclusion=success
80	  metrics: NO_METRICS
81	  server=westd-32935
82	  output_path=?
83	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json
84	  created=2026-05-22T14:22:33.753Z, updated=2026-05-22T16:49:54.123Z, completed=2026-05-22T16:49:54.123Z
85	  parent=grpo_random_20_seed123_v2
86	  hypothesis=MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。
87	  command=CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output
88	
89	=== eval_gsm8k_grpo_random_20_seed456 ===
90	  status=DONE, conclusion=success
91	  metrics: gsm8k_accuracy=0.5087, gsm8k_accuracy_se=0.0138, gsm8k_correct=671, gsm8k_total=1319, eos_rate=0.9954, avg_response_length=163.5, truncated=6
92	  server=westb-23072
93	  output_path=?
94	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log
95	  created=2026-05-22T16:26:01.516Z, updated=2026-05-22T18:27:22.282Z, completed=2026-05-22T17:48:17.521Z
96	  parent=grpo_random_20_seed456
97	  hypothesis=MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.
98	  command=CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --outp
99	
100	=== eval_gsm8k_grpo_random_20_v2 ===
101	  status=DONE, conclusion=success
102	  metrics: gsm8k_accuracy=0.5057, gsm8k_stderr=0.0138, correct=667, total=1319, eos_rate=0.9954, avg_response_length=173
103	  server=westd-29022
104	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100
105	  log_path=~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log
106	  created=2026-05-21T04:56:53.980Z, updated=2026-05-21T06:38:00.000Z, completed=2026-05-21T06:38:00.000Z
107	  parent=grpo_random_20
108	  hypothesis=Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。
109	  command=python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42
110	
111	=== eval_gsm8k_grpo_standard_25 ===
112	  status=DONE, conclusion=success
113	  metrics: gsm8k_accuracy=0.5186, stderr=0.0138, correct=684, n_total=1319, eos_rate=0.9575, avg_response_length=314.47
114	  server=westb-23072
115	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100
116	  log_path=/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log
117	  created=2026-05-21T06:42:08.819Z, updated=2026-05-21T12:37:17.579Z, completed=2026-05-21T12:37:17.579Z
118	  parent=grpo_standard_25_westb
119	  hypothesis=Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。
120	  command=python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42
121	
122	=== eval_gsm8k_sft_alpha0p5_20 ===
123	  status=DONE, conclusion=success
124	  metrics: gsm8k_accuracy=0.6073, gsm8k_correct=801, gsm8k_total=1319
125	  server=westd-32935
126	  output_path=?
127	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json
128	  created=2026-05-22T10:19:48.133Z, updated=2026-05-22T10:20:57.690Z, completed=2026-05-22T10:20:50.793Z
129	  parent=pipeline_alpha0p5_20
130	  hypothesis=α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.
131	  command=eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048
132	
133	=== eval_gsm8k_sft_alpha2p0_20 ===
134	  status=DONE, conclusion=success
135	  metrics: gsm8k_accuracy=0.6497, gsm8k_correct=857, gsm8k_total=1319
136	  server=westd-32935
137	  output_path=?
138	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json
139	  created=2026-05-22T10:19:50.623Z, updated=2026-05-22T10:22:56.503Z, completed=2026-05-22T10:22:49.360Z
140	  parent=pipeline_alpha2p0_20
141	  hypothesis=α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.
142	  command=eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048
143	
144	=== eval_gsm8k_sft_alpha3p0_20 ===
145	  status=DONE, conclusion=success
146	  metrics: gsm8k_accuracy=0.6414, gsm8k_correct=846, gsm8k_total=1319, gsm8k_stderr=0.0132, eos_rate=0.9879, avg_response_length=188.63, natural_eos=1303, truncated=16
147	  server=westd-32935
148	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935
149	  log_path=?
150	  created=2026-05-22T10:24:58.696Z, updated=2026-05-22T12:38:25.600Z, completed=2026-05-22T12:35:05.634Z
151	  parent=grpo_rasp_alpha3p0_20
152	  hypothesis=α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.
153	  command=eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048
154	
155	=== eval_gsm8k_sft_alpha4_20_v5 ===
156	  status=DONE, conclusion=success
157	  metrics: gsm8k_accuracy=0.6194, correct=817, total=1319, stderr=0.0134, eos_rate=0.981, avg_response_length=197.85
158	  server=?
159	  output_path=?
160	  log_path=/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log
161	  created=2026-05-22T03:49:50.201Z, updated=2026-05-22T06:05:53.848Z, completed=2026-05-22T05:47:34.101Z
162	  parent=eval_gsm8k_sft_alpha4_20_v4
163	  hypothesis=α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.
164	  command=?
165	
166	=== eval_gsm8k_sft_cka_only_25 ===
167	  status=DONE, conclusion=success
168	  metrics: gsm8k_accuracy=0.6012, correct=793, n_total=1319, stderr=0.0135, eos_rate=0.9803, avg_response_length=243.6
169	  server=westd-29022
170	  output_path=N/A (eval only)
171	  log_path=/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log
172	  created=2026-05-21T06:47:14.010Z, updated=2026-05-21T10:17:58.203Z, completed=2026-05-21T10:17:58.203Z
173	  parent=
174	  hypothesis=CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity
175	  command=nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autod
176	
177	=== eval_gsm8k_sft_depth_first_20 ===
178	  status=DONE, conclusion=success
179	  metrics: NO_METRICS
180	  server=westd-32935
181	  output_path=?
182	  log_path=/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log
183	  created=2026-05-22T14:20:43.950Z, updated=2026-05-22T15:19:31.829Z, completed=2026-05-22T15:19:31.829Z
184	  parent=pipeline_depth_first_20
185	  hypothesis=MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.
186	  command=CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype 
187	
188	=== eval_gsm8k_sft_random_20 ===
189	  status=DONE, conclusion=success
190	  metrics: gsm8k_accuracy=0.5125, correct=676, n_total=1319, stderr=0.0138, eos_rate=0.9932, avg_response_length=182.4
191	  server=westd-29022
192	  output_path=N/A (eval only)
193	  log_path=/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log
194	  created=2026-05-21T06:47:16.459Z, updated=2026-05-21T08:47:06.620Z, completed=2026-05-21T08:47:06.620Z
195	  parent=
196	  hypothesis=Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity
197	  command=nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autod
198	
199	=== eval_gsm8k_sft_standard_25 ===
200	  status=DONE, conclusion=success
201	  metrics: gsm8k_accuracy=0.5087, stderr=0.0138, correct=671, n_total=1319, eos_rate=0.953, avg_response_length=333.15
202	  server=westd-29022
203	  output_path=?
204	  log_path=/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log
205	  created=2026-05-21T08:13:12.112Z, updated=2026-05-21T14:40:37.092Z, completed=2026-05-21T14:40:37.092Z
206	  parent=
207	  hypothesis=Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%
208	  command=nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autod
209	
210	=== eval_math500_grpo_cka_only_20 ===
211	  status=DONE, conclusion=success
212	  metrics: accuracy=0.266, n_correct=133, n_total=500, stderr=0.0198, truncated=108, truncation_rate=0.216, avg_response_length=1124.24
213	  server=?
214	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json
215	  log_path=?
216	  created=2026-05-18T02:41:32.199Z, updated=2026-05-21T12:47:30.348Z, completed=2026-05-18T14:09:25.937Z
217	  parent=grpo_cka_only_20
218	  hypothesis=CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500
219	  command=?
220	
221	=== eval_math500_grpo_cka_only_20_2048_v2 ===
222	  status=DONE, conclusion=success
223	  metrics: accuracy=0.274, correct=137, total=500, stderr=0.01995, natural_eos=390, truncated=110, avg_response_length=654.746
224	  server=westd-32935
225	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json
226	  log_path=?
227	  created=2026-05-23T05:07:09.002Z, updated=2026-05-23T08:55:58.278Z, completed=2026-05-23T08:55:58.278Z
228	  parent=eval_math500_grpo_cka_only_20_2048
229	  hypothesis=GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ|
230	  command=bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_
231	
232	=== eval_math500_grpo_cka_only_25_v2 ===
233	  status=DONE, conclusion=success
234	  metrics: math500_accuracy=0.184, math500_stderr=0.0173, correct=92, n_total=500
235	  server=westd-29022
236	  output_path=N/A (eval only)
237	  log_path=/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log
238	  created=2026-05-21T13:54:50.310Z, updated=2026-05-21T17:33:50.709Z, completed=2026-05-21T17:33:40.068Z
239	  parent=eval_math500_grpo_cka_only_25
240	  hypothesis=CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data
241	  command=nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tm
242	
243	=== eval_math500_grpo_rasp_alpha0p5_20 ===
244	  status=DONE, conclusion=success
245	  metrics: accuracy=0.248, stderr=0.0193, correct=124, total=500, natural_eos=274, truncated=226, avg_response_length=1110.462
246	  server=westb-23072
247	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json
248	  log_path=?
249	  created=2026-05-23T02:59:15.985Z, updated=2026-05-23T10:11:11.002Z, completed=2026-05-23T10:11:11.002Z
250	  parent=eval_gsm8k_grpo_alpha0p5_20
251	  hypothesis=GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.
252	  command=python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alp
253	
254	=== eval_math500_grpo_rasp_alpha1p0_20 ===
255	  status=DONE, conclusion=success
256	  metrics: accuracy=0.226, stderr=0.0187, n_correct=113, n_total=500, avg_response_length=903.536, natural_eos=320, truncated=180
257	  server=?
258	  output_path=?
259	  log_path=~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log
260	  created=2026-05-22T23:02:44.335Z, updated=2026-05-23T04:44:32.303Z, completed=2026-05-23T04:44:32.303Z
261	  parent=
262	  hypothesis=GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.
263	  command=?
264	
265	=== eval_math500_grpo_rasp_alpha2p0_20 ===
266	  status=DONE, conclusion=success
267	  metrics: accuracy=0.262, correct=131, total=500, stderr=0.0197, natural_eos=349, truncated=151, avg_response_length=785.326
268	  server=westd-32935
269	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20
270	  log_path=~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log
271	  created=2026-05-22T22:23:27.589Z, updated=2026-05-23T03:16:40.537Z, completed=2026-05-23T03:16:40.537Z
272	  parent=
273	  hypothesis=GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.
274	  command=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path
275	
276	=== eval_math500_grpo_rasp_alpha3p0_20 ===
277	  status=DONE, conclusion=success
278	  metrics: accuracy=0.228, correct=114, total=500, stderr=0.0188, truncated_ratio=0.28, avg_response_length=745.038
279	  server=westd-32935
280	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json
281	  log_path=?
282	  created=2026-05-23T03:19:40.950Z, updated=2026-05-23T07:48:57.618Z, completed=2026-05-23T07:48:50.736Z
283	  parent=eval_gsm8k_grpo_alpha3p0_20
284	  hypothesis=GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.
285	  command=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_
286	
287	=== eval_math500_grpo_rasp_alpha4p0_20 ===
288	  status=DONE, conclusion=success
289	  metrics: accuracy=0.262, stderr=0.01966, correct=131, total=500, truncated=180, natural_eos=320, avg_response_length=925.48
290	  server=?
291	  output_path=?
292	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log
293	  created=2026-05-23T00:01:54.194Z, updated=2026-05-23T05:58:52.769Z, completed=2026-05-23T05:58:52.769Z
294	  parent=eval_gsm8k_grpo_alpha4_20_v3
295	  hypothesis=GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.
296	  command=?
297	
298	=== eval_math500_grpo_standard_20_fair_2048_v2 ===
299	  status=DONE, conclusion=success
300	  metrics: math500_accuracy=0.264, math500_correct=132, math500_total=500, math500_stderr=0.0197
301	  server=westd-32935
302	  output_path=?
303	  log_path=/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log
304	  created=2026-05-22T03:49:45.575Z, updated=2026-05-22T11:17:52.493Z, completed=2026-05-22T11:12:27.767Z
305	  parent=eval_math500_grpo_standard_20_fair_2048
306	  hypothesis=Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.
307	  command=python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_mat
308	
309	=== eval_math500_sft_cka_only_20_westd ===
310	  status=DONE, conclusion=success
311	  metrics: accuracy=0.268, correct=134, total=500, truncated=116, stderr=0.0198, natural_eos_pct=0.768, avg_response_length=673.278, note=PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.
312	  server=westd-32935
313	  output_path=?
314	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log
315	  created=2026-05-22T20:45:21.526Z, updated=2026-05-23T03:21:26.164Z, completed=2026-05-23T00:00:43.009Z
316	  parent=eval_math500_sft_cka_only_20_westb
317	  hypothesis=CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishe
318	  command=CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sf
319	
320	=== eval_math500_sft_cka_only_25_v2 ===
321	  status=DONE, conclusion=success
322	  metrics: math500_accuracy=0.192, correct=96, n_total=500, std_err=0.0176
323	  server=westd-29022
324	  output_path=N/A (eval only)
325	  log_path=/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log
326	  created=2026-05-21T13:54:51.945Z, updated=2026-05-21T17:29:14.940Z, completed=2026-05-21T17:29:10.900Z
327	  parent=eval_math500_sft_cka_only_25
328	  hypothesis=CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency
329	  command=nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tm
330	
331	=== eval_math500_sft_qwen_math_cka_only_20 ===
332	  status=DONE, conclusion=success
333	  metrics: accuracy=0.216, stderr=0.0184, correct=108, total=500, natural_eos=90, truncated=410, avg_response_length=1745.338
334	  server=westb-23072
335	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json
336	  log_path=/tmp/eval_math500_sft_qwen_cka_only_20.log
337	  created=2026-05-22T23:11:09.017Z, updated=2026-05-23T10:44:00.535Z, completed=2026-05-23T10:44:00.535Z
338	  parent=sft_qwen_math_cka_only_20
339	  hypothesis=Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Pai
340	  command=CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/r
341	
342	=== eval_math500_sft_random_20_v3 ===
343	  status=DONE, conclusion=success
344	  metrics: accuracy=0.144, correct=72, total=500, stderr=0.0157, natural_eos=171, truncated=329, avg_response_length=1470.44
345	  server=westd-32935
346	  output_path=?
347	  log_path=/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log
348	  created=2026-05-22T04:11:52.462Z, updated=2026-05-22T14:10:18.359Z, completed=2026-05-22T14:10:18.359Z
349	  parent=eval_math500_sft_random_20_v2
350	  hypothesis=Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.
351	  command=python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random
352	
353	=== eval_math500_sft_rasp_alpha0p5_20 ===
354	  status=DONE, conclusion=success
355	  metrics: accuracy=0.254, correct=127, total=500, truncated=220, stderr=0.0195
356	  server=?
357	  output_path=?
358	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log
359	  created=2026-05-22T15:20:44.460Z, updated=2026-05-22T22:18:43.350Z, completed=2026-05-22T22:18:43.350Z
360	  parent=
361	  hypothesis=α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).
362	  command=?
363	
364	=== eval_math500_sft_rasp_alpha1p0_20_v2 ===
365	  status=DONE, conclusion=success
366	  metrics: accuracy=0.212, correct=106, total=500, truncated=186, stderr=0.0183
367	  server=?
368	  output_path=?
369	  log_path=/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log
370	  created=2026-05-22T20:50:24.239Z, updated=2026-05-22T23:01:03.419Z, completed=2026-05-22T23:01:03.420Z
371	  parent=eval_math500_sft_rasp_alpha1p0_20
372	  hypothesis=α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response
373	  command=?
374	
375	=== eval_math500_sft_rasp_alpha2p0_20 ===
376	  status=DONE, conclusion=success
377	  metrics: accuracy=0.24, correct=120, total=500, truncated=155, stderr=0.0191
378	  server=westd-32935
379	  output_path=?
380	  log_path=/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log
381	  created=2026-05-22T15:06:22.386Z, updated=2026-05-22T20:44:52.970Z, completed=2026-05-22T20:12:32.633Z
382	  parent=
383	  hypothesis=α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).
384	  command=CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval
385	
386	=== eval_math500_sft_rasp_alpha3p0_20 ===
387	  status=DONE, conclusion=success
388	  metrics: accuracy=0.232, correct=116, total=500, truncated=144, stderr=0.0189
389	  server=?
390	  output_path=?
391	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log
392	  created=2026-05-22T18:26:16.273Z, updated=2026-05-22T22:12:26.406Z, completed=2026-05-22T22:12:26.406Z
393	  parent=
394	  hypothesis=α=3.0 SFT MATH-500 eval @2048. Dose-response "下降段确认点": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Compl
395	  command=?
396	
397	=== eval_math500_sft_rasp_alpha4p0_20 ===
398	  status=DONE, conclusion=success
399	  metrics: accuracy=0.266, correct=133, total=500, truncated=190, stderr=0.0198
400	  server=?
401	  output_path=?
402	  log_path=/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log
403	  created=2026-05-22T15:20:47.150Z, updated=2026-05-22T21:22:35.441Z, completed=2026-05-22T21:22:35.442Z
404	  parent=
405	  hypothesis=α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).
406	  command=?
407	
408	=== eval_math500_sft_standard_20_1p5b ===
409	  status=DONE, conclusion=success
410	  metrics: math500_accuracy=0.054, correct=27, total=500, truncated=335
411	  server=westb-23072
412	  output_path=?
413	  log_path=/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log
414	  created=2026-05-22T04:31:30.202Z, updated=2026-05-22T08:27:40.167Z, completed=2026-05-22T07:50:22.759Z
415	  parent=
416	  hypothesis=1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.
417	  command=python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft
418	
419	=== eval_math500_sft_standard_20_2048_v2 ===
420	  status=DONE, conclusion=success
421	  metrics: accuracy=0.258, n_correct=129, n_total=500
422	  server=westd-32935
423	  output_path=?
424	  log_path=~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log
425	  created=2026-05-19T01:34:44.782Z, updated=2026-05-22T22:19:38.080Z, completed=2026-05-19T13:08:16.850Z
426	  parent=eval_math500_sft_standard_20
427	  hypothesis=Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.
428	  command=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path
429	
430	=== eval_math500_sft_standard_25 ===
431	  status=DONE, conclusion=success
432	  metrics: math500_accuracy=0.14, correct=70, n_total=500, natural_eos=185, truncated=315, avg_response_length=1367.82, v1_accuracy=0.13, v1_correct=65
433	  server=westb-23072
434	  output_path=?
435	  log_path=/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log
436	  created=2026-05-21T02:58:32.492Z, updated=2026-05-22T02:31:03.648Z, completed=2026-05-21T19:22:29.444Z
437	  parent=
438	  hypothesis=Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500
439	  command=CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_ma
440	
441	=== grpo_alpha4_20 ===
442	  status=DONE, conclusion=success
443	  metrics: final_reward=0.198, reward_range=0.146-0.256, steps=100, final_loss=0.018, final_kl=0.00198
444	  server=westd-29022
445	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100
446	  log_path=~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log
447	  created=2026-05-21T18:59:18.863Z, updated=2026-05-21T19:32:31.353Z, completed=2026-05-21T19:27:23.228Z
448	  parent=sft_alpha4_20_v2
449	  hypothesis=α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning ca
450	  command=python src/train_grpo_v5.py --alpha 4.0 --max_steps 100
451	
452	=== grpo_qwen_math_cka_only_20 ===
453	  status=DONE, conclusion=success
454	  metrics: NO_METRICS
455	  server=westb-23072
456	  output_path=?
457	  log_path=/tmp/mf3_qwen_grpo.log
458	  created=2026-05-22T08:50:34.293Z, updated=2026-05-22T09:54:05.974Z, completed=2026-05-22T09:54:05.974Z
459	  parent=sft_qwen_math_cka_only_20_v2
460	  hypothesis=MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priori
461	  command=train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperatur
462	
463	=== grpo_random_20_seed123 ===
464	  status=DONE, conclusion=success
465	  metrics: NO_METRICS
466	  server=westd-32935
467	  output_path=?
468	  log_path=/tmp/mf2_random_seed123_grpo.log
469	  created=2026-05-22T10:34:12.100Z, updated=2026-05-22T11:17:21.388Z, completed=2026-05-22T11:12:57.919Z
470	  parent=
471	  hypothesis=MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.
472	  command=bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_pat
473	
474	=== grpo_random_20_seed123_v2 ===
475	  status=DONE, conclusion=success
476	  metrics: NO_METRICS
477	  server=westd-32935
478	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100
479	  log_path=/tmp/grpo_random_seed123_v2.log
480	  created=2026-05-22T14:22:29.868Z, updated=2026-05-22T15:00:23.101Z, completed=2026-05-22T15:00:23.101Z
481	  parent=grpo_random_20_seed123
482	  hypothesis=MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling rob
483	  command=CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/re
484	
485	=== grpo_random_20_seed456 ===
486	  status=DONE, conclusion=success
487	  metrics: NO_METRICS
488	  server=westb-23072
489	  output_path=?
490	  log_path=/tmp/grpo_random_seed456.log
491	  created=2026-05-22T12:00:38.940Z, updated=2026-05-22T16:27:46.810Z, completed=2026-05-22T16:22:44.289Z
492	  parent=
493	  hypothesis=MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 clai
494	  command=CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/re
495	
496	=== grpo_rasp_alpha3p0_20 ===
497	  status=DONE, conclusion=success
498	  metrics: NO_METRICS
499	  server=westb-23072
500	  output_path=?
501	  log_path=/tmp/alpha3p0_grpo.log
502	  created=2026-05-22T08:48:06.001Z, updated=2026-05-22T10:39:07.034Z, completed=2026-05-22T10:31:57.909Z
503	  parent=grpo_alpha4_20
504	  hypothesis=α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harm
505	  command=train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 
506	
507	=== grpo_rasp_alpha3p0_20_v2 ===
508	  status=DONE, conclusion=success
509	  metrics: NO_METRICS
510	  server=westd-32935
511	  output_path=?
512	  log_path=/tmp/grpo_alpha3p0_v2.log
513	  created=2026-05-22T10:40:19.362Z, updated=2026-05-22T11:58:15.586Z, completed=2026-05-22T11:58:15.586Z
514	  parent=grpo_rasp_alpha3p0_20
515	  hypothesis=Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 d
516	  command=CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_d
517	
518	=== grpo_standard_25_westb ===
519	  status=DONE, conclusion=success
520	  metrics: reward=0.00813, steps=100, collapse_pattern=near_total_collapse
521	  server=westb-23072
522	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100
523	  log_path=?
524	  created=2026-05-21T03:00:00.000Z, updated=2026-05-21T06:40:00.000Z, completed=2026-05-21T06:40:00.000Z
525	  parent=sft_standard_25
526	  hypothesis=Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.
527	  command=python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 -
528	
529	=== sft_alpha4_20_v2 ===
530	  status=PREPARING, conclusion=success
531	  metrics: final_train_loss=0.8118, token_accuracy=0.8165, epochs=2, steps=936
532	  server=westd-29022
533	  output_path=?
534	  log_path=~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log
535	  created=2026-05-21T18:30:48.284Z, updated=2026-05-21T19:32:28.482Z, completed=?
536	  parent=sft_alpha4_20_manual
537	  hypothesis=α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after full SFT→GRPO→eval pipeline.
538	  command=bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_st
539	
540	=== sft_random_20 ===
541	  status=DONE, conclusion=success
542	  metrics: steps=1870, model_size_gb=12
543	  server=westd-29022
544	  output_path=/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20
545	  log_path=?
546	  created=2026-05-21T03:44:24.654Z, updated=2026-05-21T04:45:00.000Z, completed=2026-05-21T03:50:00.000Z
547	  parent=
548	  hypothesis=Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。
549	  command=python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20
550	
551	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "bc8a0b50-9a4a-409d-866a-bfd69e05328b"
}
```

</details>

---


### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Check for additional data fields and missing parent references",
  "usage": {
    "total_tokens": 39678,
    "tool_uses": 6,
    "duration_ms": 43211
  },
  "last_tool_name": "Bash",
  "uuid": "b59bd335-ab8f-4146-91a4-ae5f0c24cf0e",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01MAk4t4s9WwUNQYQCTH3xYm`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Check for any additional data in the registry\nother_keys = [k for k in data['data'].keys() if k != 'experiments']\nprint('Other keys in data:', other_keys)\n\n# Check for tags field\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    tags = e.get('tags')\n    if tags:\n        print(f'{k}: tags={tags}')\n        \n# Find parent references that are NOT in the registry\nprint()\nprint('=== Parent references NOT in registry ===')\nfor k in sorted(exps.keys()):\n    e = exps[k]\n    p = e.get('parent','')\n    if p and p not in exps:\n        print(f'  {k} -> parent={p} (NOT IN REGISTRY)')\n\"",
  "description": "Check for additional data fields and missing parent references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "d2d271ad-c9e3-49e0-999c-87b4f007e792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnncYTSggVkFYQ8Ty75NuJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17852,
      "cache_read_input_tokens": 21715,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17852,
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

_source line 59 · 2026-05-23T10:49:26.972Z_

<details><summary>↩ Tool result · `toolu_01MAk4t4s9WwUNQYQCTH3xYm`</summary>

```text
Other keys in data: ['count', 'total', 'baseline']

=== Parent references NOT in registry ===
  eval_gsm8k_grpo_alpha0p5_20 -> parent=pipeline_alpha0p5_20 (NOT IN REGISTRY)
  eval_gsm8k_grpo_alpha2p0_20 -> parent=pipeline_alpha2p0_20 (NOT IN REGISTRY)
  eval_gsm8k_grpo_alpha4_20_v3 -> parent=eval_gsm8k_grpo_alpha4_20_v2 (NOT IN REGISTRY)
  eval_gsm8k_grpo_cka_only_25_v3 -> parent=grpo_cka_only_25 (NOT IN REGISTRY)
  eval_gsm8k_grpo_depth_first_20 -> parent=pipeline_depth_first_20 (NOT IN REGISTRY)
  eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3 -> parent=eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2 (NOT IN REGISTRY)
  eval_gsm8k_grpo_random_20_v2 -> parent=grpo_random_20 (NOT IN REGISTRY)
  eval_gsm8k_sft_alpha0p5_20 -> parent=pipeline_alpha0p5_20 (NOT IN REGISTRY)
  eval_gsm8k_sft_alpha2p0_20 -> parent=pipeline_alpha2p0_20 (NOT IN REGISTRY)
  eval_gsm8k_sft_alpha4_20_v5 -> parent=eval_gsm8k_sft_alpha4_20_v4 (NOT IN REGISTRY)
  eval_gsm8k_sft_depth_first_20 -> parent=pipeline_depth_first_20 (NOT IN REGISTRY)
  eval_math500_grpo_cka_only_20 -> parent=grpo_cka_only_20 (NOT IN REGISTRY)
  eval_math500_grpo_cka_only_20_2048_v2 -> parent=eval_math500_grpo_cka_only_20_2048 (NOT IN REGISTRY)
  eval_math500_grpo_cka_only_25_v2 -> parent=eval_math500_grpo_cka_only_25 (NOT IN REGISTRY)
  eval_math500_grpo_standard_20_fair_2048_v2 -> parent=eval_math500_grpo_standard_20_fair_2048 (NOT IN REGISTRY)
  eval_math500_sft_cka_only_20_westd -> parent=eval_math500_sft_cka_only_20_westb (NOT IN REGISTRY)
  eval_math500_sft_cka_only_25_v2 -> parent=eval_math500_sft_cka_only_25 (NOT IN REGISTRY)
  eval_math500_sft_qwen_math_cka_only_20 -> parent=sft_qwen_math_cka_only_20 (NOT IN REGISTRY)
  eval_math500_sft_random_20_v3 -> parent=eval_math500_sft_random_20_v2 (NOT IN REGISTRY)
  eval_math500_sft_rasp_alpha1p0_20_v2 -> parent=eval_math500_sft_rasp_alpha1p0_20 (NOT IN REGISTRY)
  eval_math500_sft_standard_20_2048_v2 -> parent=eval_math500_sft_standard_20 (NOT IN REGISTRY)
  grpo_qwen_math_cka_only_20 -> parent=sft_qwen_math_cka_only_20_v2 (NOT IN REGISTRY)
  grpo_standard_25_westb -> parent=sft_standard_25 (NOT IN REGISTRY)
  sft_alpha4_20_v2 -> parent=sft_alpha4_20_manual (NOT IN REGISTRY)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "47ba60cd-02ee-4a49-a1b6-cf23bd9da102"
}
```

</details>

---


### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Check baseline and other metadata",
  "usage": {
    "total_tokens": 41204,
    "tool_uses": 7,
    "duration_ms": 51103
  },
  "last_tool_name": "Bash",
  "uuid": "ec59a76b-2188-4cce-ae64-3940a4b0687a",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01AHFmaKC4YEmefK2zpZknR9`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\n\n# Check baseline data\nbaseline = data['data'].get('baseline', {})\nprint('=== BASELINE DATA ===')\nprint(json.dumps(baseline, indent=2))\nprint()\nprint('count:', data['data'].get('count'))\nprint('total:', data['data'].get('total'))\n\"",
  "description": "Check baseline and other metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "00554167-ecf9-4a40-b069-dcf003cf6045",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmTgS4M1AdyJCem8YZTCCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1491,
      "cache_read_input_tokens": 39567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1491,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 62 · 2026-05-23T10:49:34.858Z_

<details><summary>↩ Tool result · `toolu_01AHFmaKC4YEmefK2zpZknR9`</summary>

```text
=== BASELINE DATA ===
null

count: 50
total: 249
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "a8591a7c-e938-4814-ade4-c79af4d4a71c"
}
```

</details>

---


### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "description": "Running Build complete experiment-to-paper mapping",
  "usage": {
    "total_tokens": 41613,
    "tool_uses": 8,
    "duration_ms": 133106
  },
  "last_tool_name": "Bash",
  "uuid": "8c0cab17-88a5-48c3-9050-1d30f7f6677b",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01LN9qsYfmq1w6Qd5CBGurKf`</summary>

```json
{
  "command": "cat \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt\" | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\ndata = json.loads(raw['result'])\nexps = data['data']['experiments']\n\n# Build comprehensive mapping\n# Format: paper_value -> { exp_id, metric_key, metric_value, server, output_path, created, updated }\n\nprint('=' * 120)\nprint('COMPLETE EXPERIMENT-TO-PAPER MAPPING')\nprint('=' * 120)\n\n#-----------------------------------------------------------\n# SECTION 1: GSM8K 7B 20% SPARSITY - DOSE RESPONSE (alpha)\n#-----------------------------------------------------------\nprint()\nprint('=' * 120)\nprint('SECTION 1: GSM8K 7B 20% -- alpha DOSE-RESPONSE')\nprint('=' * 120)\n\ndose_response = {\n    'eval_gsm8k_sft_alpha0p5_20':  {'paper': 'alpha=0.5 SFT=60.73%',  'actual': None},\n    'eval_gsm8k_grpo_alpha0p5_20': {'paper': 'alpha=0.5 GRPO=61.18%', 'actual': None},\n    'eval_gsm8k_sft_alpha3p0_20':  {'paper': 'alpha=3.0 SFT=64.14%',  'actual': None},\n    'eval_gsm8k_grpo_alpha3p0_20': {'paper': 'alpha=3.0 GRPO=63.46%', 'actual': None},  # note: paper says 63.46%\n    'eval_gsm8k_sft_alpha2p0_20':  {'paper': 'alpha=2.0 SFT=64.97%',  'actual': None},\n    'eval_gsm8k_grpo_alpha2p0_20': {'paper': 'alpha=2.0 GRPO=66.11%', 'actual': None},\n    'eval_gsm8k_sft_alpha4_20_v5': {'paper': 'alpha=4.0 SFT=61.94%',  'actual': None},\n    'eval_gsm8k_grpo_alpha4_20_v3':{'paper': 'alpha=4.0 GRPO=62.77%', 'actual': None},\n}\n\nfor eid, info in dose_response.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('gsm8k_accuracy', m.get('accuracy', '?'))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.2f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    output = e.get('spec', {}).get('output_path', e.get('checkpoint_path', '?'))\n    created = e.get('created_at', '?')\n    updated = e.get('updated_at', '?')\n    \n    match = 'MATCH' if acc != '?' else 'NO_METRIC'\n    print(f'  {eid}')\n    print(f'    Paper value: {info[\\\"paper\\\"]}')\n    print(f'    Registry:    {acc_pct}  ({match})')\n    print(f'    Server: {server} | Created: {created} | Updated: {updated}')\n    print(f'    Output: {output}')\n    print()\n\n#-----------------------------------------------------------\n# SECTION 2: GSM8K 7B 20% MAIN COMPARISON\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 2: GSM8K 7B 20% -- MAIN METHOD COMPARISON')\nprint('=' * 120)\n\n# CKA-only SFT=63.91% -- NOT in these 50 experiments (older run)\n# CKA-only GRPO seeds: 64.37%, 64.22%, 64.58% -- NOT in these 50 \n# Standard SFT=59.29%, GRPO=59.84% -- NOT in these 50\n# RASP alpha=1.0 SFT=61.49%, GRPO=60.88% -- NOT in these 50\n\n# Random:\nprint('  === Random 20% ===')\nfor eid in ['eval_gsm8k_sft_random_20', 'eval_gsm8k_grpo_random_20_v2', 'eval_gsm8k_grpo_random_20_seed123_v2', 'eval_gsm8k_grpo_random_20_seed456']:\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('gsm8k_accuracy', m.get('accuracy', '?'))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.2f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    output = e.get('spec', {}).get('output_path', e.get('checkpoint_path', '?'))\n    created = e.get('created_at', '?')\n    updated = e.get('updated_at', '?')\n    print(f'  {eid}')\n    print(f'    Registry: {acc_pct}')\n    print(f'    Server: {server} | Created: {created}')\n    print(f'    Output: {output}')\n    print()\n\n# Paper values for Random:\nprint('  Paper: Random SFT=51.25%, GRPO seeds: 50.57%, 50.72%, 50.87%')\nprint()\n\n#-----------------------------------------------------------\n# SECTION 3: GSM8K CROSS-SPARSITY (15%, 25%, 30%)\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 3: GSM8K 7B CROSS-SPARSITY (25%)')\nprint('=' * 120)\n\ncross_sparsity_25 = {\n    'eval_gsm8k_sft_cka_only_25':   {'paper': 'CKA-only 25% SFT=60.12%'},\n    'eval_gsm8k_grpo_cka_only_25_v3':{'paper': 'CKA-only 25% GRPO=59.59%'},\n    'eval_gsm8k_sft_standard_25':   {'paper': 'Standard 25% SFT=50.87%'},\n    'eval_gsm8k_grpo_standard_25':  {'paper': 'Standard 25% GRPO=51.86%'},\n}\nfor eid, info in cross_sparsity_25.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('gsm8k_accuracy', m.get('accuracy', '?'))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.2f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    output = e.get('spec', {}).get('output_path', e.get('checkpoint_path', '?'))\n    created = e.get('created_at', '?')\n    updated = e.get('updated_at', '?')\n    print(f'  {eid}')\n    print(f'    Paper: {info[\\\"paper\\\"]}')\n    print(f'    Registry: {acc_pct}')\n    print(f'    Server: {server} | Created: {created}')\n    print(f'    Output: {output}')\n    print()\n\n#-----------------------------------------------------------\n# SECTION 4: MATH-500 EVALUATIONS\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 4: MATH-500 EVALUATIONS')\nprint('=' * 120)\n\nmath500_map = {\n    'eval_math500_sft_cka_only_20_westd':        {'paper': 'CKA-only 20% SFT=26.8%'},\n    'eval_math500_grpo_cka_only_20_2048_v2':     {'paper': 'CKA-only 20% GRPO=27.4%'},\n    'eval_math500_grpo_cka_only_20':             {'paper': 'CKA-only 20% GRPO=27.4% (old eval, 26.6%)'},\n    'eval_math500_sft_standard_20_2048_v2':      {'paper': 'Standard 20% SFT=25.8%'},\n    'eval_math500_grpo_standard_20_fair_2048_v2':{'paper': 'Standard 20% GRPO=26.4%'},\n    'eval_math500_sft_random_20_v3':             {'paper': 'Random 20% SFT=14.4%'},\n    'eval_math500_sft_rasp_alpha0p5_20':         {'paper': 'alpha=0.5 SFT=25.4%'},\n    'eval_math500_grpo_rasp_alpha0p5_20':        {'paper': 'alpha=0.5 GRPO=24.8%'},\n    'eval_math500_sft_rasp_alpha1p0_20_v2':      {'paper': 'RASP alpha=1.0 SFT=21.2%'},\n    'eval_math500_grpo_rasp_alpha1p0_20':        {'paper': 'RASP alpha=1.0 GRPO=22.6%'},\n    'eval_math500_sft_rasp_alpha2p0_20':         {'paper': 'alpha=2.0 SFT=24.0%'},\n    'eval_math500_grpo_rasp_alpha2p0_20':        {'paper': 'alpha=2.0 GRPO=26.2%'},\n    'eval_math500_sft_rasp_alpha3p0_20':         {'paper': 'alpha=3.0 SFT=23.2%'},\n    'eval_math500_grpo_rasp_alpha3p0_20':        {'paper': 'alpha=3.0 GRPO=22.8%'},\n    'eval_math500_sft_rasp_alpha4p0_20':         {'paper': 'alpha=4.0 SFT=26.6%'},\n    'eval_math500_grpo_rasp_alpha4p0_20':        {'paper': 'alpha=4.0 GRPO=26.2%'},\n    'eval_math500_sft_cka_only_25_v2':           {'paper': 'CKA-only 25% SFT=19.2%'},\n    'eval_math500_grpo_cka_only_25_v2':          {'paper': 'CKA-only 25% GRPO=18.4%'},\n    'eval_math500_sft_standard_25':              {'paper': 'Standard 25% SFT=14.0%'},\n}\nfor eid, info in math500_map.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('accuracy', m.get('math500_accuracy', '?'))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.1f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    output = e.get('spec', {}).get('output_path', e.get('checkpoint_path', '?'))\n    created = e.get('created_at', '?')\n    updated = e.get('updated_at', '?')\n    print(f'  {eid}')\n    print(f'    Paper: {info[\\\"paper\\\"]}')\n    print(f'    Registry: {acc_pct}')\n    print(f'    Server: {server} | Created: {created}')\n    print(f'    Output: {output}')\n    print()\n\n#-----------------------------------------------------------\n# SECTION 5: CROSS-ARCHITECTURE (Qwen)\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 5: CROSS-ARCHITECTURE (Qwen2.5-Math-7B)')\nprint('=' * 120)\n\nqwen_map = {\n    'eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3': {'paper': 'CKA-only GRPO GSM8K (N=500)'},\n    'eval_math500_sft_qwen_math_cka_only_20':        {'paper': 'CKA-only SFT MATH-500=21.6%'},\n    'grpo_qwen_math_cka_only_20':                    {'paper': 'CKA-only GRPO training'},\n}\nfor eid, info in qwen_map.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('accuracy', m.get('gsm8k_accuracy', '?'))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.1f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    created = e.get('created_at', '?')\n    print(f'  {eid}')\n    print(f'    Paper: {info[\\\"paper\\\"]}')\n    print(f'    Registry: {acc_pct}')\n    print(f'    Server: {server} | Created: {created}')\n    print()\n\n#-----------------------------------------------------------\n# SECTION 6: TRAINING RUNS (GRPO / SFT, no eval metrics)\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 6: TRAINING RUNS (GRPO/SFT)')\nprint('=' * 120)\n\ntraining = {\n    'grpo_alpha4_20':           {'paper': 'alpha=4.0 GRPO training, reward=0.198'},\n    'grpo_rasp_alpha3p0_20':    {'paper': 'alpha=3.0 GRPO training (v1, corrupted)'},\n    'grpo_rasp_alpha3p0_20_v2': {'paper': 'alpha=3.0 GRPO training (v2, used for eval)'},\n    'grpo_random_20_seed123':   {'paper': 'Random seed123 GRPO v1 (wrong batch_size)'},\n    'grpo_random_20_seed123_v2':{'paper': 'Random seed123 GRPO v2 (correct)'},\n    'grpo_random_20_seed456':   {'paper': 'Random seed456 GRPO'},\n    'grpo_standard_25_westb':   {'paper': 'Standard 25% GRPO, reward=0.00813 (collapse)'},\n    'sft_alpha4_20_v2':         {'paper': 'alpha=4.0 SFT, loss=0.8118'},\n    'sft_random_20':            {'paper': 'Random 20% SFT'},\n}\nfor eid, info in training.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    server = e.get('spec', {}).get('server', '?')\n    output = e.get('spec', {}).get('output_path', e.get('checkpoint_path', '?'))\n    created = e.get('created_at', '?')\n    m_str = ', '.join(f'{k}={v}' for k,v in m.items()) if m else 'NO_METRICS'\n    print(f'  {eid}')\n    print(f'    Paper: {info[\\\"paper\\\"]}')\n    print(f'    Metrics: {m_str}')\n    print(f'    Server: {server} | Created: {created}')\n    print(f'    Output: {output}')\n    print()\n\n#-----------------------------------------------------------\n# SECTION 7: 1.5B AND DEPTH-FIRST (special)\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 7: 1.5B CROSS-SCALE & DEPTH-FIRST')\nprint('=' * 120)\n\nspecial = {\n    'eval_math500_sft_standard_20_1p5b': {'paper': '1.5B Standard 20% SFT MATH-500=5.4%'},\n    'eval_gsm8k_sft_depth_first_20':     {'paper': 'Depth-first (ShortGPT?) SFT GSM8K'},\n    'eval_gsm8k_grpo_depth_first_20':    {'paper': 'Depth-first (ShortGPT?) GRPO GSM8K'},\n}\nfor eid, info in special.items():\n    e = exps.get(eid, {})\n    m = e.get('metrics', {})\n    acc = m.get('accuracy', m.get('gsm8k_accuracy', m.get('math500_accuracy', '?')))\n    if acc != '?' and isinstance(acc, (int, float)):\n        acc_pct = f'{acc*100:.1f}%'\n    else:\n        acc_pct = str(acc)\n    server = e.get('spec', {}).get('server', '?')\n    created = e.get('created_at', '?')\n    hyp = e.get('hypothesis', '')[:200]\n    m_str = ', '.join(f'{k}={v}' for k,v in m.items()) if m else 'NO_METRICS'\n    print(f'  {eid}')\n    print(f'    Paper: {info[\\\"paper\\\"]}')\n    print(f'    Metrics: {m_str}')\n    print(f'    Registry acc: {acc_pct}')\n    print(f'    Server: {server} | Created: {created}')\n    print(f'    Hypothesis: {hyp}')\n    print()\n\n#-----------------------------------------------------------\n# MISSING FROM THIS REGISTRY PAGE\n#-----------------------------------------------------------\nprint('=' * 120)\nprint('SECTION 8: PAPER VALUES NOT IN THIS REGISTRY PAGE (50 of 249 total)')\nprint('=' * 120)\n\nmissing = [\n    'CKA-only 20% SFT=63.91% (GSM8K)',\n    'CKA-only 20% GRPO mean=64.39%, seeds: 64.37%, 64.22%, 64.58% (GSM8K)',\n    'CKA-only 20% Peak Reward=0.354',\n    'Standard 20% SFT=59.29%, GRPO=59.84% (GSM8K)',\n    'Standard 20% Peak Reward=0.081',\n    'RASP alpha=1.0 SFT=61.49%, GRPO=60.88% (GSM8K)',\n    'RASP alpha=1.0 Peak Reward=0.061',\n    'ShortGPT SFT=44.73%, GRPO=43.37% (GSM8K)',\n    'Dense baseline 81.27% SFT / 90.83% original (GSM8K)',\n    'CKA-only 15% SFT=72.18%, GRPO=72.76% (GSM8K)',\n    'Standard 15% SFT=66.49%, GRPO=65.56% (GSM8K)',\n    '30% sparsity cliff: Standard=4%, RASP=0%, CKA=0%',\n    'Dense MATH-500=53.0%',\n    'RASP 20% SFT MATH-500=21.2%  <-- eval_math500_sft_rasp_alpha1p0_20_v2 = 21.2% MATCHES',\n    'Standard 25% GRPO MATH-500=12.8%',\n    'MBPP all values (Dense=53.48%, CKA SFT=12.83%, etc.)',\n    '1.5B CKA-only: Rew=0.238, GSM8K=35.48%',\n    '1.5B Standard: Rew=0.084, GSM8K=22.29%',\n    '1.5B RASP: Rew=0.099, GSM8K=26.16%',\n    'Qwen cross-arch: CKA Post-Prune=1.0%, Post-SFT=51.50%, Standard Post-Prune=18.5%, Post-SFT=21.00%',\n    'Inference efficiency values (latency, memory, TPS, etc.)',\n    'CKA stability (Spearman rho)',\n    'Gradient flow values',\n    'Extended training 300 steps',\n    'Unstructured pruning SFT=87.87%, GRPO=87.64%',\n    'alpha=1.0 GRPO GSM8K=60.88%',\n    'alpha=1.0 SFT GSM8K=61.49%',\n]\nfor m in missing:\n    print(f'  - {m}')\n\" 2>&1",
  "description": "Build complete experiment-to-paper mapping"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "6ea28679-5812-4945-9352-7f10c8ea35f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jTvGEGNxehNumZSEyCw3J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 41058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 407,
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

_source line 65 · 2026-05-23T10:50:56.924Z_

<details><summary>↩ Tool result · `toolu_01LN9qsYfmq1w6Qd5CBGurKf`</summary>

```text
========================================================================================================================
COMPLETE EXPERIMENT-TO-PAPER MAPPING
========================================================================================================================

========================================================================================================================
SECTION 1: GSM8K 7B 20% -- alpha DOSE-RESPONSE
========================================================================================================================
  eval_gsm8k_sft_alpha0p5_20
    Paper value: alpha=0.5 SFT=60.73%
    Registry:    60.73%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T10:19:48.133Z | Updated: 2026-05-22T10:20:57.690Z
    Output: ?

  eval_gsm8k_grpo_alpha0p5_20
    Paper value: alpha=0.5 GRPO=61.18%
    Registry:    61.18%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T09:28:05.478Z | Updated: 2026-05-22T09:29:23.350Z
    Output: ?

  eval_gsm8k_sft_alpha3p0_20
    Paper value: alpha=3.0 SFT=64.14%
    Registry:    64.14%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T10:24:58.696Z | Updated: 2026-05-22T12:38:25.600Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935

  eval_gsm8k_grpo_alpha3p0_20
    Paper value: alpha=3.0 GRPO=63.46%
    Registry:    63.45%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T09:30:06.630Z | Updated: 2026-05-22T14:47:06.188Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100

  eval_gsm8k_sft_alpha2p0_20
    Paper value: alpha=2.0 SFT=64.97%
    Registry:    64.97%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T10:19:50.623Z | Updated: 2026-05-22T10:22:56.503Z
    Output: ?

  eval_gsm8k_grpo_alpha2p0_20
    Paper value: alpha=2.0 GRPO=66.11%
    Registry:    66.11%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T09:28:08.089Z | Updated: 2026-05-22T09:29:24.824Z
    Output: ?

  eval_gsm8k_sft_alpha4_20_v5
    Paper value: alpha=4.0 SFT=61.94%
    Registry:    61.94%  (MATCH)
    Server: ? | Created: 2026-05-22T03:49:50.201Z | Updated: 2026-05-22T06:05:53.848Z
    Output: ?

  eval_gsm8k_grpo_alpha4_20_v3
    Paper value: alpha=4.0 GRPO=62.77%
    Registry:    62.77%  (MATCH)
    Server: westd-32935 | Created: 2026-05-22T03:49:52.414Z | Updated: 2026-05-22T05:33:39.349Z
    Output: ?

========================================================================================================================
SECTION 2: GSM8K 7B 20% -- MAIN METHOD COMPARISON
========================================================================================================================
  === Random 20% ===
  eval_gsm8k_sft_random_20
    Registry: 51.25%
    Server: westd-29022 | Created: 2026-05-21T06:47:16.459Z
    Output: N/A (eval only)

  eval_gsm8k_grpo_random_20_v2
    Registry: 50.57%
    Server: westd-29022 | Created: 2026-05-21T04:56:53.980Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100

  eval_gsm8k_grpo_random_20_seed123_v2
    Registry: ?
    Server: westd-32935 | Created: 2026-05-22T14:22:33.753Z
    Output: ?

  eval_gsm8k_grpo_random_20_seed456
    Registry: 50.87%
    Server: westb-23072 | Created: 2026-05-22T16:26:01.516Z
    Output: ?

  Paper: Random SFT=51.25%, GRPO seeds: 50.57%, 50.72%, 50.87%

========================================================================================================================
SECTION 3: GSM8K 7B CROSS-SPARSITY (25%)
========================================================================================================================
  eval_gsm8k_sft_cka_only_25
    Paper: CKA-only 25% SFT=60.12%
    Registry: 60.12%
    Server: westd-29022 | Created: 2026-05-21T06:47:14.010Z
    Output: N/A (eval only)

  eval_gsm8k_grpo_cka_only_25_v3
    Paper: CKA-only 25% GRPO=59.59%
    Registry: 59.59%
    Server: westd-29022 | Created: 2026-05-21T04:56:52.006Z
    Output: N/A (eval only)

  eval_gsm8k_sft_standard_25
    Paper: Standard 25% SFT=50.87%
    Registry: 50.87%
    Server: westd-29022 | Created: 2026-05-21T08:13:12.112Z
    Output: ?

  eval_gsm8k_grpo_standard_25
    Paper: Standard 25% GRPO=51.86%
    Registry: 51.86%
    Server: westb-23072 | Created: 2026-05-21T06:42:08.819Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100

========================================================================================================================
SECTION 4: MATH-500 EVALUATIONS
========================================================================================================================
  eval_math500_sft_cka_only_20_westd
    Paper: CKA-only 20% SFT=26.8%
    Registry: 26.8%
    Server: westd-32935 | Created: 2026-05-22T20:45:21.526Z
    Output: ?

  eval_math500_grpo_cka_only_20_2048_v2
    Paper: CKA-only 20% GRPO=27.4%
    Registry: 27.4%
    Server: westd-32935 | Created: 2026-05-23T05:07:09.002Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json

  eval_math500_grpo_cka_only_20
    Paper: CKA-only 20% GRPO=27.4% (old eval, 26.6%)
    Registry: 26.6%
    Server: ? | Created: 2026-05-18T02:41:32.199Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json

  eval_math500_sft_standard_20_2048_v2
    Paper: Standard 20% SFT=25.8%
    Registry: 25.8%
    Server: westd-32935 | Created: 2026-05-19T01:34:44.782Z
    Output: ?

  eval_math500_grpo_standard_20_fair_2048_v2
    Paper: Standard 20% GRPO=26.4%
    Registry: 26.4%
    Server: westd-32935 | Created: 2026-05-22T03:49:45.575Z
    Output: ?

  eval_math500_sft_random_20_v3
    Paper: Random 20% SFT=14.4%
    Registry: 14.4%
    Server: westd-32935 | Created: 2026-05-22T04:11:52.462Z
    Output: ?

  eval_math500_sft_rasp_alpha0p5_20
    Paper: alpha=0.5 SFT=25.4%
    Registry: 25.4%
    Server: ? | Created: 2026-05-22T15:20:44.460Z
    Output: ?

  eval_math500_grpo_rasp_alpha0p5_20
    Paper: alpha=0.5 GRPO=24.8%
    Registry: 24.8%
    Server: westb-23072 | Created: 2026-05-23T02:59:15.985Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json

  eval_math500_sft_rasp_alpha1p0_20_v2
    Paper: RASP alpha=1.0 SFT=21.2%
    Registry: 21.2%
    Server: ? | Created: 2026-05-22T20:50:24.239Z
    Output: ?

  eval_math500_grpo_rasp_alpha1p0_20
    Paper: RASP alpha=1.0 GRPO=22.6%
    Registry: 22.6%
    Server: ? | Created: 2026-05-22T23:02:44.335Z
    Output: ?

  eval_math500_sft_rasp_alpha2p0_20
    Paper: alpha=2.0 SFT=24.0%
    Registry: 24.0%
    Server: westd-32935 | Created: 2026-05-22T15:06:22.386Z
    Output: ?

  eval_math500_grpo_rasp_alpha2p0_20
    Paper: alpha=2.0 GRPO=26.2%
    Registry: 26.2%
    Server: westd-32935 | Created: 2026-05-22T22:23:27.589Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20

  eval_math500_sft_rasp_alpha3p0_20
    Paper: alpha=3.0 SFT=23.2%
    Registry: 23.2%
    Server: ? | Created: 2026-05-22T18:26:16.273Z
    Output: ?

  eval_math500_grpo_rasp_alpha3p0_20
    Paper: alpha=3.0 GRPO=22.8%
    Registry: 22.8%
    Server: westd-32935 | Created: 2026-05-23T03:19:40.950Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json

  eval_math500_sft_rasp_alpha4p0_20
    Paper: alpha=4.0 SFT=26.6%
    Registry: 26.6%
    Server: ? | Created: 2026-05-22T15:20:47.150Z
    Output: ?

  eval_math500_grpo_rasp_alpha4p0_20
    Paper: alpha=4.0 GRPO=26.2%
    Registry: 26.2%
    Server: ? | Created: 2026-05-23T00:01:54.194Z
    Output: ?

  eval_math500_sft_cka_only_25_v2
    Paper: CKA-only 25% SFT=19.2%
    Registry: 19.2%
    Server: westd-29022 | Created: 2026-05-21T13:54:51.945Z
    Output: N/A (eval only)

  eval_math500_grpo_cka_only_25_v2
    Paper: CKA-only 25% GRPO=18.4%
    Registry: 18.4%
    Server: westd-29022 | Created: 2026-05-21T13:54:50.310Z
    Output: N/A (eval only)

  eval_math500_sft_standard_25
    Paper: Standard 25% SFT=14.0%
    Registry: 14.0%
    Server: westb-23072 | Created: 2026-05-21T02:58:32.492Z
    Output: ?

========================================================================================================================
SECTION 5: CROSS-ARCHITECTURE (Qwen2.5-Math-7B)
========================================================================================================================
  eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3
    Paper: CKA-only GRPO GSM8K (N=500)
    Registry: 48.6%
    Server: westb-23072 | Created: 2026-05-22T15:12:46.181Z

  eval_math500_sft_qwen_math_cka_only_20
    Paper: CKA-only SFT MATH-500=21.6%
    Registry: 21.6%
    Server: westb-23072 | Created: 2026-05-22T23:11:09.017Z

  grpo_qwen_math_cka_only_20
    Paper: CKA-only GRPO training
    Registry: ?
    Server: westb-23072 | Created: 2026-05-22T08:50:34.293Z

========================================================================================================================
SECTION 6: TRAINING RUNS (GRPO/SFT)
========================================================================================================================
  grpo_alpha4_20
    Paper: alpha=4.0 GRPO training, reward=0.198
    Metrics: final_reward=0.198, reward_range=0.146-0.256, steps=100, final_loss=0.018, final_kl=0.00198
    Server: westd-29022 | Created: 2026-05-21T18:59:18.863Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100

  grpo_rasp_alpha3p0_20
    Paper: alpha=3.0 GRPO training (v1, corrupted)
    Metrics: NO_METRICS
    Server: westb-23072 | Created: 2026-05-22T08:48:06.001Z
    Output: ?

  grpo_rasp_alpha3p0_20_v2
    Paper: alpha=3.0 GRPO training (v2, used for eval)
    Metrics: NO_METRICS
    Server: westd-32935 | Created: 2026-05-22T10:40:19.362Z
    Output: ?

  grpo_random_20_seed123
    Paper: Random seed123 GRPO v1 (wrong batch_size)
    Metrics: NO_METRICS
    Server: westd-32935 | Created: 2026-05-22T10:34:12.100Z
    Output: ?

  grpo_random_20_seed123_v2
    Paper: Random seed123 GRPO v2 (correct)
    Metrics: NO_METRICS
    Server: westd-32935 | Created: 2026-05-22T14:22:29.868Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100

  grpo_random_20_seed456
    Paper: Random seed456 GRPO
    Metrics: NO_METRICS
    Server: westb-23072 | Created: 2026-05-22T12:00:38.940Z
    Output: ?

  grpo_standard_25_westb
    Paper: Standard 25% GRPO, reward=0.00813 (collapse)
    Metrics: reward=0.00813, steps=100, collapse_pattern=near_total_collapse
    Server: westb-23072 | Created: 2026-05-21T03:00:00.000Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100

  sft_alpha4_20_v2
    Paper: alpha=4.0 SFT, loss=0.8118
    Metrics: final_train_loss=0.8118, token_accuracy=0.8165, epochs=2, steps=936
    Server: westd-29022 | Created: 2026-05-21T18:30:48.284Z
    Output: ?

  sft_random_20
    Paper: Random 20% SFT
    Metrics: steps=1870, model_size_gb=12
    Server: westd-29022 | Created: 2026-05-21T03:44:24.654Z
    Output: /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20

========================================================================================================================
SECTION 7: 1.5B CROSS-SCALE & DEPTH-FIRST
========================================================================================================================
  eval_math500_sft_standard_20_1p5b
    Paper: 1.5B Standard 20% SFT MATH-500=5.4%
    Metrics: math500_accuracy=0.054, correct=27, total=500, truncated=335
    Registry acc: 5.4%
    Server: westb-23072 | Created: 2026-05-22T04:31:30.202Z
    Hypothesis: 1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.

  eval_gsm8k_sft_depth_first_20
    Paper: Depth-first (ShortGPT?) SFT GSM8K
    Metrics: NO_METRICS
    Registry acc: ?
    Server: westd-32935 | Created: 2026-05-22T14:20:43.950Z
    Hypothesis: MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.

  eval_gsm8k_grpo_depth_first_20
    Paper: Depth-first (ShortGPT?) GRPO GSM8K
    Metrics: NO_METRICS
    Registry acc: ?
    Server: westd-32935 | Created: 2026-05-22T14:20:41.126Z
    Hypothesis: MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior 

========================================================================================================================
SECTION 8: PAPER VALUES NOT IN THIS REGISTRY PAGE (50 of 249 total)
========================================================================================================================
  - CKA-only 20% SFT=63.91% (GSM8K)
  - CKA-only 20% GRPO mean=64.39%, seeds: 64.37%, 64.22%, 64.58% (GSM8K)
  - CKA-only 20% Peak Reward=0.354
  - Standard 20% SFT=59.29%, GRPO=59.84% (GSM8K)
  - Standard 20% Peak Reward=0.081
  - RASP alpha=1.0 SFT=61.49%, GRPO=60.88% (GSM8K)
  - RASP alpha=1.0 Peak Reward=0.061
  - ShortGPT SFT=44.73%, GRPO=43.37% (GSM8K)
  - Dense baseline 81.27% SFT / 90.83% original (GSM8K)
  - CKA-only 15% SFT=72.18%, GRPO=72.76% (GSM8K)
  - Standard 15% SFT=66.49%, GRPO=65.56% (GSM8K)
  - 30% sparsity cliff: Standard=4%, RASP=0%, CKA=0%
  - Dense MATH-500=53.0%
  - RASP 20% SFT MATH-500=21.2%  <-- eval_math500_sft_rasp_alpha1p0_20_v2 = 21.2% MATCHES
  - Standard 25% GRPO MATH-500=12.8%
  - MBPP all values (Dense=53.48%, CKA SFT=12.83%, etc.)
  - 1.5B CKA-only: Rew=0.238, GSM8K=35.48%
  - 1.5B Standard: Rew=0.084, GSM8K=22.29%
  - 1.5B RASP: Rew=0.099, GSM8K=26.16%
  - Qwen cross-arch: CKA Post-Prune=1.0%, Post-SFT=51.50%, Standard Post-Prune=18.5%, Post-SFT=21.00%
  - Inference efficiency values (latency, memory, TPS, etc.)
  - CKA stability (Spearman rho)
  - Gradient flow values
  - Extended training 300 steps
  - Unstructured pruning SFT=87.87%, GRPO=87.64%
  - alpha=1.0 GRPO GSM8K=60.88%
  - alpha=1.0 SFT GSM8K=61.49%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "07ae0338-a94b-4a4c-94de-b45ebae4af91"
}
```

</details>

---


### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad6a32a709aac350a",
  "tool_use_id": "toolu_01Nf8X2QpYuR5f2HKgrP8EYj",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry JSON for provenance",
  "usage": {
    "total_tokens": 53068,
    "tool_uses": 8,
    "duration_ms": 206810
  },
  "uuid": "a9a70bc1-9a40-4486-8e66-3add875dfca4",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool result

_source line 67 · 2026-05-23T10:52:10.480Z_

<details><summary>↩ Tool result · `toolu_01Nf8X2QpYuR5f2HKgrP8EYj`</summary>

```text
Here is the complete structured mapping of all 50 experiments in this registry page to their paper values.

---

## Summary of Findings

**Total experiments in registry:** 249 (only 50 returned in this page -- the most recent ones)

### Experiments Successfully Matched to Paper Values (43 of 50)

**All metric matches are EXACT** -- every registry value matches its corresponding paper value precisely.

---

### SECTION 1: GSM8K 7B 20% -- Alpha Dose-Response (8 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_alpha0p5_20` | alpha=0.5 SFT=60.73% | 60.73% | westd-32935 | 2026-05-22T10:19 |
| `eval_gsm8k_grpo_alpha0p5_20` | alpha=0.5 GRPO=61.18% | 61.18% | westd-32935 | 2026-05-22T09:28 |
| `eval_gsm8k_sft_alpha2p0_20` | alpha=2.0 SFT=64.97% | 64.97% | westd-32935 | 2026-05-22T10:19 |
| `eval_gsm8k_grpo_alpha2p0_20` | alpha=2.0 GRPO=66.11% | 66.11% | westd-32935 | 2026-05-22T09:28 |
| `eval_gsm8k_sft_alpha3p0_20` | alpha=3.0 SFT=64.14% | 64.14% | westd-32935 | 2026-05-22T10:24 |
| `eval_gsm8k_grpo_alpha3p0_20` | alpha=3.0 GRPO=63.46% | 63.45% (rounding) | westd-32935 | 2026-05-22T09:30 |
| `eval_gsm8k_sft_alpha4_20_v5` | alpha=4.0 SFT=61.94% | 61.94% | ? (westd-32935 per hypothesis) | 2026-05-22T03:49 |
| `eval_gsm8k_grpo_alpha4_20_v3` | alpha=4.0 GRPO=62.77% | 62.77% | westd-32935 | 2026-05-22T03:49 |

**Key paths:** alpha=3.0 GRPO model at `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100`

---

### SECTION 2: GSM8K 7B 20% -- Random Pruning Multi-Seed (4 experiments)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_random_20` | Random SFT=51.25% | 51.25% | westd-29022 | 2026-05-21T06:47 |
| `eval_gsm8k_grpo_random_20_v2` | Random GRPO seed42=50.57% | 50.57% | westd-29022 | 2026-05-21T04:56 |
| `eval_gsm8k_grpo_random_20_seed123_v2` | Random GRPO seed123=50.72% | NO_METRICS in registry | westd-32935 | 2026-05-22T14:22 |
| `eval_gsm8k_grpo_random_20_seed456` | Random GRPO seed456=50.87% | 50.87% | westb-23072 | 2026-05-22T16:26 |

**Note:** `eval_gsm8k_grpo_random_20_seed123_v2` has status=DONE, conclusion=success, but NO_METRICS recorded in registry. The paper value 50.72% likely came from the result JSON file on disk.

---

### SECTION 3: GSM8K 7B 25% Cross-Sparsity (4 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_sft_cka_only_25` | CKA-only 25% SFT=60.12% | 60.12% | westd-29022 | 2026-05-21T06:47 |
| `eval_gsm8k_grpo_cka_only_25_v3` | CKA-only 25% GRPO=59.59% | 59.59% | westd-29022 | 2026-05-21T04:56 |
| `eval_gsm8k_sft_standard_25` | Standard 25% SFT=50.87% | 50.87% | westd-29022 | 2026-05-21T08:13 |
| `eval_gsm8k_grpo_standard_25` | Standard 25% GRPO=51.86% | 51.86% | westb-23072 | 2026-05-21T06:42 |

---

### SECTION 4: MATH-500 Evaluations (19 experiments, ALL MATCH)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_math500_sft_cka_only_20_westd` | CKA-only 20% SFT=26.8% | 26.8% | westd-32935 | 2026-05-22T20:45 |
| `eval_math500_grpo_cka_only_20_2048_v2` | CKA-only 20% GRPO=27.4% | 27.4% | westd-32935 | 2026-05-23T05:07 |
| `eval_math500_grpo_cka_only_20` | (old eval script) | 26.6% | ? | 2026-05-18T02:41 |
| `eval_math500_sft_standard_20_2048_v2` | Standard 20% SFT=25.8% | 25.8% | westd-32935 | 2026-05-19T01:34 |
| `eval_math500_grpo_standard_20_fair_2048_v2` | Standard 20% GRPO=26.4% | 26.4% | westd-32935 | 2026-05-22T03:49 |
| `eval_math500_sft_random_20_v3` | Random 20% SFT=14.4% | 14.4% | westd-32935 | 2026-05-22T04:11 |
| `eval_math500_sft_rasp_alpha0p5_20` | alpha=0.5 SFT=25.4% | 25.4% | ? | 2026-05-22T15:20 |
| `eval_math500_grpo_rasp_alpha0p5_20` | alpha=0.5 GRPO=24.8% | 24.8% | westb-23072 | 2026-05-23T02:59 |
| `eval_math500_sft_rasp_alpha1p0_20_v2` | RASP SFT=21.2% | 21.2% | ? | 2026-05-22T20:50 |
| `eval_math500_grpo_rasp_alpha1p0_20` | RASP GRPO=22.6% | 22.6% | ? | 2026-05-22T23:02 |
| `eval_math500_sft_rasp_alpha2p0_20` | alpha=2.0 SFT=24.0% | 24.0% | westd-32935 | 2026-05-22T15:06 |
| `eval_math500_grpo_rasp_alpha2p0_20` | alpha=2.0 GRPO=26.2% | 26.2% | westd-32935 | 2026-05-22T22:23 |
| `eval_math500_sft_rasp_alpha3p0_20` | alpha=3.0 SFT=23.2% | 23.2% | ? | 2026-05-22T18:26 |
| `eval_math500_grpo_rasp_alpha3p0_20` | alpha=3.0 GRPO=22.8% | 22.8% | westd-32935 | 2026-05-23T03:19 |
| `eval_math500_sft_rasp_alpha4p0_20` | alpha=4.0 SFT=26.6% | 26.6% | ? | 2026-05-22T15:20 |
| `eval_math500_grpo_rasp_alpha4p0_20` | alpha=4.0 GRPO=26.2% | 26.2% | ? | 2026-05-23T00:01 |
| `eval_math500_sft_cka_only_25_v2` | CKA-only 25% SFT=19.2% | 19.2% | westd-29022 | 2026-05-21T13:54 |
| `eval_math500_grpo_cka_only_25_v2` | CKA-only 25% GRPO=18.4% | 18.4% | westd-29022 | 2026-05-21T13:54 |
| `eval_math500_sft_standard_25` | Standard 25% SFT=14.0% | 14.0% | westb-23072 | 2026-05-21T02:58 |

**Note:** `eval_math500_grpo_cka_only_20` (26.6%) was from an OLD eval script. The paper uses `eval_math500_grpo_cka_only_20_2048_v2` (27.4%) which used the NEW consistent answer extraction.

---

### SECTION 5: Cross-Architecture Qwen2.5-Math-7B (3 experiments)

| exp_id | Paper Value | Registry Value | Server | Created |
|--------|------------|----------------|--------|---------|
| `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` | CKA-only GRPO GSM8K (N=500) | 48.6% | westb-23072 | 2026-05-22T15:12 |
| `eval_math500_sft_qwen_math_cka_only_20` | CKA-only SFT MATH-500 | 21.6% | westb-23072 | 2026-05-22T23:11 |
| `grpo_qwen_math_cka_only_20` | GRPO training run | NO_METRICS | westb-23072 | 2026-05-22T08:50 |

**Note:** The paper reports Qwen CKA-only Post-SFT=51.50% for GSM8K but this was N=200. The registry `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` is N=500 with 48.6% and 83.8% truncation, suggesting max_new_tokens=2048 was insufficient for Qwen-Math's verbose reasoning.

---

### SECTION 6: Training Runs (9 experiments)

| exp_id | Key Metrics | Server | Output Path |
|--------|------------|--------|-------------|
| `grpo_alpha4_20` | reward=0.198, kl=0.00198 | westd-29022 | `/root/autodl-tmp/.../grpo_alpha4_20/checkpoint-100` |
| `grpo_rasp_alpha3p0_20` | (v1 corrupted by disk-full) | westb-23072 | ? |
| `grpo_rasp_alpha3p0_20_v2` | (v2 used for eval) | westd-32935 | ? |
| `grpo_random_20_seed123` | (v1 wrong batch_size=1) | westd-32935 | ? |
| `grpo_random_20_seed123_v2` | (v2 correct batch_size=2) | westd-32935 | `/root/autodl-tmp/.../grpo_random_20_seed123_v2/checkpoint-100` |
| `grpo_random_20_seed456` | seed456 GRPO | westb-23072 | ? |
| `grpo_standard_25_westb` | reward=0.00813, collapse | westb-23072 | `/root/autodl-tmp/.../grpo_standard_25_westb/checkpoint-100` |
| `sft_alpha4_20_v2` | loss=0.8118, tok_acc=0.8165 | westd-29022 | ? |
| `sft_random_20` | 1870 steps, 12GB | westd-29022 | `/root/autodl-tmp/.../sft_random_20` |

---

### SECTION 7: 1.5B and Depth-First (3 experiments)

| exp_id | Paper Value | Registry Value | Server |
|--------|------------|----------------|--------|
| `eval_math500_sft_standard_20_1p5b` | 1.5B Standard MATH-500=5.4% | 5.4% | westb-23072 |
| `eval_gsm8k_sft_depth_first_20` | ShortGPT SFT GSM8K | NO_METRICS (disk-full) | westd-32935 |
| `eval_gsm8k_grpo_depth_first_20` | ShortGPT GRPO GSM8K | NO_METRICS (disk-full) | westd-32935 |

---

### SECTION 8: Paper Values NOT in This Registry Page

The registry only returned 50 of 249 total experiments. The following paper values are sourced from the other 199 experiments not in this page:

- **GSM8K 7B 20% core results:** CKA-only (SFT=63.91%, GRPO=64.37/64.22/64.58%), Standard (SFT=59.29%, GRPO=59.84%), RASP alpha=1.0 (SFT=61.49%, GRPO=60.88%), ShortGPT (SFT=44.73%, GRPO=43.37%), Dense (81.27%/90.83%)
- **GSM8K 15% sparsity:** CKA-only (72.18%/72.76%), Standard (66.49%/65.56%)
- **GSM8K 30% sparsity cliff:** Standard=4%, RASP=0%, CKA=0%
- **Peak rewards:** CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190
- **MATH-500:** Dense=53.0%, Standard 25% GRPO=12.8%
- **MBPP:** All values
- **1.5B cross-scale:** CKA (GSM8K=35.48%, Rew=0.238), Standard (22.29%, 0.084), RASP (26.16%, 0.099)
- **Qwen cross-arch:** CKA Post-Prune=1.0%, Standard Post-Prune=18.5%, Standard Post-SFT=21.00%
- **Infrastructure:** Inference efficiency, CKA stability, gradient flow, extended training, unstructured pruning

---

### Servers Used

- **westd-32935**: Primary compute, most dose-response and MATH-500 evals
- **westd-29022**: Earlier runs (25% sparsity, some 20% baselines) -- had an outage requiring re-runs on westd-32935
- **westb-23072**: Qwen cross-architecture, some seed456/standard runs

### Key Observations

1. **One minor rounding discrepancy:** alpha=3.0 GRPO registry=63.45% vs paper=63.46% (837/1319 = 63.456%, paper rounded up)
2. **3 experiments with NO_METRICS** despite DONE status: `eval_gsm8k_grpo_random_20_seed123_v2`, `eval_gsm8k_sft_depth_first_20`, `eval_gsm8k_grpo_depth_first_20` -- results exist in JSON files on disk but weren't recorded to registry
3. **`eval_math500_grpo_cka_only_20`** (26.6%) was superseded by **`eval_math500_grpo_cka_only_20_2048_v2`** (27.4%) after switching to new answer extraction code
4. **Multiple version chains** visible (v1->v2->v3) due to server outages (westd-29022), disk-full errors, batch_size misconfigurations, and eval script updates

agentId: ad6a32a709aac350a (use SendMessage with to: 'ad6a32a709aac350a' to continue this agent)
&lt;usage>total_tokens: 57351
tool_uses: 8
duration_ms: 206813&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "d198add0-0891-4741-9031-765a77b8407b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to parse a large JSON file containing experiment registry data and extract structured information for building a data provenance table.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533249026.txt`\n\nThe file is JSON with schema: `{result: string}`. The `result` field is itself a string that contains the actual data (likely JSON or YAML).\n\n**What to extract for each experiment:**\n1. `exp_id`\n2. `status` and `conclusion`\n3. `metrics` (any accuracy, reward, etc.)\n4. `spec` fields: `server`, `output_path`, `checkpoint_path`, `log_path`, `command`\n5. `created_at` or `updated_at` timestamps\n6. `tags` or any other identifying info\n\n**What I need mapped:**\nI need to match these experiments to paper values. The paper has these key experiments:\n\n**GSM8K 7B 20% sparsity:**\n- CKA-only: SFT=63.91%, GRPO=64.39% (3 seeds: 64.37%, 64.22%, 64.58%), Peak Rew=0.354\n- Standard: SFT=59.29%, GRPO=59.84% (3 seeds), Peak Rew=0.081\n- RASP (α=1.0): SFT=61.49%, GRPO=60.88%, Peak Rew=0.061\n- Random: SFT=51.25%, GRPO=50.72% (3 seeds: 50.57%, 50.72%, 50.87%), Peak Rew=0.190\n- ShortGPT: SFT=44.73%, GRPO=43.37%\n- Unpruned/Dense: 81.27% (SFT) or 90.83% (original)\n\n**GSM8K 7B α dose-response:**\n- α=0.5: SFT=60.73%, GRPO=61.18%\n- α=1.0: SFT=61.49%, GRPO=60.88%\n- α=2.0: SFT=64.97%, GRPO=66.11%\n- α=3.0: SFT=64.14%, GRPO=63.46%\n- α=4.0: SFT=61.94%, GRPO=62.77%\n\n**GSM8K 7B 15% sparsity:**\n- CKA-only: SFT=72.18%, GRPO=72.76% (3 seeds)\n- Standard: SFT=66.49%, GRPO=65.56% (3 seeds)\n\n**GSM8K 7B 25% sparsity:**\n- CKA-only: SFT=60.12%, GRPO=59.59%\n- Standard: SFT=50.87%, GRPO=51.86%\n\n**GSM8K 7B 30% sparsity (cliff):**\n- Standard: 4%\n- RASP: 0%\n- CKA-only: 0%\n\n**MATH-500 evaluations:**\n- Dense: 53.0%\n- CKA-only 20%: SFT=26.8%, GRPO=27.4%\n- Standard 20%: SFT=25.8%, GRPO=26.4%\n- RASP 20%: SFT=21.2%, GRPO=22.6%\n- Random 20%: SFT=14.4%\n- α=0.5: SFT=25.4%, GRPO=24.8%\n- α=2.0: SFT=24.0%, GRPO=26.2%\n- α=3.0: SFT=23.2%, GRPO=22.8%\n- α=4.0: SFT=26.6%, GRPO=26.2%\n- CKA-only 25%: SFT=19.2%, GRPO=18.4%\n- Standard 25%: SFT=14.0%, GRPO=12.8%\n\n**MBPP evaluations:**\n- Dense: 53.48%\n- CKA-only 20%: SFT=12.83%, GRPO=14.17%\n- Standard 20%: SFT=12.03%, GRPO=13.10%\n- RASP 20%: SFT=11.76%, GRPO=13.10%\n- ShortGPT 20%: SFT=10.43%, GRPO=14.44%\n\n**1.5B cross-scale:**\n- CKA-only: Rew=0.238, GSM8K=35.48%\n- Standard: Rew=0.084, GSM8K=22.29%\n- RASP: Rew=0.099, GSM8K=26.16%\n\n**Cross-architecture (Qwen2.5-Math-7B):**\n- CKA-only: Post-Prune=1.0%, Post-SFT=51.50%\n- Standard: Post-Prune=18.5%, Post-SFT=21.00%\n\n**Inference efficiency:**\n- Dense: Latency=6.682s, Memory=16.22GB, TPS=72.0, TTFT=20.1ms, Per-token=13.9ms, Params=7.62B\n- RASP 20%: Latency=4.156s, Speedup=37.8%, Memory=11.60GB\n- Standard 20%: Latency=6.167s, Speedup=7.7%, Memory=11.61GB\n- CKA-only 20%: TPS=58.3, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n- Standard 20%: TPS=58.2, TTFT=16.4ms, Per-token=16.7ms, Params=6.16B\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n\n**Gradient flow:**\n- CKA vs Standard: 2.89×, 55/56\n- CKA vs RASP: 2.26×, 56/56\n- RASP vs Standard: 1.28×, 45/56\n\n**Extended training 300 steps:**\n- CKA-only: 64.37%→64.37%\n- Standard: 59.44%→59.29%\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n\n**Instructions:**\n1. First probe the file structure with `jq` to understand the format\n2. Parse the `result` field content\n3. For each experiment, output a line with: `exp_id | metrics_summary | server | output_path | created_at/updated_at`\n4. Try to match experiments to the paper values above\n5. Output the COMPLETE list of all experiments with their details - don't summarize or truncate\n\nOutput the full results as a structured mapping. Be thorough - I need every experiment matched.",
    "agentId": "ad6a32a709aac350a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete structured mapping of all 50 experiments in this registry page to their paper values.\n\n---\n\n## Summary of Findings\n\n**Total experiments in registry:** 249 (only 50 returned in this page -- the most recent ones)\n\n### Experiments Successfully Matched to Paper Values (43 of 50)\n\n**All metric matches are EXACT** -- every registry value matches its corresponding paper value precisely.\n\n---\n\n### SECTION 1: GSM8K 7B 20% -- Alpha Dose-Response (8 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_alpha0p5_20` | alpha=0.5 SFT=60.73% | 60.73% | westd-32935 | 2026-05-22T10:19 |\n| `eval_gsm8k_grpo_alpha0p5_20` | alpha=0.5 GRPO=61.18% | 61.18% | westd-32935 | 2026-05-22T09:28 |\n| `eval_gsm8k_sft_alpha2p0_20` | alpha=2.0 SFT=64.97% | 64.97% | westd-32935 | 2026-05-22T10:19 |\n| `eval_gsm8k_grpo_alpha2p0_20` | alpha=2.0 GRPO=66.11% | 66.11% | westd-32935 | 2026-05-22T09:28 |\n| `eval_gsm8k_sft_alpha3p0_20` | alpha=3.0 SFT=64.14% | 64.14% | westd-32935 | 2026-05-22T10:24 |\n| `eval_gsm8k_grpo_alpha3p0_20` | alpha=3.0 GRPO=63.46% | 63.45% (rounding) | westd-32935 | 2026-05-22T09:30 |\n| `eval_gsm8k_sft_alpha4_20_v5` | alpha=4.0 SFT=61.94% | 61.94% | ? (westd-32935 per hypothesis) | 2026-05-22T03:49 |\n| `eval_gsm8k_grpo_alpha4_20_v3` | alpha=4.0 GRPO=62.77% | 62.77% | westd-32935 | 2026-05-22T03:49 |\n\n**Key paths:** alpha=3.0 GRPO model at `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100`\n\n---\n\n### SECTION 2: GSM8K 7B 20% -- Random Pruning Multi-Seed (4 experiments)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_random_20` | Random SFT=51.25% | 51.25% | westd-29022 | 2026-05-21T06:47 |\n| `eval_gsm8k_grpo_random_20_v2` | Random GRPO seed42=50.57% | 50.57% | westd-29022 | 2026-05-21T04:56 |\n| `eval_gsm8k_grpo_random_20_seed123_v2` | Random GRPO seed123=50.72% | NO_METRICS in registry | westd-32935 | 2026-05-22T14:22 |\n| `eval_gsm8k_grpo_random_20_seed456` | Random GRPO seed456=50.87% | 50.87% | westb-23072 | 2026-05-22T16:26 |\n\n**Note:** `eval_gsm8k_grpo_random_20_seed123_v2` has status=DONE, conclusion=success, but NO_METRICS recorded in registry. The paper value 50.72% likely came from the result JSON file on disk.\n\n---\n\n### SECTION 3: GSM8K 7B 25% Cross-Sparsity (4 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_sft_cka_only_25` | CKA-only 25% SFT=60.12% | 60.12% | westd-29022 | 2026-05-21T06:47 |\n| `eval_gsm8k_grpo_cka_only_25_v3` | CKA-only 25% GRPO=59.59% | 59.59% | westd-29022 | 2026-05-21T04:56 |\n| `eval_gsm8k_sft_standard_25` | Standard 25% SFT=50.87% | 50.87% | westd-29022 | 2026-05-21T08:13 |\n| `eval_gsm8k_grpo_standard_25` | Standard 25% GRPO=51.86% | 51.86% | westb-23072 | 2026-05-21T06:42 |\n\n---\n\n### SECTION 4: MATH-500 Evaluations (19 experiments, ALL MATCH)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_math500_sft_cka_only_20_westd` | CKA-only 20% SFT=26.8% | 26.8% | westd-32935 | 2026-05-22T20:45 |\n| `eval_math500_grpo_cka_only_20_2048_v2` | CKA-only 20% GRPO=27.4% | 27.4% | westd-32935 | 2026-05-23T05:07 |\n| `eval_math500_grpo_cka_only_20` | (old eval script) | 26.6% | ? | 2026-05-18T02:41 |\n| `eval_math500_sft_standard_20_2048_v2` | Standard 20% SFT=25.8% | 25.8% | westd-32935 | 2026-05-19T01:34 |\n| `eval_math500_grpo_standard_20_fair_2048_v2` | Standard 20% GRPO=26.4% | 26.4% | westd-32935 | 2026-05-22T03:49 |\n| `eval_math500_sft_random_20_v3` | Random 20% SFT=14.4% | 14.4% | westd-32935 | 2026-05-22T04:11 |\n| `eval_math500_sft_rasp_alpha0p5_20` | alpha=0.5 SFT=25.4% | 25.4% | ? | 2026-05-22T15:20 |\n| `eval_math500_grpo_rasp_alpha0p5_20` | alpha=0.5 GRPO=24.8% | 24.8% | westb-23072 | 2026-05-23T02:59 |\n| `eval_math500_sft_rasp_alpha1p0_20_v2` | RASP SFT=21.2% | 21.2% | ? | 2026-05-22T20:50 |\n| `eval_math500_grpo_rasp_alpha1p0_20` | RASP GRPO=22.6% | 22.6% | ? | 2026-05-22T23:02 |\n| `eval_math500_sft_rasp_alpha2p0_20` | alpha=2.0 SFT=24.0% | 24.0% | westd-32935 | 2026-05-22T15:06 |\n| `eval_math500_grpo_rasp_alpha2p0_20` | alpha=2.0 GRPO=26.2% | 26.2% | westd-32935 | 2026-05-22T22:23 |\n| `eval_math500_sft_rasp_alpha3p0_20` | alpha=3.0 SFT=23.2% | 23.2% | ? | 2026-05-22T18:26 |\n| `eval_math500_grpo_rasp_alpha3p0_20` | alpha=3.0 GRPO=22.8% | 22.8% | westd-32935 | 2026-05-23T03:19 |\n| `eval_math500_sft_rasp_alpha4p0_20` | alpha=4.0 SFT=26.6% | 26.6% | ? | 2026-05-22T15:20 |\n| `eval_math500_grpo_rasp_alpha4p0_20` | alpha=4.0 GRPO=26.2% | 26.2% | ? | 2026-05-23T00:01 |\n| `eval_math500_sft_cka_only_25_v2` | CKA-only 25% SFT=19.2% | 19.2% | westd-29022 | 2026-05-21T13:54 |\n| `eval_math500_grpo_cka_only_25_v2` | CKA-only 25% GRPO=18.4% | 18.4% | westd-29022 | 2026-05-21T13:54 |\n| `eval_math500_sft_standard_25` | Standard 25% SFT=14.0% | 14.0% | westb-23072 | 2026-05-21T02:58 |\n\n**Note:** `eval_math500_grpo_cka_only_20` (26.6%) was from an OLD eval script. The paper uses `eval_math500_grpo_cka_only_20_2048_v2` (27.4%) which used the NEW consistent answer extraction.\n\n---\n\n### SECTION 5: Cross-Architecture Qwen2.5-Math-7B (3 experiments)\n\n| exp_id | Paper Value | Registry Value | Server | Created |\n|--------|------------|----------------|--------|---------|\n| `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` | CKA-only GRPO GSM8K (N=500) | 48.6% | westb-23072 | 2026-05-22T15:12 |\n| `eval_math500_sft_qwen_math_cka_only_20` | CKA-only SFT MATH-500 | 21.6% | westb-23072 | 2026-05-22T23:11 |\n| `grpo_qwen_math_cka_only_20` | GRPO training run | NO_METRICS | westb-23072 | 2026-05-22T08:50 |\n\n**Note:** The paper reports Qwen CKA-only Post-SFT=51.50% for GSM8K but this was N=200. The registry `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3` is N=500 with 48.6% and 83.8% truncation, suggesting max_new_tokens=2048 was insufficient for Qwen-Math's verbose reasoning.\n\n---\n\n### SECTION 6: Training Runs (9 experiments)\n\n| exp_id | Key Metrics | Server | Output Path |\n|--------|------------|--------|-------------|\n| `grpo_alpha4_20` | reward=0.198, kl=0.00198 | westd-29022 | `/root/autodl-tmp/.../grpo_alpha4_20/checkpoint-100` |\n| `grpo_rasp_alpha3p0_20` | (v1 corrupted by disk-full) | westb-23072 | ? |\n| `grpo_rasp_alpha3p0_20_v2` | (v2 used for eval) | westd-32935 | ? |\n| `grpo_random_20_seed123` | (v1 wrong batch_size=1) | westd-32935 | ? |\n| `grpo_random_20_seed123_v2` | (v2 correct batch_size=2) | westd-32935 | `/root/autodl-tmp/.../grpo_random_20_seed123_v2/checkpoint-100` |\n| `grpo_random_20_seed456` | seed456 GRPO | westb-23072 | ? |\n| `grpo_standard_25_westb` | reward=0.00813, collapse | westb-23072 | `/root/autodl-tmp/.../grpo_standard_25_westb/checkpoint-100` |\n| `sft_alpha4_20_v2` | loss=0.8118, tok_acc=0.8165 | westd-29022 | ? |\n| `sft_random_20` | 1870 steps, 12GB | westd-29022 | `/root/autodl-tmp/.../sft_random_20` |\n\n---\n\n### SECTION 7: 1.5B and Depth-First (3 experiments)\n\n| exp_id | Paper Value | Registry Value | Server |\n|--------|------------|----------------|--------|\n| `eval_math500_sft_standard_20_1p5b` | 1.5B Standard MATH-500=5.4% | 5.4% | westb-23072 |\n| `eval_gsm8k_sft_depth_first_20` | ShortGPT SFT GSM8K | NO_METRICS (disk-full) | westd-32935 |\n| `eval_gsm8k_grpo_depth_first_20` | ShortGPT GRPO GSM8K | NO_METRICS (disk-full) | westd-32935 |\n\n---\n\n### SECTION 8: Paper Values NOT in This Registry Page\n\nThe registry only returned 50 of 249 total experiments. The following paper values are sourced from the other 199 experiments not in this page:\n\n- **GSM8K 7B 20% core results:** CKA-only (SFT=63.91%, GRPO=64.37/64.22/64.58%), Standard (SFT=59.29%, GRPO=59.84%), RASP alpha=1.0 (SFT=61.49%, GRPO=60.88%), ShortGPT (SFT=44.73%, GRPO=43.37%), Dense (81.27%/90.83%)\n- **GSM8K 15% sparsity:** CKA-only (72.18%/72.76%), Standard (66.49%/65.56%)\n- **GSM8K 30% sparsity cliff:** Standard=4%, RASP=0%, CKA=0%\n- **Peak rewards:** CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190\n- **MATH-500:** Dense=53.0%, Standard 25% GRPO=12.8%\n- **MBPP:** All values\n- **1.5B cross-scale:** CKA (GSM8K=35.48%, Rew=0.238), Standard (22.29%, 0.084), RASP (26.16%, 0.099)\n- **Qwen cross-arch:** CKA Post-Prune=1.0%, Standard Post-Prune=18.5%, Standard Post-SFT=21.00%\n- **Infrastructure:** Inference efficiency, CKA stability, gradient flow, extended training, unstructured pruning\n\n---\n\n### Servers Used\n\n- **westd-32935**: Primary compute, most dose-response and MATH-500 evals\n- **westd-29022**: Earlier runs (25% sparsity, some 20% baselines) -- had an outage requiring re-runs on westd-32935\n- **westb-23072**: Qwen cross-architecture, some seed456/standard runs\n\n### Key Observations\n\n1. **One minor rounding discrepancy:** alpha=3.0 GRPO registry=63.45% vs paper=63.46% (837/1319 = 63.456%, paper rounded up)\n2. **3 experiments with NO_METRICS** despite DONE status: `eval_gsm8k_grpo_random_20_seed123_v2`, `eval_gsm8k_sft_depth_first_20`, `eval_gsm8k_grpo_depth_first_20` -- results exist in JSON files on disk but weren't recorded to registry\n3. **`eval_math500_grpo_cka_only_20`** (26.6%) was superseded by **`eval_math500_grpo_cka_only_20_2048_v2`** (27.4%) after switching to new answer extraction code\n4. **Multiple version chains** visible (v1->v2->v3) due to server outages (westd-29022), disk-full errors, batch_size misconfigurations, and eval script updates"
      }
    ],
    "totalDurationMs": 206813,
    "totalTokens": 57351,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11454,
      "cache_read_input_tokens": 41465,
      "output_tokens": 4431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4431,
          "cache_read_input_tokens": 41465,
          "cache_creation_input_tokens": 11454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11454,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Good, I have 50 experiments from the first page. But there are 249 total and I need to get the rest to find the core 20% sparsity results, 15% sparsity, 30% cliff, MBPP, 1.5B cross-scale, inference, etc. Let me fetch more registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "9ec5cde9-8158-4379-b7f3-1a109ad48663",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9236
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

_source line 69_

需要继续读取剩余 registry 数据（已有 50/249）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "a541f288-3073-4e45-82b3-076d703e55c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9236
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

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AJfnnzVJ957on4rhjNfPcg`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 50,
  "fields": [
    "*"
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
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "fab33cb5-f090-4a9b-af22-7bf869df109c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Y7Yz61fDsSUbjfXfQojR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 46521,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9236
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

_source line 71 · 2026-05-23T10:52:18.238Z_

<details><summary>↩ Tool result · `toolu_01AJfnnzVJ957on4rhjNfPcg`</summary>

```text
Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "37dfbb3b-7fbe-4af0-9a4b-e816cbddb1fd",
  "tool_use_result": {
    "content": "Error: result (72,347 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533538235.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"hypothesis\": \"Qwen2.5-Math-7B CKA-only 20% SFT MATH-500 eval @2048. Cross-architecture validation: if CKA-only criterion generalizes from DeepSeek-R1-Distill to Qwen-Math on MATH-500. SFT GSM8K = 51.5% (N=200). Paired with westb:1 GRPO GSM8K for C1 decoupling cross-arch.\", \"parent\": \"sft_qwen_math_cka_only_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json\", \"completed_at\": \"2026-05-23T10:44:00.535Z\"}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"hypothesis\": \"GRPO RASP α=0.5 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=0.5 = 25.4%. GSM8K GRPO α=0.5 = 61.18%. Completes MATH-500 GRPO dose-response curve.\", \"parent\": \"eval_gsm8k_grpo_alpha0p5_20\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.log\", \"completed_at\": \"2026-05-23T10:11:11.002Z\"}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"hypothesis\": \"GRPO CKA-only 20% MATH-500 @2048 rerun with NEW eval script. Previous 29.2% (eval_math500_grpo_cka_only_20_2048) used OLD answer extraction. SFT CKA-only = 26.8% (NEW). Rerun ensures consistent C1 |Δ| comparison.\", \"parent\": \"eval_math500_grpo_cka_only_20_2048\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_cka_only_20_2048_v2.log\", \"completed_at\": \"2026-05-23T08:55:58.278Z\"}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"hypothesis\": \"GRPO RASP α=3.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=3.0 = 23.2%. GSM8K GRPO α=3.0 = 63.45%. Completes MATH-500 GRPO dose-response curve for α=3.0 data point.\", \"parent\": \"eval_gsm8k_grpo_alpha3p0_20\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_alpha3p0_20.log\", \"completed_at\": \"2026-05-23T07:48:50.736Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"hypothesis\": \"GRPO RASP α=4.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=4.0 = 26.6%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=4.0. GSM8K GRPO α=4.0 = 62.77%.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v3\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T05:58:52.769Z\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"hypothesis\": \"GRPO RASP α=1.0 MATH-500 eval @2048. C1 decoupling on MATH-500: SFT α=1.0 = 21.2%. If |GRPO - SFT| < 2pp, C1 decoupling holds cross-benchmark for α=1.0.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T04:41:44.783Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T04:41:56.794961+00:00\"}]}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:44:32.303Z\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"hypothesis\": \"CKA-only 20% SFT MATH-500 eval @2048 on westd (migrated from westb for speed). Dose-response endpoint control: CKA-only is the best-performing pruning method (GSM8K 64.37%). MATH-500 result establishes upper bound for cross-benchmark dose-response curve.\", \"parent\": \"eval_math500_sft_cka_only_20_westb\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T00:00:43.009Z\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"hypothesis\": \"GRPO RASP α=2.0 MATH-500 eval @2048. C1 decoupling evidence on MATH-500: SFT α=2.0 = 24.0%, GRPO expected similar (~24%). If |GRPO - SFT| < 1pp, C1 decoupling holds cross-benchmark.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"reproduce\": {\"finished_at\": \"2026-05-23T03:14:21.897Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:14:37.164633+00:00\"}]}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:16:40.537Z\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"hypothesis\": \"MF3 cross-architecture validation v3 (N=500, max_new_tokens=2048): Qwen2.5-Math-7B CKA-only 20% GRPO GSM8K eval with absolute model_path fix. v2 crashed due to relative path OSError. v1 killed due to 337s/sample (no token limit). Tests whether CKA-only pruning + GRPO recovery generalizes beyond DeepSeek-R1-Distill to Qwen-Math architecture.\", \"parent\": \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T02:53:37.071Z\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"hypothesis\": \"α=1.0 SFT MATH-500 eval @2048 v2 (on westb). Default RASP α=1.0. Cross-benchmark dose-response: GSM8K α=1.0 SFT=63.31%. v1 killed at 304/500, result file never written. Completes 5-point dose-response curve on MATH-500.\", \"parent\": \"eval_math500_sft_rasp_alpha1p0_20\", \"notes\": \"westb submission failed: model sft_rasp_20_westd not found on westb. Only exists on westd-32935. Waiting for westd:3 (α=4.0, 85%) to free up.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T22:58:10.208Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T22:58:19.219921+00:00\"}]}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:01:03.420Z\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"Standard (random) 20% SFT MATH-500 eval @2048. Baseline comparison: Standard pruning without CKA guidance. Cross-benchmark extension of GSM8K Standard results.\", \"parent\": \"eval_math500_sft_standard_20\", \"reproduce\": {\"finished_at\": \"2026-05-19T08:54:35.352Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T08:54:40.855817+00:00\"}]}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T13:08:16.850Z\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"hypothesis\": \"α=0.5 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=0.5 SFT=60.73%. If MATH-500 also shows α=0.5 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:18:43.350Z\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"hypothesis\": \"α=3.0 SFT MATH-500 eval @2048. Dose-response \\\"下降段确认点\\\": GSM8K α=3.0 SFT=64.14% (below α=2.0 peak 64.97%). If MATH-500 also shows α=3.0 < α=2.0, confirms inverted-U descending arm cross-benchmark. Completes 5/5 MATH-500 dose-response.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:12:26.406Z\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"hypothesis\": \"α=4.0 SFT MATH-500 eval @2048. Cross-benchmark dose-response validation: GSM8K shows α=4.0 SFT=61.94%. If MATH-500 also shows α=4.0 < α=2.0, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}, \"completed_at\": \"2026-05-22T21:22:35.442Z\"}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"hypothesis\": \"α=2.0 SFT MATH-500 eval @2048. Dose-response peak on GSM8K (64.97% SFT). Cross-benchmark validation: if α=2.0 also peaks on MATH-500, inverted-U generalizes beyond GSM8K (strengthens MF4 + N1).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T20:12:27.595Z\"}, \"failure_reason\": \"cron false positive: process exited normally, result file confirmed by Reviewer (24.0% accuracy)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T20:12:32.633Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T20:12:40.230344+00:00\"}]}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"hypothesis\": \"MF2 seed456 GSM8K eval (N=1319, greedy, max_new_tokens=2048). Paired with seed42 (50.57%) and seed123 v2 (running, interim 52.40%@1000). Validates C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed456\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T17:48:12.480Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T17:48:17.521Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T17:48:25.193120+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}, \"notes\": \"Cron 误判 (已知模式): 实验实际完成 1319/1319, acc=50.87%. 与 seed42 (50.57%) 一致, 验证 C1 decoupling. Results: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\"}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\", \"hypothesis\": \"MF2 seed123 v2 GSM8K eval (N=1319, greedy, max_new_tokens=2048). 配对 seed42 (50.57%) 和 seed456 (pending). 验证 C1 decoupling 跨 seed 鲁棒性。v1 因 batch_size=1 配置错误作废。\", \"parent\": \"grpo_random_20_seed123_v2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed456. Third seed for C1 decoupling robustness check. seed42: Δ=-0.68pp, seed123: pending eval. If all seeds show |Δ(GRPO-SFT)| ≤ 2pp, C1 claim is robust across random seeds.\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:22:39.316Z\"}, \"failure_reason\": \"磁盘满: GRPO训练100/100完成但save_pretrained失败 (No space left on device)。westb-23072:/root/autodl-tmp 空间不足。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:22:44.289Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:22:54.301751+00:00\"}]}, \"notes\": \"失败原因: GRPO 训练 100/100 步已完成 (3h02min)，但 save_pretrained 时磁盘满 (No space left on device, os error 28)。保存路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456。W&B run auv9riek 有完整训练 metrics。save_steps=100=max_steps，无中间 checkpoint，需重跑。 | 已有成果: W&B metrics 完整 | 建议: 清理 westb-23072 磁盘后重提交\"}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\", \"hypothesis\": \"MF5 depth-first SFT GSM8K eval. Establishes SFT baseline for depth-first pruning method, paired with GRPO eval to check C1 decoupling for this baseline method.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\", \"hypothesis\": \"MF5 depth-first GRPO GSM8K eval re-run. Previous pipeline_depth_first_20 results lost due to disk-full during JSON write. GRPO checkpoint intact. Re-running eval to get formal JSON result file. Prior log recovery showed ~24.18% from nohup output.\", \"parent\": \"pipeline_depth_first_20\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\", \"hypothesis\": \"MF2 multi-seed validation v2: Random 20% GRPO with seed123, correct batch_size=2 (matching seed42/seed456). v1 used batch_size=1 (half data per 100 steps), results invalidated. Tests C1 decoupling robustness across random seeds.\", \"parent\": \"grpo_random_20_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\", \"completed_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"hypothesis\": \"α=3.0 GRPO GSM8K eval. Dose-response 5th data point: α=3.0 between α=2.0 (66.11%) and α=4.0 (62.77%). Completes the 5-point dose-response curve for causal evidence of CKA overlap suppression effect.\", \"notes\": \"UNBLOCKED: grpo_rasp_alpha3p0_20_v2 checkpoint-100 完整 (12.3GB). Eval 已启动 PID 43755 on westd:0, 2.8s/sample, ETA ~60 min.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\", \"completed_at\": \"2026-05-22T14:46:15.365Z\"}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"hypothesis\": \"Random 20% SFT MATH-500 @2048. v2 failed due to old eval_math500.py on westd-32935. Code synced from westb.\", \"parent\": \"eval_math500_sft_random_20_v2\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:10:18.359Z\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"hypothesis\": \"α=3.0 SFT GSM8K eval (checkpoint-935, 1 epoch). Dose-response 5th SFT data point for C1 decoupling. Paired with α=3.0 GRPO (pending). Completes the 5-point dose-response SFT column.\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T12:34:57.027Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T12:35:05.634Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:35:15.663664+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}, \"log_path\": \"/tmp/eval_gsm8k_sft_alpha3p0.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"notes\": \"Cron 误判。评估 1319/1319 全部完成，accuracy=64.14%。进程因写结果 JSON 时磁盘满 (OSError: No space left on device) 以非零码退出，但所有推理已完成、accuracy 已计算。结果 JSON 未写入磁盘，数据从日志提取。中间进度 ~64.15%@1300 与最终 64.14% 一致。\"}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\", \"hypothesis\": \"Re-run of grpo_rasp_alpha3p0_20 (checkpoint corrupted by disk-full). α=3.0 GRPO 100 steps on sft_rasp_alpha3p0_20/checkpoint-935. Critical for dose-response curve (α=3.0 between α=2.0 peak and α=4.0 decline).\", \"parent\": \"grpo_rasp_alpha3p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"hypothesis\": \"Standard 20% fair GRPO MATH-500 @2048. P0 data gap for cross-method MATH-500 table. Re-run on westd-32935 after westd-29022 outage.\", \"parent\": \"eval_math500_grpo_standard_20_fair_2048\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:19.798Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:27.767Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:38.330160+00:00\"}]}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}, \"notes\": \"Cron 误判。实际正常完成。MATH-500 Accuracy = 0.2640 ± 0.0197 (132/500)。运行时长 ~7h11min。结果文件: /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\"}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\", \"hypothesis\": \"MF2 multi-seed validation: Random pruning 20% GRPO with seed123. Tests if GRPO decoupling result (C1) is robust across random seeds. If variance across seeds is low (±2pp), C1 claim is strengthened.\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:49.435Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:12:57.919Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:13:16.493425+00:00\"}]}, \"notes\": \"Cron 误判 (已知 pattern: process dead 5× with no sentinel/W&B)。实际 GRPO 训练正常完成 (19:02 CST)。模型保存: /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123。WandB run: grpo_sft_random_20 (ID: 1silchcm)。日志: /tmp/mf2_random_seed123_grpo.log\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\", \"hypothesis\": \"α=3.0 GRPO 100 steps on checkpoint-935 (1 epoch SFT). Dose-response data point between α=2.0 and α=4.0. If monotonic: higher α → higher GSM8K accuracy, confirming CKA overlap suppression causally harms recovery.\", \"parent\": \"grpo_alpha4_20\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:31:57.909Z\", \"notes\": \"GRPO 训练 100/100 steps 完成，但 checkpoint-100/model.safetensors 被截断（7.2GB vs 应有 11.5GB）。原因：westb 数据盘在保存时 100% 满。需要重跑 GRPO。SFT checkpoint-935 完好（11.5GB）。\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"hypothesis\": \"α=2.0 SFT GSM8K eval for C1 decoupling. Paired with α=2.0 GRPO (66.11%). Critical: if SFT ~61-62%, Δ ≈ +4-5pp would break C1 universal ±2pp claim. Reviewer-flagged risk.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:22:49.360Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"hypothesis\": \"α=0.5 SFT GSM8K eval for C1 decoupling. Paired with α=0.5 GRPO (61.18%). Δ(GRPO-SFT) tests whether GRPO benefit is universal ±2pp across α values.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:20:50.793Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\", \"hypothesis\": \"MF3 cross-architecture validation: Qwen2.5-Math-7B CKA-only 20% pruned → SFT → GRPO 100 steps. Tests if CKA-guided pruning advantage transfers beyond DeepSeek-R1 to Qwen-Math family. P0 highest priority.\", \"parent\": \"sft_qwen_math_cka_only_20_v2\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"hypothesis\": \"α=2.0 GRPO GSM8K eval. Dose-response data point: moderate overlap suppression (α=2.0) between α=1.0 (61.49%) and α=4.0 (62.77%). Tests monotonicity of dose-response curve.\", \"parent\": \"pipeline_alpha2p0_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:16.837Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"hypothesis\": \"α=0.5 GRPO GSM8K eval. Dose-response data point: low overlap suppression (α=0.5) should yield lower accuracy than α=1.0 (61.49%) if CKA overlap suppression causally harms recovery.\", \"parent\": \"pipeline_alpha0p5_20\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:29:13.196Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"hypothesis\": \"1.5B Standard 20% SFT MATH-500 @2048. Cross-scale comparison with CKA-only 1.5B (10.6%) to test if CKA-guided pruning advantage is scale-invariant.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}, \"completed_at\": \"2026-05-22T07:50:22.759Z\"}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"hypothesis\": \"α=4.0 SFT GSM8K N=1319 full eval @2048. D100 critical for C1 decoupling universality. v4 lost to westd-29022 outage. Re-run on westd-32935.\", \"parent\": \"eval_gsm8k_sft_alpha4_20_v4\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:47:27.370Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:47:34.101Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:47:41.693855+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"hypothesis\": \"α=4.0 GRPO GSM8K N=1319 full eval @2048. v1 timed out at 774/1319 (62.93% interim). v2 ALLOCATED but westd-29022 died. Re-run on westd-32935 with --max_new_tokens 2048.\", \"parent\": \"eval_gsm8k_grpo_alpha4_20_v2\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T05:30:52.773Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T05:30:50.611Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T05:31:04.453494+00:00\"}]}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}, \"notes\": \"Cron 误判为 failed（进程正常退出但 cron 未检测到 sentinel）。实际完成 1319/1319，accuracy=62.77%。α=4.0 GRPO > Standard GRPO (59.84%) > RASP α=1.0 GRPO (54.43%)。确认 α tuning 有效缓解 RASP collapse。checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100, log_path: /root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log, results_path: /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\"}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T02:58:40.587Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:58:45.343074+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.13, \"correct\": 65, \"n_total\": 500}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\"}}, \"notes\": \"v1 结果采用（v2 启动即崩溃）。结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25.json。Director 于 2026-05-21 批准采用 v1 数据。\", \"hypothesis\": \"Standard 25% SFT model MATH-500 accuracy establishes pre-GRPO baseline for standard pruning at 25% sparsity, enabling SFT→GRPO recovery delta on MATH-500\", \"completed_at\": \"2026-05-21T19:22:29.444Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"hypothesis\": \"α=4.0 GRPO after SFT: if reward collapses (→0 like α=1.0 RASP GRPO), proves RASP collapse is structural, not hyperparameter-dependent. If reward stays positive and GSM8K improves over SFT, α tuning can mitigate collapse.\", \"parent\": \"sft_alpha4_20_v2\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_alpha4_20.log\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T19:27:23.228Z\"}, \"sft_alpha4_20_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"hypothesis\": \"α=4.0 SFT recovery with save_only_model=True to prevent disk overflow. Pruning successful (19.09% sparsity). Testing if higher α mitigates RASP collapse after full SFT→GRPO→eval pipeline.\", \"parent\": \"sft_alpha4_20_manual\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T18:54:53.481Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:54:59.708620+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"hypothesis\": \"CKA-only 25% GRPO model MATH-500 @2048 accuracy for cross-benchmark validation, re-run with correct max_new_tokens=2048 for consistency with 20% data\", \"parent\": \"eval_math500_grpo_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:33:40.068Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}, \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"hypothesis\": \"CKA-only 25% SFT model MATH-500 @2048 accuracy establishes pre-GRPO baseline, re-run with correct max_new_tokens=2048 for consistency\", \"parent\": \"eval_math500_sft_cka_only_25\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\", \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T17:29:10.900Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}, \"notes\": \"Eval completed all 500 problems. Result JSON not saved due to IsADirectoryError (output_path pointed to directory instead of file). Metrics extracted from log.\"}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"hypothesis\": \"Standard 25% SFT GSM8K accuracy establishes pre-GRPO floor for importance-based pruning at 25% sparsity, enabling SFT→GRPO recovery delta comparison with CKA-only 25%\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T14:40:37.092Z\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"hypothesis\": \"CKA-only 20% GRPO model MATH-500 accuracy provides cross-benchmark validation at 20% sparsity and cross-method comparison with Random 20% GRPO MATH-500\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"parent\": \"grpo_cka_only_20\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:05:38.456Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:05:47.086682+00:00\"}]}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20.json\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:09:25.937Z\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"hypothesis\": \"Standard 25% GRPO后GSM8K评估。GRPO reward=0.00813 (near-total collapse)。验证 Standard pruning 在 25% 稀疏度下 GRPO 后数学推理能力。\", \"parent\": \"grpo_standard_25_westb\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\", \"completed_at\": \"2026-05-21T12:37:17.579Z\"}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"hypothesis\": \"CKA-only 25% SFT model retains higher GSM8K accuracy than GRPO-recovered model's SFT baseline, establishing the pre-GRPO accuracy floor for measuring recovery delta at 25% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T10:17:58.203Z\"}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"hypothesis\": \"Random 20% SFT model GSM8K accuracy establishes the pre-GRPO floor for random pruning, enabling SFT→GRPO recovery delta comparison across pruning methods at 20% sparsity\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:47:06.620Z\"}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"hypothesis\": \"CKA-only 25% GRPO后GSM8K评估。model_path=/grpo_cka_only_25（根目录）。Cross-sparsity对比: Standard 25% GRPO=51.1%, RASP 25% GRPO=53.15%。\", \"parent\": \"grpo_cka_only_25\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"notes\": \"正确 PID=322443 (v3提交)。323174 是重复提交已 kill。\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}, \"checkpoint_path\": \"N/A (eval only)\", \"completed_at\": \"2026-05-21T08:17:13.429Z\"}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"hypothesis\": \"Standard 25% GRPO v5 fair config (100 steps, lr=1e-6, beta=0.01, T=0.4, seed=42) on westb. Re-run with fair config for cross-method comparison.\", \"parent\": \"sft_standard_25\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_25.log\"}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"hypothesis\": \"Random 20% GRPO后GSM8K评估。Random pruning reward=0.189（最低），验证无结构保留的pruning在GRPO后数学推理能力。\", \"parent\": \"grpo_random_20\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\"}, \"sft_random_20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"hypothesis\": \"Random 20% pruning baseline SFT recovery. Random pruning 不保留任何结构信息，作为 ablation baseline 验证 CKA-guided pruning 的结构保留优势。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:50:00.000Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_random_20.log\"}}, \"count\": 50, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9127}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
The registry returns the same 50 most recent results. I need to use `offset` to get more. But looking at the API, there's no `offset` parameter. Let me check the registry tool definition again... It has `limit` but no `offset`. 

Let me try a different approach - let me read the full registry without a limit, and use an agent to parse it.

Actually wait, the `limit` parameter says "0 = all". So let me try limit=0 to get all experiments. But that'll be too big. Let me try a different approach - read all with limit=0, save to disk, then have an agent parse the full thing.


Actually, I could try limit=0 with minimal fields to reduce the payload size.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "ab0f6c9a-9077-4219-87d6-5f0ae63387af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lrxj2W2npRMFZcTNFfv5bM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 55757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BSoaLqkwubkCC7EAUvLzVF`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
    "created_at",
    "updated_at",
    "tags"
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
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "23ca0e31-fe63-4b43-9d20-38c5e0c3aa5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lrxj2W2npRMFZcTNFfv5bM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 55757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
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

_source line 74 · 2026-05-23T10:52:27.525Z_

<details><summary>↩ Tool result · `toolu_01BSoaLqkwubkCC7EAUvLzVF`</summary>

```text
Error: result (72,125 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "e4bc7c49-4335-41db-a060-e969df0f0e8d",
  "tool_use_result": {
    "content": "Error: result (72,125 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533547522.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T23:11:09.017Z\", \"updated_at\": \"2026-05-23T10:44:00.535Z\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-23T02:59:15.985Z\", \"updated_at\": \"2026-05-23T10:11:11.002Z\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-23T05:07:09.002Z\", \"updated_at\": \"2026-05-23T08:55:58.278Z\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-23T03:19:40.950Z\", \"updated_at\": \"2026-05-23T07:48:57.618Z\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-23T00:01:54.194Z\", \"updated_at\": \"2026-05-23T05:58:52.769Z\", \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"created_at\": \"2026-05-22T23:02:44.335Z\", \"updated_at\": \"2026-05-23T04:44:32.303Z\", \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}}, \"eval_math500_sft_cka_only_20_westd\": {\"created_at\": \"2026-05-22T20:45:21.526Z\", \"updated_at\": \"2026-05-23T03:21:26.164Z\", \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T22:23:27.589Z\", \"updated_at\": \"2026-05-23T03:16:40.537Z\", \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"created_at\": \"2026-05-22T15:12:46.181Z\", \"updated_at\": \"2026-05-23T02:53:37.071Z\", \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"created_at\": \"2026-05-22T20:50:24.239Z\", \"updated_at\": \"2026-05-22T23:01:03.419Z\", \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}}, \"eval_math500_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-19T01:34:44.782Z\", \"updated_at\": \"2026-05-22T22:19:38.080Z\", \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-22T15:20:44.460Z\", \"updated_at\": \"2026-05-22T22:18:43.350Z\", \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T18:26:16.273Z\", \"updated_at\": \"2026-05-22T22:12:26.406Z\", \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-22T15:20:47.150Z\", \"updated_at\": \"2026-05-22T21:22:35.441Z\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T15:06:22.386Z\", \"updated_at\": \"2026-05-22T20:44:52.970Z\", \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T16:26:01.516Z\", \"updated_at\": \"2026-05-22T18:27:22.282Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:33.753Z\", \"updated_at\": \"2026-05-22T16:49:54.123Z\"}, \"grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T12:00:38.940Z\", \"updated_at\": \"2026-05-22T16:27:46.810Z\"}, \"eval_gsm8k_sft_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:43.950Z\", \"updated_at\": \"2026-05-22T15:19:31.829Z\"}, \"eval_gsm8k_grpo_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:41.126Z\", \"updated_at\": \"2026-05-22T15:18:38.970Z\"}, \"grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:29.868Z\", \"updated_at\": \"2026-05-22T15:00:23.101Z\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"created_at\": \"2026-05-22T09:30:06.630Z\", \"updated_at\": \"2026-05-22T14:47:06.188Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}}, \"eval_math500_sft_random_20_v3\": {\"created_at\": \"2026-05-22T04:11:52.462Z\", \"updated_at\": \"2026-05-22T14:10:18.359Z\", \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}}, \"eval_gsm8k_sft_alpha3p0_20\": {\"created_at\": \"2026-05-22T10:24:58.696Z\", \"updated_at\": \"2026-05-22T12:38:25.600Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}}, \"grpo_rasp_alpha3p0_20_v2\": {\"created_at\": \"2026-05-22T10:40:19.362Z\", \"updated_at\": \"2026-05-22T11:58:15.586Z\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"created_at\": \"2026-05-22T03:49:45.575Z\", \"updated_at\": \"2026-05-22T11:17:52.493Z\", \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}}, \"grpo_random_20_seed123\": {\"created_at\": \"2026-05-22T10:34:12.100Z\", \"updated_at\": \"2026-05-22T11:17:21.388Z\"}, \"grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T08:48:06.001Z\", \"updated_at\": \"2026-05-22T10:39:07.034Z\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"created_at\": \"2026-05-22T10:19:50.623Z\", \"updated_at\": \"2026-05-22T10:22:56.503Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"created_at\": \"2026-05-22T10:19:48.133Z\", \"updated_at\": \"2026-05-22T10:20:57.690Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T08:50:34.293Z\", \"updated_at\": \"2026-05-22T09:54:05.974Z\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"created_at\": \"2026-05-22T09:28:08.089Z\", \"updated_at\": \"2026-05-22T09:29:24.824Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"created_at\": \"2026-05-22T09:28:05.478Z\", \"updated_at\": \"2026-05-22T09:29:23.350Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-22T04:31:30.202Z\", \"updated_at\": \"2026-05-22T08:27:40.167Z\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"created_at\": \"2026-05-22T03:49:50.201Z\", \"updated_at\": \"2026-05-22T06:05:53.848Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"created_at\": \"2026-05-22T03:49:52.414Z\", \"updated_at\": \"2026-05-22T05:33:39.349Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}}, \"eval_math500_sft_standard_25\": {\"created_at\": \"2026-05-21T02:58:32.492Z\", \"updated_at\": \"2026-05-22T02:31:03.648Z\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"created_at\": \"2026-05-21T18:59:18.863Z\", \"updated_at\": \"2026-05-21T19:32:31.353Z\", \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}}, \"sft_alpha4_20_v2\": {\"created_at\": \"2026-05-21T18:30:48.284Z\", \"updated_at\": \"2026-05-21T19:32:28.482Z\", \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:50.310Z\", \"updated_at\": \"2026-05-21T17:33:50.709Z\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}}, \"eval_math500_sft_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:51.945Z\", \"updated_at\": \"2026-05-21T17:29:14.940Z\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}}, \"eval_gsm8k_sft_standard_25\": {\"created_at\": \"2026-05-21T08:13:12.112Z\", \"updated_at\": \"2026-05-21T14:40:37.092Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}}, \"eval_math500_grpo_cka_only_20\": {\"created_at\": \"2026-05-18T02:41:32.199Z\", \"updated_at\": \"2026-05-21T12:47:30.348Z\", \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}}, \"eval_gsm8k_grpo_standard_25\": {\"created_at\": \"2026-05-21T06:42:08.819Z\", \"updated_at\": \"2026-05-21T12:37:17.579Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}}, \"eval_gsm8k_sft_cka_only_25\": {\"created_at\": \"2026-05-21T06:47:14.010Z\", \"updated_at\": \"2026-05-21T10:17:58.203Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}}, \"eval_gsm8k_sft_random_20\": {\"created_at\": \"2026-05-21T06:47:16.459Z\", \"updated_at\": \"2026-05-21T08:47:06.620Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"created_at\": \"2026-05-21T04:56:52.006Z\", \"updated_at\": \"2026-05-21T08:17:13.429Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}}, \"grpo_standard_25_westb\": {\"created_at\": \"2026-05-21T03:00:00.000Z\", \"updated_at\": \"2026-05-21T06:40:00.000Z\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}}, \"eval_gsm8k_grpo_random_20_v2\": {\"created_at\": \"2026-05-21T04:56:53.980Z\", \"updated_at\": \"2026-05-21T06:38:00.000Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}}, \"sft_random_20\": {\"created_at\": \"2026-05-21T03:44:24.654Z\", \"updated_at\": \"2026-05-21T04:45:00.000Z\", \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}}, \"grpo_random_20\": {\"created_at\": \"2026-05-17T13:30:31.016Z\", \"updated_at\": \"2026-05-21T04:42:00.000Z\", \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}}, \"grpo_cka_only_25\": {\"created_at\": \"2026-05-21T02:49:22.258Z\", \"updated_at\": \"2026-05-21T03:22:07.134Z\", \"metrics\": {\"reward\": 0.2875, \"steps\": 100}}, \"eval_humaneval_sft_standard_25\": {\"created_at\": \"2026-05-21T02:43:32.214Z\", \"updated_at\": \"2026-05-21T02:44:15.495Z\", \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}}, \"sft_cka_only_25\": {\"created_at\": \"2026-05-21T01:50:42.758Z\", \"updated_at\": \"2026-05-21T02:40:00.000Z\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}}, \"prune_cka_only_25\": {\"created_at\": \"2026-05-18T13:43:54.266Z\", \"updated_at\": \"2026-05-21T01:50:00.000Z\", \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T23:00:14.007Z\", \"updated_at\": \"2026-05-21T00:57:58.499Z\", \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T23:00:15.387Z\", \"updated_at\": \"2026-05-21T00:51:20.262Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T21:35:28.222Z\", \"updated_at\": \"2026-05-21T00:18:00.000Z\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T21:35:29.444Z\", \"updated_at\": \"2026-05-21T00:06:17.294Z\", \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}}, \"grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T21:58:14.439Z\", \"updated_at\": \"2026-05-20T22:51:31.775Z\"}, \"grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T21:58:11.697Z\", \"updated_at\": \"2026-05-20T22:51:30.499Z\"}, \"grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T20:54:57.409Z\", \"updated_at\": \"2026-05-20T21:35:16.671Z\"}, \"grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T20:54:54.710Z\", \"updated_at\": \"2026-05-20T21:35:14.509Z\"}, \"eval_gsm8k_sft_standard_20\": {\"created_at\": \"2026-05-20T17:07:58.760Z\", \"updated_at\": \"2026-05-20T19:58:14.139Z\", \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}}, \"eval_gsm8k_dense_unpruned\": {\"created_at\": \"2026-05-20T16:28:28.020Z\", \"updated_at\": \"2026-05-20T19:36:49.374Z\", \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"created_at\": \"2026-05-20T16:32:21.874Z\", \"updated_at\": \"2026-05-20T18:49:11.554Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}}, \"eval_gsm8k_sft_cka_only_15\": {\"created_at\": \"2026-05-20T15:19:42.152Z\", \"updated_at\": \"2026-05-20T18:33:53.213Z\", \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}}, \"eval_gsm8k_sft_rasp_20\": {\"created_at\": \"2026-05-20T17:09:04.809Z\", \"updated_at\": \"2026-05-20T18:10:54.576Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}}, \"eval_gsm8k_grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T14:43:21.408Z\", \"updated_at\": \"2026-05-20T16:28:25.206Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}}, \"eval_gsm8k_sft_standard_15\": {\"created_at\": \"2026-05-20T14:23:49.568Z\", \"updated_at\": \"2026-05-20T16:28:23.020Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T13:32:17.474Z\", \"updated_at\": \"2026-05-20T16:04:05.569Z\", \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"created_at\": \"2026-05-20T13:31:33.529Z\", \"updated_at\": \"2026-05-20T16:04:03.508Z\", \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}}, \"eval_gsm8k_sft_qwen_standard_20\": {\"created_at\": \"2026-05-20T10:32:12.883Z\", \"updated_at\": \"2026-05-20T15:44:54.102Z\", \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"created_at\": \"2026-05-20T10:32:11.084Z\", \"updated_at\": \"2026-05-20T15:39:07.657Z\", \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T13:42:06.715Z\", \"updated_at\": \"2026-05-20T14:23:39.083Z\", \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"created_at\": \"2026-05-20T10:27:04.283Z\", \"updated_at\": \"2026-05-20T13:38:49.241Z\", \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"created_at\": \"2026-05-20T10:27:05.741Z\", \"updated_at\": \"2026-05-20T13:38:47.186Z\", \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}}, \"grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T11:58:03.218Z\", \"updated_at\": \"2026-05-20T13:35:06.015Z\", \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"created_at\": \"2026-05-20T11:36:13.866Z\", \"updated_at\": \"2026-05-20T13:35:02.652Z\", \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"created_at\": \"2026-05-20T04:08:24.071Z\", \"updated_at\": \"2026-05-20T11:56:25.682Z\", \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"created_at\": \"2026-05-20T04:08:22.614Z\", \"updated_at\": \"2026-05-20T11:56:24.517Z\", \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"created_at\": \"2026-05-20T09:18:17.089Z\", \"updated_at\": \"2026-05-20T09:50:15.333Z\", \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T09:15:10.283Z\", \"updated_at\": \"2026-05-20T09:49:10.630Z\", \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T09:15:16.595Z\", \"updated_at\": \"2026-05-20T09:49:08.654Z\", \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}}, \"grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T06:22:10.493Z\", \"updated_at\": \"2026-05-20T09:13:48.616Z\", \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}}, \"grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T06:22:27.444Z\", \"updated_at\": \"2026-05-20T09:13:45.445Z\", \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}}, \"eval_mbpp_grpo_standard_20_v3\": {\"created_at\": \"2026-05-19T21:00:40.293Z\", \"updated_at\": \"2026-05-20T03:06:43.359Z\", \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:45.876Z\", \"updated_at\": \"2026-05-20T03:06:22.483Z\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"created_at\": \"2026-05-19T10:05:36.497Z\", \"updated_at\": \"2026-05-20T03:06:20.863Z\", \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:47.965Z\", \"updated_at\": \"2026-05-20T03:06:19.658Z\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:50.649Z\", \"updated_at\": \"2026-05-20T03:06:18.579Z\", \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:23:35.431Z\", \"updated_at\": \"2026-05-20T02:43:15.577Z\", \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:33:19.363Z\", \"updated_at\": \"2026-05-20T02:43:06.318Z\", \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"created_at\": \"2026-05-19T22:26:22.996Z\", \"updated_at\": \"2026-05-20T02:16:04.699Z\", \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}}, \"eval_mbpp_grpo_standard_20_v4\": {\"created_at\": \"2026-05-19T21:01:23.058Z\", \"updated_at\": \"2026-05-20T01:46:54.906Z\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}}, \"cka_scoring_stability_ablation\": {\"created_at\": \"2026-05-19T21:21:10.933Z\", \"updated_at\": \"2026-05-19T22:21:53.770Z\", \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}}, \"eval_mbpp_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-19T18:56:15.766Z\", \"updated_at\": \"2026-05-19T21:57:06.135Z\", \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}}, \"eval_mbpp_grpo_rasp_20\": {\"created_at\": \"2026-05-19T18:18:35.729Z\", \"updated_at\": \"2026-05-19T21:55:32.779Z\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}}, \"eval_mbpp_sft_rasp_20\": {\"created_at\": \"2026-05-19T18:18:34.640Z\", \"updated_at\": \"2026-05-19T21:08:00.610Z\", \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"created_at\": \"2026-05-19T17:20:00.596Z\", \"updated_at\": \"2026-05-19T19:58:30.970Z\", \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:50.597Z\", \"updated_at\": \"2026-05-19T18:52:30.545Z\", \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"created_at\": \"2026-05-19T14:41:07.213Z\", \"updated_at\": \"2026-05-19T18:17:54.178Z\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"created_at\": \"2026-05-19T17:19:18.419Z\", \"updated_at\": \"2026-05-19T18:17:53.164Z\", \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"created_at\": \"2026-05-19T15:47:16.122Z\", \"updated_at\": \"2026-05-19T18:03:15.831Z\", \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"created_at\": \"2026-05-19T14:22:26.084Z\", \"updated_at\": \"2026-05-19T18:02:48.590Z\"}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T17:47:34.008Z\", \"updated_at\": \"2026-05-19T17:48:24.627Z\", \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:48.029Z\", \"updated_at\": \"2026-05-19T17:02:50.370Z\"}, \"gradient_flow_v3\": {\"created_at\": \"2026-05-19T15:03:16.535Z\", \"updated_at\": \"2026-05-19T16:38:41.269Z\", \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-19T12:47:37.399Z\", \"updated_at\": \"2026-05-19T16:17:16.053Z\", \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}}, \"eval_mbpp_dense_unpruned\": {\"created_at\": \"2026-05-19T13:47:53.814Z\", \"updated_at\": \"2026-05-19T16:17:00.452Z\", \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"created_at\": \"2026-05-19T13:18:20.664Z\", \"updated_at\": \"2026-05-19T15:47:14.846Z\", \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}, \"grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T09:27:11.294Z\", \"updated_at\": \"2026-05-19T15:21:17.415Z\", \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"created_at\": \"2026-05-19T14:44:25.606Z\", \"updated_at\": \"2026-05-19T14:45:13.584Z\", \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"created_at\": \"2026-05-19T14:21:15.548Z\", \"updated_at\": \"2026-05-19T14:32:43.647Z\", \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"created_at\": \"2026-05-19T07:05:14.343Z\", \"updated_at\": \"2026-05-19T14:20:25.129Z\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-19T09:27:07.470Z\", \"updated_at\": \"2026-05-19T13:22:29.762Z\", \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}}, \"eval_math500_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-18T22:36:14.421Z\", \"updated_at\": \"2026-05-19T13:08:18.617Z\", \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:55.912Z\", \"updated_at\": \"2026-05-19T13:07:57.786Z\", \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-19T09:27:09.334Z\", \"updated_at\": \"2026-05-19T12:47:36.437Z\", \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"created_at\": \"2026-05-19T06:38:59.146Z\", \"updated_at\": \"2026-05-19T09:44:43.320Z\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"created_at\": \"2026-05-19T04:46:38.286Z\", \"updated_at\": \"2026-05-19T08:05:04.224Z\", \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-19T04:11:28.637Z\", \"updated_at\": \"2026-05-19T07:36:55.239Z\", \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}}, \"grpo_standard_20_fair\": {\"created_at\": \"2026-05-18T01:05:44.644Z\", \"updated_at\": \"2026-05-19T06:39:34.930Z\", \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}}, \"inference_bench_clean_v2\": {\"created_at\": \"2026-05-19T01:42:25.421Z\", \"updated_at\": \"2026-05-19T02:44:07.178Z\", \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:57.471Z\", \"updated_at\": \"2026-05-19T02:43:38.445Z\", \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}}, \"eval_math500_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-18T18:24:25.108Z\", \"updated_at\": \"2026-05-19T01:39:52.608Z\", \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}}, \"eval_math500_sft_rasp_20_2048\": {\"created_at\": \"2026-05-18T22:36:16.836Z\", \"updated_at\": \"2026-05-19T01:39:03.294Z\", \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}}, \"eval_math500_dense_2048\": {\"created_at\": \"2026-05-18T22:08:58.081Z\", \"updated_at\": \"2026-05-19T01:34:41.598Z\", \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}}, \"eval_math500_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-18T18:16:25.616Z\", \"updated_at\": \"2026-05-18T23:53:54.384Z\", \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T17:51:20.577Z\", \"updated_at\": \"2026-05-18T23:46:01.152Z\", \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}}, \"sft_standard_20_retrain_westd\": {\"created_at\": \"2026-05-18T22:40:50.567Z\", \"updated_at\": \"2026-05-18T23:24:15.076Z\", \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T16:59:22.921Z\", \"updated_at\": \"2026-05-18T23:02:00.110Z\", \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"created_at\": \"2026-05-18T18:16:24.171Z\", \"updated_at\": \"2026-05-18T22:12:04.614Z\", \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}}, \"grpo_cka_only_20_extended_300\": {\"created_at\": \"2026-05-18T14:51:36.423Z\", \"updated_at\": \"2026-05-18T21:43:18.847Z\", \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T16:38:01.585Z\", \"updated_at\": \"2026-05-18T21:03:21.558Z\", \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T16:35:29.923Z\", \"updated_at\": \"2026-05-18T20:09:40.771Z\", \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}}, \"eval_math500_dense_unpruned\": {\"created_at\": \"2026-05-18T13:42:10.786Z\", \"updated_at\": \"2026-05-18T18:15:28.383Z\", \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}}, \"grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T15:12:41.395Z\", \"updated_at\": \"2026-05-18T16:32:13.529Z\", \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T12:50:08.570Z\", \"updated_at\": \"2026-05-18T16:08:40.491Z\", \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}}, \"grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T14:15:13.990Z\", \"updated_at\": \"2026-05-18T15:11:31.870Z\", \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}}, \"grpo_standard_20_extended_300_v2\": {\"created_at\": \"2026-05-18T13:53:41.781Z\", \"updated_at\": \"2026-05-18T14:50:59.377Z\", \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}}, \"sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:56.278Z\", \"updated_at\": \"2026-05-18T12:31:29.300Z\"}, \"sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T11:29:09.842Z\", \"updated_at\": \"2026-05-18T12:31:27.978Z\"}, \"sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:57.178Z\", \"updated_at\": \"2026-05-18T12:29:19.746Z\"}, \"inference_bench_cka_only_20_clean\": {\"created_at\": \"2026-05-18T09:47:42.247Z\", \"updated_at\": \"2026-05-18T10:07:56.924Z\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"created_at\": \"2026-05-18T05:54:02.634Z\", \"updated_at\": \"2026-05-18T08:50:27.816Z\", \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}}, \"grpo_cka_only_20\": {\"created_at\": \"2026-05-17T14:51:36.653Z\", \"updated_at\": \"2026-05-18T02:21:23.748Z\", \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}}, \"grpo_rasp_20_fair\": {\"created_at\": \"2026-05-17T23:50:31.502Z\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"updated_at\": \"2026-05-18T01:08:19.563Z\"}, \"eval_postprune_standard_30\": {\"created_at\": \"2026-05-17T19:08:46.051Z\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"updated_at\": \"2026-05-18T00:27:39.362Z\"}, \"eval_sft_cka_only_20_n1319\": {\"created_at\": \"2026-05-17T18:20:20.406Z\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"updated_at\": \"2026-05-17T23:48:58.392Z\"}, \"prune_cka_only_30\": {\"created_at\": \"2026-05-17T21:42:06.467Z\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"updated_at\": \"2026-05-17T21:42:06.467Z\"}, \"eval_postprune_rasp_30\": {\"created_at\": \"2026-05-17T18:22:00Z\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"updated_at\": \"2026-05-17T21:39:43.149Z\"}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-17T16:26:15.836Z\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"updated_at\": \"2026-05-17T19:09:18.456Z\"}, \"eval_humaneval_grpo_standard_20_2048\": {\"created_at\": \"2026-05-17T13:41:03.761Z\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"updated_at\": \"2026-05-17T18:16:11.481Z\"}, \"grpo_rasp_25\": {\"created_at\": \"2026-05-16T08:42:40.256Z\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"updated_at\": \"2026-05-17T18:06:56.419Z\"}, \"eval_humaneval_grpo_rasp_20_2048\": {\"created_at\": \"2026-05-17T13:41:44.795Z\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"updated_at\": \"2026-05-17T16:24:44.117Z\"}, \"eval_sft_cka_only_20\": {\"created_at\": \"2026-05-17T14:28:35.380Z\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"updated_at\": \"2026-05-17T14:48:17.267Z\"}, \"sft_cka_only_20\": {\"created_at\": \"2026-05-17T13:43:50.320Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"updated_at\": \"2026-05-17T14:28:29.688Z\"}, \"eval_humaneval_unpruned_2048\": {\"created_at\": \"2026-05-17T12:40:50.255Z\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"updated_at\": \"2026-05-17T13:53:59.636Z\"}, \"eval_humaneval_sft_rasp_20_2048\": {\"created_at\": \"2026-05-17T12:40:51.686Z\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"updated_at\": \"2026-05-17T13:42:41.560Z\"}, \"eval_humaneval_grpo_standard_20\": {\"created_at\": \"2026-05-17T10:00:40.683Z\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"updated_at\": \"2026-05-17T13:33:59.897Z\"}, \"eval_math500_unpruned\": {\"created_at\": \"2026-05-17T06:23:49.923Z\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"updated_at\": \"2026-05-17T12:40:26.343Z\"}, \"eval_gradient_postsft\": {\"created_at\": \"2026-05-17T10:07:58.644Z\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"updated_at\": \"2026-05-17T11:24:16.260Z\"}, \"gradient_sft_v3\": {\"created_at\": \"2026-05-17T09:28:21.646Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"updated_at\": \"2026-05-17T10:08:07.026Z\"}, \"eval_math500_sft_standard_20\": {\"created_at\": \"2026-05-17T06:23:54.283Z\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"updated_at\": \"2026-05-17T10:00:26.439Z\"}, \"eval_math500_sft_rasp_20\": {\"created_at\": \"2026-05-17T06:23:52.474Z\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"updated_at\": \"2026-05-17T09:24:16.959Z\"}, \"eval_unstructured_20\": {\"created_at\": \"2026-05-17T05:35:41.205Z\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"updated_at\": \"2026-05-17T08:50:18.688Z\"}, \"eval_humaneval_sft_standard_20\": {\"created_at\": \"2026-05-17T07:56:08.222Z\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"updated_at\": \"2026-05-17T08:31:52.684Z\"}, \"eval_humaneval_sft_rasp_20\": {\"created_at\": \"2026-05-17T07:19:22.820Z\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"updated_at\": \"2026-05-17T07:55:52.564Z\"}, \"multiseed_serial_westb\": {\"created_at\": \"2026-05-17T05:47:08.060Z\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"updated_at\": \"2026-05-17T07:50:11.807Z\"}, \"eval_humaneval_grpo_rasp_20\": {\"created_at\": \"2026-05-17T06:42:19.044Z\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"updated_at\": \"2026-05-17T07:15:58.856Z\"}, \"eval_humaneval_unpruned\": {\"created_at\": \"2026-05-17T06:23:55.527Z\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"updated_at\": \"2026-05-17T06:42:38.578Z\"}, \"eval_grpo_rasp_25\": {\"created_at\": \"2026-05-16T20:04:16.057Z\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"updated_at\": \"2026-05-17T05:27:33.072Z\"}, \"eval_grpo_standard_25\": {\"created_at\": \"2026-05-16T19:39:31.510Z\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"updated_at\": \"2026-05-17T04:49:07.062Z\"}, \"sft_standard_20_retrain\": {\"created_at\": \"2026-05-15T08:00:22.779Z\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"updated_at\": \"2026-05-17T03:29:39.616Z\"}, \"eval_sft_grasp_20\": {\"created_at\": \"2026-05-15T15:45:15.051Z\", \"metrics\": {\"accuracy\": 0.41, \"n_total\": 100, \"note\": \"论文核心数据点: GraSP post-SFT 41% vs Standard 64% (p=0.001) vs RASP 57%\", \"p_value_vs_standard\": 0.001, \"rasp_ref\": 0.57, \"standard_ref\": 0.64}, \"updated_at\": \"2026-05-17T03:29:38.882Z\"}, \"eval-sft-alpha-0p0\": {\"created_at\": \"2026-05-15T14:26:31.883Z\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"updated_at\": \"2026-05-17T03:29:37.940Z\"}, \"eval-sft-alpha-1p0\": {\"created_at\": \"2026-05-15T14:51:22.694Z\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"updated_at\": \"2026-05-17T03:29:36.910Z\"}, \"eval_sft_unpruned_n100\": {\"created_at\": \"2026-05-16T01:40:17.686Z\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"updated_at\": \"2026-05-17T03:29:35.970Z\"}, \"eval_sft_unpruned_full\": {\"created_at\": \"2026-05-16T01:40:17.174Z\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"updated_at\": \"2026-05-17T03:29:35.056Z\"}, \"eval_grpo_unpruned_v2_step90\": {\"created_at\": \"2026-05-16T03:05:00.333Z\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-17T03:29:34.226Z\"}, \"eval_grpo_unpruned_v2_step100\": {\"created_at\": \"2026-05-16T03:04:55.936Z\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-17T03:29:33.203Z\"}, \"sft_rasp_25\": {\"created_at\": \"2026-05-16T05:26:38.517Z\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"updated_at\": \"2026-05-17T03:29:32.685Z\"}, \"sft_standard_25\": {\"created_at\": \"2026-05-16T05:21:16.758Z\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"updated_at\": \"2026-05-17T03:29:22.232Z\"}, \"sft_standard_25_westd\": {\"created_at\": \"2026-05-16T15:52:30.818Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"updated_at\": \"2026-05-17T03:29:21.686Z\"}, \"eval_grpo_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:57.504Z\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:20.851Z\"}, \"eval_grpo_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:59.175Z\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:19.801Z\"}, \"eval_grpo_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:53.951Z\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:18.878Z\"}, \"eval_pass_k8_unpruned_qwen_math\": {\"created_at\": \"2026-05-16T16:43:10.425Z\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:29:17.923Z\"}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"created_at\": \"2026-05-16T16:43:12.096Z\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:29:16.961Z\"}, \"eval_sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T18:16:58.087Z\", \"metrics\": {\"accuracy\": 0.73, \"mode\": \"greedy\", \"n_correct\": 146, \"n_samples\": 200}, \"updated_at\": \"2026-05-17T03:29:16.019Z\"}, \"eval_grpo_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:55.747Z\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-17T03:29:14.637Z\"}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"created_at\": \"2026-05-16T16:43:11.344Z\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"updated_at\": \"2026-05-17T03:29:13.689Z\"}, \"sft-alpha-1p0\": {\"created_at\": \"2026-05-15T13:53:32.178Z\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"updated_at\": \"2026-05-17T03:28:07.214Z\"}, \"prune_rasp_30\": {\"created_at\": \"2026-05-16T09:03:45.925Z\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"updated_at\": \"2026-05-17T03:28:01.089Z\"}, \"prune_standard_30\": {\"created_at\": \"2026-05-16T09:06:31.546Z\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"updated_at\": \"2026-05-17T03:27:59.680Z\"}, \"prune_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T09:30:44.270Z\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"updated_at\": \"2026-05-17T03:27:58.263Z\"}, \"prune_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T11:00:13.880Z\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"updated_at\": \"2026-05-17T03:27:56.876Z\"}, \"prune_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:05.915Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"updated_at\": \"2026-05-17T03:27:55.586Z\"}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:27:01.192Z\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"updated_at\": \"2026-05-17T03:15:54.640Z\"}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:31:55.162Z\", \"updated_at\": \"2026-05-17T01:56:11.192Z\"}, \"eval_sft_rasp_20_full\": {\"created_at\": \"2026-05-15T16:21:29.964Z\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"updated_at\": \"2026-05-17T01:29:36.754Z\"}, \"inference_speedup_plan016_v2\": {\"created_at\": \"2026-05-16T21:56:34.646Z\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"updated_at\": \"2026-05-17T00:49:42.978Z\"}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"created_at\": \"2026-05-16T21:54:25.214Z\", \"updated_at\": \"2026-05-16T23:23:37.778Z\"}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:39:30.069Z\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"updated_at\": \"2026-05-16T20:25:58.464Z\"}, \"eval_postprune_rasp_25\": {\"created_at\": \"2026-05-16T08:07:02.187Z\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"updated_at\": \"2026-05-16T20:09:54.911Z\"}, \"grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:37:40.324Z\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"updated_at\": \"2026-05-16T20:02:41.614Z\"}, \"grpo_standard_25\": {\"created_at\": \"2026-05-16T08:42:41.240Z\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"updated_at\": \"2026-05-16T19:37:31.250Z\"}, \"eval_sft_rasp_25\": {\"created_at\": \"2026-05-16T06:17:33.814Z\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"updated_at\": \"2026-05-16T19:15:43.879Z\"}, \"sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:51.076Z\", \"updated_at\": \"2026-05-16T18:01:41.992Z\"}, \"grpo_rasp_qwen_math_v3\": {\"created_at\": \"2026-05-16T14:49:39.708Z\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"updated_at\": \"2026-05-16T15:54:29.413Z\"}, \"sft_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:43.369Z\", \"updated_at\": \"2026-05-16T14:50:02.686Z\"}, \"eval_sft_standard_25\": {\"created_at\": \"2026-05-16T07:05:10.825Z\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"updated_at\": \"2026-05-16T13:23:38.482Z\"}, \"eval_sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T12:04:49.969Z\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"updated_at\": \"2026-05-16T12:50:43.619Z\"}, \"eval_sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T12:04:49.248Z\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"updated_at\": \"2026-05-16T12:50:42.647Z\"}, \"sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T11:15:20.187Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"updated_at\": \"2026-05-16T12:04:20.943Z\"}, \"sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T11:15:13.431Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"updated_at\": \"2026-05-16T12:03:33.361Z\"}, \"eval_sft_standard_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:10.910Z\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"updated_at\": \"2026-05-16T11:32:27.012Z\"}, \"eval_sft_rasp_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:07.028Z\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"updated_at\": \"2026-05-16T11:32:23.931Z\"}, \"prune_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:39.656Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"updated_at\": \"2026-05-16T10:31:42.144Z\"}, \"sft_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:11:00.051Z\", \"updated_at\": \"2026-05-16T10:10:19.019Z\"}, \"sft_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:10:59.311Z\", \"updated_at\": \"2026-05-16T10:10:17.852Z\"}, \"prune_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:03:56.378Z\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"updated_at\": \"2026-05-16T08:04:22.864Z\"}, \"prune_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:01:57.095Z\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"updated_at\": \"2026-05-16T08:04:20.185Z\"}, \"eval_grpo_rasp_v9_step10\": {\"created_at\": \"2026-05-16T03:40:46.186Z\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"updated_at\": \"2026-05-16T08:01:06.191Z\"}, \"eval_grpo_rasp_v9_step5\": {\"created_at\": \"2026-05-16T01:55:35.424Z\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"updated_at\": \"2026-05-16T05:18:16.131Z\"}, \"prune_standard_25\": {\"created_at\": \"2026-05-16T05:13:52.855Z\", \"updated_at\": \"2026-05-16T05:16:41.032Z\"}, \"prune_rasp_25\": {\"created_at\": \"2026-05-16T05:13:52.292Z\", \"updated_at\": \"2026-05-16T05:16:39.998Z\"}, \"grpo_unpruned_v2\": {\"created_at\": \"2026-05-16T01:45:10.586Z\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"updated_at\": \"2026-05-16T04:43:16.844Z\"}, \"grpo_stage2_rasp_20_v9\": {\"created_at\": \"2026-05-15T22:37:13.593Z\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"updated_at\": \"2026-05-16T03:38:37.387Z\"}, \"alpha_ablation_sweep\": {\"created_at\": \"2026-05-15T20:15:39.765Z\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"updated_at\": \"2026-05-16T00:18:46.780Z\"}, \"sft_unpruned_baseline\": {\"created_at\": \"2026-05-15T22:07:43.929Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"updated_at\": \"2026-05-16T00:18:44.096Z\"}, \"eval_sft_rasp_full_westd\": {\"created_at\": \"2026-05-15T20:36:02.786Z\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"updated_at\": \"2026-05-15T21:42:41.916Z\"}, \"eval_sft_standard_full_westd\": {\"created_at\": \"2026-05-15T20:36:01.803Z\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"updated_at\": \"2026-05-15T21:42:40.854Z\"}, \"eval_sft_rasp_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:08.437Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"updated_at\": \"2026-05-15T20:11:02.033Z\"}, \"eval_sft_standard_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:09.850Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"updated_at\": \"2026-05-15T20:11:00.967Z\"}, \"eval_sft_standard_20_westd_n100\": {\"created_at\": \"2026-05-15T17:39:03.607Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"updated_at\": \"2026-05-15T19:30:00.797Z\"}, \"eval_sft_rasp_20_westd_n100\": {\"created_at\": \"2026-05-15T17:35:08.417Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"updated_at\": \"2026-05-15T19:29:59.250Z\"}, \"sft_rasp_20_westd_retrain\": {\"created_at\": \"2026-05-15T16:59:51.103Z\", \"updated_at\": \"2026-05-15T18:36:33.103Z\"}, \"sft_standard_20_westd_retrain\": {\"created_at\": \"2026-05-15T17:05:52.927Z\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"updated_at\": \"2026-05-15T18:36:32.558Z\"}, \"grasp_baseline_westd\": {\"created_at\": \"2026-05-15T12:40:34.072Z\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"updated_at\": \"2026-05-15T17:12:21.555Z\"}, \"eval_sft_alpha_2p0\": {\"created_at\": \"2026-05-15T15:42:36.917Z\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"updated_at\": \"2026-05-15T16:41:41.929Z\"}, \"sft_alpha2_0_westd\": {\"created_at\": \"2026-05-15T14:32:54.953Z\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"updated_at\": \"2026-05-15T15:41:31.384Z\"}, \"alpha_ablation_westd_cal256\": {\"created_at\": \"2026-05-15T09:46:30.119Z\", \"metrics\": {\"alpha_4_0_accuracy\": 0.4, \"finding\": \"α=4.0 gives 40% post-prune accuracy (highest), non-monotonic relationship between α and accuracy\"}, \"updated_at\": \"2026-05-15T15:07:37.593Z\"}, \"sft_grasp_20_westd\": {\"created_at\": \"2026-05-15T13:50:39.294Z\", \"updated_at\": \"2026-05-15T15:01:02.359Z\"}, \"sft_alpha4_0_westd_retry\": {\"created_at\": \"2026-05-15T12:46:36.918Z\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"updated_at\": \"2026-05-15T13:48:13.666Z\"}, \"reeval_postprune_definitive\": {\"created_at\": \"2026-05-15T09:46:32.498Z\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"updated_at\": \"2026-05-15T12:30:41.698Z\"}, \"sft_standard_20\": {\"created_at\": \"2026-05-14T23:37:34.863Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"updated_at\": \"2026-05-15T02:49:41.141Z\"}, \"sft_rasp_20\": {\"created_at\": \"2026-05-14T23:37:33.162Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"updated_at\": \"2026-05-15T02:49:39.222Z\"}}, \"count\": 249, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
OK, this is returning all data but it's too large. Let me also get the full registry with spec fields. I need to have an agent parse both files and extract all mappings. 

Actually, I already have one file with full fields (50 results) and now I have another with all results (just exp_id, metrics, created_at, updated_at, tags). Let me also get all with spec fields.

Let me have an agent do all the remaining parsing work - matching the additional experiments that weren't in the first 50.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "d06d4134-1a14-4c2c-9e0a-6f7661ec58f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVMQW3VJFX2zf7AkbguAWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 56515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 892
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

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Tc7ZkPR52HzWNi9Rt7jTxS`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "exp_id",
    "metrics",
    "spec",
    "created_at"
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
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "4a7541bf-eb55-449f-a1b0-07409f178bce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVMQW3VJFX2zf7AkbguAWt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 56515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 892
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

_source line 77 · 2026-05-23T10:52:35.172Z_

<details><summary>↩ Tool result · `toolu_01Tc7ZkPR52HzWNi9Rt7jTxS`</summary>

```text
Error: result (245,301 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "69ae3b7b-911e-4228-a783-ae52dd177cb4",
  "tool_use_result": {
    "content": "Error: result (245,301 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T23:11:09.017Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-23T02:59:15.985Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-23T05:07:09.002Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-23T03:19:40.950Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-23T00:01:54.194Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"created_at\": \"2026-05-22T23:02:44.335Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}}, \"eval_math500_sft_cka_only_20_westd\": {\"created_at\": \"2026-05-22T20:45:21.526Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T22:23:27.589Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"created_at\": \"2026-05-22T15:12:46.181Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"created_at\": \"2026-05-22T20:50:24.239Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}}, \"eval_math500_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-19T01:34:44.782Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"created_at\": \"2026-05-22T15:20:44.460Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T18:26:16.273Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"created_at\": \"2026-05-22T15:20:47.150Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"created_at\": \"2026-05-22T15:06:22.386Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T16:26:01.516Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:33.753Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}}, \"grpo_random_20_seed456\": {\"created_at\": \"2026-05-22T12:00:38.940Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}}, \"eval_gsm8k_sft_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:43.950Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"eval_gsm8k_grpo_depth_first_20\": {\"created_at\": \"2026-05-22T14:20:41.126Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}}, \"grpo_random_20_seed123_v2\": {\"created_at\": \"2026-05-22T14:22:29.868Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"created_at\": \"2026-05-22T09:30:06.630Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}}, \"eval_math500_sft_random_20_v3\": {\"created_at\": \"2026-05-22T04:11:52.462Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}}, \"eval_gsm8k_sft_alpha3p0_20\": {\"created_at\": \"2026-05-22T10:24:58.696Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}}, \"grpo_rasp_alpha3p0_20_v2\": {\"created_at\": \"2026-05-22T10:40:19.362Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"created_at\": \"2026-05-22T03:49:45.575Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}}, \"grpo_random_20_seed123\": {\"created_at\": \"2026-05-22T10:34:12.100Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}}, \"grpo_rasp_alpha3p0_20\": {\"created_at\": \"2026-05-22T08:48:06.001Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}}, \"eval_gsm8k_sft_alpha2p0_20\": {\"created_at\": \"2026-05-22T10:19:50.623Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"created_at\": \"2026-05-22T10:19:48.133Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T08:50:34.293Z\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"created_at\": \"2026-05-22T09:28:08.089Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"created_at\": \"2026-05-22T09:28:05.478Z\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-22T04:31:30.202Z\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"created_at\": \"2026-05-22T03:49:50.201Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"created_at\": \"2026-05-22T03:49:52.414Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}}, \"eval_math500_sft_standard_25\": {\"created_at\": \"2026-05-21T02:58:32.492Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"created_at\": \"2026-05-21T18:59:18.863Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}}, \"sft_alpha4_20_v2\": {\"created_at\": \"2026-05-21T18:30:48.284Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20 --num_epochs 2 --lr 2e-5\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"401581\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_alpha4_20_v2.log\", \"submitted_at\": \"2026-05-21T18:31:05.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"final_train_loss\": 0.8118, \"token_accuracy\": 0.8165, \"epochs\": 2, \"steps\": 936}}, \"eval_math500_grpo_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:50.310Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}}, \"eval_math500_sft_cka_only_25_v2\": {\"created_at\": \"2026-05-21T13:54:51.945Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}}, \"eval_gsm8k_sft_standard_25\": {\"created_at\": \"2026-05-21T08:13:12.112Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}}, \"eval_math500_grpo_cka_only_20\": {\"created_at\": \"2026-05-18T02:41:32.199Z\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}}, \"eval_gsm8k_grpo_standard_25\": {\"created_at\": \"2026-05-21T06:42:08.819Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}}, \"eval_gsm8k_sft_cka_only_25\": {\"created_at\": \"2026-05-21T06:47:14.010Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}}, \"eval_gsm8k_sft_random_20\": {\"created_at\": \"2026-05-21T06:47:16.459Z\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"created_at\": \"2026-05-21T04:56:52.006Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}}, \"grpo_standard_25_westb\": {\"created_at\": \"2026-05-21T03:00:00.000Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}}, \"eval_gsm8k_grpo_random_20_v2\": {\"created_at\": \"2026-05-21T04:56:53.980Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}}, \"sft_random_20\": {\"created_at\": \"2026-05-21T03:44:24.654Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}}, \"grpo_random_20\": {\"created_at\": \"2026-05-17T13:30:31.016Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20 --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"317332\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20.log\", \"submitted_at\": \"2026-05-21T03:46:03.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}}, \"grpo_cka_only_25\": {\"created_at\": \"2026-05-21T02:49:22.258Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"310542\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-SFT\", \"seed\": 42}, \"metrics\": {\"reward\": 0.2875, \"steps\": 100}}, \"eval_humaneval_sft_standard_25\": {\"created_at\": \"2026-05-21T02:43:32.214Z\", \"spec\": {\"command\": \"python eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"server\": \"westb-23072\", \"data_path\": \"openai/openai_humaneval\", \"data_count\": 164, \"model_name\": \"Qwen2.5-Coder-3B-pruned-standard-25-sft\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"eval_data\": \"HumanEval\"}, \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}}, \"sft_cka_only_25\": {\"created_at\": \"2026-05-21T01:50:42.758Z\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}, \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"307651\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_25.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\"}}, \"prune_cka_only_25\": {\"created_at\": \"2026-05-18T13:43:54.266Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode cka_only --sparsity 0.25 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --seed 42 --dtype bfloat16\", \"server\": \"westd-29022\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42}, \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T23:00:14.007Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed123_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T23:00:15.387Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed456_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T21:35:28.222Z\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}, \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed123_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed123\", \"eval_data\": \"gsm8k_test_n1319\"}}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T21:35:29.444Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed456\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}}, \"grpo_standard_15_seed456_v3\": {\"created_at\": \"2026-05-20T21:58:14.439Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed456_v3 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"287862\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed456_v3.log\", \"submitted_at\": \"2026-05-20T21:58:13.750Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 456}}, \"grpo_standard_15_seed123_v3\": {\"created_at\": \"2026-05-20T21:58:11.697Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed123_v3 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"287784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed123_v3.log\", \"submitted_at\": \"2026-05-20T21:58:10.978Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 123}}, \"grpo_cka_only_15_seed456\": {\"created_at\": \"2026-05-20T20:54:57.409Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed456 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"281727\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed456.log\", \"submitted_at\": \"2026-05-20T20:54:56.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 456, \"wall_clock_seconds\": 2420.0, \"gpu_hours\": 0.67}}, \"grpo_cka_only_15_seed123\": {\"created_at\": \"2026-05-20T20:54:54.710Z\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed123 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"281647\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed123.log\", \"submitted_at\": \"2026-05-20T20:54:54.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 123, \"wall_clock_seconds\": 2420.5, \"gpu_hours\": 0.67}}, \"eval_gsm8k_sft_standard_20\": {\"created_at\": \"2026-05-20T17:07:58.760Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 266847, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_20 (Qwen2.5-7B, 20% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}}, \"eval_gsm8k_dense_unpruned\": {\"created_at\": \"2026-05-20T16:28:28.020Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": 32154, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense, unpruned)\", \"seed\": 42, \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_dense_unpruned.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"created_at\": \"2026-05-20T16:32:21.874Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 264522, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_20 (Qwen2.5-7B, 20% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}}, \"eval_gsm8k_sft_cka_only_15\": {\"created_at\": \"2026-05-20T15:19:42.152Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 262728, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_15 (Qwen2.5-7B, 15% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}}, \"eval_gsm8k_sft_rasp_20\": {\"created_at\": \"2026-05-20T17:09:04.809Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 267009, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_rasp_20_westd (Qwen2.5-7B, 20% RASP sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}}, \"eval_gsm8k_grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T14:43:21.408Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 256586, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"grpo_standard_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}}, \"eval_gsm8k_sft_standard_15\": {\"created_at\": \"2026-05-20T14:23:49.568Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 256743, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_15 (Qwen2.5-7B, 15% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T13:32:17.474Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 252919, \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"created_at\": \"2026-05-20T13:31:33.529Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 252604, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\", \"eval_data\": \"gsm8k_n1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_seed456_full.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}}, \"eval_gsm8k_sft_qwen_standard_20\": {\"created_at\": \"2026-05-20T10:32:12.883Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_standard_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"18114\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_standard_20.log\", \"submitted_at\": \"2026-05-20T11:32:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 15018.0, \"gpu_hours\": 4.17}, \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"created_at\": \"2026-05-20T10:32:11.084Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_cka_only_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"18038\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_cka_only_20.log\", \"submitted_at\": \"2026-05-20T11:32:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 14658.4, \"gpu_hours\": 4.07}, \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"created_at\": \"2026-05-20T13:42:06.715Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 253918, \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"sft_standard_15 (pruned Qwen2.5-7B, 15% standard sparsity)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\"}, \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"created_at\": \"2026-05-20T10:27:04.283Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\"}, \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"created_at\": \"2026-05-20T10:27:05.741Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\"}, \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}}, \"grpo_cka_only_15_v2\": {\"created_at\": \"2026-05-20T11:58:03.218Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 250149, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_15_v2.log\", \"model_name\": \"sft_cka_only_15\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\"}, \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"created_at\": \"2026-05-20T11:36:13.866Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 249963, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_20_seed456.log\", \"model_name\": \"sft_cka_only_20\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"created_at\": \"2026-05-20T04:08:24.071Z\", \"spec\": {\"command\": \"python src/prune.py --mode standard --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 190349, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_standard_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"created_at\": \"2026-05-20T04:08:22.614Z\", \"spec\": {\"command\": \"python src/prune.py --mode cka_only --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 190269, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_cka_only_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"created_at\": \"2026-05-20T09:18:17.089Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --gpu 0 --num_train_epochs 1 --save_strategy no\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"9952\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-20T09:18:16.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-Pruned-20%\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"GSM8K train (7473 samples, SFT epoch 2)\", \"wall_clock_seconds\": 1918.9, \"gpu_hours\": 0.53}, \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T09:15:10.283Z\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed456 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"221008\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T09:15:19.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed456_n200.json\", \"wall_clock_seconds\": 2030.9, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T09:15:16.595Z\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed123 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"221158\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T09:15:26.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed123_n200.json\", \"wall_clock_seconds\": 2022.3, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}}, \"grpo_standard_20_seed456\": {\"created_at\": \"2026-05-20T06:22:10.493Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_steps 100 --save_steps 100 --gpu 0 --seed 456\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"211798\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T06:22:19.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"wall_clock_seconds\": 10289.1, \"gpu_hours\": 2.86}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}}, \"grpo_standard_20_seed123\": {\"created_at\": \"2026-05-20T06:22:27.444Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_steps 100 --max_completion_length 1024 --save_steps 100 --gpu 0 --run_name grpo_standard_20_seed123 --seed 123\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"211972\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T06:22:37.312Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"tmux_session\": \"grpo_standard_20_seed123\", \"wall_clock_seconds\": 10268.1, \"gpu_hours\": 2.85}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}}, \"eval_mbpp_grpo_standard_20_v3\": {\"created_at\": \"2026-05-19T21:00:40.293Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/logs/eval_mbpp_grpo_standard_20_v3.log\"}, \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:45.876Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"890564\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T12:23:31.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_1p5b\", \"seed\": 42, \"wall_clock_seconds\": 5434.5, \"gpu_hours\": 1.51}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"created_at\": \"2026-05-19T10:05:36.497Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"86171\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048_v3.log\", \"result_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"}, \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:47.965Z\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/sft_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"95940\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:45:57.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"metrics\": {\"pass_at_1\": 0.0061, \"n_correct\": 1, \"n_total\": 164, \"avg_response_length\": 1968.76, \"median_response_length\": 2048}, \"wall_clock_seconds\": 6208.0, \"gpu_hours\": 1.72}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:32:50.649Z\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/grpo_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"96018\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:46:00.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\", \"wall_clock_seconds\": 7116.7, \"gpu_hours\": 1.98}, \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:23:35.431Z\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-SFT\", \"seed\": 42, \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"created_at\": \"2026-05-19T22:33:19.363Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-GRPO\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"created_at\": \"2026-05-19T22:26:22.996Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_standard_20.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"tmux_session\": \"eval_mbpp_sft_standard_20_v4\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}}, \"eval_mbpp_grpo_standard_20_v4\": {\"created_at\": \"2026-05-19T21:01:23.058Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"mbpp_sanitized_374\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}}, \"cka_scoring_stability_ablation\": {\"created_at\": \"2026-05-19T21:21:10.933Z\", \"spec\": {\"command\": \"python src/cka_stability_analysis.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json --device cuda:0\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 143187, \"data_path\": \"openai/gsm8k\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\"}, \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}}, \"eval_mbpp_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-19T18:56:15.766Z\", \"spec\": {\"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": \"0\", \"model_name\": \"sft_standard_20_1p5b\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"mbpp\", \"data_path\": \"mbpp\", \"data_count\": 0, \"seed\": 0}, \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}}, \"eval_mbpp_grpo_rasp_20\": {\"created_at\": \"2026-05-19T18:18:35.729Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"127964\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}}, \"eval_mbpp_sft_rasp_20\": {\"created_at\": \"2026-05-19T18:18:34.640Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"133674\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log\", \"submitted_at\": \"2026-05-19T20:00:13.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 4067.0, \"gpu_hours\": 1.13}, \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"created_at\": \"2026-05-19T17:20:00.596Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_cka_only_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 123029, \"log_path\": \"/tmp/eval_mbpp_sft_cka_only_20.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-pruned-20%-SFT-CKA-only\", \"seed\": 42}, \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:50.597Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"909411\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-rasp-20-SFT\", \"metrics\": {\"pass_at_1\": 0, \"stderr\": 0, \"n_passed\": 0, \"n_total\": 164}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_1p5b_2048.log\"}, \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"created_at\": \"2026-05-19T14:41:07.213Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_cka_only_20.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_cka_only_20.log\", \"submitted_at\": \"2026-05-19T18:08:02.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 17.3, \"gpu_hours\": 0.0}, \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"created_at\": \"2026-05-19T17:19:18.419Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_shortgpt_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 122867, \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_shortgpt_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/tmp/eval_gsm8k_grpo_shortgpt_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\"}, \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"created_at\": \"2026-05-19T15:47:16.122Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-7B-ShortGPT-20pct-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20/\", \"eval_data\": \"gsm8k:test\"}, \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"created_at\": \"2026-05-19T14:22:26.084Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --gpu 3 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"112015\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_shortgpt_20.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"shortgpt_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\"}}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T17:47:34.008Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_seed123.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"eval_data\": \"gsm8k_test\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed123\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\"}, \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"created_at\": \"2026-05-19T11:35:48.029Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-standard-20-GRPO\", \"tmux_session\": \"eval_humaneval_grpo_standard_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.log\"}}, \"gradient_flow_v3\": {\"created_at\": \"2026-05-19T15:03:16.535Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 pruned_rasp_20 --model_names CKA-only Standard RASP --n_steps 200 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"901553\", \"data_path\": \"openai/gsm8k train split\", \"data_count\": 200, \"model_name\": \"pruned_cka_only_20 + pruned_standard_20 + pruned_rasp_20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/gradient_flow_v3.log\"}, \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-19T12:47:37.399Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.json\", \"server\": \"westd-29022\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"GSM8K\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}}, \"eval_mbpp_dense_unpruned\": {\"created_at\": \"2026-05-19T13:47:53.814Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python src/eval_mbpp.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_dense_unpruned.json'\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_dense_unpruned.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"pid\": \"108291\"}, \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"created_at\": \"2026-05-19T13:18:20.664Z\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"pid\": \"107932\"}, \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}, \"grpo_cka_only_20_seed123\": {\"created_at\": \"2026-05-19T09:27:11.294Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/grpo_train.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --num_train_steps 100 --seed 123'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"857962\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"pruned_cka_only_20\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_20_seed123.log\"}, \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"created_at\": \"2026-05-19T14:44:25.606Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 --model_names CKA-only Standard --n_steps 20 --seed 42\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 20, \"model_name\": \"Qwen2-7B pruned variants\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/gradient_flow.log\"}, \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"created_at\": \"2026-05-19T14:21:15.548Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_cka_reliability.py --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --pruned_model /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --num_samples 1024 --n_splits 5 --max_length 512 --output /root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"cka_reliability\", \"data_path\": \"GSM8K calibration subset\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + pruned_cka_only_20\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/cka_reliability_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"created_at\": \"2026-05-19T07:05:14.343Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048\", \"server\": \"westd-29022\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.log\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"created_at\": \"2026-05-19T09:27:07.470Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"78740\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048, sys.executable fix)\"}, \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}}, \"eval_math500_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-18T22:36:14.421Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"36703\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-18T23:23:59.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wall_clock_seconds\": 49459.6, \"gpu_hours\": 13.74}, \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:55.912Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"wall_clock_seconds\": 50738.5, \"gpu_hours\": 14.09}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-19T09:27:09.334Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"83299\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"GSM8K (1319 samples)\"}, \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"created_at\": \"2026-05-19T06:38:59.146Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"HumanEval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"created_at\": \"2026-05-19T04:46:38.286Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json\", \"server\": \"westb-23072\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_unstructured_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\"}, \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"created_at\": \"2026-05-19T04:11:28.637Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"66521\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-19T04:11:28.118Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"HumanEval\", \"wall_clock_seconds\": 12309.1, \"gpu_hours\": 3.42}, \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}}, \"grpo_standard_20_fair\": {\"created_at\": \"2026-05-18T01:05:44.644Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_total_limit 3 --save_steps 10 --reward_desert_patience 200 --run_name grpo_standard_20_fair\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (GRPO training)\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_fair.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"74224\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-18T01:05:44.210Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3631.9, \"gpu_hours\": 1.01}, \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}}, \"inference_bench_clean_v2\": {\"created_at\": \"2026-05-19T01:42:25.421Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/measure_inference_speed.py --models original:/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B pruned_cka_only_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 pruned_standard_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json --n_prompts 50 --max_new_tokens 256'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"56892\", \"log_path\": \"~/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log\", \"submitted_at\": \"2026-05-19T01:42:24.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Dense + CKA-only 20% + Standard 20%\", \"data_path\": \"gsm8k test (50 prompts)\", \"data_count\": 50, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"wall_clock_seconds\": 3702.3, \"gpu_hours\": 1.03}, \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T18:10:57.471Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"845212\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json\", \"submitted_at\": \"2026-05-18T23:43:58.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_1p5b\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"gsm8k\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"wall_clock_seconds\": 10779.5, \"gpu_hours\": 2.99}, \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}}, \"eval_math500_grpo_standard_20_fair_v2\": {\"created_at\": \"2026-05-18T18:24:25.108Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json --max_new_tokens 2048'\", \"gpu\": [\"cuda:1\"], \"pid\": \"22049\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fair_v2.log\"}, \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}}, \"eval_math500_sft_rasp_20_2048\": {\"created_at\": \"2026-05-18T22:36:16.836Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"39767\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.log\", \"submitted_at\": \"2026-05-18T23:54:16.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_westd\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 6287.1, \"gpu_hours\": 1.75}, \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}}, \"eval_math500_dense_2048\": {\"created_at\": \"2026-05-18T22:08:58.081Z\", \"spec\": {\"gpu\": [\"cuda:0\"], \"pid\": \"32469\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_2048.json\"}, \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}}, \"eval_math500_grpo_rasp_20_fair\": {\"created_at\": \"2026-05-18T18:16:25.616Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_fair.json --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"model_name\": \"grpo_stage2_rasp_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_grpo_rasp_20_fair.log\"}, \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T17:51:20.577Z\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-1.5B-sft-cka-only-20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}}, \"sft_standard_20_retrain_westd\": {\"created_at\": \"2026-05-18T22:40:50.567Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 2\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"34346\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain_westd.log\", \"submitted_at\": \"2026-05-18T22:40:50.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pruned_standard_20 -> sft_standard_20\", \"data_path\": \"gsm8k (SFT recovery)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"wall_clock_seconds\": 2533.8, \"gpu_hours\": 0.7}, \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T16:59:22.921Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_rasp_20_1p5b/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"eval_data\": \"gsm8k:test\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"created_at\": \"2026-05-18T18:16:24.171Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_sft_cka_only_20_v4.log\", \"results_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v4.json\"}, \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}}, \"grpo_cka_only_20_extended_300\": {\"created_at\": \"2026-05-18T14:51:36.423Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"11457\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log\", \"submitted_at\": \"2026-05-18T15:10:04.515Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (CKA-only 20% pruned, SFT recovered, GRPO extended)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"z9f0z901\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 100}, \"wall_clock_seconds\": 23392.2, \"gpu_hours\": 6.5}, \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T16:38:01.585Z\", \"spec\": {\"gpu\": [\"cuda:0\"], \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T16:35:29.923Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_1p5b.json\"}, \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}}, \"eval_math500_dense_unpruned\": {\"created_at\": \"2026-05-18T13:42:10.786Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_unpruned.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"4223\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense unpruned)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_dense_unpruned.log\"}, \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}}, \"grpo_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T15:12:41.395Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"815395\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_1p5b.log\", \"submitted_at\": \"2026-05-18T15:13:38.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"a18r8uyw\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"learning_rate\": 1e-06, \"max_steps\": 100, \"optimizer\": \"adamw_8bit\"}, \"wall_clock_seconds\": 4438.5, \"gpu_hours\": 1.23}, \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T12:50:08.570Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"806188\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"8zkpr0hh\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training, not eval)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}}, \"grpo_standard_20_1p5b\": {\"created_at\": \"2026-05-18T14:15:13.990Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"811558\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"mm31apn0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}}, \"grpo_standard_20_extended_300_v2\": {\"created_at\": \"2026-05-18T13:53:41.781Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"6346\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 20% pruned, SFT recovered, GRPO extended v2)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"44cjdoiy\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 111}}, \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}}, \"sft_standard_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:56.278Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned)\", \"seed\": 42}}, \"sft_cka_only_20_1p5b\": {\"created_at\": \"2026-05-18T11:29:09.842Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy epoch --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned)\", \"seed\": 42}}, \"sft_rasp_20_1p5b\": {\"created_at\": \"2026-05-18T12:09:57.178Z\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"802010\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20_1p5b.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b\"}}, \"inference_bench_cka_only_20_clean\": {\"created_at\": \"2026-05-18T09:47:42.247Z\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --n_prompts 50 --max_new_tokens 512 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_cka_only_clean.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"openai/gsm8k (50 prompts)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20 + dense\", \"eval_data\": \"GSM8K 50 prompts (inference latency benchmark)\"}}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"created_at\": \"2026-05-18T05:54:02.634Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:0\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"776884\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-18T05:54:02.072Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20\", \"eval_data\": \"GSM8K test (1319 samples)\", \"wall_clock_seconds\": 10583.6, \"gpu_hours\": 2.94}, \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}}, \"grpo_cka_only_20\": {\"created_at\": \"2026-05-17T14:51:36.653Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_steps 99999 --reward_desert_patience 50 --run_name grpo_cka_only_20\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20.log\", \"pid\": \"725227\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:51:36.270Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 41272.3, \"gpu_hours\": 11.46, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wandb_run_id\": \"li451oi4\"}, \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}}, \"grpo_rasp_20_fair\": {\"created_at\": \"2026-05-17T23:50:31.502Z\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/train_grpo_v5.py --model_path sft_rasp_20_westd --output_dir grpo_stage2_rasp_20_fair --gpu 0 --max_steps 100 --lr 1e-6 --beta 0.01 --loss_type dapo\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.3, \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_fair.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"68913\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T23:50:31.086Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4668.5}}, \"eval_postprune_standard_30\": {\"created_at\": \"2026-05-17T19:08:46.051Z\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\", \"checkpoint_source\": \"pruned_standard_30\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\\\"\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (N=200, post-prune accuracy eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.3, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_standard_30.log\", \"model_name\": \"pruned_standard_30\", \"pid\": \"47667\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:09:42.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19076.9}}, \"eval_sft_cka_only_20_n1319\": {\"created_at\": \"2026-05-17T18:20:20.406Z\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (1319 samples, greedy)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"49475\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:17:43.358Z\", \"submitted_via\": \"submit_training_job\"}}, \"prune_cka_only_30\": {\"created_at\": \"2026-05-17T21:42:06.467Z\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=\\\"\\\" python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores_dummy_ones.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\", \"data_count\": 0, \"data_path\": \"importance_scores_dummy_ones.pt + cka_scores.pt\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_postprune_rasp_30\": {\"created_at\": \"2026-05-17T18:22:00Z\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_30.json\", \"checkpoint_source\": \"pruned_rasp_30\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (200 samples, greedy)\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_rasp_30.log\", \"model_name\": \"pruned_rasp_30\", \"pid\": \"43911\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_via\": \"submit_training_job\"}}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"created_at\": \"2026-05-17T16:26:15.836Z\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.34, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_2048_v2.log\", \"pid\": \"36724\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T16:26:15.449Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4840.6}}, \"eval_humaneval_grpo_standard_20_2048\": {\"created_at\": \"2026-05-17T13:41:03.761Z\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 4.58, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"pid\": \"27194\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16473.3}}, \"grpo_rasp_25\": {\"created_at\": \"2026-05-16T08:42:40.256Z\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"spec\": {\"command\": \"previous run (bc4ojqie) completed 100/100 steps, restoring status\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"model_name\": \"sft_rasp_25 (RASP 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_humaneval_grpo_rasp_20_2048\": {\"created_at\": \"2026-05-17T13:41:44.795Z\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"spec\": {\"account\": \"root\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_cka_only_20\": {\"created_at\": \"2026-05-17T14:28:35.380Z\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20.json\\\"\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"GSM8K (N=200)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"723605\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:29:08.063Z\", \"submitted_via\": \"submit_training_job\"}}, \"sft_cka_only_20\": {\"created_at\": \"2026-05-17T13:43:50.320Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --save_strategy no --gpu 0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.69, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_20.log\", \"pid\": \"720955\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T13:47:02.912Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2486.8}}, \"eval_humaneval_unpruned_2048\": {\"created_at\": \"2026-05-17T12:40:50.255Z\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_unpruned_2048.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": \"23707\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:06.754Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4337.5}}, \"eval_humaneval_sft_rasp_20_2048\": {\"created_at\": \"2026-05-17T12:40:51.686Z\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.03, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_2048.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"23785\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:09.839Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3691.7}}, \"eval_humaneval_grpo_standard_20\": {\"created_at\": \"2026-05-17T10:00:40.683Z\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"python src/eval_humaneval.py --model_path grpo_stage2_standard_20_v8/checkpoint-50\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.56, \"log_path\": \"westd results/eval_humaneval_grpo_standard_20.json\", \"model_name\": \"grpo_stage2_standard_20_v8\", \"pid\": \"16483\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T10:00:40.348Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12799.5}}, \"eval_math500_unpruned\": {\"created_at\": \"2026-05-17T06:23:49.923Z\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_gradient_postsft\": {\"created_at\": \"2026-05-17T10:07:58.644Z\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gradient_postsft.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.27, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gradient_postsft.log\", \"pid\": \"701495\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T10:07:58.275Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4578.0}}, \"gradient_sft_v3\": {\"created_at\": \"2026-05-17T09:28:21.646Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"checkpoint_source\": \"pruned_gradient_20 (gradient scoring, 19.09% sparsity)\", \"command\": \"python src/sft_recovery.py --model_path pruned_gradient_20 --output_dir sft_gradient_20 --gpu 0 --save_strategy no --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (SFT training data)\", \"eval_data\": \"N/A - this is SFT training, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.66, \"log_path\": \"~/runs/recovery_aware_struct_prune/gradient_sft_v3.log\", \"model_name\": \"pruned_gradient_20\", \"pid\": \"699032\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T09:28:21.306Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2385.7}}, \"eval_math500_sft_standard_20\": {\"created_at\": \"2026-05-17T06:23:54.283Z\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_standard_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard.log\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_math500_sft_rasp_20\": {\"created_at\": \"2026-05-17T06:23:52.474Z\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_rasp_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp.log\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_unstructured_20\": {\"created_at\": \"2026-05-17T05:35:41.205Z\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"checkpoint_source\": \"pruned_unstructured_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_unstructured_20_n1319.json'\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=1319, greedy)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_unstructured_20.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unstructured magnitude 20%)\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"pid\": \"eval_unstructured_20\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_humaneval_sft_standard_20\": {\"created_at\": \"2026-05-17T07:56:08.222Z\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.6, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"9605\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:56:07.888Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2144.8}}, \"eval_humaneval_sft_rasp_20\": {\"created_at\": \"2026-05-17T07:19:22.820Z\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.61, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"7528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:19:22.501Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2190.1}}, \"multiseed_serial_westb\": {\"created_at\": \"2026-05-17T05:47:08.060Z\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20, sft_standard_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py (4 serial evals)'\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=200, seeds 123+456)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/multiseed_serial.log\", \"model_name\": \"sft_rasp_20 + sft_standard_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20\", \"pid\": 681896, \"seed\": \"123,456\", \"server\": \"westb-23072\"}}, \"eval_humaneval_grpo_rasp_20\": {\"created_at\": \"2026-05-17T06:42:19.044Z\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"humaneval\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log\", \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"5264\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T06:42:18.740Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2020.1}}, \"eval_humaneval_unpruned\": {\"created_at\": \"2026-05-17T06:23:55.527Z\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"checkpoint_source\": \"DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, pass@1)\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"model_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_25\": {\"created_at\": \"2026-05-16T20:04:16.057Z\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test split (N=1319, greedy)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_rasp_25.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP 25% pruned, SFT, GRPO 100 steps)\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"pid\": \"639423\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_grpo_standard_25\": {\"created_at\": \"2026-05-16T19:39:31.510Z\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"eval_data\": \"GSM8K test (n=1319)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_standard_25.log\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"pid\": 48540, \"seed\": 42, \"server\": \"westd-11672\", \"started_at\": \"2026-05-17T05:19:52\"}}, \"sft_standard_20_retrain\": {\"created_at\": \"2026-05-15T08:00:22.779Z\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"checkpoint_source\": \"/root/autodl-tmp/pruned_standard_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.81, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"515168\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-15T11:47:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2914.0}}, \"eval_sft_grasp_20\": {\"created_at\": \"2026-05-15T15:45:15.051Z\", \"metrics\": {\"accuracy\": 0.41, \"n_total\": 100, \"note\": \"论文核心数据点: GraSP post-SFT 41% vs Standard 64% (p=0.001) vs RASP 57%\", \"p_value_vs_standard\": 0.001, \"rasp_ref\": 0.57, \"standard_ref\": 0.64}, \"spec\": {\"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_grasp_20_n100.json\", \"hypothesis\": \"GraSP post-SFT GSM8K eval (N=100, greedy). GraSP post-prune ~6%, post-SFT loss=0.59, token_acc=0.84. Three-way comparison: Standard 64% vs RASP 57% vs GraSP ?%. Parent: sft_grasp_20_westd.\", \"model_name\": \"Qwen2.5-1.5B-GraSP-20%-SFT\", \"parent\": \"sft_grasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval-sft-alpha-0p0\": {\"created_at\": \"2026-05-15T14:26:31.883Z\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.42, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-0p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=0.0 post-SFT\", \"pid\": \"40489\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:26:31.816Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1529.3}}, \"eval-sft-alpha-1p0\": {\"created_at\": \"2026-05-15T14:51:22.694Z\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"pid\": \"42530\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2013.4}}, \"eval_sft_unpruned_n100\": {\"created_at\": \"2026-05-16T01:40:17.686Z\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_n100.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 100 --seed 42\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"log_path\": \"/tmp/eval_unpruned_n100.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_unpruned_full\": {\"created_at\": \"2026-05-16T01:40:17.174Z\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_full.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 1319 --seed 42\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full_1319\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Unpruned SFT baseline full GSM8K eval for three-way comparison\", \"log_path\": \"/tmp/eval_unpruned_full.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"pid\": 74129, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_unpruned_v2_step90\": {\"created_at\": \"2026-05-16T03:05:00.333Z\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step90.json\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step90.log\", \"pid\": \"83667\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:13.660Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6194.8}}, \"eval_grpo_unpruned_v2_step100\": {\"created_at\": \"2026-05-16T03:04:55.936Z\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step100.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step100.log\", \"pid\": \"83589\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:11.392Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6195.8}}, \"sft_rasp_25\": {\"created_at\": \"2026-05-16T05:26:38.517Z\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_25.log\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"pid\": \"88528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T05:27:08.163Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3002.5}}, \"sft_standard_25\": {\"created_at\": \"2026-05-16T05:21:16.758Z\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_standard_25_retry.log\", \"model_name\": \"pruned_standard_25 (Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_standard_25_westd\": {\"created_at\": \"2026-05-16T15:52:30.818Z\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.91, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_westd.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned)\", \"pid\": \"21488\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T15:52:30.596Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3273.0}}, \"eval_grpo_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:57.504Z\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:2\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-postGRPO\", \"parent\": \"grpo_rasp_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T15:59:59.175Z\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:3\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-postGRPO\", \"parent\": \"grpo_standard_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:53.951Z\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_25_qwen_math.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-postGRPO\", \"parent\": \"grpo_rasp_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_unpruned_qwen_math\": {\"created_at\": \"2026-05-16T16:43:10.425Z\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:1\", \"model_name\": \"grpo_unpruned_v2\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"created_at\": \"2026-05-16T16:43:12.096Z\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:3\", \"model_name\": \"grpo_rasp_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T18:16:58.087Z\", \"metrics\": {\"accuracy\": 0.73, \"mode\": \"greedy\", \"n_correct\": 146, \"n_samples\": 200}}, \"eval_grpo_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T15:59:55.747Z\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_25_qwen_math.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-postGRPO\", \"parent\": \"grpo_standard_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"created_at\": \"2026-05-16T16:43:11.344Z\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_sft_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:2\", \"model_name\": \"sft_qwen_math_rasp_20\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft-alpha-1p0\": {\"created_at\": \"2026-05-15T13:53:32.178Z\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_1.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.57, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft-alpha-1p0.log\", \"model_name\": \"pruned_alpha1.0 (α=1.0, 20% sparsity)\", \"pid\": \"38797\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:53:32.117Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2069.9}}, \"prune_rasp_30\": {\"created_at\": \"2026-05-16T09:03:45.925Z\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt\", \"data_count\": 512, \"data_path\": \"calibration data\", \"log_path\": \"N/A (CPU)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_standard_30\": {\"created_at\": \"2026-05-16T09:06:31.546Z\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.30 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_prune_standard_30_20260516T090533.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_rasp_25_qwen_math\": {\"created_at\": \"2026-05-16T09:30:44.270Z\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_standard_25_qwen_math\": {\"created_at\": \"2026-05-16T11:00:13.880Z\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.25 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:05.915Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math\", \"command\": \"python src/prune.py --mode rasp-rlvr --sparsity 0.20\", \"data_count\": 0, \"data_path\": \"N/A\", \"log_path\": \"/tmp/prune_rasp_rlvr_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:27:01.192Z\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"gsm8k_test\", \"eval_data\": \"gsm8k_test\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 162.58, \"eos_rate\": 0.995, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.89, \"stderr\": 0.0221, \"temperature\": 0.7, \"truncated\": 8}, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"61473\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"created_at\": \"2026-05-16T23:31:55.162Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k (test split, N=200)\", \"eval_data\": \"GSM8K test (200 samples, pass@k=8, T=0.7)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_standard_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 164.15, \"eos_rate\": 0.9956, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.855, \"stderr\": 0.0249, \"temperature\": 0.7}, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_full\": {\"created_at\": \"2026-05-15T16:21:29.964Z\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full_n1319.json\", \"data_count\": 1319, \"data_path\": \"gsm8k:test\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full.log\", \"model_name\": \"sft_rasp_20\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"inference_speedup_plan016_v2\": {\"created_at\": \"2026-05-16T21:56:34.646Z\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20 + sft_standard_20 + dense\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --n_prompts 50 --max_new_tokens 512\", \"data_count\": 50, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test 50 prompts (inference latency benchmark)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense/rasp_20/standard_20)\", \"seed\": 42, \"server\": \"westb-23072\", \"tmux_session\": \"inference_bench\"}}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"created_at\": \"2026-05-16T21:54:25.214Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --pass_k 8 --num_samples_per_prompt 8 --temperature 0.7 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json\", \"data_count\": 200, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test (200 samples)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_pass_k8_standard_20_v2.log\", \"metrics\": {\"avg_response_length\": 129.995, \"eos_rate\": 0.999375, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1599, \"pass_at_k\": 0.91, \"stderr\": 0.0202, \"temperature\": 0.7, \"truncated\": 1}, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:39:30.069Z\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_rlvr_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k\", \"model_name\": \"grpo_rasp_rlvr_20_qwen_math\", \"parent\": \"grpo_rasp_rlvr_20_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_postprune_rasp_25\": {\"created_at\": \"2026-05-16T08:07:02.187Z\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --max_samples 100 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split (N=100)\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned, no SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T19:37:40.324Z\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --gpu 0 --max_steps 100 --run_name grpo_rasp_rlvr_20_qwen_math --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR 20% pruned, SFT recovered)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_standard_25\": {\"created_at\": \"2026-05-16T08:42:41.240Z\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_standard_25 --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% GRPO (100 steps). 25% Standard 对照，配合 grpo_rasp_25 (frac_zero=0.875)。Parent: sft_standard_25_westd.\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned, SFT recovered)\", \"parent\": \"sft_standard_25_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_25\": {\"created_at\": \"2026-05-16T06:17:33.814Z\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log\", \"model_name\": \"sft_rasp_25 (RASP 25% SFT recovered)\", \"pid\": \"602990\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_rasp_rlvr_20_qwen_math\": {\"created_at\": \"2026-05-16T17:11:51.076Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/sft_recovery.py --model_path pruned_rasp_rlvr_20_qwen_math --num_train_epochs 2 --lr 2e-5\", \"data_count\": 0, \"data_path\": \"built-in SFT data\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_rasp_qwen_math_v3\": {\"created_at\": \"2026-05-16T14:49:39.708Z\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_rasp_qwen_math_v3 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.01, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP 20% SFT recovered)\", \"pid\": \"16812\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T14:49:39.494Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3634.1}}, \"sft_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:43.369Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k_sft\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20.log\", \"model_name\": \"Qwen2.5-7B-Instruct (RASP-RLVR pruned 20%)\", \"pid\": \"620651\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_sft_standard_25\": {\"created_at\": \"2026-05-16T07:05:10.825Z\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"model_name\": \"sft_standard_25 (Standard 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"eval_sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T12:04:49.969Z\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_standard_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:3\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-SFT\", \"pid\": \"6215\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:12.481Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2731.1}}, \"eval_sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T12:04:49.248Z\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_rasp_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:2\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-SFT\", \"pid\": \"6135\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:10.285Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2732.4}}, \"sft_qwen_math_standard_25\": {\"created_at\": \"2026-05-16T11:15:20.187Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --gpu 3 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_qwen_math_rasp_25\": {\"created_at\": \"2026-05-16T11:15:13.431Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --gpu 2 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_standard_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:10.910Z\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_standard_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_qwen_math_n200\": {\"created_at\": \"2026-05-16T11:15:07.028Z\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_rasp_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_rlvr_20\": {\"created_at\": \"2026-05-16T09:50:39.656Z\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp-rlvr --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_code_rasp_rlvr_prune_20260516T095028.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"sft_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:11:00.051Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --gpu 1 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:10:59.311Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --gpu 0 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_standard_20_qwen_math\": {\"created_at\": \"2026-05-16T08:03:56.378Z\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.20 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"prune_rasp_20_qwen_math\": {\"created_at\": \"2026-05-16T08:01:57.095Z\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt + cka_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_grpo_rasp_v9_step10\": {\"created_at\": \"2026-05-16T03:40:46.186Z\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\\\"\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step10.log\", \"model_name\": \"grpo_stage2_rasp_20_v9 checkpoint-10\", \"pid\": \"585618\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-16T04:57:36.867Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11009.3}}, \"eval_grpo_rasp_v9_step5\": {\"created_at\": \"2026-05-16T01:55:35.424Z\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-5\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step5.log\"}}, \"prune_standard_25\": {\"created_at\": \"2026-05-16T05:13:52.855Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.25 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"prune_rasp_25\": {\"created_at\": \"2026-05-16T05:13:52.292Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance/CKA scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}}, \"grpo_unpruned_v2\": {\"created_at\": \"2026-05-16T01:45:10.586Z\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"resume from checkpoint-20, save_total_limit=3, max_steps=100\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_train_7473\", \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_unpruned_v2.log\", \"model_name\": \"sft_unpruned_baseline (unpruned)\", \"pid\": 77647, \"seed\": 42, \"server\": \"westd-11672\"}}, \"grpo_stage2_rasp_20_v9\": {\"created_at\": \"2026-05-15T22:37:13.593Z\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 30 --save_steps 5 --save_total_limit 5 --reward_desert_patience 50 --run_name grpo_stage2_rasp_20_v9\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/grpo_rasp_v9.log\", \"model_name\": \"sft_rasp_20\", \"notes\": \"Auto-launcher tmux session auto_v9_launcher waiting for alpha sweep to finish before starting on cuda:0\", \"pid\": 566666, \"seed\": 42, \"server\": \"westb-23072\"}}, \"alpha_ablation_sweep\": {\"created_at\": \"2026-05-15T20:15:39.765Z\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"spec\": {\"alphas\": [0, 0.25, 0.5, 1, 2], \"calibration_samples\": 512, \"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/\", \"command\": \"bash run_alpha_sweep_fix.sh\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/alpha_sweep_fix.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"notes\": \"Alpha ablation: 0.25, 0.5, 1.0, 2.0. Partial results: alpha=0.0 acc=0.27 eos=0.80, alpha=0.25 acc=0.23 eos=0.63. Currently running alpha=0.5 eval.\", \"pid\": 556867, \"seed\": 42, \"server\": \"westb-23072\", \"sparsity\": 0.2}}, \"sft_unpruned_baseline\": {\"created_at\": \"2026-05-15T22:07:43.929Z\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"checkpoint_source\": \"/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/sft_recovery.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42 --save_strategy no --run_name sft_unpruned_baseline_v2\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k train\", \"estimated_time_minutes\": 33, \"gpu_id\": \"cuda:1\", \"hyperparams\": {\"batch_size\": 1, \"epochs\": 2, \"gradient_accumulation_steps\": 8, \"lr\": 2e-05, \"max_seq_length\": 2048, \"save_strategy\": \"no\", \"seed\": 42}, \"log_path\": \"/tmp/sft_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": 67546, \"seed\": 42, \"server\": \"westd-11672\", \"tmux_session\": \"sft_unpruned\", \"total_steps\": 1870}}, \"eval_sft_rasp_full_westd\": {\"created_at\": \"2026-05-15T20:36:02.786Z\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output results/eval_sft_rasp_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:1\", \"log_path\": \"/tmp/eval_rasp_full.log\", \"model_name\": \"sft_rasp_20_westd\", \"output_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"pid\": 62565, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_standard_full_westd\": {\"created_at\": \"2026-05-15T20:36:01.803Z\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_standard_20_westd_full.json\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output results/eval_sft_standard_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/eval_standard_full.log\", \"model_name\": \"sft_standard_20_westd\", \"output_path\": \"results/eval_sft_standard_20_westd_full.json\", \"pid\": 62463, \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:08.437Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_rasp_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:08.325Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2807.6}}, \"eval_sft_standard_20_westd_n100_v2\": {\"created_at\": \"2026-05-15T19:24:09.850Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_standard_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_standard_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:09.745Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2805.4}}, \"eval_sft_standard_20_westd_n100\": {\"created_at\": \"2026-05-15T17:39:03.607Z\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"spec\": {\"checkpoint_source\": \"sft_standard_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_standard_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"eval_sft_rasp_20_westd_n100\": {\"created_at\": \"2026-05-15T17:35:08.417Z\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_rasp_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_rasp_20_westd_retrain\": {\"created_at\": \"2026-05-15T16:59:51.103Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --gpu 0 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"sft_standard_20_westd_retrain\": {\"created_at\": \"2026-05-15T17:05:52.927Z\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}}, \"grasp_baseline_westd\": {\"created_at\": \"2026-05-15T12:40:34.072Z\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"GraSP pruning pipeline\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096\", \"command_note\": \"实际运行命令无 --output_path 和 --seed，但源码默认 seed=42 且 output_path 自动回退到 results/eval_pruned_graspune_20_greedy.json\", \"data_count\": 100, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.44, \"log_path\": \"results/eval_grasp_n100.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (GraSP pruned 20%)\", \"pid\": \"38120\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T12:45:44.074Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15997.5}}, \"eval_sft_alpha_2p0\": {\"created_at\": \"2026-05-15T15:42:36.917Z\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_alpha_2.0_n100.json\", \"data_count\": 100, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.98, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"model_name\": \"alpha_2.0_sft\", \"pid\": \"45428\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T15:42:47.927Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3534.0}}, \"sft_alpha2_0_westd\": {\"created_at\": \"2026-05-15T14:32:54.953Z\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"spec\": {\"checkpoint_source\": \"alpha_ablation_westd_cal256 (pruned_rasp_20_alpha2.0)\", \"command\": \"python sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_models/pruned_rasp_20_alpha2.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8\", \"data_count\": 7473, \"data_path\": \"gsm8k train split\", \"eval_data\": \"gsm8k train (SFT recovery, not eval)\", \"gpu\": \"cuda:1\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned alpha=2.0, 20% sparsity)\", \"pid\": 43065, \"seed\": 42, \"server\": \"westd-11672\"}}, \"alpha_ablation_westd_cal256\": {\"created_at\": \"2026-05-15T09:46:30.119Z\", \"metrics\": {\"alpha_4_0_accuracy\": 0.4, \"finding\": \"α=4.0 gives 40% post-prune accuracy (highest), non-monotonic relationship between α and accuracy\"}}, \"sft_grasp_20_westd\": {\"created_at\": \"2026-05-15T13:50:39.294Z\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.15, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_grasp_20_westd.log\", \"pid\": \"38509\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:51:47.632Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4148.4}}, \"sft_alpha4_0_westd_retry\": {\"created_at\": \"2026-05-15T12:46:36.918Z\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.1, \"log_path\": \"/tmp/sft_alpha4.0.log\", \"model_name\": \"pruned_alpha4.0 (a=4.0, 20% sparsity)\", \"pid\": \"37013\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:42:03.641Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 358.8}}, \"reeval_postprune_definitive\": {\"created_at\": \"2026-05-15T09:46:32.498Z\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/pruned_{rasp,standard}_20 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"gsm8k_test\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_20 + pruned_standard_20\", \"seed\": 42, \"server\": \"westb-23072 + westd-11672\"}}, \"sft_standard_20\": {\"created_at\": \"2026-05-14T23:37:34.863Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"249655\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:25.361Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2999.5}}, \"sft_rasp_20\": {\"created_at\": \"2026-05-14T23:37:33.162Z\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.82, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20.log\", \"model_name\": \"pruned_rasp_20\", \"pid\": \"249577\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:23.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2961.2}}}, \"count\": 249, \"total\": 249, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9186}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have 245K chars with exp_id, metrics, spec, created_at for ALL success experiments. Let me launch an agent to parse this larger file and complete the mapping for all the experiments I still need. 

Let me launch the agent with all the paper values that still need mapping.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "15531f10-ed03-4730-95f9-b2ac4d5a9048",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 789
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

_source line 79_

有了完整 registry 数据（245K），启动 agent 解析剩余实验映射。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5992aa79-f55b-4562-9da5-4ad60fa1cf29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 789
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

_source line 80_

<details open><summary>🔧 Tool call — Agent · `toolu_01FCi6H5x65GUEFHnY4j1d2s`</summary>

```json
{
  "description": "Parse full registry for remaining mappings",
  "prompt": "You need to parse a large JSON registry file and extract ALL experiment records, matching them to paper values.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt`\n\nFormat: JSON `{result: string}` where `result` is a YAML string containing experiment records. Each has `exp_id`, `metrics`, `spec` (with server, output_path, checkpoint_path, command etc.), `created_at`.\n\n**I already have matches for these from the first 50 results (the most recent). I need you to find ALL remaining experiments. Specifically, I need matches for:**\n\n### MUST FIND (not in first 50):\n\n**GSM8K 7B 20% core results:**\n- CKA-only SFT=63.91% → look for exp_id like `eval_gsm8k_sft_cka_only_20*`\n- CKA-only GRPO seed42=64.37% → look for `eval_gsm8k_grpo_cka_only_20*`\n- CKA-only GRPO seed123=64.22% → look for `eval_gsm8k_grpo_cka_only_20*seed123*`\n- CKA-only GRPO seed456=64.58% → look for `eval_gsm8k_grpo_cka_only_20*seed456*`\n- Standard SFT=59.29% → look for `eval_gsm8k_sft_standard_20*`\n- Standard GRPO seeds (59.44%, 60.20%, ?) → look for `eval_gsm8k_grpo_standard_20*`\n- RASP α=1.0 SFT=61.49% → look for `eval_gsm8k_sft_rasp*` or `eval_gsm8k_sft_alpha1*`\n- RASP α=1.0 GRPO=60.88% → look for `eval_gsm8k_grpo_rasp*` or `eval_gsm8k_grpo_alpha1*`\n- ShortGPT SFT=44.73% → look for `eval_gsm8k_sft_shortgpt*` or `eval_gsm8k_sft_depth*`\n- ShortGPT GRPO=43.37% → look for `eval_gsm8k_grpo_shortgpt*` or `eval_gsm8k_grpo_depth*`\n- Dense/Unpruned 81.27% or 90.83% → look for `eval_gsm8k*unpruned*` or `eval_gsm8k*dense*`\n\n**GSM8K 15% sparsity:**\n- CKA-only SFT=72.18% → `eval_gsm8k_sft_cka_only_15*`\n- CKA-only GRPO=72.76% (3 seeds: 72.10%, ?, 73.09%) → `eval_gsm8k_grpo_cka_only_15*`\n- Standard SFT=66.49% → `eval_gsm8k_sft_standard_15*`\n- Standard GRPO=65.56% (3 seeds) → `eval_gsm8k_grpo_standard_15*`\n\n**GSM8K 30% sparsity cliff:**\n- Standard=4%, RASP=0%, CKA=0% → look for `*30*` experiments\n\n**Peak rewards:**\n- CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190 → look for GRPO training runs\n\n**MBPP evaluations:**\n- Dense 53.48%, CKA 12.83%/14.17%, Standard 12.03%/13.10%, RASP 11.76%/13.10%, ShortGPT 10.43%/14.44%\n- Look for `eval_mbpp*`\n\n**1.5B cross-scale:**\n- CKA GSM8K=35.48%, Rew=0.238 → `*1p5b*` or `*1.5b*`\n- Standard 22.29%, 0.084\n- RASP 26.16%, 0.099\n\n**Inference efficiency:**\n- Dense Latency=6.682s, Memory=16.22GB, TPS=72.0\n- Look for `*inference*` or `*benchmark*` or `*latency*`\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n- Look for `*cka_stability*` or `*calibration*`\n\n**Gradient flow:**\n- CKA vs Standard=2.89×, CKA vs RASP=2.26×, RASP vs Standard=1.28×\n- Look for `*gradient*`\n\n**Extended training 300 steps:**\n- CKA-only 64.37%→64.37%, Standard 59.44%→59.29%\n- Look for `*300*` or `*extended*`\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n- Look for `*unstructured*` or `*magnitude*`\n\n**Cross-architecture Qwen2.5-Math-7B (remaining):**\n- Standard Post-Prune=18.5%, Post-SFT=21.00%\n- Look for `*qwen_math*standard*`\n\n**MATH-500 Standard 25% GRPO=12.8%:**\n- Look for `eval_math500_grpo_standard_25*`\n\n**Dense MATH-500=53.0%:**\n- Look for `eval_math500*dense*` or `eval_math500*unpruned*`\n\n**Instructions:**\n1. Use `python3` or `jq` to parse the file\n2. First probe structure: `jq 'keys' file`, then parse the result field\n3. Extract ALL experiments (may be YAML inside the result string)\n4. For EACH experiment, output: `exp_id | metrics | server (from spec) | output_path/checkpoint_path (from spec) | created_at`\n5. Group by which paper value they match\n6. For any paper value that has NO matching registry experiment, explicitly say so\n7. Note the eval script version: if created_at is 2026-05-23 or later → NEW, before → OLD. Experiments with v2/v3 suffix re-evaluated with NEW script.\n\nOutput the COMPLETE mapping. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "85510dbe-4454-4a97-9654-e8ac41d34a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCHRqnYiKhSB1KYzod2yYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 789,
      "cache_read_input_tokens": 57407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 789
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


### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Parse full registry for remaining mappings",
  "task_type": "local_agent",
  "prompt": "You need to parse a large JSON registry file and extract ALL experiment records, matching them to paper values.\n\nThe file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt`\n\nFormat: JSON `{result: string}` where `result` is a YAML string containing experiment records. Each has `exp_id`, `metrics`, `spec` (with server, output_path, checkpoint_path, command etc.), `created_at`.\n\n**I already have matches for these from the first 50 results (the most recent). I need you to find ALL remaining experiments. Specifically, I need matches for:**\n\n### MUST FIND (not in first 50):\n\n**GSM8K 7B 20% core results:**\n- CKA-only SFT=63.91% → look for exp_id like `eval_gsm8k_sft_cka_only_20*`\n- CKA-only GRPO seed42=64.37% → look for `eval_gsm8k_grpo_cka_only_20*`\n- CKA-only GRPO seed123=64.22% → look for `eval_gsm8k_grpo_cka_only_20*seed123*`\n- CKA-only GRPO seed456=64.58% → look for `eval_gsm8k_grpo_cka_only_20*seed456*`\n- Standard SFT=59.29% → look for `eval_gsm8k_sft_standard_20*`\n- Standard GRPO seeds (59.44%, 60.20%, ?) → look for `eval_gsm8k_grpo_standard_20*`\n- RASP α=1.0 SFT=61.49% → look for `eval_gsm8k_sft_rasp*` or `eval_gsm8k_sft_alpha1*`\n- RASP α=1.0 GRPO=60.88% → look for `eval_gsm8k_grpo_rasp*` or `eval_gsm8k_grpo_alpha1*`\n- ShortGPT SFT=44.73% → look for `eval_gsm8k_sft_shortgpt*` or `eval_gsm8k_sft_depth*`\n- ShortGPT GRPO=43.37% → look for `eval_gsm8k_grpo_shortgpt*` or `eval_gsm8k_grpo_depth*`\n- Dense/Unpruned 81.27% or 90.83% → look for `eval_gsm8k*unpruned*` or `eval_gsm8k*dense*`\n\n**GSM8K 15% sparsity:**\n- CKA-only SFT=72.18% → `eval_gsm8k_sft_cka_only_15*`\n- CKA-only GRPO=72.76% (3 seeds: 72.10%, ?, 73.09%) → `eval_gsm8k_grpo_cka_only_15*`\n- Standard SFT=66.49% → `eval_gsm8k_sft_standard_15*`\n- Standard GRPO=65.56% (3 seeds) → `eval_gsm8k_grpo_standard_15*`\n\n**GSM8K 30% sparsity cliff:**\n- Standard=4%, RASP=0%, CKA=0% → look for `*30*` experiments\n\n**Peak rewards:**\n- CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190 → look for GRPO training runs\n\n**MBPP evaluations:**\n- Dense 53.48%, CKA 12.83%/14.17%, Standard 12.03%/13.10%, RASP 11.76%/13.10%, ShortGPT 10.43%/14.44%\n- Look for `eval_mbpp*`\n\n**1.5B cross-scale:**\n- CKA GSM8K=35.48%, Rew=0.238 → `*1p5b*` or `*1.5b*`\n- Standard 22.29%, 0.084\n- RASP 26.16%, 0.099\n\n**Inference efficiency:**\n- Dense Latency=6.682s, Memory=16.22GB, TPS=72.0\n- Look for `*inference*` or `*benchmark*` or `*latency*`\n\n**CKA stability:**\n- Spearman ρ min=0.964, mean=0.979\n- Look for `*cka_stability*` or `*calibration*`\n\n**Gradient flow:**\n- CKA vs Standard=2.89×, CKA vs RASP=2.26×, RASP vs Standard=1.28×\n- Look for `*gradient*`\n\n**Extended training 300 steps:**\n- CKA-only 64.37%→64.37%, Standard 59.44%→59.29%\n- Look for `*300*` or `*extended*`\n\n**Unstructured pruning:**\n- SFT=87.87%, GRPO=87.64%\n- Look for `*unstructured*` or `*magnitude*`\n\n**Cross-architecture Qwen2.5-Math-7B (remaining):**\n- Standard Post-Prune=18.5%, Post-SFT=21.00%\n- Look for `*qwen_math*standard*`\n\n**MATH-500 Standard 25% GRPO=12.8%:**\n- Look for `eval_math500_grpo_standard_25*`\n\n**Dense MATH-500=53.0%:**\n- Look for `eval_math500*dense*` or `eval_math500*unpruned*`\n\n**Instructions:**\n1. Use `python3` or `jq` to parse the file\n2. First probe structure: `jq 'keys' file`, then parse the result field\n3. Extract ALL experiments (may be YAML inside the result string)\n4. For EACH experiment, output: `exp_id | metrics | server (from spec) | output_path/checkpoint_path (from spec) | created_at`\n5. Group by which paper value they match\n6. For any paper value that has NO matching registry experiment, explicitly say so\n7. Note the eval script version: if created_at is 2026-05-23 or later → NEW, before → OLD. Experiments with v2/v3 suffix re-evaluated with NEW script.\n\nOutput the COMPLETE mapping. Be thorough.",
  "uuid": "303e2a18-d489-4ad5-b2be-1f77f60d2904",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


## Round 2

## Round 2

74 recorded events


### User

_source line 82 · 2026-05-23T10:53:17.827Z_

You need to parse a large JSON registry file and extract ALL experiment records, matching them to paper values.

The file is at: `/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt`

Format: JSON `{result: string}` where `result` is a YAML string containing experiment records. Each has `exp_id`, `metrics`, `spec` (with server, output_path, checkpoint_path, command etc.), `created_at`.

**I already have matches for these from the first 50 results (the most recent). I need you to find ALL remaining experiments. Specifically, I need matches for:**

### MUST FIND (not in first 50):

**GSM8K 7B 20% core results:**
- CKA-only SFT=63.91% → look for exp_id like `eval_gsm8k_sft_cka_only_20*`
- CKA-only GRPO seed42=64.37% → look for `eval_gsm8k_grpo_cka_only_20*`
- CKA-only GRPO seed123=64.22% → look for `eval_gsm8k_grpo_cka_only_20*seed123*`
- CKA-only GRPO seed456=64.58% → look for `eval_gsm8k_grpo_cka_only_20*seed456*`
- Standard SFT=59.29% → look for `eval_gsm8k_sft_standard_20*`
- Standard GRPO seeds (59.44%, 60.20%, ?) → look for `eval_gsm8k_grpo_standard_20*`
- RASP α=1.0 SFT=61.49% → look for `eval_gsm8k_sft_rasp*` or `eval_gsm8k_sft_alpha1*`
- RASP α=1.0 GRPO=60.88% → look for `eval_gsm8k_grpo_rasp*` or `eval_gsm8k_grpo_alpha1*`
- ShortGPT SFT=44.73% → look for `eval_gsm8k_sft_shortgpt*` or `eval_gsm8k_sft_depth*`
- ShortGPT GRPO=43.37% → look for `eval_gsm8k_grpo_shortgpt*` or `eval_gsm8k_grpo_depth*`
- Dense/Unpruned 81.27% or 90.83% → look for `eval_gsm8k*unpruned*` or `eval_gsm8k*dense*`

**GSM8K 15% sparsity:**
- CKA-only SFT=72.18% → `eval_gsm8k_sft_cka_only_15*`
- CKA-only GRPO=72.76% (3 seeds: 72.10%, ?, 73.09%) → `eval_gsm8k_grpo_cka_only_15*`
- Standard SFT=66.49% → `eval_gsm8k_sft_standard_15*`
- Standard GRPO=65.56% (3 seeds) → `eval_gsm8k_grpo_standard_15*`

**GSM8K 30% sparsity cliff:**
- Standard=4%, RASP=0%, CKA=0% → look for `*30*` experiments

**Peak rewards:**
- CKA=0.354, Standard=0.081, RASP=0.061, Random=0.190 → look for GRPO training runs

**MBPP evaluations:**
- Dense 53.48%, CKA 12.83%/14.17%, Standard 12.03%/13.10%, RASP 11.76%/13.10%, ShortGPT 10.43%/14.44%
- Look for `eval_mbpp*`

**1.5B cross-scale:**
- CKA GSM8K=35.48%, Rew=0.238 → `*1p5b*` or `*1.5b*`
- Standard 22.29%, 0.084
- RASP 26.16%, 0.099

**Inference efficiency:**
- Dense Latency=6.682s, Memory=16.22GB, TPS=72.0
- Look for `*inference*` or `*benchmark*` or `*latency*`

**CKA stability:**
- Spearman ρ min=0.964, mean=0.979
- Look for `*cka_stability*` or `*calibration*`

**Gradient flow:**
- CKA vs Standard=2.89×, CKA vs RASP=2.26×, RASP vs Standard=1.28×
- Look for `*gradient*`

**Extended training 300 steps:**
- CKA-only 64.37%→64.37%, Standard 59.44%→59.29%
- Look for `*300*` or `*extended*`

**Unstructured pruning:**
- SFT=87.87%, GRPO=87.64%
- Look for `*unstructured*` or `*magnitude*`

**Cross-architecture Qwen2.5-Math-7B (remaining):**
- Standard Post-Prune=18.5%, Post-SFT=21.00%
- Look for `*qwen_math*standard*`

**MATH-500 Standard 25% GRPO=12.8%:**
- Look for `eval_math500_grpo_standard_25*`

**Dense MATH-500=53.0%:**
- Look for `eval_math500*dense*` or `eval_math500*unpruned*`

**Instructions:**
1. Use `python3` or `jq` to parse the file
2. First probe structure: `jq 'keys' file`, then parse the result field
3. Extract ALL experiments (may be YAML inside the result string)
4. For EACH experiment, output: `exp_id | metrics | server (from spec) | output_path/checkpoint_path (from spec) | created_at`
5. Group by which paper value they match
6. For any paper value that has NO matching registry experiment, explicitly say so
7. Note the eval script version: if created_at is 2026-05-23 or later → NEW, before → OLD. Experiments with v2/v3 suffix re-evaluated with NEW script.

Output the COMPLETE mapping. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "517aebd0-0c0f-4ea3-b17f-be89eb7e8c1e"
}
```

</details>

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 16611,
    "tool_uses": 1,
    "duration_ms": 10627
  },
  "last_tool_name": "Bash",
  "uuid": "7519ce36-1b77-4bcb-8edc-9ea465412bef",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01LLWwLKuFAFrBAuTFrGmhPB`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "14ae84ec-ff5b-46b5-ac97-929d5fa76e50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QmS3UWPLtF9w7SaJzeEe1c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8352,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8352,
        "ephemeral_1h_input_tokens": 0
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

_source line 85 · 2026-05-23T10:53:28.506Z_

<details><summary>↩ Tool result · `toolu_01LLWwLKuFAFrBAuTFrGmhPB`</summary>

```text
245538 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "5d053e2a-fc5f-41b0-878c-7541890de01d"
}
```

</details>

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Running Probe file structure",
  "usage": {
    "total_tokens": 16613,
    "tool_uses": 2,
    "duration_ms": 11597
  },
  "last_tool_name": "Bash",
  "uuid": "92c086d3-88c1-4479-8451-6c9ab63e4d1c",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01HBDiq9WDa9Q4jj5AS15WTK`</summary>

```json
{
  "command": "head -c 500 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/mcp-agent-ml-research-read_registry-1779533555169.txt",
  "description": "Probe file structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "1610b899-6eee-4fa9-b50a-620bfefaa9b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QmS3UWPLtF9w7SaJzeEe1c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8352,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8352,
        "ephemeral_1h_input_tokens": 0
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

_source line 88 · 2026-05-23T10:53:29.498Z_

<details><summary>↩ Tool result · `toolu_01HBDiq9WDa9Q4jj5AS15WTK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_qwen_math_cka_only_20\": {\"created_at\": \"2026-05-22T23:11:09.017Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "0dc6668d-eb41-4fe0-811b-cbe25b7f4f62"
}
```

</details>

---


### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Running Parse JSON and list all experiment IDs",
  "usage": {
    "total_tokens": 18161,
    "tool_uses": 3,
    "duration_ms": 22821
  },
  "last_tool_name": "Bash",
  "uuid": "4aa41b46-c305-4e12-aefa-56c9f9d87465",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_015EMWiwRffjm3QCDgdsswkp`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779533555169.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\n# Print all exp_ids sorted\nfor eid in sorted(exps.keys()):\n    print(eid)\n\"",
  "description": "Parse JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "4ad4a15c-d59a-4db2-9419-d4d235f62fd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q92yKNWtewwdK8JmzksQ5o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 16604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1548,
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

_source line 91 · 2026-05-23T10:53:40.740Z_

<details><summary>↩ Tool result · `toolu_015EMWiwRffjm3QCDgdsswkp`</summary>

```text
Total experiments: 249

alpha_ablation_sweep
alpha_ablation_westd_cal256
cka_calibration_stability_ablation
cka_scoring_stability_ablation
eval-sft-alpha-0p0
eval-sft-alpha-1p0
eval_gradient_postsft
eval_grpo_rasp_20_qwen_math
eval_grpo_rasp_25
eval_grpo_rasp_25_qwen_math
eval_grpo_rasp_rlvr_20_qwen_math
eval_grpo_rasp_v9_step10
eval_grpo_rasp_v9_step5
eval_grpo_standard_20_qwen_math
eval_grpo_standard_25
eval_grpo_standard_25_qwen_math
eval_grpo_unpruned_v2_step100
eval_grpo_unpruned_v2_step90
eval_gsm8k_dense_unpruned
eval_gsm8k_grpo_alpha0p5_20
eval_gsm8k_grpo_alpha2p0_20
eval_gsm8k_grpo_alpha3p0_20
eval_gsm8k_grpo_alpha4_20_v3
eval_gsm8k_grpo_cka_only_15_seed123
eval_gsm8k_grpo_cka_only_15_seed456
eval_gsm8k_grpo_cka_only_15_v2
eval_gsm8k_grpo_cka_only_20_1p5b
eval_gsm8k_grpo_cka_only_20_seed123
eval_gsm8k_grpo_cka_only_20_seed456_full
eval_gsm8k_grpo_cka_only_20_v2
eval_gsm8k_grpo_cka_only_25_v3
eval_gsm8k_grpo_depth_first_20
eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3
eval_gsm8k_grpo_random_20_seed123_v2
eval_gsm8k_grpo_random_20_seed456
eval_gsm8k_grpo_random_20_v2
eval_gsm8k_grpo_rasp_20_1p5b
eval_gsm8k_grpo_rasp_20_fair
eval_gsm8k_grpo_shortgpt_20
eval_gsm8k_grpo_standard_15_seed123_v3
eval_gsm8k_grpo_standard_15_seed456_v3
eval_gsm8k_grpo_standard_15_v2
eval_gsm8k_grpo_standard_20_1p5b
eval_gsm8k_grpo_standard_20_fair_v2
eval_gsm8k_grpo_standard_20_seed123
eval_gsm8k_grpo_standard_20_seed123_full
eval_gsm8k_grpo_standard_20_seed456
eval_gsm8k_grpo_standard_20_seed456_full
eval_gsm8k_grpo_standard_25
eval_gsm8k_grpo_unstructured_20
eval_gsm8k_sft_alpha0p5_20
eval_gsm8k_sft_alpha2p0_20
eval_gsm8k_sft_alpha3p0_20
eval_gsm8k_sft_alpha4_20_v5
eval_gsm8k_sft_cka_only_15
eval_gsm8k_sft_cka_only_20
eval_gsm8k_sft_cka_only_20_1p5b
eval_gsm8k_sft_cka_only_25
eval_gsm8k_sft_depth_first_20
eval_gsm8k_sft_qwen_cka_only_20
eval_gsm8k_sft_qwen_standard_20
eval_gsm8k_sft_random_20
eval_gsm8k_sft_rasp_20
eval_gsm8k_sft_rasp_20_1p5b
eval_gsm8k_sft_shortgpt_20
eval_gsm8k_sft_standard_15
eval_gsm8k_sft_standard_20
eval_gsm8k_sft_standard_20_1p5b
eval_gsm8k_sft_standard_25
eval_humaneval_grpo_cka_only_20_1p5b_2048
eval_humaneval_grpo_cka_only_20_2048
eval_humaneval_grpo_rasp_20
eval_humaneval_grpo_rasp_20_2048
eval_humaneval_grpo_rasp_20_fair_2048
eval_humaneval_grpo_standard_20
eval_humaneval_grpo_standard_20_1p5b_2048
eval_humaneval_grpo_standard_20_2048
eval_humaneval_grpo_standard_20_fair_2048_v3
eval_humaneval_sft_cka_only_20_1p5b_2048
eval_humaneval_sft_cka_only_20_2048_v2
eval_humaneval_sft_rasp_20
eval_humaneval_sft_rasp_20_1p5b_2048
eval_humaneval_sft_rasp_20_2048
eval_humaneval_sft_rasp_20_2048_v2
eval_humaneval_sft_standard_20
eval_humaneval_sft_standard_20_1p5b_2048
eval_humaneval_sft_standard_20_2048_v2
eval_humaneval_sft_standard_20_2048_v3
eval_humaneval_sft_standard_25
eval_humaneval_unpruned
eval_humaneval_unpruned_2048
eval_math500_dense_2048
eval_math500_dense_unpruned
eval_math500_grpo_cka_only_20
eval_math500_grpo_cka_only_20_2048
eval_math500_grpo_cka_only_20_2048_v2
eval_math500_grpo_cka_only_25_v2
eval_math500_grpo_rasp_20_fair
eval_math500_grpo_rasp_alpha0p5_20
eval_math500_grpo_rasp_alpha1p0_20
eval_math500_grpo_rasp_alpha2p0_20
eval_math500_grpo_rasp_alpha3p0_20
eval_math500_grpo_rasp_alpha4p0_20
eval_math500_grpo_standard_20_fair_2048_v2
eval_math500_grpo_standard_20_fair_v2
eval_math500_sft_cka_only_20_v4_restart
eval_math500_sft_cka_only_20_westd
eval_math500_sft_cka_only_25_v2
eval_math500_sft_qwen_math_cka_only_20
eval_math500_sft_random_20_v3
eval_math500_sft_rasp_20
eval_math500_sft_rasp_20_2048
eval_math500_sft_rasp_alpha0p5_20
eval_math500_sft_rasp_alpha1p0_20_v2
eval_math500_sft_rasp_alpha2p0_20
eval_math500_sft_rasp_alpha3p0_20
eval_math500_sft_rasp_alpha4p0_20
eval_math500_sft_standard_20
eval_math500_sft_standard_20_1p5b
eval_math500_sft_standard_20_2048_v2
eval_math500_sft_standard_25
eval_math500_unpruned
eval_mbpp_dense_unpruned
eval_mbpp_grpo_cka_only_20
eval_mbpp_grpo_rasp_20
eval_mbpp_grpo_shortgpt_20_v2
eval_mbpp_grpo_standard_20_v3
eval_mbpp_grpo_standard_20_v4
eval_mbpp_sft_cka_only_20
eval_mbpp_sft_rasp_20
eval_mbpp_sft_shortgpt_20_v2
eval_mbpp_sft_standard_20_1p5b
eval_mbpp_sft_standard_20_v4
eval_pass_k8_rasp_20_grpo_deepseek
eval_pass_k8_rasp_20_grpo_qwen_math
eval_pass_k8_rasp_20_sft_qwen_math
eval_pass_k8_standard_20_grpo_deepseek
eval_pass_k8_standard_20_grpo_qwen_math_v2
eval_pass_k8_unpruned_qwen_math
eval_postprune_rasp_25
eval_postprune_rasp_30
eval_postprune_standard_30
eval_sft_alpha_2p0
eval_sft_cka_only_20
eval_sft_cka_only_20_n1319
eval_sft_grasp_20
eval_sft_qwen_math_rasp_25
eval_sft_qwen_math_standard_25
eval_sft_rasp_20_full
eval_sft_rasp_20_westd_n100
eval_sft_rasp_20_westd_n100_v2
eval_sft_rasp_25
eval_sft_rasp_full_westd
eval_sft_rasp_qwen_math_n200
eval_sft_rasp_rlvr_20_qwen_math
eval_sft_standard_20_westd_n100
eval_sft_standard_20_westd_n100_v2
eval_sft_standard_25
eval_sft_standard_full_westd
eval_sft_standard_qwen_math_n200
eval_sft_unpruned_full
eval_sft_unpruned_n100
eval_unstructured_20
gradient_flow_analysis
gradient_flow_v3
gradient_sft_v3
grasp_baseline_westd
grpo_alpha4_20
grpo_cka_only_15_seed123
grpo_cka_only_15_seed456
grpo_cka_only_15_v2
grpo_cka_only_20
grpo_cka_only_20_1p5b
grpo_cka_only_20_extended_300
grpo_cka_only_20_seed123
grpo_cka_only_20_seed456
grpo_cka_only_25
grpo_qwen_math_cka_only_20
grpo_random_20
grpo_random_20_seed123
grpo_random_20_seed123_v2
grpo_random_20_seed456
grpo_rasp_20_1p5b
grpo_rasp_20_fair
grpo_rasp_25
grpo_rasp_alpha3p0_20
grpo_rasp_alpha3p0_20_v2
grpo_rasp_qwen_math_v3
grpo_rasp_rlvr_20_qwen_math
grpo_stage2_rasp_20_v9
grpo_standard_15_seed123_v3
grpo_standard_15_seed456_v3
grpo_standard_15_v2
grpo_standard_20_1p5b
grpo_standard_20_extended_300_v2
grpo_standard_20_fair
grpo_standard_20_seed123
grpo_standard_20_seed456
grpo_standard_25
grpo_standard_25_westb
grpo_unpruned_v2
inference_bench_cka_only_20_clean
inference_bench_clean_v2
inference_speedup_plan016_v2
multiseed_serial_westb
prune_cka_only_25
prune_cka_only_30
prune_eval_cka_only_30
prune_eval_standard_30
prune_rasp_20_qwen_math
prune_rasp_25
prune_rasp_25_qwen_math
prune_rasp_30
prune_rasp_rlvr_20
prune_rasp_rlvr_20_qwen_math
prune_standard_20_qwen_math
prune_standard_25
prune_standard_25_qwen_math
prune_standard_30
reeval_postprune_definitive
sft-alpha-1p0
sft_alpha2_0_westd
sft_alpha4_0_westd_retry
sft_alpha4_20_v2
sft_cka_only_20
sft_cka_only_20_1p5b
sft_cka_only_25
sft_grasp_20_westd
sft_qwen_math_cka_only_20_v2
sft_qwen_math_rasp_25
sft_qwen_math_standard_25
sft_random_20
sft_rasp_20
sft_rasp_20_1p5b
sft_rasp_20_qwen_math
sft_rasp_20_westd_retrain
sft_rasp_25
sft_rasp_rlvr_20
sft_rasp_rlvr_20_qwen_math
sft_shortgpt_20
sft_standard_20
sft_standard_20_1p5b
sft_standard_20_qwen_math
sft_standard_20_retrain
sft_standard_20_retrain_westd
sft_standard_20_westd_retrain
sft_standard_25
sft_standard_25_westd
sft_unpruned_baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "4304c6ea-c98d-4d41-b60d-4284774d35da"
}
```

</details>

---


### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Running Extract full details for all 249 experiments",
  "usage": {
    "total_tokens": 22046,
    "tool_uses": 4,
    "duration_ms": 38585
  },
  "last_tool_name": "Bash",
  "uuid": "642f9222-1ba7-47fa-95b7-d0a938c375f9",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01SChnpyXRTAcVLix7697myX`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results && python3 << 'PYEOF'\nimport json\n\nwith open('mcp-agent-ml-research-read_registry-1779533555169.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Dump all experiments with full details\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    metrics = e.get('metrics', {})\n    spec = e.get('spec', {})\n    created = e.get('created_at', 'N/A')\n    server = spec.get('server', 'N/A')\n    output_path = spec.get('output_path', 'N/A')\n    checkpoint_path = spec.get('checkpoint_path', 'N/A')\n    command = spec.get('command', 'N/A')\n    \n    print(f\"=== {eid} ===\")\n    print(f\"  created_at: {created}\")\n    print(f\"  server: {server}\")\n    print(f\"  metrics: {json.dumps(metrics, indent=4)}\")\n    print(f\"  output_path: {output_path}\")\n    print(f\"  checkpoint_path: {checkpoint_path}\")\n    print(f\"  command: {command[:200] if command != 'N/A' else 'N/A'}\")\n    print()\nPYEOF",
  "description": "Extract full details for all 249 experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "bac29db9-b4df-4838-a242-bea93bc7adb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XPyuqzh8tKpw9iSWH61c42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3883,
      "cache_read_input_tokens": 18152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3883,
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

_source line 94 · 2026-05-23T10:53:56.519Z_

<details><summary>↩ Tool result · `toolu_01SChnpyXRTAcVLix7697myX`</summary>

```text
&lt;persisted-output>
Output too large (130.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/b1bham6qw.txt

Preview (first 2KB):
=== alpha_ablation_sweep ===
  created_at: 2026-05-15T20:15:39.765Z
  server: westb-23072
  metrics: {
    "alpha_0.0": {
        "accuracy": 0.27,
        "avg_len": 1192,
        "eos_rate": 0.8,
        "n_correct": 27,
        "n_total": 100
    },
    "alpha_0.25": {
        "accuracy": 0.23,
        "avg_len": 1834,
        "eos_rate": 0.63,
        "n_correct": 23,
        "n_total": 100
    },
    "alpha_0.5": {
        "accuracy": 0.22,
        "avg_len": 1141,
        "eos_rate": 0.81,
        "n_correct": 22,
        "n_total": 100
    },
    "alpha_1.0": {
        "accuracy": 0.31,
        "avg_len": 733,
        "eos_rate": 0.92,
        "n_correct": 31,
        "n_total": 100
    },
    "alpha_2.0": {
        "accuracy": 0.36,
        "avg_len": 2130,
        "eos_rate": 0.59,
        "n_correct": 36,
        "n_total": 100
    }
}
  output_path: N/A
  checkpoint_path: /root/recovery_aware_struct_prune/results/
  command: bash run_alpha_sweep_fix.sh

=== alpha_ablation_westd_cal256 ===
  created_at: 2026-05-15T09:46:30.119Z
  server: N/A
  metrics: {
    "alpha_4_0_accuracy": 0.4,
    "finding": "\u03b1=4.0 gives 40% post-prune accuracy (highest), non-monotonic relationship between \u03b1 and accuracy"
}
  output_path: N/A
  checkpoint_path: N/A
  command: N/A

=== cka_calibration_stability_ablation ===
  created_at: 2026-05-19T14:21:15.548Z
  server: westb-23072
  metrics: {
    "split_half_rho": 0.9932,
    "n_splits": 5,
    "size_sensitivity_128": 0.982,
    "size_sensitivity_256": 0.989,
    "size_sensitivity_512": 0.995
}
  output_path: N/A
  checkpoint_path: /root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json
  command: CUDA_VISIBLE_DEVICES=0 python src/run_cka_reliability.py --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --pruned_model /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --

=== cka_scoring_stability_ablation ===
  created_at: 2026-05-19T21:21:10.933Z
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "9a7cc1a4-7650-4042-873b-f980cb57422b"
}
```

</details>

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aaf740c46822c95dd",
  "tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/b1bham6qw.txt",
  "usage": {
    "total_tokens": 23595,
    "tool_uses": 5,
    "duration_ms": 41499
  },
  "last_tool_name": "Read",
  "uuid": "2ce014f1-39fa-4b70-b200-693facdc3e7d",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f"
}
```

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01Dp2Ri6XVQ3pWif9WQxyVFJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/3a90179e-e19e-41d1-8fb4-f23e916f555f/tool-results/b1bham6qw.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FCi6H5x65GUEFHnY4j1d2s",
  "session_id": "3a90179e-e19e-41d1-8fb4-f23e916f555f",
  "uuid": "7320817d-50c9-4bb3-ab36-01fd8e9fb3b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pzQDmvSiJ3KpeGAMFyG17",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1517,
      "cache_read_input_tokens": 22035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1517,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 32,
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
