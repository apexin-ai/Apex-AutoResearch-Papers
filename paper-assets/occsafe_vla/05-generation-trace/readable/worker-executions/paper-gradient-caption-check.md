# paper gradient caption check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_gradient_caption_check_20260525T112650.log`
- **Structured JSON:** [`0c94c396eccee87ed16c.json`](../../sessions/0c/0c94c396eccee87ed16c.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
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
  "uuid": "1b835fe1-0862-4afe-a1cd-8309083aaa89",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779722400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2d6fe478-6fd0-4ee0-b0c5-3481a98e179b",
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af"
}
```

---

### Assistant

_source line 4_

I'll search for the gradient analysis figure in the paper and the corresponding image file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "8358f25d-9bc4-468f-97c8-5633bcb9fb86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VddC7nRw5nBeHAN2PhkLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11420,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11420
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Grep · `toolu_013X76QZZYBdbFdNj4ovA5yC`</summary>

```json
{
  "pattern": "gradient|fig:gradient",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper",
  "output_mode": "content",
  "-n": true,
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "184d4ec2-a181-4754-91dc-938105cc4f99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VddC7nRw5nBeHAN2PhkLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11420,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11420
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 6 · 2026-05-25T11:27:04.679Z_

<details><summary>↩ Tool result · reported error · `toolu_013X76QZZYBdbFdNj4ovA5yC`</summary>

```text
&lt;tool_use_error>Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "68378203-2c55-461d-8502-819dcd6ed6f9",
  "tool_use_result": "Error: Path does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_019n9osccxMKpifr9Gaufszi`</summary>

```json
{
  "pattern": "*gradient_analysis*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "43ad3eba-2bf8-40df-a8c7-5f079536edeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VddC7nRw5nBeHAN2PhkLQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11420,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11420
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 8 · 2026-05-25T11:27:04.980Z_

<details><summary>↩ Tool result · `toolu_019n9osccxMKpifr9Gaufszi`</summary>

```text
artifacts/_project/report/gradient_analysis_report.md
artifacts/figures/gradient_analysis_combined.pdf
artifacts/_project/chart/gradient_analysis_combined.png
artifacts/figures/gradient_analysis_combined.png
artifacts/_project/data/same_seed_gradient_analysis.py
artifacts/same_seed_gradient_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "9e6fc72c-5283-4471-b16d-550b5330a304",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/gradient_analysis_report.md",
      "artifacts/figures/gradient_analysis_combined.pdf",
      "artifacts/_project/chart/gradient_analysis_combined.png",
      "artifacts/figures/gradient_analysis_combined.png",
      "artifacts/_project/data/same_seed_gradient_analysis.py",
      "artifacts/same_seed_gradient_analysis.py"
    ],
    "durationMs": 6,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_01Le3F9zjYdpDQL2RjkkLLi7`</summary>

```json
{
  "pattern": "gradient|fig:gradient",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "-C": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "fe3d3bed-ca40-47bd-9374-9ad3bc902974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vz22LQPoeDMKEWt7qrWZBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 23261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 10 · 2026-05-25T11:27:08.653Z_

<details><summary>↩ Tool result · `toolu_01Le3F9zjYdpDQL2RjkkLLi7`</summary>

```text
&lt;persisted-output>
Output too large (41.7KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/ae2d4a3c-06b0-45da-9eaf-0c50a936a8af/tool-results/toolu_01Le3F9zjYdpDQL2RjkkLLi7.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-29-\begin{abstract}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-30-Adding auxiliary spatial prediction heads (e.g., occupancy, depth) to Vision-Language-Action (VLA) models during fine-tuning is a natural strategy for improving collision avoidance.
artifacts/dream_reports/dream_20260523T025401/best/paper.tex-31-We conduct a systematic mechanism analysis on a 7.6B-parameter VLA using a six-condition factorial ablation on the LIBERO-Spatial benchmark, disentangling \emph{what} drives safety outcomes along three axes:
artifacts/dream_reports/dream_20260523T025401/best/paper.tex:32:(1)~\textbf{gradient flow existence}---severing the backward gradient from an auxiliary head to the vision encoder (Detach) degrades collision avoidance by $-3.4$\,pp relative to a no-auxiliary baseline, while all gradient-flow conditions remain within seed noise of the baseline;
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-33-(2)~\textbf{content irrelevance}---replacing ground-truth BEV occupancy targets with spatially-random targets (Random OCC, CAR\,$=$\,0.789) or egocentric depth (Depth, CAR\,$=$\,0.780) yields performance statistically indistinguishable from full occupancy supervision (Full OCC, CAR\,$=$\,0.797);
artifacts/dream_reports/dream_20260523T025401/best/paper.tex:34:(3)~\textbf{temporal sufficiency}---a dose-response analysis with cutoff ablations at 15K/25K/35K/45K steps reveals that early-phase gradient flow exposure (first 70\% of training) suffices for full protection, while a reverse-cutoff experiment shows that late-phase exposure alone fails (CAR\,$=$\,0.752 vs.\,0.785 for early exposure).
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
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "b3dc2bb7-e89e-4f17-98b5-21f3b09d0de3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-29-\\begin{abstract}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-30-Adding auxiliary spatial prediction heads (e.g., occupancy, depth) to Vision-Language-Action (VLA) models during fine-tuning is a natural strategy for improving collision avoidance.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-31-We conduct a systematic mechanism analysis on a 7.6B-parameter VLA using a six-condition factorial ablation on the LIBERO-Spatial benchmark, disentangling \\emph{what} drives safety outcomes along three axes:\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:32:(1)~\\textbf{gradient flow existence}---severing the backward gradient from an auxiliary head to the vision encoder (Detach) degrades collision avoidance by $-3.4$\\,pp relative to a no-auxiliary baseline, while all gradient-flow conditions remain within seed noise of the baseline;\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-33-(2)~\\textbf{content irrelevance}---replacing ground-truth BEV occupancy targets with spatially-random targets (Random OCC, CAR\\,$=$\\,0.789) or egocentric depth (Depth, CAR\\,$=$\\,0.780) yields performance statistically indistinguishable from full occupancy supervision (Full OCC, CAR\\,$=$\\,0.797);\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:34:(3)~\\textbf{temporal sufficiency}---a dose-response analysis with cutoff ablations at 15K/25K/35K/45K steps reveals that early-phase gradient flow exposure (first 70\\% of training) suffices for full protection, while a reverse-cutoff experiment shows that late-phase exposure alone fails (CAR\\,$=$\\,0.752 vs.\\,0.785 for early exposure).\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:35:Gradient norm tracking confirms that auxiliary gradients decay to $<$5\\% of action gradients by the saturation point, explaining the lossless removal.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-36-All findings replicate on LIBERO-Goal with identical condition ordering.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:37:Our results establish that auxiliary gradient flow is a \\emph{necessary condition} for preventing safety degradation during VLA fine-tuning, but the spatial content of supervision is secondary to its mere presence.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-38-\\end{abstract}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-39-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-40-%======================================================================\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-47-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-48-In this work, we subject this hypothesis to a rigorous mechanism analysis.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-49-Rather than simply comparing ``with auxiliary head'' versus ``without,'' we design a factorial ablation that independently varies three factors:\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:50:(i) whether the auxiliary head's gradients flow back into the vision encoder,\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-51-(ii) what spatial content the auxiliary targets encode, and\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:52:(iii) when during training the gradient signal is active.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-53-This three-axis decomposition reveals a surprising picture.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-54-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-55-\\textbf{Core finding.}\\quad\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:56:Auxiliary gradient flow is a \\emph{necessary condition} for preventing safety degradation---but the spatial content of the auxiliary targets is largely irrelevant.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:57:When gradient flow is severed (the Detach condition), collision avoidance rate (CAR) drops by 3.4\\,pp below a vanilla baseline that uses no auxiliary head at all.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:58:In contrast, all conditions that preserve gradient flow---whether predicting ground-truth BEV occupancy, random spatial noise, or egocentric depth---perform comparably to the vanilla baseline.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:59:The mechanism is not ``learning 3D structure helps avoid collisions'' but rather ``auxiliary gradient flow provides lightweight regularization that prevents encoder degradation during fine-tuning.''\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-60-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:61:We further show that this regularization effect is \\emph{temporally front-loaded}: gradient flow during the first 70\\% of training suffices for full protection, and late-phase exposure alone cannot compensate for early absence.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:62:A dose-response analysis with five cutoff points traces a saturation curve that aligns with gradient norm measurements, providing a mechanistic account of the temporal dynamics.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-63-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-64-\\textbf{Contributions.}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-65-\\begin{enumerate}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:66:\\item A three-axis mechanism analysis establishing that auxiliary gradient flow existence, not spatial content, is the necessary condition for preventing VLA safety degradation during fine-tuning.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:67:\\item A temporal dose-response analysis with forward and reverse cutoff experiments that identifies the critical window for gradient flow exposure and establishes a causal direction (early $\\gg$ late).\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-68-\\item Cross-benchmark replication on LIBERO-Goal confirming that all six conditions preserve their relative ordering, eliminating single-benchmark bias.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-69-\\end{enumerate}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-70-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-82-Our factorial design isolates the mechanism by which auxiliary tasks affect safety.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-83-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-84-\\textbf{Gradient Flow and Regularization.}\\quad\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:85:The role of auxiliary gradients as implicit regularizers has been studied in multi-task learning~\\cite{ruder2017overview,standley2020tasks}.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:86:Our finding that gradient flow presence matters more than target content connects to work on random-target training~\\cite{maennel2020neural}, which shows that even nonsensical supervision can shape representations through gradient dynamics.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-87-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-88-%======================================================================\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-89-\\section{Method}\n--\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-107-\\subsection{Experimental Design: Six-Condition Factorial Ablation}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-108-\\label{sec:conditions}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-109-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:110:We design six training conditions that independently vary gradient flow, target content, and temporal schedule:\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-111-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-112-\\begin{enumerate}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-113-\\item \\textbf{Vanilla}: No auxiliary head. Pure action loss baseline.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:114:\\item \\textbf{Full OCC}: Occupancy head with ground-truth BEV targets. Full gradient flow to encoders throughout training.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-115-\\item \\textbf{Random OCC}: Same architecture as Full OCC, but targets are spatially random binary grids (resampled each step). Gradient flow preserved; spatial content removed.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-116-\\item \\textbf{Depth}: Depth head with ground-truth egocentric depth targets. Tests whether egocentric spatial structure outperforms allocentric.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:117:\\item \\textbf{Detach}: Occupancy head with ground-truth targets, but \\texttt{.detach()} severs the gradient path from the occupancy loss to the vision encoders. The head trains (consuming compute) but cannot regularize the encoder.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-118-\\item \\textbf{Cutoff@$t$}: Occupancy head active for steps $[0, t]$, then removed. Tested at $t \\in \\{15\\text{K}, 25\\text{K}, 35\\text{K}, 45\\text{K}\\}$.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-119-\\end{enumerate}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-120-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-164-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-165-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-166-The dominant pattern is a binary split.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:167:All gradient-flow conditions (Full OCC, Random OCC, Cutoff@35K, Depth) cluster within $\\pm$1.7\\,pp of Vanilla---well within the seed standard deviation ($\\sigma \\approx 0.012$--$0.037$).\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:168:The Detach condition, which severs gradient flow while maintaining identical forward-pass computation, falls 3.4\\,pp below Vanilla.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-169-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-170-The Detach condition also exhibits extreme TSR instability: $\\sigma_\\text{TSR} = 0.163$ (one seed collapses to TSR\\,=\\,0.624), compared with $\\sigma_\\text{TSR} < 0.050$ for all other conditions.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-171-This suggests that the absence of encoder regularization not only harms safety but destabilizes task execution.\n--\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-177-\\subsection{Axis 2: Spatial Content Irrelevance}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-178-\\label{sec:axis2}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-179-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:180:Among the gradient-flow conditions, the content of auxiliary targets has negligible effect:\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-181-\\begin{itemize}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-182-\\item Full OCC (ground-truth BEV): CAR\\,=\\,0.797\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-183-\\item Random OCC (random binary grids): CAR\\,=\\,0.789\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-188-In particular, Depth matches Vanilla exactly (CAR\\,=\\,0.780 with 4 seeds), confirming that even geometrically meaningful egocentric supervision provides no advantage over the no-auxiliary baseline.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-189-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-190-This rules out the intuitive hypothesis that ``better spatial targets yield safer policies.''\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:191:The mechanism is content-agnostic: any auxiliary head that preserves gradient flow provides equivalent regularization.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-192-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-193-\\subsection{Axis 3: Temporal Sufficiency}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-194-\\label{sec:axis3}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-195-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-196-\\subsubsection{Dose-Response Analysis}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-197-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:198:We train four additional cutoff conditions, each receiving occupancy gradient flow for a prefix of training before removal.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-199-Table~\\ref{tab:dose} presents the complete dose-response curve.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-200-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-201-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-202-\\centering\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:203:\\caption{Dose-response: CAR as a function of gradient flow duration. Cutoff@35K uses 3-seed mean; others are single-seed.}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-204-\\label{tab:dose}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-205-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-206-\\begin{tabular}{@{}llccc@{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-220-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-221-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-222-The dose-response curve exhibits a classic saturation shape.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:223:The marginal CAR gain per 10K additional steps of gradient flow (Table~\\ref{tab:marginal}) peaks at 1.6\\,pp/10K in the 15K--25K interval and declines to 0.6\\,pp/10K beyond 45K.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:224:The Cutoff@35K condition (70\\% of training) already matches Vanilla, indicating that the remaining 30\\% of gradient flow is unnecessary.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-225-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-226-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-227-\\centering\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:228:\\caption{Marginal CAR gain per additional 10K steps of gradient flow exposure.}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-229-\\label{tab:marginal}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-230-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-231-\\begin{tabular}{@{}lcc@{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-243-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-244-\\subsubsection{Temporal Asymmetry: Forward vs.\\ Reverse Cutoff}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-245-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:246:The reverse-cutoff experiment provides causal evidence that \\emph{early} gradient flow, not total exposure, drives the regularization effect.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-247-In the reverse condition, the occupancy head is inactive for steps 0--35K (identical to Vanilla) and activated at step 35K.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-248-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-249-\\begin{table}[t]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-268-Forward cutoff (early exposure) achieves CAR\\,=\\,0.785, matching Vanilla.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-269-Reverse cutoff (late exposure) achieves only CAR\\,=\\,0.752---nearly identical to Detach (0.746).\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-270-The forward condition gains 3.9\\,pp over Detach; the reverse gains only 0.6\\,pp.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:271:The 3.3\\,pp asymmetry rules out the alternative hypothesis that total gradient flow exposure, rather than its timing, determines effectiveness.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-272-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:273:This temporal asymmetry reflects a ``critical period'' for encoder representations: during early training, LoRA parameters exhibit high plasticity, and auxiliary gradients can shape spatial awareness structures.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:274:Once the action loss drives parameters toward a task-specific optimum, subsequent auxiliary gradients are too weak to reshape the established representations.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-275-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-276-\\subsection{Mechanistic Evidence: Gradient Norm Tracking}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-277-\\label{sec:gradnorm}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-278-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:279:To ground the behavioral dose-response curve in optimization dynamics, we track the L2 norm of gradients flowing from the occupancy and action heads to the DINOv2 and SigLIP LoRA parameters during training.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-280-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-281-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-282-\\centering\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:283:\\caption{Gradient norm temporal evolution (Full OCC condition). The OCC/Action ratio quantifies the relative strength of auxiliary gradient signal.}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-284-\\label{tab:gradnorm}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-285-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-286-\\begin{tabular}{@{}ccccc@{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-297-\\end{tabular}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-298-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-299-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:300:Table~\\ref{tab:gradnorm} shows that the OCC-to-Action gradient ratio decays monotonically from 8.6\\% to 3.2\\% over training.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:301:At step 35K---the dose-response saturation point---the ratio has dropped to 4.5\\%, meaning the auxiliary signal contributes less than 5\\% of the encoder's total gradient.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:302:This explains why removing the occupancy head at 35K incurs no measurable CAR loss: the signal being removed is already negligible relative to the action gradient.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-303-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-304-\\begin{table}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-305-\\centering\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:306:\\caption{Gradient norms at step 25K across conditions. Detach produces exactly zero auxiliary gradient to the encoder, confirming the severed gradient path.}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-307-\\label{tab:gradcond}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-308-\\small\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-309-\\begin{tabular}{@{}lccc@{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-318-\\end{tabular}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-319-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-320-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:321:Table~\\ref{tab:gradcond} compares gradient norms across conditions at step 25K.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:322:Full OCC and Random OCC exhibit nearly identical gradient magnitudes (1.8e-4 vs.\\ 1.9e-4), directly supporting the content-irrelevance finding: the encoder receives gradient signals of similar magnitude and structure regardless of whether the targets are meaningful or random.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:323:Detach produces exactly zero gradient to the encoder, confirming the mechanism of its degradation.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-324-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-325-\\subsection{Cross-Benchmark Replication: LIBERO-Goal}\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-326-\\label{sec:goal}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-347-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-348-\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-349-Table~\\ref{tab:goal} confirms that all three axes replicate:\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:350:(1) Detach degrades by $-3.2$\\,pp (vs.\\ $-3.4$\\,pp on Spatial), confirming gradient flow necessity;\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:351:(2) gradient-flow conditions cluster within 1.4\\,pp of Vanilla, confirming content irrelevance;\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-352-(3) Cutoff@35K matches Vanilla, confirming temporal sufficiency.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-353-The six-condition ordering is consistent across both benchmarks: the probability of observing this consistency under random ordering is $1/6! = 0.14\\%$, providing strong evidence that the mechanism generalizes across task structures.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-354-\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-358-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-359-\\textbf{Three-axis mechanism model.}\\quad\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-360-Our factorial analysis decomposes the effect of auxiliary spatial supervision into three independent factors.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:361:The gradient flow existence axis reveals a binary mechanism: with flow, the auxiliary head provides lightweight regularization equivalent to the no-auxiliary baseline; without flow, the head actively harms the model.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-362-The content irrelevance axis shows that the regularization effect is agnostic to what is being predicted---random noise works as well as ground-truth spatial structure.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:363:The temporal sufficiency axis establishes that early-phase gradient flow exposure is both necessary and sufficient, with a critical window in the first 50--70\\% of training.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-364-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-365-\\textbf{Practical implications.}\\quad\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-366-For practitioners adding auxiliary heads to VLA models:\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:367:(1)~always ensure gradient flow to the encoder---a detached head is worse than no head at all;\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-368-(2)~do not invest in expensive ground-truth spatial labels when random targets suffice;\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-369-(3)~auxiliary supervision can be safely removed after the early training phase, reducing computational cost in the later stages.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-370-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-371-\\textbf{Connection to multi-task learning.}\\quad\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:372:Our finding that gradient flow presence matters more than target content resonates with results in multi-task learning showing that auxiliary task gradients can regularize shared representations even when tasks are unrelated.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-373-The exponential decay schedule ($w(t) = 0.01 \\cdot \\exp(-t/50000)$) naturally implements a ``let go'' curriculum that transitions from multi-task to single-task optimization.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-374-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-375-\\textbf{Limitations.}\\quad\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-384-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-385-We present a three-axis mechanism analysis of auxiliary spatial supervision in VLA fine-tuning.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex-386-Through a six-condition factorial ablation on two LIBERO benchmarks, we establish that:\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:387:auxiliary gradient flow existence is a necessary condition for preventing safety degradation;\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:388:the content of auxiliary targets is secondary to gradient flow presence;\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-389-and the regularization effect is temporally front-loaded, with a critical window in the first 70\\% of training.\nartifacts/dream_reports/dream_20260523T025401/best/paper.tex:390:These findings shift the design question from ``what spatial representation should we predict?'' to ``how do we ensure auxiliary gradient flow reaches the encoder during early training?''---a simpler and more actionable guideline for safe VLA deployment.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-391-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-392-\\bibliographystyle{plain}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/best/paper.tex-393-\\begin{thebibliography}{10}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-38-A natural hypothesis is that auxiliary spatial supervision---such as occupancy prediction from Bird's-Eye View---could improve safety by forcing the vision encoder to develop 3D spatial awareness.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-39-We conduct a systematic factorial study with 5+ experimental conditions and 3 random seeds to dissect \\emph{how} auxiliary spatial heads affect collision avoidance in VLA fine-tuning.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-40-Our findings reveal two axes of analysis:\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:41:(1)~\\textbf{Gradient flow is necessary}: detaching the auxiliary head from the encoder (removing gradient flow while preserving forward-pass computation) degrades collision avoidance rate (CAR) by 3.4 percentage points relative to the no-auxiliary baseline (Cohen's $d\\!\\approx\\!4.0$), while all gradient-flow conditions remain statistically indistinguishable from the baseline.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-42-(2)~\\textbf{Spatial content is irrelevant}: replacing ground-truth BEV occupancy with random labels, monocular depth, or removing the auxiliary head entirely yields equivalent CAR ($\\Delta\\!\\leq\\!1.7$pp, within seed variance).\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:43:Gradient norm analysis, CKA representation similarity, and normalization-controlled ablations provide converging mechanistic evidence that auxiliary gradient flow acts as a mild regularizer on optimization dynamics rather than restructuring encoder representations.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:44:These results caution practitioners: if attaching an auxiliary head to a VLA, preserving gradient flow is critical---otherwise the head actively harms safety.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-45-\\end{abstract}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-46-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-47-% ============================================================\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-52-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-53-Vision-Language-Action (VLA) models that map visual observations and language instructions to robot actions have achieved impressive manipulation capabilities. However, collision safety---the ability to avoid unintended contacts during task execution---remains under-addressed. A VLA trained solely on action imitation may learn to complete tasks without developing explicit spatial awareness, leading to unsafe trajectories in cluttered environments.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-54-\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:55:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-56-\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-57-In this work, we disentangle these factors through a controlled factorial study on SafeLIBERO, evaluating a 7.65B-parameter VLA across the following conditions:\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-58-\\begin{itemize}[nosep,leftmargin=1.5em]\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-59-  \\item \\textbf{Vanilla}: no auxiliary head (action loss only).\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:60:  \\item \\textbf{Full OCC}: auxiliary BEV occupancy head with gradient flow.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-61-  \\item \\textbf{Random OCC}: same architecture, but predicting random binary labels.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:62:  \\item \\textbf{Detach}: same architecture, but with \\texttt{stop\\_gradient} between encoder and auxiliary head.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-63-  \\item \\textbf{Depth}: auxiliary monocular depth prediction head (egocentric, regression).\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-64-  \\item \\textbf{Cutoff@$t$}: OCC loss active for the first $t$ steps, then removed.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-65-\\end{itemize}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-66-\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:67:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-68-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-69-\\paragraph{Contributions.}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-70-\\begin{enumerate}[nosep,leftmargin=1.5em]\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:71:  \\item We demonstrate that auxiliary gradient flow is a \\emph{necessary condition} for preventing safety degradation in VLA fine-tuning, while spatial content is secondary (Section~\\ref{sec:core}).\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:72:  \\item We provide converging mechanistic evidence---gradient norms, CKA, normalization-controlled ablations---that gradient flow operates through subtle optimization dynamics, not representation restructuring (Section~\\ref{sec:mechanism}).\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-73-  \\item We present the first multi-condition factorial ablation study specifically targeting VLA collision safety mechanisms, establishing a methodology for future mechanism analyses.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-74-\\end{enumerate}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-75-\n--\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-114-We define six primary conditions to isolate different mechanistic hypotheses:\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-115-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-116-\\begin{enumerate}[nosep,leftmargin=1.5em]\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:117:  \\item \\textbf{Full OCC}: Standard auxiliary training. Occupancy gradients flow through the encoder.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-118-  \\item \\textbf{Random OCC}: Identical architecture, but ground-truth BEV labels are replaced with random binary grids. Tests whether \\emph{spatial content} matters.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:119:  \\item \\textbf{Detach}: \\texttt{stop\\_gradient} is applied between the encoder output and the auxiliary head input. The head still performs forward computation (affecting BatchNorm statistics) but provides zero gradient to the encoder. Tests whether \\emph{gradient flow} is the active mechanism.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-120-  \\item \\textbf{Depth}: Monocular depth prediction replaces BEV occupancy. Tests whether the viewpoint (egocentric vs.\\ allocentric) or task modality matters.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex:121:  \\item \\textbf{Cutoff@$t$}: Auxiliary loss is active for steps $[0, t]$ and removed thereafter. Tests the \\emph{temporal} dependency of gradient flow.\nartifacts/dream_reports/dream_20260523T025401/median/paper.tex-122-  \\item \\textbf{Vanilla}: No auxiliary head. Pure action-loss baseline.\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-123-\\end{enumerate}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/dream_reports/dream_20260523T025401/median/paper.tex-124-",
    "numLines": 250,
    "appliedLimit": 250
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01GGagJEKXoSgZXW94xbwsez`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/_project/chart/gradient_analysis_combined.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "a08a9929-0391-45f3-a768-b0f58bb80cc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vz22LQPoeDMKEWt7qrWZBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 23261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
      },
      "output_tokens": 73,
      "service_tier": "standard",
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

_source line 12 · 2026-05-25T11:27:10.872Z_

<details><summary>↩ Tool result · `toolu_01GGagJEKXoSgZXW94xbwsez`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
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
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "4faea535-19ff-44f9-8195-9a1822cd7f20",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 309456
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
I can see the image. Let me analyze the conditions in each subplot:

(a) Action Gradient Norms per Layer: Shows Vanilla, Full OCC, Random OCC, Detach - that's 4 conditions
(b) OCC Auxiliary Gradient Norms: Shows Full OCC, Random OCC - 2 conditions
(c) Action-Auxiliary Gradient Cosine Similarity: Shows Full OCC, Random OCC - 2 conditions
(d) Gradient Collapse (Detach vs. Vanilla): Shows Detach/Vanilla ratio - effectively 1 condition comparison

So the main comparison in subplot (a) has 4 conditions: Vanilla, Full OCC, Random OCC, Detach. 

I don't see a "Detach+LN" variant in the plots. Now let me check the caption text in the tex file to understand what these experiments are measuring.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "bf231d28-9766-417b-bc80-173d450a2289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LaCkPhrsivh15FtRqYURW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 23738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 14_

The image shows 4 conditions in subplot (a): **Vanilla, Full OCC, Random OCC, Detach**. No "Detach+LN" is visible. Let me find the caption text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "c8abb841-2772-4e87-a5c9-498aaed085f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LaCkPhrsivh15FtRqYURW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 23738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 15_

<details open><summary>🔧 Tool call — Grep · `toolu_01JYZ3vgLUcAbUXkEB7KKr5L`</summary>

```json
{
  "pattern": "fig:gradient_analysis|gradient_analysis_combined",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true,
  "-C": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "31634411-b250-48e4-9cdb-a3dd7f9f76f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LaCkPhrsivh15FtRqYURW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 23738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1382
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

_source line 16 · 2026-05-25T11:27:19.700Z_

<details><summary>↩ Tool result · `toolu_01JYZ3vgLUcAbUXkEB7KKr5L`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-70-\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
docs/paper/results.tex-71-\caption{$2{\times}2$ factorial interaction: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). Gradient flow improves CAR under BN ($+$5.1\,pp) but degrades it under LN ($-$2.2\,pp), yielding a 7.3\,pp crossover interaction ($p{=}0.025$). Error bars: cross-seed SD ($n{=}3$ per cell).}
docs/paper/results.tex-72-\label{fig:factorial}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-73-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-74-
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-75-\subsection{Gradient Dynamics}
docs/paper/results.tex-76-\label{sec:gradient_dynamics}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-77-
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-78-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-79-\centering
docs/paper/results.tex:80:\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-81-[Omitted long context line]
docs/paper/results.tex:82:\label{fig:gradient_analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-83-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-84-
docs/paper/results.tex:85:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-86-
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-87-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-88-
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-89-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-90-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-91-\includegraphics[width=0.75\textwidth]{figures/cka_analysis.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-92-\caption{CKA similarity between fine-tuned and pretrained encoder features. All conditions except Detach OCC preserve pretrained structure (CKA $\geq$0.95), including Full OCC+LN, which achieves the lowest CAR despite high CKA (a representation-behavior dissociation). Detach OCC drifts catastrophically, especially in SigLIP middle layers, which confirms BatchNorm as the sole cause of representational drift.}
docs/paper/results.tex-93-\label{fig:cka_analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-94-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-95-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "79a17933-b718-4362-a0e6-f47ab76dc6ec",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-70-\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\ndocs/paper/results.tex-71-\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Gradient flow improves CAR under BN ($+$5.1\\,pp) but degrades it under LN ($-$2.2\\,pp), yielding a 7.3\\,pp crossover interaction ($p{=}0.025$). Error bars: cross-seed SD ($n{=}3$ per cell).}\ndocs/paper/results.tex-72-\\label{fig:factorial}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-73-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-74-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-75-\\subsection{Gradient Dynamics}\ndocs/paper/results.tex-76-\\label{sec:gradient_dynamics}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-77-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-78-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-79-\\centering\ndocs/paper/results.tex:80:\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-81-[Omitted long context line]\ndocs/paper/results.tex:82:\\label{fig:gradient_analysis}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-83-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-84-\ndocs/paper/results.tex:85:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-86-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-87-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-88-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-89-\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-90-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-91-\\includegraphics[width=0.75\\textwidth]{figures/cka_analysis.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-92-\\caption{CKA similarity between fine-tuned and pretrained encoder features. All conditions except Detach OCC preserve pretrained structure (CKA $\\geq$0.95), including Full OCC+LN, which achieves the lowest CAR despite high CKA (a representation-behavior dissociation). Detach OCC drifts catastrophically, especially in SigLIP middle layers, which confirms BatchNorm as the sole cause of representational drift.}\ndocs/paper/results.tex-93-\\label{fig:cka_analysis}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-94-\\end{figure}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-95-",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 17_

Line 81 was truncated. Let me read it directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "0359e98c-426f-45f6-81e3-e3c1336821e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es3NHAWuGtkMAgiexorT67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 25120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1637
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_017g7ihF6rKTX4WrKMVbMUHy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 78,
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
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "bb97bb7b-7bf1-4271-b2d4-5de6d7ad0780",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es3NHAWuGtkMAgiexorT67",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1637,
      "cache_read_input_tokens": 25120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1637
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

_source line 19 · 2026-05-25T11:27:23.425Z_

<details><summary>↩ Tool result · `toolu_017g7ihF6rKTX4WrKMVbMUHy`</summary>

```text
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}
81	\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}
82	\label{fig:gradient_analysis}
83	\end{figure}
84	
85	Figure~\ref{fig:gradient_analysis} reveals a gradient collapse mechanism underlying the Detach degradation. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\times$ Vanilla norms), which rules out gradient amplification. Detach OCC, however, exhibits catastrophic collapse: encoder gradient norms fall to 1--13\% of Vanilla across all layers (action gradient norm 0.005 vs.\ Vanilla 0.126, a 25$\times$ reduction). Per-layer analysis (Figure~\ref{fig:per_layer_combined}, Appendix) decomposes auxiliary gradient flow into amplitude and direction: Detach collapses uniformly while gradient-flow conditions maintain Vanilla-comparable norms; DINOv2 layers show $\sim$50\% conflict rate while SigLIP late layers (blocks 21--24) drop to 19--25\%, which indicates cooperative alignment. Both patterns are identical for structured and random labels. The crossover interaction (Section~\ref{sec:mechanism}) reveals that gradient flow's collapse-prevention effect is BN-mediated: under LN, gradient flow degrades rather than improves CAR.
86	
87	\textbf{LN induces cross-backbone gradient redistribution.} Same-seed analysis (seed 42, four conditions, 200 batches at 50K checkpoint) reveals why LayerNorm with gradient flow degrades CAR. Under Full OCC+LN, action loss gradients in DINOv2 are suppressed 3.5$\times$ relative to BN (mean norm 0.048 vs.\ 0.168), while SigLIP action gradients are amplified 2.5$\times$ (0.206 vs.\ 0.081). Conflict rates remain ${\sim}$50\% in both conditions, which rules out directional conflict as the cause. The mechanism is cross-backbone amplitude redistribution: LN normalization redistributes gradient magnitude from DINOv2 to SigLIP, disrupting the balanced allocation that BN maintains (DINOv2: 0.8$\times$ Vanilla, SigLIP: 1.0$\times$ Vanilla). This explains why Full OCC+LN degrades CAR despite preserving pretrained representations: the problem is not \emph{what} the encoders represent, but \emph{how} gradient flow allocates learning signal across them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "4db33fa7-30e5-42de-a4df-1e5c0a946a99",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nFigure~\\ref{fig:gradient_analysis} reveals a gradient collapse mechanism underlying the Detach degradation. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\\times$ Vanilla norms), which rules out gradient amplification. Detach OCC, however, exhibits catastrophic collapse: encoder gradient norms fall to 1--13\\% of Vanilla across all layers (action gradient norm 0.005 vs.\\ Vanilla 0.126, a 25$\\times$ reduction). Per-layer analysis (Figure~\\ref{fig:per_layer_combined}, Appendix) decomposes auxiliary gradient flow into amplitude and direction: Detach collapses uniformly while gradient-flow conditions maintain Vanilla-comparable norms; DINOv2 layers show $\\sim$50\\% conflict rate while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative alignment. Both patterns are identical for structured and random labels. The crossover interaction (Section~\\ref{sec:mechanism}) reveals that gradient flow's collapse-prevention effect is BN-mediated: under LN, gradient flow degrades rather than improves CAR.\n\n\\textbf{LN induces cross-backbone gradient redistribution.} Same-seed analysis (seed 42, four conditions, 200 batches at 50K checkpoint) reveals why LayerNorm with gradient flow degrades CAR. Under Full OCC+LN, action loss gradients in DINOv2 are suppressed 3.5$\\times$ relative to BN (mean norm 0.048 vs.\\ 0.168), while SigLIP action gradients are amplified 2.5$\\times$ (0.206 vs.\\ 0.081). Conflict rates remain ${\\sim}$50\\% in both conditions, which rules out directional conflict as the cause. The mechanism is cross-backbone amplitude redistribution: LN normalization redistributes gradient magnitude from DINOv2 to SigLIP, disrupting the balanced allocation that BN maintains (DINOv2: 0.8$\\times$ Vanilla, SigLIP: 1.0$\\times$ Vanilla). This explains why Full OCC+LN degrades CAR despite preserving pretrained representations: the problem is not \\emph{what} the encoders represent, but \\emph{how} gradient flow allocates learning signal across them.",
      "numLines": 10,
      "startLine": 78,
      "totalLines": 109
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Found the issue. The caption on line 81 says:

"four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN"

But looking at the image, subplot (a) actually shows 4 conditions: Vanilla, Full OCC, Random OCC, Detach. The legend clearly shows these four.

Wait, let me re-read. The caption says "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN" but then in the description of subplot (a) it mentions "Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses..."
 
There's a clear mismatch here. The caption header lists "Vanilla, Full OCC, Detach OCC, Full OCC+LN" but the actual figure shows "Vanilla, Full OCC, Random OCC, Detach" across all subplots. The caption text itself even references Random OCC in subplot (a), which contradicts the header. So either the caption header needs to be corrected to match what's actually plotted, or the figure is wrong. and the caption incorrectly lists "Full OCC+LN" when it should say "Random OCC" instead. The user's question is asking whether to change "four" to "five" if there are 5 conditions, but since there are only 4 conditions in the figure, the fix needed is just correcting the condition names in the caption, not changing the number.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "e1c0bea3-7670-430d-876c-111831332b06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES5RNNzxTshMPPrKuYphW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 26757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 21_

图中有 **4 个 condition**：Vanilla, Full OCC, Random OCC, Detach。数量 "four" 是对的，不需要改成 "five"。

但 caption 中列举的条件名称有误——写的是 "Vanilla, Full OCC, Detach OCC, Full OCC+LN"，实际图中没有 Full OCC+LN，有的是 Random OCC。需要修正条件列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "a72bb916-659e-4bf1-a609-6b2d5ce860e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES5RNNzxTshMPPrKuYphW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 26757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_016zQrhhBRL7ByF9aTmexLJ3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN",
  "new_string": "four conditions: Vanilla, Full OCC, Random OCC, Detach OCC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "de39ff4e-b7a0-4975-964e-e945a9eee89e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES5RNNzxTshMPPrKuYphW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 994,
      "cache_read_input_tokens": 26757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 994
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

_source line 23 · 2026-05-25T11:27:44.627Z_

<details><summary>↩ Tool result · `toolu_016zQrhhBRL7ByF9aTmexLJ3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "89249903-77c8-4376-822c-8ddf823453c7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN",
    "newString": "four conditions: Vanilla, Full OCC, Random OCC, Detach OCC",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). Statistical comparisons use paired $t$-tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Crossover interaction between normalization and gradient flow.} The four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) reveal a crossover interaction rather than additive effects (Section~\\ref{sec:mechanism}). Full OCC with BN maintains CAR comparable to Vanilla (0.797 vs.\\ 0.780, $d{=}+0.69$, $p{=}0.44$). Detach OCC with BN falls 3.4\\,pp below Vanilla ($p{=}0.031$, $d{=}-3.90$), the only statistically significant pairwise difference. Detach+LN (0.765) recovers 1.9\\,pp of this deficit by eliminating BatchNorm interference. However, Full OCC+LN (0.743) consistently degrades CAR by 3.7\\,pp below Vanilla despite maintaining gradient flow; this is the worst configuration tested. BN is thus beneficial when gradient flow calibrates its statistics, but harmful when gradient flow is absent; LN shows the opposite pattern. These results are consistent with the hypothesis that label content does not affect outcomes: Random OCC (0.789), Depth (0.780), and Full OCC (0.797) are all within cross-seed variance ($p > 0.4$).\n\n\\textbf{Detach destabilizes optimization broadly.} Detach OCC exhibits TSR variance an order of magnitude above other conditions ($\\sigma = 0.163$ vs.\\ $< 0.050$): one seed collapses to TSR 0.624 with uniform degradation across all tasks, while its CAR (0.748) stays comparable to the other two seeds. The low CAR variance ($\\sigma = 0.002$) despite volatile TSR ($\\sigma = 0.163$) suggests deterministic convergence to a degraded safety behavior: BN interference imposes a consistent representational distortion regardless of initialization.\n\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Overall results on SafeLIBERO Level~I (10 tasks). Mean $\\pm$ SD across seeds; 95\\% CIs via bootstrap. $^\\dagger$1 seed; $^\\ddagger$2 seeds. $^*$Statistically significant vs.\\ Vanilla (paired $t$-test $p{<}0.05$). Cutoff conditions retain the auxiliary head forward pass post-cutoff (Detach mode).}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Seeds & TSR & CAR & $95\\%$ CI & $\\Delta$CAR \\\\\n\\midrule\nFull OCC (BN)      & 3 & 0.894 $\\pm$ 0.050 & \\textbf{0.797} $\\pm$ 0.032 & [0.770, 0.832] & $+$1.7 \\\\\nRandom OCC (BN)    & 3 & 0.869 $\\pm$ 0.029 & 0.789 $\\pm$ 0.031 & [0.754, 0.814] & $+$0.9 \\\\\nVanilla       & 3 & 0.907 $\\pm$ 0.009 & 0.780 $\\pm$ 0.012 & [0.766, 0.788] & ---    \\\\\nDetach+LN     & 3 & 0.901 $\\pm$ 0.016 & 0.765 $\\pm$ 0.023 & [0.748, 0.792] & $-$1.5 \\\\\nDetach OCC (BN)$^*$    & 3 & 0.812 $\\pm$ 0.163 & 0.746 $\\pm$ 0.002 & [0.744, 0.748] & $-$3.4 \\\\\nFull OCC+LN   & 3 & 0.897 $\\pm$ 0.032 & 0.743 $\\pm$ 0.024 & [0.718, 0.766] & $-$3.7 \\\\\n\\midrule\nDepth             & 4 & 0.889 $\\pm$ 0.042 & 0.780 $\\pm$ 0.039 & [0.747, 0.812] & 0.0 \\\\\nCutoff@15K$^\\ddagger$   & 2 & 0.883 $\\pm$ 0.041 & 0.782 $\\pm$ 0.031 & --- & $+$0.2 \\\\\nCutoff@25K$^\\ddagger$   & 2 & 0.887 $\\pm$ 0.061 & 0.724 $\\pm$ 0.051 & --- & $-$5.6 \\\\\nCutoff@35K        & 3 & 0.933 $\\pm$ 0.032 & 0.779 $\\pm$ 0.017 & [0.768, 0.798] & $-$0.1 \\\\\nCutoff@45K$^\\dagger$    & 1 & 0.896 & 0.764 & --- & $-$1.6 \\\\\nReverse Cutoff$^\\ddagger$ & 2 & 0.839 $\\pm$ 0.072 & 0.718 $\\pm$ 0.025 & --- & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization--Gradient Flow Interaction}\n\\label{sec:mechanism}\n\nThe four conditions crossing normalization type (BN/LN) with gradient flow (ON/OFF) form a $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}). A $2{\\times}2$ ANOVA confirms a significant interaction ($F(1,8){=}7.511$, $p{=}0.025$, partial $\\eta^2{=}0.484$, Cohen's $f{=}0.969$), while neither main effect reaches significance (gradient flow: $p{=}0.326$; normalization: $p{=}0.231$). The interaction effect is 7.3\\,pp: gradient flow's effect on CAR reverses sign depending on normalization type.\n\n\\textbf{Crossover, not additive.} With BN, gradient flow improves CAR by $+$5.1\\,pp (Full OCC 0.797 vs.\\ Detach 0.746; simple effect $p{=}0.052$, $d{=}5.13$). With LN, gradient flow \\emph{degrades} CAR by $-$2.2\\,pp (Full OCC+LN 0.743 vs.\\ Detach+LN 0.765; $p{=}0.26$). Neither simple effect reaches significance individually, but the large effect sizes and opposing directions confirm the crossover pattern. This rules out an additive decomposition: gradient flow benefits are BatchNorm-mediated, arising from gradient calibration of BN running statistics, not from an intrinsic regularization property of auxiliary gradients.\n\n\\textbf{Full OCC+LN is the worst configuration.} Despite maintaining gradient flow and using a normalization layer that eliminates representational drift (Section~\\ref{sec:gradient_dynamics}), Full OCC+LN (0.743) falls 3.7\\,pp below Vanilla, consistently across all three seeds (0.766, 0.718, 0.744). This is the strongest evidence for a representation-behavior dissociation: the configuration that best preserves pretrained representations produces the worst safety behavior.\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow. The 7.3\\,pp interaction effect indicates a crossover: gradient flow benefits are BN-mediated.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (\\textbf{0.797}) & Detach OCC (0.746) & $+$5.1 \\\\\nLayerNorm    & Full OCC+LN (0.743) & Detach+LN (0.765) & $-$2.2 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $+$5.4 & $-$1.9 & interaction: 7.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial interaction: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). Gradient flow improves CAR under BN ($+$5.1\\,pp) but degrades it under LN ($-$2.2\\,pp), yielding a 7.3\\,pp crossover interaction ($p{=}0.025$). Error bars: cross-seed SD ($n{=}3$ per cell).}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\\label{sec:gradient_dynamics}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nFigure~\\ref{fig:gradient_analysis} reveals a gradient collapse mechanism underlying the Detach degradation. All gradient norms are computed with respect to the L1 action loss (action tokens only), not the full language modeling objective. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (0.87--1.14$\\times$ Vanilla norms), which rules out gradient amplification. Detach OCC, however, exhibits catastrophic collapse: encoder gradient norms fall to 1--13\\% of Vanilla across all layers (action gradient norm 0.005 vs.\\ Vanilla 0.126, a 25$\\times$ reduction). Per-layer analysis (Figure~\\ref{fig:per_layer_combined}, Appendix) decomposes auxiliary gradient flow into amplitude and direction: Detach collapses uniformly while gradient-flow conditions maintain Vanilla-comparable norms; DINOv2 layers show $\\sim$50\\% conflict rate while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative alignment. Both patterns are identical for structured and random labels. The crossover interaction (Section~\\ref{sec:mechanism}) reveals that gradient flow's collapse-prevention effect is BN-mediated: under LN, gradient flow degrades rather than improves CAR.\n\n\\textbf{LN induces cross-backbone gradient redistribution.} Same-seed analysis (seed 42, four conditions, 200 batches at 50K checkpoint) reveals why LayerNorm with gradient flow degrades CAR. Under Full OCC+LN, action loss gradients in DINOv2 are suppressed 3.5$\\times$ relative to BN (mean norm 0.048 vs.\\ 0.168), while SigLIP action gradients are amplified 2.5$\\times$ (0.206 vs.\\ 0.081). Conflict rates remain ${\\sim}$50\\% in both conditions, which rules out directional conflict as the cause. The mechanism is cross-backbone amplitude redistribution: LN normalization redistributes gradient magnitude from DINOv2 to SigLIP, disrupting the balanced allocation that BN maintains (DINOv2: 0.8$\\times$ Vanilla, SigLIP: 1.0$\\times$ Vanilla). This explains why Full OCC+LN degrades CAR despite preserving pretrained representations: the problem is not \\emph{what} the encoders represent, but \\emph{how} gradient flow allocates learning signal across them.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/cka_analysis.pdf}\n\\caption{CKA similarity between fine-tuned and pretrained encoder features. All conditions except Detach OCC preserve pretrained structure (CKA $\\geq$0.95), including Full OCC+LN, which achieves the lowest CAR despite high CKA (a representation-behavior dissociation). Detach OCC drifts catastrophically, especially in SigLIP middle layers, which confirms BatchNorm as the sole cause of representational drift.}\n\\label{fig:cka_analysis}\n\\end{figure}\n\n\\textbf{CKA confirms BN as the sole cause of representational drift; however, representations do not predict behavior.} CKA between fine-tuned and pretrained features (Figure~\\ref{fig:cka_analysis}) shows that all non-Detach-BN conditions preserve pretrained structure (CKA $\\geq$ 0.95): Vanilla, Full OCC, Random OCC, Detach+LN, and Full OCC+LN. Detach OCC alone drifts catastrophically (DINOv2: 0.539; SigLIP: 0.312). CKA analysis indicates that LN generally does not cause representational drift (s1, s2 CKA${\\approx}$0.97), suggesting that the CAR degradation under Full OCC+LN operates through gradient dynamics (specifically the cross-backbone gradient redistribution described above) rather than representation corruption. Yet Full OCC+LN achieves the \\emph{lowest} CAR (0.743) while Full OCC with BN achieves the highest (0.797), both at high CKA. This \\emph{representation-behavior dissociation} demonstrates that preserving pretrained features is neither sufficient nor predictive of collision avoidance.\n\n\\textbf{Same-seed validation.} The cross-backbone gradient redistribution findings are confirmed by same-seed analysis (seed 42, four conditions trained identically except for normalization and gradient flow), eliminating cross-seed confounds present in earlier cross-seed comparisons.\n\n\\subsection{Additional Observations}\n\\label{sec:per_task}\n\\label{sec:temporal}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task}). Detach is systematically worst on these hard tasks (T3: 0.11, T5: 0.05), consistent with gradient collapse exacerbating degradation where obstacle proximity is tight.\n\n\\textbf{Egocentric depth matches Vanilla.} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla, despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla ($\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Appendix~\\ref{app:temporal}.\n",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}",
          "-\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}",
          "+\\caption{Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a)~Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1--13\\% of Vanilla. (b)~Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d)~Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.}",
          " \\label{fig:gradient_analysis}",
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

### Assistant

_source line 24_

结果：

**(a) 图中实际包含的 conditions：** Vanilla, Full OCC, Random OCC, Detach — 共 4 个。

**(b) 修改内容：** 数量 "four" 不变（确实是 4 个），但修正了条件列表：`Full OCC+LN` → `Random OCC`（Full OCC+LN 不在图中，Random OCC 在图中）。

**(c) 修改后的 caption 全文：**

> Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a) Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1–13% of Vanilla. (b) Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c) Action–auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d) Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "uuid": "9615e805-aad2-4156-a11f-ce829edca85b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8swX2wcd7qhUDm3s9J9UX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 27751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1398
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

_source line 25_

结果：

**(a) 图中实际包含的 conditions：** Vanilla, Full OCC, Random OCC, Detach — 共 4 个。

**(b) 修改内容：** 数量 "four" 不变（确实是 4 个），但修正了条件列表：`Full OCC+LN` → `Random OCC`（Full OCC+LN 不在图中，Random OCC 在图中）。

**(c) 修改后的 caption 全文：**

> Gradient dynamics during VLA fine-tuning (seed 42, 200 batches at 50K checkpoint; four conditions: Vanilla, Full OCC, Random OCC, Detach OCC). (a) Action loss gradient norms per encoder layer: Vanilla, Full OCC, and Random OCC are comparable, while Detach collapses to 1–13% of Vanilla. (b) Auxiliary loss gradient norms in the shared encoder (Detach excluded; no auxiliary gradients by design). (c) Action–auxiliary gradient cosine similarity per layer (near zero for both Full OCC and Random OCC, which confirms orthogonality). (d) Gradient collapse ratio (Detach / Vanilla) quantifying the per-layer collapse magnitude.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 50798,
  "duration_api_ms": 50188,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "ae2d4a3c-06b0-45da-9eaf-0c50a936a8af",
  "total_cost_usd": 0.243965,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 17308,
    "cache_read_input_tokens": 138468,
    "output_tokens": 2609,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17308,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 311,
        "cache_read_input_tokens": 27751,
        "cache_creation_input_tokens": 1398,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1398
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1211,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001291,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2609,
      "cacheReadInputTokens": 138468,
      "cacheCreationInputTokens": 17308,
      "webSearchRequests": 0,
      "costUSD": 0.242674,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c7fad70e-713e-4f0e-912a-c65d99e0960e"
}
```

</details>

---
