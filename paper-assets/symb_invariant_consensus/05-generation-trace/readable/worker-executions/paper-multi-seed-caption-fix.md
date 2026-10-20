# paper multi seed caption fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_multi-seed-caption-fix_20260524T123924.log`
- **Structured JSON:** [`d59bfd8db425f7a01ee3.json`](../../sessions/d5/d59bfd8db425f7a01ee3.json)

## Before a recorded user message

38 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
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
  "uuid": "096588e0-0fbc-4386-a40e-b5025539939f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779890400,
    "rateLimitType": "seven_day",
    "utilization": 0.85,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "80ab3505-8e9f-46f8-ad7f-211957ca5311",
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the paper files to find the relevant sections. I need to:
1. Find the appendix tex file with tab:multi-seed
2. Find the discussion section label
3. Search for the relevant numbers (75.98, 77.50, 77.45)

Let me explore the paper directory structure first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "4dbb0f27-4c1c-42de-a415-562a99c93a81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZndDKSPqLbHqBDMD1PVEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12934,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12934
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

_source line 4_

Let me find the paper files and the relevant sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "64ac12cd-7682-423e-a2f6-13dd5102ee0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZndDKSPqLbHqBDMD1PVEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12934,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12934
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

_source line 5_

<details open><summary>🔧 Tool call — Glob · `toolu_01MHYAoiazwBAxm8buoHXuGj`</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "a832d8fe-32c3-4827-806f-796a44bfd0e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZndDKSPqLbHqBDMD1PVEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12934,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12934
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

_source line 6 · 2026-05-24T12:57:41.526Z_

<details><summary>↩ Tool result · `toolu_01MHYAoiazwBAxm8buoHXuGj`</summary>

```text
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/limitations_content.tex
docs/paper/introduction.tex
docs/paper/solutions.tex
docs/paper/diagnosis.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/abstract.tex
docs/paper/analysis.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "6aec50be-f056-42eb-83a1-b9fe78568ad1",
  "tool_use_result": {
    "filenames": [
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/limitations_content.tex",
      "docs/paper/introduction.tex",
      "docs/paper/solutions.tex",
      "docs/paper/diagnosis.tex",
      "docs/paper/experiments.tex",
      "docs/paper/discussion.tex",
      "docs/paper/abstract.tex",
      "docs/paper/analysis.tex",
      "docs/paper/appendix.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 33,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Grep · `toolu_0146xzwXyqp88sHFqQpRZYHh`</summary>

```json
{
  "pattern": "multi-seed|tab:multi.seed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "38e48282-26ed-41a2-bb31-df98ee12c0fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZndDKSPqLbHqBDMD1PVEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12934,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12934
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

_source line 8 · 2026-05-24T12:57:42.969Z_

<details><summary>↩ Tool result · `toolu_0146xzwXyqp88sHFqQpRZYHh`</summary>

```text
docs/paper/experiments.tex:5:[Omitted long matching line]
docs/paper/experiments.tex:10:[Omitted long matching line]
docs/paper/experiments.tex:52:[Omitted long matching line]
docs/paper/appendix.tex:1402:\label{app:multi-seed}
docs/paper/appendix.tex:1408:\label{tab:multi-seed}
docs/paper/introduction.tex:7:[Omitted long matching line]
docs/paper/main.aux:475:[Omitted long matching line]
docs/paper/main.aux:476:[Omitted long matching line]
docs/paper/main.aux:2399:\newlabel{app:multi-seed}{{X}{25}{Multi-seed replication}{section*.112}{}}
docs/paper/main.aux:2400:\newlabel{app:multi-seed@cref}{{[section][24][]X}{[1][25][]25}{}{}{}}
docs/paper/main.aux:2722:\newlabel{tab:multi-seed}{{42}{29}{Multi-seed replication results across six model$\times $dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\times $FOLIO shows directionally unstable $\Delta $ ($+0.16 \pm 2.70$\,pp); three of four ProofWriter conditions show consistently negative $\Delta $ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\,pp)}{table.caption.113}{}}
docs/paper/main.aux:2723:\newlabel{tab:multi-seed@cref}{{[table][42][]42}{[1][25][]29}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "c1286a88-b691-47e4-b0e0-2ab18f6b4628",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:5:[Omitted long matching line]\ndocs/paper/experiments.tex:10:[Omitted long matching line]\ndocs/paper/experiments.tex:52:[Omitted long matching line]\ndocs/paper/appendix.tex:1402:\\label{app:multi-seed}\ndocs/paper/appendix.tex:1408:\\label{tab:multi-seed}\ndocs/paper/introduction.tex:7:[Omitted long matching line]\ndocs/paper/main.aux:475:[Omitted long matching line]\ndocs/paper/main.aux:476:[Omitted long matching line]\ndocs/paper/main.aux:2399:\\newlabel{app:multi-seed}{{X}{25}{Multi-seed replication}{section*.112}{}}\ndocs/paper/main.aux:2400:\\newlabel{app:multi-seed@cref}{{[section][24][]X}{[1][25][]25}{}{}{}}\ndocs/paper/main.aux:2722:\\newlabel{tab:multi-seed}{{42}{29}{Multi-seed replication results across six model$\\times $dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times $FOLIO shows directionally unstable $\\Delta $ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta $ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp)}{table.caption.113}{}}\ndocs/paper/main.aux:2723:\\newlabel{tab:multi-seed@cref}{{[table][42][]42}{[1][25][]29}{}{}{}}",
    "numLines": 12
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_011916pjekf6FhrwtcvwVfQB`</summary>

```json
{
  "pattern": "75\\.98|77\\.50|77\\.45",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "0663cd27-bc70-4911-bbb0-4c2b71993ce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZndDKSPqLbHqBDMD1PVEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12934,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12934
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

_source line 10 · 2026-05-24T12:57:43.561Z_

<details><summary>↩ Tool result · `toolu_011916pjekf6FhrwtcvwVfQB`</summary>

```text
docs/paper/experiments.tex:33:Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
docs/paper/diagnosis.tex:30:Qwen2.5-14B & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000 \\
docs/paper/diagnosis.tex:31:Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
docs/paper/diagnosis.tex:41:Qwen2.5-14B & FOLIO & 204 & 75.98 & \textbf{89.71} & $\mathbf{+13.73}$ & $2.0{\times}10^{-7}${***} \\
docs/paper/diagnosis.tex:70:Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\
docs/paper/diagnosis.tex:71:Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
docs/paper/diagnosis.tex:157:Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
docs/paper/diagnosis.tex:158:Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\
docs/paper/main.aux:1762:\@writefile{lot}{\contentsline {table}{\numberline {11}{\ignorespaces Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\%$, $\Delta = -0.49$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref {tab:method_interventions}.}}{17}{table.caption.50}\protected@file@percent }
docs/paper/main.aux:1763:\newlabel{tab:remediation}{{11}{17}{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\%$, $\Delta = -0.49$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref {tab:method_interventions}}{table.caption.50}{}}
docs/paper/figures/gen_f2_regime_scatter_v2.py:63:    ('Qwen2.5',      'Q7B FOLIO',         204, 75.98,  0.49, 1.000),
docs/paper/figures/gen_f6_kappa_accuracy_scatter.py:33:x_acc    = [66.18,      75.98,     75.98]
docs/paper/appendix.tex:442:\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\%$, $\Delta = -0.49$\,pp. None reaches significance. Three method-level strategies are reported in Table~\ref{tab:method_interventions}.}
docs/paper/appendix.tex:643:Qwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\
docs/paper/appendix.tex:713:Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\
docs/paper/appendix.tex:714:Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\
docs/paper/appendix.tex:737:Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\
docs/paper/appendix.tex:738:Qwen2.5-7B & FOLIO & 0.66$^{\dag}$ & 1.46 & 75.98 & $+$0.49 \\
docs/paper/appendix.tex:768:Qwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\
docs/paper/appendix.tex:769:Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\
docs/paper/appendix.tex:1084:\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\
docs/paper/appendix.tex:1112:\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\
docs/paper/appendix.tex:1140:\multirow{3}{*}{Qwen2.5-14B} & 1 & \multirow{3}{*}{75.98} & 75.98 & $\pm$0.00 & n.s. \\
docs/paper/appendix.tex:1201: & 5 & & 77.50 & $-$1.50 & n.s. \\
docs/paper/appendix.tex:1229: & 5 & & 77.50 & $-$1.50 & n.s. \\
docs/paper/appendix.tex:1319:  & \multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\
docs/paper/appendix.tex:1320:  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\
docs/paper/appendix.tex:1321:  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\
docs/paper/appendix.tex:1422:42 & 77.50 & 75.49 & $-$2.01 \\
docs/paper/figures/gen_f6_kappa_accuracy_scatter_v2.py:49:x_acc     = [66.18,       75.98,     75.98]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "f7e22b58-301d-46fa-8d34-72a923082eac",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:33:Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\ndocs/paper/diagnosis.tex:30:Qwen2.5-14B & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000 \\\\\ndocs/paper/diagnosis.tex:31:Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\ndocs/paper/diagnosis.tex:41:Qwen2.5-14B & FOLIO & 204 & 75.98 & \\textbf{89.71} & $\\mathbf{+13.73}$ & $2.0{\\times}10^{-7}${***} \\\\\ndocs/paper/diagnosis.tex:70:Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\ndocs/paper/diagnosis.tex:71:Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\ndocs/paper/diagnosis.tex:157:Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\ndocs/paper/diagnosis.tex:158:Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\ndocs/paper/main.aux:1762:\\@writefile{lot}{\\contentsline {table}{\\numberline {11}{\\ignorespaces Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref {tab:method_interventions}.}}{17}{table.caption.50}\\protected@file@percent }\ndocs/paper/main.aux:1763:\\newlabel{tab:remediation}{{11}{17}{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref {tab:method_interventions}}{table.caption.50}{}}\ndocs/paper/figures/gen_f2_regime_scatter_v2.py:63:    ('Qwen2.5',      'Q7B FOLIO',         204, 75.98,  0.49, 1.000),\ndocs/paper/figures/gen_f6_kappa_accuracy_scatter.py:33:x_acc    = [66.18,      75.98,     75.98]\ndocs/paper/appendix.tex:442:\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\ndocs/paper/appendix.tex:643:Qwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\\\\ndocs/paper/appendix.tex:713:Qwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\ndocs/paper/appendix.tex:714:Qwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\ndocs/paper/appendix.tex:737:Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\ndocs/paper/appendix.tex:738:Qwen2.5-7B & FOLIO & 0.66$^{\\dag}$ & 1.46 & 75.98 & $+$0.49 \\\\\ndocs/paper/appendix.tex:768:Qwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\ndocs/paper/appendix.tex:769:Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\ndocs/paper/appendix.tex:1084:\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\ndocs/paper/appendix.tex:1112:\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\ndocs/paper/appendix.tex:1140:\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\ndocs/paper/appendix.tex:1201: & 5 & & 77.50 & $-$1.50 & n.s. \\\\\ndocs/paper/appendix.tex:1229: & 5 & & 77.50 & $-$1.50 & n.s. \\\\\ndocs/paper/appendix.tex:1319:  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\ndocs/paper/appendix.tex:1320:  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\ndocs/paper/appendix.tex:1321:  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\ndocs/paper/appendix.tex:1422:42 & 77.50 & 75.49 & $-$2.01 \\\\\ndocs/paper/figures/gen_f6_kappa_accuracy_scatter_v2.py:49:x_acc     = [66.18,       75.98,     75.98]",
    "numLines": 30
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
I found the key issue. In `diagnosis.tex:30`, Qwen2.5-14B FOLIO SC is listed as 75.98, but according to the task, the correct value for Qwen2.5-14B is 77.50 (or 77.45), and 75.98 is for Qwen2.5-7B.

Wait, let me re-read the task more carefully. The task says:
- exp-multi-seed-qwen25 folio_seed42: SC = 77.50% ✓
- 75.98% is Qwen2.5-7B FOLIO's value (from exp-061), not 14B


Looking at the grep results, I'm seeing 75.98 appear for both model sizes across different files, which suggests there might be a copy-paste error where the 7B value got used for the 14B model as well. The main results table in `experiments.tex:33` shows Qwen2.5-7B with 75.98, but `diagnosis.tex:30` incorrectly uses the same value for Qwen2.5-14B.

However, the registry note mentions that Qwen2.5-14B with seed42 should be 77.50%, and I can see this value does appear in the multi-seed table at `appendix.tex:1422`. So the 75.98 values in the main tables are likely from a different experimental setup or seed, while the multi-seed table has the correct 77.50 for seed42. I need to examine the actual files to understand which values belong where.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "77058a8f-a5e8-44b1-82db-b41ab7b46690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEFzrP8dma2UpavJhiqMmD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 24775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2852
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_013uaA44vtoarNBM31gFxS9w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 1395,
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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "eb1aa9cd-c307-4f4a-89cc-a32095920267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEFzrP8dma2UpavJhiqMmD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 24775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2852
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

_source line 13 · 2026-05-24T12:58:03.038Z_

<details><summary>↩ Tool result · `toolu_013uaA44vtoarNBM31gFxS9w`</summary>

```text
1395	\bottomrule
1396	\end{tabular}
1397	\end{table}
1398	
1399	Controlling for the trace set (excluding $T_{\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\Delta \leq +1.47$\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.
1400	
1401	\paragraph{Multi-seed replication.}
1402	\label{app:multi-seed}
1403	
1404	\begin{table}[h]
1405	\centering
1406	\small
1407	\caption{Multi-seed replication results across six model$\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\times$FOLIO shows directionally unstable $\Delta$ ($+0.16 \pm 2.70$\,pp); three of four ProofWriter conditions show consistently negative $\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\,pp).}
1408	\label{tab:multi-seed}
1409	\resizebox{\columnwidth}{!}{%
1410	\begin{tabular}{@{}lrrrr@{}}
1411	\toprule
1412	Seed & SC (\%) & SICA (\%) & $\Delta$ (pp) \\
1413	\midrule
1414	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ FOLIO ($n{=}204$)\textsuperscript{a}}} \\
1415	123 & 54.41 & 57.35 & $+$2.94 \\
1416	456 & 55.88 & 55.88 & 0.00 \\
1417	789 & 59.31 & 56.86 & $-$2.45 \\
1418	\midrule
1419	Mean $\pm$ SD & 56.53 $\pm$ 2.51 & 56.70 $\pm$ 0.75 & $+$0.16 $\pm$ 2.70 \\
1420	\midrule
1421	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ FOLIO ($n{=}204$)}} \\
1422	42 & 77.50 & 75.49 & $-$2.01 \\
1423	123 & 74.51 & 73.04 & $-$1.47 \\
1424	456 & 74.02 & 74.02 & 0.00 \\
1425	789 & 74.02 & 72.55 & $-$1.47 \\
1426	\midrule
1427	Mean $\pm$ SD & 75.01 $\pm$ 1.67 & 73.78 $\pm$ 1.30 & $-$1.24 $\pm$ 0.86 \\
1428	\midrule
1429	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ ProofWriter ($n{=}600$)}} \\
1430	42  & 39.33 & 36.50 & $-$2.83 \\
1431	123 & 40.83 & 37.50 & $-$3.33 \\
1432	456 & 39.83 & 38.50 & $-$1.33 \\
1433	789 & 38.83 & 37.17 & $-$1.67 \\
1434	\midrule
1435	Mean $\pm$ SD & 39.70 $\pm$ 0.85 & 37.42 $\pm$ 0.83 & $-$2.29 $\pm$ 0.95 \\
1436	\midrule
1437	\multicolumn{4}{@{}l}{\textit{LLaMA-3.1-8B $\times$ ProofWriter ($n{=}600$)}} \\
1438	42  & 72.50 & 65.00 & $-$7.50 \\
1439	123 & 71.33 & 64.00 & $-$7.33 \\
1440	456 & 71.67 & 66.17 & $-$5.50 \\
1441	789 & 71.17 & 66.50 & $-$4.67 \\
1442	\midrule
1443	Mean $\pm$ SD & 71.67 $\pm$ 0.59 & 65.42 $\pm$ 1.14 & $-$6.25 $\pm$ 1.34 \\
1444	\midrule
1445	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ ProofWriter ($n{=}600$)}} \\
1446	42  & 74.00 & 71.50 & $-$2.50 \\
1447	123 & 72.33 & 70.83 & $-$1.50 \\
1448	456 & 73.00 & 72.17 & $-$0.83 \\
1449	789 & 73.50 & 71.50 & $-$2.00 \\
1450	\midrule
1451	Mean $\pm$ SD & 73.21 $\pm$ 0.71 & 71.50 $\pm$ 0.55 & $-$1.71 $\pm$ 0.71 \\
1452	\midrule
1453	\multicolumn{4}{@{}l}{\textit{Qwen3-14B $\times$ ProofWriter ($n{=}600$)}} \\
1454	42  & 85.83 & 85.67 & $-$0.17 \\
1455	123 & 85.17 & 86.50 & $+$1.33 \\
1456	456 & 84.50 & 86.83 & $+$2.33 \\
1457	789 & 85.50 & 85.67 & $+$0.17 \\
1458	\midrule
1459	Mean $\pm$ SD & 85.25 $\pm$ 0.57 & 86.17 $\pm$ 0.59 & $+$0.92 $\pm$ 1.14 \\
1460	\bottomrule
1461	\end{tabular}}
1462	\vspace{2pt}
1463	{\footnotesize \textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}
1464	\end{table}
1465	
1466	On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\Delta$ (range $-0.83$ to $-7.50$\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\Delta$ is positive ($+0.92 \pm 1.14$\,pp), revealing a capability-dependent gradient: LLaMA-8B $\Delta{=}-6.25$ $\to$ Mistral-7B $\Delta{=}-2.29$ $\to$ Qwen2.5-14B $\Delta{=}-1.63$ $\to$ Qwen3-14B $\Delta{=}+0.92$\,pp. The consistency across seeds confirms that the sign of $\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.
1467	
1468	\subsection{Sub-population Analysis}
1469	\label{app:subpopulation}
1470	
1471	\begin{table}[h]
1472	\centering
1473	\small
1474	\caption{SICA vs.\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\Delta$\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}
1475	\label{tab:subpop-answer-type}
1476	\resizebox{\columnwidth}{!}{%
1477	\begin{tabular}{ll rrr rr}
1478	\toprule
1479	\textbf{Dataset} & \textbf{Label} & $n$ & \textbf{SC} & \textbf{SICA} & $\Delta$\,pp & $p$ \\
1480	\midrule
1481	\multirow{4}{*}{FOLIO-204}
1482	 & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\
1483	 & False   &  63 & 42.9 & 42.9 & $\pm$0.0 & 1.0\hphantom{00} \\
1484	 & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\
1485	 & \textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\
1486	\midrule
1487	\multirow{4}{*}{PW-600}
1488	 & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\
1489	 & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\
1490	 & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\
1491	 & \textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\rlap{*} \\
1492	\bottomrule
1493	\end{tabular}}
1494	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "5c52b5b0-1c77-47a4-be17-b4dd5abd2719",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp).}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 74.00 & 71.50 & $-$2.50 \\\\\n123 & 72.33 & 70.83 & $-$1.50 \\\\\n456 & 73.00 & 72.17 & $-$0.83 \\\\\n789 & 73.50 & 71.50 & $-$2.00 \\\\\n\\midrule\nMean $\\pm$ SD & 73.21 $\\pm$ 0.71 & 71.50 $\\pm$ 0.55 & $-$1.71 $\\pm$ 0.71 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen3-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 85.83 & 85.67 & $-$0.17 \\\\\n123 & 85.17 & 86.50 & $+$1.33 \\\\\n456 & 84.50 & 86.83 & $+$2.33 \\\\\n789 & 85.50 & 85.67 & $+$0.17 \\\\\n\\midrule\nMean $\\pm$ SD & 85.25 $\\pm$ 0.57 & 86.17 $\\pm$ 0.59 & $+$0.92 $\\pm$ 1.14 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
      "numLines": 100,
      "startLine": 1395,
      "totalLines": 1591
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_016inLhDvfdx5Vhj56mKKZw2`</summary>

```json
{
  "pattern": "\\\\label\\{sec:discussion\\}|\\\\label\\{sec:disc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "71faba95-bfb3-4239-baa0-c83b66e9e3b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEFzrP8dma2UpavJhiqMmD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2852,
      "cache_read_input_tokens": 24775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2852
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

_source line 15 · 2026-05-24T12:58:04.221Z_

<details><summary>↩ Tool result · `toolu_016inLhDvfdx5Vhj56mKKZw2`</summary>

```text
docs/paper/discussion.tex:2:\label{sec:discussion}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "930484eb-4074-49cb-ada5-ef1da20319c1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:2:\\label{sec:discussion}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me understand what needs to be done:

1. **Caption (L1407)**: The current caption says "three of four ProofWriter conditions show consistently negative $\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\,pp)." This already mentions Qwen3-14B but doesn't explicitly describe the Qwen3 pattern with the negligible mixed-sign and SC baseline info as requested.

The task asks to change the caption to something like: "Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative Δ on ProofWriter; Qwen3-14B shows negligible mixed-sign Δ ($+0.92 \pm 1.14$\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (§

\ref{sec:discussion})"

2. **Analysis paragraph (L1466)**: Need to add a sentence about Qwen3 being the exception reflecting the capability-modulated pattern. The current text already mentions Qwen3 somewhat but doesn't explicitly tie to the discussion section.

3. **Data verification**: I'm checking whether 75.98 is incorrectly used for Qwen2.5-14B anywhere. Looking at the grep results, I can see Qwen2.5-14B appears in the FOLIO dataset with an SC baseline of 75.98, which matches the expected value, so there's no data error to correct there. I'm noticing both the 7B and 14B models show 75.98 in the main experiments table, which seems odd. Let me trace through the experiments.tex file to verify whether these are actually the same value or if there's a discrepancy between the model sizes. 7B value, not 14B. I need to locate tab:independence in the appendix or diagnosis files and cross-reference the tables there to verify which model and seed configuration produced that 75.98% score.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "2e82f939-fe99-4586-9762-df5ec1c59c1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxbR9B5DDSU2HZTP1yLaC9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3657,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3657
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01CEjwrR5HGh2rVTbJR6mbsY`</summary>

```json
{
  "pattern": "tab:independence",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper",
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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "97e3ee7e-5539-4003-ba79-0ce87113b7b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxbR9B5DDSU2HZTP1yLaC9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3657,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3657
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

_source line 18 · 2026-05-24T12:58:32.465Z_

<details><summary>↩ Tool result · `toolu_01CEjwrR5HGh2rVTbJR6mbsY`</summary>

```text
docs/paper/experiments.tex:50:[Omitted long matching line]
docs/paper/diagnosis.tex:51:[Omitted long matching line]
docs/paper/diagnosis.tex:61:\label{tab:independence}
docs/paper/appendix.tex:722:Table~\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\kappa$ and Effective-K at $K = 12$, referenced in \S\ref{sec:effective-k}.
docs/paper/appendix.tex:729:\label{tab:independence}
docs/paper/main.aux:2031:[Omitted long matching line]
docs/paper/main.aux:2032:\newlabel{tab:independence@cref}{{[table][19][]19}{[1][20][]20}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "71721300-5a7b-4db2-9308-56ac0be5b0dd",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experiments.tex:50:[Omitted long matching line]\ndocs/paper/diagnosis.tex:51:[Omitted long matching line]\ndocs/paper/diagnosis.tex:61:\\label{tab:independence}\ndocs/paper/appendix.tex:722:Table~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\ndocs/paper/appendix.tex:729:\\label{tab:independence}\ndocs/paper/main.aux:2031:[Omitted long matching line]\ndocs/paper/main.aux:2032:\\newlabel{tab:independence@cref}{{[table][19][]19}{[1][20][]20}{}{}{}}",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_016JKXYMeGB8BQixBgdUeqXq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex",
  "offset": 25,
  "limit": 55
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "9007fb11-7daa-44c3-9c90-4390978d21c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxbR9B5DDSU2HZTP1yLaC9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3657,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3657
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

_source line 20 · 2026-05-24T12:58:33.381Z_

<details><summary>↩ Tool result · `toolu_016JKXYMeGB8BQixBgdUeqXq`</summary>

```text
25	\multicolumn{7}{l}{\textit{Type A: confirmation bias (SC $\geq$ 60\%)}} \\
26	LLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\
27	LLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\
28	Qwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\
29	Qwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\mathbf{-2.50}$ & 0.011{*} \\
30	Qwen2.5-14B & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000 \\
31	Qwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\
32	Qwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\
33	Qwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\
34	Qwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
35	\midrule
36	\multicolumn{7}{l}{\textit{Degenerate ($C_0 < 5\%$)}} \\
37	QwQ-32B & AIME 2024$^\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \textrm{---} \\
38	Qwen2.5-14B & GSM8K$^\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \textrm{---} \\
39	\midrule
40	\multicolumn{7}{l}{\textit{Oracle upper bound (gold logical annotations + Z3)}} \\
41	Qwen2.5-14B & FOLIO & 204 & 75.98 & \textbf{89.71} & $\mathbf{+13.73}$ & $2.0{\times}10^{-7}${***} \\
42	Qwen2.5-14B & ProofWriter & 600 & 74.00 & \textbf{91.17} & $\mathbf{+17.17}$ & $9.21{\times}10^{-15}${***} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\subsection{Symbolic Confirmation Bias}
48	\label{sec:confirmation-bias}
49	\label{sec:effective-k}
50	
51	Table~\ref{tab:independence} reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 16 conditions at $K = 12$. Among non-thinking instruction-tuned models, $\kappa$ ranges from 0.19 to 0.82 ($K_{\text{eff}} = 1.20\text{--}3.94$); thinking-mode Qwen3 reaches $\kappa = 0.91$ ($K_{\text{eff}} = 1.09$). Two conditions are jointly necessary for any positive trend: sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\text{eff}} = 3.94$ with SC $= 39\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
52	
53	This correlation manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\times$ compared to correct problems. Consequently, 94\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.
54	
55	The causal chain is: the model generates an answer, then extracts logical constraints consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\times$ (Mistral-7B), $3.85\times$ (Qwen2.5-14B), and $2.88{\times}^{\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\dag}$based on 4/12 traces due to extraction failures; Table~\ref{tab:cross-model-bias}). The oracle ceiling (\S\ref{sec:oracle}) confirms that 75.9\% of the potential gain is lost to self-extraction quality.
56	
57	\begin{table}[t]
58	\centering
59	\small
60	\caption{Trace independence metrics ($K = 12$, sorted by $\kappa$ descending). $\kappa$: Fleiss' Kappa. $K_{\text{eff}}$: Effective-K (Eq.~\ref{eq:effk}). SC: Self-Consistency baseline. $\Delta$: SICA $-$ SC (pp). {*}\,$p < 0.05$; positive $\Delta$ values do not reach significance. multi-T $= T \in \{0.3, 0.7, 1.2\}$, 4 traces each.}
61	\label{tab:independence}
62	\begin{tabular}{@{}llccrr@{}}
63	\toprule
64	Model & Condition & $\kappa$ & $K_{\text{eff}}$ & SC (\%) & $\Delta$ (pp) \\
65	\midrule
66	Qwen3 (think) & FOLIO & 0.91 & 1.09 & ${\sim}$84 & ${\sim}$0 \\
67	Qwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\
68	Qwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\
69	Qwen3 & PW-D5 & 0.78 & 1.25 & 85.83 & $-$0.17 \\
70	Qwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\
71	Qwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\
72	\addlinespace
73	Mistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\
74	Mistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\
75	Mistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\
76	Mistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\
77	Mistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\
78	Mistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\
79	Mistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "4ed4b286-c1ca-4553-bc96-ac00c2cc1124",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex",
      "content": "\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.98 & 75.49 & $-$0.49 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Degenerate ($C_0 < 5\\%$)}} \\\\\nQwQ-32B & AIME 2024$^\\dagger$ & 22 & 72.70 & 72.70 & 0.00 & \\textrm{---} \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 30 & 96.67 & 96.67 & 0.00 & \\textrm{---} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Oracle upper bound (gold logical annotations + Z3)}} \\\\\nQwen2.5-14B & FOLIO & 204 & 75.98 & \\textbf{89.71} & $\\mathbf{+13.73}$ & $2.0{\\times}10^{-7}${***} \\\\\nQwen2.5-14B & ProofWriter & 600 & 74.00 & \\textbf{91.17} & $\\mathbf{+17.17}$ & $9.21{\\times}10^{-15}${***} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Symbolic Confirmation Bias}\n\\label{sec:confirmation-bias}\n\\label{sec:effective-k}\n\nTable~\\ref{tab:independence} reports Fleiss' $\\kappa$ and Effective-K (Eq.~\\ref{eq:effk}) across 16 conditions at $K = 12$. Among non-thinking instruction-tuned models, $\\kappa$ ranges from 0.19 to 0.82 ($K_{\\text{eff}} = 1.20\\text{--}3.94$); thinking-mode Qwen3 reaches $\\kappa = 0.91$ ($K_{\\text{eff}} = 1.09$). Two conditions are jointly necessary for any positive trend: sufficient $K_{\\text{eff}}$ ($\\leq 1.30$ never improves) and sufficient SC accuracy ($K_{\\text{eff}} = 3.94$ with SC $= 39\\%$ produces significant degradation). Cross-model validation confirms universality: all four families produce $\\kappa \\geq 0.41$ (Table~\\ref{tab:kappa_generalization}).\n\nThis correlation manifests through a specific mechanism: self-extracted constraints systematically confirm the model's majority answer regardless of correctness. On Mistral-7B FOLIO ($n = 204$), when SICA errs, 83.3\\% of extracted constraints support the incorrect majority answer---a bias ratio of $4.97\\times$ compared to correct problems. Consequently, 94\\% of SICA errors overlap with SC errors: symbolic aggregation adds no independent corrective signal.\n\nThe causal chain is: the model generates an answer, then extracts logical constraints consistent with it. Constraints from majority-answer traces use trace-specific variable names (56.4\\% of cross-answer pairs share zero Z3 variables), so MAX-SAT retains nearly all, and aggregation reduces to a weighted majority vote (Eq.~\\ref{eq:degenerate}). Confirmation bias generalizes across model families: bias ratios of $4.97\\times$ (Mistral-7B), $3.85\\times$ (Qwen2.5-14B), and $2.88{\\times}^{\\dag}$ (LLaMA-3.1-8B) all significantly exceed $1.0$ ($^{\\dag}$based on 4/12 traces due to extraction failures; Table~\\ref{tab:cross-model-bias}). The oracle ceiling (\\S\\ref{sec:oracle}) confirms that 75.9\\% of the potential gain is lost to self-extraction quality.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$; positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91 & 1.09 & ${\\sim}$84 & ${\\sim}$0 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\\\\nQwen3 & PW-D5 & 0.78 & 1.25 & 85.83 & $-$0.17 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53 & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52 & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48 & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\\\\nMistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\\\",
      "numLines": 55,
      "startLine": 25,
      "totalLines": 162
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01KwhVgP9aGKeNPhzwKCLfk8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
  "offset": 1,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "ee681806-ef5e-4776-b5be-6e177688acd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxbR9B5DDSU2HZTP1yLaC9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3657,
      "cache_read_input_tokens": 27627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3657
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

_source line 22 · 2026-05-24T12:58:34.190Z_

<details><summary>↩ Tool result · `toolu_01KwhVgP9aGKeNPhzwKCLfk8`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$, adj.\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$, adj.\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal (representative cases in Appendix~\ref{app:case-studies}).
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,BH adj.\ $p = 0.042$; $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate; $^\dagger$\,4-seed replication in Table~\ref{tab:multi-seed} (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\Delta = 0$ and are reported separately in Appendix~\ref{app:oracle}.}
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
37	Qwen3-14B$^\dagger$ & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\
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
50	\looseness=-1 Figure~\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\kappa$ ranges from 0.19 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.94$ at $K = 12$ (Table~\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\leq 40\%$), where low accuracy causes error amplification; an intermediate band (50--60\%), containing the only positive trends; and Type~A (SC $\geq 60\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\Delta$ ranges from $+2.94$ to $-2.45$\,pp despite $\kappa \in [0.45, 0.46]$. We trace the mechanism in \S\ref{sec:analysis}.
51	
52	\looseness=-1 TOST equivalence tests \citep{lakens2017equivalence} with pre-specified margin $\pm 2$\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\sim}2$\,pp (MDE 1.86--4.84\,pp; sensitivity analysis in Appendix~\ref{app:power},~\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\Delta = +0.16 \pm 2.70$\,pp across three Mistral-7B seeds (Table~\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\Delta \in [0.00, -2.01]$\,pp; four Qwen3-14B seeds yield mean $\Delta = +0.92 \pm 1.14$\,pp (n.s.). Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\sim}$12\% of this ceiling (Appendix~\ref{app:oracle}).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "2bfb97fc-b545-4127-803e-9c17a0c83335",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\\label{sec:main-results}\n\n\\looseness=-1 Table~\\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. Two confirmatory conditions show significant degradation after BH FDR control ($m{=}6$; multi-seed aggregates and extensions are exploratory): Mistral-7B on ProofWriter ($-2.83$\\,pp, raw $p = 0.014$, adj.\\ $p = 0.042$) and Qwen2.5-14B on ProofWriter ($-2.50$\\,pp, raw $p = 0.011$, adj.\\ $p = 0.042$). No condition shows a significant positive effect. An aggregate sign test yields 8 positive and 7 negative $\\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\\times$ more often (139 vs.\\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal (representative cases in Appendix~\\ref{app:case-studies}).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC across all non-degenerate self-extraction conditions (sorted by SC). Two conditions show significant degradation after BH correction ($m{=}6$ confirmatory; remaining exploratory); no condition shows a significant gain. $\\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \\textbf{bold}: $p < 0.05$; {*}\\,BH adj.\\ $p = 0.042$; $^{3s}$\\,3-seed aggregate; $^{4s}$\\,4-seed confirmatory aggregate; $^\\dagger$\\,4-seed replication in Table~\\ref{tab:multi-seed} (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\\%$ for $|\\Delta| = 2$\\,pp (Appendix~\\ref{app:power}). Degenerate conditions ($C_0 < 5\\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$) yield $\\Delta = 0$ and are reported separately in Appendix~\\ref{app:oracle}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Domain & $n$ & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type C: error amplification (SC $\\leq$ 40\\%)}} \\\\\nMistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\\mathbf{-2.83}$ & 0.014{*} \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Intermediate SC (SC $\\sim$50--60\\%, Mistral-7B only)}} \\\\\nMistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\\\\nMistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\\\\nMistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\\\\nMistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\\\\nMistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Type A: confirmation bias (SC $\\geq$ 60\\%)}} \\\\\nLLaMA-3.1-8B & FOLIO & 204 & 66.18 & 61.76 & $-$4.41 & 0.093 \\\\\nLLaMA-3.1-8B & StrategyQA & 200 & 72.00 & 74.00 & $+$2.00 & 0.424 \\\\\n\\addlinespace\nQwen2.5-14B & FOLIO (ICL)$^b$ & 199 & 74.37 & 74.87 & $+$0.50 & 1.000 \\\\\nQwen2.5-14B & PW-D5 & 600 & 74.00 & 71.50 & $\\mathbf{-2.50}$ & 0.011{*} \\\\\nQwen2.5-14B$^{4s}$ & FOLIO & 204 & 75.01 & 73.78 & $-$1.24 & 1.000 \\\\\nQwen2.5-7B & FOLIO & 204 & 75.98 & 76.47 & $+$0.49 & 1.000 \\\\\nQwen2.5-14B & LogiQA & 200 & 79.00 & 78.00 & $-$1.00 & 0.625 \\\\\n\\addlinespace\nQwen3-14B & FOLIO & 204 & 83.33 & 84.80 & $+$1.47 & 1.000 \\\\\nQwen3-14B$^\\dagger$ & PW-D5 & 600 & 85.83 & 85.67 & $-$0.17 & 1.000 \\\\\nQwen3-14B (think) & FOLIO & 204 & 86.27 & 86.76 & $+$0.49 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{f2_regime_scatter}\n\\caption{SICA $\\Delta$ (pp) vs.\\ SC baseline. Filled: $n \\geq 100$; open: $n < 100$. The intermediate-SC region (50--60\\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\\ $p = 0.042$).}\n\\label{fig:regime-scatter}\n\\end{figure}\n\n\\looseness=-1 Figure~\\ref{fig:regime-scatter} reveals regime structure. Fleiss' $\\kappa$ ranges from 0.19 to 0.82, yielding $K_{\\text{eff}} = 1.20\\text{--}3.94$ at $K = 12$ (Table~\\ref{tab:independence}, Appendix). Three regimes emerge: Type~C (SC $\\leq 40\\%$), where low accuracy causes error amplification; an intermediate band (50--60\\%), containing the only positive trends; and Type~A (SC $\\geq 60\\%$), where symbolic confirmation bias dominates. Seed-level noise is substantial: across three Mistral-7B seeds, $\\Delta$ ranges from $+2.94$ to $-2.45$\\,pp despite $\\kappa \\in [0.45, 0.46]$. We trace the mechanism in \\S\\ref{sec:analysis}.\n\n\\looseness=-1 TOST equivalence tests \\citep{lakens2017equivalence} with pre-specified margin $\\pm 2$\\,pp confirm four conditions as equivalent; ten remain underpowered for effects below ${\\sim}2$\\,pp (MDE 1.86--4.84\\,pp; sensitivity analysis in Appendix~\\ref{app:power},~\\ref{app:tost}). Absence of evidence is not evidence of absence for small effects. Multi-seed replication confirms robustness: mean $\\Delta = +0.16 \\pm 2.70$\\,pp across three Mistral-7B seeds (Table~\\ref{tab:multi-seed}); four Qwen2.5-14B seeds yield $\\Delta \\in [0.00, -2.01]$\\,pp; four Qwen3-14B seeds yield mean $\\Delta = +0.92 \\pm 1.14$\\,pp (n.s.). Oracle controls with gold annotations confirm the MAX-SAT mechanism is sound ($+29.90$/$+13.73$\\,pp FOLIO, $+17.17$\\,pp ProofWriter; $p < 0.001$), yet self-extraction captures only ${\\sim}$12\\% of this ceiling (Appendix~\\ref{app:oracle}).\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me analyze:

1. **Caption (L1407)**: Current caption says "three of four ProofWriter conditions show consistently negative $\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\,pp)." The task wants it to explicitly mention all three negative models and add detail about Qwen3's pattern.

2. **Analysis paragraph (L1466)**: Current text already mentions Qwen3-14B but doesn't explicitly reference §discussion. Need to add the capability-modulated reference.
   
3. **Data verification**: I'm checking the experimental results table to confirm the aggregate scores and individual model performance across FOLIO, particularly verifying the Qwen2.5 variants and their self-consistency values.

Now I'm noticing a discrepancy—the diagnosis table shows Qwen2.5-14B FOLIO with SC=75.98, but when I look at the multi-seed breakdown (seed42=77.50, seed123=74.51, seed456=74.02, seed789=74.02), the average doesn't match that value. It seems the original diagnosis experiment may have used a different seed configuration than what's reflected in the multi-seed analysis. Both rows show SC=75.98, which seems like it could be a copy-paste error since the 7B and 14B models shouldn't have identical accuracy. Looking at the multi-seed data, the 4-seed mean for 14B is 75.01 ± 1.67, which is notably different from the 77.50 reported for seed42 in the multi-seed table, suggesting there might be inconsistencies in how these results are being reported across different experiments.

The task is asking me to verify whether 75.98 is incorrectly attributed to the 14B model when it should actually belong to the 7B model, and to check if the 14B value should instead be 77.45 or 77.50 based on the other tables. I need to search through the document to confirm where each value appears and whether they're assigned to the correct model size. Looking at the actual table entries in the LaTeX files, I can see that both the main Qwen2.5-14B FOLIO row and the independence tab row are showing 75.98 as the SC value, but the registry confirms the correct value should be 77.50 for the 14B model with seed42. This means I need to update these entries to use the correct value and fix the discrepancy.

However, I'm realizing that changing this value would require updates across multiple tables and figures throughout the document, which conflicts with the instruction not to modify other tables. I need to determine whether the current 75.98 might actually be correct for a different experimental configuration, or if this is indeed an error that needs fixing despite the cascading changes required. The original single-seed experiment for Qwen2.5-14B FOLIO was exp-041 with SC=77.45%, so the 75.98 value in diagnosis.tex appears to be an error—likely copied from the 7B result. The task explicitly confirms this is wrong, but also says not to modify other tables, which creates a conflict. I think the safest approach is to make just the two requested caption and paragraph modifications and report the discrepancy rather than changing values across multiple tables. I'm verifying the data in the multi-seed and independence tables against the original experiments. The Qwen2.5-14B FOLIO value of 75.98% in the independence table appears inconsistent with the expected 77.45% from the original experiment, so I need to check if this is the error mentioned in the task. Let me start with the explicitly requested edits and report my findings as I go.

For the caption revision, I'm replacing the current text with a more precise version that clarifies which models show negative deltas on ProofWriter, specifies that Qwen3-14B's results are not statistically significant, and adds context about why the high baseline limits error correction potential.

For the analysis paragraph, I'm condensing the detailed seed-by-seed breakdown and capability gradient into a tighter statement: across ProofWriter, Mistral-7B, LLaMA-8B, and Qwen2.5-14B consistently show negative performance changes (with LLaMA-8B reaching statistical significance), while Qwen3-14B alone shows a positive mean delta, revealing a clear pattern where model capability inversely correlates with the magnitude of performance decline. I'm noticing a discrepancy between the paragraph value for Qwen2.5-14B ($-1.63$) and what the table shows ($-1.71$), so I need to verify which is correct before finalizing the text. I should also integrate the capability-modulated explanation for Qwen3 more smoothly into the existing discussion about the gradient pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "c4ce597a-6625-467a-afc2-9f8ed4401a29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HM5seFKBV4Nff1McYBxM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 31284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6495
      },
      "output_tokens": 11,
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

_source line 24_

Now I have the full picture. Let me make the three edits.

**Edit 1 — Caption:**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "7c22fab2-64cb-4c9d-bd28-d0a552bbc888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HM5seFKBV4Nff1McYBxM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 31284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6495
      },
      "output_tokens": 11,
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01XNXr7Aq1MWsPeUBm3YCKDm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "old_string": "\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp).}",
  "new_string": "\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "bc3c1d80-5512-47a4-abad-5737c2c5e14f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HM5seFKBV4Nff1McYBxM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 31284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6495
      },
      "output_tokens": 11,
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

_source line 26 · 2026-05-24T12:59:56.380Z_

<details><summary>↩ Tool result · `toolu_01XNXr7Aq1MWsPeUBm3YCKDm`</summary>

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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "2a54a27a-9ba3-407d-9152-33be185ae515",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "oldString": "\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp).}",
    "newString": "\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}",
    "originalFile": "\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability-Accuracy Constraint Diagnostics}\n\\label{app:diagnostics}\n\\label{app:cil}\n\n\\paragraph{Conditional Correction Ratio.}\nWe define the \\textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:\n\\begin{equation}\n\\label{eq:cil}\n\\text{CCR}(V, G) = \\log \\frac{P(V \\text{ correct} \\mid G \\text{ wrong})}{P(V \\text{ correct} \\mid G \\text{ correct})}.\n\\end{equation}\n$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n\n\\paragraph{Empirical CCR across verifier--generator pairs.}\nTable~\\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\\rho = 0.839$, 95\\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\\text{CCR} < 0$: same-model SICA or mismatched capability gap.}\n\\label{tab:cil_empirical}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllrr@{}}\n\\toprule\nGenerator & Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\\\\nMistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\\\\nMistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\\\\nMistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\\\\nQwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\\\\nMistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-condition diagnostics.}\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Oracle Control}\n\\label{app:oracle}\n\\label{sec:oracle}\n\\label{app:pw-oracle-subtype}\n\nReplacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \\times 10^{-7}$), and $+17.17$\\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\\Delta$ ($+3.43$\\,pp) captures only 11.5\\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\\,pp) against an oracle ceiling of $+17.17$\\,pp, indicating that stronger models do not self-extract more effectively.\n\n\\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 90.26 & \\textbf{98.70} & +8.44 \\\\\nAttNeg & 160 & 81.88 & \\textbf{91.88} & +10.00 \\\\\nRelNoneg & 146 & 60.96 & \\textbf{84.25} & +23.29 \\\\\nRelNeg & 140 & 60.71 & \\textbf{89.29} & +28.58 \\\\\n\\midrule\nOverall & 600 & 74.00 & \\textbf{91.17} & +17.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAX-SAT vs.\\ count-only agreement across constraint weight $\\alpha \\in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\\times$, seed 42); Qwen2.5-14B (BR $= 3.85\\times$, seed 123). $\\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\\alpha{=}1$: full source-attribution penalty. Agreement $\\geq 99\\%$ at all $\\alpha$ including endpoints, confirming vacuity is weight-insensitive.}\n\\label{tab:alpha-ablation}\n\\begin{tabular}{@{}crr@{}}\n\\toprule\n$\\alpha$ & Mistral Agr.\\ (\\%) & Qwen2.5 Agr.\\ (\\%) \\\\\n\\midrule\n0.0 & 100 & 100 \\\\\n0.1 & 100 & 100 \\\\\n0.3 & 100 & 100 \\\\\n0.5 & 100 & 100 \\\\\n0.7 & 99 & 100 \\\\\n0.9 & 99 & 100 \\\\\n1.0 & 99 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_interventions_compact.pdf}\n\\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\\Delta$ vs.\\ SC. Grey band: $\\pm 1$\\,pp noise zone.}\n\\label{fig:interventions-summary}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 83.33\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\addlinespace\n24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\\\\n25 & Premise-only filter & Constraint sel.\\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\\\\n26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\\text{sel}}{=}8$ \\\\\n27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\\% UNSAT \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 25.0\\% of the oracle ceiling ($+13.73$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\\times$, $3.85\\times$, $2.88\\times$) are reported in \\S\\ref{sec:confirmation-bias}. LLaMA weighted BR CI: [2.19, 3.28].\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\\ correct problems. Wrong \\%: weighted fraction of constraints supporting the incorrect majority on error problems. $\\Delta$: SICA $-$ SC (pp).}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & BR (wtd.) & Wrong (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $4.24\\times$ & 80.9 & $+$4.90 \\\\\nQwen2.5-14B & $3.69\\times$ & 78.7 & $-$0.98 \\\\\nLLaMA-3.1-8B & $2.66\\times$ & 72.7 & $-$4.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Frontier model universality.}\n\\label{app:frontier-scb}\nTable~\\ref{tab:frontier-scb} extends confirmation bias analysis to nine models spanning 7B open-source to frontier closed-source. All models exhibit $\\text{BR} > 1$ (range: $1.66$--$4.97\\times$). Extraction context varies: open-source models use self-extraction (the model extracts constraints from its own traces); frontier models use cross-model extraction (Mistral-7B extracts FOL from the target model's traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\\text{err}$: number of incorrect instances on which BR is computed. $\\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). $^\\dagger$8 API-failure questions excluded ($n = 196$). All models exhibit $\\text{BR} > 1$; BR estimates for high-accuracy models ($n_\\text{err} < 40$) have wider confidence intervals; Gemini ($n_\\text{err} \\approx 12$) should be interpreted with particular caution. Process-level similarity ($\\kappa_{\\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\\ref{tab:cross-model-process}.}\n\\label{tab:frontier-scb}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Ext. & SC (\\%) & $n_\\text{err}$ & BR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\\\\nLLaMA-8B & $^a$ & \\textrm{---} & \\textrm{---} & 2.88 & \\textrm{---} \\\\\nQwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\\\\n\\addlinespace\nR1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\\\\ngpt-4o & $^a$ & 76.96 & 47 & 2.65 & $-$1.96 \\\\\ngpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\\\\ngpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\\\\no3$^\\dagger$ & $^b$ & 82.65 & 34 & 1.66 & 0.00 \\\\\nGemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.05 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{ProcessSim definition.}\n\\label{app:process-sim}\nProcess similarity is the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.\n\n\\paragraph{Process-$\\kappa$ gradient.}\n\\label{app:process-gradient}\nUnder cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\\ref{tab:process-gradient}; Spearman $\\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\\kappa_{\\text{proc}}$) \\emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\\kappa_{\\text{proc}} = 0.248$, $\\text{BR} = 2.92$) and gains $+2.45$\\,pp; o3 has moderate trace diversity ($\\kappa_{\\text{proc}} = 0.596$) but near-minimal bias ($\\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\\% of error problems have $\\text{BR} = \\infty$ but low finite-BR), yielding $\\Delta = 0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Process-$\\kappa$ gradient under cross-model extraction (Mistral-7B $\\rightarrow$ target model traces, FOLIO). $\\kappa_{\\text{proc}}$: process-level cosine similarity. $\\Delta$: SICA $-$ SC (pp). Spearman $\\rho(\\kappa_{\\text{proc}} \\rightarrow \\Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}\n\\label{tab:process-gradient}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & $\\kappa_{\\text{proc}}$ & $\\Delta$ (pp) & BR \\\\\n\\midrule\nR1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\\\\ngpt-5.5 & 0.563 & $+$0.49 & 3.48 \\\\\no3 & 0.596 & 0.00 & 1.66 \\\\\nGemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\\\\ngpt-4.1 & 0.792 & $-$1.47 & 2.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Trace independence metrics.}\n\\label{app:trace-independence}\n\nTable~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.042$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each. $^{\\dag}$\\,$\\kappa$ computed in an earlier pipeline run; all other rows recomputed from per-problem vote distributions with answer labels normalized to canonical categories.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91$^{\\dag}$ & 1.09 & 86.27 & $+$0.49 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66$^{\\dag}$ & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53$^{\\dag}$ & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52$^{\\dag}$ & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48$^{\\dag}$ & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\\\\nMistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\\\\nMistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\\\\nMistral-7B (multi-T) & FOLIO & 0.43 & 2.11 & 57.84 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.46$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.05$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.20 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\\ TF-IDF $0.74$), widening the gap over answer-level $\\kappa = 0.55$. The process homogeneity finding is robust to representation choice.\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-trace constraint yield uniformity.}\n\\label{app:yield-cv}\n\nObservation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\\% of problems fall below $\\text{CV} = 0.3$, and 91.2\\% below $0.5$, supporting the uniformity assumption. Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \\times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \\times 10^{-11}$). Although statistically significant, the absolute difference (${\\sim}0.6$ constraints, $< 12\\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\\%$ of problems regardless of yield variation.\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{TOST Equivalence Tests}\n\\label{app:tost}\n\nWe apply two one-sided tests (TOST) \\citep{lakens2017equivalence} with equivalence margin $\\pm 2$\\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \\emph{equivalent} (TOST significant), \\emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \\emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\\Delta| \\leq 2$\\,pp effects.\n\n\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\n\\label{tab:tost-sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMargin & Equivalent & Different & Underpowered \\\\\n\\midrule\n$\\pm 1$\\,pp & 0 & 2 & 14 \\\\\n$\\pm 2$\\,pp & 4 & 2 & 10 \\\\\n$\\pm 3$\\,pp & 10 & 0 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Relative-margin TOST.}\n\\label{app:relative_tost}\nThe absolute $\\pm 2$\\,pp margin is more stringent at high baselines ($\\pm 2.4\\%$ relative at SC $= 85\\%$) than low ones ($\\pm 5.1\\%$ at SC $= 39\\%$). A relative $\\pm 5\\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\\geq 75\\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.\n\n\\paragraph{Conditional Correction Ratio data.}\n\\label{app:cil-data}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\\text{CCR} < 0$: same-model SICA or weak capability gap.}\n\\label{tab:cil_main}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nGenerator--Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral $\\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\\\\nMistral $\\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\\\\nMistral $\\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen-14B $\\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\\\\nMistral $\\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral $\\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\\\\nQwen-14B $\\times$ SICA & PW & $-$4.21 & $-$2.50 \\\\\nMistral $\\times$ SICA & PW & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade details.}\n\\label{app:drc}\nDRC invokes NLI only when SC consensus falls below threshold $\\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\\%$), consistent with the capability-gap hypothesis (\\S\\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\\ref{app:2x2}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\\tau{=}0.7$ recovers 83--90\\% of full-combo gain at ${\\sim}35\\%$ NLI cost across both datasets.}\n\\label{tab:drc}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Method & Acc.\\ & NLI Calls & Cost & Recovery \\\\\n\\midrule\n\\multirow{3}{*}{PW-D5} & SC only & 39.33\\% & 0/600 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{45.33\\%} & \\textbf{207/600} & \\textbf{34.5\\%} & \\textbf{90.0\\%} \\\\\n& Full combo & 46.00\\% & 600/600 & 100\\% & 100\\% \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO} & SC only & 55.88\\% & 0/204 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{58.33\\%} & \\textbf{71/204} & \\textbf{34.8\\%} & \\textbf{83.3\\%} \\\\\n& Full combo & 58.82\\% & 204/204 & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%, gap\\,$+$15.67}}}\n  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 46.00 & $+$6.67 & $1.13{\\times}10^{-5}$ & $6.78{\\times}10^{-5}$ & {***} \\\\\n  & 5 & 50.33 & $+$11.00 & $6.18{\\times}10^{-7}$ & $7.41{\\times}10^{-6}$ & {***} \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%, gap\\,$-$17.50}}}\n  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\\\\n  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen2.5-14B\\\\{\\scriptsize SC\\,74.00\\%, gap\\,$-$19.00}}}\n  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\\\\n  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize SC\\,85.83\\%, gap\\,$-$30.83}}}\n  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\\\\n  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{BART-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}\n\\label{tab:bart-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\\pm$0.00 & --- \\\\\nQwen2.5-14B {\\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoBERTa-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}\n\\label{tab:roberta-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\\\\nQwen2.5-14B {\\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FOLIO NLI combo results.}\n\\label{app:folio-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\\ref{tab:cross-model-ablation}).}\n\\label{tab:folio-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 58.82 & $+$2.94 & n.s. \\\\\n & 5 & & 59.80 & $+$3.92 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 65.20 & $-$0.98 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\n & 3 & & 75.49 & $-$0.49 & n.s. \\\\\n & 5 & & 73.53 & $-$2.45 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.80 & $+$1.47 & n.s. \\\\\n & 5 & & 83.33 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \\emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}\n\\label{tab:folio-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\\\\n & 3 & & 56.37 & $+$0.49 & n.s. \\\\\n & 5 & & 56.86 & $+$0.98 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\\\\n & 3 & & 67.65 & $+$1.47 & n.s. \\\\\n & 5 & & 64.71 & $-$1.47 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 72.55 & $-$3.43 & .039{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 82.84 & $-$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \\emph{degradation} at $w{=}5$ ($p{=}.012$)---the same capability-gap signature as BART.}\n\\label{tab:folio-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 57.84 & $+$1.96 & n.s. \\\\\n & 5 & & 58.82 & $+$2.94 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 66.67 & $+$0.49 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 71.57 & $-$4.41 & .012{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 83.82 & $+$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LogiQA NLI combo results.}\n\\label{app:logiqa-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\n\\label{tab:logiqa-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 54.00 & $+$1.00 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\\\\n & 3 & & 58.00 & $-$1.50 & n.s. \\\\\n & 5 & & 58.00 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.00 & $-$1.00 & n.s. \\\\\n & 5 & & 78.00 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 80.50 & $-$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}\n\\label{tab:logiqa-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 52.50 & $-$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\\\\n & 3 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 81.50 & $+$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\\% standalone). All three NLI verifiers produce the same null result on LogiQA.}\n\\label{tab:logiqa-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\\\\n & 3 & & 58.50 & $-$1.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier results.}\n\\label{app:finetuned-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\\cap$SC-incorrect to SC-correct$\\cap$NLI-incorrect.}\n\\label{tab:finetuned-nli}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}lrrrrc@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & Compl.\\ ratio \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%}}}\n  & 1 & 42.17 & $+$2.83 & \\multirow{3}{*}{364:2} \\\\\n  & 3 & 52.00 & $+$12.67 & \\\\\n  & 5 & 65.50 & $+$26.17 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%}}}\n  & 1 & 76.00 & $+$3.50 & \\multirow{3}{*}{164:1} \\\\\n  & 3 & 84.17 & $+$11.67 & \\\\\n  & 5 & 91.67 & $+$19.17 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model voting ablation.}\n\\label{app:cross-model-ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model voting ablation ($w \\in \\{3,5\\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators---worsening at higher $w$---while NLI combo does not, indicating that structural independence---not merely model diversity---drives the escape.}\n\\label{tab:cross-model-ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccrl@{}}\n\\toprule\nGenerator & Voter/Verifier & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{ProofWriter ($n{=}600$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\\\\n  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\\\\n\\addlinespace\n\\multirow{5}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\\\\n  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\\\\n  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\\\\n  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\\\\n  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\\\\n  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\\\\n  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\\\\n  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{FOLIO ($n{=}204$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\\\\n  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\\\\n  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\\\\n  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\n  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\n  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\\\\n  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\\\\n  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Generator$\\times$Extractor 2$\\times$2 Matrix.}\n\\label{app:2x2}\n\nTable~\\ref{tab:2x2-folio} reports the full $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\\sim}25$\\,pp vs.\\ column difference ${\\sim}3$\\,pp), contrasting with ProofWriter where the extractor dominates ($\\Delta$ range ${\\pm}40$--$50$\\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\\Delta = +2.94$\\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\\Delta = +2.94$\\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\\Delta$ is coincidental---the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FOLIO $2{\\times}2$ generator${\\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}\n\\label{tab:2x2-folio}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Extractor & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & BR \\\\\n\\midrule\n\\multirow{2}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize $\\kappa{=}0.46$}}}\n  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\\\\n  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\\\\n\\addlinespace\n\\multirow{2}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize $\\kappa{=}0.79$}}}\n  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\\\\n  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Single-Trace and Aggregation Statistics}\n\\label{app:single-trace}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Single-trace accuracy (mean $\\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\\ref{tab:main_results}).}\n\\label{tab:single-trace-stats}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & Single (\\%) & Std & SC@12 (\\%) & Gain (pp) \\\\\n\\midrule\nMistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\\\\nQwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\\\\nQwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize Inter-trace standard deviation shrinks $2.8\\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\\S\\ref{sec:cross-arch}).}\n\\end{table}\n\n\\paragraph{Extraction temperature sensitivity.}\n\\label{app:text-sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of extraction temperature $T_{\\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\\dagger$\\,Uses a different trace set (SC $= 54.41\\%$); all other conditions share the same traces (SC $= 55.88\\%$).}\n\\label{tab:text-sensitivity}\n\\begin{tabular}{@{}cccr@{}}\n\\toprule\n$T_{\\text{ext}}$ & SICA (\\%) & $\\Delta$ vs.\\ SC (pp) & Avg.\\ \\#Constr. \\\\\n\\midrule\n0.1 & 57.35 & $+$1.47 & 69.3 \\\\\n$0.3^\\dagger$ & 59.31 & $+$3.43 & 68.8 \\\\\n0.5 & 56.37 & $+$0.49 & 68.2 \\\\\n0.7 & 53.43 & $-$2.45 & 67.3 \\\\\n1.0 & 55.39 & $-$0.49 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp).}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 74.00 & 71.50 & $-$2.50 \\\\\n123 & 72.33 & 70.83 & $-$1.50 \\\\\n456 & 73.00 & 72.17 & $-$0.83 \\\\\n789 & 73.50 & 71.50 & $-$2.00 \\\\\n\\midrule\nMean $\\pm$ SD & 73.21 $\\pm$ 0.71 & 71.50 $\\pm$ 0.55 & $-$1.71 $\\pm$ 0.71 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen3-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 85.83 & 85.67 & $-$0.17 \\\\\n123 & 85.17 & 86.50 & $+$1.33 \\\\\n456 & 84.50 & 86.83 & $+$2.33 \\\\\n789 & 85.50 & 85.67 & $+$0.17 \\\\\n\\midrule\nMean $\\pm$ SD & 85.25 $\\pm$ 0.57 & 86.17 $\\pm$ 0.59 & $+$0.92 $\\pm$ 1.14 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}\n\\label{tab:subpop-constraint}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rr rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Tertile} & $n$ & $\\bar{c}$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO-204}\n & Low \\scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\\hphantom{00} \\\\\n & Mid \\scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\\rlap{*} \\\\\n & High \\scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n\\midrule\n\\multirow{3}{*}{PW-600}\n & Low \\scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\\\\n & Mid \\scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\\\\n & High \\scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\\hphantom{00} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\\,pp overall (55.9\\% $\\to$ 59.3\\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).\nThe gain concentrates in the mid-constraint tertile ($+$9.4\\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.\nOn ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\\Delta{=}{-}0.5$\\,pp, $p{=}1.0$).\nWe note that with six subgroup tests, one significant result at $\\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.\n\n\\paragraph{Individual intervention significance.}\n\\label{app:intervention-individual}\nOf the 27 training-free remediation strategies (Figure~\\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\\to$Mistral ($+0.98$\\,pp) and Generational ($+0.49$\\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\\label{app:limitations-extended}\n\n\\paragraph{SCB versus CoT unfaithfulness.}\nSCB is distinct from CoT unfaithfulness \\citep{turpin2023language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \\emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias---the constraint $P(\\text{answer\\_A})$ reflects vote share, not logical validity. The shuffle control (\\S\\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.\n\n\\paragraph{Implications for neuro-symbolic practitioners.}\nOur results do not imply that neuro-symbolic methods are inherently flawed---they imply that \\emph{self-extracted} constraints cannot provide independent verification. The key distinction is \\emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \\citep{ye2024satlm}, Logic-LM \\citep{pan2023logiclm}) formalize the problem \\emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\\S\\ref{sec:cross-arch}) and use the diagnostic framework in \\S\\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.\n\n\\paragraph{Test-time scaling implications.}\nVote diversity decreases with model capability: $K_\\text{eff}$ drops from 3.94 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \\citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\\kappa$ analysis (\\S\\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level---traces that disagree on final answers still share 69\\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\\S\\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.\n\n\\paragraph{SCB diagnostic toolkit.}\n\\label{app:diagnostic-toolkit}\nWe recommend four zero-cost diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.\n\\emph{Bias Ratio} (BR; \\S\\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\\text{BR} > 1$ indicates constraints are biased toward the majority; $\\text{BR} \\gg 2$ (as in all nine models tested; Table~\\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\\pm$ bootstrap 95\\% CI.\n\\emph{Effective-K} ($K_\\text{eff}$; Eq.~\\ref{eq:effk}): compute Fleiss' $\\kappa$ across $K$ traces, then $K_\\text{eff} = 1 + (K-1)(1-\\kappa)$. Threshold: $K_\\text{eff} \\leq 1.30$ never improves in our experiments---aggregation collapses to majority voting. $K_\\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.\n\\emph{Degenerate Consensus} ($C_0$; \\S\\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\\%$ renders aggregation moot; $C_0 < 5\\%$ means the model is maximally uncertain and constraints tend to amplify noise.\n\\emph{ProcessSim} (Eq.~\\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\\text{BR} > 2$, this predicts SCB will dominate.\nA practitioner should compute all four on a held-out sample ($n \\geq 50$). If $K_\\text{eff} \\leq 1.30$ or $C_0 > 95\\%$ or ($\\text{BR} > 2$ and $\\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.\n\n\\paragraph{BR permutation null model.}\n\\label{app:br-permutation}\nThe permutation test referenced in \\S\\ref{sec:confirmation-bias} proceeds as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item For each problem $p$ with extracted constraints $\\{c_1, \\ldots, c_M\\}$ and source answers $\\{a_1, \\ldots, a_M\\}$:\n\\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).\n\\item Compute $\\text{BR}_\\text{null}$ from the permuted assignments.\n\\item Repeat $10{,}000$ times to obtain the null distribution.\n\\item Compute $p$-value $= |\\{r : \\text{BR}_\\text{null}^{(r)} \\geq \\text{BR}_\\text{obs}\\}| / 10{,}000$.\n\\end{enumerate}\nAcross all tested conditions, $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.\n\n\\paragraph{Future directions: trained extractors and beyond.}\n\\label{app:future-directions}\nOur oracle controls reveal that perfect extraction would yield $+29.90$\\,pp over SC on Mistral-7B FOLIO---self-extraction captures only ${\\sim}12\\%$ of this ceiling. This gap motivates several future directions.\n\\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence---the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\\S\\ref{sec:cross-arch}).\n\\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\\S\\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.\n\\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.\n\\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.\n\n\\paragraph{SCB as an evaluation framework.}\n\\label{app:scb-evaluation}\nThe SCB metrics---BR, $K_\\text{eff}$, ProcessSim, and CCR---can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \\citep{huang2024selfcorrect}, self-refinement \\citep{madaan2023selfrefine}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-consistency \\citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\\text{BR} < 1$, high $K_\\text{eff}$, and $\\text{CCR} > 0$ demonstrates genuine self-improvement; $\\text{BR} > 1$ with $\\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.\n\n\\paragraph{Additional scope considerations.}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers ($\\forall$/$\\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\\sim}$10\\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 1404,
        "oldLines": 7,
        "newStart": 1404,
        "newLines": 7,
        "lines": [
          " \\begin{table}[h]",
          " \\centering",
          " \\small",
          "-\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp); three of four ProofWriter conditions show consistently negative $\\Delta$ ($p < .001$ for LLaMA-8B and Mistral-7B), while Qwen3-14B is the sole positive condition ($+0.92$\\,pp).}",
          "+\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}",
          " \\label{tab:multi-seed}",
          " \\resizebox{\\columnwidth}{!}{%",
          " \\begin{tabular}{@{}lrrrr@{}}"
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

_source line 27_

**Edit 2 — Analysis paragraph, add Qwen3 capability-modulated sentence:**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "8043dc46-ea91-4015-8000-3ecc0235da49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L492HDB2zPKLfsFihYyFbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 37779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4541
      },
      "output_tokens": 7,
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rw1MTjYNQxGegZqoQb6fju`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "old_string": "The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
  "new_string": "Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "92189cfe-5ca9-4a70-bfe9-a67fda3dacec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L492HDB2zPKLfsFihYyFbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4541,
      "cache_read_input_tokens": 37779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4541
      },
      "output_tokens": 7,
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

_source line 29 · 2026-05-24T13:00:02.290Z_

<details><summary>↩ Tool result · `toolu_01Rw1MTjYNQxGegZqoQb6fju`</summary>

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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "7c1e9209-c932-4040-953d-c0488b3f2094",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "oldString": "The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
    "newString": "Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
    "originalFile": "\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability-Accuracy Constraint Diagnostics}\n\\label{app:diagnostics}\n\\label{app:cil}\n\n\\paragraph{Conditional Correction Ratio.}\nWe define the \\textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:\n\\begin{equation}\n\\label{eq:cil}\n\\text{CCR}(V, G) = \\log \\frac{P(V \\text{ correct} \\mid G \\text{ wrong})}{P(V \\text{ correct} \\mid G \\text{ correct})}.\n\\end{equation}\n$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n\n\\paragraph{Empirical CCR across verifier--generator pairs.}\nTable~\\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\\rho = 0.839$, 95\\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\\text{CCR} < 0$: same-model SICA or mismatched capability gap.}\n\\label{tab:cil_empirical}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllrr@{}}\n\\toprule\nGenerator & Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\\\\nMistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\\\\nMistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\\\\nMistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\\\\nQwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\\\\nMistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-condition diagnostics.}\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Oracle Control}\n\\label{app:oracle}\n\\label{sec:oracle}\n\\label{app:pw-oracle-subtype}\n\nReplacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \\times 10^{-7}$), and $+17.17$\\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\\Delta$ ($+3.43$\\,pp) captures only 11.5\\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\\,pp) against an oracle ceiling of $+17.17$\\,pp, indicating that stronger models do not self-extract more effectively.\n\n\\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 90.26 & \\textbf{98.70} & +8.44 \\\\\nAttNeg & 160 & 81.88 & \\textbf{91.88} & +10.00 \\\\\nRelNoneg & 146 & 60.96 & \\textbf{84.25} & +23.29 \\\\\nRelNeg & 140 & 60.71 & \\textbf{89.29} & +28.58 \\\\\n\\midrule\nOverall & 600 & 74.00 & \\textbf{91.17} & +17.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAX-SAT vs.\\ count-only agreement across constraint weight $\\alpha \\in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\\times$, seed 42); Qwen2.5-14B (BR $= 3.85\\times$, seed 123). $\\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\\alpha{=}1$: full source-attribution penalty. Agreement $\\geq 99\\%$ at all $\\alpha$ including endpoints, confirming vacuity is weight-insensitive.}\n\\label{tab:alpha-ablation}\n\\begin{tabular}{@{}crr@{}}\n\\toprule\n$\\alpha$ & Mistral Agr.\\ (\\%) & Qwen2.5 Agr.\\ (\\%) \\\\\n\\midrule\n0.0 & 100 & 100 \\\\\n0.1 & 100 & 100 \\\\\n0.3 & 100 & 100 \\\\\n0.5 & 100 & 100 \\\\\n0.7 & 99 & 100 \\\\\n0.9 & 99 & 100 \\\\\n1.0 & 99 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_interventions_compact.pdf}\n\\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\\Delta$ vs.\\ SC. Grey band: $\\pm 1$\\,pp noise zone.}\n\\label{fig:interventions-summary}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 83.33\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\addlinespace\n24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\\\\n25 & Premise-only filter & Constraint sel.\\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\\\\n26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\\text{sel}}{=}8$ \\\\\n27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\\% UNSAT \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 25.0\\% of the oracle ceiling ($+13.73$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\\times$, $3.85\\times$, $2.88\\times$) are reported in \\S\\ref{sec:confirmation-bias}. LLaMA weighted BR CI: [2.19, 3.28].\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\\ correct problems. Wrong \\%: weighted fraction of constraints supporting the incorrect majority on error problems. $\\Delta$: SICA $-$ SC (pp).}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & BR (wtd.) & Wrong (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $4.24\\times$ & 80.9 & $+$4.90 \\\\\nQwen2.5-14B & $3.69\\times$ & 78.7 & $-$0.98 \\\\\nLLaMA-3.1-8B & $2.66\\times$ & 72.7 & $-$4.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Frontier model universality.}\n\\label{app:frontier-scb}\nTable~\\ref{tab:frontier-scb} extends confirmation bias analysis to nine models spanning 7B open-source to frontier closed-source. All models exhibit $\\text{BR} > 1$ (range: $1.66$--$4.97\\times$). Extraction context varies: open-source models use self-extraction (the model extracts constraints from its own traces); frontier models use cross-model extraction (Mistral-7B extracts FOL from the target model's traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\\text{err}$: number of incorrect instances on which BR is computed. $\\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). $^\\dagger$8 API-failure questions excluded ($n = 196$). All models exhibit $\\text{BR} > 1$; BR estimates for high-accuracy models ($n_\\text{err} < 40$) have wider confidence intervals; Gemini ($n_\\text{err} \\approx 12$) should be interpreted with particular caution. Process-level similarity ($\\kappa_{\\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\\ref{tab:cross-model-process}.}\n\\label{tab:frontier-scb}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Ext. & SC (\\%) & $n_\\text{err}$ & BR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\\\\nLLaMA-8B & $^a$ & \\textrm{---} & \\textrm{---} & 2.88 & \\textrm{---} \\\\\nQwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\\\\n\\addlinespace\nR1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\\\\ngpt-4o & $^a$ & 76.96 & 47 & 2.65 & $-$1.96 \\\\\ngpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\\\\ngpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\\\\no3$^\\dagger$ & $^b$ & 82.65 & 34 & 1.66 & 0.00 \\\\\nGemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.05 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{ProcessSim definition.}\n\\label{app:process-sim}\nProcess similarity is the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.\n\n\\paragraph{Process-$\\kappa$ gradient.}\n\\label{app:process-gradient}\nUnder cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\\ref{tab:process-gradient}; Spearman $\\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\\kappa_{\\text{proc}}$) \\emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\\kappa_{\\text{proc}} = 0.248$, $\\text{BR} = 2.92$) and gains $+2.45$\\,pp; o3 has moderate trace diversity ($\\kappa_{\\text{proc}} = 0.596$) but near-minimal bias ($\\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\\% of error problems have $\\text{BR} = \\infty$ but low finite-BR), yielding $\\Delta = 0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Process-$\\kappa$ gradient under cross-model extraction (Mistral-7B $\\rightarrow$ target model traces, FOLIO). $\\kappa_{\\text{proc}}$: process-level cosine similarity. $\\Delta$: SICA $-$ SC (pp). Spearman $\\rho(\\kappa_{\\text{proc}} \\rightarrow \\Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}\n\\label{tab:process-gradient}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & $\\kappa_{\\text{proc}}$ & $\\Delta$ (pp) & BR \\\\\n\\midrule\nR1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\\\\ngpt-5.5 & 0.563 & $+$0.49 & 3.48 \\\\\no3 & 0.596 & 0.00 & 1.66 \\\\\nGemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\\\\ngpt-4.1 & 0.792 & $-$1.47 & 2.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Trace independence metrics.}\n\\label{app:trace-independence}\n\nTable~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.042$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each. $^{\\dag}$\\,$\\kappa$ computed in an earlier pipeline run; all other rows recomputed from per-problem vote distributions with answer labels normalized to canonical categories.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91$^{\\dag}$ & 1.09 & 86.27 & $+$0.49 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66$^{\\dag}$ & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53$^{\\dag}$ & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52$^{\\dag}$ & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48$^{\\dag}$ & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\\\\nMistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\\\\nMistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\\\\nMistral-7B (multi-T) & FOLIO & 0.43 & 2.11 & 57.84 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.46$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.05$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.20 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\\ TF-IDF $0.74$), widening the gap over answer-level $\\kappa = 0.55$. The process homogeneity finding is robust to representation choice.\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-trace constraint yield uniformity.}\n\\label{app:yield-cv}\n\nObservation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\\% of problems fall below $\\text{CV} = 0.3$, and 91.2\\% below $0.5$, supporting the uniformity assumption. Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \\times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \\times 10^{-11}$). Although statistically significant, the absolute difference (${\\sim}0.6$ constraints, $< 12\\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\\%$ of problems regardless of yield variation.\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{TOST Equivalence Tests}\n\\label{app:tost}\n\nWe apply two one-sided tests (TOST) \\citep{lakens2017equivalence} with equivalence margin $\\pm 2$\\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \\emph{equivalent} (TOST significant), \\emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \\emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\\Delta| \\leq 2$\\,pp effects.\n\n\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\n\\label{tab:tost-sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMargin & Equivalent & Different & Underpowered \\\\\n\\midrule\n$\\pm 1$\\,pp & 0 & 2 & 14 \\\\\n$\\pm 2$\\,pp & 4 & 2 & 10 \\\\\n$\\pm 3$\\,pp & 10 & 0 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Relative-margin TOST.}\n\\label{app:relative_tost}\nThe absolute $\\pm 2$\\,pp margin is more stringent at high baselines ($\\pm 2.4\\%$ relative at SC $= 85\\%$) than low ones ($\\pm 5.1\\%$ at SC $= 39\\%$). A relative $\\pm 5\\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\\geq 75\\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.\n\n\\paragraph{Conditional Correction Ratio data.}\n\\label{app:cil-data}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\\text{CCR} < 0$: same-model SICA or weak capability gap.}\n\\label{tab:cil_main}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nGenerator--Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral $\\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\\\\nMistral $\\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\\\\nMistral $\\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen-14B $\\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\\\\nMistral $\\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral $\\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\\\\nQwen-14B $\\times$ SICA & PW & $-$4.21 & $-$2.50 \\\\\nMistral $\\times$ SICA & PW & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade details.}\n\\label{app:drc}\nDRC invokes NLI only when SC consensus falls below threshold $\\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\\%$), consistent with the capability-gap hypothesis (\\S\\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\\ref{app:2x2}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\\tau{=}0.7$ recovers 83--90\\% of full-combo gain at ${\\sim}35\\%$ NLI cost across both datasets.}\n\\label{tab:drc}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Method & Acc.\\ & NLI Calls & Cost & Recovery \\\\\n\\midrule\n\\multirow{3}{*}{PW-D5} & SC only & 39.33\\% & 0/600 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{45.33\\%} & \\textbf{207/600} & \\textbf{34.5\\%} & \\textbf{90.0\\%} \\\\\n& Full combo & 46.00\\% & 600/600 & 100\\% & 100\\% \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO} & SC only & 55.88\\% & 0/204 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{58.33\\%} & \\textbf{71/204} & \\textbf{34.8\\%} & \\textbf{83.3\\%} \\\\\n& Full combo & 58.82\\% & 204/204 & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%, gap\\,$+$15.67}}}\n  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 46.00 & $+$6.67 & $1.13{\\times}10^{-5}$ & $6.78{\\times}10^{-5}$ & {***} \\\\\n  & 5 & 50.33 & $+$11.00 & $6.18{\\times}10^{-7}$ & $7.41{\\times}10^{-6}$ & {***} \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%, gap\\,$-$17.50}}}\n  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\\\\n  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen2.5-14B\\\\{\\scriptsize SC\\,74.00\\%, gap\\,$-$19.00}}}\n  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\\\\n  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize SC\\,85.83\\%, gap\\,$-$30.83}}}\n  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\\\\n  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{BART-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}\n\\label{tab:bart-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\\pm$0.00 & --- \\\\\nQwen2.5-14B {\\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoBERTa-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}\n\\label{tab:roberta-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\\\\nQwen2.5-14B {\\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FOLIO NLI combo results.}\n\\label{app:folio-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\\ref{tab:cross-model-ablation}).}\n\\label{tab:folio-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 58.82 & $+$2.94 & n.s. \\\\\n & 5 & & 59.80 & $+$3.92 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 65.20 & $-$0.98 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\n & 3 & & 75.49 & $-$0.49 & n.s. \\\\\n & 5 & & 73.53 & $-$2.45 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.80 & $+$1.47 & n.s. \\\\\n & 5 & & 83.33 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \\emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}\n\\label{tab:folio-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\\\\n & 3 & & 56.37 & $+$0.49 & n.s. \\\\\n & 5 & & 56.86 & $+$0.98 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\\\\n & 3 & & 67.65 & $+$1.47 & n.s. \\\\\n & 5 & & 64.71 & $-$1.47 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 72.55 & $-$3.43 & .039{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 82.84 & $-$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \\emph{degradation} at $w{=}5$ ($p{=}.012$)---the same capability-gap signature as BART.}\n\\label{tab:folio-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 57.84 & $+$1.96 & n.s. \\\\\n & 5 & & 58.82 & $+$2.94 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 66.67 & $+$0.49 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 71.57 & $-$4.41 & .012{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 83.82 & $+$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LogiQA NLI combo results.}\n\\label{app:logiqa-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\n\\label{tab:logiqa-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 54.00 & $+$1.00 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\\\\n & 3 & & 58.00 & $-$1.50 & n.s. \\\\\n & 5 & & 58.00 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.00 & $-$1.00 & n.s. \\\\\n & 5 & & 78.00 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 80.50 & $-$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}\n\\label{tab:logiqa-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 52.50 & $-$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\\\\n & 3 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 81.50 & $+$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\\% standalone). All three NLI verifiers produce the same null result on LogiQA.}\n\\label{tab:logiqa-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\\\\n & 3 & & 58.50 & $-$1.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier results.}\n\\label{app:finetuned-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\\cap$SC-incorrect to SC-correct$\\cap$NLI-incorrect.}\n\\label{tab:finetuned-nli}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}lrrrrc@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & Compl.\\ ratio \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%}}}\n  & 1 & 42.17 & $+$2.83 & \\multirow{3}{*}{364:2} \\\\\n  & 3 & 52.00 & $+$12.67 & \\\\\n  & 5 & 65.50 & $+$26.17 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%}}}\n  & 1 & 76.00 & $+$3.50 & \\multirow{3}{*}{164:1} \\\\\n  & 3 & 84.17 & $+$11.67 & \\\\\n  & 5 & 91.67 & $+$19.17 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model voting ablation.}\n\\label{app:cross-model-ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model voting ablation ($w \\in \\{3,5\\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators---worsening at higher $w$---while NLI combo does not, indicating that structural independence---not merely model diversity---drives the escape.}\n\\label{tab:cross-model-ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccrl@{}}\n\\toprule\nGenerator & Voter/Verifier & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{ProofWriter ($n{=}600$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\\\\n  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\\\\n\\addlinespace\n\\multirow{5}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\\\\n  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\\\\n  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\\\\n  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\\\\n  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\\\\n  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\\\\n  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\\\\n  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{FOLIO ($n{=}204$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\\\\n  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\\\\n  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\\\\n  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\n  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\n  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\\\\n  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\\\\n  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Generator$\\times$Extractor 2$\\times$2 Matrix.}\n\\label{app:2x2}\n\nTable~\\ref{tab:2x2-folio} reports the full $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\\sim}25$\\,pp vs.\\ column difference ${\\sim}3$\\,pp), contrasting with ProofWriter where the extractor dominates ($\\Delta$ range ${\\pm}40$--$50$\\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\\Delta = +2.94$\\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\\Delta = +2.94$\\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\\Delta$ is coincidental---the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FOLIO $2{\\times}2$ generator${\\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}\n\\label{tab:2x2-folio}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Extractor & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & BR \\\\\n\\midrule\n\\multirow{2}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize $\\kappa{=}0.46$}}}\n  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\\\\n  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\\\\n\\addlinespace\n\\multirow{2}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize $\\kappa{=}0.79$}}}\n  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\\\\n  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Single-Trace and Aggregation Statistics}\n\\label{app:single-trace}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Single-trace accuracy (mean $\\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\\ref{tab:main_results}).}\n\\label{tab:single-trace-stats}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & Single (\\%) & Std & SC@12 (\\%) & Gain (pp) \\\\\n\\midrule\nMistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\\\\nQwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\\\\nQwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize Inter-trace standard deviation shrinks $2.8\\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\\S\\ref{sec:cross-arch}).}\n\\end{table}\n\n\\paragraph{Extraction temperature sensitivity.}\n\\label{app:text-sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of extraction temperature $T_{\\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\\dagger$\\,Uses a different trace set (SC $= 54.41\\%$); all other conditions share the same traces (SC $= 55.88\\%$).}\n\\label{tab:text-sensitivity}\n\\begin{tabular}{@{}cccr@{}}\n\\toprule\n$T_{\\text{ext}}$ & SICA (\\%) & $\\Delta$ vs.\\ SC (pp) & Avg.\\ \\#Constr. \\\\\n\\midrule\n0.1 & 57.35 & $+$1.47 & 69.3 \\\\\n$0.3^\\dagger$ & 59.31 & $+$3.43 & 68.8 \\\\\n0.5 & 56.37 & $+$0.49 & 68.2 \\\\\n0.7 & 53.43 & $-$2.45 & 67.3 \\\\\n1.0 & 55.39 & $-$0.49 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 74.00 & 71.50 & $-$2.50 \\\\\n123 & 72.33 & 70.83 & $-$1.50 \\\\\n456 & 73.00 & 72.17 & $-$0.83 \\\\\n789 & 73.50 & 71.50 & $-$2.00 \\\\\n\\midrule\nMean $\\pm$ SD & 73.21 $\\pm$ 0.71 & 71.50 $\\pm$ 0.55 & $-$1.71 $\\pm$ 0.71 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen3-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 85.83 & 85.67 & $-$0.17 \\\\\n123 & 85.17 & 86.50 & $+$1.33 \\\\\n456 & 84.50 & 86.83 & $+$2.33 \\\\\n789 & 85.50 & 85.67 & $+$0.17 \\\\\n\\midrule\nMean $\\pm$ SD & 85.25 $\\pm$ 0.57 & 86.17 $\\pm$ 0.59 & $+$0.92 $\\pm$ 1.14 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}\n\\label{tab:subpop-constraint}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rr rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Tertile} & $n$ & $\\bar{c}$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO-204}\n & Low \\scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\\hphantom{00} \\\\\n & Mid \\scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\\rlap{*} \\\\\n & High \\scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n\\midrule\n\\multirow{3}{*}{PW-600}\n & Low \\scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\\\\n & Mid \\scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\\\\n & High \\scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\\hphantom{00} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\\,pp overall (55.9\\% $\\to$ 59.3\\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).\nThe gain concentrates in the mid-constraint tertile ($+$9.4\\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.\nOn ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\\Delta{=}{-}0.5$\\,pp, $p{=}1.0$).\nWe note that with six subgroup tests, one significant result at $\\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.\n\n\\paragraph{Individual intervention significance.}\n\\label{app:intervention-individual}\nOf the 27 training-free remediation strategies (Figure~\\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\\to$Mistral ($+0.98$\\,pp) and Generational ($+0.49$\\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\\label{app:limitations-extended}\n\n\\paragraph{SCB versus CoT unfaithfulness.}\nSCB is distinct from CoT unfaithfulness \\citep{turpin2023language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \\emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias---the constraint $P(\\text{answer\\_A})$ reflects vote share, not logical validity. The shuffle control (\\S\\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.\n\n\\paragraph{Implications for neuro-symbolic practitioners.}\nOur results do not imply that neuro-symbolic methods are inherently flawed---they imply that \\emph{self-extracted} constraints cannot provide independent verification. The key distinction is \\emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \\citep{ye2024satlm}, Logic-LM \\citep{pan2023logiclm}) formalize the problem \\emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\\S\\ref{sec:cross-arch}) and use the diagnostic framework in \\S\\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.\n\n\\paragraph{Test-time scaling implications.}\nVote diversity decreases with model capability: $K_\\text{eff}$ drops from 3.94 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \\citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\\kappa$ analysis (\\S\\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level---traces that disagree on final answers still share 69\\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\\S\\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.\n\n\\paragraph{SCB diagnostic toolkit.}\n\\label{app:diagnostic-toolkit}\nWe recommend four zero-cost diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.\n\\emph{Bias Ratio} (BR; \\S\\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\\text{BR} > 1$ indicates constraints are biased toward the majority; $\\text{BR} \\gg 2$ (as in all nine models tested; Table~\\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\\pm$ bootstrap 95\\% CI.\n\\emph{Effective-K} ($K_\\text{eff}$; Eq.~\\ref{eq:effk}): compute Fleiss' $\\kappa$ across $K$ traces, then $K_\\text{eff} = 1 + (K-1)(1-\\kappa)$. Threshold: $K_\\text{eff} \\leq 1.30$ never improves in our experiments---aggregation collapses to majority voting. $K_\\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.\n\\emph{Degenerate Consensus} ($C_0$; \\S\\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\\%$ renders aggregation moot; $C_0 < 5\\%$ means the model is maximally uncertain and constraints tend to amplify noise.\n\\emph{ProcessSim} (Eq.~\\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\\text{BR} > 2$, this predicts SCB will dominate.\nA practitioner should compute all four on a held-out sample ($n \\geq 50$). If $K_\\text{eff} \\leq 1.30$ or $C_0 > 95\\%$ or ($\\text{BR} > 2$ and $\\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.\n\n\\paragraph{BR permutation null model.}\n\\label{app:br-permutation}\nThe permutation test referenced in \\S\\ref{sec:confirmation-bias} proceeds as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item For each problem $p$ with extracted constraints $\\{c_1, \\ldots, c_M\\}$ and source answers $\\{a_1, \\ldots, a_M\\}$:\n\\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).\n\\item Compute $\\text{BR}_\\text{null}$ from the permuted assignments.\n\\item Repeat $10{,}000$ times to obtain the null distribution.\n\\item Compute $p$-value $= |\\{r : \\text{BR}_\\text{null}^{(r)} \\geq \\text{BR}_\\text{obs}\\}| / 10{,}000$.\n\\end{enumerate}\nAcross all tested conditions, $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.\n\n\\paragraph{Future directions: trained extractors and beyond.}\n\\label{app:future-directions}\nOur oracle controls reveal that perfect extraction would yield $+29.90$\\,pp over SC on Mistral-7B FOLIO---self-extraction captures only ${\\sim}12\\%$ of this ceiling. This gap motivates several future directions.\n\\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence---the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\\S\\ref{sec:cross-arch}).\n\\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\\S\\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.\n\\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.\n\\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.\n\n\\paragraph{SCB as an evaluation framework.}\n\\label{app:scb-evaluation}\nThe SCB metrics---BR, $K_\\text{eff}$, ProcessSim, and CCR---can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \\citep{huang2024selfcorrect}, self-refinement \\citep{madaan2023selfrefine}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-consistency \\citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\\text{BR} < 1$, high $K_\\text{eff}$, and $\\text{CCR} > 0$ demonstrates genuine self-improvement; $\\text{BR} > 1$ with $\\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.\n\n\\paragraph{Additional scope considerations.}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers ($\\forall$/$\\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\\sim}$10\\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 1463,
        "oldLines": 7,
        "newStart": 1463,
        "newLines": 7,
        "lines": [
          " {\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}",
          " \\end{table}",
          " ",
          "-On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
          "+On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
          " ",
          " \\subsection{Sub-population Analysis}",
          " \\label{app:subpopulation}"
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

_source line 30_

Now let me verify the edits and check the data consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "9fc78fae-deb4-4b84-bc9f-f5ceecf18003",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiBczhbHY9XYbQjQH8cyi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 42320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01NBvSTzKUmtrZNaC8QvQfiB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": 1404,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "969d242d-9008-4261-8fc6-f3ed9712b8d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XiBczhbHY9XYbQjQH8cyi6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 42320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 32 · 2026-05-24T13:00:06.289Z_

<details><summary>↩ Tool result · `toolu_01NBvSTzKUmtrZNaC8QvQfiB`</summary>

```text
1404	\begin{table}[h]
1405	\centering
1406	\small
1407	\caption{Multi-seed replication results across six model$\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\times$FOLIO shows directionally unstable $\Delta$ ($+0.16 \pm 2.70$\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\Delta$ ($+0.92 \pm 1.14$\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\S\ref{sec:discussion}).}
1408	\label{tab:multi-seed}
1409	\resizebox{\columnwidth}{!}{%
1410	\begin{tabular}{@{}lrrrr@{}}
1411	\toprule
1412	Seed & SC (\%) & SICA (\%) & $\Delta$ (pp) \\
1413	\midrule
1414	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ FOLIO ($n{=}204$)\textsuperscript{a}}} \\
1415	123 & 54.41 & 57.35 & $+$2.94 \\
1416	456 & 55.88 & 55.88 & 0.00 \\
1417	789 & 59.31 & 56.86 & $-$2.45 \\
1418	\midrule
1419	Mean $\pm$ SD & 56.53 $\pm$ 2.51 & 56.70 $\pm$ 0.75 & $+$0.16 $\pm$ 2.70 \\
1420	\midrule
1421	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ FOLIO ($n{=}204$)}} \\
1422	42 & 77.50 & 75.49 & $-$2.01 \\
1423	123 & 74.51 & 73.04 & $-$1.47 \\
1424	456 & 74.02 & 74.02 & 0.00 \\
1425	789 & 74.02 & 72.55 & $-$1.47 \\
1426	\midrule
1427	Mean $\pm$ SD & 75.01 $\pm$ 1.67 & 73.78 $\pm$ 1.30 & $-$1.24 $\pm$ 0.86 \\
1428	\midrule
1429	\multicolumn{4}{@{}l}{\textit{Mistral-7B $\times$ ProofWriter ($n{=}600$)}} \\
1430	42  & 39.33 & 36.50 & $-$2.83 \\
1431	123 & 40.83 & 37.50 & $-$3.33 \\
1432	456 & 39.83 & 38.50 & $-$1.33 \\
1433	789 & 38.83 & 37.17 & $-$1.67 \\
1434	\midrule
1435	Mean $\pm$ SD & 39.70 $\pm$ 0.85 & 37.42 $\pm$ 0.83 & $-$2.29 $\pm$ 0.95 \\
1436	\midrule
1437	\multicolumn{4}{@{}l}{\textit{LLaMA-3.1-8B $\times$ ProofWriter ($n{=}600$)}} \\
1438	42  & 72.50 & 65.00 & $-$7.50 \\
1439	123 & 71.33 & 64.00 & $-$7.33 \\
1440	456 & 71.67 & 66.17 & $-$5.50 \\
1441	789 & 71.17 & 66.50 & $-$4.67 \\
1442	\midrule
1443	Mean $\pm$ SD & 71.67 $\pm$ 0.59 & 65.42 $\pm$ 1.14 & $-$6.25 $\pm$ 1.34 \\
1444	\midrule
1445	\multicolumn{4}{@{}l}{\textit{Qwen2.5-14B $\times$ ProofWriter ($n{=}600$)}} \\
1446	42  & 74.00 & 71.50 & $-$2.50 \\
1447	123 & 72.33 & 70.83 & $-$1.50 \\
1448	456 & 73.00 & 72.17 & $-$0.83 \\
1449	789 & 73.50 & 71.50 & $-$2.00 \\
1450	\midrule
1451	Mean $\pm$ SD & 73.21 $\pm$ 0.71 & 71.50 $\pm$ 0.55 & $-$1.71 $\pm$ 0.71 \\
1452	\midrule
1453	\multicolumn{4}{@{}l}{\textit{Qwen3-14B $\times$ ProofWriter ($n{=}600$)}} \\
1454	42  & 85.83 & 85.67 & $-$0.17 \\
1455	123 & 85.17 & 86.50 & $+$1.33 \\
1456	456 & 84.50 & 86.83 & $+$2.33 \\
1457	789 & 85.50 & 85.67 & $+$0.17 \\
1458	\midrule
1459	Mean $\pm$ SD & 85.25 $\pm$ 0.57 & 86.17 $\pm$ 0.59 & $+$0.92 $\pm$ 1.14 \\
1460	\bottomrule
1461	\end{tabular}}
1462	\vspace{2pt}
1463	{\footnotesize \textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}
1464	\end{table}
1465	
1466	On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\Delta$ (range $-0.83$ to $-7.50$\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\Delta$ is positive ($+0.92 \pm 1.14$\,pp), revealing a capability-dependent gradient: LLaMA-8B $\Delta{=}-6.25$ $\to$ Mistral-7B $\Delta{=}-2.29$ $\to$ Qwen2.5-14B $\Delta{=}-1.63$ $\to$ Qwen3-14B $\Delta{=}+0.92$\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\Delta$ is slightly positive ($+0.92$\,pp), reflecting the capability-modulated pattern discussed in \S\ref{sec:discussion}---models with SC baselines above 85\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.
1467	
1468	\subsection{Sub-population Analysis}
1469	\label{app:subpopulation}
1470	
1471	\begin{table}[h]
1472	\centering
1473	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "5c6fc276-c6d2-4506-a10f-57bf6b7e64f0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 74.00 & 71.50 & $-$2.50 \\\\\n123 & 72.33 & 70.83 & $-$1.50 \\\\\n456 & 73.00 & 72.17 & $-$0.83 \\\\\n789 & 73.50 & 71.50 & $-$2.00 \\\\\n\\midrule\nMean $\\pm$ SD & 73.21 $\\pm$ 0.71 & 71.50 $\\pm$ 0.55 & $-$1.71 $\\pm$ 0.71 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen3-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 85.83 & 85.67 & $-$0.17 \\\\\n123 & 85.17 & 86.50 & $+$1.33 \\\\\n456 & 84.50 & 86.83 & $+$2.33 \\\\\n789 & 85.50 & 85.67 & $+$0.17 \\\\\n\\midrule\nMean $\\pm$ SD & 85.25 $\\pm$ 0.57 & 86.17 $\\pm$ 0.59 & $+$0.92 $\\pm$ 1.14 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small",
      "numLines": 70,
      "startLine": 1404,
      "totalLines": 1591
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The edits look good. Now let me check the data consistency.

For modification 3 - Qwen2.5-14B FOLIO SC data verification:

**tab:multi-seed** (appendix.tex L1422): Qwen2.5-14B FOLIO seed42 SC = 77.50 ✓

**tab:independence** (diagnosis.tex L70): Qwen2.5-14B FOLIO SC = 75.98

Now I need to figure out if the 75.98 for Qwen2.5-14B in diagnosis.tex and other places is correct or wrong. 

Looking at the main results table in experiments.tex, there's no single-seed Qwen2.5-14B FOLIO entry—only the 4-seed aggregate showing 75.01. But diagnosis.tex has a single-seed entry with SC=75.98, which suggests it's from the original table before the multi-seed expansion. I need to determine whether this 75.98 value should be updated to match the seed42 value of 77.50.

The task instructions seem contradictory—it says to fix the 75.98 if it's wrong for Qwen2.5-14B, but also says not to modify other tables. I think the primary focus is verifying the multi-seed table and its caption, and the instruction about fixing 75.98 applies only if it's genuinely incorrect for that model.

Since I don't have direct access to the experiment registry beyond what's provided, I should report what I find: confirm the three edits are complete, document where 75.98 appears in the Qwen2.5-14B rows, and note whether it matches the registry data or represents a potential error that needs correction.

I'm also noticing some redundancy in the analysis paragraph where Qwen3-14B's positive delta is mentioned twice in slightly different ways—I should streamline that to avoid the repetition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "e723aebf-9d48-4d7a-98da-ea67f0a21580",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5ga4CtEA9sDVZJt152Pz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 42685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2293
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

_source line 34_

The paragraph reads slightly redundant now — "Qwen3-14B is the only condition" then "Qwen3-14B is the sole exception" back to back. Let me tighten it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "ea6782bd-6242-4cf5-8221-17fcb1ab5eca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5ga4CtEA9sDVZJt152Pz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 42685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2293
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_014XN4SutyS6cxYjbdHHFLLH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "old_string": "On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
  "new_string": "On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The results reveal a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92 \\pm 1.14$\\,pp, all n.s.), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "bf70fd0b-4ba3-42d1-94b1-51549b7cc30d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5ga4CtEA9sDVZJt152Pz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2293,
      "cache_read_input_tokens": 42685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2293
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

_source line 36 · 2026-05-24T13:00:38.547Z_

<details><summary>↩ Tool result · `toolu_014XN4SutyS6cxYjbdHHFLLH`</summary>

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
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "325b52b3-22db-4fc2-8ef1-0b4bfe717250",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "oldString": "On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
    "newString": "On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The results reveal a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92 \\pm 1.14$\\,pp, all n.s.), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
    "originalFile": "\\section{Prompt Templates}\n\\label{app:prompts}\n\nSICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).\n\n\\paragraph{System Prompt.}\n\n\\begin{lstlisting}\nYou are a constraint extraction tool. Output ONLY\nvalid JSON. Do NOT solve problems, reason about\ncorrectness, or think step-by-step. Extract\nconstraints from the given trace exactly as stated.\n\\end{lstlisting}\n\n\\paragraph{Mathematical Constraint Extraction (EXTRACTION\\_PROMPT).}\n\nUsed for GSM8K and AIME datasets. The placeholder \\texttt{\\{trace\\}} is replaced with the reasoning trace at runtime.\n\n\\begin{lstlisting}\nExtract mathematical constraints from this reasoning\ntrace as a JSON object.\n\nRules:\n- type: \"equation\", \"inequality\", or \"predicate\"\n- expression: human-readable, e.g. \"x + y == 14\"\n- z3_formula: a single comparison expression in\n  Python Z3 syntax\n- source_step: step number where the constraint\n  appears\n- Use variable names from the trace\n\nz3_formula MUST follow these rules:\n- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,\n  /, **, %\n- Use individual named variables: a1, a2, a3...\n  NOT arrays a[1] or sets A\n- Expand all sums explicitly:\n  \"a1 + a2 + a3 == 55\" NOT \"sum([a1,a2,a3])\"\n- NO Python builtins: sum(), len(), max(), min(),\n  list(), set(), range(), int()\n- Each z3_formula must be exactly ONE comparison\n  (==, !=, <, >, <=, >=)\n- For multiple values, write separate constraints\n  for each\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"equation\",\n  \"expression\": \"x + y == 14\",\n  \"z3_formula\": \"x + y == 14\",\n  \"source_step\": 1}],\n \"answer\": \"final_answer\",\n \"variables\": [\"x\", \"y\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Logical Constraint Extraction (LOGIC\\_EXTRACTION\\_PROMPT).}\n\nUsed for ProofWriter and FOLIO datasets.\n\n\\begin{lstlisting}\nIMPORTANT: You are an EXTRACTION tool, NOT a problem\nsolver.\n- Do NOT re-solve or re-reason about the problem.\n- Do NOT verify whether the trace's reasoning is\n  correct.\n- ONLY extract the logical constraints that are\n  explicitly stated or used in the trace below.\n- Output ONLY the JSON object, nothing else.\n\nExtract logical constraints from this reasoning trace\nabout a logic problem.\n\nThe problem has facts (base assertions), rules\n(grounded implications), and derived conclusions.\nConvert each into a Z3 boolean formula.\n\nVariable naming:\n- Unary property: property_entity\n  (e.g., kind_anne, red_charlie, round_fiona)\n- Binary relation: relation_subject_object\n  (e.g., eats_bear_squirrel, likes_lion_cat)\n- Use lowercase with underscores only\n\nConstraint types:\n- \"fact\": a given assertion,\n  e.g., kind_anne == True\n- \"rule\": a grounded implication over specific\n  entities, e.g., Implies(kind_anne, nice_anne)\n- \"derived\": an inferred conclusion from facts +\n  rules, e.g., nice_anne == True\n\nZ3 operators:\n- Implies(a, b) for if-then rules\n- And(a, b, ...) for conjunctive conditions\n- Or(a, b, ...) for disjunctive conditions\n- Not(a) for negation\n- == True / == False for boolean assertions\n\nOutput ONLY the JSON below, nothing else:\n{\"constraints\": [{\"type\": \"fact\",\n  \"expression\": \"kind(anne)\",\n  \"z3_formula\": \"kind_anne == True\",\n  \"source_step\": 1}],\n \"answer\": \"True or False or Unknown\",\n \"variables\": [\"kind_anne\"]}\n\nTrace:\n{trace}\n\\end{lstlisting}\n\n\\paragraph{Output Schema.}\n\nBoth prompts produce a JSON object with the following structure:\n\n\\begin{lstlisting}\n{\n  \"constraints\": [\n    {\n      \"type\": \"&lt;equation|inequality|predicate>\n               or &lt;fact|rule|derived>\",\n      \"expression\": \"&lt;human-readable description>\",\n      \"z3_formula\": \"&lt;Z3-compatible expression>\",\n      \"source_step\": &lt;integer>\n    }\n  ],\n  \"answer\": \"&lt;final answer string>\",\n  \"variables\": [\"&lt;var1>\", \"&lt;var2>\", \"...\"]\n}\n\\end{lstlisting}\n\nThe pipeline additionally injects an \\texttt{answer\\_assertion} constraint per trace (not produced by the LLM):\n\n\\begin{lstlisting}\n{\"type\": \"answer_assertion\",\n \"expression\": \"answer is &lt;ans>\",\n \"z3_formula\": \"__sica_answer_&lt;ans> == True\",\n \"source_step\": -1}\n\\end{lstlisting}\n\n\\paragraph{Prompt Selection Logic.}\n\nDomain assignment is determined by dataset: FOLIO and ProofWriter use \\textsc{Logic\\_Extraction\\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \\textsc{Extraction\\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.\n\n\n\\section{Z3 MaxSAT Evaluation Pseudocode}\n\\label{app:z3-pseudocode}\n\nAlgorithm~\\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\\ref{alg:scorer} describes the source-trace attribution scoring.\n\nDomain constraint variables (e.g., \\texttt{x + y == 14}) and answer assertion variables (e.g., \\texttt{\\_\\_sica\\_answer\\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.\n\n\\begin{algorithm}[h]\n\\caption{Z3 Weighted Partial MAX-SAT}\n\\label{alg:maxsat}\n\\begin{algorithmic}[1]\n\\Require Deduplicated constraint set $\\mathcal{C} = \\{(c_m, w_m, S_m)\\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices\n\\Ensure Partition $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$ where $\\mathcal{C}^*$ is the max-weight satisfiable subset\n\\State $\\textit{opt} \\gets \\textsc{Z3.Optimize()}$\n\\For{$m = 1, \\ldots, M$}\n    \\State $b_m \\gets$ fresh Boolean indicator\n    \\State $\\textit{opt}.\\textsc{Add}(b_m \\Rightarrow c_m)$ \\Comment{soft clause guarded by indicator}\n    \\State $\\textit{opt}.\\textsc{AddSoft}(b_m,\\; \\text{weight}=w_m)$\n\\EndFor\n\\State $\\textit{result} \\gets \\textit{opt}.\\textsc{Check}()$\n\\State $\\textit{model} \\gets \\textit{opt}.\\textsc{Model}()$\n\\State $\\mathcal{C}^* \\gets \\{(c_m, w_m, S_m) : \\textit{model}(b_m) = \\top\\}$\n\\State $\\mathcal{C}^{\\setminus} \\gets \\mathcal{C} \\setminus \\mathcal{C}^*$\n\\State \\Return $(\\mathcal{C}^*, \\mathcal{C}^{\\setminus})$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\begin{algorithm}[h]\n\\caption{Source-Trace Attribution Scoring}\n\\label{alg:scorer}\n\\begin{algorithmic}[1]\n\\Require Satisfied set $\\mathcal{C}^*$, excluded set $\\mathcal{C}^{\\setminus}$, candidate answers $\\mathcal{A}$, trace-answer mapping $\\tau: \\text{trace\\_idx} \\to a$, penalty weight $\\alpha$\n\\Ensure Score $s(a)$ for each $a \\in \\mathcal{A}$\n\\For{each $a \\in \\mathcal{A}$}\n    \\State $T_a \\gets \\{i : \\tau(i) = a\\}$ \\Comment{trace indices producing answer $a$}\n    \\State $\\textit{pos}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^*} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $\\textit{neg}(a) \\gets \\sum_{(c,w,S) \\in \\mathcal{C}^{\\setminus}} w \\cdot \\mathbf{1}[S \\cap T_a \\neq \\emptyset]$\n    \\State $s(a) \\gets \\textit{pos}(a) - \\alpha \\cdot \\textit{neg}(a)$\n\\EndFor\n\\State \\Return $a^* = \\arg\\max_{a \\in \\mathcal{A}} s(a)$\n\\end{algorithmic}\n\\end{algorithm}\n\n\n\\section{Capability-Accuracy Constraint Diagnostics}\n\\label{app:diagnostics}\n\\label{app:cil}\n\n\\paragraph{Conditional Correction Ratio.}\nWe define the \\textit{Conditional Correction Ratio} (CCR) to summarize verifier--generator complementarity:\n\\begin{equation}\n\\label{eq:cil}\n\\text{CCR}(V, G) = \\log \\frac{P(V \\text{ correct} \\mid G \\text{ wrong})}{P(V \\text{ correct} \\mid G \\text{ correct})}.\n\\end{equation}\n$\\text{CCR} > 0$ means $V$ preferentially corrects $G$'s errors; $\\text{CCR} < 0$ indicates shared bias. CCR links our findings: (1)~SCB corresponds to $\\text{CCR}(\\text{self}, G) \\approx 0$; (2)~Finding~2 predicts $\\text{CCR}(V, G) > 0$ when $V$ is independent and capable.\n\n\\paragraph{Empirical CCR across verifier--generator pairs.}\nTable~\\ref{tab:cil_empirical} reports CCR for eight verifier--generator--dataset conditions, sorted by CCR descending. All three cross-architecture NLI pairs on ProofWriter yield $\\text{CCR} > 0$ (verifier preferentially corrects generator errors), while all three same-model SICA conditions yield $\\text{CCR} < 0$ (shared bias). CCR correlates with combo gain: Spearman $\\rho = 0.839$, 95\\% bootstrap CI $[0.338, 0.990]$; LOO-robust (min $p = 0.014$). Four of eight conditions share the DeBERTa verifier, yielding effective $n < 10$; results should be interpreted as a consistent pattern rather than a precise effect size.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical CCR across eight verifier--generator conditions (sorted by CCR descending). $\\text{CCR} > 0$: cross-architecture NLI verifiers on ProofWriter. $\\text{CCR} < 0$: same-model SICA or mismatched capability gap.}\n\\label{tab:cil_empirical}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllrr@{}}\n\\toprule\nGenerator & Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & BART-MNLI & PW-600 & $+$1.86 & $+$5.17 \\\\\nMistral-7B & DeBERTa-MNLI & PW-600 & $+$1.67 & $+$6.67 \\\\\nMistral-7B & RoBERTa-MNLI & PW-600 & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen2.5-14B & DeBERTa-MNLI & PW-600 & $-$0.21 & $+$0.33 \\\\\nMistral-7B & DeBERTa-MNLI & FOLIO-204 & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral-7B & SICA & FOLIO-204 & $-$2.93 & $+$3.43 \\\\\nQwen2.5-14B & SICA & PW-600 & $-$4.21 & $-$2.50 \\\\\nMistral-7B & SICA & PW-600 & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-condition diagnostics.}\nTable~\\ref{tab:capability_trap} reports per-condition diagnostic metrics referenced in \\S\\ref{sec:entropy}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Domain & $C_0$ (\\%) & Extr.\\ Rate & Contr.\\ Rate & $\\Delta$ (pp) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 35.3 & 0.89 & 0.022 & 0.00 \\\\\nQwen2.5-14B & ProofWriter & 39.2 & 0.89 & 0.022 & $+$0.33 \\\\\nQwen2.5-14B & StrategyQA$^\\dagger$ & 10.0 & 0.70 & --- & $+$3.33 \\\\\nQwen2.5-14B & ARC-Chall.$^\\dagger$ & 5.0 & 1.00 & --- & $-$1.67 \\\\\nQwen2.5-7B & FOLIO+PW$^\\dagger$ & 42.1 & 0.94 & 0.027 & 0.00 \\\\\nMistral-7B & FOLIO+PW$^\\dagger$ & 50.0 & 0.88 & 0.056 & 0.00 \\\\\nLLaMA-3.1-8B & StrategyQA & 41.0 & --- & --- & $+$2.00 \\\\\nLLaMA-3.1-8B & FOLIO & 61.8 & 0.94 & 0.062 & $-$4.41 \\\\\nDeepSeek-R1-7B & FOLIO+PW$^\\dagger$ & 58.3 & 0.84 & 0.037 & $-$3.33 \\\\\nQwQ-32B & Combined$^\\dagger$ & 2.6 & --- & --- & 0.00 \\\\\nQwen2.5-14B & GSM8K$^\\dagger$ & 13.3 & 0.15 & --- & 0.00 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Capability-accuracy constraint diagnostics. $C_0$: fraction of questions with multiple distinct candidate answers across $K=12$ traces. Extraction rate: fraction of traces yielding at least one parseable logical constraint. Contradiction rate: fraction of extracted constraint sets with internal contradictions. $\\Delta$: SICA$-$SC gap (pp). $\\dagger$: $n \\leq 60$. Dashes indicate conditions where extraction diagnostics were not computed (StrategyQA uses boolean answers without symbolic extraction; QwQ-32B Combined had near-zero $C_0$, making extraction analysis uninformative). This table includes additional exploratory conditions not reported in Table~\\ref{tab:main_results}.}\n\\label{tab:capability_trap}\n\\end{table}\n\n\n\\section{Statistical Power Analysis}\n\\label{app:power}\n\nWe compute the minimum detectable effect (MDE) for each condition at $\\alpha = 0.05$ and 80\\% power using exact binomial power calculations over McNemar discordant pairs. Table~\\ref{tab:power} reports three grouped conditions with $n \\geq 200$ (Qwen2.5-14B FOLIO and ProofWriter are pooled into a single $n{=}804$ analysis, corresponding to four Table~\\ref{tab:main_results} rows), which constitute our confirmatory analyses. The remaining seven conditions ($n \\leq 60$) yield infinite MDE due to insufficient discordant pairs and serve only as regime characterization.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{MDE} & \\textbf{Obs.\\ $\\Delta$} & \\textbf{Obs.\\ Pow.} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & 1.86pp & $+$0.25pp & 5.7\\%  \\\\\nLLaMA-8B StrategyQA  & 200 & 4.64pp & $+$2.00pp & 20.6\\% \\\\\nLLaMA-8B FOLIO       & 204 & 4.84pp & $-$4.41pp & 18.6\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Power analysis for confirmatory conditions ($n \\geq 200$). MDE = minimum detectable effect at 80\\% power. All observed effects fall below their respective MDEs, and observed power remains below 21\\% in every case.}\n\\label{tab:power}\n\\end{table}\n\nThe largest study (Qwen-14B, $n{=}804$, 30 discordant pairs) can detect effects as small as 1.86pp, yet the observed $\\Delta$ of $+$0.25pp is an order of magnitude smaller. The two LLaMA-8B conditions require effects of 4.64pp and 4.84pp to reach significance; neither observed $\\Delta$ approaches these thresholds. All three conditions are consistent with the null hypothesis that SICA provides no accuracy gain over self-consistency.\n\n\n\\section{Bootstrap Confidence Intervals}\n\\label{app:bootstrap}\n\nWe compute 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ via 10{,}000 bootstrap resamples (percentile method, seed 42). Table~\\ref{tab:bootstrap} reports the results for the three confirmatory conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrl}\n\\toprule\n\\textbf{Condition} & $n$ & \\textbf{Obs.\\ $\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen-14B FOLIO+PW   & 804 & $+$0.25pp & [$-$1.12, $+$1.62] \\\\\nLLaMA-8B StrategyQA  & 200 & $+$2.00pp & [$-$1.50, $+$5.50] \\\\\nLLaMA-8B FOLIO       & 204 & $-$4.41pp & [$-$5.88, $+$0.98] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Bootstrap 95\\% confidence intervals for $\\Delta(\\text{SICA} - \\text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}\n\\label{tab:bootstrap}\n\\end{table}\n\nAll three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.\n\n\n\\section{Case Studies: Discordant Predictions}\n\\label{app:case-studies}\n\nAmong 804 problems, SICA and SC agree on 773 (96.1\\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.\n\n\\paragraph{Case 1: SICA Wins (folio\\_134, FOLIO).}\n\n\\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \\emph{Conclusion}: Humans are mammals. \\emph{Gold}: Unknown.\n\nThe premises state that \\emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing the weighted score for True-voting traces and tipping the aggregation to Unknown (correct). The excluded constraint likely captured an incorrect inference step (e.g., affirming the consequent) present only in True-voting traces. While SICA succeeds here, the success is coincidental: the excluded constraint happens to anti-correlate with the correct answer.\n\n\\paragraph{Case 2: SC Wins (ProofWriter-1066\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: White(Bob)$\\to$Round(Bob) [white things are round] $\\to$ Young(Bob) [all round things are young]. \\emph{Conclusion}: ``Bob is not young.'' \\emph{Gold}: False (Bob IS young).\n\nSC produces a 6:6 split (False:6, True:6) and tiebreaks to False (correct). SICA extracts 17 constraints; MaxSAT excludes 2 that appear preferentially in False-voting traces. These excluded constraints likely captured correct intermediate derivations (e.g., \\texttt{young\\_bob == True}) that appeared only in traces completing the full deduction chain. By excluding them, MaxSAT removes evidence supporting the correct answer. SICA selects True (wrong). This case illustrates how self-extracted constraints can systematically mislead: correct reasoning steps become discriminative signals that the solver mistakenly penalizes.\n\n\\paragraph{Case 3: Non-discriminative Constraints (ProofWriter-903\\_Q6, ProofWriter).}\n\n\\emph{Key chain}: Nice(Mouse)$\\to$Cold(Mouse) [all nice people are cold] $\\to$ Chases(Mouse,Mouse) [nice and cold $\\to$ chase mouse]. \\emph{Conclusion}: ``The mouse does not chase the mouse.'' \\emph{Gold}: False.\n\nSC produces a 6:6 split (False:6, Unknown:6) and tiebreaks to False (correct). SICA extracts 44 constraints but excludes only 1 (2.3\\%). The remaining 43 are domain facts and grounded rules (\\texttt{nice\\_mouse == True}, \\texttt{Implies(nice\\_mouse, cold\\_mouse)}, etc.) that Z3 satisfies identically regardless of the final answer. Both False-voting and Unknown-voting traces share the same premises and grounded rules; they differ only in whether the trace completed the full derivation chain. The single excluded constraint carries negligible weight against 43 shared constraints, so SICA collapses to SC.\n\n\\paragraph{Pattern.}\n\nThese cases exemplify the general pattern across the 773 agreeing problems: the vast majority of extracted constraints encode shared domain structure rather than answer-specific reasoning, and MaxSAT aggregation degenerates to majority vote. Table~\\ref{tab:case_summary} summarizes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Summary of three representative discordant cases. All occur at exact 6:6 vote ties. Constraint exclusion can break ties in either direction (Cases 1--2) or have no effect (Case 3).}\n\\label{tab:case_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lllcccc@{}}\n\\toprule\nCase & ID & Gold & SC & SICA & \\#Constr. & Excl.\\ (\\%) \\\\\n\\midrule\n1 (SICA win) & folio\\_134 & Unknown & True $\\times$ & Unknown $\\checkmark$ & 7 & 1 (14.3\\%) \\\\\n2 (SC win) & PW-1066\\_Q6 & False & False $\\checkmark$ & True $\\times$ & 17 & 2 (11.8\\%) \\\\\n3 (Non-disc.) & PW-903\\_Q6 & False & False $\\checkmark$ & False $\\checkmark$ & 44 & 1 (2.3\\%) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Oracle Control}\n\\label{app:oracle}\n\\label{sec:oracle}\n\\label{app:pw-oracle-subtype}\n\nReplacing self-extracted constraints with gold annotations (FOLIO logical formulae, ProofWriter DSL), Oracle-SICA yields $+29.90$\\,pp on Mistral-7B FOLIO ($p < 10^{-13}$), $+13.73$\\,pp on Qwen2.5-14B FOLIO ($p = 2.0 \\times 10^{-7}$), and $+17.17$\\,pp on ProofWriter ($p < 10^{-14}$). Z3 agrees with gold labels on 95.1\\% (FOLIO) and 97.1\\% (ProofWriter). The MAX-SAT mechanism is sound; Mistral-7B's best self-extracted $\\Delta$ ($+3.43$\\,pp) captures only 11.5\\% of its oracle ceiling. For Qwen2.5-14B on ProofWriter, the gap is wider still: self-extraction degrades accuracy ($-2.50$\\,pp) against an oracle ceiling of $+17.17$\\,pp, indicating that stronger models do not self-extract more effectively.\n\n\\paragraph{ProofWriter per-subtype analysis.} ProofWriter problems encode deductive rules as Domain-Specific Language (DSL) logic programs. Each problem uses one of four predicate subtypes: attribute predicates with or without negation (AttNeg, AttNoneg), and relation predicates with or without negation (RelNeg, RelNoneg). Relation predicates involve binary relations between entities (e.g., \\texttt{eats(bear, squirrel)}), while attribute predicates assign unary properties (e.g., \\texttt{kind(anne)}).\n\nThe oracle pipeline parses these DSL annotations deterministically into Z3 formulas without any LLM involvement. Of the 600 ProofWriter problems, 594 (99.0\\%) produce valid Z3 parses; the remaining 6 fail due to unsupported DSL constructs. Across all 7{,}128 trace-problem pairs submitted to Z3, the solver returns a result in every case (0\\% solver errors). Z3 evaluations agree with ground-truth labels on 577 of 594 parseable problems (97.14\\%), confirming that the deterministic DSL-to-Z3 translation faithfully preserves problem semantics.\n\nTable~\\ref{tab:pw_oracle_subtype} reports the per-subtype breakdown. Relation-predicate subtypes show substantially larger gains than attribute-predicate subtypes: RelNeg improves by $+28.58$~pp and RelNoneg by $+23.29$~pp, compared to $+10.00$~pp for AttNeg and $+8.44$~pp for AttNoneg. Relation predicates involve longer reasoning chains with more intermediate entities, producing greater answer diversity across traces ($C_0$) and more opportunities for oracle constraints to correct errors.\n\n\\begin{table}[h]\n\\centering\n\\caption{ProofWriter oracle experiment per-subtype breakdown. Oracle-SICA uses gold DSL annotations parsed deterministically to Z3 for consistency checking. Relation-predicate subtypes (RelNeg, RelNoneg) show larger gains than attribute-predicate subtypes; relation subtypes involve longer reasoning chains and benefit more from oracle constraints. Bold indicates best accuracy per row.}\n\\label{tab:pw_oracle_subtype}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nSubtype & $n$ & SC Acc (\\%) & Oracle Acc (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nAttNoneg & 154 & 90.26 & \\textbf{98.70} & +8.44 \\\\\nAttNeg & 160 & 81.88 & \\textbf{91.88} & +10.00 \\\\\nRelNoneg & 146 & 60.96 & \\textbf{84.25} & +23.29 \\\\\nRelNeg & 140 & 60.71 & \\textbf{89.29} & +28.58 \\\\\n\\midrule\nOverall & 600 & 74.00 & \\textbf{91.17} & +17.17 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Constraint Ablation Details}\n\\label{app:ablation}\n\\label{sec:ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint ablation (Qwen2.5-14B, $n = 804$). Agreement: predictions identical to SC. MAX-SAT and count-only produce nearly identical predictions, confirming that self-extracted constraints carry no signal beyond vote counts.}\n\\label{tab:ablation}\n\\begin{tabular}{@{}lrc@{}}\n\\toprule\nAggregation & Acc.\\ (\\%) & Agreement w/ SC \\\\\n\\midrule\nSC (majority vote) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & 773\\,/\\,804 \\\\\nCount-only & 76.62 & 774\\,/\\,804 \\\\\nRandom-weight & 75.87 & 764\\,/\\,804 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAX-SAT vs.\\ count-only agreement across constraint weight $\\alpha \\in [0,1]$ on FOLIO ($n = 204$). Mistral-7B (BR $= 4.97\\times$, seed 42); Qwen2.5-14B (BR $= 3.85\\times$, seed 123). $\\alpha{=}0$: pure Z3 satisfiability (no source-attribution); $\\alpha{=}1$: full source-attribution penalty. Agreement $\\geq 99\\%$ at all $\\alpha$ including endpoints, confirming vacuity is weight-insensitive.}\n\\label{tab:alpha-ablation}\n\\begin{tabular}{@{}crr@{}}\n\\toprule\n$\\alpha$ & Mistral Agr.\\ (\\%) & Qwen2.5 Agr.\\ (\\%) \\\\\n\\midrule\n0.0 & 100 & 100 \\\\\n0.1 & 100 & 100 \\\\\n0.3 & 100 & 100 \\\\\n0.5 & 100 & 100 \\\\\n0.7 & 99 & 100 \\\\\n0.9 & 99 & 100 \\\\\n1.0 & 99 & 100 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Remediation Strategy Details}\n\\label{app:remediation}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_interventions_compact.pdf}\n\\caption{Twenty-three of 27 training-free strategies across four categories (four additional strategies tested but omitted for clarity). All produce neutral-to-negative $\\Delta$ vs.\\ SC. Grey band: $\\pm 1$\\,pp noise zone.}\n\\label{fig:interventions-summary}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Nine prompt-level remediation strategies. Baseline: Qwen2.5-14B FOLIO, SC $= 75.98\\%$, $\\Delta = -0.49$\\,pp. None reaches significance. Three method-level strategies are reported in Table~\\ref{tab:method_interventions}.}\n\\label{tab:remediation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrl@{}}\n\\toprule\nStrategy & Target & $\\Delta$ (pp) & Key finding \\\\\n\\midrule\nContrastive$^a$ & Prompt & $-$1.10 & non-disc.\\ 6.0\\% ($\\downarrow$ from 8.2\\%) \\\\\nCross-model$^b$ & Architecture & 0.00 & disc.\\ 0\\% (weak$\\to$strong); $\\pm$1\\,pp (strong$\\to$weak) \\\\\nQwen3-14B$^c$ & Capability & $-$0.49 & $p = 0.655$ \\\\\nZ3 feedback & Solver & --- & 0.9\\% UNSAT trigger \\\\\nCons.\\ filtering & Noise & 0.00 & $T{\\geq}4 \\to$ SC \\\\\nCross-trace UNSAT & Independence & --- & 56.4\\% $\\emptyset$ vars \\\\\n$T{=}1.0$$^d$ & Diversity & 0.00 & isolated peak at $T{=}0.7$ only \\\\\nMulti-temp$^e$ & Diversity & 0.00 & $b{=}5$, $c{=}5$ (balanced) \\\\\nDisc.\\ filtering$^f$ & Filtering & 0.00 & 803/804 agree w/ SICA \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize $^a$\\,$n{=}182$ (extraction failures excluded). $^b$\\,Weak$\\to$strong: Mistral-7B extracts from Qwen2.5-14B traces. Strong$\\to$weak: Qwen3-14B (60.29\\%) and Qwen2.5-14B (58.33\\%) extract from Mistral-7B FOLIO traces ($n{=}204$); self-extraction baseline 59.31\\%. $^c$\\,$n{=}204$, SC $= 83.33\\%$. $^d$\\,Mistral-7B FOLIO, $n{=}204$. $^e$\\,Mistral-7B FOLIO, $T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each, $n{=}204$. $^f$\\,Qwen2.5-14B, $n{=}804$; removing non-discriminative constraints.}\n\\end{table}\n\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Method-level interventions on Mistral-7B with McNemar's paired test. All produce neutral-to-catastrophic results. ICG shows two FOLIO seeds; $p$ for the first. {*}{*}{*}\\,$p < 0.001$; {*}{*}\\,$p < 0.01$.}\n\\label{tab:method_interventions}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}ll rc rc@{}}\n\\toprule\n& & \\multicolumn{2}{c}{FOLIO ($n = 204$)} & \\multicolumn{2}{c}{LogiQA ($n = 200$)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nMethod & Target & $\\Delta$ (pp) & $p$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nSC baseline & --- & 0.00 & --- & 0.00 & --- \\\\\nICG & Trace coupling & $-$1.96\\,/\\,$+$1.47 & .206 & $-$0.50 & .706 \\\\\nContrastive & Scoring bias & $\\mathbf{-9.31}$ & .007 & $-$4.50 & .160 \\\\\nDebate & Role diversity & $\\mathbf{-18.63}$ & ${<}.001$ & $\\mathbf{-23.00}$ & ${<}.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Additional Intervention Results}\n\\label{app:additional-interventions}\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Additional intervention results beyond the nine prompt-level and three method-level strategies reported in the main text. All produce neutral-to-negative results, completing the exhaustive remediation analysis across 27 distinct approaches.}\n\\label{tab:additional_interventions}\n\\begin{tabular}{@{}llllrl@{}}\n\\toprule\n\\# & Method & Type & Target & $\\Delta$ (pp) & Key Finding \\\\\n\\midrule\n13 & PROVE (code verif.) & Paradigm & Formal proof & $-$1.9 & 15.2\\% compilable; conclusive acc.\\ = 50\\% \\\\\n14 & CEGIS (iterative) & Multi-round & Consistency & 0.0$^\\dagger$ & R1 $+$3.43\\,pp then oscillates \\\\\n15 & DeepConf (logprob) & Filtering & Confidence & 0.0 & $\\Delta_{\\text{logprob}} = 0.006$ (no separation) \\\\\n16 & Cross-model SICA & Cross-model & Independence & $-$0.49 & $\\kappa_{\\text{cross}}{=}0.42$ vs $\\kappa_{\\text{within}}{=}0.53$ \\\\\n17 & Problem perturbation & Input diversity & Trace diversity & $<$0 & $\\kappa$ \\emph{increased} to 0.70 (anti-effect) \\\\\n18 & MIN-UNSAT & Solver objective & Constraint sel.\\ & $-$6.5 & Mean excluded constraints $= 1.3$ \\\\\n19 & $\\kappa$-aware SC & Voting rule & Weighted voting & 0.0 & 11/11 conditions $\\Delta = 0$ \\\\\n20 & Z3 trace filter & Trace filtering & Quality & $-$0.49 & Precision 49.1\\%, 7 questions affected \\\\\n21 & Bootstrapped gold & Iterative & Self-improvement & 0.0$^\\dagger$ & R1 $+$2.45\\,pp then oscillates \\\\\n22 & Selective abstention & Diagnostic & Confidence & $+$4.4$^*$ & AUROC $= 0.673$, at 80\\% coverage \\\\\n23 & ASCII perturbation & Input diversity & Format diversity & 0.0 & $\\kappa$: $0.39 \\to 0.36$ (negligible) \\\\\n\\addlinespace\n24 & Atom pipeline & Paradigm & Decomposition & $-$10.0 & Atomic extraction degrades \\\\\n25 & Premise-only filter & Constraint sel.\\ & Bias isolation & $+$2.45 & $p = 0.359$; halves conclusion-bias \\\\\n26 & DPP trace selection & Trace diversity & Determinantal & $+$1.47 & $p = 0.629$; $K_{\\text{sel}}{=}8$ \\\\\n27 & Z3 strict-mode & Solver config & UNSAT filtering & 0.0 & McNemar $b{=}1, c{=}1$; 63\\% UNSAT \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All experiments on Mistral-7B FOLIO ($n{=}204$) unless noted. $^\\dagger$\\,Oscillates without convergence; net effect $\\approx 0$. $^*$\\,Accuracy gain only at reduced coverage (diagnostic value, not a general improvement). Methods 1--12 are reported in Table~\\ref{tab:remediation} and Table~\\ref{tab:method_interventions}.}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_process_kappa_scatter.pdf}\n\\caption{Answer agreement vs.\\ CoT cosine similarity (Mistral-7B, FOLIO, $n{=}204$). Flat regression ($r = -0.06$, $p = 0.36$); stronger models show significant positive correlation ($r = +0.24$, Qwen-14B; Table~\\ref{tab:cross-model-process}).}\n\\label{fig:process-kappa}\n\\end{figure}\n\n\n\\section{Extraction Error Taxonomy}\n\\label{app:extraction}\n\\label{sec:extraction-taxonomy}\n\nConstraints must discriminate between candidate answers for MAX-SAT to produce a ranking different from majority vote. We measure discriminative power at two levels on Qwen2.5-14B across FOLIO and ProofWriter ($n = 804$). At the source-trace level, 39.2\\% of total constraint weight originates from traces whose answer differs from the plurality, but only 12.1\\% of individual constraints fall into this minority category. At the Z3 semantic level, 91.8\\% of constraints [95\\% CI: 91.2, 92.4] are technically discriminative, producing different satisfiability outcomes when evaluated against different candidate answers. Only 8.2\\% are non-discriminative.\n\nThe high discriminative rate does not translate into accuracy gains because discrimination mirrors the model's own answer distribution. Each trace produces constraints with its own variable names, so Z3 treats identically-intended propositions as unrelated symbols; among cross-answer constraint pairs, 56.4\\% share zero Z3 variables. This variable isolation means constraints from different traces are trivially jointly satisfiable, and MAX-SAT retains nearly all of them regardless of source answer. Removing the 8.2\\% non-discriminative constraints yields zero accuracy improvement. The discriminative majority does not provide independent signal; it reinforces the majority answer that SC would already select. This confirmation bias, not a lack of discrimination, explains why SICA degenerates to majority voting (Appendix~\\ref{app:ablation}).\n\n\n\\section{Hyperparameter Sensitivity}\n\\label{app:sensitivity}\n\\label{sec:k-sensitivity}\n\\label{sec:t-sensitivity}\n\n\\subsection{K Sensitivity}\n\nFigure~\\ref{fig:k-sensitivity} shows SICA $\\Delta$ as a function of the number of sampled traces $K$ for Mistral-7B on FOLIO ($n = 204$, no fixed seed). The relationship is non-monotonic: $K = 4$ yields $\\Delta = -1.47$\\,pp, $K = 8$ yields $\\Delta = -1.96$\\,pp, $K = 12$ reaches $\\Delta = +3.43$\\,pp, $K = 16$ drops to $\\Delta = +1.47$\\,pp, and $K = 20$ partially recovers to $\\Delta = +1.96$\\,pp. The recovery at $K = 20$ rules out a simple peaked pattern, but $K = 12$ remains the only setting with $\\Delta > 2$\\,pp ($p = 0.092$, marginal).\n\nThe apparent $\\Delta$ peak at $K = 12$ is confounded with SC baseline. SICA absolute accuracy plateaus at 59.31\\% (121/204) for $K \\geq 12$: identical at $K = 12$ and $K = 20$. The $\\Delta$ variation across these settings is driven primarily by SC fluctuations rather than by SICA improvement. $K = 12$ produces a relatively low SC (55.88\\%), placing it in the intermediate-SC region; $K = 8$ (SC $= 58.33\\%$) and $K = 20$ (SC $= 57.35\\%$) have higher baselines, compressing $\\Delta$ even though SICA accuracy does not change for $K \\geq 12$. Additional traces beyond $K = 12$ provide no benefit to SICA absolute performance, consistent with the constraint quality bottleneck. The $K = 12$ $\\Delta$ captures only 25.0\\% of the oracle ceiling ($+13.73$\\,pp).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{f3_k_sensitivity}\n\\caption{SICA $\\Delta$ (pp) vs.\\ number of traces $K$ for Mistral-7B on FOLIO ($n = 204$, default seed, $T = 0.7$). Non-monotonic pattern: SICA accuracy plateaus at 59.31\\% for $K \\geq 12$; the apparent $\\Delta$ peak at $K = 12$ partly reflects a relatively low SC baseline (55.88\\%) at that point. Error bars: 95\\% bootstrap CI.}\n\\label{fig:k-sensitivity}\n\\end{figure}\n\n\\subsection{Temperature Sensitivity}\n\nTemperature sensitivity on Mistral-7B FOLIO ($n = 204$, default seed) reveals a sharp isolated peak rather than a smooth trend. Across four temperature settings, only $T = 0.7$ produces a positive effect: $T = 0.3$ yields $\\Delta = -1.47$\\,pp (SC $= 58.33\\%$), $T = 0.5$ yields $\\Delta = -0.98$\\,pp (SC $= 58.33\\%$), $T = 0.7$ yields $\\Delta = +3.43$\\,pp (SC $= 55.88\\%$), and $T = 1.0$ yields $\\Delta = 0.00$\\,pp (SC $= 55.39\\%$). All other temperatures yield negative or null effects, and the single positive result at $T = 0.7$ is confounded with SC baseline. Combined with the seed sensitivity (0 of 4 seeds reaching $p < 0.05$ at $T = 0.7$), the positive trend depends on a specific combination of temperature, seed, and baseline accuracy that same-model sampling rarely achieves.\n\nThe parallel between $K$ and $T$ sensitivity points to a common underlying variable. In both sweeps, the setting that produces the largest SICA gain also produces a relatively low SC baseline (55.88\\%), which places it in the intermediate-SC region. The hyperparameters themselves ($K$, $T$) are not the causal driver; they modulate SC level, and it is the SC level that determines whether SICA has operating room.\n\n\n\\section{Entropy Decomposition}\n\\label{app:entropy}\n\\label{sec:entropy}\n\nWe partition problems by trace agreement: high-entropy (majority count $\\leq 8$ out of $K = 12$) and low-entropy (majority count $\\geq 9$). Table~\\ref{tab:entropy} reports SICA $\\Delta$ within each partition across eight model-dataset conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entropy decomposition of SICA $\\Delta$ (pp). High-entropy: majority count $\\leq 8$; low-entropy: majority count $\\geq 9$. $^\\dagger$Partial data (180/600). Pre-tiebreaking SC values; pattern robust to D064 correction.}\n\\label{tab:entropy}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nModel & Dataset & \\multicolumn{2}{c}{High-entropy} & \\multicolumn{2}{c}{Low-entropy} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\n & & $n$ & $\\Delta$ & $n$ & $\\Delta$ \\\\\n\\midrule\nMistral-7B & FOLIO & 78 & $\\mathbf{+12.8}$ & 126 & 0.0 \\\\\nMistral-7B (s123) & FOLIO & 77 & $\\mathbf{+9.1}$ & 127 & 0.0 \\\\\nMistral-7B (s456) & FOLIO & 75 & $-$1.3 & 129 & 0.0 \\\\\nMistral-7B & PW-D5 & 267 & $-$4.9 & 333 & $-$1.2 \\\\\nQwen2.5-14B & FOLIO & 37 & $-$8.2 & 167 & $-$0.6 \\\\\nQwen2.5-14B & LogiQA & 23 & $-$4.3 & 177 & 0.0 \\\\\nQwen2.5-7B & FOLIO & 47 & $-$2.1 & 157 & 0.0 \\\\\nLLaMA-3.1-8B$^\\dagger$ & PW-D5 & 76 & $-$3.9 & 104 & $-$1.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo patterns emerge. First, low-entropy problems produce $\\Delta \\approx 0$\\,pp across all eight conditions: when traces agree, constraints carry no information beyond the majority vote.\n\nSecond, the direction of SICA's effect on high-entropy problems depends on the accuracy regime, not on entropy alone. In the intermediate-SC region (Mistral-7B on FOLIO, default-seed and seed-123 runs), high-entropy $\\Delta$ reaches $+12.8$ and $+9.1$\\,pp: traces genuinely disagree, and constraints from correct-answer traces provide discriminative signal that resolves the disagreement. In Type~A conditions (Qwen2.5-14B on FOLIO, $\\Delta = -8.2$\\,pp), high-entropy problems represent rare deviations from a strong model's consensus; constraints inherit the model's confirmation bias. In Type~C (Mistral-7B on ProofWriter, $\\Delta = -4.9$\\,pp), high-entropy problems reflect systematic errors. The mechanism is not entropy per se but the interaction of entropy with model capability.\n\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\\label{sec:failure-modes}\n\nThe regime-dependent pattern in Table~\\ref{tab:main_results} reflects three distinct failure modes of self-extracted logical constraints.\n\n\\paragraph{Type A: confirmation bias (SC $\\geq$ $\\sim$60\\%).} Strong models produce consistent reasoning traces, and constraints extracted from those traces mirror the answer distribution. When most constraints support the same candidate, MAX-SAT excludes few clauses ($|\\mathcal{C}^{\\setminus}| \\approx 0$), the penalty term in Eq.~\\ref{eq:score} vanishes, and the scoring function degenerates to weighted vote counting (Eq.~\\ref{eq:degenerate}). SICA and SC then produce identical predictions. The ablation in Appendix~\\ref{app:ablation} confirms this empirically: on Qwen2.5-14B (FOLIO + ProofWriter, $n = 804$), MAX-SAT and count-only baselines agree on 803 of 804 predictions.\n\n\\paragraph{Type B: non-formalizable domains.} LogiQA problems require pragmatic and contextual reasoning that resists clean logical formalization. Qwen2.5-14B on LogiQA achieves an extraction rate of 86.4\\%, but the resulting constraints have a contradiction rate of only 0.8\\%: extracted formulas rarely conflict across traces, leaving MAX-SAT with no logical tension to exploit. Mistral-7B on LogiQA sits in the same SC range (50.00\\%) yet produces $\\Delta = +1.50$\\,pp ($p = 0.581$); Qwen2.5-14B on the same domain yields $\\Delta = -1.00$\\,pp ($p = 0.625$). Neither model benefits, confirming that the right accuracy regime is necessary but not sufficient when the domain resists formalization.\n\n\\paragraph{Type C: error amplification (SC $\\leq$ $\\sim$40\\%).} When model accuracy is low, the majority of traces reach incorrect answers. Constraints extracted from wrong traces encode incorrect reasoning as formal rules. Z3 treats these rules as soft clauses with weight proportional to their frequency, so the solver preferentially satisfies the wrong constraints and penalizes traces that happen to reach the correct answer. Mistral-7B on ProofWriter ($\\Delta = -2.83$\\,pp, raw $p = 0.014$; BH adj.\\ $p = 0.042$) demonstrates this effect: SICA converts a weak positive signal in trace diversity into a net negative by formalizing the errors.\n\n\n\\section{Cross-Model Confirmation Bias}\n\\label{app:cross-model-bias}\n\nTable~\\ref{tab:cross-model-bias} reports MaxSAT-weighted confirmation bias metrics across three model families on FOLIO ($n = 204$). Weighted bias ratio and wrong-supporting constraint percentage both decrease with model capability, while SICA's accuracy effect shifts from positive (Mistral, intermediate-SC regime) to negative (LLaMA, high-SC regime). Raw bias ratios ($4.97\\times$, $3.85\\times$, $2.88\\times$) are reported in \\S\\ref{sec:confirmation-bias}. LLaMA weighted BR CI: [2.19, 3.28].\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model confirmation bias on FOLIO ($n = 204$, $K = 12$). BR (wtd.): MaxSAT-weighted ratio of error-supporting constraints on incorrect vs.\\ correct problems. Wrong \\%: weighted fraction of constraints supporting the incorrect majority on error problems. $\\Delta$: SICA $-$ SC (pp).}\n\\label{tab:cross-model-bias}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & BR (wtd.) & Wrong (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $4.24\\times$ & 80.9 & $+$4.90 \\\\\nQwen2.5-14B & $3.69\\times$ & 78.7 & $-$0.98 \\\\\nLLaMA-3.1-8B & $2.66\\times$ & 72.7 & $-$4.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Frontier model universality.}\n\\label{app:frontier-scb}\nTable~\\ref{tab:frontier-scb} extends confirmation bias analysis to nine models spanning 7B open-source to frontier closed-source. All models exhibit $\\text{BR} > 1$ (range: $1.66$--$4.97\\times$). Extraction context varies: open-source models use self-extraction (the model extracts constraints from its own traces); frontier models use cross-model extraction (Mistral-7B extracts FOL from the target model's traces), as closed-source APIs do not expose internal representations suitable for direct symbolic extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Symbolic confirmation bias across nine models on FOLIO ($n = 204$). BR: mean per-problem bias ratio. $n_\\text{err}$: number of incorrect instances on which BR is computed. $\\Delta$: SICA $-$ SC (pp). Ext.: $^a$self-extraction; $^b$cross-model (Mistral-7B extracts FOL from target traces). $^*$Interim ($n = 95/204$). $^\\dagger$8 API-failure questions excluded ($n = 196$). All models exhibit $\\text{BR} > 1$; BR estimates for high-accuracy models ($n_\\text{err} < 40$) have wider confidence intervals; Gemini ($n_\\text{err} \\approx 12$) should be interpreted with particular caution. Process-level similarity ($\\kappa_{\\text{proc}}$) ranges from $0.25$ (R1-Distill) to $0.79$ (gpt-4o/4.1/Gemini); see Table~\\ref{tab:cross-model-process}.}\n\\label{tab:frontier-scb}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Ext. & SC (\\%) & $n_\\text{err}$ & BR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral-7B & $^a$ & 55.88 & 90 & 4.97 & 0.00 \\\\\nLLaMA-8B & $^a$ & \\textrm{---} & \\textrm{---} & 2.88 & \\textrm{---} \\\\\nQwen-14B & $^a$ & 75.98 & 49 & 3.85 & $-$0.49 \\\\\n\\addlinespace\nR1-Distill-8B & $^b$ & 74.51 & 52 & 2.92 & $+$2.45 \\\\\ngpt-4o & $^a$ & 76.96 & 47 & 2.65 & $-$1.96 \\\\\ngpt-4.1 & $^b$ & 82.84 & 35 & 2.70 & $-$1.47 \\\\\ngpt-5.5 & $^b$ & 84.31 & 32 & 3.48 & $+$0.49 \\\\\no3$^\\dagger$ & $^b$ & 82.65 & 34 & 1.66 & 0.00 \\\\\nGemini-2.5-Pro$^*$ & $^b$ & 87.37 & 12 & 2.79 & $-$1.05 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{ProcessSim definition.}\n\\label{app:process-sim}\nProcess similarity is the mean pairwise cosine similarity of TF-IDF trace representations:\n\\begin{equation}\n\\label{eq:process-sim}\n\\text{ProcessSim}(q) = \\frac{2}{K(K{-}1)} \\sum_{i < j} \\cos(\\mathbf{v}_i^q, \\mathbf{v}_j^q),\n\\end{equation}\nwhere $\\mathbf{v}_i^q$ is the TF-IDF vector of trace $t_i$ for question $q$.\n\n\\paragraph{Process-$\\kappa$ gradient.}\n\\label{app:process-gradient}\nUnder cross-model extraction (Mistral-7B extracts FOL from other models' traces), SICA gain decreases monotonically with process-level cosine similarity (Table~\\ref{tab:process-gradient}; Spearman $\\rho = -1.0$, $n = 5$, one-tailed $p = 0.0083$). Gain requires two conditions: diverse traces (low $\\kappa_{\\text{proc}}$) \\emph{and} substantial self-bias (high BR). R1-Distill-8B satisfies both ($\\kappa_{\\text{proc}} = 0.248$, $\\text{BR} = 2.92$) and gains $+2.45$\\,pp; o3 has moderate trace diversity ($\\kappa_{\\text{proc}} = 0.596$) but near-minimal bias ($\\text{BR} = 1.66$, exhibiting a bimodal error pattern: 82\\% of error problems have $\\text{BR} = \\infty$ but low finite-BR), yielding $\\Delta = 0$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Process-$\\kappa$ gradient under cross-model extraction (Mistral-7B $\\rightarrow$ target model traces, FOLIO). $\\kappa_{\\text{proc}}$: process-level cosine similarity. $\\Delta$: SICA $-$ SC (pp). Spearman $\\rho(\\kappa_{\\text{proc}} \\rightarrow \\Delta) = -1.0$, $p = 0.0083$. $^*$Interim ($n = 95/204$).}\n\\label{tab:process-gradient}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nModel & $\\kappa_{\\text{proc}}$ & $\\Delta$ (pp) & BR \\\\\n\\midrule\nR1-Distill-8B & 0.248 & $+$2.45 & 2.92 \\\\\ngpt-5.5 & 0.563 & $+$0.49 & 3.48 \\\\\no3 & 0.596 & 0.00 & 1.66 \\\\\nGemini-2.5-Pro$^*$ & 0.790 & $-$1.05 & 2.79 \\\\\ngpt-4.1 & 0.792 & $-$1.47 & 2.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Independence-Accuracy Scatter Plot}\n\\label{app:kappa-scatter}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/f6_kappa_accuracy_scatter}\n\\caption{Independence-accuracy trade-off across aggregation methods (Mistral-7B, filled markers) and model families (LLaMA-3.1-8B, Qwen2.5-7B, Qwen2.5-14B; open markers) on FOLIO ($n = 204$). Same-model methods cluster at $\\kappa \\approx 0.40$--$0.47$ (gray band), while cross-model SC shows stronger correlations ($\\kappa = 0.41$--$0.74$) at higher accuracy. Debate breaks correlation ($\\kappa = 0.15$) at catastrophic accuracy cost. Dashed line: Mistral-7B SC baseline.}\n\\label{fig:kappa-accuracy}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Independence-accuracy trade-off (FOLIO, $n = 204$). Top: aggregation methods on Mistral-7B; bottom: SC across three model families. All families produce $\\kappa \\geq 0.41$, confirming an architecture-independent ceiling. $\\kappa$: Fleiss' kappa on raw answers.}\n\\label{tab:kappa_generalization}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Aggregation & $\\kappa$ & Eff-$K$ & $K$ & Acc.\\ (\\%) \\\\\n\\midrule\nMistral-7B & Debate & 0.15 & 4.44 & 12 & 38.24 \\\\\n& Diverse-Prompt & 0.40 & 2.21 & 12 & 54.41 \\\\\n& Self-Consistency & 0.44 & 2.02 & 10 & 56.86 \\\\\n& ICG & 0.47 & 1.93 & 10 & 51.96 \\\\\n\\addlinespace\nLLaMA-3.1-8B & Self-Consistency & 0.41 & 2.17 & 12 & 66.18 \\\\\nQwen2.5-7B & Self-Consistency & 0.66 & 1.46 & 12 & 75.98 \\\\\nQwen2.5-14B & Self-Consistency & 0.74 & 1.32 & 12 & 75.98 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Trace independence metrics.}\n\\label{app:trace-independence}\n\nTable~\\ref{tab:independence} reports the full 15-condition breakdown of Fleiss' $\\kappa$ and Effective-K at $K = 12$, referenced in \\S\\ref{sec:effective-k}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Trace independence metrics ($K = 12$, sorted by $\\kappa$ descending). $\\kappa$: Fleiss' Kappa. $K_{\\text{eff}}$: Effective-K (Eq.~\\ref{eq:effk}). SC: Self-Consistency baseline. $\\Delta$: SICA $-$ SC (pp). {*}\\,$p < 0.05$ (uncorrected; BH adj.\\ $p = 0.042$, $m{=}6$); positive $\\Delta$ values do not reach significance. multi-T $= T \\in \\{0.3, 0.7, 1.2\\}$, 4 traces each. $^{\\dag}$\\,$\\kappa$ computed in an earlier pipeline run; all other rows recomputed from per-problem vote distributions with answer labels normalized to canonical categories.}\n\\label{tab:independence}\n\\begin{tabular}{@{}llccrr@{}}\n\\toprule\nModel & Condition & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nQwen3 (think) & FOLIO & 0.91$^{\\dag}$ & 1.09 & 86.27 & $+$0.49 \\\\\nQwen2.5-14B & LogiQA & 0.82 & 1.20 & 79.00 & $-$1.00 \\\\\nQwen3 & FOLIO & 0.79 & 1.24 & 83.33 & $+$1.47 \\\\\nQwen2.5-14B & FOLIO & 0.74 & 1.31 & 75.98 & $-$0.49 \\\\\nQwen2.5-7B & FOLIO & 0.66$^{\\dag}$ & 1.46 & 75.98 & $+$0.49 \\\\\n\\addlinespace\nMistral-7B ($T{=}0.3$) & FOLIO & 0.53$^{\\dag}$ & 1.77 & 58.33 & $-$1.47 \\\\\nMistral-7B ($T{=}0.5$) & FOLIO & 0.52$^{\\dag}$ & 1.80 & 58.33 & $-$0.98 \\\\\nMistral-7B & LogiQA & 0.51 & 1.81 & 50.00 & $+$1.50 \\\\\nMistral-7B ($T{=}1.0$) & FOLIO & 0.48$^{\\dag}$ & 1.91 & 55.39 & 0.00 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 & $+$3.43 \\\\\nMistral-7B (s123) & FOLIO & 0.46 & 1.99 & 54.41 & $+$2.94 \\\\\nMistral-7B (s456) & FOLIO & 0.46 & 1.99 & 55.88 & 0.00 \\\\\nMistral-7B (s789) & FOLIO & 0.45 & 2.03 & 59.31 & $-$2.45 \\\\\nMistral-7B (multi-T) & FOLIO & 0.43 & 2.11 & 57.84 & 0.00 \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 & $\\mathbf{-2.83}${*} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Cross-Model Kappa Analysis}\n\\label{app:cross-model-kappa}\n\nTable~\\ref{tab:cross_model_kappa} compares trace independence across three model families on the same benchmarks. On FOLIO ($n = 204$), all four models produce $\\kappa \\geq 0.41$: LLaMA-3.1-8B ($\\kappa = 0.41$), Mistral-7B ($\\kappa = 0.46$), Qwen2.5-7B ($\\kappa = 0.66$), and Qwen2.5-14B ($\\kappa = 0.74$). The bottleneck is architecture-independent---no family escapes the correlation floor. Within the Qwen family, $\\kappa$ increases from 0.66 (7B) to 0.74 (14B), but Mistral-7B (7B) and LLaMA-3.1-8B (8B) differ by $\\Delta\\kappa = 0.05$ despite belonging to different families, suggesting that cross-family variation ($\\Delta\\kappa$ up to 0.20 at similar scale) exceeds within-family scale effects ($\\Delta\\kappa = 0.08$). Disentangling scale from architecture requires controlled same-family experiments across $\\geq$3 scales.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model trace independence ($K = 12$, SC aggregation, FOLIO + ProofWriter). Higher $\\kappa$ indicates stronger correlation and lower effective sample size.}\n\\label{tab:cross_model_kappa}\n\\begin{tabular}{@{}llccr@{}}\n\\toprule\nModel & Dataset & $\\kappa$ & $K_{\\text{eff}}$ & SC (\\%) \\\\\n\\midrule\nQwen2.5-14B & FOLIO & 0.74 & 1.32 & 75.98 \\\\\nQwen2.5-7B & FOLIO & 0.66 & 1.46 & 75.98 \\\\\nMistral-7B & FOLIO & 0.46 & 1.98 & 55.88 \\\\\nLLaMA-3.1-8B & FOLIO & 0.41 & 2.17 & 66.18 \\\\\n\\addlinespace\nQwen2.5-14B & PW-D5 & 0.62 & 1.54 & --- \\\\\nMistral-7B & PW-D5 & 0.19 & 3.94 & 39.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Cross-Model Process-Level Independence}\n\\label{app:cross-model-process}\n\nTable~\\ref{tab:cross-model-process} extends the process-level independence analysis (\\S\\ref{sec:process-kappa}) to four model families on FOLIO ($n = 204$). Mean pairwise cosine similarity of TF-IDF trace representations exceeds answer-level $\\kappa$ in every family, but the gap is model-strength dependent: it narrows from $0.31$ (LLaMA) and $0.23$ (Mistral) to $0.02$ (Qwen-14B). For weaker models ($r \\approx 0$), answer diversity does not reflect reasoning diversity---process-convergent but answer-divergent trace pairs constitute 9.5\\% of all pairs on Mistral-7B versus 2.5--3.2\\% on other families. For stronger models ($r \\approx 0.23$, $p \\leq 0.001$), process and answer agreement align, and answer-level $\\kappa$ already captures the bottleneck. Process-$\\kappa$ thus provides a crucial additional diagnostic specifically for weaker models, where answer-level metrics underestimate reasoning homogeneity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model process-level independence on FOLIO ($n = 204$, $K = 12$). Mean Cosine: mean pairwise TF-IDF cosine similarity of reasoning traces (Eq.~\\ref{eq:process-sim}). Answer $\\kappa$: per-question answer agreement. Gap: Cosine $-$ $\\kappa$. $r$: Pearson correlation between ProcessSim and answer agreement. Conv.: fraction of process-convergent but answer-divergent trace pairs. {*}{*}\\,$p < 0.01$; {*}{*}{*}\\,$p < 0.001$.}\n\\label{tab:cross-model-process}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccrlr@{}}\n\\toprule\nModel & Mean Cos. & Ans.\\ $\\kappa$ & Gap & $r$ & $p$ & Conv.\\ (\\%) \\\\\n\\midrule\nMistral-7B & 0.690 & 0.460 & 0.230 & $-$0.064 & 0.362 & 9.5 \\\\\nLLaMA-3.1-8B & 0.759 & 0.447 & 0.312 & $-$0.001 & 0.985 & 3.2 \\\\\nQwen2.5-7B & 0.790 & 0.658 & 0.132 & $+$0.226 & 0.001{*}{*} & 2.8 \\\\\nQwen2.5-14B & 0.766 & 0.744 & 0.022 & $+$0.244 & ${<}$0.001{*}{*}{*} & 2.5 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Representation robustness.} Replacing TF-IDF with SBERT embeddings (all-MiniLM-L6-v2) yields ProcessSim $= 0.91$ (vs.\\ TF-IDF $0.74$), widening the gap over answer-level $\\kappa = 0.55$. The process homogeneity finding is robust to representation choice.\n\n\\section{Constraint Quality Across Methods}\n\\label{app:constraint-quality}\n\nTable~\\ref{tab:constraint_quality} compares constraint quality metrics across the three method-level interventions on Mistral-7B FOLIO ($n = 204$). Standard SICA extracts from reasoning traces and achieves the highest parse rate (97.1\\%) but also the highest redundancy (42.9\\%): nearly half of all constraints are syntactic duplicates across the 12 traces, quantifying the co-sourcing effect of same-model generation. ICG generates constraints directly from the problem statement without trace conditioning. Its lower parse rate (74.6\\%) reflects the difficulty of standalone formalization at the 7B scale, though successfully parsed constraints compile at a higher rate (99.4\\% vs.\\ 96.5\\%). ICG produces fewer unique constraints per question (24.9 vs.\\ 39.3) with lower redundancy (32.3\\%), consistent with the absence of trace-level repetition. Contrastive scoring generates pro and con constraint sets for each candidate answer. The format yields far fewer unique constraints per question (9.2) with zero redundancy (each pro/con pair is structurally distinct), but 62.7\\% of constraints are trivially satisfied by Z3---they impose no logical tension and cannot discriminate between candidates. Only 51.0\\% of Contrastive constraints are discriminative, compared to 81.4\\% for standard SICA and 77.0\\% for ICG.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Constraint quality metrics across method-level interventions (Mistral-7B, FOLIO, $n = 204$). Parse: fraction of extraction attempts yielding valid JSON. Z3 Compile: fraction compiling to Z3 formulas. Unique/q: mean unique constraints per question. Redundancy: fraction of constraints duplicated across traces. Disc.: fraction discriminative (different Z3 outcome per candidate). Triv.\\ Sat.: fraction trivially satisfied (no logical tension).}\n\\label{tab:constraint_quality}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr@{}}\n\\toprule\nMethod & Parse & Z3 & Uniq/q & Redund. & Disc. & Triv.\\ Sat. \\\\\n\\midrule\nStandard SICA & 97.1\\% & 96.5\\% & 39.3 & 42.9\\% & 81.4\\% & --- \\\\\nICG & 74.6\\% & 99.4\\% & 24.9 & 32.3\\% & 77.0\\% & --- \\\\\nContrastive & 74.0\\% & 94.4\\% & 9.2 & 0.0\\% & 51.0\\% & 62.7\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-trace constraint yield uniformity.}\n\\label{app:yield-cv}\n\nObservation~1 assumes approximately uniform constraint yield per trace within each answer group. We verify this on Mistral-7B FOLIO ($K{=}12$, $n{=}204$). Per-problem yield CV (coefficient of variation across traces within each problem) has median $0.257$ and mean $0.319$; 64.2\\% of problems fall below $\\text{CV} = 0.3$, and 91.2\\% below $0.5$, supporting the uniformity assumption. Majority-answer traces average $5.61$ constraints and minority-answer traces $6.04$ (Mann--Whitney $p = 5.2 \\times 10^{-6}$); correct-answer traces average $5.41$ and incorrect $6.05$ ($p = 5.3 \\times 10^{-11}$). Although statistically significant, the absolute difference (${\\sim}0.6$ constraints, $< 12\\%$) is insufficient to alter the argmax-preservation result: SICA and SC select the same answer on ${>}96\\%$ of problems regardless of yield variation.\n\n\\section{Error Categorization of Method-Level Interventions}\n\\label{app:error-categorization}\n\nWe categorize discordant predictions (where the method and SC disagree) for Debate and Contrastive on FOLIO ($n = 204$) to understand why these interventions degrade accuracy.\n\n\\paragraph{Debate discordant analysis.} Debate produces 60 correct$\\to$wrong flips and 22 wrong$\\to$correct flips on FOLIO. Answer-type breakdown reveals that False-labeled questions are most vulnerable: 82.8\\% of False questions that SC answers correctly are flipped by Debate, compared to 63.9\\% for True and 25.5\\% for Unknown. Counterintuitively, failures concentrate not where debate breaks down but where it succeeds most thoroughly: discordant questions average 2.93 effective debate rounds (proposer-critic exchanges producing substantive updates) versus 2.52 for concordant ones. More extensive same-model debate produces more confident but incorrect constraints, consistent with the independence limitation---the critic draws on the same model distribution as the proposer, reinforcing shared biases rather than correcting them.\n\n\\paragraph{Contrastive discordant analysis.} Contrastive produces 34 discordant questions on FOLIO. All 34 produced non-degenerate scores (both pro and con constraint sets non-empty), compared to 20.1\\% degenerate scores in the full sample. This indicates that scoring failures on discordant questions stem from systematic pro-bias rather than missing constraints. Among discordant questions, 97.1\\% contain negation words in the problem statement versus 76.5\\% in the full sample, suggesting that negation-bearing problems are particularly susceptible to pro-constraint imbalance. The average pro/con score ratio is 1.0 for discordant questions versus 0.68 for the full sample: the method generates balanced-looking scores that mask directional errors.\n\n\\paragraph{Cross-method overlap.} Of the 79 unique questions on which either method disagrees with SC, only 15 overlap between Debate and Contrastive (Jaccard index $= 0.19$). All 15 shared discordant questions contain negation words. The low overlap confirms that the two methods attack different vulnerability types---Debate through extended same-model argumentation that amplifies confident errors, Contrastive through pro-bias in constraint generation---while sharing a common root cause in correlated same-model voting: both methods rely on the same model's output distribution and cannot introduce genuinely independent signal.\n\n\n\\section{TOST Equivalence Tests}\n\\label{app:tost}\n\nWe apply two one-sided tests (TOST) \\citep{lakens2017equivalence} with equivalence margin $\\pm 2$\\,pp to all 16 non-degenerate SICA--SC comparisons, classifying each condition as \\emph{equivalent} (TOST significant), \\emph{genuinely different} (McNemar $p < 0.05$ and TOST not significant), or \\emph{underpowered} (neither test significant). Four conditions are equivalent, confirming that SICA and SC produce statistically indistinguishable accuracy. Two conditions show genuine differences, both negative: Mistral-7B ProofWriter ($-2.83$\\,pp, $p = 0.014$) and Qwen2.5-14B ProofWriter ($-2.50$\\,pp, $p = 0.011$). The remaining ten conditions are underpowered, reflecting the limited statistical power at $n{=}200$--$204$ for detecting $|\\Delta| \\leq 2$\\,pp effects.\n\n\\paragraph{Margin sensitivity.} Table~\\ref{tab:tost-sensitivity} shows that the classification is robust across margins: regardless of the chosen margin, no condition shows a significant positive SICA effect.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST classification sensitivity across equivalence margins (16 non-degenerate conditions).}\n\\label{tab:tost-sensitivity}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMargin & Equivalent & Different & Underpowered \\\\\n\\midrule\n$\\pm 1$\\,pp & 0 & 2 & 14 \\\\\n$\\pm 2$\\,pp & 4 & 2 & 10 \\\\\n$\\pm 3$\\,pp & 10 & 0 & 6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Relative-margin TOST.}\n\\label{app:relative_tost}\nThe absolute $\\pm 2$\\,pp margin is more stringent at high baselines ($\\pm 2.4\\%$ relative at SC $= 85\\%$) than low ones ($\\pm 5.1\\%$ at SC $= 39\\%$). A relative $\\pm 5\\%$ of SC margin addresses this asymmetry: 8 conditions are equivalent, 2 genuinely different (both negative), and 6 underpowered. The additional four equivalent conditions are all high-SC ($\\geq 75\\%$), where the wider relative band captures practical indistinguishability. No condition shows a significant positive effect under either margin.\n\n\\paragraph{Conditional Correction Ratio data.}\n\\label{app:cil-data}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\caption{Conditional Correction Ratio across eight verifier--generator conditions. $\\text{CCR} > 0$: cross-arch NLI on ProofWriter. $\\text{CCR} < 0$: same-model SICA or weak capability gap.}\n\\label{tab:cil_main}\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nGenerator--Verifier & Dataset & CCR & $\\Delta$ (pp) \\\\\n\\midrule\nMistral $\\times$ BART-NLI & PW & $+$1.86 & $+$5.17 \\\\\nMistral $\\times$ DeBERTa-NLI & PW & $+$1.67 & $+$6.67 \\\\\nMistral $\\times$ RoBERTa-NLI & PW & $+$1.42 & $+$4.17 \\\\\n\\addlinespace\nQwen-14B $\\times$ DeBERTa-NLI & PW & $-$0.21 & $+$0.33 \\\\\nMistral $\\times$ DeBERTa-NLI & FOLIO & $-$0.47 & $+$2.94 \\\\\n\\addlinespace\nMistral $\\times$ SICA & FOLIO & $-$2.93 & $+$3.43 \\\\\nQwen-14B $\\times$ SICA & PW & $-$4.21 & $-$2.50 \\\\\nMistral $\\times$ SICA & PW & $-$4.61 & $-$2.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Disagreement-Routed Cascade details.}\n\\label{app:drc}\nDRC invokes NLI only when SC consensus falls below threshold $\\tau$, avoiding unnecessary verifier calls on high-agreement problems. Gains concentrate on weak generators (SC $< 40\\%$), consistent with the capability-gap hypothesis (\\S\\ref{sec:cross-arch}). Regime-dependent bottleneck analysis appears in Appendix~\\ref{app:2x2}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DRC on Mistral-7B ($K{=}12$, DeBERTa-large-mnli, $w{=}3$). $\\tau{=}0.7$ recovers 83--90\\% of full-combo gain at ${\\sim}35\\%$ NLI cost across both datasets.}\n\\label{tab:drc}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Method & Acc.\\ & NLI Calls & Cost & Recovery \\\\\n\\midrule\n\\multirow{3}{*}{PW-D5} & SC only & 39.33\\% & 0/600 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{45.33\\%} & \\textbf{207/600} & \\textbf{34.5\\%} & \\textbf{90.0\\%} \\\\\n& Full combo & 46.00\\% & 600/600 & 100\\% & 100\\% \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO} & SC only & 55.88\\% & 0/204 & 0\\% & --- \\\\\n& \\textbf{DRC $\\tau{=}0.7$} & \\textbf{58.33\\%} & \\textbf{71/204} & \\textbf{34.8\\%} & \\textbf{83.3\\%} \\\\\n& Full combo & 58.82\\% & 204/204 & 100\\% & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Verifier NLI Results}\n\\label{app:multi-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-architecture NLI combo on ProofWriter depth-5 ($n{=}600$, Mistral-7B traces, SC $= 39.33\\%$). Three NLI verifiers $\\times$ three weight settings. {*}\\,$p < 0.05$;\\enspace{**}\\,$p < 0.01$;\\enspace{***}\\,$p < 0.001$ (McNemar).}\n\\label{tab:multi-nli}\n\\begin{tabular}{@{}llrrl@{}}\n\\toprule\nVerifier & Standalone & $w$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\nDeBERTa-MNLI & 55.00\\% & 1 & $+$0.83 & n.s. \\\\\n & & 3 & $+$6.67 & ${<}0.001${***} \\\\\n & & 5 & $+$11.00 & ${<}0.001${***} \\\\\n\\addlinespace\nRoBERTa-MNLI & 37.67\\% & 1 & $-$0.17 & n.s. \\\\\n & & 3 & $+$4.17 & 0.003{**} \\\\\n & & 5 & $+$4.33 & 0.037{*} \\\\\n\\addlinespace\nBART-MNLI & 46.17\\% & 1 & 0.00 & n.s. \\\\\n & & 3 & $+$5.17 & ${<}0.001${***} \\\\\n & & 5 & $+$6.33 & 0.003{**} \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize All verifiers fine-tuned on MultiNLI. Unknown recall ${<}3.5\\%$ across all verifiers.}\n\\end{table}\n\n\\paragraph{Three-verifier BH correction.}\n\\label{app:3verifier-bh}\nTable~\\ref{tab:3verifier-bh} applies Benjamini--Hochberg correction across all 15 Mistral-7B verifier--weight conditions ($m{=}15$, $\\alpha{=}0.05$; distinct from the $m{=}12$ cross-generator analysis in \\S\\ref{sec:cross-arch}). Ten of 15 conditions remain significant after correction, confirming that multi-verifier NLI gains are robust to multiple testing.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH correction across 3 verifiers $\\times$ 5 weights on Mistral-7B ProofWriter ($n{=}600$, $m{=}15$). \\checkmark: $p_{\\text{BH}} < 0.05$.}\n\\label{tab:3verifier-bh}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nVerifier & $w{=}1$ & $w{=}2$ & $w{=}3$ & $w{=}4$ & $w{=}5$ \\\\\n\\midrule\nDeBERTa-MNLI & & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\nRoBERTa-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\nBART-MNLI & & & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\\\\[2pt]\n{\\footnotesize 10/15 significant at $\\alpha{=}0.05$ after BH correction. All $w{=}1$ conditions and RoBERTa $w{=}2$ are non-significant.}\n\\end{table}\n\n\\section{Capability Gap Data Points}\n\\label{app:capability-gap}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.78\\columnwidth]{figures/capability_gap_scatter}\n\\caption{Combo gain vs.\\ capability gap (verifier standalone $-$ generator SC) at $w{=}3$ across three NLI architectures. Gain decreases monotonically (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n{=}6$; four of six conditions share the DeBERTa verifier---see Limitations); significant gains occur only for generators below the verifier's standalone accuracy. Stars: domain-adapted DeBERTa (99.67\\% standalone, Table~\\ref{tab:finetuned-nli}).}\n\\label{fig:capability-gap}\n\\end{figure}\n\nTable~\\ref{tab:cross_generator_nli} reports the controlled cross-generator comparison with DeBERTa-large-mnli on ProofWriter ($n{=}600$). We extend this analysis by pairing Mistral-7B with two additional NLI architectures: BART-large-mnli (46.17\\% standalone, combo $+5.17$\\,pp, $p = 0.0002$) and RoBERTa-large-mnli (37.67\\% standalone, combo $+4.17$\\,pp, $p = 0.003$). All three NLI architectures produce significant gains on Mistral-7B at $w \\geq 3$.\n\nAcross all six ProofWriter verifier-generator pairs at $w{=}3$ (three verifiers $\\times$ Mistral-7B plus three negative-gap generators $\\times$ DeBERTa), combo gain decreases monotonically with the capability gap (Spearman $\\rho = 1.0$, exact permutation $p = 0.003$, $n = 6$; however, four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom---see Limitations; Figure~\\ref{fig:capability-gap}). Significant $w{=}3$ gains are observed only for Mistral-7B (SC 39.33\\%, below the verifier); the three above-verifier generators show no significant improvement at any $w$. After BH correction ($m{=}12$), two of twelve conditions survive: Mistral-7B $w{=}3$ (adj.\\ $p = 6.78 \\times 10^{-5}$) and $w{=}5$ (adj.\\ $p = 7.41 \\times 10^{-6}$).\n\n\\paragraph{Robustness check.} Including all nine conditions (three verifiers $\\times$ three weight levels on Mistral-7B) yields Spearman $\\rho = 0.836$ (exact permutation $p = 0.007$, $n = 9$), confirming that the monotonic trend is robust to the choice of weight parameter.\n\n\\paragraph{Full NLI combo with BH correction.}\n\\label{app:nli-combo-full}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full cross-generator NLI combo results on ProofWriter depth-5 ($n{=}600$) with Benjamini--Hochberg correction ($m{=}12$, $\\alpha{=}0.05$). All conditions use DeBERTa-large-mnli verifier (55.00\\% standalone). Two of twelve conditions survive correction (Mistral-7B $w{=}3$ and $w{=}5$). {***}\\,$p_{\\text{BH}} < 0.001$.}\n\\label{tab:nli-combo-full}\n\\setlength{\\tabcolsep}{3.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{raw}}$ & $p_{\\text{BH}}$ & \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%, gap\\,$+$15.67}}}\n  & 1 & 40.17 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 46.00 & $+$6.67 & $1.13{\\times}10^{-5}$ & $6.78{\\times}10^{-5}$ & {***} \\\\\n  & 5 & 50.33 & $+$11.00 & $6.18{\\times}10^{-7}$ & $7.41{\\times}10^{-6}$ & {***} \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%, gap\\,$-$17.50}}}\n  & 1 & 73.33 & $+$0.83 & .359 & .721 & \\\\\n  & 3 & 73.33 & $+$0.83 & .665 & .886 & \\\\\n  & 5 & 72.00 & $-$0.50 & .871 & 1.000 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen2.5-14B\\\\{\\scriptsize SC\\,74.00\\%, gap\\,$-$19.00}}}\n  & 1 & 74.17 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 74.67 & $+$0.67 & .503 & .755 & \\\\\n  & 5 & 75.17 & $+$1.17 & .360 & .721 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize SC\\,85.83\\%, gap\\,$-$30.83}}}\n  & 1 & 86.00 & $+$0.17 & 1.000 & 1.000 & \\\\\n  & 3 & 86.33 & $+$0.50 & .453 & .755 & \\\\\n  & 5 & 87.00 & $+$1.17 & .210 & .721 & \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{BART-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with BART-large-mnli verifier (46.17\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (below the verifier) gains significantly after BH correction.}\n\\label{tab:bart-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $+$6.84)} & 39.33 & 44.50 & $+$5.17 & .003{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$26.33)} & 72.50 & 72.50 & $\\pm$0.00 & --- \\\\\nQwen2.5-14B {\\scriptsize (gap $-$27.83)} & 74.00 & 75.50 & $+$1.50 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$39.66)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{RoBERTa-large-mnli cross-generator results.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-generator NLI combo with RoBERTa-large-mnli verifier (37.67\\% standalone) on ProofWriter depth-5 ($n{=}600$, $w{=}3$). Only Mistral-7B (marginally above the verifier) gains significantly after BH correction.}\n\\label{tab:roberta-combo-full}\n\\begin{tabular}{@{}lccrl@{}}\n\\toprule\nGenerator & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p_{\\text{BH}}$ \\\\\n\\midrule\nMistral-7B {\\scriptsize (gap $-$1.66)} & 39.33 & 43.50 & $+$4.17 & .016{*} \\\\\nLLaMA-3.1-8B {\\scriptsize (gap $-$34.83)} & 72.50 & 71.33 & $-$1.17 & n.s. \\\\\nQwen2.5-14B {\\scriptsize (gap $-$36.33)} & 74.00 & 74.17 & $+$0.17 & n.s. \\\\\nQwen3-14B {\\scriptsize (gap $-$48.16)} & 85.83 & 86.50 & $+$0.67 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FOLIO NLI combo results.}\n\\label{app:folio-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with DeBERTa-large-mnli verifier (49.51\\% standalone). No condition reaches significance; all generators exceed the verifier's standalone accuracy, consistent with the capability-gap pattern. SC baselines match the cross-model ablation traces (Table~\\ref{tab:cross-model-ablation}).}\n\\label{tab:folio-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 58.82 & $+$2.94 & n.s. \\\\\n & 5 & & 59.80 & $+$3.92 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 65.20 & $-$0.98 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.96 & $+$0.98 & n.s. \\\\\n & 3 & & 75.49 & $-$0.49 & n.s. \\\\\n & 5 & & 73.53 & $-$2.45 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.80 & $+$1.47 & n.s. \\\\\n & 5 & & 83.33 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with BART-large-mnli verifier (47.06\\% standalone). No positive improvement reaches significance; for Qwen2.5-14B the weak verifier produces a significant \\emph{degradation} at $w{=}5$ ($p{=}.039$), consistent with the capability-gap pattern.}\n\\label{tab:folio-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 54.90 & $-$0.98 & n.s. \\\\\n & 3 & & 56.37 & $+$0.49 & n.s. \\\\\n & 5 & & 56.86 & $+$0.98 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 67.65 & $+$1.47 & n.s. \\\\\n & 3 & & 67.65 & $+$1.47 & n.s. \\\\\n & 5 & & 64.71 & $-$1.47 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 76.47 & $+$0.49 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 72.55 & $-$3.43 & .039{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 82.84 & $-$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on FOLIO ($n{=}204$) with RoBERTa-large-mnli verifier (46.57\\% standalone). Cross-verifier consistency: no positive gain reaches significance, and Qwen2.5-14B shows a significant \\emph{degradation} at $w{=}5$ ($p{=}.012$)---the same capability-gap signature as BART.}\n\\label{tab:folio-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{55.88} & 56.37 & $+$0.49 & n.s. \\\\\n & 3 & & 57.84 & $+$1.96 & n.s. \\\\\n & 5 & & 58.82 & $+$2.94 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{66.18} & 65.69 & $-$0.49 & n.s. \\\\\n & 3 & & 66.67 & $+$0.49 & n.s. \\\\\n & 5 & & 64.22 & $-$1.96 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{75.98} & 75.98 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 75.00 & $-$0.98 & n.s. \\\\\n & 5 & & 71.57 & $-$4.41 & .012{*} \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{83.33} & 83.33 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 84.31 & $+$0.98 & n.s. \\\\\n & 5 & & 83.82 & $+$0.49 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LogiQA NLI combo results.}\n\\label{app:logiqa-nli-combo}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with DeBERTa-large-mnli verifier (26.50\\% standalone, near the 25\\% random baseline for 4-way classification). No condition reaches significance.}\n\\label{tab:logiqa-nli-deberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 54.00 & $+$1.00 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 58.50 & $-$1.00 & n.s. \\\\\n & 3 & & 58.00 & $-$1.50 & n.s. \\\\\n & 5 & & 58.00 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.00 & $-$1.00 & n.s. \\\\\n & 5 & & 78.00 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 80.50 & $-$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with BART-large-mnli verifier (33.00\\% standalone). Near-random NLI accuracy yields no significant combo improvements.}\n\\label{tab:logiqa-nli-bart}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 53.50 & $+$0.50 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 52.50 & $-$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 59.50 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.50 & $+$0.50 & n.s. \\\\\n & 3 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 5 & & 81.50 & $+$0.50 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI combo on LogiQA ($n{=}200$) with RoBERTa-large-mnli verifier (31.50\\% standalone). All three NLI verifiers produce the same null result on LogiQA.}\n\\label{tab:logiqa-nli-roberta}\n\\begin{tabular}{@{}lcccrl@{}}\n\\toprule\nGenerator & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{Mistral-7B} & 1 & \\multirow{3}{*}{53.00} & 54.00 & $+$1.00 & n.s. \\\\\n & 3 & & 53.50 & $+$0.50 & n.s. \\\\\n & 5 & & 53.50 & $+$0.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B} & 1 & \\multirow{3}{*}{59.50} & 59.00 & $-$0.50 & n.s. \\\\\n & 3 & & 58.50 & $-$1.00 & n.s. \\\\\n & 5 & & 58.50 & $-$1.00 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B} & 1 & \\multirow{3}{*}{79.00} & 78.50 & $-$0.50 & n.s. \\\\\n & 3 & & 78.50 & $-$0.50 & n.s. \\\\\n & 5 & & 77.50 & $-$1.50 & n.s. \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B} & 1 & \\multirow{3}{*}{81.00} & 81.00 & $\\pm$0.00 & n.s. \\\\\n & 3 & & 80.50 & $-$0.50 & n.s. \\\\\n & 5 & & 81.00 & $\\pm$0.00 & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain-adapted verifier results.}\n\\label{app:finetuned-nli}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Domain-adapted NLI combo on ProofWriter depth-5 ($n{=}600$). DeBERTa-large fine-tuned on ProofWriter OWA (99.67\\% standalone). All $p < 0.0001$. Complementarity: ratio of NLI-correct$\\cap$SC-incorrect to SC-correct$\\cap$NLI-incorrect.}\n\\label{tab:finetuned-nli}\n\\setlength{\\tabcolsep}{3.5pt}\n\\begin{tabular}{@{}lrrrrc@{}}\n\\toprule\nGenerator & $w$ & Combo (\\%) & $\\Delta$ (pp) & Compl.\\ ratio \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize SC\\,39.33\\%}}}\n  & 1 & 42.17 & $+$2.83 & \\multirow{3}{*}{364:2} \\\\\n  & 3 & 52.00 & $+$12.67 & \\\\\n  & 5 & 65.50 & $+$26.17 & \\\\\n\\addlinespace\n\\multirow{3}{*}{\\shortstack[l]{LLaMA-3.1-8B\\\\{\\scriptsize SC\\,72.50\\%}}}\n  & 1 & 76.00 & $+$3.50 & \\multirow{3}{*}{164:1} \\\\\n  & 3 & 84.17 & $+$11.67 & \\\\\n  & 5 & 91.67 & $+$19.17 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model voting ablation.}\n\\label{app:cross-model-ablation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model voting ablation ($w \\in \\{3,5\\}$). ``Cross LLM'' replaces the NLI verifier with a second LLM's SC votes at weight $w$; ``NLI'' uses DeBERTa-large-mnli (55.00\\% standalone) at $w{=}3$. On ProofWriter, cross-model SC with a weak voter (Mistral-7B) degrades all strong generators---worsening at higher $w$---while NLI combo does not, indicating that structural independence---not merely model diversity---drives the escape.}\n\\label{tab:cross-model-ablation}\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccrl@{}}\n\\toprule\nGenerator & Voter/Verifier & $w$ & SC (\\%) & Combo (\\%) & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{ProofWriter ($n{=}600$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 39.33 & 47.67 & $+$8.33 & $<$.001 \\\\\n  & & 5 & 39.33 & 55.33 & $+$16.00 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 39.33 & 46.00 & $+$6.67 & $<$.001 \\\\\n\\addlinespace\n\\multirow{5}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 72.50 & 75.33 & $+$2.83 & .060 \\\\\n  & & 5 & 72.50 & 75.33 & $+$2.83 & .125 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 72.50 & 63.17 & $-$9.33 & $<$.001 \\\\\n  & & 5 & 72.50 & 56.17 & $-$16.33 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 72.50 & 73.33 & $+$0.83 & .665 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 74.00 & 74.50 & $+$0.50 & .664 \\\\\n  & & 5 & 74.00 & 76.00 & $+$2.00 & .096 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 74.00 & 71.67 & $-$2.33 & .020 \\\\\n  & & 5 & 74.00 & 69.67 & $-$4.33 & .002 \\\\\n  & DeBERTa NLI & 3 & 74.00 & 74.67 & $+$0.67 & .503 \\\\\n\\addlinespace\n\\multirow{5}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 85.83 & 84.67 & $-$1.17 & .143 \\\\\n  & & 5 & 85.83 & 83.33 & $-$2.50 & .006 \\\\\n  & \\multirow{2}{*}{Mistral-7B (cross)} & 3 & 85.83 & 83.17 & $-$2.67 & .002 \\\\\n  & & 5 & 85.83 & 81.17 & $-$4.67 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 85.83 & 86.33 & $+$0.50 & .453 \\\\\n\\midrule\n\\multicolumn{7}{@{}l}{\\textit{FOLIO ($n{=}204$)}} \\\\\n\\addlinespace\n\\multirow{3}{*}{Mistral-7B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 55.88 & 63.73 & $+$7.84 & .002 \\\\\n  & & 5 & 55.88 & 68.63 & $+$12.75 & $<$.001 \\\\\n  & DeBERTa NLI & 3 & 55.88 & 58.82 & $+$2.94 & .210 \\\\\n\\addlinespace\n\\multirow{3}{*}{LLaMA-3.1-8B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 66.18 & 70.10 & $+$3.92 & .134 \\\\\n  & & 5 & 66.18 & 73.53 & $+$7.35 & .014 \\\\\n  & DeBERTa NLI & 3 & 66.18 & 65.20 & $-$0.98 & .824 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen2.5-14B}\n  & \\multirow{2}{*}{LLaMA-8B (cross)} & 3 & 75.98 & 76.96 & $+$0.98 & .727 \\\\\n  & & 5 & 75.98 & 79.41 & $+$3.43 & .143 \\\\\n  & DeBERTa NLI & 3 & 75.98 & 75.49 & $-$0.49 & 1.00 \\\\\n\\addlinespace\n\\multirow{3}{*}{Qwen3-14B}\n  & \\multirow{2}{*}{Qwen2.5-14B (cross)} & 3 & 83.33 & 85.78 & $+$2.45 & .125 \\\\\n  & & 5 & 83.33 & 86.76 & $+$3.43 & .039 \\\\\n  & DeBERTa NLI & 3 & 83.33 & 84.80 & $+$1.47 & .250 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Generator$\\times$Extractor 2$\\times$2 Matrix.}\n\\label{app:2x2}\n\nTable~\\ref{tab:2x2-folio} reports the full $2{\\times}2$ generator${\\times}$extractor matrix on FOLIO ($n{=}204$). The generator dominates accuracy (row difference ${\\sim}25$\\,pp vs.\\ column difference ${\\sim}3$\\,pp), contrasting with ProofWriter where the extractor dominates ($\\Delta$ range ${\\pm}40$--$50$\\,pp). Cross-extractor McNemar tests: Mistral-7B gen, $\\Delta = +2.94$\\,pp, $p = 0.143$ (n.s.); Qwen3-14B gen, $\\Delta = +2.94$\\,pp, $p = 0.021$ (statistically significant but practically small: 6/204 problems changed). The identical net $\\Delta$ is coincidental---the two generators have different discordant-pair distributions that happen to yield the same net advantage. BR $> 1$ in all eight cells across both datasets (range $1.94$--$2.70$), confirming SCB universality under cross-model extraction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FOLIO $2{\\times}2$ generator${\\times}$extractor matrix ($n{=}204$). SC: Self-Consistency baseline. $\\kappa$: answer-level Fleiss' kappa. BR: bias ratio.}\n\\label{tab:2x2-folio}\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nGenerator & Extractor & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) & BR \\\\\n\\midrule\n\\multirow{2}{*}{\\shortstack[l]{Mistral-7B\\\\{\\scriptsize $\\kappa{=}0.46$}}}\n  & Mistral & 55.88 & 56.86 & $+$0.98 & 2.70 \\\\\n  & Qwen3 & 55.88 & 59.80 & $+$3.92 & 1.94 \\\\\n\\addlinespace\n\\multirow{2}{*}{\\shortstack[l]{Qwen3-14B\\\\{\\scriptsize $\\kappa{=}0.79$}}}\n  & Qwen3 & 83.33 & 84.80 & $+$1.47 & 2.35 \\\\\n  & Mistral & 83.33 & 81.86 & $-$1.47 & 2.66 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Single-Trace and Aggregation Statistics}\n\\label{app:single-trace}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Single-trace accuracy (mean $\\pm$ std over $K{=}12$ traces) and SC@12 majority vote on FOLIO ($n{=}204$). Aggregation gain = SC@12 $-$ single-trace mean. SC@12 uses alphabetical tiebreaking (consistent with Table~\\ref{tab:main_results}).}\n\\label{tab:single-trace-stats}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & Single (\\%) & Std & SC@12 (\\%) & Gain (pp) \\\\\n\\midrule\nMistral-7B & 46.41 & 2.80 & 55.88 & $+$9.47 \\\\\nQwen3-14B & 79.37 & 1.98 & 84.80 & $+$5.43 \\\\\nQwen3-14B (think) & 85.42 & 0.99 & 86.27 & $+$0.86 \\\\\n\\bottomrule\n\\end{tabular}}\\\\[2pt]\n{\\footnotesize Inter-trace standard deviation shrinks $2.8\\times$ from Mistral-7B to Qwen3-14B thinking mode, reflecting the diversity compression that underlies the aggregation ceiling (\\S\\ref{sec:cross-arch}).}\n\\end{table}\n\n\\paragraph{Extraction temperature sensitivity.}\n\\label{app:text-sensitivity}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Effect of extraction temperature $T_{\\text{ext}}$ on SICA accuracy (Mistral-7B, FOLIO $n{=}204$). $^\\dagger$\\,Uses a different trace set (SC $= 54.41\\%$); all other conditions share the same traces (SC $= 55.88\\%$).}\n\\label{tab:text-sensitivity}\n\\begin{tabular}{@{}cccr@{}}\n\\toprule\n$T_{\\text{ext}}$ & SICA (\\%) & $\\Delta$ vs.\\ SC (pp) & Avg.\\ \\#Constr. \\\\\n\\midrule\n0.1 & 57.35 & $+$1.47 & 69.3 \\\\\n$0.3^\\dagger$ & 59.31 & $+$3.43 & 68.8 \\\\\n0.5 & 56.37 & $+$0.49 & 68.2 \\\\\n0.7 & 53.43 & $-$2.45 & 67.3 \\\\\n1.0 & 55.39 & $-$0.49 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nControlling for the trace set (excluding $T_{\\text{ext}} = 0.3$, which uses a different seed), all conditions yield $\\Delta \\leq +1.47$\\,pp (n.s.), indicating that extraction temperature has no significant effect on SICA accuracy. This supports the structural nature of symbolic confirmation bias: the bottleneck is what gets extracted, not the temperature at which extraction occurs.\n\n\\paragraph{Multi-seed replication.}\n\\label{app:multi-seed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Multi-seed replication results across six model$\\times$dataset conditions. Each row uses an independent seed with fresh traces ($K{=}12$, $T{=}0.7$). Mistral-7B$\\times$FOLIO shows directionally unstable $\\Delta$ ($+0.16 \\pm 2.70$\\,pp). Mistral-7B, LLaMA-8B, and Qwen2.5-14B show consistently negative $\\Delta$ on ProofWriter ($p < .001$ for LLaMA-8B and Mistral-7B); Qwen3-14B shows negligible mixed-sign $\\Delta$ ($+0.92 \\pm 1.14$\\,pp, all n.s.), consistent with its high SC baseline minimizing correctable errors (\\S\\ref{sec:discussion}).}\n\\label{tab:multi-seed}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nSeed & SC (\\%) & SICA (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ FOLIO ($n{=}204$)\\textsuperscript{a}}} \\\\\n123 & 54.41 & 57.35 & $+$2.94 \\\\\n456 & 55.88 & 55.88 & 0.00 \\\\\n789 & 59.31 & 56.86 & $-$2.45 \\\\\n\\midrule\nMean $\\pm$ SD & 56.53 $\\pm$ 2.51 & 56.70 $\\pm$ 0.75 & $+$0.16 $\\pm$ 2.70 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ FOLIO ($n{=}204$)}} \\\\\n42 & 77.50 & 75.49 & $-$2.01 \\\\\n123 & 74.51 & 73.04 & $-$1.47 \\\\\n456 & 74.02 & 74.02 & 0.00 \\\\\n789 & 74.02 & 72.55 & $-$1.47 \\\\\n\\midrule\nMean $\\pm$ SD & 75.01 $\\pm$ 1.67 & 73.78 $\\pm$ 1.30 & $-$1.24 $\\pm$ 0.86 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Mistral-7B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 39.33 & 36.50 & $-$2.83 \\\\\n123 & 40.83 & 37.50 & $-$3.33 \\\\\n456 & 39.83 & 38.50 & $-$1.33 \\\\\n789 & 38.83 & 37.17 & $-$1.67 \\\\\n\\midrule\nMean $\\pm$ SD & 39.70 $\\pm$ 0.85 & 37.42 $\\pm$ 0.83 & $-$2.29 $\\pm$ 0.95 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{LLaMA-3.1-8B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 72.50 & 65.00 & $-$7.50 \\\\\n123 & 71.33 & 64.00 & $-$7.33 \\\\\n456 & 71.67 & 66.17 & $-$5.50 \\\\\n789 & 71.17 & 66.50 & $-$4.67 \\\\\n\\midrule\nMean $\\pm$ SD & 71.67 $\\pm$ 0.59 & 65.42 $\\pm$ 1.14 & $-$6.25 $\\pm$ 1.34 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen2.5-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 74.00 & 71.50 & $-$2.50 \\\\\n123 & 72.33 & 70.83 & $-$1.50 \\\\\n456 & 73.00 & 72.17 & $-$0.83 \\\\\n789 & 73.50 & 71.50 & $-$2.00 \\\\\n\\midrule\nMean $\\pm$ SD & 73.21 $\\pm$ 0.71 & 71.50 $\\pm$ 0.55 & $-$1.71 $\\pm$ 0.71 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Qwen3-14B $\\times$ ProofWriter ($n{=}600$)}} \\\\\n42  & 85.83 & 85.67 & $-$0.17 \\\\\n123 & 85.17 & 86.50 & $+$1.33 \\\\\n456 & 84.50 & 86.83 & $+$2.33 \\\\\n789 & 85.50 & 85.67 & $+$0.17 \\\\\n\\midrule\nMean $\\pm$ SD & 85.25 $\\pm$ 0.57 & 86.17 $\\pm$ 0.59 & $+$0.92 $\\pm$ 1.14 \\\\\n\\bottomrule\n\\end{tabular}}\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}\n\\end{table}\n\nOn ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.\n\n\\subsection{Sub-population Analysis}\n\\label{app:subpopulation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by gold-label type (Mistral-7B). Corrected SC baseline uses alphabetical tiebreaking. $\\Delta$\\,pp = SICA $-$ SC. $p$-values from exact McNemar test (two-sided).}\n\\label{tab:subpop-answer-type}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Label} & $n$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{4}{*}{FOLIO-204}\n & True    &  72 & 56.9 & 62.5 & $+$5.6 & .125 \\\\\n & False   &  63 & 42.9 & 42.9 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n & Unknown &  69 & 66.7 & 71.0 & $+$4.3 & .250 \\\\\n & \\textit{Overall} & 204 & 55.9 & 59.3 & $+$3.4 & .092 \\\\\n\\midrule\n\\multirow{4}{*}{PW-600}\n & True    & 200 &  8.5 &  6.0 & $-$2.5 & .063 \\\\\n & False   & 200 & 19.5 & 14.5 & $-$5.0 & .076 \\\\\n & Unknown & 200 & 90.0 & 89.0 & $-$1.0 & .774 \\\\\n & \\textit{Overall} & 600 & 39.3 & 36.5 & $-$2.8 & .014\\rlap{*} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SICA vs.\\ SC accuracy by extracted constraint count tertile (Mistral-7B). Corrected SC baseline (alphabetical tiebreaking). Constraint counts are unique deduplicated constraints per problem.}\n\\label{tab:subpop-constraint}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll rr rrr rr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Tertile} & $n$ & $\\bar{c}$ & \\textbf{SC} & \\textbf{SICA} & $\\Delta$\\,pp & $p$ \\\\\n\\midrule\n\\multirow{3}{*}{FOLIO-204}\n & Low \\scriptsize{[0--32]}   &  74 & 21.7 & 62.2 & 63.5 & $+$1.4 & 1.0\\hphantom{00} \\\\\n & Mid \\scriptsize{[33--47]}  &  64 & 39.7 & 50.0 & 59.4 & $+$9.4 & .031\\rlap{*} \\\\\n & High \\scriptsize{[48--83]} &  66 & 58.7 & 54.5 & 54.5 & $\\pm$0.0 & 1.0\\hphantom{00} \\\\\n\\midrule\n\\multirow{3}{*}{PW-600}\n & Low \\scriptsize{[0--39]}   & 212 & 28.8 & 43.9 & 39.6 & $-$4.3 & .078 \\\\\n & Mid \\scriptsize{[40--52]}  & 196 & 45.8 & 40.8 & 37.2 & $-$3.6 & .143 \\\\\n & High \\scriptsize{[53--99]} & 192 & 63.7 & 32.8 & 32.3 & $-$0.5 & 1.0\\hphantom{00} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn FOLIO-204 with the corrected SC baseline (alphabetical tiebreaking), SICA improves over SC by $+$3.4\\,pp overall (55.9\\% $\\to$ 59.3\\%), though the aggregate McNemar test is marginally non-significant ($p{=}.092$).\nThe gain concentrates in the mid-constraint tertile ($+$9.4\\,pp, $p{=}.031$), where sufficient symbolic evidence exists for MaxSAT to meaningfully re-rank answers; in the low- and high-constraint groups the methods perform comparably.\nOn ProofWriter-600, SICA shows a small uniform degradation consistent with the main results, attenuating in the high-constraint tertile ($\\Delta{=}{-}0.5$\\,pp, $p{=}1.0$).\nWe note that with six subgroup tests, one significant result at $\\alpha{=}0.05$ is expected by chance; the mid-constraint finding should be interpreted as exploratory.\n\n\\paragraph{Individual intervention significance.}\n\\label{app:intervention-individual}\nOf the 27 training-free remediation strategies (Figure~\\ref{fig:interventions-summary}), the two largest positive effects are Cross-model Qwen3$\\to$Mistral ($+0.98$\\,pp) and Generational ($+0.49$\\,pp); neither approaches statistical significance ($p > 0.5$ for both). The largest negative effects are LLM-Debate ($-18.6$\\,pp, $p < 0.001$) and Contrastive Scoring ($-9.3$\\,pp, $p < 0.001$). After BH correction across all 27 comparisons, only these two negative results remain significant. No strategy produces a significant positive effect under any correction procedure.\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\\label{app:limitations-extended}\n\n\\paragraph{SCB versus CoT unfaithfulness.}\nSCB is distinct from CoT unfaithfulness \\citep{turpin2023language} and CoT-level confirmation bias \\citep{wan2025unveiling, jhaveri2026failing}. CoT unfaithfulness concerns whether stated reasoning reflects actual computation; SCB concerns whether \\emph{self-extracted formal constraints} mirror the model's answer distribution. Even if traces were perfectly faithful, self-extraction would still inherit the distributional bias---the constraint $P(\\text{answer\\_A})$ reflects vote share, not logical validity. The shuffle control (\\S\\ref{sec:confirmation-bias}) confirms this: randomizing constraint--answer associations preserves BR, showing the bias is in the trace-count distribution, not in extraction-specific errors. However, if traces are unfaithful, the mirage may be worse than our measurements suggest, because constraints would reflect not the model's reasoning but its post-hoc rationalization.\n\n\\paragraph{Implications for neuro-symbolic practitioners.}\nOur results do not imply that neuro-symbolic methods are inherently flawed---they imply that \\emph{self-extracted} constraints cannot provide independent verification. The key distinction is \\emph{when} formalization occurs relative to answer generation. Specification-generation approaches (e.g., SatLM \\citep{ye2024satlm}, Logic-LM \\citep{pan2023logiclm}) formalize the problem \\emph{before} generating candidate answers, avoiding the extraction bottleneck; SatLM's success confirms that the formal verification mechanism is sound when constraints are independently derived. Trace-extraction (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting the distributional prior that generates SCB. When post-hoc verification is unavoidable, practitioners should employ external verifiers from a different architecture family (\\S\\ref{sec:cross-arch}) and use the diagnostic framework in \\S\\ref{sec:discussion} to assess feasibility before deployment. The SCB diagnostic toolkit (below) provides detailed computation methods and threshold recommendations.\n\n\\paragraph{Test-time scaling implications.}\nVote diversity decreases with model capability: $K_\\text{eff}$ drops from 3.94 (Mistral-7B on ProofWriter) to 1.09 (Qwen3-14B thinking mode). This creates a fundamental tension for o1/R1-style scaling \\citep{guo2025deepseekr1}: longer reasoning chains produce more coherent but less diverse traces, reducing the marginal value of additional samples. Our Process-$\\kappa$ analysis (\\S\\ref{sec:process-kappa}) reveals that this homogenization operates at the reasoning-process level, not just answer level---traces that disagree on final answers still share 69\\% of their reasoning structure. Cross-architecture ensembles offer a path forward, but the capability-gap condition (\\S\\ref{sec:cross-arch}) implies that the verifier must be genuinely complementary, not just different.\n\n\\paragraph{SCB diagnostic toolkit.}\n\\label{app:diagnostic-toolkit}\nWe recommend four zero-cost diagnostics, computable from sampled traces alone, to predict whether symbolic self-verification will help or hurt before deployment.\n\\emph{Bias Ratio} (BR; \\S\\ref{sec:confirmation-bias}): for each problem, compute the fraction of constraints supporting the majority answer, divided by majority vote share. $\\text{BR} > 1$ indicates constraints are biased toward the majority; $\\text{BR} \\gg 2$ (as in all nine models tested; Table~\\ref{tab:frontier-scb}) signals that extraction amplifies rather than checks the model's prior. Report as mean $\\pm$ bootstrap 95\\% CI.\n\\emph{Effective-K} ($K_\\text{eff}$; Eq.~\\ref{eq:effk}): compute Fleiss' $\\kappa$ across $K$ traces, then $K_\\text{eff} = 1 + (K-1)(1-\\kappa)$. Threshold: $K_\\text{eff} \\leq 1.30$ never improves in our experiments---aggregation collapses to majority voting. $K_\\text{eff} > 1.8$ is a necessary (not sufficient) condition for gain.\n\\emph{Degenerate Consensus} ($C_0$; \\S\\ref{sec:condorcet}): the fraction of problems where all $K$ traces agree. $C_0 > 95\\%$ renders aggregation moot; $C_0 < 5\\%$ means the model is maximally uncertain and constraints tend to amplify noise.\n\\emph{ProcessSim} (Eq.~\\ref{eq:process-sim}): mean pairwise cosine similarity of TF-IDF trace vectors. $\\text{ProcessSim} > 0.6$ indicates homogeneous reasoning; combined with $\\text{BR} > 2$, this predicts SCB will dominate.\nA practitioner should compute all four on a held-out sample ($n \\geq 50$). If $K_\\text{eff} \\leq 1.30$ or $C_0 > 95\\%$ or ($\\text{BR} > 2$ and $\\text{ProcessSim} > 0.6$), symbolic self-verification is unlikely to help.\n\n\\paragraph{BR permutation null model.}\n\\label{app:br-permutation}\nThe permutation test referenced in \\S\\ref{sec:confirmation-bias} proceeds as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item For each problem $p$ with extracted constraints $\\{c_1, \\ldots, c_M\\}$ and source answers $\\{a_1, \\ldots, a_M\\}$:\n\\item Randomly permute constraint-to-answer assignments within $p$ (preserving per-trace constraint counts).\n\\item Compute $\\text{BR}_\\text{null}$ from the permuted assignments.\n\\item Repeat $10{,}000$ times to obtain the null distribution.\n\\item Compute $p$-value $= |\\{r : \\text{BR}_\\text{null}^{(r)} \\geq \\text{BR}_\\text{obs}\\}| / 10{,}000$.\n\\end{enumerate}\nAcross all tested conditions, $\\text{BR}_\\text{null} \\approx \\text{BR}_\\text{obs}$ ($p > 0.7$), confirming that the observed bias ratio is fully explained by trace-count geometry under source-attribution scoring (Observation~1), not by an independent extraction bias.\n\n\\paragraph{Future directions: trained extractors and beyond.}\n\\label{app:future-directions}\nOur oracle controls reveal that perfect extraction would yield $+29.90$\\,pp over SC on Mistral-7B FOLIO---self-extraction captures only ${\\sim}12\\%$ of this ceiling. This gap motivates several future directions.\n\\emph{Trained constraint extractors}: fine-tuning a small model (e.g., encoder-only) on human-annotated FOL from logic benchmarks could produce genuinely discriminative constraints that break the distributional prior. The key design constraint is structural independence---the extractor should not share training data or architecture with the generator, mirroring the cross-architecture NLI escape (\\S\\ref{sec:cross-arch}).\n\\emph{Multi-model ensembles}: rather than single cross-architecture pairs, combining $M$ structurally independent verifiers could further reduce correlated errors. The capability-gap condition (\\S\\ref{sec:cross-arch}) predicts that each verifier must exceed the generator on the target task to contribute positively; empirical verification across heterogeneous verifier pools is needed.\n\\emph{External knowledge grounding}: connecting to knowledge bases (Wikidata, domain ontologies) could inject verification signal absent from any model's parameters. This avoids SCB entirely by grounding constraints in external facts rather than self-generated traces.\n\\emph{SCB-aware aggregation}: current MAX-SAT aggregation treats all constraints equally. Weighting constraints by estimated independence (e.g., inverse ProcessSim with other traces' constraints) or by discriminative power (e.g., cross-validation on held-out traces) could partially mitigate SCB without requiring external verifiers.\n\n\\paragraph{SCB as an evaluation framework.}\n\\label{app:scb-evaluation}\nThe SCB metrics---BR, $K_\\text{eff}$, ProcessSim, and CCR---can serve as a general evaluation framework for self-improvement methods beyond SICA. Any method that extracts structured representations from a model's own outputs (self-verification \\citep{huang2024selfcorrect}, self-refinement \\citep{madaan2023selfrefine}, chain-of-verification \\citep{dhuliawala2023chainofverification}, self-consistency \\citep{wang2023sc}) faces the distributional prior that generates SCB. We propose that future work on self-improvement methods report: (1)~BR on error cases (does the method's verification signal correlate with the model's majority answer, or does it provide independent information?); (2)~$K_\\text{eff}$ or an analogous diversity metric (does the method generate genuinely diverse candidates, or does it amplify a single mode?); (3)~CCR (does the method preferentially correct errors, or does it preferentially confirm them?). A method with $\\text{BR} < 1$, high $K_\\text{eff}$, and $\\text{CCR} > 0$ demonstrates genuine self-improvement; $\\text{BR} > 1$ with $\\text{CCR} < 0$ indicates that the method suffers from SCB regardless of aggregate accuracy gains, which may reflect favorable base rates rather than corrective signal.\n\n\\paragraph{Additional scope considerations.}\n\nBeyond the limitations discussed in the main text, several additional constraints bound our conclusions. Seven of our eleven model-domain conditions have $n \\leq 60$, providing insufficient statistical power for confirmatory claims; power analysis shows that the minimum detectable effect exceeds 5\\,pp for these conditions (Table~\\ref{tab:power}), so they serve as regime characterization rather than definitive tests. Our extraction prompts use a single zero-shot template per domain; alternative prompting strategies (few-shot exemplars, chain-of-thought extraction, or iterative refinement) might yield higher-quality constraints, though the oracle gap suggests the bottleneck is structural rather than prompt-specific. The constraint quality analysis (91.8\\% discriminative rate, 39.2\\% source-trace minority weight) covers Qwen2.5-14B on FOLIO + ProofWriter ($N = 804$); other model-domain combinations may exhibit different characteristics. Constraint extraction uses $T_{\\text{ext}} = 0.3$ while trace sampling uses $T = 0.7$; alternative extraction temperatures might yield different results. Although we prompt for first-order logic formalizations, 99.0\\% of extracted constraints are propositional at the Z3 level, with only 1.0\\% using true quantifiers ($\\forall$/$\\exists$); whether models capable of genuine quantified reasoning would yield higher discriminative rates is untested. Deduplication uses syntactic equivalence (global average dedup ratio: 46.0\\%), so semantically equivalent constraints with different surface forms receive separate weights; Z3-based semantic deduplication removes an additional ${\\sim}$10\\% of constraints and yields a small but significant improvement over no deduplication ($p = 0.013$), suggesting room for better dedup strategies. The GSM8K pilot ($n = 30$) illustrates the constraint-absent regime and should not be interpreted as confirmatory evidence.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 1463,
        "oldLines": 7,
        "newStart": 1463,
        "newLines": 7,
        "lines": [
          " {\\footnotesize \\textsuperscript{a}Original baseline (exp033) used no fixed seed and is excluded from seed statistics.}",
          " \\end{table}",
          " ",
          "-On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. Qwen3-14B is the only condition where mean $\\Delta$ is positive ($+0.92 \\pm 1.14$\\,pp), revealing a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92$\\,pp), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
          "+On ProofWriter, all twelve Mistral-7B, LLaMA-8B, and Qwen2.5-14B seeds yield negative $\\Delta$ (range $-0.83$ to $-7.50$\\,pp), with all LLaMA-8B McNemar tests reaching $p < .001$. The results reveal a capability-dependent gradient: LLaMA-8B $\\Delta{=}-6.25$ $\\to$ Mistral-7B $\\Delta{=}-2.29$ $\\to$ Qwen2.5-14B $\\Delta{=}-1.63$ $\\to$ Qwen3-14B $\\Delta{=}+0.92$\\,pp. Qwen3-14B is the sole exception: its 4-seed mean $\\Delta$ is slightly positive ($+0.92 \\pm 1.14$\\,pp, all n.s.), reflecting the capability-modulated pattern discussed in \\S\\ref{sec:discussion}---models with SC baselines above 85\\% leave few correctable errors for SICA to exploit. The consistency across seeds confirms that the sign of $\\Delta$ on ProofWriter is not an artifact of any single random sample but reflects model-level reasoning capacity.",
          " ",
          " \\subsection{Sub-population Analysis}",
          " \\label{app:subpopulation}"
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

_source line 37_

All 3 edits done. Here's the summary:

---

**修改 1 — Caption (L1407)**
- 旧：`three of four ProofWriter conditions show consistently negative Δ (...), while Qwen3-14B is the sole positive condition (+0.92 pp)`
- 新：明确列出三个负 Δ 模型（Mistral-7B, LLaMA-8B, Qwen2.5-14B），Qwen3-14B 描述为 "negligible mixed-sign Δ (+0.92 ± 1.14 pp, all n.s.)"，加 `§\ref{sec:discussion}` 引用（label 确认正确：`\label{sec:discussion}` 在 discussion.tex:2）

**修改 2 — 分析段落 (L1466)**
- 消除原有 "Qwen3-14B is the only condition" 与新增句的重复
- 插入："Qwen3-14B is the sole exception: its 4-seed mean Δ is slightly positive (+0.92 ± 1.14 pp, all n.s.), reflecting the capability-modulated pattern discussed in §discussion—models with SC baselines above 85% leave few correctable errors for SICA to exploit."

**修改 3 — 数据核实**

| 位置 | Qwen2.5-14B FOLIO SC | 状态 |
|------|---------------------|------|
| tab:multi-seed seed42 (appendix L1422) | **77.50** | ✓ 正确 |
| tab:multi-seed 4-seed mean (appendix L1427) | 75.01 | ✓ 正确 (= mean of 77.50, 74.51, 74.02, 74.02) |
| tab:main_results 4s aggregate (experiments L32) | 75.01 | ✓ 与 multi-seed 一致 |

**75.98 出现位置（Qwen2.5-14B 相关）：**

| 文件 | 行 | 表格/上下文 |
|------|-----|-----------|
| diagnosis.tex | 30 | 主诊断表 Type A |
| diagnosis.tex | 41 | Oracle upper bound |
| diagnosis.tex | 70 | tab:independence |
| diagnosis.tex | 158 | SC baseline 表 |
| appendix.tex | 442 | tab:remediation caption |
| appendix.tex | 643, 713-714, 737, 768 | 多个附录表 |
| appendix.tex | 1084, 1112, 1140 | K-sensitivity 表 |

75.98 同时被 Qwen2.5-**7B** (experiments.tex:33) 和 Qwen2.5-**14B** 使用。按 registry 信息（exp-041 SC=77.45%, 75.98 来自 exp-061 即 7B），Qwen2.5-14B 处的 75.98 可能有误，但涉及 ~15 处表格/图/caption，按"不要修改其他表格"约束未动。如需全面修正，建议单独处理。

**附带发现：** 分析段落中 Qwen2.5-14B ProofWriter `Δ=−1.63` 与 multi-seed 表中 mean `−1.71` 不一致（可能来自不同计算方式），未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "uuid": "635da093-d378-465e-a734-22f6cd9c81e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DfivTphCwFr6x718UNxiHK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1849,
      "cache_read_input_tokens": 44978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1849
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

_source line 38_

All 3 edits done. Here's the summary:

---

**修改 1 — Caption (L1407)**
- 旧：`three of four ProofWriter conditions show consistently negative Δ (...), while Qwen3-14B is the sole positive condition (+0.92 pp)`
- 新：明确列出三个负 Δ 模型（Mistral-7B, LLaMA-8B, Qwen2.5-14B），Qwen3-14B 描述为 "negligible mixed-sign Δ (+0.92 ± 1.14 pp, all n.s.)"，加 `§\ref{sec:discussion}` 引用（label 确认正确：`\label{sec:discussion}` 在 discussion.tex:2）

**修改 2 — 分析段落 (L1466)**
- 消除原有 "Qwen3-14B is the only condition" 与新增句的重复
- 插入："Qwen3-14B is the sole exception: its 4-seed mean Δ is slightly positive (+0.92 ± 1.14 pp, all n.s.), reflecting the capability-modulated pattern discussed in §discussion—models with SC baselines above 85% leave few correctable errors for SICA to exploit."

**修改 3 — 数据核实**

| 位置 | Qwen2.5-14B FOLIO SC | 状态 |
|------|---------------------|------|
| tab:multi-seed seed42 (appendix L1422) | **77.50** | ✓ 正确 |
| tab:multi-seed 4-seed mean (appendix L1427) | 75.01 | ✓ 正确 (= mean of 77.50, 74.51, 74.02, 74.02) |
| tab:main_results 4s aggregate (experiments L32) | 75.01 | ✓ 与 multi-seed 一致 |

**75.98 出现位置（Qwen2.5-14B 相关）：**

| 文件 | 行 | 表格/上下文 |
|------|-----|-----------|
| diagnosis.tex | 30 | 主诊断表 Type A |
| diagnosis.tex | 41 | Oracle upper bound |
| diagnosis.tex | 70 | tab:independence |
| diagnosis.tex | 158 | SC baseline 表 |
| appendix.tex | 442 | tab:remediation caption |
| appendix.tex | 643, 713-714, 737, 768 | 多个附录表 |
| appendix.tex | 1084, 1112, 1140 | K-sensitivity 表 |

75.98 同时被 Qwen2.5-**7B** (experiments.tex:33) 和 Qwen2.5-**14B** 使用。按 registry 信息（exp-041 SC=77.45%, 75.98 来自 exp-061 即 7B），Qwen2.5-14B 处的 75.98 可能有误，但涉及 ~15 处表格/图/caption，按"不要修改其他表格"约束未动。如需全面修正，建议单独处理。

**附带发现：** 分析段落中 Qwen2.5-14B ProofWriter `Δ=−1.63` 与 multi-seed 表中 mean `−1.71` 不一致（可能来自不同计算方式），未修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 229862,
  "duration_api_ms": 230967,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "8b5b0dbe-a34d-4d25-9e97-2ef9be512101",
  "total_cost_usd": 0.608901,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 34986,
    "cache_read_input_tokens": 263289,
    "output_tokens": 10258,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34986,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 925,
        "cache_read_input_tokens": 44978,
        "cache_creation_input_tokens": 1849,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1849
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1964,
      "outputTokens": 27,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002099,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 10258,
      "cacheReadInputTokens": 263289,
      "cacheCreationInputTokens": 34986,
      "webSearchRequests": 0,
      "costUSD": 0.606802,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b6a84c08-b56b-4f1c-99f1-5534c4eea5d1"
}
```

</details>

---
