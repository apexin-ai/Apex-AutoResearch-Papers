# paper d048 text modifications

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 156
- **Recorded user turns:** 1
- **Tool calls:** 59
- **Original source:** `logs/workers/worker_paper_d048_text_modifications_20260516T143117.log`
- **Structured JSON:** [`4eb920e05d6955ac66d2.json`](../../sessions/4e/4eb920e05d6955ac66d2.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
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
  "uuid": "5bbd8711-8fa4-4f40-8fc6-7eaa8c80033a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1778958000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "031523ab-1901-4824-9de0-2a1631f25d74",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper files to understand the current state before making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ab8cbf4c-5893-4759-ae69-48e84e87d25b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDKMrs3fopsdPXaBhYPWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12737,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12737
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01Gtz55sft5SfHGhts3ijVj3`</summary>

```json
{
  "description": "Explore paper .tex files",
  "subagent_type": "Explore",
  "prompt": "List all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and search for:\n1. All occurrences of \"31.2\" or \"31\\.2\" — show file, line number, and surrounding context (5 lines)\n2. All occurrences of \"two-channel model\" or \"two-channel degradation model\" — show file, line number, context\n3. All occurrences of \"first\" that might be claiming priority (like \"first controlled\", \"first to show\", \"first study\") — show file, line number, context\n4. All occurrences of \"seed\" — show file, line number, context\n5. All occurrences of \"bootstrap\" — show file, line number, context\n6. All occurrences of \"internal project designation\" — show file, line number, context\n7. The contribution list in introduction.tex — show the full contribution section\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "5fd158b9-ca36-41a0-9a83-07cffd0ab475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDKMrs3fopsdPXaBhYPWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12737,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12737
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Explore paper .tex files",
  "task_type": "local_agent",
  "prompt": "List all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and search for:\n1. All occurrences of \"31.2\" or \"31\\.2\" — show file, line number, and surrounding context (5 lines)\n2. All occurrences of \"two-channel model\" or \"two-channel degradation model\" — show file, line number, context\n3. All occurrences of \"first\" that might be claiming priority (like \"first controlled\", \"first to show\", \"first study\") — show file, line number, context\n4. All occurrences of \"seed\" — show file, line number, context\n5. All occurrences of \"bootstrap\" — show file, line number, context\n6. All occurrences of \"internal project designation\" — show file, line number, context\n7. The contribution list in introduction.tex — show the full contribution section\n\nSearch breadth: very thorough",
  "uuid": "725c522b-eef6-46a7-856e-b3b1cd5b6408",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

## Round 1

150 recorded events

### User

_source line 7 · 2026-05-16T14:31:39.138Z_

List all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and search for:
1. All occurrences of "31.2" or "31\.2" — show file, line number, and surrounding context (5 lines)
2. All occurrences of "two-channel model" or "two-channel degradation model" — show file, line number, context
3. All occurrences of "first" that might be claiming priority (like "first controlled", "first to show", "first study") — show file, line number, context
4. All occurrences of "seed" — show file, line number, context
5. All occurrences of "bootstrap" — show file, line number, context
6. All occurrences of "internal project designation" — show file, line number, context
7. The contribution list in introduction.tex — show the full contribution section

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "da857401-8dd9-4193-b608-7c20f6401418"
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01EDddRN6WKS55rkYB2f99vW`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "cc1e0b6c-d4bf-4d1a-9328-51386ab67900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeDKMrs3fopsdPXaBhYPWG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12737,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12737
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

### Tool result

_source line 9 · 2026-05-16T14:31:39.751Z_

<details><summary>↩ Tool result · `toolu_01EDddRN6WKS55rkYB2f99vW`</summary>

```text
docs/paper/conclusion.tex
docs/paper/prompt_appendix.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/checklist.tex
docs/paper/experimental_setup.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/results.tex
docs/paper/sdgd_negative.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "4b221998-59f5-4b2c-89ec-1367d80b93fe",
  "tool_use_result": {
    "filenames": [
      "docs/paper/conclusion.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/related_work.tex",
      "docs/paper/abstract.tex",
      "docs/paper/checklist.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/results.tex",
      "docs/paper/sdgd_negative.tex"
    ],
    "durationMs": 6,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_18/…",
  "usage": {
    "total_tokens": 18946,
    "tool_uses": 1,
    "duration_ms": 1785
  },
  "last_tool_name": "Glob",
  "uuid": "943e47cd-b1d2-4ed4-97b7-67087f8a2b5b",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_017XH4uxPbn1nCj7ZXATcCt5`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3f90eded-9d1f-498e-83ea-658e0d19b1f7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EzJTyQix2QB4Ys9Cad8QSm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18937,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18937,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 12 · 2026-05-16T14:31:40.936Z_

<details><summary>↩ Tool result · `toolu_017XH4uxPbn1nCj7ZXATcCt5`</summary>

```text
docs/paper/conclusion.tex
docs/paper/prompt_appendix.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/checklist.tex
docs/paper/experimental_setup.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/results.tex
docs/paper/sdgd_negative.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "dc2d1969-0247-4d7d-8f09-79ff6d0f8a9f"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for 31[.]2|31\\.2",
  "usage": {
    "total_tokens": 20013,
    "tool_uses": 2,
    "duration_ms": 4290
  },
  "last_tool_name": "Grep",
  "uuid": "2a411f47-c520-4121-82df-b7432609a60c",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_0197kx3UwFiiAjarSCzFKRqJ`</summary>

```json
{
  "pattern": "31[.]2|31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "2e91c997-f812-4c8c-b309-51393990d8c6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 15 · 2026-05-16T14:31:43.482Z_

<details><summary>↩ Tool result · `toolu_0197kx3UwFiiAjarSCzFKRqJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-86-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-87-& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-88-\cmidrule(lr){2-4} \cmidrule(lr){5-7}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-89-\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-90-\midrule
docs/paper/main.tex:91:8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
docs/paper/main.tex:92:16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-93-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-94-\end{tabular}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-95-\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
docs/paper/main.tex-96-\label{tab:cross_model_bcs}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-97-\end{table}
--
docs/paper/main.tex-212-\label{sec:appendix_prompt_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-213-
docs/paper/main.tex-214-We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-215-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-216-\paragraph{RE (FewRel).}
docs/paper/main.tex:217:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-218-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-219-\paragraph{NER (Few-NERD).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-220-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-221-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-222-\paragraph{Interpretation.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-258-\begin{tabular}{lcrrrr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-259-\toprule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-260-\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-261-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-262-16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
docs/paper/main.tex:263:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
docs/paper/main.tex:264:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-265-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-266-\end{tabular}}
docs/paper/main.tex:267:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
docs/paper/main.tex-268-\label{tab:bcs_controlled}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-269-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-270-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-271-\section{Within-Pool Analysis Methodology}
docs/paper/main.tex-272-\label{app:within-pool-method}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-1-\section{Discussion}
docs/paper/discussion.tex-2-\label{sec:discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-4-\paragraph{Boundary conditions.}
docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-7-\paragraph{Why does embedding similarity predict LLM confusion?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-8-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-10-\paragraph{Schema design implications.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-1-\begin{abstract}
docs/paper/abstract.tex-2-Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-3-
docs/paper/abstract.tex:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-5-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-7-
docs/paper/introduction.tex-8-We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-9-
docs/paper/introduction.tex-10-We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-11-
docs/paper/introduction.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-13-
docs/paper/introduction.tex-14-Our contributions are:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-15-\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
docs/paper/introduction.tex-16-    \item \textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\S\ref{sec:centrality_confound}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-17-    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
--
docs/paper/results.tex-44-\label{tab:pairwise}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-45-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-46-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-47-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-48-
docs/paper/results.tex:49:The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching, reaching 31.2\,pp under extreme-batch construction (\S\ref{sec:practical_magnitude}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-50-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-51-\subsection{BCS-Controlled Experiments}
docs/paper/results.tex-52-\label{sec:bcs_controlled}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-53-
docs/paper/results.tex-54-We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-55-
docs/paper/results.tex:56:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-57-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-58-\paragraph{Document-level RE (DocRED).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-59-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-60-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-61-\paragraph{Within-pool controlled comparison.}
docs/paper/results.tex-62-\label{sec:within_pool}
docs/paper/results.tex:63:Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\,pp) reflects wider BCS range, not stronger per-unit sensitivity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-64-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-65-\paragraph{Practical magnitude.}
docs/paper/results.tex-66-\label{sec:practical_magnitude}
docs/paper/results.tex:67:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-68-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-69-\paragraph{Cross-model validation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-70-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-71-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-72-\paragraph{Prompt sensitivity.}
docs/paper/results.tex:73:Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\ref{sec:appendix_prompt_sensitivity}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-74-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-75-\subsection{Multi-Channel Degradation}
docs/paper/results.tex-76-\label{sec:multi_channel}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-77-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-78-\begin{figure}[t]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1725-\@LN{1472}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1726-\@LN{1473}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1727-\@LN{1474}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1728-\@writefile{toc}{\contentsline {section}{\numberline {J}BCS-Controlled Detailed Results}{17}{appendix.J}\protected@file@percent }
docs/paper/main.aux-1729-\newlabel{app:bcs-controlled-table}{{J}{17}{BCS-Controlled Detailed Results}{appendix.J}{}}
docs/paper/main.aux:1730:[Omitted long matching line]
docs/paper/main.aux:1731:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1732-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1733-\@LN{1475}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1734-\@writefile{toc}{\contentsline {section}{\numberline {K}Within-Pool Analysis Methodology}{17}{appendix.K}\protected@file@percent }
docs/paper/main.aux-1735-\newlabel{app:within-pool-method}{{K}{17}{Within-Pool Analysis Methodology}{appendix.K}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1736-\@LN{1476}{16}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "6d8fd82e-f00b-4aa3-b350-b7d651e9ab7c"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for two-channel (model|degradation model)",
  "usage": {
    "total_tokens": 20014,
    "tool_uses": 3,
    "duration_ms": 4838
  },
  "last_tool_name": "Grep",
  "uuid": "fef53329-b13b-4ea5-ae5e-10007c3e1f8f",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01KR2r7BxtUzYjhFwfXFqBUv`</summary>

```json
{
  "pattern": "two-channel (model|degradation model)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "7ab894c7-2d84-45c7-b4ca-41b43a59a0d4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-16T14:31:44.007Z_

<details><summary>↩ Tool result · `toolu_01KR2r7BxtUzYjhFwfXFqBUv`</summary>

```text
docs/paper/discussion.tex-2-\label{sec:discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-4-\paragraph{Boundary conditions.}
docs/paper/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-7-\paragraph{Why does embedding similarity predict LLM confusion?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-8-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-9-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-10-\paragraph{Schema design implications.}
docs/paper/discussion.tex:11:Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-12-(i)~\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex-13-(ii)~\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;
docs/paper/discussion.tex-14-(iii)~\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\S\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ac0ef4bc-5f70-40da-8838-f1b89b504502"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for first (controlled|to show|study|method|approach|w…",
  "usage": {
    "total_tokens": 20015,
    "tool_uses": 4,
    "duration_ms": 5476
  },
  "last_tool_name": "Grep",
  "uuid": "07c72dd2-3a54-424d-ab42-7bfc7ca780a3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01P4HLh5LkrtrxLLuurcFyNA`</summary>

```json
{
  "pattern": "first (controlled|to show|study|method|approach|work|technique|framework|system)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "5d78eb40-b959-4110-be58-506af9ebae34",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-16T14:31:44.649Z_

<details><summary>↩ Tool result · `toolu_01P4HLh5LkrtrxLLuurcFyNA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-1-\begin{abstract}
docs/paper/abstract.tex:2:Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-3-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-4-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex-5-\end{abstract}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-7-
docs/paper/introduction.tex-8-We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-9-
docs/paper/introduction.tex:10:We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-11-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-12-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex-13-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "4f6a98a3-7a11-4a8a-8f8c-ef5a729d9580"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for seed",
  "usage": {
    "total_tokens": 20016,
    "tool_uses": 5,
    "duration_ms": 6043
  },
  "last_tool_name": "Grep",
  "uuid": "c75c613a-958e-46c5-b915-7eaaea290dd9",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Grep · `toolu_0148Ty7tWBBha9VFhodekpuw`</summary>

```json
{
  "pattern": "seed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "436c6317-c87a-4c73-b3a7-a3449e932270",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-16T14:31:45.212Z_

<details><summary>↩ Tool result · `toolu_0148Ty7tWBBha9VFhodekpuw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-64-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-65-\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-66-
docs/paper/checklist.tex:67:Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-68-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-69-\item \textbf{Did you report descriptive statistics about your results?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-70-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-11-This appendix reproduces the complete prompt templates used for all three extraction tasks.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-12-All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-13-Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
docs/paper/prompt_appendix.tex:14:We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-16-\medskip\noindent
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex-17-\textbf{Notation.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-687-\@LN{562}{6}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-688-\@LN{563}{6}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-689-\@LN@col{2}
docs/paper/main.aux:690:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger $Mean $\pm $ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}}{7}{table.caption.26}\protected@file@percent }
docs/paper/main.aux:691:\newlabel{tab:batch_composition}{{3}{7}{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger $Mean $\pm $ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent}{table.caption.26}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-692-\@LN{564}{6}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-693-\@writefile{toc}{\contentsline {paragraph}{Oracle routing as performance ceiling.}{7}{section*.25}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-694-\@LN{565}{6}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-19-\paragraph{Oracle routing as performance ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-20-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-21-
docs/paper/sdgd_negative.tex:22:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-23-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-24-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-25-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-30-\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-31-\midrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-32-Single-pass (80 types) & 0.504 & 0.557 \\
docs/paper/sdgd_negative.tex:33:Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-34-Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-35-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-36-\end{tabular}}
docs/paper/sdgd_negative.tex:37:\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}
docs/paper/sdgd_negative.tex-38-\label{tab:batch_composition}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-39-\end{table}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex-79-\subsection{Model and Inference}
docs/paper/experimental_setup.tex-80-\label{sec:model}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex-81-
docs/paper/experimental_setup.tex:82:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c7164123-5330-454a-8667-e20fd0e0525c"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for bootstrap",
  "usage": {
    "total_tokens": 20017,
    "tool_uses": 6,
    "duration_ms": 6360
  },
  "last_tool_name": "Grep",
  "uuid": "e97453c7-383a-4949-9baf-2b9db85a38c4",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01H6Kuc98doRBuRcnjbKVR6Y`</summary>

```json
{
  "pattern": "bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "8eb7c465-90ed-45de-858e-316e5b1b52c4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-16T14:31:45.530Z_

<details><summary>↩ Tool result · `toolu_01H6Kuc98doRBuRcnjbKVR6Y`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex-79-\subsection{Model and Inference}
docs/paper/experimental_setup.tex-80-\label{sec:model}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex-81-
docs/paper/experimental_setup.tex:82:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-264-80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-265-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-266-\end{tabular}}
docs/paper/main.tex:267:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
docs/paper/main.tex-268-\label{tab:bcs_controlled}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-269-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-270-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-291-\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-292-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-293-\end{tabular}}
docs/paper/main.tex:294:\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
docs/paper/main.tex-295-\label{tab:within_pool}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-296-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex-297-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-26-\subsection{Pairwise Confusability and Type Confusion}
docs/paper/results.tex-27-\label{sec:pairwise}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-28-
docs/paper/results.tex:29:We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-30-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-31-\begin{table}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-32-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-40-MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-41-\bottomrule
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-42-\end{tabular}}
docs/paper/results.tex:43:[Omitted long matching line]
docs/paper/results.tex-44-\label{tab:pairwise}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-45-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-46-
docs/paper/results.tex:47:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-48-
docs/paper/results.tex-49-The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching, reaching 31.2\,pp under extreme-batch construction (\S\ref{sec:practical_magnitude}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex-50-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-68-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-69-\item \textbf{Did you report descriptive statistics about your results?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-70-
docs/paper/checklist.tex:71:Yes. All key metrics include 95\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-72-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-73-\item \textbf{Did you report implementation details, e.g., versions of packages?}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex-74-
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-439-\@LN{346}{3}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-440-\citation{lost-in-middle-2024}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-441-\@LN@col{1}
docs/paper/main.aux:442:[Omitted long matching line]
docs/paper/main.aux:443:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-444-\@LN{347}{4}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-445-\@LN{348}{4}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-446-\@LN{349}{4}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1727-\@LN{1474}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1728-\@writefile{toc}{\contentsline {section}{\numberline {J}BCS-Controlled Detailed Results}{17}{appendix.J}\protected@file@percent }
docs/paper/main.aux-1729-\newlabel{app:bcs-controlled-table}{{J}{17}{BCS-Controlled Detailed Results}{appendix.J}{}}
docs/paper/main.aux:1730:[Omitted long matching line]
docs/paper/main.aux:1731:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1732-\@LN@col{2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1733-\@LN{1475}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1734-\@writefile{toc}{\contentsline {section}{\numberline {K}Within-Pool Analysis Methodology}{17}{appendix.K}\protected@file@percent }
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1740-\@LN{1480}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1741-\@LN{1481}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1742-\@LN{1482}{16}
docs/paper/main.aux:1743:\@writefile{lot}{\contentsline {table}{\numberline {11}{\ignorespaces Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta $: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref {sec:appendix_within_pool} for CI interpretation.}}{17}{table.caption.61}\protected@file@percent }
docs/paper/main.aux:1744:\newlabel{tab:within_pool}{{11}{17}{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta $: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref {sec:appendix_within_pool} for CI interpretation}{table.caption.61}{}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1745-\@LN{1483}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1746-\@LN{1484}{16}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.aux-1747-\@LN{1485}{16}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "fdd275e0-c190-42fa-880f-ae8e717f5d23"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Searching for internal project designation",
  "usage": {
    "total_tokens": 20018,
    "tool_uses": 7,
    "duration_ms": 6774
  },
  "last_tool_name": "Grep",
  "uuid": "61e5adbd-2b74-460b-8176-2322f6bcb889",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01NDEnoSzsC1FZYCCLyba6om`</summary>

```json
{
  "pattern": "internal project designation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c1047c39-21dd-415c-8f8f-8d64105db15e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N5ZXvvT9vpRc3W4xoYWRNT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 18937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1063,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-16T14:31:45.934Z_

<details><summary>↩ Tool result · `toolu_01NDEnoSzsC1FZYCCLyba6om`</summary>

```text
docs/paper/sdgd_negative.tex-1-\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
docs/paper/sdgd_negative.tex-2-\label{sec:sdgd}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-3-
docs/paper/sdgd_negative.tex:4:A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-5-
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-6-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex-7-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a97bdbe4-ee9a-408b-a982-779688d50889"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 34252,
    "tool_uses": 8,
    "duration_ms": 8646
  },
  "last_tool_name": "Read",
  "uuid": "0415b47f-8b29-4565-9a26-17c9b34bcb73",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_019Q4Q8PB3McJvhrehW8wgoY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0180e5ca-879b-4e94-9199-0a1650c2d2ec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MbCMuBCBwDAoTK5tY6qFGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14231,
      "cache_read_input_tokens": 20000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14231,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-16T14:31:47.801Z_

<details><summary>↩ Tool result · `toolu_019Q4Q8PB3McJvhrehW8wgoY`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
11	
12	Our experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\approx}\,2.2$\,pp (quartile $\Delta = -5.3$\,pp, 95\% CI: [$-$7.4, $-$3.2]; up to 31.2\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\,pp gain.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\S\ref{sec:centrality_confound}).
17	    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
19	    \item \textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\,pp, $p\approx 0.19$). Oracle routing (+29.8\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "cbe63616-d317-4d9e-9ae6-2f7ac99842fa"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "description": "Reading docs/paper/experimental_setup.tex",
  "usage": {
    "total_tokens": 35757,
    "tool_uses": 9,
    "duration_ms": 11178
  },
  "last_tool_name": "Read",
  "uuid": "fe6ffb5f-9bfb-49c0-8bd2-92b3be6e38fc",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01WH6DY2p7rXYKQw1JzxU3qT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "offset": 75,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9b8fd064-19e3-4f9a-bcad-7b43c206439c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01T7KEptbtQLrdYSZMcB5pp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 34231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1503,
        "ephemeral_1h_input_tokens": 0
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

### Tool result

_source line 36 · 2026-05-16T14:31:50.325Z_

<details><summary>↩ Tool result · `toolu_01WH6DY2p7rXYKQw1JzxU3qT`</summary>

```text
75	
76	\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \emph{and} the type matches. \textbf{RE}: accuracy---exact match of predicted relation label to gold. \textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.
77	
78	
79	\subsection{Model and Inference}
80	\label{sec:model}
81	
82	We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single 96\,GB GPU with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}. All metrics include 95\% bootstrap CIs ($B{=}1{,}000$).
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ff64d43f-0e60-491a-bda7-d639be88ba59"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a428d1139e43572a6",
  "tool_use_id": "toolu_01Gtz55sft5SfHGhts3ijVj3",
  "status": "completed",
  "output_file": "",
  "summary": "Explore paper .tex files",
  "usage": {
    "total_tokens": 36268,
    "tool_uses": 9,
    "duration_ms": 29302
  },
  "uuid": "8f8f2dd3-9604-45f3-9542-e88d8417c572",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a"
}
```

---

### Tool result

_source line 38 · 2026-05-16T14:32:08.447Z_

<details><summary>↩ Tool result · `toolu_01Gtz55sft5SfHGhts3ijVj3`</summary>

````text
Perfect! Now let me compile all the findings in a comprehensive report.

## Summary of Search Results

Based on a very thorough search of all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`, here are my findings:

### 1. All Occurrences of "31.2" or "31\.2"

Found in 5 locations across 4 files:

**main.tex (lines 91-92, 263-264, 267):**
- Line 91: `8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\`
- Line 92: `16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\`
- Line 263: `80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\`
- Line 264: `80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\`
- Line 267: Caption text: "The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches."

**results.tex (lines 49, 63, 73):**
- Line 49: "Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching, reaching 31.2\,pp under extreme-batch construction"
- Line 63: "The 80-relation extreme-batch gap (31.2\,pp) reflects wider BCS range, not stronger per-unit sensitivity."
- Line 73: "Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\,pp but highly significant."

### 2. All Occurrences of "Two-Channel Model" or "Two-Channel Degradation Model"

Found in 2 locations:

**introduction.tex (line 16):**
- "\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\S\ref{sec:centrality_confound})."

**discussion.tex (line 11):**
- "Three mitigation strategies follow from the two-channel model:"

### 3. All Occurrences of "First" Claiming Priority/Novelty

Found in 4 locations claiming novelty/primacy:

**abstract.tex (line 2):**
- "We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets..."

**introduction.tex (line 10):**
- "We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED)."

**introduction.tex (line 12):**
- "pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE"

### 4. All Occurrences of "Seed"

Found in 3 locations:

**checklist.tex (line 67):**
- "Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions."

**prompt_appendix.tex (line 14):**
- "We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout."

**experimental_setup.tex (line 82):**
- "We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single 96\,GB GPU with greedy decoding (temperature${}\,=\,0$, seed 42)."

### 5. All Occurrences of "Bootstrap"

Found in 5 locations:

**main.tex (line 267):**
- "The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches."

**main.tex (line 294):**
- "Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$)."

**results.tex (line 29):**
- "For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs."

**checklist.tex (line 71):**
- "Yes. All key metrics include 95\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \S\ref{sec:model}."

**experimental_setup.tex (line 82):**
- "All metrics include 95\% bootstrap CIs ($B{=}1{,}000$)."

### 6. All Occurrences of "Internal Project Designation"

Found in 1 location:

**sdgd_negative.tex (line 4):**
- "SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected."

### 7. Full Contribution Section from introduction.tex

**introduction.tex (lines 14-20):**

```
Our contributions are:
\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
    \item \textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\S\ref{sec:centrality_confound}).
    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
    \item \textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\,pp, $p\approx 0.19$). Oracle routing (+29.8\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.
\end{enumerate}
```

All .tex files found: abstract.tex, checklist.tex, conclusion.tex, discussion.tex, experimental_setup.tex, introduction.tex, main.tex, prompt_appendix.tex, related_work.tex, results.tex, sdgd_negative.tex
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "af5f63ee-e70f-46f3-be5f-d742e404281d",
  "tool_use_result": {
    "status": "completed",
    "prompt": "List all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and search for:\n1. All occurrences of \"31.2\" or \"31\\.2\" — show file, line number, and surrounding context (5 lines)\n2. All occurrences of \"two-channel model\" or \"two-channel degradation model\" — show file, line number, context\n3. All occurrences of \"first\" that might be claiming priority (like \"first controlled\", \"first to show\", \"first study\") — show file, line number, context\n4. All occurrences of \"seed\" — show file, line number, context\n5. All occurrences of \"bootstrap\" — show file, line number, context\n6. All occurrences of \"internal project designation\" — show file, line number, context\n7. The contribution list in introduction.tex — show the full contribution section\n\nSearch breadth: very thorough",
    "agentId": "a428d1139e43572a6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile all the findings in a comprehensive report.\n\n## Summary of Search Results\n\nBased on a very thorough search of all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`, here are my findings:\n\n### 1. All Occurrences of \"31.2\" or \"31\\.2\"\n\nFound in 5 locations across 4 files:\n\n**main.tex (lines 91-92, 263-264, 267):**\n- Line 91: `8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\`\n- Line 92: `16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\`\n- Line 263: `80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\`\n- Line 264: `80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\`\n- Line 267: Caption text: \"The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.\"\n\n**results.tex (lines 49, 63, 73):**\n- Line 49: \"Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching, reaching 31.2\\,pp under extreme-batch construction\"\n- Line 63: \"The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.\"\n- Line 73: \"Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant.\"\n\n### 2. All Occurrences of \"Two-Channel Model\" or \"Two-Channel Degradation Model\"\n\nFound in 2 locations:\n\n**introduction.tex (line 16):**\n- \"\\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).\"\n\n**discussion.tex (line 11):**\n- \"Three mitigation strategies follow from the two-channel model:\"\n\n### 3. All Occurrences of \"First\" Claiming Priority/Novelty\n\nFound in 4 locations claiming novelty/primacy:\n\n**abstract.tex (line 2):**\n- \"We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets...\"\n\n**introduction.tex (line 10):**\n- \"We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED).\"\n\n**introduction.tex (line 12):**\n- \"pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE\"\n\n### 4. All Occurrences of \"Seed\"\n\nFound in 3 locations:\n\n**checklist.tex (line 67):**\n- \"Yes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions.\"\n\n**prompt_appendix.tex (line 14):**\n- \"We use greedy decoding (\\texttt{temperature=0}, \\texttt{seed=42}) throughout.\"\n\n**experimental_setup.tex (line 82):**\n- \"We use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42).\"\n\n### 5. All Occurrences of \"Bootstrap\"\n\nFound in 5 locations:\n\n**main.tex (line 267):**\n- \"The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.\"\n\n**main.tex (line 294):**\n- \"Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$).\"\n\n**results.tex (line 29):**\n- \"For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\"\n\n**checklist.tex (line 71):**\n- \"Yes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}.\"\n\n**experimental_setup.tex (line 82):**\n- \"All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).\"\n\n### 6. All Occurrences of \"Internal Project Designation\"\n\nFound in 1 location:\n\n**sdgd_negative.tex (line 4):**\n- \"SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.\"\n\n### 7. Full Contribution Section from introduction.tex\n\n**introduction.tex (lines 14-20):**\n\n```\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}\n```\n\nAll .tex files found: abstract.tex, checklist.tex, conclusion.tex, discussion.tex, experimental_setup.tex, introduction.tex, main.tex, prompt_appendix.tex, related_work.tex, results.tex, sdgd_negative.tex"
      }
    ],
    "totalDurationMs": 29305,
    "totalTokens": 38329,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 35734,
      "output_tokens": 2081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 510
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2081,
          "cache_read_input_tokens": 35734,
          "cache_creation_input_tokens": 510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 510,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 7,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me read the relevant files to make precise edits. I need to read several files to understand the exact context around each edit point.

Let me plan the work:

### B1: 31.2pp occurrences
From the search results:
- **main.tex lines 91-92, 263-264, 267**: These are in tables and captions — these are data values, not text mentions. The task says to keep 4 explicit textual references. Let me re-read the task.

Wait, looking at the task again:
**Keep**:
1. abstract.tex: "gap reaches 31.2pp under extreme-batch construction" — but the search didn't find 31.2 in abstract.tex! Let me check.


2. introduction.tex: "up to 31.2pp under extreme-batch construction" — not found either!
3. results.tex §4.3 BCS-controlled main result: "−31.2pp (CI: [17.7, 42.7])" — this could be in main.tex table
4. results.tex practical magnitude "The 31.2pp figure reflects..." — not found with that exact wording

**Need to replace** (~5):
5. results.tex §4.2 line 49: "reaching 31.2pp under extreme-batch construction" → delete clause
6. results.tex line 63: "extreme-batch gap" — need to see the full context here

I'm realizing the search results don't match the task's expected locations exactly. I should read the actual files directly to find where these references are and what needs to be changed. I'm looking at the search results more carefully now. The tables contain the raw 31.2 values which should stay as-is, but I need to focus on the explicit textual references. The task asks to reduce from about 9 mentions down to 4 kept references, and I'm trying to identify which files actually contain those references — the search might have missed some occurrences in abstract.tex and introduction.tex that I need to verify. my own grep.

Actually, wait — the task instructions might be anticipating a state where 31.2 appears in specific places. Since those "keep" spots don't currently exist based on my search, maybe the task means I should keep the ones that ARE in those files, and treat table data as separate from explicit text references.

Let me re-read the task more carefully. It says the 4 to keep are specific text mentions. Looking at what actually exists: I found 4 text mentions across the files (in captions and prose) and 4 table data occurrences, totaling 8 instances of "31.2".

Now checking the task's "keep" list against what I found — some of those locations don't seem to exist yet, or maybe the task expects them to be there already but they're not.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "18613b00-254a-47ec-930d-f95aa56cb2e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

### Assistant

_source line 40_

Good, I have a comprehensive map. Let me read the files I need to edit in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0508e186-570a-4a97-9b1c-3192c07cc909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_019TT8jK7BF3AoJUbzo1Tb4B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "e5c75832-3b21-4c8c-b301-98c65b183c63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 42 · 2026-05-16T14:32:40.860Z_

<details><summary>↩ Tool result · `toolu_019TT8jK7BF3AoJUbzo1Tb4B`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\%), FewRel accuracy from 85.7\% to 50.4\% ($-$35.3\,pp), and DocRED from 88.0\% to 38.7\% ($-$56\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.
25	
26	\subsection{Pairwise Confusability and Type Confusion}
27	\label{sec:pairwise}
28	
29	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{llrrrrr}
36	\toprule
37	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
38	\midrule
39	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
40	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
41	\bottomrule
42	\end{tabular}}
43	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}
44	\label{tab:pairwise}
45	\end{table}
46	
47	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
48	
49	The remaining variance likely reflects entity frequency, prompt position \cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\,pp under typical batching, reaching 31.2\,pp under extreme-batch construction (\S\ref{sec:practical_magnitude}).
50	
51	\subsection{BCS-Controlled Experiments}
52	\label{sec:bcs_controlled}
53	
54	We fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
55	
56	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16), confirming monotonic decline.
57	
58	\paragraph{Document-level RE (DocRED).}
59	The effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\,pp at count 16 (slope $= -0.713$, $\rho = -0.661$, $p < 0.001$) and $-$17.6\,pp at count 32 (slope $= -0.690$, $\rho = -0.509$, $p = 0.002$). BCS explains 44--53\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.
60	
61	\paragraph{Within-pool controlled comparison.}
62	\label{sec:within_pool}
63	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\,pp) reflects wider BCS range, not stronger per-unit sensitivity.
64	
65	\paragraph{Practical magnitude.}
66	\label{sec:practical_magnitude}
67	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the 31.2\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \approx 7\%$ among non-zero confusion pairs (vs.\ $r^2 = 1.3$--$1.7\%$ across all pairs; Table~\ref{tab:pairwise}) aggregates to batch-level $R^2 \approx 22\%$ ($\sim$3$\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\ref{app:aggregation-sim}).
68	
69	\paragraph{Cross-model validation.}
70	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\S\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).
71	
72	\paragraph{Prompt sensitivity.}
73	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\ref{sec:appendix_prompt_sensitivity}).
74	
75	\subsection{Multi-Channel Degradation}
76	\label{sec:multi_channel}
77	
78	\begin{figure}[t]
79	\centering
80	\includegraphics[width=\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}
81	\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
82	\label{fig:error_taxonomy}
83	\end{figure}
84	
85	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches.
86	
87	These results establish two channels: \textbf{Channel~1} (count predicts recall decline) and \textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.
88	
89	\subsection{Centrality Confound on Homogeneous Schemas}
90	\label{sec:centrality_confound}
91	
92	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation (Qwen3 $\rho = +0.184$, $p = 0.025$; MiniLM $\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "96355b76-91ee-4b18-a790-a8efbd61c604",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching, reaching 31.2\\,pp under extreme-batch construction (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01Ws96iPZ87TqXVSLt4pjXTh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "7ae54c49-c8ad-48c9-b2ae-9d7e4567c6d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 44 · 2026-05-16T14:32:41.331Z_

<details><summary>↩ Tool result · `toolu_01Ws96iPZ87TqXVSLt4pjXTh`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
9	
10	We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, and MAVEN \cite{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
11	
12	Our experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\approx}\,2.2$\,pp (quartile $\Delta = -5.3$\,pp, 95\% CI: [$-$7.4, $-$3.2]; up to 31.2\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\,pp gain.
13	
14	Our contributions are:
15	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
16	    \item \textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\S\ref{sec:centrality_confound}).
17	    \item \textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.
18	    \item \textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).
19	    \item \textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\,pp, $p\approx 0.19$). Oracle routing (+29.8\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.
20	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "bdd6a164-0736-419e-bb69-b2472b5aecbb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_017H1xaWpk7c1xHbT7vrSVw7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ac7b7577-28d3-40a3-b4be-512b8d3b1c4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 46 · 2026-05-16T14:32:41.809Z_

<details><summary>↩ Tool result · `toolu_017H1xaWpk7c1xHbT7vrSVw7`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \approx 7\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\sim}3\times$, yielding batch-level $R^2 \approx 22\%$ from pair-level $R^2 \approx 7\%$ (Appendix~\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.
9	
10	\paragraph{Schema design implications.}
11	Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:
12	(i)~\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;
13	(ii)~\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;
14	(iii)~\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\S\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.
15	We deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.
16	
17	\paragraph{Cross-domain connections.}
18	Schema complexity effects may parallel findings in schema-guided dialogue systems (\S2; see Appendix~\ref{app:cross-domain} for discussion).
19	
20	\paragraph{Model scale and confusability sensitivity.}
21	Preliminary evidence from two model sizes (32B vs.\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\ref{tab:cross_model}--\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.
22	
23	\paragraph{Future directions.}
24	Three directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\S\ref{sec:sdgd}).
25	
26	\section{Conclusion}
27	\label{sec:conclusion}
28	
29	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count $r = 0.725$, confusability $\Delta = -27$\,pp) and extraction granularities (DocRED: slope $= -0.71$, $R^2 = 0.53$). We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural barrier to NER decomposition, while RE batch composition yields a directional +1.4\,pp gain ($p\approx 0.19$). Cross-batch calibration and broader model validation are key next steps.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "42981faf-01e7-4375-94b1-3058b848725f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.\n\n\\paragraph{Schema design implications.}\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count $r = 0.725$, confusability $\\Delta = -27$\\,pp) and extraction granularities (DocRED: slope $= -0.71$, $R^2 = 0.53$). We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural barrier to NER decomposition, while RE batch composition yields a directional +1.4\\,pp gain ($p\\approx 0.19$). Cross-batch calibration and broader model validation are key next steps.\n",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01PnWNsARo89MSLhjVz35xuq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d2bb5afc-ba08-4cff-89b3-a13d65cb51da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 48 · 2026-05-16T14:32:42.284Z_

<details><summary>↩ Tool result · `toolu_01PnWNsARo89MSLhjVz35xuq`</summary>

```text
1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction (a methodological upper-bound), the gap reaches 31.2\,pp. Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "288b047a-4367-45fe-b929-c45d8ef4cdb5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction (a methodological upper-bound), the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01ExJ2u3AF6AZjNnWpp8Ld8Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "576b88fe-b3a2-480b-829c-446eead2f4aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 50 · 2026-05-16T14:32:43.110Z_

<details><summary>↩ Tool result · `toolu_01ExJ2u3AF6AZjNnWpp8Ld8Z`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	We introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
45	{\small
46	\[
47	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
48	\]
49	}
50	
51	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
52	\[
53	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
54	\]
55	
56	We compute SCS with two embedding models: (1)~Qwen3-32B \cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\,=\,0.034$ vs.\ MiniLM std${}\,=\,0.081$), consistent with known autoregressive anisotropy \cite{ethayarajh-contextual-2019}.
57	
58	\paragraph{SCS as a lightweight proxy.}
59	\label{sec:scs-validation}
60	SCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on Few-NERD ($r = 0.112$, $p < 0.001$) and FewRel ($r = 0.187$, $p < 0.001$). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\S\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.
61	
62	\subsection{Experimental Design}
63	\label{sec:exp_design}
64	
65	We conduct two complementary experimental paradigms.
66	
67	\paragraph{Experiment 1: Count Curves.}
68	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{1, 2, 6, 12, 22, 44, 64\} for Few-NERD, \{1, 4, 8, 16, 32, 64, 80\} for FewRel, \{1, 4, 8, 16, 32, 64, 96\} for DocRED, and \{1, 6, 12, 22, 44, 64\} for MAVEN.
69	
70	\paragraph{Experiment 2: BCS-Controlled.}
71	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
72	
73	\subsection{Evaluation Metrics}
74	\label{sec:metrics}
75	
76	\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \emph{and} the type matches. \textbf{RE}: accuracy---exact match of predicted relation label to gold. \textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.
77	
78	
79	\subsection{Model and Inference}
80	\label{sec:model}
81	
82	We use Qwen3-32B-FP8 \cite{qwen3-2025} served via vLLM v0.20.2 \cite{vllm-2023} on a single 96\,GB GPU with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \cite{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \cite{llama3-2024}. All metrics include 95\% bootstrap CIs ($B{=}1{,}000$).
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "630d131d-54c9-4b3b-9eea-92d0288e88d9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on Few-NERD ($r = 0.112$, $p < 0.001$) and FewRel ($r = 0.187$, $p < 0.001$). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01Mbk61RYhzPkwjt7KF4BQXS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0be637e1-a6d1-4c57-ab7e-f0c023f10357",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3KBBw2vEytGUZnqKkaG1m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "2a96bb83-3c71-4501-b308-a72902ca3792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 53 · 2026-05-16T14:32:43.689Z_

<details><summary>↩ Tool result · `toolu_01Mbk61RYhzPkwjt7KF4BQXS`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
47	
48	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.
49	
50	\item \textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.
51	
52	\item \textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\%$\to$50.4\%) cannot be explained by uniform contamination, which would elevate all conditions equally.
53	\end{enumerate}
54	
55	\input{checklist}
56	
57	\bibliography{references}
58	
59	\appendix
60	
61	\section{Additional Figures}
62	\label{sec:appendix_figures}
63	
64	\begin{table}[h]
65	\centering
66	\small
67	\begin{tabular}{lrr}
68	\toprule
69	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
70	\midrule
71	1 & 0.702 & 0.640 \\
72	64 & 0.273 & 0.304 \\
73	\midrule
74	Decline & $-$43\,pp & $-$34\,pp \\
75	\bottomrule
76	\end{tabular}
77	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
78	\label{tab:cross_model}
79	\end{table}
80	
81	\begin{table}[h]
82	\centering
83	\small
84	\resizebox{\columnwidth}{!}{%
85	\begin{tabular}{crrrrrr}
86	\toprule
87	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
88	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
89	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
90	\midrule
91	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
92	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
93	\bottomrule
94	\end{tabular}}
95	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
96	\label{tab:cross_model_bcs}
97	\end{table}
98	
99	\begin{table}[h]
100	\centering
101	\small
102	\resizebox{\columnwidth}{!}{%
103	\begin{tabular}{llrrrrrrr}
104	\toprule
105	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
106	\cmidrule(lr){3-7}
107	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
108	\midrule
109	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
110	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
111	\midrule
112	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
113	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
114	\bottomrule
115	\end{tabular}}
116	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
117	\label{tab:error_taxonomy}
118	\end{table}
119	
120	\section{SDGD Full Protocol and Results}
121	\label{sec:appendix_sdgd}
122	
123	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
124	
125	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
126	
127	\begin{table}[h]
128	\centering
129	\small
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{lrccc}
132	\toprule
133	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
134	\midrule
135	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
136	\midrule
137	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
138	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
139	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
140	\midrule
141	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
142	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
143	\bottomrule
144	\end{tabular}}
145	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
146	\label{tab:sdgd_results}
147	\end{table}
148	
149	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.
150	
151	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), yielding lower F1 in both modes (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
152	
153	\section{Factorial Analysis}
154	\label{sec:appendix_factorial}
155	
156	We conducted a within-dataset $2\!\times\!2$ factorial analysis (count $\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\S\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p \approx 0.60$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.
157	
158	\section{Within-Pool CI Details}
159	\label{sec:appendix_within_pool}
160	
161	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
162	
163	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
164	\label{sec:appendix_residualized_bcs}
165	
166	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
167	
168	\paragraph{Confound identification.}
169	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
170	\begin{itemize}[itemsep=2pt,leftmargin=*]
171	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.
172	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.
173	\end{itemize}
174	
175	\paragraph{Partial correlation results.}
176	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{llcccc}
183	\toprule
184	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
185	\midrule
186	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
187	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
188	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
189	\midrule
190	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
191	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
192	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
193	\bottomrule
194	\end{tabular}}
195	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
196	\label{tab:residualized_bcs}
197	\end{table}
198	
199	\paragraph{Interpretation.}
200	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
201	
202	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
203	
204	\section{Batch Composition Results}
205	\label{sec:appendix_batch_composition}
206	
207	See Table~\ref{tab:batch_composition} and the accompanying discussion in \S\ref{sec:sdgd}.
208	
209	\input{prompt_appendix}
210	
211	\section{Prompt Version Sensitivity Analysis}
212	\label{sec:appendix_prompt_sensitivity}
213	
214	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
215	
216	\paragraph{RE (FewRel).}
217	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
218	
219	\paragraph{NER (Few-NERD).}
220	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
221	
222	\paragraph{Interpretation.}
223	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.
224	
225	\section{BCS Aggregation Sensitivity}
226	\label{sec:appendix_bcs_sensitivity}
227	
228	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.
229	
230	\begin{table}[h]
231	\centering
232	\small
233	\resizebox{\columnwidth}{!}{%
234	\begin{tabular}{llcccc}
235	\toprule
236	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
237	\midrule
238	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
239	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
240	\midrule
241	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
242	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
243	\bottomrule
244	\end{tabular}}
245	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
246	\label{tab:bcs_aggregation}
247	\end{table}
248	
249	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
250	
251	\section{BCS-Controlled Detailed Results}
252	\label{app:bcs-controlled-table}
253	
254	\begin{table}[h]
255	\centering
256	\small
257	\resizebox{\columnwidth}{!}{%
258	\begin{tabular}{lcrrrr}
259	\toprule
260	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
261	\midrule
262	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
263	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
264	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
265	\bottomrule
266	\end{tabular}}
267	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
268	\label{tab:bcs_controlled}
269	\end{table}
270	
271	\section{Within-Pool Analysis Methodology}
272	\label{app:within-pool-method}
273	
274	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
275	
276	\begin{table}[h]
277	\centering
278	\small
279	\resizebox{\columnwidth}{!}{%
280	\begin{tabular}{lrrrrrrr}
281	\toprule
282	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
283	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
284	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
285	\midrule
286	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
287	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
288	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
289	\midrule
290	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
291	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
292	\bottomrule
293	\end{tabular}}
294	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
295	\label{tab:within_pool}
296	\end{table}
297	
298	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
299	
300	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
301	
302	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
303	\label{app:scs-ablation}
304	
305	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
306	
307	\begin{table}[h]
308	\centering
309	\small
310	\begin{tabular}{lcccc}
311	\toprule
312	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
313	\midrule
314	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
315	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
316	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
317	\bottomrule
318	\end{tabular}
319	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates no systematic benefit from including definitions.}
320	\label{tab:scs-ablation}
321	\end{table}
322	
323	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
324	
325	\section{Pair-to-Batch Aggregation Simulation}
326	\label{app:aggregation-sim}
327	
328	We verify that the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation.
329	
330	\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
331	
332	\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
333	
334	\section{Cross-Domain Connections}
335	\label{app:cross-domain}
336	
337	The schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
338	
339	\end{document}
340	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "4dc9afb4-5389-4721-ad05-37a23677e877",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p \\approx 0.60$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
      "numLines": 340,
      "startLine": 1,
      "totalLines": 340
    }
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T14:32:43.686Z_

<details><summary>↩ Tool result · `toolu_01Q3KBBw2vEytGUZnqKkaG1m`</summary>

```text
1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \textbf{Schema-DAG-Guided Decomposition} (SDGD\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.
5	
6	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\,=\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\ref{tab:sdgd_results}, Appendix~\ref{sec:appendix_sdgd}).
7	
8	\paragraph{Merge amplification in NER.}
9	The core failure mechanism is \emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.
10	
11	Quantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\to$ 0.314 for sdgd\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\to$ 0.251 (sdgd\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\,=\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.
12	
13	\paragraph{Confidence gating does not resolve merge amplification.}
14	Confidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\ref{sec:appendix_sdgd}).
15	
16	\paragraph{Why NER fails but RE does not.}
17	Merge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.
18	
19	\paragraph{Oracle routing as performance ceiling.}
20	Oracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\,pp (Table~\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.
21	
22	However, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\,pp for random batching, +29.8\,pp for graph coloring), the \emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\,pp, $p \approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\resizebox{\columnwidth}{!}{%
28	\begin{tabular}{@{}lcc@{}}
29	\toprule
30	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
31	\midrule
32	Single-pass (80 types) & 0.504 & 0.557 \\
33	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
34	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}
38	\label{tab:batch_composition}
39	\end{table}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "17762e80-c744-49cf-88f6-b54dbc8aeac8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mechanism is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nConfidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01GXDXNFGGFTu6T5Cke2sjbe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9be6b6ae-8c53-4d88-99dc-24fba5ec462a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BnWTsof9BL1grzW8h1Ho5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 130,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 24578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2535
      },
      "output_tokens": 12,
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

_source line 56 · 2026-05-16T14:32:44.256Z_

<details><summary>↩ Tool result · `toolu_01GXDXNFGGFTu6T5Cke2sjbe`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \cite{vllm-2023}, and all-MiniLM-L6-v2 \cite{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9665d391-0df7-4c77-9a2c-358f53738036",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me also check a few more things before making edits:

1. For B4 - Few-NERD description in experimental_setup.tex - I need to add the pairwise analysis line
2. For B7 - Limitations section is in main.tex lines 38-53
3. For B8 item 1 - introduction.tex first paragraph
4. For B8 item 6 - appendix.tex NER metric - I need to check if there's relevant text

Let me also check for "first" claims more carefully, and look at the discussion.tex for the "v1: −31.2pp" mention.


Now I'm mapping out the edits I need to make. For the 31.2pp reduction claim, I'm finding all the text occurrences and deciding which ones to keep or delete - the abstract and introduction findings summary should stay, but I need to remove the redundant clause from results.tex and check the confidence interval mention there. I'm noticing that line 67 actually contains two separate references to the 31.2pp figure—one embedded in the percentage calculation and another in the standalone sentence about maximum BCS contrast. The task wants me to keep the second occurrence while handling the first one, so I need to clarify which instances stay and which get revised.

Looking at the remaining locations, I see there are several more places where the 31.2pp value appears: in results.tex, discussion.tex, and potentially in the appendix and table captions. The task specifies keeping it in four places, but I need to determine whether the appendix and caption references count toward that limit or if they should be handled differently since the original instructions don't explicitly address them. I'm mapping out the remaining replacements for the numeric value across the files. Looking at the appendix sections in main.tex, I see there's a reference in the prompt sensitivity section at line 217 that also needs updating, and the table caption at line 267 contains the same value. The task specifies that after all changes, the number should appear exactly 4 times, so I need to account for which occurrences stay (the table data values and captions) versus which get replaced with the generic reference. I'm seeing a discrepancy in how to count the occurrences. The table data cells contain numeric values that would show up in a grep search, but the task distinguishes between "explicit references" in text versus raw data in tables. If I count everything including table cells, there are far more than 4 instances across the files, but the task specifies reducing from ~9 explicit references down to 4, which suggests the table data might not count toward that target.

Looking at what needs to stay versus what to replace, I can keep the four key textual mentions in the abstract, introduction, and two instances in the results section, then replace the remaining prose references in results and discussion sections to meet the constraint. to the prose mentions only. Let me revise my approach—I need to handle the caption on line 267 and the appendix reference on line 217 as well, replacing them similarly to how I'm handling the main prose mentions. The table data cells themselves are actual experimental results, so those should stay intact. I'll focus on the 5 explicit text replacements plus these two additional locations, leaving the numerical table entries untouched. I'm realizing the appendix text at line 217 is actually reference data from the table showing the prompt sensitivity analysis, so it's legitimate to keep that specific measurement there. Same reasoning applies to the caption. Let me just execute the five replacements from the task list and then verify the count—if it's not four remaining instances, I'll note which ones stay and explain why they're reference data rather than narrative text. I've identified all 9 text references across the files. Now I need to make the 5 replacements systematically—updating the pairwise comparison, within-pool mention, the second practical magnitude reference, prompt sensitivity, and discussion.tex. After those edits, I'll grep to verify we're left with 4 explicit references, though table data and captions might still appear in the results.

For plan B2, I'm replacing the contribution text at introduction.tex line 16, which handles the first occurrence of "two-channel degradation model." I also need to update discussion.tex line 11 where "two-channel model:" appears, changing both to use "decomposition" instead.

Now looking at B3, I'm checking the "first" claims across the abstract and introduction. The abstract and introduction both claim this is "the first controlled study isolating type confusability from type count" across NER, RE, and event detection, but they're missing the specific qualifier about formally isolating via stratified controlled design in zero-shot LLM IE. The introduction has another "first" claim about being the first factor empirically isolated in controlled zero-shot IE, which already has the proper context.

I need to add the qualifier to the abstract and introduction line 10 to make them more precise—something like "the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE" rather than leaving it unqualified.

For the Few-NERD section, I'm adding a sentence about the pairwise analysis covering 1,953 type pairs out of the 2,145 possible pairs at the end of that paragraph.

The seed value is already documented in the experimental setup, so that's covered.

For the R² defense, I need to locate the paragraph in discussion.tex that explains why embedding similarity predicts LLM confusion and add the aggregation mechanism sentence there.

The multiple comparisons limitation should be added as a new item in the Limitations section of main.tex.

For the introduction fixes, I'm inserting the channel labels after the first mention of the count and confusability dimensions, and I need to add a footnote at the first occurrence of "zero-shot."

In sdgd_negative.tex, I'm clarifying that the abbreviation stands for schema decomposition and grouping rather than calling it an internal project designation.

For the checklist, I'm verifying the citations for DocRED, Llama, and the other datasets and models listed.

Now I'm tracking down the bootstrap sample size across the results and experimental setup sections — there's inconsistency between B=1,000 in some places and B=10,000 in others that needs to be resolved. B value inconsistency — results.tex specifies B=10,000 for cluster bootstrap while experimental_setup.tex uses B=1,000 for general bootstrap CIs. The task requires confirming B=10,000 in the main text, but the general bootstrap description currently shows 1,000 instead. I'm realizing the task might be asking for all bootstrap mentions to specify B=10,000, but that would mean changing actual methodology values that differ across the document. The safer approach is to add B values only where they're missing, and I'm checking through the document to see where this applies—most places already have the B value specified in their captions or nearby text.

Now I'm looking at the NER metric definition in the experimental setup section, which describes it as a text-match F1 where predictions are correct if the text string matches case-insensitively and the type matches. The task wants me to expand this in the appendix with details about exact string matching after lowercasing and whitespace normalization.

Since there's no separate appendix.tex file and the NER metric is already described in experimental_setup.tex, I'll add the clarification there rather than creating a new section.

Now I need to verify the "count_40" references against constraint C001 — checking results.tex line 56 where it mentions the 40-relation evaluation sampled from the 80-relation pool, which already aligns with the constraint.

Let me systematically execute all the edits I've identified.

I'm re-examining main.tex line 267 more carefully since it's a long caption with multiple clauses. The line references 31.2pp in a table caption in the appendix, and I need to determine if this falls under the task's scope. The task specifies searching for "31.2" across all .tex files, but this is a caption rather than prose — I should verify whether captions are included in the 9 items already accounted for.

Looking at line 217 in the appendix's prompt sensitivity section, I see another instance of 31.2pp as a specific data point. The task's list of 9 items appears to focus on the main body text, leaving appendix content and table captions unaddressed. After completing my 5 replacements, I'll need to grep for all remaining instances and report them, including these caption and appendix occurrences that weren't explicitly listed.

Let me start with the 5 explicit edits across results.tex and discussion.tex, handling multiple changes in parallel where I can.

For the results section, I need to remove or replace the 31.2pp references at lines 49, 63, 67, and 73. In discussion.tex, I'll change line 5 to use "extreme-batch gap" instead of the specific percentage, and update line 11 to say "two-channel decomposition" rather than "model."

Then I'll move through the other files systematically: introduction.tex needs qualification of "first," a revised contribution statement, and the channel naming convention added; abstract.tex gets the same "first" qualification; experimental_setup.tex needs coverage details for pairwise analysis and NER metrics; sdgd_negative.tex requires rewording the project designation; checklist.tex needs additional citations; and main.tex should have a multiple comparisons discussion added after the limitations. Now I'm mapping out the remaining edits across several files. I need to qualify "first" in the introduction and abstract, replace a contribution statement, add channel labels and a footnote about training-free approaches, update the two-channel degradation model heading, add pairwise coverage details to the experimental setup, include NER metrics, fix the designation text in the negative results section, add missing citations to the checklist, and insert a paragraph about multiple comparisons after the limitations.

For the introduction.tex change on line 10, I'm revising the statement about conducting the first controlled study to emphasize that we're formally isolating confusability from count through a stratified controlled design specifically in zero-shot LLM information extraction, while still covering NER, RE, and event detection.

In the abstract, I'm making a parallel adjustment to keep the language consistent across both sections.

Looking at line 12 of introduction.tex, that phrasing about "the first factor empirically isolated" already captures what we need, so I'll leave it as is.

For the B8 item about the two mechanisms, I need to introduce the Channel labels after mentioning confusability. Rather than awkward double parentheses, I should integrate this more smoothly by renaming the concepts directly in the sentence.

Now I'm working through the footnote for B8 item 2, which will need similar treatment to establish the Channel terminology consistently throughout. Now I'm finishing that sentence about batch-level effects and adding the practical contribution of schema-level diagnostics. Then I need to insert a multiple comparisons paragraph in the Limitations section, though I'm second-guessing whether to use `\paragraph` within the enumerated list or structure it differently. I'm debating whether to add this as a new item within the enumerate or close the list first and add it as a standalone paragraph. The task specifically mentions `\paragraph{Multiple comparisons}`, which suggests it should be a paragraph element rather than an enumerated item, so I'll close the enumerate and add the paragraph after it to maintain proper LaTeX structure.

Now I'm moving on to check the other tasks—the B5 seeds are already documented so I can skip that, but for B8 item 5 about the bootstrap B value, I need to look at the table caption in results.tex more carefully since the text mentions bootstrap confidence intervals but doesn't specify B=10,000 explicitly, even though the caption does.

Actually, I'm noticing there's a potential inconsistency here—the general statement in experimental_setup.tex says B=1,000 but some specific analyses like the cluster bootstrap use B=10,000, and these might be intentionally different based on the actual methodology, so I should probably leave the values as they are rather than forcing consistency where there might be methodological reasons for the differences.

Looking at the task more carefully, it seems like I need to add B values where they're missing rather than change existing ones. In results.tex line 29, "bootstrap 95% CIs" doesn't specify B, but the table caption right after it says B=1,000, so I should add that value to the text to match the context. I need to standardize all bootstrap B values to 10,000 across the paper. Looking at the specific locations where changes are needed: experimental_setup.tex has B=1,000 that should become B=10,000, the results table caption needs the same update, checklist.tex references 1,000 resamples that should be 10,000, and there's at least one place in results.tex where B is missing entirely and needs to be added. Let me proceed with these edits systematically across all files. I'm mapping out all the edits I need to make across these files, then checking whether I can run them in parallel or need to do them sequentially. For results.tex, I have four separate bootstrap fixes that should each target unique strings, so I can execute them together as long as each one matches exactly once in the file. I'm working through the edits systematically by file. For results.tex, I need to remove the specific "31.2\,pp" mentions and replace them with either section references or more general language—deleting the extreme-batch construction phrase from line 49, swapping a numeric reference for a section link on line 63, and simplifying the gap descriptions on lines 67 and 73. Then I'll move to discussion.tex with similar replacements. I'm revising the second contribution bullet point to emphasize the mechanistic distinction between count and confusability as separate degradation channels, with count driving recall loss and confusability driving type substitution errors, and I need to verify the correct section reference for the multi-channel analysis.

Now I'm working through several edits to the paper: adding channel labels to distinguish the two degradation mechanisms, inserting a footnote to clarify the interchangeability of "training-free" and "zero-shot" terminology, and refining the abstract to emphasize that this is the first formal isolation of type confusability from type count across multiple extraction tasks. I need to clarify where these edits belong—the appendix versus main body. For the NER metric description, I'm adding detail about whitespace normalization and how partial spans are handled. Then I'm updating the SDGD abbreviation definition and fixing the checklist citations to include the proper references for DocRED and the Llama model. I'm continuing with the citation fixes—adding DocRED with its citation and the Llama reference. Then I need to update the main.tex file to include a paragraph about multiple comparisons correction in the Limitations section, and note that the bootstrap analysis uses B=10000 iterations.

Now I'm going through the remaining edits to update all references to the bootstrap sample size from 1,000 to 10,000 across the setup configuration, results table caption, checklist, and the main results text. I should verify that the pairwise table caption in results.tex has a unique instance of this value before making the change. I'm checking whether the B parameter appears consistently across all the bootstrap references in the document. The pairwise table caption specifies B=1,000, and I see the same notation in the experimental setup section. For the checklist reference to 1,000 resamples, that's also unique. I notice line 29 in results.tex mentions bootstrap CIs without specifying B, so I should add that parameter there for consistency with the table caption.

Now I'm realizing the task requires B=10,000 as the correct value throughout, so I need to update the bootstrap resample counts in experimental_setup.tex, the results table caption, and checklist.tex from 1,000 to 10,000, and ensure B=10,000 appears wherever bootstrap resamples are mentioned.

Let me verify my edit locations are all unique and non-overlapping before proceeding with the batch changes. I'm making 6 edits to results.tex, 3 to discussion.tex, and several others across the remaining files—all the target strings are distinct within their respective files, so I can execute them in parallel.

Now I need to confirm the scope of the "two-channel model" to "two-channel decomposition" replacement. Looking at the search results, I found it appears in introduction.tex at line 16 within a bold section.

I'm also checking discussion.tex more carefully—there are two instances there on lines 4 and 11, both using "two-channel model" in different contexts. Let me verify whether the abstract mentions this term as well before finalizing the replacement list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a1cc5daf-91a0-4994-aec3-69f35de1ce77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4rxD1YdhmtQQFw2MBb7Lt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25173,
      "cache_read_input_tokens": 27113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25173
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

_source line 58_

I have a complete picture of all occurrences. Now making all edits across files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "246badd1-aa63-44c9-ac2e-0cfb63b48f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4rxD1YdhmtQQFw2MBb7Lt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25173,
      "cache_read_input_tokens": 27113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25173
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

_source line 59_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016RQEo5KcjphcEakgQP4MvC`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "58a89869-5d1a-4907-86d1-04dec160989e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4rxD1YdhmtQQFw2MBb7Lt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25173,
      "cache_read_input_tokens": 27113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25173
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

_source line 60 · 2026-05-16T14:37:28.815Z_

<details><summary>↩ Tool result · `toolu_016RQEo5KcjphcEakgQP4MvC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9c21598e-925d-4df0-a12a-675dad017153",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Let me set up the todo list and start making edits. I'll make all independent edits in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "cfcda999-f9d9-4293-a4b8-24d009f8b1f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnyFbcWyaKd8oyPPncCnnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16654,
      "cache_read_input_tokens": 52286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16654
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 62_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01BDxH3Vxe93xVNc9aYxyJLd`</summary>

```json
{
  "todos": [
    {
      "content": "B1: 31.2pp削减 (5处替换)",
      "status": "in_progress",
      "activeForm": "Replacing 31.2pp references"
    },
    {
      "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
      "status": "pending",
      "activeForm": "Rewriting contribution #1 and replacing terminology"
    },
    {
      "content": "B3: first controlled study 限定",
      "status": "pending",
      "activeForm": "Qualifying 'first' claims"
    },
    {
      "content": "B4: Few-NERD pairwise coverage",
      "status": "pending",
      "activeForm": "Adding pairwise coverage info"
    },
    {
      "content": "B5: Seeds确认",
      "status": "pending",
      "activeForm": "Checking seed documentation"
    },
    {
      "content": "B6: r² defense in Discussion",
      "status": "pending",
      "activeForm": "Adding r² defense sentence"
    },
    {
      "content": "B7: Multiple comparisons in Limitations",
      "status": "pending",
      "activeForm": "Adding multiple comparisons paragraph"
    },
    {
      "content": "B8: Minor fixes (6项)",
      "status": "pending",
      "activeForm": "Applying minor fixes"
    },
    {
      "content": "编译验证 + grep检查",
      "status": "pending",
      "activeForm": "Compiling and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "1040acc0-5f6a-45a3-95d0-ef95347da8e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnyFbcWyaKd8oyPPncCnnG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16654,
      "cache_read_input_tokens": 52286,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16654
      },
      "output_tokens": 19,
      "service_tier": "standard",
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

_source line 63 · 2026-05-16T14:37:39.163Z_

<details><summary>↩ Tool result · `toolu_01BDxH3Vxe93xVNc9aYxyJLd`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "8c631aba-76e0-4235-b436-a861ee51acca",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "B1: 31.2pp削减 (5处替换)",
        "status": "in_progress",
        "activeForm": "Replacing 31.2pp references"
      },
      {
        "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
        "status": "pending",
        "activeForm": "Rewriting contribution #1 and replacing terminology"
      },
      {
        "content": "B3: first controlled study 限定",
        "status": "pending",
        "activeForm": "Qualifying 'first' claims"
      },
      {
        "content": "B4: Few-NERD pairwise coverage",
        "status": "pending",
        "activeForm": "Adding pairwise coverage info"
      },
      {
        "content": "B5: Seeds确认",
        "status": "pending",
        "activeForm": "Checking seed documentation"
      },
      {
        "content": "B6: r² defense in Discussion",
        "status": "pending",
        "activeForm": "Adding r² defense sentence"
      },
      {
        "content": "B7: Multiple comparisons in Limitations",
        "status": "pending",
        "activeForm": "Adding multiple comparisons paragraph"
      },
      {
        "content": "B8: Minor fixes (6项)",
        "status": "pending",
        "activeForm": "Applying minor fixes"
      },
      {
        "content": "编译验证 + grep检查",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Now let me make all the edits in parallel. I'll group them by file and send them all at once.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3f37d81c-0edb-4e22-90e4-cfbb32165b55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 65_

Making all edits now across all files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0d4ea168-f3ee-4925-86f5-0cc987c1654e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_012odWKMytcfLZBexqB52zLS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": ", reaching 31.2\\,pp under extreme-batch construction (\\S\\ref{sec:practical_magnitude}).",
  "new_string": " (\\S\\ref{sec:practical_magnitude})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "b3112df3-f4fe-4992-a351-4a4adff3c854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 67 · 2026-05-16T14:37:47.083Z_

<details><summary>↩ Tool result · `toolu_012odWKMytcfLZBexqB52zLS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3c87eac3-2e1d-4ecd-8cdb-be0d027fc402",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": ", reaching 31.2\\,pp under extreme-batch construction (\\S\\ref{sec:practical_magnitude}).",
    "newString": " (\\S\\ref{sec:practical_magnitude}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching, reaching 31.2\\,pp under extreme-batch construction (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " ",
          " The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).",
          " ",
          "-The remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching, reaching 31.2\\,pp under extreme-batch construction (\\S\\ref{sec:practical_magnitude}).",
          "+The remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).",
          " ",
          " \\subsection{BCS-Controlled Experiments}",
          " \\label{sec:bcs_controlled}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01X1geagasQ5jxXFvDsxrdBM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.",
  "new_string": "The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "99fb01de-24fd-4f9a-b4fa-f5e03163e7ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 69 · 2026-05-16T14:37:52.734Z_

<details><summary>↩ Tool result · `toolu_01X1geagasQ5jxXFvDsxrdBM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a7b9a0f2-95f4-4cd4-8917-56657df959e8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.",
    "newString": "The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 60,
        "oldLines": 7,
        "newStart": 60,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Within-pool controlled comparison.}",
          " \\label{sec:within_pool}",
          "-Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (31.2\\,pp) reflects wider BCS range, not stronger per-unit sensitivity.",
          "+Within-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.",
          " ",
          " \\paragraph{Practical magnitude.}",
          " \\label{sec:practical_magnitude}"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01UnkHjPdMah7oKa1tbB3Je3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "7\\% of the 31.2\\,pp extreme-batch gap",
  "new_string": "7\\% of the extreme-batch gap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "fd629038-65c9-4a76-b3a0-4143cee9c795",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 71 · 2026-05-16T14:37:54.130Z_

<details><summary>↩ Tool result · `toolu_01UnkHjPdMah7oKa1tbB3Je3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "42c72f01-bf2d-402d-bae5-88e45f377062",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "7\\% of the 31.2\\,pp extreme-batch gap",
    "newString": "7\\% of the extreme-batch gap",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 7,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Practical magnitude.}",
          " \\label{sec:practical_magnitude}",
          "-For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the 31.2\\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).",
          "+For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).",
          " ",
          " \\paragraph{Cross-model validation.}",
          " The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1)."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01QpKeSrXsdssZN24BAY4D9X`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "v1's $-$31.2\\,pp but highly significant",
  "new_string": "v1's extreme-batch gap but highly significant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "73bf8c84-06d2-4f67-9d60-26976d0ecd76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 73 · 2026-05-16T14:37:54.496Z_

<details><summary>↩ Tool result · `toolu_01QpKeSrXsdssZN24BAY4D9X`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "b89a4af8-bf5e-4d02-bb24-350cd736f684",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "v1's $-$31.2\\,pp but highly significant",
    "newString": "v1's extreme-batch gap but highly significant",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 70,
        "oldLines": 7,
        "newStart": 70,
        "newLines": 7,
        "lines": [
          " The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).",
          " ",
          " \\paragraph{Prompt sensitivity.}",
          "-Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's $-$31.2\\,pp but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          "+Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          " ",
          " \\subsection{Multi-Channel Degradation}",
          " \\label{sec:multi_channel}"
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

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01SikscDMtXxapKUXBNESgSx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "v1: $-$31.2\\,pp",
  "new_string": "v1 extreme-batch gap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ecd45c5b-f8d0-4f7d-91ba-2ed65f9b04b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 75 · 2026-05-16T14:37:54.724Z_

<details><summary>↩ Tool result · `toolu_01SikscDMtXxapKUXBNESgSx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "82e5b87e-08ae-4743-8f77-4402848e9e2f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "v1: $-$31.2\\,pp",
    "newString": "v1 extreme-batch gap",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.\n\n\\paragraph{Schema design implications.}\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count $r = 0.725$, confusability $\\Delta = -27$\\,pp) and extraction granularities (DocRED: slope $= -0.71$, $R^2 = 0.53$). We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural barrier to NER decomposition, while RE batch composition yields a directional +1.4\\,pp gain ($p\\approx 0.19$). Cross-batch calibration and broader model validation are key next steps.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Boundary conditions.}",
          "-The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1: $-$31.2\\,pp; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          "+The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          " ",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          " Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal."
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

<details open><summary>🔧 Tool call — Edit · `toolu_017Z62KHsXgJDo6wcpxsVneK`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "two-channel model",
  "new_string": "two-channel decomposition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d370e271-1d4b-4bf6-b7e5-c97d8711788c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 77 · 2026-05-16T14:37:55.016Z_

<details><summary>↩ Tool result · `toolu_017Z62KHsXgJDo6wcpxsVneK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c0305de7-faee-4aef-87f1-447d80a244a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "two-channel model",
    "newString": "two-channel decomposition",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.\n\n\\paragraph{Schema design implications.}\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count $r = 0.725$, confusability $\\Delta = -27$\\,pp) and extraction granularities (DocRED: slope $= -0.71$, $R^2 = 0.53$). We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural barrier to NER decomposition, while RE batch composition yields a directional +1.4\\,pp gain ($p\\approx 0.19$). Cross-batch calibration and broader model validation are key next steps.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 13,
        "newStart": 2,
        "newLines": 13,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Boundary conditions.}",
          "-The two-channel model applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          "+The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          " ",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          " Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.",
          " ",
          " \\paragraph{Schema design implications.}",
          "-Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel model:",
          "+Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:",
          " (i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;",
          " (ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;",
          " (iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_01R2N8g8uc2sB2Pkq7tXMogX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "despite the modest pairwise signal.",
  "new_string": "despite the modest pairwise signal. The modest pairwise effect is expected: individual substitution events are noisy and multi-causal. The practical contribution of SCS lies at the schema level, where batch-level BCS explains 22--53\\% of accuracy variance---sufficient for pre-hoc schema screening."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "46829e17-2b7f-4240-9338-b51af148027e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 79 · 2026-05-16T14:37:57.172Z_

<details><summary>↩ Tool result · `toolu_01R2N8g8uc2sB2Pkq7tXMogX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "051dad5a-53ee-4ef2-97e0-89808d51717b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "oldString": "despite the modest pairwise signal.",
    "newString": "despite the modest pairwise signal. The modest pairwise effect is expected: individual substitution events are noisy and multi-causal. The practical contribution of SCS lies at the schema level, where batch-level BCS explains 22--53\\% of accuracy variance---sufficient for pre-hoc schema screening.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\nThe two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\paragraph{Why does embedding similarity predict LLM confusion?}\nType name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.\n\n\\paragraph{Schema design implications.}\nOur findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:\n(i)~\\emph{Expand definitions}---for high-SCS pairs, include contrastive definitions or disambiguating examples in the prompt to increase representational separation;\n(ii)~\\emph{Rename types}---replace semantically proximate labels with more descriptive alternatives (e.g., ``person-artist'' $\\to$ ``visual artist (painter/sculptor)'') to reduce embedding overlap;\n(iii)~\\emph{Decompose batches}---assign high-SCS pairs to different extraction passes using graph coloring on the SCS-thresholded confusability graph (\\S\\ref{sec:sdgd}), accepting the precision--recall trade-off that merge introduces.\nWe deliberately avoid recommending a fixed SCS threshold, as optimal granularity is task-dependent: the acceptable confusion rate depends on downstream costs, schema size, and available compute budget for multi-pass extraction.\n\n\\paragraph{Cross-domain connections.}\nSchema complexity effects may parallel findings in schema-guided dialogue systems (\\S2; see Appendix~\\ref{app:cross-domain} for discussion).\n\n\\paragraph{Model scale and confusability sensitivity.}\nPreliminary evidence from two model sizes (32B vs.\\ 8B) suggests that Channel~2 (confusability) effects attenuate on smaller models due to floor effects, while Channel~1 (count) replicates fully (Tables~\\ref{tab:cross_model}--\\ref{tab:cross_model_bcs}). Systematic scaling studies remain future work.\n\n\\paragraph{Future directions.}\nThree directions merit investigation: (i)~non-oracle routing strategies that make decomposition deployable without gold labels; (ii)~broader model coverage, particularly proprietary APIs; and (iii)~definition-inclusive SCS (current name+definition ablation shows no systematic improvement; Appendix~\\ref{app:scs-ablation}). For NER, calibration-aware merge or joint decoding may address merge amplification (\\S\\ref{sec:sdgd}).\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE and replicate across model families (Llama-3.1-8B: count $r = 0.725$, confusability $\\Delta = -27$\\,pp) and extraction granularities (DocRED: slope $= -0.71$, $R^2 = 0.53$). We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural barrier to NER decomposition, while RE batch composition yields a directional +1.4\\,pp gain ($p\\approx 0.19$). Cross-batch calibration and broader model validation are key next steps.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " The two-channel decomposition applies to cross-domain schemas; same-domain schemas (e.g., MAVEN's FrameNet-derived event types) exhibit centrality confounding that obscures per-type aggregated signals, requiring pairwise SCS or centrality adjustment (\\S\\ref{sec:centrality_confound}). High-BCS accuracy converges to $\\approx$51\\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\\,pp vs.\\ v1 extreme-batch gap; Appendix~\\ref{sec:appendix_prompt_sensitivity}).",
          " ",
          " \\paragraph{Why does embedding similarity predict LLM confusion?}",
          "-Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal.",
          "+Type name embeddings capture semantic proximity in the same representational space that LLMs use for in-context type resolution. When two type names are close in embedding space, we hypothesize that the model's attention mechanism may produce overlapping key--query representations for those types, increasing the probability of substitution errors. This mechanistic link explains why a simple cosine similarity metric predicts extraction failures: high SCS directly indexes the degree of representational overlap that causes confusion during decoding. Critically, the pair-level effect is modest ($R^2 \\approx 7\\%$ over non-zero confusion pairs) because individual substitution events are stochastic and influenced by many factors beyond type similarity. However, pairs sharing a common type exhibit correlated SCS values ($\\rho = 0.35$), so when multiple high-SCS pairs co-occur in a batch, their effects aggregate constructively: noise averages out while the confusability signal is preserved. Monte Carlo simulation confirms that this inter-pair correlation produces an effective amplification of ${\\sim}3\\times$, yielding batch-level $R^2 \\approx 22\\%$ from pair-level $R^2 \\approx 7\\%$ (Appendix~\\ref{app:aggregation-sim}). This aggregation mechanism explains why weak individual pair effects produce strong batch-level degradation---and why BCS (the mean pairwise SCS) is a useful schema-level diagnostic despite the modest pairwise signal. The modest pairwise effect is expected: individual substitution events are noisy and multi-causal. The practical contribution of SCS lies at the schema level, where batch-level BCS explains 22--53\\% of accuracy variance---sufficient for pre-hoc schema screening.",
          " ",
          " \\paragraph{Schema design implications.}",
          " Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01B5eDgVbo8MUTLvaZM2eEzj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED).",
  "new_string": "We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "be8ab838-5efd-4207-8e77-a2f092034324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 81 · 2026-05-16T14:38:00.472Z_

<details><summary>↩ Tool result · `toolu_01B5eDgVbo8MUTLvaZM2eEzj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3a9acf0e-28e8-4cfb-9930-72f09eaea9b9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED).",
    "newString": "We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " ",
          " We ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?",
          " ",
          "-We conduct the first controlled study isolating type confusability from type count across NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).",
          "+We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).",
          " ",
          " Our experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
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

_source line 82_

<details open><summary>🔧 Tool call — Edit · `toolu_017kAYH6kLstE4eAMVGG4Sts`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).",
  "new_string": "    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "fa40b1ec-5cda-4da1-9afe-5dae6ed80a26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 83 · 2026-05-16T14:38:05.633Z_

<details><summary>↩ Tool result · `toolu_017kAYH6kLstE4eAMVGG4Sts`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "e0237686-c195-439b-85ba-20692063b40e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).",
    "newString": "    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]",
          "-    \\item \\textbf{Two-channel degradation model.} Type count and confusability separately predict extraction quality: count scaling degrades performance on cross-domain schemas (NER, RE; up to $-49$\\,pp), while same-domain schemas (ED) exhibit confound-driven reversal with pairwise confusability signal still detectable (\\S\\ref{sec:centrality_confound}).",
          "+    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).",
          "     \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.",
          "     \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).",
          "     \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains."
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Tvsa9hWcs7JP778ZaCESkD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "(confusability). None isolates",
  "new_string": "(confusability) (hereafter Channel~1 and Channel~2). None isolates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "acbc71a6-5f19-4163-becb-ef4ddd17f469",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 85 · 2026-05-16T14:38:07.108Z_

<details><summary>↩ Tool result · `toolu_01Tvsa9hWcs7JP778ZaCESkD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3d49d366-22a3-47e3-84e4-10413cc98a4f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "(confusability). None isolates",
    "newString": "(confusability) (hereafter Channel~1 and Channel~2). None isolates",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.",
          " ",
          "-What causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).",
          "+What causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).",
          " ",
          " We ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?",
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

_source line 86_

<details open><summary>🔧 Tool call — Edit · `toolu_01PNfJs5d2G82QK52evEtctw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "Training-free LLM information extraction",
  "new_string": "Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a63b9c8a-4010-4e4c-a112-df5bb8d610af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 87 · 2026-05-16T14:38:09.485Z_

<details><summary>↩ Tool result · `toolu_01PNfJs5d2G82QK52evEtctw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "1e774a5e-eec9-4e1a-9584-567064f79785",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "Training-free LLM information extraction",
    "newString": "Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.\n\nWhat causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what mechanisms do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\nWe present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We operationalize confusability via the \\emph{Schema Confusability Score} (SCS)---pairwise embedding cosine similarity---and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, and MAVEN \\cite{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield five findings: (1)~degradation operates through two empirically separable channels---a confusability channel with a typical-batch gap of ${\\approx}\\,2.2$\\,pp (quartile $\\Delta = -5.3$\\,pp, 95\\% CI: [$-$7.4, $-$3.2]; up to 31.2\\,pp under extreme-batch construction), and a count channel associated with recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item \\textbf{Controlled evidence for two degradation channels.} Count and confusability constitute mechanistically distinguishable dimensions: count predicts recall decline while confusability predicts type substitution, with differential error signatures (\\S\\ref{sec:multi_channel}).\n    \\item \\textbf{Pairwise confusability as predictor.} SCS predicts type confusion ($r = 0.112$--$0.129$) while centrality confounds per-type aggregation on homogeneous schemas.\n    \\item \\textbf{Cross-task BCS-controlled experiments.} BCS--accuracy slopes are consistent across schema sizes ($p = 0.60$) and replicate at document level (DocRED: $R^2 = 0.53$).\n    \\item \\textbf{Diagnosis to mitigation.} Schema decomposition proves structurally infeasible for NER (merge amplification collapses precision from 0.56 to 0.21) and yields no statistically significant improvement for RE (graph-coloring: +1.4\\,pp, $p\\approx 0.19$). Oracle routing (+29.8\\,pp) confirms the performance ceiling exists but highlights the gap between theoretical and achievable gains.\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:introduction}",
          " ",
          "-Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.",
          "+Training-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \\cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\\% relative decline. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.",
          " ",
          " What causes this degradation? Prior decomposition strategies \\cite{uniner-2024,llm-pee-2025,parse-2025} conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Channel~1 and Channel~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).",
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

_source line 88_

<details open><summary>🔧 Tool call — Edit · `toolu_01YGHGC9jpfbbhAoLgsve9H9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets",
  "new_string": "We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "7d3d12f0-b522-4388-a30b-568c55ad01b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 89 · 2026-05-16T14:38:11.292Z_

<details><summary>↩ Tool result · `toolu_01YGHGC9jpfbbhAoLgsve9H9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c0f00fc0-81b9-4a93-93bd-6ef39c4af725",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "oldString": "We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets",
    "newString": "We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets",
    "originalFile": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction (a methodological upper-bound), the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\begin{abstract}",
          "-Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.",
          "+Training-free LLM information extraction degrades as schema complexity grows. We present the first study to formally isolate type confusability from type count via stratified controlled design in zero-shot LLM IE, spanning NER, RE (a closed-set classification task), and event detection across four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.",
          " ",
          " We identify two empirically separable degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction (a methodological upper-bound), the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. Count increases generally suppress extraction on cross-domain schemas; MAVEN's same-domain schema exhibits centrality confounding that reverses this trend. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).",
          " \\end{abstract}"
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

_source line 90_

<details open><summary>🔧 Tool call — Edit · `toolu_01PZH4BMRaMRDXUEKYAKr3iA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "We sample 1{,}000 test instances and evaluate with token-level text matching.",
  "new_string": "We sample 1{,}000 test instances and evaluate with token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "8c9b485d-969e-44bb-a582-3947236347ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 91 · 2026-05-16T14:38:14.292Z_

<details><summary>↩ Tool result · `toolu_01PZH4BMRaMRDXUEKYAKr3iA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d313b753-4420-414a-8c50-7629778fc8ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "We sample 1{,}000 test instances and evaluate with token-level text matching.",
    "newString": "We sample 1{,}000 test instances and evaluate with token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on Few-NERD ($r = 0.112$, $p < 0.001$) and FewRel ($r = 0.187$, $p < 0.001$). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\label{sec:datasets}",
          " ",
          " \\paragraph{Few-NERD (NER).}",
          "-Few-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching.",
          "+Few-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.",
          " ",
          " \\paragraph{FewRel (RE).}",
          " FewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation."
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

_source line 92_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q8TAQdUJcCWzBka5RnRdmd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches.",
  "new_string": "text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "50f329b4-c6a6-4bec-bff4-08376f2c0400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 93 · 2026-05-16T14:38:17.017Z_

<details><summary>↩ Tool result · `toolu_01Q8TAQdUJcCWzBka5RnRdmd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d9fa610d-d329-4d5d-85ad-ab88d4e40400",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches.",
    "newString": "text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on Few-NERD ($r = 0.112$, $p < 0.001$) and FewRel ($r = 0.187$, $p < 0.001$). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).\n",
    "structuredPatch": [
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 73,
        "newLines": 7,
        "lines": [
          " \\subsection{Evaluation Metrics}",
          " \\label{sec:metrics}",
          " ",
          "-\\textbf{NER}: text-match F1---a prediction is correct if the text string matches (case-insensitive) a gold entity \\emph{and} the type matches. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          "+\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.",
          " ",
          " ",
          " \\subsection{Model and Inference}"
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

_source line 94_

<details open><summary>🔧 Tool call — Edit · `toolu_01BbKBGJAJG6WEZELGcWsCyQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "($B{=}1{,}000$).",
  "new_string": "($B{=}10{,}000$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "882ccea3-7620-45e3-9719-b7b7d2d9fe1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 95 · 2026-05-16T14:38:17.950Z_

<details><summary>↩ Tool result · `toolu_01BbKBGJAJG6WEZELGcWsCyQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "eb522353-a94f-4f02-ac6f-cf2b59252ef7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "($B{=}1{,}000$).",
    "newString": "($B{=}10{,}000$).",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains, making it suitable for cross-domain evaluation. We sample 1{,}000 test instances and evaluate with token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\cite{maven-2020} defines 168 event types derived from the FrameNet ontology, making it a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification.\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range indicates the min--max Batch Confusability Scores across count-curve batches (Experiment~1). Embedding column indicates the model used for SCS/BCS computation. $^\\dagger$Trigger mentions across 8{,}042 sentences in 710 documents.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\nWe introduce the Schema Confusability Score to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe compute SCS with two embedding models: (1)~Qwen3-32B \\cite{qwen3-2025} hidden-state representations (5{,}120-d), which capture the extraction model's own type representations, and (2)~all-MiniLM-L6-v2 \\cite{minilm-2020,sentence-bert-2019}, a 384-dimensional general-purpose sentence encoder. SCS uses name-only embeddings as a practical simplification. We validate this choice empirically: name+definition SCS yields equivalent predictive accuracy ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}), and for MAVEN/FewRel prompts that use type names without definitions, name-only SCS directly matches prompt content. We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity \\cite{sentence-bert-2019}; a cross-embedding sensitivity check using Qwen3-32B causal-LM hidden states confirms directional consistency but with compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with known autoregressive anisotropy \\cite{ethayarajh-contextual-2019}.\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS measures embedding-space similarity rather than task-grounded confusion, making it a pre-hoc proxy computable without running extraction experiments. Empirical validation confirms the proxy is informative: pairwise SCS correlates with observed type confusion on Few-NERD ($r = 0.112$, $p < 0.001$) and FewRel ($r = 0.187$, $p < 0.001$). However, SCS is a partial proxy---context, type frequency, mention ambiguity, and definition quality also contribute to confusion (\\S\\ref{sec:pairwise}). Task-grounded confusion scores derived from empirical error matrices would capture these factors but require running extraction first, forfeiting the predictive utility that makes SCS useful for schema design.\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 5 random type batches and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{1, 2, 6, 12, 22, 44, 64\\} for Few-NERD, \\{1, 4, 8, 16, 32, 64, 80\\} for FewRel, \\{1, 4, 8, 16, 32, 64, 96\\} for DocRED, and \\{1, 6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1---a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy---exact match of predicted relation label to gold. \\textbf{ED}: relaxed F1---any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\nWe use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).\n",
    "structuredPatch": [
      {
        "oldStart": 79,
        "oldLines": 4,
        "newStart": 79,
        "newLines": 4,
        "lines": [
          " \\subsection{Model and Inference}",
          " \\label{sec:model}",
          " ",
          "-We use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}1{,}000$).",
          "+We use Qwen3-32B-FP8 \\cite{qwen3-2025} served via vLLM v0.20.2 \\cite{vllm-2023} on a single 96\\,GB GPU with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints, doubling precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\cite{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}. All metrics include 95\\% bootstrap CIs ($B{=}10{,}000$)."
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

_source line 96_

<details open><summary>🔧 Tool call — Edit · `toolu_011kmg8CLHYyiXayZDUaMrET`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "is an internal project designation",
  "new_string": "is an adopted abbreviation for schema decomposition and grouping"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "27320ee4-db95-4e5a-bdc6-186327eb446b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 97 · 2026-05-16T14:38:20.344Z_

<details><summary>↩ Tool result · `toolu_011kmg8CLHYyiXayZDUaMrET`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d3d11656-f488-40e8-9d63-1b772dc7897c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "oldString": "is an internal project designation",
    "newString": "is an adopted abbreviation for schema decomposition and grouping",
    "originalFile": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mechanism is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nConfidence-based gating (retaining only predictions above threshold) trades recall for precision but does not recover net F1 (0.251$\\to$0.241), confirming that merge artifacts are systemic rather than confined to low-confidence predictions (Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}",
          " \\label{sec:sdgd}",
          " ",
          "-A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.",
          "+A natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an adopted abbreviation for schema decomposition and grouping; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.",
          " ",
          " We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.251, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).",
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

_source line 98_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q1mE6hr5EwG7pcRXbA9bav`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
  "old_string": "FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}",
  "new_string": "FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "afd529f3-f5c9-4d43-be57-8bffb20c81ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 99 · 2026-05-16T14:38:21.949Z_

<details><summary>↩ Tool result · `toolu_01Q1mE6hr5EwG7pcRXbA9bav`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a3ab34e8-f006-43e4-bf8c-90b1f676a20e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
    "oldString": "FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}",
    "newString": "FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}",
    "originalFile": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Did you cite the creators of artifacts you used?}",
          " ",
          "-Yes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.",
          "+Yes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.",
          " ",
          " \\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}",
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

_source line 100_

<details open><summary>🔧 Tool call — Edit · `toolu_01JHz5f5wvTaasVtvgiFbuqB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
  "old_string": "Meta-Llama-3.1-8B-Instruct, vLLM",
  "new_string": "Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0a910cd1-84a7-4198-a7e8-ee65faec1689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 101 · 2026-05-16T14:38:23.353Z_

<details><summary>↩ Tool result · `toolu_01JHz5f5wvTaasVtvgiFbuqB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3d034783-b11f-421f-9323-db2bdb914636",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
    "oldString": "Meta-Llama-3.1-8B-Instruct, vLLM",
    "newString": "Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM",
    "originalFile": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Did you cite the creators of artifacts you used?}",
          " ",
          "-Yes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.",
          "+Yes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.",
          " ",
          " \\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}",
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

_source line 102_

<details open><summary>🔧 Tool call — Edit · `toolu_01GdKANub1J7zghiSFG3Bu17`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
  "old_string": "1{,}000 resamples",
  "new_string": "10{,}000 resamples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ad91d052-2c20-4c04-98d6-3abfbdda90f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 103 · 2026-05-16T14:38:24.937Z_

<details><summary>↩ Tool result · `toolu_01GdKANub1J7zghiSFG3Bu17`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "47f9d5fb-adb6-4316-8e8e-cfe583a66e30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
    "oldString": "1{,}000 resamples",
    "newString": "10{,}000 resamples",
    "originalFile": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, non-significant factorial results, decomposition scope, and metric scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nN/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-channel degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. An AI coding assistant was used for experiment scripting and LaTeX formatting. All scientific claims, experimental design, and analysis were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\cite{fewnerd-2021}, FewRel \\cite{fewrel-2018}, DocRED \\cite{docred-2019}, MAVEN \\cite{maven-2020}, Qwen3-32B \\cite{qwen3-2025}, Meta-Llama-3.1-8B-Instruct \\cite{llama3-2024}, vLLM \\cite{vllm-2023}, and all-MiniLM-L6-v2 \\cite{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Models are used under their respective open-weight licenses.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8) and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on a single RTX PRO 6000 Blackwell GPU (96\\,GB) served via vLLM. Total compute was approximately 48 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 7,
        "newStart": 68,
        "newLines": 7,
        "lines": [
          " ",
          " \\item \\textbf{Did you report descriptive statistics about your results?}",
          " ",
          "-Yes. All key metrics include 95\\% bootstrap confidence intervals (1{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.",
          "+Yes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.",
          " ",
          " \\item \\textbf{Did you report implementation details, e.g., versions of packages?}",
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

_source line 104_

<details open><summary>🔧 Tool call — Edit · `toolu_01XfsLgyhnTitvGESYpc3A4S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\end{enumerate}\n\n\\input{checklist}",
  "new_string": "\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "7b601e52-3271-4eb0-bc8b-6d5acd9b0dca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9i1VTWcxBEXCnCZtRGW5m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 68940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 105 · 2026-05-16T14:38:27.650Z_

<details><summary>↩ Tool result · `toolu_01XfsLgyhnTitvGESYpc3A4S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "8776d4fc-7d42-43d2-be43-5a6ebb2740da",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "\\end{enumerate}\n\n\\input{checklist}",
    "newString": "\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p \\approx 0.60$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 52,
        "oldLines": 6,
        "newStart": 52,
        "newLines": 8,
        "lines": [
          " \\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.",
          " \\end{enumerate}",
          " ",
          "+\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.",
          "+",
          " \\input{checklist}",
          " ",
          " \\bibliography{references}"
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

_source line 106_

<details><summary>Logged reasoning block</summary>

```text
All 20 edits completed successfully. Now I need to also handle the bootstrap B value in results.tex table caption. Let me check: I changed `$B{=}1{,}000$` in experimental_setup.tex, but there's also one in results.tex table caption (line 43). Let me handle that, and also update the todo list.

Also need to handle the results.tex line 29 bootstrap mention without B value.

Let me also verify the changes by reading key files and doing grep checks.

Let me also fix the bootstrap in results.tex pairwise table caption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "643f8ea4-694c-4d7c-9cfc-ccd580362f2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBYmiTDBqXdcBEKJAxbbCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 62827,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 62827
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

_source line 107_

All 20 edits applied. Now handling remaining bootstrap B values in results.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "f1e75bec-3076-444f-8e0d-31e7cd065382",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBYmiTDBqXdcBEKJAxbbCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 62827,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 62827
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

_source line 108_

<details open><summary>🔧 Tool call — Edit · `toolu_0173XnLJU9tZHD1R587JVods`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "pair-level percentile bootstrap ($B{=}1{,}000$)",
  "new_string": "pair-level percentile bootstrap ($B{=}10{,}000$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "fb4c7fea-644d-4013-9e20-4c2c9570fdb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBYmiTDBqXdcBEKJAxbbCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 62827,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 62827
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

_source line 109 · 2026-05-16T14:38:37.734Z_

<details><summary>↩ Tool result · `toolu_0173XnLJU9tZHD1R587JVods`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "1b2d3a08-330f-4604-81b0-4059fb5f14a5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "pair-level percentile bootstrap ($B{=}1{,}000$)",
    "newString": "pair-level percentile bootstrap ($B{=}10{,}000$)",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nUnless otherwise noted, all experiments in this section use the v1 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\begin{figure}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\columnwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves across four datasets. NER recall generally declines and RE accuracy (both FewRel and DocRED) declines monotonically with schema size; MAVEN relaxed F1 increases (\\S\\ref{sec:centrality_confound}). \\textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}\n\\label{fig:main_results}\n\\end{figure}\n\nFigure~\\ref{fig:main_results}a shows extraction quality degrades monotonically with schema size across three datasets: Few-NERD recall drops from 0.72 to 0.42 ($-$42\\%), FewRel accuracy from 85.7\\% to 50.4\\% ($-$35.3\\,pp), and DocRED from 88.0\\% to 38.7\\% ($-$56\\%). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}), indicating schema configuration rather than model-specific factors predicts difficulty.\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate---the fraction of $t_i$ gold instances misclassified as $t_j$---and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Both datasets show significant positive correlations between pairwise SCS and type confusion rates. Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\nThe remaining variance likely reflects entity frequency, prompt position \\cite{lost-in-middle-2024}, mention ambiguity, and definition quality. Although pairwise $r^2$ is modest, the signal compounds at the batch level into quartile gaps of 3.9--5.3\\,pp under typical batching (\\S\\ref{sec:practical_magnitude}).\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\nWe fix type count and vary BCS. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound; the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (CI: [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16), confirming monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema: BCS gap $-$23.3\\,pp at count 16 (slope $= -0.713$, $\\rho = -0.661$, $p < 0.001$) and $-$17.6\\,pp at count 32 (slope $= -0.690$, $\\rho = -0.509$, $p = 0.002$). BCS explains 44--53\\% of cross-batch variance ($R^2 = 0.525$ at count 16), substantially higher than FewRel ($R^2 = 0.218$), possibly reflecting a wider confusability range in the DocRED schema, though document-level context may also provide richer cues for type confusion. Across all RE settings, BCS slopes range from $-$0.40 to $-$0.71, significant in all conditions with sufficient BCS range.\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\nFor representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI: [0.4, 4.0])---roughly 7\\% of the extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The 31.2\\,pp figure reflects maximum BCS contrast, not the typical batch experience. Pair-level $R^2 \\approx 7\\%$ among non-zero confusion pairs (vs.\\ $r^2 = 1.3$--$1.7\\%$ across all pairs; Table~\\ref{tab:pairwise}) aggregates to batch-level $R^2 \\approx 22\\%$ ($\\sim$3$\\times$ amplification, reproduced by Monte Carlo simulation accounting for inter-pair correlation structure; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap. Both models converge to $\\approx$51\\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\\ref{tab:cross_model_bcs}). Channel~1 replicates fully on Llama-3.1-8B (\\S\\ref{sec:count_curves}); Channel~2 replicates on RE but shows floor effects on 8B NER (Limitations, item~1).\n\n\\paragraph{Prompt sensitivity.}\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; $n{=}25$; $r = -0.919$; $p < 0.001$)---modestly attenuated from v1's extreme-batch gap but highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\\ $r = +0.50$ under v1). Prompt design modulates magnitude but does not eliminate the effect (Appendix~\\ref{sec:appendix_prompt_sensitivity}).\n\n\\subsection{Multi-Channel Degradation}\n\\label{sec:multi_channel}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition. IntraSub scales monotonically with BCS in both tasks. RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure}\n\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\\rho = 1.0$ ($p < 0.001$) for NER and $\\rho = 0.954$ ($p < 0.001$) for RE. Under closed-set classification, non-\\texttt{none} errors are necessarily intra-batch; the more informative finding is that IntraSub confusion frequency correlates with pairwise SCS ($\\rho{=}0.954$, $p{<}0.001$). In NER, missed rates are higher (43--65\\%) and non-monotonic, indicating confusable types impair entity detection itself. Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches.\n\nThese results establish two channels: \\textbf{Channel~1} (count predicts recall decline) and \\textbf{Channel~2} (confusability predicts type confusion), cleanly separable in RE but coupled in NER where type ambiguity and boundary ambiguity interact.\n\n\\subsection{Centrality Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation (Qwen3 $\\rho = +0.184$, $p = 0.025$; MiniLM $\\rho = +0.208$, $p = 0.011$). This traces to same-domain embedding collapse \\cite{cai-isotropy-clusters-2021}: MAVEN's FrameNet-derived types cluster tightly, so mean BCS conflates confusability with centrality---high-BCS types are semantically central and easy to extract. Controlling for log frequency and degree centrality, the positive correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}). The pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}); the problem is per-type aggregation, not the underlying relationship. Few-NERD's cross-domain schema does not exhibit this confound ($\\rho = -0.293$, $p = 0.02$). Mean BCS is thus reliable only for cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment.",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 7,
        "newStart": 40,
        "newLines": 7,
        "lines": [
          " MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          "-\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}",
          "+\\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \\ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}10{,}000$). We omit FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) as RE's per-instance format precludes direct cross-task comparison of confusion rates. Type-level cluster bootstrap CIs: Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]---both exclude zero, confirming robustness to within-type correlation.}",
          " \\label{tab:pairwise}",
          " \\end{table}",
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

_source line 110_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_013QBLERP3epHFSYFgpSruhh`</summary>

```json
{
  "todos": [
    {
      "content": "B1: 31.2pp削减 (5处替换)",
      "status": "completed",
      "activeForm": "Replacing 31.2pp references"
    },
    {
      "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
      "status": "completed",
      "activeForm": "Rewriting contribution #1 and replacing terminology"
    },
    {
      "content": "B3: first controlled study 限定",
      "status": "completed",
      "activeForm": "Qualifying 'first' claims"
    },
    {
      "content": "B4: Few-NERD pairwise coverage",
      "status": "completed",
      "activeForm": "Adding pairwise coverage info"
    },
    {
      "content": "B5: Seeds确认 (already present, skipped)",
      "status": "completed",
      "activeForm": "Checking seed documentation"
    },
    {
      "content": "B6: r² defense in Discussion",
      "status": "completed",
      "activeForm": "Adding r² defense sentence"
    },
    {
      "content": "B7: Multiple comparisons in Limitations",
      "status": "completed",
      "activeForm": "Adding multiple comparisons paragraph"
    },
    {
      "content": "B8: Minor fixes (6项)",
      "status": "completed",
      "activeForm": "Applying minor fixes"
    },
    {
      "content": "编译验证 + grep检查",
      "status": "in_progress",
      "activeForm": "Compiling and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "3a70fb5b-b94e-4611-b537-f30c5e2dfdf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBYmiTDBqXdcBEKJAxbbCt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 62827,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 62827
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

_source line 111 · 2026-05-16T14:38:44.073Z_

<details><summary>↩ Tool result · `toolu_013QBLERP3epHFSYFgpSruhh`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0442a357-508b-4936-a1bc-687c7444d4a2",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "B1: 31.2pp削减 (5处替换)",
        "status": "in_progress",
        "activeForm": "Replacing 31.2pp references"
      },
      {
        "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
        "status": "pending",
        "activeForm": "Rewriting contribution #1 and replacing terminology"
      },
      {
        "content": "B3: first controlled study 限定",
        "status": "pending",
        "activeForm": "Qualifying 'first' claims"
      },
      {
        "content": "B4: Few-NERD pairwise coverage",
        "status": "pending",
        "activeForm": "Adding pairwise coverage info"
      },
      {
        "content": "B5: Seeds确认",
        "status": "pending",
        "activeForm": "Checking seed documentation"
      },
      {
        "content": "B6: r² defense in Discussion",
        "status": "pending",
        "activeForm": "Adding r² defense sentence"
      },
      {
        "content": "B7: Multiple comparisons in Limitations",
        "status": "pending",
        "activeForm": "Adding multiple comparisons paragraph"
      },
      {
        "content": "B8: Minor fixes (6项)",
        "status": "pending",
        "activeForm": "Applying minor fixes"
      },
      {
        "content": "编译验证 + grep检查",
        "status": "pending",
        "activeForm": "Compiling and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "B1: 31.2pp削减 (5处替换)",
        "status": "completed",
        "activeForm": "Replacing 31.2pp references"
      },
      {
        "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
        "status": "completed",
        "activeForm": "Rewriting contribution #1 and replacing terminology"
      },
      {
        "content": "B3: first controlled study 限定",
        "status": "completed",
        "activeForm": "Qualifying 'first' claims"
      },
      {
        "content": "B4: Few-NERD pairwise coverage",
        "status": "completed",
        "activeForm": "Adding pairwise coverage info"
      },
      {
        "content": "B5: Seeds确认 (already present, skipped)",
        "status": "completed",
        "activeForm": "Checking seed documentation"
      },
      {
        "content": "B6: r² defense in Discussion",
        "status": "completed",
        "activeForm": "Adding r² defense sentence"
      },
      {
        "content": "B7: Multiple comparisons in Limitations",
        "status": "completed",
        "activeForm": "Adding multiple comparisons paragraph"
      },
      {
        "content": "B8: Minor fixes (6项)",
        "status": "completed",
        "activeForm": "Applying minor fixes"
      },
      {
        "content": "编译验证 + grep检查",
        "status": "in_progress",
        "activeForm": "Compiling and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the grep checks and compile. Let me run the grep checks first and compile in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "5454d482-23b1-4af1-b555-67828f5166d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeDCGEsW6noEYRvRECgYFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 74668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 113_

Now running grep verification and compilation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d396a8dc-e718-4af4-bcb5-e42c7faf3abd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeDCGEsW6noEYRvRECgYFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 74668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 114_

<details open><summary>🔧 Tool call — Grep · `toolu_01SFRZt7u8arNumV9tnUiihm`</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9e725cfa-423d-43af-acc8-1e871c6d357d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeDCGEsW6noEYRvRECgYFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 74668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 115 · 2026-05-16T14:38:49.097Z_

<details><summary>↩ Tool result · `toolu_01SFRZt7u8arNumV9tnUiihm`</summary>

```text
docs/paper/main.tex:93:8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
docs/paper/main.tex:94:16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
docs/paper/main.tex:219:[Omitted long matching line]
docs/paper/main.tex:265:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
docs/paper/main.tex:266:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
docs/paper/main.tex:269:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
docs/paper/abstract.tex:4:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/results.tex:56:[Omitted long matching line]
docs/paper/results.tex:67:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "5dc13cea-c564-42aa-8985-dca78dc83c33",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:93:8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\ndocs/paper/main.tex:94:16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\ndocs/paper/main.tex:219:[Omitted long matching line]\ndocs/paper/main.tex:265:80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\ndocs/paper/main.tex:266:80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\ndocs/paper/main.tex:269:\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\ndocs/paper/abstract.tex:4:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/results.tex:56:[Omitted long matching line]\ndocs/paper/results.tex:67:[Omitted long matching line]",
    "numLines": 10
  }
}
```

</details>

---

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Grep · `toolu_013JTKVynpp24kae485xCUkJ`</summary>

```json
{
  "pattern": "two-channel model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a63b9e0e-eead-48aa-a300-68740161c65e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeDCGEsW6noEYRvRECgYFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 74668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 117 · 2026-05-16T14:38:50.331Z_

<details><summary>↩ Tool result · `toolu_013JTKVynpp24kae485xCUkJ`</summary>

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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c762f568-c21c-4655-8077-64f0dea92430",
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

_source line 118_

<details open><summary>🔧 Tool call — Grep · `toolu_011wm6Eb1kCZmLYnaobHeQdN`</summary>

```json
{
  "pattern": "two-channel decomposition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "87456a4b-efa8-471e-a019-fc6c534e8c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JeDCGEsW6noEYRvRECgYFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 74668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 905
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

_source line 119 · 2026-05-16T14:38:51.028Z_

<details><summary>↩ Tool result · `toolu_011wm6Eb1kCZmLYnaobHeQdN`</summary>

```text
docs/paper/main.tex:339:[Omitted long matching line]
docs/paper/discussion.tex:5:[Omitted long matching line]
docs/paper/discussion.tex:11:Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "b1c2cc96-795d-4590-b1c7-7e7e5606cf35",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/main.tex:339:[Omitted long matching line]\ndocs/paper/discussion.tex:5:[Omitted long matching line]\ndocs/paper/discussion.tex:11:Our findings suggest a pre-hoc workflow for practitioners designing extraction schemas. Before deployment, one can compute all-pairs SCS across the type inventory and flag pairs exceeding a high percentile (e.g., 75th) of the corpus's SCS distribution as high-risk for mutual confusion. Three mitigation strategies follow from the two-channel decomposition:",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 120_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the "31.2" grep results:

**Text references (kept as intended):**
1. abstract.tex:4 — "gap reaches 31.2\,pp" ✓ KEEP
2. introduction.tex:12 — "up to 31.2\,pp" ✓ KEEP
3. results.tex:56 — "$-$31.2\,pp (CI: [17.7, 42.7])" ✓ KEEP (§4.3 main result)


4. results.tex:67 — "The 31.2\,pp figure reflects..." ✓ KEEP

**Table data (numeric values, cannot change):**
5-8. main.tex:93-94, 265-266 — table cells with `$-$31.2` values

**Appendix/caption (extra):**
9-10. main.tex:219, 269 — appendix prompt sensitivity detail and table caption

So I've identified 4 prose references to keep, 4 table data cells that are locked (numeric data shouldn't be modified), and 2 appendix/caption instances I can trim. For the caption at line 269, I can remove the parenthetical "(31.2\,pp)" entirely and just say "The 80-relation extreme-batch gap reflects the wider BCS range." For the appendix section at line 219, I need to check what can be condensed there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "ffe96508-eeea-4a1b-ac20-865143cde681",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFpTbCncu5tgvcPUnjZoBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1154
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

_source line 121_

"two-channel model" is 0 occurrences — good. 31.2 still appears in table data and 2 extra text mentions. Let me clean those up too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "c2bf44bb-4385-449e-9a55-c35308a69b9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFpTbCncu5tgvcPUnjZoBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1154
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

_source line 122_

<details open><summary>🔧 Tool call — Read · `toolu_01APuhsX2aiXsq1Qct7DsXLd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 215,
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "dce09eb3-7993-45dd-ac44-83b954d88ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFpTbCncu5tgvcPUnjZoBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1154
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

_source line 123 · 2026-05-16T14:39:09.562Z_

<details><summary>↩ Tool result · `toolu_01APuhsX2aiXsq1Qct7DsXLd`</summary>

```text
215	
216	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
217	
218	\paragraph{RE (FewRel).}
219	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
220	
221	\paragraph{NER (Few-NERD).}
222	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
223	
224	\paragraph{Interpretation.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "a8043a6d-a701-4eef-ada9-815d5372f503",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}",
      "numLines": 10,
      "startLine": 215,
      "totalLines": 342
    }
  }
}
```

</details>

---

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Edit · `toolu_019fXfZzsE5YEL1hHLKzKV6p`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled})",
  "new_string": "the extreme-batch BCS gap is $-$31.2\\,pp (Table~\\ref{tab:bcs_controlled})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "557b4544-d067-4e6e-8e3d-81532edbeeb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLNVaXkh1XSX2zYLEM54NK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1385,
      "cache_read_input_tokens": 76727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1385
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 125 · 2026-05-16T14:39:13.869Z_

<details><summary>↩ Tool result · `toolu_019fXfZzsE5YEL1hHLKzKV6p`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "e42d0be1-4ed2-48d1-891e-1a115f804328",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled})",
    "newString": "the extreme-batch BCS gap is $-$31.2\\,pp (Table~\\ref{tab:bcs_controlled})",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p \\approx 0.60$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 216,
        "oldLines": 7,
        "newStart": 216,
        "newLines": 7,
        "lines": [
          " We assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).",
          " ",
          " \\paragraph{RE (FewRel).}",
          "-Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (low-BCS 82.3\\% vs.\\ high-BCS 51.0\\%; Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.",
          "+Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.",
          " ",
          " \\paragraph{NER (Few-NERD).}",
          " The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel."
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

_source line 126_

<details open><summary>🔧 Tool call — Edit · `toolu_01FGm3qYXpvof176M8QVv7sf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes",
  "new_string": "The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "017100d2-b1eb-4061-a437-d1a5634cf0e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLNVaXkh1XSX2zYLEM54NK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1385,
      "cache_read_input_tokens": 76727,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1385
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 127 · 2026-05-16T14:39:15.313Z_

<details><summary>↩ Tool result · `toolu_01FGm3qYXpvof176M8QVv7sf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "d6c634f5-f10b-44cd-b2ab-c2dcf0042ab6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "oldString": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes",
    "newString": "The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes",
    "originalFile": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.\n\n\\item \\textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.\n\n\\item \\textbf{Non-significant factorial test.} Within-dataset count $\\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.\n\n\\item \\textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.\n\n\\item \\textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits for 80 types and characterizes classification accuracy rather than end-to-end extraction.\n\n\\item \\textbf{Causal mechanism.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality.\n\n\\item \\textbf{Data contamination.} FewRel (2018) may appear in pretraining corpora. However, train-origin relations show numerically lower accuracy than val-origin ($-8.8$\\,pp, $p=0.06$, n.s.), opposite to the contamination hypothesis. Moreover, the monotonic count-dependent degradation curve (85.7\\%$\\to$50.4\\%) cannot be explained by uniform contamination, which would elevate all conditions equally.\n\\end{enumerate}\n\n\\paragraph{Multiple comparisons.} We do not apply family-wise correction across datasets, treating each as an independent replication. Within-dataset secondary analyses are reported with individual $p$-values; core claims rest on effects reaching $p < 0.001$.\n\n\\input{checklist}\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}\n\\label{tab:error_taxonomy}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions, inflating false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\section{Factorial Analysis}\n\\label{sec:appendix_factorial}\n\nWe conducted a within-dataset $2\\!\\times\\!2$ factorial analysis (count $\\times$ BCS) on Few-NERD to test whether the two degradation channels exhibit a statistical interaction. The interaction term was directionally consistent but not statistically significant ($z = -0.67$, $p = 0.50$), likely underpowered due to BCS range compression in high-count schemas. Cross-pool slope analysis on FewRel (\\S\\ref{sec:bcs_controlled}) shows consistent BCS--accuracy sensitivity across pool sizes (permutation $p \\approx 0.60$), suggesting that the per-unit confusability effect is stable rather than amplifying with schema size. A formal factorial test on FewRel was not conducted because the BCS-controlled design varies confusability within fixed count levels rather than crossing both factors.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (CI: [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, producing the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors---central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap is $-$31.2\\,pp (Table~\\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI: [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\\,=\\,12$, $r = +0.58$ ($p = 0.002$, 95\\% CI: [0.19, 0.81]) vs.\\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \\S\\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary driver. The underlying confusability signal---pairwise SCS--confusion correlation and the directional BCS--accuracy relationship---persists across both prompt versions.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch, capturing the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect---the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied---but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates no systematic benefit from including definitions.}\n\\label{tab:scs-ablation}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, making name-only SCS a direct match to model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nWe verify that the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation.\n\n\\paragraph{Setup.} From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ [95\\% CI: 0.092--0.361], matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-induced degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-channel decomposition offers a more refined explanation: schema size per se is not the sole driver; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications---a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics---and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 266,
        "oldLines": 7,
        "newStart": 266,
        "newLines": 7,
        "lines": [
          " 80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          "-\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
          "+\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}",
          " \\label{tab:bcs_controlled}",
          " \\end{table}",
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

_source line 128_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the final grep check and compilation. The appendix line 219 still has "31.2\,pp" but it's referencing the table value directly. Let me check the new count.

Actually, I just changed the caption but kept the appendix line 219 mention. Let me re-check. The appendix line says "the extreme-batch BCS gap is $-$31.2\,pp (Table~\ref{tab:bcs_controlled})". This is in the appendix and references the table data. I could change it to just reference the table: "the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is..." but the original intent is to state the v1 gap value before comparing with v2. 

This is a valid reference in the appendix analysis, so I'll keep it as is and run the final grep check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "2c74119e-e8f6-4b6c-adb3-0be85e32e231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPxVSqzJLz5t9TpCZziwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 78112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 535
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

_source line 129_

<details open><summary>🔧 Tool call — Grep · `toolu_01GztnL8sFsCgDzNRi3z2y87`</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "1be6f39b-526f-48d8-964e-0c8c1ef00718",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNPxVSqzJLz5t9TpCZziwU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 78112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 535
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

_source line 130 · 2026-05-16T14:39:25.004Z_

<details><summary>↩ Tool result · `toolu_01GztnL8sFsCgDzNRi3z2y87`</summary>

```text
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/results.tex:56:[Omitted long matching line]
docs/paper/results.tex:67:[Omitted long matching line]
docs/paper/abstract.tex:4:[Omitted long matching line]
docs/paper/main.tex:93:8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
docs/paper/main.tex:94:16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
docs/paper/main.tex:219:[Omitted long matching line]
docs/paper/main.tex:265:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
docs/paper/main.tex:266:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "6049665c-1e0b-451e-9247-50944b73f967",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/results.tex:56:[Omitted long matching line]\ndocs/paper/results.tex:67:[Omitted long matching line]\ndocs/paper/abstract.tex:4:[Omitted long matching line]\ndocs/paper/main.tex:93:8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\ndocs/paper/main.tex:94:16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\ndocs/paper/main.tex:219:[Omitted long matching line]\ndocs/paper/main.tex:265:80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\ndocs/paper/main.tex:266:80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 131_

<details><summary>Logged reasoning block</summary>

```text
Current 31.2 occurrences:
1. introduction.tex:12 — KEEP (prose, one of the 4)
2. results.tex:56 — KEEP (prose, §4.3 main result)
3. results.tex:67 — KEEP (prose, "The 31.2\,pp figure reflects...")
4. abstract.tex:4 — KEEP (prose, one of the 4)
5. main.tex:93 — TABLE DATA (numeric cell)
6. main.tex:94 — TABLE DATA (numeric cell)


7. main.tex:219 — APPENDIX (references table value for comparison)
8. main.tex:265 — TABLE DATA (numeric cell)
9. main.tex:266 — TABLE DATA (numeric cell)

So I've got the four prose references I need, plus four table cells and one appendix reference that cites the same value. The appendix line is describing the extreme-batch BCS gap with a table reference, which is supporting documentation rather than a primary statement of the finding.

The grep confirms 31.2 appears exactly four times in the prose sections, with the remaining five occurrences split between table data and the appendix comparison. I'll report these findings and move forward with compilation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "0791bb55-b0ca-4fe1-ac7e-746929bb0dcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGJHUHaZp2mqiUsfLyy2uJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 78647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

_source line 132_

31.2 now has 4 prose references (abstract, introduction, results x2) as intended. The remaining 5 are table data cells (4) and 1 appendix comparison value. Now compiling.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "cc784f46-3794-45f1-af1c-d2b4bb1f995a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGJHUHaZp2mqiUsfLyy2uJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 78647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

_source line 133_

<details open><summary>🔧 Tool call — Bash · `toolu_01U6Yb5UqDA2Xs8vwPpZaDQP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "86eb82f9-51a7-4bdb-b4be-f3ba9cabd690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PGJHUHaZp2mqiUsfLyy2uJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 78647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 699
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

_source line 134 · 2026-05-16T14:39:38.836Z_

<details><summary>↩ Tool result · `toolu_01U6Yb5UqDA2Xs8vwPpZaDQP`</summary>

```text
lvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 416999 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "94093adb-aaf5-471d-9ef7-976da429123e",
  "tool_use_result": {
    "stdout": "lvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (18 pages, 416999 bytes).\nTranscript written on main.log.",
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

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_01UMsox2JHqEyJBtK5ApwyGB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>&1 | tail -5",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "761e0d4c-4d3d-4d85-998f-12abb2f92eb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8XsUjKovfiTUyV7SQo3wz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1015,
      "cache_read_input_tokens": 79346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1015
      },
      "output_tokens": 67,
      "service_tier": "standard",
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

_source line 136 · 2026-05-16T14:39:41.495Z_

<details><summary>↩ Tool result · `toolu_01UMsox2JHqEyJBtK5ApwyGB`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "13879833-c671-4424-9c62-81c4c036c7d6",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib",
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

_source line 137_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1bs5ZRp3Uh8wDzmFswZRp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
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
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "742677e5-3bae-440d-a886-ea2399ad77c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMC2YxoQcuxKp9cpjXozzh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 80361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 186
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

_source line 138 · 2026-05-16T14:39:47.274Z_

<details><summary>↩ Tool result · `toolu_01W1bs5ZRp3Uh8wDzmFswZRp`</summary>

```text
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 416737 bytes).
Transcript written on main.log.
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (18 pages, 416737 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "cbadf8b7-5067-4f86-b70d-452f4be695c7",
  "tool_use_result": {
    "stdout": "pe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (18 pages, 416737 bytes).\nTranscript written on main.log.\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (18 pages, 416737 bytes).\nTranscript written on main.log.",
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

_source line 139_

<details open><summary>🔧 Tool call — Bash · `toolu_01Km1oCpKbNjUpiUBbMytt5a`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && echo \"=== ERRORS ===\" && grep \"^!\" main.log | head -5 && echo \"=== UNDEFINED ===\" && grep -i \"undefined\" main.log | head -5 && echo \"=== PAGE COUNT ===\" && grep \"Output written\" main.log | tail -1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "fba7093a-3604-4b1d-ae9a-259e06a91702",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfofsyqMCb5RgsgLsPJfAF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 80547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 251
      },
      "output_tokens": 66,
      "service_tier": "standard",
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

_source line 140 · 2026-05-16T14:39:51.123Z_

<details><summary>↩ Tool result · `toolu_01Km1oCpKbNjUpiUBbMytt5a`</summary>

```text
=== ERRORS ===
=== UNDEFINED ===
=== PAGE COUNT ===
Output written on main.pdf (18 pages, 416737 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "875ca9ab-6462-475e-a2f5-b3357019cd13",
  "tool_use_result": {
    "stdout": "=== ERRORS ===\n=== UNDEFINED ===\n=== PAGE COUNT ===\nOutput written on main.pdf (18 pages, 416737 bytes).",
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

_source line 141_

<details><summary>Logged reasoning block</summary>

```text
The compilation succeeds with:
- No errors
- No undefined references
- 18 pages total

But the task says "正文页数（必须 ≤8）". 18 pages is the full paper including appendix. Let me check how many pages are body vs appendix by looking at where \appendix starts. Let me check the page count of the body.

Actually, for ACL papers, the limit is usually 8 pages for the main body, plus unlimited appendix. The \appendix command starts at some point. Let me check where it is and how many pages the body takes.

Actually, I saw main.tex line 59 has `\appendix`. 

So the body runs from the start through the checklist and bibliography, which come before the appendix. The checklist and references don't count toward the page limit anyway, so I need to figure out what page the appendix actually starts on to see how many pages the main content occupies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "39c6f20d-4e6e-44b9-9eee-aa3b4d11a5c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfyBnc3vNptYmF3dRBcnL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 80798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
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

_source line 142_

Compilation clean — no errors, no undefined references. Let me check body page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "e135606a-02d8-49ed-928b-2edeb5040f4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfyBnc3vNptYmF3dRBcnL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 80798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
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

_source line 143_

<details open><summary>🔧 Tool call — Bash · `toolu_01FEuaGg8Z24r2u81E7Nx6HE`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\appendix\\|\\\\\\\\bibliography\\|\\\\\\\\section\\*{Limitations}\" main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "06d009fa-1762-43c8-a3c5-de0af78fbc77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfyBnc3vNptYmF3dRBcnL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 80798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
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

_source line 144 · 2026-05-16T14:40:03.192Z_

<details><summary>↩ Tool result · `toolu_01FEuaGg8Z24r2u81E7Nx6HE`</summary>

```text
38:\section*{Limitations}
59:\bibliography{references}
61:\appendix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "86a85894-ac4f-4d27-8e63-912feab39aa2",
  "tool_use_result": {
    "stdout": "38:\\section*{Limitations}\n59:\\bibliography{references}\n61:\\appendix",
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

_source line 145_

<details open><summary>🔧 Tool call — Bash · `toolu_014nFMCRG7Qa7M6EQezG29dh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"\\\\[{[0-9]*}\" main.aux | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "727022f8-7b3e-41f3-9fec-871658a23fc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsuZtDWcH1oQTRxNEDNRso",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 80999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 146 · 2026-05-16T14:40:06.054Z_

<details><summary>↩ Tool result · `toolu_014nFMCRG7Qa7M6EQezG29dh`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "9b9a8672-6aa1-4d59-8037-477a43a86474",
  "tool_use_result": {
    "stdout": "",
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

_source line 147_

<details open><summary>🔧 Tool call — Bash · `toolu_01XGxDnFUhpNWgDop1KEfVYy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:appendix\" main.aux | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "1ad3d4c5-1cd2-44ca-bbd8-2efc3f66ec7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGMTUH33gKtFoEN5pnzgxM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 121,
      "cache_read_input_tokens": 81463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 121
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

_source line 148 · 2026-05-16T14:40:10.012Z_

<details><summary>↩ Tool result · `toolu_01XGxDnFUhpNWgDop1KEfVYy`</summary>

```text
\newlabel{sec:appendix_figures}{{A}{13}{Additional Figures}{appendix.A}{}}
\newlabel{sec:appendix_sdgd}{{B}{13}{SDGD Full Protocol and Results}{appendix.B}{}}
\newlabel{sec:appendix_factorial}{{C}{14}{Factorial Analysis}{appendix.C}{}}
\newlabel{sec:appendix_within_pool}{{D}{14}{Within-Pool CI Details}{appendix.D}{}}
\newlabel{sec:appendix_residualized_bcs}{{E}{14}{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}{appendix.E}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "8c9c2ef6-7efe-48f8-8480-f23b645da3bf",
  "tool_use_result": {
    "stdout": "\\newlabel{sec:appendix_figures}{{A}{13}{Additional Figures}{appendix.A}{}}\n\\newlabel{sec:appendix_sdgd}{{B}{13}{SDGD Full Protocol and Results}{appendix.B}{}}\n\\newlabel{sec:appendix_factorial}{{C}{14}{Factorial Analysis}{appendix.C}{}}\n\\newlabel{sec:appendix_within_pool}{{D}{14}{Within-Pool CI Details}{appendix.D}{}}\n\\newlabel{sec:appendix_residualized_bcs}{{E}{14}{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}{appendix.E}{}}",
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

_source line 149_

<details><summary>Logged reasoning block</summary>

```text
Appendix starts at page 13. So the body (including limitations, checklist, references) is 12 pages. For ACL, the page limit of 8 is for the main content, not including references, checklist, and appendix. Let me check where the main content ends.

Let me check what page the Limitations section starts on, and what page references start on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "dd35ec38-68f0-45e6-9cf6-ce2f5038f7a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx5zVZhj85sa9w8XCG5LyB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 81584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
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

_source line 150_

<details open><summary>🔧 Tool call — Bash · `toolu_01WmaabeoLtViFmfhZdCGPXk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:conclusion\\|newlabel{sec:discussion\\|newlabel{sec:sdgd}\" main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "86a07583-cd56-4169-bf33-49148841a9b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hx5zVZhj85sa9w8XCG5LyB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 81584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
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

_source line 151 · 2026-05-16T14:40:15.700Z_

<details><summary>↩ Tool result · `toolu_01WmaabeoLtViFmfhZdCGPXk`</summary>

```text
\newlabel{sec:sdgd}{{5}{6}{Schema Decomposition: Failure, Diagnosis, and Mitigation}{section.5}{}}
\newlabel{sec:discussion}{{6}{7}{Discussion}{section.6}{}}
\newlabel{sec:conclusion}{{7}{8}{Conclusion}{section.7}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "e70e4680-f81a-43ce-a722-dab91eb13aff",
  "tool_use_result": {
    "stdout": "\\newlabel{sec:sdgd}{{5}{6}{Schema Decomposition: Failure, Diagnosis, and Mitigation}{section.5}{}}\n\\newlabel{sec:discussion}{{6}{7}{Discussion}{section.6}{}}\n\\newlabel{sec:conclusion}{{7}{8}{Conclusion}{section.7}{}}",
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

_source line 152_

Conclusion is on page 8, appendix starts on page 13. Body ≤8 pages confirmed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "f0e89b94-86c4-40ec-9248-c8350016f720",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVXzhK4EGoYQvVWBEGtjw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 81866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

### Tool call

_source line 153_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01QGHdXeN3Zsw5yqNxqHnCzG`</summary>

```json
{
  "todos": [
    {
      "content": "B1: 31.2pp削减 (5处替换)",
      "status": "completed",
      "activeForm": "Replacing 31.2pp references"
    },
    {
      "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
      "status": "completed",
      "activeForm": "Rewriting contribution #1 and replacing terminology"
    },
    {
      "content": "B3: first controlled study 限定",
      "status": "completed",
      "activeForm": "Qualifying 'first' claims"
    },
    {
      "content": "B4: Few-NERD pairwise coverage",
      "status": "completed",
      "activeForm": "Adding pairwise coverage info"
    },
    {
      "content": "B5: Seeds确认 (already present, skipped)",
      "status": "completed",
      "activeForm": "Checking seed documentation"
    },
    {
      "content": "B6: r² defense in Discussion",
      "status": "completed",
      "activeForm": "Adding r² defense sentence"
    },
    {
      "content": "B7: Multiple comparisons in Limitations",
      "status": "completed",
      "activeForm": "Adding multiple comparisons paragraph"
    },
    {
      "content": "B8: Minor fixes (6项)",
      "status": "completed",
      "activeForm": "Applying minor fixes"
    },
    {
      "content": "编译验证 + grep检查",
      "status": "completed",
      "activeForm": "Compiling and verifying"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "11e706c8-ff69-4e1e-b0ed-f6a925b3a08f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVXzhK4EGoYQvVWBEGtjw9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 81866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

### Tool result

_source line 154 · 2026-05-16T14:40:28.131Z_

<details><summary>↩ Tool result · `toolu_01QGHdXeN3Zsw5yqNxqHnCzG`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "6a639f61-e2ad-4da5-8f07-2311ad51eb4b",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "B1: 31.2pp削减 (5处替换)",
        "status": "completed",
        "activeForm": "Replacing 31.2pp references"
      },
      {
        "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
        "status": "completed",
        "activeForm": "Rewriting contribution #1 and replacing terminology"
      },
      {
        "content": "B3: first controlled study 限定",
        "status": "completed",
        "activeForm": "Qualifying 'first' claims"
      },
      {
        "content": "B4: Few-NERD pairwise coverage",
        "status": "completed",
        "activeForm": "Adding pairwise coverage info"
      },
      {
        "content": "B5: Seeds确认 (already present, skipped)",
        "status": "completed",
        "activeForm": "Checking seed documentation"
      },
      {
        "content": "B6: r² defense in Discussion",
        "status": "completed",
        "activeForm": "Adding r² defense sentence"
      },
      {
        "content": "B7: Multiple comparisons in Limitations",
        "status": "completed",
        "activeForm": "Adding multiple comparisons paragraph"
      },
      {
        "content": "B8: Minor fixes (6项)",
        "status": "completed",
        "activeForm": "Applying minor fixes"
      },
      {
        "content": "编译验证 + grep检查",
        "status": "in_progress",
        "activeForm": "Compiling and verifying"
      }
    ],
    "newTodos": [
      {
        "content": "B1: 31.2pp削减 (5处替换)",
        "status": "completed",
        "activeForm": "Replacing 31.2pp references"
      },
      {
        "content": "B2: Contribution #1 重写 + two-channel model→decomposition",
        "status": "completed",
        "activeForm": "Rewriting contribution #1 and replacing terminology"
      },
      {
        "content": "B3: first controlled study 限定",
        "status": "completed",
        "activeForm": "Qualifying 'first' claims"
      },
      {
        "content": "B4: Few-NERD pairwise coverage",
        "status": "completed",
        "activeForm": "Adding pairwise coverage info"
      },
      {
        "content": "B5: Seeds确认 (already present, skipped)",
        "status": "completed",
        "activeForm": "Checking seed documentation"
      },
      {
        "content": "B6: r² defense in Discussion",
        "status": "completed",
        "activeForm": "Adding r² defense sentence"
      },
      {
        "content": "B7: Multiple comparisons in Limitations",
        "status": "completed",
        "activeForm": "Adding multiple comparisons paragraph"
      },
      {
        "content": "B8: Minor fixes (6项)",
        "status": "completed",
        "activeForm": "Applying minor fixes"
      },
      {
        "content": "编译验证 + grep检查",
        "status": "completed",
        "activeForm": "Compiling and verifying"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 155_

全部完成。

## 报告

### 1. 编译状态
编译成功，无错误 (`^!` = 0)，无 undefined 引用。

### 2. 正文页数
**8 页**（Conclusion 在第 8 页，Limitations/Checklist/References 在 9-12 页，Appendix 从第 13 页开始）。

### 3. "31.2" grep 结果
- **正文 4 处**（符合要求）：abstract.tex:4, introduction.tex:12, results.tex:56, results.tex:67
- **表格数据 4 处**（数值不可改）：main.tex:93, 94, 265, 266
- **附录 1 处**：main.tex:219（prompt sensitivity 对比，引用表格数值）

### 4. "two-channel model" grep 结果
**0 次**，全部替换为 "two-channel decomposition"。

### 各任务完成清单

| 任务 | 状态 | 修改文件 |
|------|------|----------|
| B1: 31.2pp 削减 | ✓ 5处替换 + 2处附录/caption | results.tex, discussion.tex, main.tex |
| B2: Contribution #1 + model→decomposition | ✓ | introduction.tex, discussion.tex (2处) |
| B3: "first" 限定 | ✓ abstract + introduction | abstract.tex, introduction.tex |
| B4: Few-NERD pairwise coverage | ✓ | experimental_setup.tex |
| B5: Seeds | ✓ 已有 seed=42，跳过 | — |
| B6: r² defense | ✓ 段末加句 | discussion.tex |
| B7: Multiple comparisons | ✓ Limitations 末尾加段 | main.tex |
| B8.1: Channel labels | ✓ "(hereafter Channel~1 and Channel~2)" | introduction.tex |
| B8.2: training-free 脚注 | ✓ | introduction.tex |
| B8.3: SDGD designation | ✓ "adopted abbreviation" | sdgd_negative.tex |
| B8.4: DocRED/Llama citations | ✓ | checklist.tex |
| B8.5: Bootstrap B=10,000 | ✓ 统一为 B=10,000 | experimental_setup.tex, results.tex, checklist.tex |
| B8.6: NER metric detail | ✓ 加 lowercasing/whitespace/partial | experimental_setup.tex |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "uuid": "90f27778-322d-443f-b314-fed0b65d5a19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MxK1CRdayTFjbniMzZjAp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 82176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 514
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

_source line 156_

全部完成。

## 报告

### 1. 编译状态
编译成功，无错误 (`^!` = 0)，无 undefined 引用。

### 2. 正文页数
**8 页**（Conclusion 在第 8 页，Limitations/Checklist/References 在 9-12 页，Appendix 从第 13 页开始）。

### 3. "31.2" grep 结果
- **正文 4 处**（符合要求）：abstract.tex:4, introduction.tex:12, results.tex:56, results.tex:67
- **表格数据 4 处**（数值不可改）：main.tex:93, 94, 265, 266
- **附录 1 处**：main.tex:219（prompt sensitivity 对比，引用表格数值）

### 4. "two-channel model" grep 结果
**0 次**，全部替换为 "two-channel decomposition"。

### 各任务完成清单

| 任务 | 状态 | 修改文件 |
|------|------|----------|
| B1: 31.2pp 削减 | ✓ 5处替换 + 2处附录/caption | results.tex, discussion.tex, main.tex |
| B2: Contribution #1 + model→decomposition | ✓ | introduction.tex, discussion.tex (2处) |
| B3: "first" 限定 | ✓ abstract + introduction | abstract.tex, introduction.tex |
| B4: Few-NERD pairwise coverage | ✓ | experimental_setup.tex |
| B5: Seeds | ✓ 已有 seed=42，跳过 | — |
| B6: r² defense | ✓ 段末加句 | discussion.tex |
| B7: Multiple comparisons | ✓ Limitations 末尾加段 | main.tex |
| B8.1: Channel labels | ✓ "(hereafter Channel~1 and Channel~2)" | introduction.tex |
| B8.2: training-free 脚注 | ✓ | introduction.tex |
| B8.3: SDGD designation | ✓ "adopted abbreviation" | sdgd_negative.tex |
| B8.4: DocRED/Llama citations | ✓ | checklist.tex |
| B8.5: Bootstrap B=10,000 | ✓ 统一为 B=10,000 | experimental_setup.tex, results.tex, checklist.tex |
| B8.6: NER metric detail | ✓ 加 lowercasing/whitespace/partial | experimental_setup.tex |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 558696,
  "duration_api_ms": 556296,
  "num_turns": 51,
  "stop_reason": "end_turn",
  "session_id": "18c986ba-0778-4578-97e2-0c3365da4e5a",
  "total_cost_usd": 2.1847449500000002,
  "usage": {
    "input_tokens": 153,
    "cache_creation_input_tokens": 128471,
    "cache_read_input_tokens": 1309466,
    "output_tokens": 26052,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 128471,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 703,
        "cache_read_input_tokens": 82176,
        "cache_creation_input_tokens": 514,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 514
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2578,
      "outputTokens": 3246,
      "cacheReadInputTokens": 108902,
      "cacheCreationInputTokens": 36244,
      "webSearchRequests": 0,
      "costUSD": 0.07500319999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 153,
      "outputTokens": 26052,
      "cacheReadInputTokens": 1309466,
      "cacheCreationInputTokens": 128471,
      "webSearchRequests": 0,
      "costUSD": 2.1097417500000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "94bbef70-9e83-4c8e-9e1e-2ddc8e65a88f"
}
```

</details>

---
