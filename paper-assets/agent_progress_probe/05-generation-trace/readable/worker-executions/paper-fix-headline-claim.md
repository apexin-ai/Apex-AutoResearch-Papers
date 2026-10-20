# paper fix headline claim

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_fix-headline-claim_20260515T043347.log`
- **Structured JSON:** [`9a6dd35a33ab9e2dd0fb.json`](../../sessions/9a/9a6dd35a33ab9e2dd0fb.json)

## Before a recorded user message

24 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
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
  "uuid": "7293dffe-83dd-43af-aae9-f906345883f2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778836800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c921da34-a71c-4317-bad4-8a7081cc0020",
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the relevant files first to understand the current content before making edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "5bb7781f-3522-469a-8f4a-f4824e0c7925",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 5_

先读取所有需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "1334ca36-06f4-4ddb-bdbf-e84be352fa1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01GVZq5xiA9wuDsHM4ABMZ63`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "e82fe347-4f8f-4551-a139-701c957467b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 7 · 2026-05-15T04:34:04.586Z_

<details><summary>↩ Tool result · `toolu_01GVZq5xiA9wuDsHM4ABMZ63`</summary>

```text
1	% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	LLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges.
3	No systematic study has compared detection approaches across deployment scenarios or investigated what signals carry stagnation information.
4	
5	We propose a weak supervision methodology for agent stagnation monitoring: three labeling functions aggregated by majority vote produce silver labels over 205K+ windows from two coding agents (SWE-Agent and OpenHands) on SWE-bench.
6	Against these labels, we compare 30 structural features, a GRU-based neural probe, and LLM-as-judge baselines across zero-data and fine-tuned regimes.
7	
8	We find a deployment-regime trade-off.
9	In zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp (in-domain structural 0.995 vs.\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).
10	With target-agent fine-tuning, the probe catches up and surpasses structural features (0.976 vs.\ 0.967), demonstrating that the structural advantage is specific to the zero-data regime.
11	Structural features are also data-efficient, exceeding 0.987 F1 at 10\% training data.
12	
13	Labeling functions exhibit agent-specific temporal dynamics: command repetition leads stagnation by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.
14	Label version bias---not LF noise---was the dominant cross-coding-agent transfer bottleneck; fixing it improved 5\% fine-tuning F1 from 0.570 to 0.850.
15	Five label models (three temporal, two generative) all fail to improve over majority vote; the bottleneck is LF quantity, not aggregation sophistication.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "c70d7e12-3397-4548-b177-116c0342f1b1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex",
      "content": "% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\nLLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges.\nNo systematic study has compared detection approaches across deployment scenarios or investigated what signals carry stagnation information.\n\nWe propose a weak supervision methodology for agent stagnation monitoring: three labeling functions aggregated by majority vote produce silver labels over 205K+ windows from two coding agents (SWE-Agent and OpenHands) on SWE-bench.\nAgainst these labels, we compare 30 structural features, a GRU-based neural probe, and LLM-as-judge baselines across zero-data and fine-tuned regimes.\n\nWe find a deployment-regime trade-off.\nIn zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp (in-domain structural 0.995 vs.\\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).\nWith target-agent fine-tuning, the probe catches up and surpasses structural features (0.976 vs.\\ 0.967), demonstrating that the structural advantage is specific to the zero-data regime.\nStructural features are also data-efficient, exceeding 0.987 F1 at 10\\% training data.\n\nLabeling functions exhibit agent-specific temporal dynamics: command repetition leads stagnation by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.\nLabel version bias---not LF noise---was the dominant cross-coding-agent transfer bottleneck; fixing it improved 5\\% fine-tuning F1 from 0.570 to 0.850.\nFive label models (three temporal, two generative) all fail to improve over majority vote; the bottleneck is LF quantity, not aggregation sophistication.\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_012VN7izGPWyDpUQW5BFajEV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "345e6472-7ba5-4f96-b83f-3aa8df60122e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 9 · 2026-05-15T04:34:05.043Z_

<details><summary>↩ Tool result · `toolu_012VN7izGPWyDpUQW5BFajEV`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\% and quality drops of 75.5\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 20.9\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.
13	Second, \emph{step-level scoring} via process reward models \citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \citep{chen2025monitoring}.
14	A sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.
15	Third, \emph{LLM self-evaluation} \citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \$11.66 per test set, well below lightweight feature-based alternatives.
16	More fundamentally, none of these approaches asks the prior question: \emph{what signals actually carry stagnation information?}
17	No systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.
18	
19	We address this question through a systematic empirical study (Figure~\ref{fig:pipeline}).
20	Using a weak supervision framework \citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\% stagnation).
21	Three labeling functions provide complementary noisy votes: command repetition ($\lambda_1$) targets repetitive behavior, file diff delta ($\lambda_2$) targets output productivity, and outcome backpropagation ($\lambda_3$) propagates task-level outcomes backward through the trajectory.
22	Majority vote aggregation produces window-level binary labels with confidence scores.
23	Our window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.
24	Against these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.
25	
26	Our study yields three principal findings.
27	
28	\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}
29	Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \citep{cho2014gru} zero-shot by 36.9\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 19.6\,pp.
30	However, with 100\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.
31	We note that in-domain evaluation uses silver labels (\S\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\S\ref{sec:gold_set}) provide non-circular validation.
32	The structural advantage is encoder-agnostic: three embedding backbones \citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.
33	The in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.
34	A feature overlap ablation (\S\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full model by 1.0\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.
35	This finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.
36	
37	\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}
38	Labeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.
39	A label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\% to 21.4\%---improves 5\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.
40	Prevalence-matched ablation shows that $\lambda_1$'s core value is coverage ($-29.4$\,pp when removed, $p \approx 0$), not label precision: it fires on only 5.39\% of OH windows with precision 97.91\% (FP rate 2.3\%).
41	
42	\textbf{Finding 3: No label model improves over majority vote.}
43	Five label models---three temporal (TWV, HMM \citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.
44	TWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
45	The bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.
46	
47	Our contributions are:
48	\begin{enumerate}
49	    \item \textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.
50	    \item \textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\%$\to$21.4\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.
51	    \item \textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.
52	    \item \textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp on silver labels (no GPU, ${<}$5\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.
53	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "ebb1ab48-6726-4f3e-abeb-ce3198ff5c91",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\\% and quality drops of 75.5\\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.\nCrucially, the dominant failure pattern is not simple repetition but what we term \\emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nThis ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.\nWe observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \\citep{yang2024sweagent} and OpenHands \\citep{wang2025openhands}---on SWE-bench tasks \\citep{jimenez2024swebench}, 28.5\\% and 20.9\\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.\n\nExisting approaches address aspects of this problem but fall short in three ways.\nFirst, \\emph{repetition detectors} such as cycle detection \\citep{george2025cycledetection} and SpecRA \\citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\nSecond, \\emph{step-level scoring} via process reward models \\citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \\citep{chen2025monitoring}.\nA sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.\nThird, \\emph{LLM self-evaluation} \\citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \\$11.66 per test set, well below lightweight feature-based alternatives.\nMore fundamentally, none of these approaches asks the prior question: \\emph{what signals actually carry stagnation information?}\nNo systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.\n\nWe address this question through a systematic empirical study (Figure~\\ref{fig:pipeline}).\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\\% stagnation).\nThree labeling functions provide complementary noisy votes: command repetition ($\\lambda_1$) targets repetitive behavior, file diff delta ($\\lambda_2$) targets output productivity, and outcome backpropagation ($\\lambda_3$) propagates task-level outcomes backward through the trajectory.\nMajority vote aggregation produces window-level binary labels with confidence scores.\nOur window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \\emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.\nAgainst these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.\n\nOur study yields three principal findings.\n\n\\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}\nThirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \\citep{cho2014gru} zero-shot by 36.9\\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 19.6\\,pp.\nHowever, with 100\\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.\nWe note that in-domain evaluation uses silver labels (\\S\\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\\S\\ref{sec:gold_set}) provide non-circular validation.\nThe structural advantage is encoder-agnostic: three embedding backbones \\citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.\nThe in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.\nA feature overlap ablation (\\S\\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full model by 1.0\\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.\nThis finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\n\\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}\nLabeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.\nA label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\\% to 21.4\\%---improves 5\\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.\nPrevalence-matched ablation shows that $\\lambda_1$'s core value is coverage ($-29.4$\\,pp when removed, $p \\approx 0$), not label precision: it fires on only 5.39\\% of OH windows with precision 97.91\\% (FP rate 2.3\\%).\n\n\\textbf{Finding 3: No label model improves over majority vote.}\nFive label models---three temporal (TWV, HMM \\citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.\nTWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.\n    \\item \\textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\\%$\\to$21.4\\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.\n    \\item \\textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.\n    \\item \\textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp on silver labels (no GPU, ${<}$5\\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.\n\\end{enumerate}",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01CoTL1tvsjXXPXvK9VvxiqX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "de75ddb4-3360-41e4-b9b1-c54a96a55974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 11 · 2026-05-15T04:34:05.518Z_

<details><summary>↩ Tool result · `toolu_01CoTL1tvsjXXPXvK9VvxiqX`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We organize results around three questions:
5	(1)~which method best detects stagnation across deployment scenarios? (\S\ref{sec:main_results}--\S\ref{sec:robustness});
6	(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\S\ref{sec:lf_temporal}--\S\ref{sec:cmd_rep_ablation});
7	(3)~can temporal structure in LFs improve labels? (\S\ref{sec:temporal_label_models}).
8	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
9	
10	\paragraph{Circular evaluation caveat.}
11	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
12	Consequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
13	The cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
14	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
15	
16	%-------------------------------------------------------------------
17	\subsection{Experimental Setup}
18	\label{sec:setup}
19	
20	\paragraph{Datasets.}
21	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
22	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
23	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\%.
24	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
25	Train/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\%), ensuring no windows from the same task appear across splits.
26	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\begin{tabular}{llrrc}
32	\toprule
33	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
34	\midrule
35	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
36	OpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\
37	\bottomrule
38	\end{tabular}
39	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
40	\label{tab:dataset_stats}
41	\end{table}
42	
43	\paragraph{Detection methods.}
44	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
45	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
46	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
47	(4)~\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\$11.66 API cost for the SWE test set).
48	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
49	
50	\paragraph{Metrics.}
51	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
52	
53	%-------------------------------------------------------------------
54	\subsection{Main Results}
55	\label{sec:main_results}
56	
57	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-coding-agent transfer to OpenHands.
58	
59	\begin{table*}[t]
60	\centering
61	\small
62	\begin{tabular}{l ccc cc}
63	\toprule
64	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
65	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
66	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
67	\midrule
68	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
69	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9918} \\
70	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
71	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\
72	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\
73	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
74	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
75	Cosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\
76	\bottomrule
77	\end{tabular}
78	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\geq}$2 subset ($N{=}43{,}376$). The structural conf${\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Probe fine-tuned macro-F1 confirmed on conf${\geq}$2 via paired bootstrap with GB ($p{<}0.001$); all-windows value from the same model. Best in \textbf{bold}, second-best \underline{underlined}.}
79	\label{tab:main_results}
80	\end{table*}
81	
82	In-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\,pp.
83	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
84	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
85	The zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\$11.66 per test set).
86	Extended evaluation with chain-of-thought and few-shot prompting (Appendix~\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 19.6\,pp below structural in-domain performance (0.995).
87	CoT alone adds only 0.1\,pp over zero-shot; the key gain comes from few-shot examples ($+$8.9\,pp), with CoT providing a complementary further $+$4.8\,pp when combined.
88	
89	%-------------------------------------------------------------------
90	\subsection{Cross-Agent Transfer}
91	\label{sec:cross_agent}
92	
93	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
94	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows.
95	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
96	Both structural models exceed 0.99 macro-F1 on conf${\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.
97	
98	The probe's zero-shot transfer (0.598) lags structural GB by 36.9\,pp---cosine similarity collapses further to 0.447---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\,pp (\S\ref{sec:cmd_rep_ablation}).
99	The asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\,pp on all windows).
100	The practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.
101	
102	\paragraph{Multi-seed stability.}
103	Structural RF: $0.995{\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\pm}0.002$.
104	The probe shows higher variance: $0.919{\pm}0.011$, though all seeds exceed 0.90.
105	
106	%-------------------------------------------------------------------
107	\subsection{Robustness Analysis}
108	\label{sec:robustness}
109	
110	\paragraph{Encoder ablation.}
111	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\ 0.906 for Qwen3).
112	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
113	We use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\ 0.906), confirming encoder-agnostic findings.
114	
115	\paragraph{Architecture ablation.}
116	Replacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\ 0.933 for GRU ($+$0.18\,pp, not significant under paired bootstrap $p{=}0.82$).
117	The two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.
118	
119	\paragraph{Window size.}
120	$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
121	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
122	The 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.
123	Details in Appendix Table~\ref{tab:window_ablation}.
124	
125	\paragraph{Data scaling.}
126	Figure~\ref{fig:data_scaling} compares data efficiency across methods.
127	Structural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\% training data, fully saturating by 50\%.
128	The probe scales monotonically from 0.805 (10\%) to 0.906 (100\%) but has not plateaued---a 10.1\,pp drop that is roughly 20$\times$ the structural degradation (${\sim}$0.4--0.8\,pp).
129	This data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
134	\caption{Macro-F1 vs.\ training data fraction. Structural classifiers (RF, GB) saturate by 50\% data; the probe scales monotonically but remains 9\,pp below at 100\%.}
135	\label{fig:data_scaling}
136	\end{figure}
137	
138	%-------------------------------------------------------------------
139	\subsection{Labeling Function Temporal Dynamics}
140	\label{sec:lf_temporal}
141	
142	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
143	
144	\begin{table}[t]
145	\centering
146	\small
147	\begin{tabular}{lrrrr}
148	\toprule
149	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
150	\midrule
151	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
152	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
153	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
154	\bottomrule
155	\end{tabular}
156	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
157	\label{tab:lf_temporal}
158	\end{table}
159	
160	The three LFs occupy distinct temporal niches.
161	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
162	File diff is near-concurrent ($-1.20$ steps).
163	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
164	
165	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
166	
167	\paragraph{Cross-agent reversal.}
168	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
169	Under corrected OH labels (\S\ref{sec:cmd_rep_ablation}), cmd\_rep fires on only 5.4\% of OH windows with 97.9\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.
170	
171	\begin{figure}[t]
172	\centering
173	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
174	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
175	\label{fig:lf_temporal}
176	\end{figure}
177	
178	%-------------------------------------------------------------------
179	\subsection{Label Quality and cmd\_rep Coverage}
180	\label{sec:cmd_rep_ablation}
181	
182	A label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.
183	After correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\% to 21.4\%, with 21,898 window labels flipping.
184	This section quantifies how label quality and cmd\_rep coverage jointly affect probe transfer.
185	
186	\paragraph{Label correction impact on probe transfer.}
187	With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).
188	The improvement is most dramatic at low data fractions: 5\% fine-tuning reaches 0.850, exceeding the old 50\% result (0.69) by 16.0\,pp.
189	The probe converges rapidly: at 50\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\ref{tab:cross_agent_cmdrep}).
190	Label quality, not model capacity, was the transfer bottleneck.
191	
192	\paragraph{Prevalence-matched ablation.}
193	To isolate cmd\_rep's contribution, we compare 3-LF and 2-LF (no cmd\_rep) models on the same test set with matched class prevalence.
194	
195	\begin{table}[t]
196	\centering
197	\small
198	\begin{tabular}{lccc}
199	\toprule
200	\textbf{LF Config} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} \\
201	\midrule
202	3-LF (w/ cmd\_rep) & \textbf{0.9763} & 0.9600 & 0.9930 \\
203	2-LF (no cmd\_rep) & 0.6822 & 0.4810 & 0.8840 \\
204	\midrule
205	$\Delta$ & $-29.4$\,pp & $-47.9$\,pp & $-10.9$\,pp \\
206	\bottomrule
207	\end{tabular}
208	\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\%). Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$).}
209	\label{tab:cmd_rep_ablation}
210	\end{table}
211	
212	Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\,pp F1\textsubscript{stag}).
213	
214	\paragraph{Coverage, not label quality, explains the gap.}
215	The 29.4\,pp drop is not caused by cmd\_rep improving label accuracy.
216	After correction, cmd\_rep fires on only 5.39\% of OH windows (down from the previously reported 92.2\% under corrupted embeddings) with 97.91\% precision---a high-precision, low-recall signal.
217	On the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\% of labels: cmd\_rep does not change any label where the other two LFs already vote.
218	Its contribution is purely \emph{coverage}: including cmd\_rep expands the training set from ${\sim}$4K to ${\sim}$43K windows (a ${\sim}$10$\times$ increase).
219	The 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.
220	
221	\paragraph{Implications for weak supervision.}
222	These results reframe how labeling functions contribute to weak supervision pipelines.
223	A high-precision, low-recall LF like cmd\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.
224	In prevalence-matched evaluation, this data reduction manifests as a 29.4\,pp F1 drop.
225	The core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.
226	
227	%-------------------------------------------------------------------
228	\subsection{Temporal Label Models}
229	\label{sec:temporal_label_models}
230	
231	We investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).
232	Table~\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\ models (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal}).
233	
234	\begin{table}[t]
235	\centering
236	\small
237	\begin{tabular}{lcccc}
238	\toprule
239	\textbf{Method} & \textbf{MV Agr.} & \textbf{Conf${\geq}$2 F1} & \textbf{$\Delta$ vs MV} & \textbf{Probe F1$^\ddagger$} \\
240	\midrule
241	MV (baseline) & 1.000 & 0.8946$^\ast$ & --- & 0.8468 \\
242	\midrule
243	\multicolumn{5}{l}{\emph{Temporal}} \\
244	TWV ($\sigma{=}2$) & 0.885 & \textbf{0.9003} & $+$0.6\,pp & 0.8211 \\
245	Lag-HMM & 0.820 & 0.8936 & $-$0.1\,pp & --- \\
246	HMM & 0.685 & 0.7502 & $-$14.4\,pp & 0.6564 \\
247	\midrule
248	\multicolumn{5}{l}{\emph{Generative (i.i.d.)}} \\
249	FlyingSquid & 0.820 & 0.7820 & $-$11.3\,pp & --- \\
250	Snorkel MeTaL & 0.423 & 0.2580 & $-$63.6\,pp & --- \\
251	\bottomrule
252	\end{tabular}
253	\caption{Label model comparison. Conf${\geq}$2 F1: each model's labels evaluated against MV labels on conf${\geq}$2 windows. $^\ast$MV conf${\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}
254	\label{tab:temporal_models}
255	\end{table}
256	
257	\paragraph{Temporal models.}
258	TWV achieves the highest conf${\geq}$2 F1 (0.900, $+$0.6\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\ 0.847 for MV-trained ($-$2.57\,pp).
259	TWV flips 14.1\% of conf${=}$1 labels, introducing noise that hurts probe training.
260	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal; $\sigma{=}1$ drops to 0.811 and $\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.
261	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), degrading conf${\geq}$2 F1 by 14.4\,pp and downstream performance to 0.656.
262	Lag-HMM closely tracks MV ($-$0.1\,pp) despite explicitly modeling temporal offsets.
263	
264	\paragraph{Generative (i.i.d.) models.}
265	FlyingSquid \citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\,pp below MV.
266	On the full dataset, agreement with MV is 82\%; all divergent labels flip progress$\to$stagnation, introducing systematic stagnation bias.
267	Snorkel MeTaL \citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\,pp), with only 42.3\% MV agreement.
268	Both models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.
269	
270	\paragraph{Root cause: insufficient inter-LF conflict.}
271	These results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.
272	Three binary LFs produce at most $2^3{=}8$ voting patterns; conf${\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.
273	The bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.
274	In the current 3-LF, low-conflict regime (conf${\geq}$2 agreement rate 95.1\%), temporal alignment gains are offset by noise introduction.
275	With 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.
276	
277	%-------------------------------------------------------------------
278	\subsection{Gold Set Validation}
279	\label{sec:gold_set}
280	We construct a stratified gold set of 650 windows for non-circular evaluation.
281	Windows are sampled along two axes: \emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \S\ref{sec:error_analysis}).
282	
283	\paragraph{Annotation protocol.}
284	Two annotators independently label each window as stagnation or progress using an operational definition: \emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.
285	Annotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\lambda_3$.
286	Disagreements are resolved by a third annotator.
287	Gold validation results are pending; in the interim, cross-coding-agent transfer (\S\ref{sec:cross_agent}) and the feature overlap ablation (\S\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "6924e817-afba-4214-afad-501b24efb117",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe organize results around three questions:\n(1)~which method best detects stagnation across deployment scenarios? (\\S\\ref{sec:main_results}--\\S\\ref{sec:robustness});\n(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\\S\\ref{sec:lf_temporal}--\\S\\ref{sec:cmd_rep_ablation});\n(3)~can temporal structure in LFs improve labels? (\\S\\ref{sec:temporal_label_models}).\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nTrain/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\\%), ensuring no windows from the same task appear across splits.\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-coding-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9918} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\\geq}$2 subset ($N{=}43{,}376$). The structural conf${\\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Probe fine-tuned macro-F1 confirmed on conf${\\geq}$2 via paired bootstrap with GB ($p{<}0.001$); all-windows value from the same model. Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\\$11.66 per test set).\nExtended evaluation with chain-of-thought and few-shot prompting (Appendix~\\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 19.6\\,pp below structural in-domain performance (0.995).\nCoT alone adds only 0.1\\,pp over zero-shot; the key gain comes from few-shot examples ($+$8.9\\,pp), with CoT providing a complementary further $+$4.8\\,pp when combined.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models exceed 0.99 macro-F1 on conf${\\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.\n\nThe probe's zero-shot transfer (0.598) lags structural GB by 36.9\\,pp---cosine similarity collapses further to 0.447---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\\,pp (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\\,pp on all windows).\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.995{\\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\\pm}0.002$.\nThe probe shows higher variance: $0.919{\\pm}0.011$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\\ 0.906 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\nWe use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\\ 0.906), confirming encoder-agnostic findings.\n\n\\paragraph{Architecture ablation.}\nReplacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\\ 0.933 for GRU ($+$0.18\\,pp, not significant under paired bootstrap $p{=}0.82$).\nThe two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nUnder corrected OH labels (\\S\\ref{sec:cmd_rep_ablation}), cmd\\_rep fires on only 5.4\\% of OH windows with 97.9\\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\\% to 21.4\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning reaches 0.850, exceeding the old 50\\% result (0.69) by 16.0\\,pp.\nThe probe converges rapidly: at 50\\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\\ref{tab:cross_agent_cmdrep}).\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.9600 & 0.9930 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.4810 & 0.8840 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \\citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\\ models (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{MV Agr.} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{$\\Delta$ vs MV} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 1.000 & 0.8946$^\\ast$ & --- & 0.8468 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Temporal}} \\\\\nTWV ($\\sigma{=}2$) & 0.885 & \\textbf{0.9003} & $+$0.6\\,pp & 0.8211 \\\\\nLag-HMM & 0.820 & 0.8936 & $-$0.1\\,pp & --- \\\\\nHMM & 0.685 & 0.7502 & $-$14.4\\,pp & 0.6564 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Generative (i.i.d.)}} \\\\\nFlyingSquid & 0.820 & 0.7820 & $-$11.3\\,pp & --- \\\\\nSnorkel MeTaL & 0.423 & 0.2580 & $-$63.6\\,pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Label model comparison. Conf${\\geq}$2 F1: each model's labels evaluated against MV labels on conf${\\geq}$2 windows. $^\\ast$MV conf${\\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}\n\\label{tab:temporal_models}\n\\end{table}\n\n\\paragraph{Temporal models.}\nTWV achieves the highest conf${\\geq}$2 F1 (0.900, $+$0.6\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\\ 0.847 for MV-trained ($-$2.57\\,pp).\nTWV flips 14.1\\% of conf${=}$1 labels, introducing noise that hurts probe training.\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal; $\\sigma{=}1$ drops to 0.811 and $\\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.\nHMM overpredicts stagnation (29,176 vs.\\ 25,633 progress windows), degrading conf${\\geq}$2 F1 by 14.4\\,pp and downstream performance to 0.656.\nLag-HMM closely tracks MV ($-$0.1\\,pp) despite explicitly modeling temporal offsets.\n\n\\paragraph{Generative (i.i.d.) models.}\nFlyingSquid \\citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\\,pp below MV.\nOn the full dataset, agreement with MV is 82\\%; all divergent labels flip progress$\\to$stagnation, introducing systematic stagnation bias.\nSnorkel MeTaL \\citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\\,pp), with only 42.3\\% MV agreement.\nBoth models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.\n\n\\paragraph{Root cause: insufficient inter-LF conflict.}\nThese results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.\nThree binary LFs produce at most $2^3{=}8$ voting patterns; conf${\\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.\nThe bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.\nIn the current 3-LF, low-conflict regime (conf${\\geq}$2 agreement rate 95.1\\%), temporal alignment gains are offset by noise introduction.\nWith 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\nWe construct a stratified gold set of 650 windows for non-circular evaluation.\nWindows are sampled along two axes: \\emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \\emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \\S\\ref{sec:error_analysis}).\n\n\\paragraph{Annotation protocol.}\nTwo annotators independently label each window as stagnation or progress using an operational definition: \\emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.\nAnnotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \\emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\\lambda_3$.\nDisagreements are resolved by a third annotator.\nGold validation results are pending; in the interim, cross-coding-agent transfer (\\S\\ref{sec:cross_agent}) and the feature overlap ablation (\\S\\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.",
      "numLines": 287,
      "startLine": 1,
      "totalLines": 287
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_015CBjcMJBayPCbPnB4sCU9C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "1d629f8a-940a-4abc-9800-e27ef07840ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 13 · 2026-05-15T04:34:05.985Z_

<details><summary>↩ Tool result · `toolu_015CBjcMJBayPCbPnB4sCU9C`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.
5	Three findings emerge.
6	
7	First, a deployment-regime trade-off governs method selection.
8	In zero-data cross-coding-agent transfer (SWE-Agent $\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp (in-domain structural 0.995 vs.\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).
9	With target-agent fine-tuning the probe surpasses structural features (0.976 vs.\ 0.967), demonstrating that the structural advantage is specific to zero-data deployment.
10	A feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1, exceeding the full 30-feature model (+1.0\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.
11	
12	Second, labeling functions exhibit agent-specific temporal dynamics.
13	Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.
14	A label quality audit reveals cmd\_rep is a high-precision detector (97.91\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\times$ (43K$\to$4K) and costs $-$29.4\,pp (p$\approx$0).
15	Label version bias---not LF noise---was the dominant transfer bottleneck.
16	
17	Third, no label model improves over majority vote.
18	Five label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
19	The bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.
20	
21	Agent monitoring should therefore prioritize lightweight structural features ({<}5\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.
22	All reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.
23	
24	Future work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.
25	
26	\paragraph{Reproducibility.}
27	Code, silver labels, and trained models will be released upon acceptance.
28	All agent trajectories are derived from publicly available SWE-bench runs \citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "aad5de41-c849-44e5-bda4-deb4814de969",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.\nThree findings emerge.\n\nFirst, a deployment-regime trade-off governs method selection.\nIn zero-data cross-coding-agent transfer (SWE-Agent $\\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp (in-domain structural 0.995 vs.\\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).\nWith target-agent fine-tuning the probe surpasses structural features (0.976 vs.\\ 0.967), demonstrating that the structural advantage is specific to zero-data deployment.\nA feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1, exceeding the full 30-feature model (+1.0\\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.\n\nSecond, labeling functions exhibit agent-specific temporal dynamics.\nCommand repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.\nA label quality audit reveals cmd\\_rep is a high-precision detector (97.91\\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\\times$ (43K$\\to$4K) and costs $-$29.4\\,pp (p$\\approx$0).\nLabel version bias---not LF noise---was the dominant transfer bottleneck.\n\nThird, no label model improves over majority vote.\nFive label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.\n\nAgent monitoring should therefore prioritize lightweight structural features ({<}5\\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.\nAll reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.\n\nFuture work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.\n\n\\paragraph{Reproducibility.}\nCode, silver labels, and trained models will be released upon acceptance.\nAll agent trajectories are derived from publicly available SWE-bench runs \\citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Kop5ZB4DfWbkQ6CRPTTgib`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "a353d808-711e-4ac6-aebc-e4de96a23747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxvHTYquWYbLQBXfyNTBm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13012
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

_source line 15 · 2026-05-15T04:34:06.224Z_

<details><summary>↩ Tool result · `toolu_01Kop5ZB4DfWbkQ6CRPTTgib`</summary>

```text
1	\section{Supplementary Results}
2	\label{sec:appendix}
3	
4	%-------------------------------------------------------------------
5	\subsection{Encoder Ablation}
6	\label{sec:app_encoder}
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Encoder} & \textbf{Dim} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Best Ep.} \\
14	\midrule
15	Qwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\
16	E5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\
17	BGE-M3 & 1024 & \textbf{0.9413} & \textbf{0.9147} & \textbf{0.9679} & 5 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Encoder ablation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\,pp over Qwen3), but the gap between encoders (0.5\,pp) is small relative to the structural--probe gap (8.96\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}
21	\label{tab:encoder_ablation}
22	\end{table}
23	
24	%-------------------------------------------------------------------
25	\subsection{Window Size Ablation}
26	\label{sec:app_window}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\begin{tabular}{ccccc}
32	\toprule
33	\textbf{Window $k$} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{$\Delta$ vs.\ $k{=}5$} \\
34	\midrule
35	3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\,pp \\
36	\textbf{5} & \textbf{0.9309} & \textbf{0.8917} & \textbf{0.9701} & --- \\
37	7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\,pp \\
38	\bottomrule
39	\end{tabular}
40	\caption{Window size ablation on SWE-Agent conf${\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\textsubscript{stag} drops 11.3\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}
41	\label{tab:window_ablation}
42	\end{table}
43	
44	%-------------------------------------------------------------------
45	\subsection{Multi-Seed Stability}
46	\label{sec:app_multiseed}
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\begin{tabular}{lcccc}
52	\toprule
53	\textbf{Method} & \textbf{In-Domain F1} & \textbf{Seeds} & \textbf{Cross-Agent F1} & \textbf{Seeds} \\
54	\midrule
55	Structural RF & $0.9951 \pm 0.0000$ & 5 & --- & --- \\
56	Structural GB & --- & --- & $0.9678 \pm 0.0015$ & 5 \\
57	ProgressProbe (GRU) & $0.9185 \pm 0.0113$ & 5 & --- & --- \\
58	\bottomrule
59	\end{tabular}
60	\caption{Multi-seed stability (mean $\pm$ std). In-domain: SWE-Agent conf${\geq}$2; cross-coding-agent: SWE-Agent $\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}
61	\label{tab:multiseed}
62	\end{table}
63	
64	%-------------------------------------------------------------------
65	\subsection{Cross-Agent Label Quality and Few-Shot Transfer}
66	\label{sec:app_cmdrep}
67	
68	Table~\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \S\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.
69	
70	\begin{table}[h]
71	\centering
72	\small
73	\begin{tabular}{lc}
74	\toprule
75	\textbf{OH Data Fraction} & \textbf{Probe Macro-F1} \\
76	\midrule
77	0\% (zero-shot) & 0.598 \\
78	5\% & 0.850 \\
79	10\% & 0.918 \\
80	20\% & 0.948 \\
81	50\% & 0.968 \\
82	100\% & 0.976 \\
83	\bottomrule
84	\end{tabular}
85	\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\% jump ($+$25.2\,pp) and rapid convergence toward structural GB (0.992 on conf${\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\% fine-tuning reached only 0.570.}
86	\label{tab:cross_agent_cmdrep}
87	\end{table}
88	
89	The probe reaches 0.948 macro-F1 at 20\% OH data---within 5\,pp of structural GB on conf${\geq}$2 windows (0.992)---and at 50\% (0.968) closes to within 2.5\,pp of structural GB on conf${\geq}$2 (0.992).
90	This rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\% fine-tuning reached only 0.751.
91	The improvement is driven entirely by label quality: the model architecture and training procedure are identical.
92	
93	Under the prevalence-matched ablation (\S\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\% of overlapping windows, confirming that cmd\_rep's contribution is coverage (expanding conf${\geq}$2 training data from ${\sim}$4K to ${\sim}$43K windows) rather than label refinement.
94	The $-29.4$\,pp drop upon removing cmd\_rep (McNemar $\chi^2{=}1{,}551$, $p{\approx}0$) is thus attributable to data volume collapse, not label noise.
95	
96	%-------------------------------------------------------------------
97	\subsection{Structural Feature Definitions}
98	\label{sec:app_features}
99	
100	Table~\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.
101	A feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\S\ref{sec:feature_overlap}).
102	
103	\begin{table*}[h]
104	\centering
105	\small
106	\begin{tabular}{rlll}
107	\toprule
108	\textbf{\#} & \textbf{Feature} & \textbf{Category} & \textbf{LF Overlap} \\
109	\midrule
110	1  & num\_steps             & Trajectory stats    & --- \\
111	2  & num\_actions           & Trajectory stats    & --- \\
112	3  & num\_observations      & Trajectory stats    & --- \\
113	4  & action\_ratio          & Trajectory stats    & --- \\
114	5  & mean\_text\_len        & Text statistics     & --- \\
115	6  & std\_text\_len         & Text statistics     & --- \\
116	7  & max\_text\_len         & Text statistics     & --- \\
117	8  & min\_text\_len         & Text statistics     & --- \\
118	9  & mean\_action\_len      & Text statistics     & --- \\
119	10 & mean\_obs\_len         & Text statistics     & --- \\
120	11 & text\_len\_trend       & Text statistics     & --- \\
121	12 & num\_commands          & Command stats       & --- \\
122	13 & mean\_cmd\_len         & Command stats       & --- \\
123	14 & max\_cmd\_len          & Command stats       & --- \\
124	15 & unique\_cmd\_ratio     & Repetition          & $\lambda_1$ \\
125	16 & max\_repeat\_ratio     & Repetition          & $\lambda_1$ \\
126	17 & num\_edit\_cmds        & File operations     & $\lambda_2$ \\
127	18 & num\_search\_cmds      & File operations     & $\lambda_2$ \\
128	19 & num\_nav\_cmds         & File operations     & --- \\
129	20 & num\_submit\_cmds      & File operations     & --- \\
130	21 & edit\_ratio            & File operations     & $\lambda_2$ \\
131	22 & search\_ratio          & File operations     & $\lambda_2$ \\
132	23 & avg\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
133	24 & max\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
134	25 & max\_consec\_similar   & Edit distance       & $\lambda_1$ \\
135	26 & num\_errors            & Output statistics   & --- \\
136	27 & num\_test\_outputs     & Output statistics   & --- \\
137	28 & num\_file\_displays    & Output statistics   & $\lambda_2$ \\
138	29 & num\_nonzero\_exits    & Output statistics   & --- \\
139	30 & is\_short\_trajectory  & Trajectory stats    & $\lambda_3$ \\
140	\bottomrule
141	\end{tabular}
142	\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\lambda_1$ (command repetition), $\lambda_2$ (file diff), $\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}
143	\label{tab:feature_defs}
144	\end{table*}
145	
146	%-------------------------------------------------------------------
147	\subsection{Instance Isolation}
148	\label{sec:app_instance_isolation}
149	
150	\begin{table}[h]
151	\centering
152	\small
153	\begin{tabular}{lccc}
154	\toprule
155	\textbf{Model} & \textbf{Full} & \textbf{Unseen-only} & \textbf{$\Delta$} \\
156	\midrule
157	GB all & 0.9674 & 0.9669 & $-$0.05\,pp \\
158	RF all & 0.9123 & 0.9121 & $-$0.01\,pp \\
159	GB conf${\geq}$2 & 0.9919 & 0.9917 & $-$0.02\,pp \\
160	RF conf${\geq}$2 & 0.9959 & 0.9962 & $+$0.03\,pp \\
161	\bottomrule
162	\end{tabular}
163	\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\% of OH). All $|\Delta| < 0.1$\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}
164	\label{tab:instance_isolation}
165	\end{table}
166	
167	%-------------------------------------------------------------------
168	\subsection{Extended LLM-as-Judge Evaluation}
169	\label{sec:llm_extended}
170	
171	Table~\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\ref{tab:main_results}) with chain-of-thought (CoT) prompting, few-shot examples, and an alternative model, all evaluated on the SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$).
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\begin{tabular}{llcccc}
177	\toprule
178	\textbf{Model} & \textbf{Setting} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Cost} \\
179	\midrule
180	Claude Sonnet 4.6 & zero-shot & 0.6625 & 0.6055 & 0.7195 & \$11.66 \\
181	Claude Sonnet 4.6 & CoT & 0.7499 & 0.6808 & 0.8189 & \$17.16 \\
182	Claude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \$36.08 \\
183	Claude Sonnet 4.6 & 5-shot-CoT & \textbf{0.7994} & \textbf{0.7306} & \textbf{0.8681} & \$40.56 \\
184	GPT-5.5$^\dagger$ & zero-shot & 0.7465 & 0.7110 & 0.7819 & \$11.62 \\
185	\bottomrule
186	\end{tabular}
187	\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All Claude rows use the same model; the performance gain comes from prompting strategy. CoT alone adds only 0.1\,pp over zero-shot, while 5-shot examples add 8.9\,pp; their combination (5-shot-CoT) yields a further 4.8\,pp, suggesting complementary mechanisms. $^\dagger$GPT-5.5: 22.4\% of responses (408/1,824) failed to parse; macro-F1 is computed over the 1,416 windows with valid outputs. The best LLM configuration (0.799 in-domain) trails structural in-domain performance (0.995) by 19.6\,pp. Total API cost across all configurations: \$117.}
188	\label{tab:llm_extended}
189	\label{tab:llm_extended}
190	\end{table}
191	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "2bc88221-c35d-4287-a8b9-2db5d26c2079",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex",
      "content": "\\section{Supplementary Results}\n\\label{sec:appendix}\n\n%-------------------------------------------------------------------\n\\subsection{Encoder Ablation}\n\\label{sec:app_encoder}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Dim} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Best Ep.} \\\\\n\\midrule\nQwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\\\\nE5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\\\\nBGE-M3 & 1024 & \\textbf{0.9413} & \\textbf{0.9147} & \\textbf{0.9679} & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Encoder ablation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\\,pp over Qwen3), but the gap between encoders (0.5\\,pp) is small relative to the structural--probe gap (8.96\\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}\n\\label{tab:encoder_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Window Size Ablation}\n\\label{sec:app_window}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Window $k$} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{$\\Delta$ vs.\\ $k{=}5$} \\\\\n\\midrule\n3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\\,pp \\\\\n\\textbf{5} & \\textbf{0.9309} & \\textbf{0.8917} & \\textbf{0.9701} & --- \\\\\n7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Window size ablation on SWE-Agent conf${\\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\\textsubscript{stag} drops 11.3\\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}\n\\label{tab:window_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Multi-Seed Stability}\n\\label{sec:app_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{In-Domain F1} & \\textbf{Seeds} & \\textbf{Cross-Agent F1} & \\textbf{Seeds} \\\\\n\\midrule\nStructural RF & $0.9951 \\pm 0.0000$ & 5 & --- & --- \\\\\nStructural GB & --- & --- & $0.9678 \\pm 0.0015$ & 5 \\\\\nProgressProbe (GRU) & $0.9185 \\pm 0.0113$ & 5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed stability (mean $\\pm$ std). In-domain: SWE-Agent conf${\\geq}$2; cross-coding-agent: SWE-Agent $\\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}\n\\label{tab:multiseed}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Label Quality and Few-Shot Transfer}\n\\label{sec:app_cmdrep}\n\nTable~\\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \\S\\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{OH Data Fraction} & \\textbf{Probe Macro-F1} \\\\\n\\midrule\n0\\% (zero-shot) & 0.598 \\\\\n5\\% & 0.850 \\\\\n10\\% & 0.918 \\\\\n20\\% & 0.948 \\\\\n50\\% & 0.968 \\\\\n100\\% & 0.976 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\\% jump ($+$25.2\\,pp) and rapid convergence toward structural GB (0.992 on conf${\\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\\% fine-tuning reached only 0.570.}\n\\label{tab:cross_agent_cmdrep}\n\\end{table}\n\nThe probe reaches 0.948 macro-F1 at 20\\% OH data---within 5\\,pp of structural GB on conf${\\geq}$2 windows (0.992)---and at 50\\% (0.968) closes to within 2.5\\,pp of structural GB on conf${\\geq}$2 (0.992).\nThis rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\\% fine-tuning reached only 0.751.\nThe improvement is driven entirely by label quality: the model architecture and training procedure are identical.\n\nUnder the prevalence-matched ablation (\\S\\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\\% of overlapping windows, confirming that cmd\\_rep's contribution is coverage (expanding conf${\\geq}$2 training data from ${\\sim}$4K to ${\\sim}$43K windows) rather than label refinement.\nThe $-29.4$\\,pp drop upon removing cmd\\_rep (McNemar $\\chi^2{=}1{,}551$, $p{\\approx}0$) is thus attributable to data volume collapse, not label noise.\n\n%-------------------------------------------------------------------\n\\subsection{Structural Feature Definitions}\n\\label{sec:app_features}\n\nTable~\\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.\nA feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\\S\\ref{sec:feature_overlap}).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\begin{tabular}{rlll}\n\\toprule\n\\textbf{\\#} & \\textbf{Feature} & \\textbf{Category} & \\textbf{LF Overlap} \\\\\n\\midrule\n1  & num\\_steps             & Trajectory stats    & --- \\\\\n2  & num\\_actions           & Trajectory stats    & --- \\\\\n3  & num\\_observations      & Trajectory stats    & --- \\\\\n4  & action\\_ratio          & Trajectory stats    & --- \\\\\n5  & mean\\_text\\_len        & Text statistics     & --- \\\\\n6  & std\\_text\\_len         & Text statistics     & --- \\\\\n7  & max\\_text\\_len         & Text statistics     & --- \\\\\n8  & min\\_text\\_len         & Text statistics     & --- \\\\\n9  & mean\\_action\\_len      & Text statistics     & --- \\\\\n10 & mean\\_obs\\_len         & Text statistics     & --- \\\\\n11 & text\\_len\\_trend       & Text statistics     & --- \\\\\n12 & num\\_commands          & Command stats       & --- \\\\\n13 & mean\\_cmd\\_len         & Command stats       & --- \\\\\n14 & max\\_cmd\\_len          & Command stats       & --- \\\\\n15 & unique\\_cmd\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n16 & max\\_repeat\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n17 & num\\_edit\\_cmds        & File operations     & $\\lambda_2$ \\\\\n18 & num\\_search\\_cmds      & File operations     & $\\lambda_2$ \\\\\n19 & num\\_nav\\_cmds         & File operations     & --- \\\\\n20 & num\\_submit\\_cmds      & File operations     & --- \\\\\n21 & edit\\_ratio            & File operations     & $\\lambda_2$ \\\\\n22 & search\\_ratio          & File operations     & $\\lambda_2$ \\\\\n23 & avg\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n24 & max\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n25 & max\\_consec\\_similar   & Edit distance       & $\\lambda_1$ \\\\\n26 & num\\_errors            & Output statistics   & --- \\\\\n27 & num\\_test\\_outputs     & Output statistics   & --- \\\\\n28 & num\\_file\\_displays    & Output statistics   & $\\lambda_2$ \\\\\n29 & num\\_nonzero\\_exits    & Output statistics   & --- \\\\\n30 & is\\_short\\_trajectory  & Trajectory stats    & $\\lambda_3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\\lambda_1$ (command repetition), $\\lambda_2$ (file diff), $\\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}\n\\label{tab:feature_defs}\n\\end{table*}\n\n%-------------------------------------------------------------------\n\\subsection{Instance Isolation}\n\\label{sec:app_instance_isolation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full} & \\textbf{Unseen-only} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGB all & 0.9674 & 0.9669 & $-$0.05\\,pp \\\\\nRF all & 0.9123 & 0.9121 & $-$0.01\\,pp \\\\\nGB conf${\\geq}$2 & 0.9919 & 0.9917 & $-$0.02\\,pp \\\\\nRF conf${\\geq}$2 & 0.9959 & 0.9962 & $+$0.03\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\\% of OH). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}\n\\label{tab:instance_isolation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Extended LLM-as-Judge Evaluation}\n\\label{sec:llm_extended}\n\nTable~\\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\\ref{tab:main_results}) with chain-of-thought (CoT) prompting, few-shot examples, and an alternative model, all evaluated on the SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Setting} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Cost} \\\\\n\\midrule\nClaude Sonnet 4.6 & zero-shot & 0.6625 & 0.6055 & 0.7195 & \\$11.66 \\\\\nClaude Sonnet 4.6 & CoT & 0.7499 & 0.6808 & 0.8189 & \\$17.16 \\\\\nClaude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \\$36.08 \\\\\nClaude Sonnet 4.6 & 5-shot-CoT & \\textbf{0.7994} & \\textbf{0.7306} & \\textbf{0.8681} & \\$40.56 \\\\\nGPT-5.5$^\\dagger$ & zero-shot & 0.7465 & 0.7110 & 0.7819 & \\$11.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All Claude rows use the same model; the performance gain comes from prompting strategy. CoT alone adds only 0.1\\,pp over zero-shot, while 5-shot examples add 8.9\\,pp; their combination (5-shot-CoT) yields a further 4.8\\,pp, suggesting complementary mechanisms. $^\\dagger$GPT-5.5: 22.4\\% of responses (408/1,824) failed to parse; macro-F1 is computed over the 1,416 windows with valid outputs. The best LLM configuration (0.799 in-domain) trails structural in-domain performance (0.995) by 19.6\\,pp. Total API cost across all configurations: \\$117.}\n\\label{tab:llm_extended}\n\\label{tab:llm_extended}\n\\end{table}\n",
      "numLines": 191,
      "startLine": 1,
      "totalLines": 191
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
Now I have all the files. Let me analyze what needs to be changed:

1. **abstract.tex line 9**: Currently says "19.6\,pp" — wait, it already says 19.6\,pp, not 21.6\,pp. Let me re-read the user's request.

The user says:
1. `abstract.tex` ~line 9 — "best LLM judge (in-domain) by 21.6 pp" → "16.8 pp"


2. `introduction.tex` ~line 29 — "best LLM judge (in-domain) by 21.6 pp" → "16.8 pp"
3. `introduction.tex` ~line 52 (contribution 4) — "best LLM judge (in-domain) by 21.6 pp" → "16.8 pp"
4. `experiments.tex` ~line 86 — "best LLM macro-F1 of 0.751" → "0.799 (few-shot chain-of-thought)"
5. `conclusion.tex` ~line 8 — "best LLM judge" (appears to be cut off in the request)

So I need to find and replace these specific metric values across multiple files. Let me start by locating each occurrence and making the necessary updates. I'm re-reading the user's clarification about the values—they're saying the old numbers were 0.751 for best LLM with a 21.6 pp gap, but the new numbers should be 0.799 (5-shot-CoT) with a 16.8 pp gap. Looking at the math, 0.995 - 0.799 = 19.6 pp for in-domain structural versus best LLM in-domain, but the user wants 16.8 pp, which would be the cross-domain comparison (0.967 - 0.799). So the text might need to specify which comparison it's actually making. The file already contains the updated values of 0.799 and 19.6pp, so I'm searching through the repository to confirm there are no remaining instances of the old numbers 0.751 and 21.6pp that still need to be fixed. Looking at the calculation, cross-agent structural (0.967) minus best LLM in-domain (0.799) gives 16.8pp, which is what the user expects. But the abstract currently states 19.6pp by comparing in-domain structural (0.995) against the best LLM instead. The issue is that the text claims to be discussing "zero-data cross-coding-agent transfer" but then uses the in-domain structural score in the comparison, which creates a mismatch between what's being claimed and what's actually being compared. The user wants me to update references from the old baseline (0.751, 21.6pp gap) to the correct values, but the files have already been partially updated to (0.799, 19.6pp). However, the user is asking for 16.8pp instead, which would come from using the cross-agent structural score (0.967) rather than the in-domain score (0.995) in the gap calculation. I need to find and update all instances of 19.6pp to 16.8pp throughout the files. I need to search for the actual values in the files to see what needs changing. The user wants 16.8pp as the correct gap (based on cross-agent 0.967 vs LLM 0.799), so I should look for any instances of 19.6pp that use the in-domain comparison and update those, plus fix the duplicate label issue in the appendix. I need to verify which gap is correct by checking the context. The abstract mentions "zero-data cross-coding-agent transfer," which suggests I should use the cross-agent structural score of 0.967 rather than the in-domain 0.995. That gives 16.8pp when compared to the best LLM's 0.799, not 19.6pp. So the user's instruction to change it to 16.8pp aligns with the proper framing—I'll search for and replace all instances of the gap value throughout the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "22ec43b0-2b9d-4971-8f9a-6452f0e91de1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLCJn2cEPTZdAEq468pxyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16771,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16771
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

_source line 17_

Let me grep for the values the user mentioned to confirm current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "cb9e43eb-89d7-4f7e-b7af-128bf1903c5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLCJn2cEPTZdAEq468pxyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16771,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16771
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

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01Kur2mdYQmAPReqgBaYkuc9`</summary>

```json
{
  "pattern": "21\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "0f2ebbf9-d854-4ccf-877e-6088866a33b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLCJn2cEPTZdAEq468pxyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16771,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16771
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

_source line 19 · 2026-05-15T04:35:09.354Z_

<details><summary>↩ Tool result · `toolu_01Kur2mdYQmAPReqgBaYkuc9`</summary>

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
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "aae03149-0ec1-4d43-b976-f66966a2e689",
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

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01WdDHhjGkpo3KwYM92g7qCX`</summary>

```json
{
  "pattern": "0\\.751",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "e591d8a5-37a1-43b5-a913-12559e0bee98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLCJn2cEPTZdAEq468pxyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16771,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16771
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

_source line 21 · 2026-05-15T04:35:10.300Z_

<details><summary>↩ Tool result · `toolu_01WdDHhjGkpo3KwYM92g7qCX`</summary>

```text
docs/paper/sections/experiments.tex:187:With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).
docs/paper/sections/appendix.tex:90:This rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\% fine-tuning reached only 0.751.
docs/paper/sections/appendix.tex:182:Claude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \$36.08 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "97af87ad-56b1-422f-9cef-309c0a00a5bc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:187:With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).\ndocs/paper/sections/appendix.tex:90:This rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\\% fine-tuning reached only 0.751.\ndocs/paper/sections/appendix.tex:182:Claude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \\$36.08 \\\\",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01UsDN7o8PG2FEJJrixWiHT1`</summary>

```json
{
  "pattern": "19\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "c4a3013a-dcd5-4f93-839d-a324935a8187",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLCJn2cEPTZdAEq468pxyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16771,
      "cache_read_input_tokens": 24853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16771
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

_source line 23 · 2026-05-15T04:35:10.712Z_

<details><summary>↩ Tool result · `toolu_01UsDN7o8PG2FEJJrixWiHT1`</summary>

```text
docs/paper/sections/experiments.tex:86:Extended evaluation with chain-of-thought and few-shot prompting (Appendix~\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 19.6\,pp below structural in-domain performance (0.995).
docs/paper/sections/conclusion.tex:8:In zero-data cross-coding-agent transfer (SWE-Agent $\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp (in-domain structural 0.995 vs.\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).
docs/paper/sections/abstract.tex:9:In zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp (in-domain structural 0.995 vs.\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).
docs/paper/sections/appendix.tex:187:[Omitted long matching line]
docs/paper/sections/introduction.tex:29:Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \citep{cho2014gru} zero-shot by 36.9\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 19.6\,pp.
docs/paper/sections/introduction.tex:52:    \item \textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\,pp and the best LLM judge (in-domain) by 19.6\,pp on silver labels (no GPU, ${<}$5\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "09a2f503-6ea5-4a79-8161-bae2bc246784",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/experiments.tex:86:Extended evaluation with chain-of-thought and few-shot prompting (Appendix~\\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 19.6\\,pp below structural in-domain performance (0.995).\ndocs/paper/sections/conclusion.tex:8:In zero-data cross-coding-agent transfer (SWE-Agent $\\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp (in-domain structural 0.995 vs.\\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).\ndocs/paper/sections/abstract.tex:9:In zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp (in-domain structural 0.995 vs.\\ best LLM 0.799; the cross-coding-agent score of 0.967 is non-circular).\ndocs/paper/sections/appendix.tex:187:[Omitted long matching line]\ndocs/paper/sections/introduction.tex:29:Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \\citep{cho2014gru} zero-shot by 36.9\\,pp (0.598 on OpenHands, near chance) and the best LLM judge (in-domain) by 19.6\\,pp.\ndocs/paper/sections/introduction.tex:52:    \\item \\textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\\,pp and the best LLM judge (in-domain) by 19.6\\,pp on silver labels (no GPU, ${<}$5\\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
OK so now I see the current state:

1. No "21.6" found anywhere — it's already been changed to "19.6"
2. "0.751" appears in:
   - experiments.tex:187 — "previously 0.7512 under corrupted labels" — this is referring to old corrupted label results, NOT the LLM baseline. Keep as-is.
   - appendix.tex:90 — "even 100\% fine-tuning reached only 0.751" — again, about old label regime probe performance. Keep as-is.
   - appendix.tex:182 — "0.7514" in the LLM table — this is the 5-shot LLM result (without CoT). Keep as-is since this is a specific data point in a table, not the "best LLM".

3. "19.6" appears across five files (experiments.tex, conclusion.tex, abstract.tex, appendix.tex, introduction.tex in two places), and the user wants to change the gap from 19.6pp to 16.8pp by adjusting the best LLM baseline from 0.799 to 0.827.

The current comparison uses in-domain structural (0.995) against best LLM in-domain (0.799), yielding 19.6pp. But looking at the abstract context about cross-agent transfer, it seems the user wants to compare cross-agent structural (0.967) against best LLM in-domain (0.799) instead, which gives 16.8pp — a more conservative claim that accounts for the transfer setting. I see the issue now — the probe gap correctly uses the cross-agent structural score (0.967 - 0.598 = 36.9pp), but the LLM comparison was inconsistently using the in-domain score instead. To fix this, I need to update the LLM gap to also use the cross-agent structural number, which gives 0.967 - 0.799 = 16.8pp rather than 19.6pp. I need to figure out how to handle the abstract.tex edit carefully. The user wants me to change the 19.6pp gap to 16.8pp, but I also need to decide whether to keep the in-domain structural score (0.995) or switch to the cross-coding-agent score (0.967) in the parenthetical explanation. Looking at the structure, it seems cleaner to use the cross-coding-agent comparison since that's what the 16.8pp gap actually represents, which would make the statement more internally consistent. I need to go through the fix list systematically. Items 1, 3, and 5 all involve changing 19.6 to 16.8 across different files, while item 4 is already corrected in the current version. Item 6 requires removing a duplicate label in the appendix.

For the gap value changes, I notice the parenthetical explanation "(in-domain structural 0.995 vs. best LLM 0.799)" actually produces 19.6pp, not 16.8pp, so I'll need to adjust what comparison is being shown to match the corrected gap value. However, the user's instruction appears to be cut off, so I should focus on just the items they explicitly listed. I need to update the parenthetical explanation to match the new gap number—changing the comparison from the in-domain structural score of 0.995 to the cross-coding-agent score of 0.967, since that's what produces the 16.8 percentage point difference. This keeps the numbers consistent throughout without making unnecessary changes beyond what the user asked for. I'm working through the metric updates across the paper—changing 19.6pp to 16.8pp where it compares the cross-coding-agent structural score (0.967) against the best LLM result (0.799). For the experiments.tex line 86, I need to decide whether to update just the percentage point gap or also clarify what structural performance we're comparing against, since the current text references in-domain (0.995) but the actual comparison should be to the cross-coding-agent score (0.967). I need to update that caption line too—it currently references the 19.6 percentage point difference, but I'm changing the comparison to use the cross-coding-agent baseline instead. Let me find where that specific number appears in the caption and swap it out for the corrected 16.8 pp figure. I'm reconsidering the scope of these edits—the user specified only the changes in their list, so I should be careful not to alter things beyond what they explicitly requested. The key updates are changing 19.6 to 16.8 in the LLM gap contexts and removing the duplicate label, but I need to think through whether updating the parenthetical reference values is necessary for consistency or if that goes beyond the stated scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cfb854eb-1424-4504-9900-31620e1fb4b2",
  "uuid": "2135243c-4042-411f-bb1a-64c799af7b4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MYkUdxtMak82AAakEeqXL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4307,
      "cache_read_input_tokens": 41624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4307
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
