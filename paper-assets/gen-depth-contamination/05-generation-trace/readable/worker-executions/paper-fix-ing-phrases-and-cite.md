# paper fix ing phrases and cite

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_fix-ing-phrases-and-cite_20260519T035804.log`
- **Structured JSON:** [`8e12bb167089949ee05c.json`](../../sessions/8e/8e12bb167089949ee05c.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
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
    "mcp__agent-ml-research__distill_papers",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_distill_status",
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
    "mcp__agent-ml-research__read_mistakes",
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
  "uuid": "bb2e7647-114e-48c8-bce7-ed3e1b2ebd66",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779180000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "26d84c17-e18d-4b4c-8ed6-144246adb3e3",
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant files to understand the current content and make the required changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "d11424dd-c806-427e-990f-1bf9e385cc71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

Reading the target files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "0d57f46a-0f58-405a-81db-5b6c3eece3c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01RwzEgWb9emucv92f4CTBto`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "78ba7477-78aa-4a89-a815-847b3cb66a5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01KyPkMxkR6vjXHACbUz6jUV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "1c1e3bb0-c103-4330-b3e2-c17643c3cb57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01QbWKg47h24kCZi981j9bTK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "a1da36c3-2f42-4f59-9741-bce2d62c78de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Kib7Ltwkt8GdhyKUXdiUJj`</summary>

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
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "b41bb90a-6d93-4139-9804-d60127d2f402",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YeeqAwdRRKJrUfjJjqtte",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13946,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13946
      },
      "output_tokens": 21,
      "service_tier": "standard",
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

_source line 10 · 2026-05-19T03:58:21.541Z_

<details><summary>↩ Tool result · `toolu_01QbWKg47h24kCZi981j9bTK`</summary>

```text
1	% EMNLP 2026 Main - ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{pifont}
18	\newcommand{\cmark}{\ding{51}}
19	\newcommand{\xmark}{\ding{55}}
20	\usepackage[section]{placeins}
21	
22	\newcommand{\Kstar}{{K^*}}
23	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
24	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
25	\newcommand{\auc}{\text{AUC}}
26	\newcommand{\jsd}{\text{JSD}}
27	\newcommand{\tpm}{\ensuremath{\,\pm\,}}
28	
29	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	% === Abstract ===
37	\begin{abstract}
38	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
39	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
40	Across five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\theta{=}0.60$ (AUC decision threshold), $\Kempirical{=}2$ for general web text (8/9 model configurations), $\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\Kempirical{=}3$ for structured academic text (arXiv).
41	A single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
42	Largely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\Kempirical$ is largely robust to scorer choice.
43	Downstream, $\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.
44	\end{abstract}
45	
46	% === Section 1: Introduction ===
47	\input{introduction}
48	
49	% === Section 2: Related Work ===
50	\input{related_work}
51	
52	% === Section 3: Method ===
53	\input{method}
54	
55	% === Section 4: Experiments ===
56	\input{experiments_c1}
57	
58	% === Section 5: K*-Aware Data Filtering ===
59	\input{experiments_c3}
60	
61	% === Section 6: Discussion ===
62	\input{discussion}
63	
64	% === Section 7: Conclusion ===
65	\input{conclusion}
66	
67	% === Limitations (ACL required, unnumbered) ===
68	\clearpage
69	\section*{Limitations}
70	
71	Our findings are bounded by:
72	(1)~\emph{Scope}: model scale $\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with two models (Qwen2.5-1.5B, $\Kempirical{=}2$; Pythia-1.4B, borderline $\Kempirical{=}1$ with 1v2 CI upper $> \theta$); subsampling analysis indicates $n{\geq}2{,}000$ suffices for 100\% reliable $\Kempirical$ determination (Appendix~\ref{sec:power_curve}).
73	(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
74	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
75	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\theta$.
76	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
77	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.
78	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
79	(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
80	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
81	
82	% === Ethics Statement (ACL required, unnumbered) ===
83	\section*{Ethics Statement}
84	
85	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
86	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
87	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
88	Code and generated corpora will be released upon acceptance to enable reproducibility.
89	
90	\bibliography{references}
91	
92	\input{appendix}
93	\input{appendix_extended}
94	
95	\end{document}
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "e7d62b97-b6fc-41bf-9e4d-a530fbc02bd6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main - ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{pifont}\n\\newcommand{\\cmark}{\\ding{51}}\n\\newcommand{\\xmark}{\\ding{55}}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\\newcommand{\\tpm}{\\ensuremath{\\,\\pm\\,}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\\theta{=}0.60$ (AUC decision threshold), $\\Kempirical{=}2$ for general web text (8/9 model configurations), $\\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\\Kempirical{=}3$ for structured academic text (arXiv).\nA single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nLargely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\\Kempirical$ is largely robust to scorer choice.\nDownstream, $\\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with two models (Qwen2.5-1.5B, $\\Kempirical{=}2$; Pythia-1.4B, borderline $\\Kempirical{=}1$ with 1v2 CI upper $> \\theta$); subsampling analysis indicates $n{\\geq}2{,}000$ suffices for 100\\% reliable $\\Kempirical$ determination (Appendix~\\ref{sec:power_curve}).\n(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\n(8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T03:58:21.546Z_

<details><summary>↩ Tool result · `toolu_01RwzEgWb9emucv92f4CTBto`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.
9	
10	This gap cuts across multiple communities.
11	Binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}).
12	Membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
13	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
14	No existing method estimates how many rounds of recursive generation a text has undergone.
15	
16	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
17	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
18	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
19	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
20	
21	The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$.
22	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
23	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
24	
25	Our contributions:
26	\begin{enumerate}[label=(\alph*),nosep]
27	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\Kempirical{=}2$ on C4 ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
28	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
29	  \item \textbf{Domain ordering}: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\ref{sec:cross_domain}).
30	  \item \textbf{Practical validation}: largely generator-independent features enable 80--92\% accuracy retention among tested continuation-mode configurations ($\rho > 0.90$; Section~\ref{sec:transfer}), and $\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\ref{sec:filtering}).
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
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "585f162f-e34b-462d-8030-94006552ee77",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.\n\nThis gap cuts across multiple communities.\nBinary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}).\nMembership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\\Kempirical{=}2$ on C4 ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering}: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}), and $\\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:58:21.550Z_

<details><summary>↩ Tool result · `toolu_01KyPkMxkR6vjXHACbUz6jUV`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$.
19	A single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.
20	Converging evidence supports a data-intrinsic interpretation: OBD achieves 96\% depth-0 recall but only 14--22\% for depths 2--4; frontier LLMs show 8--38\% (McNemar $p > 0.05$ vs.\ OBD; Table~\ref{tab:s3_llm_zeroshot}).
21	Baseline classifier substitution (logistic regression, linear SVC, random forest) yields non-significant McNemar differences in 31/36 comparisons (Table~\ref{tab:mcnemar_obd_baselines}).
22	
23	\paragraph{JSD decay and the discrimination boundary.}
24	Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$); cross-model consistency indicates the contraction rate is domain-governed.
25	The retrain-chain ($\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts: $\Kempirical{=}7$ for both Qwen-1.5B and Pythia-1.4B LoRA (Table~\ref{tab:retrain_ci}), 5 generations beyond prompt-chain $\Kempirical{=}2$ (Appendix~\ref{sec:jsd_extended}).
26	
27	\paragraph{Graduated filtering failure.}
28	For web text, 2v3 $\auc < \theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels and graduated weighting injects noise (Appendix~\ref{sec:extended_limitations}).
29	The strategy ordering binary $>$ graduated aligns with $\Kempirical{=}2$; on arXiv ($\Kempirical{=}3$), graduated filtering similarly shows no improvement, consistent with $\Kempirical$ capturing discriminability rather than curation utility.
30	
31	\paragraph{Representation and scorer dependence.}
32	$\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$ vs.\ $\Kempirical^{\text{neural}} = 2$ for Pythia and OLMo; Table~\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\Kempirical$ from 2 to 1, Appendix~\ref{sec:wiki_domain}, while preserving C4 feature rankings $\rho > 0.90$ and $\Kempirical$ for 6/8 configurations, Section~\ref{sec:transfer}).
33	
34	\paragraph{Domain dependence of $\Kempirical$.}
35	C4 web text yields $\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\auc = 0.74$) and borderline $\Kempirical{=}1$ for Pythia-1.4B (1v2 $\auc = 0.598$, CI $[0.593, 0.603]$; Section~\ref{sec:cross_domain}), arXiv yields $\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\Kempirical{=}1$ with scorer confound controlled (Appendix~\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}).
36	For Qwen, code and C4 share $\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\to$1v2 ($9.8\times$ JSD drop), while code collapses at 1v2$\to$2v3 ($11.7\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.
37	Pythia's code 1v2 falls just below $\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\Kempirical$ but also the decay profile.
38	The only C4 exception (Mistral-7B, $\Kempirical{=}1$) has $\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\Delta = -1.8$\,pp, $\Kempirical$ unchanged; Appendix~\ref{sec:latex_ablation}).
39	
40	\paragraph{Surprisal attenuation and boundary variation.}
41	\label{sec:surprisal_attenuation}
42	The Mistral-7B exception ($\Kempirical{=}1$) arises from compressed surprisal dynamic range (depth-0 mean surprisal 2.32 vs.\ 2.90--3.02 for $\Kempirical{=}2$ models; mean $|\text{Cohen's}\;d| = 0.112$; Table~\ref{tab:cohens_d_full}).
43	Larger 0$\to$1 surprisal drops correlate with higher 1v2 $\auc$ across six C4 configurations (Table~\ref{tab:borderline_features}); this attenuation predicts that $\Kempirical$ may decrease as capability scales beyond 14B (Qwen-14B: $\Kempirical{=}2$, $\auc = 0.621$).
44	
45	\paragraph{Why $\Kempirical$ matters.}
46	For curation, $\Kempirical{=}2$ validates binary filtering for web text (Section~\ref{sec:filtering}) and provides post-hoc grounding for the binary approach of \citet{drayson2025}.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "63909bbb-382b-4921-8b23-fef8bf668023",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nBaseline classifier substitution (logistic regression, linear SVC, random forest) yields non-significant McNemar differences in 31/36 comparisons (Table~\\ref{tab:mcnemar_obd_baselines}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$); cross-model consistency indicates the contraction rate is domain-governed.\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts: $\\Kempirical{=}7$ for both Qwen-1.5B and Pythia-1.4B LoRA (Table~\\ref{tab:retrain_ci}), 5 generations beyond prompt-chain $\\Kempirical{=}2$ (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels and graduated weighting injects noise (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$; on arXiv ($\\Kempirical{=}3$), graduated filtering similarly shows no improvement, consistent with $\\Kempirical$ capturing discriminability rather than curation utility.\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nFor Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.\nPythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (depth-0 mean surprisal 2.32 vs.\\ 2.90--3.02 for $\\Kempirical{=}2$ models; mean $|\\text{Cohen's}\\;d| = 0.112$; Table~\\ref{tab:cohens_d_full}).\nLarger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ across six C4 configurations (Table~\\ref{tab:borderline_features}); this attenuation predicts that $\\Kempirical$ may decrease as capability scales beyond 14B (Qwen-14B: $\\Kempirical{=}2$, $\\auc = 0.621$).\n\n\\paragraph{Why $\\Kempirical$ matters.}\nFor curation, $\\Kempirical{=}2$ validates binary filtering for web text (Section~\\ref{sec:filtering}) and provides post-hoc grounding for the binary approach of \\citet{drayson2025}.\n",
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

_source line 13 · 2026-05-19T03:58:21.937Z_

<details><summary>↩ Tool result · `toolu_01Kib7Ltwkt8GdhyKUXdiUJj`</summary>

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
37	Both Qwen2.5-1.5B and Pythia-1.4B yield $\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$.
38	Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
40	This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.
41	Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models, suggesting $\Kempirical{=}7$ is near the ceiling.
42	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
43	
44	\begin{table}[h]
45	\centering
46	\small
47	\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. Both models yield $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
48	\label{tab:retrain_ci}
49	\begin{tabular}{lcccc}
50	\toprule
51	 & \multicolumn{2}{c}{\textbf{Qwen-1.5B}} & \multicolumn{2}{c}{\textbf{Pythia-1.4B}} \\
52	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
53	\textbf{Pair} & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
54	\midrule
55	0v1 & 0.9837 & $[.982,\,.985]$ & 0.9844 & $[.983,\,.986]$ \\
56	1v2 & 0.8971 & $[.895,\,.899]$ & 0.9470 & $[.942,\,.952]$ \\
57	2v3 & 0.8098 & $[.805,\,.814]$ & 0.8891 & $[.882,\,.896]$ \\
58	3v4 & 0.7600 & $[.753,\,.767]$ & 0.7999 & $[.795,\,.805]$ \\
59	4v5 & 0.7459 & $[.738,\,.754]$ & 0.6907 & $[.688,\,.693]$ \\
60	5v6 & 0.7017 & $[.696,\,.708]$ & 0.6497 & $[.643,\,.657]$ \\
61	6v7 & 0.6410 & $[.638,\,.645]$ & 0.6340 & $[.628,\,.641]$ \\
62	\bottomrule
63	\end{tabular}
64	\end{table}
65	
66	\paragraph{CI methodology note.}
67	\label{sec:retrain_ci_note}
68	The main pipeline reports bootstrap 95\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.
69	In the retrain-chain setting, each generation's training corpus is the \emph{output} of the previous generation's fine-tuned model, creating inter-generation dependencies that standard bootstrap resampling cannot preserve without inflating AUC estimates.
70	We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
71	
72	\emph{Threshold sensitivity.}
73	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
74	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
75	
76	\begin{table}[h]
77	\centering
78	\small
79	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
80	\label{tab:theta_sensitivity}
81	\resizebox{\columnwidth}{!}{%
82	\begin{tabular}{llcccc}
83	\toprule
84	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
85	\midrule
86	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
87	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
88	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
89	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
90	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
91	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
92	\midrule
93	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
94	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
95	\midrule
96	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
97	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
98	\bottomrule
99	\end{tabular}}
100	\end{table}
101	
102	\begin{figure}[h]
103	\centering
104	\includegraphics[width=\columnwidth]{figures/fig_theta_sensitivity.pdf}
105	\caption{$\Kempirical$ as a function of $\theta$ across all model $\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\Kempirical{\leq}1$ $<$ C4 $\Kempirical{\leq}2$ $<$ arXiv $\Kempirical{\leq}3$) is preserved across the full $\theta \in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\Kempirical$.}
106	\label{fig:theta_sensitivity}
107	\end{figure}
108	
109	\emph{Structural confound: token length.}
110	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
111	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
112	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
113	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
114	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
115	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.
116	
117	\emph{Graduated filtering.}
118	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
119	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
120	\label{tab:pairwise_significance}
121	
122	\subsection{Dose-Response: Contamination Ratio Effect}
123	\label{sec:dose_response}
124	
125	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
126	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
127	
128	\begin{table}[h]
129	\centering
130	\small
131	\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
132	\label{tab:dose_response}
133	\resizebox{\columnwidth}{!}{%
134	\begin{tabular}{lcccccc}
135	\toprule
136	& \multicolumn{2}{c}{\textbf{10\%}} & \multicolumn{2}{c}{\textbf{30\%}} & \multicolumn{2}{c}{\textbf{50\%}} \\
137	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
138	\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\
139	\midrule
140	No-filter   & $.6058{\pm}.0002$ & $.6689{\pm}.0006$ & $.6069{\pm}.0007$ & $.6664{\pm}.0018$ & $.6063{\pm}.0012$ & $.6680{\pm}.0005$ \\
141	Binary-ours & $\mathbf{.6079{\pm}.0004}$ & $\mathbf{.6727{\pm}.0007}$ & $\mathbf{.6082{\pm}.0011}$ & $\mathbf{.6725{\pm}.0006}$ & $\mathbf{.6088{\pm}.0009}$ & $\mathbf{.6731{\pm}.0004}$ \\
142	Graduated   & $.6066{\pm}.0010$ & $.6700{\pm}.0014$ & $.6072{\pm}.0008$ & $.6665{\pm}.0012$ & $.6062{\pm}.0008$ & $.6679{\pm}.0001$ \\
143	\bottomrule
144	\end{tabular}}
145	\end{table}
146	
147	At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.
148	Binary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).
149	MMLU differences are smaller and significant only at 10\% after correction ($p = 0.001$).
150	Graduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \geq 0.27$; HellaSwag $p \geq 0.06$), confirming that depth assignments beyond $\Kempirical$ inject noise regardless of contamination severity.
151	Effect sizes diminish 3--6$\times$ relative to the 100\% setting (Section~\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\approx$ no-filter) is preserved.
152	
153	\subsection{Cross-Model Filtering Replication}
154	\label{sec:pythia_filtering}
155	
156	To test whether $\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\ref{tab:pythia_filtering}).
157	
158	\begin{table}[h]
159	\centering
160	\small
161	\caption{Pythia-1.4B filtering replication (3 seeds, mean $\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}
162	\label{tab:pythia_filtering}
163	\begin{tabular}{lcc}
164	\toprule
165	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
166	\midrule
167	No-filter & $.2568{\pm}.0012$ & $.5250{\pm}.0008$ \\
168	Binary-ours & $\mathbf{.2585{\pm}.0004}$ & $.5251{\pm}.0001$ \\
169	Graduated$_{0.9}$ & $.2561{\pm}.0009$ & $\mathbf{.5253{\pm}.0007}$ \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
175	The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
176	HellaSwag differences are negligible across all strategies.
177	
178	\subsection{Feature Subset Stability}
179	\label{sec:feature_subset}
180	
181	To test whether $\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\ref{tab:feature_subset}).
182	
183	\begin{table}[h]
184	\centering
185	\small
186	\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
187	\label{tab:feature_subset}
188	\begin{tabular}{lcccc}
189	\toprule
190	\textbf{Subset} & \textbf{Tested} & \textbf{Pass} & \textbf{Min $\auc$} & \textbf{Mean $\auc$} \\
191	\midrule
192	15D (full) & 1 & 1 & 0.6262 & 0.6262 \\
193	10D        & 5 & 5 & 0.6153 & 0.6191 \\
194	8D         & 5 & 5 & 0.6056 & 0.6159 \\
195	5D         & 5 & 2 & 0.5856 & 0.5998 \\
196	3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
202	The boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.
203	
204	\subsection{self\_BLEU Feature Independence}
205	\label{sec:selfbleu_ablation}
206	
207	To verify that $\Kempirical$ does not depend on the self\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\_BLEU removed) classifiers across four model configurations (Table~\ref{tab:selfbleu_ablation}).
208	
209	\begin{table}[h]
210	\centering
211	\small
212	\caption{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).}
213	\label{tab:selfbleu_ablation}
214	\resizebox{\columnwidth}{!}{%
215	\begin{tabular}{lcccc}
216	\toprule
217	\textbf{Model} & $\Kempirical$ & \textbf{15D $\auc$ [CI]} & \textbf{14D $\auc$ [CI]} & $\Delta$ \\
218	\midrule
219	Qwen-base   & 2/2 & $.6288$ $[.620,\,.638]$ & $.6258$ $[.616,\,.635]$ & $-.0031$ \\
220	Pythia-1.4B  & 2/2 & $.8840$ $[.878,\,.890]$ & $.8830$ $[.876,\,.889]$ & $-.0010$ \\
221	LLaMA-8B     & 2/2 & $.6075$ $[.598,\,.617]$ & $.6074$ $[.598,\,.617]$ & $-.0001$ \\
222	Mistral-7B   & 1/1 & $.5902$ $[.580,\,.600]$ & $.5903$ $[.580,\,.600]$ & $+.0002$ \\
223	\bottomrule
224	\end{tabular}}
225	\end{table}
226	
227	All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
228	The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
229	
230	\subsection{Wikipedia Domain: Scorer Confound Resolution}
231	\label{sec:wiki_domain}
232	
233	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
234	A scorer confound ablation resolves this apparent split.
235	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
236	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
237	
238	\begin{table}[h]
239	\centering
240	\small
241	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
242	\label{tab:wiki_domain}
243	\resizebox{\columnwidth}{!}{%
244	\begin{tabular}{llccccc}
245	\toprule
246	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
247	\midrule
248	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
249	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
250	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
251	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
252	\midrule
253	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
254	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
255	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
256	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
257	\bottomrule
258	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
259	\end{tabular}}
260	\end{table}
261	
262	\paragraph{Per-fold transparency.}
263	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
264	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
265	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
266	
267	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
268	\label{sec:arxiv_crossscorer_ci}
269	
270	\begin{table}[h]
271	\centering
272	\small
273	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
274	\label{tab:arxiv_crossscorer_ci}
275	\resizebox{\columnwidth}{!}{%
276	\begin{tabular}{lccc}
277	\toprule
278	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
279	\midrule
280	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
281	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
282	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
283	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
284	\bottomrule
285	\end{tabular}}
286	\end{table}
287	
288	\subsection{JSD Decay Analysis}
289	\label{sec:jsd_extended}
290	
291	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
292	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
293	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
294	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
295	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\lambda \approx 1.0$.
296	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
297	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
298	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\Kempirical{=}3$.
299	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs (Figure~\ref{fig:retrain_decay}).
300	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
301	
302	\begin{figure}[h]
303	\centering
304	\includegraphics[width=\columnwidth]{figures/fig_retrain_decay.png}
305	\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
306	\label{fig:retrain_decay}
307	\end{figure}
308	
309	\subsection{Boundary Cases and Scale Effect}
310	\label{sec:boundary_extended}
311	
312	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
313	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain lexical diversity can rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
314	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
315	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.
316	
317	\paragraph{Sample-size control.}
318	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
319	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, confirming that arXiv's $\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.
320	
321	\subsection{LaTeX Markup Ablation (arXiv)}
322	\label{sec:latex_ablation}
323	
324	To disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\ref{tab:latex_ablation}).
325	
326	\begin{table}[h]
327	\centering
328	\small
329	\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), indicating that deeper generations produce proportionally more formatting tokens.}
330	\label{tab:latex_ablation}
331	\resizebox{\columnwidth}{!}{%
332	\begin{tabular}{lccr}
333	\toprule
334	\textbf{Pair} & \textbf{Original} & \textbf{Stripped} & $\Delta$ \\
335	\midrule
336	0v1 & 0.9946 & 0.9948 & $+$0.0002 \\
337	1v2 & 0.8580 & 0.8297 & $-$0.028 \\
338	2v3 & 0.6427 $[0.628,\,0.658]$ & 0.6248 $[0.610,\,0.640]$ & $-$0.018 \\
339	3v4 & 0.5437 & 0.5468 & $+$0.003 \\
340	\midrule
341	$\Kempirical$ & 3 & 3 & --- \\
342	\bottomrule
343	\end{tabular}}
344	\end{table}
345	
346	Content-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\sim}$1.8\,pp at the boundary pair).
347	The depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\%, depth 5: $-$4.6\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.
348	
349	\subsection{Statistical Power Analysis}
350	\label{sec:power_curve}
351	
352	To characterize the minimum sample size required for reliable $\Kempirical$ determination, we subsample C4 at $n \in \{500, 1000, 2000, 3000, 4000, 5000\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\ref{tab:power_curve}, Figure~\ref{fig:power_curve}).
353	
354	\begin{table}[h]
355	\centering
356	\small
357	\caption{Subsampling power analysis for $\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\auc > \theta{=}0.60$.}
358	\label{tab:power_curve}
359	\begin{tabular}{rccc}
360	\toprule
361	$n$ & \textbf{Mean 1v2 $\auc$} & \textbf{Std} & \textbf{Detection Prob.} \\
362	\midrule
363	500 & 0.581 & 0.018 & 20\% \\
364	1{,}000 & 0.591 & 0.014 & 30\% \\
365	2{,}000 & 0.610 & 0.009 & 100\% \\
366	3{,}000 & 0.617 & 0.005 & 100\% \\
367	4{,}000 & 0.622 & 0.004 & 100\% \\
368	5{,}000 & 0.629 & 0.000 & 100\% \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	\begin{figure}[h]
374	\centering
375	\includegraphics[width=\columnwidth]{figures/fig_power_curve.png}
376	\caption{$\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\% at $n{=}2{,}000$; the 80\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\pm$1 std over 10 resamples. The dashed red line marks $\theta{=}0.60$.}
377	\label{fig:power_curve}
378	\end{figure}
379	
380	Detection rate jumps from 20\% ($n{=}500$) to 100\% ($n{=}2{,}000$), with the 80\% power threshold crossed near $n{=}1{,}500$.
381	At $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, confirming that our results are well above the minimum required for reliable boundary estimation.
382	The sharp transition reflects the proximity of the 1v2 AUC to $\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.
383	
384	\subsection{Feature Group Ablation}
385	\label{sec:feature_ablation}
386	
387	To assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\ref{sec:method}) on the 1\,vs.\,2 task using (a) each feature group alone (\emph{single}) and (b) the full 15D set minus one group (\emph{leave-one-out}).
388	Representative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).
389	
390	\begin{figure}[h]
391	\centering
392	\includegraphics[width=\columnwidth]{figures/fig_feature_ablation.pdf}
393	\caption{Feature group ablation heatmap for 1\,vs.\,2 classification AUC. \emph{Left}: single-group performance. \emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}
394	\label{fig:feature_ablation}
395	\end{figure}
396	
397	\begin{table}[h]
398	\centering
399	\small
400	\caption{Feature group ablation for 1\,vs.\,2 classification (AUC). \textbf{Single}: using only features from one group. \textbf{Leave-one-out}: removing one group from the full 15D feature set. $\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\ref{tab:kstar_ci}.}
401	\label{tab:feature_ablation}
402	\resizebox{\columnwidth}{!}{%
403	\begin{tabular}{l ccc ccc}
404	\toprule
405	& \multicolumn{3}{c}{\textbf{Single Group}} & \multicolumn{3}{c}{\textbf{Leave-One-Out ($\Delta$)}} \\
406	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
407	Feature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\
408	\midrule
409	Surprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\
410	Surprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\
411	Lexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\
412	Freq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\
413	\midrule
414	Full (15D) & 0.609 & 0.860 & 0.619 & \multicolumn{3}{c}{---} \\
415	\bottomrule
416	\end{tabular}}
417	\end{table}
418	
419	Surprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.
420	On C4 and Wikipedia, all LOO drops are small ($\leq 0.007$, within cross-fold standard deviation), indicating that no single feature group is individually critical for the weaker low-$\Kempirical$ signal.
421	Removing surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\Kempirical$ domains.
422	
423	\subsection{Classifier Choice: McNemar Test}
424	\label{sec:mcnemar_baselines}
425	
426	To verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\ref{tab:mcnemar_obd_baselines}).
427	Of 36 comparisons, 31 are non-significant ($p \geq 0.05$), and all five significant results concentrate in two model $\times$ domain conditions.
428	For LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.
429	For Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).
430	
431	\begin{table*}[h]
432	\centering
433	\small
434	\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}
435	\label{tab:mcnemar_obd_baselines}
436	\resizebox{\textwidth}{!}{%
437	\begin{tabular}{llcccc}
438	\toprule
439	\textbf{Model} & \textbf{Domain} & \textbf{OBD Acc.} & \textbf{vs.\ LogReg} & \textbf{vs.\ LinearSVC} & \textbf{vs.\ RandomForest} \\
440	\midrule
441	Qwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\
442	Pythia-1.4B     & C4    & .631 & $\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\
443	LLaMA-8B        & C4    & .573 & $\mathbf{6.2{\times}10^{-5\,***}}$ (.592) & $\mathbf{1.1{\times}10^{-4\,***}}$ (.591) & $\mathbf{.001^{**}}$ (.586) \\
444	\midrule
445	Qwen-1.5B      & Wiki  & .588 & $\mathbf{9.4{\times}10^{-4\,***}}$ (.570) & $\mathbf{2.3{\times}10^{-4\,***}}$ (.568) & .655 (.590) \\
446	Pythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\
447	OLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\
448	LLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\
449	\midrule
450	Qwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\
451	Pythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\
452	OLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\
453	Qwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\
454	Mistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\
455	\bottomrule
456	\end{tabular}%
457	}
458	
459	\vspace{4pt}
460	\footnotesize
461	36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.
462	The predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.
463	\end{table*}
464	
465	\subsection{Domain Lexical Statistics}
466	\label{sec:domain_lexical_stats}
467	
468	Table~\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.
469	The TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\ Wikipedia).
470	Vocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).
471	This reversal likely reflects C4's greater content heterogeneity (higher variance: $\sigma = 0.706$ vs.\ $0.284$), which inflates TTR but depresses mean entropy.
472	As depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\Kempirical$ and slower convergence to the stationary distribution.
473	
474	\begin{table*}[h]
475	\centering
476	\small
477	\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.
478	At depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\,=\,0.755, $H$\,=\,6.853),
479	followed by C4 and Wikipedia.
480	As depth increases, all domains converge, with arXiv showing the steepest decline.
481	Cohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}
482	\label{tab:domain-ttr-entropy}
483	\begin{tabular}{ll rrr rrr}
484	\toprule
485	& & \multicolumn{3}{c}{\textbf{TTR}} & \multicolumn{3}{c}{\textbf{Vocab Entropy ($H$)}} \\
486	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
487	\textbf{Depth} & $N$ & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} \\
488	\midrule
489	0 & 5k/5k/2.2k & .665\tpm.061 & .720\tpm.105 & \textbf{.755}\tpm.055 & 6.408\tpm.284 & 6.225\tpm.706 & \textbf{6.853}\tpm.295 \\
490	1 &             & .655\tpm.121 & .707\tpm.149 & \textbf{.732}\tpm.098 & 5.932\tpm.843 & 5.737\tpm1.189 & \textbf{6.113}\tpm.655 \\
491	2 &             & .647\tpm.145 & .676\tpm.159 & \textbf{.677}\tpm.131 & 5.784\tpm.905 & 5.774\tpm1.139 & \textbf{5.998}\tpm.967 \\
492	3 &             & .645\tpm.159 & \textbf{.662}\tpm.164 & .635\tpm.134 & 5.664\tpm1.085 & 5.743\tpm1.161 & \textbf{5.964}\tpm.933 \\
493	4 &             & .636\tpm.164 & \textbf{.647}\tpm.169 & .621\tpm.140 & 5.660\tpm1.062 & 5.758\tpm1.167 & \textbf{5.898}\tpm.942 \\
494	5 &             & .632\tpm.172 & \textbf{.636}\tpm.175 & .618\tpm.150 & 5.593\tpm1.130 & 5.772\tpm1.141 & \textbf{5.816}\tpm.968 \\
495	\midrule
496	\multicolumn{8}{l}{\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\
497	\multicolumn{2}{l}{C4 vs.\ Wiki}   & \multicolumn{3}{c}{$d = +0.65$} & \multicolumn{3}{c}{$d = -0.34$} \\
498	\multicolumn{2}{l}{arXiv vs.\ C4}  & \multicolumn{3}{c}{$d = +0.37$} & \multicolumn{3}{c}{$d = +1.03$} \\
499	\multicolumn{2}{l}{arXiv vs.\ Wiki} & \multicolumn{3}{c}{$d = +1.52$} & \multicolumn{3}{c}{$d = +1.55$} \\
500	\bottomrule
501	\end{tabular}
502	\end{table*}
503	
504	\subsection{Leave-One-Family-Out Threshold Validation}
505	\label{sec:theta_lofo}
506	
507	To validate $\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, then predicts $\Kempirical$ for the held-out models.
508	Table~\ref{tab:theta_lofo} reports results across all three domains.
509	
510	On C4, 8/9 held-out predictions agree with the original $\Kempirical$ assignment at $\theta{=}0.60$ (agreement: 89\%).
511	The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the sole rewrite-mode model, making the discrepancy attributable to mode rather than threshold instability.
512	The derived $\hat{\theta}$ values span $[0.5725, 0.6004]$, and $\theta{=}0.60$ falls within this range.
513	
514	ArXiv corroborates with 6/6 agreement (100\%), though the wide $\hat{\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.
515	
516	Wikipedia yields only 1/6 agreement (17\%).
517	This failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ is narrow or inverted, invalidating the gap-based threshold derivation.
518	Wikipedia's $\Kempirical{=}1$ assignment is independently confirmed by the global $\theta{=}0.60$ criterion (Section~\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.
519	
520	\begin{table*}[t]
521	\centering
522	\small
523	\caption{Leave-One-Family-Out (LOFO) cross-validation of $\theta$ across three domains. Each fold holds out one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\text{AUC}_{1\text{v}2})$ and $\max(\text{AUC}_{2\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\%). arXiv: 6/6 (100\%). Wikipedia: 1/6 (17\%, see text).}
524	\label{tab:theta_lofo}
525	\begin{tabular}{l l l c c c c c c}
526	\toprule
527	Domain & Held-out & Model & $\text{AUC}_{1\text{v}2}$ & $\text{AUC}_{2\text{v}3}$ & $\hat{\theta}$ & $K^*_{\hat{\theta}}$ & $K^*_{0.60}$ & Match \\
528	\midrule
529	C4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \cmark \\
530	 & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \cmark \\
531	 & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \xmark \\
532	 &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \cmark \\
533	 &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \cmark \\
534	 &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \cmark \\
535	 &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \cmark \\
536	 & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \cmark \\
537	 & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \cmark \\
538	\cmidrule{2-9}
539	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5725, 0.6004], agreement: 8/9 (89\%)} \\
540	\midrule
541	arXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \cmark \\
542	 & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \cmark \\
543	 & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \cmark \\
544	 &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \cmark \\
545	 & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \cmark \\
546	 & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \cmark \\
547	\cmidrule{2-9}
548	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5735, 0.7296], agreement: 6/6 (100\%)} \\
549	\midrule
550	Wikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \xmark \\
551	 & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \cmark \\
552	 & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \xmark \\
553	 &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \xmark \\
554	 & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \xmark \\
555	 & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \xmark \\
556	\cmidrule{2-9}
557	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5215, 0.5557], agreement: 1/6 (17\%)} \\
558	\bottomrule
559	\end{tabular}
560	\end{table*}
561	
562	\subsection{Code Domain Results}
563	\label{sec:code_domain}
564	
565	\begin{table}[h]
566	\centering
567	\small
568	\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
569	\label{tab:code_domain_qwen}
570	\begin{tabular}{l c c c}
571	\toprule
572	Pair & AUC & 95\% CI & JSD \\
573	\midrule
574	0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\
575	1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\
576	2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\
577	3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\
578	4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\
579	\midrule
580	\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	\begin{table}[h]
586	\centering
587	\small
588	\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\% CIs. Qwen2.5-1.5B yields $\Kempirical{=}2$; Pythia-1.4B yields borderline $\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \theta$). Additional models pending completion.}
589	\label{tab:code_crossmodel_kstar}
590	\begin{tabular}{l cc cc}
591	\toprule
592	 & \multicolumn{2}{c}{Qwen2.5-1.5B} & \multicolumn{2}{c}{Pythia-1.4B} \\
593	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
594	 & AUC & 95\% CI & AUC & 95\% CI \\
595	\midrule
596	0v1 & .9388 & [.929,\,.949] & \textbf{.9592} & [.956,\,.963] \\
597	1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .5983 & [.593,\,.603] \\
598	2v3 & .5300 & [.514,\,.546] & .5215 & --- \\
599	3v4 & .5022 & --- & .5152 & --- \\
600	4v5 & .5219 & --- & .5046 & --- \\
601	\midrule
602	$K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} \\
603	\bottomrule
604	\multicolumn{5}{l}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\geq \theta = 0.60$.}
605	\end{tabular}
606	\end{table}
607	
608	\subsection{Borderline Feature Analysis}
609	\label{sec:borderline_analysis}
610	
611	To understand why Mistral-7B yields $\Kempirical{=}1$ while other C4 models yield $\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).
612	
613	Mistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\ 2.90--3.02 for other models), indicating that the scorer model already finds Mistral's output highly predictable.
614	This compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\bar{|d|} = 0.112$; Table~\ref{tab:cohens_d_full}), and no single feature exceeds 13\% of total classifier importance.
615	The borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.
616	
617	Greedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.
618	
619	\begin{table*}[h]
620	\centering
621	\small
622	\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\ = normalized LightGBM gain importance (\%). $\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\Delta\text{surp}_{1\to2}$: change in mean surprisal from depth 1 to depth 2.}
623	\label{tab:borderline_features}
624	\begin{tabular}{@{}llc lcc@{}}
625	\toprule
626	Category & Model & AUC & Top-3 Features (Imp.\%) & $\bar{|d|}$ & $\Delta\text{surp}_{1\to2}$ \\
627	\midrule
628	Strong & Pythia-greedy & 0.884 & hapax\_ratio (47), surp\_mean (11), low\_freq\_ratio (8) & 0.365 & $-$0.160 \\
629	Strong & Pythia-nuc09 & 0.677 & surp\_std (20), freq\_entropy (11), surp\_d1\_std (8) & 0.170 & $-$0.196 \\
630	Strong & Qwen-1.5B-base & 0.626 & surp\_std (13), freq\_entropy (10), surp\_mean (9) & 0.125 & $-$0.159 \\
631	\midrule
632	Borderline & Pythia-$T{=}1.2$ & 0.617 & surp\_std (15), freq\_entropy (10), surp\_kurt (8) & 0.112 & $-$0.059 \\
633	Borderline & LLaMA-3.1-8B & 0.612 & surp\_std (12), surp\_d1\_std (10), freq\_entropy (9) & 0.137 & $-$0.215 \\
634	\midrule
635	Below $\theta$ & Mistral-7B & 0.594 & surp\_std (13), freq\_entropy (9), surp\_d1\_skew (9) & 0.112 & $-$0.086 \\
636	\bottomrule
637	\end{tabular}
638	\end{table*}
639	
640	\begin{table*}[h]
641	\centering
642	\scriptsize
643	\caption{Cohen's $d$ (depth-1 vs.\ depth-2) for all 15 features across six C4 models. \textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\_ratio, low\_freq\_ratio); under sampling, surprisal variability features (surp\_std, surp\_d1\_std, surp\_d2\_std) carry the dominant signal.}
644	\label{tab:cohens_d_full}
645	\begin{tabular}{@{}lrrrrrr@{}}
646	\toprule
647	Feature & \rotatebox{60}{Pythia-greedy} & \rotatebox{60}{Pythia-nuc09} & \rotatebox{60}{Qwen-1.5B-base} & \rotatebox{60}{Pythia-$T{=}1.2$} & \rotatebox{60}{LLaMA-3.1-8B} & \rotatebox{60}{Mistral-7B} \\
648	\midrule
649	surp\_mean & \textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\
650	surp\_std & $-$0.301 & \textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\
651	surp\_skew & \textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\
652	surp\_kurt & \textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\
653	surp\_d1\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \textbf{$+$0.080} & $+$0.026 \\
654	surp\_d1\_std & $-$0.318 & \textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\
655	surp\_d1\_skew & \textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\
656	surp\_d2\_mean & $+$0.004 & $+$0.001 & \textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\
657	surp\_d2\_std & $-$0.312 & \textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\
658	ttr & \textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\
659	hapax\_ratio & \textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\
660	self\_bleu & $-$0.056 & $+$0.031 & \textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\
661	freq\_kurtosis & $+$0.071 & \textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\
662	freq\_entropy & \textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\
663	low\_freq\_ratio & \textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\
664	\midrule
665	$\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\
666	\bottomrule
667	\end{tabular}
668	\end{table*}
669	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "17e2b32e-7a38-43d7-8600-bcf3418d6628",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\\eta^2_p$ is approximately 5$\\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nBoth Qwen2.5-1.5B and Pythia-1.4B yield $\\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$.\nCumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nThe two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\nThis convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. Both models yield $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{Qwen-1.5B}} & \\multicolumn{2}{c}{\\textbf{Pythia-1.4B}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n\\textbf{Pair} & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & 0.9837 & $[.982,\\,.985]$ & 0.9844 & $[.983,\\,.986]$ \\\\\n1v2 & 0.8971 & $[.895,\\,.899]$ & 0.9470 & $[.942,\\,.952]$ \\\\\n2v3 & 0.8098 & $[.805,\\,.814]$ & 0.8891 & $[.882,\\,.896]$ \\\\\n3v4 & 0.7600 & $[.753,\\,.767]$ & 0.7999 & $[.795,\\,.805]$ \\\\\n4v5 & 0.7459 & $[.738,\\,.754]$ & 0.6907 & $[.688,\\,.693]$ \\\\\n5v6 & 0.7017 & $[.696,\\,.708]$ & 0.6497 & $[.643,\\,.657]$ \\\\\n6v7 & 0.6410 & $[.638,\\,.645]$ & 0.6340 & $[.628,\\,.641]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CI methodology note.}\n\\label{sec:retrain_ci_note}\nThe main pipeline reports bootstrap 95\\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.\nIn the retrain-chain setting, each generation's training corpus is the \\emph{output} of the previous generation's fine-tuned model, creating inter-generation dependencies that standard bootstrap resampling cannot preserve without inflating AUC estimates.\nWe therefore report fold-based 95\\% CIs for retrain-chain experiments, computed as $\\bar{x} \\pm 1.96 \\cdot s / \\sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\\Kempirical$.}\n\\label{fig:theta_sensitivity}\n\\end{figure}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), confirming that EOS truncation does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), indicating that synthetic data at these proportions is net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), confirming that depth assignments beyond $\\Kempirical$ inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, making the exponential fit unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, explaining the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), indicating that domain lexical diversity can rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), indicating that scale in the 1B--14B range does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, confirming that arXiv's $\\Kempirical{=}3$ at the same sample size reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), indicating that deeper generations produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\\n3v4 & 0.5437 & 0.5468 & $+$0.003 \\\\\n\\midrule\n$\\Kempirical$ & 3 & 3 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nContent-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\\sim}$1.8\\,pp at the boundary pair).\nThe depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\\%, depth 5: $-$4.6\\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.\n\n\\subsection{Statistical Power Analysis}\n\\label{sec:power_curve}\n\nTo characterize the minimum sample size required for reliable $\\Kempirical$ determination, we subsample C4 at $n \\in \\{500, 1000, 2000, 3000, 4000, 5000\\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\\ref{tab:power_curve}, Figure~\\ref{fig:power_curve}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\n\\label{tab:power_curve}\n\\begin{tabular}{rccc}\n\\toprule\n$n$ & \\textbf{Mean 1v2 $\\auc$} & \\textbf{Std} & \\textbf{Detection Prob.} \\\\\n\\midrule\n500 & 0.581 & 0.018 & 20\\% \\\\\n1{,}000 & 0.591 & 0.014 & 30\\% \\\\\n2{,}000 & 0.610 & 0.009 & 100\\% \\\\\n3{,}000 & 0.617 & 0.005 & 100\\% \\\\\n4{,}000 & 0.622 & 0.004 & 100\\% \\\\\n5{,}000 & 0.629 & 0.000 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_power_curve.png}\n\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\n\\label{fig:power_curve}\n\\end{figure}\n\nDetection rate jumps from 20\\% ($n{=}500$) to 100\\% ($n{=}2{,}000$), with the 80\\% power threshold crossed near $n{=}1{,}500$.\nAt $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, confirming that our results are well above the minimum required for reliable boundary estimation.\nThe sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\n\n\\subsection{Feature Group Ablation}\n\\label{sec:feature_ablation}\n\nTo assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\\ref{sec:method}) on the 1\\,vs.\\,2 task using (a) each feature group alone (\\emph{single}) and (b) the full 15D set minus one group (\\emph{leave-one-out}).\nRepresentative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_ablation.pdf}\n\\caption{Feature group ablation heatmap for 1\\,vs.\\,2 classification AUC. \\emph{Left}: single-group performance. \\emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}\n\\label{fig:feature_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation for 1\\,vs.\\,2 classification (AUC). \\textbf{Single}: using only features from one group. \\textbf{Leave-one-out}: removing one group from the full 15D feature set. $\\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\\ref{tab:kstar_ci}.}\n\\label{tab:feature_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Single Group}} & \\multicolumn{3}{c}{\\textbf{Leave-One-Out ($\\Delta$)}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nFeature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\\\\n\\midrule\nSurprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\nSurprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\\\\nLexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\nFreq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\n\\midrule\nFull (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSurprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.\nOn C4 and Wikipedia, all LOO drops are small ($\\leq 0.007$, within cross-fold standard deviation), indicating that no single feature group is individually critical for the weaker low-$\\Kempirical$ signal.\nRemoving surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\\Kempirical$ domains.\n\n\\subsection{Classifier Choice: McNemar Test}\n\\label{sec:mcnemar_baselines}\n\nTo verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\\ref{tab:mcnemar_obd_baselines}).\nOf 36 comparisons, 31 are non-significant ($p \\geq 0.05$), and all five significant results concentrate in two model $\\times$ domain conditions.\nFor LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \\leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.\nFor Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \\textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}\n\\label{tab:mcnemar_obd_baselines}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{OBD Acc.} & \\textbf{vs.\\ LogReg} & \\textbf{vs.\\ LinearSVC} & \\textbf{vs.\\ RandomForest} \\\\\n\\midrule\nQwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\\\\nPythia-1.4B     & C4    & .631 & $\\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\\\\nLLaMA-8B        & C4    & .573 & $\\mathbf{6.2{\\times}10^{-5\\,***}}$ (.592) & $\\mathbf{1.1{\\times}10^{-4\\,***}}$ (.591) & $\\mathbf{.001^{**}}$ (.586) \\\\\n\\midrule\nQwen-1.5B      & Wiki  & .588 & $\\mathbf{9.4{\\times}10^{-4\\,***}}$ (.570) & $\\mathbf{2.3{\\times}10^{-4\\,***}}$ (.568) & .655 (.590) \\\\\nPythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\\\\nOLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\\\\nLLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\\\\n\\midrule\nQwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\\\\nPythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\\\\nOLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\\\\nQwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\\\\nMistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\n\\vspace{4pt}\n\\footnotesize\n36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.\nThe predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.\n\\end{table*}\n\n\\subsection{Domain Lexical Statistics}\n\\label{sec:domain_lexical_stats}\n\nTable~\\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.\nThe TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\\ Wikipedia).\nVocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).\nThis reversal likely reflects C4's greater content heterogeneity (higher variance: $\\sigma = 0.706$ vs.\\ $0.284$), which inflates TTR but depresses mean entropy.\nAs depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\\Kempirical$ and slower convergence to the stationary distribution.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.\nAt depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\\,=\\,0.755, $H$\\,=\\,6.853),\nfollowed by C4 and Wikipedia.\nAs depth increases, all domains converge, with arXiv showing the steepest decline.\nCohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}\n\\label{tab:domain-ttr-entropy}\n\\begin{tabular}{ll rrr rrr}\n\\toprule\n& & \\multicolumn{3}{c}{\\textbf{TTR}} & \\multicolumn{3}{c}{\\textbf{Vocab Entropy ($H$)}} \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Depth} & $N$ & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} \\\\\n\\midrule\n0 & 5k/5k/2.2k & .665\\tpm.061 & .720\\tpm.105 & \\textbf{.755}\\tpm.055 & 6.408\\tpm.284 & 6.225\\tpm.706 & \\textbf{6.853}\\tpm.295 \\\\\n1 &             & .655\\tpm.121 & .707\\tpm.149 & \\textbf{.732}\\tpm.098 & 5.932\\tpm.843 & 5.737\\tpm1.189 & \\textbf{6.113}\\tpm.655 \\\\\n2 &             & .647\\tpm.145 & .676\\tpm.159 & \\textbf{.677}\\tpm.131 & 5.784\\tpm.905 & 5.774\\tpm1.139 & \\textbf{5.998}\\tpm.967 \\\\\n3 &             & .645\\tpm.159 & \\textbf{.662}\\tpm.164 & .635\\tpm.134 & 5.664\\tpm1.085 & 5.743\\tpm1.161 & \\textbf{5.964}\\tpm.933 \\\\\n4 &             & .636\\tpm.164 & \\textbf{.647}\\tpm.169 & .621\\tpm.140 & 5.660\\tpm1.062 & 5.758\\tpm1.167 & \\textbf{5.898}\\tpm.942 \\\\\n5 &             & .632\\tpm.172 & \\textbf{.636}\\tpm.175 & .618\\tpm.150 & 5.593\\tpm1.130 & 5.772\\tpm1.141 & \\textbf{5.816}\\tpm.968 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\\\\n\\multicolumn{2}{l}{C4 vs.\\ Wiki}   & \\multicolumn{3}{c}{$d = +0.65$} & \\multicolumn{3}{c}{$d = -0.34$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ C4}  & \\multicolumn{3}{c}{$d = +0.37$} & \\multicolumn{3}{c}{$d = +1.03$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ Wiki} & \\multicolumn{3}{c}{$d = +1.52$} & \\multicolumn{3}{c}{$d = +1.55$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Leave-One-Family-Out Threshold Validation}\n\\label{sec:theta_lofo}\n\nTo validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\nTable~\\ref{tab:theta_lofo} reports results across all three domains.\n\nOn C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\nThe single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, making the discrepancy attributable to mode rather than threshold instability.\nThe derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\n\nArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\n\nWikipedia yields only 1/6 agreement (17\\%).\nThis failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ is narrow or inverted, invalidating the gap-based threshold derivation.\nWikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\n\\label{tab:theta_lofo}\n\\begin{tabular}{l l l c c c c c c}\n\\toprule\nDomain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\n\\midrule\nC4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\n\\midrule\narXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \\cmark \\\\\n &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\n\\midrule\nWikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \\xmark \\\\\n & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \\xmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \\xmark \\\\\n & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \\xmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Code Domain Results}\n\\label{sec:code_domain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\n\\label{tab:code_domain_qwen}\n\\begin{tabular}{l c c c}\n\\toprule\nPair & AUC & 95\\% CI & JSD \\\\\n\\midrule\n0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\\\\n1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\\\\n2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\\\\n3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\\\\n4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\\\\n\\midrule\n\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\\% CIs. Qwen2.5-1.5B yields $\\Kempirical{=}2$; Pythia-1.4B yields borderline $\\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \\theta$). Additional models pending completion.}\n\\label{tab:code_crossmodel_kstar}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen2.5-1.5B} & \\multicolumn{2}{c}{Pythia-1.4B} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n & AUC & 95\\% CI & AUC & 95\\% CI \\\\\n\\midrule\n0v1 & .9388 & [.929,\\,.949] & \\textbf{.9592} & [.956,\\,.963] \\\\\n1v2 & \\textbf{.7382} & [.709,\\,.767]\\rlap{$^*$} & .5983 & [.593,\\,.603] \\\\\n2v3 & .5300 & [.514,\\,.546] & .5215 & --- \\\\\n3v4 & .5022 & --- & .5152 & --- \\\\\n4v5 & .5219 & --- & .5046 & --- \\\\\n\\midrule\n$K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}\n\\label{sec:borderline_analysis}\n\nTo understand why Mistral-7B yields $\\Kempirical{=}1$ while other C4 models yield $\\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).\n\nMistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\\ 2.90--3.02 for other models), indicating that the scorer model already finds Mistral's output highly predictable.\nThis compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\\bar{|d|} = 0.112$; Table~\\ref{tab:cohens_d_full}), and no single feature exceeds 13\\% of total classifier importance.\nThe borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.\n\nGreedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\\ = normalized LightGBM gain importance (\\%). $\\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\\Delta\\text{surp}_{1\\to2}$: change in mean surprisal from depth 1 to depth 2.}\n\\label{tab:borderline_features}\n\\begin{tabular}{@{}llc lcc@{}}\n\\toprule\nCategory & Model & AUC & Top-3 Features (Imp.\\%) & $\\bar{|d|}$ & $\\Delta\\text{surp}_{1\\to2}$ \\\\\n\\midrule\nStrong & Pythia-greedy & 0.884 & hapax\\_ratio (47), surp\\_mean (11), low\\_freq\\_ratio (8) & 0.365 & $-$0.160 \\\\\nStrong & Pythia-nuc09 & 0.677 & surp\\_std (20), freq\\_entropy (11), surp\\_d1\\_std (8) & 0.170 & $-$0.196 \\\\\nStrong & Qwen-1.5B-base & 0.626 & surp\\_std (13), freq\\_entropy (10), surp\\_mean (9) & 0.125 & $-$0.159 \\\\\n\\midrule\nBorderline & Pythia-$T{=}1.2$ & 0.617 & surp\\_std (15), freq\\_entropy (10), surp\\_kurt (8) & 0.112 & $-$0.059 \\\\\nBorderline & LLaMA-3.1-8B & 0.612 & surp\\_std (12), surp\\_d1\\_std (10), freq\\_entropy (9) & 0.137 & $-$0.215 \\\\\n\\midrule\nBelow $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[h]\n\\centering\n\\scriptsize\n\\caption{Cohen's $d$ (depth-1 vs.\\ depth-2) for all 15 features across six C4 models. \\textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\\_ratio, low\\_freq\\_ratio); under sampling, surprisal variability features (surp\\_std, surp\\_d1\\_std, surp\\_d2\\_std) carry the dominant signal.}\n\\label{tab:cohens_d_full}\n\\begin{tabular}{@{}lrrrrrr@{}}\n\\toprule\nFeature & \\rotatebox{60}{Pythia-greedy} & \\rotatebox{60}{Pythia-nuc09} & \\rotatebox{60}{Qwen-1.5B-base} & \\rotatebox{60}{Pythia-$T{=}1.2$} & \\rotatebox{60}{LLaMA-3.1-8B} & \\rotatebox{60}{Mistral-7B} \\\\\n\\midrule\nsurp\\_mean & \\textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\\\\nsurp\\_std & $-$0.301 & \\textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\\\\nsurp\\_skew & \\textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\\\\nsurp\\_kurt & \\textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\\\\nsurp\\_d1\\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \\textbf{$+$0.080} & $+$0.026 \\\\\nsurp\\_d1\\_std & $-$0.318 & \\textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\\\\nsurp\\_d1\\_skew & \\textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\\\\nsurp\\_d2\\_mean & $+$0.004 & $+$0.001 & \\textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\\\\nsurp\\_d2\\_std & $-$0.312 & \\textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\\\\nttr & \\textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\\\\nhapax\\_ratio & \\textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\\\\nself\\_bleu & $-$0.056 & $+$0.031 & \\textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\\\\nfreq\\_kurtosis & $+$0.071 & \\textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\\\\nfreq\\_entropy & \\textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\\\\nlow\\_freq\\_ratio & \\textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\\\\n\\midrule\n$\\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 669,
      "startLine": 1,
      "totalLines": 669
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the file contents. Let me make the edits:

**Task A: Fix 6 -ing phrases**

1. **introduction.tex:8** — "...treats all machine-generated text identically, discarding the generational depth dimension."
   - Change to something like: "...treats all machine-generated text identically; the generational depth dimension is entirely ignored."
   - Or: "...treats all machine-generated text identically and ignores the generational depth dimension."

2. **introduction.tex:21** — "...information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$."
   - I need to split this into two independent sentences or use a "which" clause instead. The instruction warns against using "This indicates/confirms/produces" as those are AI markers. So I could write: "...information degrades monotonically across generations, which motivates a finite discrimination boundary $\Kstar$." or restructure it as two separate sentences entirely.
   - For the second issue, I'm looking at how to rephrase the "producing" construction in the discussion section. The sentence currently chains multiple clauses together, so I should break it into cleaner independent statements that avoid the "producing" connector.
   - On the third point, I'm reconsidering the phrasing around "paralleling" — swapping it for "consistent with" feels more direct and avoids the slightly awkward parallel construction while maintaining the same logical relationship between Pythia's code performance and its surprisal range.
   - For the fourth item, I need to rethink the structure entirely since the constraint flags -ing constructions; splitting it into two independent clauses with a semicolon lets me explain the causal relationship more clearly without relying on that participle form. I'm settling on "which reinforces" as the phrasing since it follows the guidelines, then moving to fix the next sentence by converting it to a semicolon structure that makes the boundary weakening claim more direct. Let me also verify the references and check the appendix for the retrain-chain discussion.

Looking at the extended appendix, the retrain-chain results show both models reaching $\Kempirical{=}7$ under LoRA fine-tuning—a significant jump from the prompt-chain baseline of 2—with cumulative adaptation artifacts like vocabulary narrowing making each generation increasingly distinguishable, and the convergence metrics suggesting this represents a practical ceiling for detection depth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "c0df2f37-94ce-4b5c-9709-f6dcf1515e0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fdsh4X6CzmKh6pg5b4Skzh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26760,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26760
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

_source line 15_

Let me verify the bib entries exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "694bff0f-2bfd-43ef-849c-4bb013fcc72b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fdsh4X6CzmKh6pg5b4Skzh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26760,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26760
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01632PeV91xY35qq1y45SNPY`</summary>

```json
{
  "pattern": "bertrand2024stability|gerstgrasser2024model",
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
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "88634516-f1f2-411f-b53c-c0c293b584ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fdsh4X6CzmKh6pg5b4Skzh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 26760,
      "cache_read_input_tokens": 25787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 26760
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

_source line 17 · 2026-05-19T03:59:08.387Z_

<details><summary>↩ Tool result · `toolu_01632PeV91xY35qq1y45SNPY`</summary>

```text
docs/paper/related_work.tex:5:Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
docs/paper/main.bbl:105:  Koyejo}]{gerstgrasser2024model}
docs/paper/references.bib:79:@inproceedings{bertrand2024stability,
docs/paper/references.bib:213:@inproceedings{gerstgrasser2024model,
docs/paper/main.aux:101:\citation{schaeffer2025position,kazdan2025collapse,gerstgrasser2024model,shi2025collapse}
docs/paper/main.aux:893:\bibcite{gerstgrasser2024model}{{16}{2024}{{Gerstgrasser et~al.}}{{Gerstgrasser, Schaeffer, Dey, Rafailov, Sleight, Hughes, Korbak, Agrawal, Pai, Gromov, Roberts, Yang, Donoho, and Koyejo}}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "0702ffd6-aabc-46af-989b-f8a4429768d0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:5:Iterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.\ndocs/paper/main.bbl:105:  Koyejo}]{gerstgrasser2024model}\ndocs/paper/references.bib:79:@inproceedings{bertrand2024stability,\ndocs/paper/references.bib:213:@inproceedings{gerstgrasser2024model,\ndocs/paper/main.aux:101:\\citation{schaeffer2025position,kazdan2025collapse,gerstgrasser2024model,shi2025collapse}\ndocs/paper/main.aux:893:\\bibcite{gerstgrasser2024model}{{16}{2024}{{Gerstgrasser et~al.}}{{Gerstgrasser, Schaeffer, Dey, Rafailov, Sleight, Hughes, Korbak, Agrawal, Pai, Gromov, Roberts, Yang, Donoho, and Koyejo}}}",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Good. Both `bertrand2024stability` and `gerstgrasser2024model` exist in `references.bib`. `gerstgrasser2024model` is already cited in `related_work.tex`, but `bertrand2024stability` is not cited anywhere in the paper. Let me now verify that.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "ca9c31f1-9eab-46e2-ba1f-8eaf032a559b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 19_

Both bib entries exist. `bertrand2024stability` is uncited; `gerstgrasser2024model` is cited in `related_work.tex` but not in the appendix discussion. Now applying all edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "5c9ee45a-943a-4f42-a8b1-103bb3f29cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01MjWFfGBn8JnJjZSKZB5Dxh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
  "old_string": "Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.",
  "new_string": "Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "ce16bb9a-f63e-4397-a4ac-ad4dbdce497e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 21 · 2026-05-19T04:05:20.313Z_

<details><summary>↩ Tool result · `toolu_01MjWFfGBn8JnJjZSKZB5Dxh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "83281342-a354-404d-970f-783ab35e2672",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
    "oldString": "Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.",
    "newString": "Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.\n\nThis gap cuts across multiple communities.\nBinary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}).\nMembership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\\Kempirical{=}2$ on C4 ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering}: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}), and $\\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " Estimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.",
          " When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.",
          " This degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).",
          "-Yet the dominant paradigm treats all machine-generated text identically, discarding the generational depth dimension.",
          "+Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.",
          " ",
          " This gap cuts across multiple communities.",
          " Binary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence})."
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01PzhURcR4AH6QzHjS3WtHJy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
  "old_string": "The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.",
  "new_string": "The Data Processing Inequality implies that information degrades monotonically across generations; a finite discrimination boundary $\\Kstar$ follows from this monotonic loss."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "0d9b674c-6a29-4b0d-9998-8c942cf77095",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 23 · 2026-05-19T04:05:22.650Z_

<details><summary>↩ Tool result · `toolu_01PzhURcR4AH6QzHjS3WtHJy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "bfc458a2-8218-4491-9570-55379b8a7cb1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
    "oldString": "The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.",
    "newString": "The Data Processing Inequality implies that information degrades monotonically across generations; a finite discrimination boundary $\\Kstar$ follows from this monotonic loss.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.\n\nThis gap cuts across multiple communities.\nBinary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}).\nMembership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\\Kempirical{=}2$ on C4 ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering}: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}), and $\\Kempirical{=}2$ correctly predicts binary filtering as optimal granularity for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.",
          " $\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.",
          " ",
          "-The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$.",
          "+The Data Processing Inequality implies that information degrades monotonically across generations; a finite discrimination boundary $\\Kstar$ follows from this monotonic loss.",
          " We empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.",
          " We operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).",
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_011tbFqaXsZkuZzxLDA4i4wh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
  "new_string": "and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "0245b63b-e780-4186-be7b-4ddd723600ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 25 · 2026-05-19T04:05:26.153Z_

<details><summary>↩ Tool result · `toolu_011tbFqaXsZkuZzxLDA4i4wh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "937b7f7d-8c2b-463b-83bb-1df65518a224",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "oldString": "and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
    "newString": "and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nBaseline classifier substitution (logistic regression, linear SVC, random forest) yields non-significant McNemar differences in 31/36 comparisons (Table~\\ref{tab:mcnemar_obd_baselines}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$); cross-model consistency indicates the contraction rate is domain-governed.\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts: $\\Kempirical{=}7$ for both Qwen-1.5B and Pythia-1.4B LoRA (Table~\\ref{tab:retrain_ci}), 5 generations beyond prompt-chain $\\Kempirical{=}2$ (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels and graduated weighting injects noise (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$; on arXiv ($\\Kempirical{=}3$), graduated filtering similarly shows no improvement, consistent with $\\Kempirical$ capturing discriminability rather than curation utility.\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nFor Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.\nPythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (depth-0 mean surprisal 2.32 vs.\\ 2.90--3.02 for $\\Kempirical{=}2$ models; mean $|\\text{Cohen's}\\;d| = 0.112$; Table~\\ref{tab:cohens_d_full}).\nLarger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ across six C4 configurations (Table~\\ref{tab:borderline_features}); this attenuation predicts that $\\Kempirical$ may decrease as capability scales beyond 14B (Qwen-14B: $\\Kempirical{=}2$, $\\auc = 0.621$).\n\n\\paragraph{Why $\\Kempirical$ matters.}\nFor curation, $\\Kempirical{=}2$ validates binary filtering for web text (Section~\\ref{sec:filtering}) and provides post-hoc grounding for the binary approach of \\citet{drayson2025}.\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 7,
        "newStart": 32,
        "newLines": 7,
        "lines": [
          " $\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).",
          " ",
          " \\paragraph{Domain dependence of $\\Kempirical$.}",
          "-C4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}), producing a consistent ordering that correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
          "+C4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
          " For Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.",
          " Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
          " The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation})."
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01HuGEudcew1cVTayWovokLp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
  "new_string": "Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "97b4eaa1-9b63-4d61-83df-15b945984a9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 27 · 2026-05-19T04:05:29.291Z_

<details><summary>↩ Tool result · `toolu_01HuGEudcew1cVTayWovokLp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "ba16a57e-972f-4c41-9398-52e40c03be3c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "oldString": "Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
    "newString": "Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nBaseline classifier substitution (logistic regression, linear SVC, random forest) yields non-significant McNemar differences in 31/36 comparisons (Table~\\ref{tab:mcnemar_obd_baselines}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$); cross-model consistency indicates the contraction rate is domain-governed.\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts: $\\Kempirical{=}7$ for both Qwen-1.5B and Pythia-1.4B LoRA (Table~\\ref{tab:retrain_ci}), 5 generations beyond prompt-chain $\\Kempirical{=}2$ (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels and graduated weighting injects noise (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$; on arXiv ($\\Kempirical{=}3$), graduated filtering similarly shows no improvement, consistent with $\\Kempirical$ capturing discriminability rather than curation utility.\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nFor Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.\nPythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (depth-0 mean surprisal 2.32 vs.\\ 2.90--3.02 for $\\Kempirical{=}2$ models; mean $|\\text{Cohen's}\\;d| = 0.112$; Table~\\ref{tab:cohens_d_full}).\nLarger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ across six C4 configurations (Table~\\ref{tab:borderline_features}); this attenuation predicts that $\\Kempirical$ may decrease as capability scales beyond 14B (Qwen-14B: $\\Kempirical{=}2$, $\\auc = 0.621$).\n\n\\paragraph{Why $\\Kempirical$ matters.}\nFor curation, $\\Kempirical{=}2$ validates binary filtering for web text (Section~\\ref{sec:filtering}) and provides post-hoc grounding for the binary approach of \\citet{drayson2025}.\n",
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 34,
        "newLines": 7,
        "lines": [
          " \\paragraph{Domain dependence of $\\Kempirical$.}",
          " C4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
          " For Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.",
          "-Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), paralleling its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
          "+Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
          " The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).",
          " ",
          " \\paragraph{Surprisal attenuation and boundary variation.}"
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01CdDhUucZGDtiQ1RrFefXLS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
  "old_string": "The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation",
  "new_string": "The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, which reinforces the domain-governed interpretation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "65549ee3-9322-44d3-a147-d14de7df7438",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 29 · 2026-05-19T04:05:32.179Z_

<details><summary>↩ Tool result · `toolu_01CdDhUucZGDtiQ1RrFefXLS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "c0562fac-53f0-4b2b-b529-885fe002aab4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "oldString": "The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation",
    "newString": "The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, which reinforces the domain-governed interpretation",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$.\nA single generation pass renders text indistinguishable from multiply recycled content, limiting depth-aware curation to a binary boundary.\nConverging evidence supports a data-intrinsic interpretation: OBD achieves 96\\% depth-0 recall but only 14--22\\% for depths 2--4; frontier LLMs show 8--38\\% (McNemar $p > 0.05$ vs.\\ OBD; Table~\\ref{tab:s3_llm_zeroshot}).\nBaseline classifier substitution (logistic regression, linear SVC, random forest) yields non-significant McNemar differences in 31/36 comparisons (Table~\\ref{tab:mcnemar_obd_baselines}).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$); cross-model consistency indicates the contraction rate is domain-governed.\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts: $\\Kempirical{=}7$ for both Qwen-1.5B and Pythia-1.4B LoRA (Table~\\ref{tab:retrain_ci}), 5 generations beyond prompt-chain $\\Kempirical{=}2$ (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels and graduated weighting injects noise (Appendix~\\ref{sec:extended_limitations}).\nThe strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$; on arXiv ($\\Kempirical{=}3$), graduated filtering similarly shows no improvement, consistent with $\\Kempirical$ capturing discriminability rather than curation utility.\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nFor Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.\nPythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (depth-0 mean surprisal 2.32 vs.\\ 2.90--3.02 for $\\Kempirical{=}2$ models; mean $|\\text{Cohen's}\\;d| = 0.112$; Table~\\ref{tab:cohens_d_full}).\nLarger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ across six C4 configurations (Table~\\ref{tab:borderline_features}); this attenuation predicts that $\\Kempirical$ may decrease as capability scales beyond 14B (Qwen-14B: $\\Kempirical{=}2$, $\\auc = 0.621$).\n\n\\paragraph{Why $\\Kempirical$ matters.}\nFor curation, $\\Kempirical{=}2$ validates binary filtering for web text (Section~\\ref{sec:filtering}) and provides post-hoc grounding for the binary approach of \\citet{drayson2025}.\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 7,
        "newStart": 35,
        "newLines": 7,
        "lines": [
          " C4 web text yields $\\Kempirical{=}2$ (8/9 configurations, 1B--14B), Python code yields $\\Kempirical{=}2$ for Qwen2.5-1.5B (1v2 $\\auc = 0.74$) and borderline $\\Kempirical{=}1$ for Pythia-1.4B (1v2 $\\auc = 0.598$, CI $[0.593, 0.603]$; Section~\\ref{sec:cross_domain}), arXiv yields $\\Kempirical{=}3$ (five models, four families), and Wikipedia yields $\\Kempirical{=}1$ with scorer confound controlled (Appendix~\\ref{sec:wiki_domain}); the resulting ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).",
          " For Qwen, code and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: C4 collapses at 0v1$\\to$1v2 ($9.8\\times$ JSD drop), while code collapses at 1v2$\\to$2v3 ($11.7\\times$) because syntactic constraints (indentation, bracket matching, keyword frequencies) preserve depth-1 signal.",
          " Pythia's code 1v2 falls just below $\\theta$ (CI upper $= 0.603$), consistent with its narrower surprisal dynamic range on code generation; domain structure thus governs not only $\\Kempirical$ but also the decay profile.",
          "-The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, reinforcing the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).",
          "+The only C4 exception (Mistral-7B, $\\Kempirical{=}1$) has $\\Kempirical{=}3$ on arXiv, which reinforces the domain-governed interpretation (Appendix~\\ref{sec:boundary_extended}); a LaTeX markup ablation confirms content-level properties dominate (2v3 $\\Delta = -1.8$\\,pp, $\\Kempirical$ unchanged; Appendix~\\ref{sec:latex_ablation}).",
          " ",
          " \\paragraph{Surprisal attenuation and boundary variation.}",
          " \\label{sec:surprisal_attenuation}"
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01YMKMrWfUk9ENPLDXHtLwyz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
  "old_string": "512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.",
  "new_string": "512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "3a56c3cb-938b-42f3-a8ae-4c13f847700f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 31 · 2026-05-19T04:05:33.606Z_

<details><summary>↩ Tool result · `toolu_01YMKMrWfUk9ENPLDXHtLwyz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "7fdcef8e-2f8b-4bbe-9c96-86183affd323",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "oldString": "512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.",
    "newString": "512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths.",
    "originalFile": "% EMNLP 2026 Main - ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{pifont}\n\\newcommand{\\cmark}{\\ding{51}}\n\\newcommand{\\xmark}{\\ding{55}}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\\newcommand{\\tpm}{\\ensuremath{\\,\\pm\\,}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\\theta{=}0.60$ (AUC decision threshold), $\\Kempirical{=}2$ for general web text (8/9 model configurations), $\\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\\Kempirical{=}3$ for structured academic text (arXiv).\nA single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nLargely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\\Kempirical$ is largely robust to scorer choice.\nDownstream, $\\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with two models (Qwen2.5-1.5B, $\\Kempirical{=}2$; Pythia-1.4B, borderline $\\Kempirical{=}1$ with 1v2 CI upper $> \\theta$); subsampling analysis indicates $n{\\geq}2{,}000$ suffices for 100\\% reliable $\\Kempirical$ determination (Appendix~\\ref{sec:power_curve}).\n(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\n(8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 7,
        "newStart": 74,
        "newLines": 7,
        "lines": [
          " (3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).",
          " (4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B represents the most marginal $\\Kempirical{=}2$ assignment, with the 1v2 CI lower bound within 0.3 percentage points of $\\theta$.",
          " (5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).",
          "-(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$), indicating the boundary weakens at longer generation lengths.",
          "+(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths.",
          " (7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).",
          " (8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.",
          " Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}."
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01NGwnpaLZSiDrpwKnXMjv8i`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.",
  "new_string": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nThe extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "28fcae98-83ab-45f7-a13e-1ee8cbd46c41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161fYzE86AFKo7AfMU7Zjn6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2230,
      "cache_read_input_tokens": 52547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2230
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

_source line 33 · 2026-05-19T04:05:38.778Z_

<details><summary>↩ Tool result · reported error · `toolu_01NGwnpaLZSiDrpwKnXMjv8i`</summary>

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
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "b3d6631e-a625-4bd3-a7a0-b17f4c2039ec",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
The appendix_extended.tex edit failed because the file was modified. Let me re-read it and try again.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "1c2b4a60-23c0-4d83-83d8-65567496c373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFxaHbEHqCgZeVpxHbXRcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2400,
      "cache_read_input_tokens": 54777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2400
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_013g9FAavxp1p7XVYstPs9L8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 36,
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
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "4bca55cd-eb2d-4ade-ab91-97944753f9a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MFxaHbEHqCgZeVpxHbXRcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2400,
      "cache_read_input_tokens": 54777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2400
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T04:05:42.697Z_

<details><summary>↩ Tool result · `toolu_013g9FAavxp1p7XVYstPs9L8`</summary>

```text
36	\emph{Prompt-chain versus retrain-chain.}
37	Both Qwen2.5-1.5B and Pythia-1.4B yield $\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$.
38	Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
40	This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.
41	Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models, suggesting $\Kempirical{=}7$ is near the ceiling.
42	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
43	
44	\begin{table}[h]
45	\centering
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "8b2fc01d-3371-4250-a539-337320b6461c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\emph{Prompt-chain versus retrain-chain.}\nBoth Qwen2.5-1.5B and Pythia-1.4B yield $\\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$.\nCumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nThe two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\nThis convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering",
      "numLines": 10,
      "startLine": 36,
      "totalLines": 669
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01JNYmG8LZ2yiGz5WYvsA1L5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "old_string": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.",
  "new_string": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nThe extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "ab2e7f62-1186-43ed-a0e9-61a538b3e9b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSmiJ55egxp5qp7ooQEfJx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3010,
      "cache_read_input_tokens": 54777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3010
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T04:05:50.139Z_

<details><summary>↩ Tool result · `toolu_01JNYmG8LZ2yiGz5WYvsA1L5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "f1aeb08a-ffc7-4f3d-9f03-a2e00d83622e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "oldString": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.",
    "newString": "This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nThe extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.",
    "originalFile": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\\eta^2_p$ is approximately 5$\\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nBoth Qwen2.5-1.5B and Pythia-1.4B yield $\\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$.\nCumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nThe two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\nThis convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. Both models yield $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{Qwen-1.5B}} & \\multicolumn{2}{c}{\\textbf{Pythia-1.4B}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n\\textbf{Pair} & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & 0.9837 & $[.982,\\,.985]$ & 0.9844 & $[.983,\\,.986]$ \\\\\n1v2 & 0.8971 & $[.895,\\,.899]$ & 0.9470 & $[.942,\\,.952]$ \\\\\n2v3 & 0.8098 & $[.805,\\,.814]$ & 0.8891 & $[.882,\\,.896]$ \\\\\n3v4 & 0.7600 & $[.753,\\,.767]$ & 0.7999 & $[.795,\\,.805]$ \\\\\n4v5 & 0.7459 & $[.738,\\,.754]$ & 0.6907 & $[.688,\\,.693]$ \\\\\n5v6 & 0.7017 & $[.696,\\,.708]$ & 0.6497 & $[.643,\\,.657]$ \\\\\n6v7 & 0.6410 & $[.638,\\,.645]$ & 0.6340 & $[.628,\\,.641]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CI methodology note.}\n\\label{sec:retrain_ci_note}\nThe main pipeline reports bootstrap 95\\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.\nIn the retrain-chain setting, each generation's training corpus is the \\emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.\nWe therefore report fold-based 95\\% CIs for retrain-chain experiments, computed as $\\bar{x} \\pm 1.96 \\cdot s / \\sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences, confirming that source domain rather than model identity governs $\\Kempirical$.}\n\\label{fig:theta_sensitivity}\n\\end{figure}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), EOS truncation therefore does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), depth assignments beyond $\\Kempirical$ therefore inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on both C4 and Wikipedia, it yields $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, arXiv's $\\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\\n3v4 & 0.5437 & 0.5468 & $+$0.003 \\\\\n\\midrule\n$\\Kempirical$ & 3 & 3 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nContent-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\\sim}$1.8\\,pp at the boundary pair).\nThe depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\\%, depth 5: $-$4.6\\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.\n\n\\subsection{Statistical Power Analysis}\n\\label{sec:power_curve}\n\nTo characterize the minimum sample size required for reliable $\\Kempirical$ determination, we subsample C4 at $n \\in \\{500, 1000, 2000, 3000, 4000, 5000\\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\\ref{tab:power_curve}, Figure~\\ref{fig:power_curve}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\n\\label{tab:power_curve}\n\\begin{tabular}{rccc}\n\\toprule\n$n$ & \\textbf{Mean 1v2 $\\auc$} & \\textbf{Std} & \\textbf{Detection Prob.} \\\\\n\\midrule\n500 & 0.581 & 0.018 & 20\\% \\\\\n1{,}000 & 0.591 & 0.014 & 30\\% \\\\\n2{,}000 & 0.610 & 0.009 & 100\\% \\\\\n3{,}000 & 0.617 & 0.005 & 100\\% \\\\\n4{,}000 & 0.622 & 0.004 & 100\\% \\\\\n5{,}000 & 0.629 & 0.000 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_power_curve.png}\n\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\n\\label{fig:power_curve}\n\\end{figure}\n\nDetection rate jumps from 20\\% ($n{=}500$) to 100\\% ($n{=}2{,}000$), with the 80\\% power threshold crossed near $n{=}1{,}500$.\nAt $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, our results are therefore well above the minimum required for reliable boundary estimation.\nThe sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\n\n\\subsection{Feature Group Ablation}\n\\label{sec:feature_ablation}\n\nTo assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\\ref{sec:method}) on the 1\\,vs.\\,2 task using (a) each feature group alone (\\emph{single}) and (b) the full 15D set minus one group (\\emph{leave-one-out}).\nRepresentative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_ablation.pdf}\n\\caption{Feature group ablation heatmap for 1\\,vs.\\,2 classification AUC. \\emph{Left}: single-group performance. \\emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}\n\\label{fig:feature_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation for 1\\,vs.\\,2 classification (AUC). \\textbf{Single}: using only features from one group. \\textbf{Leave-one-out}: removing one group from the full 15D feature set. $\\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\\ref{tab:kstar_ci}.}\n\\label{tab:feature_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Single Group}} & \\multicolumn{3}{c}{\\textbf{Leave-One-Out ($\\Delta$)}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nFeature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\\\\n\\midrule\nSurprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\nSurprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\\\\nLexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\nFreq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\n\\midrule\nFull (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSurprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.\nOn C4 and Wikipedia, all LOO drops are small ($\\leq 0.007$, within cross-fold standard deviation), no single feature group is therefore individually critical for the weaker low-$\\Kempirical$ signal.\nRemoving surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004), suggesting partial redundancy with the base surprisal group in low-$\\Kempirical$ domains.\n\n\\subsection{Classifier Choice: McNemar Test}\n\\label{sec:mcnemar_baselines}\n\nTo verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\\ref{tab:mcnemar_obd_baselines}).\nOf 36 comparisons, 31 are non-significant ($p \\geq 0.05$), and all five significant results concentrate in two model $\\times$ domain conditions.\nFor LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \\leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.\nFor Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \\textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}\n\\label{tab:mcnemar_obd_baselines}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{OBD Acc.} & \\textbf{vs.\\ LogReg} & \\textbf{vs.\\ LinearSVC} & \\textbf{vs.\\ RandomForest} \\\\\n\\midrule\nQwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\\\\nPythia-1.4B     & C4    & .631 & $\\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\\\\nLLaMA-8B        & C4    & .573 & $\\mathbf{6.2{\\times}10^{-5\\,***}}$ (.592) & $\\mathbf{1.1{\\times}10^{-4\\,***}}$ (.591) & $\\mathbf{.001^{**}}$ (.586) \\\\\n\\midrule\nQwen-1.5B      & Wiki  & .588 & $\\mathbf{9.4{\\times}10^{-4\\,***}}$ (.570) & $\\mathbf{2.3{\\times}10^{-4\\,***}}$ (.568) & .655 (.590) \\\\\nPythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\\\\nOLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\\\\nLLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\\\\n\\midrule\nQwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\\\\nPythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\\\\nOLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\\\\nQwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\\\\nMistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\n\\vspace{4pt}\n\\footnotesize\n36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.\nThe predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.\n\\end{table*}\n\n\\subsection{Domain Lexical Statistics}\n\\label{sec:domain_lexical_stats}\n\nTable~\\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.\nThe TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\\ Wikipedia).\nVocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).\nThis reversal likely reflects C4's greater content heterogeneity (higher variance: $\\sigma = 0.706$ vs.\\ $0.284$), which inflates TTR but depresses mean entropy.\nAs depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\\Kempirical$ and slower convergence to the stationary distribution.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.\nAt depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\\,=\\,0.755, $H$\\,=\\,6.853),\nfollowed by C4 and Wikipedia.\nAs depth increases, all domains converge, with arXiv showing the steepest decline.\nCohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}\n\\label{tab:domain-ttr-entropy}\n\\begin{tabular}{ll rrr rrr}\n\\toprule\n& & \\multicolumn{3}{c}{\\textbf{TTR}} & \\multicolumn{3}{c}{\\textbf{Vocab Entropy ($H$)}} \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Depth} & $N$ & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} \\\\\n\\midrule\n0 & 5k/5k/2.2k & .665\\tpm.061 & .720\\tpm.105 & \\textbf{.755}\\tpm.055 & 6.408\\tpm.284 & 6.225\\tpm.706 & \\textbf{6.853}\\tpm.295 \\\\\n1 &             & .655\\tpm.121 & .707\\tpm.149 & \\textbf{.732}\\tpm.098 & 5.932\\tpm.843 & 5.737\\tpm1.189 & \\textbf{6.113}\\tpm.655 \\\\\n2 &             & .647\\tpm.145 & .676\\tpm.159 & \\textbf{.677}\\tpm.131 & 5.784\\tpm.905 & 5.774\\tpm1.139 & \\textbf{5.998}\\tpm.967 \\\\\n3 &             & .645\\tpm.159 & \\textbf{.662}\\tpm.164 & .635\\tpm.134 & 5.664\\tpm1.085 & 5.743\\tpm1.161 & \\textbf{5.964}\\tpm.933 \\\\\n4 &             & .636\\tpm.164 & \\textbf{.647}\\tpm.169 & .621\\tpm.140 & 5.660\\tpm1.062 & 5.758\\tpm1.167 & \\textbf{5.898}\\tpm.942 \\\\\n5 &             & .632\\tpm.172 & \\textbf{.636}\\tpm.175 & .618\\tpm.150 & 5.593\\tpm1.130 & 5.772\\tpm1.141 & \\textbf{5.816}\\tpm.968 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\\\\n\\multicolumn{2}{l}{C4 vs.\\ Wiki}   & \\multicolumn{3}{c}{$d = +0.65$} & \\multicolumn{3}{c}{$d = -0.34$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ C4}  & \\multicolumn{3}{c}{$d = +0.37$} & \\multicolumn{3}{c}{$d = +1.03$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ Wiki} & \\multicolumn{3}{c}{$d = +1.52$} & \\multicolumn{3}{c}{$d = +1.55$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Leave-One-Family-Out Threshold Validation}\n\\label{sec:theta_lofo}\n\nTo validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\nTable~\\ref{tab:theta_lofo} reports results across all three domains.\n\nOn C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\nThe single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.\nThe derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\n\nArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\n\nWikipedia yields only 1/6 agreement (17\\%).\nThis failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ is narrow or inverted, the gap-based threshold derivation is therefore invalid.\nWikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\n\\label{tab:theta_lofo}\n\\begin{tabular}{l l l c c c c c c}\n\\toprule\nDomain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\n\\midrule\nC4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\n\\midrule\narXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \\cmark \\\\\n &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\n\\midrule\nWikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \\xmark \\\\\n & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \\xmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \\xmark \\\\\n & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \\xmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Code Domain Results}\n\\label{sec:code_domain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\n\\label{tab:code_domain_qwen}\n\\begin{tabular}{l c c c}\n\\toprule\nPair & AUC & 95\\% CI & JSD \\\\\n\\midrule\n0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\\\\n1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\\\\n2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\\\\n3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\\\\n4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\\\\n\\midrule\n\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\\% CIs. Qwen2.5-1.5B yields $\\Kempirical{=}2$; Pythia-1.4B yields borderline $\\Kempirical{=}1$ (1v2 CI upper $= 0.603 > \\theta$). Additional models pending completion.}\n\\label{tab:code_crossmodel_kstar}\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen2.5-1.5B} & \\multicolumn{2}{c}{Pythia-1.4B} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n & AUC & 95\\% CI & AUC & 95\\% CI \\\\\n\\midrule\n0v1 & .9388 & [.929,\\,.949] & \\textbf{.9592} & [.956,\\,.963] \\\\\n1v2 & \\textbf{.7382} & [.709,\\,.767]\\rlap{$^*$} & .5983 & [.593,\\,.603] \\\\\n2v3 & .5300 & [.514,\\,.546] & .5215 & --- \\\\\n3v4 & .5022 & --- & .5152 & --- \\\\\n4v5 & .5219 & --- & .5046 & --- \\\\\n\\midrule\n$K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ AUC $\\geq \\theta = 0.60$.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}\n\\label{sec:borderline_analysis}\n\nTo understand why Mistral-7B yields $\\Kempirical{=}1$ while other C4 models yield $\\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).\n\nMistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\\ 2.90--3.02 for other models), the scorer model therefore already finds Mistral's output highly predictable.\nThis compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\\bar{|d|} = 0.112$; Table~\\ref{tab:cohens_d_full}), and no single feature exceeds 13\\% of total classifier importance.\nThe borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.\n\nGreedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\\ = normalized LightGBM gain importance (\\%). $\\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\\Delta\\text{surp}_{1\\to2}$: change in mean surprisal from depth 1 to depth 2.}\n\\label{tab:borderline_features}\n\\begin{tabular}{@{}llc lcc@{}}\n\\toprule\nCategory & Model & AUC & Top-3 Features (Imp.\\%) & $\\bar{|d|}$ & $\\Delta\\text{surp}_{1\\to2}$ \\\\\n\\midrule\nStrong & Pythia-greedy & 0.884 & hapax\\_ratio (47), surp\\_mean (11), low\\_freq\\_ratio (8) & 0.365 & $-$0.160 \\\\\nStrong & Pythia-nuc09 & 0.677 & surp\\_std (20), freq\\_entropy (11), surp\\_d1\\_std (8) & 0.170 & $-$0.196 \\\\\nStrong & Qwen-1.5B-base & 0.626 & surp\\_std (13), freq\\_entropy (10), surp\\_mean (9) & 0.125 & $-$0.159 \\\\\n\\midrule\nBorderline & Pythia-$T{=}1.2$ & 0.617 & surp\\_std (15), freq\\_entropy (10), surp\\_kurt (8) & 0.112 & $-$0.059 \\\\\nBorderline & LLaMA-3.1-8B & 0.612 & surp\\_std (12), surp\\_d1\\_std (10), freq\\_entropy (9) & 0.137 & $-$0.215 \\\\\n\\midrule\nBelow $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[h]\n\\centering\n\\scriptsize\n\\caption{Cohen's $d$ (depth-1 vs.\\ depth-2) for all 15 features across six C4 models. \\textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\\_ratio, low\\_freq\\_ratio); under sampling, surprisal variability features (surp\\_std, surp\\_d1\\_std, surp\\_d2\\_std) carry the dominant signal.}\n\\label{tab:cohens_d_full}\n\\begin{tabular}{@{}lrrrrrr@{}}\n\\toprule\nFeature & \\rotatebox{60}{Pythia-greedy} & \\rotatebox{60}{Pythia-nuc09} & \\rotatebox{60}{Qwen-1.5B-base} & \\rotatebox{60}{Pythia-$T{=}1.2$} & \\rotatebox{60}{LLaMA-3.1-8B} & \\rotatebox{60}{Mistral-7B} \\\\\n\\midrule\nsurp\\_mean & \\textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\\\\nsurp\\_std & $-$0.301 & \\textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\\\\nsurp\\_skew & \\textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\\\\nsurp\\_kurt & \\textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\\\\nsurp\\_d1\\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \\textbf{$+$0.080} & $+$0.026 \\\\\nsurp\\_d1\\_std & $-$0.318 & \\textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\\\\nsurp\\_d1\\_skew & \\textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\\\\nsurp\\_d2\\_mean & $+$0.004 & $+$0.001 & \\textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\\\\nsurp\\_d2\\_std & $-$0.312 & \\textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\\\\nttr & \\textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\\\\nhapax\\_ratio & \\textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\\\\nself\\_bleu & $-$0.056 & $+$0.031 & \\textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\\\\nfreq\\_kurtosis & $+$0.071 & \\textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\\\\nfreq\\_entropy & \\textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\\\\nlow\\_freq\\_ratio & \\textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\\\\n\\midrule\n$\\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
    "structuredPatch": [
      {
        "oldStart": 38,
        "oldLines": 6,
        "newStart": 38,
        "newLines": 7,
        "lines": [
          " Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.",
          " The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).",
          " This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.",
          "+The extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.",
          " Extrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models, suggesting $\\Kempirical{=}7$ is near the ceiling.",
          " Prompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).",
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

### Assistant

_source line 39_

All 7 edits applied. Diff summary:

**Task A: 6 -ing phrase fixes**

| # | File | Before | After |
|---|------|--------|-------|
| 1 | `introduction.tex:8` | `...identically, **discarding** the generational depth dimension.` | `...identically and ignores the generational depth dimension.` |
| 2 | `introduction.tex:21` | `...across generations, **motivating** a finite discrimination boundary $K^*$.` | `...across generations; a finite discrimination boundary $K^*$ follows from this monotonic loss.` |
| 3 | `discussion.tex:35` | `...), **producing** a consistent ordering that correlates with...` | `...); the resulting ordering correlates with...` |
| 4 | `discussion.tex:37` | `...), **paralleling** its narrower surprisal dynamic range...` | `...), consistent with its narrower surprisal dynamic range...` |
| 5 | `discussion.tex:38` | `...on arXiv, **reinforcing** the domain-governed interpretation` | `...on arXiv, which reinforces the domain-governed interpretation` |
| 6 | `main.tex:77` | `...($0.5979$), **indicating** the boundary weakens...` | `...($0.5979$); the boundary weakens...` |

**Task B: Citation added**

`appendix_extended.tex:41` (new line between LoRA robustness sentence and "Extrapolating yields..."):
```
The extended discriminability under retraining aligns with theoretical analyses of
iterative retraining instability on synthetic data~\cite{bertrand2024stability,
gerstgrasser2024model}, where each retraining cycle amplifies distributional
artifacts beyond the text-intrinsic degradation observed in prompt-chains.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "uuid": "e3fb41cd-2b95-4a6e-9dc5-81e68f9d9965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uc9JBZAMcVjesUKZdUMuqz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 57787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 472
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

_source line 40_

All 7 edits applied. Diff summary:

**Task A: 6 -ing phrase fixes**

| # | File | Before | After |
|---|------|--------|-------|
| 1 | `introduction.tex:8` | `...identically, **discarding** the generational depth dimension.` | `...identically and ignores the generational depth dimension.` |
| 2 | `introduction.tex:21` | `...across generations, **motivating** a finite discrimination boundary $K^*$.` | `...across generations; a finite discrimination boundary $K^*$ follows from this monotonic loss.` |
| 3 | `discussion.tex:35` | `...), **producing** a consistent ordering that correlates with...` | `...); the resulting ordering correlates with...` |
| 4 | `discussion.tex:37` | `...), **paralleling** its narrower surprisal dynamic range...` | `...), consistent with its narrower surprisal dynamic range...` |
| 5 | `discussion.tex:38` | `...on arXiv, **reinforcing** the domain-governed interpretation` | `...on arXiv, which reinforces the domain-governed interpretation` |
| 6 | `main.tex:77` | `...($0.5979$), **indicating** the boundary weakens...` | `...($0.5979$); the boundary weakens...` |

**Task B: Citation added**

`appendix_extended.tex:41` (new line between LoRA robustness sentence and "Extrapolating yields..."):
```
The extended discriminability under retraining aligns with theoretical analyses of
iterative retraining instability on synthetic data~\cite{bertrand2024stability,
gerstgrasser2024model}, where each retraining cycle amplifies distributional
artifacts beyond the text-intrinsic degradation observed in prompt-chains.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 466542,
  "duration_api_ms": 466911,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "4a9bc0e7-d7fb-418c-b68d-f7912d4a11b8",
  "total_cost_usd": 0.5591425,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 48818,
    "cache_read_input_tokens": 257516,
    "output_tokens": 4954,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48818,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 453,
        "cache_read_input_tokens": 57787,
        "cache_creation_input_tokens": 472,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 472
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1302,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001382,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 4954,
      "cacheReadInputTokens": 257516,
      "cacheCreationInputTokens": 48818,
      "webSearchRequests": 0,
      "costUSD": 0.5577605,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f6c82e8f-5262-4715-a6d2-6369c9a37932"
}
```

</details>

---
