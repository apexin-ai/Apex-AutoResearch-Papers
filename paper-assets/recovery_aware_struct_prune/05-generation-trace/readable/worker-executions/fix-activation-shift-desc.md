# fix activation shift desc

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_fix_activation-shift-desc_20260514T090643.log`
- **Structured JSON:** [`445e3c5c884869d11a7a.json`](../../sessions/44/445e3c5c884869d11a7a.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "d985791e-8163-4017-b101-33591234225b",
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
  "uuid": "4d835bf8-4524-46f3-bbc2-bff70d076a24",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778763000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "952b793e-8c9f-4420-a5ef-25f9a8b64c34",
  "session_id": "d985791e-8163-4017-b101-33591234225b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the file to find the relevant section around line 65.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "62575a2d-3d90-4c4e-9e29-477f2fe8a857",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtvtoqMaBmkJYCTLzGG9Cn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_0147mth5GhUtJ91UvAT4hY5E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
  "offset": 55,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "3c0042d7-299f-4749-a34b-083516744229",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtvtoqMaBmkJYCTLzGG9Cn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11152,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11152
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

_source line 6 · 2026-05-14T09:06:59.412Z_

<details><summary>↩ Tool result · `toolu_0147mth5GhUtJ91UvAT4hY5E`</summary>

```text
55	\paragraph{Recoverability.}
56	We define the recoverability of a pruning configuration as:
57	\begin{equation}
58	\Delta_{\text{acc}} = \text{Acc}_{\text{post-recovery}} - \text{Acc}_{\text{post-prune}}
59	\label{eq:recoverability}
60	\end{equation}
61	This measures how much accuracy a pruned model regains through RLVR recovery, capturing the ease of fine-tuning recovery independent of the initial pruning damage.
62	
63	\paragraph{Correlation Analysis.}
64	To validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.
65	We measure structure-level recoverability using \emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \cos(\mathbf{a}^{\text{pre}}_h, \mathbf{a}^{\text{post}}_h)$, where $\mathbf{a}^{\text{pre}}_h$ and $\mathbf{a}^{\text{post}}_h$ are the hidden states before and after pruning structure $h$.
66	This proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\Delta_{\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.
67	A statistically significant positive correlation ($\rho \geq 0.4$, $p < 0.01$) supports the claim that RASP's overlap-aware scoring preferentially retains groups whose removal would be hardest to recover from.
68	
69	\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "e8c11687-5141-480c-a70b-3523f834fea2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
      "content": "\\paragraph{Recoverability.}\nWe define the recoverability of a pruning configuration as:\n\\begin{equation}\n\\Delta_{\\text{acc}} = \\text{Acc}_{\\text{post-recovery}} - \\text{Acc}_{\\text{post-prune}}\n\\label{eq:recoverability}\n\\end{equation}\nThis measures how much accuracy a pruned model regains through RLVR recovery, capturing the ease of fine-tuning recovery independent of the initial pruning damage.\n\n\\paragraph{Correlation Analysis.}\nTo validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.\nWe measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\nThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.\nA statistically significant positive correlation ($\\rho \\geq 0.4$, $p < 0.01$) supports the claim that RASP's overlap-aware scoring preferentially retains groups whose removal would be hardest to recover from.\n\n\\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}\n",
      "numLines": 16,
      "startLine": 55,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Edit · `toolu_011p79xegVNByr4QvWrvEPhD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
  "old_string": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\n\tThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
  "new_string": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each pruned structure $g_p$, we identify its most CKA-similar retained structure $g_r$ and compute $1 - \\cos(\\mathbf{a}^{\\text{pruned}}_{g_r}, \\mathbf{a}^{\\text{recovered}}_{g_r})$, measuring the degree to which RLVR redistributes the pruned structure's function to its nearest functional neighbor.\n\tThis proxy is justified on two grounds: (i)~activation shift on the retained neighbor quantifies how much functional compensation occurs during recovery, which is positively correlated with model-level accuracy regain; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "33e4e87f-6dfe-45ed-a2c8-a925bfdab378",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CE8ngH2tDmWBZeAfaLL4qX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 22993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 691
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 8 · 2026-05-14T09:07:05.912Z_

<details><summary>↩ Tool result · reported error · `toolu_011p79xegVNByr4QvWrvEPhD`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String: We measure structure-level recoverability using \emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \cos(\mathbf{a}^{\text{pre}}_h, \mathbf{a}^{\text{post}}_h)$, where $\mathbf{a}^{\text{pre}}_h$ and $\mathbf{a}^{\text{post}}_h$ are the hidden states before and after pruning structure $h$.
	This proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\Delta_{\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "c419ca1b-d04b-4128-afdb-184126603cf8",
  "tool_use_result": "Error: String to replace not found in file.\nString: We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\n\tThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure."
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The tab character might be different. Let me read the raw content more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "4e1d24c5-5db0-4c8c-a471-90a6a6e1509f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qh7SNGJP351yDu1Pj5mnfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 23684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01DwmqAytBsDrtPXFHMaPkUd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
  "offset": 64,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "6e72d50c-bdaa-4634-8a50-a9608ac7ebef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qh7SNGJP351yDu1Pj5mnfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 23684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 11 · 2026-05-14T09:07:08.747Z_

<details><summary>↩ Tool result · `toolu_01DwmqAytBsDrtPXFHMaPkUd`</summary>

```text
64	To validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.
65	We measure structure-level recoverability using \emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \cos(\mathbf{a}^{\text{pre}}_h, \mathbf{a}^{\text{post}}_h)$, where $\mathbf{a}^{\text{pre}}_h$ and $\mathbf{a}^{\text{post}}_h$ are the hidden states before and after pruning structure $h$.
66	This proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\Delta_{\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "98570dca-aeb8-444e-8f28-8a5d786f15c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
      "content": "To validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.\nWe measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\nThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
      "numLines": 3,
      "startLine": 64,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fi2n8KPDrE27YThqe2EZes`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
  "old_string": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\nThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
  "new_string": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each pruned structure $g_p$, we identify its most CKA-similar retained structure $g_r$ and compute $1 - \\cos(\\mathbf{a}^{\\text{pruned}}_{g_r}, \\mathbf{a}^{\\text{recovered}}_{g_r})$, measuring the degree to which RLVR redistributes the pruned structure's function to its nearest functional neighbor.\nThis proxy is justified on two grounds: (i)~activation shift on the retained neighbor quantifies how much functional compensation occurs during recovery, which is positively correlated with model-level accuracy regain; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "05e38098-d2f1-4d3f-ad7c-4732cc725427",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01891BpFc2LA8obcYM2kVxHM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 24481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 427
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 13 · 2026-05-14T09:07:14.578Z_

<details><summary>↩ Tool result · `toolu_01Fi2n8KPDrE27YThqe2EZes`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "8a52926c-f588-4544-9741-28f87196b64b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
    "oldString": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\nThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
    "newString": "We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each pruned structure $g_p$, we identify its most CKA-similar retained structure $g_r$ and compute $1 - \\cos(\\mathbf{a}^{\\text{pruned}}_{g_r}, \\mathbf{a}^{\\text{recovered}}_{g_r})$, measuring the degree to which RLVR redistributes the pruned structure's function to its nearest functional neighbor.\nThis proxy is justified on two grounds: (i)~activation shift on the retained neighbor quantifies how much functional compensation occurs during recovery, which is positively correlated with model-level accuracy regain; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
    "originalFile": "\n\\section{Experiments}\n\n\\subsection{Models and Datasets}\n\n\\paragraph{Base Model.}\nWe use DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} as our base model, a 7B-parameter reasoning-distilled model built on the Qwen2.5 architecture~\\citep{qwen2.5} with 28 transformer layers.\nThe model employs Grouped Query Attention (GQA) with 28 query heads and 4 key-value groups per layer (group size $G{=}7$), and an intermediate FFN dimension of 18944.\nThis model represents a compelling testbed for our study: as a reasoning-specialized model, its performance depends critically on chain-of-thought capabilities that are acquired through reinforcement learning, making the interaction between structural pruning and RL-based recovery particularly salient.\n\n\\paragraph{Calibration Data.}\nWe use 512 randomly sampled examples from the GSM8K training set~\\citep{cobbe2021gsm8k} for all calibration-dependent operations, including importance scoring, CKA computation, and GRASPrune gate training.\n\n\\paragraph{Evaluation Benchmarks.}\nOur primary evaluation benchmark is GSM8K~\\citep{cobbe2021gsm8k} (1319 test problems), measuring grade-school mathematical reasoning with exact-match accuracy.\n\\textbf{[Phase 2: We extend evaluation to MMLU~\\citep{hendrycks2021mmlu} for broad knowledge, HumanEval~\\citep{chen2021humaneval} for code generation, and LongBench~\\citep{bai2024longbench} for long-context understanding.]}\n\n\\subsection{Pruning Methods}\n\nWe compare three structured pruning strategies at the granularity of GQA groups (each comprising one KV head and $G{=}7$ query heads) and MLP intermediate channels:\n\n\\paragraph{Standard Importance-Only Pruning.}\nFollowing LLM-Pruner~\\citep{llmpruner2023}, we compute Taylor-expansion-based importance scores $I(h) = \\|w_h \\cdot g_h\\|_2$ for each structural group $h$, where $w_h$ and $g_h$ denote the weight and gradient vectors respectively. Groups are ranked globally by importance and the lowest-scoring groups are removed to meet the target sparsity.\n\n\\paragraph{RASP (Ours).}\nRecovery-Aware Structured Pruning augments the importance score with a functional overlap penalty derived from Centered Kernel Alignment (CKA)~\\citep{kornblith2019cka}.\nThe recovery-aware score (Eq.~\\eqref{eq:score}) is $S(h) = I(h) \\times (1 - F(h))^\\alpha$, where $F(h) \\in [0,1]$ is the CKA-based functional overlap of group $h$ with its neighboring groups, and $\\alpha{=}1.0$ controls the penalty strength.\nIntuitively, groups with high functional overlap ($F(h) \\to 1$) are more likely to be compensated by remaining groups during recovery, so RASP deprioritizes their retention.\nThe scoring and pruning remain one-shot with no iterative optimization.\n\n\\paragraph{GRASPrune.}\nGRASPrune~\\citep{graspprune2026} is a recent post-training structured pruning method that learns differentiable binary gates via a projected straight-through estimator (PSTE) under a global parameter budget constraint.\nIt jointly prunes FFN channels and KV groups with learned gate scores optimized over 4 epochs, followed by a rescale compensation stage that learns multiplicative scaling factors to mitigate pruning-induced distribution shift.\nWe use the official implementation with default hyperparameters.\n\n\\paragraph{Sparsity Levels.}\nOur primary experiments use 35\\% structural sparsity (keep ratio $\\rho{=}0.65$).\nAt this sparsity level, global importance ranking naturally concentrates pruning on MLP groups (attention GQA groups have uniformly higher importance), yielding \\textbf{[TBD]} pruned MLP groups across 28 layers with all attention groups retained.\n\\textbf{[Phase 2: We extend to 25\\% and 45\\% sparsity to study the interaction between pruning aggressiveness and recoverability.]}\n\n\\subsection{Recovery Methods}\n\n\\paragraph{GRPO (Primary).}\nWe use Group Relative Policy Optimization (GRPO)~\\citep{shao2024grpo} as the primary RLVR recovery method.\nGRPO generates $K$ candidate responses per problem and uses the group-relative advantage as the reward signal, avoiding the need for a separate reward model.\nTraining is performed on the GSM8K training set with the following hyperparameters: learning rate \\textbf{[TBD]}, $K{=}$\\textbf{[TBD]} rollouts per prompt, KL coefficient $\\beta{=}$\\textbf{[TBD]}, batch size \\textbf{[TBD]}, trained for \\textbf{[TBD]} steps on 2$\\times$ NVIDIA RTX PRO 6000 (96GB each).\n\n\\textbf{[Phase 2: We additionally compare SFT recovery using the same GSM8K training data to isolate the effect of the RL-based recovery signal.]}\n\n\\subsection{Evaluation Metrics}\n\n\\paragraph{Task Accuracy.}\nWe report exact-match accuracy on GSM8K, extracting the final numerical answer from model generations and comparing against ground truth.\n\n\\paragraph{Recoverability.}\nWe define the recoverability of a pruning configuration as:\n\\begin{equation}\n\\Delta_{\\text{acc}} = \\text{Acc}_{\\text{post-recovery}} - \\text{Acc}_{\\text{post-prune}}\n\\label{eq:recoverability}\n\\end{equation}\nThis measures how much accuracy a pruned model regains through RLVR recovery, capturing the ease of fine-tuning recovery independent of the initial pruning damage.\n\n\\paragraph{Correlation Analysis.}\nTo validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.\nWe measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.\nThis proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.\nA statistically significant positive correlation ($\\rho \\geq 0.4$, $p < 0.01$) supports the claim that RASP's overlap-aware scoring preferentially retains groups whose removal would be hardest to recover from.\n\n\\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}\n",
    "structuredPatch": [
      {
        "oldStart": 62,
        "oldLines": 8,
        "newStart": 62,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Correlation Analysis.}",
          " To validate our core hypothesis that functional overlap predicts recoverability, we compute the Spearman rank correlation $\\rho$ between per-group CKA overlap $F(h)$ and per-group contribution to recoverability.",
          "-We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each structure $h$, we compute $1 - \\cos(\\mathbf{a}^{\\text{pre}}_h, \\mathbf{a}^{\\text{post}}_h)$, where $\\mathbf{a}^{\\text{pre}}_h$ and $\\mathbf{a}^{\\text{post}}_h$ are the hidden states before and after pruning structure $h$.",
          "-This proxy is justified on two grounds: (i)~activation shift quantifies the magnitude of feature disruption caused by removing a given structure, which is positively correlated with model-level accuracy degradation; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
          "+We measure structure-level recoverability using \\emph{activation shift} as a proxy: for each pruned structure $g_p$, we identify its most CKA-similar retained structure $g_r$ and compute $1 - \\cos(\\mathbf{a}^{\\text{pruned}}_{g_r}, \\mathbf{a}^{\\text{recovered}}_{g_r})$, measuring the degree to which RLVR redistributes the pruned structure's function to its nearest functional neighbor.",
          "+This proxy is justified on two grounds: (i)~activation shift on the retained neighbor quantifies how much functional compensation occurs during recovery, which is positively correlated with model-level accuracy regain; and (ii)~unlike direct $\\Delta_{\\text{acc}}$ measurement, activation shift can be computed at individual structure granularity without requiring a full recovery training run for each candidate structure.",
          " A statistically significant positive correlation ($\\rho \\geq 0.4$, $p < 0.01$) supports the claim that RASP's overlap-aware scoring preferentially retains groups whose removal would be hardest to recover from.",
          " ",
          " \\textbf{[Phase 2: We additionally report perplexity on WikiText-2 and per-benchmark accuracy on MMLU, HumanEval, and LongBench.]}"
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

_source line 14_

已修改 `experiments.tex` 第 65-66 行。activation shift proxy 描述现在正确反映了 `correlation_analysis.py` 的实现：对每个被剪结构找到 CKA 最相似的保留结构，测量该保留结构在 RLVR 前后的激活变化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "uuid": "b09c1eb5-4356-49f9-88d1-38383e983cee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrdhLYt9RixxkEgLChG7a7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 24908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 15_

已修改 `experiments.tex` 第 65-66 行。activation shift proxy 描述现在正确反映了 `correlation_analysis.py` 的实现：对每个被剪结构找到 CKA 最相似的保留结构，测量该保留结构在 RLVR 前后的激活变化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 25971,
  "duration_api_ms": 26960,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "d985791e-8163-4017-b101-33591234225b",
  "total_cost_usd": 0.17700575,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 13669,
    "cache_read_input_tokens": 107907,
    "output_tokens": 1460,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 13669,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 94,
        "cache_read_input_tokens": 24908,
        "cache_creation_input_tokens": 602,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 602
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1001,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001086,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 1460,
      "cacheReadInputTokens": 107907,
      "cacheCreationInputTokens": 13669,
      "webSearchRequests": 0,
      "costUSD": 0.17591975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "71d84c6f-5233-42fb-9226-8e2bc09726bd"
}
```

</details>

---
