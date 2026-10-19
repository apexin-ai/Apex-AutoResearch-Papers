# paper d055 table consistency fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_d055-table-consistency-fix_20260518T050839.log`
- **Structured JSON:** [`0bdbafa49dd58a499133.json`](../../sessions/0b/0bdbafa49dd58a499133.json)

## Before a recorded user message

45 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
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
  "uuid": "f76f3850-be3c-461b-a955-bf2b87c7bbec",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1779085800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "307b427b-6962-471e-a683-1093de754fc7",
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant tex files and searching for the old numbers that need to be updated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "10dded16-7e09-440c-8c83-ce44b9ab3bdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

I'll find all locations needing updates by searching for the old numbers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "22b952d2-d425-45c4-a9d4-ec2dece76411",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Edyp6XRQZZHAPZ2i5soNgr`</summary>

```json
{
  "pattern": "30\\.3|7\\.1pp|43\\.9|3\\.9pp|70\\.6|8\\.9\\\\pm|8\\.9±|0\\.7pp",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "9b6adbf8-c9d5-4953-9d36-2f50957b46b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

_source line 7 · 2026-05-18T05:08:54.846Z_

<details><summary>↩ Tool result · `toolu_01Edyp6XRQZZHAPZ2i5soNgr`</summary>

```text
paper/experiments.tex:49:& KL global (Ours) & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
paper/experiments.tex:166:& KL global & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "44943550-6902-4cd7-808e-bd7c50e2643c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:49:& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:166:& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_019SgPmVMoMwkLV64XrdKSDK`</summary>

```json
{
  "pattern": "8\\.96\\\\pm|8\\.96±|0\\.03",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "3f0d4463-9599-4a8d-935e-71b429e53961",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

_source line 9 · 2026-05-18T05:08:56.351Z_

<details><summary>↩ Tool result · `toolu_019SgPmVMoMwkLV64XrdKSDK`</summary>

```text
paper/related_work.tex:23:SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
paper/experiments.tex:28:At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
paper/experiments.tex:49:& KL global (Ours) & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
paper/experiments.tex:166:& KL global & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
paper/experiments.tex:199:At 50\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\% PPL improvement (12.08$\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "6bad8776-2edc-4353-b34b-bc9563df7117",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/related_work.tex:23:SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \\S\\ref{sec:experiments}).\npaper/experiments.tex:28:At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\npaper/experiments.tex:49:& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:166:& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:199:At 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Grep · `toolu_01XfG51vcWkfM3CcvMPJhUGH`</summary>

```json
{
  "pattern": "tab:main|tab:phase",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "51b1a0f5-4abe-4412-a321-73c664f81c3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

_source line 11 · 2026-05-18T05:08:57.443Z_

<details><summary>↩ Tool result · `toolu_01XfG51vcWkfM3CcvMPJhUGH`</summary>

```text
paper/experiments.tex:27:Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
paper/experiments.tex:39:\label{tab:main}
paper/experiments.tex:151:Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\% sparsity) would be needed to precisely locate region boundaries.
paper/experiments.tex:156:\label{tab:phase}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "575395d9-182b-4415-ad3e-06559568361d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:27:Table~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\npaper/experiments.tex:39:\\label{tab:main}\npaper/experiments.tex:151:Table~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\\% sparsity) would be needed to precisely locate region boundaries.\npaper/experiments.tex:156:\\label{tab:phase}",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01Si9yX2Ddo3BADDWfzmk7DV`</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "3c7bb50f-ec45-45d6-8207-eadd0730ca9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvxUZxSW73pPz18BxvuunU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14243,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14243
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

_source line 13 · 2026-05-18T05:08:57.899Z_

<details><summary>↩ Tool result · `toolu_01Si9yX2Ddo3BADDWfzmk7DV`</summary>

```text
paper/main.tex
paper/ethics.tex
paper/related_work.tex
paper/method.tex
paper/experiments.tex
paper/abstract.tex
paper/introduction.tex
paper/conclusion.tex
paper/limitations.tex
paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "2863f881-a1b8-4cc1-886b-272d0cecef57",
  "tool_use_result": {
    "filenames": [
      "paper/main.tex",
      "paper/ethics.tex",
      "paper/related_work.tex",
      "paper/method.tex",
      "paper/experiments.tex",
      "paper/abstract.tex",
      "paper/introduction.tex",
      "paper/conclusion.tex",
      "paper/limitations.tex",
      "paper/appendix.tex"
    ],
    "durationMs": 35,
    "numFiles": 10,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

Found the locations. Let me read the relevant sections of experiments.tex and check for references in abstract/introduction/conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "f672ce81-7ca4-44be-96be-0c0500f051fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g37Y7M4RVMWdg6qNowTi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01N5Yk8zE2h9zUoaaZdE1TGz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 25,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "e3c6da9f-be0c-4c6f-9639-e4b2724ba846",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g37Y7M4RVMWdg6qNowTi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 16 · 2026-05-18T05:09:03.081Z_

<details><summary>↩ Tool result · `toolu_01N5Yk8zE2h9zUoaaZdE1TGz`</summary>

```text
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
29	The advantage holds across additional downstream benchmarks (Appendix~\ref{app:downstream}).
30	Uniform allocation at 30\% provides stable downstream performance (MMLU 40.7$\pm$1.3\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%), with late-layer starvation (L31 retention 28.4\%) interacting with predictor initialization (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed
31	
32	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
33	The predictor generalizes to C4 validation at both 30\% (PPL 16.05) and 50\% (52.5\% over TEAL; Appendix~\ref{app:ood}).
34	However, all methods exhibit downstream collapse on MMLU (28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, both $\approx$ random, 3-seed) and GSM8K ($<$2.2\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global
35	
36	\begin{table}[t]
37	\centering
38	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\pm$ report 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); 50\% uniform PPL is 3-seed ($11.92 \pm 0.07$; Appendix~\ref{app:stability}); remaining entries use seed 42.}
39	\label{tab:main}
40	\resizebox{\columnwidth}{!}{
41	\begin{tabular}{llccccc}
42	\toprule
43	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
44	\midrule
45	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
46	\midrule
47	\multirow{3}{*}{30\%}
48	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
49	& KL global (Ours) & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
50	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.7$\pm$1.3} & 7.35 \\ % exp_id: kl30_3seed_uniform
51	\midrule
52	\multirow{4}{*}{50\%}
53	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
54	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
55	& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
56	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
57	\bottomrule
58	\end{tabular}}
59	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "72241ae5-a072-4ebd-837d-66f0347ec17d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\nThe advantage holds across additional downstream benchmarks (Appendix~\\ref{app:downstream}).\nUniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor generalizes to C4 validation at both 30\\% (PPL 16.05) and 50\\% (52.5\\% over TEAL; Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, both $\\approx$ random, 3-seed) and GSM8K ($<$2.2\\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\\pm$ report 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); 50\\% uniform PPL is 3-seed ($11.92 \\pm 0.07$; Appendix~\\ref{app:stability}); remaining entries use seed 42.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
      "numLines": 35,
      "startLine": 25,
      "totalLines": 256
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01XSkhfXHGCLGgLo6PsCLx7B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 145,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "d60a4a64-300f-4b08-9989-922fbc912554",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g37Y7M4RVMWdg6qNowTi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 18 · 2026-05-18T05:09:04.278Z_

<details><summary>↩ Tool result · `toolu_01XSkhfXHGCLGgLo6PsCLx7B`</summary>

```text
145	\end{table}
146	
147	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
148	In absolute terms, KL/Dense degradation is $1.47\times$ at 30\%, $1.93\times$ at 50\%, and $2.93\times$ at 70\%, compared to TEAL/Dense ratios of $1.79\times$, $3.81\times$, and $16.4\times$ respectively.
149	
150	\paragraph{Three Operating Regions.}
151	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\% sparsity) would be needed to precisely locate region boundaries.
152	
153	\begin{table}[t]
154	\centering
155	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. Entries with $\pm$ report 3-seed mean$\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}
156	\label{tab:phase}
157	\resizebox{\columnwidth}{!}{
158	\begin{tabular}{llccccc}
159	\toprule
160	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
161	\midrule
162	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
163	\midrule
164	\multirow{3}{*}{30\%}
165	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
166	& KL global & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
167	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.7$\pm$1.3} & 7.35 \\ % exp_id: kl30_3seed_uniform
168	\midrule
169	\multirow{2}{*}{40\%}
170	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
171	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
172	\midrule
173	\multirow{3}{*}{50\%}
174	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
175	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
176	& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
177	\bottomrule
178	\end{tabular}}
179	\end{table}
180	
181	The allocation preference is \emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):
182	
183	\noindent\textbf{Budget-surplus ($\leq$30\%).}
184	Uniform allocation provides $7.5\times$ smaller cross-seed MMLU standard deviation ($\sigma$: 1.3pp vs.\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\pm$9.5\% vs.\ 40.7$\pm$1.3\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\ref{app:lagrangian}). % exp_id: kl30_3seed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "fc0f8a85-576a-409f-a678-c29932d48852",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\nIn absolute terms, KL/Dense degradation is $1.47\\times$ at 30\\%, $1.93\\times$ at 50\\%, and $2.93\\times$ at 70\\%, compared to TEAL/Dense ratios of $1.79\\times$, $3.81\\times$, and $16.4\\times$ respectively.\n\n\\paragraph{Three Operating Regions.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\\% sparsity) would be needed to precisely locate region boundaries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. Entries with $\\pm$ report 3-seed mean$\\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation provides $7.5\\times$ smaller cross-seed MMLU standard deviation ($\\sigma$: 1.3pp vs.\\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\\pm$9.5\\% vs.\\ 40.7$\\pm$1.3\\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\\ref{app:lagrangian}). % exp_id: kl30_3seed",
      "numLines": 40,
      "startLine": 145,
      "totalLines": 256
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01KXiyHnb4yct6SmSPDTLDks`</summary>

```json
{
  "pattern": "8\\.9|MMLU|GSM|ARC|Winogrande|70\\.6|43\\.9|30\\.3|35\\.7|9\\.5",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content",
  "-n": true,
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "0ac369d5-59d2-47db-85bf-d1bc4ee6a1b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012g37Y7M4RVMWdg6qNowTi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1680,
      "cache_read_input_tokens": 26084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1680
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

_source line 20 · 2026-05-18T05:09:05.942Z_

<details><summary>↩ Tool result · `toolu_01KXiyHnb4yct6SmSPDTLDks`</summary>

```text
paper/experiments.tex:15:We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
paper/experiments.tex:28:At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
paper/experiments.tex:30:Uniform allocation at 30\% provides stable downstream performance (MMLU 40.7$\pm$1.3\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%), with late-layer starvation (L31 retention 28.4\%) interacting with predictor initialization (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed
paper/experiments.tex:34:However, all methods exhibit downstream collapse on MMLU (28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, both $\approx$ random, 3-seed) and GSM8K ($<$2.2\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global
paper/experiments.tex:43:Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
paper/experiments.tex:49:& KL global (Ours) & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
paper/experiments.tex:140:30\% & \textbf{8.96} & 10.97 & 18\% \\ % exp_id: kl30_3seed_global
paper/experiments.tex:160:Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
paper/experiments.tex:166:& KL global & 8.96$\pm$0.03 & \textbf{43.9$\pm$3.9} & \textbf{70.6$\pm$0.7} & 35.7$\pm$9.5 & \textbf{8.9$\pm$0.2} \\ % exp_id: kl30_3seed_global
paper/experiments.tex:184:Uniform allocation provides $7.5\times$ smaller cross-seed MMLU standard deviation ($\sigma$: 1.3pp vs.\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\pm$9.5\% vs.\ 40.7$\pm$1.3\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\ref{app:lagrangian}). % exp_id: kl30_3seed
paper/experiments.tex:187:The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
paper/experiments.tex:191:Global/uniform gap vanishes (MMLU 28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, $\sigma\leq$0.6pp; contrast 9.5pp at 30\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform
paper/experiments.tex:215:30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global
paper/experiments.tex:226:[Omitted long matching line]
paper/experiments.tex:235:Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
paper/experiments.tex:241:TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 \\ % exp_id: qwen14b_teal30_eval
paper/limitations.tex:3:Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
paper/limitations.tex:5:Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B (Qwen-2.5-14B), KL's PPL advantage persists but the MMLU gap relative to TEAL/BCE is not resolved by uniform allocation (+0.8pp vs.\ +8.1pp at 8B), suggesting that KL's output-preservation objective may underweight task-specific features at higher knowledge densities. Scaling to 70B remains untested.
paper/limitations.tex:8:At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
paper/ethics.tex:3:This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
paper/ethics.tex:32:\item[\textbf{C4.}] Yes. All evaluation uses established metrics (perplexity, accuracy) on standard benchmarks with standard few-shot protocols (ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 8-shot).
paper/abstract.tex:7:Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.
paper/appendix.tex:23:Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
paper/appendix.tex:148:For the recommended 30\% operating point, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at interpolated 28.5\% actual sparsity yields PPL$\approx$10.7 (vs.\ 10.97 at exact 30\%), a $<$0.3 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
paper/appendix.tex:194:Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
paper/appendix.tex:196:Under global allocation at 50\%, MMLU is equally stable: $28.1 \pm 0.2$\% (s42=27.89, s123=28.34, s456=27.94); the near-random performance is therefore capacity-limited rather than seed-sensitive ($\sigma$=0.2pp vs.\ 9.5pp at 30\% global). % exp_id: multi_seed_kl50_global
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "da64bda8-0283-4de9-b4a4-6d42b717fa42",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/experiments.tex:15:We report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\npaper/experiments.tex:28:At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\npaper/experiments.tex:30:Uniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed\npaper/experiments.tex:34:However, all methods exhibit downstream collapse on MMLU (28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, both $\\approx$ random, 3-seed) and GSM8K ($<$2.2\\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global\npaper/experiments.tex:43:Sparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\npaper/experiments.tex:49:& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:140:30\\% & \\textbf{8.96} & 10.97 & 18\\% \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:160:Sparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\npaper/experiments.tex:166:& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\npaper/experiments.tex:184:Uniform allocation provides $7.5\\times$ smaller cross-seed MMLU standard deviation ($\\sigma$: 1.3pp vs.\\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\\pm$9.5\\% vs.\\ 40.7$\\pm$1.3\\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\\ref{app:lagrangian}). % exp_id: kl30_3seed\npaper/experiments.tex:187:The preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\npaper/experiments.tex:191:Global/uniform gap vanishes (MMLU 28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, $\\sigma\\leq$0.6pp; contrast 9.5pp at 30\\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform\npaper/experiments.tex:215:30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global\npaper/experiments.tex:226:[Omitted long matching line]\npaper/experiments.tex:235:Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\npaper/experiments.tex:241:TEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 \\\\ % exp_id: qwen14b_teal30_eval\npaper/limitations.tex:3:Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\\% as the recommended operating point for downstream fidelity.\npaper/limitations.tex:5:Our recommended operating point (30\\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B (Qwen-2.5-14B), KL's PPL advantage persists but the MMLU gap relative to TEAL/BCE is not resolved by uniform allocation (+0.8pp vs.\\ +8.1pp at 8B), suggesting that KL's output-preservation objective may underweight task-specific features at higher knowledge densities. Scaling to 70B remains untested.\npaper/limitations.tex:8:At 30\\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.\npaper/ethics.tex:3:This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).\npaper/ethics.tex:32:\\item[\\textbf{C4.}] Yes. All evaluation uses established metrics (perplexity, accuracy) on standard benchmarks with standard few-shot protocols (ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 8-shot).\npaper/abstract.tex:7:Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though 14B reveals a scale-dependent MMLU gap not resolved by allocation strategy.\npaper/appendix.tex:23:Predictor + compensation & 50\\% & 129.71$\\pm$0.53 & 15{,}789 & +8.9\\% \\\\ % exp_id: latency_bench\npaper/appendix.tex:148:For the recommended 30\\% operating point, actual sparsity is $\\approx$28.5\\% (5\\% deviation). This does not affect conclusions: TEAL at interpolated 28.5\\% actual sparsity yields PPL$\\approx$10.7 (vs.\\ 10.97 at exact 30\\%), a $<$0.3 PPL difference negligible relative to the KL vs.\\ TEAL gap (8.96 vs.\\ 10.97).\npaper/appendix.tex:194:Downstream metrics are similarly stable: ARC-c $33.8 \\pm 1.2$\\%, WinoGrande $62.9 \\pm 0.1$\\%, MMLU $28.0 \\pm 0.6$\\%, GSM8K $2.2 \\pm 0.1$\\%.\npaper/appendix.tex:196:Under global allocation at 50\\%, MMLU is equally stable: $28.1 \\pm 0.2$\\% (s42=27.89, s123=28.34, s456=27.94); the near-random performance is therefore capacity-limited rather than seed-sensitive ($\\sigma$=0.2pp vs.\\ 9.5pp at 30\\% global). % exp_id: multi_seed_kl50_global",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me identify all the changes needed:

**Old data (currently in paper) for KL 30% global row:**
- PPL: 8.96±0.03
- ARC-C: 43.9±3.9
- WG: 70.6±0.7
- MMLU: 35.7±9.5 (already updated in a previous commit!)
- GSM8K: 8.9±0.2


**New data:**
- PPL: 8.96±0.02
- ARC-C: 43.8±3.6
- WG: 70.2±0.9
- MMLU: 35.7±9.5 (no change!)
- GSM8K: 8.0±0.7

So the MMLU value was already updated previously—the task mentioned changing it from 30.3±7.1 to 35.7±9.5, but it's already at 35.7±9.5 in the paper, which means that commit already went through.

The actual remaining updates I need to make are: PPL from 8.96±0.03 to 8.96±0.02, ARC-C from 43.9±3.9 to 43.8±3.6, WG from 70.6±0.7 to 70.2±0.9, and GSM8K from 8.9±0.2 to 8.0±0.7. I also need to check the inline text references—line 28 mentions PPL 8.96±0.03 and line 184 references a "7.5×" smaller standard deviation, but let me verify that calculation since 9.5/1.3 gives about 7.3×. on MMLU, which hasn't changed.

Wait, I need to check whether the task specifically asks for updating data or whether MMLU was already updated. Looking at the task again: the old data had MMLU 30.3±7.1 and new data has 35.7±9.5. From the commit history, MMLU was already updated, but other metrics still need work.

Let me map out what needs changing across the file. PPL standard deviation drops from 0.03 to 0.02 in a couple places, ARC-C goes from 43.9±3.9 to 43.8±3.6, and GSM8K changes from 70.6±0.7 to 70.2±0.9 while WG shifts from 8.9±0.2 to 8.0±0.7. Some entries like the single PPL value of 8.96 don't need updates, and the ratio calculation stays the same since MMLU's standard deviation hasn't changed. Checking whether the bold markings need to stay in place across the tables. For ARC-c, WG, and GSM8K, the updated values still outperform both the TEAL and uniform baselines, so the bold formatting remains correct throughout.

The PPL improvement calculation checks out at 18.3%, which rounds to the stated 18%, and I'm updating the uncertainty notation from ±0.03 to ±0.02. The speedup factor of 7.5× also holds up under recalculation, so no adjustments needed there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "f2f385bc-3db6-4b81-b9fb-ccd4861c2308",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnAHvqptbHPf7UpcZ47D1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 27764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

MMLU was already updated (35.7±9.5) in a prior commit. The remaining changes are: PPL std (0.03→0.02), ARC-C (43.9±3.9→43.8±3.6), WG (70.6±0.7→70.2±0.9), GSM8K (8.9±0.2→8.0±0.7). Making all edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "df0f077d-831f-4bc9-9acd-16a5ab8471d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnAHvqptbHPf7UpcZ47D1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 27764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

<details open><summary>🔧 Tool call — Edit · `toolu_0132JBidp31t8E76118iq4aj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "old_string": "At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed)",
  "new_string": "At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "2802a427-a64d-4d4a-a4c9-483d46401efd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnAHvqptbHPf7UpcZ47D1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 27764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 24 · 2026-05-18T05:09:37.103Z_

<details><summary>↩ Tool result · `toolu_0132JBidp31t8E76118iq4aj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "95f05d48-b928-4584-80b7-e3de54f2611a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "oldString": "At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed)",
    "newString": "At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed)",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $5 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\nThe advantage holds across additional downstream benchmarks (Appendix~\\ref{app:downstream}).\nUniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor generalizes to C4 validation at both 30\\% (PPL 16.05) and 50\\% (52.5\\% over TEAL; Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, both $\\approx$ random, 3-seed) and GSM8K ($<$2.2\\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\\pm$ report 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); 50\\% uniform PPL is 3-seed ($11.92 \\pm 0.07$; Appendix~\\ref{app:stability}); remaining entries use seed 42.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nTo test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\\times$ the KL step budget, approximately equal wall-clock time: $\\sim$46 min BCE vs.\\ $\\sim$45 min KL on RTX PRO 6000).\nThe BCE predictor achieves PPL 28.13$\\pm$0.20 (3-seed), still 2.39$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed\nThe difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL (28.13 vs.\\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42\nCoupled training correlates with better output preservation, but disentangling gradient coupling from oracle quality remains open (BCE uses magnitude oracles while KL optimizes output directly; an ablation using KL-derived masks as BCE targets would isolate the effect).\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nJSD (symmetric) + Gumbel & 12.54 & +0.75 \\\\ % exp_id: jsd_ablation_s42\nReverse KL + Gumbel & 12.80 & +1.01 \\\\ % exp_id: reverse_kl_ablation_s42\nForward KL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{3}{l}{\\textit{BCE-based variants}} \\\\\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\nBCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid with STE~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42\n\n\\paragraph{Divergence Direction.}\nForward KL (mode-covering) outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with the SNR analysis in \\S\\ref{sec:method:gradient}: complete teacher supervision is associated with better global allocation quality. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42\nThis contrasts with MiniLLM~\\cite{gu2024minillm} (reverse KL for generation); in mask prediction, mode-covering ensures no important neuron is omitted.\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\\% relative); see \\S\\ref{sec:spon} for decomposition.\\footnote{SPON analysis uses \\texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Loss Function Isolation.}\nBCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation\nThe loss effect ($\\Delta$PPL=26.23) is $6.6\\times$ the relaxation effect ($\\Delta$PPL=3.98).\n\n\\paragraph{BCE + Compensation.}\nFastForward-style compensation~\\cite{gautam2026fastforward} improves BCE from 27.97 to 25.44 (9.0\\%), still $2.16\\times$ worse than KL. % exp_id: bce_comp_staged_s42\n\n\\paragraph{Hyperparameter Robustness.}\nAppendix~\\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\\%), temperature ($<$1.8\\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}\n\\label{fig:sparsity_sweep}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.96} & 10.97 & 18\\% \\\\ % exp_id: kl30_3seed_global\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\nIn absolute terms, KL/Dense degradation is $1.47\\times$ at 30\\%, $1.93\\times$ at 50\\%, and $2.93\\times$ at 70\\%, compared to TEAL/Dense ratios of $1.79\\times$, $3.81\\times$, and $16.4\\times$ respectively.\n\n\\paragraph{Three Operating Regions.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\\% sparsity) would be needed to precisely locate region boundaries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. Entries with $\\pm$ report 3-seed mean$\\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation provides $7.5\\times$ smaller cross-seed MMLU standard deviation ($\\sigma$: 1.3pp vs.\\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\\pm$9.5\\% vs.\\ 40.7$\\pm$1.3\\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\\ref{app:lagrangian}). % exp_id: kl30_3seed\n\n\\noindent\\textbf{Budget-constrained ($\\sim$40\\%).}\nThe preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\nPPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.\n\n\\noindent\\textbf{Capacity-limited ($\\geq$50\\%).}\nGlobal/uniform gap vanishes (MMLU 28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, $\\sigma\\leq$0.6pp; contrast 9.5pp at 30\\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform\nLate-layer starvation persists across levels (L24--31 retention: 50.1/34.2/22.6\\% at 30/50/70\\% sparsity; Figure~\\ref{fig:retention}), consistent on both 7--8B models (\\S\\ref{sec:cross_arch}).\nUnder uniform allocation, 53\\% of the Dense$\\to$KL gap is predictor approximation vs.\\ 47\\% budget allocation (Appendix~\\ref{app:db_sensitivity}).\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nAt 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Cross-Architecture Validation.}\n\\label{sec:cross_arch}\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity; 4.63$\\times$ vs.\\ 5.59$\\times$ at 70\\%) and provides preliminary evidence of generality at the 7--8B scale.\n\n\\paragraph{Scale Generalization: Qwen-2.5-14B.}\n\\label{sec:14b}\nTable~\\ref{tab:14b} evaluates Qwen-2.5-14B~\\cite{qwen2024qwen25} at 30\\%: KL's PPL advantage generalizes ($1.47\\times$ dense) under both allocations, but MMLU falls below TEAL/BCE regardless (63.7/64.5 vs.\\ 71.8/66.3\\%), and uniform recovers only +0.8pp. Unlike 8B, the gap appears intrinsic to KL's output-preservation objective rather than allocation-induced. BCE with native allocation collapses to 6.4\\% sparsity (\\S\\ref{sec:method:gradient}); Table~\\ref{tab:14b} uses forced global top-$k$. % exp_id: qwen14b_kl30_s42, qwen14b_bce30_s42, qwen14b_bce30_s42_v2, qwen14b_teal30_eval, qwen14b_kl30_uniform, qwen14b_teal30_uniform\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% sparsity. \\textbf{Bold}: best sparse per column per group.}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{6}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.63} & 54.44 & \\textbf{72.45} & 64.49 & --- \\\\ % exp_id: qwen14b_kl30_uniform\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & --- \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\enlargethispage{3\\baselineskip}\n\\paragraph{Inference Efficiency.}\nThe pipeline adds 6.4\\% overhead while removing the compensation network ($-$2.7\\% latency, $-$67.2M params); the predictor internalizes most error-correction signal (Appendix~\\ref{app:latency}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 25,
        "oldLines": 7,
        "newStart": 25,
        "newLines": 7,
        "lines": [
          " \\subsection{Main Results}",
          " ",
          " Table~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).",
          "-At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.03 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global",
          "+At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global",
          " The advantage holds across additional downstream benchmarks (Appendix~\\ref{app:downstream}).",
          " Uniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed",
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ty6hiPxDVmWeJyRhY8dntw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "old_string": "& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform",
  "new_string": "& KL global (Ours) & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global\n& KL uniform"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "c83d3bcb-f337-42cd-a06a-926411ef1e5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnAHvqptbHPf7UpcZ47D1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 27764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 26 · 2026-05-18T05:09:39.957Z_

<details><summary>↩ Tool result · `toolu_01Ty6hiPxDVmWeJyRhY8dntw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "f8cd5dbf-6494-4daf-8e5f-c562fa14f148",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "oldString": "& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform",
    "newString": "& KL global (Ours) & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global\n& KL uniform",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $5 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\nThe advantage holds across additional downstream benchmarks (Appendix~\\ref{app:downstream}).\nUniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor generalizes to C4 validation at both 30\\% (PPL 16.05) and 50\\% (52.5\\% over TEAL; Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, both $\\approx$ random, 3-seed) and GSM8K ($<$2.2\\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\\pm$ report 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); 50\\% uniform PPL is 3-seed ($11.92 \\pm 0.07$; Appendix~\\ref{app:stability}); remaining entries use seed 42.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nTo test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\\times$ the KL step budget, approximately equal wall-clock time: $\\sim$46 min BCE vs.\\ $\\sim$45 min KL on RTX PRO 6000).\nThe BCE predictor achieves PPL 28.13$\\pm$0.20 (3-seed), still 2.39$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed\nThe difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL (28.13 vs.\\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42\nCoupled training correlates with better output preservation, but disentangling gradient coupling from oracle quality remains open (BCE uses magnitude oracles while KL optimizes output directly; an ablation using KL-derived masks as BCE targets would isolate the effect).\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nJSD (symmetric) + Gumbel & 12.54 & +0.75 \\\\ % exp_id: jsd_ablation_s42\nReverse KL + Gumbel & 12.80 & +1.01 \\\\ % exp_id: reverse_kl_ablation_s42\nForward KL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{3}{l}{\\textit{BCE-based variants}} \\\\\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\nBCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid with STE~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42\n\n\\paragraph{Divergence Direction.}\nForward KL (mode-covering) outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with the SNR analysis in \\S\\ref{sec:method:gradient}: complete teacher supervision is associated with better global allocation quality. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42\nThis contrasts with MiniLLM~\\cite{gu2024minillm} (reverse KL for generation); in mask prediction, mode-covering ensures no important neuron is omitted.\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\\% relative); see \\S\\ref{sec:spon} for decomposition.\\footnote{SPON analysis uses \\texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Loss Function Isolation.}\nBCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation\nThe loss effect ($\\Delta$PPL=26.23) is $6.6\\times$ the relaxation effect ($\\Delta$PPL=3.98).\n\n\\paragraph{BCE + Compensation.}\nFastForward-style compensation~\\cite{gautam2026fastforward} improves BCE from 27.97 to 25.44 (9.0\\%), still $2.16\\times$ worse than KL. % exp_id: bce_comp_staged_s42\n\n\\paragraph{Hyperparameter Robustness.}\nAppendix~\\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\\%), temperature ($<$1.8\\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}\n\\label{fig:sparsity_sweep}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.96} & 10.97 & 18\\% \\\\ % exp_id: kl30_3seed_global\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\nIn absolute terms, KL/Dense degradation is $1.47\\times$ at 30\\%, $1.93\\times$ at 50\\%, and $2.93\\times$ at 70\\%, compared to TEAL/Dense ratios of $1.79\\times$, $3.81\\times$, and $16.4\\times$ respectively.\n\n\\paragraph{Three Operating Regions.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\\% sparsity) would be needed to precisely locate region boundaries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. Entries with $\\pm$ report 3-seed mean$\\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation provides $7.5\\times$ smaller cross-seed MMLU standard deviation ($\\sigma$: 1.3pp vs.\\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\\pm$9.5\\% vs.\\ 40.7$\\pm$1.3\\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\\ref{app:lagrangian}). % exp_id: kl30_3seed\n\n\\noindent\\textbf{Budget-constrained ($\\sim$40\\%).}\nThe preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\nPPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.\n\n\\noindent\\textbf{Capacity-limited ($\\geq$50\\%).}\nGlobal/uniform gap vanishes (MMLU 28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, $\\sigma\\leq$0.6pp; contrast 9.5pp at 30\\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform\nLate-layer starvation persists across levels (L24--31 retention: 50.1/34.2/22.6\\% at 30/50/70\\% sparsity; Figure~\\ref{fig:retention}), consistent on both 7--8B models (\\S\\ref{sec:cross_arch}).\nUnder uniform allocation, 53\\% of the Dense$\\to$KL gap is predictor approximation vs.\\ 47\\% budget allocation (Appendix~\\ref{app:db_sensitivity}).\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nAt 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Cross-Architecture Validation.}\n\\label{sec:cross_arch}\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity; 4.63$\\times$ vs.\\ 5.59$\\times$ at 70\\%) and provides preliminary evidence of generality at the 7--8B scale.\n\n\\paragraph{Scale Generalization: Qwen-2.5-14B.}\n\\label{sec:14b}\nTable~\\ref{tab:14b} evaluates Qwen-2.5-14B~\\cite{qwen2024qwen25} at 30\\%: KL's PPL advantage generalizes ($1.47\\times$ dense) under both allocations, but MMLU falls below TEAL/BCE regardless (63.7/64.5 vs.\\ 71.8/66.3\\%), and uniform recovers only +0.8pp. Unlike 8B, the gap appears intrinsic to KL's output-preservation objective rather than allocation-induced. BCE with native allocation collapses to 6.4\\% sparsity (\\S\\ref{sec:method:gradient}); Table~\\ref{tab:14b} uses forced global top-$k$. % exp_id: qwen14b_kl30_s42, qwen14b_bce30_s42, qwen14b_bce30_s42_v2, qwen14b_teal30_eval, qwen14b_kl30_uniform, qwen14b_teal30_uniform\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% sparsity. \\textbf{Bold}: best sparse per column per group.}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{6}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.63} & 54.44 & \\textbf{72.45} & 64.49 & --- \\\\ % exp_id: qwen14b_kl30_uniform\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & --- \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\enlargethispage{3\\baselineskip}\n\\paragraph{Inference Efficiency.}\nThe pipeline adds 6.4\\% overhead while removing the compensation network ($-$2.7\\% latency, $-$67.2M params); the predictor internalizes most error-correction signal (Appendix~\\ref{app:latency}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " \\multirow{3}{*}{30\\%}",
          " & TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30",
          "-& KL global (Ours) & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global",
          "+& KL global (Ours) & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global",
          " & KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform",
          " \\midrule",
          " \\multirow{4}{*}{50\\%}"
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_0116T6pRa5yys9BxYJtFajmc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "old_string": "& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82}",
  "new_string": "& KL global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "166ef3c6-ea23-4244-b9e1-e0a811806496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnAHvqptbHPf7UpcZ47D1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5547,
      "cache_read_input_tokens": 27764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5547
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

_source line 28 · 2026-05-18T05:09:42.194Z_

<details><summary>↩ Tool result · `toolu_0116T6pRa5yys9BxYJtFajmc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "a08e5c2f-d736-453c-bf74-88218236e39e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
    "oldString": "& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82}",
    "newString": "& KL global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + GELU + Linear($128 \\to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\\cite{loshchilov2019adamw} with learning rate $1 \\times 10^{-3}$, weight decay $5 \\times 10^{-2}$, and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor} (DejaVu-style~\\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\\S\\ref{sec:scaling}).\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global\nThe advantage holds across additional downstream benchmarks (Appendix~\\ref{app:downstream}).\nUniform allocation at 30\\% provides stable downstream performance (MMLU 40.7$\\pm$1.3\\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\\pm$9.5\\%), with late-layer starvation (L31 retention 28.4\\%) interacting with predictor initialization (\\S\\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed\n\nAt 50\\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nThe predictor generalizes to C4 validation at both 30\\% (PPL 16.05) and 50\\% (52.5\\% over TEAL; Appendix~\\ref{app:ood}).\nHowever, all methods exhibit downstream collapse on MMLU (28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, both $\\approx$ random, 3-seed) and GSM8K ($<$2.2\\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\\pm$ report 3-seed mean$\\pm$std ($s \\in \\{42, 123, 456\\}$); 50\\% uniform PPL is 3-seed ($11.92 \\pm 0.07$; Appendix~\\ref{app:stability}); remaining entries use seed 42.}\n\\label{tab:main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 28.13$\\pm$0.20 & 27.6$\\pm$0.6 & 51.8$\\pm$0.6 & 26.1$\\pm$0.5 & 2.1$\\pm$0.2 \\\\ % exp_id: bce50_3seed\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\subsection{Extended Training Analysis}\n\\label{sec:isocompute}\n\nTo test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\\times$ the KL step budget, approximately equal wall-clock time: $\\sim$46 min BCE vs.\\ $\\sim$45 min KL on RTX PRO 6000).\nThe BCE predictor achieves PPL 28.13$\\pm$0.20 (3-seed), still 2.39$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed\nThe difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\\ 0.540) with 139\\% worse PPL (28.13 vs.\\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42\nCoupled training correlates with better output preservation, but disentangling gradient coupling from oracle quality remains open (BCE uses magnitude oracles while KL optimizes output directly; an ablation using KL-derived masks as BCE targets would isolate the effect).\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{KL-based variants}} \\\\\nForward KL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nJSD (symmetric) + Gumbel & 12.54 & +0.75 \\\\ % exp_id: jsd_ablation_s42\nReverse KL + Gumbel & 12.80 & +1.01 \\\\ % exp_id: reverse_kl_ablation_s42\nForward KL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\n\\midrule\n\\multicolumn{3}{l}{\\textit{BCE-based variants}} \\\\\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\nBCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\\\ % exp_id: bce_gumbel_lagrangian_isolation\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid with STE~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42\n\n\\paragraph{Divergence Direction.}\nForward KL (mode-covering) outperforms JSD (+6.4\\%) and reverse KL (+8.6\\%), consistent with the SNR analysis in \\S\\ref{sec:method:gradient}: complete teacher supervision is associated with better global allocation quality. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42\nThis contrasts with MiniLLM~\\cite{gu2024minillm} (reverse KL for generation); in mask prediction, mode-covering ensures no important neuron is omitted.\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\\% relative); see \\S\\ref{sec:spon} for decomposition.\\footnote{SPON analysis uses \\texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Loss Function Isolation.}\nBCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation\nThe loss effect ($\\Delta$PPL=26.23) is $6.6\\times$ the relaxation effect ($\\Delta$PPL=3.98).\n\n\\paragraph{BCE + Compensation.}\nFastForward-style compensation~\\cite{gautam2026fastforward} improves BCE from 27.97 to 25.44 (9.0\\%), still $2.16\\times$ worse than KL. % exp_id: bce_comp_staged_s42\n\n\\paragraph{Hyperparameter Robustness.}\nAppendix~\\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\\%), temperature ($<$1.8\\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep\n\n\n\\subsection{Sparsity Scaling and Regime Analysis}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig2_sparsity_sweep.pdf}\n\\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}\n\\label{fig:sparsity_sweep}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.96} & 10.97 & 18\\% \\\\ % exp_id: kl30_3seed_global\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage grows from 18\\% at 30\\% to 82\\% at 70\\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.\nIn absolute terms, KL/Dense degradation is $1.47\\times$ at 30\\%, $1.93\\times$ at 50\\%, and $2.93\\times$ at 70\\%, compared to TEAL/Dense ratios of $1.79\\times$, $3.81\\times$, and $16.4\\times$ respectively.\n\n\\paragraph{Three Operating Regions.}\nTable~\\ref{tab:phase} presents global vs.\\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\\% sparsity) would be needed to precisely locate region boundaries.\n\n\\begin{table}[t]\n\\centering\n\\caption{Allocation analysis: global (TEAL) vs.\\ uniform per-layer allocation across sparsity levels. Entries with $\\pm$ report 3-seed mean$\\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}\n\\label{tab:phase}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Allocation & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform\n\\midrule\n\\multirow{2}{*}{40\\%}\n& KL global & 10.12 & 40.96 & 65.35 & \\textbf{38.06} & \\textbf{5.00} \\\\ % exp_id: bench_kl40_global\n& KL uniform & \\textbf{8.36} & \\textbf{41.81} & \\textbf{67.17} & 30.68 & 3.94 \\\\ % exp_id: d030_kl40_uniform\n\\midrule\n\\multirow{3}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 28.1$\\pm$0.2 & 1.29 \\\\ % exp_id: multi_seed_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 28.0$\\pm$0.6 & \\textbf{2.12} \\\\ % exp_id: multi_seed_kl50_uniform\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe allocation preference is \\emph{non-monotonic}. We observe three qualitative behaviors at the sampled sparsity levels (7--8B scale):\n\n\\noindent\\textbf{Budget-surplus ($\\leq$30\\%).}\nUniform allocation provides $7.5\\times$ smaller cross-seed MMLU standard deviation ($\\sigma$: 1.3pp vs.\\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\\pm$9.5\\% vs.\\ 40.7$\\pm$1.3\\%, 3-seed). Global top-$k$ starves late layers (L31: 28.4\\%, std/mean$=$1.89), and this starvation interacts unpredictably with predictor initialization (Appendix~\\ref{app:lagrangian}). % exp_id: kl30_3seed\n\n\\noindent\\textbf{Budget-constrained ($\\sim$40\\%).}\nThe preference reverses: global achieves MMLU 38.06\\% vs.\\ uniform's 30.68\\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform\nPPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.\n\n\\noindent\\textbf{Capacity-limited ($\\geq$50\\%).}\nGlobal/uniform gap vanishes (MMLU 28.1$\\pm$0.2\\% vs.\\ 28.0$\\pm$0.6\\%, $\\sigma\\leq$0.6pp; contrast 9.5pp at 30\\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform\nLate-layer starvation persists across levels (L24--31 retention: 50.1/34.2/22.6\\% at 30/50/70\\% sparsity; Figure~\\ref{fig:retention}), consistent on both 7--8B models (\\S\\ref{sec:cross_arch}).\nUnder uniform allocation, 53\\% of the Dense$\\to$KL gap is predictor approximation vs.\\ 47\\% budget allocation (Appendix~\\ref{app:db_sensitivity}).\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nAt 50\\% sparsity, the predictor's hidden-state perturbation (L2=482.65) and SPON's additive correction (L2=76.2, cosine similarity 0.196) are weakly correlated ($R^2$=0.038); SPON yields only 2.4\\% PPL improvement (12.08$\\to$11.79); the KL predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42\n\n\\paragraph{Cross-Architecture Validation.}\n\\label{sec:cross_arch}\nTable~\\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture comparison (WikiText-2 PPL$\\downarrow$). Adv = TEAL\\,/\\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{l@{\\hspace{4pt}}cc@{\\hspace{3pt}}c@{\\hspace{6pt}}|@{\\hspace{6pt}}cc@{\\hspace{3pt}}c}\n\\toprule\n & \\multicolumn{3}{c}{Mistral-7B} & \\multicolumn{3}{c}{LLaMA-8B} \\\\\n & KL & TEAL & Adv & KL & TEAL & Adv \\\\\n\\midrule\n30\\% & \\textbf{6.77} & 8.38 & 1.24$\\times$ & \\textbf{8.96} & 10.97 & 1.22$\\times$ \\\\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global\n50\\% & \\textbf{8.65} & 18.31 & 2.12$\\times$ & \\textbf{11.79} & 23.31 & 1.98$\\times$ \\\\ % exp_id: kl_50_mistral, teal_50_mistral\n70\\% & \\textbf{13.33} & 61.72 & 4.63$\\times$ & \\textbf{17.91} & 100.11 & 5.59$\\times$ \\\\ % exp_id: kl_70_mistral, teal_70_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL advantage ratio is consistent across architectures (within 8\\% at $\\leq$50\\% sparsity; 4.63$\\times$ vs.\\ 5.59$\\times$ at 70\\%) and provides preliminary evidence of generality at the 7--8B scale.\n\n\\paragraph{Scale Generalization: Qwen-2.5-14B.}\n\\label{sec:14b}\nTable~\\ref{tab:14b} evaluates Qwen-2.5-14B~\\cite{qwen2024qwen25} at 30\\%: KL's PPL advantage generalizes ($1.47\\times$ dense) under both allocations, but MMLU falls below TEAL/BCE regardless (63.7/64.5 vs.\\ 71.8/66.3\\%), and uniform recovers only +0.8pp. Unlike 8B, the gap appears intrinsic to KL's output-preservation objective rather than allocation-induced. BCE with native allocation collapses to 6.4\\% sparsity (\\S\\ref{sec:method:gradient}); Table~\\ref{tab:14b} uses forced global top-$k$. % exp_id: qwen14b_kl30_s42, qwen14b_bce30_s42, qwen14b_bce30_s42_v2, qwen14b_teal30_eval, qwen14b_kl30_uniform, qwen14b_teal30_uniform\n\n\\begin{table}[t]\n\\centering\n\\caption{Qwen-2.5-14B at 30\\% sparsity. \\textbf{Bold}: best sparse per column per group.}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\nDense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Global top-$k$ allocation}} \\\\\nKL (Ours) & \\textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 \\\\ % exp_id: qwen14b_kl30_s42\nTEAL & 8.73 & 56.83 & \\textbf{72.69} & \\textbf{71.83} & 49.51 \\\\ % exp_id: qwen14b_teal30_eval\nBCE & 8.76 & \\textbf{57.59} & 72.61 & 71.67 & \\textbf{53.07} \\\\ % exp_id: qwen14b_bce30_s42_eval\n\\midrule\n\\multicolumn{6}{l}{\\emph{Uniform allocation}} \\\\\nKL (Ours) & \\textbf{7.63} & 54.44 & \\textbf{72.45} & 64.49 & --- \\\\ % exp_id: qwen14b_kl30_uniform\nTEAL & 8.01 & \\textbf{55.29} & 69.85 & \\textbf{66.34} & --- \\\\ % exp_id: qwen14b_teal30_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\enlargethispage{3\\baselineskip}\n\\paragraph{Inference Efficiency.}\nThe pipeline adds 6.4\\% overhead while removing the compensation network ($-$2.7\\% latency, $-$67.2M params); the predictor internalizes most error-correction signal (Appendix~\\ref{app:latency}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 163,
        "oldLines": 7,
        "newStart": 163,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " \\multirow{3}{*}{30\\%}",
          " & TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30",
          "-& KL global & 8.96$\\pm$0.03 & \\textbf{43.9$\\pm$3.9} & \\textbf{70.6$\\pm$0.7} & 35.7$\\pm$9.5 & \\textbf{8.9$\\pm$0.2} \\\\ % exp_id: kl30_3seed_global",
          "+& KL global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global",
          " & KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.7$\\pm$1.3} & 7.35 \\\\ % exp_id: kl30_3seed_uniform",
          " \\midrule",
          " \\multirow{2}{*}{40\\%}"
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

_source line 29_

Now let me check if the GSM8K change (8.9→8.0) affects any bold markings or inline text, and verify the "7.5×" ratio still holds. Let me also check for any other references to the old GSM8K value.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "3a41a08e-96b2-442e-959f-defb9c4dc120",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsWYkfWjFXaFvQj5uboybE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 33311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2923
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

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_01LAVL5bMRVAataJJoPmUS2g`</summary>

```json
{
  "pattern": "8\\.9\\\\pm0\\.2|8\\.9\\$\\\\pm\\$0\\.2",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "1d79df8b-81a1-49d1-a1bd-d8474f997c9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsWYkfWjFXaFvQj5uboybE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 33311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2923
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

_source line 31 · 2026-05-18T05:09:47.386Z_

<details><summary>↩ Tool result · `toolu_01LAVL5bMRVAataJJoPmUS2g`</summary>

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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "635eff63-af54-4b35-a56f-0009ff03c29d",
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

_source line 32_

<details open><summary>🔧 Tool call — Grep · `toolu_01MwVtHp84M9eoCnGshqmBKZ`</summary>

```json
{
  "pattern": "70\\.6|43\\.9|8\\.96.*0\\.03",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "a1a2a160-5458-43c2-8239-efc53bb64bdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsWYkfWjFXaFvQj5uboybE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2923,
      "cache_read_input_tokens": 33311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2923
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

_source line 33 · 2026-05-18T05:09:48.550Z_

<details><summary>↩ Tool result · `toolu_01MwVtHp84M9eoCnGshqmBKZ`</summary>

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
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "080cddec-4528-4953-b881-80cd20ff6bd6",
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

_source line 34_

All old values are gone. Now let me compile to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "54150a37-1930-464e-b0a4-557ed88e239e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuVoCPtpvZ8Nm6A3x5x391",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 36234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01P4JLYojRp6sjohkT8foTxF`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Compile LaTeX to verify no errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "61d35c8c-4b57-4194-84c0-920834232ed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuVoCPtpvZ8Nm6A3x5x391",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 36234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
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

_source line 36 · 2026-05-18T05:09:53.098Z_

<details><summary>↩ Tool result · `toolu_01P4JLYojRp6sjohkT8foTxF`</summary>

```text
hare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 391731 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "ebfebae8-8a44-47bc-80cc-1fcd16d7eaec",
  "tool_use_result": {
    "stdout": "hare/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (14 pages, 391731 bytes).\nTranscript written on main.log.",
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

_source line 37_

Compilation successful (14 pages, no errors). Let me verify the final state of the updated lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "00114a97-e0f2-4e31-944c-63d788c7100b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpybqtfuXtw7FVwZoynYfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 36688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_015cmiJB1L4bsgcgrkesUNiA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 28,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "130679ce-b61e-4922-9b72-cbe913d8a65c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpybqtfuXtw7FVwZoynYfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 36688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 39 · 2026-05-18T05:09:57.491Z_

<details><summary>↩ Tool result · `toolu_015cmiJB1L4bsgcgrkesUNiA`</summary>

```text
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "e10a2ebf-8b02-4b62-b6ab-f58543a71b48",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "At 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\\to$ 8.96, an 18\\% improvement). % exp_id: kl30_3seed_global",
      "numLines": 1,
      "startLine": 28,
      "totalLines": 256
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01DwwShmnS26r9AoxbEdTtbT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 49,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "33fdd555-6e79-49d0-bd84-ce203e8b3a68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpybqtfuXtw7FVwZoynYfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 36688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 41 · 2026-05-18T05:09:58.034Z_

<details><summary>↩ Tool result · `toolu_01DwwShmnS26r9AoxbEdTtbT`</summary>

```text
49	& KL global (Ours) & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "c30c4ab7-be02-4ee4-afc2-3c7fca367fa0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "& KL global (Ours) & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global",
      "numLines": 1,
      "startLine": 49,
      "totalLines": 256
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01XRg2NCg1cmtUMNaC76aMwW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 166,
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "edb7fc5e-1f1a-489b-9129-848108d45a08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpybqtfuXtw7FVwZoynYfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 36688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 43 · 2026-05-18T05:09:58.732Z_

<details><summary>↩ Tool result · `toolu_01XRg2NCg1cmtUMNaC76aMwW`</summary>

```text
166	& KL global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "8598aa38-1cc8-4201-af39-5ecea685c998",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "& KL global & 8.96$\\pm$0.02 & \\textbf{43.8$\\pm$3.6} & \\textbf{70.2$\\pm$0.9} & 35.7$\\pm$9.5 & \\textbf{8.0$\\pm$0.7} \\\\ % exp_id: kl30_3seed_global",
      "numLines": 1,
      "startLine": 166,
      "totalLines": 256
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

All updates applied and verified. Summary of changes in `experiments.tex`:

| Metric | Old | New |
|--------|-----|-----|
| PPL std | 0.03 | 0.02 |
| ARC-C | 43.9±3.9 | 43.8±3.6 |
| WG | 70.6±0.7 | 70.2±0.9 |
| GSM8K | 8.9±0.2 | 8.0±0.7 |
| MMLU | 35.7±9.5 | (unchanged, already correct) |

Updated 3 locations: inline text (line 28), Table 1 (line 49), Table 3 (line 166). Bold markings remain correct (KL global still best for ARC-C, WG, GSM8K at 30%). The "7.5×" MMLU stability ratio and "9.5pp" references are unchanged since MMLU data didn't change. Compilation passes cleanly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "uuid": "2aa7d5c4-2f65-4f0c-b4d8-a1beb5159b7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbKPFV6CmWjwmQj32u1ubL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 36973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

### Task result

_source line 45_

All updates applied and verified. Summary of changes in `experiments.tex`:

| Metric | Old | New |
|--------|-----|-----|
| PPL std | 0.03 | 0.02 |
| ARC-C | 43.9±3.9 | 43.8±3.6 |
| WG | 70.6±0.7 | 70.2±0.9 |
| GSM8K | 8.9±0.2 | 8.0±0.7 |
| MMLU | 35.7±9.5 | (unchanged, already correct) |

Updated 3 locations: inline text (line 28), Table 1 (line 49), Table 3 (line 166). Bold markings remain correct (KL global still best for ARC-C, WG, GSM8K at 30%). The "7.5×" MMLU stability ratio and "9.5pp" references are unchanged since MMLU data didn't change. Compilation passes cleanly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 75609,
  "duration_api_ms": 75445,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "6c909dcf-efc5-4e92-b7cd-6cbd45b16f76",
  "total_cost_usd": 0.38762475,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 25857,
    "cache_read_input_tokens": 208895,
    "output_tokens": 4771,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25857,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 252,
        "cache_read_input_tokens": 36973,
        "cache_creation_input_tokens": 725,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 725
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2161,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002251,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 4771,
      "cacheReadInputTokens": 208895,
      "cacheCreationInputTokens": 25857,
      "webSearchRequests": 0,
      "costUSD": 0.38537375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ab10284d-2764-4236-840a-eaa997e8fd76"
}
```

</details>

---
