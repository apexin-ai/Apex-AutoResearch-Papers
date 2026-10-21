# analysis rho paper impact list

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_analysis_rho_paper_impact_list_20260515T132710.log`
- **Structured JSON:** [`4217b32195eb0256866f.json`](../../sessions/42/4217b32195eb0256866f.json)

## Before a recorded user message

58 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "53a2d3b0-2dba-43a2-9f8f-1702e9326113",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778868600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fd5ed86a-8e20-418e-ae48-9c0327bb5b54",
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the unified rho JSON and the paper tex files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "2339f0e9-b6ae-49f7-9f09-929b56fab0e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqJMG2pYvkLJmBKz6bQKsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Read · `toolu_01KdxfBtRtdgupMHyXccUJGd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_unified_rho.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "834e61f8-0154-4c00-b2a9-cfa8292bec39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqJMG2pYvkLJmBKz6bQKsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
      },
      "output_tokens": 26,
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

_source line 6 · 2026-05-15T13:27:23.121Z_

<details><summary>↩ Tool result · `toolu_01KdxfBtRtdgupMHyXccUJGd`</summary>

```text
1	{
2	  "audit_date": "2026-05-15",
3	  "pipeline": "unified (gold-filtered, consistency.py FK/SJ, evaluation.py per_instance_f1)",
4	  "filter": "exclude instances where len(gold.entities) == 0",
5	  "experiments": {
6	    "exp_017_llama_conll_n16_r1024": {
7	      "description": "LLaMA CoNLL seed42 n16 r1024",
8	      "n_total": 3453,
9	      "n_gold_empty": 697,
10	      "n_valid": 2756,
11	      "n_conditional": 2641,
12	      "old_registry_rho_fk": 0.8095,
13	      "old_registry_rho_sj": 0.1815,
14	      "unified_full": {
15	        "rho_fk": 0.4752,
16	        "rho_sj": 0.4836,
17	        "rho_vc": 0.4746,
18	        "rho_em": 0.4818,
19	        "rho_lp": 0.3136,
20	        "auroc_fk": 0.7467,
21	        "auroc_sj": 0.7496,
22	        "auroc_vc": 0.7529,
23	        "auroc_em": 0.7508,
24	        "auroc_lp": 0.7661,
25	        "median_f1": 1.0
26	      },
27	      "unified_conditional": {
28	        "rho_fk": 0.4767,
29	        "rho_sj": 0.4856
30	      }
31	    },
32	    "exp_017_llama_conll_n16_s456_r1024": {
33	      "description": "LLaMA CoNLL seed456 n16 r1024",
34	      "n_total": 3453,
35	      "n_gold_empty": 697,
36	      "n_valid": 2756,
37	      "n_conditional": 2642,
38	      "old_registry_rho_fk": 0.8085,
39	      "old_registry_rho_sj": 0.1895,
40	      "unified_full": {
41	        "rho_fk": 0.469,
42	        "rho_sj": 0.4734,
43	        "rho_vc": 0.4722,
44	        "rho_em": 0.4752,
45	        "rho_lp": 0.3099,
46	        "auroc_fk": 0.7408,
47	        "auroc_sj": 0.7428,
48	        "auroc_vc": 0.7495,
49	        "auroc_em": 0.7444,
50	        "auroc_lp": 0.7628,
51	        "median_f1": 1.0
52	      },
53	      "unified_conditional": {
54	        "rho_fk": 0.4694,
55	        "rho_sj": 0.4728
56	      }
57	    },
58	    "exp_001_n16_seed456": {
59	      "description": "Qwen SciERC seed456 joint n16",
60	      "n_total": 551,
61	      "n_gold_empty": 22,
62	      "n_valid": 529,
63	      "n_conditional": 478,
64	      "old_registry_rho_fk": 0.3448,
65	      "old_registry_rho_sj": 0.4134,
66	      "unified_full_ner": {
67	        "rho_fk": 0.2723,
68	        "rho_sj": 0.4098,
69	        "rho_vc": 0.4449,
70	        "rho_em": 0.3363,
71	        "rho_lp": 0.2415,
72	        "auroc_fk": 0.6179,
73	        "auroc_sj": 0.6823,
74	        "auroc_vc": 0.6981,
75	        "auroc_em": 0.649,
76	        "auroc_lp": 0.5885,
77	        "median_f1": 0.6667
78	      },
79	      "unified_conditional_ner": {
80	        "rho_fk": 0.1887,
81	        "rho_sj": 0.3735
82	      },
83	      "unified_re": {
84	        "n_re_valid": 397,
85	        "rho_fk": 0.2929,
86	        "rho_sj": 0.2835
87	      }
88	    },
89	    "exp_011_ood_conll_to_scierc": {
90	      "description": "OOD ConLL-trained on SciERC test",
91	      "n_total": 551,
92	      "n_gold_empty": 22,
93	      "n_valid": 529,
94	      "n_conditional": 12,
95	      "registry_already_correct": true,
96	      "unified_full": {
97	        "rho_fk": -0.0695,
98	        "rho_sj": -0.1857,
99	        "rho_vc": 0.1972,
100	        "rho_em": -0.2015,
101	        "rho_lp": -0.1521
102	      }
103	    }
104	  }
105	}
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "0240c67d-a930-4554-a5ce-029bc1464255",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_unified_rho.json",
      "content": "{\n  \"audit_date\": \"2026-05-15\",\n  \"pipeline\": \"unified (gold-filtered, consistency.py FK/SJ, evaluation.py per_instance_f1)\",\n  \"filter\": \"exclude instances where len(gold.entities) == 0\",\n  \"experiments\": {\n    \"exp_017_llama_conll_n16_r1024\": {\n      \"description\": \"LLaMA CoNLL seed42 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2641,\n      \"old_registry_rho_fk\": 0.8095,\n      \"old_registry_rho_sj\": 0.1815,\n      \"unified_full\": {\n        \"rho_fk\": 0.4752,\n        \"rho_sj\": 0.4836,\n        \"rho_vc\": 0.4746,\n        \"rho_em\": 0.4818,\n        \"rho_lp\": 0.3136,\n        \"auroc_fk\": 0.7467,\n        \"auroc_sj\": 0.7496,\n        \"auroc_vc\": 0.7529,\n        \"auroc_em\": 0.7508,\n        \"auroc_lp\": 0.7661,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4767,\n        \"rho_sj\": 0.4856\n      }\n    },\n    \"exp_017_llama_conll_n16_s456_r1024\": {\n      \"description\": \"LLaMA CoNLL seed456 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2642,\n      \"old_registry_rho_fk\": 0.8085,\n      \"old_registry_rho_sj\": 0.1895,\n      \"unified_full\": {\n        \"rho_fk\": 0.469,\n        \"rho_sj\": 0.4734,\n        \"rho_vc\": 0.4722,\n        \"rho_em\": 0.4752,\n        \"rho_lp\": 0.3099,\n        \"auroc_fk\": 0.7408,\n        \"auroc_sj\": 0.7428,\n        \"auroc_vc\": 0.7495,\n        \"auroc_em\": 0.7444,\n        \"auroc_lp\": 0.7628,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4694,\n        \"rho_sj\": 0.4728\n      }\n    },\n    \"exp_001_n16_seed456\": {\n      \"description\": \"Qwen SciERC seed456 joint n16\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 478,\n      \"old_registry_rho_fk\": 0.3448,\n      \"old_registry_rho_sj\": 0.4134,\n      \"unified_full_ner\": {\n        \"rho_fk\": 0.2723,\n        \"rho_sj\": 0.4098,\n        \"rho_vc\": 0.4449,\n        \"rho_em\": 0.3363,\n        \"rho_lp\": 0.2415,\n        \"auroc_fk\": 0.6179,\n        \"auroc_sj\": 0.6823,\n        \"auroc_vc\": 0.6981,\n        \"auroc_em\": 0.649,\n        \"auroc_lp\": 0.5885,\n        \"median_f1\": 0.6667\n      },\n      \"unified_conditional_ner\": {\n        \"rho_fk\": 0.1887,\n        \"rho_sj\": 0.3735\n      },\n      \"unified_re\": {\n        \"n_re_valid\": 397,\n        \"rho_fk\": 0.2929,\n        \"rho_sj\": 0.2835\n      }\n    },\n    \"exp_011_ood_conll_to_scierc\": {\n      \"description\": \"OOD ConLL-trained on SciERC test\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 12,\n      \"registry_already_correct\": true,\n      \"unified_full\": {\n        \"rho_fk\": -0.0695,\n        \"rho_sj\": -0.1857,\n        \"rho_vc\": 0.1972,\n        \"rho_em\": -0.2015,\n        \"rho_lp\": -0.1521\n      }\n    }\n  }\n}\n",
      "numLines": 106,
      "startLine": 1,
      "totalLines": 106
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01RYrFThVknGo1BNwWcaLErL`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "d874f488-ad05-4d35-83ff-1306971f327c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqJMG2pYvkLJmBKz6bQKsm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
      },
      "output_tokens": 26,
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

_source line 8 · 2026-05-15T13:27:23.656Z_

<details><summary>↩ Tool result · `toolu_01RYrFThVknGo1BNwWcaLErL`</summary>

```text
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/sections/method.tex
docs/paper/sections/introduction.tex
docs/paper/sections/related_work.tex
docs/paper/sections/limitations.tex
docs/paper/main.tex
docs/paper/sections/discussion.tex
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "286d9254-ea72-4635-bdba-92066f690ba7",
  "tool_use_result": {
    "filenames": [
      "docs/paper/abstract.tex",
      "docs/paper/discussion.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/experiments.tex"
    ],
    "durationMs": 18,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_018W9WL8s98festwh4dFgafa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "96c85fcf-97f9-4b19-abaa-919b2be1b02c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 10 · 2026-05-15T13:27:26.578Z_

<details><summary>↩ Tool result · `toolu_018W9WL8s98festwh4dFgafa`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\ref{app:n_scaling}. A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .694 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17 ($N{=}16$), where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances separates binary success detection (can the model extract \textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.
79	This reshuffles signal rankings (Figure~\ref{fig:signal_heatmap}, right).
80	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
81	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
82	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
83	
84	%% ============================================================
85	\subsection{The Correlation-Selection Gap}
86	\label{sec:selection_gap}
87	
88	\begin{figure*}[t]
89	\centering
90	\includegraphics[width=\textwidth]{fig_selection_gap}
91	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
92	\label{fig:selection_gap}
93	\end{figure*}
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\ref{eq:voting}).}
99	\label{tab:selection}
100	\begin{tabular}{lcc}
101	\toprule
102	Method & NER F1 & RE F1 \\
103	\midrule
104	Oracle & 0.776 & 0.585 \\
105	\midrule
106	LP           & \textbf{0.650} & 0.395 \\
107	SJ       & 0.645 & 0.386 \\
108	EM        & 0.636 & 0.372 \\
109	VC                 & 0.634 & 0.359 \\
110	\midrule
111	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
112	Random             & 0.608 & 0.354 \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
118	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
119	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
120	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
121	
122	\paragraph{No significant improvement over greedy.}
123	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
124	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
125	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
126	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\ref{app:lp_failure_stability}).
127	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
128	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{significantly below} greedy ($\Delta{=}{-}2.6$~pp, $p{<}0.03$ across 3 seeds).
129	The gap extends to CoNLL at $N{=}8$ (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
130	
131	\paragraph{Quality estimation $\neq$ output selection.}
132	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
133	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
134	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
135	
136	%% ============================================================
137	\subsection{Robustness}
138	\label{sec:robustness_main}
139	
140	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
141	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
142	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "e2bbfe22-4e4a-44fa-946e-0e38cd5fd01d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\\ref{app:n_scaling}. A 3-seed stability analysis ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .694 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .601 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{Semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17 ($N{=}16$), where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances separates binary success detection (can the model extract \\textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.\nThis reshuffles signal rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\\ref{eq:voting}).}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\\ref{app:lp_failure_stability}).\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{significantly below} greedy ($\\Delta{=}{-}2.6$~pp, $p{<}0.03$ across 3 seeds).\nThe gap extends to CoNLL at $N{=}8$ (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nOn RE, only VC consistently outperforms LP ($\\Delta\\rho{=}{+}0.012$, preliminary).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01TV5Frgx1jwyvXYniXVzZZ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "01043749-e160-4cf5-9956-0cf398287431",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 12 · 2026-05-15T13:27:27.054Z_

<details><summary>↩ Tool result · `toolu_01TV5Frgx1jwyvXYniXVzZZ6`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled NER ablation (\S\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{Connection to MBR decoding.}
20	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
21	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
22	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
23	
24	\paragraph{Score compression under free-form decoding.}\label{sec:ablation}
25	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
26	We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
27	For NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.
28	However, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).
29	This reversal falls within the NER bootstrap 95\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.
30	The NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.
31	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
32	
33	\paragraph{Task-specific decoding interactions.}
34	The free-form ablation reveals divergent behavior across tasks.
35	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
36	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
37	This interaction does not generalize to NER, where selection remains negligible under both regimes.
38	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
39	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
40	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
41	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
42	
43	\paragraph{Methodological implications.}
44	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
45	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.
46	Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
47	Our findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.
48	Whether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "9805356c-10da-43d2-91ea-f9f51623d11e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.\nAt higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) with lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nLP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\\varepsilon{=}0.05$ threshold at which 60\\% of instances are effectively tied, and 75\\% of pairwise comparisons fall within $|\\Delta|{<}0.026$ (Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled NER ablation (\\S\\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression under free-form decoding.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nFor NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.\nHowever, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).\nThis reversal falls within the NER bootstrap 95\\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.\nThe NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation reveals divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.\nCross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\\rho{=}0.469$ OOD vs.\\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\\ref{app:ood}).\nOur findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.\nWhether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01HqQX3hfBjce69hisWvzJmV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "d07238f4-624b-4b86-a2ce-23b240f4d35a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 14 · 2026-05-15T13:27:27.535Z_

<details><summary>↩ Tool result · `toolu_01HqQX3hfBjce69hisWvzJmV`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2025scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	Four of five signals are instance-level by construction---this is definitional, not empirical.
24	The non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{Evaluation framework and metric dissociation.}
39	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection.
40	    These metrics decouple: EM leads AUROC (0.749) but ranks third in $\rho$ (0.295), demonstrating that single-metric evaluation risks selecting the wrong signal.
41	
42	    \item \textbf{Diagnosing why selection fails beyond definitional limitations.}
43	    Four of five signals are instance-level by definition and cannot rank candidates---this is not an empirical finding.
44	    The empirical contribution is diagnosing why the two mechanisms that \textit{could} bridge the gap both fail: (a)~consensus-proximity selection (MBR decoding) correlates with quality across instances but not within them; (b)~log-probability scores are compressed into effective ties (60\% of instances within $\varepsilon{=}0.05$), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
45	    A controlled NER ablation confirms that LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), suggesting task-dependent interaction with decoding regime.
46	
47	    \item \textbf{Task-complexity boundary conditions.}
48	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
49	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \citet{nedellec2026consistency}'s quality-estimation analysis.
50	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
51	\end{enumerate}
52	
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "1e286f52-327b-4120-a670-cb77ef97008b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2025scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nFour of five signals are instance-level by construction---this is definitional, not empirical.\nThe non-trivial questions are whether (a)~consensus-proximity selection, instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding}, can recover per-sample discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), revealing task-dependent interaction with decoding regime (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: high inter-sample agreement correlates with high F1 (quality estimation). \\textbf{Right}: instance-level signals assign identical scores to all candidates, precluding sample selection.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Evaluation framework and metric dissociation.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection.\n    These metrics decouple: EM leads AUROC (0.749) but ranks third in $\\rho$ (0.295), demonstrating that single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{Diagnosing why selection fails beyond definitional limitations.}\n    Four of five signals are instance-level by definition and cannot rank candidates---this is not an empirical finding.\n    The empirical contribution is diagnosing why the two mechanisms that \\textit{could} bridge the gap both fail: (a)~consensus-proximity selection (MBR decoding) correlates with quality across instances but not within them; (b)~log-probability scores are compressed into effective ties (60\\% of instances within $\\varepsilon{=}0.05$), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    A controlled NER ablation confirms that LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), suggesting task-dependent interaction with decoding regime.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$)---phenomena invisible on a single dataset that extend \\citet{nedellec2026consistency}'s quality-estimation analysis.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01A4jqG5TSbp2bKW9UHi5aoG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "20de01c0-e646-4e6a-ab65-37ee0f418eb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 16 · 2026-05-15T13:27:27.966Z_

<details><summary>↩ Tool result · `toolu_01A4jqG5TSbp2bKW9UHi5aoG`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majority fraction---the proportion of samples producing the most common output:
29	\begin{equation}\label{eq:em}
30	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
31	\end{equation}
32	
33	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
34	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
35	\begin{equation}\label{eq:fk}
36	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
37	\end{equation}
38	where $\bar{P}$ is mean observed pairwise agreement and $\bar{P}_e$ is expected agreement under random assignment.
39	While FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.
40	Empirically, we measure excess agreement ($\bar{P} - \bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\% and $-$4.0\%, indicating mild \textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.
41	(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)
42	Unlike structural signals, FK relies on exact string matching and does not tolerate surface variations.
43	
44	\paragraph{Soft Jaccard (structural, instance-level).}
45	Our primary structural signal extends Jaccard similarity \cite{jaccard1901distribution} to extracted entity/relation sets.
46	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:
47	\begin{equation}\label{eq:sj}
48	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
49	\end{equation}
50	where $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.
51	We use $\max(|g_i|, |g_j|)$ rather than $|g_i \cup g_j|$ as the normalizer to penalize length asymmetry between samples.
52	The instance-level signal averages over all pairs:
53	\begin{equation}\label{eq:sj_instance}
54	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
55	\end{equation}
56	
57	\paragraph{Entity voting confidence (structural, instance-level).}
58	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
59	The instance-level confidence is the mean frequency:
60	\begin{equation}\label{eq:voting}
61	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
62	\end{equation}
63	When $E_\cup = \emptyset$ (no entity extracted by any sample), we set $c_{\mathrm{vc}}(x) = 0$.\footnote{This occurs in $<$1\% of instances in our experiments (WNUT-17 only). Equation~\ref{eq:voting} defines the continuous QE signal used throughout Table~\ref{tab:quality_estimation} and all correlation analyses. For voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\rho{=}0.252$ (vs.\ $0.379$ for Eq.~\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\Delta\rho{=}0.019$).}
64	
65	\subsection{Evaluation Framework}\label{sec:evaluation}
66	
67	\paragraph{Quality estimation.}
68	We measure rank correlation (Spearman $\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.
69	
70	\paragraph{Sample selection.}
71	We report best-of-$N$ F1: for each instance, the signal selects one sample.
72	Per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).
73	We compare against an \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$, $N{=}1$).
74	
75	\paragraph{Complementarity.}
76	High rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\S\ref{sec:selection_gap}).
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "5842892e-914c-446b-bbb7-ffb51bddb84a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}.\nEach $y_i$ is an entity set (NER) or relation set (RE).\nA confidence signal $c$ serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among $N$ candidates.\n\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct candidate ranking.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\nNotation is summarized in Appendix~\\ref{app:notation}.\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe use \\textit{confidence signal} as the umbrella term for all five measures.\nFour are \\textit{consistency signals}---computed from inter-sample agreement---spanning two families: \\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \\textit{surface} (exact match [EM], Fleiss' $\\kappa$ [FK]).\nThe fifth, log-probability, is the sole \\textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal.\nFor sample $y_i$ with tokens $t_1, \\ldots, t_{|y_i|}$:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{&lt;j}, x)\n\\end{equation}\n\n\\paragraph{Exact match voting (surface, instance-level).}\nThe majority fraction---the proportion of samples producing the most common output:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{N} \\max_{y} \\big|\\{i : y_i = y\\}\\big|\n\\end{equation}\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is mean observed pairwise agreement and $\\bar{P}_e$ is expected agreement under random assignment.\nWhile FK assumes independent raters, temperature-based sampling yields mild negative dependence rather than positive correlation among samples.\nEmpirically, we measure excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations (SciERC NER/RE, CoNLL, WNUT-17; $N{=}8$, $T{=}1.0$) and find values between $-$0.4\\% and $-$4.0\\%, indicating mild \\textit{negative} dependence---samples from the same model tend to err on different items---which confirms that FK is not inflated by inter-sample dependence.\n(All excess agreement values are negative across 5 configurations; a one-sample $t$-test against zero yields $p{<}0.05$.)\nUnlike structural signals, FK relies on exact string matching and does not tolerate surface variations.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur primary structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to extracted entity/relation sets.\nFor samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching via the Hungarian algorithm (maximizing total token-level IoU; zero-IoU pairs automatically receive zero weight), and define:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{\\sum_{m \\in M} \\text{sim}(a_m, b_m)}{\\sum_{g} \\max(|g_i|, |g_j|)}\n\\end{equation}\nwhere $M$ is the matched set from the Hungarian algorithm (without minimum similarity threshold), $\\text{sim}(a_m, b_m)$ is the token-level IoU (intersection of tokens divided by union of tokens) between matched entity spans $a_m$ and $b_m$, and $g_i, g_j$ index per-type extraction counts.\nWe use $\\max(|g_i|, |g_j|)$ rather than $|g_i \\cup g_j|$ as the normalizer to penalize length asymmetry between samples.\nThe instance-level signal averages over all pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i&lt;j} \\text{SJ}(y_i, y_j)\n\\end{equation}\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nFor each entity $e$ in the union $E_\\cup$ of all samples, we compute frequency $\\text{freq}(e) = |\\{i : e \\in y_i\\}| / N$.\nThe instance-level confidence is the mean frequency:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nWhen $E_\\cup = \\emptyset$ (no entity extracted by any sample), we set $c_{\\mathrm{vc}}(x) = 0$.\\footnote{This occurs in $<$1\\% of instances in our experiments (WNUT-17 only). Equation~\\ref{eq:voting} defines the continuous QE signal used throughout Table~\\ref{tab:quality_estimation} and all correlation analyses. For voted-output \\textit{selection} (Table~\\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting. The two computations serve different purposes: Eq.~\\ref{eq:voting} assigns a continuous quality score per instance; the majority threshold constructs a discrete output for F1 evaluation. On NER, the threshold variant yields $\\rho{=}0.252$ (vs.\\ $0.379$ for Eq.~\\ref{eq:voting}), reflecting information loss from binarization; on RE, the difference is negligible ($\\Delta\\rho{=}0.019$).}\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\n\\paragraph{Quality estimation.}\nWe measure rank correlation (Spearman $\\rho$) between the confidence signal and instance-level F1, and binary discrimination (AUROC) by classifying instances as above or below median F1.\n\n\\paragraph{Sample selection.}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample.\nPer-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to the consensus output (the consensus-proximity score for SJ is mathematically equivalent to leave-one-out SJ selection).\nWe compare against an \\textit{oracle} (highest-F1 sample) and \\textit{greedy} ($T{=}0$, $N{=}1$).\n\n\\paragraph{Complementarity.}\nHigh rank correlation does not guarantee effective sample selection: if per-sample variance is low, even a perfect quality estimator cannot distinguish among near-identical candidates (\\S\\ref{sec:selection_gap}).\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_016vzXTMbkU2xeSfZanPAMkQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "3fa692c2-dfdd-4228-a162-128a10c4bf94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 18 · 2026-05-15T13:27:28.897Z_

<details><summary>↩ Tool result · `toolu_016vzXTMbkU2xeSfZanPAMkQ`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We evaluate five confidence signals on three NER benchmarks and one RE benchmark with two 8B-parameter model families.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom.
5	Given that four of five signals are instance-level by construction and cannot rank candidates, the empirical question is whether per-sample log-probability or consensus-proximity selection (MBR decoding) can bridge the gap.
6	Neither succeeds: log-probability scores are compressed into effective ties within instances (median within-instance range 0.041 nats), and MBR utility correlates with quality across instances but not within them.
7	A controlled NER ablation confirms that LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary, single seed), suggesting task-dependent interaction with decoding regime.
8	These findings, observed across two model families at 8B scale, indicate that closing the gap likely requires per-sample scoring beyond unsupervised signals.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "d4f6e1ed-1a1c-43ee-a837-0e4d68ccadac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nWe evaluate five confidence signals on three NER benchmarks and one RE benchmark with two 8B-parameter model families.\nAll signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom.\nGiven that four of five signals are instance-level by construction and cannot rank candidates, the empirical question is whether per-sample log-probability or consensus-proximity selection (MBR decoding) can bridge the gap.\nNeither succeeds: log-probability scores are compressed into effective ties within instances (median within-instance range 0.041 nats), and MBR utility correlates with quality across instances but not within them.\nA controlled NER ablation confirms that LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary, single seed), suggesting task-dependent interaction with decoding regime.\nThese findings, observed across two model families at 8B scale, indicate that closing the gap likely requires per-sample scoring beyond unsupervised signals.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_014VB1XigwWNwXffoBBN6jzQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "2460f3ab-b6a2-483f-8a70-5352ab637438",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 20 · 2026-05-15T13:27:29.401Z_

<details><summary>↩ Tool result · `toolu_014VB1XigwWNwXffoBBN6jzQ`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "7e1d3fa2-5456-4d0c-bc3b-d1e88c67a52c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.\nAll signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom---the \\textit{correlation-selection gap}.\nThe instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.\nMBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.\nSignal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.\nRE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.\nTrained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01BuAZc91cghGgGvUsU7Jfi5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "95f2cc54-f6ef-460f-ba81-4c1dd6f31681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 22 · 2026-05-15T13:27:30.179Z_

<details><summary>↩ Tool result · `toolu_01BuAZc91cghGgGvUsU7Jfi5`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
82	
83	\paragraph{Transfer across model families.}
84	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
85	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
86	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
87	
88	\section{Calibration Analysis}\label{app:calibration}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{fig_reliability}
93	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
94	\label{fig:reliability}
95	\end{figure*}
96	
97	Reliability diagrams use 10 equal-width bins.
98	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
99	
100	\section{Additional Analyses}\label{app:additional}
101	
102	\paragraph{Per-relation diagnostic.}
103	RE signal degradation is relation-specific.
104	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
105	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
106	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
107	
108	\paragraph{Capability stratification.}
109	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
110	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
111	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
112	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
113	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
114	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
115	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
116	
117	\paragraph{Length vs.\ log-probability.}
118	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
123	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
124	\label{fig:length_logprob_scatter}
125	\end{figure}
126	
127	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
128	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
130	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
131	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
132	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
133	Evaluation circularity is negligible.
134	
135	\paragraph{Conditional filtering details.}
136	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
137	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
138	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
139	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
140	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
141	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
142	
143	\paragraph{WNUT-17 full signal analysis.}
144	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
145	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
146	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
147	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
153	\label{tab:wnut}
154	\begin{tabular}{lccccc}
155	\toprule
156	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
157	\midrule
158	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
159	FK      & .125 & .001 & .555 & .169 & .002 \\
160	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
161	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
162	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{Cross-configuration selection analysis.}
168	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
169	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
170	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
171	
172	\begin{table*}[t]
173	\centering
174	\small
175	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
176	\label{tab:cross_selection}
177	\begin{tabular}{llccccccc}
178	\toprule
179	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
180	\midrule
181	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
182	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
183	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
184	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
185	\bottomrule
186	\end{tabular}
187	\end{table*}
188	
189	\paragraph{Diminishing returns of $N$-scaling.}
190	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
191	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
192	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
193	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
194	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
195	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
196	
197	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
198	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
199	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
200	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
201	This reinforces the core finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
202	
203	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
204	
205	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
206	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
207	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
208	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
214	\label{tab:bootstrap_signal_ci}
215	\begin{tabular}{lcc}
216	\toprule
217	Signal & $\rho$ & 95\% CI \\
218	\midrule
219	VC & +0.379 & [+0.299, +0.456] \\
220	SJ & +0.360 & [+0.277, +0.437] \\
221	EM & +0.295 & [+0.212, +0.371] \\
222	FK & +0.267 & [+0.176, +0.354] \\
223	LP & +0.205 & [+0.119, +0.291] \\
224	\bottomrule
225	\end{tabular}
226	
227	\vspace{0.5em}
228	
229	\begin{tabular}{lccc}
230	\toprule
231	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
232	\midrule
233	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
234	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
235	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
236	\bottomrule
237	\end{tabular}
238	
239	\smallskip
240	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
241	\end{table}
242	
243	\section{Diversity and Selection Analysis}\label{app:diversity}
244	
245	\paragraph{Output diversity quantification.}
246	Table~\ref{tab:diversity} summarizes output diversity across configurations.
247	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
248	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
249	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
250	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
256	\label{tab:diversity}
257	\begin{tabular}{lcc}
258	\toprule
259	Config & Identical & Unique \\
260	\midrule
261	Qwen/SciERC & 11\% & 43\% \\
262	LLaMA/SciERC & 18\% & 39\% \\
263	Qwen/CoNLL & 57\% & --- \\
264	LLaMA/CoNLL & 88\% & --- \\
265	WNUT-17 & 55\% & --- \\
266	\bottomrule
267	\end{tabular}
268	\end{table}
269	
270	\paragraph{Oracle-improvable fraction.}
271	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
272	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
273	
274	\paragraph{Diversity-stratified selection gap.}
275	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
276	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
277	This rules out insufficient diversity as an explanation for the correlation-selection gap.
278	
279	\paragraph{TOST equivalence testing.}
280	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
281	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
282	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
283	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
284	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
285	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
286	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
287	
288	\begin{table}[t]
289	\centering
290	\small
291	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
292	\label{tab:tost}
293	\begin{tabular}{l cccc cccc}
294	\toprule
295	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
296	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
297	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
298	\midrule
299	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
300	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
301	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
302	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
303	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
304	\bottomrule
305	\end{tabular}
306	\end{table}
307	
308	\section{Multi-Seed Stability}\label{app:multiseed}
309	
310	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
311	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
312	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
313	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
319	\label{tab:multiseed}
320	\begin{tabular}{lccccc}
321	\toprule
322	& LP & FK & SJ & VC & EM \\
323	\midrule
324	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
325	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
326	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
327	\midrule
328	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
329	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
330	\midrule
331	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
332	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
333	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\section{Training Configuration}\label{app:training}
339	
340	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
346	\label{tab:training}
347	\begin{tabular}{ll}
348	\toprule
349	Parameter & Value \\
350	\midrule
351	LoRA rank / $\alpha$ & 32 / 64 \\
352	LoRA target & All linear modules \\
353	LoRA dropout & 0 \\
354	Optimizer & AdamW \\
355	Learning rate & 2e-4, cosine schedule \\
356	Warmup ratio & 0.1 \\
357	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
358	Epochs & 5 \\
359	Max sequence length & 2048 \\
360	Precision & bf16 \\
361	Gradient checkpointing & Enabled \\
362	Max gradient norm & 1.0 \\
363	Training seed & 42 \\
364	Framework & LLaMA Factory \\
365	\midrule
366	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
367	SciERC split & 1861 / 275 / 551 \\
368	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
369	& eval\_steps${=}$200, save\_limit${=}$5 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\paragraph{Prompt template.}
375	For NER, we use a structured prompt:
376	\begin{quote}
377	\small
378	\texttt{System:} You are an expert in Named Entity Recognition.\\
379	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
380	Text: \texttt{\{input\_text\}}\\
381	Entity types: \texttt{\{schema\_types\}}
382	\end{quote}
383	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
384	
385	\paragraph{Constrained decoding.}
386	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
387	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
388	
389	\section{Log-Probability Score Compression}\label{app:logprob_ties}
390	
391	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
392	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
393	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
394	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
395	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
396	
397	\begin{figure}[t]
398	\centering
399	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
400	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
401	\label{fig:lp_range_cdf}
402	\end{figure}
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
408	\label{tab:logprob_ties}
409	\begin{tabular}{lc}
410	\toprule
411	$\varepsilon$ threshold & Tied instances (\%) \\
412	\midrule
413	0.01 & 1.1\% \\
414	0.05 & 60.3\% \\
415	0.1  & ${\sim}$84\% \\
416	0.5  & ${\sim}$99\% \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	\paragraph{Non-tied subset.}
422	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
423	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
424	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
425	
426	\section{RE Conditional Selection}\label{app:re_conditional_selection}
427	
428	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
429	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
430	All five signals underperform greedy on both subsets.
431	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
432	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
433	
434	\begin{table}[t]
435	\centering
436	\small
437	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
438	\label{tab:re_cond_selection}
439	\begin{tabular}{lcc}
440	\toprule
441	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
442	\midrule
443	Oracle & 0.585 & 0.757 \\
444	\midrule
445	LP & 0.395 & 0.600 \\
446	SJ & 0.386 & 0.604 \\
447	EM & 0.372 & 0.583 \\
448	VC & 0.359 & 0.574 \\
449	\midrule
450	Greedy & 0.404 & 0.674 \\
451	\bottomrule
452	\end{tabular}
453	\end{table}
454	
455	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
456	
457	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
458	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
459	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
460	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
461	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
462	
463	\begin{table*}[t]
464	\centering
465	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
466	\label{tab:freeform_ablation}
467	
468	\vspace{2pt}
469	{\small\textsc{Panel A: Logprob Distribution}}
470	\vspace{2pt}
471	
472	\begin{tabular}{lccc}
473	\toprule
474	Metric & Constrained & Free-form & $\Delta$ \\
475	\midrule
476	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
477	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
478	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
479	\bottomrule
480	\end{tabular}
481	
482	\vspace{8pt}
483	
484	{\small\textsc{Panel B: Selection F1}}
485	\vspace{2pt}
486	
487	\begin{tabular}{llccc}
488	\toprule
489	Task & Method & Constrained & Free-form & $\Delta$ \\
490	\midrule
491	\multirow{3}{*}{NER}
492	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
493	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
494	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
495	\midrule
496	\multirow{3}{*}{RE}
497	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
498	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
499	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
500	\bottomrule
501	\end{tabular}
502	
503	\vspace{8pt}
504	
505	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
506	\vspace{2pt}
507	
508	\begin{tabular}{l ccc ccc}
509	\toprule
510	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
511	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
512	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
513	\midrule
514	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
515	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
516	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
517	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
518	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
519	\bottomrule
520	\end{tabular}
521	
522	\vspace{8pt}
523	
524	{\small\textsc{Panel D: Parse Rate (Free-form)}}
525	\vspace{2pt}
526	
527	\begin{tabular}{lc}
528	\toprule
529	Metric & Value \\
530	\midrule
531	Total samples          & 4408 \\
532	Parse rate             & 99.95\% \\
533	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
534	\bottomrule
535	\end{tabular}
536	
537	\end{table*}
538	
539	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
540	
541	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
542	
543	\paragraph{Pairwise overlap.}
544	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
545	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
546	
547	\paragraph{Instance complexity drives failure.}
548	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
549	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
550	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
551	
552	\begin{table}[t]
553	\centering
554	\small
555	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
556	\label{tab:stable_failures}
557	\begin{tabular}{lcccc}
558	\toprule
559	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
560	\midrule
561	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
562	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
563	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
564	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
565	\bottomrule
566	\end{tabular}
567	\end{table}
568	
569	\paragraph{Flip instances.}
570	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
571	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
572	
573	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
574	
575	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
576	
577	\begin{table}[t]
578	\centering
579	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
580	\label{tab:n-scaling}
581	\small
582	\begin{tabular}{l ccc ccc}
583	\toprule
584	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
585	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
586	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
587	\midrule
588	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
589	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
590	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
591	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
592	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
593	\midrule
594	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
595	\bottomrule
596	\end{tabular}
597	\end{table}
598	
599	\begin{table}[t]
600	\centering
601	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
602	\label{tab:ranking-stability}
603	\small
604	\begin{tabular}{ll cc l}
605	\toprule
606	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
607	\midrule
608	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
609	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
610	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
611	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
612	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
613	\bottomrule
614	\end{tabular}
615	\end{table}
616	
617	\begin{table}[t]
618	\centering
619	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
620	\label{tab:sigma-comparison}
621	\small
622	\begin{tabular}{l cc cc}
623	\toprule
624	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
625	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
626	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
627	\midrule
628	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
629	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
630	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
631	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
632	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
633	\midrule
634	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
635	\bottomrule
636	\end{tabular}
637	\end{table}
638	
639	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
640	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
641	
642	\section{Cross-Dataset OOD Analysis}\label{app:ood}
643	
644	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
645	
646	\begin{table}[t]
647	\centering
648	\small
649	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
650	\label{tab:ood}
651	\begin{tabular}{l ccc ccc}
652	\toprule
653	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
654	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
655	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
656	\midrule
657	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
658	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
659	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
660	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
661	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
662	\bottomrule
663	\end{tabular}
664	\end{table}
665	
666	\paragraph{Wider-to-narrower schema transfer.}
667	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
668	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
669	
670	\paragraph{Narrower-to-wider schema transfer (excluded).}
671	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
672	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
673	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
674	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
675	
676	\paragraph{Asymmetry interpretation.}
677	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
678	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
679	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "be4a445f-60a9-4139-8390-bd1456717b53",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as population standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), making it a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \\textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the core finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats---below the $\\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}).\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER), confirming that additional samples stabilize structural signals more than LP.\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}), not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is driven by schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n",
      "numLines": 679,
      "startLine": 1,
      "totalLines": 679
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01BJSzobP1ksU1U1vU1Mj3WF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "78bcad60-4553-45cf-bf6f-b2c42ac2c84e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 24 · 2026-05-15T13:27:30.346Z_

<details><summary>↩ Tool result · `toolu_01BJSzobP1ksU1U1vU1Mj3WF`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling \cite{zhang2025tts}, \citet{snell2025scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.
15	Our Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\S\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).
16	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
17	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \cite{willard2023guided}.
18	
19	\paragraph{Uncertainty estimation and calibration.}
20	Surveys cover confidence estimation \cite{geng2024confidence}, selective abstention \cite{wen2025know}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs; \citet{xiong2024llm} find LLMs tend toward overconfidence, and \citet{heo2025uncertainty} show calibration degrades with task complexity.
21	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; \citet{kossen2024semantic} distill this into probes; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.
22	Our structural signals instead measure agreement over output \textit{structure}.
23	Neural networks are often miscalibrated \cite{guo2017calibration, desai2020calibration}; deep ensembles \cite{lakshminarayanan2017ensembles} and MC-dropout \cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.
24	Prior NER uncertainty work spans Bayesian inference for sequence labeling \cite{xiao2019uncertainty}, active learning under uncertainty \cite{shelmanov2021active}, evidential deep learning \cite{zhang2023ener}, verification-augmented NER \cite{kim2024verifiner}, and uncertainty transmission across label sequences \cite{he2024uncertainty}---all within discriminative paradigms.
25	Conformal prediction \cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \cite{wang2024mathshepherd} learn per-sample scoring.
26	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \cite{freitag2022high} and other generation tasks \cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\S\ref{sec:discussion}).
27	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding.
28	Selective prediction \cite{geifman2017selective} and confidence-based IE filtering \cite{culotta2004confidence} establish the broader framework.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "138a9842-4925-4a2b-a2ae-ce9ddc865b8d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Self-consistency and test-time scaling.}\nSelf-consistency decoding \\cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.\nExtensions to free-form text use LLM-based comparison \\cite{chen2024usc}, atomic sub-claim decomposition \\cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \\cite{manakul2023selfcheckgpt}.\nFor test-time scaling \\cite{zhang2025tts}, \\citet{snell2025scaling} characterize compute scaling laws and \\citet{brown2024monkeys} show best-of-$N$ gains across tasks.\nRecent reward-free selectors include confidence-weighted voting \\cite{taubenfeld2025cisc}, KL-based self-certainty \\cite{kang2025selfcertainty}, adaptive sampling \\cite{kim2026reasc}, ranked aggregation \\cite{wang2025rankedvoting}, and latent-space consistency \\cite{oh2025latentsc}.\nConcurrently, \\citet{feng2025optimal} and \\citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \\citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.\nAll of the above target reasoning/QA with discrete answers or specific aggregation strategies.\nOur work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).\n\n\\paragraph{Consistency for structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.\nTheir work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whether findings generalize across a difficulty gradient.\nOur Soft Jaccard signal addresses (i) through type-aware bipartite matching with token-level span overlap; our selection analysis (\\S\\ref{sec:selection_gap}) directly addresses (ii); and our three-dataset evaluation spanning easy (CoNLL) to hard (SciERC) tasks addresses (iii).\nCoCoA \\cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.\nOur evaluation builds on generative IE work \\cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie} and constrained decoding \\cite{willard2023guided}.\n\n\\paragraph{Uncertainty estimation and calibration.}\nSurveys cover confidence estimation \\cite{geng2024confidence}, selective abstention \\cite{wen2025know}, uncertainty quantification \\cite{xia2025survey}, and calibration \\cite{hobelsberger2025systematic} for LLMs; \\citet{xiong2024llm} find LLMs tend toward overconfidence, and \\citet{heo2025uncertainty} show calibration degrades with task complexity.\nSemantic uncertainty \\cite{kuhn2023semantic} clusters generations by meaning; \\citet{kossen2024semantic} distill this into probes; P(True) \\cite{kadavath2022language} queries model confidence directly; \\citet{malinin2021uncertainty} distinguish data and model uncertainty in autoregressive models.\nOur structural signals instead measure agreement over output \\textit{structure}.\nNeural networks are often miscalibrated \\cite{guo2017calibration, desai2020calibration}; deep ensembles \\cite{lakshminarayanan2017ensembles} and MC-dropout \\cite{gal2016dropout} obtain uncertainty from model variation, while our approach requires no model modification.\nPrior NER uncertainty work spans Bayesian inference for sequence labeling \\cite{xiao2019uncertainty}, active learning under uncertainty \\cite{shelmanov2021active}, evidential deep learning \\cite{zhang2023ener}, verification-augmented NER \\cite{kim2024verifiner}, and uncertainty transmission across label sequences \\cite{he2024uncertainty}---all within discriminative paradigms.\nConformal prediction \\cite{fisch2021conformal, angelopoulos2021conformal} provides coverage guarantees; trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, venktesh2025trust} and reward models \\cite{wang2024mathshepherd} learn per-sample scoring.\nOur selection strategies instantiate MBR decoding \\cite{eikema2022sampling} with structural utility functions; despite MBR's success in translation \\cite{freitag2022high} and other generation tasks \\cite{jinnai2024mbr}, we find utility-quality misalignment at the per-sample level for structured IE (\\S\\ref{sec:discussion}).\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding.\nSelective prediction \\cite{geifman2017selective} and confidence-based IE filtering \\cite{culotta2004confidence} establish the broader framework.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01DQXgiL6wjk38EGAeEWoi4X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "ee57a9aa-ed63-4c25-9b71-173c8f1d7bdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 26 · 2026-05-15T13:27:30.915Z_

<details><summary>↩ Tool result · `toolu_01DQXgiL6wjk38EGAeEWoi4X`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.
21	The absence of any reasoning content further limits the representational impact.
22	
23	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data; all LP compression analyses use $T{=}1.0$ exclusively, and whether compression behavior changes at lower temperatures remains unknown.
24	The free-form ablation (within-instance std ratio $0.97{\times}$) provides stronger evidence that compression is not an artifact of the decoding strategy, but does not address temperature as a variable.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "cae13c6f-220a-4100-9813-cbbb78aa6b3d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.026$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.047$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, potentially shifting LP score calibration on SciERC; however, since LP selection fails across all datasets including CoNLL and WNUT-17 (which lack this confound), the thinking token inconsistency is unlikely to explain the correlation-selection gap.\nThe absence of any reasoning content further limits the representational impact.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data; all LP compression analyses use $T{=}1.0$ exclusively, and whether compression behavior changes at lower temperatures remains unknown.\nThe free-form ablation (within-instance std ratio $0.97{\\times}$) provides stronger evidence that compression is not an artifact of the decoding strategy, but does not address temperature as a variable.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01BuKqoYbwDs8gzPqyWVNdtV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "bb1a52c9-7761-4cae-bb9e-409ac3a600c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 28 · 2026-05-15T13:27:31.398Z_

<details><summary>↩ Tool result · `toolu_01BuKqoYbwDs8gzPqyWVNdtV`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "aa478286-0b1d-47b1-9597-7580a735f6d2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Confidence Signals Predict but Do Not Select in 8B-Scale Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01WHRAhHpHfBMAz1YSzPQFHU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "2a32e2ed-f3a7-472b-b29c-a4f7a176b74c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 30 · 2026-05-15T13:27:32.369Z_

<details><summary>↩ Tool result · `toolu_01WHRAhHpHfBMAz1YSzPQFHU`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	Under constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.
4	These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.
5	Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.
6	Neither succeeds: log-probability scores are compressed into effective ties for 60\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.
7	Where log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.
8	Signal rankings further depend on task complexity, with findings consistent across model families.
9	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "b9b98cd7-8800-428f-a3c4-769273cfacc0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nUnder constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.\nThese signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.\nFour of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.\nNeither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.\nWhere log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.\nSignal rankings further depend on task complexity, with findings consistent across model families.\n\\end{abstract}",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01Q85SB7VUbHtRCKEcKbrBqZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "d9c3ca9d-819b-4b63-aad3-349995e4feca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 32 · 2026-05-15T13:27:32.918Z_

<details><summary>↩ Tool result · `toolu_01Q85SB7VUbHtRCKEcKbrBqZ`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	The LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Toward mechanistic confirmation.}
24	Our diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.
25	A controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.
26	\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}
27	All findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
31	Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "eed94776-5dc1-4862-a474-66f9aba86daa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nUnder constrained decoding, LP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.\nThe LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.\nA controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.\n\\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}\nAll findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires either per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.",
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_019Ct8jKGGHGG7x4m5xpeqtC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "e058417e-1051-4955-a682-c27fd18f6afd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5qeHL2yPimXKWNkqwYgYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1935,
      "cache_read_input_tokens": 23341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1935
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

_source line 34 · 2026-05-15T13:27:33.185Z_

<details><summary>↩ Tool result · `toolu_019Ct8jKGGHGG7x4m5xpeqtC`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
8	A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.
9	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "cad3e5d0-29d1-4cda-a16b-ed73cfcf6478",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWithin the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nA direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.\nTrained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of all the tex files and the unified rho JSON. Let me analyze what needs to change.

Key findings from the unified rho JSON:

**exp_017_llama_conll_n16_r1024 (LLaMA CoNLL seed42 N=16):**
- Old FK ρ: 0.8095, New FK ρ: 0.4752
- Old SJ ρ: 0.1815, New SJ ρ: 0.4836
- New values: VC 0.4746, EM 0.4818, LP 0.3136


- **exp_017_llama_conll_n16_s456_r1024 (LLaMA CoNLL seed456 N=16):**
- Old FK ρ: 0.8085, New FK ρ: 0.469
- Old SJ ρ: 0.1895, New SJ ρ: 0.4734
- New values: VC 0.4722, EM 0.4752, LP 0.3099

I'm also seeing a significant shift in the Qwen SciERC seed456 experiment where FK ρ dropped from 0.3448 to 0.2.

For the NER task, the SJ ρ values are nearly identical at 0.4134 versus 0.4098, so that's essentially unchanged. The OOD experiment doesn't need any corrections.

Now I'm checking the main quality estimation table in the paper, which reports N=8 results as the primary findings with N=16 robustness checks in the appendix. I need to verify whether these updated N=16 values should propagate to the main table or if they're separate robustness results.

Looking at the structure, the N=16 experiments are distinct from the N=8 seed=42 baseline results shown in Table 1. The robustness table in the appendix will need updates for the LLaMA CoNLL N=16 results, but I should confirm which specific cells in the appendix table are affected by these changes. I'm noticing a major discrepancy—the old registry values (FK 0.8095, SJ 0.1815) are completely different from what the paper reports (FK 0.455, SJ 0.463), so either the registry was from an older pipeline or it was never actually used in the paper. Let me step back and reread what I'm actually supposed to be checking here. description more carefully:
   > ρ 一致性审计已完成，发现旧管道（含 gold-empty 实例）导致 ρ 值严重偏差。统一管道的修正值已在 analysis_unified_rho.json

   So the old pipeline had gold-empty instances causing ρ bias. The unified pipeline fixes this. The "old_registry" values in the JSON are what was in the experiment registry (which may or may not be what's in the paper).

   Looking at the paper values more carefully:

   **LLaMA CoNLL N=16 3-seed (tab:robustness):**
   Paper: SJ 0.463±0.007, FK 0.455±0.006, EM 0.460±0.008, VC 0.458±0.003, LP 0.310±0.005

   Now comparing against the unified JSON values for N=16 across the two seeds I can see: seed42 gives SJ 0.484 and FK 0.475, while seed456 gives SJ 0.473 and FK 0.469. If I average these two seeds along with a third one, the means would be around 0.478-0.479 for SJ and 0.472 for FK, which is notably higher than the paper's reported 0.463 and 0.455.

   This discrepancy suggests the paper values come from a different calculation or pipeline variant than what's in the unified JSON. Let me look at the robustness table structure to understand what's being measured. Looking at the second and third seed results, I can extrapolate what the third seed values might be, which suggests the paper's reported numbers are lower than what the unified pipeline produces. I'm wondering if there's a discrepancy in how the paper computed these metrics versus my current approach, or if the "old_registry" values in the JSON represent something different entirely.

Let me reconsider the structure here. The paper actually reports LLaMA CoNLL results across different experimental setups—one table with N=8 using seed42, and a robustness section with N=16 averaging across three seeds. The JSON data I'm looking at only covers the N=16 experiments, so the N=8 results might follow a different pattern altogether.

Now I'm checking where the N=16 Qwen SciERC values show up in the paper, since the JSON reveals some discrepancies between the old and new FK scores for that configuration. I'm checking whether the paper's reported values align with the individual seed results—the SJ N=16 value of 0.411 matches closely with seed456's 0.410, but FK N=16 shows a discrepancy where the paper reports 0.283 while seed456 gives 0.272, suggesting the paper averaged across multiple seeds. Let me systematically compare the full N=16 results from the appendix table to verify this pattern. So the key changes are LLaMA CoNLL showing FK dropping from 0.81 to 0.48 and SJ rising from 0.18 to 0.48, while SciERC seed456 has FK falling from 0.34 to 0.27. The paper reports LLaMA CoNLL with FK=0.455±0.006 and SJ=0.463±0.007, which doesn't match either the old or new registry values—this suggests the paper might be using data from a partially corrected pipeline, or there's another discrepancy I need to track down.

The unified pipeline gives me seed42 and seed456 values that are closer to the paper's reported means, but they still don't align exactly, so I need to examine what the robustness table is actually measuring and whether the paper's 3-seed averages are pulling from a different set of runs. 3-seed averages from unified or from old pipeline.

Actually, let me think differently. The paper's robustness table reports LLaMA CoNLL N=16 3-seed means. The JSON gives unified values for seed42 and seed456. If I assume there's also a seed123 (not in the JSON), then:

For SJ: (0.484 + x + 0.473) / 3 = 0.463 → x = 0.432 (plausible?)
For FK: (0.475 + x + 0.469) / 3 = 0.455 → x = 0.421 (seems low for the pattern)

Hmm, these x values seem inconsistent. The paper's 3-seed means are lower than both JSON seeds. This suggests the paper might have been computed from a different pipeline.

Wait, let me look at the JSON more carefully. The unified pipeline excludes gold-empty instances—n_valid is 2756 after removing 697 gold-empty cases from the total 3453. So the paper's reported dataset size and the actual experimental setup might differ depending on which pipeline was used. at the paper: experiments.tex L123: "We exclude 22 instances with empty gold annotations ($n{=}529$)" - this is for SciERC. For CoNLL, the paper also mentions n=2,756 in tab:cross_selection. So the paper also uses n=2756 for CoNLL, meaning it already excludes gold-empty. 

   So the paper already uses n=2756 for CoNLL. The unified JSON also uses n_valid=2756. If both exclude the same instances, the ρ values should match if they use the same computation.

   But the paper's 3-seed mean for SJ is 0.463 while the JSON seed42 gives SJ=0.484. They don't match. 

   Unless... the paper was originally computed with the OLD pipeline that included gold-empty instances (n=3453), which gave different ρ values. The old registry values came from that earlier pipeline with n=3453, but the paper doesn't report those either.

   I think I need to stop trying to reverse-engineer the exact pipeline and instead focus on what matters: identifying all ρ values in the paper that could shift due to the rho unification, then flagging them for review. The unified pipeline is now producing consistent results across seeds and models—LLaMA on CoNLL with N=16 gives FK around 0.47, SJ around 0.48, VC around 0.47, EM around 0.48, and LP around 0.31 across different seeds, and I should check what Qwen produces on SciERC.

Now I'm systematically going through the paper to locate every instance where LLaMA CoNLL ρ values or N=16 SciERC values appear, starting with the robustness table in the appendix which shows the 3-seed means and standard deviations for LLaMA CoNLL, and also lists Qwen SciERC N=16 results. I'm cross-referencing the experimental results across different settings and model configurations. The appendix contains the 3-seed averaged results for LLaMA on CoNLL, showing SJ consistently outperforms LP with deltas around +0.124 to +0.153, and I'm noting how the scaling behavior differs across these metrics. Now I need to figure out which values in the paper actually need correcting. The registry shows FK ρ should be 0.48 instead of 0.81 for LLaMA CoNLL, and 0.27 instead of 0.34 for SciERC seed456, but the paper doesn't report those old registry values anywhere—so the paper's reported numbers must have come from a different calculation, possibly mixing old and new pipeline results across the three seeds. Looking at the paper's results, SJ already outperforms FK in the LLaMA CoNLL dataset (0.463 vs 0.455), which matches the expected ranking reversal mentioned in the task description. The old registry values had this backwards with FK at 0.81 and SJ at 0.18, so the discrepancy was indeed between what the registry stored and what the paper actually reported.

However, comparing the paper's values directly to the unified JSON pipeline reveals a consistent pattern—all the paper's metrics are slightly lower across SJ, FK, EM, VC, and LP, suggesting the paper may have used a slightly different pipeline configuration than the unified one.

The old pipeline with gold-empty instances produced drastically different values (FK=0.81, SJ=0.18), so the paper's numbers can't be from that. This points to the unified pipeline having standardized not just the filtering approach but also the actual metric computation itself, which explains why the values diverge from what was published.

Now I need to systematically locate every ρ value in the paper for the affected experiments—specifically LLaMA and Qwen at N=16—and cross-check them against the unified JSON. I should also examine the N=8 LLaMA CoNLL results, which show FK=0.428 and SJ=0.431 in the paper but appear lower than the N=16 unified values of roughly 0.47 and 0.48, which seems backwards since smaller sample sizes should yield worse estimates.

The pattern suggests the paper's N=8 values came from a different pipeline than the old registry (which had the extreme FK=0.81, SJ=0.18 split), and the unified pipeline represents yet another corrected version. I need to compile all discrepancies between the paper and unified values to assess the scope of the issue.

I'm noticing there are duplicate files in the paper structure—both top-level and sections/ subdirectories contain abstract.tex, discussion.tex, and conclusion.tex. Since main.tex only includes from sections/, those are the active versions and the top-level files are likely outdated. Let me focus on the sections/ files and compile the full comparison.

Now I'm systematically checking all ρ values in the paper that involve LLaMA CoNLL or N=16 SciERC to see which ones are affected by the pipeline change. Looking through experiments.tex, I see Table 1 has CoNLL results for N=8 with LLaMA, and while those aren't in the JSON data I have, they could still be impacted if the pipeline change affected that configuration too. There are also various ρ values scattered throughout the text for different conditions and models that I need to track down. Now I'm looking at the performance metrics across different models and datasets — the structural signals consistently outperform the baseline approach, with SJ showing strong results around 0.46 on LLaMA CoNLL while LP stays much lower at 0.31, and similar patterns emerging in the Qwen SciERC experiments where temperature adjustments affect the robustness measurements. Looking at the consistency metrics across different model-dataset combinations, I'm seeing that SJ performs nearly identically between LLaMA and Qwen on CoNLL (both around 0.43), while VC and EM show much larger gaps favoring Qwen on SciERC and CoNLL respectively—VC differs by 0.17 and EM by 0.135—with LLaMA's VC on SciERC reaching 0.452 versus LP's 0.277. Looking at the scaling results across different methods, SJ consistently outperforms LP with the gap widening as N increases, and VC shows the most substantial improvement over the greedy baseline with statistical significance across multiple seeds. Now examining the detailed performance metrics for Qwen on SciERC across the three-seed runs, where SJ demonstrates stronger scaling gains compared to FK. Now I'm checking the unified values for LLaMA on CoNLL at N=16 across different seeds to identify where the paper's reported numbers diverge from the computed metrics.

The 3-seed averages in the paper are consistently lower than what I'm seeing in the unified JSON for individual seeds, which suggests they might be using a different sample size — possibly including gold-empty instances that would add noise to the evaluation. The paper does mention excluding 22 instances with empty gold annotations for SciERC, and the cross-selection analysis uses n=2,756 for CoNLL, so there's a discrepancy in how the samples were constructed.

Looking more carefully at the paper's methodology, it appears they're also using n=2,756 for CoNLL, same as the unified pipeline. But the actual metric values still don't align exactly, which points to differences in how FK/SJ were implemented or how per-instance F1 scores were computed between the two approaches.

Now I need to step back and address what the task is actually asking for: finding all ρ references across the paper's .tex files, generating a comprehensive impact list, and checking whether any changes to these values would affect the paper's core claims. Let me approach this systematically.

Looking at the experimental data, the main discrepancies are in LLaMA CoNLL with N=16 across different seeds and Qwen SciERC N=16, where the ρ values shift noticeably between the old registry and unified versions. The OOD results appear consistent. I need to identify every location in the paper where these specific results are cited, and also flag that the N=8 results might be affected by the same pipeline issue even though I don't have unified values for them yet. Let me start drafting the impact document now.

I should also verify the conditional metrics from the JSON since those appear in the appendix as well—checking whether the FK and SJ values for the conditional cases show similar discrepancies to the main results.

Now I'm comparing the two versions of the discussion section in the paper. The main.tex references sections/discussion.tex, which covers practical recommendations and methodological implications, while the top-level discussion.tex has some different content including a section on score compression under free-form decoding. I need to focus on the version actually included in the compiled paper. The top-level files appear to be newer versions with actual ablation results, while the sections/ directory contains earlier drafts, but since main.tex pulls from sections/, that's what's currently active. I need to track down all the ρ values throughout the paper and determine which ones are affected by the unified approach.

Looking at the specific tables: the quality estimation table uses N=8 seeds that aren't in the unified JSON and need verification, the robustness table has direct impacts on LLaMA CoNLL and potential impacts on Qwen SciERC depending on seed changes, and the n-scaling table's means could shift if the seed456 FK value dropped significantly.

Now I'm assessing how these pipeline changes affect the core claims. The correlation-selection gap claim relies primarily on SciERC N=8 results, which aren't affected by the unified changes, so that claim should hold. The difficulty-dependent signal complementarity claim about EM leading on easy tasks like CoNLL is what I need to verify against the actual pipeline impacts.

For the structural signals advantage, the unified pipeline actually shows a larger gap between SJ and LP on LLaMA CoNLL N=16 compared to the original paper, which strengthens rather than weakens that claim.

Now looking at the SJ-FK gap on CoNLL with LLaMA—the original N=8 data shows only a 0.003 difference, but in the unified N=16 results the gap widens to 0.009, suggesting the pattern might shift slightly when verified against the actual N=8 values. The uniform scaling claim about consistency signals gaining roughly 0.030 correlation points from N=8 to N=16 also hinges on confirming those N=8 values. And I'm noticing the rankings have flipped—the old registry showed FK substantially outperforming SJ, whereas now they're nearly equivalent.

The paper already demonstrates SJ ≥ FK, so that ranking appears sound. For the Qwen SciERC seed456 issue where FK dropped from 0.345 to 0.272, I can work backward from the reported N=16 mean of 0.283—if the other two seeds sum to 0.504, then replacing that seed value brings the new mean down to approximately 0.259, which would noticeably impact the overall FK N=16 average.

However, I'm realizing I don't actually know whether the paper computed its 3-seed mean directly or pulled it from the registry, so the seed456 value they used might differ from what I'm assuming. The most reliable approach is to flag all potentially affected metrics and have the authors confirm which values need updating. Now I'm going to compile the full impact document, making sure to be systematic about which results depend on these changed values.

I'm also noticing the JSON only provides N=16 unified results, but the same gold-empty filtering issue would impact N=8 experiments too since they use the same CoNLL dataset with 697 affected instances. The Table 1 N=8 results aren't in the JSON, so I'll need to note that those require separate verification even though they'd be affected by the same pipeline bug.

I should also check the AUROC values—the JSON has unified AUROC for LLaMA CoNLL N=16 and Qwen SciERC seed456, but the paper's Table 1 only reports N=8 AUROC values, and I don't see N=16 AUROC explicitly mentioned elsewhere in the text. So there's a mismatch in what's directly comparable.

Now I'll write up the final document. I'm setting up the SSH connection to save the document to the server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "79cd6340-a209-46bd-96d2-e12c21ece310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5PE9xXxJWFwbGuZreFJXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 49706,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49706
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

读取完成，正在分析所有 tex 文件中的 ρ 值引用位置并与统一管道修正值交叉比对。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "f99b43d8-612b-4d41-b0d7-ca6a9789dcb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5PE9xXxJWFwbGuZreFJXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 49706,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49706
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HsQmybYFbvw4gRnuYhPRQN`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
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
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "49af1326-d2f8-440c-8e90-3e691dc71b28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5PE9xXxJWFwbGuZreFJXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 49706,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 49706
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

_source line 38 · 2026-05-15T13:31:22.746Z_

<details><summary>↩ Tool result · `toolu_01HsQmybYFbvw4gRnuYhPRQN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "68e1eef1-3a05-4d2b-b8ac-ee3a57bd7611",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now let me compose the comprehensive impact list document. I've read all the tex files and the unified rho JSON. Let me write the impact list.

Let me organize my findings systematically:

**Unified JSON key values:**

LLaMA CoNLL N=16 seed42:
- FK: 0.8095 → 0.4752
- SJ: 0.1815 → 0.4836
- VC: 0.4746, EM: 0.4818, LP: 0.3136


- AUROC: FK 0.7467, SJ 0.7496, VC 0.7529, EM 0.7508, LP 0.7661
- Conditional: FK 0.4767, SJ 0.4856

LLaMA CoNLL N=16 seed456:
- FK: 0.8085 → 0.469
- SJ: 0.1895 → 0.4734
- VC: 0.4722, EM: 0.4752, LP: 0.3099
- AUROC and conditional metrics showing similar patterns across the different relation types
- Now moving into the Qwen SciERC results with NER and RE tasks, where I'm seeing different performance patterns — NER metrics ranging from 0.2415 to 0.4449, and RE scores in the 0.28-0.29 range. The OOD results are already validated. I'm starting to compile the paper values against the unified values to check for consistency across the LLaMA CoNLL benchmarks.

Looking at the robustness metrics with N=16 across multiple seeds, I'm noticing that the unified values consistently exceed the paper means — SJ, FK, EM, and VC all show improvements, while LP stays close to the reported 0.310. I'm working through the assumption that a third seed exists to complete the 3-seed average from the paper.

For SJ to average 0.463 with seeds at 0.484 and 0.473, the missing seed would need to be 0.432, but that creates a standard deviation of 0.022, which is far larger than the paper's reported 0.007. I'm now testing whether a mean of 0.463 is even mathematically consistent with σ=0.007 across three seeds, which requires solving for what the actual seed values would need to be.

Working through the variance equation with σ=0.007 and assuming a mean around 0.478, I get possible seed values of 0.469 or 0.487. But neither combination with 0.484 and 0.473 produces the paper's reported mean of 0.463—the resulting means would be 0.475 or 0.481 instead. This confirms the paper's reported values couldn't have come from the unified pipeline.

Now I'm realizing the old registry values (FK=0.81, SJ=0.18) don't match the paper's values (FK=0.455, SJ=0.463) either, which suggests these three sets of numbers—the registry, the paper, and the unified pipeline—all came from different computational approaches. The registry might have computed metrics at the per-sample level with the gold-empty bug inflating FK, while the paper used a different implementation at the instance level, and the unified pipeline is yet another variant entirely.

Since the task specifies that the unified pipeline values are the ground truth, I need to update the paper to match them. However, I'm missing data—only 2 of 3 seeds for LLaMA CoNLL N=16 and 1 of 3 seeds for Qwen SciERC N=16—so I can't compute exact 3-seed means. The N=8 values aren't even in the JSON, so I'll need to flag that the pipeline change would affect them too but I can't provide corrected values. Let me start drafting the document with clear notes about what I can and can't determine.

The unified JSON only has N=16 corrections, but the pipeline change affects all CoNLL experiments since they all have those 697 gold-empty instances. Now I'm checking how the corrected values shift the signal rankings—comparing the paper's original ordering against what the unified seeds show, which reveals some rankings flip depending on which seed is used.

Looking at the impact on the paper's core claim about consistency signals gaining roughly +0.030, the unified N=16 values actually show larger gains (around +0.041 to +0.053), which would contradict the paper's reported effect size if the N=8 values remain unchanged.

For the Qwen SciERC case, I'm working through what happens when seed456's FK value shifts from 0.345 to 0.272 at N=16. The other two seeds must have contributed 0.504 combined, giving a new mean of 0.259—a drop of 0.024 from the paper's reported 0.283. But the paper claims FK improved by +0.030 going from N=8 to N=16, so this new calculation would suggest the opposite direction of change.

Let me check the actual paper values more carefully. The robustness table shows FK N=16 as 0.283, but the n-scaling table lists it as 0.2833 with a delta of +0.0297 from N=8. Yet the text explicitly states FK shows degradation on SciERC with values between -0.007 and -0.019, which directly contradicts the positive scaling delta reported in the table. Looking at the actual numbers in the n-scaling table, both FK metrics on SciERC show gains—NER improves by 0.030 and RE by 0.006—so the degradation mentioned in the text likely refers to LLaMA results specifically rather than the Qwen baseline. I'm getting into the weeds here when I should focus on drafting the impact section, so let me move forward with that and circle back to verify the quality estimation table values for LLaMA CoNLL if needed. see what the implications are.

Looking at the performance metrics across different configurations: for CoNLL with LLaMA at N=8, the values are quite close—SJ and EM both hit .431, with FK at .428. This tight clustering is worth noting since the limitations mention a gap of only 0.003, but when I look at the unified pipeline results at N=16, that gap widens to 0.009. The pattern suggests the limitations section might need adjustment.

Now I'm working through the core claims to see what holds up. The ρ up to 0.38 figure comes from SciERC N=8 with VC at 0.379, which isn't affected by the JSON experiments. The correlation-selection gap is also primarily demonstrated on SciERC N=8 and remains valid. For the difficulty-dependent complementarity claim, EM should lead on easier tasks like CoNLL, but the current data shows EM and SJ tied at .431 for LLaMA CoNLL—though the stronger evidence comes from Qwen where EM clearly leads at .451. The signal stability claim about SJ achieving 0.436 on Qwen versus 0.431 on LLaMA needs checking if these values shift.

The structural advantage over LP persists and actually strengthens in the unified pipeline. But the uniform scaling claim on LLaMA CoNLL depends entirely on those N=8 and N=16 values, so I need full verification there. The SJ-FK gap claim of 0.003 on CoNLL with LLaMA will likely increase if N=8 changes, which could weaken the argument about structural advantages not generalizing to simple-schema datasets. The 3-seed standard deviation values will shift as well.

Now I'm checking the N=16 CoNLL selection result where VC shows a +0.28pp improvement — though this is about selection F1 rather than correlation, so it depends on which samples get selected rather than the correlation values themselves. If the filtering changes the instance set, the selection outcomes could shift too. I'm ready to write up all these findings in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "740590cf-00e1-4c88-8f52-52935a70af95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh7hwBo69WTZNRy6rjQKc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13370,
      "cache_read_input_tokens": 61407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13370
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

_source line 40_

Now I'll compose the impact list and save it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "52ccf9df-2e3a-4f81-ad5a-4ef914aa3ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh7hwBo69WTZNRy6rjQKc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13370,
      "cache_read_input_tokens": 61407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13370
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

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_01BEVreoaA4ehSZe8y2GZimS`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_paper_impact_list.md",
  "content": "# ρ 值论文影响清单\n\n**生成日期**: 2026-05-15\n**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)\n**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1\n\n---\n\n## 统一管道修正值摘要\n\n| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |\n|------|--------|---------------|--------|---|------|\n| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |\n| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |\n| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |\n| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |\n| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |\n\n**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。\n\n---\n\n## 需更新的 ρ 值位置\n\n### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section\n\n**文件**: `sections/appendix.tex`, L52-57\n\n**当前值**:\n```\nSJ:  0.463 ± 0.007\nFK:  0.455 ± 0.006\nEM:  0.460 ± 0.008\nVC:  0.458 ± 0.003\nLP:  0.310 ± 0.005\n```\n\n**统一管道 (2/3 seeds available)**:\n| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |\n|--------|--------|---------|----------------|------|\n| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |\n| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |\n| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |\n| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |\n| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |\n\n**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。**需用统一管道重算 3 seed 并更新此表。** seed123 的统一值不在 JSON 中，需补算。\n\n**σ 值也需更新**: 当前 σ(SJ)=0.007，若统一 seed42=0.484、seed456=0.473，新 σ 取决于 seed123。\n\n### 2. Table tab:robustness — Qwen SciERC N=16 section\n\n**文件**: `sections/appendix.tex`, L47-50\n\n**当前值**:\n```\nSJ N=16: 0.411 (3-seed mean, footnote †)\nFK N=16: 0.283\n```\n\n**统一管道 seed456**:\n- SJ: 0.4098 (vs 旧 registry 0.4134, Δ=-0.004, 几乎不变)\n- FK: 0.2723 (vs 旧 registry 0.3448, **Δ=-0.073**)\n\n**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259（估算: 若 seed456 从 0.345→0.272，其他 2 seed 不变）。需用统一管道重算全部 3 seed。SJ 基本不受影响。\n\n### 3. Table tab:n-scaling — Qwen SciERC 3-seed\n\n**文件**: `sections/appendix.tex`, L582-596\n\n**当前值** (受影响行):\n```\nFK: N=8: 0.2536, N=16: 0.2833, Δ: +0.0297\n```\n\n**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，则:\n- FK Δ(N=8→N=16) 从 +0.030 降至 **~+0.005**\n- FK N-scaling 从\"弱正\"变为\"近乎零\"\n\n其他行 (SJ, VC, EM, LP) 受影响较小。需重算。\n\n### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8\n\n**文件**: `sections/experiments.tex`, L38-42\n\n**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307\n\n**状态**: ⚠️ **统一 JSON 不含 N=8 数据**。但同一管道问题（gold-empty filtering + FK/SJ 计算）同样影响 N=8 实验。**需用统一管道重算 N=8 LLaMA CoNLL 并验证**。\n\n> 若 N=8 也出现 FK↓SJ↑ 的趋势，Table 1 数值和排名可能变化。\n\n### 5. Table tab:sigma-comparison\n\n**文件**: `sections/appendix.tex`, L619-637\n\nLLaMA CoNLL 不在此表（此表是 Qwen SciERC），但 Qwen SciERC N=16 σ 值受 seed456 FK 变化影响。需重算。\n\n### 6. Table tab:ranking-stability (Kendall's W)\n\n**文件**: `sections/appendix.tex`, L599-615\n\nQwen NER N=16 行: 当前 W=0.956, consensus \"SJ ≈ VC > EM > FK > LP\"。若 FK N=16 下降，排名可能变为 \"SJ ≈ VC > EM > LP > FK\"（FK 和 LP 可能交换）。需验证。\n\n---\n\n## 正文引用\n\n### experiments.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L71 | \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005, within 3-seed σ≈0.007)\" | N=8 LLaMA CoNLL SJ=0.431 需验证；σ≈0.007 可能变化 | ⚠️ 需 N=8 数据 |\n| L140 | \"structural signals maintaining their advantage over LP across all NER settings (Δρ=+0.135 to +0.175)\" | 此 Δρ 范围源自 N=16 各配置。统一管道下 LLaMA CoNLL SJ-LP Δ≈+0.170 (seed42)，可能使范围上移 | 中 |\n\n### appendix.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L53-54 | \"SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153\" | 统一管道 SJ 更高，Δ 增大至 ~+0.170 | 高 |\n| L77 | \"LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain Δρ≈+0.030 (range: +0.027 to +0.032) while LP gains only +0.003\" | 依赖 N=8 和 N=16 差值。若 N=16 升高而 N=8 不变，Δρ 增大；若 N=8 也升高，可能抵消 | ⚠️ 需 N=8 数据 |\n| L78-79 | \"FK N-scaling is inconsistent: degradation on SciERC (-0.007 to -0.019) but improvement on CoNLL with LLaMA (+0.027)\" | SciERC FK N-scaling Δ 可能从+0.030 变为+0.005，且 CoNLL 的+0.027 可能变化 | 高 |\n| L84 | \"LLaMA SciERC NER (SJ ρ=0.325±0.021, FK ρ=0.256±0.024)\" | LLaMA SciERC N=8 — 不在 JSON 中，但可能受同一管道影响 | ⚠️ 需验证 |\n| L85-86 | \"SJ achieves ρ=0.431 (LLaMA) vs. 0.436 (Qwen), Δ=0.005\" | N=8 LLaMA CoNLL 值 | ⚠️ 需 N=8 数据 |\n| L86 | \"LLaMA CoNLL 3-seed (SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153)\" | 同 L53-54 | 高 |\n| L138 | \"CoNLL LLaMA 3-seed (ρ=0.462)\" [conditional EM] | 条件过滤值，受管道变化影响 | 高 |\n| L191-193 | \"SJ already achieves ρ=0.431 on LLaMA CoNLL (vs. LP ρ=0.307, Δ=+0.124), and the gap widens at N=16 (Δ=+0.153)\" | N=8 + N=16 混合引用 | 高 |\n| L199 | \"VC achieves the largest gain over greedy (+0.28 pp, p=0.003–0.027 across 3 seeds)\" | 选择 F1 非 ρ，但若实例集变化，选择结果可能不同 | 中 |\n\n### sections/discussion.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L6 | \"At higher sample sizes (N=16), SJ converges to comparable NER performance with VC (Δ=0.002) with lower cross-seed variance (σ=0.010 vs. 0.026)\" | SJ/VC N=16 值变化 → Δ 和 σ 需重算 | 中 |\n\n### sections/limitations.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L15 | \"On CoNLL with LLaMA, the SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\" | N=8 值。统一管道 N=16 gap≈0.009 (seed42)。若 N=8 也扩大，此 claim 需修改 | ⚠️ 需 N=8 数据 |\n\n---\n\n## 排名变化\n\n### LLaMA CoNLL N=16 (最重要)\n\n**旧 Registry 排名**: FK (0.81) >> SJ (0.18) — FK 绝对主导\n**论文当前排名**: SJ (0.463) > EM (0.460) > VC (0.458) > FK (0.455) > LP (0.310) — SJ 略高于 FK\n**统一管道排名 (seed42)**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314) — SJ > FK，但 FK 上升\n**统一管道排名 (seed456)**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310) — 四信号趋同\n\n**关键变化**:\n1. 旧 registry → 统一: **FK/SJ 排名完全反转**（FK 从第一降至中间，SJ 从最后升至顶部）\n2. 论文 → 统一: 排名方向一致（SJ ≥ FK），但**绝对值系统性偏低 ~0.015**\n3. 统一管道下四个一致性信号更加趋同（range 0.009 vs 论文的 0.008），LP 差距更大\n\n### Qwen SciERC N=16 NER\n\n**旧 Registry**: FK=0.345, SJ=0.413\n**统一管道 seed456**: FK=0.272, SJ=0.410\n\n**排名影响**: FK 从 SJ 的 83% 降至 66%。在 3-seed 排名中，FK 可能从 #4 降至 #5（与 LP 交换）。\n\n---\n\n## 核心 Claim 影响评估\n\n### 1. Correlation-Selection Gap (核心贡献)\n\n**Claim**: \"ρ up to 0.38, AUROC up to 0.75, yet none significantly improves sample selection\"\n\n**影响**: ✅ **不受影响**。此 claim 基于 SciERC N=8 seed=42 结果（VC ρ=0.379），不在本次修正范围内。选择实验也在 SciERC N=8 上进行。\n\n### 2. Difficulty-Dependent Signal Complementarity\n\n**Claim**: \"EM leads on easy tasks (CoNLL), SJ on hard tasks (SciERC)\"\n\n**影响**: ⚠️ **需验证 N=8 CoNLL LLaMA**。\n- CoNLL Qwen N=8: EM=0.451 明确领先 → 不受影响\n- CoNLL LLaMA N=8: EM=0.431 = SJ=0.431（并列） → 若统一管道下排名变化，claim 需调整措辞\n- SciERC N=8: VC/SJ 领先 → 不受影响\n\n### 3. Signal Stability Across Model Families\n\n**Claim**: \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005)\"\n\n**影响**: ⚠️ **需 N=8 统一值**。若 LLaMA CoNLL N=8 SJ 值变化，Δ 可能不再是 0.005。但 claim 的方向（跨模型稳定）可能仍成立。\n\n### 4. Structural Advantage Over LP\n\n**Claim**: \"Δρ=+0.135 to +0.175\"\n\n**影响**: ✅ **加强**。统一管道下 SJ-LP 差距更大（N=16 seed42: 0.484-0.314=+0.170），structural advantage 更明显。\n\n### 5. \"Uniform N-Scaling\" on LLaMA CoNLL\n\n**Claim**: \"all four consistency signals gain Δρ≈+0.030\"\n\n**影响**: ⚠️ **需全面重算**。N=16 值升高但 N=8 值未知。若 N=8 也升高，Δ 可能不变；若只有 N=16 升高，Δ 增大。\n\n### 6. FK N-Scaling on SciERC\n\n**Claim**: FK N=16 Δ=+0.030 (tab:n-scaling)\n\n**影响**: ❌ **可能失效**。seed456 FK 从 0.345 降至 0.272，3-seed mean N=16 FK 可能降至 ~0.259，使 Δ 从 +0.030 降至 +0.005。相关文本 \"FK N-scaling is inconsistent\" 的具体数值需更新。\n\n### 7. SJ-FK Gap on CoNLL (Limitations)\n\n**Claim**: \"SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\"\n\n**影响**: ⚠️ **需 N=8 验证**。统一 N=16 gap=0.009 (seed42)。若 N=8 gap 也扩大，此 limitation 的具体数值需更新，但方向（gap 较小）可能仍成立。\n\n### 8. 3-Seed σ Values\n\n**Claim**: \"σ≤0.026\" (multiseed stability)\n\n**影响**: ⚠️ σ 值会随 ρ 值变化。需用统一管道重算所有 3-seed 统计量。\n\n---\n\n## 未覆盖的缺口\n\n以下实验/配置受同一管道问题影响，但统一 JSON 未提供修正值:\n\n1. **LLaMA CoNLL N=8** (Table 1, 多处正文引用) — 697 gold-empty 实例同样存在\n2. **LLaMA CoNLL N=16 seed123** — 3-seed mean 需要全部 3 个 seed\n3. **Qwen SciERC N=16 seed42 和 seed123** — 3-seed mean 需要全部 3 个 seed\n4. **Qwen CoNLL N=8 / N=16** — 同一 CoNLL 数据集，可能受影响\n5. **WNUT-17** — 有 gold-empty 实例（JSON 中 WNUT 未出现，需确认）\n6. **LLaMA SciERC N=8** (appendix L84) — 可能受影响\n7. **条件过滤值** (conditional ρ) — JSON 仅提供部分 conditional 值\n8. **AUROC 值** — JSON 提供了统一 AUROC，但论文中的 AUROC 主要在 Table 1 (N=8)，无法直接比对\n9. **Selection F1 值** — 管道变化可能影响实例集，间接影响选择实验结果\n\n---\n\n## 建议行动\n\n### 立即执行 (高优先级)\n1. **重算全部 3 seed 的统一 ρ** for LLaMA CoNLL N=16 → 更新 tab:robustness 和所有引用\n2. **重算全部 3 seed 的统一 ρ** for Qwen SciERC N=16 → 更新 tab:robustness 和 tab:n-scaling\n3. **重算 LLaMA CoNLL N=8 统一 ρ** → 更新 Table 1 和所有 N=8 引用\n\n### 随后更新 (中优先级)\n4. 更新所有衍生统计量 (Δρ, σ, Kendall's W, conditional ρ)\n5. 重跑 N-scaling 分析 (tab:n-scaling)，特别关注 FK\n6. 验证 AUROC 值是否也受影响\n7. 检查 selection F1 是否需要重算（实例集 n 是否变化）\n\n### 最后检查 (低优先级)\n8. 审查所有正文 claim 是否仍与更新后数值一致\n9. 更新 Figure fig_signal_heatmap（若 heatmap 包含 N=16 数据）\n10. 确认 WNUT-17 不受影响（或补算）\n\n---\n\n## 核心结论\n\n**论文的核心贡献（correlation-selection gap）不受影响**，因为它基于 SciERC N=8 实验，不在本次修正范围内。\n\n主要影响集中在:\n- **Appendix robustness 分析** (LLaMA CoNLL N=16 和 Qwen SciERC N=16)\n- **N-scaling 分析** (FK scaling 可能失效)\n- **跨模型稳定性的具体数值** (N=8 LLaMA CoNLL 需验证)\n\n论文的 claim 方向大多不变，但**具体数值需全面更新**。唯一可能受实质影响的是 FK N-scaling 的 claim 和 SJ-FK gap 的 limitations 描述。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "bd3e5ad3-0d8e-40dd-96a6-89f312e222f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh7hwBo69WTZNRy6rjQKc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13370,
      "cache_read_input_tokens": 61407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13370
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

_source line 42 · 2026-05-15T13:34:11.738Z_

<details><summary>↩ Tool result · `toolu_01BEVreoaA4ehSZe8y2GZimS`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_paper_impact_list.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "806dc090-80d2-4214-a677-d27036b821c7",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_paper_impact_list.md",
    "content": "# ρ 值论文影响清单\n\n**生成日期**: 2026-05-15\n**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)\n**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1\n\n---\n\n## 统一管道修正值摘要\n\n| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |\n|------|--------|---------------|--------|---|------|\n| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |\n| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |\n| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |\n| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |\n| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |\n\n**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。\n\n---\n\n## 需更新的 ρ 值位置\n\n### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section\n\n**文件**: `sections/appendix.tex`, L52-57\n\n**当前值**:\n```\nSJ:  0.463 ± 0.007\nFK:  0.455 ± 0.006\nEM:  0.460 ± 0.008\nVC:  0.458 ± 0.003\nLP:  0.310 ± 0.005\n```\n\n**统一管道 (2/3 seeds available)**:\n| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |\n|--------|--------|---------|----------------|------|\n| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |\n| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |\n| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |\n| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |\n| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |\n\n**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。**需用统一管道重算 3 seed 并更新此表。** seed123 的统一值不在 JSON 中，需补算。\n\n**σ 值也需更新**: 当前 σ(SJ)=0.007，若统一 seed42=0.484、seed456=0.473，新 σ 取决于 seed123。\n\n### 2. Table tab:robustness — Qwen SciERC N=16 section\n\n**文件**: `sections/appendix.tex`, L47-50\n\n**当前值**:\n```\nSJ N=16: 0.411 (3-seed mean, footnote †)\nFK N=16: 0.283\n```\n\n**统一管道 seed456**:\n- SJ: 0.4098 (vs 旧 registry 0.4134, Δ=-0.004, 几乎不变)\n- FK: 0.2723 (vs 旧 registry 0.3448, **Δ=-0.073**)\n\n**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259（估算: 若 seed456 从 0.345→0.272，其他 2 seed 不变）。需用统一管道重算全部 3 seed。SJ 基本不受影响。\n\n### 3. Table tab:n-scaling — Qwen SciERC 3-seed\n\n**文件**: `sections/appendix.tex`, L582-596\n\n**当前值** (受影响行):\n```\nFK: N=8: 0.2536, N=16: 0.2833, Δ: +0.0297\n```\n\n**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，则:\n- FK Δ(N=8→N=16) 从 +0.030 降至 **~+0.005**\n- FK N-scaling 从\"弱正\"变为\"近乎零\"\n\n其他行 (SJ, VC, EM, LP) 受影响较小。需重算。\n\n### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8\n\n**文件**: `sections/experiments.tex`, L38-42\n\n**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307\n\n**状态**: ⚠️ **统一 JSON 不含 N=8 数据**。但同一管道问题（gold-empty filtering + FK/SJ 计算）同样影响 N=8 实验。**需用统一管道重算 N=8 LLaMA CoNLL 并验证**。\n\n> 若 N=8 也出现 FK↓SJ↑ 的趋势，Table 1 数值和排名可能变化。\n\n### 5. Table tab:sigma-comparison\n\n**文件**: `sections/appendix.tex`, L619-637\n\nLLaMA CoNLL 不在此表（此表是 Qwen SciERC），但 Qwen SciERC N=16 σ 值受 seed456 FK 变化影响。需重算。\n\n### 6. Table tab:ranking-stability (Kendall's W)\n\n**文件**: `sections/appendix.tex`, L599-615\n\nQwen NER N=16 行: 当前 W=0.956, consensus \"SJ ≈ VC > EM > FK > LP\"。若 FK N=16 下降，排名可能变为 \"SJ ≈ VC > EM > LP > FK\"（FK 和 LP 可能交换）。需验证。\n\n---\n\n## 正文引用\n\n### experiments.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L71 | \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005, within 3-seed σ≈0.007)\" | N=8 LLaMA CoNLL SJ=0.431 需验证；σ≈0.007 可能变化 | ⚠️ 需 N=8 数据 |\n| L140 | \"structural signals maintaining their advantage over LP across all NER settings (Δρ=+0.135 to +0.175)\" | 此 Δρ 范围源自 N=16 各配置。统一管道下 LLaMA CoNLL SJ-LP Δ≈+0.170 (seed42)，可能使范围上移 | 中 |\n\n### appendix.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L53-54 | \"SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153\" | 统一管道 SJ 更高，Δ 增大至 ~+0.170 | 高 |\n| L77 | \"LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain Δρ≈+0.030 (range: +0.027 to +0.032) while LP gains only +0.003\" | 依赖 N=8 和 N=16 差值。若 N=16 升高而 N=8 不变，Δρ 增大；若 N=8 也升高，可能抵消 | ⚠️ 需 N=8 数据 |\n| L78-79 | \"FK N-scaling is inconsistent: degradation on SciERC (-0.007 to -0.019) but improvement on CoNLL with LLaMA (+0.027)\" | SciERC FK N-scaling Δ 可能从+0.030 变为+0.005，且 CoNLL 的+0.027 可能变化 | 高 |\n| L84 | \"LLaMA SciERC NER (SJ ρ=0.325±0.021, FK ρ=0.256±0.024)\" | LLaMA SciERC N=8 — 不在 JSON 中，但可能受同一管道影响 | ⚠️ 需验证 |\n| L85-86 | \"SJ achieves ρ=0.431 (LLaMA) vs. 0.436 (Qwen), Δ=0.005\" | N=8 LLaMA CoNLL 值 | ⚠️ 需 N=8 数据 |\n| L86 | \"LLaMA CoNLL 3-seed (SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153)\" | 同 L53-54 | 高 |\n| L138 | \"CoNLL LLaMA 3-seed (ρ=0.462)\" [conditional EM] | 条件过滤值，受管道变化影响 | 高 |\n| L191-193 | \"SJ already achieves ρ=0.431 on LLaMA CoNLL (vs. LP ρ=0.307, Δ=+0.124), and the gap widens at N=16 (Δ=+0.153)\" | N=8 + N=16 混合引用 | 高 |\n| L199 | \"VC achieves the largest gain over greedy (+0.28 pp, p=0.003–0.027 across 3 seeds)\" | 选择 F1 非 ρ，但若实例集变化，选择结果可能不同 | 中 |\n\n### sections/discussion.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L6 | \"At higher sample sizes (N=16), SJ converges to comparable NER performance with VC (Δ=0.002) with lower cross-seed variance (σ=0.010 vs. 0.026)\" | SJ/VC N=16 值变化 → Δ 和 σ 需重算 | 中 |\n\n### sections/limitations.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L15 | \"On CoNLL with LLaMA, the SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\" | N=8 值。统一管道 N=16 gap≈0.009 (seed42)。若 N=8 也扩大，此 claim 需修改 | ⚠️ 需 N=8 数据 |\n\n---\n\n## 排名变化\n\n### LLaMA CoNLL N=16 (最重要)\n\n**旧 Registry 排名**: FK (0.81) >> SJ (0.18) — FK 绝对主导\n**论文当前排名**: SJ (0.463) > EM (0.460) > VC (0.458) > FK (0.455) > LP (0.310) — SJ 略高于 FK\n**统一管道排名 (seed42)**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314) — SJ > FK，但 FK 上升\n**统一管道排名 (seed456)**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310) — 四信号趋同\n\n**关键变化**:\n1. 旧 registry → 统一: **FK/SJ 排名完全反转**（FK 从第一降至中间，SJ 从最后升至顶部）\n2. 论文 → 统一: 排名方向一致（SJ ≥ FK），但**绝对值系统性偏低 ~0.015**\n3. 统一管道下四个一致性信号更加趋同（range 0.009 vs 论文的 0.008），LP 差距更大\n\n### Qwen SciERC N=16 NER\n\n**旧 Registry**: FK=0.345, SJ=0.413\n**统一管道 seed456**: FK=0.272, SJ=0.410\n\n**排名影响**: FK 从 SJ 的 83% 降至 66%。在 3-seed 排名中，FK 可能从 #4 降至 #5（与 LP 交换）。\n\n---\n\n## 核心 Claim 影响评估\n\n### 1. Correlation-Selection Gap (核心贡献)\n\n**Claim**: \"ρ up to 0.38, AUROC up to 0.75, yet none significantly improves sample selection\"\n\n**影响**: ✅ **不受影响**。此 claim 基于 SciERC N=8 seed=42 结果（VC ρ=0.379），不在本次修正范围内。选择实验也在 SciERC N=8 上进行。\n\n### 2. Difficulty-Dependent Signal Complementarity\n\n**Claim**: \"EM leads on easy tasks (CoNLL), SJ on hard tasks (SciERC)\"\n\n**影响**: ⚠️ **需验证 N=8 CoNLL LLaMA**。\n- CoNLL Qwen N=8: EM=0.451 明确领先 → 不受影响\n- CoNLL LLaMA N=8: EM=0.431 = SJ=0.431（并列） → 若统一管道下排名变化，claim 需调整措辞\n- SciERC N=8: VC/SJ 领先 → 不受影响\n\n### 3. Signal Stability Across Model Families\n\n**Claim**: \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005)\"\n\n**影响**: ⚠️ **需 N=8 统一值**。若 LLaMA CoNLL N=8 SJ 值变化，Δ 可能不再是 0.005。但 claim 的方向（跨模型稳定）可能仍成立。\n\n### 4. Structural Advantage Over LP\n\n**Claim**: \"Δρ=+0.135 to +0.175\"\n\n**影响**: ✅ **加强**。统一管道下 SJ-LP 差距更大（N=16 seed42: 0.484-0.314=+0.170），structural advantage 更明显。\n\n### 5. \"Uniform N-Scaling\" on LLaMA CoNLL\n\n**Claim**: \"all four consistency signals gain Δρ≈+0.030\"\n\n**影响**: ⚠️ **需全面重算**。N=16 值升高但 N=8 值未知。若 N=8 也升高，Δ 可能不变；若只有 N=16 升高，Δ 增大。\n\n### 6. FK N-Scaling on SciERC\n\n**Claim**: FK N=16 Δ=+0.030 (tab:n-scaling)\n\n**影响**: ❌ **可能失效**。seed456 FK 从 0.345 降至 0.272，3-seed mean N=16 FK 可能降至 ~0.259，使 Δ 从 +0.030 降至 +0.005。相关文本 \"FK N-scaling is inconsistent\" 的具体数值需更新。\n\n### 7. SJ-FK Gap on CoNLL (Limitations)\n\n**Claim**: \"SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\"\n\n**影响**: ⚠️ **需 N=8 验证**。统一 N=16 gap=0.009 (seed42)。若 N=8 gap 也扩大，此 limitation 的具体数值需更新，但方向（gap 较小）可能仍成立。\n\n### 8. 3-Seed σ Values\n\n**Claim**: \"σ≤0.026\" (multiseed stability)\n\n**影响**: ⚠️ σ 值会随 ρ 值变化。需用统一管道重算所有 3-seed 统计量。\n\n---\n\n## 未覆盖的缺口\n\n以下实验/配置受同一管道问题影响，但统一 JSON 未提供修正值:\n\n1. **LLaMA CoNLL N=8** (Table 1, 多处正文引用) — 697 gold-empty 实例同样存在\n2. **LLaMA CoNLL N=16 seed123** — 3-seed mean 需要全部 3 个 seed\n3. **Qwen SciERC N=16 seed42 和 seed123** — 3-seed mean 需要全部 3 个 seed\n4. **Qwen CoNLL N=8 / N=16** — 同一 CoNLL 数据集，可能受影响\n5. **WNUT-17** — 有 gold-empty 实例（JSON 中 WNUT 未出现，需确认）\n6. **LLaMA SciERC N=8** (appendix L84) — 可能受影响\n7. **条件过滤值** (conditional ρ) — JSON 仅提供部分 conditional 值\n8. **AUROC 值** — JSON 提供了统一 AUROC，但论文中的 AUROC 主要在 Table 1 (N=8)，无法直接比对\n9. **Selection F1 值** — 管道变化可能影响实例集，间接影响选择实验结果\n\n---\n\n## 建议行动\n\n### 立即执行 (高优先级)\n1. **重算全部 3 seed 的统一 ρ** for LLaMA CoNLL N=16 → 更新 tab:robustness 和所有引用\n2. **重算全部 3 seed 的统一 ρ** for Qwen SciERC N=16 → 更新 tab:robustness 和 tab:n-scaling\n3. **重算 LLaMA CoNLL N=8 统一 ρ** → 更新 Table 1 和所有 N=8 引用\n\n### 随后更新 (中优先级)\n4. 更新所有衍生统计量 (Δρ, σ, Kendall's W, conditional ρ)\n5. 重跑 N-scaling 分析 (tab:n-scaling)，特别关注 FK\n6. 验证 AUROC 值是否也受影响\n7. 检查 selection F1 是否需要重算（实例集 n 是否变化）\n\n### 最后检查 (低优先级)\n8. 审查所有正文 claim 是否仍与更新后数值一致\n9. 更新 Figure fig_signal_heatmap（若 heatmap 包含 N=16 数据）\n10. 确认 WNUT-17 不受影响（或补算）\n\n---\n\n## 核心结论\n\n**论文的核心贡献（correlation-selection gap）不受影响**，因为它基于 SciERC N=8 实验，不在本次修正范围内。\n\n主要影响集中在:\n- **Appendix robustness 分析** (LLaMA CoNLL N=16 和 Qwen SciERC N=16)\n- **N-scaling 分析** (FK scaling 可能失效)\n- **跨模型稳定性的具体数值** (N=8 LLaMA CoNLL 需验证)\n\n论文的 claim 方向大多不变，但**具体数值需全面更新**。唯一可能受实质影响的是 FK N-scaling 的 claim 和 SJ-FK gap 的 limitations 描述。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 43_

本地文件已保存。现在同步到服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "414178e5-c59f-4e23-919e-6543056e1c2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTk63KjfAZ5hmEAnpaRz59",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9613,
      "cache_read_input_tokens": 74777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9613
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016pQ5X6y9bZtV3Mo3YvTKGs`</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "dd6ffc1d-22df-4fda-be2c-584ced279d46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTk63KjfAZ5hmEAnpaRz59",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9613,
      "cache_read_input_tokens": 74777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9613
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

_source line 45 · 2026-05-15T13:34:16.779Z_

<details><summary>↩ Tool result · `toolu_016pQ5X6y9bZtV3Mo3YvTKGs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "3b7b6003-5d47-4c79-958c-4e41e0e5d7e4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.0}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_016TAn7LNxsjwwkoWBMQYtPd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_paper_impact_list.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "9b234223-fc63-4159-a857-2db9f37f64c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017223EJmXpPEWvXdqUQcAdY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 216,
      "cache_read_input_tokens": 84390,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 216
      },
      "output_tokens": 64,
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

_source line 47 · 2026-05-15T13:34:19.456Z_

<details><summary>↩ Tool result · `toolu_016TAn7LNxsjwwkoWBMQYtPd`</summary>

````text
1	# ρ 值论文影响清单
2	
3	**生成日期**: 2026-05-15
4	**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)
5	**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1
6	
7	---
8	
9	## 统一管道修正值摘要
10	
11	| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |
12	|------|--------|---------------|--------|---|------|
13	| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |
14	| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |
15	| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |
16	| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |
17	| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |
18	| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |
19	| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |
20	
21	**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。
22	
23	---
24	
25	## 需更新的 ρ 值位置
26	
27	### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section
28	
29	**文件**: `sections/appendix.tex`, L52-57
30	
31	**当前值**:
32	```
33	SJ:  0.463 ± 0.007
34	FK:  0.455 ± 0.006
35	EM:  0.460 ± 0.008
36	VC:  0.458 ± 0.003
37	LP:  0.310 ± 0.005
38	```
39	
40	**统一管道 (2/3 seeds available)**:
41	| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |
42	|--------|--------|---------|----------------|------|
43	| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |
44	| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |
45	| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |
46	| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |
47	| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |
48	
49	**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。**需用统一管道重算 3 seed 并更新此表。** seed123 的统一值不在 JSON 中，需补算。
50	
51	**σ 值也需更新**: 当前 σ(SJ)=0.007，若统一 seed42=0.484、seed456=0.473，新 σ 取决于 seed123。
52	
53	### 2. Table tab:robustness — Qwen SciERC N=16 section
54	
55	**文件**: `sections/appendix.tex`, L47-50
56	
57	**当前值**:
58	```
59	SJ N=16: 0.411 (3-seed mean, footnote †)
60	FK N=16: 0.283
61	```
62	
63	**统一管道 seed456**:
64	- SJ: 0.4098 (vs 旧 registry 0.4134, Δ=-0.004, 几乎不变)
65	- FK: 0.2723 (vs 旧 registry 0.3448, **Δ=-0.073**)
66	
67	**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259（估算: 若 seed456 从 0.345→0.272，其他 2 seed 不变）。需用统一管道重算全部 3 seed。SJ 基本不受影响。
68	
69	### 3. Table tab:n-scaling — Qwen SciERC 3-seed
70	
71	**文件**: `sections/appendix.tex`, L582-596
72	
73	**当前值** (受影响行):
74	```
75	FK: N=8: 0.2536, N=16: 0.2833, Δ: +0.0297
76	```
77	
78	**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，则:
79	- FK Δ(N=8→N=16) 从 +0.030 降至 **~+0.005**
80	- FK N-scaling 从"弱正"变为"近乎零"
81	
82	其他行 (SJ, VC, EM, LP) 受影响较小。需重算。
83	
84	### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8
85	
86	**文件**: `sections/experiments.tex`, L38-42
87	
88	**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307
89	
90	**状态**: ⚠️ **统一 JSON 不含 N=8 数据**。但同一管道问题（gold-empty filtering + FK/SJ 计算）同样影响 N=8 实验。**需用统一管道重算 N=8 LLaMA CoNLL 并验证**。
91	
92	> 若 N=8 也出现 FK↓SJ↑ 的趋势，Table 1 数值和排名可能变化。
93	
94	### 5. Table tab:sigma-comparison
95	
96	**文件**: `sections/appendix.tex`, L619-637
97	
98	LLaMA CoNLL 不在此表（此表是 Qwen SciERC），但 Qwen SciERC N=16 σ 值受 seed456 FK 变化影响。需重算。
99	
100	### 6. Table tab:ranking-stability (Kendall's W)
101	
102	**文件**: `sections/appendix.tex`, L599-615
103	
104	Qwen NER N=16 行: 当前 W=0.956, consensus "SJ ≈ VC > EM > FK > LP"。若 FK N=16 下降，排名可能变为 "SJ ≈ VC > EM > LP > FK"（FK 和 LP 可能交换）。需验证。
105	
106	---
107	
108	## 正文引用
109	
110	### experiments.tex
111	
112	| 行号 | 原文 | 影响 | 优先级 |
113	|------|------|------|--------|
114	| L71 | "SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005, within 3-seed σ≈0.007)" | N=8 LLaMA CoNLL SJ=0.431 需验证；σ≈0.007 可能变化 | ⚠️ 需 N=8 数据 |
115	| L140 | "structural signals maintaining their advantage over LP across all NER settings (Δρ=+0.135 to +0.175)" | 此 Δρ 范围源自 N=16 各配置。统一管道下 LLaMA CoNLL SJ-LP Δ≈+0.170 (seed42)，可能使范围上移 | 中 |
116	
117	### appendix.tex
118	
119	| 行号 | 原文 | 影响 | 优先级 |
120	|------|------|------|--------|
121	| L53-54 | "SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153" | 统一管道 SJ 更高，Δ 增大至 ~+0.170 | 高 |
122	| L77 | "LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain Δρ≈+0.030 (range: +0.027 to +0.032) while LP gains only +0.003" | 依赖 N=8 和 N=16 差值。若 N=16 升高而 N=8 不变，Δρ 增大；若 N=8 也升高，可能抵消 | ⚠️ 需 N=8 数据 |
123	| L78-79 | "FK N-scaling is inconsistent: degradation on SciERC (-0.007 to -0.019) but improvement on CoNLL with LLaMA (+0.027)" | SciERC FK N-scaling Δ 可能从+0.030 变为+0.005，且 CoNLL 的+0.027 可能变化 | 高 |
124	| L84 | "LLaMA SciERC NER (SJ ρ=0.325±0.021, FK ρ=0.256±0.024)" | LLaMA SciERC N=8 — 不在 JSON 中，但可能受同一管道影响 | ⚠️ 需验证 |
125	| L85-86 | "SJ achieves ρ=0.431 (LLaMA) vs. 0.436 (Qwen), Δ=0.005" | N=8 LLaMA CoNLL 值 | ⚠️ 需 N=8 数据 |
126	| L86 | "LLaMA CoNLL 3-seed (SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153)" | 同 L53-54 | 高 |
127	| L138 | "CoNLL LLaMA 3-seed (ρ=0.462)" [conditional EM] | 条件过滤值，受管道变化影响 | 高 |
128	| L191-193 | "SJ already achieves ρ=0.431 on LLaMA CoNLL (vs. LP ρ=0.307, Δ=+0.124), and the gap widens at N=16 (Δ=+0.153)" | N=8 + N=16 混合引用 | 高 |
129	| L199 | "VC achieves the largest gain over greedy (+0.28 pp, p=0.003–0.027 across 3 seeds)" | 选择 F1 非 ρ，但若实例集变化，选择结果可能不同 | 中 |
130	
131	### sections/discussion.tex
132	
133	| 行号 | 原文 | 影响 | 优先级 |
134	|------|------|------|--------|
135	| L6 | "At higher sample sizes (N=16), SJ converges to comparable NER performance with VC (Δ=0.002) with lower cross-seed variance (σ=0.010 vs. 0.026)" | SJ/VC N=16 值变化 → Δ 和 σ 需重算 | 中 |
136	
137	### sections/limitations.tex
138	
139	| 行号 | 原文 | 影响 | 优先级 |
140	|------|------|------|--------|
141	| L15 | "On CoNLL with LLaMA, the SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)" | N=8 值。统一管道 N=16 gap≈0.009 (seed42)。若 N=8 也扩大，此 claim 需修改 | ⚠️ 需 N=8 数据 |
142	
143	---
144	
145	## 排名变化
146	
147	### LLaMA CoNLL N=16 (最重要)
148	
149	**旧 Registry 排名**: FK (0.81) >> SJ (0.18) — FK 绝对主导
150	**论文当前排名**: SJ (0.463) > EM (0.460) > VC (0.458) > FK (0.455) > LP (0.310) — SJ 略高于 FK
151	**统一管道排名 (seed42)**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314) — SJ > FK，但 FK 上升
152	**统一管道排名 (seed456)**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310) — 四信号趋同
153	
154	**关键变化**:
155	1. 旧 registry → 统一: **FK/SJ 排名完全反转**（FK 从第一降至中间，SJ 从最后升至顶部）
156	2. 论文 → 统一: 排名方向一致（SJ ≥ FK），但**绝对值系统性偏低 ~0.015**
157	3. 统一管道下四个一致性信号更加趋同（range 0.009 vs 论文的 0.008），LP 差距更大
158	
159	### Qwen SciERC N=16 NER
160	
161	**旧 Registry**: FK=0.345, SJ=0.413
162	**统一管道 seed456**: FK=0.272, SJ=0.410
163	
164	**排名影响**: FK 从 SJ 的 83% 降至 66%。在 3-seed 排名中，FK 可能从 #4 降至 #5（与 LP 交换）。
165	
166	---
167	
168	## 核心 Claim 影响评估
169	
170	### 1. Correlation-Selection Gap (核心贡献)
171	
172	**Claim**: "ρ up to 0.38, AUROC up to 0.75, yet none significantly improves sample selection"
173	
174	**影响**: ✅ **不受影响**。此 claim 基于 SciERC N=8 seed=42 结果（VC ρ=0.379），不在本次修正范围内。选择实验也在 SciERC N=8 上进行。
175	
176	### 2. Difficulty-Dependent Signal Complementarity
177	
178	**Claim**: "EM leads on easy tasks (CoNLL), SJ on hard tasks (SciERC)"
179	
180	**影响**: ⚠️ **需验证 N=8 CoNLL LLaMA**。
181	- CoNLL Qwen N=8: EM=0.451 明确领先 → 不受影响
182	- CoNLL LLaMA N=8: EM=0.431 = SJ=0.431（并列） → 若统一管道下排名变化，claim 需调整措辞
183	- SciERC N=8: VC/SJ 领先 → 不受影响
184	
185	### 3. Signal Stability Across Model Families
186	
187	**Claim**: "SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005)"
188	
189	**影响**: ⚠️ **需 N=8 统一值**。若 LLaMA CoNLL N=8 SJ 值变化，Δ 可能不再是 0.005。但 claim 的方向（跨模型稳定）可能仍成立。
190	
191	### 4. Structural Advantage Over LP
192	
193	**Claim**: "Δρ=+0.135 to +0.175"
194	
195	**影响**: ✅ **加强**。统一管道下 SJ-LP 差距更大（N=16 seed42: 0.484-0.314=+0.170），structural advantage 更明显。
196	
197	### 5. "Uniform N-Scaling" on LLaMA CoNLL
198	
199	**Claim**: "all four consistency signals gain Δρ≈+0.030"
200	
201	**影响**: ⚠️ **需全面重算**。N=16 值升高但 N=8 值未知。若 N=8 也升高，Δ 可能不变；若只有 N=16 升高，Δ 增大。
202	
203	### 6. FK N-Scaling on SciERC
204	
205	**Claim**: FK N=16 Δ=+0.030 (tab:n-scaling)
206	
207	**影响**: ❌ **可能失效**。seed456 FK 从 0.345 降至 0.272，3-seed mean N=16 FK 可能降至 ~0.259，使 Δ 从 +0.030 降至 +0.005。相关文本 "FK N-scaling is inconsistent" 的具体数值需更新。
208	
209	### 7. SJ-FK Gap on CoNLL (Limitations)
210	
211	**Claim**: "SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)"
212	
213	**影响**: ⚠️ **需 N=8 验证**。统一 N=16 gap=0.009 (seed42)。若 N=8 gap 也扩大，此 limitation 的具体数值需更新，但方向（gap 较小）可能仍成立。
214	
215	### 8. 3-Seed σ Values
216	
217	**Claim**: "σ≤0.026" (multiseed stability)
218	
219	**影响**: ⚠️ σ 值会随 ρ 值变化。需用统一管道重算所有 3-seed 统计量。
220	
221	---
222	
223	## 未覆盖的缺口
224	
225	以下实验/配置受同一管道问题影响，但统一 JSON 未提供修正值:
226	
227	1. **LLaMA CoNLL N=8** (Table 1, 多处正文引用) — 697 gold-empty 实例同样存在
228	2. **LLaMA CoNLL N=16 seed123** — 3-seed mean 需要全部 3 个 seed
229	3. **Qwen SciERC N=16 seed42 和 seed123** — 3-seed mean 需要全部 3 个 seed
230	4. **Qwen CoNLL N=8 / N=16** — 同一 CoNLL 数据集，可能受影响
231	5. **WNUT-17** — 有 gold-empty 实例（JSON 中 WNUT 未出现，需确认）
232	6. **LLaMA SciERC N=8** (appendix L84) — 可能受影响
233	7. **条件过滤值** (conditional ρ) — JSON 仅提供部分 conditional 值
234	8. **AUROC 值** — JSON 提供了统一 AUROC，但论文中的 AUROC 主要在 Table 1 (N=8)，无法直接比对
235	9. **Selection F1 值** — 管道变化可能影响实例集，间接影响选择实验结果
236	
237	---
238	
239	## 建议行动
240	
241	### 立即执行 (高优先级)
242	1. **重算全部 3 seed 的统一 ρ** for LLaMA CoNLL N=16 → 更新 tab:robustness 和所有引用
243	2. **重算全部 3 seed 的统一 ρ** for Qwen SciERC N=16 → 更新 tab:robustness 和 tab:n-scaling
244	3. **重算 LLaMA CoNLL N=8 统一 ρ** → 更新 Table 1 和所有 N=8 引用
245	
246	### 随后更新 (中优先级)
247	4. 更新所有衍生统计量 (Δρ, σ, Kendall's W, conditional ρ)
248	5. 重跑 N-scaling 分析 (tab:n-scaling)，特别关注 FK
249	6. 验证 AUROC 值是否也受影响
250	7. 检查 selection F1 是否需要重算（实例集 n 是否变化）
251	
252	### 最后检查 (低优先级)
253	8. 审查所有正文 claim 是否仍与更新后数值一致
254	9. 更新 Figure fig_signal_heatmap（若 heatmap 包含 N=16 数据）
255	10. 确认 WNUT-17 不受影响（或补算）
256	
257	---
258	
259	## 核心结论
260	
261	**论文的核心贡献（correlation-selection gap）不受影响**，因为它基于 SciERC N=8 实验，不在本次修正范围内。
262	
263	主要影响集中在:
264	- **Appendix robustness 分析** (LLaMA CoNLL N=16 和 Qwen SciERC N=16)
265	- **N-scaling 分析** (FK scaling 可能失效)
266	- **跨模型稳定性的具体数值** (N=8 LLaMA CoNLL 需验证)
267	
268	论文的 claim 方向大多不变，但**具体数值需全面更新**。唯一可能受实质影响的是 FK N-scaling 的 claim 和 SJ-FK gap 的 limitations 描述。
269	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "46a58b88-524d-4f43-9007-049bceb08f48",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_paper_impact_list.md",
      "content": "# ρ 值论文影响清单\n\n**生成日期**: 2026-05-15\n**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)\n**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1\n\n---\n\n## 统一管道修正值摘要\n\n| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |\n|------|--------|---------------|--------|---|------|\n| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |\n| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |\n| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |\n| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |\n| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |\n\n**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。\n\n---\n\n## 需更新的 ρ 值位置\n\n### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section\n\n**文件**: `sections/appendix.tex`, L52-57\n\n**当前值**:\n```\nSJ:  0.463 ± 0.007\nFK:  0.455 ± 0.006\nEM:  0.460 ± 0.008\nVC:  0.458 ± 0.003\nLP:  0.310 ± 0.005\n```\n\n**统一管道 (2/3 seeds available)**:\n| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |\n|--------|--------|---------|----------------|------|\n| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |\n| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |\n| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |\n| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |\n| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |\n\n**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。**需用统一管道重算 3 seed 并更新此表。** seed123 的统一值不在 JSON 中，需补算。\n\n**σ 值也需更新**: 当前 σ(SJ)=0.007，若统一 seed42=0.484、seed456=0.473，新 σ 取决于 seed123。\n\n### 2. Table tab:robustness — Qwen SciERC N=16 section\n\n**文件**: `sections/appendix.tex`, L47-50\n\n**当前值**:\n```\nSJ N=16: 0.411 (3-seed mean, footnote †)\nFK N=16: 0.283\n```\n\n**统一管道 seed456**:\n- SJ: 0.4098 (vs 旧 registry 0.4134, Δ=-0.004, 几乎不变)\n- FK: 0.2723 (vs 旧 registry 0.3448, **Δ=-0.073**)\n\n**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259（估算: 若 seed456 从 0.345→0.272，其他 2 seed 不变）。需用统一管道重算全部 3 seed。SJ 基本不受影响。\n\n### 3. Table tab:n-scaling — Qwen SciERC 3-seed\n\n**文件**: `sections/appendix.tex`, L582-596\n\n**当前值** (受影响行):\n```\nFK: N=8: 0.2536, N=16: 0.2833, Δ: +0.0297\n```\n\n**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，则:\n- FK Δ(N=8→N=16) 从 +0.030 降至 **~+0.005**\n- FK N-scaling 从\"弱正\"变为\"近乎零\"\n\n其他行 (SJ, VC, EM, LP) 受影响较小。需重算。\n\n### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8\n\n**文件**: `sections/experiments.tex`, L38-42\n\n**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307\n\n**状态**: ⚠️ **统一 JSON 不含 N=8 数据**。但同一管道问题（gold-empty filtering + FK/SJ 计算）同样影响 N=8 实验。**需用统一管道重算 N=8 LLaMA CoNLL 并验证**。\n\n> 若 N=8 也出现 FK↓SJ↑ 的趋势，Table 1 数值和排名可能变化。\n\n### 5. Table tab:sigma-comparison\n\n**文件**: `sections/appendix.tex`, L619-637\n\nLLaMA CoNLL 不在此表（此表是 Qwen SciERC），但 Qwen SciERC N=16 σ 值受 seed456 FK 变化影响。需重算。\n\n### 6. Table tab:ranking-stability (Kendall's W)\n\n**文件**: `sections/appendix.tex`, L599-615\n\nQwen NER N=16 行: 当前 W=0.956, consensus \"SJ ≈ VC > EM > FK > LP\"。若 FK N=16 下降，排名可能变为 \"SJ ≈ VC > EM > LP > FK\"（FK 和 LP 可能交换）。需验证。\n\n---\n\n## 正文引用\n\n### experiments.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L71 | \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005, within 3-seed σ≈0.007)\" | N=8 LLaMA CoNLL SJ=0.431 需验证；σ≈0.007 可能变化 | ⚠️ 需 N=8 数据 |\n| L140 | \"structural signals maintaining their advantage over LP across all NER settings (Δρ=+0.135 to +0.175)\" | 此 Δρ 范围源自 N=16 各配置。统一管道下 LLaMA CoNLL SJ-LP Δ≈+0.170 (seed42)，可能使范围上移 | 中 |\n\n### appendix.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L53-54 | \"SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153\" | 统一管道 SJ 更高，Δ 增大至 ~+0.170 | 高 |\n| L77 | \"LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain Δρ≈+0.030 (range: +0.027 to +0.032) while LP gains only +0.003\" | 依赖 N=8 和 N=16 差值。若 N=16 升高而 N=8 不变，Δρ 增大；若 N=8 也升高，可能抵消 | ⚠️ 需 N=8 数据 |\n| L78-79 | \"FK N-scaling is inconsistent: degradation on SciERC (-0.007 to -0.019) but improvement on CoNLL with LLaMA (+0.027)\" | SciERC FK N-scaling Δ 可能从+0.030 变为+0.005，且 CoNLL 的+0.027 可能变化 | 高 |\n| L84 | \"LLaMA SciERC NER (SJ ρ=0.325±0.021, FK ρ=0.256±0.024)\" | LLaMA SciERC N=8 — 不在 JSON 中，但可能受同一管道影响 | ⚠️ 需验证 |\n| L85-86 | \"SJ achieves ρ=0.431 (LLaMA) vs. 0.436 (Qwen), Δ=0.005\" | N=8 LLaMA CoNLL 值 | ⚠️ 需 N=8 数据 |\n| L86 | \"LLaMA CoNLL 3-seed (SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153)\" | 同 L53-54 | 高 |\n| L138 | \"CoNLL LLaMA 3-seed (ρ=0.462)\" [conditional EM] | 条件过滤值，受管道变化影响 | 高 |\n| L191-193 | \"SJ already achieves ρ=0.431 on LLaMA CoNLL (vs. LP ρ=0.307, Δ=+0.124), and the gap widens at N=16 (Δ=+0.153)\" | N=8 + N=16 混合引用 | 高 |\n| L199 | \"VC achieves the largest gain over greedy (+0.28 pp, p=0.003–0.027 across 3 seeds)\" | 选择 F1 非 ρ，但若实例集变化，选择结果可能不同 | 中 |\n\n### sections/discussion.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L6 | \"At higher sample sizes (N=16), SJ converges to comparable NER performance with VC (Δ=0.002) with lower cross-seed variance (σ=0.010 vs. 0.026)\" | SJ/VC N=16 值变化 → Δ 和 σ 需重算 | 中 |\n\n### sections/limitations.tex\n\n| 行号 | 原文 | 影响 | 优先级 |\n|------|------|------|--------|\n| L15 | \"On CoNLL with LLaMA, the SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\" | N=8 值。统一管道 N=16 gap≈0.009 (seed42)。若 N=8 也扩大，此 claim 需修改 | ⚠️ 需 N=8 数据 |\n\n---\n\n## 排名变化\n\n### LLaMA CoNLL N=16 (最重要)\n\n**旧 Registry 排名**: FK (0.81) >> SJ (0.18) — FK 绝对主导\n**论文当前排名**: SJ (0.463) > EM (0.460) > VC (0.458) > FK (0.455) > LP (0.310) — SJ 略高于 FK\n**统一管道排名 (seed42)**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314) — SJ > FK，但 FK 上升\n**统一管道排名 (seed456)**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310) — 四信号趋同\n\n**关键变化**:\n1. 旧 registry → 统一: **FK/SJ 排名完全反转**（FK 从第一降至中间，SJ 从最后升至顶部）\n2. 论文 → 统一: 排名方向一致（SJ ≥ FK），但**绝对值系统性偏低 ~0.015**\n3. 统一管道下四个一致性信号更加趋同（range 0.009 vs 论文的 0.008），LP 差距更大\n\n### Qwen SciERC N=16 NER\n\n**旧 Registry**: FK=0.345, SJ=0.413\n**统一管道 seed456**: FK=0.272, SJ=0.410\n\n**排名影响**: FK 从 SJ 的 83% 降至 66%。在 3-seed 排名中，FK 可能从 #4 降至 #5（与 LP 交换）。\n\n---\n\n## 核心 Claim 影响评估\n\n### 1. Correlation-Selection Gap (核心贡献)\n\n**Claim**: \"ρ up to 0.38, AUROC up to 0.75, yet none significantly improves sample selection\"\n\n**影响**: ✅ **不受影响**。此 claim 基于 SciERC N=8 seed=42 结果（VC ρ=0.379），不在本次修正范围内。选择实验也在 SciERC N=8 上进行。\n\n### 2. Difficulty-Dependent Signal Complementarity\n\n**Claim**: \"EM leads on easy tasks (CoNLL), SJ on hard tasks (SciERC)\"\n\n**影响**: ⚠️ **需验证 N=8 CoNLL LLaMA**。\n- CoNLL Qwen N=8: EM=0.451 明确领先 → 不受影响\n- CoNLL LLaMA N=8: EM=0.431 = SJ=0.431（并列） → 若统一管道下排名变化，claim 需调整措辞\n- SciERC N=8: VC/SJ 领先 → 不受影响\n\n### 3. Signal Stability Across Model Families\n\n**Claim**: \"SJ achieves ρ=0.436 (Qwen) vs. 0.431 (LLaMA) on CoNLL (Δ=0.005)\"\n\n**影响**: ⚠️ **需 N=8 统一值**。若 LLaMA CoNLL N=8 SJ 值变化，Δ 可能不再是 0.005。但 claim 的方向（跨模型稳定）可能仍成立。\n\n### 4. Structural Advantage Over LP\n\n**Claim**: \"Δρ=+0.135 to +0.175\"\n\n**影响**: ✅ **加强**。统一管道下 SJ-LP 差距更大（N=16 seed42: 0.484-0.314=+0.170），structural advantage 更明显。\n\n### 5. \"Uniform N-Scaling\" on LLaMA CoNLL\n\n**Claim**: \"all four consistency signals gain Δρ≈+0.030\"\n\n**影响**: ⚠️ **需全面重算**。N=16 值升高但 N=8 值未知。若 N=8 也升高，Δ 可能不变；若只有 N=16 升高，Δ 增大。\n\n### 6. FK N-Scaling on SciERC\n\n**Claim**: FK N=16 Δ=+0.030 (tab:n-scaling)\n\n**影响**: ❌ **可能失效**。seed456 FK 从 0.345 降至 0.272，3-seed mean N=16 FK 可能降至 ~0.259，使 Δ 从 +0.030 降至 +0.005。相关文本 \"FK N-scaling is inconsistent\" 的具体数值需更新。\n\n### 7. SJ-FK Gap on CoNLL (Limitations)\n\n**Claim**: \"SJ-FK gap is only 0.003 (ρ=0.431 vs. 0.428)\"\n\n**影响**: ⚠️ **需 N=8 验证**。统一 N=16 gap=0.009 (seed42)。若 N=8 gap 也扩大，此 limitation 的具体数值需更新，但方向（gap 较小）可能仍成立。\n\n### 8. 3-Seed σ Values\n\n**Claim**: \"σ≤0.026\" (multiseed stability)\n\n**影响**: ⚠️ σ 值会随 ρ 值变化。需用统一管道重算所有 3-seed 统计量。\n\n---\n\n## 未覆盖的缺口\n\n以下实验/配置受同一管道问题影响，但统一 JSON 未提供修正值:\n\n1. **LLaMA CoNLL N=8** (Table 1, 多处正文引用) — 697 gold-empty 实例同样存在\n2. **LLaMA CoNLL N=16 seed123** — 3-seed mean 需要全部 3 个 seed\n3. **Qwen SciERC N=16 seed42 和 seed123** — 3-seed mean 需要全部 3 个 seed\n4. **Qwen CoNLL N=8 / N=16** — 同一 CoNLL 数据集，可能受影响\n5. **WNUT-17** — 有 gold-empty 实例（JSON 中 WNUT 未出现，需确认）\n6. **LLaMA SciERC N=8** (appendix L84) — 可能受影响\n7. **条件过滤值** (conditional ρ) — JSON 仅提供部分 conditional 值\n8. **AUROC 值** — JSON 提供了统一 AUROC，但论文中的 AUROC 主要在 Table 1 (N=8)，无法直接比对\n9. **Selection F1 值** — 管道变化可能影响实例集，间接影响选择实验结果\n\n---\n\n## 建议行动\n\n### 立即执行 (高优先级)\n1. **重算全部 3 seed 的统一 ρ** for LLaMA CoNLL N=16 → 更新 tab:robustness 和所有引用\n2. **重算全部 3 seed 的统一 ρ** for Qwen SciERC N=16 → 更新 tab:robustness 和 tab:n-scaling\n3. **重算 LLaMA CoNLL N=8 统一 ρ** → 更新 Table 1 和所有 N=8 引用\n\n### 随后更新 (中优先级)\n4. 更新所有衍生统计量 (Δρ, σ, Kendall's W, conditional ρ)\n5. 重跑 N-scaling 分析 (tab:n-scaling)，特别关注 FK\n6. 验证 AUROC 值是否也受影响\n7. 检查 selection F1 是否需要重算（实例集 n 是否变化）\n\n### 最后检查 (低优先级)\n8. 审查所有正文 claim 是否仍与更新后数值一致\n9. 更新 Figure fig_signal_heatmap（若 heatmap 包含 N=16 数据）\n10. 确认 WNUT-17 不受影响（或补算）\n\n---\n\n## 核心结论\n\n**论文的核心贡献（correlation-selection gap）不受影响**，因为它基于 SciERC N=8 实验，不在本次修正范围内。\n\n主要影响集中在:\n- **Appendix robustness 分析** (LLaMA CoNLL N=16 和 Qwen SciERC N=16)\n- **N-scaling 分析** (FK scaling 可能失效)\n- **跨模型稳定性的具体数值** (N=8 LLaMA CoNLL 需验证)\n\n论文的 claim 方向大多不变，但**具体数值需全面更新**。唯一可能受实质影响的是 FK N-scaling 的 claim 和 SJ-FK gap 的 limitations 描述。\n",
      "numLines": 269,
      "startLine": 1,
      "totalLines": 269
    }
  }
}
````

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01WUr2VJYwBmKTPJD8AHQ6R6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_unified_rho.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "5423f03e-2d7c-4437-80df-e0adcd7f5312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWitMqNYJcFjkg5cs8anvd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6577,
      "cache_read_input_tokens": 84606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6577
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

_source line 49 · 2026-05-15T13:34:23.795Z_

<details><summary>↩ Tool result · `toolu_01WUr2VJYwBmKTPJD8AHQ6R6`</summary>

```text
1	{
2	  "audit_date": "2026-05-15",
3	  "pipeline": "unified (gold-filtered, consistency.py FK/SJ, evaluation.py per_instance_f1)",
4	  "filter": "exclude instances where len(gold.entities) == 0",
5	  "experiments": {
6	    "exp_017_llama_conll_n16_r1024": {
7	      "description": "LLaMA CoNLL seed42 n16 r1024",
8	      "n_total": 3453,
9	      "n_gold_empty": 697,
10	      "n_valid": 2756,
11	      "n_conditional": 2641,
12	      "old_registry_rho_fk": 0.8095,
13	      "old_registry_rho_sj": 0.1815,
14	      "unified_full": {
15	        "rho_fk": 0.4752,
16	        "rho_sj": 0.4836,
17	        "rho_vc": 0.4746,
18	        "rho_em": 0.4818,
19	        "rho_lp": 0.3136,
20	        "auroc_fk": 0.7467,
21	        "auroc_sj": 0.7496,
22	        "auroc_vc": 0.7529,
23	        "auroc_em": 0.7508,
24	        "auroc_lp": 0.7661,
25	        "median_f1": 1.0
26	      },
27	      "unified_conditional": {
28	        "rho_fk": 0.4767,
29	        "rho_sj": 0.4856
30	      }
31	    },
32	    "exp_017_llama_conll_n16_s456_r1024": {
33	      "description": "LLaMA CoNLL seed456 n16 r1024",
34	      "n_total": 3453,
35	      "n_gold_empty": 697,
36	      "n_valid": 2756,
37	      "n_conditional": 2642,
38	      "old_registry_rho_fk": 0.8085,
39	      "old_registry_rho_sj": 0.1895,
40	      "unified_full": {
41	        "rho_fk": 0.469,
42	        "rho_sj": 0.4734,
43	        "rho_vc": 0.4722,
44	        "rho_em": 0.4752,
45	        "rho_lp": 0.3099,
46	        "auroc_fk": 0.7408,
47	        "auroc_sj": 0.7428,
48	        "auroc_vc": 0.7495,
49	        "auroc_em": 0.7444,
50	        "auroc_lp": 0.7628,
51	        "median_f1": 1.0
52	      },
53	      "unified_conditional": {
54	        "rho_fk": 0.4694,
55	        "rho_sj": 0.4728
56	      }
57	    },
58	    "exp_001_n16_seed456": {
59	      "description": "Qwen SciERC seed456 joint n16",
60	      "n_total": 551,
61	      "n_gold_empty": 22,
62	      "n_valid": 529,
63	      "n_conditional": 478,
64	      "old_registry_rho_fk": 0.3448,
65	      "old_registry_rho_sj": 0.4134,
66	      "unified_full_ner": {
67	        "rho_fk": 0.2723,
68	        "rho_sj": 0.4098,
69	        "rho_vc": 0.4449,
70	        "rho_em": 0.3363,
71	        "rho_lp": 0.2415,
72	        "auroc_fk": 0.6179,
73	        "auroc_sj": 0.6823,
74	        "auroc_vc": 0.6981,
75	        "auroc_em": 0.649,
76	        "auroc_lp": 0.5885,
77	        "median_f1": 0.6667
78	      },
79	      "unified_conditional_ner": {
80	        "rho_fk": 0.1887,
81	        "rho_sj": 0.3735
82	      },
83	      "unified_re": {
84	        "n_re_valid": 397,
85	        "rho_fk": 0.2929,
86	        "rho_sj": 0.2835
87	      }
88	    },
89	    "exp_011_ood_conll_to_scierc": {
90	      "description": "OOD ConLL-trained on SciERC test",
91	      "n_total": 551,
92	      "n_gold_empty": 22,
93	      "n_valid": 529,
94	      "n_conditional": 12,
95	      "registry_already_correct": true,
96	      "unified_full": {
97	        "rho_fk": -0.0695,
98	        "rho_sj": -0.1857,
99	        "rho_vc": 0.1972,
100	        "rho_em": -0.2015,
101	        "rho_lp": -0.1521
102	      }
103	    }
104	  }
105	}
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "8f650145-9755-4e87-9032-bd306e2fddcf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_unified_rho.json",
      "content": "{\n  \"audit_date\": \"2026-05-15\",\n  \"pipeline\": \"unified (gold-filtered, consistency.py FK/SJ, evaluation.py per_instance_f1)\",\n  \"filter\": \"exclude instances where len(gold.entities) == 0\",\n  \"experiments\": {\n    \"exp_017_llama_conll_n16_r1024\": {\n      \"description\": \"LLaMA CoNLL seed42 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2641,\n      \"old_registry_rho_fk\": 0.8095,\n      \"old_registry_rho_sj\": 0.1815,\n      \"unified_full\": {\n        \"rho_fk\": 0.4752,\n        \"rho_sj\": 0.4836,\n        \"rho_vc\": 0.4746,\n        \"rho_em\": 0.4818,\n        \"rho_lp\": 0.3136,\n        \"auroc_fk\": 0.7467,\n        \"auroc_sj\": 0.7496,\n        \"auroc_vc\": 0.7529,\n        \"auroc_em\": 0.7508,\n        \"auroc_lp\": 0.7661,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4767,\n        \"rho_sj\": 0.4856\n      }\n    },\n    \"exp_017_llama_conll_n16_s456_r1024\": {\n      \"description\": \"LLaMA CoNLL seed456 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2642,\n      \"old_registry_rho_fk\": 0.8085,\n      \"old_registry_rho_sj\": 0.1895,\n      \"unified_full\": {\n        \"rho_fk\": 0.469,\n        \"rho_sj\": 0.4734,\n        \"rho_vc\": 0.4722,\n        \"rho_em\": 0.4752,\n        \"rho_lp\": 0.3099,\n        \"auroc_fk\": 0.7408,\n        \"auroc_sj\": 0.7428,\n        \"auroc_vc\": 0.7495,\n        \"auroc_em\": 0.7444,\n        \"auroc_lp\": 0.7628,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4694,\n        \"rho_sj\": 0.4728\n      }\n    },\n    \"exp_001_n16_seed456\": {\n      \"description\": \"Qwen SciERC seed456 joint n16\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 478,\n      \"old_registry_rho_fk\": 0.3448,\n      \"old_registry_rho_sj\": 0.4134,\n      \"unified_full_ner\": {\n        \"rho_fk\": 0.2723,\n        \"rho_sj\": 0.4098,\n        \"rho_vc\": 0.4449,\n        \"rho_em\": 0.3363,\n        \"rho_lp\": 0.2415,\n        \"auroc_fk\": 0.6179,\n        \"auroc_sj\": 0.6823,\n        \"auroc_vc\": 0.6981,\n        \"auroc_em\": 0.649,\n        \"auroc_lp\": 0.5885,\n        \"median_f1\": 0.6667\n      },\n      \"unified_conditional_ner\": {\n        \"rho_fk\": 0.1887,\n        \"rho_sj\": 0.3735\n      },\n      \"unified_re\": {\n        \"n_re_valid\": 397,\n        \"rho_fk\": 0.2929,\n        \"rho_sj\": 0.2835\n      }\n    },\n    \"exp_011_ood_conll_to_scierc\": {\n      \"description\": \"OOD ConLL-trained on SciERC test\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 12,\n      \"registry_already_correct\": true,\n      \"unified_full\": {\n        \"rho_fk\": -0.0695,\n        \"rho_sj\": -0.1857,\n        \"rho_vc\": 0.1972,\n        \"rho_em\": -0.2015,\n        \"rho_lp\": -0.1521\n      }\n    }\n  }\n}\n",
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

_source line 50_

Now syncing both files to the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "b18bed83-6ecc-4e78-b175-39f71a0411f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xp7Zmpsn9FaKe8nd3CNDFL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 91183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1643
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

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01K4kuBzCWG2o9anapDjgDdN`</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/analysis_unified_rho.json << 'JSONEOF'\n{\n  \"audit_date\": \"2026-05-15\",\n  \"pipeline\": \"unified (gold-filtered, consistency.py FK/SJ, evaluation.py per_instance_f1)\",\n  \"filter\": \"exclude instances where len(gold.entities) == 0\",\n  \"experiments\": {\n    \"exp_017_llama_conll_n16_r1024\": {\n      \"description\": \"LLaMA CoNLL seed42 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2641,\n      \"old_registry_rho_fk\": 0.8095,\n      \"old_registry_rho_sj\": 0.1815,\n      \"unified_full\": {\n        \"rho_fk\": 0.4752,\n        \"rho_sj\": 0.4836,\n        \"rho_vc\": 0.4746,\n        \"rho_em\": 0.4818,\n        \"rho_lp\": 0.3136,\n        \"auroc_fk\": 0.7467,\n        \"auroc_sj\": 0.7496,\n        \"auroc_vc\": 0.7529,\n        \"auroc_em\": 0.7508,\n        \"auroc_lp\": 0.7661,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4767,\n        \"rho_sj\": 0.4856\n      }\n    },\n    \"exp_017_llama_conll_n16_s456_r1024\": {\n      \"description\": \"LLaMA CoNLL seed456 n16 r1024\",\n      \"n_total\": 3453,\n      \"n_gold_empty\": 697,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2642,\n      \"old_registry_rho_fk\": 0.8085,\n      \"old_registry_rho_sj\": 0.1895,\n      \"unified_full\": {\n        \"rho_fk\": 0.469,\n        \"rho_sj\": 0.4734,\n        \"rho_vc\": 0.4722,\n        \"rho_em\": 0.4752,\n        \"rho_lp\": 0.3099,\n        \"auroc_fk\": 0.7408,\n        \"auroc_sj\": 0.7428,\n        \"auroc_vc\": 0.7495,\n        \"auroc_em\": 0.7444,\n        \"auroc_lp\": 0.7628,\n        \"median_f1\": 1.0\n      },\n      \"unified_conditional\": {\n        \"rho_fk\": 0.4694,\n        \"rho_sj\": 0.4728\n      }\n    },\n    \"exp_001_n16_seed456\": {\n      \"description\": \"Qwen SciERC seed456 joint n16\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 478,\n      \"old_registry_rho_fk\": 0.3448,\n      \"old_registry_rho_sj\": 0.4134,\n      \"unified_full_ner\": {\n        \"rho_fk\": 0.2723,\n        \"rho_sj\": 0.4098,\n        \"rho_vc\": 0.4449,\n        \"rho_em\": 0.3363,\n        \"rho_lp\": 0.2415,\n        \"auroc_fk\": 0.6179,\n        \"auroc_sj\": 0.6823,\n        \"auroc_vc\": 0.6981,\n        \"auroc_em\": 0.649,\n        \"auroc_lp\": 0.5885,\n        \"median_f1\": 0.6667\n      },\n      \"unified_conditional_ner\": {\n        \"rho_fk\": 0.1887,\n        \"rho_sj\": 0.3735\n      },\n      \"unified_re\": {\n        \"n_re_valid\": 397,\n        \"rho_fk\": 0.2929,\n        \"rho_sj\": 0.2835\n      }\n    },\n    \"exp_011_ood_conll_to_scierc\": {\n      \"description\": \"OOD ConLL-trained on SciERC test\",\n      \"n_total\": 551,\n      \"n_gold_empty\": 22,\n      \"n_valid\": 529,\n      \"n_conditional\": 12,\n      \"registry_already_correct\": true,\n      \"unified_full\": {\n        \"rho_fk\": -0.0695,\n        \"rho_sj\": -0.1857,\n        \"rho_vc\": 0.1972,\n        \"rho_em\": -0.2015,\n        \"rho_lp\": -0.1521\n      }\n    }\n  }\n}\nJSONEOF\necho \"JSON written: $(wc -c < /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/analysis_unified_rho.json) bytes\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "b80bb81a-7f55-4925-8674-a9473949f09f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xp7Zmpsn9FaKe8nd3CNDFL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1643,
      "cache_read_input_tokens": 91183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1643
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

_source line 52 · 2026-05-15T13:34:39.052Z_

<details><summary>↩ Tool result · `toolu_01K4kuBzCWG2o9anapDjgDdN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"JSON written: 2806 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "a364ab22-9bb3-4a45-a640-347e7c885414",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"JSON written: 2806 bytes\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"JSON written: 2806 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01CDCtnKgQhXAGGAtQWwVskq`</summary>

````json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/paper_impact_list.md << 'MDEOF'\n# ρ 值论文影响清单\n\n**生成日期**: 2026-05-15\n**数据源**: `analysis_unified_rho.json` (unified pipeline, gold-filtered)\n**管道变化**: 排除 gold-empty 实例 + 统一 consistency.py FK/SJ + evaluation.py per_instance_f1\n\n---\n\n## 统一管道修正值摘要\n\n| 实验 | Signal | 旧 Registry ρ | 统一 ρ | Δ | 说明 |\n|------|--------|---------------|--------|---|------|\n| LLaMA CoNLL N=16 seed42 | FK | 0.8095 | 0.4752 | **-0.334** | 排名反转 |\n| LLaMA CoNLL N=16 seed42 | SJ | 0.1815 | 0.4836 | **+0.302** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | FK | 0.8085 | 0.4690 | **-0.340** | 排名反转 |\n| LLaMA CoNLL N=16 seed456 | SJ | 0.1895 | 0.4734 | **+0.284** | 排名反转 |\n| Qwen SciERC N=16 seed456 NER | FK | 0.3448 | 0.2723 | **-0.073** | 幅度下降 |\n| Qwen SciERC N=16 seed456 NER | SJ | 0.4134 | 0.4098 | -0.004 | 基本不变 |\n| OOD CoNLL→SciERC | — | — | — | — | 已正确，无需变更 |\n\n**关键发现**: LLaMA CoNLL N=16 旧管道中 FK ρ 严重虚高（0.81），SJ 严重偏低（0.18），统一管道修正后二者趋同（~0.48），**排名发生反转**。\n\n---\n\n## 需更新的 ρ 值位置\n\n### 1. Table tab:robustness — LLaMA CoNLL N=16 3-seed section\n\n**文件**: `sections/appendix.tex`, L52-57\n\n**当前值**:\n```\nSJ:  0.463 ± 0.007\nFK:  0.455 ± 0.006\nEM:  0.460 ± 0.008\nVC:  0.458 ± 0.003\nLP:  0.310 ± 0.005\n```\n\n**统一管道 (2/3 seeds available)**:\n| Signal | seed42 | seed456 | 论文3-seed mean | 差异 |\n|--------|--------|---------|----------------|------|\n| SJ | 0.4836 | 0.4734 | 0.463 | 论文偏低 ~0.015 |\n| FK | 0.4752 | 0.4690 | 0.455 | 论文偏低 ~0.017 |\n| EM | 0.4818 | 0.4752 | 0.460 | 论文偏低 ~0.018 |\n| VC | 0.4746 | 0.4722 | 0.458 | 论文偏低 ~0.015 |\n| LP | 0.3136 | 0.3099 | 0.310 | 基本一致 |\n\n**问题**: 论文 3-seed mean 系统性低于统一管道两个 seed 的值（一致性信号低 ~0.015-0.018，LP 无差异）。推测论文使用了与统一管道不同的计算路径。需用统一管道重算 3 seed 并更新此表。seed123 的统一值不在 JSON 中，需补算。\n\n### 2. Table tab:robustness — Qwen SciERC N=16 section\n\n**文件**: `sections/appendix.tex`, L47-50\n\n**当前值**:\n```\nSJ N=16: 0.411 (3-seed mean)\nFK N=16: 0.283\n```\n\n**统一管道 seed456**: SJ=0.4098 (Δ=-0.004), FK=0.2723 (**Δ=-0.073**)\n**影响**: FK 3-seed mean 可能从 0.283 降至 ~0.259。\n\n### 3. Table tab:n-scaling — Qwen SciERC 3-seed\n\n**文件**: `sections/appendix.tex`, L582-596\n\n**当前值**: FK N=8: 0.2536, N=16: 0.2833, Δ: +0.0297\n**影响**: 若 FK N=16 3-seed mean 降至 ~0.259，Δ 从 +0.030 降至 ~+0.005。\n\n### 4. Table tab:quality_estimation (Table 1) — CoNLL (LLaMA) N=8\n\n**文件**: `sections/experiments.tex`, L38-42\n\n**当前值**: VC .426, SJ .431, FK .428, EM .431, LP .307\n**状态**: 统一 JSON 不含 N=8 数据，需用统一管道重算验证。\n\n### 5-6. tab:sigma-comparison 和 tab:ranking-stability\n\n需用统一管道全部 seed 重算。\n\n---\n\n## 正文引用 (按优先级)\n\n### 高优先级\n- appendix.tex L53-54: \"SJ ρ=0.463±0.007 vs. LP 0.310±0.005, Δ=+0.153\" → 统一管道 Δ 增大至 ~+0.170\n- appendix.tex L86: 同上\n- appendix.tex L78-79: FK N-scaling 具体数值需更新\n- appendix.tex L138: conditional EM CoNLL LLaMA 3-seed (ρ=0.462) 需更新\n- appendix.tex L191-193: N=8 + N=16 混合引用\n\n### 需 N=8 数据验证\n- experiments.tex L71: SJ 0.431 (LLaMA CoNLL N=8)\n- appendix.tex L85-86: SJ 0.431 (LLaMA) vs. 0.436 (Qwen)\n- limitations.tex L15: SJ-FK gap 0.003\n\n### 中优先级\n- experiments.tex L140: Δρ 范围 +0.135 to +0.175\n- discussion.tex L6: SJ/VC N=16 Δ=0.002, σ 值\n\n---\n\n## 排名变化\n\n### LLaMA CoNLL N=16\n- **旧 Registry**: FK (0.81) >> SJ (0.18) — FK 主导\n- **论文当前**: SJ (0.463) > EM > VC > FK (0.455) > LP\n- **统一 seed42**: SJ (0.484) > EM (0.482) > FK (0.475) ≈ VC (0.475) > LP (0.314)\n- **统一 seed456**: EM (0.475) > SJ (0.473) > VC (0.472) > FK (0.469) > LP (0.310)\n\n### Qwen SciERC N=16\n- FK 从 SJ 的 83% 降至 66%，可能与 LP 交换排名\n\n---\n\n## 核心 Claim 影响评估\n\n| Claim | 影响 | 说明 |\n|-------|------|------|\n| Correlation-selection gap | ✅ 不受影响 | 基于 SciERC N=8，不在修正范围 |\n| Difficulty-dependent complementarity | ⚠️ 需验证 | N=8 LLaMA CoNLL 排名可能变化 |\n| Signal stability across models | ⚠️ 需 N=8 数据 | Δ=0.005 可能变化 |\n| Structural advantage over LP | ✅ 加强 | 统一管道下差距更大 |\n| Uniform N-scaling | ⚠️ 需全面重算 | 依赖 N=8 和 N=16 |\n| FK N-scaling on SciERC | ❌ 可能失效 | Δ 从 +0.030 降至 ~+0.005 |\n| SJ-FK gap is 0.003 | ⚠️ 需 N=8 验证 | Gap 可能扩大 |\n\n**核心结论**: 论文核心贡献不受影响。主要影响在 appendix robustness/N-scaling 分析和 FK 相关 claim。\n\n---\n\n## 建议行动\n\n1. 重算全部 3 seed 统一 ρ for LLaMA CoNLL N=16\n2. 重算全部 3 seed 统一 ρ for Qwen SciERC N=16\n3. 重算 LLaMA CoNLL N=8 统一 ρ\n4. 更新所有衍生统计量\n5. 审查正文 claim 与更新数值一致性\nMDEOF\necho \"MD written: $(wc -c < /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/paper_impact_list.md) bytes\"",
  "account": "root"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "d7aa941f-5e89-4848-ab95-247af8b779d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtshpJaVV5r8gM1nUokb94",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 92826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1714
      },
      "output_tokens": 72,
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

_source line 54 · 2026-05-15T13:35:29.592Z_

<details><summary>↩ Tool result · `toolu_01CDCtnKgQhXAGGAtQWwVskq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"MD written: 5116 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "c246290f-4107-4bd3-8b4e-cb0cb1a4b15a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"MD written: 5116 bytes\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"MD written: 5116 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01DfttuUkiHSXbmpk95utxxH`</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "2f4d0551-a728-44aa-a892-62765d760cb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HK2bza3UZxZjH26PXZErJe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 94540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2768
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

_source line 56 · 2026-05-15T13:35:33.827Z_

<details><summary>↩ Tool result · `toolu_01DfttuUkiHSXbmpk95utxxH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  2 root root   79 May 15 21:35 .\\ndrwxr-xr-x 13 root root 4096 May 15 21:34 ..\\n-rw-r--r--  1 root root 2806 May 15 21:34 analysis_unified_rho.json\\n-rw-r--r--  1 root root 5116 May 15 21:35 paper_impact_list.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "79c9feb9-2236-4b61-bc35-40b70b85eaa5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 16\\\\ndrwxr-xr-x  2 root root   79 May 15 21:35 .\\\\ndrwxr-xr-x 13 root root 4096 May 15 21:34 ..\\\\n-rw-r--r--  1 root root 2806 May 15 21:34 analysis_unified_rho.json\\\\n-rw-r--r--  1 root root 5116 May 15 21:35 paper_impact_list.md\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  2 root root   79 May 15 21:35 .\\ndrwxr-xr-x 13 root root 4096 May 15 21:34 ..\\n-rw-r--r--  1 root root 2806 May 15 21:34 analysis_unified_rho.json\\n-rw-r--r--  1 root root 5116 May 15 21:35 paper_impact_list.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

全部完成。产出：

**本地**: `artifacts/rho_paper_impact_list.md` (详细版，269 行)
**服务器**: `/root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/` 下:
- `paper_impact_list.md` (精简版)
- `analysis_unified_rho.json` (已同步)

核心结论：

1. **论文核心贡献（correlation-selection gap）不受影响** — 基于 SciERC N=8，不在修正范围内
2. **主要影响在 appendix**: tab:robustness (LLaMA CoNLL N=16 全部 5 signal 偏低 ~0.015)、tab:n-scaling (FK N-scaling 可能从 +0.030 降至 +0.005)
3. **FK N-scaling claim 可能失效** — seed456 FK 从 0.345→0.272，是唯一可能受实质影响的 claim
4. **Structural advantage over LP 反而加强** — 统一管道下 SJ-LP Δ 从 +0.153 增至 ~+0.170
5. **关键缺口**: JSON 不含 N=8 数据和 seed123，Table 1 (N=8 LLaMA CoNLL) 及多处正文引用需用统一管道补算后才能确定是否需更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "uuid": "1c149567-d37c-43a4-8215-7a064e06a473",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUALYVJ4u5NzT1Qx3qAiow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 97308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 330
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

_source line 58_

全部完成。产出：

**本地**: `artifacts/rho_paper_impact_list.md` (详细版，269 行)
**服务器**: `/root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/` 下:
- `paper_impact_list.md` (精简版)
- `analysis_unified_rho.json` (已同步)

核心结论：

1. **论文核心贡献（correlation-selection gap）不受影响** — 基于 SciERC N=8，不在修正范围内
2. **主要影响在 appendix**: tab:robustness (LLaMA CoNLL N=16 全部 5 signal 偏低 ~0.015)、tab:n-scaling (FK N-scaling 可能从 +0.030 降至 +0.005)
3. **FK N-scaling claim 可能失效** — seed456 FK 从 0.345→0.272，是唯一可能受实质影响的 claim
4. **Structural advantage over LP 反而加强** — 统一管道下 SJ-LP Δ 从 +0.153 增至 ~+0.170
5. **关键缺口**: JSON 不含 N=8 数据和 seed123，Table 1 (N=8 LLaMA CoNLL) 及多处正文引用需用统一管道补算后才能确定是否需更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 503719,
  "duration_api_ms": 502619,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "bb6876e6-19f7-4a9e-9822-d639fb7e36ea",
  "total_cost_usd": 1.704795,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 99512,
    "cache_read_input_tokens": 727780,
    "output_tokens": 28694,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 99512,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 389,
        "cache_read_input_tokens": 97308,
        "cache_creation_input_tokens": 330,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 330
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1450,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00153,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 28694,
      "cacheReadInputTokens": 727780,
      "cacheCreationInputTokens": 99512,
      "webSearchRequests": 0,
      "costUSD": 1.7032650000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2ea61fd-d0a7-4c59-9eb9-ec86a546f936"
}
```

</details>

---
