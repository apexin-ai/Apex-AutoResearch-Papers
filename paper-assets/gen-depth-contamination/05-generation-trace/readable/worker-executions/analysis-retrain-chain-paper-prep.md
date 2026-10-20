# analysis retrain chain paper prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_analysis_retrain-chain-paper-prep_20260519T025458.log`
- **Structured JSON:** [`fff350ddebcc533189d6.json`](../../sessions/ff/fff350ddebcc533189d6.json)

## Before a recorded user message

41 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "b3c823af-a0e4-4fe7-bafd-99c1e1b538fe",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779172800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "102c881b-43ef-46f8-888b-fadd19dfcedd",
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the relevant files to gather the data needed for this task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "13b3c91c-8615-409d-8a38-0332f646ebb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q8YGpwhycRQTaxpbx4yTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13106
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

### Assistant

_source line 5_

读取所有相关文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "213d94fe-e3ac-48a9-b024-def85e77b01e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q8YGpwhycRQTaxpbx4yTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13106
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01J17iKwZ1bCTGqdkDK2H4Ld`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_depth7/retrain_depth7_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "636a844d-9168-4e40-aba2-b1d528def961",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q8YGpwhycRQTaxpbx4yTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13106
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

_source line 7 · 2026-05-19T02:55:10.472Z_

<details><summary>↩ Tool result · `toolu_01J17iKwZ1bCTGqdkDK2H4Ld`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\begin{tabular}{lcccc}
5	\toprule
6	\textbf{Pair} & \textbf{AUC} & \textbf{95\% CI} & \textbf{Per-fold AUC} & \textbf{JSD} \\
7	\midrule
8	0\,vs\,1 & 0.984 & [0.982, 0.985] & .983, .982, .984, .982, .987 & 0.2301 \\
9	1\,vs\,2 & 0.897 & [0.895, 0.899] & .892, .899, .899, .899, .897 & 0.1039 \\
10	2\,vs\,3 & 0.810 & [0.805, 0.814] & .809, .807, .818, .802, .813 & 0.0750 \\
11	3\,vs\,4 & 0.760 & [0.753, 0.767] & .753, .762, .775, .757, .753 & 0.0654 \\
12	4\,vs\,5 & 0.746 & [0.738, 0.754] & .743, .756, .752, .730, .748 & 0.0605 \\
13	5\,vs\,6 & 0.702 & [0.696, 0.708] & .701, .708, .710, .692, .698 & 0.0350 \\
14	6\,vs\,7 & 0.641 & [0.638, 0.645] & .642, .635, .646, .639, .643 & 0.0177 \\
15	\bottomrule
16	\end{tabular}
17	\caption{Qwen2.5-1.5B retrain-chain pairwise classification (depth 0--7). AUC and 95\% CI from 5-fold GroupKFold CV ($\text{mean} \pm 1.96 \cdot \text{std} / \sqrt{5}$). $K^{*}=7$ at $\theta=0.60$. JSD computed on full token-level log-probability distributions.}
18	\label{tab:retrain_depth7}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "36b2780d-ab01-471b-8949-c6999aa577ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_depth7/retrain_depth7_results.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Pair} & \\textbf{AUC} & \\textbf{95\\% CI} & \\textbf{Per-fold AUC} & \\textbf{JSD} \\\\\n\\midrule\n0\\,vs\\,1 & 0.984 & [0.982, 0.985] & .983, .982, .984, .982, .987 & 0.2301 \\\\\n1\\,vs\\,2 & 0.897 & [0.895, 0.899] & .892, .899, .899, .899, .897 & 0.1039 \\\\\n2\\,vs\\,3 & 0.810 & [0.805, 0.814] & .809, .807, .818, .802, .813 & 0.0750 \\\\\n3\\,vs\\,4 & 0.760 & [0.753, 0.767] & .753, .762, .775, .757, .753 & 0.0654 \\\\\n4\\,vs\\,5 & 0.746 & [0.738, 0.754] & .743, .756, .752, .730, .748 & 0.0605 \\\\\n5\\,vs\\,6 & 0.702 & [0.696, 0.708] & .701, .708, .710, .692, .698 & 0.0350 \\\\\n6\\,vs\\,7 & 0.641 & [0.638, 0.645] & .642, .635, .646, .639, .643 & 0.0177 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Qwen2.5-1.5B retrain-chain pairwise classification (depth 0--7). AUC and 95\\% CI from 5-fold GroupKFold CV ($\\text{mean} \\pm 1.96 \\cdot \\text{std} / \\sqrt{5}$). $K^{*}=7$ at $\\theta=0.60$. JSD computed on full token-level log-probability distributions.}\n\\label{tab:retrain_depth7}\n\\end{table}\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01N64JwQNAdFGmsstTAeWf92`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_chain/final_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "b9d343d9-38c4-4d00-a4b9-7dd7c48e2ca9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q8YGpwhycRQTaxpbx4yTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13106
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

_source line 9 · 2026-05-19T02:55:11.429Z_

<details><summary>↩ Tool result · `toolu_01N64JwQNAdFGmsstTAeWf92`</summary>

```text
1	{
2	  "experiment": "exp_qwen_retrain_chain",
3	  "model": "Qwen-1.5B",
4	  "domain": "retrain-chain",
5	  "status": "DONE",
6	  "checked_at": "2026-05-18T22:30:00Z",
7	  "ci_method": "5-fold CV",
8	  "K_star": 4,
9	  "pairwise_auc": {
10	    "mean": {
11	      "0v1": 0.9838,
12	      "1v2": 0.8969,
13	      "2v3": 0.8100,
14	      "3v4": 0.7624
15	    },
16	    "per_fold": {
17	      "0v1": [0.9838, 0.9819, 0.9839, 0.9822, 0.9870],
18	      "1v2": [0.8909, 0.8979, 0.8985, 0.9007, 0.8965],
19	      "2v3": [0.8104, 0.8060, 0.8185, 0.8047, 0.8103],
20	      "3v4": [0.7546, 0.7650, 0.7775, 0.7574, 0.7577]
21	    }
22	  },
23	  "jsd": {
24	    "0v1": 0.226339,
25	    "1v2": 0.104630,
26	    "2v3": 0.075186,
27	    "3v4": 0.065361
28	  },
29	  "bootstrap_ci": "INVALIDATED — bootstrap resampling broke GroupKFold structure, causing data leakage (+6.4pp inflation on 1v2). Use fold-based CI from pairwise_auc.per_fold instead.",
30	  "fold_ci_95": {
31	    "0v1": [0.9820, 0.9855],
32	    "1v2": [0.8937, 0.9001],
33	    "2v3": [0.8052, 0.8147],
34	    "3v4": [0.7543, 0.7706]
35	  }
36	}
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "8c16809e-bc62-40ca-9fa7-3a995bf223ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_chain/final_results.json",
      "content": "{\n  \"experiment\": \"exp_qwen_retrain_chain\",\n  \"model\": \"Qwen-1.5B\",\n  \"domain\": \"retrain-chain\",\n  \"status\": \"DONE\",\n  \"checked_at\": \"2026-05-18T22:30:00Z\",\n  \"ci_method\": \"5-fold CV\",\n  \"K_star\": 4,\n  \"pairwise_auc\": {\n    \"mean\": {\n      \"0v1\": 0.9838,\n      \"1v2\": 0.8969,\n      \"2v3\": 0.8100,\n      \"3v4\": 0.7624\n    },\n    \"per_fold\": {\n      \"0v1\": [0.9838, 0.9819, 0.9839, 0.9822, 0.9870],\n      \"1v2\": [0.8909, 0.8979, 0.8985, 0.9007, 0.8965],\n      \"2v3\": [0.8104, 0.8060, 0.8185, 0.8047, 0.8103],\n      \"3v4\": [0.7546, 0.7650, 0.7775, 0.7574, 0.7577]\n    }\n  },\n  \"jsd\": {\n    \"0v1\": 0.226339,\n    \"1v2\": 0.104630,\n    \"2v3\": 0.075186,\n    \"3v4\": 0.065361\n  },\n  \"bootstrap_ci\": \"INVALIDATED — bootstrap resampling broke GroupKFold structure, causing data leakage (+6.4pp inflation on 1v2). Use fold-based CI from pairwise_auc.per_fold instead.\",\n  \"fold_ci_95\": {\n    \"0v1\": [0.9820, 0.9855],\n    \"1v2\": [0.8937, 0.9001],\n    \"2v3\": [0.8052, 0.8147],\n    \"3v4\": [0.7543, 0.7706]\n  }\n}\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01AtFNYAvD1wwCTVDhn3UMTZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_depth7/retrain_depth7_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "e4f3cc12-7563-4e47-81d1-85e01309aaae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Q8YGpwhycRQTaxpbx4yTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13106
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

_source line 11 · 2026-05-19T02:55:11.751Z_

<details><summary>↩ Tool result · reported error · `toolu_01AtFNYAvD1wwCTVDhn3UMTZ`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination. Did you mean retrain_depth7_results.tex?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "f4efe425-8815-44a8-bcc1-be1e94057138",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination. Did you mean retrain_depth7_results.tex?"
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01NrffBPWw1EXoJZUcae4kz3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "5d6e1ad1-34cd-401d-819a-2eb7a92c78e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wvXXseXfAmxssSb8zDssd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 24947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1695
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

_source line 13 · 2026-05-19T02:55:14.836Z_

<details><summary>↩ Tool result · `toolu_01NrffBPWw1EXoJZUcae4kz3`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\eta^2_p$ is approximately 5$\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Retrain-chain validation yields $\Kempirical{=}7$ for Qwen2.5-1.5B LoRA (7 generations; Table~\ref{tab:retrain_ci}) and $\Kempirical{\geq}4$ for Pythia-1.4B LoRA (4 generations tested, all above $\theta$).
38	Retrain-chain extends detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$; cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	AUC decay accelerates across deeper pairs (6v7 $= 0.641$ vs.\ 5v6 $= 0.702$); extrapolating yields 7v8 $\approx 0.57 < \theta$, suggesting $\Kempirical{=}7$ is near the ceiling.
40	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
41	
42	\begin{table}[h]
43	\centering
44	\small
45	\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. \textbf{Qwen2.5-1.5B LoRA} (7 generations): $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\Kempirical{\geq}4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
46	\label{tab:retrain_ci}
47	\begin{tabular}{lcc}
48	\toprule
49	\textbf{Pair} & $\auc$ & \textbf{95\% CI} \\
50	\midrule
51	\multicolumn{3}{l}{\emph{Qwen2.5-1.5B LoRA ($\Kempirical{=}7$)}} \\
52	0v1 & 0.9837 & $[0.9821,\,0.9854]$ \\
53	1v2 & 0.8971 & $[0.8949,\,0.8993]$ \\
54	2v3 & 0.8098 & $[0.8052,\,0.8144]$ \\
55	3v4 & 0.7600 & $[0.7528,\,0.7672]$ \\
56	4v5 & 0.7459 & $[0.7379,\,0.7538]$ \\
57	5v6 & 0.7017 & $[0.6958,\,0.7076]$ \\
58	6v7 & 0.6410 & $[0.6376,\,0.6445]$ \\
59	\midrule
60	\multicolumn{3}{l}{\emph{Pythia-1.4B LoRA ($\Kempirical{\geq}4$)}} \\
61	0v1 & 0.9842 & $[0.9823,\,0.9860]$ \\
62	1v2 & 0.9471 & $[0.9432,\,0.9509]$ \\
63	2v3 & 0.8888 & $[0.8832,\,0.8943]$ \\
64	3v4 & 0.7994 & $[0.7920,\,0.8067]$ \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	\paragraph{CI methodology note.}
70	\label{sec:retrain_ci_note}
71	The main pipeline reports bootstrap 95\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.
72	In the retrain-chain setting, each generation's training corpus is the \emph{output} of the previous generation's fine-tuned model, creating inter-generation dependencies that standard bootstrap resampling cannot preserve without inflating AUC estimates.
73	We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
74	
75	\emph{Threshold sensitivity.}
76	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
77	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
78	
79	\begin{table}[h]
80	\centering
81	\small
82	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
83	\label{tab:theta_sensitivity}
84	\resizebox{\columnwidth}{!}{%
85	\begin{tabular}{llcccc}
86	\toprule
87	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
88	\midrule
89	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
90	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
91	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
92	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
93	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
94	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
95	\midrule
96	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
97	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
98	\midrule
99	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
100	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
101	\bottomrule
102	\end{tabular}}
103	\end{table}
104	
105	\begin{figure}[h]
106	\centering
107	\includegraphics[width=\columnwidth]{figures/fig_theta_sensitivity.pdf}
108	\caption{$\Kempirical$ as a function of $\theta$ across all model $\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\Kempirical{\leq}1$ $<$ C4 $\Kempirical{\leq}2$ $<$ arXiv $\Kempirical{\leq}3$) is preserved across the full $\theta \in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\Kempirical$.}
109	\label{fig:theta_sensitivity}
110	\end{figure}
111	
112	\emph{Structural confound: token length.}
113	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
114	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
115	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
116	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
117	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
118	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
119	
120	\emph{Graduated filtering.}
121	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
122	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
123	\label{tab:pairwise_significance}
124	
125	\subsection{Dose-Response: Contamination Ratio Effect}
126	\label{sec:dose_response}
127	
128	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
129	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
130	
131	\begin{table}[h]
132	\centering
133	\small
134	\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
135	\label{tab:dose_response}
136	\resizebox{\columnwidth}{!}{%
137	\begin{tabular}{lcccccc}
138	\toprule
139	& \multicolumn{2}{c}{\textbf{10\%}} & \multicolumn{2}{c}{\textbf{30\%}} & \multicolumn{2}{c}{\textbf{50\%}} \\
140	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
141	\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\
142	\midrule
143	No-filter   & $.6058{\pm}.0002$ & $.6689{\pm}.0006$ & $.6069{\pm}.0007$ & $.6664{\pm}.0018$ & $.6063{\pm}.0012$ & $.6680{\pm}.0005$ \\
144	Binary-ours & $\mathbf{.6079{\pm}.0004}$ & $\mathbf{.6727{\pm}.0007}$ & $\mathbf{.6082{\pm}.0011}$ & $\mathbf{.6725{\pm}.0006}$ & $\mathbf{.6088{\pm}.0009}$ & $\mathbf{.6731{\pm}.0004}$ \\
145	Graduated   & $.6066{\pm}.0010$ & $.6700{\pm}.0014$ & $.6072{\pm}.0008$ & $.6665{\pm}.0012$ & $.6062{\pm}.0008$ & $.6679{\pm}.0001$ \\
146	\bottomrule
147	\end{tabular}}
148	\end{table}
149	
150	At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.
151	Binary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).
152	MMLU differences are smaller and significant only at 10\% after correction ($p = 0.001$).
153	Graduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \geq 0.27$; HellaSwag $p \geq 0.06$), confirming that depth assignments beyond $\Kempirical$ inject noise regardless of contamination severity.
154	Effect sizes diminish 3--6$\times$ relative to the 100\% setting (Section~\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\approx$ no-filter) is preserved.
155	
156	\subsection{Cross-Model Filtering Replication}
157	\label{sec:pythia_filtering}
158	
159	To test whether $\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\ref{tab:pythia_filtering}).
160	
161	\begin{table}[h]
162	\centering
163	\small
164	\caption{Pythia-1.4B filtering replication (3 seeds, mean $\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}
165	\label{tab:pythia_filtering}
166	\begin{tabular}{lcc}
167	\toprule
168	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
169	\midrule
170	No-filter & $.2568{\pm}.0012$ & $.5250{\pm}.0008$ \\
171	Binary-ours & $\mathbf{.2585{\pm}.0004}$ & $.5251{\pm}.0001$ \\
172	Graduated$_{0.9}$ & $.2561{\pm}.0009$ & $\mathbf{.5253{\pm}.0007}$ \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
178	The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
179	HellaSwag differences are negligible across all strategies.
180	
181	\subsection{Feature Subset Stability}
182	\label{sec:feature_subset}
183	
184	To test whether $\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\ref{tab:feature_subset}).
185	
186	\begin{table}[h]
187	\centering
188	\small
189	\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
190	\label{tab:feature_subset}
191	\begin{tabular}{lcccc}
192	\toprule
193	\textbf{Subset} & \textbf{Tested} & \textbf{Pass} & \textbf{Min $\auc$} & \textbf{Mean $\auc$} \\
194	\midrule
195	15D (full) & 1 & 1 & 0.6262 & 0.6262 \\
196	10D        & 5 & 5 & 0.6153 & 0.6191 \\
197	8D         & 5 & 5 & 0.6056 & 0.6159 \\
198	5D         & 5 & 2 & 0.5856 & 0.5998 \\
199	3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\
200	\bottomrule
201	\end{tabular}
202	\end{table}
203	
204	$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
205	The boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.
206	
207	\subsection{self\_BLEU Feature Independence}
208	\label{sec:selfbleu_ablation}
209	
210	To verify that $\Kempirical$ does not depend on the self\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\_BLEU removed) classifiers across four model configurations (Table~\ref{tab:selfbleu_ablation}).
211	
212	\begin{table}[h]
213	\centering
214	\small
215	\caption{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).}
216	\label{tab:selfbleu_ablation}
217	\resizebox{\columnwidth}{!}{%
218	\begin{tabular}{lcccc}
219	\toprule
220	\textbf{Model} & $\Kempirical$ & \textbf{15D $\auc$ [CI]} & \textbf{14D $\auc$ [CI]} & $\Delta$ \\
221	\midrule
222	Qwen-base   & 2/2 & $.6288$ $[.620,\,.638]$ & $.6258$ $[.616,\,.635]$ & $-.0031$ \\
223	Pythia-1.4B  & 2/2 & $.8840$ $[.878,\,.890]$ & $.8830$ $[.876,\,.889]$ & $-.0010$ \\
224	LLaMA-8B     & 2/2 & $.6075$ $[.598,\,.617]$ & $.6074$ $[.598,\,.617]$ & $-.0001$ \\
225	Mistral-7B   & 1/1 & $.5902$ $[.580,\,.600]$ & $.5903$ $[.580,\,.600]$ & $+.0002$ \\
226	\bottomrule
227	\end{tabular}}
228	\end{table}
229	
230	All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
231	The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
232	
233	\subsection{Wikipedia Domain: Scorer Confound Resolution}
234	\label{sec:wiki_domain}
235	
236	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
237	A scorer confound ablation resolves this apparent split.
238	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
239	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
240	
241	\begin{table}[h]
242	\centering
243	\small
244	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
245	\label{tab:wiki_domain}
246	\resizebox{\columnwidth}{!}{%
247	\begin{tabular}{llccccc}
248	\toprule
249	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
250	\midrule
251	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
252	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
253	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
254	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
255	\midrule
256	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
257	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
258	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
259	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
260	\bottomrule
261	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
262	\end{tabular}}
263	\end{table}
264	
265	\paragraph{Per-fold transparency.}
266	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
267	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
268	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
269	
270	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
271	\label{sec:arxiv_crossscorer_ci}
272	
273	\begin{table}[h]
274	\centering
275	\small
276	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
277	\label{tab:arxiv_crossscorer_ci}
278	\resizebox{\columnwidth}{!}{%
279	\begin{tabular}{lccc}
280	\toprule
281	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
282	\midrule
283	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
284	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
285	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
286	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
287	\bottomrule
288	\end{tabular}}
289	\end{table}
290	
291	\subsection{JSD Decay Analysis}
292	\label{sec:jsd_extended}
293	
294	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
295	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
296	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
297	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
298	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\lambda \approx 1.0$.
299	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
300	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
301	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\Kempirical{=}3$.
302	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs (Figure~\ref{fig:retrain_decay}).
303	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
304	
305	\begin{figure}[h]
306	\centering
307	\includegraphics[width=\columnwidth]{figures/fig_retrain_decay.png}
308	\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
309	\label{fig:retrain_decay}
310	\end{figure}
311	
312	\subsection{Boundary Cases and Scale Effect}
313	\label{sec:boundary_extended}
314	
315	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
316	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain lexical diversity can rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
317	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
318	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.
319	
320	\paragraph{Sample-size control.}
321	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
322	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, confirming that arXiv's $\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.
323	
324	\subsection{LaTeX Markup Ablation (arXiv)}
325	\label{sec:latex_ablation}
326	
327	To disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\ref{tab:latex_ablation}).
328	
329	\begin{table}[h]
330	\centering
331	\small
332	\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), indicating that deeper generations produce proportionally more formatting tokens.}
333	\label{tab:latex_ablation}
334	\resizebox{\columnwidth}{!}{%
335	\begin{tabular}{lccr}
336	\toprule
337	\textbf{Pair} & \textbf{Original} & \textbf{Stripped} & $\Delta$ \\
338	\midrule
339	0v1 & 0.9946 & 0.9948 & $+$0.0002 \\
340	1v2 & 0.8580 & 0.8297 & $-$0.028 \\
341	2v3 & 0.6427 $[0.628,\,0.658]$ & 0.6248 $[0.610,\,0.640]$ & $-$0.018 \\
342	3v4 & 0.5437 & 0.5468 & $+$0.003 \\
343	\midrule
344	$\Kempirical$ & 3 & 3 & --- \\
345	\bottomrule
346	\end{tabular}}
347	\end{table}
348	
349	Content-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\sim}$1.8\,pp at the boundary pair).
350	The depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\%, depth 5: $-$4.6\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.
351	
352	\subsection{Statistical Power Analysis}
353	\label{sec:power_curve}
354	
355	To characterize the minimum sample size required for reliable $\Kempirical$ determination, we subsample C4 at $n \in \{500, 1000, 2000, 3000, 4000, 5000\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\ref{tab:power_curve}, Figure~\ref{fig:power_curve}).
356	
357	\begin{table}[h]
358	\centering
359	\small
360	\caption{Subsampling power analysis for $\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\auc > \theta{=}0.60$.}
361	\label{tab:power_curve}
362	\begin{tabular}{rccc}
363	\toprule
364	$n$ & \textbf{Mean 1v2 $\auc$} & \textbf{Std} & \textbf{Detection Prob.} \\
365	\midrule
366	500 & 0.581 & 0.018 & 20\% \\
367	1{,}000 & 0.591 & 0.014 & 30\% \\
368	2{,}000 & 0.610 & 0.009 & 100\% \\
369	3{,}000 & 0.617 & 0.005 & 100\% \\
370	4{,}000 & 0.622 & 0.004 & 100\% \\
371	5{,}000 & 0.629 & 0.000 & 100\% \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\begin{figure}[h]
377	\centering
378	\includegraphics[width=\columnwidth]{figures/fig_power_curve.png}
379	\caption{$\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\% at $n{=}2{,}000$; the 80\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\pm$1 std over 10 resamples. The dashed red line marks $\theta{=}0.60$.}
380	\label{fig:power_curve}
381	\end{figure}
382	
383	Detection rate jumps from 20\% ($n{=}500$) to 100\% ($n{=}2{,}000$), with the 80\% power threshold crossed near $n{=}1{,}500$.
384	At $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, confirming that our results are well above the minimum required for reliable boundary estimation.
385	The sharp transition reflects the proximity of the 1v2 AUC to $\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.
386	
387	\subsection{Feature Group Ablation}
388	\label{sec:feature_ablation}
389	
390	To assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\ref{sec:method}) on the 1\,vs.\,2 task using (a) each feature group alone (\emph{single}) and (b) the full 15D set minus one group (\emph{leave-one-out}).
391	Representative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).
392	
393	\begin{figure}[h]
394	\centering
395	\includegraphics[width=\columnwidth]{figures/fig_feature_ablation.pdf}
396	\caption{Feature group ablation heatmap for 1\,vs.\,2 classification AUC. \emph{Left}: single-group performance. \emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}
397	\label{fig:feature_ablation}
398	\end{figure}
399	
400	\begin{table}[h]
401	\centering
402	\small
403	\caption{Feature group ablation for 1\,vs.\,2 classification (AUC). \textbf{Single}: using only features from one group. \textbf{Leave-one-out}: removing one group from the full 15D feature set. $\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\ref{tab:kstar_ci}.}
404	\label{tab:feature_ablation}
405	\resizebox{\columnwidth}{!}{%
406	\begin{tabular}{l ccc ccc}
407	\toprule
408	& \multicolumn{3}{c}{\textbf{Single Group}} & \multicolumn{3}{c}{\textbf{Leave-One-Out ($\Delta$)}} \\
409	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
410	Feature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\
411	\midrule
412	Surprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\
413	Surprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\
414	Lexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\
415	Freq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\
416	\midrule
417	Full (15D) & 0.609 & 0.860 & 0.619 & \multicolumn{3}{c}{---} \\
418	\bottomrule
419	\end{tabular}}
420	\end{table}
421	
422	Surprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.
423	On C4 and Wikipedia, all LOO drops are small ($\leq 0.007$, within cross-fold standard deviation), indicating that no single feature group is individually critical for the weaker low-$\Kempirical$ signal.
424	Removing surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\Kempirical$ domains.
425	
426	\subsection{Classifier Choice: McNemar Test}
427	\label{sec:mcnemar_baselines}
428	
429	To verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\ref{tab:mcnemar_obd_baselines}).
430	Of 36 comparisons, 31 are non-significant ($p \geq 0.05$), and all five significant results concentrate in two model $\times$ domain conditions.
431	For LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.
432	For Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).
433	
434	\begin{table*}[h]
435	\centering
436	\small
437	\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}
438	\label{tab:mcnemar_obd_baselines}
439	\resizebox{\textwidth}{!}{%
440	\begin{tabular}{llcccc}
441	\toprule
442	\textbf{Model} & \textbf{Domain} & \textbf{OBD Acc.} & \textbf{vs.\ LogReg} & \textbf{vs.\ LinearSVC} & \textbf{vs.\ RandomForest} \\
443	\midrule
444	Qwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\
445	Pythia-1.4B     & C4    & .631 & $\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\
446	LLaMA-8B        & C4    & .573 & $\mathbf{6.2{\times}10^{-5\,***}}$ (.592) & $\mathbf{1.1{\times}10^{-4\,***}}$ (.591) & $\mathbf{.001^{**}}$ (.586) \\
447	\midrule
448	Qwen-1.5B      & Wiki  & .588 & $\mathbf{9.4{\times}10^{-4\,***}}$ (.570) & $\mathbf{2.3{\times}10^{-4\,***}}$ (.568) & .655 (.590) \\
449	Pythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\
450	OLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\
451	LLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\
452	\midrule
453	Qwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\
454	Pythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\
455	OLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\
456	Qwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\
457	Mistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\
458	\bottomrule
459	\end{tabular}%
460	}
461	
462	\vspace{4pt}
463	\footnotesize
464	36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.
465	The predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.
466	\end{table*}
467	
468	\subsection{Domain Lexical Statistics}
469	\label{sec:domain_lexical_stats}
470	
471	Table~\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.
472	The TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\ Wikipedia).
473	Vocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).
474	This reversal likely reflects C4's greater content heterogeneity (higher variance: $\sigma = 0.706$ vs.\ $0.284$), which inflates TTR but depresses mean entropy.
475	As depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\Kempirical$ and slower convergence to the stationary distribution.
476	
477	\begin{table*}[h]
478	\centering
479	\small
480	\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.
481	At depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\,=\,0.755, $H$\,=\,6.853),
482	followed by C4 and Wikipedia.
483	As depth increases, all domains converge, with arXiv showing the steepest decline.
484	Cohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}
485	\label{tab:domain-ttr-entropy}
486	\begin{tabular}{ll rrr rrr}
487	\toprule
488	& & \multicolumn{3}{c}{\textbf{TTR}} & \multicolumn{3}{c}{\textbf{Vocab Entropy ($H$)}} \\
489	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
490	\textbf{Depth} & $N$ & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} \\
491	\midrule
492	0 & 5k/5k/2.2k & .665\tpm.061 & .720\tpm.105 & \textbf{.755}\tpm.055 & 6.408\tpm.284 & 6.225\tpm.706 & \textbf{6.853}\tpm.295 \\
493	1 &             & .655\tpm.121 & .707\tpm.149 & \textbf{.732}\tpm.098 & 5.932\tpm.843 & 5.737\tpm1.189 & \textbf{6.113}\tpm.655 \\
494	2 &             & .647\tpm.145 & .676\tpm.159 & \textbf{.677}\tpm.131 & 5.784\tpm.905 & 5.774\tpm1.139 & \textbf{5.998}\tpm.967 \\
495	3 &             & .645\tpm.159 & \textbf{.662}\tpm.164 & .635\tpm.134 & 5.664\tpm1.085 & 5.743\tpm1.161 & \textbf{5.964}\tpm.933 \\
496	4 &             & .636\tpm.164 & \textbf{.647}\tpm.169 & .621\tpm.140 & 5.660\tpm1.062 & 5.758\tpm1.167 & \textbf{5.898}\tpm.942 \\
497	5 &             & .632\tpm.172 & \textbf{.636}\tpm.175 & .618\tpm.150 & 5.593\tpm1.130 & 5.772\tpm1.141 & \textbf{5.816}\tpm.968 \\
498	\midrule
499	\multicolumn{8}{l}{\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\
500	\multicolumn{2}{l}{C4 vs.\ Wiki}   & \multicolumn{3}{c}{$d = +0.65$} & \multicolumn{3}{c}{$d = -0.34$} \\
501	\multicolumn{2}{l}{arXiv vs.\ C4}  & \multicolumn{3}{c}{$d = +0.37$} & \multicolumn{3}{c}{$d = +1.03$} \\
502	\multicolumn{2}{l}{arXiv vs.\ Wiki} & \multicolumn{3}{c}{$d = +1.52$} & \multicolumn{3}{c}{$d = +1.55$} \\
503	\bottomrule
504	\end{tabular}
505	\end{table*}
506	
507	\subsection{Leave-One-Family-Out Threshold Validation}
508	\label{sec:theta_lofo}
509	
510	To validate $\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, then predicts $\Kempirical$ for the held-out models.
511	Table~\ref{tab:theta_lofo} reports results across all three domains.
512	
513	On C4, 8/9 held-out predictions agree with the original $\Kempirical$ assignment at $\theta{=}0.60$ (agreement: 89\%).
514	The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the sole rewrite-mode model, making the discrepancy attributable to mode rather than threshold instability.
515	The derived $\hat{\theta}$ values span $[0.5725, 0.6004]$, and $\theta{=}0.60$ falls within this range.
516	
517	ArXiv corroborates with 6/6 agreement (100\%), though the wide $\hat{\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.
518	
519	Wikipedia yields only 1/6 agreement (17\%).
520	This failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ is narrow or inverted, invalidating the gap-based threshold derivation.
521	Wikipedia's $\Kempirical{=}1$ assignment is independently confirmed by the global $\theta{=}0.60$ criterion (Section~\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.
522	
523	\begin{table*}[t]
524	\centering
525	\small
526	\caption{Leave-One-Family-Out (LOFO) cross-validation of $\theta$ across three domains. Each fold holds out one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\text{AUC}_{1\text{v}2})$ and $\max(\text{AUC}_{2\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\%). arXiv: 6/6 (100\%). Wikipedia: 1/6 (17\%, see text).}
527	\label{tab:theta_lofo}
528	\begin{tabular}{l l l c c c c c c}
529	\toprule
530	Domain & Held-out & Model & $\text{AUC}_{1\text{v}2}$ & $\text{AUC}_{2\text{v}3}$ & $\hat{\theta}$ & $K^*_{\hat{\theta}}$ & $K^*_{0.60}$ & Match \\
531	\midrule
532	C4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \cmark \\
533	 & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \cmark \\
534	 & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \xmark \\
535	 &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \cmark \\
536	 &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \cmark \\
537	 &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \cmark \\
538	 &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \cmark \\
539	 & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \cmark \\
540	 & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \cmark \\
541	\cmidrule{2-9}
542	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5725, 0.6004], agreement: 8/9 (89\%)} \\
543	\midrule
544	arXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \cmark \\
545	 & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \cmark \\
546	 & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \cmark \\
547	 &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \cmark \\
548	 & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \cmark \\
549	 & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \cmark \\
550	\cmidrule{2-9}
551	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5735, 0.7296], agreement: 6/6 (100\%)} \\
552	\midrule
553	Wikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \xmark \\
554	 & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \cmark \\
555	 & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \xmark \\
556	 &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \xmark \\
557	 & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \xmark \\
558	 & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \xmark \\
559	\cmidrule{2-9}
560	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5215, 0.5557], agreement: 1/6 (17\%)} \\
561	\bottomrule
562	\end{tabular}
563	\end{table*}
564	
565	\subsection{Code Domain Results}
566	\label{sec:code_domain}
567	
568	\begin{table}[h]
569	\centering
570	\small
571	\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
572	\label{tab:code_domain_qwen}
573	\begin{tabular}{l c c c}
574	\toprule
575	Pair & AUC & 95\% CI & JSD \\
576	\midrule
577	0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\
578	1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\
579	2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\
580	3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\
581	4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\
582	\midrule
583	\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
584	\bottomrule
585	\end{tabular}
586	\end{table}
587	
588	\subsection{Borderline Feature Analysis}
589	\label{sec:borderline_analysis}
590	
591	To understand why Mistral-7B yields $\Kempirical{=}1$ while other C4 models yield $\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).
592	
593	Mistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\ 2.90--3.02 for other models), indicating that the scorer model already finds Mistral's output highly predictable.
594	This compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\bar{|d|} = 0.112$; Table~\ref{tab:cohens_d_full}), and no single feature exceeds 13\% of total classifier importance.
595	The borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.
596	
597	Greedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.
598	
599	\begin{table*}[h]
600	\centering
601	\small
602	\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\ = normalized LightGBM gain importance (\%). $\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\Delta\text{surp}_{1\to2}$: change in mean surprisal from depth 1 to depth 2.}
603	\label{tab:borderline_features}
604	\begin{tabular}{@{}llc lcc@{}}
605	\toprule
606	Category & Model & AUC & Top-3 Features (Imp.\%) & $\bar{|d|}$ & $\Delta\text{surp}_{1\to2}$ \\
607	\midrule
608	Strong & Pythia-greedy & 0.884 & hapax\_ratio (47), surp\_mean (11), low\_freq\_ratio (8) & 0.365 & $-$0.160 \\
609	Strong & Pythia-nuc09 & 0.677 & surp\_std (20), freq\_entropy (11), surp\_d1\_std (8) & 0.170 & $-$0.196 \\
610	Strong & Qwen-1.5B-base & 0.626 & surp\_std (13), freq\_entropy (10), surp\_mean (9) & 0.125 & $-$0.159 \\
611	\midrule
612	Borderline & Pythia-$T{=}1.2$ & 0.617 & surp\_std (15), freq\_entropy (10), surp\_kurt (8) & 0.112 & $-$0.059 \\
613	Borderline & LLaMA-3.1-8B & 0.612 & surp\_std (12), surp\_d1\_std (10), freq\_entropy (9) & 0.137 & $-$0.215 \\
614	\midrule
615	Below $\theta$ & Mistral-7B & 0.594 & surp\_std (13), freq\_entropy (9), surp\_d1\_skew (9) & 0.112 & $-$0.086 \\
616	\bottomrule
617	\end{tabular}
618	\end{table*}
619	
620	\begin{table*}[h]
621	\centering
622	\scriptsize
623	\caption{Cohen's $d$ (depth-1 vs.\ depth-2) for all 15 features across six C4 models. \textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\_ratio, low\_freq\_ratio); under sampling, surprisal variability features (surp\_std, surp\_d1\_std, surp\_d2\_std) carry the dominant signal.}
624	\label{tab:cohens_d_full}
625	\begin{tabular}{@{}lrrrrrr@{}}
626	\toprule
627	Feature & \rotatebox{60}{Pythia-greedy} & \rotatebox{60}{Pythia-nuc09} & \rotatebox{60}{Qwen-1.5B-base} & \rotatebox{60}{Pythia-$T{=}1.2$} & \rotatebox{60}{LLaMA-3.1-8B} & \rotatebox{60}{Mistral-7B} \\
628	\midrule
629	surp\_mean & \textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\
630	surp\_std & $-$0.301 & \textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\
631	surp\_skew & \textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\
632	surp\_kurt & \textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\
633	surp\_d1\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \textbf{$+$0.080} & $+$0.026 \\
634	surp\_d1\_std & $-$0.318 & \textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\
635	surp\_d1\_skew & \textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\
636	surp\_d2\_mean & $+$0.004 & $+$0.001 & \textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\
637	surp\_d2\_std & $-$0.312 & \textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\
638	ttr & \textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\
639	hapax\_ratio & \textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\
640	self\_bleu & $-$0.056 & $+$0.031 & \textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\
641	freq\_kurtosis & $+$0.071 & \textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\
642	freq\_entropy & \textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\
643	low\_freq\_ratio & \textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\
644	\midrule
645	$\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\
646	\bottomrule
647	\end{tabular}
648	\end{table*}
649	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "90463a07-0745-4d78-bc47-d8f34d40980e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\\eta^2_p$ is approximately 5$\\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nRetrain-chain validation yields $\\Kempirical{=}7$ for Qwen2.5-1.5B LoRA (7 generations; Table~\\ref{tab:retrain_ci}) and $\\Kempirical{\\geq}4$ for Pythia-1.4B LoRA (4 generations tested, all above $\\theta$).\nRetrain-chain extends detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$; cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nAUC decay accelerates across deeper pairs (6v7 $= 0.641$ vs.\\ 5v6 $= 0.702$); extrapolating yields 7v8 $\\approx 0.57 < \\theta$, suggesting $\\Kempirical{=}7$ is near the ceiling.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. \\textbf{Qwen2.5-1.5B LoRA} (7 generations): $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\\Kempirical{\\geq}4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Pair} & $\\auc$ & \\textbf{95\\% CI} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Qwen2.5-1.5B LoRA ($\\Kempirical{=}7$)}} \\\\\n0v1 & 0.9837 & $[0.9821,\\,0.9854]$ \\\\\n1v2 & 0.8971 & $[0.8949,\\,0.8993]$ \\\\\n2v3 & 0.8098 & $[0.8052,\\,0.8144]$ \\\\\n3v4 & 0.7600 & $[0.7528,\\,0.7672]$ \\\\\n4v5 & 0.7459 & $[0.7379,\\,0.7538]$ \\\\\n5v6 & 0.7017 & $[0.6958,\\,0.7076]$ \\\\\n6v7 & 0.6410 & $[0.6376,\\,0.6445]$ \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{Pythia-1.4B LoRA ($\\Kempirical{\\geq}4$)}} \\\\\n0v1 & 0.9842 & $[0.9823,\\,0.9860]$ \\\\\n1v2 & 0.9471 & $[0.9432,\\,0.9509]$ \\\\\n2v3 & 0.8888 & $[0.8832,\\,0.8943]$ \\\\\n3v4 & 0.7994 & $[0.7920,\\,0.8067]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CI methodology note.}\n\\label{sec:retrain_ci_note}\nThe main pipeline reports bootstrap 95\\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.\nIn the retrain-chain setting, each generation's training corpus is the \\emph{output} of the previous generation's fine-tuned model, creating inter-generation dependencies that standard bootstrap resampling cannot preserve without inflating AUC estimates.\nWe therefore report fold-based 95\\% CIs for retrain-chain experiments, computed as $\\bar{x} \\pm 1.96 \\cdot s / \\sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\\Kempirical$.}\n\\label{fig:theta_sensitivity}\n\\end{figure}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), confirming that depth assignments beyond $\\Kempirical$ inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain lexical diversity can rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, confirming that arXiv's $\\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), indicating that deeper generations produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\\n3v4 & 0.5437 & 0.5468 & $+$0.003 \\\\\n\\midrule\n$\\Kempirical$ & 3 & 3 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nContent-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\\sim}$1.8\\,pp at the boundary pair).\nThe depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\\%, depth 5: $-$4.6\\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.\n\n\\subsection{Statistical Power Analysis}\n\\label{sec:power_curve}\n\nTo characterize the minimum sample size required for reliable $\\Kempirical$ determination, we subsample C4 at $n \\in \\{500, 1000, 2000, 3000, 4000, 5000\\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\\ref{tab:power_curve}, Figure~\\ref{fig:power_curve}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\n\\label{tab:power_curve}\n\\begin{tabular}{rccc}\n\\toprule\n$n$ & \\textbf{Mean 1v2 $\\auc$} & \\textbf{Std} & \\textbf{Detection Prob.} \\\\\n\\midrule\n500 & 0.581 & 0.018 & 20\\% \\\\\n1{,}000 & 0.591 & 0.014 & 30\\% \\\\\n2{,}000 & 0.610 & 0.009 & 100\\% \\\\\n3{,}000 & 0.617 & 0.005 & 100\\% \\\\\n4{,}000 & 0.622 & 0.004 & 100\\% \\\\\n5{,}000 & 0.629 & 0.000 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_power_curve.png}\n\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\n\\label{fig:power_curve}\n\\end{figure}\n\nDetection rate jumps from 20\\% ($n{=}500$) to 100\\% ($n{=}2{,}000$), with the 80\\% power threshold crossed near $n{=}1{,}500$.\nAt $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, confirming that our results are well above the minimum required for reliable boundary estimation.\nThe sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\n\n\\subsection{Feature Group Ablation}\n\\label{sec:feature_ablation}\n\nTo assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\\ref{sec:method}) on the 1\\,vs.\\,2 task using (a) each feature group alone (\\emph{single}) and (b) the full 15D set minus one group (\\emph{leave-one-out}).\nRepresentative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_ablation.pdf}\n\\caption{Feature group ablation heatmap for 1\\,vs.\\,2 classification AUC. \\emph{Left}: single-group performance. \\emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}\n\\label{fig:feature_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation for 1\\,vs.\\,2 classification (AUC). \\textbf{Single}: using only features from one group. \\textbf{Leave-one-out}: removing one group from the full 15D feature set. $\\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\\ref{tab:kstar_ci}.}\n\\label{tab:feature_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Single Group}} & \\multicolumn{3}{c}{\\textbf{Leave-One-Out ($\\Delta$)}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nFeature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\\\\n\\midrule\nSurprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\nSurprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\\\\nLexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\nFreq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\n\\midrule\nFull (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSurprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.\nOn C4 and Wikipedia, all LOO drops are small ($\\leq 0.007$, within cross-fold standard deviation), indicating that no single feature group is individually critical for the weaker low-$\\Kempirical$ signal.\nRemoving surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\\Kempirical$ domains.\n\n\\subsection{Classifier Choice: McNemar Test}\n\\label{sec:mcnemar_baselines}\n\nTo verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\\ref{tab:mcnemar_obd_baselines}).\nOf 36 comparisons, 31 are non-significant ($p \\geq 0.05$), and all five significant results concentrate in two model $\\times$ domain conditions.\nFor LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \\leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.\nFor Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \\textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}\n\\label{tab:mcnemar_obd_baselines}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{OBD Acc.} & \\textbf{vs.\\ LogReg} & \\textbf{vs.\\ LinearSVC} & \\textbf{vs.\\ RandomForest} \\\\\n\\midrule\nQwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\\\\nPythia-1.4B     & C4    & .631 & $\\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\\\\nLLaMA-8B        & C4    & .573 & $\\mathbf{6.2{\\times}10^{-5\\,***}}$ (.592) & $\\mathbf{1.1{\\times}10^{-4\\,***}}$ (.591) & $\\mathbf{.001^{**}}$ (.586) \\\\\n\\midrule\nQwen-1.5B      & Wiki  & .588 & $\\mathbf{9.4{\\times}10^{-4\\,***}}$ (.570) & $\\mathbf{2.3{\\times}10^{-4\\,***}}$ (.568) & .655 (.590) \\\\\nPythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\\\\nOLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\\\\nLLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\\\\n\\midrule\nQwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\\\\nPythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\\\\nOLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\\\\nQwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\\\\nMistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\n\\vspace{4pt}\n\\footnotesize\n36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.\nThe predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.\n\\end{table*}\n\n\\subsection{Domain Lexical Statistics}\n\\label{sec:domain_lexical_stats}\n\nTable~\\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.\nThe TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\\ Wikipedia).\nVocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).\nThis reversal likely reflects C4's greater content heterogeneity (higher variance: $\\sigma = 0.706$ vs.\\ $0.284$), which inflates TTR but depresses mean entropy.\nAs depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\\Kempirical$ and slower convergence to the stationary distribution.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.\nAt depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\\,=\\,0.755, $H$\\,=\\,6.853),\nfollowed by C4 and Wikipedia.\nAs depth increases, all domains converge, with arXiv showing the steepest decline.\nCohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}\n\\label{tab:domain-ttr-entropy}\n\\begin{tabular}{ll rrr rrr}\n\\toprule\n& & \\multicolumn{3}{c}{\\textbf{TTR}} & \\multicolumn{3}{c}{\\textbf{Vocab Entropy ($H$)}} \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Depth} & $N$ & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} \\\\\n\\midrule\n0 & 5k/5k/2.2k & .665\\tpm.061 & .720\\tpm.105 & \\textbf{.755}\\tpm.055 & 6.408\\tpm.284 & 6.225\\tpm.706 & \\textbf{6.853}\\tpm.295 \\\\\n1 &             & .655\\tpm.121 & .707\\tpm.149 & \\textbf{.732}\\tpm.098 & 5.932\\tpm.843 & 5.737\\tpm1.189 & \\textbf{6.113}\\tpm.655 \\\\\n2 &             & .647\\tpm.145 & .676\\tpm.159 & \\textbf{.677}\\tpm.131 & 5.784\\tpm.905 & 5.774\\tpm1.139 & \\textbf{5.998}\\tpm.967 \\\\\n3 &             & .645\\tpm.159 & \\textbf{.662}\\tpm.164 & .635\\tpm.134 & 5.664\\tpm1.085 & 5.743\\tpm1.161 & \\textbf{5.964}\\tpm.933 \\\\\n4 &             & .636\\tpm.164 & \\textbf{.647}\\tpm.169 & .621\\tpm.140 & 5.660\\tpm1.062 & 5.758\\tpm1.167 & \\textbf{5.898}\\tpm.942 \\\\\n5 &             & .632\\tpm.172 & \\textbf{.636}\\tpm.175 & .618\\tpm.150 & 5.593\\tpm1.130 & 5.772\\tpm1.141 & \\textbf{5.816}\\tpm.968 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\\\\n\\multicolumn{2}{l}{C4 vs.\\ Wiki}   & \\multicolumn{3}{c}{$d = +0.65$} & \\multicolumn{3}{c}{$d = -0.34$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ C4}  & \\multicolumn{3}{c}{$d = +0.37$} & \\multicolumn{3}{c}{$d = +1.03$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ Wiki} & \\multicolumn{3}{c}{$d = +1.52$} & \\multicolumn{3}{c}{$d = +1.55$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Leave-One-Family-Out Threshold Validation}\n\\label{sec:theta_lofo}\n\nTo validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\nTable~\\ref{tab:theta_lofo} reports results across all three domains.\n\nOn C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\nThe single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, making the discrepancy attributable to mode rather than threshold instability.\nThe derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\n\nArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\n\nWikipedia yields only 1/6 agreement (17\\%).\nThis failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ is narrow or inverted, invalidating the gap-based threshold derivation.\nWikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\n\\label{tab:theta_lofo}\n\\begin{tabular}{l l l c c c c c c}\n\\toprule\nDomain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\n\\midrule\nC4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\n\\midrule\narXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \\cmark \\\\\n &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\n\\midrule\nWikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \\xmark \\\\\n & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \\xmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \\xmark \\\\\n & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \\xmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Code Domain Results}\n\\label{sec:code_domain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\n\\label{tab:code_domain_qwen}\n\\begin{tabular}{l c c c}\n\\toprule\nPair & AUC & 95\\% CI & JSD \\\\\n\\midrule\n0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\\\\n1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\\\\n2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\\\\n3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\\\\n4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\\\\n\\midrule\n\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}\n\\label{sec:borderline_analysis}\n\nTo understand why Mistral-7B yields $\\Kempirical{=}1$ while other C4 models yield $\\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).\n\nMistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\\ 2.90--3.02 for other models), indicating that the scorer model already finds Mistral's output highly predictable.\nThis compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\\bar{|d|} = 0.112$; Table~\\ref{tab:cohens_d_full}), and no single feature exceeds 13\\% of total classifier importance.\nThe borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.\n\nGreedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\\ = normalized LightGBM gain importance (\\%). $\\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\\Delta\\text{surp}_{1\\to2}$: change in mean surprisal from depth 1 to depth 2.}\n\\label{tab:borderline_features}\n\\begin{tabular}{@{}llc lcc@{}}\n\\toprule\nCategory & Model & AUC & Top-3 Features (Imp.\\%) & $\\bar{|d|}$ & $\\Delta\\text{surp}_{1\\to2}$ \\\\\n\\midrule\nStrong & Pythia-greedy & 0.884 & hapax\\_ratio (47), surp\\_mean (11), low\\_freq\\_ratio (8) & 0.365 & $-$0.160 \\\\\nStrong & Pythia-nuc09 & 0.677 & surp\\_std (20), freq\\_entropy (11), surp\\_d1\\_std (8) & 0.170 & $-$0.196 \\\\\nStrong & Qwen-1.5B-base & 0.626 & surp\\_std (13), freq\\_entropy (10), surp\\_mean (9) & 0.125 & $-$0.159 \\\\\n\\midrule\nBorderline & Pythia-$T{=}1.2$ & 0.617 & surp\\_std (15), freq\\_entropy (10), surp\\_kurt (8) & 0.112 & $-$0.059 \\\\\nBorderline & LLaMA-3.1-8B & 0.612 & surp\\_std (12), surp\\_d1\\_std (10), freq\\_entropy (9) & 0.137 & $-$0.215 \\\\\n\\midrule\nBelow $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[h]\n\\centering\n\\scriptsize\n\\caption{Cohen's $d$ (depth-1 vs.\\ depth-2) for all 15 features across six C4 models. \\textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\\_ratio, low\\_freq\\_ratio); under sampling, surprisal variability features (surp\\_std, surp\\_d1\\_std, surp\\_d2\\_std) carry the dominant signal.}\n\\label{tab:cohens_d_full}\n\\begin{tabular}{@{}lrrrrrr@{}}\n\\toprule\nFeature & \\rotatebox{60}{Pythia-greedy} & \\rotatebox{60}{Pythia-nuc09} & \\rotatebox{60}{Qwen-1.5B-base} & \\rotatebox{60}{Pythia-$T{=}1.2$} & \\rotatebox{60}{LLaMA-3.1-8B} & \\rotatebox{60}{Mistral-7B} \\\\\n\\midrule\nsurp\\_mean & \\textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\\\\nsurp\\_std & $-$0.301 & \\textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\\\\nsurp\\_skew & \\textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\\\\nsurp\\_kurt & \\textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\\\\nsurp\\_d1\\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \\textbf{$+$0.080} & $+$0.026 \\\\\nsurp\\_d1\\_std & $-$0.318 & \\textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\\\\nsurp\\_d1\\_skew & \\textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\\\\nsurp\\_d2\\_mean & $+$0.004 & $+$0.001 & \\textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\\\\nsurp\\_d2\\_std & $-$0.312 & \\textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\\\\nttr & \\textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\\\\nhapax\\_ratio & \\textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\\\\nself\\_bleu & $-$0.056 & $+$0.031 & \\textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\\\\nfreq\\_kurtosis & $+$0.071 & \\textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\\\\nfreq\\_entropy & \\textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\\\\nlow\\_freq\\_ratio & \\textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\\\\n\\midrule\n$\\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 649,
      "startLine": 1,
      "totalLines": 649
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01WWYSezbyabBZEBGgm7Uy62`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "523d5e19-2877-48a2-a266-6324e8875bee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wvXXseXfAmxssSb8zDssd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 24947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1695
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

_source line 15 · 2026-05-19T02:55:15.141Z_

<details><summary>↩ Tool result · `toolu_01WWYSezbyabBZEBGgm7Uy62`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\ref{sec:power_curve}).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 $\auc > \theta{=}0.60$ and 2v3 $\auc < \theta$; CIs quantify boundary uncertainty.
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
46	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
47	
48	\paragraph{Scale and instruction-tuning invariance.}
49	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
50	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$); the boundary is not an instruction-tuning artifact.
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
55	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
56	\label{fig:kstar_theta}
57	\end{figure}
58	
59	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
60	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix shows the complete model $\times$ domain $\theta$ sensitivity).
61	All four decoding strategies likewise yield $\Kempirical = 2$ at $\theta{=}0.60$ (1v2 $\auc \in [0.687, 0.704]$; Table~\ref{tab:s2_decoding}).
62	
63	%% ====================================================================
64	\subsection{Largely Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
79	$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
80	Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
81	For arXiv, cross-scoring with Pythia-1.4B preserves $\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\auc$ range: 0.608--0.632).
82	Qwen-7B exhibits a borderline decrease to $\Kempirical{=}2$ (2v3 $\auc = 0.599$ vs.\ $0.626$ self-scored, $\Delta = -2.7$\,pp; 3/5 folds above $\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.
83	Bootstrap CIs (10{,}000 resamples) confirm $\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\theta$; their $\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\ref{tab:arxiv_crossscorer_ci}).
84	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
85	
86	%% ====================================================================
87	\subsection{Feature Ordering and Generation Mode}
88	\label{sec:feature_degradation}
89	\label{sec:generation_mode}
90	
91	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
92	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
93	A feature group ablation (Appendix~\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\leq 0.007$).
94	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
95	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
96	
97	%% ====================================================================
98	\subsection{Neural Probe}
99	\label{sec:neural_probe}
100	
101	Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
102	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
103	
104	\noindent\begin{minipage}{\columnwidth}
105	\centering
106	\footnotesize
107	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
108	\label{tab:neural_probe_crossmodel}
109	\resizebox{\columnwidth}{!}{%
110	\begin{tabular}{lccc}
111	\toprule
112	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
113	\midrule
114	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
115	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
116	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
117	\bottomrule
118	\end{tabular}}
119	\end{minipage}
120	
121	%% ====================================================================
122	\subsection{Cross-Domain Variation}
123	\label{sec:cross_domain}
124	
125	The preceding experiments use C4 (general web text).
126	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
127	
128	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
129	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
130	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
131	Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}); content-level properties dominate.
132	OLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\Kempirical{=}1$.
133	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv: domain structure alone can shift $\Kempirical$ by two levels within the same model.
134	
135	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
136	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
137	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
138	A same-family scorer confound inflates the apparent $\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\Kempirical{=}2$ (1v2 $\auc \approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\,pp to below $\theta$ (Appendix~\ref{sec:wiki_domain}).
139	This +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\ref{sec:transfer}).
140	
141	\paragraph{Code ($\Kempirical{=}2$): cross-modality confirmation.}
142	Python functions from CodeSearchNet~\cite{husain2019codesearchnet} ($n{=}5{,}000$, Qwen2.5-1.5B) yield $\Kempirical{=}2$ (1v2 $\auc = 0.738$, CI $[0.709, 0.767]$; 2v3 $\auc = 0.530$; Table~\ref{tab:code_domain_qwen} in Appendix), matching C4 despite a different modality: higher 1v2 AUC (0.74 vs.\ 0.61--0.70) but the same sharp 2v3 collapse (JSD ratio $11.7\times$).
143	
144	\paragraph{Domain as the primary factor.}
145	With the scorer confound controlled, the domain ordering is uniform: arXiv ($\Kempirical{=}3$) $>$ C4/Code ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
146	Neither scale (1B--14B), architecture, nor modality alters this ordering; domain structural complexity determines $\Kempirical$.
147	
148	\noindent\begin{minipage}{\columnwidth}
149	\centering
150	\footnotesize
151	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\dagger$Same-family scorer yields $\Kempirical{=}2$; controlled value shown.}
152	\label{tab:domain_kstar}
153	\resizebox{\columnwidth}{!}{%
154	\begin{tabular}{lcccc}
155	\toprule
156	\textbf{Model} & \textbf{C4} & \textbf{Code} & \textbf{arXiv} & \textbf{Wikipedia} \\
157	\midrule
158	Qwen-1.5B    & 2 & 2 & 3 & 1$^\dagger$ \\
159	Qwen-7B      & 2 & --- & 3 & 1$^\dagger$ \\
160	Pythia-1.4B  & 2 & --- & 3 & 1 \\
161	OLMo-1B      & 2 & --- & 1$^*$ & 1 \\
162	LLaMA-3.1-8B & 2 & --- & 3 & 1 \\
163	Mistral-7B   & 1 & --- & 3 & 1 \\
164	\bottomrule
165	\end{tabular}}
166	\end{minipage}
167	
168	%% ====================================================================
169	\subsection{Binary Detector Confidence}
170	\label{sec:binary_confidence}
171	
172	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
173	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "83d1e582-3242-41ff-ad0c-df602ff28431",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\\ref{sec:power_curve}).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 $\\auc > \\theta{=}0.60$ and 2v3 $\\auc < \\theta$; CIs quantify boundary uncertainty.\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$); the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix shows the complete model $\\times$ domain $\\theta$ sensitivity).\nAll four decoding strategies likewise yield $\\Kempirical = 2$ at $\\theta{=}0.60$ (1v2 $\\auc \\in [0.687, 0.704]$; Table~\\ref{tab:s2_decoding}).\n\n%% ====================================================================\n\\subsection{Largely Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$; Table~\\ref{tab:crossscorer}).\n$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\nQwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp (Table~\\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\\theta$.\nFor arXiv, cross-scoring with Pythia-1.4B preserves $\\Kempirical{=}3$ for three of four generators (Qwen-1.5B, LLaMA-8B, Mistral-7B; 2v3 $\\auc$ range: 0.608--0.632).\nQwen-7B exhibits a borderline decrease to $\\Kempirical{=}2$ (2v3 $\\auc = 0.599$ vs.\\ $0.626$ self-scored, $\\Delta = -2.7$\\,pp; 3/5 folds above $\\theta$), consistent with the Qwen family's scorer sensitivity observed on C4 and Wikipedia.\nBootstrap CIs (10{,}000 resamples) confirm $\\Kempirical{=}3$ for Qwen-1.5B (CI lower $= 0.617$) and LLaMA-8B (CI lower $= 0.605$); for Mistral-7B (CI: $[0.593, 0.622]$) and Qwen-7B (CI: $[0.584, 0.613]$), the CI straddles $\\theta$; their $\\Kempirical{=}3$ assignment is sensitive to resampling variance (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nA feature group ablation (Appendix~\\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\\leq 0.007$).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nRemoving LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}); content-level properties dominate.\nOLMo-1B constitutes a capacity failure rather than a counter-example; its arXiv generations are entirely out-of-domain (0v1 JSD $= 0.33$, near-total information loss at the first step), yielding $\\Kempirical{=}1$.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv: domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nA same-family scorer confound inflates the apparent $\\Kempirical$ for Qwen generators: Qwen-1.5B scoring yields $\\Kempirical{=}2$ (1v2 $\\auc \\approx 0.61$--$0.62$), but cross-family scoring reduces 1v2 by 2.4\\,pp to below $\\theta$ (Appendix~\\ref{sec:wiki_domain}).\nThis +1 depth bias under same-family scoring is specific to Qwen generators on Wikipedia and does not affect C4 results (Section~\\ref{sec:transfer}).\n\n\\paragraph{Code ($\\Kempirical{=}2$): cross-modality confirmation.}\nPython functions from CodeSearchNet~\\cite{husain2019codesearchnet} ($n{=}5{,}000$, Qwen2.5-1.5B) yield $\\Kempirical{=}2$ (1v2 $\\auc = 0.738$, CI $[0.709, 0.767]$; 2v3 $\\auc = 0.530$; Table~\\ref{tab:code_domain_qwen} in Appendix), matching C4 despite a different modality: higher 1v2 AUC (0.74 vs.\\ 0.61--0.70) but the same sharp 2v3 collapse (JSD ratio $11.7\\times$).\n\n\\paragraph{Domain as the primary factor.}\nWith the scorer confound controlled, the domain ordering is uniform: arXiv ($\\Kempirical{=}3$) $>$ C4/Code ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\nNeither scale (1B--14B), architecture, nor modality alters this ordering; domain structural complexity determines $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\\dagger$Same-family scorer yields $\\Kempirical{=}2$; controlled value shown.}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{Code} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & --- & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & --- & 3 & 1 \\\\\nOLMo-1B      & 2 & --- & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & --- & 3 & 1 \\\\\nMistral-7B   & 1 & --- & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011uVV5kx6AohYgoG2xWPDtY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "0470bb71-83b0-4fd7-ab6d-3e9b5bf80e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011wvXXseXfAmxssSb8zDssd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1695,
      "cache_read_input_tokens": 24947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1695
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

_source line 17 · 2026-05-19T02:55:15.479Z_

<details><summary>↩ Tool result · `toolu_011uVV5kx6AohYgoG2xWPDtY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "7d46939a-4e2f-44b4-81dc-7e06d17e727d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the paper_framing.md and also check if there's prompt-chain data for comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "7fc99381-ea6c-4f32-bd4e-94fc2dc8f5fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UXTJCQVNLVvWZNLHxwWKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27078,
      "cache_read_input_tokens": 26642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27078
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DAjz2cars8CYsHV7LbKma2`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "87cfd839-c0f8-4453-b3ac-4e5093ba3575",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UXTJCQVNLVvWZNLHxwWKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27078,
      "cache_read_input_tokens": 26642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27078
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

_source line 20 · 2026-05-19T02:55:21.280Z_

<details><summary>↩ Tool result · `toolu_01DAjz2cars8CYsHV7LbKma2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\n\\n**子组件：**\\n\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\n>\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|-----------|---------|--------|-----------------|\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\n>\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\n> - Paper 措辞：\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\"\\n\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\"domain competence prerequisite\\\" 分析放 Appendix\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\n> - Sample size: n=2,200 per model\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\"K*=3 with boundary pair AUC of 0.62\\\" 而非 \\\"robustly K*=3\\\"\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\n\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\n\\n**(d) Cross-model transfer (scorer invariance)**\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\n\\n**(e) Representation dependence of K* (Neural Probe)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\n\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection，不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\n\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\"universally beneficial\\\"。维持 \\\"consistent advantage\\\" 措辞，以 HellaSwag 显著性为主要证据。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\"one-wash laundering\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\n- **Headline result template**: \\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\n2. **\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\n3. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\n4. **\\\"arXiv K*=3 样本量够吗？\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\n5. **\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\"异常\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\n6. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7（Qwen-1.5B LoRA, D077: 6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 K*≥4（Pythia-1.4B LoRA），远高于 prompt-chain K*=2。AUC 从 0v1=0.98 单调衰减至 6v7=0.64，衰减加速（Δ从-0.014到-0.061），外推 7v8≈0.57 < θ，K*=7 大概率是 retrain-chain ceiling。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\n7. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\n8. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\n9. **\\\"θ=0.60 选择是否 arbitrary？\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\n10. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\"K*=2 everywhere\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\n- One-wash laundering effect 是 memorable concept 便于传播\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\n\", \"total_chars\": 15556, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "aef09b48-158e-4279-927b-b5ed9c916677",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — gen-depth-contamination\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\\\n\\\\n## Canonical Experimental Condition\\\\n\\\\n**Continuation mode 是 cross-model 结论的基础。**\\\\n\\\\n> \\\\\\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\\\\\"\\\\n\\\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\\\n|-----------|-------------|-------------|---------|\\\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\\\n\\\\n**原则**：\\\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\\\n- mvp-001 (Qwen-rewrite) 定位为 \\\\\\\"pilot study demonstrating feasibility\\\\\\\"，后续用 continuation mode rigorously validate\\\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\\\n\\\\n## Core Claims (2+1 结构, updated D049/D050)\\\\n\\\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\\\n\\\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\\\n\\\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\\\n\\\\n**子组件：**\\\\n\\\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\\\n>\\\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\\\n> |-------|-----------|---------|--------|-----------------|\\\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\\\n>\\\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\\\n>\\\\n> *Decoding strategy invariance (exp-003):*\\\\n> | Decoding | AUC 1v2 | K* |\\\\n> |----------|---------|-----|\\\\n> | greedy | 0.6893 | 2 |\\\\n> | nucleus p=0.9 | 0.6866 | 2 |\\\\n> | temp=0.7 | 0.6887 | 2 |\\\\n> | temp=1.2 | 0.7039 | 2 |\\\\n>\\\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\\\n> - Paper 措辞：\\\\\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\\\\\"\\\\n\\\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\\\\\"domain competence prerequisite\\\\\\\" 分析放 Appendix\\\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\\\n> - Sample size: n=2,200 per model\\\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\\\\\"K*=3 with boundary pair AUC of 0.62\\\\\\\" 而非 \\\\\\\"robustly K*=3\\\\\\\"\\\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\\\n\\\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\\\n\\\\n**(d) Cross-model transfer (scorer invariance)**\\\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\\\n\\\\n**(e) Representation dependence of K* (Neural Probe)**\\\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\\\n\\\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\\\n> - 论文定位：Analysis subsection，不是独立 claim\\\\n\\\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\\\n\\\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\\\\\"universally beneficial\\\\\\\"。维持 \\\\\\\"consistent advantage\\\\\\\" 措辞，以 HellaSwag 显著性为主要证据。\\\\n\\\\n### Supporting Analysis: Canonical Condition Selection\\\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\\\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\\\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\\\\\"one-wash laundering\\\\\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\\\n- **Headline result template**: \\\\\\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\\\\\"\\\\n\\\\n## Anticipated Reviewer Concerns & Responses\\\\n\\\\n1. **\\\\\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\\\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\\\n2. **\\\\\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\\\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\\\n3. **\\\\\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\\\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\\\n4. **\\\\\\\"arXiv K*=3 样本量够吗？\\\\\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\\\n5. **\\\\\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\\\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\\\\\"异常\\\\\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\\\n6. **\\\\\\\"Prompt-chain 不代表真实世界递归污染\\\\\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7（Qwen-1.5B LoRA, D077: 6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 K*≥4（Pythia-1.4B LoRA），远高于 prompt-chain K*=2。AUC 从 0v1=0.98 单调衰减至 6v7=0.64，衰减加速（Δ从-0.014到-0.061），外推 7v8≈0.57 < θ，K*=7 大概率是 retrain-chain ceiling。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\\\n7. **\\\\\\\"同模型做生成和 surprisal 计算有 bias\\\\\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\\\n8. **\\\\\\\"为什么不用 learned representations\\\\\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\\\n9. **\\\\\\\"θ=0.60 选择是否 arbitrary？\\\\\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\\\n10. **\\\\\\\"Graduated filtering 没和 data selection methods 比\\\\\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\\\n\\\\n## Venue Fit\\\\n\\\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\\\\\"K*=2 everywhere\\\\\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\\\n- One-wash laundering effect 是 memorable concept 便于传播\\\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\\\n\\\", \\\"total_chars\\\": 15556, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/paper_framing.md\", \"content\": \"# Paper Framing — gen-depth-contamination\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\\n- Fallback: EMNLP 2026 Findings\\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\\n\\n## Canonical Experimental Condition\\n\\n**Continuation mode 是 cross-model 结论的基础。**\\n\\n> \\\"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\\\"\\n\\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\\n|-----------|-------------|-------------|---------|\\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\\n\\n**原则**：\\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\\n- mvp-001 (Qwen-rewrite) 定位为 \\\"pilot study demonstrating feasibility\\\"，后续用 continuation mode rigorously validate\\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\\n\\n## Core Claims (2+1 结构, updated D049/D050)\\n\\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\\n\\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\\n\\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\\n- **Web text K*=2 是 dominant mode**（C4 7/8 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。LLaMA/Mistral/Qwen-7B Code 结果待更新\\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\\n\\n**子组件：**\\n\\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\\n> **7/8 model configurations yield K*=2 on C4 web text：**\\n>\\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\\n> |-------|-----------|---------|--------|-----------------|\\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\\n>\\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\\n>\\n> *Decoding strategy invariance (exp-003):*\\n> | Decoding | AUC 1v2 | K* |\\n> |----------|---------|-----|\\n> | greedy | 0.6893 | 2 |\\n> | nucleus p=0.9 | 0.6866 | 2 |\\n> | temp=0.7 | 0.6887 | 2 |\\n> | temp=1.2 | 0.7039 | 2 |\\n>\\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\\n> - Paper 措辞：\\\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\\\"\\n\\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \\\"domain competence prerequisite\\\" 分析放 Appendix\\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\\n> - Sample size: n=2,200 per model\\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \\\"K*=3 with boundary pair AUC of 0.62\\\" 而非 \\\"robustly K*=3\\\"\\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\\n\\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\\n\\n**(d) Cross-model transfer (scorer invariance)**\\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\\n\\n**(e) Representation dependence of K* (Neural Probe)**\\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\\n> - 论文定位：validates choice of model-free 15D features for headline characterization\\n\\n**(f) Generation mode analysis (§4.x Analysis subsection)**\\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\\n> - 论文定位：Analysis subsection，不是独立 claim\\n\\n### Secondary: C3 (K*-Aware Data Curation Validation)\\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\\n\\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \\\"universally beneficial\\\"。维持 \\\"consistent advantage\\\" 措辞，以 HellaSwag 显著性为主要证据。\\n\\n### Supporting Analysis: Canonical Condition Selection\\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\\n\\n## Story Spine\\n\\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\\\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\\\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\\\"one-wash laundering\\\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\\n- **Headline result template**: \\\"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 7/8 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\\\"\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"K*∈{1,2,3} 范围太小，结论是否 trivial？\\\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\\n2. **\\\"只基于小模型（≤8B），能推广到更大模型吗？\\\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\\n3. **\\\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\\\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\\n4. **\\\"arXiv K*=3 样本量够吗？\\\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\\n5. **\\\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\\\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \\\"异常\\\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\\n6. **\\\"Prompt-chain 不代表真实世界递归污染\\\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7（Qwen-1.5B LoRA, D077: 6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 K*≥4（Pythia-1.4B LoRA），远高于 prompt-chain K*=2。AUC 从 0v1=0.98 单调衰减至 6v7=0.64，衰减加速（Δ从-0.014到-0.061），外推 7v8≈0.57 < θ，K*=7 大概率是 retrain-chain ceiling。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\\n7. **\\\"同模型做生成和 surprisal 计算有 bias\\\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\\n8. **\\\"为什么不用 learned representations\\\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\\n9. **\\\"θ=0.60 选择是否 arbitrary？\\\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\\n10. **\\\"Graduated filtering 没和 data selection methods 比\\\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\\n\\n## Venue Fit\\n\\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \\\"K*=2 everywhere\\\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\\n- One-wash laundering effect 是 memorable concept 便于传播\\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\\n\", \"total_chars\": 15556, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01CWCzAU1XAy5UJpH3nFMQSd`</summary>

```json
{
  "pattern": "prompt.chain|prompt_chain|exp_qwen_prompt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "53fd8d4b-c0a3-433f-bb0c-828c12dd1b20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UXTJCQVNLVvWZNLHxwWKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27078,
      "cache_read_input_tokens": 26642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 27078
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

_source line 22 · 2026-05-19T02:55:24.357Z_

<details><summary>↩ Tool result · `toolu_01CWCzAU1XAy5UJpH3nFMQSd`</summary>

```text
Found 161 files
artifacts/manifest.yaml
artifacts/exp_qwen_retrain_depth7/analysis_report.md
artifacts/exp_qwen_retrain_depth7/report/analysis_report.md
artifacts/exp_olmo_retrain_chain.py
artifacts/review_issues.yaml
artifacts/exp_olmo_retrain_chain/intermediate/exp_olmo_retrain_chain.py
artifacts/review_reports/round_8.md
artifacts/dream_reports/dream_20260518T125757/meta.yaml
artifacts/dream_reports/dream_20260518T125757/logs/review_worst.log
artifacts/dream_reports/dream_20260518T125757/worst/review_context.yaml
artifacts/dream_reports/dream_20260518T125757/logs/review_median.log
artifacts/dream_reports/dream_20260518T125757/median/review_report.md
artifacts/dream_reports/dream_20260518T125757/median/review_context.yaml
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T125757/worst/paper.tex
artifacts/dream_reports/dream_20260518T125757/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T125757/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T125757/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T125757/median/paper.tex
artifacts/dream_reports/dream_20260518T125757/median/paper_framing.md
artifacts/dream_reports/dream_20260518T125757/median/experiment_data.json
artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T125757/best/paper_framing.md
artifacts/dream_reports/dream_20260518T125757/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260518T125757/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T125757/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T123349/worst/paper.tex
artifacts/dream_reports/dream_20260518T123349/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T123349/median/paper.log
artifacts/dream_reports/dream_20260518T123349/median/paper.tex
artifacts/dream_reports/dream_20260518T123349/median/paper_framing.md
artifacts/dream_reports/dream_20260518T123349/median/experiment_data.json
artifacts/dream_reports/dream_20260518T123349/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T123349/best/paper.tex
artifacts/dream_reports/dream_20260518T123349/best/paper_framing.md
artifacts/dream_reports/dream_20260518T123349/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T123349/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260518T122223/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T122223/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260518T122223/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260518T113009/meta.yaml
artifacts/dream_reports/dream_20260518T113009/logs/review_worst.log
artifacts/dream_reports/dream_20260518T113009/worst/review_context.yaml
artifacts/dream_reports/dream_20260518T113009/logs/review_median.log
artifacts/dream_reports/dream_20260518T113009/median/review_report.md
artifacts/dream_reports/dream_20260518T113009/best/review_report.md
artifacts/dream_reports/dream_20260518T113009/logs/review_best.log
artifacts/dream_reports/dream_20260518T113009/best/review_context.yaml
artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T113009/worst/paper.tex
artifacts/dream_reports/dream_20260518T113009/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T113009/worst/experiment_data.json
artifacts/dream_reports/dream_20260518T113009/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T113009/median/paper.tex
artifacts/dream_reports/dream_20260518T113009/median/paper_framing.md
artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T113009/best/paper.tex
artifacts/dream_reports/dream_20260518T113009/best/paper_framing.md
artifacts/dream_reports/dream_20260518T113009/best/experiment_data.json
artifacts/dream_reports/dream_20260518T113009/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T113009/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260518T113009/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260518T113009/logs/phase1_attempt0.log
artifacts/review_reports/round_6.md
artifacts/review_reports/round_5.md
artifacts/_project/report/theta_sensitivity_analysis.md
artifacts/theta_sensitivity_analysis.md
artifacts/dream_reports/dream_20260516T073047/meta.yaml
artifacts/dream_reports/dream_20260516T073047/logs/review_worst.log
artifacts/dream_reports/dream_20260516T073047/worst/review_report.md
artifacts/dream_reports/dream_20260516T073047/worst/review_context.yaml
artifacts/dream_reports/dream_20260516T073047/logs/review_median.log
artifacts/dream_reports/dream_20260516T073047/median/review_report.md
artifacts/dream_reports/dream_20260516T073047/median/review_context.yaml
artifacts/dream_reports/dream_20260516T073047/logs/review_best.log
artifacts/dream_reports/dream_20260516T073047/best/review_report.md
artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260516T073047/worst/paper.tex
artifacts/dream_reports/dream_20260516T073047/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T073047/worst/experiment_data.json
artifacts/dream_reports/dream_20260516T073047/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260516T073047/median/paper.tex
artifacts/dream_reports/dream_20260516T073047/median/paper_framing.md
artifacts/dream_reports/dream_20260516T073047/median/experiment_data.json
artifacts/dream_reports/dream_20260516T073047/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260516T073047/best/paper_framing.md
artifacts/dream_reports/dream_20260516T073047/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260516T073047/logs/phase2_median_attempt1.log
artifacts/dream_reports/dream_20260516T073047/logs/phase2_median_attempt0.log
artifacts/review_reports/round_1.md
artifacts/_project/paper/discussion_v2.md
artifacts/drafts/discussion_v2.md
artifacts/_project/paper/discussion_section_info.md
artifacts/_project/paper/discussion_outline.md
artifacts/discussion_outline.md
artifacts/dream_reports/dream_20260513T080728/meta.yaml
artifacts/dream_reports/dream_20260513T080728/logs/review_worst.log
artifacts/dream_reports/dream_20260513T080728/worst/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/logs/review_median.log
artifacts/dream_reports/dream_20260513T080728/median/review_report.md
artifacts/dream_reports/dream_20260513T080728/median/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/logs/review_best.log
artifacts/dream_reports/dream_20260513T080728/best/review_report.md
artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T080728/best/paper.aux
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md
artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json
artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T080728/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T080728/logs/phase2_best_attempt0.log
artifacts/_project/report/literature_positioning_notes_d23bf4.md
artifacts/_project/report/literature_positioning_notes.md
artifacts/literature_positioning_notes.md
artifacts/dream_reports/dream_20260512T200328/meta.yaml
artifacts/dream_reports/dream_20260512T200328/logs/review_worst.log
artifacts/dream_reports/dream_20260512T200328/worst/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_median.log
artifacts/dream_reports/dream_20260512T200328/median/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/review_best.log
artifacts/dream_reports/dream_20260512T200328/best/review_report.md
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260512T200328/best/paper.aux
artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json
artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T200328/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260512T200328/logs/phase1_attempt0.log
artifacts/_project/report/methodology_draft.md
artifacts/_project/report/full_study_plan.md
artifacts/_project/report/theory_framework.md
artifacts/_project/report/claim_routes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "a0fa67fa-d368-4ee3-9e9e-22920f6a19a4",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/manifest.yaml",
      "artifacts/exp_qwen_retrain_depth7/analysis_report.md",
      "artifacts/exp_qwen_retrain_depth7/report/analysis_report.md",
      "artifacts/exp_olmo_retrain_chain.py",
      "artifacts/review_issues.yaml",
      "artifacts/exp_olmo_retrain_chain/intermediate/exp_olmo_retrain_chain.py",
      "artifacts/review_reports/round_8.md",
      "artifacts/dream_reports/dream_20260518T125757/meta.yaml",
      "artifacts/dream_reports/dream_20260518T125757/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260518T125757/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260518T125757/logs/review_median.log",
      "artifacts/dream_reports/dream_20260518T125757/median/review_report.md",
      "artifacts/dream_reports/dream_20260518T125757/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260518T125757/worst/paper.tex",
      "artifacts/dream_reports/dream_20260518T125757/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T125757/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T125757/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260518T125757/median/paper.tex",
      "artifacts/dream_reports/dream_20260518T125757/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T125757/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260518T125757/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T125757/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260518T123349/worst/paper.tex",
      "artifacts/dream_reports/dream_20260518T123349/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260518T123349/median/paper.log",
      "artifacts/dream_reports/dream_20260518T123349/median/paper.tex",
      "artifacts/dream_reports/dream_20260518T123349/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T123349/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T123349/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260518T123349/best/paper.tex",
      "artifacts/dream_reports/dream_20260518T123349/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T123349/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260518T123349/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260518T122223/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260518T122223/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260518T122223/logs/phase1_attempt0.log",
      "artifacts/dream_reports/dream_20260518T113009/meta.yaml",
      "artifacts/dream_reports/dream_20260518T113009/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260518T113009/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260518T113009/logs/review_median.log",
      "artifacts/dream_reports/dream_20260518T113009/median/review_report.md",
      "artifacts/dream_reports/dream_20260518T113009/best/review_report.md",
      "artifacts/dream_reports/dream_20260518T113009/logs/review_best.log",
      "artifacts/dream_reports/dream_20260518T113009/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260518T113009/worst/paper.tex",
      "artifacts/dream_reports/dream_20260518T113009/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T113009/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T113009/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260518T113009/median/paper.tex",
      "artifacts/dream_reports/dream_20260518T113009/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T113009/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260518T113009/best/paper.tex",
      "artifacts/dream_reports/dream_20260518T113009/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260518T113009/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260518T113009/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260518T113009/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260518T113009/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260518T113009/logs/phase1_attempt0.log",
      "artifacts/review_reports/round_6.md",
      "artifacts/review_reports/round_5.md",
      "artifacts/_project/report/theta_sensitivity_analysis.md",
      "artifacts/theta_sensitivity_analysis.md",
      "artifacts/dream_reports/dream_20260516T073047/meta.yaml",
      "artifacts/dream_reports/dream_20260516T073047/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260516T073047/worst/review_report.md",
      "artifacts/dream_reports/dream_20260516T073047/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T073047/logs/review_median.log",
      "artifacts/dream_reports/dream_20260516T073047/median/review_report.md",
      "artifacts/dream_reports/dream_20260516T073047/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260516T073047/logs/review_best.log",
      "artifacts/dream_reports/dream_20260516T073047/best/review_report.md",
      "artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260516T073047/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T073047/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T073047/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T073047/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260516T073047/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T073047/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T073047/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260516T073047/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260516T073047/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260516T073047/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T073047/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260516T073047/logs/phase2_median_attempt1.log",
      "artifacts/dream_reports/dream_20260516T073047/logs/phase2_median_attempt0.log",
      "artifacts/review_reports/round_1.md",
      "artifacts/_project/paper/discussion_v2.md",
      "artifacts/drafts/discussion_v2.md",
      "artifacts/_project/paper/discussion_section_info.md",
      "artifacts/_project/paper/discussion_outline.md",
      "artifacts/discussion_outline.md",
      "artifacts/dream_reports/dream_20260513T080728/meta.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260513T080728/worst/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/review_median.log",
      "artifacts/dream_reports/dream_20260513T080728/median/review_report.md",
      "artifacts/dream_reports/dream_20260513T080728/median/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/review_best.log",
      "artifacts/dream_reports/dream_20260513T080728/best/review_report.md",
      "artifacts/dream_reports/dream_20260513T080728/best/review_context.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260513T080728/worst/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T080728/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T080728/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260513T080728/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T080728/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T080728/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260513T080728/best/paper.aux",
      "artifacts/dream_reports/dream_20260513T080728/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T080728/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260513T080728/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260513T080728/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260513T080728/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260513T080728/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260513T080728/logs/phase2_best_attempt0.log",
      "artifacts/_project/report/literature_positioning_notes_d23bf4.md",
      "artifacts/_project/report/literature_positioning_notes.md",
      "artifacts/literature_positioning_notes.md",
      "artifacts/dream_reports/dream_20260512T200328/meta.yaml",
      "artifacts/dream_reports/dream_20260512T200328/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260512T200328/worst/review_report.md",
      "artifacts/dream_reports/dream_20260512T200328/logs/review_median.log",
      "artifacts/dream_reports/dream_20260512T200328/median/review_report.md",
      "artifacts/dream_reports/dream_20260512T200328/logs/review_best.log",
      "artifacts/dream_reports/dream_20260512T200328/best/review_report.md",
      "artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json",
      "artifacts/dream_reports/dream_20260512T200328/worst/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json",
      "artifacts/dream_reports/dream_20260512T200328/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260512T200328/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260512T200328/best/paper.aux",
      "artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
      "artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json",
      "artifacts/dream_reports/dream_20260512T200328/best/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260512T200328/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260512T200328/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260512T200328/logs/phase2_best_attempt0.log",
      "artifacts/dream_reports/dream_20260512T200328/logs/phase1_attempt0.log",
      "artifacts/_project/report/methodology_draft.md",
      "artifacts/_project/report/full_study_plan.md",
      "artifacts/_project/report/theory_framework.md",
      "artifacts/_project/report/claim_routes.md"
    ],
    "numFiles": 161
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me now look at the retrain-chain analysis report for the depth 7 experiment and the JSD decay analysis specific to retrain-chain to get full context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "a9f164ba-fc33-451b-8219-956b3251f88f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiCst54s9gcVXPoefF1HHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 53720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11475
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

_source line 24_

Let me get the retrain depth7 analysis report for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "9fd94a15-a506-4b7d-974e-dae58dd7007c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiCst54s9gcVXPoefF1HHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 53720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11475
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01Xd7XDaTBTnU88o4xNbtPJc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_depth7/analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "f5e67e38-cc29-4385-8a1c-bc3f82523297",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiCst54s9gcVXPoefF1HHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 53720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11475
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

_source line 26 · 2026-05-19T02:55:29.936Z_

<details><summary>↩ Tool result · `toolu_01Xd7XDaTBTnU88o4xNbtPJc`</summary>

```text
1	# Retrain-Chain Depth 0-7 Analysis Report
2	
3	**Experiment**: exp_qwen_retrain_depth7 (extends exp_qwen_retrain_chain)  
4	**Model**: Qwen2.5-1.5B, LoRA rank=16, alpha=32, target=[q,k,v], 1 epoch/gen  
5	**Data**: C4, 5000 docs, nucleus sampling p=0.95 T=1.0  
6	**Scorer**: Qwen2.5-1.5B (self-scoring)  
7	**CI Method**: 5-fold GroupKFold CV, mean ± 1.96·std/√5
8	
9	---
10	
11	## 1. Complete Results
12	
13	| Pair | Mean AUC | 95% CI | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | JSD |
14	|------|----------|--------|--------|--------|--------|--------|--------|-----|
15	| 0v1 | 0.9837 | [0.982, 0.985] | 0.9832 | 0.9821 | 0.9837 | 0.9823 | 0.9873 | 0.2301 |
16	| 1v2 | 0.8971 | [0.895, 0.899] | 0.8923 | 0.8988 | 0.8986 | 0.8991 | 0.8967 | 0.1039 |
17	| 2v3 | 0.8098 | [0.805, 0.814] | 0.8086 | 0.8074 | 0.8180 | 0.8024 | 0.8128 | 0.0750 |
18	| 3v4 | 0.7600 | [0.753, 0.767] | 0.7534 | 0.7617 | 0.7753 | 0.7566 | 0.7531 | 0.0654 |
19	| 4v5 | 0.7459 | [0.738, 0.754] | 0.7429 | 0.7562 | 0.7521 | 0.7300 | 0.7482 | 0.0605 |
20	| 5v6 | 0.7017 | [0.696, 0.708] | 0.7006 | 0.7077 | 0.7104 | 0.6915 | 0.6984 | 0.0350 |
21	| 6v7 | 0.6410 | [0.638, 0.645] | 0.6419 | 0.6349 | 0.6464 | 0.6390 | 0.6430 | 0.0177 |
22	
23	**K\* = 7** (all pairs AUC > θ=0.60; 6v7 CI lower bound = 0.638 > 0.60)
24	
25	---
26	
27	## 2. Consistency with Depth 0-4 (exp_qwen_retrain_chain)
28	
29	| Pair | ext AUC | orig AUC | Δ |
30	|------|---------|----------|------|
31	| 0v1 | 0.9837 | 0.9838 | -0.0001 |
32	| 1v2 | 0.8971 | 0.8969 | +0.0002 |
33	| 2v3 | 0.8098 | 0.8100 | -0.0002 |
34	| 3v4 | 0.7600 | 0.7624 | -0.0024 |
35	
36	All differences < 0.003. The 3v4 pair shows the largest discrepancy (0.0024), within expected variation from feature re-extraction. Per-fold values also match within 0.005. **Consistency confirmed.**
37	
38	---
39	
40	## 3. AUC Decay Trend
41	
42	### Step-wise AUC decrease:
43	
44	| Transition | ΔAUC |
45	|-----------|------|
46	| 0v1 → 1v2 | -0.0866 |
47	| 1v2 → 2v3 | -0.0873 |
48	| 2v3 → 3v4 | -0.0498 |
49	| 3v4 → 4v5 | -0.0141 |
50	| 4v5 → 5v6 | -0.0442 |
51	| 5v6 → 6v7 | -0.0607 |
52	
53	The decay is **not monotonically decreasing** in step size. Three phases are visible:
54	
55	1. **Rapid initial decay** (depth 1-3): ~0.087 AUC/step. The first few generations produce large distributional shifts.
56	2. **Plateau** (depth 3-5): ~0.014-0.050 AUC/step. The model enters a quasi-stable regime where each retrained LoRA produces similar output.
57	3. **Resumed decline** (depth 5-7): ~0.053 AUC/step. Cumulative drift pushes the distributions apart again, but at a rate that will converge.
58	
59	### Linear vs exponential fit
60	
61	- **Linear**: AUC(pair_d) ≈ 1.026 - 0.0571·d → predicts AUC < 0.60 at d ≈ 7.5 (i.e., 7v8 pair). R² ≈ 0.96.
62	- **Logarithmic**: AUC(pair_d) ≈ 0.983 - 0.176·ln(d) → predicts AUC < 0.60 at d ≈ 8.7. Better fit to the concave shape.
63	
64	Both models agree: **K\* ceiling ≈ 7-8** for this configuration.
65	
66	---
67	
68	## 4. JSD Convergence
69	
70	| Pair | JSD | Ratio to previous |
71	|------|-----|-------------------|
72	| 0v1 | 0.2301 | - |
73	| 1v2 | 0.1039 | 0.45x |
74	| 2v3 | 0.0750 | 0.72x |
75	| 3v4 | 0.0654 | 0.87x |
76	| 4v5 | 0.0605 | 0.93x |
77	| 5v6 | 0.0350 | 0.58x |
78	| 6v7 | 0.0177 | 0.51x |
79	
80	JSD decays from 0.230 to 0.018 across 7 steps (92% reduction). The decay is roughly exponential with two rates:
81	- Depth 1-5: gradual convergence (JSD halving every ~3 steps)
82	- Depth 5-7: accelerated convergence (JSD halving every ~1 step)
83	
84	At depth 6v7, JSD = 0.0177 is approaching the noise floor where distributional differences become negligible. This suggests that even if K\* = 8 is achievable, the classifier would need to extract signal from extremely subtle differences (JSD < 0.01).
85	
86	---
87	
88	## 5. K\* Ceiling Prediction
89	
90	Based on the converging trends:
91	- **Conservative estimate**: K\* = 7 (current measurement, fully validated)
92	- **Optimistic extrapolation**: K\* = 8 (logarithmic model predicts 7v8 AUC ≈ 0.60-0.62, borderline)
93	- **Practical ceiling**: K\* ≈ 7-8 for Qwen2.5-1.5B retrain-chain on C4
94	
95	The 6v7 pair (AUC=0.641, margin=0.041 above threshold) is tight enough that 7v8 would likely be borderline or below threshold. The rapidly shrinking JSD (0.018 at 6v7, projected ~0.009 at 7v8) suggests the distributional signal is nearly exhausted.
96	
97	---
98	
99	## 6. Key Takeaways
100	
101	- Retrain-chain K\*=7 is 3.5x the prompt-chain K\*=2, confirming that parameter update creates a qualitatively different and deeper degradation trajectory
102	- The AUC decay is sublinear (concave), not linear, meaning each additional generation adds less distinguishable drift
103	- JSD convergence at depth 7 (0.018) is approaching noise floor, setting a natural ceiling
104	- All 5 folds for 6v7 individually exceed θ=0.60 (range: 0.635-0.646), so K\*=7 is robust across data splits
105	- Depth 0-4 consistency between original and extended experiments validates the pipeline's reproducibility
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "81287099-b21e-48e8-ac77-511ddb1c8902",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_qwen_retrain_depth7/analysis_report.md",
      "content": "# Retrain-Chain Depth 0-7 Analysis Report\n\n**Experiment**: exp_qwen_retrain_depth7 (extends exp_qwen_retrain_chain)  \n**Model**: Qwen2.5-1.5B, LoRA rank=16, alpha=32, target=[q,k,v], 1 epoch/gen  \n**Data**: C4, 5000 docs, nucleus sampling p=0.95 T=1.0  \n**Scorer**: Qwen2.5-1.5B (self-scoring)  \n**CI Method**: 5-fold GroupKFold CV, mean ± 1.96·std/√5\n\n---\n\n## 1. Complete Results\n\n| Pair | Mean AUC | 95% CI | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | JSD |\n|------|----------|--------|--------|--------|--------|--------|--------|-----|\n| 0v1 | 0.9837 | [0.982, 0.985] | 0.9832 | 0.9821 | 0.9837 | 0.9823 | 0.9873 | 0.2301 |\n| 1v2 | 0.8971 | [0.895, 0.899] | 0.8923 | 0.8988 | 0.8986 | 0.8991 | 0.8967 | 0.1039 |\n| 2v3 | 0.8098 | [0.805, 0.814] | 0.8086 | 0.8074 | 0.8180 | 0.8024 | 0.8128 | 0.0750 |\n| 3v4 | 0.7600 | [0.753, 0.767] | 0.7534 | 0.7617 | 0.7753 | 0.7566 | 0.7531 | 0.0654 |\n| 4v5 | 0.7459 | [0.738, 0.754] | 0.7429 | 0.7562 | 0.7521 | 0.7300 | 0.7482 | 0.0605 |\n| 5v6 | 0.7017 | [0.696, 0.708] | 0.7006 | 0.7077 | 0.7104 | 0.6915 | 0.6984 | 0.0350 |\n| 6v7 | 0.6410 | [0.638, 0.645] | 0.6419 | 0.6349 | 0.6464 | 0.6390 | 0.6430 | 0.0177 |\n\n**K\\* = 7** (all pairs AUC > θ=0.60; 6v7 CI lower bound = 0.638 > 0.60)\n\n---\n\n## 2. Consistency with Depth 0-4 (exp_qwen_retrain_chain)\n\n| Pair | ext AUC | orig AUC | Δ |\n|------|---------|----------|------|\n| 0v1 | 0.9837 | 0.9838 | -0.0001 |\n| 1v2 | 0.8971 | 0.8969 | +0.0002 |\n| 2v3 | 0.8098 | 0.8100 | -0.0002 |\n| 3v4 | 0.7600 | 0.7624 | -0.0024 |\n\nAll differences < 0.003. The 3v4 pair shows the largest discrepancy (0.0024), within expected variation from feature re-extraction. Per-fold values also match within 0.005. **Consistency confirmed.**\n\n---\n\n## 3. AUC Decay Trend\n\n### Step-wise AUC decrease:\n\n| Transition | ΔAUC |\n|-----------|------|\n| 0v1 → 1v2 | -0.0866 |\n| 1v2 → 2v3 | -0.0873 |\n| 2v3 → 3v4 | -0.0498 |\n| 3v4 → 4v5 | -0.0141 |\n| 4v5 → 5v6 | -0.0442 |\n| 5v6 → 6v7 | -0.0607 |\n\nThe decay is **not monotonically decreasing** in step size. Three phases are visible:\n\n1. **Rapid initial decay** (depth 1-3): ~0.087 AUC/step. The first few generations produce large distributional shifts.\n2. **Plateau** (depth 3-5): ~0.014-0.050 AUC/step. The model enters a quasi-stable regime where each retrained LoRA produces similar output.\n3. **Resumed decline** (depth 5-7): ~0.053 AUC/step. Cumulative drift pushes the distributions apart again, but at a rate that will converge.\n\n### Linear vs exponential fit\n\n- **Linear**: AUC(pair_d) ≈ 1.026 - 0.0571·d → predicts AUC < 0.60 at d ≈ 7.5 (i.e., 7v8 pair). R² ≈ 0.96.\n- **Logarithmic**: AUC(pair_d) ≈ 0.983 - 0.176·ln(d) → predicts AUC < 0.60 at d ≈ 8.7. Better fit to the concave shape.\n\nBoth models agree: **K\\* ceiling ≈ 7-8** for this configuration.\n\n---\n\n## 4. JSD Convergence\n\n| Pair | JSD | Ratio to previous |\n|------|-----|-------------------|\n| 0v1 | 0.2301 | - |\n| 1v2 | 0.1039 | 0.45x |\n| 2v3 | 0.0750 | 0.72x |\n| 3v4 | 0.0654 | 0.87x |\n| 4v5 | 0.0605 | 0.93x |\n| 5v6 | 0.0350 | 0.58x |\n| 6v7 | 0.0177 | 0.51x |\n\nJSD decays from 0.230 to 0.018 across 7 steps (92% reduction). The decay is roughly exponential with two rates:\n- Depth 1-5: gradual convergence (JSD halving every ~3 steps)\n- Depth 5-7: accelerated convergence (JSD halving every ~1 step)\n\nAt depth 6v7, JSD = 0.0177 is approaching the noise floor where distributional differences become negligible. This suggests that even if K\\* = 8 is achievable, the classifier would need to extract signal from extremely subtle differences (JSD < 0.01).\n\n---\n\n## 5. K\\* Ceiling Prediction\n\nBased on the converging trends:\n- **Conservative estimate**: K\\* = 7 (current measurement, fully validated)\n- **Optimistic extrapolation**: K\\* = 8 (logarithmic model predicts 7v8 AUC ≈ 0.60-0.62, borderline)\n- **Practical ceiling**: K\\* ≈ 7-8 for Qwen2.5-1.5B retrain-chain on C4\n\nThe 6v7 pair (AUC=0.641, margin=0.041 above threshold) is tight enough that 7v8 would likely be borderline or below threshold. The rapidly shrinking JSD (0.018 at 6v7, projected ~0.009 at 7v8) suggests the distributional signal is nearly exhausted.\n\n---\n\n## 6. Key Takeaways\n\n- Retrain-chain K\\*=7 is 3.5x the prompt-chain K\\*=2, confirming that parameter update creates a qualitatively different and deeper degradation trajectory\n- The AUC decay is sublinear (concave), not linear, meaning each additional generation adds less distinguishable drift\n- JSD convergence at depth 7 (0.018) is approaching noise floor, setting a natural ceiling\n- All 5 folds for 6v7 individually exceed θ=0.60 (range: 0.635-0.646), so K\\*=7 is robust across data splits\n- Depth 0-4 consistency between original and extended experiments validates the pipeline's reproducibility\n",
      "numLines": 106,
      "startLine": 1,
      "totalLines": 106
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also quickly check for prompt-chain K* data to compare. The prompt-chain data is essentially the main experiments data from experiments_c1.tex (Table tab:kstar_ci), where K*=2 for most configurations. Let me also look for the Pythia retrain-chain data more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "605fe983-44d1-455a-a5d4-a5d4ca1da201",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uUtHfTkjStNZHGtaKGgc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2714,
      "cache_read_input_tokens": 65195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2714
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

_source line 28_

Now let me check the Pythia retrain-chain status and any existing prompt-chain comparison data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "c8549a4d-d97f-4cbd-9a1c-50868adfd9d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uUtHfTkjStNZHGtaKGgc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2714,
      "cache_read_input_tokens": 65195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2714
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

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_015cQ95jFSgpxhvwpbGQ2nB7`</summary>

```json
{
  "pattern": "pythia.*retrain|retrain.*pythia",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts",
  "output_mode": "files_with_matches",
  "head_limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "83d85fa4-84e9-49a2-8127-73cc229724b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uUtHfTkjStNZHGtaKGgc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2714,
      "cache_read_input_tokens": 65195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2714
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

_source line 30 · 2026-05-19T02:55:39.897Z_

<details><summary>↩ Tool result · `toolu_015cQ95jFSgpxhvwpbGQ2nB7`</summary>

```text
Found 10 files limit: 10
artifacts/_project/report/dream_simulation_readiness.md
artifacts/dream_simulation_readiness.md
artifacts/dream_reports/dream_20260518T125757/logs/review_worst.log
artifacts/dream_reports/dream_20260518T125757/logs/review_median.log
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260518T125757/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260518T125757/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "3b7e1178-6c25-49fc-bbd7-18f39b130040",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/report/dream_simulation_readiness.md",
      "artifacts/dream_simulation_readiness.md",
      "artifacts/dream_reports/dream_20260518T125757/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/review_median.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_worst.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/phase2_worst_attempt0.log",
      "artifacts/dream_reports/dream_20260518T125757/logs/phase2_median_attempt0.log",
      "artifacts/dream_reports/dream_20260518T123349/logs/paper_agent_median.log"
    ],
    "numFiles": 10,
    "appliedLimit": 10
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01M3wpWcDV7bSHqv696XWuxg`</summary>

```json
{
  "pattern": "Pythia.*LoRA.*retrain|retrain.*Pythia",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "f19a80d1-6ff9-414d-a64e-1d28e51a07ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uUtHfTkjStNZHGtaKGgc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2714,
      "cache_read_input_tokens": 65195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2714
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

_source line 32 · 2026-05-19T02:55:41.001Z_

<details><summary>↩ Tool result · `toolu_01M3wpWcDV7bSHqv696XWuxg`</summary>

```text
docs/paper/appendix_extended.tex:37:Retrain-chain validation yields $\Kempirical{=}7$ for Qwen2.5-1.5B LoRA (7 generations; Table~\ref{tab:retrain_ci}) and $\Kempirical{\geq}4$ for Pythia-1.4B LoRA (4 generations tested, all above $\theta$).
docs/paper/appendix_extended.tex:45:\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. \textbf{Qwen2.5-1.5B LoRA} (7 generations): $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\Kempirical{\geq}4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
docs/paper/main.tex:73:(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (Qwen-1.5B LoRA, confirmed ${\geq}4$ for Pythia; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
docs/paper/main.aux:1170:\@writefile{lot}{\contentsline {table}{\numberline {24}{\ignorespaces Retrain-chain pairwise $\text  {AUC}$ with 5-fold CV 95\% CIs. \textbf  {Qwen2.5-1.5B LoRA} (7 generations): ${K^*_{\text  {empirical}}}{=}7$; all CI lower bounds $> \theta {=}0.60$. Pythia-1.4B LoRA (4 generations tested): ${K^*_{\text  {empirical}}}{\geq }4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\ref {sec:retrain_ci_note}).}}{21}{table.caption.49}\protected@file@percent }
docs/paper/main.aux:1171:\newlabel{tab:retrain_ci}{{24}{21}{Retrain-chain pairwise $\auc $ with 5-fold CV 95\% CIs. \textbf {Qwen2.5-1.5B LoRA} (7 generations): $\Kempirical {=}7$; all CI lower bounds $> \theta {=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\Kempirical {\geq }4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\ref {sec:retrain_ci_note})}{table.caption.49}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "b32c3f8c-bca2-48c5-9d0c-70fd1e68fb8b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/appendix_extended.tex:37:Retrain-chain validation yields $\\Kempirical{=}7$ for Qwen2.5-1.5B LoRA (7 generations; Table~\\ref{tab:retrain_ci}) and $\\Kempirical{\\geq}4$ for Pythia-1.4B LoRA (4 generations tested, all above $\\theta$).\ndocs/paper/appendix_extended.tex:45:\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. \\textbf{Qwen2.5-1.5B LoRA} (7 generations): $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\\Kempirical{\\geq}4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\ndocs/paper/main.tex:73:(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{=}7$ (Qwen-1.5B LoRA, confirmed ${\\geq}4$ for Pythia; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\ndocs/paper/main.aux:1170:\\@writefile{lot}{\\contentsline {table}{\\numberline {24}{\\ignorespaces Retrain-chain pairwise $\\text  {AUC}$ with 5-fold CV 95\\% CIs. \\textbf  {Qwen2.5-1.5B LoRA} (7 generations): ${K^*_{\\text  {empirical}}}{=}7$; all CI lower bounds $> \\theta {=}0.60$. Pythia-1.4B LoRA (4 generations tested): ${K^*_{\\text  {empirical}}}{\\geq }4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\\ref {sec:retrain_ci_note}).}}{21}{table.caption.49}\\protected@file@percent }\ndocs/paper/main.aux:1171:\\newlabel{tab:retrain_ci}{{24}{21}{Retrain-chain pairwise $\\auc $ with 5-fold CV 95\\% CIs. \\textbf {Qwen2.5-1.5B LoRA} (7 generations): $\\Kempirical {=}7$; all CI lower bounds $> \\theta {=}0.60$. Pythia-1.4B LoRA (4 generations tested): $\\Kempirical {\\geq }4$. Unlike prompt-chain experiments, retrain-chain CIs use fold-level estimates (Section~\\ref {sec:retrain_ci_note})}{table.caption.49}{}}",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 33_

All data collected. Now writing the notes document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "0e6ceec1-5db3-48b6-8ba2-20f901e82737",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xYxaWAz9K4TDy2VKWo5Hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 67909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1462
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

_source line 34_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JLU4BQF3oBM8U7zs1NeinR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "9073307c-dd89-4200-b75e-39c744220644",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xYxaWAz9K4TDy2VKWo5Hh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 67909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1462
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

_source line 35 · 2026-05-19T02:55:44.572Z_

<details><summary>↩ Tool result · `toolu_01JLU4BQF3oBM8U7zs1NeinR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "03e4ea49-9507-46b7-97be-7d661f2f91c7",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Write · `toolu_01WdbTDp3aTBmdePi97nYLFW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/retrain_chain_paper_notes.md",
  "content": "# Retrain-Chain K*=7 Paper Notes\n\n> 素材文档，供 Paper Agent 写作使用。非论文正文。\n\n---\n\n## A. 完整 AUC 数值 + CI（Qwen2.5-1.5B LoRA, 7 generations）\n\n| Pair | AUC | 95% CI | Per-fold AUC | JSD |\n|------|-----|--------|-------------|-----|\n| 0v1 | 0.9837 | [0.9821, 0.9854] | .9832, .9821, .9837, .9823, .9873 | 0.2301 |\n| 1v2 | 0.8971 | [0.8949, 0.8993] | .8923, .8988, .8986, .8991, .8967 | 0.1039 |\n| 2v3 | 0.8098 | [0.8052, 0.8144] | .8086, .8074, .8180, .8024, .8128 | 0.0750 |\n| 3v4 | 0.7600 | [0.7528, 0.7672] | .7534, .7617, .7753, .7566, .7531 | 0.0654 |\n| 4v5 | 0.7459 | [0.7379, 0.7538] | .7429, .7562, .7521, .7300, .7482 | 0.0605 |\n| 5v6 | 0.7017 | [0.6958, 0.7076] | .7006, .7077, .7104, .6915, .6984 | 0.0350 |\n| 6v7 | 0.6410 | [0.6376, 0.6445] | .6419, .6349, .6464, .6390, .6430 | 0.0177 |\n\n**K\\*=7** at θ=0.60。6v7 CI lower bound = 0.6376，margin = +3.76pp above θ。\n\n### Pythia-1.4B LoRA retrain-chain（depth 0-4, K\\*≥4）\n\n| Pair | AUC | 95% CI |\n|------|-----|--------|\n| 0v1 | 0.9842 | [0.9823, 0.9860] |\n| 1v2 | 0.9471 | [0.9432, 0.9509] |\n| 2v3 | 0.8888 | [0.8832, 0.8943] |\n| 3v4 | 0.7994 | [0.7920, 0.8067] |\n\n4 generations tested, all above θ. Pythia depth extension 正在跑，预期 K\\* 与 Qwen 同量级。\n\n---\n\n## B. Retrain-Chain vs Prompt-Chain 对比\n\n### 同 depth pair 的 AUC 差异（Qwen2.5-1.5B, C4）\n\n| Pair | Retrain AUC | Prompt AUC (best cont.) | Δ | 倍率 |\n|------|-------------|------------------------|---|------|\n| 0v1 | 0.9837 | 0.9971 | -0.0134 | ~1.0x |\n| 1v2 | 0.8971 | 0.6112 | +0.2859 | 1.47x |\n| 2v3 | 0.8098 | 0.5609 | +0.2489 | 1.44x |\n| 3v4 | 0.7600 | 0.5409 | +0.2191 | 1.41x |\n| 4v5 | 0.7459 | 0.5141 | +0.2318 | 1.45x |\n\n- Prompt-chain: K\\*=2（1v2=0.6112, 2v3=0.5609 < θ）\n- Retrain-chain: K\\*=7（所有 7 对 > θ）\n- **K\\* 差距 = 5 generations**（retrain 7 vs prompt 2）\n- 0v1 pair 反向：prompt > retrain，因为 prompt-chain depth-0 是 human text 而 depth-1 是纯 LLM output（最大信号），retrain-chain depth-0 同样是 human text 但 depth-1 是 LoRA-finetuned model output（仍保留大量原模型特征）\n\n### JSD 对比\n\n| Metric | Prompt-chain (C4 Qwen-cont) | Retrain-chain |\n|--------|------------------------------|---------------|\n| 0v1 JSD | ~0.29 | 0.2301 |\n| 1v2 JSD | ~0.01 | 0.1039 |\n| Cliff ratio (0v1/1v2) | ~29x | 2.2x |\n| λ (exponential decay) | ~2.9 | 0.285 |\n| K\\* | 2 | 7 |\n\n**核心差异**：Prompt-chain 有 sharp cliff（0v1→1v2 JSD 下降 ~29x），retrain-chain 无 cliff（比率仅 2.2x），衰减缓慢且持续。\n\n### Pythia 也复现了 retrain >> prompt 的差距\n\n| Pair | Retrain AUC | Prompt AUC (cont.) | Δ |\n|------|-------------|---------------------|---|\n| 0v1 | 0.9842 | 0.9932 | -0.0090 |\n| 1v2 | 0.9471 | 0.6539 | +0.2932 |\n| 2v3 | 0.8888 | 0.5514 | +0.3374 |\n| 3v4 | 0.7994 | 0.5152 | +0.2842 |\n\nPythia retrain 1v2=0.9471 vs prompt 1v2=0.6539，差距更大（+29.3pp vs Qwen +28.6pp）。\n\n---\n\n## C. 关键 Narrative Points\n\n### C1. 为什么 retrain K\\* >> prompt K\\*？\n\n**机制解释**：\n1. **Prompt-chain** 仅传递 text（上一代 output 作为下一代 input），信息丧失纯粹来自 text-intrinsic degradation（autoregressive generation 的信息压缩）。经过 1-2 代，文本统计分布快速收敛到模型的 stationary distribution，后续代际几乎不可区分。\n2. **Retrain-chain** 传递 model weights（在上一代 output 上 fine-tune 出新模型，再用新模型生成）。每一代 LoRA fine-tune 引入**累积的 model-adaptation artifacts**：\n   - Vocabulary narrowing（词表使用逐代收窄）\n   - Repetition bias amplification（重复倾向逐代增强）\n   - Mode collapse（模型行为逐代趋向更窄的分布）\n   - 这些 artifacts 叠加在 text-intrinsic degradation 之上，提供**额外的 depth-distinguishing signal**\n\n**类比**：Prompt-chain 像复印文件（每次复印都有信息损失，但损失很快饱和）；retrain-chain 像让不同人根据上一份复印件重新手写一遍（每次手写都引入个人风格累积漂移）。\n\n### C2. 与 model collapse 文献的关系\n\n- Shumailov et al. (2024) \"The Curse of Recursion\"：描述 iterative retraining on self-generated data 导致 model collapse（分布坍缩、tail loss）。我们的 retrain-chain 正是这一设置的受控版本。\n- Alemohammad et al. (2024) \"Self-Consuming Generative Models Go MAD\"：理论分析 iterative training 的分布退化。\n- **关键定位**：model collapse 文献关注**模型质量退化**（performance degradation），我们关注**可检测性**（discriminability between adjacent generations）。两者互补：\n  - Model collapse = \"what happens to the model\"\n  - 我们的 K\\* = \"what happens to the text, and how long can we tell\"\n- **Retrain K\\*=7 的含义**：即使在 model collapse 进行到第 7 代，我们仍然能区分相邻代际的文本。这意味着 model collapse 的累积效应（vocabulary narrowing 等）恰好是**可检测的 fingerprint**，它们让代际差异持续可观测远超 text-intrinsic saturation point。\n\n### C3. 两种 K\\* 的 operational 含义\n\n| | Prompt-chain K\\* | Retrain-chain K\\* |\n|---|---|---|\n| 测量对象 | Text-intrinsic information loss | Model-adaptation artifacts + text loss |\n| 适用场景 | Data curation（不知道数据来源） | Model archaeology（知道训练 pipeline） |\n| 实操边界 | K\\*=2: 只需 binary filter (gen-0 vs gen-≥1) | K\\*=7: 可做更细粒度的 depth estimation |\n| Generalizability | High（不依赖训练 pipeline 信息） | Low（artifacts 是 setup-specific） |\n\n**论文定位**：Prompt-chain K\\*=2 是 **operational boundary for data curation**（保守的、可泛化的）；retrain-chain K\\*=7 是 **upper bound achievable via model archaeology**（乐观的、需要 pipeline 信息的）。\n\n### C4. AUC 衰减形态对比\n\n- **Prompt-chain**：Step function。0v1 极高（~0.99），1v2 骤降到 ~0.61-0.70（刚好过 θ），2v3 直接到 ~0.55（chance level）。之后 flat。\n- **Retrain-chain**：Smooth concave decay。从 0.98 平滑下降到 0.64，无 cliff。三阶段：\n  1. Rapid (depth 1-3): ~0.087/step\n  2. Plateau (depth 3-5): ~0.014-0.050/step  \n  3. Resumed decline (depth 5-7): ~0.053-0.061/step\n- **Extrapolation**：Linear fit → 7v8 AUC ≈ 0.57 < θ；Logarithmic → 7v8 ≈ 0.60-0.62 borderline. K\\* ceiling ≈ 7-8.\n\n---\n\n## D. Gap 分析：当前论文已写 vs 缺失\n\n### 已入稿内容\n\n| 位置 | 内容 | 数据完整度 |\n|------|------|-----------|\n| `appendix_extended.tex` §Extended Limitations | Retrain-chain K\\*=7 (Qwen) + K\\*≥4 (Pythia) 的完整 AUC/CI 表 (Table 24) | ✅ 完整 |\n| `appendix_extended.tex` §Extended Limitations | CI methodology note（为什么 retrain-chain 用 fold-based CI 而非 bootstrap） | ✅ 完整 |\n| `appendix_extended.tex` §JSD Decay Analysis | Retrain-chain JSD λ=0.285, cliff ratio 1.31x，与 prompt-chain 对比 | ✅ 完整 |\n| `appendix_extended.tex` Fig retrain_decay | AUC decay 图（7 pairs + θ line + extrapolation） | ✅ 完整 |\n| `main.tex` Limitations paragraph | 一句话提及 \"retrain-chain yields K\\*=7...confirmed ≥4 for Pythia\" | ✅ 但极简 |\n| `paper_framing.md` Q6 defense | Retrain-chain 作为 \"prompt-chain ≠ real-world\" concern 的 defense | ✅ 完整 framing |\n\n### 缺失/不足内容\n\n| 缺失点 | 重要性 | 建议处理 |\n|--------|--------|---------|\n| **正文无 retrain-chain 专门段落** | 🔴 高 | 需要在 Experiments 或 Discussion 加一个段落（而非仅在 appendix 和 limitations 提及） |\n| **Retrain vs prompt 的 side-by-side AUC 对比表** | 🔴 高 | 本文档 §B 的对比表应入稿（至少入 appendix） |\n| **机制解释不足** | 🟡 中 | 当前论文只说 \"cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias)\"，缺少对为什么 retrain artifacts 持续更久的 deeper analysis |\n| **与 model collapse 文献的 explicit 连接** | 🟡 中 | 需要在 Related Work 或 Discussion 明确 cite Shumailov et al. / Alemohammad et al. 并 position our retrain-chain 结果 |\n| **Pythia depth extension 结果** | 🟡 中 | 目前只有 K\\*≥4（4 depths tested），depth extension 正在跑。完成后更新 Table 24 和相关段落 |\n| **两种 K\\* 的 operational 区别的 explicit framing** | 🟡 中 | paper_framing.md 有此 framing 但论文正文未充分展开 |\n| **Retrain-chain 的 JSD 衰减形态与 prompt-chain 的 formal 对比图** | 🟡 中 | fig_retrain_decay.png 已有，但缺少 prompt-chain vs retrain-chain overlay 对比 |\n| **K\\* ceiling extrapolation 的 uncertainty quantification** | 🟢 低 | Linear/log 两种 fit 已在 analysis_report，可选入 appendix |\n\n---\n\n## E. 建议论文段落结构\n\n### 方案 1：Discussion 段落（推荐）\n\n在 Discussion/Analysis section 加一个 paragraph 或 subsection：\n\n**\"Retrain-Chain: Upper Bound on Discriminability\"**\n\n1. **Setup**（2 句）：Prompt-chain isolates text-intrinsic degradation; retrain-chain adds model-adaptation artifacts. 两者对应不同 real-world scenarios.\n2. **Result**（3 句）：Retrain K\\*=7 (Qwen, all CI > θ), K\\*≥4 (Pythia, ongoing). 比 prompt K\\*=2 多 5 generations. AUC 从 0.98 smooth decay 到 0.64，无 cliff structure.\n3. **Mechanism**（2 句）：Each retrain step introduces cumulative vocabulary narrowing and repetition bias (consistent with model collapse literature: Shumailov et al. 2024). 这些 artifacts 提供 persistent depth signal absent in prompt-chain.\n4. **Operational implication**（2 句）：Prompt-chain K\\* is the conservative, generalizable boundary for data curation. Retrain-chain K\\* represents the upper bound achievable when the training pipeline is known.\n\n**需要的数据支撑**：\n- Table 24 (appendix, 已有) 的 cross-reference\n- Fig retrain_decay (appendix, 已有) 的 cross-reference\n- Prompt vs retrain AUC 对比（可 inline 或新建 appendix table）\n\n### 方案 2：Experiments subsection（备选）\n\n如果 reviewer 认为 retrain-chain 应是核心 finding 而非 supporting analysis，可提升为 §4.x：\n\n**\"§4.x Retrain-Chain Extends K\\* to 7 Generations\"**\n\n- 正文放 key numbers + AUC decay figure\n- Appendix 放完整 per-fold 表 + JSD analysis\n- 这个方案占用更多正文空间（~0.5 column），需要权衡\n\n### Claims 与数据支撑映射\n\n| Claim | 必需数据 | 数据来源 | 状态 |\n|-------|---------|---------|------|\n| Retrain K\\*=7 | 7-pair AUC + CI | Table 24 | ✅ |\n| Retrain K\\* >> Prompt K\\* | Side-by-side comparison | §B of this doc | ⚠️ 需入稿 |\n| Cross-model consistency | Pythia K\\*≥4 (→ full depth) | Table 24 + ongoing exp | ⚠️ Pythia ext pending |\n| Smooth decay (no cliff) | JSD λ + cliff ratio | §JSD Decay Analysis | ✅ in appendix |\n| K\\* ceiling ≈ 7-8 | Extrapolation + JSD convergence | analysis_report | ✅ in appendix |\n| Operational distinction (curation vs archaeology) | Qualitative framing | paper_framing.md Q6 | ⚠️ 需正文段落 |\n| Model collapse connection | Literature citation + positioning | Shumailov, Alemohammad | ⚠️ 需 Related Work mention |\n\n---\n\n## F. 数据一致性检查\n\n### exp_qwen_retrain_chain (depth 0-4) vs exp_qwen_retrain_depth7 (depth 0-7)\n\n重叠的 depth 0-4 pairs 一致性：\n\n| Pair | Original (final_results.json) | Extended (depth7_results.tex) | Δ |\n|------|-------------------------------|-------------------------------|---|\n| 0v1 | 0.9838 | 0.9837 | -0.0001 |\n| 1v2 | 0.8969 | 0.8971 | +0.0002 |\n| 2v3 | 0.8100 | 0.8098 | -0.0002 |\n| 3v4 | 0.7624 | 0.7600 | -0.0024 |\n\n最大差异 0.0024（3v4 pair），在 fold variance 内。Pipeline reproducibility confirmed.\n\n### 论文中的数值 vs 原始数据\n\nappendix_extended.tex Table 24 中的数值与 analysis_report.md 完全一致。✅\n\n---\n\n*Last updated: 2026-05-19*\n*Source experiments: exp_qwen_retrain_chain, exp_qwen_retrain_depth7*\n*Pending: Pythia retrain-chain depth extension results*\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "f040729e-f305-4504-809a-ca0d8cad11ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKSCEz6sDqCtTXeoqXsytG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 69371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
      },
      "output_tokens": 63,
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

_source line 37 · 2026-05-19T02:57:23.653Z_

<details><summary>↩ Tool result · `toolu_01WdbTDp3aTBmdePi97nYLFW`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/retrain_chain_paper_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "2cd0924e-68ae-46c8-917c-f272ef650707",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/retrain_chain_paper_notes.md",
    "content": "# Retrain-Chain K*=7 Paper Notes\n\n> 素材文档，供 Paper Agent 写作使用。非论文正文。\n\n---\n\n## A. 完整 AUC 数值 + CI（Qwen2.5-1.5B LoRA, 7 generations）\n\n| Pair | AUC | 95% CI | Per-fold AUC | JSD |\n|------|-----|--------|-------------|-----|\n| 0v1 | 0.9837 | [0.9821, 0.9854] | .9832, .9821, .9837, .9823, .9873 | 0.2301 |\n| 1v2 | 0.8971 | [0.8949, 0.8993] | .8923, .8988, .8986, .8991, .8967 | 0.1039 |\n| 2v3 | 0.8098 | [0.8052, 0.8144] | .8086, .8074, .8180, .8024, .8128 | 0.0750 |\n| 3v4 | 0.7600 | [0.7528, 0.7672] | .7534, .7617, .7753, .7566, .7531 | 0.0654 |\n| 4v5 | 0.7459 | [0.7379, 0.7538] | .7429, .7562, .7521, .7300, .7482 | 0.0605 |\n| 5v6 | 0.7017 | [0.6958, 0.7076] | .7006, .7077, .7104, .6915, .6984 | 0.0350 |\n| 6v7 | 0.6410 | [0.6376, 0.6445] | .6419, .6349, .6464, .6390, .6430 | 0.0177 |\n\n**K\\*=7** at θ=0.60。6v7 CI lower bound = 0.6376，margin = +3.76pp above θ。\n\n### Pythia-1.4B LoRA retrain-chain（depth 0-4, K\\*≥4）\n\n| Pair | AUC | 95% CI |\n|------|-----|--------|\n| 0v1 | 0.9842 | [0.9823, 0.9860] |\n| 1v2 | 0.9471 | [0.9432, 0.9509] |\n| 2v3 | 0.8888 | [0.8832, 0.8943] |\n| 3v4 | 0.7994 | [0.7920, 0.8067] |\n\n4 generations tested, all above θ. Pythia depth extension 正在跑，预期 K\\* 与 Qwen 同量级。\n\n---\n\n## B. Retrain-Chain vs Prompt-Chain 对比\n\n### 同 depth pair 的 AUC 差异（Qwen2.5-1.5B, C4）\n\n| Pair | Retrain AUC | Prompt AUC (best cont.) | Δ | 倍率 |\n|------|-------------|------------------------|---|------|\n| 0v1 | 0.9837 | 0.9971 | -0.0134 | ~1.0x |\n| 1v2 | 0.8971 | 0.6112 | +0.2859 | 1.47x |\n| 2v3 | 0.8098 | 0.5609 | +0.2489 | 1.44x |\n| 3v4 | 0.7600 | 0.5409 | +0.2191 | 1.41x |\n| 4v5 | 0.7459 | 0.5141 | +0.2318 | 1.45x |\n\n- Prompt-chain: K\\*=2（1v2=0.6112, 2v3=0.5609 < θ）\n- Retrain-chain: K\\*=7（所有 7 对 > θ）\n- **K\\* 差距 = 5 generations**（retrain 7 vs prompt 2）\n- 0v1 pair 反向：prompt > retrain，因为 prompt-chain depth-0 是 human text 而 depth-1 是纯 LLM output（最大信号），retrain-chain depth-0 同样是 human text 但 depth-1 是 LoRA-finetuned model output（仍保留大量原模型特征）\n\n### JSD 对比\n\n| Metric | Prompt-chain (C4 Qwen-cont) | Retrain-chain |\n|--------|------------------------------|---------------|\n| 0v1 JSD | ~0.29 | 0.2301 |\n| 1v2 JSD | ~0.01 | 0.1039 |\n| Cliff ratio (0v1/1v2) | ~29x | 2.2x |\n| λ (exponential decay) | ~2.9 | 0.285 |\n| K\\* | 2 | 7 |\n\n**核心差异**：Prompt-chain 有 sharp cliff（0v1→1v2 JSD 下降 ~29x），retrain-chain 无 cliff（比率仅 2.2x），衰减缓慢且持续。\n\n### Pythia 也复现了 retrain >> prompt 的差距\n\n| Pair | Retrain AUC | Prompt AUC (cont.) | Δ |\n|------|-------------|---------------------|---|\n| 0v1 | 0.9842 | 0.9932 | -0.0090 |\n| 1v2 | 0.9471 | 0.6539 | +0.2932 |\n| 2v3 | 0.8888 | 0.5514 | +0.3374 |\n| 3v4 | 0.7994 | 0.5152 | +0.2842 |\n\nPythia retrain 1v2=0.9471 vs prompt 1v2=0.6539，差距更大（+29.3pp vs Qwen +28.6pp）。\n\n---\n\n## C. 关键 Narrative Points\n\n### C1. 为什么 retrain K\\* >> prompt K\\*？\n\n**机制解释**：\n1. **Prompt-chain** 仅传递 text（上一代 output 作为下一代 input），信息丧失纯粹来自 text-intrinsic degradation（autoregressive generation 的信息压缩）。经过 1-2 代，文本统计分布快速收敛到模型的 stationary distribution，后续代际几乎不可区分。\n2. **Retrain-chain** 传递 model weights（在上一代 output 上 fine-tune 出新模型，再用新模型生成）。每一代 LoRA fine-tune 引入**累积的 model-adaptation artifacts**：\n   - Vocabulary narrowing（词表使用逐代收窄）\n   - Repetition bias amplification（重复倾向逐代增强）\n   - Mode collapse（模型行为逐代趋向更窄的分布）\n   - 这些 artifacts 叠加在 text-intrinsic degradation 之上，提供**额外的 depth-distinguishing signal**\n\n**类比**：Prompt-chain 像复印文件（每次复印都有信息损失，但损失很快饱和）；retrain-chain 像让不同人根据上一份复印件重新手写一遍（每次手写都引入个人风格累积漂移）。\n\n### C2. 与 model collapse 文献的关系\n\n- Shumailov et al. (2024) \"The Curse of Recursion\"：描述 iterative retraining on self-generated data 导致 model collapse（分布坍缩、tail loss）。我们的 retrain-chain 正是这一设置的受控版本。\n- Alemohammad et al. (2024) \"Self-Consuming Generative Models Go MAD\"：理论分析 iterative training 的分布退化。\n- **关键定位**：model collapse 文献关注**模型质量退化**（performance degradation），我们关注**可检测性**（discriminability between adjacent generations）。两者互补：\n  - Model collapse = \"what happens to the model\"\n  - 我们的 K\\* = \"what happens to the text, and how long can we tell\"\n- **Retrain K\\*=7 的含义**：即使在 model collapse 进行到第 7 代，我们仍然能区分相邻代际的文本。这意味着 model collapse 的累积效应（vocabulary narrowing 等）恰好是**可检测的 fingerprint**，它们让代际差异持续可观测远超 text-intrinsic saturation point。\n\n### C3. 两种 K\\* 的 operational 含义\n\n| | Prompt-chain K\\* | Retrain-chain K\\* |\n|---|---|---|\n| 测量对象 | Text-intrinsic information loss | Model-adaptation artifacts + text loss |\n| 适用场景 | Data curation（不知道数据来源） | Model archaeology（知道训练 pipeline） |\n| 实操边界 | K\\*=2: 只需 binary filter (gen-0 vs gen-≥1) | K\\*=7: 可做更细粒度的 depth estimation |\n| Generalizability | High（不依赖训练 pipeline 信息） | Low（artifacts 是 setup-specific） |\n\n**论文定位**：Prompt-chain K\\*=2 是 **operational boundary for data curation**（保守的、可泛化的）；retrain-chain K\\*=7 是 **upper bound achievable via model archaeology**（乐观的、需要 pipeline 信息的）。\n\n### C4. AUC 衰减形态对比\n\n- **Prompt-chain**：Step function。0v1 极高（~0.99），1v2 骤降到 ~0.61-0.70（刚好过 θ），2v3 直接到 ~0.55（chance level）。之后 flat。\n- **Retrain-chain**：Smooth concave decay。从 0.98 平滑下降到 0.64，无 cliff。三阶段：\n  1. Rapid (depth 1-3): ~0.087/step\n  2. Plateau (depth 3-5): ~0.014-0.050/step  \n  3. Resumed decline (depth 5-7): ~0.053-0.061/step\n- **Extrapolation**：Linear fit → 7v8 AUC ≈ 0.57 < θ；Logarithmic → 7v8 ≈ 0.60-0.62 borderline. K\\* ceiling ≈ 7-8.\n\n---\n\n## D. Gap 分析：当前论文已写 vs 缺失\n\n### 已入稿内容\n\n| 位置 | 内容 | 数据完整度 |\n|------|------|-----------|\n| `appendix_extended.tex` §Extended Limitations | Retrain-chain K\\*=7 (Qwen) + K\\*≥4 (Pythia) 的完整 AUC/CI 表 (Table 24) | ✅ 完整 |\n| `appendix_extended.tex` §Extended Limitations | CI methodology note（为什么 retrain-chain 用 fold-based CI 而非 bootstrap） | ✅ 完整 |\n| `appendix_extended.tex` §JSD Decay Analysis | Retrain-chain JSD λ=0.285, cliff ratio 1.31x，与 prompt-chain 对比 | ✅ 完整 |\n| `appendix_extended.tex` Fig retrain_decay | AUC decay 图（7 pairs + θ line + extrapolation） | ✅ 完整 |\n| `main.tex` Limitations paragraph | 一句话提及 \"retrain-chain yields K\\*=7...confirmed ≥4 for Pythia\" | ✅ 但极简 |\n| `paper_framing.md` Q6 defense | Retrain-chain 作为 \"prompt-chain ≠ real-world\" concern 的 defense | ✅ 完整 framing |\n\n### 缺失/不足内容\n\n| 缺失点 | 重要性 | 建议处理 |\n|--------|--------|---------|\n| **正文无 retrain-chain 专门段落** | 🔴 高 | 需要在 Experiments 或 Discussion 加一个段落（而非仅在 appendix 和 limitations 提及） |\n| **Retrain vs prompt 的 side-by-side AUC 对比表** | 🔴 高 | 本文档 §B 的对比表应入稿（至少入 appendix） |\n| **机制解释不足** | 🟡 中 | 当前论文只说 \"cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias)\"，缺少对为什么 retrain artifacts 持续更久的 deeper analysis |\n| **与 model collapse 文献的 explicit 连接** | 🟡 中 | 需要在 Related Work 或 Discussion 明确 cite Shumailov et al. / Alemohammad et al. 并 position our retrain-chain 结果 |\n| **Pythia depth extension 结果** | 🟡 中 | 目前只有 K\\*≥4（4 depths tested），depth extension 正在跑。完成后更新 Table 24 和相关段落 |\n| **两种 K\\* 的 operational 区别的 explicit framing** | 🟡 中 | paper_framing.md 有此 framing 但论文正文未充分展开 |\n| **Retrain-chain 的 JSD 衰减形态与 prompt-chain 的 formal 对比图** | 🟡 中 | fig_retrain_decay.png 已有，但缺少 prompt-chain vs retrain-chain overlay 对比 |\n| **K\\* ceiling extrapolation 的 uncertainty quantification** | 🟢 低 | Linear/log 两种 fit 已在 analysis_report，可选入 appendix |\n\n---\n\n## E. 建议论文段落结构\n\n### 方案 1：Discussion 段落（推荐）\n\n在 Discussion/Analysis section 加一个 paragraph 或 subsection：\n\n**\"Retrain-Chain: Upper Bound on Discriminability\"**\n\n1. **Setup**（2 句）：Prompt-chain isolates text-intrinsic degradation; retrain-chain adds model-adaptation artifacts. 两者对应不同 real-world scenarios.\n2. **Result**（3 句）：Retrain K\\*=7 (Qwen, all CI > θ), K\\*≥4 (Pythia, ongoing). 比 prompt K\\*=2 多 5 generations. AUC 从 0.98 smooth decay 到 0.64，无 cliff structure.\n3. **Mechanism**（2 句）：Each retrain step introduces cumulative vocabulary narrowing and repetition bias (consistent with model collapse literature: Shumailov et al. 2024). 这些 artifacts 提供 persistent depth signal absent in prompt-chain.\n4. **Operational implication**（2 句）：Prompt-chain K\\* is the conservative, generalizable boundary for data curation. Retrain-chain K\\* represents the upper bound achievable when the training pipeline is known.\n\n**需要的数据支撑**：\n- Table 24 (appendix, 已有) 的 cross-reference\n- Fig retrain_decay (appendix, 已有) 的 cross-reference\n- Prompt vs retrain AUC 对比（可 inline 或新建 appendix table）\n\n### 方案 2：Experiments subsection（备选）\n\n如果 reviewer 认为 retrain-chain 应是核心 finding 而非 supporting analysis，可提升为 §4.x：\n\n**\"§4.x Retrain-Chain Extends K\\* to 7 Generations\"**\n\n- 正文放 key numbers + AUC decay figure\n- Appendix 放完整 per-fold 表 + JSD analysis\n- 这个方案占用更多正文空间（~0.5 column），需要权衡\n\n### Claims 与数据支撑映射\n\n| Claim | 必需数据 | 数据来源 | 状态 |\n|-------|---------|---------|------|\n| Retrain K\\*=7 | 7-pair AUC + CI | Table 24 | ✅ |\n| Retrain K\\* >> Prompt K\\* | Side-by-side comparison | §B of this doc | ⚠️ 需入稿 |\n| Cross-model consistency | Pythia K\\*≥4 (→ full depth) | Table 24 + ongoing exp | ⚠️ Pythia ext pending |\n| Smooth decay (no cliff) | JSD λ + cliff ratio | §JSD Decay Analysis | ✅ in appendix |\n| K\\* ceiling ≈ 7-8 | Extrapolation + JSD convergence | analysis_report | ✅ in appendix |\n| Operational distinction (curation vs archaeology) | Qualitative framing | paper_framing.md Q6 | ⚠️ 需正文段落 |\n| Model collapse connection | Literature citation + positioning | Shumailov, Alemohammad | ⚠️ 需 Related Work mention |\n\n---\n\n## F. 数据一致性检查\n\n### exp_qwen_retrain_chain (depth 0-4) vs exp_qwen_retrain_depth7 (depth 0-7)\n\n重叠的 depth 0-4 pairs 一致性：\n\n| Pair | Original (final_results.json) | Extended (depth7_results.tex) | Δ |\n|------|-------------------------------|-------------------------------|---|\n| 0v1 | 0.9838 | 0.9837 | -0.0001 |\n| 1v2 | 0.8969 | 0.8971 | +0.0002 |\n| 2v3 | 0.8100 | 0.8098 | -0.0002 |\n| 3v4 | 0.7624 | 0.7600 | -0.0024 |\n\n最大差异 0.0024（3v4 pair），在 fold variance 内。Pipeline reproducibility confirmed.\n\n### 论文中的数值 vs 原始数据\n\nappendix_extended.tex Table 24 中的数值与 analysis_report.md 完全一致。✅\n\n---\n\n*Last updated: 2026-05-19*\n*Source experiments: exp_qwen_retrain_chain, exp_qwen_retrain_depth7*\n*Pending: Pythia retrain-chain depth extension results*\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LopSZi6DF5NCjPVELhWMN6`</summary>

```json
{
  "name": "retrain_chain_paper_notes",
  "type": "report",
  "description": "Retrain-chain K*=7 论文素材整理：完整数据、prompt vs retrain 对比、narrative points、gap 分析、段落结构建议",
  "project": "gen-depth-contamination",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/retrain_chain_paper_notes.md",
  "tags": [
    "paper-writing",
    "retrain-chain",
    "K-star"
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
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "9c36f9cf-449c-4d31-9860-89c2a6cacdb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGD6wHpVEzjQwgRPPw6VGd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5214,
      "cache_read_input_tokens": 70094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5214
      },
      "output_tokens": 47,
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

_source line 39 · 2026-05-19T02:57:29.580Z_

<details><summary>↩ Tool result · `toolu_01LopSZi6DF5NCjPVELhWMN6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_a12fef\", \"name\": \"retrain_chain_paper_notes\", \"type\": \"report\", \"description\": \"Retrain-chain K*=7 论文素材整理：完整数据、prompt vs retrain 对比、narrative points、gap 分析、段落结构建议\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/retrain_chain_paper_notes.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T02:57:29.200524+00:00\", \"tags\": [\"paper-writing\", \"retrain-chain\", \"K-star\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "5632c290-3c27-488f-8856-c888b8e96dcd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_a12fef\\\", \\\"name\\\": \\\"retrain_chain_paper_notes\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Retrain-chain K*=7 论文素材整理：完整数据、prompt vs retrain 对比、narrative points、gap 分析、段落结构建议\\\", \\\"path\\\": \\\"projects/gen-depth-contamination/artifacts/_project/report/retrain_chain_paper_notes.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"gen-depth-contamination\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T02:57:29.200524+00:00\\\", \\\"tags\\\": [\\\"paper-writing\\\", \\\"retrain-chain\\\", \\\"K-star\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_a12fef\", \"name\": \"retrain_chain_paper_notes\", \"type\": \"report\", \"description\": \"Retrain-chain K*=7 论文素材整理：完整数据、prompt vs retrain 对比、narrative points、gap 分析、段落结构建议\", \"path\": \"projects/gen-depth-contamination/artifacts/_project/report/retrain_chain_paper_notes.md\", \"url\": null, \"project\": \"gen-depth-contamination\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T02:57:29.200524+00:00\", \"tags\": [\"paper-writing\", \"retrain-chain\", \"K-star\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

素材文档已写入 `artifacts/retrain_chain_paper_notes.md` 并注册。核心内容总结：

**数据层面**：
- 完整 7-pair AUC/CI/JSD + per-fold 数值（§A）
- Retrain vs prompt side-by-side 对比表：retrain 在 1v2 处 AUC 高出 +28.6pp (Qwen) / +29.3pp (Pythia)，K\* 差距 5 generations（§B）

**Narrative 层面**（§C）：
- Retrain K\*>>prompt K\* 的机制：LoRA fine-tune 每代引入累积 model-adaptation artifacts（vocabulary narrowing, repetition bias），叠加在 text-intrinsic degradation 之上
- 与 model collapse 文献（Shumailov, Alemohammad）的定位区分：他们关注 model quality degradation，我们关注 discriminability
- 两种 K\* 的 operational 含义：prompt K\*=2 是 data curation boundary（保守/可泛化），retrain K\*=7 是 model archaeology upper bound

**Gap 分析**（§D）：
- 🔴 **正文缺 retrain-chain 专门段落**（目前仅 appendix + limitations 一句话）
- 🔴 **缺 retrain vs prompt 的 side-by-side 对比表**
- 🟡 缺 model collapse 文献的 explicit citation/positioning
- 🟡 Pythia depth extension 结果 pending

**段落建议**（§E）：推荐在 Discussion 加一个 "Retrain-Chain: Upper Bound on Discriminability" 段落（~8 句），cross-reference 已有的 appendix Table 24 和 fig_retrain_decay。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "uuid": "f1c9cc34-e30b-4ab8-bc36-aae6b3222e63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKxiFvq4huMLVqTWHnok3U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 75308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 554
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

_source line 41_

素材文档已写入 `artifacts/retrain_chain_paper_notes.md` 并注册。核心内容总结：

**数据层面**：
- 完整 7-pair AUC/CI/JSD + per-fold 数值（§A）
- Retrain vs prompt side-by-side 对比表：retrain 在 1v2 处 AUC 高出 +28.6pp (Qwen) / +29.3pp (Pythia)，K\* 差距 5 generations（§B）

**Narrative 层面**（§C）：
- Retrain K\*>>prompt K\* 的机制：LoRA fine-tune 每代引入累积 model-adaptation artifacts（vocabulary narrowing, repetition bias），叠加在 text-intrinsic degradation 之上
- 与 model collapse 文献（Shumailov, Alemohammad）的定位区分：他们关注 model quality degradation，我们关注 discriminability
- 两种 K\* 的 operational 含义：prompt K\*=2 是 data curation boundary（保守/可泛化），retrain K\*=7 是 model archaeology upper bound

**Gap 分析**（§D）：
- 🔴 **正文缺 retrain-chain 专门段落**（目前仅 appendix + limitations 一句话）
- 🔴 **缺 retrain vs prompt 的 side-by-side 对比表**
- 🟡 缺 model collapse 文献的 explicit citation/positioning
- 🟡 Pythia depth extension 结果 pending

**段落建议**（§E）：推荐在 Discussion 加一个 "Retrain-Chain: Upper Bound on Discriminability" 段落（~8 句），cross-reference 已有的 appendix Table 24 和 fig_retrain_decay。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 156042,
  "duration_api_ms": 156408,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "ac0f61d8-2066-4d5d-86dd-115b0d84c571",
  "total_cost_usd": 0.81858275,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 64021,
    "cache_read_input_tokens": 465027,
    "output_tokens": 7376,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 64021,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 501,
        "cache_read_input_tokens": 75308,
        "cache_creation_input_tokens": 554,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 554
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1353,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001463,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 7376,
      "cacheReadInputTokens": 465027,
      "cacheCreationInputTokens": 64021,
      "webSearchRequests": 0,
      "costUSD": 0.81711975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "90be7ebb-ffce-47d1-be67-2394c517d282"
}
```

</details>

---
