# paper appendix tables

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_paper_appendix-tables_20260514T070136.log`
- **Structured JSON:** [`15868aafca94e964a47e.json`](../../sessions/15/15868aafca94e964a47e.json)

## Before a recorded user message

12 recorded events

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
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
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
  "uuid": "df54774e-91ae-4af7-b197-b72ac284105d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1778745000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6b3e6841-3811-4032-aeaf-cb75a20e9d30",
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33"
}
```

---

### Assistant

_source line 4_

Let me read the current appendix file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "68bf61ae-1051-441a-9866-a088865511b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2z2hnJYYaMQc89m6XjNBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12488,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12488
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

<details open><summary>🔧 Tool call — Read · `toolu_012vNszwAWuh4tHQSwo5ekE8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "288b2306-63e2-4c77-90f8-f9d0361d92e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2z2hnJYYaMQc89m6XjNBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12488,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12488
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

_source line 6 · 2026-05-14T07:01:52.960Z_

<details><summary>↩ Tool result · `toolu_012vNszwAWuh4tHQSwo5ekE8`</summary>

```text
1	\appendix
2	\section{Supplementary Figures}
3	
4	\begin{figure}[t]
5	  \centering
6	  \includegraphics[width=\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}
7	  \caption{Pairwise $\auc$ decay curves for four model-mode configurations with bootstrap 95\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\Kempirical=2$ boundary where $\auc$ drops below $\theta=0.60$. This figure complements Figure~\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}
8	  \label{fig:s1_auc_decay_ci}
9	\end{figure}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "5240dd47-11e9-4f51-b4ec-51c342da53e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
      "content": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for four model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I need to append the three tables after the existing content. Let me construct the LaTeX code carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "78aeb735-957c-40c1-b3b4-c1aabd6fdb43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141ukD7UXtvK37w1kFuTt28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 24329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 8_

Now I'll append the three supplementary tables.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "811e69ab-3d2a-459f-8c09-f10207925fe6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141ukD7UXtvK37w1kFuTt28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 24329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01AMDJWsQvxSeWpra4Tcd9Q3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
  "old_string": "  \\label{fig:s1_auc_decay_ci}\n\\end{figure}",
  "new_string": "  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the binary classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC across depth pairs for four decoding configurations. The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$: pairs above this line are reliably separable ($\\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\\rho$ on per-sample feature vectors, indicating the degree to which feature rankings are preserved across decoding strategies.}\n  \\label{tab:s2_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\\\\n    1 vs.\\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\\\\n    3 vs.\\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\\\\n    4 vs.\\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S3: LLM Baseline Per-Depth Accuracy (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\caption{Per-depth classification accuracy for LLM-based detectors (GPT-5.5 and Claude Opus~4.6) compared with the OBD-LightGBM statistical baseline. LLMs receive the raw text and a structured prompt; OBD-LightGBM uses the full 23-feature vector. Overall 5-class and binary (human vs.\\ any synthetic) accuracies are reported at the bottom.}\n  \\label{tab:s3_llm}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth} & \\textbf{GPT-5.5} & \\textbf{Claude Opus 4.6} & \\textbf{OBD-LightGBM} \\\\\n    \\midrule\n    0 (human)    & 0.77  & 0.69  & --- \\\\\n    1            & 0.19  & 0.21  & --- \\\\\n    2            & 0.38  & 0.28  & --- \\\\\n    3            & 0.24  & 0.101 & --- \\\\\n    4            & 0.08  & 0.37  & --- \\\\\n    \\midrule\n    5-class acc  & 0.332 & 0.331 & 0.386 \\\\\n    Binary acc   & 0.878 & 0.882 & --- \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "3d0ba8a4-acd6-4fd6-b26c-a9229e18e253",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141ukD7UXtvK37w1kFuTt28",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 24329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 10 · 2026-05-14T07:02:26.634Z_

<details><summary>↩ Tool result · `toolu_01AMDJWsQvxSeWpra4Tcd9Q3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "248aeb6e-0bb3-4e7d-be03-c61fb8b075ca",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex",
    "oldString": "  \\label{fig:s1_auc_decay_ci}\n\\end{figure}",
    "newString": "  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n\n\\section{Supplementary Tables}\n\n%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Cross-model transfer accuracy matrix. Each cell reports the binary classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n  \\label{tab:s1_transfer}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\\n    \\cmidrule(lr){2-5}\n    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\\n    \\midrule\n    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\\n    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\\n    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\\n    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\\n    \\bottomrule\n  \\end{tabular}\n  \\vspace{4pt}\n\n  \\footnotesize\n  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.\n  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.\n\\end{table*}\n\n%%% Table S2: Decoding Ablation AUC (exp-003)\n\\begin{table*}[t]\n  \\centering\n  \\caption{Pairwise AUC across depth pairs for four decoding configurations. The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$: pairs above this line are reliably separable ($\\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\\rho$ on per-sample feature vectors, indicating the degree to which feature rankings are preserved across decoding strategies.}\n  \\label{tab:s2_decoding}\n  \\begin{tabular}{lcccc}\n    \\toprule\n    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\\n    \\midrule\n    0 vs.\\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\\\\n    1 vs.\\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\\\\n    \\cmidrule(lr){1-5}\n    2 vs.\\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\\\\n    3 vs.\\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\\\\n    4 vs.\\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\\\\n    \\midrule\n    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\\n    \\midrule\n    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &\n    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\\n    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &\n    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table*}\n\n%%% Table S3: LLM Baseline Per-Depth Accuracy (exp-011)\n\\begin{table}[t]\n  \\centering\n  \\caption{Per-depth classification accuracy for LLM-based detectors (GPT-5.5 and Claude Opus~4.6) compared with the OBD-LightGBM statistical baseline. LLMs receive the raw text and a structured prompt; OBD-LightGBM uses the full 23-feature vector. Overall 5-class and binary (human vs.\\ any synthetic) accuracies are reported at the bottom.}\n  \\label{tab:s3_llm}\n  \\begin{tabular}{lccc}\n    \\toprule\n    \\textbf{Depth} & \\textbf{GPT-5.5} & \\textbf{Claude Opus 4.6} & \\textbf{OBD-LightGBM} \\\\\n    \\midrule\n    0 (human)    & 0.77  & 0.69  & --- \\\\\n    1            & 0.19  & 0.21  & --- \\\\\n    2            & 0.38  & 0.28  & --- \\\\\n    3            & 0.24  & 0.101 & --- \\\\\n    4            & 0.08  & 0.37  & --- \\\\\n    \\midrule\n    5-class acc  & 0.332 & 0.331 & 0.386 \\\\\n    Binary acc   & 0.878 & 0.882 & --- \\\\\n    \\bottomrule\n  \\end{tabular}\n\\end{table}",
    "originalFile": "\\appendix\n\\section{Supplementary Figures}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{figures/fig_s1_auc_decay_ci.pdf}\n  \\caption{Pairwise $\\auc$ decay curves for four model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}\n  \\label{fig:s1_auc_decay_ci}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 3,
        "newStart": 7,
        "newLines": 78,
        "lines": [
          "   \\caption{Pairwise $\\auc$ decay curves for four model-mode configurations with bootstrap 95\\% confidence intervals. Error bars computed from 1{,}000 bootstrap resamples. The shaded region marks the $\\Kempirical=2$ boundary where $\\auc$ drops below $\\theta=0.60$. This figure complements Figure~\\ref{fig:auc_decay} in the main text by showing statistical uncertainty for each measurement point.}",
          "   \\label{fig:s1_auc_decay_ci}",
          " \\end{figure}",
          "+",
          "+\\section{Supplementary Tables}",
          "+",
          "+%%% Table S1: Cross-Transfer Confusion Matrix (exp-013)",
          "+\\begin{table*}[t]",
          "+  \\centering",
          "+  \\caption{Cross-model transfer accuracy matrix. Each cell reports the binary classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}",
          "+  \\label{tab:s1_transfer}",
          "+  \\begin{tabular}{lcccc}",
          "+    \\toprule",
          "+    \\multirow{2}{*}{\\textbf{Train Model}} & \\multicolumn{4}{c}{\\textbf{Test Model}} \\\\",
          "+    \\cmidrule(lr){2-5}",
          "+    & Qwen-rw & Pythia & OLMo & Qwen-cont \\\\",
          "+    \\midrule",
          "+    Qwen-rw   & \\textbf{0.4229} & 0.2590 & 0.2653 & 0.3466 \\\\",
          "+    Pythia    & 0.2718 & \\textbf{0.3856} & 0.3531 & 0.3287 \\\\",
          "+    OLMo      & 0.2768 & 0.3450 & \\textbf{0.3822} & 0.3244 \\\\",
          "+    Qwen-cont & 0.3440 & 0.3284 & 0.3112 & \\textbf{0.3875} \\\\",
          "+    \\bottomrule",
          "+  \\end{tabular}",
          "+  \\vspace{4pt}",
          "+",
          "+  \\footnotesize",
          "+  \\textit{Transfer retention} between models $A$ and $B$ is defined as $\\frac{1}{2}\\bigl(\\frac{\\mathrm{acc}(A \\to B)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}} + \\frac{\\mathrm{acc}(B \\to A)}{\\sqrt{\\mathrm{acc}(A \\to A) \\cdot \\mathrm{acc}(B \\to B)}}\\bigr)$.",
          "+  Notable pairs: Pythia$\\leftrightarrow$OLMo 91--92\\%, Qwen-cont$\\leftrightarrow$Pythia 83--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\%, Qwen-rw$\\to$Pythia/OLMo 61--63\\%.",
          "+\\end{table*}",
          "+",
          "+%%% Table S2: Decoding Ablation AUC (exp-003)",
          "+\\begin{table*}[t]",
          "+  \\centering",
          "+  \\caption{Pairwise AUC across depth pairs for four decoding configurations. The horizontal rule between depth pairs 1\\,vs.\\,2 and 2\\,vs.\\,3 marks the empirical detectability boundary $\\Kempirical=2$: pairs above this line are reliably separable ($\\auc > 0.60$), while those below approach chance. Bottom rows report cross-configuration Spearman $\\rho$ on per-sample feature vectors, indicating the degree to which feature rankings are preserved across decoding strategies.}",
          "+  \\label{tab:s2_decoding}",
          "+  \\begin{tabular}{lcccc}",
          "+    \\toprule",
          "+    \\textbf{Depth Pair} & \\textbf{Greedy} & \\textbf{Nuc $p{=}0.9$, $T{=}1.0$} & \\textbf{Nuc $p{=}0.95$, $T{=}0.7$} & \\textbf{Nuc $p{=}0.95$, $T{=}1.2$} \\\\",
          "+    \\midrule",
          "+    0 vs.\\ 1 & 0.9797 & 0.9946 & 0.9878 & 0.9982 \\\\",
          "+    1 vs.\\ 2 & 0.6893 & 0.6866 & 0.6887 & 0.7039 \\\\",
          "+    \\cmidrule(lr){1-5}",
          "+    2 vs.\\ 3 & 0.5613 & 0.5917 & 0.5902 & 0.5823 \\\\",
          "+    3 vs.\\ 4 & 0.5404 & 0.5466 & 0.5393 & 0.5293 \\\\",
          "+    4 vs.\\ 5 & 0.5139 & 0.5068 & 0.5349 & 0.5237 \\\\",
          "+    \\midrule",
          "+    \\multicolumn{5}{l}{\\textbf{Cross-config feature Spearman $\\rho$}} \\\\",
          "+    \\midrule",
          "+    \\multicolumn{2}{l}{Greedy vs.\\ Nuc $p{=}0.9$} & 0.600 &",
          "+    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}0.7$} & 0.782 \\\\",
          "+    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}0.7$} & 0.914 &",
          "+    \\multicolumn{1}{l}{Nuc $p{=}0.9$ vs.\\ $T{=}1.2$} & 0.893 \\\\",
          "+    \\multicolumn{2}{l}{Greedy vs.\\ $T{=}1.2$} & 0.532 &",
          "+    \\multicolumn{1}{l}{$T{=}0.7$ vs.\\ $T{=}1.2$} & 0.668 \\\\",
          "+    \\bottomrule",
          "+  \\end{tabular}",
          "+\\end{table*}",
          "+",
          "+%%% Table S3: LLM Baseline Per-Depth Accuracy (exp-011)",
          "+\\begin{table}[t]",
          "+  \\centering",
          "+  \\caption{Per-depth classification accuracy for LLM-based detectors (GPT-5.5 and Claude Opus~4.6) compared with the OBD-LightGBM statistical baseline. LLMs receive the raw text and a structured prompt; OBD-LightGBM uses the full 23-feature vector. Overall 5-class and binary (human vs.\\ any synthetic) accuracies are reported at the bottom.}",
          "+  \\label{tab:s3_llm}",
          "+  \\begin{tabular}{lccc}",
          "+    \\toprule",
          "+    \\textbf{Depth} & \\textbf{GPT-5.5} & \\textbf{Claude Opus 4.6} & \\textbf{OBD-LightGBM} \\\\",
          "+    \\midrule",
          "+    0 (human)    & 0.77  & 0.69  & --- \\\\",
          "+    1            & 0.19  & 0.21  & --- \\\\",
          "+    2            & 0.38  & 0.28  & --- \\\\",
          "+    3            & 0.24  & 0.101 & --- \\\\",
          "+    4            & 0.08  & 0.37  & --- \\\\",
          "+    \\midrule",
          "+    5-class acc  & 0.332 & 0.331 & 0.386 \\\\",
          "+    Binary acc   & 0.878 & 0.882 & --- \\\\",
          "+    \\bottomrule",
          "+  \\end{tabular}",
          "+\\end{table}"
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

_source line 11_

API Error: 522 {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/","title":"Error 522: Connection timed out","status":522,"detail":"Cloudflare could not establish a TCP connection to the origin server. The TCP handshake timed out, which may indicate the origin is overloaded, firewalling Cloudflare, or unreachable at the network level.","instance":"9fb8099089d0d75e","error_code":522,"error_name":"connection_timeout","error_category":"origin","ray_id":"9fb8099089d0d75e","timestamp":"2026-05-14T07:02:46Z","zone":"api.anthropic.com","cloudflare_error":true,"retryable":true,"retry_after":120,"owner_action_required":true,"what_you_should_do":"**Wait and retry.** Back off for at least 120 seconds. If the error persists, the website operator should verify firewall rules and ensure the origin accepts connections from Cloudflare IP ranges.","footer":"This error was generated by Cloudflare on behalf of the website owner."}. This is a server-side issue, usually temporary — try again in a moment. If it persists, check status.claude.com.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "uuid": "da04e89d-00f4-4d27-a2b0-0ea7495ee6b7",
  "error": "server_error",
  "message": {
    "id": "cebbfaf1-0052-45d1-abb5-c5897ba3dabb",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 12_

API Error: 522 {"type":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/","title":"Error 522: Connection timed out","status":522,"detail":"Cloudflare could not establish a TCP connection to the origin server. The TCP handshake timed out, which may indicate the origin is overloaded, firewalling Cloudflare, or unreachable at the network level.","instance":"9fb8099089d0d75e","error_code":522,"error_name":"connection_timeout","error_category":"origin","ray_id":"9fb8099089d0d75e","timestamp":"2026-05-14T07:02:46Z","zone":"api.anthropic.com","cloudflare_error":true,"retryable":true,"retry_after":120,"owner_action_required":true,"what_you_should_do":"**Wait and retry.** Back off for at least 120 seconds. If the error persists, the website operator should verify firewall rules and ensure the origin accepts connections from Cloudflare IP ranges.","footer":"This error was generated by Cloudflare on behalf of the website owner."}. This is a server-side issue, usually temporary — try again in a moment. If it persists, check status.claude.com.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": true,
  "api_error_status": 522,
  "duration_ms": 57226,
  "duration_api_ms": 38471,
  "num_turns": 3,
  "stop_reason": "stop_sequence",
  "session_id": "f2659105-fce4-49fc-a7b6-fe960e3bca33",
  "total_cost_usd": 0.1560595,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 12814,
    "cache_read_input_tokens": 36170,
    "output_tokens": 2217,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 12814,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2116,
        "cache_read_input_tokens": 24329,
        "cache_creation_input_tokens": 326,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 326
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2357,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002442,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 2217,
      "cacheReadInputTokens": 36170,
      "cacheCreationInputTokens": 12814,
      "webSearchRequests": 0,
      "costUSD": 0.1536175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bcdca87a-fa1d-478f-bfea-e2597dddd463"
}
```

</details>

---
