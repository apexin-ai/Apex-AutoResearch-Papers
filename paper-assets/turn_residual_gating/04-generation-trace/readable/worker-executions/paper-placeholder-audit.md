# paper placeholder audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_placeholder_audit_20260523T144109.log`
- **Structured JSON:** [`0edb89adfe2fffea758e.json`](../../sessions/0e/0edb89adfe2fffea758e.json)

## Before a recorded user message

46 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
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
  "uuid": "21464ca1-1e51-4f9c-993a-a54740c01858",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779562800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9e2c4149-76e8-46e1-9327-0348cb700437",
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to scan several LaTeX files for placeholders, TODOs, and incomplete data markers. Let me read all the files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "54e8a2e5-9d61-4acb-ac9f-398643d4bf7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

读取论文各章节文件，搜索占位符。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "e4584575-16a4-4d28-926e-2892097fe23f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Read · `toolu_011QVzAktpd5moBybeAq6zrr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "7fe131a2-514f-4ecd-a426-e4c0ecd49347",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

_source line 7 · 2026-05-23T14:41:25.982Z_

<details><summary>↩ Tool result · `toolu_011QVzAktpd5moBybeAq6zrr`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\to$${\sim}$0.50). Convergence near $\tau$\,=\,0.5 is expected given the shared GAR loss and does not demonstrate gating benefit. GAR-Dongre remains low (0.01--0.02); scheduled sampling breaks this pattern (\S\ref{sec:discussion}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). ThreadGate significantly outperforms LoRA-only (Wilcoxon $p$\,=\,0.004, $r$\,=\,0.454; GAR-ours 0.064 vs 0.037; Appendix~\ref{sec:appendix-stats}), yet the residual gap remains large (7.8$\times$). A second seed (123) confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{table*}[t]
15	\centering
16	\small
17	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
18	\label{tab:four-way}
19	\begin{tabular}{l ccc ccc cc c}
20	\toprule
21	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
22	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
23	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
24	\midrule
25	\multicolumn{10}{l}{\emph{Baseline}} \\
26	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
27	\midrule
28	\multicolumn{10}{l}{\emph{Gated variants}} \\
29	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
30	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
31	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
32	\midrule
33	\multicolumn{10}{l}{\emph{Ungated}} \\
34	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\begin{figure}[t]
40	  \centering
41	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
42	  \caption{Per-turn GAR-ours under TF evaluation ($N$\,=\,45, $\pm$1\,std). Fine-tuned variants maintain GAR near $\tau$\,=\,0.5 (7--8\% decay T1$\to$T4); Base decays 80\%. AR GAR collapses to 0.019--0.064 for all variants (Table~\ref{tab:four-way}).}
43	  \label{fig:attention-heatmap}
44	\end{figure}
45	
46	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
47	
48	All training-time interventions leave the exposure bias gap intact. We test inference-time recovery by applying additive bias $\beta$ to goal-token attention logits during generation (Figure~\ref{fig:headline}b). At $\beta$\,=\,3 ($N$\,=\,50), GAR recovers 8.7$\times$ (0.064$\to$0.556) with only 9\% PPL cost; at $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77). An initial sweep ($N$\,=\,5, 10-turn; Appendix~\ref{sec:appendix-steering}) reveals sharp nonlinearity at $\beta \in [2, 5]$ with ${\sim}$11$\times$ recovery.
49	
50	This provides constructive evidence that attention misallocation---not representation degradation---is the proximal cause: manually correcting attention restores GAR, circumventing the exposure bias barrier. The experiment is diagnostic, requiring goal-token identification.
51	
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "b0d5ecff-b6a0-456a-a1fe-a072f86e9f3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\\,GB). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and PPL.\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\\to$${\\sim}$0.50). Convergence near $\\tau$\\,=\\,0.5 is expected given the shared GAR loss and does not demonstrate gating benefit. GAR-Dongre remains low (0.01--0.02); scheduled sampling breaks this pattern (\\S\\ref{sec:discussion}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}a). ThreadGate significantly outperforms LoRA-only (Wilcoxon $p$\\,=\\,0.004, $r$\\,=\\,0.454; GAR-ours 0.064 vs 0.037; Appendix~\\ref{sec:appendix-stats}), yet the residual gap remains large (7.8$\\times$). A second seed (123) confirms TF stability ($0.504\\pm0.001$). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\\,=\\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\\leq$2\\,pp spread); the 8--17$\\times$ TF-AR gap persists across all configurations. $\\bar{g}\\!\\pm\\!\\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\n\\label{tab:four-way}\n\\begin{tabular}{l ccc ccc cc c}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{IID (TF)}} & \\multicolumn{3}{c}{\\textbf{Held-out (TF)}} & \\multicolumn{2}{c}{\\textbf{AR ($N$\\,=\\,50)}} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7} \\cmidrule(lr){8-9}\n\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\\% CI & $\\bar{g}\\!\\pm\\!\\sigma_g$ \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Baseline}} \\\\\nBase              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\\scriptsize[.014,\\,.024]} & --- \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Gated variants}} \\\\\nThreadGate        & 0.50 & \\textbf{0.02} & 2.78 & 0.50 & \\textbf{0.02} & 2.78 & \\textbf{0.064} & {\\scriptsize[.041,\\,.091]} & .93\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\;+\\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\\scriptsize[.023,\\,.038]} & --- \\\\\nUniform Gate      & 0.49 & 0.01 & 2.78 & \\textbf{0.51} & 0.01 & 2.78 & 0.033 & {\\scriptsize[.025,\\,.043]} & .96\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Ungated}} \\\\\nLoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\\scriptsize[.027,\\,.050]} & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig4_attention_heatmap.pdf}\n  \\caption{Per-turn GAR-ours under TF evaluation ($N$\\,=\\,45, $\\pm$1\\,std). Fine-tuned variants maintain GAR near $\\tau$\\,=\\,0.5 (7--8\\% decay T1$\\to$T4); Base decays 80\\%. AR GAR collapses to 0.019--0.064 for all variants (Table~\\ref{tab:four-way}).}\n  \\label{fig:attention-heatmap}\n\\end{figure}\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\nAll training-time interventions leave the exposure bias gap intact. We test inference-time recovery by applying additive bias $\\beta$ to goal-token attention logits during generation (Figure~\\ref{fig:headline}b). At $\\beta$\\,=\\,3 ($N$\\,=\\,50), GAR recovers 8.7$\\times$ (0.064$\\to$0.556) with only 9\\% PPL cost; at $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77). An initial sweep ($N$\\,=\\,5, 10-turn; Appendix~\\ref{sec:appendix-steering}) reveals sharp nonlinearity at $\\beta \\in [2, 5]$ with ${\\sim}$11$\\times$ recovery.\n\nThis provides constructive evidence that attention misallocation---not representation degradation---is the proximal cause: manually correcting attention restores GAR, circumventing the exposure bias barrier. The experiment is diagnostic, requiring goal-token identification.\n\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Tf5nWmjTZRjmHWJxh8xmbf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "b1a10c4a-a405-4ca5-a08c-691af5a2d0f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

_source line 9 · 2026-05-23T14:41:26.515Z_

<details><summary>↩ Tool result · `toolu_01Tf5nWmjTZRjmHWJxh8xmbf`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ GAR magnitude) pushes gates toward identity (2--7\% attenuation). Steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (\S\ref{subsec:steering}).
4	
5	\paragraph{Scheduled sampling and downstream effects.} Scheduled sampling \citep{bengio2015scheduled} increases AR GAR-ours from 0.064 to 0.347 (5.4$\times$), compressing the 7.8$\times$ gap to 1.44$\times$ with negligible PPL change (1.44 vs.\ 1.43); a second seed yields 0.418 (gap 1.20$\times$). GAR-Dongre also rises (0.019$\to$0.353; $N$\,=\,5 pilot). The gating benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with compounding over turns. KV cache drift is a downstream consequence; instruction retention ($\beta$\,=\,3) shows content compliance rising +23.8\,pp ($p$\,=\,0.077) with GAR correlation $r$\,=\,0.200 ($p$\,=\,0.007), while format constraints show no change (Appendix~\ref{sec:appendix-ir}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "612ed69e-7158-4676-b6bc-40e9c897ecdf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\\times$ GAR magnitude) pushes gates toward identity (2--7\\% attenuation). Steering ($\\beta$\\,=\\,5) recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (\\S\\ref{subsec:steering}).\n\n\\paragraph{Scheduled sampling and downstream effects.} Scheduled sampling \\citep{bengio2015scheduled} increases AR GAR-ours from 0.064 to 0.347 (5.4$\\times$), compressing the 7.8$\\times$ gap to 1.44$\\times$ with negligible PPL change (1.44 vs.\\ 1.43); a second seed yields 0.418 (gap 1.20$\\times$). GAR-Dongre also rises (0.019$\\to$0.353; $N$\\,=\\,5 pilot). The gating benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with compounding over turns. KV cache drift is a downstream consequence; instruction retention ($\\beta$\\,=\\,3) shows content compliance rising +23.8\\,pp ($p$\\,=\\,0.077) with GAR correlation $r$\\,=\\,0.200 ($p$\\,=\\,0.007), while format constraints show no change (Appendix~\\ref{sec:appendix-ir}).",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01N2VicqdXyPyVF5Jv19q8XP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "cce43e32-93fd-4c66-81e3-ce92ffad0e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

_source line 11 · 2026-05-23T14:41:26.872Z_

<details><summary>↩ Tool result · `toolu_01N2VicqdXyPyVF5Jv19q8XP`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Fine-tuned to allocate 50\% of its attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse that widens to 27$\times$ on Llama-3.1-8B. This paper traces the failure to exposure bias \citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, even when next-token prediction (NTP) remains robust.
4	
5	Multi-turn attention decay is well-documented---\citet{dongre2026attention} showed that the Goal Accessibility Ratio (GAR), measuring attention to system-prompt goal tokens, declines 27--48\% across 12 models (we observe 70.8\% on Qwen-2.5-7B) while residual stream probes retain goal content (AUC\,=\,0.98)---but three research gaps remain open. To our knowledge, no work examines how per-layer transformer behavior varies across conversation turns (the \emph{turn$\times$depth} gap). Existing remediations---split-softmax \citep{li2024measuring}, StreamingLLM \citep{xiao2024streaming}, gated attention \citep{qiu2025gated}---operate at inference time or are turn-agnostic; \emph{training-time} multi-turn attention optimization has not been attempted. And classical exposure bias mitigation \citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no \emph{multi-turn transformer equivalent} exists.
6	
7	ThreadGate addresses these gaps with per-layer content-and-turn-conditioned MLP gates on the residual stream: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$, where $g_l$ is a two-layer network conditioned on hidden states and turn position. A five-way controlled comparison---ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base---isolates turn conditioning, gating, gradient conflict, and fine-tuning (\S\ref{sec:comparison-design}), where each adjacent pair kills exactly one alternative hypothesis.
8	
9	\begin{figure*}[t]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\approx$0.50; under AR generation ($N$\,=\,50), GAR collapses 7.8--16.7$\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause (9\% PPL cost at $\beta$\,=\,3).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Training succeeds: all variants converge to TF GAR\,=\,0.50 (Figure~\ref{fig:headline}a). AR GAR collapses to 0.019--0.064 (8--17$\times$). Gating outperforms LoRA-only ($p$\,=\,0.004) yet the gap remains 7.8$\times$. PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling it out by \emph{modus tollens}. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a prefix property with no AR counterpart. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to 1.44$\times$ (\S\ref{sec:discussion}).
17	
18	Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\times$$\to$1.44$\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "c3290e10-f6aa-4e46-91c2-4789a1bea8c6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nFine-tuned to allocate 50\\% of its attention to system-prompt goals (GAR\\,=\\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\\,=\\,0.064 under autoregressive generation---an 8$\\times$ collapse that widens to 27$\\times$ on Llama-3.1-8B. This paper traces the failure to exposure bias \\citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, even when next-token prediction (NTP) remains robust.\n\nMulti-turn attention decay is well-documented---\\citet{dongre2026attention} showed that the Goal Accessibility Ratio (GAR), measuring attention to system-prompt goal tokens, declines 27--48\\% across 12 models (we observe 70.8\\% on Qwen-2.5-7B) while residual stream probes retain goal content (AUC\\,=\\,0.98)---but three research gaps remain open. To our knowledge, no work examines how per-layer transformer behavior varies across conversation turns (the \\emph{turn$\\times$depth} gap). Existing remediations---split-softmax \\citep{li2024measuring}, StreamingLLM \\citep{xiao2024streaming}, gated attention \\citep{qiu2025gated}---operate at inference time or are turn-agnostic; \\emph{training-time} multi-turn attention optimization has not been attempted. And classical exposure bias mitigation \\citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no \\emph{multi-turn transformer equivalent} exists.\n\nThreadGate addresses these gaps with per-layer content-and-turn-conditioned MLP gates on the residual stream: $x_{l+1} = x_l + g_l \\cdot f_l(x_l)$, where $g_l$ is a two-layer network conditioned on hidden states and turn position. A five-way controlled comparison---ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base---isolates turn conditioning, gating, gradient conflict, and fine-tuning (\\S\\ref{sec:comparison-design}), where each adjacent pair kills exactly one alternative hypothesis.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\\approx$0.50; under AR generation ($N$\\,=\\,50), GAR collapses 7.8--16.7$\\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3).}\n  \\label{fig:headline}\n\\end{figure*}\n\nTraining succeeds: all variants converge to TF GAR\\,=\\,0.50 (Figure~\\ref{fig:headline}a). AR GAR collapses to 0.019--0.064 (8--17$\\times$). Gating outperforms LoRA-only ($p$\\,=\\,0.004) yet the gap remains 7.8$\\times$. PCGrad eliminates gradient conflict but \\emph{worsens} AR GAR ($p$\\,=\\,0.002), ruling it out by \\emph{modus tollens}. NTP self-recovers \\citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a prefix property with no AR counterpart. Steering ($\\beta$\\,=\\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to 1.44$\\times$ (\\S\\ref{sec:discussion}).\n\nOur contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\\,=\\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\\times$$\\to$1.44$\\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01CyMK48V25dE3QV6g8yjt22`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "23f0523f-7318-4321-a7f5-00cf2b84cde3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

_source line 13 · 2026-05-23T14:41:27.321Z_

<details><summary>↩ Tool result · `toolu_01CyMK48V25dE3QV6g8yjt22`</summary>

```text
1	\begin{abstract}
2	Fine-tuned to allocate 50\% of attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse. We trace this failure to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. ThreadGate, per-layer content-and-turn-conditioned MLP gates trained with an auxiliary GAR loss, provides a controlled testbed. A five-way comparison isolates turn conditioning, gating, gradient conflict, and fine-tuning; each pair kills one hypothesis. Gating outperforms LoRA-only ($p$\,=\,0.004) but the gap remains 7.8$\times$; PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling out the most intuitive failure mechanism by \emph{modus tollens}. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to 1.44$\times$ (single seed). Cross-model evaluation on Llama-3.1-8B confirms a 27$\times$ gap. These findings establish that exposure bias selectively destroys auxiliary attention losses while NTP self-recovers---a failure mode without prior multi-turn transformer characterization.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "33e20858-b13b-4ed9-9fb5-0ecfa9d82bf2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nFine-tuned to allocate 50\\% of attention to system-prompt goals (GAR\\,=\\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\\,=\\,0.064 under autoregressive generation---an 8$\\times$ collapse. We trace this failure to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. ThreadGate, per-layer content-and-turn-conditioned MLP gates trained with an auxiliary GAR loss, provides a controlled testbed. A five-way comparison isolates turn conditioning, gating, gradient conflict, and fine-tuning; each pair kills one hypothesis. Gating outperforms LoRA-only ($p$\\,=\\,0.004) but the gap remains 7.8$\\times$; PCGrad eliminates gradient conflict but \\emph{worsens} AR GAR ($p$\\,=\\,0.002), ruling out the most intuitive failure mechanism by \\emph{modus tollens}. Steering ($\\beta$\\,=\\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to 1.44$\\times$ (single seed). Cross-model evaluation on Llama-3.1-8B confirms a 27$\\times$ gap. These findings establish that exposure bias selectively destroys auxiliary attention losses while NTP self-recovers---a failure mode without prior multi-turn transformer characterization.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01UH9424D1K1YhErZhmG2K4H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "f8280e3d-7c31-41e5-9cfe-71ada01934f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Em4ANY1fFAeyNWSKdh4KTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13711,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13711
      },
      "output_tokens": 27,
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

_source line 15 · 2026-05-23T14:41:27.787Z_

<details><summary>↩ Tool result · `toolu_01UH9424D1K1YhErZhmG2K4H`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	A five-way controlled comparison on ThreadGate---per-layer content-and-turn-conditioned gates with an auxiliary GAR loss---reveals that training succeeds (TF GAR\,=\,0.50) but autoregressive GAR collapses 8--17$\times$ on Qwen-2.5-7B (27$\times$ on Llama-3.1-8B). Each ablation pair kills one hypothesis: turn conditioning does not rescue late-turn attention; gradient conflict is causally inconsequential ($p$\,=\,0.002, effect reverses); gating outperforms LoRA-only ($p$\,=\,0.004) but cannot close the gap. The failure traces to exposure bias---a mechanism classical in origin but with no prior multi-turn transformer characterization. Steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap 7.8$\times$$\to$1.44$\times$; single seed) provide the first evidence that this barrier is surmountable.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "9d660be9-e7a5-4115-8650-439489d3bb32",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nA five-way controlled comparison on ThreadGate---per-layer content-and-turn-conditioned gates with an auxiliary GAR loss---reveals that training succeeds (TF GAR\\,=\\,0.50) but autoregressive GAR collapses 8--17$\\times$ on Qwen-2.5-7B (27$\\times$ on Llama-3.1-8B). Each ablation pair kills one hypothesis: turn conditioning does not rescue late-turn attention; gradient conflict is causally inconsequential ($p$\\,=\\,0.002, effect reverses); gating outperforms LoRA-only ($p$\\,=\\,0.004) but cannot close the gap. The failure traces to exposure bias---a mechanism classical in origin but with no prior multi-turn transformer characterization. Steering ($\\beta$\\,=\\,5, GAR 0.727) and scheduled sampling (gap 7.8$\\times$$\\to$1.44$\\times$; single seed) provide the first evidence that this barrier is surmountable.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the appendix and any other sections for completeness. Let me also search for specific placeholder patterns across all tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "c300fb3d-962a-4122-8768-5f814243f3a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbP5sPhtnKBrTSiCHF4kqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4839,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4839
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

_source line 17_

搜索更多占位符模式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "8504b819-64a0-4ed4-af1b-a9860f2edbfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbP5sPhtnKBrTSiCHF4kqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4839,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4839
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

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01DnvrpwcHGSnR1dFvWGKpoQ`</summary>

```json
{
  "pattern": "TODO|XXX|FIXME|TBD|PLACEHOLDER|\\?\\?|single seed|preliminary|to be updated",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
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
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "88f78628-cd3a-471d-ad1b-2ebde088c79b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbP5sPhtnKBrTSiCHF4kqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4839,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4839
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

_source line 19 · 2026-05-23T14:41:34.635Z_

<details><summary>↩ Tool result · `toolu_01DnvrpwcHGSnR1dFvWGKpoQ`</summary>

```text
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/limitations.tex:3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "ae8c5674-b939-4b85-9fb5-d817a8d14008",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/conclusion.tex:3:[Omitted long matching line]\npaper/sections/abstract.tex:2:[Omitted long matching line]\npaper/sections/limitations.tex:3:[Omitted long matching line]",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01DUv4kiXtbcTYk9hnpksAzS`</summary>

```json
{
  "pattern": "\\\\textbf\\{\\?\\}|---\\s*$|1\\.5B|MMLU|bootstrap|multi-seed|three.seed|3.seed",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
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
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "b6049b93-c3f8-44af-8072-b5c4a91a115f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbP5sPhtnKBrTSiCHF4kqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4839,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4839
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

_source line 21 · 2026-05-23T14:41:36.970Z_

<details><summary>↩ Tool result · `toolu_01DUv4kiXtbcTYk9hnpksAzS`</summary>

```text
paper/sections/related_work.tex:13:[Omitted long matching line]
paper/sections/appendix.tex:120:\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "8afe6515-f3b1-4356-814e-4e4dda1bffb0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/related_work.tex:13:[Omitted long matching line]\npaper/sections/appendix.tex:120:\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_016g1Y7tcoQ3m96nYwbFDvyA`</summary>

```json
{
  "pattern": "% .*update|% .*fill|% .*replace|% .*pending|% .*need",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
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
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "100c6b0b-c682-4bb9-a1c8-e5c72d4ff8bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbP5sPhtnKBrTSiCHF4kqW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4839,
      "cache_read_input_tokens": 25552,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4839
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

_source line 23 · 2026-05-23T14:41:38.519Z_

<details><summary>↩ Tool result · `toolu_016g1Y7tcoQ3m96nYwbFDvyA`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "b3677ba9-ba49-4043-865f-4ba57aa8363b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_013bqHFrysUM8NDY6LRsgoJN`</summary>

```json
{
  "pattern": "single seed",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "742176cf-39d5-45d5-bcdd-a3ec3f49502b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118k3ht9y5UvbaMPTNbWpir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 30391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 61,
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

_source line 25 · 2026-05-23T14:41:42.041Z_

<details><summary>↩ Tool result · `toolu_013bqHFrysUM8NDY6LRsgoJN`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex-2-
paper/sections/conclusion.tex:3:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex-2-
paper/sections/limitations.tex:3:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-1-\begin{abstract}
paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-3-\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "9ab5abed-5950-4833-af56-b9047017c232",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex-2-\npaper/sections/conclusion.tex:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex-2-\npaper/sections/limitations.tex:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-1-\\begin{abstract}\npaper/sections/abstract.tex:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-3-\\end{abstract}",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01TruG72E9TpEkqkFZqQGJjS`</summary>

```json
{
  "pattern": "Llama.*gap|cross.model|27",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "35232fa0-a72a-4007-b0b4-c0315a241487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118k3ht9y5UvbaMPTNbWpir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 30391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 61,
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

_source line 27 · 2026-05-23T14:41:43.510Z_

<details><summary>↩ Tool result · `toolu_01TruG72E9TpEkqkFZqQGJjS`</summary>

```text
paper/sections/analysis.tex:3:[Omitted long matching line]
paper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
paper/sections/analysis.tex:16:  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}
paper/sections/analysis.tex:39:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
paper/sections/analysis.tex:41:\subsection{Cross-Model Replication}\label{subsec:cross-model}
paper/sections/analysis.tex:43:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:19:[Omitted long matching line]
paper/sections/experiments.tex:34:LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
paper/sections/experiments.tex:48:[Omitted long matching line]
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/discussion.tex:3:The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ GAR magnitude) pushes gates toward identity (2--7\% attenuation). Steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (\S\ref{subsec:steering}).
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/appendix.tex:152:Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
paper/sections/appendix.tex:158:\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
paper/sections/appendix.tex:178:\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
paper/sections/appendix.tex:199:\subsection{Cross-Model Gate Profile Comparison}
paper/sections/appendix.tex:212:[Omitted long matching line]
paper/sections/appendix.tex:247:[Omitted long matching line]
paper/sections/appendix.tex:265:L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
paper/sections/appendix.tex:271:The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
paper/sections/appendix.tex:273:\paragraph{Cross-model comparison.} Llama-3.1-8B-Instruct (32 layers) shows a qualitatively different profile: a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809) rather than early-layer dips. Both architectures converge toward identity at output-adjacent layers, but the location of maximum attenuation differs---early for Qwen, late-middle for Llama---suggesting that layer importance hierarchies are architecture-dependent rather than universal.
paper/sections/introduction.tex:3:Fine-tuned to allocate 50\% of its attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse that widens to 27$\times$ on Llama-3.1-8B. This paper traces the failure to exposure bias \citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, even when next-token prediction (NTP) remains robust.
paper/sections/introduction.tex:5:[Omitted long matching line]
paper/sections/introduction.tex:12:  \caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\approx$0.50; under AR generation ($N$\,=\,50), GAR collapses 7.8--16.7$\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause (9\% PPL cost at $\beta$\,=\,3).}
paper/sections/introduction.tex:16:[Omitted long matching line]
paper/sections/introduction.tex:18:Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\times$$\to$1.44$\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "a8797126-d341-49c7-a752-bd689c004804",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/analysis.tex:3:[Omitted long matching line]\npaper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.\npaper/sections/analysis.tex:16:  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}\npaper/sections/analysis.tex:39:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\npaper/sections/analysis.tex:41:\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\npaper/sections/analysis.tex:43:[Omitted long matching line]\npaper/sections/related_work.tex:4:[Omitted long matching line]\npaper/sections/related_work.tex:19:[Omitted long matching line]\npaper/sections/experiments.tex:34:LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\\scriptsize[.027,\\,.050]} & 1.00 \\\\\npaper/sections/experiments.tex:48:[Omitted long matching line]\npaper/sections/conclusion.tex:3:[Omitted long matching line]\npaper/sections/discussion.tex:3:The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\\times$ GAR magnitude) pushes gates toward identity (2--7\\% attenuation). Steering ($\\beta$\\,=\\,5) recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (\\S\\ref{subsec:steering}).\npaper/sections/abstract.tex:2:[Omitted long matching line]\npaper/sections/appendix.tex:152:Table~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\npaper/sections/appendix.tex:158:\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\npaper/sections/appendix.tex:178:\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\npaper/sections/appendix.tex:199:\\subsection{Cross-Model Gate Profile Comparison}\npaper/sections/appendix.tex:212:[Omitted long matching line]\npaper/sections/appendix.tex:247:[Omitted long matching line]\npaper/sections/appendix.tex:265:L24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\npaper/sections/appendix.tex:271:The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\npaper/sections/appendix.tex:273:\\paragraph{Cross-model comparison.} Llama-3.1-8B-Instruct (32 layers) shows a qualitatively different profile: a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809) rather than early-layer dips. Both architectures converge toward identity at output-adjacent layers, but the location of maximum attenuation differs---early for Qwen, late-middle for Llama---suggesting that layer importance hierarchies are architecture-dependent rather than universal.\npaper/sections/introduction.tex:3:Fine-tuned to allocate 50\\% of its attention to system-prompt goals (GAR\\,=\\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\\,=\\,0.064 under autoregressive generation---an 8$\\times$ collapse that widens to 27$\\times$ on Llama-3.1-8B. This paper traces the failure to exposure bias \\citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, even when next-token prediction (NTP) remains robust.\npaper/sections/introduction.tex:5:[Omitted long matching line]\npaper/sections/introduction.tex:12:  \\caption{Exposure bias selectively destroys auxiliary attention losses. (a)~Under TF evaluation, all fine-tuned variants converge to GAR-ours$\\approx$0.50; under AR generation ($N$\\,=\\,50), GAR collapses 7.8--16.7$\\times$. Log scale; dashed slopes connect paired TF-AR values. (b)~Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation---not representation degradation---as the proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3).}\npaper/sections/introduction.tex:16:[Omitted long matching line]\npaper/sections/introduction.tex:18:Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\\,=\\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\\times$$\\to$1.44$\\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.",
    "numLines": 27
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01VSrvg87AJMYZ5ZKjJd7nxp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "c36ac907-bb93-44d5-b9f2-6e43b54152ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0118k3ht9y5UvbaMPTNbWpir",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 30391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
      },
      "output_tokens": 61,
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

_source line 29 · 2026-05-23T14:41:44.041Z_

<details><summary>↩ Tool result · `toolu_01VSrvg87AJMYZ5ZKjJd7nxp`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B), one dataset (UltraChat, 8K conversations), and primarily a single seed (ThreadGate adds seed\,=\,123; the remaining variants rely on cross-variant convergence); the instruction retention analysis is exploratory (single model, single $\beta$). We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific attention losses may exhibit different sensitivity to exposure bias, and all variants share the same GAR objective, so we do not test whether gating could succeed under a different training signal. The PCGrad exclusion addresses gradient direction conflict only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium approaches \citep{navon2022nash} remain untested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "64d0af97-7fcd-42b1-b218-4a81325be445",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
      "content": "\\section{Limitations}\\label{sec:limitations}\n\nOur findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B), one dataset (UltraChat, 8K conversations), and primarily a single seed (ThreadGate adds seed\\,=\\,123; the remaining variants rely on cross-variant convergence); the instruction retention analysis is exploratory (single model, single $\\beta$). We test only one auxiliary loss family (GAR with MSE target $\\tau$\\,=\\,0.5); head-specific or layer-specific attention losses may exhibit different sensitivity to exposure bias, and all variants share the same GAR objective, so we do not test whether gating could succeed under a different training signal. The PCGrad exclusion addresses gradient direction conflict only; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibrium approaches \\citep{navon2022nash} remain untested.",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the analysis section and appendix for more context about SS data and cross-model data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "18d0dd81-6798-4e05-a765-3363cf70bd8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162rmcdkMbVAEnFkw2bAJjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3066,
      "cache_read_input_tokens": 31298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3066
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01U8THHDtyE7cS111QsoDTmP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "3ad5f155-28c2-445d-8bde-19e86e3ce427",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162rmcdkMbVAEnFkw2bAJjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3066,
      "cache_read_input_tokens": 31298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3066
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

_source line 32 · 2026-05-23T14:41:49.524Z_

<details><summary>↩ Tool result · `toolu_01U8THHDtyE7cS111QsoDTmP`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain---each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
10	
11	Inference-time gate values range from 0.93 to 0.98 (2--7\% attenuation), explaining the near-convergence in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the inversion (Appendix~\ref{sec:appendix-viz}). Does the NTP-GAR gradient conflict prevent the intended behavior? If so, resolving it should rescue gate conditioning.
12	
13	\begin{figure}[t]
14	  \centering
15	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig3_gate_shift.pdf}
16	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}
17	  \label{fig:gate-shift}
18	\end{figure}
19	
20	\subsection{PCGrad Gradient Conflict Exclusion}\label{subsec:pcgrad}
21	
22	NTP and GAR gradients oppose in 68--79\% of layers (mean cosine similarity $-$0.089 to $-$0.042), with NTP magnitude dominating 7.5--14.7$\times$. If this directional conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}---projecting conflicting gradients onto the other's normal plane---should prevent the collapse. We apply PCGrad to gate parameters only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium violations \citep{navon2022nash} remain untested.
23	
24	PCGrad shifts cosine similarity from consistently negative to oscillating around zero, yet TF metrics are unchanged (GAR-ours 0.50, PPL 2.78). AR GAR, however, \emph{worsens}: 0.064$\to$0.030 (Wilcoxon $p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b). By \emph{modus tollens}: if direction conflict causes the collapse, removing it should prevent it; PCGrad removes it; the collapse worsens; therefore direction conflict is not the cause. The 7.5--14.7$\times$ NTP magnitude dominance renders directional interference inconsequential. With gradient conflict excluded, the failure must occur at the training-to-inference transition.
25	
26	\begin{figure}[t]
27	  \centering
28	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
29	  \caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID GAR and PPL are unchanged; AR GAR worsens (0.064$\to$0.030), ruling out gradient conflict as the cause.}
30	  \label{fig:training-pcgrad}
31	\end{figure}
32	
33	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
34	
35	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: under standard training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \citep{bengio2015scheduled,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property of the prefix with no autoregressive counterpart. TF GAR-ours remains near $\tau$\,=\,0.5 (7--8\% decay; Figure~\ref{fig:attention-heatmap}), yet AR GAR collapses for all variants (Figure~\ref{fig:headline}a; Figure~\ref{fig:gate-shift}b shows the same pattern on 10-turn conversations with 20--33$\times$ gaps).
36	
37	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
38	
39	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
40	
41	\subsection{Cross-Model Replication}\label{subsec:cross-model}
42	
43	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (CoV\,$>$\,100\%), so we report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\times$ and 26$\times$. Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\times$ and 17$\times$ (outlier spikes inflate means; Appendix~\ref{sec:appendix-llama}). The gap is substantial on both architectures (8--17$\times$ on Qwen, 27$\times$ on Llama), consistent with exposure bias.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "2a60af3a-6401-4b9c-8ea3-1878fcce3948",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\\label{sec:analysis}\n\nThe five-way comparison (\\S\\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain---each subsection kills one alternative hypothesis: \\S\\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \\S\\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \\S\\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \\S\\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \\S\\ref{subsec:cross-model} confirms generalization across architectures.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nThe design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\\S\\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.\n\nThe gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.\n\nInference-time gate values range from 0.93 to 0.98 (2--7\\% attenuation), explaining the near-convergence in Table~\\ref{tab:four-way}. Figure~\\ref{fig:gate-shift}(a) visualizes the inversion (Appendix~\\ref{sec:appendix-viz}). Does the NTP-GAR gradient conflict prevent the intended behavior? If so, resolving it should rescue gate conditioning.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}\n  \\label{fig:gate-shift}\n\\end{figure}\n\n\\subsection{PCGrad Gradient Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (mean cosine similarity $-$0.089 to $-$0.042), with NTP magnitude dominating 7.5--14.7$\\times$. If this directional conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}---projecting conflicting gradients onto the other's normal plane---should prevent the collapse. We apply PCGrad to gate parameters only; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibrium violations \\citep{navon2022nash} remain untested.\n\nPCGrad shifts cosine similarity from consistently negative to oscillating around zero, yet TF metrics are unchanged (GAR-ours 0.50, PPL 2.78). AR GAR, however, \\emph{worsens}: 0.064$\\to$0.030 (Wilcoxon $p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b). By \\emph{modus tollens}: if direction conflict causes the collapse, removing it should prevent it; PCGrad removes it; the collapse worsens; therefore direction conflict is not the cause. The 7.5--14.7$\\times$ NTP magnitude dominance renders directional interference inconsequential. With gradient conflict excluded, the failure must occur at the training-to-inference transition.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID GAR and PPL are unchanged; AR GAR worsens (0.064$\\to$0.030), ruling out gradient conflict as the cause.}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: under standard training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys concentrated last-token attention while leaving diffuse attention unaffected. The mechanism is exposure bias \\citep{bengio2015scheduled,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. NTP self-recovers \\citep{he2019exposure} because prediction is the same task at both regimes; GAR optimizes a distributional property of the prefix with no autoregressive counterpart. TF GAR-ours remains near $\\tau$\\,=\\,0.5 (7--8\\% decay; Figure~\\ref{fig:attention-heatmap}), yet AR GAR collapses for all variants (Figure~\\ref{fig:headline}a; Figure~\\ref{fig:gate-shift}b shows the same pattern on 10-turn conversations with 20--33$\\times$ gaps).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only). TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (CoV\\,$>$\\,100\\%), so we report medians: 0.018 for both TG and LoRA-only (Base: 0.009), yielding TF-AR gaps of 27$\\times$ and 26$\\times$. Mean GAR-ours is 0.043 (TG) and 0.028 (LoRA-only), gaps of 11$\\times$ and 17$\\times$ (outlier spikes inflate means; Appendix~\\ref{sec:appendix-llama}). The gap is substantial on both architectures (8--17$\\times$ on Qwen, 27$\\times$ on Llama), consistent with exposure bias.",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01TuwoBuAskv9esNenGCEua9`</summary>

```json
{
  "pattern": "0\\.347|0\\.418|scheduled sampling|SS |seed 123|seed.?42|\\\\pm",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "2e58140d-1c30-48a8-ad48-1895c6625976",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162rmcdkMbVAEnFkw2bAJjU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3066,
      "cache_read_input_tokens": 31298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3066
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

_source line 34 · 2026-05-23T14:41:51.905Z_

<details><summary>↩ Tool result · `toolu_01TuwoBuAskv9esNenGCEua9`</summary>

```text
paper/sections/analysis.tex:3:[Omitted long matching line]
paper/sections/analysis.tex:7:The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
paper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
paper/sections/analysis.tex:16:  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}
paper/sections/analysis.tex:35:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:[Omitted long matching line]
paper/sections/related_work.tex:13:[Omitted long matching line]
paper/sections/related_work.tex:19:[Omitted long matching line]
paper/sections/experiments.tex:6:[Omitted long matching line]
paper/sections/experiments.tex:10:Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\to$${\sim}$0.50). Convergence near $\tau$\,=\,0.5 is expected given the shared GAR loss and does not demonstrate gating benefit. GAR-Dongre remains low (0.01--0.02); scheduled sampling breaks this pattern (\S\ref{sec:discussion}).
paper/sections/experiments.tex:12:Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). ThreadGate significantly outperforms LoRA-only (Wilcoxon $p$\,=\,0.004, $r$\,=\,0.454; GAR-ours 0.064 vs 0.037; Appendix~\ref{sec:appendix-stats}), yet the residual gap remains large (7.8$\times$). A second seed (123) confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
paper/sections/experiments.tex:17:\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
paper/sections/experiments.tex:23:\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
paper/sections/experiments.tex:29:ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
paper/sections/experiments.tex:31:Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
paper/sections/experiments.tex:42:  \caption{Per-turn GAR-ours under TF evaluation ($N$\,=\,45, $\pm$1\,std). Fine-tuned variants maintain GAR near $\tau$\,=\,0.5 (7--8\% decay T1$\to$T4); Base decays 80\%. AR GAR collapses to 0.019--0.064 for all variants (Table~\ref{tab:four-way}).}
paper/sections/experiments.tex:48:[Omitted long matching line]
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/discussion.tex:5:[Omitted long matching line]
paper/sections/method.tex:36:\paragraph{Initialization.} Gate biases are set to 1.5 (${\sim}$82\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\times$ learning rate multiplier.
paper/sections/method.tex:44:$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. The GAR loss targets a fixed attention level to goal tokens:
paper/sections/method.tex:48:where $\tau = 0.5$. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). The gate diversity loss prevents collapse to a uniform value:
paper/sections/method.tex:54:\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.
paper/sections/limitations.tex:3:[Omitted long matching line]
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/appendix.tex:3:[Omitted long matching line]
paper/sections/appendix.tex:35:\section{Loss Formulation Search}\label{sec:appendix-loss}
paper/sections/appendix.tex:37:The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
paper/sections/appendix.tex:39:\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
paper/sections/appendix.tex:43:\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
paper/sections/appendix.tex:45:\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
paper/sections/appendix.tex:49:\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
paper/sections/appendix.tex:53: & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
paper/sections/appendix.tex:55:v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
paper/sections/appendix.tex:60:v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
paper/sections/appendix.tex:68:To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').
paper/sections/appendix.tex:70:Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.
paper/sections/appendix.tex:118:[Omitted long matching line]
paper/sections/appendix.tex:138:SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
paper/sections/appendix.tex:178:\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
paper/sections/appendix.tex:180:\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger intermediate dimension (14336 vs.\ 18944).
paper/sections/appendix.tex:190:[Omitted long matching line]
paper/sections/appendix.tex:195:\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
paper/sections/appendix.tex:212:[Omitted long matching line]
paper/sections/appendix.tex:217:\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
paper/sections/appendix.tex:223:Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
paper/sections/appendix.tex:232:\subsection{Training Loss Curves}
paper/sections/appendix.tex:234:[Omitted long matching line]
paper/sections/appendix.tex:239:\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
paper/sections/appendix.tex:247:[Omitted long matching line]
paper/sections/appendix.tex:251:\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
paper/sections/appendix.tex:271:The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
paper/sections/appendix.tex:275:\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
paper/sections/appendix.tex:277:Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
paper/sections/appendix.tex:283:[Omitted long matching line]
paper/sections/appendix.tex:289:\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\,GB VRAM).}
paper/sections/appendix.tex:301:SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
paper/sections/appendix.tex:302:SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
paper/sections/appendix.tex:311:\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
paper/sections/appendix.tex:313:\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$20\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
paper/sections/appendix.tex:315:\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
paper/sections/appendix.tex:323:\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
paper/sections/introduction.tex:5:[Omitted long matching line]
paper/sections/introduction.tex:16:[Omitted long matching line]
paper/sections/introduction.tex:18:Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\,=\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\times$$\to$1.44$\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "00792989-86a1-4354-be96-6714639e7bf6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/analysis.tex:3:[Omitted long matching line]\npaper/sections/analysis.tex:7:The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\\S\\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.\npaper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.\npaper/sections/analysis.tex:16:  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}\npaper/sections/analysis.tex:35:[Omitted long matching line]\npaper/sections/related_work.tex:4:[Omitted long matching line]\npaper/sections/related_work.tex:7:[Omitted long matching line]\npaper/sections/related_work.tex:13:[Omitted long matching line]\npaper/sections/related_work.tex:19:[Omitted long matching line]\npaper/sections/experiments.tex:6:[Omitted long matching line]\npaper/sections/experiments.tex:10:Table~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\\to$${\\sim}$0.50). Convergence near $\\tau$\\,=\\,0.5 is expected given the shared GAR loss and does not demonstrate gating benefit. GAR-Dongre remains low (0.01--0.02); scheduled sampling breaks this pattern (\\S\\ref{sec:discussion}).\npaper/sections/experiments.tex:12:Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}a). ThreadGate significantly outperforms LoRA-only (Wilcoxon $p$\\,=\\,0.004, $r$\\,=\\,0.454; GAR-ours 0.064 vs 0.037; Appendix~\\ref{sec:appendix-stats}), yet the residual gap remains large (7.8$\\times$). A second seed (123) confirms TF stability ($0.504\\pm0.001$). We analyze this distribution shift in \\S\\ref{sec:analysis}.\npaper/sections/experiments.tex:17:\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\\,=\\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\\leq$2\\,pp spread); the 8--17$\\times$ TF-AR gap persists across all configurations. $\\bar{g}\\!\\pm\\!\\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\npaper/sections/experiments.tex:23:\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\\% CI & $\\bar{g}\\!\\pm\\!\\sigma_g$ \\\\\npaper/sections/experiments.tex:29:ThreadGate        & 0.50 & \\textbf{0.02} & 2.78 & 0.50 & \\textbf{0.02} & 2.78 & \\textbf{0.064} & {\\scriptsize[.041,\\,.091]} & .93\\,{\\scriptsize$\\pm$\\,.05} \\\\\npaper/sections/experiments.tex:31:Uniform Gate      & 0.49 & 0.01 & 2.78 & \\textbf{0.51} & 0.01 & 2.78 & 0.033 & {\\scriptsize[.025,\\,.043]} & .96\\,{\\scriptsize$\\pm$\\,.05} \\\\\npaper/sections/experiments.tex:42:  \\caption{Per-turn GAR-ours under TF evaluation ($N$\\,=\\,45, $\\pm$1\\,std). Fine-tuned variants maintain GAR near $\\tau$\\,=\\,0.5 (7--8\\% decay T1$\\to$T4); Base decays 80\\%. AR GAR collapses to 0.019--0.064 for all variants (Table~\\ref{tab:four-way}).}\npaper/sections/experiments.tex:48:[Omitted long matching line]\npaper/sections/conclusion.tex:3:[Omitted long matching line]\npaper/sections/discussion.tex:5:[Omitted long matching line]\npaper/sections/method.tex:36:\\paragraph{Initialization.} Gate biases are set to 1.5 (${\\sim}$82\\% pass-through), contrasting ReZero's zero initialization that would suppress pretrained capabilities. Gate parameters receive a $10\\times$ learning rate multiplier.\npaper/sections/method.tex:44:$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. The GAR loss targets a fixed attention level to goal tokens:\npaper/sections/method.tex:48:where $\\tau = 0.5$. GAR is measured at the last token of each assistant turn (GAR-ours, \\S\\ref{sec:background}). The gate diversity loss prevents collapse to a uniform value:\npaper/sections/method.tex:54:\\paragraph{Loss design evolution.} The MSE formulation was selected from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity. Only MSE provides bidirectional pressure---penalizing both over- and under-attention---preventing identity collapse.\npaper/sections/limitations.tex:3:[Omitted long matching line]\npaper/sections/abstract.tex:2:[Omitted long matching line]\npaper/sections/appendix.tex:3:[Omitted long matching line]\npaper/sections/appendix.tex:35:\\section{Loss Formulation Search}\\label{sec:appendix-loss}\npaper/sections/appendix.tex:37:The final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\npaper/sections/appendix.tex:39:\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\npaper/sections/appendix.tex:43:\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\npaper/sections/appendix.tex:45:\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\npaper/sections/appendix.tex:49:\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\npaper/sections/appendix.tex:53: & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\npaper/sections/appendix.tex:55:v1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\npaper/sections/appendix.tex:60:v6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\npaper/sections/appendix.tex:68:To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').\npaper/sections/appendix.tex:70:Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.\npaper/sections/appendix.tex:118:[Omitted long matching line]\npaper/sections/appendix.tex:138:SS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\npaper/sections/appendix.tex:178:\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\npaper/sections/appendix.tex:180:\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger intermediate dimension (14336 vs.\\ 18944).\npaper/sections/appendix.tex:190:[Omitted long matching line]\npaper/sections/appendix.tex:195:\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\npaper/sections/appendix.tex:212:[Omitted long matching line]\npaper/sections/appendix.tex:217:\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\npaper/sections/appendix.tex:223:Figure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\npaper/sections/appendix.tex:232:\\subsection{Training Loss Curves}\npaper/sections/appendix.tex:234:[Omitted long matching line]\npaper/sections/appendix.tex:239:\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\npaper/sections/appendix.tex:247:[Omitted long matching line]\npaper/sections/appendix.tex:251:\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\npaper/sections/appendix.tex:271:The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\npaper/sections/appendix.tex:275:\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\npaper/sections/appendix.tex:277:Our scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\npaper/sections/appendix.tex:283:[Omitted long matching line]\npaper/sections/appendix.tex:289:\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\\,GB VRAM).}\npaper/sections/appendix.tex:301:SS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\npaper/sections/appendix.tex:302:SS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\npaper/sections/appendix.tex:311:\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\npaper/sections/appendix.tex:313:\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\\sim}$20\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\npaper/sections/appendix.tex:315:\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\npaper/sections/appendix.tex:323:\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\npaper/sections/introduction.tex:5:[Omitted long matching line]\npaper/sections/introduction.tex:16:[Omitted long matching line]\npaper/sections/introduction.tex:18:Our contributions: (1)~first empirical measurement of exposure bias on auxiliary attention losses (8--27$\\times$ across two architectures); (2)~PCGrad-based causal exclusion of gradient conflict ($p$\\,=\\,0.002, effect reverses); (3)~first evidence that scheduled sampling transfers to multi-turn transformer attention objectives (gap 7.8$\\times$$\\to$1.44$\\times$); (4)~cross-architecture validation on Llama-3.1-8B confirming generalization.",
    "numLines": 66
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the appendix for SS-related data and any other sections that might have placeholders.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "31780e06-41fc-4d0c-b6b6-43749a9d38f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYge6FxW8HaxHTvC3ogwqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6978,
      "cache_read_input_tokens": 34364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6978
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01RpTfqE8cvAdovCteSK3fpy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "5f157a20-b0de-4b65-b3ec-904a1a7c3ec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYge6FxW8HaxHTvC3ogwqu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6978,
      "cache_read_input_tokens": 34364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6978
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

### Tool result

_source line 37 · 2026-05-23T14:42:02.211Z_

<details><summary>↩ Tool result · `toolu_01RpTfqE8cvAdovCteSK3fpy`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (102\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').
69	
70	Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.
71	
72	The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
73	
74	\begin{table}[h]
75	\centering\small
76	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
77	\label{tab:ir-results}
78	\begin{tabular}{lccc}
79	\toprule
80	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
81	\midrule
82	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
83	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
84	Count      & 100\%  & 100\%  & 0 \\
85	Format     & 100\%  & 100\%  & 0 \\
86	\midrule
87	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
88	\bottomrule
89	\end{tabular}
90	\end{table}
91	
92	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
93	
94	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each. In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. This length dependence is consistent with exposure bias compounding over turns---each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn 10 the accumulated drift overwhelms any gating signal.
95	
96	\begin{table}[h]
97	\centering\small
98	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
99	\label{tab:n5-ar}
100	\begin{tabular}{lcc}
101	\toprule
102	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
103	\midrule
104	Base & 0.012 & $-$0.007 \\
105	\midrule
106	ThreadGate & 0.016 & $-$0.048 \\
107	\;+\,PCGrad & 0.015 & $-$0.015 \\
108	Uniform Gate & 0.015 & $-$0.018 \\
109	LoRA-only & 0.025 & $-$0.012 \\
110	\bottomrule
111	\end{tabular}
112	\end{table}
113	
114	\section{Statistical Test Details}\label{sec:appendix-stats}
115	
116	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
117	
118	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
119	
120	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
121	
122	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
123	
124	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
125	
126	\begin{table}[h]
127	\centering\small
128	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
129	\label{tab:stat-tests}
130	\begin{tabular}{llcc}
131	\toprule
132	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
133	\midrule
134	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
135	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
136	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
137	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
138	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
139	\midrule
140	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
141	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
142	\midrule
143	\multicolumn{4}{l}{\emph{Instruction retention}} \\
144	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
145	GAR--compliance & Pearson & 0.007 & 0.200 \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
151	
152	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
153	
154	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
155	
156	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
157	
158	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
159	
160	\begin{table}[h]
161	\centering\small
162	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20, mid-turn). Median is more representative due to heavy-tailed AR distributions.}
163	\label{tab:llama-full}
164	\resizebox{\columnwidth}{!}{%
165	\begin{tabular}{lcccc}
166	\toprule
167	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
170	\midrule
171	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
172	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
173	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
174	\bottomrule
175	\end{tabular}}
176	\end{table}
177	
178	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
179	
180	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger intermediate dimension (14336 vs.\ 18944).
181	
182	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
183	
184	\section{Additional Visualizations}\label{sec:appendix-viz}
185	
186	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
187	
188	\subsection{Gate Profile Heatmap}
189	
190	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
191	
192	\begin{figure*}[h]
193	\centering
194	\includegraphics[width=0.95\textwidth]{fig_gate_profile_heatmap.pdf}
195	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
196	\label{fig:gate-heatmap}
197	\end{figure*}
198	
199	\subsection{Cross-Model Gate Profile Comparison}
200	
201	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
202	
203	\begin{figure*}[h]
204	\centering
205	\includegraphics[width=0.95\textwidth]{fig_gate_profile_crossmodel.pdf}
206	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
207	\label{fig:gate-crossmodel}
208	\end{figure*}
209	
210	\subsection{Per-Turn AR GAR Decay}
211	
212	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
213	
214	\begin{figure*}[h]
215	\centering
216	\includegraphics[width=0.95\textwidth]{fig_ar_gar_perturn.pdf}
217	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
218	\label{fig:ar-gar-perturn}
219	\end{figure*}
220	
221	\subsection{Gate Value Distributions}
222	
223	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
224	
225	\begin{figure*}[h]
226	\centering
227	\includegraphics[width=0.95\textwidth]{fig_gate_distribution.pdf}
228	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
229	\label{fig:gate-distribution}
230	\end{figure*}
231	
232	\subsection{Training Loss Curves}
233	
234	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
235	
236	\begin{figure*}[h]
237	\centering
238	\includegraphics[width=0.95\textwidth]{fig_training_loss_curves.pdf}
239	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
240	\label{fig:training-loss}
241	\end{figure*}
242	
243	\input{../artifacts/table_steering_full}
244	
245	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
246	
247	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
248	
249	\begin{table}[h]
250	\centering\small
251	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
252	\label{tab:gate-profile}
253	\resizebox{\columnwidth}{!}{%
254	\begin{tabular}{cccccccc}
255	\toprule
256	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
257	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
258	\midrule
259	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
260	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
261	\midrule
262	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
263	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
264	\midrule
265	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
266	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
267	\bottomrule
268	\end{tabular}}
269	\end{table}
270	
271	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
272	
273	\paragraph{Cross-model comparison.} Llama-3.1-8B-Instruct (32 layers) shows a qualitatively different profile: a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809) rather than early-layer dips. Both architectures converge toward identity at output-adjacent layers, but the location of maximum attenuation differs---early for Qwen, late-middle for Llama---suggesting that layer importance hierarchies are architecture-dependent rather than universal.
274	
275	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
276	
277	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
278	
279	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.5 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
280	
281	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
282	
283	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases approximately 60\% due to the autoregressive generation overhead during training (6.5h vs.\ 6.0h on Qwen; 10.8h for the seed-123 variant which uses a longer schedule).
284	
285	\section{Computational Cost Analysis}\label{sec:appendix-cost}
286	
287	\begin{table}[h]
288	\centering\small
289	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\,GB VRAM).}
290	\label{tab:cost}
291	\resizebox{\columnwidth}{!}{%
292	\begin{tabular}{lcccc}
293	\toprule
294	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
295	\midrule
296	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
297	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
298	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
299	\;+\,PCGrad & 4.3M & 7.2 & 43\,GB & $+$20\% \\
300	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
301	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
302	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
303	\midrule
304	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
305	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
306	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
307	\bottomrule
308	\end{tabular}}
309	\end{table}
310	
311	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
312	
313	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$20\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
314	
315	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
316	
317	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
318	
319	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
320	
321	\begin{table*}[h]
322	\centering\small
323	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
324	\label{tab:examples}
325	\begin{tabular}{c p{5.5cm} p{5.5cm}}
326	\toprule
327	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
328	\midrule
329	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
330	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
331	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
332	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
333	\bottomrule
334	\end{tabular}
335	\end{table*}
336	
337	The pattern is consistent with the GAR decay analysis: unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. Content constraints (e.g., ``never mention X'') show the largest improvement (+23.8\,pp at $\beta$\,=\,3; Table~\ref{tab:ir-results}), while format constraints that are more procedural show no change, consistent with the hypothesis that GAR captures attention to semantic goal content rather than procedural formatting rules.
338	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "ff066237-5218-41dc-afe7-5a50f5e6dc09",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (102\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end'').\n\nTable~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. Format and count constraints, which are more procedural and less dependent on sustained attention to the system prompt, show no change.\n\nThe GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:four-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each. In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. This length dependence is consistent with exposure bias compounding over turns---each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn 10 the accumulated drift overwhelms any gating signal.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:four-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:four-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20, mid-turn). Median is more representative due to heavy-tailed AR distributions.}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger intermediate dimension (14336 vs.\\ 18944).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure*}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure*}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure*}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure*}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure*}\n\n\\input{../artifacts/table_steering_full}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} Llama-3.1-8B-Instruct (32 layers) shows a qualitatively different profile: a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809) rather than early-layer dips. Both architectures converge toward identity at output-adjacent layers, but the location of maximum attenuation differs---early for Qwen, late-middle for Llama---suggesting that layer importance hierarchies are architecture-dependent rather than universal.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.5 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing. Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases approximately 60\\% due to the autoregressive generation overhead during training (6.5h vs.\\ 6.0h on Qwen; 10.8h for the seed-123 variant which uses a longer schedule).\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (102\\,GB VRAM).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 6.0 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 7.2 & 43\\,GB & $+$20\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\\sim}$20\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[h]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis: unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. Content constraints (e.g., ``never mention X'') show the largest improvement (+23.8\\,pp at $\\beta$\\,=\\,3; Table~\\ref{tab:ir-results}), while format constraints that are more procedural show no change, consistent with the hypothesis that GAR captures attention to semantic goal content rather than procedural formatting rules.\n",
      "numLines": 338,
      "startLine": 1,
      "totalLines": 338
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper. Let me also check the SS-related discussion data more carefully. The discussion mentions SS GAR values of 0.347 and 0.418. Let me check if these are labeled as single seed.

Let me now compile the placeholder list. Key things to look for:

1. **SS (Scheduled Sampling) data** - Currently only single seed values:
   - discussion.tex L5: "0.347" (single seed s42), "0.418" (single seed s123) 
   - These are individual seed values, not mean±std from 3 seeds


2. **"single seed" mentions** - Found scattered across abstract.tex, conclusion.tex, and limitations.tex, all referring to scheduled sampling results and gap measurements
3. **1.5B cross-model data** - Not found anywhere in the tex files
4. **MMLU data** - Also absent from the files
5. I should check if there's specific data that should have ±std but doesn't

Now I'm seeing the real issue in discussion.tex — several key results are reported from single seeds or very limited runs. The AR GAR-ours improvement from 0.064 to 0.347 is just from seed s42, with a second seed at s123 showing 0.418, and GAR-Dongre only tested with N=5. These should all be reported as mean±std across 3 seeds instead. The 1.44× gap cited in the abstract and introduction traces back to that single s42 seed calculation, so those sections need updating with proper multi-seed results.

Looking at the experiments table, the main results appear to use seed 42 for most methods except ThreadGate which has a second seed, but I need to determine whether the primary table itself requires multi-seed reporting or if that's only needed for the scheduled sampling results being highlighted in the text.

Scanning through the grep results, I found explicit "single seed" markers in the abstract, limitations, and conclusion sections, but no TODO or FIXME tags in the tex files themselves. So my task is to identify all the places needing updates: the explicit "single seed" callouts, any scheduled sampling numbers that show individual seed values instead of aggregated statistics, the missing 1.5B and MMLU data points, and any other metrics that should have uncertainty estimates attached.

Going through each file systematically, the abstract has that 1.44× figure marked as single seed, the introduction references several single-seed results including the 27× Llama number and the 7.8×→1.44× gap, and the experiments section shows the main table only used seed 42 for most variants with a second seed 123 added just for ThreadGate.

Looking more carefully at what the user specified — they mention SS currently only has single seed s42 data — but the discussion section actually shows both s42 (0.347) and s123 (0.418) for SS. So there are two seeds available for SS, though the user wants three-seed mean±std. For the main table's AR results, everything except TF is single seed s42, and only TF has confirmation with seed 123.

Now I need to identify exactly which numbers need updating: SS needs the three-seed aggregation, there's no 1.5B cross-model data yet, MMLU is missing, and bootstrap confidence intervals are needed. Let me compile what's actually available from the paper and what gaps remain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "593860b3-4c18-4070-89f9-c378386e464d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAa8eoMcBr2srcVLMqpmyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9947,
      "cache_read_input_tokens": 41342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9947
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

_source line 39_

Now let me check whether 1.5B or MMLU are mentioned anywhere, and also look at the ROADMAP for what experiments are planned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "9259f210-09b7-4465-b0b0-9b29322737e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAa8eoMcBr2srcVLMqpmyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9947,
      "cache_read_input_tokens": 41342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9947
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

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01ALpqqF3B56MW96NptsdQ1Q`</summary>

```json
{
  "pattern": "1\\.5B|1\\.5b|MMLU|mmlu",
  "-i": true,
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "ed8fb8eb-c3c5-4fe0-a5a9-879749554193",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAa8eoMcBr2srcVLMqpmyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9947,
      "cache_read_input_tokens": 41342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9947
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

_source line 41 · 2026-05-23T14:42:49.298Z_

<details><summary>↩ Tool result · `toolu_01ALpqqF3B56MW96NptsdQ1Q`</summary>

```text
paper/sections/related_work.tex:13:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "c6f5d6f6-69fe-41cd-a2ff-ee1d6f229cab",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/related_work.tex:13:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01Vvcq2W9EktesNo2QmSKo4R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "6e68379e-41ee-4e63-a8ff-532dea727647",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAa8eoMcBr2srcVLMqpmyN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9947,
      "cache_read_input_tokens": 41342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9947
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

_source line 43 · 2026-05-23T14:42:49.714Z_

<details><summary>↩ Tool result · `toolu_01Vvcq2W9EktesNo2QmSKo4R`</summary>

```text
1	# turn_residual_gating — Research Dashboard
2	
3	> 最后更新: 2026-05-22 16:57 UTC | 更新原因: DDL 修正 5/25 + 今日大量工作完成反映 + 写作线收尾
4	
5	## 核心方向
6	Diagnostic framework: lightweight residual gating 的 auxiliary attention loss 在 text distribution shift (exposure bias) 下泛化失败（~31× gap）。PCGrad 排除梯度方向冲突。**双路 mitigation 已验证**：inference-time attention steering (β=5, GAR 0.064→0.727, N=50) + training-time scheduled sampling (GAR 0.016→0.318, gap → 1.57×, PPL 不变)。**跨模型泛化确认**：Llama-3.1-8B gap 27× (median, N=20)。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: D048 修复 + 提交准备（**DDL: ARR May 2026-05-25，剩余 3 天**）
10	- **核心 claim**: C1✅ C2✅ C3✅ C4✅ C5✅ C6✅(N=50) C7✅(dual-seed)
11	- **成功率**: 27 success / 5 negative / 3 failed / 37 total
12	- **审稿**: Group C Round 3 Overall 3.0 (Findings)，目标 3.5 (Conference)
13	- **写作**: Round 3 全部 13 项修复完成，主文 8 页，编译 0 error
14	- **附录**: Appendix A-D 完整（超参/loss iterations/instruction retention/可视化 6 图表）
15	- **论文编译**: 14 页 0 error 0 undefined ref
16	
17	## 近期任务
18	
19	### 实验线（GPU 串行，westd-20861:cuda:0）
20	- [ ] **SS s42 训练** — resume v3 运行中，epoch 1-2，预计 ~20:00 UTC 完成
21	- [ ] **SS s42 eval** — TF + AR N=50 + bootstrap CI（训练完成后立即执行，~1h）
22	- [ ] **AR N=50 existing** — TG/UG/PCGrad/LO 4 条件扩容（~8h）
23	- [ ] **SS s123 + s456 训练+eval** — 各 ~5h+1h
24	- [ ] **Base/TG multi-seed** — s123/s456 各 ~5h+1h
25	- [ ] ~~GradNorm~~ / ~~Llama PCGrad+UG~~ / ~~N=200~~ — 如时间允许
26	
27	### 写作线（已基本完成）
28	- [x] Round 3 全部 13 项写作修复（GAR 命名/Rhea/贡献措辞/PCGrad scope/页数/Discussion 压缩等）
29	- [x] Appendix D: 6 个可视化（gate heatmap/cross-model/AR GAR decay/gate distribution/loss curves/β-steering table）
30	- [x] Table 2 扩展 Failure Mechanism 列
31	- [x] 图片同步 + 编译验证（14 页 0 error）
32	- [ ] Abstract/Intro/Conclusion 数字更新为 mean±std（等 multi-seed 数据）
33	
34	### 提交准备
35	- [ ] Multi-seed 数字更新论文
36	- [ ] 最终编译 + 视觉审查
37	- [ ] Round 4 Group C 审稿
38	- [ ] 5/25 提交 ARR May
39	
40	## GPU 预算
41	- **已分配**: westd-20861:cuda:0 (1×RTX PRO 6000 Blackwell, 102GB)
42	- **当前**: SS s42 resume v3 训练中
43	- **累计 GPU 时间**: ~160h
44	- **D048 剩余预估**: ~55h（SS eval 1h + AR N=50 8h + SS s123/s456 12h + Base/TG multi-seed 20h + 其余 ~14h）
45	- **GPU 扩容**: 用户确认"单卡跑就行"，不再追加
46	
47	## 风险监控
48	- **DDL 紧张**: 72h 内需完成必做实验（SS 3-seed + AR N=50）+ 论文数字更新
49	- **SS variance 风险**: 3-seed CoV>50% → 降为 promising-but-unstable
50	- **SS s42 已中断 2 次**: OOM (M023) + SSH 断连 (M024)，第 3 次启动已稳定（tmux+log+验证）
51	
52	## 关键决策日志
53	
54	| ID | 日期 | 摘要 | 关联实验 |
55	|----|------|------|----------|
56	| D050 | 2026-05-23 | Table 1 切换到 eval_200 N=50 数据，叙事从 "zero benefit" 调整 | d048_final_ar_eval, d048_eval_ss_s42 |
57	| D049 | 2026-05-22 | D049: Round 3 审稿报告 Action Matrix——不降级 SS contribut | — |
58	| D048 | 2026-05-22 | D048: Group C Round 2 审稿 3.0 修复计划——multi-seed 5 条件 | phase2_tg_s42_v7, phase2_tg_s42_v8b_resume, eval_llama_ar_n20, phase2_tg_s42_v9_pcgrad, instruction_retention_test |
59	| D047 | 2026-05-22 | D047: mid_turns 定义接受 turns 3-T（代码实际），论文措辞修正 defer  | eval_llama_ar_n20 |
60	| D046 | 2026-05-21 | W3 instruction retention test 确认 GAR → downstream  | instruction_retention_test |
61	| D045 | 2026-05-21 | C5 跨模型泛化从 preliminary 升级为 confirmed；Llama TG gap 1 | llama_tg_s42, llama_eval_s42, llama_phase1_gar_diag |
62	| D044 | 2026-05-21 | 加入 P0 instruction retention test (β-steering) 解决 W | attention_steering_gen_n50, phase2_tg_s42_v7 |
63	| D043 | 2026-05-20 | D043: Ablation 优先级精简——删除 P5 Base TRC rerun，Plan_02 | llama_tg_training, phase2_tg_s42_v8b_ss_fixed |
64	| D042 | 2026-05-20 | C5 跨模型泛化确认：Llama-3.1-8B 展现与 Qwen-2.5-7B 相同的 GAR 单调 | llama_phase1_gar_diag, attention_steering_gen_n50 |
65	| D041 | 2026-05-20 | D041: v8b SS SUCCESS — GAR-ours 0.016→0.318 (20×), | phase2_tg_s42_v8b_ss_fixed, phase2_tg_s42_v7 |
66	
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "a86c19bd-f610-479f-b9f3-1fe6487acece",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md",
      "content": "# turn_residual_gating — Research Dashboard\n\n> 最后更新: 2026-05-22 16:57 UTC | 更新原因: DDL 修正 5/25 + 今日大量工作完成反映 + 写作线收尾\n\n## 核心方向\nDiagnostic framework: lightweight residual gating 的 auxiliary attention loss 在 text distribution shift (exposure bias) 下泛化失败（~31× gap）。PCGrad 排除梯度方向冲突。**双路 mitigation 已验证**：inference-time attention steering (β=5, GAR 0.064→0.727, N=50) + training-time scheduled sampling (GAR 0.016→0.318, gap → 1.57×, PPL 不变)。**跨模型泛化确认**：Llama-3.1-8B gap 27× (median, N=20)。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: D048 修复 + 提交准备（**DDL: ARR May 2026-05-25，剩余 3 天**）\n- **核心 claim**: C1✅ C2✅ C3✅ C4✅ C5✅ C6✅(N=50) C7✅(dual-seed)\n- **成功率**: 27 success / 5 negative / 3 failed / 37 total\n- **审稿**: Group C Round 3 Overall 3.0 (Findings)，目标 3.5 (Conference)\n- **写作**: Round 3 全部 13 项修复完成，主文 8 页，编译 0 error\n- **附录**: Appendix A-D 完整（超参/loss iterations/instruction retention/可视化 6 图表）\n- **论文编译**: 14 页 0 error 0 undefined ref\n\n## 近期任务\n\n### 实验线（GPU 串行，westd-20861:cuda:0）\n- [ ] **SS s42 训练** — resume v3 运行中，epoch 1-2，预计 ~20:00 UTC 完成\n- [ ] **SS s42 eval** — TF + AR N=50 + bootstrap CI（训练完成后立即执行，~1h）\n- [ ] **AR N=50 existing** — TG/UG/PCGrad/LO 4 条件扩容（~8h）\n- [ ] **SS s123 + s456 训练+eval** — 各 ~5h+1h\n- [ ] **Base/TG multi-seed** — s123/s456 各 ~5h+1h\n- [ ] ~~GradNorm~~ / ~~Llama PCGrad+UG~~ / ~~N=200~~ — 如时间允许\n\n### 写作线（已基本完成）\n- [x] Round 3 全部 13 项写作修复（GAR 命名/Rhea/贡献措辞/PCGrad scope/页数/Discussion 压缩等）\n- [x] Appendix D: 6 个可视化（gate heatmap/cross-model/AR GAR decay/gate distribution/loss curves/β-steering table）\n- [x] Table 2 扩展 Failure Mechanism 列\n- [x] 图片同步 + 编译验证（14 页 0 error）\n- [ ] Abstract/Intro/Conclusion 数字更新为 mean±std（等 multi-seed 数据）\n\n### 提交准备\n- [ ] Multi-seed 数字更新论文\n- [ ] 最终编译 + 视觉审查\n- [ ] Round 4 Group C 审稿\n- [ ] 5/25 提交 ARR May\n\n## GPU 预算\n- **已分配**: westd-20861:cuda:0 (1×RTX PRO 6000 Blackwell, 102GB)\n- **当前**: SS s42 resume v3 训练中\n- **累计 GPU 时间**: ~160h\n- **D048 剩余预估**: ~55h（SS eval 1h + AR N=50 8h + SS s123/s456 12h + Base/TG multi-seed 20h + 其余 ~14h）\n- **GPU 扩容**: 用户确认\"单卡跑就行\"，不再追加\n\n## 风险监控\n- **DDL 紧张**: 72h 内需完成必做实验（SS 3-seed + AR N=50）+ 论文数字更新\n- **SS variance 风险**: 3-seed CoV>50% → 降为 promising-but-unstable\n- **SS s42 已中断 2 次**: OOM (M023) + SSH 断连 (M024)，第 3 次启动已稳定（tmux+log+验证）\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D050 | 2026-05-23 | Table 1 切换到 eval_200 N=50 数据，叙事从 \"zero benefit\" 调整 | d048_final_ar_eval, d048_eval_ss_s42 |\n| D049 | 2026-05-22 | D049: Round 3 审稿报告 Action Matrix——不降级 SS contribut | — |\n| D048 | 2026-05-22 | D048: Group C Round 2 审稿 3.0 修复计划——multi-seed 5 条件 | phase2_tg_s42_v7, phase2_tg_s42_v8b_resume, eval_llama_ar_n20, phase2_tg_s42_v9_pcgrad, instruction_retention_test |\n| D047 | 2026-05-22 | D047: mid_turns 定义接受 turns 3-T（代码实际），论文措辞修正 defer  | eval_llama_ar_n20 |\n| D046 | 2026-05-21 | W3 instruction retention test 确认 GAR → downstream  | instruction_retention_test |\n| D045 | 2026-05-21 | C5 跨模型泛化从 preliminary 升级为 confirmed；Llama TG gap 1 | llama_tg_s42, llama_eval_s42, llama_phase1_gar_diag |\n| D044 | 2026-05-21 | 加入 P0 instruction retention test (β-steering) 解决 W | attention_steering_gen_n50, phase2_tg_s42_v7 |\n| D043 | 2026-05-20 | D043: Ablation 优先级精简——删除 P5 Base TRC rerun，Plan_02 | llama_tg_training, phase2_tg_s42_v8b_ss_fixed |\n| D042 | 2026-05-20 | C5 跨模型泛化确认：Llama-3.1-8B 展现与 Qwen-2.5-7B 相同的 GAR 单调 | llama_phase1_gar_diag, attention_steering_gen_n50 |\n| D041 | 2026-05-20 | D041: v8b SS SUCCESS — GAR-ours 0.016→0.318 (20×), | phase2_tg_s42_v8b_ss_fixed, phase2_tg_s42_v7 |\n\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile the full placeholder list.

Key findings:

1. **SS data is single-seed (s42) in discussion, with s123 also mentioned, but needs 3-seed mean±std** — The ROADMAP confirms SS s123/s456 are pending
2. **"single seed" explicit markers** in abstract, conclusion, limitations
3. **No 1.5B data** — not mentioned in paper at all, only in related_work.tex in passing
4. **No MMLU data** — not mentioned in paper at all
5. **Main table AR data is single-seed s42** — ROADMAP says "Base/TG multi-seed s123/s456" pending


6. **No TODO/XXX/FIXME markers** found anywhere

I don't see any plans for 1.5B experiments in the ROADMAP or paper itself, so that's likely something that was considered but not pursued. Now I need to map out which specific datasets are single-seed versus multi-seed across the main results.

Looking at the AR data in Table 1, all the methods show bootstrap confidence intervals from a single seed run. The SS data has two separate single-seed runs at different random seeds, but I need the aggregated mean and standard deviation across all three seeds. The Llama experiments are also all single-seed runs so far.

Now I'm pulling together the Llama results—ThreadGate and LoRA-only both show similar performance around 0.48 on the main metric, but their AR means diverge significantly, with ThreadGate at 0.043 versus LoRA-only at 0.028. The AR medians converge at 0.018 for both. I'm ready to consolidate everything into a final organized table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "d09ea7f4-5085-4148-84e5-a9afd4bdcc3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ4Fk4iMShQZc2dsrVeJQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4218,
      "cache_read_input_tokens": 51289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4218
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

_source line 45_

## 占位符清单

| # | 文件 | 行号 | 当前内容 | 需要什么数据 |
|---|------|------|---------|------------|
| **abstract.tex** | | | | |
| 1 | abstract.tex | L2 | `1.44× (single seed)` | SS 3-seed mean±std 后的 gap 值，去掉 "single seed" 标记 |
| **introduction.tex** | | | | |
| 2 | introduction.tex | L16 | `gap 7.8×→1.44×` | SS 3-seed gap 更新值 |
| 3 | introduction.tex | L18 | `(gap 7.8×→1.44×)` | 同上，贡献 (3) 中的 SS gap |
| **experiments.tex** | | | | |
| 4 | experiments.tex | L6 | `seed 42; ThreadGate additionally with seed 123` | 如有 multi-seed，需更新描述 |
| 5 | experiments.tex | L12 | `A second seed (123) confirms TF stability ($0.504\pm0.001$)` | AR 方面也需要 multi-seed 数据 |
| 6 | experiments.tex | L29 | ThreadGate AR GAR `0.064` CI `[.041,.091]` | s42 单 seed，需 multi-seed mean±std |
| 7 | experiments.tex | L30 | +PCGrad AR GAR `0.030` CI `[.023,.038]` | s42 单 seed，需 multi-seed mean±std |
| 8 | experiments.tex | L31 | Uniform Gate AR GAR `0.033` CI `[.025,.043]` | s42 单 seed，需 multi-seed mean±std |
| 9 | experiments.tex | L34 | LoRA-only AR GAR `0.037` CI `[.027,.050]` | s42 单 seed，需 multi-seed mean±std |
| 10 | experiments.tex | L12 | `Wilcoxon p=0.004, r=0.454` | multi-seed 后可能需更新统计检验 |
| 11 | experiments.tex | L12 | `GAR-ours 0.064 vs 0.037` | 更新为 multi-seed 值 |
| 12 | experiments.tex | L10 | `8--17×` gap range | multi-seed 后 gap range 可能变化 |
| 13 | experiments.tex | L48 | steering `0.064→0.556` (β=3), `0.727±0.061` (β=5) | 基于 TG s42 单 seed，可能需 multi-seed |
| **discussion.tex** | | | | |
| 14 | discussion.tex | L3 | `0.064 to 0.727` | TG 单 seed steering 数据 |
| 15 | discussion.tex | L5 | SS GAR `0.064 to 0.347 (5.4×)` | SS s42 单 seed → 需 3-seed mean±std |
| 16 | discussion.tex | L5 | `gap to 1.44× with negligible PPL change (1.44 vs. 1.43)` | SS 3-seed mean±std gap 和 PPL |
| 17 | discussion.tex | L5 | `a second seed yields 0.418 (gap 1.20×)` | 合并为 3-seed mean±std 报告 |
| 18 | discussion.tex | L5 | `GAR-Dongre also rises (0.019→0.353; N=5 pilot)` | 仍是 N=5 pilot，是否扩大到 N=50？ |
| 19 | discussion.tex | L5 | `content compliance rising +23.8 pp (p=0.077)` | 单模型探索性数据，limitations 已声明 |
| **conclusion.tex** | | | | |
| 20 | conclusion.tex | L3 | `gap 7.8×→1.44×; single seed` | SS 3-seed gap，去掉 "single seed" |
| 21 | conclusion.tex | L3 | `8--17×` on Qwen | multi-seed 后 gap range 可能变化 |
| **limitations.tex** | | | | |
| 22 | limitations.tex | L3 | `primarily a single seed` | multi-seed 完成后需更新措辞 |
| **analysis.tex** | | | | |
| 23 | analysis.tex | L43 | Llama TF `0.484`/`0.481`, AR mean `0.043`/`0.028`, median `0.018`/`0.018` | Llama 单 seed，无 ±std |
| 24 | analysis.tex | L43 | Llama gap `27×`/`26×` (median), `11×`/`17×` (mean) | 单 seed，无置信区间 |
| **appendix.tex** | | | | |
| 25 | appendix.tex | L138 | `SS vs. TG` Wilcoxon `p<0.001, r=0.869` | 基于 s42 单 seed 对比 |
| 26 | appendix.tex | L156 | Llama AR: `mean 0.043, std 0.100` | 单 seed，无跨 seed 统计 |
| 27 | appendix.tex | L301-302 | SS s42 `6.5h`, SS s123 `10.8h` | 若有 s456 需补充训练时间 |

### 按优先级分组

**P0 — 论文中已标记 "single seed"，必须更新：**
- #1, #20: abstract/conclusion 显式标记 `single seed`
- #15-17: discussion 中 SS 两个 seed 的独立数值 → 合并为 3-seed mean±std
- #22: limitations 措辞更新

**P1 — 主表/主文 AR 数字（当前 s42 单 seed）：**
- #6-9: Table 1 所有 AR GAR 和 CI
- #10-12: 关联统计检验和 gap range
- #2-3: intro 中引用的 SS gap

**P2 — Llama 跨模型数据（单 seed，无 CI）：**
- #23-24: analysis 中 Llama 所有数字
- #26: appendix Llama 详细数据

**P3 — 论文中完全缺失的数据：**
- **1.5B cross-model**: 论文全文无任何 1.5B 模型数据
- **MMLU**: 论文全文无 MMLU 评估
- 这两项在当前论文中未承诺也未引用，如不做可无需占位

**P4 — 次要/探索性：**
- #13-14: steering 数据（单 seed，但作为 diagnostic 可接受）
- #18: GAR-Dongre SS pilot（N=5）
- #19: instruction retention（已在 limitations 声明为 exploratory）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "uuid": "6dcd0934-1e94-41b5-a593-7aaff12df11b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ4Fk4iMShQZc2dsrVeJQB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4218,
      "cache_read_input_tokens": 51289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4218
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

_source line 46_

## 占位符清单

| # | 文件 | 行号 | 当前内容 | 需要什么数据 |
|---|------|------|---------|------------|
| **abstract.tex** | | | | |
| 1 | abstract.tex | L2 | `1.44× (single seed)` | SS 3-seed mean±std 后的 gap 值，去掉 "single seed" 标记 |
| **introduction.tex** | | | | |
| 2 | introduction.tex | L16 | `gap 7.8×→1.44×` | SS 3-seed gap 更新值 |
| 3 | introduction.tex | L18 | `(gap 7.8×→1.44×)` | 同上，贡献 (3) 中的 SS gap |
| **experiments.tex** | | | | |
| 4 | experiments.tex | L6 | `seed 42; ThreadGate additionally with seed 123` | 如有 multi-seed，需更新描述 |
| 5 | experiments.tex | L12 | `A second seed (123) confirms TF stability ($0.504\pm0.001$)` | AR 方面也需要 multi-seed 数据 |
| 6 | experiments.tex | L29 | ThreadGate AR GAR `0.064` CI `[.041,.091]` | s42 单 seed，需 multi-seed mean±std |
| 7 | experiments.tex | L30 | +PCGrad AR GAR `0.030` CI `[.023,.038]` | s42 单 seed，需 multi-seed mean±std |
| 8 | experiments.tex | L31 | Uniform Gate AR GAR `0.033` CI `[.025,.043]` | s42 单 seed，需 multi-seed mean±std |
| 9 | experiments.tex | L34 | LoRA-only AR GAR `0.037` CI `[.027,.050]` | s42 单 seed，需 multi-seed mean±std |
| 10 | experiments.tex | L12 | `Wilcoxon p=0.004, r=0.454` | multi-seed 后可能需更新统计检验 |
| 11 | experiments.tex | L12 | `GAR-ours 0.064 vs 0.037` | 更新为 multi-seed 值 |
| 12 | experiments.tex | L10 | `8--17×` gap range | multi-seed 后 gap range 可能变化 |
| 13 | experiments.tex | L48 | steering `0.064→0.556` (β=3), `0.727±0.061` (β=5) | 基于 TG s42 单 seed，可能需 multi-seed |
| **discussion.tex** | | | | |
| 14 | discussion.tex | L3 | `0.064 to 0.727` | TG 单 seed steering 数据 |
| 15 | discussion.tex | L5 | SS GAR `0.064 to 0.347 (5.4×)` | SS s42 单 seed → 需 3-seed mean±std |
| 16 | discussion.tex | L5 | `gap to 1.44× with negligible PPL change (1.44 vs. 1.43)` | SS 3-seed mean±std gap 和 PPL |
| 17 | discussion.tex | L5 | `a second seed yields 0.418 (gap 1.20×)` | 合并为 3-seed mean±std 报告 |
| 18 | discussion.tex | L5 | `GAR-Dongre also rises (0.019→0.353; N=5 pilot)` | 仍是 N=5 pilot，是否扩大到 N=50？ |
| 19 | discussion.tex | L5 | `content compliance rising +23.8 pp (p=0.077)` | 单模型探索性数据，limitations 已声明 |
| **conclusion.tex** | | | | |
| 20 | conclusion.tex | L3 | `gap 7.8×→1.44×; single seed` | SS 3-seed gap，去掉 "single seed" |
| 21 | conclusion.tex | L3 | `8--17×` on Qwen | multi-seed 后 gap range 可能变化 |
| **limitations.tex** | | | | |
| 22 | limitations.tex | L3 | `primarily a single seed` | multi-seed 完成后需更新措辞 |
| **analysis.tex** | | | | |
| 23 | analysis.tex | L43 | Llama TF `0.484`/`0.481`, AR mean `0.043`/`0.028`, median `0.018`/`0.018` | Llama 单 seed，无 ±std |
| 24 | analysis.tex | L43 | Llama gap `27×`/`26×` (median), `11×`/`17×` (mean) | 单 seed，无置信区间 |
| **appendix.tex** | | | | |
| 25 | appendix.tex | L138 | `SS vs. TG` Wilcoxon `p<0.001, r=0.869` | 基于 s42 单 seed 对比 |
| 26 | appendix.tex | L156 | Llama AR: `mean 0.043, std 0.100` | 单 seed，无跨 seed 统计 |
| 27 | appendix.tex | L301-302 | SS s42 `6.5h`, SS s123 `10.8h` | 若有 s456 需补充训练时间 |

### 按优先级分组

**P0 — 论文中已标记 "single seed"，必须更新：**
- #1, #20: abstract/conclusion 显式标记 `single seed`
- #15-17: discussion 中 SS 两个 seed 的独立数值 → 合并为 3-seed mean±std
- #22: limitations 措辞更新

**P1 — 主表/主文 AR 数字（当前 s42 单 seed）：**
- #6-9: Table 1 所有 AR GAR 和 CI
- #10-12: 关联统计检验和 gap range
- #2-3: intro 中引用的 SS gap

**P2 — Llama 跨模型数据（单 seed，无 CI）：**
- #23-24: analysis 中 Llama 所有数字
- #26: appendix Llama 详细数据

**P3 — 论文中完全缺失的数据：**
- **1.5B cross-model**: 论文全文无任何 1.5B 模型数据
- **MMLU**: 论文全文无 MMLU 评估
- 这两项在当前论文中未承诺也未引用，如不做可无需占位

**P4 — 次要/探索性：**
- #13-14: steering 数据（单 seed，但作为 diagnostic 可接受）
- #18: GAR-Dongre SS pilot（N=5）
- #19: instruction retention（已在 limitations 声明为 exploratory）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 147844,
  "duration_api_ms": 148830,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "4b017c9f-450b-4456-869e-52f52e08313b",
  "total_cost_usd": 0.547783,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 43666,
    "cache_read_input_tokens": 226077,
    "output_tokens": 6416,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43666,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2540,
        "cache_read_input_tokens": 51289,
        "cache_creation_input_tokens": 4218,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4218
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1307,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001387,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6416,
      "cacheReadInputTokens": 226077,
      "cacheCreationInputTokens": 43666,
      "webSearchRequests": 0,
      "costUSD": 0.546396,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "840598d0-2fbd-462c-9aa7-64243c76123e"
}
```

</details>

---
