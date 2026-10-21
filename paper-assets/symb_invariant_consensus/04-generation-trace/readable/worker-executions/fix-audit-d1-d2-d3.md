# fix audit d1 d2 d3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_fix_audit-d1-d2-d3_20260524T044736.log`
- **Structured JSON:** [`3e94b240f4447ad983bd.json`](../../sessions/3e/3e94b240f4447ad983bd.json)

## Before a recorded user message

84 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
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
  "uuid": "60f9669d-4a3c-4333-a2e7-1588f9d0c0f2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
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
    "resetsAt": 1779818400,
    "rateLimitType": "seven_day",
    "utilization": 0.79,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "eb716840-46fb-4e3b-b456-20b83cf9b563",
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files and searching for the BH correction code in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "7cc895c2-9f34-4f2e-a06c-da5d0cbac559",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

I'll tackle all three issues in parallel. Starting with reading the relevant files and searching for BH correction code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "46a904d1-b4fa-4dc8-90b3-4cb93fc567a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Read · `toolu_013Gh57T3XWpxFjLF8X1r3Hz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "fa926e56-ec39-4561-8dfa-2d807cd7aef7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-24T04:47:49.071Z_

<details><summary>↩ Tool result · `toolu_013Gh57T3XWpxFjLF8X1r3Hz`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.066$); $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\Delta = 0$ and are reported separately in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule
19	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
20	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
21	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
22	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
23	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
24	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
25	\midrule
26	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
27	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
28	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
29	\addlinespace
30	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
31	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
32	Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\
33	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
34	Qwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\
35	\addlinespace
36	Qwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\
37	Qwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
38	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=\columnwidth]{f2_regime_scatter}
46	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--60\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.066$).}
47	\label{fig:regime-scatter}
48	\end{figure}
49	
50	\looseness=-1 Figure~\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$ at $K = 12$ (Table~\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\leq 40\%$), where low accuracy causes error amplification; an intermediate band (50--60\%), containing the only positive trends; and Type~A (SC $\geq 60\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\Delta$ ranges from $+2.94$ to $-2.45$\,pp despite $\kappa \in [0.45, 0.51]$. We trace the mechanism in \S\ref{sec:analysis}.
51	
52	\looseness=-1 TOST equivalence tests \citep{lakens2017equivalence} with pre-specified margin $\pm 2$\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\sim}2$\,pp (MDE 1.86--4.84\,pp; sensitivity analysis in Appendix~\ref{app:power},~\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\Delta = +0.16 \pm 2.70$\,pp across three Mistral-7B seeds (Table~\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\Delta \in [0.00, -2.01]$\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\sim}$12\% of this ceiling (Appendix~\ref{app:oracle}).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "efee4bb7-1919-48ae-8507-504f40edc667",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01P3wUx27aQcxYXMLFBcnRC2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "608b94d2-e53e-45ad-bfbb-4d7fe5b96128",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

_source line 9 · 2026-05-24T04:47:49.511Z_

<details><summary>↩ Tool result · `toolu_01P3wUx27aQcxYXMLFBcnRC2`</summary>

```text
1	Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? Across six confirmatory conditions ($n \geq 200$), we find no detectable improvement exceeding ${\sim}$2 percentage points (pp). We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces via weighted MAX-SAT. Despite Z3 validating 99\% of self-extracted constraints, SICA matches majority voting on over 90\% of problems across six models (7B--32B) and four benchmarks. No condition shows a significant positive effect after FDR control; four of six powered conditions confirm equivalence within $\pm$2\,pp (TOST); the remainder are underpowered for smaller effects. The failure is a robust empirical regularity: self-extracted constraints track the majority answer---a property we term \emph{symbolic confirmation bias} (bias ratios $1.66$--$4.97\times$ across nine models, 7B to frontier). Under source-attribution scoring and degeneration, SICA reduces to majority vote (Observation~1); the $M{\to}T{\to}A{\to}C$ Markov chain bounds self-extracted information, revealing a deeper mechanism underlying \citet{huang2024selfcorrect}'s findings. Twenty-seven training-free variants fail due to a persistent independence-accuracy trade-off. As exploratory evidence, cross-architecture verification escapes the bias ($+6.67$\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics characterize failure modes across all tested conditions.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a0a3f2f1-ee65-4776-b2f1-a2dc1498fec9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex",
      "content": "Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? Across six confirmatory conditions ($n \\geq 200$), we find no detectable improvement exceeding ${\\sim}$2 percentage points (pp). We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces via weighted MAX-SAT. Despite Z3 validating 99\\% of self-extracted constraints, SICA matches majority voting on over 90\\% of problems across six models (7B--32B) and four benchmarks. No condition shows a significant positive effect after FDR control; four of six powered conditions confirm equivalence within $\\pm$2\\,pp (TOST); the remainder are underpowered for smaller effects. The failure is a robust empirical regularity: self-extracted constraints track the majority answer---a property we term \\emph{symbolic confirmation bias} (bias ratios $1.66$--$4.97\\times$ across nine models, 7B to frontier). Under source-attribution scoring and degeneration, SICA reduces to majority vote (Observation~1); the $M{\\to}T{\\to}A{\\to}C$ Markov chain bounds self-extracted information, revealing a deeper mechanism underlying \\citet{huang2024selfcorrect}'s findings. Twenty-seven training-free variants fail due to a persistent independence-accuracy trade-off. As exploratory evidence, cross-architecture verification escapes the bias ($+6.67$\\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics characterize failure modes across all tested conditions.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01Nx6uDcPsgSw9hmVoadQZrb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "9490a4fd-6998-4674-8482-69e1a2451f35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

_source line 11 · 2026-05-24T04:47:50.002Z_

<details><summary>↩ Tool result · `toolu_01Nx6uDcPsgSw9hmVoadQZrb`</summary>

```text
1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). The DPI bound implies that any escape must break the self-extraction dependency: $I(C;Y) \leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +1.47$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Across 108 verifier-generator-weight combinations spanning three NLI architectures, four generators, and three domains, gain decreases monotonically with generator accuracy---a \emph{capability-gap pattern}. Of 72 above-verifier conditions, none shows a significant improvement; all significant gains concentrate below the verifier's standalone accuracy. The pattern is quantified by a perfect rank correlation across architectures ($\rho = 1.0$, $p = 0.003$, $n{=}6$; Figure~\ref{fig:capability-gap}). On ProofWriter ($n{=}600$; Table~\ref{tab:cross_generator_nli}), only Mistral-7B (SC below DeBERTa's 55.00\%) gains significantly ($+6.67$\,pp, $p < 0.001$). At $w{=}5$, BART and RoBERTa \emph{degrade} Qwen2.5-14B ($-3.43$/$-4.41$\,pp; Appendix~\ref{app:multi-nli}).
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability. Only Mistral-7B (SC below the verifier) shows a significant $w{=}3$ gain.}
21	\label{tab:cross_generator_nli}
22	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}llcccc@{}}
23	\toprule
24	Generator & Family & SC & Gap & Combo $\Delta$ ($w{=}3$) & $p$ \\
25	\midrule
26	Mistral-7B & Mistral & 39.33\% & $+$15.67 & $+$6.67\,pp & $<$0.001 \\
27	LLaMA-3.1-8B & LLaMA & 72.50\% & $-$17.50 & $+$0.83\,pp & 0.665 \\
28	Qwen2.5-14B & Qwen & 74.00\% & $-$19.00 & $+$0.67\,pp & 0.503 \\
29	Qwen3-14B & Qwen & 85.83\% & $-$30.83 & $+$0.50\,pp & 0.453 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
34	\paragraph{Domain-adapted verifier.}
35	\looseness=-1 Fine-tuning DeBERTa on ProofWriter depth-5 OWA (99.67\% standalone) amplifies escape: $+$12.67/$+$11.67\,pp for Mistral-7B/LLaMA-8B ($14\times$ over zero-shot; Table~\ref{tab:finetuned-nli}), extending gains to generators with SC up to ${\sim}$72\%. A cost-aware cascade recovers 83--90\% of gain at ${\sim}$35\% cost (Appendix~\ref{app:drc}). These results serve as directional evidence (the domain-adapted verifier introduces training).
36	
37	\paragraph{Cross-model voting vs.\ cross-architecture NLI.}
38	\looseness=-1 An ensemble diversity control replaces the NLI verifier with a second LLM as cross voter ($w{=}3$). With Mistral-7B as cross voter on ProofWriter, all three strong generators degrade significantly ($-2.33$ to $-9.33$\,pp, all $p \leq 0.020$); even a stronger cross voter (Qwen2.5-14B) degrades Qwen3-14B at $w{=}5$ ($-2.50$\,pp, $p = 0.006$). In contrast, DeBERTa NLI at comparable standalone accuracy (55.00\%) never degrades any generator ($\Delta \leq +0.83$\,pp). This asymmetry reflects the structural independence of encoder-only NLI---different architecture, training objective, and input representation---from autoregressive biases shared across LLM families (Table~\ref{tab:cross-model-ablation}).
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "ee68043d-23db-4ca1-89a7-869159097cda",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
      "content": "\\section{Escaping the Bottleneck}\n\\label{sec:solutions}\n\\label{sec:cross-arch}\n\n\\paragraph{Motivation.}\n\\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\\S\\ref{sec:remediation}). The DPI bound implies that any escape must break the self-extraction dependency: $I(C;Y) \\leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.\n\n\\paragraph{Method.}\n\\looseness=-1 We use DeBERTa-large \\citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).\n\n\\paragraph{Zero-shot results.}\n\\looseness=-1 DeBERTa NLI alone achieves 49.51\\% on FOLIO and 55.00\\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\\,pp on FOLIO (n.s.); all generators with SC $\\geq 72\\%$ show no significant improvement ($\\Delta \\leq +1.47$\\,pp). Same-model SICA \\emph{degrades} ProofWriter ($-2.83$\\,pp; Table~\\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.\n\n\\paragraph{Capability gap.}\n\\looseness=-1 Across 108 verifier-generator-weight combinations spanning three NLI architectures, four generators, and three domains, gain decreases monotonically with generator accuracy---a \\emph{capability-gap pattern}. Of 72 above-verifier conditions, none shows a significant improvement; all significant gains concentrate below the verifier's standalone accuracy. The pattern is quantified by a perfect rank correlation across architectures ($\\rho = 1.0$, $p = 0.003$, $n{=}6$; Figure~\\ref{fig:capability-gap}). On ProofWriter ($n{=}600$; Table~\\ref{tab:cross_generator_nli}), only Mistral-7B (SC below DeBERTa's 55.00\\%) gains significantly ($+6.67$\\,pp, $p < 0.001$). At $w{=}5$, BART and RoBERTa \\emph{degrade} Qwen2.5-14B ($-3.43$/$-4.41$\\,pp; Appendix~\\ref{app:multi-nli}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability. Only Mistral-7B (SC below the verifier) shows a significant $w{=}3$ gain.}\n\\label{tab:cross_generator_nli}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Family & SC & Gap & Combo $\\Delta$ ($w{=}3$) & $p$ \\\\\n\\midrule\nMistral-7B & Mistral & 39.33\\% & $+$15.67 & $+$6.67\\,pp & $<$0.001 \\\\\nLLaMA-3.1-8B & LLaMA & 72.50\\% & $-$17.50 & $+$0.83\\,pp & 0.665 \\\\\nQwen2.5-14B & Qwen & 74.00\\% & $-$19.00 & $+$0.67\\,pp & 0.503 \\\\\nQwen3-14B & Qwen & 85.83\\% & $-$30.83 & $+$0.50\\,pp & 0.453 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier.}\n\\looseness=-1 Fine-tuning DeBERTa on ProofWriter depth-5 OWA (99.67\\% standalone) amplifies escape: $+$12.67/$+$11.67\\,pp for Mistral-7B/LLaMA-8B ($14\\times$ over zero-shot; Table~\\ref{tab:finetuned-nli}), extending gains to generators with SC up to ${\\sim}$72\\%. A cost-aware cascade recovers 83--90\\% of gain at ${\\sim}$35\\% cost (Appendix~\\ref{app:drc}). These results serve as directional evidence (the domain-adapted verifier introduces training).\n\n\\paragraph{Cross-model voting vs.\\ cross-architecture NLI.}\n\\looseness=-1 An ensemble diversity control replaces the NLI verifier with a second LLM as cross voter ($w{=}3$). With Mistral-7B as cross voter on ProofWriter, all three strong generators degrade significantly ($-2.33$ to $-9.33$\\,pp, all $p \\leq 0.020$); even a stronger cross voter (Qwen2.5-14B) degrades Qwen3-14B at $w{=}5$ ($-2.50$\\,pp, $p = 0.006$). In contrast, DeBERTa NLI at comparable standalone accuracy (55.00\\%) never degrades any generator ($\\Delta \\leq +0.83$\\,pp). This asymmetry reflects the structural independence of encoder-only NLI---different architecture, training objective, and input representation---from autoregressive biases shared across LLM families (Table~\\ref{tab:cross-model-ablation}).\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_01RNnusjGaNr1M3ZabeaSd4k`</summary>

```json
{
  "pattern": "benjamini|BH|fdr|multipletests|p_adjust",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.py",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "857d51f8-79d4-425d-bc2e-862fa6e44013",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwQVbTzZb4n9ytQpdzt8ge",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12660,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12660
      },
      "output_tokens": 24,
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

_source line 13 · 2026-05-24T04:47:51.140Z_

<details><summary>↩ Tool result · `toolu_01RNnusjGaNr1M3ZabeaSd4k`</summary>

```text
Found 6 files
logiqa_nli_combo.py
artifacts/r11_3verifier_canonical.py
scripts/r11_3verifier_significance.py
artifacts/compute_cil.py
artifacts/compute_tost_sensitivity.py
direction_g_decoupling.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "2a01a135-7549-4893-9635-a57782487e89",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logiqa_nli_combo.py",
      "artifacts/r11_3verifier_canonical.py",
      "scripts/r11_3verifier_significance.py",
      "artifacts/compute_cil.py",
      "artifacts/compute_tost_sensitivity.py",
      "direction_g_decoupling.py"
    ],
    "numFiles": 6
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:

1. **D1**: Find the BH correction code and verify the p-values. The key text is in experiments.tex line 5: "adjusted p = 0.066" with m=6. Let me look at the relevant Python files to find the raw p-values and BH computation.

2. **D2**: Count words in abstract.tex. It looks like a single long paragraph.

3. **D3**: Found "14× over zero-shot" in solutions.tex line 35. Need to add "(LLaMA-8B)".

Let me read the BH-related Python files and count abstract words.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "088127df-14fb-40d4-8186-cbccbea92211",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AGUGDCVYeScizGk2q3mM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 24501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01CmNBwk4hF5kbLG37K1WiCN`</summary>

```json
{
  "pattern": "benjamini|BH|fdr|multipletests|p_adjust|adjusted",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/r11_3verifier_significance.py",
  "output_mode": "content",
  "-i": true,
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "1e246c30-e17c-4a83-9eaa-754395458382",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AGUGDCVYeScizGk2q3mM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 24501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 16 · 2026-05-24T04:48:01.045Z_

<details><summary>↩ Tool result · `toolu_01CmNBwk4hF5kbLG37K1WiCN`</summary>

```text
1-#!/usr/bin/env python3
2:"""R11: 3-verifier NLI combo significance with BH correction.
3-
4-Verifiers: DeBERTa-large-MNLI, RoBERTa-large-MNLI, BART-large-MNLI
5-Generator: Mistral-7B on ProofWriter D5-600
6-"""
7-
--
64-        return 1.0, b, c
65-    result = binomtest(min(b, c), n, 0.5)
66-    return result.pvalue, b, c
67-
68-
69:def bh_correction(p_values):
70-    n = len(p_values)
71-    if n == 0:
72-        return []
73-    sorted_indices = sorted(range(n), key=lambda i: p_values[i])
74:    adjusted = [0.0] * n
75-    for rank, idx in enumerate(sorted_indices, 1):
76:        adjusted[idx] = p_values[idx] * n / rank
77-    for i in range(n - 2, -1, -1):
78-        idx = sorted_indices[i]
79-        next_idx = sorted_indices[i + 1]
80:        adjusted[idx] = min(adjusted[idx], adjusted[next_idx])
81:    return [min(p, 1.0) for p in adjusted]
82-
83-
84-def run_nli_inference(model_name, model_path, problems, pids, device):
85-    print(f"\n--- {model_name} ---")
86-    tokenizer = AutoTokenizer.from_pretrained(model_path)
--
148-    sc_correct = [mistral_sc[pid] == gt[pid] for pid in pids]
149-    sc_acc = sum(sc_correct) / n
150-    print(f"Mistral SC baseline: {sum(sc_correct)}/{n} = {sc_acc:.4f}")
151-
152-    results = {
153:        "task": "R11: 3-verifier NLI combo BH-corrected significance",
154-        "generator": "Mistral-7B-Instruct-v0.3",
155-        "dataset": "ProofWriter-D5-600",
156-        "n": n,
157-        "sc_baseline": round(sc_acc, 4),
158-        "sc_correct_count": sum(sc_correct),
--
269-        }
270-        all_p_values.append(p)
271-        p_value_labels.append(f"3verifier_majority_w{w}")
272-        print(f"  w{w}: acc={combo_acc:.4f} Δ={delta*100:+.2f}pp p={p:.6f} (b={b},c={c_val})")
273-
274:    # BH correction on all p-values
275:    adjusted = bh_correction(all_p_values)
276:    bh_results = []
277:    for i, (label, raw_p, adj_p) in enumerate(zip(p_value_labels, all_p_values, adjusted)):
278:        bh_results.append({
279-            "test": label,
280-            "raw_p": round(raw_p, 6),
281:            "bh_adjusted_p": round(adj_p, 6),
282-            "significant_005": adj_p < 0.05,
283-            "significant_010": adj_p < 0.10,
284-        })
285-        sig = "*" if adj_p < 0.05 else ("†" if adj_p < 0.10 else "")
286:        print(f"  {label}: raw={raw_p:.6f} BH={adj_p:.6f} {sig}")
287-
288:    results["bh_correction"] = {
289-        "n_tests": len(all_p_values),
290:        "method": "Benjamini-Hochberg",
291:        "results": bh_results,
292-    }
293-
294:    n_sig_005 = sum(1 for r in bh_results if r["significant_005"])
295:    n_sig_010 = sum(1 for r in bh_results if r["significant_010"])
296-    results["summary"] = {
297-        "n_significant_005": n_sig_005,
298-        "n_significant_010": n_sig_010,
299-        "n_tests": len(all_p_values),
300:        "conclusion": f"{n_sig_005}/{len(all_p_values)} tests significant at BH-corrected α=0.05"
301-    }
302-
303-    # Save per-question data for reproducibility
304-    per_question = {}
305-    for pid in pids:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "d7195f3a-6324-4038-beea-27df2a9943af",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1-#!/usr/bin/env python3\n2:\"\"\"R11: 3-verifier NLI combo significance with BH correction.\n3-\n4-Verifiers: DeBERTa-large-MNLI, RoBERTa-large-MNLI, BART-large-MNLI\n5-Generator: Mistral-7B on ProofWriter D5-600\n6-\"\"\"\n7-\n--\n64-        return 1.0, b, c\n65-    result = binomtest(min(b, c), n, 0.5)\n66-    return result.pvalue, b, c\n67-\n68-\n69:def bh_correction(p_values):\n70-    n = len(p_values)\n71-    if n == 0:\n72-        return []\n73-    sorted_indices = sorted(range(n), key=lambda i: p_values[i])\n74:    adjusted = [0.0] * n\n75-    for rank, idx in enumerate(sorted_indices, 1):\n76:        adjusted[idx] = p_values[idx] * n / rank\n77-    for i in range(n - 2, -1, -1):\n78-        idx = sorted_indices[i]\n79-        next_idx = sorted_indices[i + 1]\n80:        adjusted[idx] = min(adjusted[idx], adjusted[next_idx])\n81:    return [min(p, 1.0) for p in adjusted]\n82-\n83-\n84-def run_nli_inference(model_name, model_path, problems, pids, device):\n85-    print(f\"\\n--- {model_name} ---\")\n86-    tokenizer = AutoTokenizer.from_pretrained(model_path)\n--\n148-    sc_correct = [mistral_sc[pid] == gt[pid] for pid in pids]\n149-    sc_acc = sum(sc_correct) / n\n150-    print(f\"Mistral SC baseline: {sum(sc_correct)}/{n} = {sc_acc:.4f}\")\n151-\n152-    results = {\n153:        \"task\": \"R11: 3-verifier NLI combo BH-corrected significance\",\n154-        \"generator\": \"Mistral-7B-Instruct-v0.3\",\n155-        \"dataset\": \"ProofWriter-D5-600\",\n156-        \"n\": n,\n157-        \"sc_baseline\": round(sc_acc, 4),\n158-        \"sc_correct_count\": sum(sc_correct),\n--\n269-        }\n270-        all_p_values.append(p)\n271-        p_value_labels.append(f\"3verifier_majority_w{w}\")\n272-        print(f\"  w{w}: acc={combo_acc:.4f} Δ={delta*100:+.2f}pp p={p:.6f} (b={b},c={c_val})\")\n273-\n274:    # BH correction on all p-values\n275:    adjusted = bh_correction(all_p_values)\n276:    bh_results = []\n277:    for i, (label, raw_p, adj_p) in enumerate(zip(p_value_labels, all_p_values, adjusted)):\n278:        bh_results.append({\n279-            \"test\": label,\n280-            \"raw_p\": round(raw_p, 6),\n281:            \"bh_adjusted_p\": round(adj_p, 6),\n282-            \"significant_005\": adj_p < 0.05,\n283-            \"significant_010\": adj_p < 0.10,\n284-        })\n285-        sig = \"*\" if adj_p < 0.05 else (\"†\" if adj_p < 0.10 else \"\")\n286:        print(f\"  {label}: raw={raw_p:.6f} BH={adj_p:.6f} {sig}\")\n287-\n288:    results[\"bh_correction\"] = {\n289-        \"n_tests\": len(all_p_values),\n290:        \"method\": \"Benjamini-Hochberg\",\n291:        \"results\": bh_results,\n292-    }\n293-\n294:    n_sig_005 = sum(1 for r in bh_results if r[\"significant_005\"])\n295:    n_sig_010 = sum(1 for r in bh_results if r[\"significant_010\"])\n296-    results[\"summary\"] = {\n297-        \"n_significant_005\": n_sig_005,\n298-        \"n_significant_010\": n_sig_010,\n299-        \"n_tests\": len(all_p_values),\n300:        \"conclusion\": f\"{n_sig_005}/{len(all_p_values)} tests significant at BH-corrected α=0.05\"\n301-    }\n302-\n303-    # Save per-question data for reproducibility\n304-    per_question = {}\n305-    for pid in pids:",
    "numLines": 81
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01FfMtXLRJEYoZ1TnSb7qU7m`</summary>

```json
{
  "pattern": "benjamini|BH|fdr|multipletests|p_adjust|adjusted|0\\.066",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.py",
  "output_mode": "content",
  "-i": true,
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "857e920c-7884-454b-82a8-0935d47c58b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AGUGDCVYeScizGk2q3mM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 24501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 18 · 2026-05-24T04:48:02.543Z_

<details><summary>↩ Tool result · `toolu_01FfMtXLRJEYoZ1TnSb7qU7m`</summary>

```text
&lt;persisted-output>
Output too large (26.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/88dd4cac-745e-4701-a7b3-bec955cff63c/tool-results/toolu_01FfMtXLRJEYoZ1TnSb7qU7m.txt

Preview (first 2KB):
artifacts/compute_cil.py-183-        for qid, qdata in pw600_pq.items():
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-184-            deberta_map[qid] = qdata["deberta_correct"]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-185-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-186-        print(f"  Loaded {len(deberta_map)} DeBERTa predictions on PW-600")
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-187-
artifacts/compute_cil.py:188:        # BH table combo gains for multi-generator pairs
artifacts/compute_cil.py:189:        bh_table = json.load(open(RESULTS / "nli_combo_full_table_bh" / "results.json"))
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-190-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-191-        # Try to match with Qwen2.5-14B (exp034)
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-192-        generators_on_server = {
artifacts/compute_cil.py-193-            "Qwen2.5-14B": RESULTS / "exp034_qwen25_14b_proofwriter",
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-194-        }
--
artifacts/compute_cil.py-219-                print(f"    SKIP: too few matches")
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-220-                continue
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-221-
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "c41e60c5-ef0f-4249-bb91-3ed930a7c8b9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/compute_cil.py-183-        for qid, qdata in pw600_pq.items():\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-184-            deberta_map[qid] = qdata[\"deberta_correct\"]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-185-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-186-        print(f\"  Loaded {len(deberta_map)} DeBERTa predictions on PW-600\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-187-\nartifacts/compute_cil.py:188:        # BH table combo gains for multi-generator pairs\nartifacts/compute_cil.py:189:        bh_table = json.load(open(RESULTS / \"nli_combo_full_table_bh\" / \"results.json\"))\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-190-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-191-        # Try to match with Qwen2.5-14B (exp034)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-192-        generators_on_server = {\nartifacts/compute_cil.py-193-            \"Qwen2.5-14B\": RESULTS / \"exp034_qwen25_14b_proofwriter\",\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-194-        }\n--\nartifacts/compute_cil.py-219-                print(f\"    SKIP: too few matches\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-220-                continue\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-221-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-222-            cil_data = compute_pair_cil_from_per_question(matched_g_correct, matched_v_correct)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-223-\nartifacts/compute_cil.py:224:            # Try to get combo gain from BH table\nartifacts/compute_cil.py:225:            bh_gen = bh_table.get(\"generators\", {}).get(gen_name, {})\nartifacts/compute_cil.py:226:            # Use local experiment's SC accuracy, not BH table\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-227-            local_sc = sum(1 for v in gen_sc.values() if v[\"sc_correct\"]) / len(gen_sc)\nartifacts/compute_cil.py:228:            bh_combo_w3 = bh_gen.get(\"w3\", {}).get(\"delta_pp\", None)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-229-\nartifacts/compute_cil.py:230:            # Note: BH table used data from westd-16639, different experiment\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-231-            # For local experiment, we don't have the combo gain\nartifacts/compute_cil.py-232-            # We'll compute a proxy: the DeBERTa combo gain at w3 with THIS generator's SC\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-233-            pair = {\nartifacts/compute_cil.py-234-                \"generator\": gen_name,\nartifacts/compute_cil.py-235-                \"verifier\": \"DeBERTa-large-MNLI\",\nartifacts/compute_cil.py-236-                \"verifier_type\": \"NLI\",\nartifacts/compute_cil.py-237-                \"dataset\": f\"PW-{n_matched}\",\nartifacts/compute_cil.py-238-                \"n\": n_matched,\nartifacts/compute_cil.py:239:                \"combo_gain_w3\": bh_combo_w3,\nartifacts/compute_cil.py:240:                \"note\": f\"local SC={local_sc:.4f}, BH table SC={bh_gen.get('sc_accuracy', 'N/A')}\",\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-241-                **cil_data,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-242-            }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-243-            pairs.append(pair)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-244-            print(f\"    CIL={cil_data['cil']}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-245-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-268-                    **cil_sica,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-269-                }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-270-                pairs.append(pair_sica)\nartifacts/compute_cil.py-271-                print(f\"    {gen_name} SICA: CIL={cil_sica['cil']}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-272-\nartifacts/compute_cil.py:273:    # For LLaMA-8B and Qwen3-14B: add from BH table complementarity if derivable\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-274-    # These are on westd-16639, so we note them as unavailable\nartifacts/compute_cil.py-275-    for gen_name in [\"LLaMA-3.1-8B\", \"Qwen3-14B\"]:\nartifacts/compute_cil.py:276:        bh_gen = bh_table.get(\"generators\", {}).get(gen_name, {})\nartifacts/compute_cil.py:277:        if bh_gen:\nartifacts/compute_cil.py:278:            print(f\"  {gen_name}: data on westd-16639, adding BH-derived entry\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-279-            # We can derive the 2x2 table from McNemar discordant pairs + total\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-280-            # At w=1 (NLI gets 1 vote, SC gets 10 votes), combo ≈ SC unless NLI flips\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-281-            # This doesn't give us the raw complementarity. Skip with note.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-282-            pairs.append({\nartifacts/compute_cil.py-283-                \"generator\": gen_name,\nartifacts/compute_cil.py-284-                \"verifier\": \"DeBERTa-large-MNLI\",\nartifacts/compute_cil.py-285-                \"verifier_type\": \"NLI\",\nartifacts/compute_cil.py-286-                \"dataset\": \"PW-600\",\nartifacts/compute_cil.py-287-                \"n\": 600,\nartifacts/compute_cil.py:288:                \"combo_gain_w3\": bh_gen.get(\"w3\", {}).get(\"delta_pp\", None),\nartifacts/compute_cil.py-289-                \"cil\": None,\nartifacts/compute_cil.py-290-                \"note\": \"per-question data on westd-16639, CIL not computable from this server\",\nartifacts/compute_cil.py:291:                \"sc_accuracy\": bh_gen.get(\"sc_accuracy\", None),\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-292-            })\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-293-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-294-    # ============================================================\nartifacts/compute_cil.py-295-    # Section 3: Mistral × DeBERTa × FOLIO-204\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-296-    # ============================================================\n--\nartifacts/cross_trace_unsat.py-159-        \"formula_counts\": {a: len(answer_formulas[a]) for a in answers},\nartifacts/cross_trace_unsat.py-160-        \"pairs\": pairs, \"has_unsat\": has_unsat, \"skipped\": False,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-161-    }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-162-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-163-\nartifacts/cross_trace_unsat.py:164:def compute_adjusted_scores(analysis, sica_result, bonus=5.0):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-165-    \"\"\"Adjust SICA scores based on cross-trace UNSAT results.\"\"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-166-    original_scores = dict(sica_result.get(\"sica_scores\", {}))\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-167-    original_answer = sica_result.get(\"sica_answer\", \"\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-168-\nartifacts/cross_trace_unsat.py-169-    if analysis[\"skipped\"] or not analysis[\"has_unsat\"]:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-170-        return {\nartifacts/cross_trace_unsat.py-171-            \"original_scores\": original_scores,\nartifacts/cross_trace_unsat.py:172:            \"adjusted_scores\": original_scores,\nartifacts/cross_trace_unsat.py-173-            \"original_answer\": original_answer,\nartifacts/cross_trace_unsat.py:174:            \"adjusted_answer\": original_answer,\nartifacts/cross_trace_unsat.py-175-            \"adjustment_applied\": False,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-176-        }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-177-\nartifacts/cross_trace_unsat.py:178:    adjusted = dict(original_scores)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-179-    answer_counts = analysis[\"answer_counts\"]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-180-\nartifacts/cross_trace_unsat.py-181-    for pair_info in analysis[\"pairs\"]:\nartifacts/cross_trace_unsat.py-182-        if pair_info[\"result\"] != \"unsat\":\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-183-            continue\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-184-        a, b = pair_info[\"pair\"]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-185-        ca = answer_counts.get(a, 0)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-186-        cb = answer_counts.get(b, 0)\nartifacts/cross_trace_unsat.py-187-        if ca > cb:\nartifacts/cross_trace_unsat.py:188:            adjusted[a] = adjusted.get(a, 0) + bonus\nartifacts/cross_trace_unsat.py:189:            adjusted[b] = adjusted.get(b, 0) - bonus\nartifacts/cross_trace_unsat.py-190-        elif cb > ca:\nartifacts/cross_trace_unsat.py:191:            adjusted[b] = adjusted.get(b, 0) + bonus\nartifacts/cross_trace_unsat.py:192:            adjusted[a] = adjusted.get(a, 0) - bonus\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-193-\nartifacts/cross_trace_unsat.py:194:    adjusted_answer = max(adjusted, key=lambda x: adjusted[x]) if adjusted else original_answer\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-195-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-196-    return {\nartifacts/cross_trace_unsat.py-197-        \"original_scores\": original_scores,\nartifacts/cross_trace_unsat.py:198:        \"adjusted_scores\": adjusted,\nartifacts/cross_trace_unsat.py-199-        \"original_answer\": original_answer,\nartifacts/cross_trace_unsat.py:200:        \"adjusted_answer\": adjusted_answer,\nartifacts/cross_trace_unsat.py-201-        \"adjustment_applied\": True,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-202-    }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-203-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-204-\nartifacts/cross_trace_unsat.py-205-def main():\n--\nartifacts/cross_trace_unsat.py-228-    for i, (pid, pdata) in enumerate(items):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-229-        analysis = analyze_problem(pid, pdata, args.timeout_ms)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-230-        analyses[pid] = analysis\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-231-\nartifacts/cross_trace_unsat.py-232-        if pid in sica_results:\nartifacts/cross_trace_unsat.py:233:            scoring[pid] = compute_adjusted_scores(analysis, sica_results[pid], args.bonus)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-234-\nartifacts/cross_trace_unsat.py-235-        if (i + 1) % 50 == 0:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-236-            print(f\"  Processed {i+1}/{len(items)}...\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-237-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-238-    elapsed = time.time() - t0\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-266-    avg_shared = sum(shared_var_stats) / len(shared_var_stats) if shared_var_stats else 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-267-    zero_shared = sum(1 for x in shared_var_stats if x == 0)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-268-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-269-    # --- Accuracy ---\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-270-    sica_correct = 0\nartifacts/cross_trace_unsat.py:271:    adjusted_correct = 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-272-    sc_correct = 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-273-    total_scored = 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-274-    flips = []\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-275-\nartifacts/cross_trace_unsat.py-276-    for pid in sorted(scoring.keys()):\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-282-        s = scoring[pid]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-283-        sr = sica_results.get(pid, {})\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-284-\nartifacts/cross_trace_unsat.py-285-        if s[\"original_answer\"] == gt:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-286-            sica_correct += 1\nartifacts/cross_trace_unsat.py:287:        if s[\"adjusted_answer\"] == gt:\nartifacts/cross_trace_unsat.py:288:            adjusted_correct += 1\nartifacts/cross_trace_unsat.py-289-        if sr.get(\"sc_answer\", \"\") == gt:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-290-            sc_correct += 1\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-291-\nartifacts/cross_trace_unsat.py:292:        if s[\"original_answer\"] != s[\"adjusted_answer\"]:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-293-            flips.append({\nartifacts/cross_trace_unsat.py-294-                \"pid\": pid, \"gt\": gt,\nartifacts/cross_trace_unsat.py-295-                \"original\": s[\"original_answer\"],\nartifacts/cross_trace_unsat.py:296:                \"adjusted\": s[\"adjusted_answer\"],\nartifacts/cross_trace_unsat.py-297-                \"original_correct\": s[\"original_answer\"] == gt,\nartifacts/cross_trace_unsat.py:298:                \"adjusted_correct\": s[\"adjusted_answer\"] == gt,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-299-            })\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-300-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-301-    summary = {\nartifacts/cross_trace_unsat.py-302-        \"n_problems\": total,\nartifacts/cross_trace_unsat.py-303-        \"n_single_answer_skipped\": skipped,\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-316-        },\nartifacts/cross_trace_unsat.py-317-        \"pair_type_breakdown\": {k: dict(v) for k, v in pair_type_counts.items()},\nartifacts/cross_trace_unsat.py-318-        \"accuracy\": {\nartifacts/cross_trace_unsat.py-319-            \"sc\": round(sc_correct / total_scored, 4) if total_scored > 0 else 0,\nartifacts/cross_trace_unsat.py-320-            \"sica\": round(sica_correct / total_scored, 4) if total_scored > 0 else 0,\nartifacts/cross_trace_unsat.py:321:            \"sica_cross_ut\": round(adjusted_correct / total_scored, 4) if total_scored > 0 else 0,\nartifacts/cross_trace_unsat.py-322-            \"n\": total_scored,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-323-        },\nartifacts/cross_trace_unsat.py-324-        \"flips\": {\nartifacts/cross_trace_unsat.py-325-            \"total\": len(flips),\nartifacts/cross_trace_unsat.py:326:            \"improved\": sum(1 for f in flips if f[\"adjusted_correct\"] and not f[\"original_correct\"]),\nartifacts/cross_trace_unsat.py:327:            \"degraded\": sum(1 for f in flips if not f[\"adjusted_correct\"] and f[\"original_correct\"]),\nartifacts/cross_trace_unsat.py:328:            \"neutral\": sum(1 for f in flips if f[\"adjusted_correct\"] == f[\"original_correct\"]),\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-329-        },\nartifacts/cross_trace_unsat.py-330-        \"bonus\": args.bonus,\nartifacts/cross_trace_unsat.py-331-        \"elapsed_s\": round(elapsed, 1),\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-332-    }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-333-\n--\nartifacts/cross_trace_unsat.py-372-        print(f\"  {pt}: {', '.join(parts)}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-373-\nartifacts/cross_trace_unsat.py-374-    print(f\"\\nAccuracy (n={total_scored}):\")\nartifacts/cross_trace_unsat.py-375-    print(f\"  SC baseline:       {sc_correct}/{total_scored} = {summary['accuracy']['sc']:.1%}\")\nartifacts/cross_trace_unsat.py-376-    print(f\"  SICA:              {sica_correct}/{total_scored} = {summary['accuracy']['sica']:.1%}\")\nartifacts/cross_trace_unsat.py:377:    print(f\"  SICA+CrossUT(b={args.bonus}): {adjusted_correct}/{total_scored} = {summary['accuracy']['sica_cross_ut']:.1%}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-378-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-379-    fl = summary[\"flips\"]\nartifacts/cross_trace_unsat.py-380-    print(f\"\\nFlips: {fl['total']} total  (+{fl['improved']} improved, -{fl['degraded']} degraded, ={fl['neutral']} neutral)\")\nartifacts/cross_trace_unsat.py-381-    if flips:\nartifacts/cross_trace_unsat.py-382-        for f in flips:\nartifacts/cross_trace_unsat.py:383:            mark = \"+\" if f[\"adjusted_correct\"] and not f[\"original_correct\"] else \\\nartifacts/cross_trace_unsat.py:384:                   \"-\" if f[\"original_correct\"] and not f[\"adjusted_correct\"] else \"=\"\nartifacts/cross_trace_unsat.py:385:            print(f\"  [{mark}] {f['pid']}: {f['original']} -> {f['adjusted']} (gt={f['gt']})\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-386-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-387-    print(f\"\\nSaved to {args.output}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-388-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/cross_trace_unsat.py-389-\nartifacts/cross_trace_unsat.py-390-if __name__ == \"__main__\":\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-1-#!/usr/bin/env python3\nartifacts/r11_3verifier_canonical.py:2:\"\"\"R11 Q3: 3-verifier BH analysis using canonical NLI predictions.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-3-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-4-Loads DeBERTa per-question data from D116, runs RoBERTa/BART inference\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-5-using canonical models already on server, computes individual + ensemble\nartifacts/r11_3verifier_canonical.py:6:combos, McNemar tests, and BH correction.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-7-\nartifacts/r11_3verifier_canonical.py-8-Canonical expectations (from nli_multi_verifier_recomputed.json):\nartifacts/r11_3verifier_canonical.py-9-  SC baseline: 39.33% (236/600) [alphabetical tiebreaking]\nartifacts/r11_3verifier_canonical.py-10-  DeBERTa-large standalone: 55.0% (330/600)\nartifacts/r11_3verifier_canonical.py-11-  RoBERTa-large standalone: 37.67% (226/600)\n--\nartifacts/r11_3verifier_canonical.py-101-    if n == 0:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-102-        return 1.0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-103-    return binomtest(min(b, c), n, 0.5).pvalue\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-104-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-105-\nartifacts/r11_3verifier_canonical.py:106:def bh_correction(p_values):\nartifacts/r11_3verifier_canonical.py:107:    \"\"\"Benjamini-Hochberg correction.\"\"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-108-    n = len(p_values)\nartifacts/r11_3verifier_canonical.py-109-    if n == 0:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-110-        return []\nartifacts/r11_3verifier_canonical.py-111-    ranked_indices = sorted(range(n), key=lambda i: p_values[i])\nartifacts/r11_3verifier_canonical.py:112:    adjusted = [0.0] * n\nartifacts/r11_3verifier_canonical.py-113-    for rank_idx, orig_idx in enumerate(ranked_indices):\nartifacts/r11_3verifier_canonical.py:114:        adjusted[orig_idx] = p_values[orig_idx] * n / (rank_idx + 1)\nartifacts/r11_3verifier_canonical.py-115-    for i in range(n - 2, -1, -1):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-116-        idx_curr = ranked_indices[i]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-117-        idx_next = ranked_indices[i + 1]\nartifacts/r11_3verifier_canonical.py:118:        adjusted[idx_curr] = min(adjusted[idx_curr], adjusted[idx_next])\nartifacts/r11_3verifier_canonical.py:119:    return [min(p, 1.0) for p in adjusted]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-120-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-121-\nartifacts/r11_3verifier_canonical.py-122-def run_nli_inference(model_name, model_path, pw_data, device):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-123-    \"\"\"Run NLI inference, return per-question predictions and probabilities.\"\"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-124-    print(f\"\\n{'='*60}\")\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-334-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-335-        sig = \"***\" if p_val < 0.001 else \"**\" if p_val < 0.01 else \"*\" if p_val < 0.05 else \"\"\nartifacts/r11_3verifier_canonical.py-336-        print(f\"  Ensemble w={w}: {combo_acc:.4f} ({combo_n_correct}), \"\nartifacts/r11_3verifier_canonical.py-337-              f\"Δ={delta_pp:+.2f}pp, b={b_count} c={c_count} p={p_val:.6f} {sig}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-338-\nartifacts/r11_3verifier_canonical.py:339:    # === Phase 5: BH correction ===\nartifacts/r11_3verifier_canonical.py:340:    print(\"\\n=== BH correction ===\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/r11_3verifier_canonical.py-341-    test_labels = [t[0] for t in all_tests]",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01F5jmsWKoZyhecKrFKcXbGv`</summary>

```json
{
  "command": "echo \"Abstract word count:\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/--/-/g' | wc -w",
  "description": "Count words in abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "bd784347-d511-4ca2-bd23-d65a38b7e17a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AGUGDCVYeScizGk2q3mM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5019,
      "cache_read_input_tokens": 24501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5019
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

_source line 20 · 2026-05-24T04:48:04.868Z_

<details><summary>↩ Tool result · `toolu_01F5jmsWKoZyhecKrFKcXbGv`</summary>

```text
Abstract word count:
192
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "ee68daa7-8bf6-4291-bfa9-1e10ea1d7a89",
  "tool_use_result": {
    "stdout": "Abstract word count:\n192",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
The abstract is 192 words — already under 200. Let me double-check by carefully counting.

Now for D1, the BH correction in the paper: The paper says m=6 confirmatory conditions, and two conditions (Mistral-7B ProofWriter p=0.014, Qwen2.5-14B ProofWriter p=0.011) have adjusted p=0.066.

But the BH code in r11_3verifier_significance.py is for a different analysis (3-verifier NLI combo). I need to find the code that computed BH correction for the main results table (m=6 confirmatory conditions).


I'm searching through the codebase to locate where the BH correction was applied to those specific p-values with m=6.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "df8f0603-b95b-4296-ae9a-722d23eaab87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHW1RXVMRQkJ5PY71V8hbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 29520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2809
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

_source line 22_

Let me find the main results BH correction code with m=6 and look for how the adjusted p=0.066 was computed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "dbff8615-2ff1-49e6-9df2-d807211b8e24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHW1RXVMRQkJ5PY71V8hbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 29520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2809
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

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_013pJuYEqmykQoKZ4VgfrWSj`</summary>

```json
{
  "pattern": "0\\.066|m.?=.?6|confirmatory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.py",
  "output_mode": "content",
  "-i": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "d6e188c9-15b2-4f3b-8c79-9974f4142aa3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHW1RXVMRQkJ5PY71V8hbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 29520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2809
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

_source line 24 · 2026-05-24T04:48:15.508Z_

<details><summary>↩ Tool result · `toolu_013pJuYEqmykQoKZ4VgfrWSj`</summary>

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
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "24822df4-e90a-461a-bb13-c54a19646e1b",
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

_source line 25_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mk8CbAVTgyiUScKPGFmdqQ`</summary>

```json
{
  "pattern": "0\\.066|m.?=.?6|confirmatory",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.json",
  "output_mode": "content",
  "-i": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "b9b433a8-50d7-4664-b7f7-151bb7ac9034",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHW1RXVMRQkJ5PY71V8hbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 29520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2809
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

_source line 26 · 2026-05-24T04:48:17.009Z_

<details><summary>↩ Tool result · `toolu_01Mk8CbAVTgyiUScKPGFmdqQ`</summary>

```text
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-263-      "length_weighted_accuracy": 0.7525,
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-264-      "constraint_count_accuracy": 0.7525,
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-265-      "all_nonsignificant": true,
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json:266:      "best_p_value": 0.066
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-267-    },
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-268-    "tables": [
artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-269-      "Appendix: Weighted SC comparison"
--
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-52-      "sica_accuracy": 0.4833,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-53-      "sc_accuracy": 0.4833,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-54-      "delta_pp": 0,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json:55:      "multi_candidate_rate": 0.0667,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-56-      "extraction_rate": 0.8819,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-57-      "answer_extraction_rate": 1,
checkpoints/exp-010-mistral-v3_DONE_20260517T082202.json-58-      "contradiction_rate": 0.0562,
--
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-20-      "inv_length_vs_sc_p": 0.453,
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-21-      "length_vs_sc_p": 0.153,
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-22-      "inv_length_vs_sica_p": 0.864,
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json:23:      "length_vs_sica_p": 0.066,
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-24-      "n_problems": 804,
checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-25-      "all_nonsignificant": true
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-26-    },
--
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-49-      "sica_accuracy": 0.4833,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-50-      "sc_accuracy": 0.4833,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-51-      "delta_pp": 0,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json:52:      "multi_candidate_rate": 0.0667,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-53-      "extraction_rate": 0.8819,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-54-      "answer_extraction_rate": 1,
checkpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-55-      "contradiction_rate": 0.0562,
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json-1-{
logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json-3-}
--
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-20-      "inv_length_vs_sc_p": 0.453,
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-21-      "length_vs_sc_p": 0.153,
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-22-      "inv_length_vs_sica_p": 0.864,
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json:23:      "length_vs_sica_p": 0.066,
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-24-      "n_problems": 804,
checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-25-      "all_nonsignificant": true
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-26-    },
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json-1-{
logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json-1-{
logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json-1-{
logs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json-1-{
logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json-1-{
logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json-1-{
logs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json-1-{
logs/workers/worker_analysis_bh-correction_20260520T152347_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_appendix_20260517T184655_result.json-1-{
logs/workers/worker_paper_writing_appendix_20260517T184655_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_appendix_20260517T184655_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json-1-{
logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json-3-}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json-1-{
logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json-3-}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "f46e8053-6332-45e0-a148-7b193983f655",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-263-      \"length_weighted_accuracy\": 0.7525,\nartifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-264-      \"constraint_count_accuracy\": 0.7525,\nartifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-265-      \"all_nonsignificant\": true,\nartifacts/dream_reports/dream_20260519T034058/best/experiment_data.json:266:      \"best_p_value\": 0.066\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-267-    },\nartifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-268-    \"tables\": [\nartifacts/dream_reports/dream_20260519T034058/best/experiment_data.json-269-      \"Appendix: Weighted SC comparison\"\n--\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-52-      \"sica_accuracy\": 0.4833,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-53-      \"sc_accuracy\": 0.4833,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-54-      \"delta_pp\": 0,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json:55:      \"multi_candidate_rate\": 0.0667,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-56-      \"extraction_rate\": 0.8819,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-57-      \"answer_extraction_rate\": 1,\ncheckpoints/exp-010-mistral-v3_DONE_20260517T082202.json-58-      \"contradiction_rate\": 0.0562,\n--\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json-20-      \"inv_length_vs_sc_p\": 0.453,\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json-21-      \"length_vs_sc_p\": 0.153,\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json-22-      \"inv_length_vs_sica_p\": 0.864,\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json:23:      \"length_vs_sica_p\": 0.066,\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json-24-      \"n_problems\": 804,\ncheckpoints/exp-016-weighted-sc_DONE_20260517T010216.json-25-      \"all_nonsignificant\": true\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/checkpoints/exp-016-weighted-sc_DONE_20260517T010216.json-26-    },\n--\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-49-      \"sica_accuracy\": 0.4833,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-50-      \"sc_accuracy\": 0.4833,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-51-      \"delta_pp\": 0,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json:52:      \"multi_candidate_rate\": 0.0667,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-53-      \"extraction_rate\": 0.8819,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-54-      \"answer_extraction_rate\": 1,\ncheckpoints/exp-010-mistral-v3_ANALYZING_20260517T082139.json-55-      \"contradiction_rate\": 0.0562,\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json-1-{\nlogs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_c0-definition-rollback_20260517T133946_result.json-3-}\n--\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-20-      \"inv_length_vs_sc_p\": 0.453,\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-21-      \"length_vs_sc_p\": 0.153,\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-22-      \"inv_length_vs_sica_p\": 0.864,\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json:23:      \"length_vs_sica_p\": 0.066,\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-24-      \"n_problems\": 804,\ncheckpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-25-      \"all_nonsignificant\": true\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/checkpoints/exp-016-weighted-sc_QUEUED_20260517T010210.json-26-    },\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json-1-{\nlogs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-numbers_20260524T042807_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json-1-{\nlogs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_fix_multi-candidate-rate_20260517T132002_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json-1-{\nlogs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-080-completion-check_20260519T203431_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json-1-{\nlogs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json-1-{\nlogs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json-1-{\nlogs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_cpu-ablations_20260518T155725_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json-1-{\nlogs/workers/worker_analysis_bh-correction_20260520T152347_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_appendix_20260517T184655_result.json-1-{\nlogs/workers/worker_paper_writing_appendix_20260517T184655_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_paper_writing_appendix_20260517T184655_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json-1-{\nlogs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json-3-}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json-1-{\nlogs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json:2:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_exp-016-weighted-sc_20260516T204729_result.json-3-}",
    "numLines": 83
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_01ENLdmD9dqVU5yMcD3ChQRy`</summary>

```json
{
  "pattern": "0\\.014|0\\.011",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "glob": "*.py",
  "output_mode": "content",
  "-i": true,
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a4a206f8-a751-4fde-aa23-c6bee9abc9a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHW1RXVMRQkJ5PY71V8hbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2809,
      "cache_read_input_tokens": 29520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2809
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

_source line 28 · 2026-05-24T04:48:18.122Z_

<details><summary>↩ Tool result · `toolu_01ENLdmD9dqVU5yMcD3ChQRy`</summary>

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
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "e7c2ce44-bbc4-4bea-83e2-40992564843b",
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

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Let me read the BH correction analysis worker result to understand what happened, and also find the analysis code that produced the p=0.066.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "132f90ed-eab8-43af-8615-1a1582aca569",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkveQZxVr9JeCBcee2kDfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4124,
      "cache_read_input_tokens": 32329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4124
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

_source line 30_

Let me read the BH correction analysis result and find the actual computation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "e71c19ae-b90e-413b-88d1-d430beaa6607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkveQZxVr9JeCBcee2kDfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4124,
      "cache_read_input_tokens": 32329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4124
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

<details open><summary>🔧 Tool call — Read · `toolu_01EeoK9EDj4YoZ1h5pb4ahXh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "019fe254-3eac-44a2-b9b5-2fd297aeacdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkveQZxVr9JeCBcee2kDfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4124,
      "cache_read_input_tokens": 32329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4124
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

_source line 32 · 2026-05-24T04:48:23.465Z_

<details><summary>↩ Tool result · `toolu_01EeoK9EDj4YoZ1h5pb4ahXh`</summary>

```text
1	{
2	  "raw": "全部结果如下：\n\n## 6 个 raw p-values\n\n| Comparison | b | c | n | raw p |\n|---|---|---|---|---|\n| FOLIO w=1 | 0 | 4 | 4 | 0.1250 |\n| FOLIO w=3 | 5 | 11 | 16 | 0.2101 |\n| **FOLIO w=5** | **7** | **16** | **23** | **0.0931** |\n| PW w=1 | 4 | 9 | 13 | 0.2668 |\n| PW w=3 | 22 | 43 | 65 | 0.0125 |\n| **PW w=5** | **35** | **99** | **134** | **2.89×10⁻⁸** |\n\n## BH 校正表 (α=0.05, m=6)\n\n| Rank | Comparison | raw p | BH threshold | adj p (BH) | Survives? |\n|---|---|---|---|---|---|\n| 1 | PW w=5 | 2.89×10⁻⁸ | 0.0083 | 1.73×10⁻⁷ | **YES** |\n| 2 | PW w=3 | 0.0125 | 0.0167 | 0.0375 | **YES** |\n| 3 | FOLIO w=5 | 0.0931 | 0.0250 | 0.1863 | no |\n| 4 | FOLIO w=1 | 0.1250 | 0.0333 | 0.1875 | no |\n| 5 | FOLIO w=3 | 0.2101 | 0.0417 | 0.2521 | no |\n| 6 | PW w=1 | 0.2668 | 0.0500 | 0.2668 | no |\n\n## 结论\n\n**2/6 comparisons survive BH at α=0.05:**\n- **PW w=5**: raw p=2.89×10⁻⁸, adj p=1.73×10⁻⁷\n- **PW w=3**: raw p=0.0125 < threshold 0.0167, adj p=0.0375\n\n关键验证：PW w=3 排在 rank 2，BH threshold = (2/6)×0.05 = 0.0167，raw p=0.0125 < 0.0167 → survives。"
3	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "bc86bfae-bccd-4734-9645-88f98ee881fe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/worker_analysis_bh-correction_20260520T152347_result.json",
      "content": "{\n  \"raw\": \"全部结果如下：\\n\\n## 6 个 raw p-values\\n\\n| Comparison | b | c | n | raw p |\\n|---|---|---|---|---|\\n| FOLIO w=1 | 0 | 4 | 4 | 0.1250 |\\n| FOLIO w=3 | 5 | 11 | 16 | 0.2101 |\\n| **FOLIO w=5** | **7** | **16** | **23** | **0.0931** |\\n| PW w=1 | 4 | 9 | 13 | 0.2668 |\\n| PW w=3 | 22 | 43 | 65 | 0.0125 |\\n| **PW w=5** | **35** | **99** | **134** | **2.89×10⁻⁸** |\\n\\n## BH 校正表 (α=0.05, m=6)\\n\\n| Rank | Comparison | raw p | BH threshold | adj p (BH) | Survives? |\\n|---|---|---|---|---|---|\\n| 1 | PW w=5 | 2.89×10⁻⁸ | 0.0083 | 1.73×10⁻⁷ | **YES** |\\n| 2 | PW w=3 | 0.0125 | 0.0167 | 0.0375 | **YES** |\\n| 3 | FOLIO w=5 | 0.0931 | 0.0250 | 0.1863 | no |\\n| 4 | FOLIO w=1 | 0.1250 | 0.0333 | 0.1875 | no |\\n| 5 | FOLIO w=3 | 0.2101 | 0.0417 | 0.2521 | no |\\n| 6 | PW w=1 | 0.2668 | 0.0500 | 0.2668 | no |\\n\\n## 结论\\n\\n**2/6 comparisons survive BH at α=0.05:**\\n- **PW w=5**: raw p=2.89×10⁻⁸, adj p=1.73×10⁻⁷\\n- **PW w=3**: raw p=0.0125 < threshold 0.0167, adj p=0.0375\\n\\n关键验证：PW w=3 排在 rank 2，BH threshold = (2/6)×0.05 = 0.0167，raw p=0.0125 < 0.0167 → survives。\"\n}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01CZTa6T64z8tkVmBuSYDPF7`</summary>

```json
{
  "pattern": "bh.*correct|main.*result.*p|mcnemar|confirmatory|0\\.014|0\\.011",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts",
  "glob": "*.py",
  "output_mode": "content",
  "-i": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "223165dd-028f-4287-bc30-5142e8b33803",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkveQZxVr9JeCBcee2kDfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4124,
      "cache_read_input_tokens": 32329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4124
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

_source line 34 · 2026-05-24T04:48:25.731Z_

<details><summary>↩ Tool result · `toolu_01CZTa6T64z8tkVmBuSYDPF7`</summary>

```text
&lt;persisted-output>
Output too large (26KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/88dd4cac-745e-4701-a7b3-bec955cff63c/tool-results/toolu_01CZTa6T64z8tkVmBuSYDPF7.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-27-    return problem_text, ""
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-28-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-29-
artifacts/d116_qwen3_pw_deberta_large.py:30:def mcnemar_test(b, c):
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-31-    n = b + c
artifacts/d116_qwen3_pw_deberta_large.py-32-    if n == 0:
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-33-        return 1.0
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-169-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-170-        combo_acc = combo_correct / total
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-171-        delta = combo_acc - sc_acc
artifacts/d116_qwen3_pw_deberta_large.py:172:        p_val = mcnemar_test(b_count, c_count)
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-173-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-174-        combo_results[w] = {
artifacts/d116_qwen3_pw_deberta_large.py-175-            "accuracy": round(combo_acc, 4),
artifacts/d116_qwen3_pw_deberta_large.py-176-            "correct": combo_correct,
artifacts/d116_qwen3_pw_deberta_large.py-177-            "delta_vs_sc": round(delta, 4),
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "9865d7f6-46cc-4872-bb80-2b7bbaee73b3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-27-    return problem_text, \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-28-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-29-\nartifacts/d116_qwen3_pw_deberta_large.py:30:def mcnemar_test(b, c):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-31-    n = b + c\nartifacts/d116_qwen3_pw_deberta_large.py-32-    if n == 0:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-33-        return 1.0\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-169-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-170-        combo_acc = combo_correct / total\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-171-        delta = combo_acc - sc_acc\nartifacts/d116_qwen3_pw_deberta_large.py:172:        p_val = mcnemar_test(b_count, c_count)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-173-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-174-        combo_results[w] = {\nartifacts/d116_qwen3_pw_deberta_large.py-175-            \"accuracy\": round(combo_acc, 4),\nartifacts/d116_qwen3_pw_deberta_large.py-176-            \"correct\": combo_correct,\nartifacts/d116_qwen3_pw_deberta_large.py-177-            \"delta_vs_sc\": round(delta, 4),\nartifacts/d116_qwen3_pw_deberta_large.py-178-            \"delta_pp\": round(delta * 100, 2),\nartifacts/d116_qwen3_pw_deberta_large.py:179:            \"mcnemar_b\": b_count,\nartifacts/d116_qwen3_pw_deberta_large.py:180:            \"mcnemar_c\": c_count,\nartifacts/d116_qwen3_pw_deberta_large.py:181:            \"mcnemar_n_discordant\": b_count + c_count,\nartifacts/d116_qwen3_pw_deberta_large.py:182:            \"mcnemar_p\": round(p_val, 4)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-183-        }\nartifacts/d116_qwen3_pw_deberta_large.py-184-        print(f\"  w={w}: {combo_acc:.4f} ({combo_correct}/{total}), Δ={delta*100:+.2f}pp, p={p_val:.4f}, discordant=[{b_count},{c_count}]\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-185-\n--\nartifacts/d116_qwen3_pw_deberta_large.py-215-            f\"w{w}\": {\nartifacts/d116_qwen3_pw_deberta_large.py-216-                \"accuracy\": combo_results[w][\"accuracy\"],\nartifacts/d116_qwen3_pw_deberta_large.py-217-                \"delta_pp\": combo_results[w][\"delta_pp\"],\nartifacts/d116_qwen3_pw_deberta_large.py:218:                \"mcnemar_p\": combo_results[w][\"mcnemar_p\"],\nartifacts/d116_qwen3_pw_deberta_large.py:219:                \"discordant\": [combo_results[w][\"mcnemar_b\"], combo_results[w][\"mcnemar_c\"]]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-220-            }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-221-            for w in WEIGHTS\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/d116_qwen3_pw_deberta_large.py-222-        },\n--\nartifacts/mcnemar_recompute.py:1:\"\"\"McNemar exact test recomputation after SC tiebreaking fix.\"\"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-2-import json\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-3-import sys\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-4-from pathlib import Path\n--\nartifacts/mcnemar_recompute.py-23-    return max(sorted(vote_dist.keys()), key=lambda k: vote_dist[k])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-24-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-25-\nartifacts/mcnemar_recompute.py:26:def compute_mcnemar(exp_info):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-27-    path = Path(exp_info[\"path\"])\nartifacts/mcnemar_recompute.py-28-    if not path.exists():\nartifacts/mcnemar_recompute.py-29-        return {\"exp_id\": exp_info[\"exp_id\"], \"error\": f\"File not found: {path}\"}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-132-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-133-    all_results = []\nartifacts/mcnemar_recompute.py-134-    for exp in experiments:\nartifacts/mcnemar_recompute.py:135:        r = compute_mcnemar(exp)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-136-        all_results.append(r)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-137-\nartifacts/mcnemar_recompute.py:138:    header = f\"{'Exp':<14} {'n':>4} {'NewSC%':>8} {'SICA%':>8} {'D(pp)':>8} {'b':>4} {'c':>4} {'McNemar_p':>12} {'Sig':>5}\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-139-    print(header)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-140-    print(\"-\" * len(header))\nartifacts/mcnemar_recompute.py-141-    for r in all_results:\n--\nartifacts/mcnemar_recompute.py-145-        print(f\"{r['exp_id']:<14} {r['n']:>4} {r['new_sc_pct']:>7.2f}% {r['sica_pct']:>7.2f}% {r['delta_pp']:>+7.2f} {r['b_sc_correct_sica_wrong']:>4} {r['c_sc_wrong_sica_correct']:>4} {r['p_value']:>12.6f} {r['sig']:>5}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-146-\nartifacts/mcnemar_recompute.py-147-    out = {\"server\": f\"westd-{server}\", \"results\": all_results}\nartifacts/mcnemar_recompute.py:148:    out_path = Path(f\"/root/symb_invariant_consensus/results/mcnemar_recomputed_{server}.json\")\nartifacts/mcnemar_recompute.py-149-    with open(out_path, \"w\") as f:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-150-        json.dump(out, f, indent=2)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/mcnemar_recompute.py-151-    print(f\"\\nSaved to {out_path}\")\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-36-    return premise, hypothesis\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-37-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-38-\nartifacts/push_b_stronger_nli.py:39:def mcnemar_test(correct_a, correct_b):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-40-    b = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-41-    c = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-42-    n = b + c\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-198-            combo_correct = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-199-            combo_acc = sum(combo_correct) / len(pids)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-200-            delta = combo_acc - sc_acc\nartifacts/push_b_stronger_nli.py:201:            p, b, c = mcnemar_test(sc_correct_list, combo_correct)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-202-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-203-            results[f\"w{w}\"] = {\nartifacts/push_b_stronger_nli.py-204-                \"accuracy\": round(combo_acc, 4),\nartifacts/push_b_stronger_nli.py-205-                \"correct\": sum(combo_correct),\nartifacts/push_b_stronger_nli.py-206-                \"delta_pp\": round(delta * 100, 2),\nartifacts/push_b_stronger_nli.py:207:                \"mcnemar_p\": round(p, 6),\nartifacts/push_b_stronger_nli.py-208-                \"discordant\": [b, c],\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/push_b_stronger_nli.py-209-            }\nartifacts/push_b_stronger_nli.py-210-            print(f\"  w={w}: {combo_acc:.4f} ({sum(combo_correct)}/{len(pids)}), \"\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-1-import json\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-2-from math import comb\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-3-\nartifacts/recompute_folio_sc.py:4:def mcnemar_exact_pvalue(b, c):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-5-    n = b + c\nartifacts/recompute_folio_sc.py-6-    if n == 0:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-7-        return 1.0\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-71-    sica_corr = sum(1 for c in subset if c[\"sica_correct\"])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-72-    b = sum(1 for c in subset if c[\"sica_correct\"] and not c[\"new_sc_correct\"])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-73-    c_val = sum(1 for c in subset if not c[\"sica_correct\"] and c[\"new_sc_correct\"])\nartifacts/recompute_folio_sc.py:74:    p = mcnemar_exact_pvalue(b, c_val)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-75-    row = {\nartifacts/recompute_folio_sc.py-76-        \"group\": f\"FOLIO-204/{label}\",\nartifacts/recompute_folio_sc.py-77-        \"n\": n,\n--\nartifacts/recompute_folio_sc.py-80-        \"sica_correct\": sica_corr,\nartifacts/recompute_folio_sc.py-81-        \"sica_accuracy\": round(sica_corr / n, 4),\nartifacts/recompute_folio_sc.py-82-        \"delta_pp\": round((sica_corr - sc_corr) / n, 4),\nartifacts/recompute_folio_sc.py:83:        \"mcnemar_b_sica_plus_sc_minus\": b,\nartifacts/recompute_folio_sc.py:84:        \"mcnemar_c_sica_minus_sc_plus\": c_val,\nartifacts/recompute_folio_sc.py:85:        \"mcnemar_exact_p\": round(p, 6),\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-86-    }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-87-    answer_type_results.append(row)\nartifacts/recompute_folio_sc.py-88-    print(f\"  {label}: n={n}, SC={sc_corr}/{n}={sc_corr/n:.4f}, SICA={sica_corr}/{n}={sica_corr/n:.4f}, Δ={row['delta_pp']}, b={b}, c={c_val}, p={p:.6f}\")\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-90-# Overall\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-91-b_all = sum(1 for c in corrected if c[\"sica_correct\"] and not c[\"new_sc_correct\"])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-92-c_all = sum(1 for c in corrected if not c[\"sica_correct\"] and c[\"new_sc_correct\"])\nartifacts/recompute_folio_sc.py:93:p_all = mcnemar_exact_pvalue(b_all, c_all)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-94-overall_row = {\nartifacts/recompute_folio_sc.py-95-    \"group\": \"FOLIO-204/Overall\",\nartifacts/recompute_folio_sc.py-96-    \"n\": total,\n--\nartifacts/recompute_folio_sc.py-99-    \"sica_correct\": sica_total,\nartifacts/recompute_folio_sc.py-100-    \"sica_accuracy\": round(sica_total / total, 4),\nartifacts/recompute_folio_sc.py-101-    \"delta_pp\": round((sica_total - new_sc_total) / total, 4),\nartifacts/recompute_folio_sc.py:102:    \"mcnemar_b_sica_plus_sc_minus\": b_all,\nartifacts/recompute_folio_sc.py:103:    \"mcnemar_c_sica_minus_sc_plus\": c_all,\nartifacts/recompute_folio_sc.py:104:    \"mcnemar_exact_p\": round(p_all, 6),\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-105-}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-106-answer_type_results.append(overall_row)\nartifacts/recompute_folio_sc.py-107-print(f\"  Overall: n={total}, SC={new_sc_total}/{total}={new_sc_total/total:.4f}, SICA={sica_total}/{total}={sica_total/total:.4f}, Δ={overall_row['delta_pp']}, b={b_all}, c={c_all}, p={p_all:.6f}\")\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-128-    sica_corr = sum(1 for c in subset if c[\"sica_correct\"])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-129-    b = sum(1 for c in subset if c[\"sica_correct\"] and not c[\"new_sc_correct\"])\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-130-    c_val = sum(1 for c in subset if not c[\"sica_correct\"] and c[\"new_sc_correct\"])\nartifacts/recompute_folio_sc.py:131:    p = mcnemar_exact_pvalue(b, c_val)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-132-    counts = [c[\"constraint_count\"] for c in subset]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-133-    mean_c = round(sum(counts) / len(counts), 1)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/recompute_folio_sc.py-134-    min_c, max_c = min(counts), max(counts)\n--\nartifacts/recompute_folio_sc.py-140-        \"sica_correct\": sica_corr,\nartifacts/recompute_folio_sc.py-141-        \"sica_accuracy\": round(sica_corr / n, 4),\nartifacts/recompute_folio_sc.py-142-        \"delta_pp\": round((sica_corr - sc_corr) / n, 4),\nartifacts/recompute_folio_sc.py:143:        \"mcnemar_b_sica_plus_sc_minus\": b,\nartifacts/recompute_folio_sc.py:144:        \"mcnemar_c_sica_minus_sc_plus\": c_val,\nartifacts/recompute_folio_sc.py:145:        \"mcnemar_exact_p\": round(p, 6),\nartifacts/recompute_folio_sc.py-146-        \"constraint_range\": f\"[{min_c}, {max_c}]\",\nartifacts/recompute_folio_sc.py-147-        \"mean_constraints\": mean_c,\nartifacts/recompute_folio_sc.py-148-        \"tertile_thresholds\": thresholds,\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-3-import json, math\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-4-from scipy.stats import norm\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-5-\nartifacts/compute_tost_sensitivity.py:6:with open(\"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/table1_bh_correction.json\") as f:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-7-    data = json.load(f)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-8-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-9-conditions = data[\"conditions\"]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-10-\nartifacts/compute_tost_sensitivity.py-11-def derive_se(cond):\nartifacts/compute_tost_sensitivity.py:12:    \"\"\"Derive SE of proportion difference from McNemar z-statistic.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-13-\nartifacts/compute_tost_sensitivity.py-14-    For raw_p < 1.0: SE = |delta| / |z| where z from two-sided p.\nartifacts/compute_tost_sensitivity.py-15-    For raw_p = 1.0: estimate using paired proportion model with assumed\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-102-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-103-output = {\nartifacts/compute_tost_sensitivity.py-104-    \"margins_pp\": margins,\nartifacts/compute_tost_sensitivity.py:105:    \"method\": \"TOST via paired proportion z-test. SE derived from McNemar z-statistic where raw_p < 1.0; \"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_tost_sensitivity.py-106-              \"estimated via paired proportion model (r=0.95 inter-method correlation) where raw_p = 1.0.\",\nartifacts/compute_tost_sensitivity.py-107-    \"conditions\": results,\nartifacts/compute_tost_sensitivity.py-108-    \"summary\": summary,\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-106-    return per_problem\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-107-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-108-\nartifacts/ablation_text.py:109:def compute_mcnemar(per_problem_results):\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-110-    b = 0  # SC correct, SICA wrong\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-111-    c = 0  # SC wrong, SICA correct\nartifacts/ablation_text.py-112-    for r in per_problem_results:\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-191-        sica_acc = sica_correct / n\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-192-        sc_acc = sc_correct / n\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-193-        delta_pp = (sica_acc - sc_acc) * 100\nartifacts/ablation_text.py:194:        mcnemar_p, b, c = compute_mcnemar(per_problem)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-195-        mean_constraints = sum(r[\"n_constraints_total\"] for r in per_problem) / n\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-196-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-197-        entry = {\n--\nartifacts/ablation_text.py-199-            \"sc_acc\": round(sc_acc, 4),\nartifacts/ablation_text.py-200-            \"sica_acc\": round(sica_acc, 4),\nartifacts/ablation_text.py-201-            \"delta_pp\": round(delta_pp, 2),\nartifacts/ablation_text.py:202:            \"mcnemar_p\": round(mcnemar_p, 6),\nartifacts/ablation_text.py:203:            \"mcnemar_b\": b,\nartifacts/ablation_text.py:204:            \"mcnemar_c\": c,\nartifacts/ablation_text.py-205-            \"n_constraints_mean\": round(mean_constraints, 1),\nartifacts/ablation_text.py-206-            \"sica_correct\": sica_correct,\nartifacts/ablation_text.py-207-            \"sc_correct\": sc_correct,\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-210-        all_results.append(entry)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-211-        logger.info(\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-212-            \"T_ext=%.1f  SC=%.1f%%  SICA=%.1f%%  Δ=%.1fpp  p=%.4f  constraints_mean=%.1f\",\nartifacts/ablation_text.py:213:            t_ext, sc_acc * 100, sica_acc * 100, delta_pp, mcnemar_p, mean_constraints,\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-214-        )\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-215-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-216-    output = {\n--\nartifacts/ablation_text.py-238-    for r in all_results:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-239-        print(\nartifacts/ablation_text.py-240-            f\"{r['t_ext']:6.1f} {r['sc_acc']*100:6.1f} {r['sica_acc']*100:7.1f} \"\nartifacts/ablation_text.py:241:            f\"{r['delta_pp']:+6.1f} {r['mcnemar_p']:8.4f} {r['n_constraints_mean']:8.1f}\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-242-        )\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-243-    print(\"=\" * 70)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/ablation_text.py-244-\n--\nartifacts/direction_r_deberta_proofwriter.py-168-    for weight in [1, 3]:\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-169-        combo_correct = 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-170-        combo_preds = {}\nartifacts/direction_r_deberta_proofwriter.py:171:        # McNemar: b = SC correct & combo wrong, c = SC wrong & combo correct\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-172-        b_count = 0\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-173-        c_count = 0\nartifacts/direction_r_deberta_proofwriter.py-174-        for qid in gt:\n--\nartifacts/direction_r_deberta_proofwriter.py-206-            \"correct\": combo_correct,\nartifacts/direction_r_deberta_proofwriter.py-207-            \"delta_vs_sc\": round(delta, 4),\nartifacts/direction_r_deberta_proofwriter.py-208-            \"delta_pp\": round(delta * 100, 2),\nartifacts/direction_r_deberta_proofwriter.py:209:            \"mcnemar_b\": b_count,\nartifacts/direction_r_deberta_proofwriter.py:210:            \"mcnemar_c\": c_count,\nartifacts/direction_r_deberta_proofwriter.py:211:            \"mcnemar_n_discordant\": n_disc,\nartifacts/direction_r_deberta_proofwriter.py:212:            \"mcnemar_p\": round(p_val, 6)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-213-        }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-214-        sig = \"***\" if p_val < 0.001 else \"**\" if p_val < 0.01 else \"*\" if p_val < 0.05 else \"\"\nartifacts/direction_r_deberta_proofwriter.py-215-        print(f\"  w={weight}: acc={combo_acc:.4f} ({combo_correct}/{total}), \"\nartifacts/direction_r_deberta_proofwriter.py-216-              f\"delta={delta:+.4f} ({delta*100:+.2f}pp), \"\nartifacts/direction_r_deberta_proofwriter.py:217:              f\"McNemar b={b_count} c={c_count} p={p_val:.4f} {sig}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-218-\nartifacts/direction_r_deberta_proofwriter.py-219-    print(f\"\\n  SC baseline: {sc_acc:.4f}\")\nartifacts/direction_r_deberta_proofwriter.py-220-    print(f\"  SICA baseline: {sica_acc:.4f}\")\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-252-        sica_combo_results[weight] = {\nartifacts/direction_r_deberta_proofwriter.py-253-            \"accuracy\": round(sica_combo_acc, 4),\nartifacts/direction_r_deberta_proofwriter.py-254-            \"delta_vs_sica\": round(sica_delta, 4),\nartifacts/direction_r_deberta_proofwriter.py:255:            \"mcnemar_b\": b_s, \"mcnemar_c\": c_s, \"mcnemar_p\": round(p_val_s, 6)\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-256-        }\nartifacts/direction_r_deberta_proofwriter.py-257-        print(f\"  w={weight} vs SICA: acc={sica_combo_acc:.4f}, delta={sica_delta:+.4f}, p={p_val_s:.4f}\")\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/direction_r_deberta_proofwriter.py-258-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/compute_cil.py-276-        bh_gen = bh_table.get(\"generators\", {}).get(gen_name, {})\nartifacts/compute_cil.py-277-        if bh_gen:\nartifacts/compute_cil.py-278-            print(f\"  {gen_name}: data on westd-16639, adding BH-derived entry\")",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
The BH correction result I found is from the 3-verifier NLI combo analysis (worker_analysis_bh-correction), which is about a different part of the paper. I need to find the BH correction for the main SICA results table (experiments.tex line 5).

The paper says m=6 confirmatory conditions, and two have raw p = 0.014 and 0.011, both reaching adjusted p = 0.066. Let me verify this manually.

With m=6 confirmatory conditions, the 6 p-values would need to be identified. 

Looking at Table 1, I need to identify which conditions are marked as confirmatory versus exploratory. The table caption indicates m=6 confirmatory with the rest exploratory. From what I can see, Mistral-7B PW-D5 shows p=0.014 as confirmatory, while other entries like LogiQA and the FOLIO variants appear to be either confirmatory or exploratory based on whether they're individual seeds or aggregates. Now I'm looking at the remaining Qwen3 results and trying to parse the table caption to understand which conditions are actually confirmatory versus exploratory. The caption indicates that 3-seed and 4-seed aggregates have different statuses, while individual seed runs and multi-seed extensions are exploratory, but I need to clarify exactly which results fall into the confirmatory category. Now I'm identifying which conditions are exploratory versus confirmatory. The exploratory ones include the individual seed runs for Mistral-7B on FOLIO, the aggregate versions, Qwen2.5-14B's gold ICL condition, and anything involving Qwen3 or Qwen2.5-7B. That leaves me with six confirmatory p-values to correct: 0.014, 0.581, 0.093, 0.424, 0.011, and 0.625. Let me sort these and apply the Benjamini-Hochberg correction.

I'm computing the adjusted p-values by multiplying each sorted p-value by the total count divided by its rank, then enforcing monotonicity from the largest p-value upward to ensure the sequence is non-decreasing. I need to recalculate the Benjamini-Hochberg adjustments properly by sorting p-values from smallest to largest, multiplying each by m/i, then enforcing monotonicity constraints from the largest index backward to ensure adjusted p-values don't decrease as you move up the sorted list. Let me recalculate this more carefully using the standard Benjamini-Hochberg procedure. I need to compute the adjusted p-values as the minimum of p_(j) * m / j for all j ≥ i, working through the sorted p-values systematically. ) = min(0.011 * 6/1, adj_(2)) = min(0.066, 0.042) = 0.042

So the correct values should be:
- Qwen2.5-14B PW (p=0.011): adj_p = 0.042
- Mistral-7B PW (p=0.014): adj_p = 0.042

Both are < 0.05, so both are significant!

The paper says "adjusted p = 0.066" — this appears to be a bug! They seem to have computed 0.011 * 6 / 1 = 0.066 for the smallest p-value and then assigned that same value to both, without applying the monotonicity enforcement step. The 0.066 is indeed the unadjusted formula for rank 1, but after monotonicity enforcement (which makes all values non-decreasing from right to left), both should actually be 0.042.

Let me reconsider whether they applied the BH formula correctly or if m=6 means something different. Looking back at the caption, it says "m=6 confirmatory; remaining exploratory" and the text mentions "BH, m=6 confirmatory conditions; multi-seed aggregates and extensions are exploratory." I need to identify which 6 conditions are actually confirmatory by examining the table more carefully to see which results they're applying the correction to. I'm seeing the pattern now—unmarked entries are single-seed exploratory runs, while those with special markers like multi-seed aggregates are the exploratory variants. So the confirmatory runs must be the ones with explicit markers, but I need to figure out which six actually count as confirmatory versus exploratory based on how they're labeled in the table. Looking at the marked conditions more carefully, I'm seeing that the 4-seed aggregate for Qwen2.5-14B is indeed marked as confirmatory in the caption. So if I treat that as confirmatory and compile the results, I get six conditions with p-values ranging from 0.011 to 1.000, with the Qwen model showing a perfect p-value on the FOLIO task.

Now I'm applying the Benjamini-Hochberg correction to these six p-values, sorting them and calculating the adjusted values by multiplying each by the ratio of total tests to its rank. I'm then enforcing monotonicity from right to left to ensure the adjusted p-values don't decrease as I move through the sorted list.

I'm noticing that regardless of which six tests I select as confirmatory, as long as only two have p-values below 0.1 and the rest are much larger, the monotonicity constraint will always reduce the rank-1 adjusted p-value from 0.066 down further.

The key insight is that the rank-2 adjusted p-value determines whether rank-1 stays put or decreases—if rank-2's adjusted value is less than 0.066, then monotonicity forces rank-1 down to match it. In our case with p-values of 0.014 and 0.011, this definitely happens, giving us 0.042.

Now I'm wondering whether the paper author might have skipped the monotonicity step entirely and just computed the Benjamini-Hochberg adjustment directly without enforcing that constraint.

Let me check what the raw calculations would give: 0.011 × 6/1 = 0.066 and 0.014 × 6/2 = 0.042. Without monotonicity, those would be different values, but the paper claims both reach 0.066. That's puzzling.

Maybe they used a simpler correction altogether—just multiplying each p-value by the total number of tests without the ranking component. That would give 0.011 × 6 = 0.066 and 0.014 × 6 = 0.084, which still doesn't match "both equal 0.066."

Bonferroni would produce the same results, so that's not it either. I need to look more carefully at what the paper actually says about these two conditions.

Re-reading the passage, they mention two confirmatory conditions with degradation: Mistral-7B on ProofWriter (p = 0.014) and Qwen2.5-14B on ProofWriter (p = 0.011), and both reach adjusted p = 0.066. This phrasing is confusing—maybe they're saying the smallest adjusted p-value across all tests is 0.066, which would be the rank-1 result, and neither condition actually survives correction. But that's misleading because the standard Benjamini-Hochberg procedure would adjust the second one to 0.042, allowing it to pass at typical significance thresholds.

The most plausible explanation is they applied a Bonferroni-like correction (multiplying by 6) to both p-values rather than using the proper Benjamini-Hochberg ranking procedure. Let me verify this computationally by identifying exactly which six conditions they're treating as confirmatory and checking the math.

Looking back at the table caption, unmarked single-seed conditions are exploratory, while the 4-seed aggregate is explicitly marked as confirmatory. I need to figure out which of the main conditions without markers count as the six confirmatory ones. I'm counting up the conditions listed and getting 10, but the text mentions m=6 confirmatory conditions, which doesn't match. Looking back at the notation explanation, "unmarked: single-seed exploratory" was specifically describing how the FOLIO results were labeled—unmarked conditions are single-seed exploratory runs, while marked ones (s123/s456/s789) are individual seed runs. But now I'm realizing the main table is actually mixing both confirmatory and exploratory conditions together, so I need to figure out which ones are actually confirmatory. I'm settling on a configuration with one model-dataset pair per model, plus the Qwen2.5-14B results across multiple datasets to get to six confirmatory conditions total. Now I need to look up what actually qualifies as confirmatory in this context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "17c6f72d-5981-434c-a7c7-8734e00c2281",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un41QksXfoQtnhVxaeKN9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2025
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

_source line 36_

Let me find what defines the 6 confirmatory conditions and verify the BH computation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "c4fc8c9e-8467-4de1-8fba-dba2d9944468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un41QksXfoQtnhVxaeKN9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2025
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

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01JRf77GtX9zMqrznHhitPPf`</summary>

```json
{
  "pattern": "confirmatory|6.*condition|pre.?registered",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "output_mode": "content",
  "-i": true,
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "473f5976-f48a-4d8f-acbe-7b8bc55a93f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un41QksXfoQtnhVxaeKN9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2025
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

_source line 38 · 2026-05-24T04:50:10.467Z_

<details><summary>↩ Tool result · `toolu_01JRf77GtX9zMqrznHhitPPf`</summary>

```text
&lt;persisted-output>
Output too large (30.5KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/88dd4cac-745e-4701-a7b3-bec955cff63c/tool-results/toolu_01JRf77GtX9zMqrznHhitPPf.txt

Preview (first 2KB):
docs/paper/analysis.tex-37-\looseness=-1 Two controls rule out answer leakage: BR is uniform across reasoning steps (Fisher $p = 0.71$), and removing answer sentences before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite accuracy loss (McNemar $p < 0.013$). The bias reflects a distributional prior embedded throughout reasoning, not answer contamination.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-38-
docs/paper/analysis.tex-39-\label{sec:process-kappa}
docs/paper/analysis.tex:40:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-41-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-42-\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a persistent empirical property of zero-shot self-extraction pipelines.
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-43-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-48-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-49-\smallskip\noindent
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-50-\textit{Empirical support.}\;%
docs/paper/analysis.tex:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-52-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-53-\smallskip\noindent
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "69a1cc0c-6576-44bb-b065-f85e93954b66",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex-37-\\looseness=-1 Two controls rule out answer leakage: BR is uniform across reasoning steps (Fisher $p = 0.71$), and removing answer sentences before extraction yields no BR decrease (Wilcoxon $p \\geq 0.12$) despite accuracy loss (McNemar $p < 0.013$). The bias reflects a distributional prior embedded throughout reasoning, not answer contamination.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-38-\ndocs/paper/analysis.tex-39-\\label{sec:process-kappa}\ndocs/paper/analysis.tex:40:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-41-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-42-\\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a persistent empirical property of zero-shot self-extraction pipelines.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-43-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-48-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-49-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-50-\\textit{Empirical support.}\\;%\ndocs/paper/analysis.tex:51:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-52-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-53-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-54-\\textit{Per-trace separation analysis.}\\;%\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-55-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-56-\ndocs/paper/analysis.tex:57:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-58-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-59-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-60-\\textbf{Remark.}\\;%\n--\ndocs/paper/analysis.tex-128-\\label{sec:diagnostic-framework}\ndocs/paper/analysis.tex-129-\\label{sec:diagnostics}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-130-\ndocs/paper/analysis.tex:131:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-132-\ndocs/paper/analysis.tex-133-\\looseness=-1 Decision boundaries ($C_0 < 5\\%$, $K_\\text{eff} \\leq 1.30$, SC $< 40\\%$) were derived from Mistral-7B and Qwen2.5-14B. We evaluate prospectively on two held-out generators: LLaMA-3.1-8B (different family) on FOLIO, where the framework predicts Type~A bias and the observed $\\Delta = -4.41$\\,pp confirms; and Qwen3-14B (same family, different generation) on FOLIO and ProofWriter, likewise confirmed ($\\Delta \\leq +1.47$\\,pp, n.s.).\n--\ndocs/paper/experiments.tex-2-\\label{sec:results}\ndocs/paper/experiments.tex-3-\\label{sec:main-results}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-4-\ndocs/paper/experiments.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-6-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-7-\\begin{table*}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-8-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-9-\\small\ndocs/paper/experiments.tex:10:[Omitted long matching line]\ndocs/paper/experiments.tex-11-\\label{tab:main_results}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-12-\\begin{tabular}{@{}llrrrrl@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-13-\\toprule\n--\ndocs/paper/r8_response_drafts.md-55-**Data**: Dir-J2 (COMPLETE): Qwen3-14B FOLIO, SC=86.27%, combo w=1 −0.49pp, w=3 +0.49pp, w=5 +0.49pp, all p=1.0.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-56-\ndocs/paper/r8_response_drafts.md-57-**Draft response**:\ndocs/paper/r8_response_drafts.md:58:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-59-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-60----\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-61-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-468-\\@LN{340}{3}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-469-\\@LN{341}{3}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-470-\\citation{lakens2017equivalence}\ndocs/paper/main.aux:471:[Omitted long matching line]\ndocs/paper/main.aux:472:[Omitted long matching line]\ndocs/paper/main.aux-473-\\newlabel{tab:main_results@cref}{{[table][1][]1}{[1][4][]5}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-474-\\@LN@col{1}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-475-\\@LN{342}{4}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1505-\\@LN{1205}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1506-\\@LN{1206}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1507-\\@LN{1207}{13}\ndocs/paper/main.aux:1508:\\newlabel{eq:cil}{{6}{14}{Conditional Correction Ratio}{equation.6}{}}\ndocs/paper/main.aux-1509-\\newlabel{eq:cil@cref}{{[equation][6][]6}{[1][14][]14}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1510-\\@LN{1208}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1511-\\@LN{1209}{13}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1535-\\@writefile{toc}{\\contentsline {paragraph}{Per-condition diagnostics.}{14}{section*.40}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1536-\\@LN{1228}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1537-\\@LN{1229}{13}\ndocs/paper/main.aux:1538:[Omitted long matching line]\ndocs/paper/main.aux:1539:[Omitted long matching line]\ndocs/paper/main.aux-1540-\\newlabel{tab:capability_trap@cref}{{[table][5][]5}{[1][14][]14}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1541-\\@LN{1230}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1542-\\@writefile{toc}{\\contentsline {section}{\\numberline {D}Statistical Power Analysis}{14}{appendix.D}\\protected@file@percent }\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1554-\\@LN{1239}{14}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1555-\\@LN{1240}{14}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1556-\\@LN{1241}{14}\ndocs/paper/main.aux:1557:\\@writefile{lot}{\\contentsline {table}{\\numberline {6}{\\ignorespaces Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}}{15}{table.caption.42}\\protected@file@percent }\ndocs/paper/main.aux:1558:\\newlabel{tab:power}{{6}{15}{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case}{table.caption.42}{}}\ndocs/paper/main.aux-1559-\\newlabel{tab:power@cref}{{[table][6][]6}{[1][15][]15}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1560-\\@LN{1242}{14}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1561-\\@LN{1243}{14}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2240-\\@LN{1750}{21}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2241-\\@LN{1751}{21}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2242-\\@LN{1752}{21}\ndocs/paper/main.aux:2243:\\@writefile{lot}{\\contentsline {table}{\\numberline {23}{\\ignorespaces TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}}{22}{table.caption.80}\\protected@file@percent }\ndocs/paper/main.aux:2244:\\newlabel{tab:tost-sensitivity}{{23}{22}{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions)}{table.caption.80}{}}\ndocs/paper/main.aux-2245-\\newlabel{tab:tost-sensitivity@cref}{{[table][23][]23}{[1][22][]22}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2246-\\@LN@col{1}\ndocs/paper/main.aux-2247-\\newlabel{app:relative_tost}{{U}{23}{Relative-margin TOST}{section*.81}{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2332-\\@LN{1806}{22}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2333-\\@LN{1807}{22}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2334-\\@LN@col{1}\ndocs/paper/main.aux:2335:[Omitted long matching line]\ndocs/paper/main.aux:2336:[Omitted long matching line]\ndocs/paper/main.aux-2337-\\newlabel{fig:capability-gap@cref}{{[figure][8][]8}{[1][23][]24}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2338-\\@LN{1808}{23}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2339-\\@LN{1809}{23}\ndocs/paper/main.aux-2340-\\newlabel{app:nli-combo-full}{{W}{24}{Full NLI combo with BH correction}{section*.91}{}}\ndocs/paper/main.aux-2341-\\newlabel{app:nli-combo-full@cref}{{[section][23][]W}{[1][24][]24}{}{}{}}\ndocs/paper/main.aux:2342:\\@writefile{lot}{\\contentsline {table}{\\numberline {28}{\\ignorespaces Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha {=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text  {BH}} < 0.001$.}}{24}{table.caption.92}\\protected@file@percent }\ndocs/paper/main.aux:2343:\\newlabel{tab:nli-combo-full}{{28}{24}{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha {=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text {BH}} < 0.001$}{table.caption.92}{}}\ndocs/paper/main.aux-2344-\\newlabel{tab:nli-combo-full@cref}{{[table][28][]28}{[1][24][]24}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2345-\\@writefile{toc}{\\contentsline {paragraph}{Full NLI combo with BH correction.}{24}{table.caption.92}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2346-\\@LN{1810}{23}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2434-\\@LN{1852}{24}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2435-\\@LN{1853}{24}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2436-\\@LN@col{2}\ndocs/paper/main.aux:2437:\\@writefile{lot}{\\contentsline {table}{\\numberline {34}{\\ignorespaces NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}}{25}{table.caption.102}\\protected@file@percent }\ndocs/paper/main.aux:2438:\\newlabel{tab:logiqa-nli-deberta}{{34}{25}{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance}{table.caption.102}{}}\ndocs/paper/main.aux-2439-\\newlabel{tab:logiqa-nli-deberta@cref}{{[table][34][]34}{[1][24][]25}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2440-\\@writefile{lot}{\\contentsline {table}{\\numberline {35}{\\ignorespaces NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}}{25}{table.caption.103}\\protected@file@percent }\ndocs/paper/main.aux-2441-\\newlabel{tab:logiqa-nli-bart}{{35}{25}{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements}{table.caption.103}{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2630-\\citation{dhuliawala2023chainofverification}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2631-\\citation{wang2023sc}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2632-\\@LN@col{1}\ndocs/paper/main.aux:2633:[Omitted long matching line]\ndocs/paper/main.aux:2634:\\newlabel{tab:multi-seed}{{42}{28}{Multi-seed replication results across four model$\\times $dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times $FOLIO shows directionally unstable $\\Delta $ ($+0.16 \\pm 2.70$\\,pp); all ProofWriter conditions show consistently negative $\\Delta $ across all seeds ($p < .001$ for LLaMA-8B and Mistral-7B). Qwen3-14B results pending}{table.caption.115}{}}\ndocs/paper/main.aux-2635-\\newlabel{tab:multi-seed@cref}{{[table][42][]42}{[1][25][]28}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2636-\\@LN{1992}{27}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-2637-\\@LN{1993}{27}\n--\ndocs/paper/diagnosis.tex-48-\\label{sec:confirmation-bias}\ndocs/paper/diagnosis.tex-49-\\label{sec:effective-k}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-50-\ndocs/paper/diagnosis.tex:51:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-52-\ndocs/paper/diagnosis.tex-53-This correlation manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\\times$ compared to correct problems. Consequently, 94\\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-54-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-111-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-112-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-113-\ndocs/paper/diagnosis.tex:114:\\paragraph{Type A (SC $\\geq$ 60\\%).} All nine Type~A conditions produce no significant positive effects. Even in-context learning with gold logical examples yields $\\Delta = +0.50$\\,pp (n.s.). Qwen2.5-14B on ProofWriter shows significant degradation ($\\Delta = -2.50$\\,pp, $p = 0.011$).\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-115-\ndocs/paper/diagnosis.tex-116-\\paragraph{Type C (SC $\\leq$ 40\\%).} Mistral-7B on ProofWriter ($n = 600$, SC $= 39.33\\%$) shows $\\Delta = -2.83$\\,pp ($p = 0.014$): SICA \\emph{significantly hurts} by formalizing incorrect reasoning. When $C_0 < 5\\%$, nearly all traces agree and SICA reduces to SC by construction.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex-117-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex-2-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex-3-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex-4-\ndocs/paper/limitations_content.tex:5:[Omitted long matching line]\n--\ndocs/paper/abstract.tex:1:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-251-Qwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-252-\\bottomrule\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-253-\\end{tabular}}\ndocs/paper/appendix.tex:254:[Omitted long matching line]\ndocs/paper/appendix.tex-255-\\label{tab:capability_trap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-256-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-257-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-259-\\section{Statistical Power Analysis}\ndocs/paper/appendix.tex-260-\\label{app:power}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-261-\ndocs/paper/appendix.tex:262:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-263-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-264-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-265-\\centering\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-274-LLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-275-\\bottomrule\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-276-\\end{tabular}}\ndocs/paper/appendix.tex:277:\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\ndocs/paper/appendix.tex-278-\\label{tab:power}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-279-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-280-\ndocs/paper/appendix.tex:281:The largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-282-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-283-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-284-\\section{Bootstrap Confidence Intervals}\ndocs/paper/appendix.tex-285-\\label{app:bootstrap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-286-\ndocs/paper/appendix.tex:287:We compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-288-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-289-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-290-\\centering\n--\ndocs/paper/appendix.tex-303-\\label{tab:bootstrap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-304-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-305-\ndocs/paper/appendix.tex:306:All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-307-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-308-\ndocs/paper/appendix.tex-309-\\section{Case Studies: Discordant Predictions}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-813-\\section{TOST Equivalence Tests}\ndocs/paper/appendix.tex-814-\\label{app:tost}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-815-\ndocs/paper/appendix.tex:816:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-817-\ndocs/paper/appendix.tex-818-\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-819-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-820-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-821-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-822-\\small\ndocs/paper/appendix.tex:823:\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\ndocs/paper/appendix.tex-824-\\label{tab:tost-sensitivity}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-825-\\begin{tabular}{@{}lccc@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-826-\\toprule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-835-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-836-\\paragraph{Relative-margin TOST.}\ndocs/paper/appendix.tex-837-\\label{app:relative_tost}\ndocs/paper/appendix.tex:838:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-839-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-840-\\paragraph{Conditional Correction Ratio data.}\ndocs/paper/appendix.tex-841-\\label{app:cil-data}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-945-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-946-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-947-\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\ndocs/paper/appendix.tex:948:\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\ndocs/paper/appendix.tex-949-\\label{fig:capability-gap}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-950-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-951-\ndocs/paper/appendix.tex-952-Table~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-953-\ndocs/paper/appendix.tex:954:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-955-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-956-\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-957-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-961-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-962-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-963-\\small\ndocs/paper/appendix.tex:964:\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\ndocs/paper/appendix.tex-965-\\label{tab:nli-combo-full}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-966-\\setlength{\\tabcolsep}{3.5pt}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-967-\\resizebox{\\columnwidth}{!}{%\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1123-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1124-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1125-\\small\ndocs/paper/appendix.tex:1126:\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\ndocs/paper/appendix.tex-1127-\\label{tab:logiqa-nli-deberta}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1128-\\begin{tabular}{@{}lcccrl@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1129-\\toprule\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1373-\\begin{table}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1374-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex-1375-\\small\ndocs/paper/appendix.tex:1376:\\caption{Multi-seed replication results across four model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); all ProofWriter conditions show consistently negative $\\Delta$ across all seeds ($p < .001$ for LLaMA-8B and Mistral-7B). Qwen3-14B results pending.}",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01JEu4DBm4MW555fHpmwf85T`</summary>

```json
{
  "command": "python3 -c \"\nfrom statsmodels.stats.multitest import multipletests\nimport numpy as np\n\n# 6 confirmatory conditions from main table\n# Need to identify which 6 - let's try various combos\n\n# All p-values from table\nall_p = {\n    'Mistral-7B PW-D5': 0.014,\n    'Mistral-7B LogiQA': 0.581,\n    'LLaMA-3.1-8B FOLIO': 0.093,\n    'LLaMA-3.1-8B StrategyQA': 0.424,\n    'Qwen2.5-14B PW-D5': 0.011,\n    'Qwen2.5-14B LogiQA': 0.625,\n    'Qwen2.5-14B FOLIO ICL': 1.000,\n    'Qwen2.5-14B FOLIO 4s': 1.000,\n    'Qwen2.5-7B FOLIO': 1.000,\n    'Qwen3-14B FOLIO': 1.000,\n    'Qwen3-14B PW-D5': 1.000,\n    'Qwen3-14B think FOLIO': 1.000,\n}\n\n# Try: 6 main conditions (3 models x 2 domains)\nprint('=== Hypothesis 1: 3 models x 2 benchmarks ===')\nconds = ['Mistral-7B PW-D5', 'Mistral-7B LogiQA', 'LLaMA-3.1-8B FOLIO', 'LLaMA-3.1-8B StrategyQA', 'Qwen2.5-14B PW-D5', 'Qwen2.5-14B LogiQA']\np_vals = [all_p[c] for c in conds]\nreject, adj_p, _, _ = multipletests(p_vals, method='fdr_bh')\nfor c, raw, adj, r in zip(conds, p_vals, adj_p, reject):\n    print(f'  {c}: raw={raw:.4f}  adj={adj:.4f}  sig={r}')\n\n# Manual BH without monotonicity (possible bug)\nprint()\nprint('=== Manual BH WITHOUT monotonicity ===')\nsorted_pairs = sorted(zip(p_vals, conds))\nm = len(sorted_pairs)\nfor rank, (p, name) in enumerate(sorted_pairs, 1):\n    adj_no_mono = p * m / rank\n    print(f'  rank {rank}: {name}: raw={p:.4f}  adj(no mono)={adj_no_mono:.4f}')\n\n# Simple Bonferroni-like: raw_p * m\nprint()\nprint('=== Simple multiplication: raw_p * m ===')\nfor c in conds:\n    print(f'  {c}: raw={all_p[c]:.4f}  raw*6={all_p[c]*6:.4f}')\n\" 2>&1",
  "description": "Verify BH correction with different possible confirmatory condition sets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "fe45f698-aaca-4b9b-ac63-af4ebdcf8543",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Un41QksXfoQtnhVxaeKN9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 36453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2025
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

_source line 40 · 2026-05-24T04:50:22.235Z_

<details><summary>↩ Tool result · `toolu_01JEu4DBm4MW555fHpmwf85T`</summary>

```text
=== Hypothesis 1: 3 models x 2 benchmarks ===
  Mistral-7B PW-D5: raw=0.0140  adj=0.0420  sig=True
  Mistral-7B LogiQA: raw=0.5810  adj=0.6250  sig=False
  LLaMA-3.1-8B FOLIO: raw=0.0930  adj=0.1860  sig=False
  LLaMA-3.1-8B StrategyQA: raw=0.4240  adj=0.6250  sig=False
  Qwen2.5-14B PW-D5: raw=0.0110  adj=0.0420  sig=True
  Qwen2.5-14B LogiQA: raw=0.6250  adj=0.6250  sig=False

=== Manual BH WITHOUT monotonicity ===
  rank 1: Qwen2.5-14B PW-D5: raw=0.0110  adj(no mono)=0.0660
  rank 2: Mistral-7B PW-D5: raw=0.0140  adj(no mono)=0.0420
  rank 3: LLaMA-3.1-8B FOLIO: raw=0.0930  adj(no mono)=0.1860
  rank 4: LLaMA-3.1-8B StrategyQA: raw=0.4240  adj(no mono)=0.6360
  rank 5: Mistral-7B LogiQA: raw=0.5810  adj(no mono)=0.6972
  rank 6: Qwen2.5-14B LogiQA: raw=0.6250  adj(no mono)=0.6250

=== Simple multiplication: raw_p * m ===
  Mistral-7B PW-D5: raw=0.0140  raw*6=0.0840
  Mistral-7B LogiQA: raw=0.5810  raw*6=3.4860
  LLaMA-3.1-8B FOLIO: raw=0.0930  raw*6=0.5580
  LLaMA-3.1-8B StrategyQA: raw=0.4240  raw*6=2.5440
  Qwen2.5-14B PW-D5: raw=0.0110  raw*6=0.0660
  Qwen2.5-14B LogiQA: raw=0.6250  raw*6=3.7500
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "14cd6e56-2449-4af8-9f7b-3ea66670189b",
  "tool_use_result": {
    "stdout": "=== Hypothesis 1: 3 models x 2 benchmarks ===\n  Mistral-7B PW-D5: raw=0.0140  adj=0.0420  sig=True\n  Mistral-7B LogiQA: raw=0.5810  adj=0.6250  sig=False\n  LLaMA-3.1-8B FOLIO: raw=0.0930  adj=0.1860  sig=False\n  LLaMA-3.1-8B StrategyQA: raw=0.4240  adj=0.6250  sig=False\n  Qwen2.5-14B PW-D5: raw=0.0110  adj=0.0420  sig=True\n  Qwen2.5-14B LogiQA: raw=0.6250  adj=0.6250  sig=False\n\n=== Manual BH WITHOUT monotonicity ===\n  rank 1: Qwen2.5-14B PW-D5: raw=0.0110  adj(no mono)=0.0660\n  rank 2: Mistral-7B PW-D5: raw=0.0140  adj(no mono)=0.0420\n  rank 3: LLaMA-3.1-8B FOLIO: raw=0.0930  adj(no mono)=0.1860\n  rank 4: LLaMA-3.1-8B StrategyQA: raw=0.4240  adj(no mono)=0.6360\n  rank 5: Mistral-7B LogiQA: raw=0.5810  adj(no mono)=0.6972\n  rank 6: Qwen2.5-14B LogiQA: raw=0.6250  adj(no mono)=0.6250\n\n=== Simple multiplication: raw_p * m ===\n  Mistral-7B PW-D5: raw=0.0140  raw*6=0.0840\n  Mistral-7B LogiQA: raw=0.5810  raw*6=3.4860\n  LLaMA-3.1-8B FOLIO: raw=0.0930  raw*6=0.5580\n  LLaMA-3.1-8B StrategyQA: raw=0.4240  raw*6=2.5440\n  Qwen2.5-14B PW-D5: raw=0.0110  raw*6=0.0660\n  Qwen2.5-14B LogiQA: raw=0.6250  raw*6=3.7500",
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Now I can see the issue clearly:

The paper says "both reach adjusted p = 0.066" — this is **wrong**. The standard BH procedure gives:
- Qwen2.5-14B PW-D5 (raw p=0.011): **adjusted p = 0.042** (significant at α=0.05)
- Mistral-7B PW-D5 (raw p=0.014): **adjusted p = 0.042** (significant at α=0.05)

The 0.066 value appears to have come from computing `0.011 * 6 / 1 = 0.066` (rank-1 BH computation) but WITHOUT applying the monotonicity enforcement step. 

The standard BH procedure requires a monotonicity correction where you work backwards from the largest p-value, ensuring each adjusted p-value is no larger than the one after it. So rank 1's adjusted p gets pulled down from 0.066 to 0.042 because rank 2's adjusted p is smaller. This means both conditions are actually significant after proper BH correction.

Let me check the grep output about the confirmatory conditions to verify I have the right count of 6, and then look at how the paper defines them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "ea6a7035-3733-4ac3-aded-5fd19831626e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fCWFwU4dwx5d61AnLZZxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8684,
      "cache_read_input_tokens": 38478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8684
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01T3EFneTTmhWjKkm7gePwU7`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/88dd4cac-745e-4701-a7b3-bec955cff63c/tool-results/toolu_01JRf77GtX9zMqrznHhitPPf.txt",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "bff8f2bb-62a0-486e-96b9-7561f09de76c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fCWFwU4dwx5d61AnLZZxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8684,
      "cache_read_input_tokens": 38478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8684
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

_source line 43 · 2026-05-24T04:50:40.682Z_

<details><summary>↩ Tool result · `toolu_01T3EFneTTmhWjKkm7gePwU7`</summary>

```text
1	docs/paper/analysis.tex-37-\looseness=-1 Two controls rule out answer leakage: BR is uniform across reasoning steps (Fisher $p = 0.71$), and removing answer sentences before extraction yields no BR decrease (Wilcoxon $p \geq 0.12$) despite accuracy loss (McNemar $p < 0.013$). The bias reflects a distributional prior embedded throughout reasoning, not answer contamination.
2	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-38-
3	docs/paper/analysis.tex-39-\label{sec:process-kappa}
4	docs/paper/analysis.tex:40:[Omitted long matching line]
5	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-41-
6	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-42-\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a persistent empirical property of zero-shot self-extraction pipelines.
7	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-43-
8	--
9	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-48-
10	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-49-\smallskip\noindent
11	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-50-\textit{Empirical support.}\;%
12	docs/paper/analysis.tex:51:[Omitted long matching line]
13	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-52-
14	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-53-\smallskip\noindent
15	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-54-\textit{Per-trace separation analysis.}\;%
16	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-55-[Omitted long context line]
17	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-56-
18	docs/paper/analysis.tex:57:[Omitted long matching line]
19	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-58-
20	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-59-\smallskip\noindent
21	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-60-\textbf{Remark.}\;%
22	--
23	docs/paper/analysis.tex-128-\label{sec:diagnostic-framework}
24	docs/paper/analysis.tex-129-\label{sec:diagnostics}
25	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-130-
26	docs/paper/analysis.tex:131:[Omitted long matching line]
27	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-132-
28	docs/paper/analysis.tex-133-\looseness=-1 Decision boundaries ($C_0 < 5\%$, $K_\text{eff} \leq 1.30$, SC $< 40\%$) were derived from Mistral-7B and Qwen2.5-14B. We evaluate prospectively on two held-out generators: LLaMA-3.1-8B (different family) on FOLIO, where the framework predicts Type~A bias and the observed $\Delta = -4.41$\,pp confirms; and Qwen3-14B (same family, different generation) on FOLIO and ProofWriter, likewise confirmed ($\Delta \leq +1.47$\,pp, n.s.).
29	--
30	docs/paper/experiments.tex-2-\label{sec:results}
31	docs/paper/experiments.tex-3-\label{sec:main-results}
32	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-4-
33	docs/paper/experiments.tex:5:[Omitted long matching line]
34	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-6-
35	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-7-\begin{table*}[t]
36	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-8-\centering
37	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-9-\small
38	docs/paper/experiments.tex:10:[Omitted long matching line]
39	docs/paper/experiments.tex-11-\label{tab:main_results}
40	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-12-\begin{tabular}{@{}llrrrrl@{}}
41	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-13-\toprule
42	--
43	docs/paper/r8_response_drafts.md-55-**Data**: Dir-J2 (COMPLETE): Qwen3-14B FOLIO, SC=86.27%, combo w=1 −0.49pp, w=3 +0.49pp, w=5 +0.49pp, all p=1.0.
44	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-56-
45	docs/paper/r8_response_drafts.md-57-**Draft response**:
46	docs/paper/r8_response_drafts.md:58:[Omitted long matching line]
47	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-59-
48	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-60----
49	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-61-
50	--
51	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-468-\@LN{340}{3}
52	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-469-\@LN{341}{3}
53	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-470-\citation{lakens2017equivalence}
54	docs/paper/main.aux:471:[Omitted long matching line]
55	docs/paper/main.aux:472:[Omitted long matching line]
56	docs/paper/main.aux-473-\newlabel{tab:main_results@cref}{{[table][1][]1}{[1][4][]5}{}{}{}}
57	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-474-\@LN@col{1}
58	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-475-\@LN{342}{4}
59	--
60	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1505-\@LN{1205}{13}
61	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1506-\@LN{1206}{13}
62	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1507-\@LN{1207}{13}
63	docs/paper/main.aux:1508:\newlabel{eq:cil}{{6}{14}{Conditional Correction Ratio}{equation.6}{}}
64	docs/paper/main.aux-1509-\newlabel{eq:cil@cref}{{[equation][6][]6}{[1][14][]14}{}{}{}}
65	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1510-\@LN{1208}{13}
66	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1511-\@LN{1209}{13}
67	--
68	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1535-\@writefile{toc}{\contentsline {paragraph}{Per-condition diagnostics.}{14}{section*.40}\protected@file@percent }
69	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1536-\@LN{1228}{13}
70	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1537-\@LN{1229}{13}
71	docs/paper/main.aux:1538:[Omitted long matching line]
72	docs/paper/main.aux:1539:[Omitted long matching line]
73	docs/paper/main.aux-1540-\newlabel{tab:capability_trap@cref}{{[table][5][]5}{[1][14][]14}{}{}{}}
74	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1541-\@LN{1230}{13}
75	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1542-\@writefile{toc}{\contentsline {section}{\numberline {D}Statistical Power Analysis}{14}{appendix.D}\protected@file@percent }
76	--
77	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1554-\@LN{1239}{14}
78	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1555-\@LN{1240}{14}
79	/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1556-\@LN{1241}{14}
80	docs/paper/main.aux:1557:\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces Power analysis for confirmatory conditions ($n \geq 200$). MDE = minimum detectable effect at 80\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\% in every case.}}{15}{table.caption.42}\protected@file@percent }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "e03e0245-1a94-4475-9e63-074ccd2fee11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/88dd4cac-745e-4701-a7b3-bec955cff63c/tool-results/toolu_01JRf77GtX9zMqrznHhitPPf.txt",
      "content": "docs/paper/analysis.tex-37-\\looseness=-1 Two controls rule out answer leakage: BR is uniform across reasoning steps (Fisher $p = 0.71$), and removing answer sentences before extraction yields no BR decrease (Wilcoxon $p \\geq 0.12$) despite accuracy loss (McNemar $p < 0.013$). The bias reflects a distributional prior embedded throughout reasoning, not answer contamination.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-38-\ndocs/paper/analysis.tex-39-\\label{sec:process-kappa}\ndocs/paper/analysis.tex:40:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-41-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-42-\\looseness=-1 These patterns---universal BR $> 1$, structural equivalence to trace-count distributions, and process-level correlation exceeding answer-level agreement---follow from a persistent empirical property of zero-shot self-extraction pipelines.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-43-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-48-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-49-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-50-\\textit{Empirical support.}\\;%\ndocs/paper/analysis.tex:51:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-52-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-53-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-54-\\textit{Per-trace separation analysis.}\\;%\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-55-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-56-\ndocs/paper/analysis.tex:57:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-58-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-59-\\smallskip\\noindent\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-60-\\textbf{Remark.}\\;%\n--\ndocs/paper/analysis.tex-128-\\label{sec:diagnostic-framework}\ndocs/paper/analysis.tex-129-\\label{sec:diagnostics}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-130-\ndocs/paper/analysis.tex:131:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex-132-\ndocs/paper/analysis.tex-133-\\looseness=-1 Decision boundaries ($C_0 < 5\\%$, $K_\\text{eff} \\leq 1.30$, SC $< 40\\%$) were derived from Mistral-7B and Qwen2.5-14B. We evaluate prospectively on two held-out generators: LLaMA-3.1-8B (different family) on FOLIO, where the framework predicts Type~A bias and the observed $\\Delta = -4.41$\\,pp confirms; and Qwen3-14B (same family, different generation) on FOLIO and ProofWriter, likewise confirmed ($\\Delta \\leq +1.47$\\,pp, n.s.).\n--\ndocs/paper/experiments.tex-2-\\label{sec:results}\ndocs/paper/experiments.tex-3-\\label{sec:main-results}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-4-\ndocs/paper/experiments.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-6-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-7-\\begin{table*}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-8-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-9-\\small\ndocs/paper/experiments.tex:10:[Omitted long matching line]\ndocs/paper/experiments.tex-11-\\label{tab:main_results}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-12-\\begin{tabular}{@{}llrrrrl@{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex-13-\\toprule\n--\ndocs/paper/r8_response_drafts.md-55-**Data**: Dir-J2 (COMPLETE): Qwen3-14B FOLIO, SC=86.27%, combo w=1 −0.49pp, w=3 +0.49pp, w=5 +0.49pp, all p=1.0.\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-56-\ndocs/paper/r8_response_drafts.md-57-**Draft response**:\ndocs/paper/r8_response_drafts.md:58:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-59-\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-60----\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/r8_response_drafts.md-61-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-468-\\@LN{340}{3}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-469-\\@LN{341}{3}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-470-\\citation{lakens2017equivalence}\ndocs/paper/main.aux:471:[Omitted long matching line]\ndocs/paper/main.aux:472:[Omitted long matching line]\ndocs/paper/main.aux-473-\\newlabel{tab:main_results@cref}{{[table][1][]1}{[1][4][]5}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-474-\\@LN@col{1}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-475-\\@LN{342}{4}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1505-\\@LN{1205}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1506-\\@LN{1206}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1507-\\@LN{1207}{13}\ndocs/paper/main.aux:1508:\\newlabel{eq:cil}{{6}{14}{Conditional Correction Ratio}{equation.6}{}}\ndocs/paper/main.aux-1509-\\newlabel{eq:cil@cref}{{[equation][6][]6}{[1][14][]14}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1510-\\@LN{1208}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1511-\\@LN{1209}{13}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1535-\\@writefile{toc}{\\contentsline {paragraph}{Per-condition diagnostics.}{14}{section*.40}\\protected@file@percent }\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1536-\\@LN{1228}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1537-\\@LN{1229}{13}\ndocs/paper/main.aux:1538:[Omitted long matching line]\ndocs/paper/main.aux:1539:[Omitted long matching line]\ndocs/paper/main.aux-1540-\\newlabel{tab:capability_trap@cref}{{[table][5][]5}{[1][14][]14}{}{}{}}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1541-\\@LN{1230}{13}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1542-\\@writefile{toc}{\\contentsline {section}{\\numberline {D}Statistical Power Analysis}{14}{appendix.D}\\protected@file@percent }\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1554-\\@LN{1239}{14}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1555-\\@LN{1240}{14}\n/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.aux-1556-\\@LN{1241}{14}\ndocs/paper/main.aux:1557:\\@writefile{lot}{\\contentsline {table}{\\numberline {6}{\\ignorespaces Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}}{15}{table.caption.42}\\protected@file@percent }",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 252
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
I see a reference to "confirmatory conditions ($n \geq 200$)" in the power analysis appendix. Let me check which conditions have n ≥ 200 and are not multi-seed/extension/individual seed runs.

Looking at the table:
- Mistral-7B PW-D5 (n=600) ✓
- Mistral-7B LogiQA (n=200) ✓
- Mistral-7B FOLIO (s123) (n=204) — individual seed, exploratory


- LLaMA-3.1-8B FOLIO (n=204) ✓
- LLaMA-3.1-8B StrategyQA (n=200) ✓

The rest of the entries are either multi-seed aggregates, individual seed runs, or extensions marked as exploratory, so they don't qualify as confirmatory conditions. W-D5 (n=600) ✓
- Qwen2.5-14B FOLIO 4s (n=204) — multi-seed aggregate, exploratory (wait, the caption says "4-seed confirmatory aggregate")
- Qwen2.5-7B FOLIO (n=204) — unmarked single-seed exploratory
- Qwen2.5-14B LogiQA (n=200) ✓
- Qwen3-14B FOLIO (n=204) — exploratory (held-out generator)
- Qwen3-14B PW-D5 (n=600) — exploratory (held-out)
- Qwen3-14B think FOLIO (n=204) — exploratory

That gives me 6 confirmatory conditions without the 4-seed aggregate: Mistral-7B PW-D5, Mistral-7B LogiQA, LLaMA-3.1-8B FOLIO, LLaMA-3.1-8B StrategyQA, Qwen2.5-14B PW-D5, and Qwen2.5-14B LogiQA. These match the 6 p-values I'm working with. When I apply the standard Benjamini-Hochberg correction properly, I get two significant results — Qwen2.5-14B PW-D5 and Mistral-7B PW-D5 both at adjusted p = 0.042 — but the paper reported 0.066, which suggests a missing monotonicity enforcement step in their implementation. This is a significant problem because it completely changes the narrative: instead of "no significant SICA effects after FDR control," I now have two conditions showing real effects.

I need to update the paper with the correct findings, which means revising the statement about significant effects to reflect that two conditions do show significant negative effects. I should check the abstract and other sections to make sure the language is consistent with this correction.

For the abstract, I'll verify the word count manually since it's already close to the 200-word limit. Then I'll make the specific edits: updating the BH-related statements in experiments.tex, fixing the table and figure captions with the correct adjusted p-values, clarifying the LLaMA-8B specification in solutions.tex, and ensuring the abstract accurately reflects that significant effects are negative rather than absent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "3a80079e-645e-4873-b1a8-6d4eff625d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyDyQFCBK8oLpHeq2VSzE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 47162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 45_

Now I have the full picture. Let me verify the abstract word count more carefully and search for all "0.066" references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "bede9c82-f7c4-4b41-94ae-264fef79b0c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyDyQFCBK8oLpHeq2VSzE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 47162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01ARRviQqcJHFA2XUWWZsTFZ`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && detex abstract.tex 2>/dev/null | wc -w || python3 -c \"\nimport re\ntext = open('abstract.tex').read()\n# Strip LaTeX commands but keep their text arguments\ntext = re.sub(r'\\\\\\\\emph\\{([^}]*)\\}', r'\\1', text)\ntext = re.sub(r'\\\\\\\\citet?\\{[^}]*\\}', 'CITE', text)\ntext = re.sub(r'\\\\\\\\[a-zA-Z]+', '', text)\ntext = re.sub(r'[{}$~]', ' ', text)\ntext = re.sub(r'---', ' ', text)\nwords = text.split()\nprint(f'Word count: {len(words)}')\nfor i, w in enumerate(words):\n    if (i+1) % 20 == 0:\n        print(f'  word {i+1}: {w}')\n\"",
  "description": "Count abstract words more accurately"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "e6afa98b-079c-496d-9ceb-1cc6e1aec8ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyDyQFCBK8oLpHeq2VSzE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 47162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 47 · 2026-05-24T04:51:10.502Z_

<details><summary>↩ Tool result · `toolu_01ARRviQqcJHFA2XUWWZsTFZ`</summary>

```text
191
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "aec03226-af0f-4b7e-95d3-62d218cf00e1",
  "tool_use_result": {
    "stdout": "191",
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

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01FN8Uz4ejndF67dMqJxune6`</summary>

```json
{
  "pattern": "0\\.066|adj.*p.*=",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "context": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "12663ce2-7dc5-4f7e-9517-ea22e919ac1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GyDyQFCBK8oLpHeq2VSzE5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3987,
      "cache_read_input_tokens": 47162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3987
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

_source line 49 · 2026-05-24T04:51:12.081Z_

<details><summary>↩ Tool result · `toolu_01FN8Uz4ejndF67dMqJxune6`</summary>

```text
experiments.tex:5:[Omitted long matching line]
experiments.tex:10:[Omitted long matching line]
experiments.tex:46:\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--60\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.066$).}
appendix.tex:596:[Omitted long matching line]
appendix.tex:697:\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$ (uncorrected; BH adj.\ $p = 0.066$, $m{=}6$); positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
appendix.tex:954:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "6e192961-7a60-44ba-866d-c2b10ac8d620",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "experiments.tex:5:[Omitted long matching line]\nexperiments.tex:10:[Omitted long matching line]\nexperiments.tex:46:\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\nappendix.tex:596:[Omitted long matching line]\nappendix.tex:697:\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.066$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\nappendix.tex:954:[Omitted long matching line]",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Let me also check appendix.tex lines 596 and 954 for the 0.066 references.

Abstract is 191 words — already under 200. No changes needed.

Now let me read the relevant appendix lines to see what needs to be updated there as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "b22ab284-3afb-45ba-a868-cdb1a2e8b81a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171n2my922YzAd8DioS92gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2111
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

_source line 51_

Abstract is 191 words — already under 200. Let me check the appendix references to 0.066.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "52ec6272-8ee1-4074-aef0-650dcc92e88e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171n2my922YzAd8DioS92gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2111
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01WR716vYR28uqwXXRw3QPgi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 592,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "4713dd2c-7ac6-4577-ae59-0860392a4e99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171n2my922YzAd8DioS92gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2111
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

_source line 53 · 2026-05-24T04:51:21.492Z_

<details><summary>↩ Tool result · `toolu_01WR716vYR28uqwXXRw3QPgi`</summary>

```text
592	\paragraph{Type A: confirmation bias (SC $\geq$ $\sim$60\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\mathcal{C}^{\setminus}| \approx 0$), the penalty term in Eq.~\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.
593	
594	\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\%, but the resulting constraints have a contradiction rate of only 0.8\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\%) yet produces $\Delta = +1.50$\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\Delta = -1.00$\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.
595	
596	\paragraph{Type C: error amplification (SC $\leq$ $\sim$40\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\Delta = -2.83$\,pp, raw $p = 0.014$; BH adj.\ $p = 0.066$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.
597	
598	
599	\section{Cross-Model Confirmation Bias}
600	\label{app:cross-model-bias}
601	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "0b9df44f-b4c5-4d8c-9a4f-e82a223c149b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.066$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n",
      "numLines": 10,
      "startLine": 592,
      "totalLines": 1544
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01EPzJhS91TynTBWxqGGw9MK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 693,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "cc253e77-ef6c-40ea-8ecb-1fe790024dd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171n2my922YzAd8DioS92gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2111
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

_source line 55 · 2026-05-24T04:51:22.388Z_

<details><summary>↩ Tool result · `toolu_01EPzJhS91TynTBWxqGGw9MK`</summary>

```text
693	\begin{table}[h]
694	\centering
695	\small
696	\setlength{\tabcolsep}{3pt}
697	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$ (uncorrected; BH adj.\ $p = 0.066$, $m{=}6$); positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
698	\label{tab:independence}
699	\begin{tabular}{@{}llccrr@{}}
700	\toprule
701	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
702	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "274017ba-8df2-4344-be64-2fbe924f7312",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.066$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule",
      "numLines": 10,
      "startLine": 693,
      "totalLines": 1544
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_0116G2ZCV4m3MBBFJmGcYdon`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 950,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "10283571-ba67-424d-9a16-2f362990d940",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171n2my922YzAd8DioS92gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2111,
      "cache_read_input_tokens": 51149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2111
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

_source line 57 · 2026-05-24T04:51:22.949Z_

<details><summary>↩ Tool result · `toolu_0116G2ZCV4m3MBBFJmGcYdon`</summary>

```text
950	\end{figure}
951	
952	Table~\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\% standalone, combo $+5.17$\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\% standalone, combo $+4.17$\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \geq 3$.
953	
954	Across all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\times$ Mistral-7B plus three negative-gap generators $\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\ $p = 6.78 \times 10^{-5}$) and $w{=}5$ (adj.\ $p = 7.41 \times 10^{-6}$).
955	
956	\paragraph{Robustness check.} Including all nine conditions (three verifiers $\times$ three weight levels on Mistral-7B) yields Spearman $\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.
957	
958	\paragraph{Full NLI combo with BH correction.}
959	\label{app:nli-combo-full}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "8c7313a7-f9de-4658-a491-79015798acff",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}",
      "numLines": 10,
      "startLine": 950,
      "totalLines": 1544
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information. Here's my plan:

**D1: BH correction fix**

The correct BH adjusted p-values for the 6 confirmatory conditions are:
- Qwen2.5-14B PW-D5 (raw p=0.011): **adj p = 0.042**
- Mistral-7B PW-D5 (raw p=0.014): **adj p = 0.042**

Both significant at α=0.05. The paper's reported "0.066" was wrong (missing monotonicity enforcement step).

Files to update:


1. `experiments.tex` line 5: Change "No condition shows a significant SICA effect after FDR control" → Update to reflect two significant negative effects
2. `experiments.tex` line 10 (table caption): Update "adj.\ $p = 0.066$" to "adj.\ $p = 0.042$" and the significance statement
3. `experiments.tex` line 46 (figure caption): Update "BH adj.\ $p = 0.066$" to "BH adj.\ $p = 0.042$"
4. `appendix.tex` line 596: Update "BH adj.\ $p = 0.066$" to "BH adj.\ $p = 0.042$"
5. `appendix.tex` line 697: Update "BH adj.\ $p = 0.066$" to "BH adj.\ $p = 0.042$"

I need to go through the manuscript and replace all instances of the incorrect p-value with the corrected one, updating the main narrative to reflect that we do have significant results after proper FDR correction. I need to update the table caption to reflect the corrected adjusted p-value of 0.042 instead of 0.066, and revise the statement about significant effects since two conditions now show significant negative results after BH correction. The asterisk markers in the table will need to be updated to match this new threshold. I'm revising the main text to reflect that these results actually do reach significance after Benjamini-Hochberg correction, so I need to flip the narrative from "no significant effects" to "two conditions show significant degradation." I'm updating the p-values to show the corrected values of 0.042 for both conditions, and restructuring the sentence to lead with the FDR-controlled finding rather than burying it. Now I'm applying these corrections throughout the document, updating the p-values and related statistical notation across the main text and appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "de755b88-975a-4cd7-81ab-5f98b611cc18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 59_

Confirmed: Standard BH gives adj p = 0.042 for both conditions (not 0.066). The paper had a bug — missing monotonicity enforcement step. Abstract is 191 words, no change needed.

Now making all edits. Starting with the 5 locations that need updating for D1, plus D3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "2b291861-6263-435e-82d8-e4d14d941378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_014o6Ui882qqdTVBSSSfsDyJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "old_string": "No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$.",
  "new_string": "Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a46fe7fe-cb28-4570-8669-27ddf32b82fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 61 · 2026-05-24T04:51:59.823Z_

<details><summary>↩ Tool result · `toolu_014o6Ui882qqdTVBSSSfsDyJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "f68cb21f-9b39-4446-ad61-ea533d0a90ad",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
    "oldString": "No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$.",
    "newString": "Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{sec:results}",
          " \\label{sec:main-results}",
          " ",
          "-\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}6$ confirmatory conditions; multi-seed aggregates and extensions are exploratory). Two confirmatory conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$); both reach adjusted $p = 0.066$. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.",
          "+\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.",
          " ",
          " \\begin{table*}[t]",
          " \\centering"
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01JrHMs4XyTZ1RuJMzsaHyyp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "old_string": "No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory).",
  "new_string": "Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "10dfc688-93ab-4007-8293-7de053b20f97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 63 · 2026-05-24T04:52:00.891Z_

<details><summary>↩ Tool result · `toolu_01JrHMs4XyTZ1RuJMzsaHyyp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "2491f3db-19c0-43f4-b895-4be7d51a8837",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
    "oldString": "No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory).",
    "newString": "Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\begin{table*}[t]",
          " \\centering",
          " \\small",
          "-\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}6$ confirmatory; remaining exploratory). $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}",
          "+\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}",
          " \\label{tab:main_results}",
          " \\begin{tabular}{@{}llrrrrl@{}}",
          " \\toprule"
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_017DqxAC41tdkUpSkFARuu75`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "old_string": "{*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$)",
  "new_string": "{*}\\,BH adj.\\ $p = 0.042$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "8fe75eff-a9c5-40fb-b3a4-6f509c3f948c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 65 · 2026-05-24T04:52:01.920Z_

<details><summary>↩ Tool result · `toolu_017DqxAC41tdkUpSkFARuu75`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "00b05848-ef1e-41d6-a245-0e325ba17a93",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
    "oldString": "{*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$)",
    "newString": "{*}\\,BH adj.\\ $p = 0.042$",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\begin{table*}[t]",
          " \\centering",
          " \\small",
          "-\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,uncorrected $p < 0.05$ (BH adj.\\ $p = 0.066$); $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}",
          "+\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,BH adj.\\ $p = 0.042$; $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}",
          " \\label{tab:main_results}",
          " \\begin{tabular}{@{}llrrrrl@{}}",
          " \\toprule"
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

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_016PER6LXrndGAE7xbCibCas`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "old_string": "BH adj.\\ $p = 0.066$).",
  "new_string": "BH adj.\\ $p = 0.042$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "e7f8b1a2-7b4d-4e61-845a-e6f950f7fac4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 67 · 2026-05-24T04:52:02.844Z_

<details><summary>↩ Tool result · `toolu_016PER6LXrndGAE7xbCibCas`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "00225940-de8a-47fd-81d1-9fca5a0f261e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
    "oldString": "BH adj.\\ $p = 0.066$).",
    "newString": "BH adj.\\ $p = 0.042$).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,BH adj.\\ $p = 0.042$; $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp. Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{f2_regime_scatter}",
          "-\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.066$).}",
          "+\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.042$).}",
          " \\label{fig:regime-scatter}",
          " \\end{figure}",
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

_source line 68_

<details open><summary>🔧 Tool call — Edit · `toolu_019rUxB7Q7vWgvk3XQsn1yAF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "old_string": "Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.066$)",
  "new_string": "Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "0d08d2e0-36d1-4778-ab76-304ea182d33b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 69 · 2026-05-24T04:52:04.875Z_

<details><summary>↩ Tool result · `toolu_019rUxB7Q7vWgvk3XQsn1yAF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "78dbb2d6-0ab1-41d8-b146-c002be2feb73",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "oldString": "Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.066$)",
    "newString": "Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$)",
    "originalFile": "\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability-Accuracy Constraint Diagnostics}\n\\label{app:diagnostics}\n\\label{app:cil}\n\n\\paragraph{Conditional Correction Ratio.}\nWe define the \\textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:\n\\begin{equation}\n\\label{eq:cil}\n\\text{CCR}(V, G) = \\log \\frac{P(V \\text{ correct} \\mid G \\text{ wrong})}{P(V \\text{ correct} \\mid G \\text{ correct})}.\n\\end{equation}\n$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n\n\\paragraph{Empirical CCR across verifier--generator pairs.}\nTable~\\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\\rho = 0.839$, 95\\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\\text{CCR} < 0$: same-model SICA or mismatched capability gap.}\n\\label{tab:cil_empirical}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllrr@{}}\n\\toprule\nGenerator & Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\\\\nMistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\\\\nMistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\\\\nMistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\\\\nQwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\\\\nMistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-condition diagnostics.}\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Oracle Control}\n\\label{app:oracle}\n\\label{sec:oracle}\n\\label{app:pw-oracle-subtype}\n\nReplacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \\times 10^{-7}$), and $+17.17$\\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\\Delta$ ($+3.43$\\,pp) captures only 11.5\\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\\,pp) against an oracle ceiling of $+17.17$\\,pp, indicating that stronger models do not self-extract more effectively.\n\n\\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 90.26 & \\textbf{98.70} & +8.44 \\\\\nAttNeg & 160 & 81.88 & \\textbf{91.88} & +10.00 \\\\\nRelNoneg & 146 & 60.96 & \\textbf{84.25} & +23.29 \\\\\nRelNeg & 140 & 60.71 & \\textbf{89.29} & +28.58 \\\\\n\\midrule\nOverall & 600 & 74.00 & \\textbf{91.17} & +17.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAX-SAT vs.\\ count-only agreement across constraint weight $\\alpha \\in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\\times$, seed 42); Qwen2.5-14B (BR $= 3.85\\times$, seed 123). $\\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\\alpha{=}1$: full source-attribution penalty. Agreement $\\geq 99\\%$ at all $\\alpha$ including endpoints, confirming vacuity is weight-insensitive.}\n\\label{tab:alpha-ablation}\n\\begin{tabular}{@{}crr@{}}\n\\toprule\n$\\alpha$ & Mistral Agr.\\ (\\%) & Qwen2.5 Agr.\\ (\\%) \\\\\n\\midrule\n0.0 & 100 & 100 \\\\\n0.1 & 100 & 100 \\\\\n0.3 & 100 & 100 \\\\\n0.5 & 100 & 100 \\\\\n0.7 & 99 & 100 \\\\\n0.9 & 99 & 100 \\\\\n1.0 & 99 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 83.33\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\addlinespace\n24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\\\\n25 & Premise-only filter & Constraint sel.\\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\\\\n26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\\text{sel}}{=}8$ \\\\\n27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\\% UNSAT \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 25.0\\% of the oracle ceiling ($+13.73$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.066$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\\times$, $3.85\\times$, $2.88\\times$) are reported in \\S\\ref{sec:confirmation-bias}. LLaMA weighted BR CI: [2.19, 3.28].\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\\ correct problems. Wrong \\%: weighted fraction of constraints supporting the incorrect majority on error problems. $\\Delta$: SICA $-$ SC (pp).}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & BR (wtd.) & Wrong (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $4.24\\times$ & 80.9 & $+$4.90 \\\\\nQwen2.5-14B & $3.69\\times$ & 78.7 & $-$0.98 \\\\\nLLaMA-3.1-8B & $2.66\\times$ & 72.7 & $-$4.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Frontier model universality.}\n\\label{app:frontier-scb}\nTable~\\ref{tab:frontier-scb} (main text, \\S\\ref{sec:confirmation-bias}) extends confirmation bias analysis to nine models spanning 7B open-source to frontier closed-source. All models exhibit $\\text{BR} > 1$ (range: $1.66$--$4.97\\times$). Extraction context varies: open-source models use self-extraction (the model extracts constraints from its own traces); frontier models use cross-model extraction (Mistral-7B extracts FOL from the target model's traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction.\n\n\\paragraph{ProcessSim definition.}\n\\label{app:process-sim}\nProcess similarity is the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.\n\n\\paragraph{Process-$\\kappa$ gradient.}\n\\label{app:process-gradient}\nUnder cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\\ref{tab:process-gradient}; Spearman $\\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\\kappa_{\\text{proc}}$) \\emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\\kappa_{\\text{proc}} = 0.248$, $\\text{BR} = 2.92$) and gains $+2.45$\\,pp; o3 has moderate trace diversity ($\\kappa_{\\text{proc}} = 0.596$) but near-minimal bias ($\\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\\% of error problems have $\\text{BR} = \\infty$ but low finite-BR), yielding $\\Delta = 0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Process-$\\kappa$ gradient under cross-model extraction (Mistral-7B $\\rightarrow$ target model traces, FOLIO). $\\kappa_{\\text{proc}}$: process-level cosine similarity. $\\Delta$: SICA $-$ SC (pp). Spearman $\\rho(\\kappa_{\\text{proc}} \\rightarrow \\Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}\n\\label{tab:process-gradient}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & $\\kappa_{\\text{proc}}$ & $\\Delta$ (pp) & BR \\\\\n\\midrule\nR1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\\\\ngpt-5.5 & 0.563 & $+$0.49 & 3.48 \\\\\no3 & 0.596 & 0.00 & 1.66 \\\\\nGemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\\\\ngpt-4.1 & 0.792 & $-$1.47 & 2.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Trace independence metrics.}\n\\label{app:trace-independence}\n\nTable~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.066$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & 86.27 & $+$0.49 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.77 & 1.26 & 83.33 & $+$1.47 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\\\\nMistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\\\\nMistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.44$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.03$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.22 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.44 & 2.02 & 56.86 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\\ TF-IDF $0.74$), widening the gap over answer-level $\\kappa = 0.55$. The process homogeneity finding is robust to representation choice.\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-trace constraint yield uniformity.}\n\\label{app:yield-cv}\n\nObservation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\\% of problems fall below $\\text{CV} = 0.3$, and 91.2\\% below $0.5$, supporting the uniformity assumption. Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \\times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \\times 10^{-11}$). Although statistically significant, the absolute difference (${\\sim}0.6$ constraints, $< 12\\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\\%$ of problems regardless of yield variation.\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{TOST Equivalence Tests}\n\\label{app:tost}\n\nWe apply two one-sided tests (TOST) \\citep{lakens2017equivalence} with equivalence margin $\\pm 2$\\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \\emph{equivalent} (TOST significant), \\emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \\emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\\Delta| \\leq 2$\\,pp effects.\n\n\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\n\\label{tab:tost-sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMargin & Equivalent & Different & Underpowered \\\\\n\\midrule\n$\\pm 1$\\,pp & 0 & 2 & 14 \\\\\n$\\pm 2$\\,pp & 4 & 2 & 10 \\\\\n$\\pm 3$\\,pp & 10 & 0 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Relative-margin TOST.}\n\\label{app:relative_tost}\nThe absolute $\\pm 2$\\,pp margin is more stringent at high baselines ($\\pm 2.4\\%$ relative at SC $= 85\\%$) than low ones ($\\pm 5.1\\%$ at SC $= 39\\%$). A relative $\\pm 5\\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\\geq 75\\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.\n\n\\paragraph{Conditional Correction Ratio data.}\n\\label{app:cil-data}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\\text{CCR} < 0$: same-model SICA or weak capability gap.}\n\\label{tab:cil_main}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nGenerator--Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral $\\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\\\\nMistral $\\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\\\\nMistral $\\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen-14B $\\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\\\\nMistral $\\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral $\\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\\\\nQwen-14B $\\times$ SICA & PW & $-$4.21 & $-$2.50 \\\\\nMistral $\\times$ SICA & PW & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade details.}\n\\label{app:drc}\nDRC invokes NLI only when SC consensus falls below threshold $\\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\\%$), consistent with the capability-gap hypothesis (\\S\\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\\ref{app:2x2}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\\tau{=}0.7$ recovers 83--90\\% of full-combo gain at ${\\sim}35\\%$ NLI cost across both datasets.}\n\\label{tab:drc}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Method & Acc.\\ & NLI Calls & Cost & Recovery \\\\\n\\midrule\n\\multirow{3}{*}{PW-D5} & SC only & 39.33\\% & 0/600 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{45.33\\%} & \\textbf{207/600} & \\textbf{34.5\\%} & \\textbf{90.0\\%} \\\\\n& Full combo & 46.00\\% & 600/600 & 100\\% & 100\\% \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO} & SC only & 55.88\\% & 0/204 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{58.33\\%} & \\textbf{71/204} & \\textbf{34.8\\%} & \\textbf{83.3\\%} \\\\\n& Full combo & 58.82\\% & 204/204 & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%, gap\\,$+$15.67}}}\n  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 46.00 & $+$6.67 & $1.13{\\times}10^{-5}$ & $6.78{\\times}10^{-5}$ & {***} \\\\\n  & 5 & 50.33 & $+$11.00 & $6.18{\\times}10^{-7}$ & $7.41{\\times}10^{-6}$ & {***} \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%, gap\\,$-$17.50}}}\n  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\\\\n  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen2.5-14B\\\\{\\scriptsize SC\\,74.00\\%, gap\\,$-$19.00}}}\n  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\\\\n  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize SC\\,85.83\\%, gap\\,$-$30.83}}}\n  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\\\\n  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{BART-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}\n\\label{tab:bart-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\\pm$0.00 & --- \\\\\nQwen2.5-14B {\\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoBERTa-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}\n\\label{tab:roberta-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\\\\nQwen2.5-14B {\\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FOLIO NLI combo results.}\n\\label{app:folio-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\\ref{tab:cross-model-ablation}).}\n\\label{tab:folio-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 58.82 & $+$2.94 & n.s. \\\\\n & 5 & & 59.80 & $+$3.92 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 65.20 & $-$0.98 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\n & 3 & & 75.49 & $-$0.49 & n.s. \\\\\n & 5 & & 73.53 & $-$2.45 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.80 & $+$1.47 & n.s. \\\\\n & 5 & & 83.33 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \\emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}\n\\label{tab:folio-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\\\\n & 3 & & 56.37 & $+$0.49 & n.s. \\\\\n & 5 & & 56.86 & $+$0.98 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\\\\n & 3 & & 67.65 & $+$1.47 & n.s. \\\\\n & 5 & & 64.71 & $-$1.47 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 72.55 & $-$3.43 & .039{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 82.84 & $-$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \\emph{degradation} at $w{=}5$ ($p{=}.012$)---the same capability-gap signature as BART.}\n\\label{tab:folio-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 57.84 & $+$1.96 & n.s. \\\\\n & 5 & & 58.82 & $+$2.94 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 66.67 & $+$0.49 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 71.57 & $-$4.41 & .012{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 83.82 & $+$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LogiQA NLI combo results.}\n\\label{app:logiqa-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\n\\label{tab:logiqa-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 54.00 & $+$1.00 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\\\\n & 3 & & 58.00 & $-$1.50 & n.s. \\\\\n & 5 & & 58.00 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.00 & $-$1.00 & n.s. \\\\\n & 5 & & 78.00 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 80.50 & $-$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}\n\\label{tab:logiqa-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 52.50 & $-$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\\\\n & 3 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 81.50 & $+$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\\% standalone). All three NLI verifiers produce the same null result on LogiQA.}\n\\label{tab:logiqa-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\\\\n & 3 & & 58.50 & $-$1.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier results.}\n\\label{app:finetuned-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\\cap$SC-incorrect to SC-correct$\\cap$NLI-incorrect.}\n\\label{tab:finetuned-nli}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}lrrrrc@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & Compl.\\ ratio \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%}}}\n  & 1 & 42.17 & $+$2.83 & \\multirow{3}{*}{364:2} \\\\\n  & 3 & 52.00 & $+$12.67 & \\\\\n  & 5 & 65.50 & $+$26.17 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%}}}\n  & 1 & 76.00 & $+$3.50 & \\multirow{3}{*}{164:1} \\\\\n  & 3 & 84.17 & $+$11.67 & \\\\\n  & 5 & 91.67 & $+$19.17 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model voting ablation.}\n\\label{app:cross-model-ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model voting ablation ($w \\in \\{3,5\\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators---worsening at higher $w$---while NLI combo does not, indicating that structural independence---not merely model diversity---drives the escape.}\n\\label{tab:cross-model-ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccrl@{}}\n\\toprule\nGenerator & Voter/Verifier & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{ProofWriter ($n{=}600$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\\\\n  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\\\\n\\addlinespace\n\\multirow{5}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\\\\n  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\\\\n  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\\\\n  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\\\\n  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\\\\n  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\\\\n  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\\\\n  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{FOLIO ($n{=}204$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\\\\n  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\\\\n  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\\\\n  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\n  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\n  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\\\\n  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\\\\n  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Generator$\\times$Extractor 2$\\times$2 Matrix.}\n\\label{app:2x2}\n\nTable~\\ref{tab:2x2-folio} reports the full $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\\sim}25$\\,pp vs.\\ column difference ${\\sim}3$\\,pp), contrasting with ProofWriter where the extractor dominates ($\\Delta$ range ${\\pm}40$--$50$\\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\\Delta = +2.94$\\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\\Delta = +2.94$\\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\\Delta$ is coincidental---the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FOLIO $2{\\times}2$ generator${\\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}\n\\label{tab:2x2-folio}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Extractor & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & BR \\\\\n\\midrule\n\\multirow{2}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize $\\kappa{=}0.46$}}}\n  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\\\\n  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\\\\n\\addlinespace\n\\multirow{2}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize $\\kappa{=}0.79$}}}\n  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\\\\n  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Single-Trace and Aggregation Statistics}\n\\label{app:single-trace}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Single-trace accuracy (mean $\\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\\ref{tab:main_results}).}\n\\label{tab:single-trace-stats}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & Single (\\%) & Std & SC@12 (\\%) & Gain (pp) \\\\\n\\midrule\nMistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\\\\nQwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\\\\nQwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize Inter-trace standard deviation shrinks $2.8\\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\\S\\ref{sec:cross-arch}).}\n\\end{table}\n\n\\paragraph{Extraction temperature sensitivity.}\n\\label{app:text-sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of extraction temperature $T_{\\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\\dagger$\\,Uses a different trace set (SC $= 54.41\\%$); all other conditions share the same traces (SC $= 55.88\\%$).}\n\\label{tab:text-sensitivity}\n\\begin{tabular}{@{}cccr@{}}\n\\toprule\n$T_{\\text{ext}}$ & SICA (\\%) & $\\Delta$ vs.\\ SC (pp) & Avg.\\ \\#Constr. \\\\\n\\midrule\n0.1 & 57.35 & $+$1.47 & 69.3 \\\\\n$0.3^\\dagger$ & 59.31 & $+$3.43 & 68.8 \\\\\n0.5 & 56.37 & $+$0.49 & 68.2 \\\\\n0.7 & 53.43 & $-$2.45 & 67.3 \\\\\n1.0 & 55.39 & $-$0.49 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across four model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); all ProofWriter conditions show consistently negative $\\Delta$ across all seeds ($p < .001$ for LLaMA-8B and Mistral-7B). Qwen3-14B results pending.}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all eight Mistral-7B and LLaMA-8B seeds yield negative $\\Delta$ (range $-1.33$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The consistency across seeds confirms that negative $\\Delta$ on ProofWriter is not an artifact of any single random sample.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}\n\\label{tab:subpop-constraint}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rr rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Tertile} & $n$ & $\\bar{c}$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO-204}\n & Low \\scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\\hphantom{00} \\\\\n & Mid \\scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\\rlap{*} \\\\\n & High \\scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n\\midrule\n\\multirow{3}{*}{PW-600}\n & Low \\scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\\\\n & Mid \\scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\\\\n & High \\scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\\hphantom{00} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\\,pp overall (55.9\\% $\\to$ 59.3\\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).\nThe gain concentrates in the mid-constraint tertile ($+$9.4\\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.\nOn ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\\Delta{=}{-}0.5$\\,pp, $p{=}1.0$).\nWe note that with six subgroup tests, one significant result at $\\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.\n\n\\paragraph{Individual intervention significance.}\n\\label{app:intervention-individual}\nOf the 27 training-free remediation strategies (Figure~\\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\\to$Mistral ($+0.98$\\,pp) and Generational ($+0.49$\\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\\label{app:limitations-extended}\n\n\\paragraph{SCB versus CoT unfaithfulness.}\nSCB is distinct from CoT unfaithfulness \\citep{turpin2023language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \\emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias---the constraint $P(\\text{answer\\_A})$ reflects vote share, not logical validity. The shuffle control (\\S\\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.\n\n\\paragraph{Implications for neuro-symbolic practitioners.}\nOur results do not imply that neuro-symbolic methods are inherently flawed---they imply that \\emph{self-extracted} constraints cannot provide independent verification. The key distinction is \\emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \\citep{ye2024satlm}, Logic-LM \\citep{pan2023logiclm}) formalize the problem \\emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\\S\\ref{sec:cross-arch}) and use the diagnostic framework in \\S\\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.\n\n\\paragraph{Test-time scaling implications.}\nVote diversity decreases with model capability: $K_\\text{eff}$ drops from 3.62 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \\citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\\kappa$ analysis (\\S\\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level---traces that disagree on final answers still share 69\\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\\S\\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.\n\n\\paragraph{SCB diagnostic toolkit.}\n\\label{app:diagnostic-toolkit}\nWe recommend four zero-cost diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.\n\\emph{Bias Ratio} (BR; \\S\\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\\text{BR} > 1$ indicates constraints are biased toward the majority; $\\text{BR} \\gg 2$ (as in all nine models tested; Table~\\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\\pm$ bootstrap 95\\% CI.\n\\emph{Effective-K} ($K_\\text{eff}$; Eq.~\\ref{eq:effk}): compute Fleiss' $\\kappa$ across $K$ traces, then $K_\\text{eff} = 1 + (K-1)(1-\\kappa)$. Threshold: $K_\\text{eff} \\leq 1.30$ never improves in our experiments---aggregation collapses to majority voting. $K_\\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.\n\\emph{Degenerate Consensus} ($C_0$; \\S\\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\\%$ renders aggregation moot; $C_0 < 5\\%$ means the model is maximally uncertain and constraints tend to amplify noise.\n\\emph{ProcessSim} (Eq.~\\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\\text{BR} > 2$, this predicts SCB will dominate.\nA practitioner should compute all four on a held-out sample ($n \\geq 50$). If $K_\\text{eff} \\leq 1.30$ or $C_0 > 95\\%$ or ($\\text{BR} > 2$ and $\\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.\n\n\\paragraph{BR permutation null model.}\n\\label{app:br-permutation}\nThe permutation test referenced in \\S\\ref{sec:confirmation-bias} proceeds as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item For each problem $p$ with extracted constraints $\\{c_1, \\ldots, c_M\\}$ and source answers $\\{a_1, \\ldots, a_M\\}$:\n\\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).\n\\item Compute $\\text{BR}_\\text{null}$ from the permuted assignments.\n\\item Repeat $10{,}000$ times to obtain the null distribution.\n\\item Compute $p$-value $= |\\{r : \\text{BR}_\\text{null}^{(r)} \\geq \\text{BR}_\\text{obs}\\}| / 10{,}000$.\n\\end{enumerate}\nAcross all tested conditions, $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.\n\n\\paragraph{Future directions: trained extractors and beyond.}\n\\label{app:future-directions}\nOur oracle controls reveal that perfect extraction would yield $+29.90$\\,pp over SC on Mistral-7B FOLIO---self-extraction captures only ${\\sim}12\\%$ of this ceiling. This gap motivates several future directions.\n\\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence---the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\\S\\ref{sec:cross-arch}).\n\\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\\S\\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.\n\\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.\n\\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.\n\n\\paragraph{SCB as an evaluation framework.}\n\\label{app:scb-evaluation}\nThe SCB metrics---BR, $K_\\text{eff}$, ProcessSim, and CCR---can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \\citep{huang2024selfcorrect}, self-refinement \\citep{madaan2023selfrefine}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-consistency \\citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\\text{BR} < 1$, high $K_\\text{eff}$, and $\\text{CCR} > 0$ demonstrates genuine self-improvement; $\\text{BR} > 1$ with $\\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.\n\n\\paragraph{Additional scope considerations.}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers ($\\forall$/$\\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\\sim}$10\\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 593,
        "oldLines": 7,
        "newStart": 593,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.",
          " ",
          "-\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.066$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.",
          "+\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.",
          " ",
          " ",
          " \\section{Cross-Model Confirmation Bias}"
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_01WMiRdwU4qJ5v3NqKxgsfit`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "old_string": "BH adj.\\ $p = 0.066$, $m{=}6$)",
  "new_string": "BH adj.\\ $p = 0.042$, $m{=}6$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a8f7a45b-0970-402e-8e9c-44d53f23e345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 71 · 2026-05-24T04:52:06.174Z_

<details><summary>↩ Tool result · `toolu_01WMiRdwU4qJ5v3NqKxgsfit`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "73c2571f-85ba-47fc-a464-2c08d2d95aba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "oldString": "BH adj.\\ $p = 0.066$, $m{=}6$)",
    "newString": "BH adj.\\ $p = 0.042$, $m{=}6$)",
    "originalFile": "\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability-Accuracy Constraint Diagnostics}\n\\label{app:diagnostics}\n\\label{app:cil}\n\n\\paragraph{Conditional Correction Ratio.}\nWe define the \\textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:\n\\begin{equation}\n\\label{eq:cil}\n\\text{CCR}(V, G) = \\log \\frac{P(V \\text{ correct} \\mid G \\text{ wrong})}{P(V \\text{ correct} \\mid G \\text{ correct})}.\n\\end{equation}\n$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n\n\\paragraph{Empirical CCR across verifier--generator pairs.}\nTable~\\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\\rho = 0.839$, 95\\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\\text{CCR} < 0$: same-model SICA or mismatched capability gap.}\n\\label{tab:cil_empirical}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllrr@{}}\n\\toprule\nGenerator & Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\\\\nMistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\\\\nMistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\\\\nMistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\\\\nQwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\\\\nMistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-condition diagnostics.}\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Oracle Control}\n\\label{app:oracle}\n\\label{sec:oracle}\n\\label{app:pw-oracle-subtype}\n\nReplacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \\times 10^{-7}$), and $+17.17$\\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\\Delta$ ($+3.43$\\,pp) captures only 11.5\\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\\,pp) against an oracle ceiling of $+17.17$\\,pp, indicating that stronger models do not self-extract more effectively.\n\n\\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 90.26 & \\textbf{98.70} & +8.44 \\\\\nAttNeg & 160 & 81.88 & \\textbf{91.88} & +10.00 \\\\\nRelNoneg & 146 & 60.96 & \\textbf{84.25} & +23.29 \\\\\nRelNeg & 140 & 60.71 & \\textbf{89.29} & +28.58 \\\\\n\\midrule\nOverall & 600 & 74.00 & \\textbf{91.17} & +17.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAX-SAT vs.\\ count-only agreement across constraint weight $\\alpha \\in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\\times$, seed 42); Qwen2.5-14B (BR $= 3.85\\times$, seed 123). $\\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\\alpha{=}1$: full source-attribution penalty. Agreement $\\geq 99\\%$ at all $\\alpha$ including endpoints, confirming vacuity is weight-insensitive.}\n\\label{tab:alpha-ablation}\n\\begin{tabular}{@{}crr@{}}\n\\toprule\n$\\alpha$ & Mistral Agr.\\ (\\%) & Qwen2.5 Agr.\\ (\\%) \\\\\n\\midrule\n0.0 & 100 & 100 \\\\\n0.1 & 100 & 100 \\\\\n0.3 & 100 & 100 \\\\\n0.5 & 100 & 100 \\\\\n0.7 & 99 & 100 \\\\\n0.9 & 99 & 100 \\\\\n1.0 & 99 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 83.33\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\addlinespace\n24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\\\\n25 & Premise-only filter & Constraint sel.\\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\\\\n26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\\text{sel}}{=}8$ \\\\\n27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\\% UNSAT \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 25.0\\% of the oracle ceiling ($+13.73$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\\times$, $3.85\\times$, $2.88\\times$) are reported in \\S\\ref{sec:confirmation-bias}. LLaMA weighted BR CI: [2.19, 3.28].\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\\ correct problems. Wrong \\%: weighted fraction of constraints supporting the incorrect majority on error problems. $\\Delta$: SICA $-$ SC (pp).}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & BR (wtd.) & Wrong (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $4.24\\times$ & 80.9 & $+$4.90 \\\\\nQwen2.5-14B & $3.69\\times$ & 78.7 & $-$0.98 \\\\\nLLaMA-3.1-8B & $2.66\\times$ & 72.7 & $-$4.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Frontier model universality.}\n\\label{app:frontier-scb}\nTable~\\ref{tab:frontier-scb} (main text, \\S\\ref{sec:confirmation-bias}) extends confirmation bias analysis to nine models spanning 7B open-source to frontier closed-source. All models exhibit $\\text{BR} > 1$ (range: $1.66$--$4.97\\times$). Extraction context varies: open-source models use self-extraction (the model extracts constraints from its own traces); frontier models use cross-model extraction (Mistral-7B extracts FOL from the target model's traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction.\n\n\\paragraph{ProcessSim definition.}\n\\label{app:process-sim}\nProcess similarity is the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.\n\n\\paragraph{Process-$\\kappa$ gradient.}\n\\label{app:process-gradient}\nUnder cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\\ref{tab:process-gradient}; Spearman $\\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\\kappa_{\\text{proc}}$) \\emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\\kappa_{\\text{proc}} = 0.248$, $\\text{BR} = 2.92$) and gains $+2.45$\\,pp; o3 has moderate trace diversity ($\\kappa_{\\text{proc}} = 0.596$) but near-minimal bias ($\\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\\% of error problems have $\\text{BR} = \\infty$ but low finite-BR), yielding $\\Delta = 0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Process-$\\kappa$ gradient under cross-model extraction (Mistral-7B $\\rightarrow$ target model traces, FOLIO). $\\kappa_{\\text{proc}}$: process-level cosine similarity. $\\Delta$: SICA $-$ SC (pp). Spearman $\\rho(\\kappa_{\\text{proc}} \\rightarrow \\Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}\n\\label{tab:process-gradient}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & $\\kappa_{\\text{proc}}$ & $\\Delta$ (pp) & BR \\\\\n\\midrule\nR1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\\\\ngpt-5.5 & 0.563 & $+$0.49 & 3.48 \\\\\no3 & 0.596 & 0.00 & 1.66 \\\\\nGemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\\\\ngpt-4.1 & 0.792 & $-$1.47 & 2.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Trace independence metrics.}\n\\label{app:trace-independence}\n\nTable~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.066$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & 86.27 & $+$0.49 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.77 & 1.26 & 83.33 & $+$1.47 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.30 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B (s456) & FOLIO & 0.51 & 1.82 & 55.88 & 0.00 \\\\\nMistral-7B & FOLIO & 0.50 & 1.84 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.49 & 1.88 & 54.41 & $+$2.94 \\\\\nMistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B (multi-T) & FOLIO & 0.48 & 1.91 & 57.84 & 0.00 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.44$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.03$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.22 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.44 & 2.02 & 56.86 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.21 & 3.62 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\\ TF-IDF $0.74$), widening the gap over answer-level $\\kappa = 0.55$. The process homogeneity finding is robust to representation choice.\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-trace constraint yield uniformity.}\n\\label{app:yield-cv}\n\nObservation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\\% of problems fall below $\\text{CV} = 0.3$, and 91.2\\% below $0.5$, supporting the uniformity assumption. Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \\times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \\times 10^{-11}$). Although statistically significant, the absolute difference (${\\sim}0.6$ constraints, $< 12\\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\\%$ of problems regardless of yield variation.\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{TOST Equivalence Tests}\n\\label{app:tost}\n\nWe apply two one-sided tests (TOST) \\citep{lakens2017equivalence} with equivalence margin $\\pm 2$\\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \\emph{equivalent} (TOST significant), \\emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \\emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\\Delta| \\leq 2$\\,pp effects.\n\n\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\n\\label{tab:tost-sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMargin & Equivalent & Different & Underpowered \\\\\n\\midrule\n$\\pm 1$\\,pp & 0 & 2 & 14 \\\\\n$\\pm 2$\\,pp & 4 & 2 & 10 \\\\\n$\\pm 3$\\,pp & 10 & 0 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Relative-margin TOST.}\n\\label{app:relative_tost}\nThe absolute $\\pm 2$\\,pp margin is more stringent at high baselines ($\\pm 2.4\\%$ relative at SC $= 85\\%$) than low ones ($\\pm 5.1\\%$ at SC $= 39\\%$). A relative $\\pm 5\\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\\geq 75\\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.\n\n\\paragraph{Conditional Correction Ratio data.}\n\\label{app:cil-data}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\\text{CCR} < 0$: same-model SICA or weak capability gap.}\n\\label{tab:cil_main}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nGenerator--Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral $\\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\\\\nMistral $\\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\\\\nMistral $\\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen-14B $\\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\\\\nMistral $\\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral $\\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\\\\nQwen-14B $\\times$ SICA & PW & $-$4.21 & $-$2.50 \\\\\nMistral $\\times$ SICA & PW & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade details.}\n\\label{app:drc}\nDRC invokes NLI only when SC consensus falls below threshold $\\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\\%$), consistent with the capability-gap hypothesis (\\S\\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\\ref{app:2x2}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\\tau{=}0.7$ recovers 83--90\\% of full-combo gain at ${\\sim}35\\%$ NLI cost across both datasets.}\n\\label{tab:drc}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Method & Acc.\\ & NLI Calls & Cost & Recovery \\\\\n\\midrule\n\\multirow{3}{*}{PW-D5} & SC only & 39.33\\% & 0/600 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{45.33\\%} & \\textbf{207/600} & \\textbf{34.5\\%} & \\textbf{90.0\\%} \\\\\n& Full combo & 46.00\\% & 600/600 & 100\\% & 100\\% \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO} & SC only & 55.88\\% & 0/204 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{58.33\\%} & \\textbf{71/204} & \\textbf{34.8\\%} & \\textbf{83.3\\%} \\\\\n& Full combo & 58.82\\% & 204/204 & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%, gap\\,$+$15.67}}}\n  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 46.00 & $+$6.67 & $1.13{\\times}10^{-5}$ & $6.78{\\times}10^{-5}$ & {***} \\\\\n  & 5 & 50.33 & $+$11.00 & $6.18{\\times}10^{-7}$ & $7.41{\\times}10^{-6}$ & {***} \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%, gap\\,$-$17.50}}}\n  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\\\\n  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen2.5-14B\\\\{\\scriptsize SC\\,74.00\\%, gap\\,$-$19.00}}}\n  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\\\\n  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize SC\\,85.83\\%, gap\\,$-$30.83}}}\n  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\\\\n  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{BART-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}\n\\label{tab:bart-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\\pm$0.00 & --- \\\\\nQwen2.5-14B {\\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoBERTa-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}\n\\label{tab:roberta-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\\\\nQwen2.5-14B {\\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FOLIO NLI combo results.}\n\\label{app:folio-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\\ref{tab:cross-model-ablation}).}\n\\label{tab:folio-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 58.82 & $+$2.94 & n.s. \\\\\n & 5 & & 59.80 & $+$3.92 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 65.20 & $-$0.98 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\n & 3 & & 75.49 & $-$0.49 & n.s. \\\\\n & 5 & & 73.53 & $-$2.45 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.80 & $+$1.47 & n.s. \\\\\n & 5 & & 83.33 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \\emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}\n\\label{tab:folio-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\\\\n & 3 & & 56.37 & $+$0.49 & n.s. \\\\\n & 5 & & 56.86 & $+$0.98 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\\\\n & 3 & & 67.65 & $+$1.47 & n.s. \\\\\n & 5 & & 64.71 & $-$1.47 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 72.55 & $-$3.43 & .039{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 82.84 & $-$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \\emph{degradation} at $w{=}5$ ($p{=}.012$)---the same capability-gap signature as BART.}\n\\label{tab:folio-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 57.84 & $+$1.96 & n.s. \\\\\n & 5 & & 58.82 & $+$2.94 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 66.67 & $+$0.49 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 71.57 & $-$4.41 & .012{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 83.82 & $+$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LogiQA NLI combo results.}\n\\label{app:logiqa-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\n\\label{tab:logiqa-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 54.00 & $+$1.00 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\\\\n & 3 & & 58.00 & $-$1.50 & n.s. \\\\\n & 5 & & 58.00 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.00 & $-$1.00 & n.s. \\\\\n & 5 & & 78.00 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 80.50 & $-$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}\n\\label{tab:logiqa-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 52.50 & $-$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\\\\n & 3 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 81.50 & $+$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\\% standalone). All three NLI verifiers produce the same null result on LogiQA.}\n\\label{tab:logiqa-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\\\\n & 3 & & 58.50 & $-$1.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier results.}\n\\label{app:finetuned-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\\cap$SC-incorrect to SC-correct$\\cap$NLI-incorrect.}\n\\label{tab:finetuned-nli}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}lrrrrc@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & Compl.\\ ratio \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%}}}\n  & 1 & 42.17 & $+$2.83 & \\multirow{3}{*}{364:2} \\\\\n  & 3 & 52.00 & $+$12.67 & \\\\\n  & 5 & 65.50 & $+$26.17 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%}}}\n  & 1 & 76.00 & $+$3.50 & \\multirow{3}{*}{164:1} \\\\\n  & 3 & 84.17 & $+$11.67 & \\\\\n  & 5 & 91.67 & $+$19.17 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model voting ablation.}\n\\label{app:cross-model-ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model voting ablation ($w \\in \\{3,5\\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators---worsening at higher $w$---while NLI combo does not, indicating that structural independence---not merely model diversity---drives the escape.}\n\\label{tab:cross-model-ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccrl@{}}\n\\toprule\nGenerator & Voter/Verifier & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{ProofWriter ($n{=}600$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\\\\n  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\\\\n\\addlinespace\n\\multirow{5}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\\\\n  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\\\\n  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\\\\n  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\\\\n  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\\\\n  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\\\\n  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\\\\n  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{FOLIO ($n{=}204$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\\\\n  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\\\\n  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\\\\n  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\n  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\n  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\\\\n  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\\\\n  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Generator$\\times$Extractor 2$\\times$2 Matrix.}\n\\label{app:2x2}\n\nTable~\\ref{tab:2x2-folio} reports the full $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\\sim}25$\\,pp vs.\\ column difference ${\\sim}3$\\,pp), contrasting with ProofWriter where the extractor dominates ($\\Delta$ range ${\\pm}40$--$50$\\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\\Delta = +2.94$\\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\\Delta = +2.94$\\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\\Delta$ is coincidental---the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FOLIO $2{\\times}2$ generator${\\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}\n\\label{tab:2x2-folio}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Extractor & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & BR \\\\\n\\midrule\n\\multirow{2}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize $\\kappa{=}0.46$}}}\n  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\\\\n  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\\\\n\\addlinespace\n\\multirow{2}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize $\\kappa{=}0.79$}}}\n  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\\\\n  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Single-Trace and Aggregation Statistics}\n\\label{app:single-trace}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Single-trace accuracy (mean $\\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\\ref{tab:main_results}).}\n\\label{tab:single-trace-stats}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & Single (\\%) & Std & SC@12 (\\%) & Gain (pp) \\\\\n\\midrule\nMistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\\\\nQwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\\\\nQwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize Inter-trace standard deviation shrinks $2.8\\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\\S\\ref{sec:cross-arch}).}\n\\end{table}\n\n\\paragraph{Extraction temperature sensitivity.}\n\\label{app:text-sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of extraction temperature $T_{\\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\\dagger$\\,Uses a different trace set (SC $= 54.41\\%$); all other conditions share the same traces (SC $= 55.88\\%$).}\n\\label{tab:text-sensitivity}\n\\begin{tabular}{@{}cccr@{}}\n\\toprule\n$T_{\\text{ext}}$ & SICA (\\%) & $\\Delta$ vs.\\ SC (pp) & Avg.\\ \\#Constr. \\\\\n\\midrule\n0.1 & 57.35 & $+$1.47 & 69.3 \\\\\n$0.3^\\dagger$ & 59.31 & $+$3.43 & 68.8 \\\\\n0.5 & 56.37 & $+$0.49 & 68.2 \\\\\n0.7 & 53.43 & $-$2.45 & 67.3 \\\\\n1.0 & 55.39 & $-$0.49 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across four model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); all ProofWriter conditions show consistently negative $\\Delta$ across all seeds ($p < .001$ for LLaMA-8B and Mistral-7B). Qwen3-14B results pending.}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all eight Mistral-7B and LLaMA-8B seeds yield negative $\\Delta$ (range $-1.33$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The consistency across seeds confirms that negative $\\Delta$ on ProofWriter is not an artifact of any single random sample.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}\n\\label{tab:subpop-constraint}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rr rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Tertile} & $n$ & $\\bar{c}$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO-204}\n & Low \\scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\\hphantom{00} \\\\\n & Mid \\scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\\rlap{*} \\\\\n & High \\scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n\\midrule\n\\multirow{3}{*}{PW-600}\n & Low \\scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\\\\n & Mid \\scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\\\\n & High \\scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\\hphantom{00} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\\,pp overall (55.9\\% $\\to$ 59.3\\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).\nThe gain concentrates in the mid-constraint tertile ($+$9.4\\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.\nOn ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\\Delta{=}{-}0.5$\\,pp, $p{=}1.0$).\nWe note that with six subgroup tests, one significant result at $\\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.\n\n\\paragraph{Individual intervention significance.}\n\\label{app:intervention-individual}\nOf the 27 training-free remediation strategies (Figure~\\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\\to$Mistral ($+0.98$\\,pp) and Generational ($+0.49$\\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\\label{app:limitations-extended}\n\n\\paragraph{SCB versus CoT unfaithfulness.}\nSCB is distinct from CoT unfaithfulness \\citep{turpin2023language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \\emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias---the constraint $P(\\text{answer\\_A})$ reflects vote share, not logical validity. The shuffle control (\\S\\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.\n\n\\paragraph{Implications for neuro-symbolic practitioners.}\nOur results do not imply that neuro-symbolic methods are inherently flawed---they imply that \\emph{self-extracted} constraints cannot provide independent verification. The key distinction is \\emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \\citep{ye2024satlm}, Logic-LM \\citep{pan2023logiclm}) formalize the problem \\emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\\S\\ref{sec:cross-arch}) and use the diagnostic framework in \\S\\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.\n\n\\paragraph{Test-time scaling implications.}\nVote diversity decreases with model capability: $K_\\text{eff}$ drops from 3.62 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \\citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\\kappa$ analysis (\\S\\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level---traces that disagree on final answers still share 69\\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\\S\\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.\n\n\\paragraph{SCB diagnostic toolkit.}\n\\label{app:diagnostic-toolkit}\nWe recommend four zero-cost diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.\n\\emph{Bias Ratio} (BR; \\S\\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\\text{BR} > 1$ indicates constraints are biased toward the majority; $\\text{BR} \\gg 2$ (as in all nine models tested; Table~\\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\\pm$ bootstrap 95\\% CI.\n\\emph{Effective-K} ($K_\\text{eff}$; Eq.~\\ref{eq:effk}): compute Fleiss' $\\kappa$ across $K$ traces, then $K_\\text{eff} = 1 + (K-1)(1-\\kappa)$. Threshold: $K_\\text{eff} \\leq 1.30$ never improves in our experiments---aggregation collapses to majority voting. $K_\\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.\n\\emph{Degenerate Consensus} ($C_0$; \\S\\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\\%$ renders aggregation moot; $C_0 < 5\\%$ means the model is maximally uncertain and constraints tend to amplify noise.\n\\emph{ProcessSim} (Eq.~\\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\\text{BR} > 2$, this predicts SCB will dominate.\nA practitioner should compute all four on a held-out sample ($n \\geq 50$). If $K_\\text{eff} \\leq 1.30$ or $C_0 > 95\\%$ or ($\\text{BR} > 2$ and $\\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.\n\n\\paragraph{BR permutation null model.}\n\\label{app:br-permutation}\nThe permutation test referenced in \\S\\ref{sec:confirmation-bias} proceeds as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item For each problem $p$ with extracted constraints $\\{c_1, \\ldots, c_M\\}$ and source answers $\\{a_1, \\ldots, a_M\\}$:\n\\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).\n\\item Compute $\\text{BR}_\\text{null}$ from the permuted assignments.\n\\item Repeat $10{,}000$ times to obtain the null distribution.\n\\item Compute $p$-value $= |\\{r : \\text{BR}_\\text{null}^{(r)} \\geq \\text{BR}_\\text{obs}\\}| / 10{,}000$.\n\\end{enumerate}\nAcross all tested conditions, $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.\n\n\\paragraph{Future directions: trained extractors and beyond.}\n\\label{app:future-directions}\nOur oracle controls reveal that perfect extraction would yield $+29.90$\\,pp over SC on Mistral-7B FOLIO---self-extraction captures only ${\\sim}12\\%$ of this ceiling. This gap motivates several future directions.\n\\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence---the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\\S\\ref{sec:cross-arch}).\n\\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\\S\\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.\n\\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.\n\\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.\n\n\\paragraph{SCB as an evaluation framework.}\n\\label{app:scb-evaluation}\nThe SCB metrics---BR, $K_\\text{eff}$, ProcessSim, and CCR---can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \\citep{huang2024selfcorrect}, self-refinement \\citep{madaan2023selfrefine}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-consistency \\citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\\text{BR} < 1$, high $K_\\text{eff}$, and $\\text{CCR} > 0$ demonstrates genuine self-improvement; $\\text{BR} > 1$ with $\\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.\n\n\\paragraph{Additional scope considerations.}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers ($\\forall$/$\\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\\sim}$10\\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 694,
        "oldLines": 7,
        "newStart": 694,
        "newLines": 7,
        "lines": [
          " \\centering",
          " \\small",
          " \\setlength{\\tabcolsep}{3pt}",
          "-\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.066$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}",
          "+\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.042$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}",
          " \\label{tab:independence}",
          " \\begin{tabular}{@{}llccrr@{}}",
          " \\toprule"
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01CREbufCThFrrHDYQypG68i`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
  "old_string": "$14\\times$ over zero-shot",
  "new_string": "up to $14\\times$ over zero-shot (LLaMA-8B)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "97d21aac-ddcb-4b79-9562-da694d85f463",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XApQLn1KuqjcgbD1zfPpZm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 53260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2019
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

_source line 73 · 2026-05-24T04:52:07.324Z_

<details><summary>↩ Tool result · `toolu_01CREbufCThFrrHDYQypG68i`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a7fc252f-db00-423a-837f-6f5c541b7c90",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex",
    "oldString": "$14\\times$ over zero-shot",
    "newString": "up to $14\\times$ over zero-shot (LLaMA-8B)",
    "originalFile": "\\section{Escaping the Bottleneck}\n\\label{sec:solutions}\n\\label{sec:cross-arch}\n\n\\paragraph{Motivation.}\n\\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\\S\\ref{sec:remediation}). The DPI bound implies that any escape must break the self-extraction dependency: $I(C;Y) \\leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.\n\n\\paragraph{Method.}\n\\looseness=-1 We use DeBERTa-large \\citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \\citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).\n\n\\paragraph{Zero-shot results.}\n\\looseness=-1 DeBERTa NLI alone achieves 49.51\\% on FOLIO and 55.00\\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\\,pp on FOLIO (n.s.); all generators with SC $\\geq 72\\%$ show no significant improvement ($\\Delta \\leq +1.47$\\,pp). Same-model SICA \\emph{degrades} ProofWriter ($-2.83$\\,pp; Table~\\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.\n\n\\paragraph{Capability gap.}\n\\looseness=-1 Across 108 verifier-generator-weight combinations spanning three NLI architectures, four generators, and three domains, gain decreases monotonically with generator accuracy---a \\emph{capability-gap pattern}. Of 72 above-verifier conditions, none shows a significant improvement; all significant gains concentrate below the verifier's standalone accuracy. The pattern is quantified by a perfect rank correlation across architectures ($\\rho = 1.0$, $p = 0.003$, $n{=}6$; Figure~\\ref{fig:capability-gap}). On ProofWriter ($n{=}600$; Table~\\ref{tab:cross_generator_nli}), only Mistral-7B (SC below DeBERTa's 55.00\\%) gains significantly ($+6.67$\\,pp, $p < 0.001$). At $w{=}5$, BART and RoBERTa \\emph{degrade} Qwen2.5-14B ($-3.43$/$-4.41$\\,pp; Appendix~\\ref{app:multi-nli}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-generator NLI escape with DeBERTa-large-mnli verifier (55.00\\% standalone, ProofWriter $n{=}600$). Combo gain decreases monotonically with generator capability. Only Mistral-7B (SC below the verifier) shows a significant $w{=}3$ gain.}\n\\label{tab:cross_generator_nli}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Family & SC & Gap & Combo $\\Delta$ ($w{=}3$) & $p$ \\\\\n\\midrule\nMistral-7B & Mistral & 39.33\\% & $+$15.67 & $+$6.67\\,pp & $<$0.001 \\\\\nLLaMA-3.1-8B & LLaMA & 72.50\\% & $-$17.50 & $+$0.83\\,pp & 0.665 \\\\\nQwen2.5-14B & Qwen & 74.00\\% & $-$19.00 & $+$0.67\\,pp & 0.503 \\\\\nQwen3-14B & Qwen & 85.83\\% & $-$30.83 & $+$0.50\\,pp & 0.453 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier.}\n\\looseness=-1 Fine-tuning DeBERTa on ProofWriter depth-5 OWA (99.67\\% standalone) amplifies escape: $+$12.67/$+$11.67\\,pp for Mistral-7B/LLaMA-8B ($14\\times$ over zero-shot; Table~\\ref{tab:finetuned-nli}), extending gains to generators with SC up to ${\\sim}$72\\%. A cost-aware cascade recovers 83--90\\% of gain at ${\\sim}$35\\% cost (Appendix~\\ref{app:drc}). These results serve as directional evidence (the domain-adapted verifier introduces training).\n\n\\paragraph{Cross-model voting vs.\\ cross-architecture NLI.}\n\\looseness=-1 An ensemble diversity control replaces the NLI verifier with a second LLM as cross voter ($w{=}3$). With Mistral-7B as cross voter on ProofWriter, all three strong generators degrade significantly ($-2.33$ to $-9.33$\\,pp, all $p \\leq 0.020$); even a stronger cross voter (Qwen2.5-14B) degrades Qwen3-14B at $w{=}5$ ($-2.50$\\,pp, $p = 0.006$). In contrast, DeBERTa NLI at comparable standalone accuracy (55.00\\%) never degrades any generator ($\\Delta \\leq +0.83$\\,pp). This asymmetry reflects the structural independence of encoder-only NLI---different architecture, training objective, and input representation---from autoregressive biases shared across LLM families (Table~\\ref{tab:cross-model-ablation}).\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 7,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          " \\end{table}",
          " ",
          " \\paragraph{Domain-adapted verifier.}",
          "-\\looseness=-1 Fine-tuning DeBERTa on ProofWriter depth-5 OWA (99.67\\% standalone) amplifies escape: $+$12.67/$+$11.67\\,pp for Mistral-7B/LLaMA-8B ($14\\times$ over zero-shot; Table~\\ref{tab:finetuned-nli}), extending gains to generators with SC up to ${\\sim}$72\\%. A cost-aware cascade recovers 83--90\\% of gain at ${\\sim}$35\\% cost (Appendix~\\ref{app:drc}). These results serve as directional evidence (the domain-adapted verifier introduces training).",
          "+\\looseness=-1 Fine-tuning DeBERTa on ProofWriter depth-5 OWA (99.67\\% standalone) amplifies escape: $+$12.67/$+$11.67\\,pp for Mistral-7B/LLaMA-8B (up to $14\\times$ over zero-shot (LLaMA-8B); Table~\\ref{tab:finetuned-nli}), extending gains to generators with SC up to ${\\sim}$72\\%. A cost-aware cascade recovers 83--90\\% of gain at ${\\sim}$35\\% cost (Appendix~\\ref{app:drc}). These results serve as directional evidence (the domain-adapted verifier introduces training).",
          " ",
          " \\paragraph{Cross-model voting vs.\\ cross-architecture NLI.}",
          " \\looseness=-1 An ensemble diversity control replaces the NLI verifier with a second LLM as cross voter ($w{=}3$). With Mistral-7B as cross voter on ProofWriter, all three strong generators degrade significantly ($-2.33$ to $-9.33$\\,pp, all $p \\leq 0.020$); even a stronger cross voter (Qwen2.5-14B) degrades Qwen3-14B at $w{=}5$ ($-2.50$\\,pp, $p = 0.006$). In contrast, DeBERTa NLI at comparable standalone accuracy (55.00\\%) never degrades any generator ($\\Delta \\leq +0.83$\\,pp). This asymmetry reflects the structural independence of encoder-only NLI---different architecture, training objective, and input representation---from autoregressive biases shared across LLM families (Table~\\ref{tab:cross-model-ablation})."
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

_source line 74_

All 7 edits done. Now let me verify the edits and compile.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "175aea73-5b59-4b33-b1d8-1a22abe9e3ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSi33aPr94yxcCxvHgBPEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3660,
      "cache_read_input_tokens": 55279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3660
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

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_01VovnFDvdLUmyubUCHeFPcs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "a29215c5-ea2c-46fe-ac3f-f1ad478c663b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSi33aPr94yxcCxvHgBPEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3660,
      "cache_read_input_tokens": 55279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3660
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

_source line 76 · 2026-05-24T04:52:23.138Z_

<details><summary>↩ Tool result · `toolu_01VovnFDvdLUmyubUCHeFPcs`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$, adj.\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$, adj.\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,BH adj.\ $p = 0.042$; $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\Delta = 0$ and are reported separately in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule
19	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
20	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
21	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
22	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
23	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
24	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
25	\midrule
26	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
27	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
28	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
29	\addlinespace
30	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
31	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
32	Qwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\
33	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
34	Qwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\
35	\addlinespace
36	Qwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\
37	Qwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
38	Qwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\
39	\bottomrule
40	\end{tabular}
41	\end{table*}
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=\columnwidth]{f2_regime_scatter}
46	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--60\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.042$).}
47	\label{fig:regime-scatter}
48	\end{figure}
49	
50	\looseness=-1 Figure~\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$ at $K = 12$ (Table~\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\leq 40\%$), where low accuracy causes error amplification; an intermediate band (50--60\%), containing the only positive trends; and Type~A (SC $\geq 60\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\Delta$ ranges from $+2.94$ to $-2.45$\,pp despite $\kappa \in [0.45, 0.51]$. We trace the mechanism in \S\ref{sec:analysis}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "1c6e3676-3d06-4036-8af7-62a962a34f28",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,BH adj.\\ $p = 0.042$; $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.042$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.21 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.62$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.51]$. We trace the mechanism in \\S\\ref{sec:analysis}.",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01JDDAAjfNWKZ8cwDaiZszxy`</summary>

```json
{
  "command": "latexmk -pdf main.tex 2>&1 | tail -20",
  "description": "Compile LaTeX document",
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
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "7bb914ff-9a41-4139-85b4-3f42d6f1d939",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSi33aPr94yxcCxvHgBPEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3660,
      "cache_read_input_tokens": 55279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3660
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

### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "by6nr2zsw",
  "tool_use_id": "toolu_01JDDAAjfNWKZ8cwDaiZszxy",
  "description": "Compile LaTeX document",
  "task_type": "local_bash",
  "uuid": "f9f885fd-db5c-49fb-9198-457272e3376d",
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c"
}
```

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "by6nr2zsw",
  "tool_use_id": "toolu_01JDDAAjfNWKZ8cwDaiZszxy",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX document",
  "uuid": "5dd4d792-c9e4-4104-b620-22457227479e",
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c"
}
```

---

### Tool result

_source line 80 · 2026-05-24T04:52:33.328Z_

<details><summary>↩ Tool result · `toolu_01JDDAAjfNWKZ8cwDaiZszxy`</summary>

```text
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utm
r8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (29 pages, 668637 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "f2bdd4a3-315b-447a-8408-e19a64582e38",
  "tool_use_result": {
    "stdout": ".pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrb8a.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utm\nr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (29 pages, 668637 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01BZWvmuXZqLfGVp2EArCoiH`</summary>

```json
{
  "command": "grep -i \"error\\|warning\" main.log | grep -v \"Font shape\\|Size substitutions\\|float specifier\\|multiply defined\\|citation\\|Rerun\\|Label(s)\" | head -20",
  "description": "Check compilation errors/warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "7664e229-1175-4a9f-8c3c-921654b9be17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2TUBXw4eybCEAFoHQgskU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2808,
      "cache_read_input_tokens": 58939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2808
      },
      "output_tokens": 38,
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

_source line 82 · 2026-05-24T04:52:40.396Z_

<details><summary>↩ Tool result · `toolu_01BZWvmuXZqLfGVp2EArCoiH`</summary>

```text
Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.1}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.2}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.3}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.4}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.5}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.6}) 
pdfTeX warning (ext4): destination with the same identifier (name{ALG@line.7})
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "215834be-f855-4b19-a144-cb4da3bd63b0",
  "tool_use_result": {
    "stdout": "Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)\npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.1}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.2}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.3}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.4}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.5}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.6}) \npdfTeX warning (ext4): destination with the same identifier (name{ALG@line.7})",
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

_source line 83_

编译通过，无错误。ALG@line 警告是既有问题（多个 algorithm 环境共享行号），不影响输出。

## 修改汇总

### D1: BH correction p-value 修正

**根因**：BH 实现缺少单调性强制步骤。`0.011 × 6/1 = 0.066` 是 rank-1 的初始值，但标准 BH 要求 `min(0.066, rank-2 的 0.042) = 0.042`。`statsmodels.multipletests(method='fdr_bh')` 验证两个条件均 adj p = 0.042 < 0.05，显著。

**5 处修改：**

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `experiments.tex` | 5 | "No condition shows a significant SICA effect after FDR control...both reach adjusted p = 0.066" | "Two confirmatory conditions show significant degradation after BH FDR control...adj. p = 0.042...No condition shows a significant positive effect" |
| `experiments.tex` | 10 | "No condition shows a significant gain after BH correction" | "Two conditions show significant degradation after BH correction...no condition shows a significant gain" |
| `experiments.tex` | 10 | "{*} uncorrected p < 0.05 (BH adj. p = 0.066)" | "{*} BH adj. p = 0.042" |
| `experiments.tex` | 46 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 596 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 697 | "BH adj. p = 0.066, m=6" | "BH adj. p = 0.042, m=6" |

### D2: Abstract 词数

191 词，已在 200 限制内，无需修改。

### D3: "14× over zero-shot" 修正

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `solutions.tex` | 35 | `$14\times$ over zero-shot` | `up to $14\times$ over zero-shot (LLaMA-8B)` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "uuid": "66cec42f-5715-4ea5-886c-4a5d3dfada3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8517Etssvq58Hzhn7xZjS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 61747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 340
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

_source line 84_

编译通过，无错误。ALG@line 警告是既有问题（多个 algorithm 环境共享行号），不影响输出。

## 修改汇总

### D1: BH correction p-value 修正

**根因**：BH 实现缺少单调性强制步骤。`0.011 × 6/1 = 0.066` 是 rank-1 的初始值，但标准 BH 要求 `min(0.066, rank-2 的 0.042) = 0.042`。`statsmodels.multipletests(method='fdr_bh')` 验证两个条件均 adj p = 0.042 < 0.05，显著。

**5 处修改：**

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `experiments.tex` | 5 | "No condition shows a significant SICA effect after FDR control...both reach adjusted p = 0.066" | "Two confirmatory conditions show significant degradation after BH FDR control...adj. p = 0.042...No condition shows a significant positive effect" |
| `experiments.tex` | 10 | "No condition shows a significant gain after BH correction" | "Two conditions show significant degradation after BH correction...no condition shows a significant gain" |
| `experiments.tex` | 10 | "{*} uncorrected p < 0.05 (BH adj. p = 0.066)" | "{*} BH adj. p = 0.042" |
| `experiments.tex` | 46 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 596 | "BH adj. p = 0.066" | "BH adj. p = 0.042" |
| `appendix.tex` | 697 | "BH adj. p = 0.066, m=6" | "BH adj. p = 0.042, m=6" |

### D2: Abstract 词数

191 词，已在 200 限制内，无需修改。

### D3: "14× over zero-shot" 修正

| 文件 | 行 | 旧值 | 新值 |
|---|---|---|---|
| `solutions.tex` | 35 | `$14\times$ over zero-shot` | `up to $14\times$ over zero-shot (LLaMA-8B)` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 338500,
  "duration_api_ms": 333353,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "88dd4cac-745e-4701-a7b3-bec955cff63c",
  "total_cost_usd": 0.9659285000000001,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 50246,
    "cache_read_input_tokens": 500658,
    "output_tokens": 15989,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 50246,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 647,
        "cache_read_input_tokens": 61747,
        "cache_creation_input_tokens": 340,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 340
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1692,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001767,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 15989,
      "cacheReadInputTokens": 500658,
      "cacheCreationInputTokens": 50246,
      "webSearchRequests": 0,
      "costUSD": 0.9641615000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "07baf0c2-e329-4467-8221-2b33d989d7d0"
}
```

</details>

---
