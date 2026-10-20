# paper page compression 8p

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 118
- **Recorded user turns:** 0
- **Tool calls:** 47
- **Original source:** `logs/workers/worker_paper_page-compression-8p_20260514T123440.log`
- **Structured JSON:** [`3913ab4e4f19b63ec9f4.json`](../../sessions/39/3913ab4e4f19b63ec9f4.json)

## Before a recorded user message

118 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "d9e2cc98-109c-4574-afa4-36f399300bf7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778778600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "31084f96-d21a-46d5-9064-689811e564f6",
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the paper tex files to understand the current state before making any changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "6edfe3af-da4f-4034-af44-5e40880b1a41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

I'll read all the tex files first to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "7928227c-6cb7-4529-9c97-f341f03f76f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

<details open><summary>🔧 Tool call — Read · `toolu_01BfvzHhShkrwtz35cB9xvMS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "be3de9c2-6581-48df-9bb3-22a576f34bdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 7 · 2026-05-14T12:34:51.714Z_

<details><summary>↩ Tool result · `toolu_01BfvzHhShkrwtz35cB9xvMS`</summary>

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{analysis}
37	\input{discussion}
38	\input{conclusion}
39	
40	\bibliography{references}
41	
42	\appendix
43	\input{appendix}
44	\input{appendix_results}
45	\input{appendix_disc_analysis}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "bd68964f-62be-4e54-b173-8ca5dc63eecb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_results}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01YAh9uNnswjcwwr3NiM4tEE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "1a6ae195-6d18-43a8-a800-bb9b2c0842b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 9 · 2026-05-14T12:34:52.191Z_

<details><summary>↩ Tool result · `toolu_01YAh9uNnswjcwwr3NiM4tEE`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "adb04512-55b7-4499-ad39-3e70e8ce2865",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01R4nMhPbaLRabHScxpmqH2t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "ad37009f-fb37-4b2b-9191-d7240a6d90ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 11 · 2026-05-14T12:34:52.662Z_

<details><summary>↩ Tool result · `toolu_01R4nMhPbaLRabHScxpmqH2t`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:results}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:analysis}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	The remainder of this paper is organized as follows: \S\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \S\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \S\ref{sec:experimental-setup} describes our experimental setup; \S\ref{sec:results} presents the main results; \S\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \S\ref{sec:discussion} discusses implications and limitations.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "57eca83d-08dd-4b24-a0e0-299f4d87af9e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon2023vllm, pope2023efficiently}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita2019heads, michel2019sixteen}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01EAyx1jkojYdyrgRFgvibEd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "64df4d7d-a153-4534-b822-61eddc223e86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 13 · 2026-05-14T12:34:53.142Z_

<details><summary>↩ Tool result · `toolu_01EAyx1jkojYdyrgRFgvibEd`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	Combining multiple compression axes produces non-additive errors.
5	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity; \cite{unicomp-2026} show that reasoning capabilities degrade disproportionately under compound compression. \cite{phase-transition-compression-2026} characterize per-dimension phase transitions whose joint safe region is the intersection of individual safe zones.  These works establish compound interaction but assume interaction magnitude is constant across generation---not modulated by reasoning phase or eviction strategy.
6	
7	Most KV cache eviction methods rely on importance scoring. Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses the cache from a prompt-end observation window; \cite{defensivekv-iclr2026} show standard aggregation is fragile with worst-case loss $2.3$--$4.3{\times}$ higher than expected. \cite{nacl-acl2024} combine proxy-token and random eviction to counteract attention bias. RetentiveKV~\cite{retentivekv-2026} identifies deferred importance---tokens with low initial salience becoming pivotal later---while \cite{greedy-bias-kvcache-2026} show any single importance metric exhibits greedy bias. A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized by aggregation functions or metric choice---not reasoning phase or concurrent head pruning.
8	
9	Several concurrent works introduce phase-awareness into LLM inference. ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction; \cite{decision-repr-transition-2026} discover that pruning sensitivity depends on silent vs.\ decisive representation phases; \cite{doing-more-with-less-2026} show sparsity can interact constructively with extended reasoning. These works examine either phase-aware single-axis compression or compound compression without phase conditioning. Our work bridges this gap by quantifying how compound severity varies across reasoning phases and is modulated by eviction strategy.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "2ddbb640-9b01-4dfe-b322-d44b0fc3b95b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity; \\cite{unicomp-2026} show that reasoning capabilities degrade disproportionately under compound compression. \\cite{phase-transition-compression-2026} characterize per-dimension phase transitions whose joint safe region is the intersection of individual safe zones.  These works establish compound interaction but assume interaction magnitude is constant across generation---not modulated by reasoning phase or eviction strategy.\n\nMost KV cache eviction methods rely on importance scoring. Ada-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses the cache from a prompt-end observation window; \\cite{defensivekv-iclr2026} show standard aggregation is fragile with worst-case loss $2.3$--$4.3{\\times}$ higher than expected. \\cite{nacl-acl2024} combine proxy-token and random eviction to counteract attention bias. RetentiveKV~\\cite{retentivekv-2026} identifies deferred importance---tokens with low initial salience becoming pivotal later---while \\cite{greedy-bias-kvcache-2026} show any single importance metric exhibits greedy bias. A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized by aggregation functions or metric choice---not reasoning phase or concurrent head pruning.\n\nSeveral concurrent works introduce phase-awareness into LLM inference. ThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction; \\cite{decision-repr-transition-2026} discover that pruning sensitivity depends on silent vs.\\ decisive representation phases; \\cite{doing-more-with-less-2026} show sparsity can interact constructively with extended reasoning. These works examine either phase-aware single-axis compression or compound compression without phase conditioning. Our work bridges this gap by quantifying how compound severity varies across reasoning phases and is modulated by eviction strategy.\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Vy6UojhGz7wtbu8yf5FNdo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "f71d952e-9d02-4142-84f5-c9a44cf2d5a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 15 · 2026-05-14T12:34:54.084Z_

<details><summary>↩ Tool result · `toolu_01Vy6UojhGz7wtbu8yf5FNdo`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer with $L$ layers and $H$ heads per layer. Let $s \in (0,1)$ denote a unified sparsity budget.
14	
15	\paragraph{Attention head pruning.}
16	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
17	\begin{equation}
18	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
19	    \label{eq:head-mask}
20	\end{equation}
21	
22	\paragraph{KV cache eviction.}
23	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
24	\begin{equation}
25	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
26	    \label{eq:kv-mask}
27	\end{equation}
28	We compare two strategies for constructing $\mathbf{m}_k$:
29	\begin{itemize}[nosep,leftmargin=*]
30	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
31	    \begin{equation}
32	        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
33	        \label{eq:kv-importance}
34	    \end{equation}
35	    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
36	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
37	\end{itemize}
38	
39	\paragraph{Compound sparsity.}
40	Applying both mechanisms simultaneously yields \emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
41	
42	\subsection{Interaction Index}
43	\label{sec:interaction-index}
44	
45	For a text segment, let $r_c = \text{PPL}_c / \text{PPL}_d$ denote the relative perplexity degradation under condition $c \in \{a\text{(attn-only)}, k\text{(kv-only)}, b\text{(both)}\}$. The Interaction Index is:
46	\begin{equation}
47	    \mathrm{II} = r_b - r_a - r_k + 1.
48	    \label{eq:ii}
49	\end{equation}
50	
51	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.
52	
53	\paragraph{Severity gradient.}
54	To capture how II varies across reasoning phases (defined in \S\ref{sec:phase-segmentation}), we define the \emph{severity gradient}:
55	\begin{equation}
56	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
57	    \label{eq:gradient}
58	\end{equation}
59	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.
60	$G \gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \approx 1$ indicates phase-invariant degradation.
61	When $\widetilde{\mathrm{II}}_{\,\textit{high}} < \varepsilon$ for a small threshold $\varepsilon > 0$, we report $G = \infty$.
62	
63	\subsection{Phase Segmentation}
64	\label{sec:phase-segmentation}
65	
66	We partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \cite{thinkv-iclr2026}.
67	
68	\paragraph{Attention sparsity.}
69	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
70	\begin{equation}
71	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
72	    \label{eq:attn-sparsity}
73	\end{equation}
74	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads.
75	
76	\paragraph{Quantile-based segmentation.}
77	Tokens are partitioned into \textbf{high-}, \textbf{mid-}, and \textbf{low-sparsity} phases by the tercile boundaries of $\{\sigma_i\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d22d1741-59f7-4fbb-96ca-8bcbe6a9f706",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer with $L$ layers and $H$ heads per layer. Let $s \\in (0,1)$ denote a unified sparsity budget.\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields \\emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by the tercile boundaries of $\\{\\sigma_i\\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01AadDbuWHqVedSGxoLckZLg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d824b4ee-a0cb-42a5-87d3-c53fcf143846",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 17 · 2026-05-14T12:34:54.572Z_

<details><summary>↩ Tool result · `toolu_01AadDbuWHqVedSGxoLckZLg`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA). \textbf{DeepSeek-R1-Distill-Qwen-7B} \cite{deepseek-r1}, distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. \textbf{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides cross-model replication with standard instruction tuning rather than reasoning distillation.
8	Both models are loaded in \texttt{bfloat16} with eager attention to permit direct manipulation of attention matrices.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B; \texttt{bfloat16} eliminated all occurrences.}
9	
10	
11	\subsection{Dataset}
12	\label{sec:dataset}
13	
14	We evaluate on a 50-problem stratified subset of MATH-500 \cite{math500}, sampling uniformly across problem categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
15	
16	
17	\subsection{Configuration and Metrics}
18	\label{sec:config-metrics}
19	
20	We apply symmetric compound sparsity: for level $s \in \{0.15, 0.20, 0.25, 0.30\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\ref{eq:kv-importance}; BOS always retained) against a \textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.
21	
22	Each sequence is segmented into three reasoning phases using the quantile-based method of \S\ref{sec:phase-segmentation} ($\texttt{min\_phase\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\ref{eq:ii}) and severity gradient (Eq.~\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\ref{app:stat-validation-details}.\footnote{Experiments were conducted on 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "13fbfd85-f14a-44dc-90de-955dcea41ecf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA). \\textbf{DeepSeek-R1-Distill-Qwen-7B} \\cite{deepseek-r1}, distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. \\textbf{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides cross-model replication with standard instruction tuning rather than reasoning distillation.\nBoth models are loaded in \\texttt{bfloat16} with eager attention to permit direct manipulation of attention matrices.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B; \\texttt{bfloat16} eliminated all occurrences.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of MATH-500 \\cite{math500}, sampling uniformly across problem categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\n\\subsection{Configuration and Metrics}\n\\label{sec:config-metrics}\n\nWe apply symmetric compound sparsity: for level $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.\n\nEach sequence is segmented into three reasoning phases using the quantile-based method of \\S\\ref{sec:phase-segmentation} ($\\texttt{min\\_phase\\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\\ref{eq:ii}) and severity gradient (Eq.~\\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\\ref{app:stat-validation-details}.\\footnote{Experiments were conducted on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01Mt7eywvZisBkdmeC4dLkoj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "21ca132c-7309-42b9-8d7d-7017605f3d09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 19 · 2026-05-14T12:34:55.047Z_

<details><summary>↩ Tool result · `toolu_01Mt7eywvZisBkdmeC4dLkoj`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity (C1)}
6	\label{sec:strategy-severity}
7	
8	The compound severity difference reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the median compound severity difference $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.
26	
27	
28	\subsection{Phase-Modulated Amplification (C2)}
29	\label{sec:phase-amplification}
30	
31	Decomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \S\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.
32	
33	Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \approx 0.9$--$1.7{\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
34	
35	\begin{table*}[t]
36	\centering
37	\small
38	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ is the median severity difference. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$ quantifies phase-dependent amplification.}
39	\label{tab:main-results}
40	\begin{tabular}{@{}llccccr@{}}
41	\toprule
42	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
43	\midrule
44	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\ % exp_id: bf16_importance_s015
45	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\ % exp_id: bf16_ds_rand_s015
46	\addlinespace
47	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\ % exp_id: bf16_importance_s020
48	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\ % exp_id: bf16_ds_rand_s020
49	\addlinespace
50	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\ % exp_id: bf16_importance_s025
51	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\ % exp_id: bf16_ds_rand_s025
52	\addlinespace
53	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\ % exp_id: bf16_importance_s030
54	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\ % exp_id: bf16_ds_rand_s030
55	\bottomrule
56	\end{tabular}
57	\end{table*}
58	
59	The gradient growth is sub-exponential: successive ratios of the median severity difference $\Delta$ between adjacent sparsity levels are $3.8{\times}$, $4.8{\times}$, and $2.0{\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\times}$, $2.2{\times}$, and $1.2{\times}$. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
60	
61	\begin{figure}[t]
62	\centering
63	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
64	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$, while random eviction (dashed) remains flat near $1{\times}$. Shaded regions denote 95\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
65	\label{fig:hero}
66	\end{figure}
67	
68	We report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\Delta = 22.94$ vs.\ median $\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\S\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586
69	
70	
71	\subsection{Phase-Strategy Crossover (C3)}
72	\label{sec:crossover}
73	
74	The phase-modulated gradient produces a striking qualitative phenomenon: a \emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{high}} = 0.032$ vs.\ $0.818$), but a higher II in the low-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{low}} = 7.196$ vs.\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
75	
76	Figure~\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
81	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28
82	\label{fig:crossover}
83	\end{figure}
84	
85	The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\S\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \emph{higher} compound severity than the explicitly random baseline.
86	
87	The crossover is present at all four tested sparsity levels ($s \geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\times}$ at $s{=}0.15$ to $5.4{\times}$ at $s{=}0.20$, before moderating to $3.6{\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62
88	
89	
90	\subsection{Cross-Model Replication (C5)}
91	\label{sec:cross-model}
92	
93	To assess generalization, we replicate importance-based eviction experiments on Qwen2.5-7B-Instruct, which shares the Qwen2 backbone but uses standard instruction tuning instead of reasoning distillation ($n{=}46$ valid problems after excluding degenerate phase assignments). Table~\ref{tab:cross-model} compares the median severity difference across both models.
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Cross-model replication: median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) under importance-based eviction.}
99	\label{tab:cross-model}
100	\begin{tabular}{@{}lcccc@{}}
101	\toprule
102	Model & \footnotesize $s{=}0.15$ & \footnotesize $s{=}0.20$ & \footnotesize $s{=}0.25$ & \footnotesize $s{=}0.30$ \\
103	\midrule
104	DeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json
105	Qwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json; 0.234979 rounds to 0.23 at 2dp
106	\bottomrule
107	\multicolumn{5}{@{}p{\columnwidth}@{}}{\footnotesize Both models share the Qwen2 architecture but differ in training (distillation vs.\ instruction tuning). DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}
108	\end{tabular}
109	\end{table}
110	
111	Qwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\ref{tab:cross-model}), paralleling DeepSeek's trajectory at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \to 0.80$; Qwen: $0.28 \to 1.02$; Table~\ref{tab:cohens-d}), with Spearman $\rho = 1.0$ between the four-point sequences (gradient permutation $p = 0.043$). % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
112	Full per-problem concordance analysis and random eviction controls appear in Appendix~\ref{app:cross-model-details}.
113	
114	The replication suggests that the phase-modulated severity gradient is an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning, not an artifact of DeepSeek's distillation-induced phase structure. Generalization to other architectures remains an open question (\S\ref{sec:limitations}).
115	
116	
117	\subsection{Statistical Validation (C6)}
118	\label{sec:stat-validation}
119	
120	All four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\text{Bonf}} < 0.005$). Paired effect sizes ($d_z$) grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Table~\ref{tab:cohens-d} reports full $d_z$ values and bootstrap CIs; details in Appendix~\ref{app:stat-validation-details}.
121	
122	\begin{table}[t]
123	\centering
124	\small
125	\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$).}
126	\label{tab:cohens-d}
127	\begin{tabular}{@{}lcccc@{}}
128	\toprule
129	$s$ & DS $d_z$ & $\widetilde{\Delta}$ [CI] & QW $d_z$ & $\widetilde{\Delta}$ [CI] \\
130	\midrule
131	0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
132	0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
133	0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
134	0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
135	\bottomrule
136	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.}
137	\end{tabular}
138	\end{table}
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e49745fa-7fb4-4e5a-8ba7-a4fbcd3b7094",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe compound severity difference reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the median compound severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ is the median severity difference. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe gradient growth is sub-exponential: successive ratios of the median severity difference $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\\times}$, $2.2{\\times}$, and $1.2{\\times}$. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$, while random eviction (dashed) remains flat near $1{\\times}$. Shaded regions denote 95\\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\\Delta = 22.94$ vs.\\ median $\\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is present at all four tested sparsity levels ($s \\geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\\times}$ at $s{=}0.15$ to $5.4{\\times}$ at $s{=}0.20$, before moderating to $3.6{\\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess generalization, we replicate importance-based eviction experiments on Qwen2.5-7B-Instruct, which shares the Qwen2 backbone but uses standard instruction tuning instead of reasoning distillation ($n{=}46$ valid problems after excluding degenerate phase assignments). Table~\\ref{tab:cross-model} compares the median severity difference across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & \\footnotesize $s{=}0.15$ & \\footnotesize $s{=}0.20$ & \\footnotesize $s{=}0.25$ & \\footnotesize $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json\nQwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json; 0.234979 rounds to 0.23 at 2dp\n\\bottomrule\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize Both models share the Qwen2 architecture but differ in training (distillation vs.\\ instruction tuning). DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}\n\\end{tabular}\n\\end{table}\n\nQwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\\ref{tab:cross-model}), paralleling DeepSeek's trajectory at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$; Table~\\ref{tab:cohens-d}), with Spearman $\\rho = 1.0$ between the four-point sequences (gradient permutation $p = 0.043$). % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\nFull per-problem concordance analysis and random eviction controls appear in Appendix~\\ref{app:cross-model-details}.\n\nThe replication suggests that the phase-modulated severity gradient is an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning, not an artifact of DeepSeek's distillation-induced phase structure. Generalization to other architectures remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation (C6)}\n\\label{sec:stat-validation}\n\nAll four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired effect sizes ($d_z$) grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Table~\\ref{tab:cohens-d} reports full $d_z$ values and bootstrap CIs; details in Appendix~\\ref{app:stat-validation-details}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 139,
      "startLine": 1,
      "totalLines": 139
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_019QFBDNn6fwxMD5yoM4fypG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "1ba18cde-d55f-41f6-bc1d-aae87d17e943",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 21 · 2026-05-14T12:34:55.530Z_

<details><summary>↩ Tool result · `toolu_019QFBDNn6fwxMD5yoM4fypG`</summary>

```text
1	
2	\section{Analysis: Mechanisms of Phase-Modulated Severity}
3	\label{sec:analysis}
4	
5	Why is compound severity phase-modulated for importance-based but not random eviction? We identify \emph{discrimination collapse} as the primary mechanism, with a secondary entropy redistribution effect that is model-dependent.
6	
7	\subsection{Discrimination Collapse Under Head Pruning}
8	\label{sec:discrimination-collapse}
9	
10	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across surviving heads. Head pruning makes the cumulative importance distribution more uniform, reducing the gap between highly-attended and rarely-attended positions. We measure this via the \textbf{Gini coefficient} (inequality of importance scores) and \textbf{coefficient of variation} (CV).
11	
12	Table~\ref{tab:discrimination-metrics} shows consistent negative deltas across both models and all sparsity levels: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$ under importance-based eviction. The same pattern holds under random eviction, confirming discrimination collapse is a consequence of head pruning \emph{per se}.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Discrimination collapse: $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction. Negative = reduced discriminative power.}
17	\label{tab:discrimination-metrics}
18	\small
19	\begin{tabular}{llrr}
20	\toprule
21	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
22	\midrule
23	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
24	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
25	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
26	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
27	\midrule
28	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
29	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
30	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
31	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
32	\bottomrule
33	\end{tabular}
34	\end{table}
35	
36	When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: importance-based eviction degenerates toward arbitrary selection. The crossover in \S\ref{sec:crossover} is thus an emergent consequence of head pruning degrading importance scoring conditioned on phase-dependent attention structure. Random eviction, whose decisions are independent of score quality, is immune---explaining its flat severity gradient.
37	
38	\subsection{Entropy Redistribution}
39	\label{sec:entropy-redistribution}
40	
41	Head pruning also redistributes attention entropy of surviving heads, but this effect is model-dependent: DeepSeek shows consistent negative entropy shifts ($\Delta\mathcal{H} \in [-0.040, -0.047]$), while Qwen exhibits a sign reversal at $s{=}0.25$. The partial replication suggests discrimination collapse alone is sufficient to explain the phase-strategy interaction; entropy redistribution may amplify the effect where it co-occurs but is not the primary driver. Details in Appendix~\ref{app:entropy-redistribution}.
42	
43	\subsection{Implications}
44	\label{sec:analysis-implications}
45	
46	Discrimination collapse depends on attention-mass-based importance scoring and sufficient head pruning---properties shared by major KV compression methods (H$_2$O \cite{h2o2024}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv2024}). The flat random baseline ($G \approx 1$) shows that phase-modulated severity is not inherent to compound sparsity but an emergent phase-strategy interaction, suggesting a phase-aware controller could mitigate it by adjusting the eviction budget per phase.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "23fc2555-99fb-496d-ad70-eb95a5241b91",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\n\\section{Analysis: Mechanisms of Phase-Modulated Severity}\n\\label{sec:analysis}\n\nWhy is compound severity phase-modulated for importance-based but not random eviction? We identify \\emph{discrimination collapse} as the primary mechanism, with a secondary entropy redistribution effect that is model-dependent.\n\n\\subsection{Discrimination Collapse Under Head Pruning}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across surviving heads. Head pruning makes the cumulative importance distribution more uniform, reducing the gap between highly-attended and rarely-attended positions. We measure this via the \\textbf{Gini coefficient} (inequality of importance scores) and \\textbf{coefficient of variation} (CV).\n\nTable~\\ref{tab:discrimination-metrics} shows consistent negative deltas across both models and all sparsity levels: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$ under importance-based eviction. The same pattern holds under random eviction, confirming discrimination collapse is a consequence of head pruning \\emph{per se}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse: $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction. Negative = reduced discriminative power.}\n\\label{tab:discrimination-metrics}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: importance-based eviction degenerates toward arbitrary selection. The crossover in \\S\\ref{sec:crossover} is thus an emergent consequence of head pruning degrading importance scoring conditioned on phase-dependent attention structure. Random eviction, whose decisions are independent of score quality, is immune---explaining its flat severity gradient.\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nHead pruning also redistributes attention entropy of surviving heads, but this effect is model-dependent: DeepSeek shows consistent negative entropy shifts ($\\Delta\\mathcal{H} \\in [-0.040, -0.047]$), while Qwen exhibits a sign reversal at $s{=}0.25$. The partial replication suggests discrimination collapse alone is sufficient to explain the phase-strategy interaction; entropy redistribution may amplify the effect where it co-occurs but is not the primary driver. Details in Appendix~\\ref{app:entropy-redistribution}.\n\n\\subsection{Implications}\n\\label{sec:analysis-implications}\n\nDiscrimination collapse depends on attention-mass-based importance scoring and sufficient head pruning---properties shared by major KV compression methods (H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv2024}). The flat random baseline ($G \\approx 1$) shows that phase-modulated severity is not inherent to compound sparsity but an emergent phase-strategy interaction, suggesting a phase-aware controller could mitigate it by adjusting the eviction budget per phase.\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01WCKp7uTtjkAKnRvCnNfVtn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "ce14c1d8-80bf-4586-905d-3f874b589f2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 23 · 2026-05-14T12:34:55.989Z_

<details><summary>↩ Tool result · `toolu_01WCKp7uTtjkAKnRvCnNfVtn`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$69$--$274{\times}$ amplification across sparsity levels (Table~\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.
10	A reviewer expecting a $2$--$3\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.
11	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment outside the main four-level range, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
13	Third, and most strikingly, a \emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\ $0.818$) yet \emph{underperforms} in low-sparsity phases ($7.196$ vs.\ $1.363$---a ${>}5{\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363
14	The same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''
15	% REVIEWER-ATTACK: "The qualitative direction is trivially expected from attention entropy arguments."
16	% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.
17	
18	\paragraph{Random masking as a falsification control.}
19	The random eviction baseline provides a decisive test against the ``trivially expected'' objection.
20	If compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.
21	It does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)
22	The absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.
23	
24	\paragraph{Cross-model replication and magnitude asymmetry.}
25	The phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of paired $d_z$ effect sizes across sparsity levels is $\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043
26	All eight paired Wilcoxon tests (4 sparsity levels $\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.
27	
28	The \emph{magnitude} of the effect, however, differs substantially.
29	Qwen's median severity differences ($0.04 \to 0.23 \to 1.27 \to 2.94$) are approximately one-fifth of DeepSeek's ($0.39 \to 1.48 \to 7.16 \to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (paired $d_z{=}0.44$), while Qwen's becomes clearly significant only at $s \geq 0.20$ ($d_z{=}0.55$; $s{=}0.15$ is borderline at $d_z{=}0.28$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds d_z: 0.4416,0.5195,0.6831,0.8031), cohens_d_bf16_qwen.json (qw d_z: 0.2811,0.5494,0.8894,1.0220).
30	The two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.
31	We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.
32	
33	\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}
34	The entropy-discrimination collapse hypothesis (\S\ref{sec:analysis}) receives partial cross-model support.
35	The discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.
36	However, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007
37	This divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.
38	We therefore characterize the mechanistic evidence as \emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.
39	
40	\paragraph{Implications for compound sparsity deployment.}
41	Our findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.
42	Compound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\S\ref{sec:analysis}) renders importance-based eviction unreliable.
43	A deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.
44	
45	This observation motivates \emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.
46	The severity gradient $G$ reported in \S\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \gg 1$ receive a reduced sparsity budget, while phases with $G \leq 1$ tolerate aggressive compression with minimal quality loss.
47	
48	\paragraph{Future directions.}
49	The phase-aware allocation principle above points toward a concrete system design: a \emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.
50	The controller would route each generation step through a low-overhead phase classifier (\S\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.
51	Whether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.
52	
53	A second direction concerns completing the mechanistic picture.
54	The discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\S\ref{sec:analysis}).
55	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.
56	
57	Finally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.
58	
59	\subsection{Limitations}
60	\label{sec:limitations}
61	
62	Our study is bounded by three principal constraints.
63	First, both models share the Qwen2ForCausalLM architecture; cross-architecture validation (e.g., LLaMA~3, Mistral) remains future work.
64	Second, evaluation is limited to MATH-500---different reasoning tasks may induce different phase structures and severity profiles.
65	Third, all experiments are conducted at the 7B scale; whether the phase-modulated severity patterns persist at larger scales is untested.
66	Extended limitations and anticipated reviewer concerns are discussed in Appendix~\ref{app:limitations}.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "cede6b76-660c-4c07-99ef-ce99b753b2a4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.\nWe do not dispute this intuition.\nThe surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.\n\nFirst, the \\emph{magnitude} of the severity gradient---$69$--$274{\\times}$ amplification across sparsity levels (Table~\\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.\nA reviewer expecting a $2$--$3\\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.\nSecond, the gradient is \\emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment outside the main four-level range, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\nThis asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.\nThird, and most strikingly, a \\emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \\emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\\ $0.818$) yet \\emph{underperforms} in low-sparsity phases ($7.196$ vs.\\ $1.363$---a ${>}5{\\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363\nThe same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''\n% REVIEWER-ATTACK: \"The qualitative direction is trivially expected from attention entropy arguments.\"\n% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.\n\n\\paragraph{Random masking as a falsification control.}\nThe random eviction baseline provides a decisive test against the ``trivially expected'' objection.\nIf compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.\nIt does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)\nThe absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.\n\n\\paragraph{Cross-model replication and magnitude asymmetry.}\nThe phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of paired $d_z$ effect sizes across sparsity levels is $\\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043\nAll eight paired Wilcoxon tests (4 sparsity levels $\\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.\n\nThe \\emph{magnitude} of the effect, however, differs substantially.\nQwen's median severity differences ($0.04 \\to 0.23 \\to 1.27 \\to 2.94$) are approximately one-fifth of DeepSeek's ($0.39 \\to 1.48 \\to 7.16 \\to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (paired $d_z{=}0.44$), while Qwen's becomes clearly significant only at $s \\geq 0.20$ ($d_z{=}0.55$; $s{=}0.15$ is borderline at $d_z{=}0.28$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds d_z: 0.4416,0.5195,0.6831,0.8031), cohens_d_bf16_qwen.json (qw d_z: 0.2811,0.5494,0.8894,1.0220).\nThe two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.\nWe conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.\n\n\\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) receives partial cross-model support.\nThe discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.\nHowever, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007\nThis divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.\nWe therefore characterize the mechanistic evidence as \\emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.\n\n\\paragraph{Implications for compound sparsity deployment.}\nOur findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.\nCompound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\\S\\ref{sec:analysis}) renders importance-based eviction unreliable.\nA deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.\n\nThis observation motivates \\emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.\nThe severity gradient $G$ reported in \\S\\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \\gg 1$ receive a reduced sparsity budget, while phases with $G \\leq 1$ tolerate aggressive compression with minimal quality loss.\n\n\\paragraph{Future directions.}\nThe phase-aware allocation principle above points toward a concrete system design: a \\emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.\nThe controller would route each generation step through a low-overhead phase classifier (\\S\\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.\nWhether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.\n\nA second direction concerns completing the mechanistic picture.\nThe discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\\S\\ref{sec:analysis}).\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.\n\nFinally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur study is bounded by three principal constraints.\nFirst, both models share the Qwen2ForCausalLM architecture; cross-architecture validation (e.g., LLaMA~3, Mistral) remains future work.\nSecond, evaluation is limited to MATH-500---different reasoning tasks may induce different phase structures and severity profiles.\nThird, all experiments are conducted at the 7B scale; whether the phase-modulated severity patterns persist at larger scales is untested.\nExtended limitations and anticipated reviewer concerns are discussed in Appendix~\\ref{app:limitations}.\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_019RnTpesaMHN2RmwA9AtHLu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "f860cb86-7797-4aff-bc6d-86ea3cd7d690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 25 · 2026-05-14T12:34:56.429Z_

<details><summary>↩ Tool result · `toolu_019RnTpesaMHN2RmwA9AtHLu`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.
5	
6	Our contributions, mapped to confirmed claims, are:
7	\begin{enumerate}[nosep,leftmargin=*]
8	    \item \textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d_z{=}{-}0.04$---has negligible effect size).
9	
10	    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large).
11	
12	    \item \textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
13	
14	    \item \textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.
15	
16	    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\sim}1/5$ of DeepSeek).
17	
18	    \item \textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.
19	\end{enumerate}
20	
21	\paragraph{Limitations.}
22	Both models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.
23	All experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.
24	We evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.
25	The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.
26	While discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.
27	
28	\paragraph{Future work.}
29	A \emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.
30	Cross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.
31	Direct measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "236ce4bb-8a3e-458b-849c-7263ffc891cc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d_z{=}{-}0.04$---has negligible effect size).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\nWhile discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01LcES2cCNWikEa5cTKXVtYK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "3ea7355c-8d0a-4f4f-8ad3-e011f41a6e91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 27 · 2026-05-14T12:34:57.390Z_

<details><summary>↩ Tool result · `toolu_01LcES2cCNWikEa5cTKXVtYK`</summary>

```text
1	\section{Multiplicative Null Verification}
2	\label{app:multiplicative-null}
3	
4	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
5	
6	\section{Bootstrap and Permutation Details}
7	\label{app:bootstrap-details}
8	
9	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.
10	
11	The permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\text{Bonf}} = 0.0032$).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e8288fe4-9f3e-49ee-af07-c0ab6d7f0c7b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n\\section{Bootstrap and Permutation Details}\n\\label{app:bootstrap-details}\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.\n\nThe permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \\geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$).\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01A5SvhE7EfFjcavde9XaT7t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "4c52e6ec-3b52-4baa-8dbe-e1a8e373146a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 29 · 2026-05-14T12:34:57.885Z_

<details><summary>↩ Tool result · `toolu_01A5SvhE7EfFjcavde9XaT7t`</summary>

```text
1	% Appendix sections for content moved from results.tex (§5.5 and §5.6)
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
7	
8	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}50$ for DeepSeek).
9	
10	\paragraph{Per-problem concordance.}
11	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json
12	
13	\paragraph{Random eviction control.}
14	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
19	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
20	\label{fig:cross-model}
21	\end{figure}
22	
23	
24	\section{Statistical Validation Details}
25	\label{app:stat-validation-details}
26	
27	\paragraph{Permutation test.}
28	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
29	
30	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
31	
32	\begin{table}[t]
33	\centering
34	\small
35	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
36	\label{tab:permutation}
37	\begin{tabular}{@{}rrcl@{}}
38	\toprule
39	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
40	\midrule
41	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference
42	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference
43	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference
44	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
54	\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}
55	\label{fig:permtest-forest}
56	\end{figure}
57	
58	\paragraph{Additional effect size analysis.}
59	For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
60	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "2ac4e59f-52d4-4e61-8410-b72b5e74092c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix sections for content moved from results.tex (§5.5 and §5.6)\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\n\\section{Statistical Validation Details}\n\\label{app:stat-validation-details}\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Additional effect size analysis.}\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01T6aXhMWbcGHrGBFFVNneZs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "26996dc3-8808-4807-883b-539c04bb2715",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UknhYNRN2wLxJvPdmqm5NW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14310,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14310
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

_source line 31 · 2026-05-14T12:34:58.188Z_

<details><summary>↩ Tool result · `toolu_01T6aXhMWbcGHrGBFFVNneZs`</summary>

```text
1	\section{Extended Limitations}
2	\label{app:limitations}
3	
4	\paragraph{Model scale.}
5	All experiments are conducted at the 7B parameter scale.
6	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
7	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
8	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
9	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
10	
11	\paragraph{Architectural scope.}
12	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
13	The cross-model replication (\S\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.
14	The entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.
15	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
16	% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.
17	
18	\paragraph{Task coverage.}
19	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
20	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
21	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
22	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
23	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
24	
25	\paragraph{Statistical scope.}
26	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
27	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
28	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
29	
30	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
31	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
32	
33	\paragraph{Sparsity range.}
34	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
35	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
36	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
37	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
38	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
39	
40	\paragraph{No throughput evaluation.}
41	This work focuses on characterizing the \emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.
42	We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.
43	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
44	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
45	
46	\section{Entropy Redistribution Analysis}
47	\label{app:entropy-redistribution}
48	
49	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
50	\begin{equation}
51	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
52	    \label{eq:attn-entropy}
53	\end{equation}
54	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
55	
56	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.040, -0.047]$; Table~\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek
57	This is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented in \S\ref{sec:discrimination-collapse}.
58	
59	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen
60	
61	The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}
66	\label{tab:entropy-deltas}
67	\small
68	\begin{tabular}{llr}
69	\toprule
70	Model & $s$ & $\Delta\mathcal{H}$ \\
71	\midrule
72	DeepSeek & $0.15$ & $-0.040$ \\
73	DeepSeek & $0.20$ & $-0.047$ \\
74	DeepSeek & $0.25$ & $-0.045$ \\
75	DeepSeek & $0.30$ & $-0.044$ \\
76	\midrule
77	Qwen & $0.15$ & $-0.073$ \\
78	Qwen & $0.20$ & $-0.076$ \\
79	Qwen & $0.25$ & $+0.045$ \\
80	Qwen & $0.30$ & $-0.007$ \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "4f4c7208-1170-4391-aa44-7b9c2a79b4d8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n\n\\section{Entropy Redistribution Analysis}\n\\label{app:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.040, -0.047]$; Table~\\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek\nThis is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented in \\S\\ref{sec:discrimination-collapse}.\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen\n\nThe $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of all the files. Let me plan the edits systematically according to the compression strategy. Let me track the work with TodoWrite and then execute each change.

Let me plan the changes:

1. **background.tex** (112→~45 lines): Keep II definition (Eq 1), severity gradient (Eq 2), phase segmentation core. Move compound sparsity formulation details, attention sparsity formula to appendix.

2. **analysis.tex** (61→~15 lines): Keep discrimination collapse table + 1 paragraph. Move entropy redistribution (§6.2) and implications (§6.3) to appendix. 

3. **results.tex** (154→~100 lines): Delete tab:aggregate-ii (redundant with tab:main-results). Move tab:cohens-d to appendix. Compress §5.1 and §5.5. I'll merge the analysis subsection into results as well.

4. **discussion.tex** (66→~35 lines): Delete Limitations subsection. Compress paragraphs.

5. **conclusion.tex** (30→shorter): Remove Limitations paragraph and Future work paragraph. Add \section*{Limitations} after conclusion.

6. **main.tex**: Remove \input{analysis} if merged into results, add appendix inputs.

7. Create appendix content for moved material.

Now I'm working through this systematically. Let me figure out what goes into the appendix: from background.tex, I need to move the compound sparsity formulation details and phase segmentation specifics, though I'll need to keep equation labels accessible since they're referenced elsewhere. From results.tex, the Cohen's d table moves to the appendix. I should also check what entropy redistribution analysis is already in the appendix and what additional implications need to be included.

Now I'm planning the specific edits. For background.tex, I'll keep the section header, the Interaction Index subsection with its core equations, and a brief mention of compound sparsity, but move the detailed formulation sections and phase segmentation details to the appendix. The tricky part is that eq:kv-importance is referenced in methodology.tex, so I need to make sure those cross-references still work when equations move. Let me trace through which background equations are cited elsewhere in the document. I've found a pre-existing bug where `discussion.tex` and `appendix_results.tex` reference `sec:phase-seg`, but the actual label in `background.tex` is `sec:phase-segmentation`. I'll proceed with moving the equations to the appendix while keeping their labels intact so references still work, then systematically rewrite each file starting with `background.tex` to keep only the core definitions and severity gradient, moving detailed formulations to a new appendix section. The file dependencies suggest I can work on `background.tex` and the appendix section in parallel with the other rewrites.

For the analysis section, I'm deciding to merge it as a subsection under Results rather than keep it standalone—this saves overhead and improves paper flow, even though the task allows either approach. Now I'm ready to execute all the edits file by file.

Starting with background.tex, I'll trim it to around 45 lines by keeping just the section header, a brief intro, the Interaction Index subsection with its key equations, and a short Phase Segmentation paragraph that references the appendix for details instead of including equations inline.

I'll need to create a new appendix section to hold the background material I'm removing from the main text. Then for results.tex, I'm removing the aggregate-II table and its surrounding text from §5.1, but I still need §5.1 itself for the first criterion—I'll just rewrite it to point to the main results table instead. The Cohen's d table will move as well.

Looking at the analysis section more carefully, I need to keep the discrimination collapse findings with its table and one summary paragraph explaining the consistent Gini/CV decline across models, but move the entropy redistribution subsection and the compound sparsity implications subsection entirely to the appendix. 现在我需要把 discrimination collapse 的表格和段落合并到 results.tex 中作为一个 subsection，然后把 implications 内容添加到 appendix_disc_analysis.tex。让我开始起草新的文件内容。

我正在定义 Interaction Index，它通过比较三种条件下的困惑度降级来量化注意力头修剪和 KV 缓存驱逐之间的相互作用——单独应用注意力修剪、单独应用缓存驱逐，以及同时应用两者——然后用一个公式来计算这个交互效应。

当指数为正时表示超加性降级，为零时表示独立性。由于分布右偏，我采用中位数来报告结果，并进一步定义了严重程度梯度来追踪这个指标在不同推理阶段的变化。

现在我需要描述如何将生成的序列分割成三个阶段——根据局部注意力稀疏性将位置分组，然后按三分位数边界划分为高、中、低稀疏度阶段。

短于10个token的片段会与相邻阶段合并。

Writing appendix section... I'm defining how to score positions for eviction based on their cumulative attention across all layers and heads, normalized by distance to account for the causal bias that favors recent tokens. Then I'm introducing a sparsity metric that measures what fraction of key positions receive negligible attention relative to each query's maximum attention weight.

Now I'm averaging the per-head sparsity scores across all attention heads to get a single sparsity value per position, then grouping tokens into three phases based on where they fall in the distribution of sparsity scores, with a minimum segment size of 10 tokens to avoid fragmentation.

For the results section, I need to restructure the document by removing the aggregate table and rewriting the strategy-dependent severity discussion to reference the main results table instead. The key finding is that importance-based eviction shows a dramatic 37-fold increase in severity difference across compression levels, while random eviction shows no systematic pattern—demonstrating that compound severity emerges from the interaction between compression and strategy rather than being inherent to compression itself. I should also move the Cohen's d table to the appendix, condense the statistical validation section, and add a new subsection on discrimination collapse. Generating LaTeX formatting...

When importance scores become less discriminative, importance-based eviction essentially becomes random selection, which explains why random eviction performs comparably at the crossover point—it's unaffected by score quality degradation. There's also a secondary entropy redistribution effect that varies by model, detailed in the appendix.

Now I'm thinking through the document structure more carefully. The current setup has analysis as a separate section that could be merged into results, which would shift the section numbering downstream. Let me map out what the final structure should look like: introduction through methodology stay as sections 1-4, results absorbs the analysis content as a subsection, discussion gets compressed and becomes the new section 6, and conclusion becomes section 7, with limitations as an unnumbered section at the end. The semantic labels in the references will handle the numbering automatically, so I just need to reorganize the file includes and content flow.

Now I'm going through each file to identify what needs trimming. The introduction has a standard roadmap paragraph at the end that's taking up space—I can either cut it or condense it significantly. The related work section is reasonably compact but could use some tightening. For methodology, I need to check if there's any redundancy with the background section, though from what I can see they cover different ground—background provides context while methodology describes the actual approach and setup.

Now I'm planning my execution strategy. Since some files need substantial rewrites while others just need minor adjustments, I'll use a complete rewrite for files like background and results where I'm restructuring content significantly, and targeted edits for the smaller changes. I'm mapping out the operations: background gets a full rewrite, results needs major restructuring, analysis will be mostly emptied with content moved elsewhere, discussion and conclusion need significant changes, while introduction and related work just need light trimming. I'll also need to add a new section to the appendix.

Let me start drafting the rewritten files, being careful to preserve all the numerical values and key definitions.

Writing background.tex... I'm defining the Interaction Index formula to quantify super-additive degradation when both attention and KV cache sparsity are applied together, where positive values indicate the combined effect exceeds the sum of individual effects. I'm also introducing a severity gradient metric that measures how this interaction varies across different reasoning phases, using normalized interaction index values at low and high extremes.

For the phase segmentation, I'm partitioning sequences into three regions based on attention sparsity patterns—computing per-position sparsity scores by measuring the fraction of negligible attention weights, then grouping tokens into tercile-based phases with a minimum segment size to avoid fragmentation.

Now moving to the results section, I'm presenting how compound severity varies dramatically with eviction strategy: under importance-based selection on DeepSeek-R1-Distill-Qwen-7B, the median severity gap grows 37× as sparsity increases from 0.15 to 0.30, whereas random eviction shows no comparable trend.

Looking at the phase-level breakdown, I'm finding that severity concentrates specifically in the low-sparsity reasoning phase, with the importance-based gradient scaling from 69× to 274× across the same sparsity range. Generating the results table... Generating the results table... The crossover phenomenon emerges at sparsity level 0.25, where importance-based eviction flips from underperforming random selection in the high-sparsity regime to substantially outperforming it in the low-sparsity regime—a strategic reversal that suggests the two approaches operate under fundamentally different constraints depending on the phase. Now I'm moving to cross-model validation by testing the same approach on Qwen2.5-7B-Instruct, which uses instruction tuning rather than reasoning distillation, across 46 valid problems. I'm comparing how median severity differences shift across different sparsity levels to see if the pattern holds. Looking at the performance comparison, Qwen shows the same monotonic gradient pattern but at roughly one-fifth the effect size. Both models demonstrate strictly increasing trajectories across sparsity levels with perfect correlation, though Qwen's effect only becomes statistically reliable at higher sparsity thresholds. Now I'm moving into the statistical validation section to confirm these differences hold up across all sparsity levels after multiple comparison correction. When importance scores become less discriminative after pruning, importance-based eviction essentially degenerates into random selection, which explains why the strategy fails at larger pruning rates—random eviction doesn't depend on score quality so it remains unaffected. I'm looking at the discrimination metrics table showing how Gini and coefficient of variation both decrease substantially across models under importance-based eviction, confirming this collapse effect. I'm tracking the page count more carefully now—the original was 154 lines, and I've removed several sections including two tables and compressed the discussion paragraphs significantly. Looking at how tables render in the two-column ACL format, full-width tables take up about 0.4 pages while single-column ones are closer to 0.3, so I need to account for that visual space rather than just line count when estimating the final length. page each
figure (single column) ≈ 0.3 page each

Current results section:
- tab:aggregate-ii (single col) ≈ 0.3 page
- tab:main-results (full width) ≈ 0.4 page
- fig:hero ≈ 0.3 page
- fig:crossover ≈ 0.3 page
- tab:cross-model ≈ 0.3 page
- tab:cohens-d ≈ 0.3 page
- Text ~50 lines ≈ 0.8 page
Total ≈ 2.7 pages

After changes:
- Remove tab:aggregate-ii: save 0.3 page
- Remove tab:cohens-d: save 0.3 page
- Add tab:discrimination-metrics: add 0.3 page
- Reduce text by ~20 lines: save 0.3 page
Net saving ≈ 0.6 page from results

That's still short of my 1 page target. But I'm also consolidating the analysis section—I'm keeping its table but cutting the text significantly, which frees up about 0.7 pages. So across both sections, I'm looking at roughly 1.3 pages of savings total.

Let me map out the full document to see where I stand:

- abstract: ~0.4 page
- introduction: ~0.7 page (33 lines)
- related work: ~0.6 page (39 lines)
- background: ~1.7 pages (112 lines with 5 equations)
- methodology: ~1.0 page (65 lines)
- results: ~2.1 pages (after cuts)
- analysis: ~0.3 page (after merging)
- discussion: ~1.1 pages (66 lines)
- conclusion: ~0.6 page (30 lines)
Total: ~8.5 pages

That gets me closer, but I still need to trim another 0.5 pages. I think the discussion section is where I can find that—it's a bit verbose and could be tightened without losing substance. I'm recalculating the page savings more carefully. After merging results and analysis sections, I'd save about a page total. The discussion can be trimmed from 66 to 35 lines for another half-page savings, while the conclusion needs only modest cuts since adding a Limitations section mostly offsets the compression. I'm checking the ACL 2026 guidelines more carefully—Limitations sections are indeed exempt from the page count, so moving it out of the conclusion works well. Looking at my savings estimates across sections, I should be able to trim about 3 pages total, bringing the draft down to roughly 6.8 pages, which gives me comfortable headroom under the 8-page limit. I still need to account for any appendix references I'm adding.

Now I'm going to start rewriting the files, beginning with the major compressions. For the discussion section, I'm drafting a much tighter version that keeps the key insights about phase-modulated severity and the quantitative findings but cuts the verbose framing.

Writing discussion section... The random masking control shows this amplification is strategy-specific rather than inherent to compression itself—only one of eight conditions shows phase modulation, and even that's negligible. Across both models, the phase-strategy interaction replicates perfectly with identical ordinal rankings, though Qwen's effect is about one-fifth the magnitude of DeepSeek's and kicks in at a higher sparsity threshold, which I suspect reflects how reasoning distillation sharpens internal phase transitions. Now I'm considering what this means for actual deployment practices. I'm seeing that compound severity isn't just a function of sparsity level—it emerges from how the model's phase strategy interacts with the sparsity setting, varying dramatically across a single generation. The data shows importance-based eviction creates massive phase-dependent severity differences, with the median impact increasing from 0.39 to 14.59 across phases, while random eviction shows no meaningful modulation. This crossover effect at certain sparsity levels where importance-based eviction simultaneously helps and hurts depending on the phase replicates across different model sizes, though with varying intensity.

The mechanism driving this appears to be discrimination collapse—when head pruning degrades the model's ability to distinguish important from unimportant components—which I can confirm across both models. These results fundamentally challenge the assumption that sparsity effects are phase-invariant and suggest we need phase-aware compression strategies for reasoning models.

However, there are important limitations: both models share the same architecture, so I'd need to test on different architectures like LLaMA or Mistral to validate generalization. The experiments are only at 7B scale, leaving open whether these severity gradients hold at larger model sizes. I'm also limited to MATH-500 for evaluation, and different reasoning tasks might produce different phase structures. The discrimination collapse mechanism is supported by correlational evidence, but I'd need direct causal validation through controlled entropy manipulation to be more confident. While the discrimination collapse pattern holds consistently, the entropy redistribution component only replicates in a subset of conditions. I'm verifying that all the key claims are covered in the compressed conclusion, and they are. Now I need to update the introduction since I'm merging the analysis section into results—the section reference to `sec:analysis` needs to be adjusted, though the label itself should still work since I'm keeping that content. I'll remove the roadmap line at the end of the introduction to tighten it up. I need to check how the methodology references background equations. The reference to the importance equation still works globally in LaTeX, but since that equation moved to the appendix, it feels awkward to cite it from the main text. I'll update the methodology section to reference the appendix directly instead of pointing to a specific equation. I'm realizing the background section already covers importance-based eviction, so I can leave that reference as is. But I've spotted some broken LaTeX references—`sec:phase-seg` should be `sec:phase-segmentation` in both discussion.tex and appendix_results.tex, and I need to update `sec:analysis` references in introduction.tex to point to `sec:discrimination-collapse` instead.

Now I'm checking whether `sec:analysis-implications` and `sec:entropy-redistribution` are actually referenced anywhere in the document, and it looks like they're either unused or have mismatched label names that need fixing.

Let me move on to trimming related_work.tex. The file is currently 39 lines but most of that is formatting—the actual content is just three paragraphs. I can compress the first paragraph on compound compression from 5 lines down to 4, and maybe trim some of the citations in the KV cache eviction section, while keeping the phase-aware paragraph as is. At 39 lines in the .tex file, this section takes up about half a page in the two-column ACL format, so there's room to tighten it up.

Now I need to reorganize the appendix. I'll add a new section for the compound sparsity formulation that I'm moving from background.tex, and it should go first since it's referenced in the background section. After that come the existing sections on multiplicative null verification and bootstrap details.

For appendix_results.tex, I need to append the coherence table.

Looking at appendix_disc_analysis.tex, the entropy redistribution subsection is already there in full, and the implications section from the main text is just a short paragraph. Since the task asks to move these into the appendix, I should add the implications content to the end of that file.

But reviewing the implications text more carefully—it's largely redundant with what's already in the Discussion section and the new discrimination collapse subsection in Results. I'll skip moving it since it doesn't add much value in the appendix.

Now I'm ready to execute the full restructuring. I need to rewrite four core files (background, results, discussion, conclusion) and make targeted edits to several others to remove the analysis section, integrate the compound formulation into the appendix, and update all the cross-references throughout the document. I need to verify the remaining equation references in methodology.tex, then decide how to handle the analysis.tex file since its content is being merged into results.tex. The `sec:analysis` label is still referenced elsewhere, so I'll need to remove the `\input{analysis}` from main.tex rather than keep a mostly empty file.

Looking through the document, introduction.tex has a reference to `sec:analysis` at line 29 that should point to `sec:discrimination-collapse` instead, and there's a roadmap line I'm removing. The other files don't seem to have lingering references to that section. Now I'll execute all the edits in batch—the major rewrites using Write operations and the smaller changes with Edit operations.

Actually, I should decide what to do with analysis.tex since I'm removing its `\input` from main.tex. I'll leave the file as-is on disk since it won't be compiled anyway, and just remove the input command.

Now I need to be strategic about batching these edits. Since I'm modifying different files, I can send all the Write and Edit calls in parallel. Let me finalize the content for each file now.

For appendix.tex, I need to prepend the new compound sparsity section before the existing multiplicative null verification section. For appendix_results.tex, I'll append the Cohen's d table after the current content that ends around line 61, which includes the cross-model replication details section.

Looking more carefully at the structure, the statistical validation details section already contains the permutation test results and forest plot, so the Cohen's d table fits naturally there. I'll add it at the end of appendix_results.tex, and I need to move the table from results.tex as-is.

Generating the Cohen's d table... Generating the results table...

Now I'm ready to execute the plan. Before I do, I should verify what needs to go into the appendix—specifically checking if sections 6.2 and 6.3 from the analysis need to be moved there, and reviewing what's currently in those sections.

Looking at section 6.2, it's just a brief pointer to the appendix, and the full content is already there, so nothing needs moving. Section 6.3 is a short implications paragraph about how discrimination collapse emerges from the interaction between attention-mass-based scoring and head pruning, and how a phase-aware controller could potentially address it. I'll add this concisely to the appendix.

Actually, reconsidering—this content is already captured in the new discrimination collapse subsection within results and expanded in the discussion, so adding it to the appendix would be redundant. I'll skip it.

Now let me execute the file writes. I should also check methodology.tex for overlap with the background section. The models, dataset, and configuration sections contain unique content, though there are some conceptual references like position-normalized cumulative attention and quantile-based phase segmentation that point back to background material—but these are just citations, not duplication.

The methodology section is already lean at 23 lines of actual content. For the equation references pointing to appendix material, I could either keep the LaTeX references (which will render as "Eq. A.3" etc.) or rephrase to point back to the background section where the concepts are introduced. I think it's cleaner to reference the background section directly since that's where the foundational definitions live.

Now I need to execute all the file operations. I'm organizing this into two groups: the complete rewrites of background, results, discussion, and conclusion sections, then the targeted edits to introduction, main, and the appendix files. The analysis.tex file can stay on disk since I'm just removing its input command from main.

tex.

Before I proceed with the batch operations, let me verify that my rewritten results section preserves all the numerical values correctly—checking the performance metrics, statistical measures, and speedup factors against the originals to ensure nothing's been altered. I'm verifying all the numerical values are preserved correctly across the files—checking metrics, ranges, and coefficients. Now I'm ready to write out the final LaTeX content carefully, starting with the background section where I'm introducing compound sparsity, the comparison between importance-based and random eviction strategies, and then moving into the interaction index framework.

For the interaction index itself, I'm defining the relative perplexity degradation metric across three conditions—attention-only, KV-only, and both applied together—then computing the interaction index formula to detect whether the combined effect is super-additive, additive, or sub-additive. I'm using an additive null model and reporting medians since the distributions are right-skewed.

Now I'm introducing a severity gradient metric to measure how the interaction index varies between low-sparsity and high-sparsity phases, where a high gradient value indicates the compound interaction concentrates in low-sparsity regions while a value near 1 suggests the degradation is consistent across phases. Next I need to describe how the sequences are partitioned into these different phases.

To segment each sequence, I'm computing a sparsity score for each token position by measuring the fraction of key positions that receive negligible attention across all heads, then dividing tokens into three groups based on tercile boundaries—with short segments merged into adjacent phases for stability.

Now I'm presenting the empirical results, showing how compound severity scales dramatically with eviction strategy: importance-based eviction exhibits a 37× amplification in median severity difference as compression increases from 15% to 30%, while random eviction shows no systematic growth, revealing that severity emerges from the interaction between compression level and strategy rather than being inherent to compression itself.

Breaking down the results by reasoning phase, I find that severity concentrates almost entirely in the low-sparsity phase where the model performs exploratory reasoning with distributed attention patterns. The severity gradient under importance-based eviction climbs from 69× to 274× across the same compression range, while the high-sparsity phase remains nearly unaffected, and random eviction shows no phase-dependent amplification. Generating the results table... Generating markdown table...

The gradient growth follows a sub-exponential pattern with successive ratios of 3.8×, 4.8×, and 2.0× across sparsity levels, showing a decreasing growth rate that suggests saturation. I'm including a figure that visualizes this trajectory, comparing how importance-based eviction scales dramatically from 69× to 274× while random eviction stays flat around 1×.

Now I'm examining a phase-modulated crossover effect: at sparsity 0.25, importance-based eviction actually performs worse than random in high-sparsity phases but better in low-sparsity phases—a complete reversal in which strategy is superior. This happens because focused attention preserves importance scores when sparsity is high, but head pruning degrades them when sparsity is low. Now I'm looking at the cross-model replication results on Qwen2.5-7B-Instruct, which uses instruction tuning rather than reasoning distillation, and comparing the median severity differences across sparsity levels with the DeepSeek-R1-7B baseline. Now I'm looking at the performance metrics across different sparsity levels. Qwen shows a similar monotonic pattern to DeepSeek but at roughly one-fifth the magnitude, with both models displaying strictly increasing trajectories and perfect correlation. The effect becomes statistically significant at higher sparsity thresholds, and I'm noting that all four sparsity levels pass the permutation tests with Bonferroni correction applied.

The pruning mechanism appears to flatten the distribution of key-value importance across attention heads—what I'm calling a discrimination collapse—which directly accounts for why the interaction between pruning phase and strategy emerges. Both models show consistent reductions in the Gini coefficient, indicating this uniformity effect is robust across architectures. Generating the discrimination metrics table... The quantitative findings are what's striking here—the severity gradient spans nearly three orders of magnitude, and the interaction effect concentrates sharply in low-sparsity regimes while vanishing in high-sparsity phases. What really stands out is the crossover behavior itself: importance-based eviction flips from better to worse depending on the phase, which can't be explained by simple entropy arguments alone. Random masking serves as a useful control to test whether this amplification is specific to importance-based methods or inherent to compression generally.

The results are clear: random eviction shows no meaningful phase modulation across nearly all conditions, with one minor exception that has negligible effect size, confirming the amplification is strategy-specific rather than a general compression artifact. The phase-strategy interaction replicates consistently across models with perfect rank correlation, though Qwen exhibits roughly one-fifth the magnitude of DeepSeek's effect and requires higher sparsity thresholds to trigger the same behavior.

I suspect the reasoning distillation process creates sharper internal phase transitions that amplify this interaction. For practical deployment, uniform compression budgets don't work well for reasoning models since the severity concentrates in low-sparsity phases where importance-based pruning becomes unreliable. A phase-aware approach that allocates lower sparsity to vulnerable phases and reclaims capacity elsewhere could preserve compression gains while avoiding the amplification problem. The next logical step would be a real-time controller that monitors attention sparsity and dynamically adjusts budgets per phase, though completing the full mechanistic picture—especially the model-dependent entropy component—remains open. The crossover at s=0.25 where importance-based eviction switches between outperforming and underperforming random depending on phase appears consistently on Qwen2.5-7B-Instruct at higher sparsity levels with weaker effects, and the severity gradient follows a sub-exponential growth pattern. Discrimination collapse—where pruning degrades the model's ability to distinguish important heads—explains these findings across both models and challenges assumptions about phase-invariant compression. I'm noting the limitations: both models share the same architecture so cross-architecture validation is needed, experiments are only at 7B scale, evaluation is restricted to MATH-500, and the discrimination collapse mechanism is currently supported by correlational evidence rather than causal proof. I'm working through the LaTeX document structure now—need to update several cross-references since the KV importance equation is moving to the appendix, which will change how it's cited in the methodology section. The reference format will depend on whether appendix equations continue the main counter or use their own numbering scheme, so I need to decide on the clearest way to handle that citation. ACL format with \appendix, it depends on the numbering scheme. Since the main text equations are (1) and (2) (eq:ii and eq:gradient), the appendix equations would be numbered starting from (3) if there's no resetcounter. Actually, wait - with \appendix in LaTeX + acl style, the equation counter typically continues. So eq:head-mask would be (3), eq:kv-mask (4), eq:kv-importance (5), eq:attn-sparsity (6). A reference to "Eq. 5" from methodology is fine.

Actually wait, let me think again. The appendix.tex also has eq:attn-entropy in appendix_disc_analysis.tex (line 52). And the multiplicative null section doesn't have any equation labels.

Looking at the new appendix structure, I've got the Compound Sparsity Formulation section with four equations, then Multiplicative Null Verification and Bootstrap sections with no labeled equations, followed by the results and analysis sections from the existing appendix files. The Entropy Redistribution Analysis at the end brings in that final equation. So the numbering flows naturally: equations (3) through (7) across the appendix, making a reference to "Eq. 5" from the methodology section perfectly standard. LaTeX will handle the numbering automatically. I've got 9 edits to make across multiple files. For the appendix.tex file, I need to insert a new section at the beginning. For appendix_results.tex, I have two separate edits—fixing a broken reference on line 8 and adding a Cohen's d table at the end after line 61. Since these edits don't overlap, I can handle them sequentially.

Let me think through the execution strategy. I could do all the edits in one batch message, but I need to be careful with multiple edits on the same file. I'll combine the two appendix_results.tex changes by appending the table at the end, which simplifies things. Now I'm ready to execute all the file operations at once. I'm checking the exact wording of that roadmap sentence to delete it cleanly. I need to make sure I capture the full line from "The remainder..." through "...and limitations." without any extra characters. I'm also realizing I should verify the label reference in discussion.tex since that roadmap sentence mentions `\S\ref{sec:analysis}` but I'm changing that reference in introduction.tex to point to a different section instead. I'm verifying that the cross-references in the appendix match the new structure—the discrimination-collapse label exists in my revised results section, and the entropy-discrimination mechanism discussion doesn't require any additional references. Now I'm checking that the equations I'm moving from the original background file are preserved exactly as they were, starting with the head-mask and key-value mask definitions. I'm preserving those equations exactly as they are. Now I need to handle the cross-reference issue in appendix_results.tex where it references a section label that no longer exists in my new discussion.tex, so I'll need to fix that reference there. I'm going to batch all my edits together—writing the four new files and making targeted edits to the existing ones—that's about 10 tool calls total. Actually, I'm hitting up against a limitation with how many edits I can make in one go, so I need to think through the order carefully.

Let me verify that each string I'm planning to replace is actually unique in its file. For the introduction.tex edit, the string with parentheses around the reference should only appear once on line 29, while a similar reference without parentheses shows up elsewhere. That distinction makes it unique enough to target safely.

For the second introduction.tex edit, I'm using the entire line 33 as my old_string, which is long enough to be guaranteed unique.

For main.tex, I need to be careful with newlines—instead of just targeting the single line, I'll use the surrounding context of the results and discussion inputs to create a unique, unambiguous match that removes the analysis input cleanly.

For the appendix.tex edit, I'm replacing the section header with new content that includes the original text.

Now looking at appendix_results.tex, I'm checking that `\S\ref{sec:phase-seg}` appears only once on line 8, so that's safe to use. For the second edit there, I'm targeting the final lines of the file with a distinctive string that captures the experimental IDs and variance discussion.

I'm ready to execute all the tool calls now. Actually, I should reconsider the methodology.tex edit—I initially thought about updating the eq:kv-importance reference, but the current setup works fine since readers can follow the cross-reference. The background section already explains importance-based eviction conceptually, so the methodology reference to the equation is appropriate as is. I'm settling on the simpler version without the equation or appendix reference—just stating "position-normalized cumulative attention; BOS always retained" since the reader will understand this from the background. I should verify that removing the `sec:compound-sparsity` label doesn't break any existing references, and it looks like nothing in the codebase references it, so that's safe. Now I'm ready to execute all 11 tool calls: 4 writes and 7 edits across the introduction, main text, appendix, and results sections.

I need to make sure the new appendix section includes the `app:compound-formulation` label that the updated background references, and I should preserve that prior work citation about super-additive joint effects to maintain full context. Let me also double-check that all the cross-references in discussion.tex are pointing to the right sections—the main results table and the phase amplification and discrimination collapse sections all check out.

For the file structure, the Limitations section needs to go between the conclusion and bibliography, which will happen naturally once I add it to conclusion.tex. The references in conclusion.tex are just claim labels with no figure or table citations, so those are fine. Now I'm ready to make all the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "7d2916ab-b4b3-4e5f-ae71-fbec29a27063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 33_

I'll now execute all compression edits across all files simultaneously. The plan: rewrite background/results/discussion/conclusion, update cross-references, and move content to appendices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d9ac96dc-4ea7-455a-95b0-f897c1664a77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_018A5FRivVjkkNoi1yfjGEhC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\n\\paragraph{Compound sparsity.}\nConsider a Transformer with $L$ layers and $H$ heads per layer under a unified sparsity budget $s \\in (0,1)$. \\emph{Attention head pruning} removes the lowest-importance $s$ fraction of heads per layer (ranked by Frobenius norm \\cite{voita2019heads, michel2019sixteen}); \\emph{KV cache eviction} discards the lowest-scoring $s$ fraction of token positions from the cache. We compare \\textbf{importance-based} eviction---scoring positions by position-normalized cumulative attention mass---against a \\textbf{random} baseline. Applying both simultaneously yields \\emph{compound sparsity}, whose joint degradation can be super-additive \\cite{spark-aaai2026}. Full formulation in Appendix~\\ref{app:compound-formulation}.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified in Appendix~\\ref{app:multiplicative-null}) and report medians throughout due to right-skewed distributions.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases. $G \\gg 1$ indicates compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}. For each query position, we compute the fraction of key positions receiving negligible attention (${<}1\\%$ of the maximum), averaged across heads, yielding a per-position sparsity score $\\sigma_i$. Tokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by tercile boundaries; segments shorter than 10 tokens are merged with adjacent phases. Full details in Appendix~\\ref{app:compound-formulation}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "44f191d2-b244-48da-8eac-6bd8654bf8b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 35 · 2026-05-14T12:43:59.959Z_

<details><summary>↩ Tool result · reported error · `toolu_018A5FRivVjkkNoi1yfjGEhC`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "22cc5dba-0bc2-4284-9ab9-6044900293f6",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Write · `toolu_01EnGU89nkaBqBvdC1Z2MvjV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nCompound severity depends qualitatively on eviction strategy. Under importance-based eviction on DeepSeek-R1-Distill-Qwen-7B, the median severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification (Table~\\ref{tab:main-results}). Under random eviction, $\\Delta$ shows no systematic growth ($-0.02$ to $1.54$), indicating that compound severity is not intrinsic to the compression level but an emergent phase-strategy interaction. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing by reasoning phase reveals that severity concentrates in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$.\n\nUnder importance-based eviction, the severity gradient increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$), confirming that phase modulation is specific to the interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level on DeepSeek-R1-Distill-Qwen-7B. II values are problem-level medians ($n{=}50$). $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$; $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe gradient growth is sub-exponential: successive ratios of $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with saturation. Figure~\\ref{fig:hero} visualizes this trajectory. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) vs.\\ sparsity level $s$. Importance-based eviction (solid) increases from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a \\emph{crossover}: at $s{=}0.25$, importance-based eviction yields lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$) but higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$)---a reversal in strategy ranking (Figure~\\ref{fig:crossover}). In high-sparsity phases, focused attention preserves importance-score quality; in low-sparsity phases, head pruning redistributes attention mass, degrading importance scores (\\S\\ref{sec:discrimination-collapse}) and producing higher compound severity than random eviction. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy crossover at $s{=}0.25$: importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nWe replicate on Qwen2.5-7B-Instruct ($n{=}46$ valid problems), which shares the Qwen2 backbone but uses instruction tuning instead of reasoning distillation. Table~\\ref{tab:cross-model} compares median severity differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median $\\Delta$ under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & \\footnotesize $s{=}0.15$ & \\footnotesize $s{=}0.20$ & \\footnotesize $s{=}0.25$ & \\footnotesize $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}\n\\end{tabular}\n\\end{table}\n\nQwen reproduces the monotonic gradient at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$), with Spearman $\\rho = 1.0$ (gradient permutation $p = 0.043$). The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Full details in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Statistical Validation (C6)}\n\\label{sec:stat-validation}\n\nAll four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired $d_z$ grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Full effect sizes and bootstrap CIs in Appendix~\\ref{app:stat-validation-details} (Table~\\ref{tab:cohens-d}). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\n\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning makes the cumulative KV importance distribution more uniform---a \\emph{discrimination collapse} that explains the phase-strategy interaction. Table~\\ref{tab:discrimination-metrics} shows consistent reductions across both models: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$. When importance scores lose discriminative power, importance-based eviction degenerates toward arbitrary selection---explaining the crossover (\\S\\ref{sec:crossover}). Random eviction is immune because its decisions are independent of score quality. A secondary entropy redistribution effect is model-dependent (Appendix~\\ref{app:entropy-redistribution}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse: $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction.}\n\\label{tab:discrimination-metrics}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e9ccd22d-fecb-44dd-b9bb-943b13a8d3ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 37 · 2026-05-14T12:44:47.268Z_

<details><summary>↩ Tool result · `toolu_01EnGU89nkaBqBvdC1Z2MvjV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "322ac10c-459d-4615-a840-d87cb0bef1b4",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nCompound severity depends qualitatively on eviction strategy. Under importance-based eviction on DeepSeek-R1-Distill-Qwen-7B, the median severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification (Table~\\ref{tab:main-results}). Under random eviction, $\\Delta$ shows no systematic growth ($-0.02$ to $1.54$), indicating that compound severity is not intrinsic to the compression level but an emergent phase-strategy interaction. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing by reasoning phase reveals that severity concentrates in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$.\n\nUnder importance-based eviction, the severity gradient increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$), confirming that phase modulation is specific to the interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level on DeepSeek-R1-Distill-Qwen-7B. II values are problem-level medians ($n{=}50$). $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$; $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe gradient growth is sub-exponential: successive ratios of $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with saturation. Figure~\\ref{fig:hero} visualizes this trajectory. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) vs.\\ sparsity level $s$. Importance-based eviction (solid) increases from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a \\emph{crossover}: at $s{=}0.25$, importance-based eviction yields lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$) but higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$)---a reversal in strategy ranking (Figure~\\ref{fig:crossover}). In high-sparsity phases, focused attention preserves importance-score quality; in low-sparsity phases, head pruning redistributes attention mass, degrading importance scores (\\S\\ref{sec:discrimination-collapse}) and producing higher compound severity than random eviction. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy crossover at $s{=}0.25$: importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nWe replicate on Qwen2.5-7B-Instruct ($n{=}46$ valid problems), which shares the Qwen2 backbone but uses instruction tuning instead of reasoning distillation. Table~\\ref{tab:cross-model} compares median severity differences.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median $\\Delta$ under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & \\footnotesize $s{=}0.15$ & \\footnotesize $s{=}0.20$ & \\footnotesize $s{=}0.25$ & \\footnotesize $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}\n\\end{tabular}\n\\end{table}\n\nQwen reproduces the monotonic gradient at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$), with Spearman $\\rho = 1.0$ (gradient permutation $p = 0.043$). The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Full details in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Statistical Validation (C6)}\n\\label{sec:stat-validation}\n\nAll four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired $d_z$ grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Full effect sizes and bootstrap CIs in Appendix~\\ref{app:stat-validation-details} (Table~\\ref{tab:cohens-d}). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\n\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning makes the cumulative KV importance distribution more uniform---a \\emph{discrimination collapse} that explains the phase-strategy interaction. Table~\\ref{tab:discrimination-metrics} shows consistent reductions across both models: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$. When importance scores lose discriminative power, importance-based eviction degenerates toward arbitrary selection---explaining the crossover (\\S\\ref{sec:crossover}). Random eviction is immune because its decisions are independent of score quality. A secondary entropy redistribution effect is model-dependent (Appendix~\\ref{app:entropy-redistribution}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse: $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction.}\n\\label{tab:discrimination-metrics}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 37,
        "newStart": 5,
        "newLines": 19,
        "lines": [
          " \\subsection{Strategy-Dependent Severity (C1)}",
          " \\label{sec:strategy-severity}",
          " ",
          "-The compound severity difference reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the median compound severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json",
          "+Compound severity depends qualitatively on eviction strategy. Under importance-based eviction on DeepSeek-R1-Distill-Qwen-7B, the median severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification (Table~\\ref{tab:main-results}). Under random eviction, $\\Delta$ shows no systematic growth ($-0.02$ to $1.54$), indicating that compound severity is not intrinsic to the compression level but an emergent phase-strategy interaction. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}",
          "-\\label{tab:aggregate-ii}",
          "-\\begin{tabular}{@{}lcccc@{}}",
          "-\\toprule",
          "-Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\",
          "-\\midrule",
          "-Importance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff",
          "-Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "-",
          "-This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.",
          "-",
          "-",
          " \\subsection{Phase-Modulated Amplification (C2)}",
          " \\label{sec:phase-amplification}",
          " ",
          "-Decomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.",
          "+Decomposing by reasoning phase reveals that severity concentrates in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$.",
          " ",
          "-Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json",
          "+Under importance-based eviction, the severity gradient increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$), confirming that phase modulation is specific to the interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json",
          " ",
          " \\begin{table*}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ is the median severity difference. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification.}",
          "+\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level on DeepSeek-R1-Distill-Qwen-7B. II values are problem-level medians ($n{=}50$). $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$; $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}",
          " \\label{tab:main-results}",
          " \\begin{tabular}{@{}llccccr@{}}",
          " \\toprule"
        ]
      },
      {
        "oldStart": 56,
        "oldLines": 83,
        "newStart": 38,
        "newLines": 82,
        "lines": [
          " \\end{tabular}",
          " \\end{table*}",
          " ",
          "-The gradient growth is sub-exponential: successive ratios of the median severity difference $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\\times}$, $2.2{\\times}$, and $1.2{\\times}$. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff",
          "+The gradient growth is sub-exponential: successive ratios of $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with saturation. Figure~\\ref{fig:hero} visualizes this trajectory. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff",
          " ",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}",
          "-\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$, while random eviction (dashed) remains flat near $1{\\times}$. Shaded regions denote 95\\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030",
          "+\\caption{Severity gradient ($G$) vs.\\ sparsity level $s$. Importance-based eviction (solid) increases from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030",
          " \\label{fig:hero}",
          " \\end{figure}",
          " ",
          "-We report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\\Delta = 22.94$ vs.\\ median $\\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586",
          " ",
          "-",
          " \\subsection{Phase-Strategy Crossover (C3)}",
          " \\label{sec:crossover}",
          " ",
          "-The phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json",
          "+The phase-modulated gradient produces a \\emph{crossover}: at $s{=}0.25$, importance-based eviction yields lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$) but higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$)---a reversal in strategy ranking (Figure~\\ref{fig:crossover}). In high-sparsity phases, focused attention preserves importance-score quality; in low-sparsity phases, head pruning redistributes attention mass, degrading importance scores (\\S\\ref{sec:discrimination-collapse}) and producing higher compound severity than random eviction. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json",
          " ",
          "-Figure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.",
          "-",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}",
          "-\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28",
          "+\\caption{Strategy crossover at $s{=}0.25$: importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28",
          " \\label{fig:crossover}",
          " \\end{figure}",
          " ",
          "-The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.",
          " ",
          "-The crossover is present at all four tested sparsity levels ($s \\geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\\times}$ at $s{=}0.15$ to $5.4{\\times}$ at $s{=}0.20$, before moderating to $3.6{\\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62",
          "-",
          "-",
          " \\subsection{Cross-Model Replication (C5)}",
          " \\label{sec:cross-model}",
          " ",
          "-To assess generalization, we replicate importance-based eviction experiments on Qwen2.5-7B-Instruct, which shares the Qwen2 backbone but uses standard instruction tuning instead of reasoning distillation ($n{=}46$ valid problems after excluding degenerate phase assignments). Table~\\ref{tab:cross-model} compares the median severity difference across both models.",
          "+We replicate on Qwen2.5-7B-Instruct ($n{=}46$ valid problems), which shares the Qwen2 backbone but uses instruction tuning instead of reasoning distillation. Table~\\ref{tab:cross-model} compares median severity differences.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Cross-model replication: median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) under importance-based eviction.}",
          "+\\caption{Cross-model replication: median $\\Delta$ under importance-based eviction.}",
          " \\label{tab:cross-model}",
          " \\begin{tabular}{@{}lcccc@{}}",
          " \\toprule",
          " Model & \\footnotesize $s{=}0.15$ & \\footnotesize $s{=}0.20$ & \\footnotesize $s{=}0.25$ & \\footnotesize $s{=}0.30$ \\\\",
          " \\midrule",
          "-DeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json",
          "-Qwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json; 0.234979 rounds to 0.23 at 2dp",
          "+DeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030",
          "+Qwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030",
          " \\bottomrule",
          "-\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize Both models share the Qwen2 architecture but differ in training (distillation vs.\\ instruction tuning). DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}",
          "+\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}",
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-Qwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\\ref{tab:cross-model}), paralleling DeepSeek's trajectory at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$; Table~\\ref{tab:cohens-d}), with Spearman $\\rho = 1.0$ between the four-point sequences (gradient permutation $p = 0.043$). % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json",
          "-Full per-problem concordance analysis and random eviction controls appear in Appendix~\\ref{app:cross-model-details}.",
          "+Qwen reproduces the monotonic gradient at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$), with Spearman $\\rho = 1.0$ (gradient permutation $p = 0.043$). The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Full details in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json",
          " ",
          "-The replication suggests that the phase-modulated severity gradient is an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning, not an artifact of DeepSeek's distillation-induced phase structure. Generalization to other architectures remains an open question (\\S\\ref{sec:limitations}).",
          " ",
          "-",
          " \\subsection{Statistical Validation (C6)}",
          " \\label{sec:stat-validation}",
          " ",
          "-All four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired effect sizes ($d_z$) grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Table~\\ref{tab:cohens-d} reports full $d_z$ values and bootstrap CIs; details in Appendix~\\ref{app:stat-validation-details}.",
          "+All four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired $d_z$ grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Full effect sizes and bootstrap CIs in Appendix~\\ref{app:stat-validation-details} (Table~\\ref{tab:cohens-d}). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json",
          " ",
          "+",
          "+\\subsection{Discrimination Collapse}",
          "+\\label{sec:discrimination-collapse}",
          "+",
          "+Head pruning makes the cumulative KV importance distribution more uniform---a \\emph{discrimination collapse} that explains the phase-strategy interaction. Table~\\ref{tab:discrimination-metrics} shows consistent reductions across both models: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$. When importance scores lose discriminative power, importance-based eviction degenerates toward arbitrary selection---explaining the crossover (\\S\\ref{sec:crossover}). Random eviction is immune because its decisions are independent of score quality. A secondary entropy redistribution effect is model-dependent (Appendix~\\ref{app:entropy-redistribution}).",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          "+\\caption{Discrimination collapse: $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction.}",
          "+\\label{tab:discrimination-metrics}",
          " \\small",
          "-\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}",
          "-\\label{tab:cohens-d}",
          "-\\begin{tabular}{@{}lcccc@{}}",
          "+\\begin{tabular}{llrr}",
          " \\toprule",
          "-$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\",
          "+Model & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\",
          " \\midrule",
          "-0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015",
          "-0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020",
          "-0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025",
          "-0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030",
          "+DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\",
          "+DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\",
          "+DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\",
          "+DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\",
          "+\\midrule",
          "+Qwen & $0.15$ & $-0.010$ & $-0.05$ \\\\",
          "+Qwen & $0.20$ & $-0.012$ & $-0.21$ \\\\",
          "+Qwen & $0.25$ & $-0.010$ & $-1.49$ \\\\",
          "+Qwen & $0.30$ & $-0.020$ & $-1.14$ \\\\",
          " \\bottomrule",
          "-\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}",
          " \\end{tabular}",
          " \\end{table}"
        ]
      }
    ],
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe compound severity difference reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the median compound severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ is the median severity difference. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe gradient growth is sub-exponential: successive ratios of the median severity difference $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\\times}$, $2.2{\\times}$, and $1.2{\\times}$. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$, while random eviction (dashed) remains flat near $1{\\times}$. Shaded regions denote 95\\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\\Delta = 22.94$ vs.\\ median $\\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is present at all four tested sparsity levels ($s \\geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\\times}$ at $s{=}0.15$ to $5.4{\\times}$ at $s{=}0.20$, before moderating to $3.6{\\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess generalization, we replicate importance-based eviction experiments on Qwen2.5-7B-Instruct, which shares the Qwen2 backbone but uses standard instruction tuning instead of reasoning distillation ($n{=}46$ valid problems after excluding degenerate phase assignments). Table~\\ref{tab:cross-model} compares the median severity difference across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & \\footnotesize $s{=}0.15$ & \\footnotesize $s{=}0.20$ & \\footnotesize $s{=}0.25$ & \\footnotesize $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json\nQwen2.5-7B     & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json; 0.234979 rounds to 0.23 at 2dp\n\\bottomrule\n\\multicolumn{5}{@{}p{\\columnwidth}@{}}{\\footnotesize Both models share the Qwen2 architecture but differ in training (distillation vs.\\ instruction tuning). DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct.}\n\\end{tabular}\n\\end{table}\n\nQwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\\ref{tab:cross-model}), paralleling DeepSeek's trajectory at approximately one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$; Table~\\ref{tab:cohens-d}), with Spearman $\\rho = 1.0$ between the four-point sequences (gradient permutation $p = 0.043$). % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\nFull per-problem concordance analysis and random eviction controls appear in Appendix~\\ref{app:cross-model-details}.\n\nThe replication suggests that the phase-modulated severity gradient is an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning, not an artifact of DeepSeek's distillation-induced phase structure. Generalization to other architectures remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation (C6)}\n\\label{sec:stat-validation}\n\nAll four sparsity levels reject $H_0$ (no strategy difference) via paired permutation tests after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$). Paired effect sizes ($d_z$) grow monotonically: DeepSeek from $0.44$ (small) to $0.80$ (large); Qwen from $0.28$ (marginal) to $1.02$ (large). Table~\\ref{tab:cohens-d} reports full $d_z$ values and bootstrap CIs; details in Appendix~\\ref{app:stat-validation-details}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Write · `toolu_011xJ8UNrJtfBJiVt8jhyY8z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction---importance-based eviction degrades when attention distributes broadly---is intuitive.\nThe surprise lies in the quantitative structure: the severity gradient ($69$--$274{\\times}$; Table~\\ref{tab:main-results}) far exceeds a naive ``somewhat worse'' prediction, compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero interaction ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$), and a crossover emerges where importance-based eviction simultaneously outperforms and underperforms random depending on phase---a reversal that cannot be derived from entropy arguments alone. % exp_id: bf16_importance_s015..s030\n\n\\paragraph{Random masking as falsification.}\nIf compound severity amplification were inherent to joint compression, random eviction should exhibit a comparable phase gradient.\nIt does not: 7/8 conditions across both models show no significant phase modulation; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) has negligible effect size ($d_z{=}{-}0.04$), isolating the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Cross-model replication.}\nThe phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\\rho{=}1.0$, gradient permutation $p{=}0.043$), though Qwen's absolute magnitude is approximately one-fifth of DeepSeek's with a higher onset threshold ($s \\geq 0.20$ vs.\\ $s{=}0.15$).\nWe conjecture that reasoning distillation amplifies the interaction by producing sharper internal phase transitions. % exp_id: cross_model_correlation\n\n\\paragraph{Implications for deployment.}\nUniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.\nA \\emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.\nThe severity gradient $G$ (\\S\\ref{sec:phase-amplification}) provides a natural signal for such allocation.\n\n\\paragraph{Future directions.}\nA phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.\nCompleting the mechanistic picture---particularly the model-dependent entropy component (\\S\\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "1bf48178-6b0f-4b21-aee8-f38053769ced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 39 · 2026-05-14T12:45:01.255Z_

<details><summary>↩ Tool result · reported error · `toolu_011xJ8UNrJtfBJiVt8jhyY8z`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "8e50688a-ab7e-4f5c-928c-550d305f4a44",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_01D441XC9LNhk7fyenAugHWE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the median II difference between low- and high-sparsity phases increases monotonically from $0.39$ to $14.59$ ($d_z$: $0.44 \\to 0.80$; all $p_{\\text{Bonf}} < 0.005$), while random eviction produces no significant phase modulation in 7/8 conditions (C1, C2). At $s{=}0.25$, a crossover emerges where importance-based eviction simultaneously outperforms and underperforms random depending on phase (C3). The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ with attenuated magnitude (C5), and the severity gradient grows sub-exponentially (C6). Discrimination collapse---whereby head pruning degrades importance-score discriminability---provides a robust mechanistic explanation confirmed across both models (C4). These findings challenge the phase-invariance assumption and motivate phase-aware compression budgets for reasoning models.\n\n\\section*{Limitations}\n\nBoth models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "14cc19b8-bc74-44d3-9210-207b5a71398e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 41 · 2026-05-14T12:45:10.314Z_

<details><summary>↩ Tool result · reported error · `toolu_01D441XC9LNhk7fyenAugHWE`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "51664466-7a12-4790-866f-38bbdae888dc",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01Pu3Zow4efBDY3ZnZe7usRG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).",
  "new_string": "    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:discrimination-collapse})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "249c6a00-46f2-449a-b039-41d779b024fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 43 · 2026-05-14T12:45:12.643Z_

<details><summary>↩ Tool result · reported error · `toolu_01Pu3Zow4efBDY3ZnZe7usRG`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "427a3019-4624-41ec-952d-f9eb8e6352e1",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01UQ7zToR9MyCmAxupoD5Xat`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.",
  "new_string": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "3e9aea2a-3c47-4dcc-a1e4-d6fe264b27ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 45 · 2026-05-14T12:45:16.878Z_

<details><summary>↩ Tool result · reported error · `toolu_01UQ7zToR9MyCmAxupoD5Xat`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "a6249054-920d-4f15-9cb4-8495146b677f",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_01VVaR56Nfb9scvtk5mh9P3e`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "old_string": "\\input{results}\n\\input{analysis}\n\\input{discussion}",
  "new_string": "\\input{results}\n\\input{discussion}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "169e0cff-a2ea-4a78-87ec-874724b33fa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 47 · 2026-05-14T12:45:17.828Z_

<details><summary>↩ Tool result · `toolu_01VVaR56Nfb9scvtk5mh9P3e`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "5d02416b-b380-4420-93b0-4c495a9ca84a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
    "oldString": "\\input{results}\n\\input{analysis}\n\\input{discussion}",
    "newString": "\\input{results}\n\\input{discussion}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_results}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 7,
        "newStart": 33,
        "newLines": 6,
        "lines": [
          " \\input{background}",
          " \\input{methodology}",
          " \\input{results}",
          "-\\input{analysis}",
          " \\input{discussion}",
          " \\input{conclusion}",
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01FzWjbnSoZyTbeMjTZ3Usmz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "old_string": "\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}",
  "new_string": "\\section{Compound Sparsity Formulation}\n\\label{app:compound-formulation}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "bcf3a4b5-3200-44c6-a807-6273d06db12c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 49 · 2026-05-14T12:45:31.990Z_

<details><summary>↩ Tool result · `toolu_01FzWjbnSoZyTbeMjTZ3Usmz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "4285ee57-0564-4ea9-9c01-dce08d895c2f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
    "oldString": "\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}",
    "newString": "\\section{Compound Sparsity Formulation}\n\\label{app:compound-formulation}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}",
    "originalFile": "\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n\\section{Bootstrap and Permutation Details}\n\\label{app:bootstrap-details}\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.\n\nThe permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \\geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 37,
        "lines": [
          "+\\section{Compound Sparsity Formulation}",
          "+\\label{app:compound-formulation}",
          "+",
          "+\\paragraph{Attention head pruning.}",
          "+Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:",
          "+\\begin{equation}",
          "+    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.",
          "+    \\label{eq:head-mask}",
          "+\\end{equation}",
          "+",
          "+\\paragraph{KV cache eviction.}",
          "+A position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):",
          "+\\begin{equation}",
          "+    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.",
          "+    \\label{eq:kv-mask}",
          "+\\end{equation}",
          "+Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:",
          "+\\begin{equation}",
          "+    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},",
          "+    \\label{eq:kv-importance}",
          "+\\end{equation}",
          "+where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.",
          "+",
          "+\\paragraph{Compound sparsity.}",
          "+Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.",
          "+",
          "+\\paragraph{Attention sparsity metric.}",
          "+For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:",
          "+\\begin{equation}",
          "+    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].",
          "+    \\label{eq:attn-sparsity}",
          "+\\end{equation}",
          "+The per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.",
          "+",
          " \\section{Multiplicative Null Verification}",
          " \\label{app:multiplicative-null}",
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01D96pmgvFoYRZLDBhka8Bfk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
  "old_string": "(\\S\\ref{sec:phase-seg})",
  "new_string": "(\\S\\ref{sec:phase-segmentation})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "602f5b28-ea44-49a6-b3a2-db86c169f172",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 51 · 2026-05-14T12:45:33.338Z_

<details><summary>↩ Tool result · reported error · `toolu_01D96pmgvFoYRZLDBhka8Bfk`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "bdc03ba4-7fc6-42c8-972e-5de41f67b6c6",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01MpqYp4fqnSGSP9ioyRQPLC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
  "old_string": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000",
  "new_string": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "206d3106-4a51-4602-beda-94985776fcc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 53 · 2026-05-14T12:45:43.326Z_

<details><summary>↩ Tool result · reported error · `toolu_01MpqYp4fqnSGSP9ioyRQPLC`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "0adcc63b-c744-4ac9-89d8-9014d37d854a",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01TEhZnQ28QRaHwJVAuz8Fbm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
  "old_string": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline.",
  "new_string": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention; BOS always retained) against a \\textbf{random} baseline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "416c4eb3-9ecd-451e-b912-dcb8c2ba7d4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1LBKzMgLYyALzdPvRWhxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37074,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 37074
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

_source line 55 · 2026-05-14T12:45:45.304Z_

<details><summary>↩ Tool result · reported error · `toolu_01TEhZnQ28QRaHwJVAuz8Fbm`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "5f9897e8-56e6-4788-9ed4-a1eaa7ab8b70",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
Some files succeeded, some failed due to "File has been modified since read". I need to re-read the files that failed and retry. Let me re-read them.

Succeeded:
- results.tex ✓
- main.tex ✓
- appendix.tex ✓

Failed (need re-read):
- background.tex
- discussion.tex
- conclusion.tex
- introduction.tex (2 edits)
- appendix_results.tex (2 edits)
- methodology.tex (1 edit)

Let me re-read all the failed files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "26094119-ab26-4aee-9f3d-007d3e69c489",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 57_

Several files need re-reading. Let me re-read them and retry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "9689f2f3-a51b-4d05-9d10-ab53afdd9831",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01QEyZSZCunMdd6mLFLm29v2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e61e1565-411c-439b-a795-81947f1d4134",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 59 · 2026-05-14T12:45:50.694Z_

<details><summary>↩ Tool result · `toolu_01QEyZSZCunMdd6mLFLm29v2`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer with $L$ layers and $H$ heads per layer. Let $s \in (0,1)$ denote a unified sparsity budget.
14	
15	\paragraph{Attention head pruning.}
16	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
17	\begin{equation}
18	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
19	    \label{eq:head-mask}
20	\end{equation}
21	
22	\paragraph{KV cache eviction.}
23	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
24	\begin{equation}
25	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
26	    \label{eq:kv-mask}
27	\end{equation}
28	We compare two strategies for constructing $\mathbf{m}_k$:
29	\begin{itemize}[nosep,leftmargin=*]
30	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
31	    \begin{equation}
32	        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
33	        \label{eq:kv-importance}
34	    \end{equation}
35	    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
36	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
37	\end{itemize}
38	
39	\paragraph{Compound sparsity.}
40	Applying both mechanisms simultaneously yields \emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
41	
42	\subsection{Interaction Index}
43	\label{sec:interaction-index}
44	
45	For a text segment, let $r_c = \text{PPL}_c / \text{PPL}_d$ denote the relative perplexity degradation under condition $c \in \{a\text{(attn-only)}, k\text{(kv-only)}, b\text{(both)}\}$. The Interaction Index is:
46	\begin{equation}
47	    \mathrm{II} = r_b - r_a - r_k + 1.
48	    \label{eq:ii}
49	\end{equation}
50	
51	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.
52	
53	\paragraph{Severity gradient.}
54	To capture how II varies across reasoning phases (defined in \S\ref{sec:phase-segmentation}), we define the \emph{severity gradient}:
55	\begin{equation}
56	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
57	    \label{eq:gradient}
58	\end{equation}
59	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.
60	$G \gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \approx 1$ indicates phase-invariant degradation.
61	When $\widetilde{\mathrm{II}}_{\,\textit{high}} < \varepsilon$ for a small threshold $\varepsilon > 0$, we report $G = \infty$.
62	
63	\subsection{Phase Segmentation}
64	\label{sec:phase-segmentation}
65	
66	We partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \cite{thinkv-iclr2026}.
67	
68	\paragraph{Attention sparsity.}
69	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
70	\begin{equation}
71	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
72	    \label{eq:attn-sparsity}
73	\end{equation}
74	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads.
75	
76	\paragraph{Quantile-based segmentation.}
77	Tokens are partitioned into \textbf{high-}, \textbf{mid-}, and \textbf{low-sparsity} phases by the tercile boundaries of $\{\sigma_i\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "c6bfb5fd-47ca-4122-b35b-0cd2b3dce9e2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer with $L$ layers and $H$ heads per layer. Let $s \\in (0,1)$ denote a unified sparsity budget.\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields \\emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by the tercile boundaries of $\\{\\sigma_i\\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_0176df15ZXCN5MewVBXP1i4Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "b7ed1f99-d949-454d-8088-f027edffe2f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 61 · 2026-05-14T12:45:51.626Z_

<details><summary>↩ Tool result · `toolu_0176df15ZXCN5MewVBXP1i4Z`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	The qualitative direction of our findings---that importance-based eviction degrades in diffuse-attention phases---may seem intuitive. The surprise is quantitative: $69$--$274{\times}$ severity amplification far exceeds a naive prediction; the crossover at $s{=}0.25$ (importance-based eviction simultaneously outperforming and underperforming random across phases) cannot be derived from the observation that ``scores are noisier when attention is diffuse.'' % exp_id: bf16_importance_s015..s030
6	
7	\paragraph{Random masking as falsification control.}
8	If compound severity amplification were inherent to applying two compression methods jointly, random eviction should exhibit a comparable phase gradient. It does not: random eviction fails 7/8 paired permutation tests across both models, with the single exception (Qwen $s{=}0.30$, $d_z{=}{-}0.04$) showing negligible effect size. This isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
9	
10	\paragraph{Cross-model replication.}
11	The phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation
12	
13	\paragraph{Deployment implications.}
14	Uniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.
15	
16	\subsection{Limitations}
17	\label{sec:limitations}
18	
19	\begin{itemize}[nosep,leftmargin=*]
20	\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.
21	\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.
22	\item All experiments at 7B scale; scaling behavior is untested.
23	\end{itemize}
24	Extended discussion in Appendix~\ref{app:limitations}.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "1c4ea828-6496-4185-8d30-b605cb0ec21a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe qualitative direction of our findings---that importance-based eviction degrades in diffuse-attention phases---may seem intuitive. The surprise is quantitative: $69$--$274{\\times}$ severity amplification far exceeds a naive prediction; the crossover at $s{=}0.25$ (importance-based eviction simultaneously outperforming and underperforming random across phases) cannot be derived from the observation that ``scores are noisier when attention is diffuse.'' % exp_id: bf16_importance_s015..s030\n\n\\paragraph{Random masking as falsification control.}\nIf compound severity amplification were inherent to applying two compression methods jointly, random eviction should exhibit a comparable phase gradient. It does not: random eviction fails 7/8 paired permutation tests across both models, with the single exception (Qwen $s{=}0.30$, $d_z{=}{-}0.04$) showing negligible effect size. This isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Cross-model replication.}\nThe phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation\n\n\\paragraph{Deployment implications.}\nUniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \\emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.\n\\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.\n\\item All experiments at 7B scale; scaling behavior is untested.\n\\end{itemize}\nExtended discussion in Appendix~\\ref{app:limitations}.\n",
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01BpabLCiYx2o1ayzsv78YTQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e211ac66-6460-4a68-8d7f-e43f221da18a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 63 · 2026-05-14T12:45:52.114Z_

<details><summary>↩ Tool result · `toolu_01BpabLCiYx2o1ayzsv78YTQ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not fixed but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Our contributions:
5	\textbf{(C1)} Compound severity depends qualitatively on eviction strategy: importance-based eviction produces phase-modulated interaction ($\Delta = 0.39$--$14.59$) while random eviction shows none (7/8 conditions).
6	\textbf{(C2)} Under importance-based eviction, the severity gradient grows monotonically with sparsity ($d_z$: $0.44 \to 0.80$, all $p_{\text{Bonf}} < 0.005$).
7	\textbf{(C3)} A crossover emerges: importance-based eviction simultaneously outperforms and underperforms random across phases.
8	\textbf{(C4)} Discrimination collapse---head pruning degrading importance score quality---is the robust mechanism (confirmed in all 16 conditions).
9	\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\rho{=}1.0$, gradient $p{=}0.043$) at ${\sim}1/5$ absolute magnitude.
10	\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.
11	These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "810fe25f-5c8a-4f04-b3b7-6bd5e6191a57",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not fixed but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Our contributions:\n\\textbf{(C1)} Compound severity depends qualitatively on eviction strategy: importance-based eviction produces phase-modulated interaction ($\\Delta = 0.39$--$14.59$) while random eviction shows none (7/8 conditions).\n\\textbf{(C2)} Under importance-based eviction, the severity gradient grows monotonically with sparsity ($d_z$: $0.44 \\to 0.80$, all $p_{\\text{Bonf}} < 0.005$).\n\\textbf{(C3)} A crossover emerges: importance-based eviction simultaneously outperforms and underperforms random across phases.\n\\textbf{(C4)} Discrimination collapse---head pruning degrading importance score quality---is the robust mechanism (confirmed in all 16 conditions).\n\\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\\rho{=}1.0$, gradient $p{=}0.043$) at ${\\sim}1/5$ absolute magnitude.\n\\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.\nThese findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Read · `toolu_0177uJ24PHm4Hos3XW6EP3Km`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "877a21ff-3b6a-4471-8fbe-2f8bc606577f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 65 · 2026-05-14T12:45:52.628Z_

<details><summary>↩ Tool result · `toolu_0177uJ24PHm4Hos3XW6EP3Km`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita-acl2019, michel-neurips2019}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:results}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:analysis}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	The remainder of this paper is organized as follows: \S\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \S\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \S\ref{sec:experimental-setup} describes our experimental setup; \S\ref{sec:results} presents the main results; \S\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \S\ref{sec:discussion} discusses implications and limitations.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "088670e1-0abb-4c0d-8582-fdad9f9037e6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita-acl2019, michel-neurips2019}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01VTi78dYBrSDq83zZAzKSZt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "6386853e-3acb-4439-aa3b-8e32a534e0ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 67 · 2026-05-14T12:45:53.054Z_

<details><summary>↩ Tool result · `toolu_01VTi78dYBrSDq83zZAzKSZt`</summary>

```text
1	% Appendix sections for content moved from results.tex (§5.5 and §5.6)
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
7	
8	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}50$ for DeepSeek).
9	
10	\paragraph{Per-problem concordance.}
11	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json
12	
13	\paragraph{Random eviction control.}
14	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
19	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
20	\label{fig:cross-model}
21	\end{figure}
22	
23	
24	\section{Statistical Validation Details}
25	\label{app:stat-validation-details}
26	
27	\paragraph{Permutation test.}
28	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
29	
30	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
31	
32	\begin{table}[t]
33	\centering
34	\small
35	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
36	\label{tab:permutation}
37	\begin{tabular}{@{}rrcl@{}}
38	\toprule
39	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
40	\midrule
41	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference
42	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference
43	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference
44	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
54	\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}
55	\label{fig:permtest-forest}
56	\end{figure}
57	
58	\paragraph{Additional effect size analysis.}
59	For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
60	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "25a6c0aa-783b-49d8-bd7c-a9bb7cecab6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix sections for content moved from results.tex (§5.5 and §5.6)\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\n\\section{Statistical Validation Details}\n\\label{app:stat-validation-details}\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Additional effect size analysis.}\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01Ejj8ipa91hHWXKpBVbvuSo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "282a5065-3d18-4b71-a7b9-6da41229122d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZHunXNoYenE24dYbDMycR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74721,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74721
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

_source line 69 · 2026-05-14T12:45:53.524Z_

<details><summary>↩ Tool result · `toolu_01Ejj8ipa91hHWXKpBVbvuSo`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA). \textbf{DeepSeek-R1-Distill-Qwen-7B} \cite{deepseek-r1-2025}, distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. \textbf{Qwen2.5-7B-Instruct} \cite{qwen25-2024} provides cross-model replication with standard instruction tuning rather than reasoning distillation.
8	Both models are loaded in \texttt{bfloat16} with eager attention to permit direct manipulation of attention matrices.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B; \texttt{bfloat16} eliminated all occurrences.}
9	
10	
11	\subsection{Dataset}
12	\label{sec:dataset}
13	
14	We evaluate on a 50-problem stratified subset of MATH-500 \cite{math500-neurips2021}, sampling uniformly across problem categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
15	
16	
17	\subsection{Configuration and Metrics}
18	\label{sec:config-metrics}
19	
20	We apply symmetric compound sparsity: for level $s \in \{0.15, 0.20, 0.25, 0.30\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\ref{eq:kv-importance}; BOS always retained) against a \textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.
21	
22	Each sequence is segmented into three reasoning phases using the quantile-based method of \S\ref{sec:phase-segmentation} ($\texttt{min\_phase\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\ref{eq:ii}) and severity gradient (Eq.~\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\ref{app:stat-validation-details}.\footnote{Experiments were conducted on 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "75a4a640-2327-4368-a3b3-decfe755da6c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA). \\textbf{DeepSeek-R1-Distill-Qwen-7B} \\cite{deepseek-r1-2025}, distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. \\textbf{Qwen2.5-7B-Instruct} \\cite{qwen25-2024} provides cross-model replication with standard instruction tuning rather than reasoning distillation.\nBoth models are loaded in \\texttt{bfloat16} with eager attention to permit direct manipulation of attention matrices.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B; \\texttt{bfloat16} eliminated all occurrences.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of MATH-500 \\cite{math500-neurips2021}, sampling uniformly across problem categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\n\\subsection{Configuration and Metrics}\n\\label{sec:config-metrics}\n\nWe apply symmetric compound sparsity: for level $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.\n\nEach sequence is segmented into three reasoning phases using the quantile-based method of \\S\\ref{sec:phase-segmentation} ($\\texttt{min\\_phase\\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\\ref{eq:ii}) and severity gradient (Eq.~\\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\\ref{app:stat-validation-details}.\\footnote{Experiments were conducted on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
I see that the files have been modified since my initial read (citation keys changed, some text reorganized). Let me now re-apply my edits with the current file content.

Key differences I notice:
1. background.tex: citation keys changed (e.g., `voita2019heads` → `voita-acl2019`, `michel2019sixteen` → `michel-neurips2019`)
2. discussion.tex: already somewhat compressed compared to original
3. conclusion.tex: already compressed into a different format
4. introduction.tex: citation keys changed
5. appendix_results.tex: the `sec:phase-seg` ref is already fixed to `sec:phase-segmentation`


6. methodology.tex: citation keys changed, Eq.~\ref{eq:kv-importance} still present

I need to adjust my edits to use the new citation keys throughout. For discussion.tex, it's already been compressed to 25 lines from 66, but I can still remove the Limitations subsection and tighten it further. Conclusion.tex is down to 12 lines from 30, so I'll focus on the remaining files that need citation key updates and any other refinements.

My plan is to update background.tex with the new citation keys, clean up discussion.tex by removing Limitations, add a Limitations section to conclusion.tex, fix the sec:analysis reference in introduction.tex, and add the cohens-d table to appendix_results.tex since the sec:phase-segmentation reference is already corrected.

Now I'm looking at the discussion.tex file to see what needs trimming—it has the Limitations subsection that should move elsewhere, but the main discussion paragraphs on predictability, masking controls, cross-model replication, and deployment implications are all staying put. I'm checking the current state of conclusion.tex and see it doesn't have a Limitations section yet, so I'll need to add that. Now I'm planning the remaining edits across all the files—I'll remove the Limitations subsection from discussion.tex and add a Future directions paragraph there, append a new Limitations section to conclusion.tex, fix the references in introduction.tex and remove the roadmap, update the equation reference in methodology.tex, and add the Cohen's d table to appendix_results.tex. Let me start with discussion.tex since it's already fairly concise.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "dedfdf70-adc4-41bd-a3a4-2730e855fe6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 71_

The files have been modified since my first read (citation keys updated, some content already compressed). Let me now apply the remaining changes with the current content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "6909fbf7-0ce8-46e2-8b9e-63b0ffa0a88a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 72_

<details open><summary>🔧 Tool call — Write · `toolu_01JwHUPYRTh7tt49L2qs2yBx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\n\\paragraph{Compound sparsity.}\nConsider a Transformer with $L$ layers and $H$ heads per layer under a unified sparsity budget $s \\in (0,1)$. \\emph{Attention head pruning} removes the lowest-importance $s$ fraction of heads per layer (ranked by Frobenius norm \\cite{voita-acl2019, michel-neurips2019}); \\emph{KV cache eviction} discards the lowest-scoring $s$ fraction of token positions from the cache. We compare \\textbf{importance-based} eviction---scoring positions by position-normalized cumulative attention mass---against a \\textbf{random} baseline. Applying both simultaneously yields \\emph{compound sparsity}, whose joint degradation can be super-additive \\cite{spark-aaai2026}. Full formulation in Appendix~\\ref{app:compound-formulation}.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified in Appendix~\\ref{app:multiplicative-null}) and report medians throughout due to right-skewed distributions.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases. $G \\gg 1$ indicates compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}. For each query position, we compute the fraction of key positions receiving negligible attention (${<}1\\%$ of the maximum), averaged across heads, yielding a per-position sparsity score $\\sigma_i$. Tokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by tercile boundaries; segments shorter than 10 tokens are merged with adjacent phases. Full details in Appendix~\\ref{app:compound-formulation}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "2fe40ac6-5b1b-43d0-ba34-02d88b028c0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 73 · 2026-05-14T12:46:41.076Z_

<details><summary>↩ Tool result · `toolu_01JwHUPYRTh7tt49L2qs2yBx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "2b7a49bb-a13c-460c-9c2a-c61fce652e89",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
    "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\n\\paragraph{Compound sparsity.}\nConsider a Transformer with $L$ layers and $H$ heads per layer under a unified sparsity budget $s \\in (0,1)$. \\emph{Attention head pruning} removes the lowest-importance $s$ fraction of heads per layer (ranked by Frobenius norm \\cite{voita-acl2019, michel-neurips2019}); \\emph{KV cache eviction} discards the lowest-scoring $s$ fraction of token positions from the cache. We compare \\textbf{importance-based} eviction---scoring positions by position-normalized cumulative attention mass---against a \\textbf{random} baseline. Applying both simultaneously yields \\emph{compound sparsity}, whose joint degradation can be super-additive \\cite{spark-aaai2026}. Full formulation in Appendix~\\ref{app:compound-formulation}.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified in Appendix~\\ref{app:multiplicative-null}) and report medians throughout due to right-skewed distributions.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases, we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases. $G \\gg 1$ indicates compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}. For each query position, we compute the fraction of key positions receiving negligible attention (${<}1\\%$ of the maximum), averaged across heads, yielding a per-position sparsity score $\\sigma_i$. Tokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by tercile boundaries; segments shorter than 10 tokens are merged with adjacent phases. Full details in Appendix~\\ref{app:compound-formulation}.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 43,
        "newStart": 1,
        "newLines": 11,
        "lines": [
          " % Section 3: Background and Problem Setup",
          " % Note: eq:ii and eq:gradient are the canonical definitions.",
          "-% Methodology.tex should reference these via \\eqref rather than redefining.",
          " ",
          " \\section{Background and Problem Setup}",
          " \\label{sec:background}",
          " ",
          "-We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.",
          "-",
          "-\\subsection{Compound Sparsity Formulation}",
          "-\\label{sec:compound-sparsity}",
          "-",
          "-Consider a Transformer with $L$ layers and $H$ heads per layer. Let $s \\in (0,1)$ denote a unified sparsity budget.",
          "-",
          "-\\paragraph{Attention head pruning.}",
          "-Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:",
          "-\\begin{equation}",
          "-    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.",
          "-    \\label{eq:head-mask}",
          "-\\end{equation}",
          "-",
          "-\\paragraph{KV cache eviction.}",
          "-A position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):",
          "-\\begin{equation}",
          "-    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.",
          "-    \\label{eq:kv-mask}",
          "-\\end{equation}",
          "-We compare two strategies for constructing $\\mathbf{m}_k$:",
          "-\\begin{itemize}[nosep,leftmargin=*]",
          "-    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:",
          "-    \\begin{equation}",
          "-        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},",
          "-        \\label{eq:kv-importance}",
          "-    \\end{equation}",
          "-    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.",
          "-    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.",
          "-\\end{itemize}",
          "-",
          " \\paragraph{Compound sparsity.}",
          "-Applying both mechanisms simultaneously yields \\emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.",
          "+Consider a Transformer with $L$ layers and $H$ heads per layer under a unified sparsity budget $s \\in (0,1)$. \\emph{Attention head pruning} removes the lowest-importance $s$ fraction of heads per layer (ranked by Frobenius norm \\cite{voita-acl2019, michel-neurips2019}); \\emph{KV cache eviction} discards the lowest-scoring $s$ fraction of token positions from the cache. We compare \\textbf{importance-based} eviction---scoring positions by position-normalized cumulative attention mass---against a \\textbf{random} baseline. Applying both simultaneously yields \\emph{compound sparsity}, whose joint degradation can be super-additive \\cite{spark-aaai2026}. Full formulation in Appendix~\\ref{app:compound-formulation}.",
          " ",
          " \\subsection{Interaction Index}",
          " \\label{sec:interaction-index}"
        ]
      },
      {
        "oldStart": 47,
        "oldLines": 31,
        "newStart": 15,
        "newLines": 17,
        "lines": [
          "     \\mathrm{II} = r_b - r_a - r_k + 1.",
          "     \\label{eq:ii}",
          " \\end{equation}",
          "+$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified in Appendix~\\ref{app:multiplicative-null}) and report medians throughout due to right-skewed distributions.",
          " ",
          "-$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.",
          "-",
          " \\paragraph{Severity gradient.}",
          "-To capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:",
          "+To capture how II varies across reasoning phases, we define the \\emph{severity gradient}:",
          " \\begin{equation}",
          "     G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},",
          "     \\label{eq:gradient}",
          " \\end{equation}",
          "-where $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.",
          "-$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.",
          "-When $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.",
          "+where $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases. $G \\gg 1$ indicates compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.",
          " ",
          " \\subsection{Phase Segmentation}",
          " \\label{sec:phase-segmentation}",
          " ",
          "-We partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}.",
          "-",
          "-\\paragraph{Attention sparsity.}",
          "-For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:",
          "-\\begin{equation}",
          "-    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].",
          "-    \\label{eq:attn-sparsity}",
          "-\\end{equation}",
          "-The per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.",
          "-",
          "-\\paragraph{Quantile-based segmentation.}",
          "-Tokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by the tercile boundaries of $\\{\\sigma_i\\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.",
          "+We partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}. For each query position, we compute the fraction of key positions receiving negligible attention (${<}1\\%$ of the maximum), averaged across heads, yielding a per-position sparsity score $\\sigma_i$. Tokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by tercile boundaries; segments shorter than 10 tokens are merged with adjacent phases. Full details in Appendix~\\ref{app:compound-formulation}."
        ]
      }
    ],
    "originalFile": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer with $L$ layers and $H$ heads per layer. Let $s \\in (0,1)$ denote a unified sparsity budget.\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields \\emph{compound sparsity}. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nFor a text segment, let $r_c = \\text{PPL}_c / \\text{PPL}_d$ denote the relative perplexity degradation under condition $c \\in \\{a\\text{(attn-only)}, k\\text{(kv-only)}, b\\text{(both)}\\}$. The Interaction Index is:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ additive independence. We adopt an additive null (verified against a multiplicative null in Appendix~\\ref{app:multiplicative-null}). Because the II distribution is right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nWe partition each generated sequence into three phases based on local attention sparsity, adapting ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into \\textbf{high-}, \\textbf{mid-}, and \\textbf{low-sparsity} phases by the tercile boundaries of $\\{\\sigma_i\\}$. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01C5iV5DUw3sKcJkzqqMcY7x`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
  "old_string": "\\paragraph{Deployment implications.}\nUniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \\emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.\n\\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.\n\\item All experiments at 7B scale; scaling behavior is untested.\n\\end{itemize}\nExtended discussion in Appendix~\\ref{app:limitations}.",
  "new_string": "\\paragraph{Deployment implications.}\nUniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.\nA \\emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.\n\n\\paragraph{Future directions.}\nA phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.\nCompleting the mechanistic picture---particularly the model-dependent entropy component (\\S\\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "748d9d71-c7b2-4674-ae6c-d4ad22dc203e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 75 · 2026-05-14T12:46:49.005Z_

<details><summary>↩ Tool result · `toolu_01C5iV5DUw3sKcJkzqqMcY7x`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "0b90e26a-9f25-4845-8a2e-c7baa83bbbb6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
    "oldString": "\\paragraph{Deployment implications.}\nUniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \\emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.\n\\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.\n\\item All experiments at 7B scale; scaling behavior is untested.\n\\end{itemize}\nExtended discussion in Appendix~\\ref{app:limitations}.",
    "newString": "\\paragraph{Deployment implications.}\nUniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.\nA \\emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.\n\n\\paragraph{Future directions.}\nA phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.\nCompleting the mechanistic picture---particularly the model-dependent entropy component (\\S\\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe qualitative direction of our findings---that importance-based eviction degrades in diffuse-attention phases---may seem intuitive. The surprise is quantitative: $69$--$274{\\times}$ severity amplification far exceeds a naive prediction; the crossover at $s{=}0.25$ (importance-based eviction simultaneously outperforming and underperforming random across phases) cannot be derived from the observation that ``scores are noisier when attention is diffuse.'' % exp_id: bf16_importance_s015..s030\n\n\\paragraph{Random masking as falsification control.}\nIf compound severity amplification were inherent to applying two compression methods jointly, random eviction should exhibit a comparable phase gradient. It does not: random eviction fails 7/8 paired permutation tests across both models, with the single exception (Qwen $s{=}0.30$, $d_z{=}{-}0.04$) showing negligible effect size. This isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Cross-model replication.}\nThe phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation\n\n\\paragraph{Deployment implications.}\nUniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \\emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.\n\\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.\n\\item All experiments at 7B scale; scaling behavior is untested.\n\\end{itemize}\nExtended discussion in Appendix~\\ref{app:limitations}.\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 14,
        "newStart": 11,
        "newLines": 9,
        "lines": [
          " The phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation",
          " ",
          " \\paragraph{Deployment implications.}",
          "-Uniform compression budgets across all inference steps are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases. A \\emph{phase-aware controller} could allocate higher capacity to low-sparsity phases and reclaim the budget in high-sparsity phases where compound behavior is near-additive.",
          "+Uniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.",
          "+A \\emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.",
          " ",
          "-\\subsection{Limitations}",
          "-\\label{sec:limitations}",
          "-",
          "-\\begin{itemize}[nosep,leftmargin=*]",
          "-\\item Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) is future work.",
          "-\\item Evaluation is limited to MATH-500; other reasoning tasks may induce different phase structures.",
          "-\\item All experiments at 7B scale; scaling behavior is untested.",
          "-\\end{itemize}",
          "-Extended discussion in Appendix~\\ref{app:limitations}.",
          "+\\paragraph{Future directions.}",
          "+A phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.",
          "+Completing the mechanistic picture---particularly the model-dependent entropy component (\\S\\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality."
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

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01XhD43NHoREuczyyrjjtBXG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
  "old_string": "These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.",
  "new_string": "These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.\n\n\\section*{Limitations}\n\nBoth models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "9de0b9c6-aec4-4d98-9794-aa1fa3edf82b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 77 · 2026-05-14T12:46:53.666Z_

<details><summary>↩ Tool result · `toolu_01XhD43NHoREuczyyrjjtBXG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "3675748e-7ae1-4318-8a94-8fb68d7251c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
    "oldString": "These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.",
    "newString": "These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.\n\n\\section*{Limitations}\n\nBoth models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation.",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not fixed but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Our contributions:\n\\textbf{(C1)} Compound severity depends qualitatively on eviction strategy: importance-based eviction produces phase-modulated interaction ($\\Delta = 0.39$--$14.59$) while random eviction shows none (7/8 conditions).\n\\textbf{(C2)} Under importance-based eviction, the severity gradient grows monotonically with sparsity ($d_z$: $0.44 \\to 0.80$, all $p_{\\text{Bonf}} < 0.005$).\n\\textbf{(C3)} A crossover emerges: importance-based eviction simultaneously outperforms and underperforms random across phases.\n\\textbf{(C4)} Discrimination collapse---head pruning degrading importance score quality---is the robust mechanism (confirmed in all 16 conditions).\n\\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\\rho{=}1.0$, gradient $p{=}0.043$) at ${\\sim}1/5$ absolute magnitude.\n\\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.\nThese findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 3,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\\rho{=}1.0$, gradient $p{=}0.043$) at ${\\sim}1/5$ absolute magnitude.",
          " \\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.",
          " These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.",
          "+",
          "+\\section*{Limitations}",
          "+",
          "+Both models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation."
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01CwmC62gZHQ624US8yRsuoY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "(\\S\\ref{sec:analysis})",
  "new_string": "(\\S\\ref{sec:discrimination-collapse})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "a3953866-ed34-44cd-9ac0-69ea39c91ee1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 79 · 2026-05-14T12:46:54.595Z_

<details><summary>↩ Tool result · `toolu_01CwmC62gZHQ624US8yRsuoY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "63476bf7-131f-4250-828d-6743b62bd234",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "oldString": "(\\S\\ref{sec:analysis})",
    "newString": "(\\S\\ref{sec:discrimination-collapse})",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita-acl2019, michel-neurips2019}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "     \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).",
          "     \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).",
          "-    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).",
          "+    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:discrimination-collapse}).",
          " \\end{enumerate}",
          " ",
          " These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe."
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_019W4dymeHQs5NhQtJFW4ttX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
  "old_string": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.",
  "new_string": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "570a46cc-5403-4400-8e05-7c4575a6f252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 81 · 2026-05-14T12:46:58.162Z_

<details><summary>↩ Tool result · `toolu_019W4dymeHQs5NhQtJFW4ttX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "08c07cd0-a417-41c4-a7b4-d897572db5f5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
    "oldString": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.",
    "newString": "These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita-acl2019, michel-neurips2019}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:discrimination-collapse}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 4,
        "newStart": 30,
        "newLines": 3,
        "lines": [
          " \\end{enumerate}",
          " ",
          " These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.",
          "-The remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations."
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

_source line 82_

<details open><summary>🔧 Tool call — Edit · `toolu_01YSqNjV6yXHY7SGoRERV4GG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
  "old_string": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000",
  "new_string": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "b95cbcbd-0ed5-4f84-b0f9-f2ad7ada7cbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 83 · 2026-05-14T12:47:08.460Z_

<details><summary>↩ Tool result · `toolu_01YSqNjV6yXHY7SGoRERV4GG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "394ab010-a13f-4c68-b5e5-b01655ac1f30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
    "oldString": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000",
    "newString": "consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}",
    "originalFile": "% Appendix sections for content moved from results.tex (§5.5 and §5.6)\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\n\\section{Statistical Validation Details}\n\\label{app:stat-validation-details}\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Additional effect size analysis.}\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\n",
    "structuredPatch": [
      {
        "oldStart": 58,
        "oldLines": 3,
        "newStart": 58,
        "newLines": 21,
        "lines": [
          " \\paragraph{Additional effect size analysis.}",
          " For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000",
          " At higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000",
          "+",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}",
          "+\\label{tab:cohens-d}",
          "+\\begin{tabular}{@{}lcccc@{}}",
          "+\\toprule",
          "+$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\",
          "+\\midrule",
          "+0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015",
          "+0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020",
          "+0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025",
          "+0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030",
          "+\\bottomrule",
          "+\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}",
          "+\\end{tabular}",
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

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_01TCFgspxfJ4Qc5HeJMbJwYJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
  "old_string": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline.",
  "new_string": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention; BOS always retained) against a \\textbf{random} baseline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "a92626a3-2aef-4394-b551-ea917b088201",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKHiNSqj3ikAHNQcmUibrf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8085,
      "cache_read_input_tokens": 86168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8085
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

_source line 85 · 2026-05-14T12:47:09.675Z_

<details><summary>↩ Tool result · `toolu_01TCFgspxfJ4Qc5HeJMbJwYJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "91068128-fe81-4552-8b4d-c303fdce8756",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
    "oldString": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline.",
    "newString": "We compare \\textbf{importance-based} eviction (position-normalized cumulative attention; BOS always retained) against a \\textbf{random} baseline.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA). \\textbf{DeepSeek-R1-Distill-Qwen-7B} \\cite{deepseek-r1-2025}, distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. \\textbf{Qwen2.5-7B-Instruct} \\cite{qwen25-2024} provides cross-model replication with standard instruction tuning rather than reasoning distillation.\nBoth models are loaded in \\texttt{bfloat16} with eager attention to permit direct manipulation of attention matrices.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B; \\texttt{bfloat16} eliminated all occurrences.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of MATH-500 \\cite{math500-neurips2021}, sampling uniformly across problem categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\n\\subsection{Configuration and Metrics}\n\\label{sec:config-metrics}\n\nWe apply symmetric compound sparsity: for level $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.\n\nEach sequence is segmented into three reasoning phases using the quantile-based method of \\S\\ref{sec:phase-segmentation} ($\\texttt{min\\_phase\\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\\ref{eq:ii}) and severity gradient (Eq.~\\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\\ref{app:stat-validation-details}.\\footnote{Experiments were conducted on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs.}\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 6,
        "newStart": 17,
        "newLines": 6,
        "lines": [
          " \\subsection{Configuration and Metrics}",
          " \\label{sec:config-metrics}",
          " ",
          "-We apply symmetric compound sparsity: for level $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \\textbf{importance-based} eviction (position-normalized cumulative attention, Eq.~\\ref{eq:kv-importance}; BOS always retained) against a \\textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.",
          "+We apply symmetric compound sparsity: for level $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, the same fraction $s$ of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only eviction, and compound. We compare \\textbf{importance-based} eviction (position-normalized cumulative attention; BOS always retained) against a \\textbf{random} baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.",
          " ",
          " Each sequence is segmented into three reasoning phases using the quantile-based method of \\S\\ref{sec:phase-segmentation} ($\\texttt{min\\_phase\\_length}{=}10$). For each condition and phase, we compute the Interaction Index (Eq.~\\ref{eq:ii}) and severity gradient (Eq.~\\ref{eq:gradient}), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap ($B{=}10{,}000$) with paired permutation tests; details in Appendix~\\ref{app:stat-validation-details}.\\footnote{Experiments were conducted on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs.}"
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

_source line 86_

<details><summary>Logged reasoning block</summary>

```text
All edits succeeded. Now I need to also update the appendix.tex to use the correct citation keys. Let me check: my earlier edit to appendix.tex used the OLD citation keys (voita2019heads, michel2019sixteen). But the current codebase uses the new keys (voita-acl2019, michel-neurips2019). Let me fix that.

Let me re-read appendix.tex to see the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "ecbfcf4f-0b7b-4815-a401-a1998db44fc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3kwGE7oBP3tYDdfoCLosy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5236,
      "cache_read_input_tokens": 94253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5236
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

_source line 87_

All edits succeeded. Now let me verify the appendix.tex citation keys match the updated bibliography, and do the final verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "91224f6f-4968-4f9c-81a9-e6d352250dfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3kwGE7oBP3tYDdfoCLosy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5236,
      "cache_read_input_tokens": 94253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5236
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

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01K6uB5q2XGoHV3NCyKCod3s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "09df2e9f-87eb-4fd0-9dd8-d49ab643cc9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3kwGE7oBP3tYDdfoCLosy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5236,
      "cache_read_input_tokens": 94253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5236
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

_source line 89 · 2026-05-14T12:47:15.460Z_

<details><summary>↩ Tool result · `toolu_01K6uB5q2XGoHV3NCyKCod3s`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:compound-formulation}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	\section{Bootstrap and Permutation Details}
41	\label{app:bootstrap-details}
42	
43	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.
44	
45	The permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\text{Bonf}} = 0.0032$).
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e726c621-f768-4c85-95c9-e655fe2c7a35",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Compound Sparsity Formulation}\n\\label{app:compound-formulation}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n\\section{Bootstrap and Permutation Details}\n\\label{app:bootstrap-details}\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.\n\nThe permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \\geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$).\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01L45Z5KDFjxaxPvQpakRDeZ`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex",
  "description": "Count lines in all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "29a3ba80-41bf-4136-b6ce-2723902cde28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3kwGE7oBP3tYDdfoCLosy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5236,
      "cache_read_input_tokens": 94253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5236
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

_source line 91 · 2026-05-14T12:47:16.133Z_

<details><summary>↩ Tool result · `toolu_01L45Z5KDFjxaxPvQpakRDeZ`</summary>

```text
   13 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
   46 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex
   45 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
   83 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
   78 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex
   31 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex
   15 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex
   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex
   32 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex
   46 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex
   22 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex
    9 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
  119 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex
  558 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "27a14a45-bd30-41f3-b24a-d6a63e2bf44b",
  "tool_use_result": {
    "stdout": "   13 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex\n   46 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex\n   45 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex\n   83 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex\n   78 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex\n   31 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex\n   15 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex\n   19 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex\n   32 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex\n   46 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex\n   22 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex\n    9 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex\n  119 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex\n  558 total",
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

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
I need to fix the citation keys in appendix.tex. The current version uses `voita2019heads, michel2019sixteen` but the bibliography now uses `voita-acl2019, michel-neurips2019`.

Let me fix that, then do the full verification.

Line counts for main text files:
- abstract.tex: 13
- introduction.tex: 32
- related_work.tex: 9 (very short, each paragraph is one long line)


- background.tex: 31
- methodology.tex: 22
- results.tex: 119
- discussion.tex: 19
- conclusion.tex: 15

That gives me 260 lines total, well under the 380-line target, though I should account for long lines that wrap in the PDF. Now I need to verify the cross-references and check the numbers throughout the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "6dcad85d-0786-408f-9657-228c348af686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFp6QoFyZop1jZuyzc8ES8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 99489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
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

_source line 93_

Need to fix citation keys in appendix.tex to match the updated bibliography.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d54839a0-952a-4581-a8db-3e2f1447b764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFp6QoFyZop1jZuyzc8ES8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 99489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
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

_source line 94_

<details open><summary>🔧 Tool call — Edit · `toolu_01HzXUuTi5LDrkpY6yZT826C`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "old_string": "\\cite{voita2019heads, michel2019sixteen}",
  "new_string": "\\cite{voita-acl2019, michel-neurips2019}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "77547138-7313-4803-9068-32446b981f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFp6QoFyZop1jZuyzc8ES8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 99489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2461
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

_source line 95 · 2026-05-14T12:47:25.072Z_

<details><summary>↩ Tool result · `toolu_01HzXUuTi5LDrkpY6yZT826C`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "f3910bd7-1133-4677-acb3-a21ce52c53a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
    "oldString": "\\cite{voita2019heads, michel2019sixteen}",
    "newString": "\\cite{voita-acl2019, michel-neurips2019}",
    "originalFile": "\\section{Compound Sparsity Formulation}\n\\label{app:compound-formulation}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n\\section{Bootstrap and Permutation Details}\n\\label{app:bootstrap-details}\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen. This motivates our use of median-based test statistics and nonparametric bootstrap inference throughout.\n\nThe permutation null distributions ($10{,}000$ permutations of strategy labels) are approximately symmetric around zero at all sparsity levels, with no observed median difference exceeding the $2.5$th or $97.5$th percentile under any permutation at $s \\geq 0.20$ (Bonferroni-corrected). At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$).\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{app:compound-formulation}",
          " ",
          " \\paragraph{Attention head pruning.}",
          "-Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita2019heads, michel2019sixteen}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:",
          "+Heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:",
          " \\begin{equation}",
          "     \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.",
          "     \\label{eq:head-mask}"
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

_source line 96_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the verification. I need to:

1. Check all \ref{} have matching \label{}
2. Check no numbers were changed
3. Estimate page count

Let me run the verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "1d4d7bea-5262-4bdb-9839-26e412c2f2ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQKLPByjiw4a6RFBHzXBuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 101950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 97_

Now let me verify cross-references and number integrity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "f1791b5b-d292-489b-911f-43a825070301",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQKLPByjiw4a6RFBHzXBuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 101950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01VurkZT1UMDex2CgxuK6Ff9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper && grep -ohP '\\\\\\\\ref\\{[^}]+\\}' *.tex | sort -u | sed 's/\\\\\\\\ref{//;s/}//' > /tmp/refs.txt && grep -ohP '\\\\\\\\label\\{[^}]+\\}' *.tex | sort -u | sed 's/\\\\\\\\label{//;s/}//' > /tmp/labels.txt && echo \"=== refs without matching labels ===\" && comm -23 /tmp/refs.txt /tmp/labels.txt && echo \"=== labels without refs (orphans) ===\" && comm -13 /tmp/refs.txt /tmp/labels.txt",
  "description": "Check cross-reference consistency between \\ref and \\label"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "396bb83c-0726-4f74-a07a-fac47fd7396d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQKLPByjiw4a6RFBHzXBuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 101950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 99 · 2026-05-14T12:47:32.612Z_

<details><summary>↩ Tool result · `toolu_01VurkZT1UMDex2CgxuK6Ff9`</summary>

```text
=== refs without matching labels ===
=== labels without refs (orphans) ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e3313c60-cf22-4d2e-8045-79b32d44a227",
  "tool_use_result": {
    "stdout": "=== refs without matching labels ===\n=== labels without refs (orphans) ===",
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01JUzWLfzTZfSQKHtMf15onX`</summary>

```json
{
  "command": "echo \"=== main.tex includes ===\" && grep '\\\\input{' main.tex && echo && echo \"=== Files with sec:analysis references ===\" && grep -rn 'sec:analysis' *.tex && echo && echo \"=== Files with sec:phase-seg} (not sec:phase-segmentation) ===\" && grep -rn 'sec:phase-seg}' *.tex",
  "description": "Verify main.tex structure and check for stale references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "8de63638-ee47-4187-8255-508b08c4bfe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQKLPByjiw4a6RFBHzXBuS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 101950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 101 · 2026-05-14T12:47:34.802Z_

<details><summary>↩ Tool result · `toolu_01JUzWLfzTZfSQKHtMf15onX`</summary>

```text
=== main.tex includes ===
\input{abstract}
\input{introduction}
\input{related_work}
\input{background}
\input{methodology}
\input{results}
\input{discussion}
\input{conclusion}
\input{appendix}
\input{appendix_results}
\input{appendix_disc_analysis}

=== Files with sec:analysis references ===
analysis.tex:3:\label{sec:analysis}
analysis.tex:44:\label{sec:analysis-implications}

=== Files with sec:phase-seg} (not sec:phase-segmentation) ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "dd46347d-c428-44cf-8338-325eca21c18b",
  "tool_use_result": {
    "stdout": "=== main.tex includes ===\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{discussion}\n\\input{conclusion}\n\\input{appendix}\n\\input{appendix_results}\n\\input{appendix_disc_analysis}\n\n=== Files with sec:analysis references ===\nanalysis.tex:3:\\label{sec:analysis}\nanalysis.tex:44:\\label{sec:analysis-implications}\n\n=== Files with sec:phase-seg} (not sec:phase-segmentation) ===",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
Cross-reference check results:
1. **All refs have matching labels** ✓ (no orphan refs)
2. **sec:analysis references**: Only in analysis.tex itself (which is no longer included in main.tex) ✓
3. **sec:phase-seg**: No stale references ✓

Now let me verify that no experimental numbers were changed by comparing key numbers in the new files against the originals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "017dddb5-8164-4927-bf36-9edcb8151141",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAXqULz8S9KYLbBLrvQtzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 102474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 103_

Cross-references are clean. Let me verify no numbers were modified by checking key metrics in the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "6661cb0e-a997-4556-b9cb-26078a6d5180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAXqULz8S9KYLbBLrvQtzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 102474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Dbxb4aUxPeQaapFwHUhazz`</summary>

```json
{
  "command": "echo \"=== Key numbers in results.tex ===\" && grep -oP '\\d+\\.\\d+' results.tex | head -60 && echo && echo \"=== Key numbers in conclusion.tex ===\" && grep -oP '\\d+\\.\\d+' conclusion.tex && echo && echo \"=== Key numbers in discussion.tex ===\" && grep -oP '\\d+\\.\\d+' discussion.tex && echo && echo \"=== discrimination metrics table ===\" && grep -A20 'tab:discrimination-metrics' results.tex | grep -P '[-0-9.]+'",
  "description": "Verify key experimental numbers are preserved"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "8d5570a0-ce44-4c7d-a223-f46d6a404a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAXqULz8S9KYLbBLrvQtzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 102474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01UtWKJWKVBwc6BMmztfGhfe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "0489d7ef-7f46-4eea-acb8-d56f7b2f2db3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAXqULz8S9KYLbBLrvQtzd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 721,
      "cache_read_input_tokens": 102474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 721
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

_source line 106 · 2026-05-14T12:47:49.724Z_

<details><summary>↩ Tool result · `toolu_01UtWKJWKVBwc6BMmztfGhfe`</summary>

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{discussion}
37	\input{conclusion}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	\input{appendix_results}
44	\input{appendix_disc_analysis}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "65594437-e558-4763-98a0-7078897a2292",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_results}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-14T12:47:49.825Z_

<details><summary>↩ Tool result · `toolu_01Dbxb4aUxPeQaapFwHUhazz`</summary>

```text
=== Key numbers in results.tex ===
0.39
0.15
14.59
0.30
0.02
1.54
0.15
0.30
0.006
0.053
0.9
1.7
0.15
0.006
0.081
0.398
0.39
0.15
0.093
0.097
0.103
0.01
1.1
0.20
0.015
0.203
1.496
1.48
0.20
0.292
0.350
0.276
0.02
0.9
0.25
0.032
1.118
7.196
7.16
0.25
0.818
0.932
1.363
0.54
1.7
0.30
0.053
2.283
14.639
14.59
0.30
2.503
2.592
4.041
1.54
1.6
3.8
4.8
2.0
0.25

=== Key numbers in conclusion.tex ===
0.39
14.59
0.44
0.80
0.005
2.5
1.0
0.043

=== Key numbers in discussion.tex ===
0.25
0.30
0.04
1.0
0.043

=== discrimination metrics table ===
Head pruning makes the cumulative KV importance distribution more uniform---a \emph{discrimination collapse} that explains the phase-strategy interaction. Table~\ref{tab:discrimination-metrics} shows consistent reductions across both models: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$. When importance scores lose discriminative power, importance-based eviction degenerates toward arbitrary selection---explaining the crossover (\S\ref{sec:crossover}). Random eviction is immune because its decisions are independent of score quality. A secondary entropy redistribution effect is model-dependent (Appendix~\ref{app:entropy-redistribution}).
\caption{Discrimination collapse: $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction.}
\label{tab:discrimination-metrics}
DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d39af830-b319-478f-97e4-be27df6907b7",
  "tool_use_result": {
    "stdout": "=== Key numbers in results.tex ===\n0.39\n0.15\n14.59\n0.30\n0.02\n1.54\n0.15\n0.30\n0.006\n0.053\n0.9\n1.7\n0.15\n0.006\n0.081\n0.398\n0.39\n0.15\n0.093\n0.097\n0.103\n0.01\n1.1\n0.20\n0.015\n0.203\n1.496\n1.48\n0.20\n0.292\n0.350\n0.276\n0.02\n0.9\n0.25\n0.032\n1.118\n7.196\n7.16\n0.25\n0.818\n0.932\n1.363\n0.54\n1.7\n0.30\n0.053\n2.283\n14.639\n14.59\n0.30\n2.503\n2.592\n4.041\n1.54\n1.6\n3.8\n4.8\n2.0\n0.25\n\n=== Key numbers in conclusion.tex ===\n0.39\n14.59\n0.44\n0.80\n0.005\n2.5\n1.0\n0.043\n\n=== Key numbers in discussion.tex ===\n0.25\n0.30\n0.04\n1.0\n0.043\n\n=== discrimination metrics table ===\nHead pruning makes the cumulative KV importance distribution more uniform---a \\emph{discrimination collapse} that explains the phase-strategy interaction. Table~\\ref{tab:discrimination-metrics} shows consistent reductions across both models: Gini decreases by $0.010$--$0.081$ and CV by $0.05$--$1.66$. When importance scores lose discriminative power, importance-based eviction degenerates toward arbitrary selection---explaining the crossover (\\S\\ref{sec:crossover}). Random eviction is immune because its decisions are independent of score quality. A secondary entropy redistribution effect is model-dependent (Appendix~\\ref{app:entropy-redistribution}).\n\\caption{Discrimination collapse: $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ (post-pruning minus baseline) under importance-based eviction.}\n\\label{tab:discrimination-metrics}\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\",
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

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
Everything looks good:

1. **Cross-references**: All refs have matching labels, no orphans. ✓
2. **sec:analysis**: Only referenced in analysis.tex (not included in main.tex anymore). ✓
3. **sec:phase-seg**: No stale references. ✓
4. **Numbers**: All key metrics preserved:
   - Delta values: 0.39, 1.48, 7.16, 14.59 ✓
   - Random deltas: 0.01, -0.02, 0.54, 1.54 ✓
   - Table values: all II values preserved exactly ✓
   - d_z values: 0.44, 0.80, 0.28, 1.02 ✓
   - p-values: 0.005, 0.043, 0.012 ✓
   - Discrimination metrics: all Gini/CV values exact ✓
5. **main.tex**: analysis.tex removed, all other files included correctly. ✓

Now I'm estimating the page count by looking at the line counts across the main text files.

The total comes to about 260 lines of .tex source, but I need to account for how these wrap in the actual PDF. In ACL's two-column format, each source line can expand to multiple PDF lines depending on character count. Let me recalculate based on what we've actually removed and moved around. We cut background.tex significantly by moving equations to the appendix, and completely removed analysis.tex from the main text, which should bring the page count down from the original ~15 pages. merged discrimination collapse into results)
3. results.tex: 154→119 lines (removed tab:aggregate-ii, moved tab:cohens-d, compressed text)
4. discussion.tex: already had been compressed, then I removed Limitations and added Future directions. ~66 original → 19 current
5. conclusion.tex: already compressed, added Limitations section. ~30 original → 15 current (Limitations is after main body)
6. introduction.tex: removed roadmap line. 33→32 lines

The files I read were already partially compressed by someone. The original task description said the files were:
- background.tex (112 lines) → now 31
- results.tex (154 lines) → now 119
- analysis.tex (61 lines) → now 0 (removed from main)
- discussion.tex (66 lines) → now 19
- conclusion.tex (30 lines) → now 15

That's substantial compression. Now I'm estimating the page count by breaking down each section. Results is mostly tables and figures taking up about 1.6 pages of space, while background, methodology, introduction, and related work together account for roughly 2.5 pages. The discussion and conclusion sections are quite lean at under a page combined.

The total comes to around 6.5 pages, which leaves room within the 8-page limit. I should note that abstracts and limitations sections typically don't count toward page limits in conference submissions, so the actual effective page count is even lower.

Let me verify the structure is correct for the submission format. Looking at how the files are organized, the conclusion flows into the limitations section before the bibliography and appendix, which matches the standard ACL/EMNLP format requirements. I'm verifying the final structure of all the files to make sure everything is in the right order and follows the ARR/EMNLP 2026 guidelines correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "ed4f7d2d-425a-4c36-95be-e036984837e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BebPaoacK9nfGCp4syQar1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 103195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 109_

All cross-references are consistent, no numbers were modified, and the main.tex structure is correct. Let me do a final read of the key modified files to confirm everything is clean.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "e6adba10-f748-43d1-a77d-42268fb1f465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BebPaoacK9nfGCp4syQar1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 103195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_016DXtUkApY6QEG8UNkSSU4G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "01cb3ca8-88f6-44c3-9c02-bded393aba78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BebPaoacK9nfGCp4syQar1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 103195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 111 · 2026-05-14T12:48:25.159Z_

<details><summary>↩ Tool result · `toolu_016DXtUkApY6QEG8UNkSSU4G`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita-acl2019, michel-neurips2019}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:results}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:discrimination-collapse}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "2f7df888-e520-4b45-96e0-38d041d52ede",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita-acl2019, michel-neurips2019}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:discrimination-collapse}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01HvWbvPDWyiNqLiejouDRFw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "20a2e563-4369-4b5d-80fa-80753c676493",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BebPaoacK9nfGCp4syQar1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 103195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 113 · 2026-05-14T12:48:25.511Z_

<details><summary>↩ Tool result · `toolu_01HvWbvPDWyiNqLiejouDRFw`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not fixed but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Our contributions:
5	\textbf{(C1)} Compound severity depends qualitatively on eviction strategy: importance-based eviction produces phase-modulated interaction ($\Delta = 0.39$--$14.59$) while random eviction shows none (7/8 conditions).
6	\textbf{(C2)} Under importance-based eviction, the severity gradient grows monotonically with sparsity ($d_z$: $0.44 \to 0.80$, all $p_{\text{Bonf}} < 0.005$).
7	\textbf{(C3)} A crossover emerges: importance-based eviction simultaneously outperforms and underperforms random across phases.
8	\textbf{(C4)} Discrimination collapse---head pruning degrading importance score quality---is the robust mechanism (confirmed in all 16 conditions).
9	\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\rho{=}1.0$, gradient $p{=}0.043$) at ${\sim}1/5$ absolute magnitude.
10	\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.
11	These findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.
12	
13	\section*{Limitations}
14	
15	Both models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "a4dc1c71-cd18-4fc8-a459-a131caefeffa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not fixed but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Our contributions:\n\\textbf{(C1)} Compound severity depends qualitatively on eviction strategy: importance-based eviction produces phase-modulated interaction ($\\Delta = 0.39$--$14.59$) while random eviction shows none (7/8 conditions).\n\\textbf{(C2)} Under importance-based eviction, the severity gradient grows monotonically with sparsity ($d_z$: $0.44 \\to 0.80$, all $p_{\\text{Bonf}} < 0.005$).\n\\textbf{(C3)} A crossover emerges: importance-based eviction simultaneously outperforms and underperforms random across phases.\n\\textbf{(C4)} Discrimination collapse---head pruning degrading importance score quality---is the robust mechanism (confirmed in all 16 conditions).\n\\textbf{(C5)} Cross-model replication on Qwen2.5-7B-Instruct ($\\rho{=}1.0$, gradient $p{=}0.043$) at ${\\sim}1/5$ absolute magnitude.\n\\textbf{(C6)} Sub-exponential growth with decelerating terminal rate.\nThese findings motivate phase-aware compound sparsity controllers that dynamically allocate compression budgets across reasoning phases.\n\n\\section*{Limitations}\n\nBoth models share the Qwen2 architecture; cross-architecture validation (e.g., LLaMA, Mistral) remains future work. All experiments are at the 7B scale; whether severity gradients persist at larger scales is untested. Evaluation is limited to MATH-500; different reasoning domains may induce different phase structures. The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation. While discrimination collapse (Gini/CV reduction) is consistent across all conditions, the entropy redistribution component replicates on only 2/4 sparsity levels for Qwen, suggesting model-dependent modulation.\n",
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

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_01P4LERaGqN78EGHWkjxmxFX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "8e92c907-7506-43a6-af26-183591ce240f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BebPaoacK9nfGCp4syQar1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 428,
      "cache_creation_input_tokens": 1310,
      "cache_read_input_tokens": 103195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1310
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

_source line 115 · 2026-05-14T12:48:25.859Z_

<details><summary>↩ Tool result · `toolu_01P4LERaGqN78EGHWkjxmxFX`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	The qualitative direction of our findings---that importance-based eviction degrades in diffuse-attention phases---may seem intuitive. The surprise is quantitative: $69$--$274{\times}$ severity amplification far exceeds a naive prediction; the crossover at $s{=}0.25$ (importance-based eviction simultaneously outperforming and underperforming random across phases) cannot be derived from the observation that ``scores are noisier when attention is diffuse.'' % exp_id: bf16_importance_s015..s030
6	
7	\paragraph{Random masking as falsification control.}
8	If compound severity amplification were inherent to applying two compression methods jointly, random eviction should exhibit a comparable phase gradient. It does not: random eviction fails 7/8 paired permutation tests across both models, with the single exception (Qwen $s{=}0.30$, $d_z{=}{-}0.04$) showing negligible effect size. This isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
9	
10	\paragraph{Cross-model replication.}
11	The phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation
12	
13	\paragraph{Deployment implications.}
14	Uniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.
15	A \emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.
16	
17	\paragraph{Future directions.}
18	A phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.
19	Completing the mechanistic picture---particularly the model-dependent entropy component (\S\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "069253dd-491a-48bc-bd94-84757ddfc290",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe qualitative direction of our findings---that importance-based eviction degrades in diffuse-attention phases---may seem intuitive. The surprise is quantitative: $69$--$274{\\times}$ severity amplification far exceeds a naive prediction; the crossover at $s{=}0.25$ (importance-based eviction simultaneously outperforming and underperforming random across phases) cannot be derived from the observation that ``scores are noisier when attention is diffuse.'' % exp_id: bf16_importance_s015..s030\n\n\\paragraph{Random masking as falsification control.}\nIf compound severity amplification were inherent to applying two compression methods jointly, random eviction should exhibit a comparable phase gradient. It does not: random eviction fails 7/8 paired permutation tests across both models, with the single exception (Qwen $s{=}0.30$, $d_z{=}{-}0.04$) showing negligible effect size. This isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Cross-model replication.}\nThe phase-strategy interaction replicates with perfect ordinal agreement (Spearman $\\rho{=}1.0$, gradient permutation $p{=}0.043$). All eight Wilcoxon tests reject $H_0$. However, Qwen's absolute magnitude is ${\\sim}1/5$ of DeepSeek's, suggesting distillation amplifies the interaction---a hypothesis testable by comparing distilled and non-distilled variants at matched scale. % exp_id: cross_model_correlation\n\n\\paragraph{Deployment implications.}\nUniform compression budgets are suboptimal for reasoning models: compound severity concentrates in low-sparsity phases where discrimination collapse renders importance-based eviction unreliable.\nA \\emph{phase-aware compression budget}---allocating lower sparsity to low-sparsity phases and reclaiming capacity in high-sparsity phases---could mitigate severity amplification while preserving compression gains.\n\n\\paragraph{Future directions.}\nA phase-gated controller that monitors attention sparsity in real time and dynamically adjusts compound sparsity budgets per phase is the natural next step.\nCompleting the mechanistic picture---particularly the model-dependent entropy component (\\S\\ref{sec:discrimination-collapse})---and scaling to larger models and diverse reasoning tasks would establish generality.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 116_

<details><summary>Logged reasoning block</summary>

```text
Everything looks clean. Let me now provide a summary of all changes made.

Let me compile the final line counts and estimated page counts:

Main text files:
- abstract.tex: 13 lines
- introduction.tex: 33→32 lines
- related_work.tex: 9 lines (was already compact)
- background.tex: 78→31 lines (moved to appendix)
- methodology.tex: 22 lines (minor edit)
- results.tex: 154→119 lines (merged analysis, removed redundant tables)
- discussion.tex: 25→19 lines (removed Limitations, added Future directions)


- conclusion.tex: 12→15 lines (added Limitations section)

I removed analysis.tex from the main text entirely. Looking at the total reduction, I'm getting 260 lines after all edits compared to 392 before, which is a 34% cut. But wait, I'm noticing the original numbers don't quite align with what was described in the task—background was supposed to be 112 lines and analysis 61 lines, not what I'm calculating here.

I realize the files were already partially compressed before I started working on them, so let me just focus on the current state. Now I'm estimating the page contribution for an ACL two-column format. The main sections break down to roughly 0.3 pages for the introduction, 0.5 for related work, 0.6 for background with the equations and compressed text, 0.5 for methodology, 2.5 for results with the tables and figures, 0.4 for discussion, and 0.3 for conclusion. Adding those up gives me about 5.1 pages of main text, which should fit within the conference limits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "74775037-91a2-4fb7-96cb-ce31611c7460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o8AE6R7suk4pgTzBqzeaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4916,
      "cache_read_input_tokens": 104505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4916
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

_source line 117_

All changes are complete. Summary:

### Changes made

| File | Before | After | Action |
|------|--------|-------|--------|
| `background.tex` | 78 lines | 31 lines | Moved compound sparsity formulation (4 equations) + phase segmentation details to appendix |
| `results.tex` | 154 lines | 119 lines | Removed redundant `tab:aggregate-ii`; moved `tab:cohens-d` to appendix; merged discrimination collapse (from analysis) as §5.7 |
| `analysis.tex` | 46 lines | removed | Content merged into results.tex; `\input{analysis}` removed from main.tex |
| `discussion.tex` | 25 lines | 19 lines | Removed Limitations subsection (consolidated); added Future directions |
| `conclusion.tex` | 12 lines | 15 lines | Added `\section*{Limitations}` (consolidated from discussion + conclusion) |
| `introduction.tex` | 33 lines | 32 lines | Removed roadmap sentence; updated `sec:analysis` → `sec:discrimination-collapse` |
| `methodology.tex` | 22 lines | 22 lines | Removed orphaned `Eq.~\ref{eq:kv-importance}` reference |
| `appendix.tex` | 11 lines | 45 lines | Added compound sparsity formulation section with all moved equations |
| `appendix_results.tex` | 60 lines | 78 lines | Appended `tab:cohens-d` table |
| `main.tex` | 47 lines | 46 lines | Removed `\input{analysis}` |

### Verification
- All `\ref{}` have matching `\label{}` — zero orphan references
- No experimental numbers modified (all metrics, p-values, Cohen's d, II values preserved)
- `\section*{Limitations}` appears after Conclusion, before `\bibliography` (EMNLP format)
- Estimated main text: ~6–7 pages (well within 8-page limit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "uuid": "d29a1c07-b886-4b92-aad5-179072b78df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011o8AE6R7suk4pgTzBqzeaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4916,
      "cache_read_input_tokens": 104505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4916
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

_source line 118_

All changes are complete. Summary:

### Changes made

| File | Before | After | Action |
|------|--------|-------|--------|
| `background.tex` | 78 lines | 31 lines | Moved compound sparsity formulation (4 equations) + phase segmentation details to appendix |
| `results.tex` | 154 lines | 119 lines | Removed redundant `tab:aggregate-ii`; moved `tab:cohens-d` to appendix; merged discrimination collapse (from analysis) as §5.7 |
| `analysis.tex` | 46 lines | removed | Content merged into results.tex; `\input{analysis}` removed from main.tex |
| `discussion.tex` | 25 lines | 19 lines | Removed Limitations subsection (consolidated); added Future directions |
| `conclusion.tex` | 12 lines | 15 lines | Added `\section*{Limitations}` (consolidated from discussion + conclusion) |
| `introduction.tex` | 33 lines | 32 lines | Removed roadmap sentence; updated `sec:analysis` → `sec:discrimination-collapse` |
| `methodology.tex` | 22 lines | 22 lines | Removed orphaned `Eq.~\ref{eq:kv-importance}` reference |
| `appendix.tex` | 11 lines | 45 lines | Added compound sparsity formulation section with all moved equations |
| `appendix_results.tex` | 60 lines | 78 lines | Appended `tab:cohens-d` table |
| `main.tex` | 47 lines | 46 lines | Removed `\input{analysis}` |

### Verification
- All `\ref{}` have matching `\label{}` — zero orphan references
- No experimental numbers modified (all metrics, p-values, Cohen's d, II values preserved)
- `\section*{Limitations}` appears after Conclusion, before `\bibliography` (EMNLP format)
- Estimated main text: ~6–7 pages (well within 8-page limit)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 840195,
  "duration_api_ms": 840759,
  "num_turns": 48,
  "stop_reason": "end_turn",
  "session_id": "c8d121e6-8d75-42ef-9c29-b7bbdf42e8e6",
  "total_cost_usd": 2.4960409999999995,
  "usage": {
    "input_tokens": 439,
    "cache_creation_input_tokens": 149358,
    "cache_read_input_tokens": 726375,
    "output_tokens": 47767,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 149358,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1129,
        "cache_read_input_tokens": 104505,
        "cache_creation_input_tokens": 4916,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4916
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2891,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 439,
      "outputTokens": 47767,
      "cacheReadInputTokens": 726375,
      "cacheCreationInputTokens": 149358,
      "webSearchRequests": 0,
      "costUSD": 2.4930449999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "79814eaa-1aae-41af-b762-2fbbaf6e4cdc"
}
```

</details>

---
