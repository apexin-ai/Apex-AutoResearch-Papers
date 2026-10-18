# audit paper section status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_audit_paper_section_status_20260527T042940.log`
- **Structured JSON:** [`8d2ab2be81477f132aaf.json`](../../sessions/8d/8d2ab2be81477f132aaf.json)

## Before a recorded user message

36 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "4bbef715-285b-4d0b-8556-574b1c2dccc4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779865200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9f5ba322-a650-4917-8ddc-73a2227accbc",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

### Assistant

_source line 4_

I'll audit the paper sections. Let me start by examining the directory structure and key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "7852c8c3-e895-48fd-9cb3-bc1054ef9e1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdC7C1ZzbhmPAvPh1kHegH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11791,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11791
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

<details open><summary>🔧 Tool call — Bash · `toolu_015eSVi5JdMB2hXUqMsHYKC1`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ -name \"*.tex\" -o -name \"*.md\" 2>/dev/null | sort",
  "description": "List paper directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "c1a29ae5-c08a-4a66-8062-b17cc9394ccd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdC7C1ZzbhmPAvPh1kHegH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11791,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11791
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

_source line 6 · 2026-05-27T04:29:51.802Z_

<details><summary>↩ Tool result · `toolu_015eSVi5JdMB2hXUqMsHYKC1`</summary>

```text
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "08602ac8-e321-4654-a2c4-8d28ac4c5e6d",
  "tool_use_result": {
    "stdout": "---",
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

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01AZFEAEgCMo9dgPFbqmQ34U`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "4b19296d-7ad2-4884-bfa3-bf8575ab8c2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdC7C1ZzbhmPAvPh1kHegH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11791,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11791
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

_source line 8 · 2026-05-27T04:29:52.109Z_

<details><summary>↩ Tool result · `toolu_01AZFEAEgCMo9dgPFbqmQ34U`</summary>

```text
artifacts/corl_template/corl_2026_template_submission/example.tex
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260516T075046/best/paper.tex
artifacts/dream_reports/dream_20260516T075046/median/paper.tex
artifacts/dream_reports/dream_20260516T075046/worst/paper.tex
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
artifacts/_project/paper/results_draft.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
artifacts/dream_reports/dream_20260520T155932/best/paper.tex
artifacts/dream_reports/dream_20260520T155932/median/paper.tex
artifacts/dream_reports/dream_20260520T155932/worst/paper.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/method.tex
artifacts/dream_reports/dream_20260525T050917/best/paper.tex
artifacts/dream_reports/dream_20260525T050917/median/paper.tex
artifacts/dream_reports/dream_20260525T050917/worst/paper.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
artifacts/_project/paper/tab_model_properties_56d5eb.tex
artifacts/_project/paper/tab_model_properties.tex
artifacts/tab_model_properties.tex
artifacts/_project/paper/tab_main_results_8f3985.tex
artifacts/_project/paper/tab_main_results.tex
artifacts/tab_main_results.tex
docs/paper/experiments.tex
docs/paper/analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "5b82f4da-bc12-4328-a382-ee77b88ffe37",
  "tool_use_result": {
    "filenames": [
      "artifacts/corl_template/corl_2026_template_submission/example.tex",
      "artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.tex",
      "artifacts/dream_reports/dream_20260516T075046/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T075046/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T075046/worst/paper.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/background.tex",
      "docs/paper/sections/experimental_setup.tex",
      "artifacts/_project/paper/results_draft.tex",
      "docs/paper/sections/results_draft.tex",
      "docs/paper/sections/analysis_draft.tex",
      "docs/paper/experiments_deprecated.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/related_work_draft.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/background.tex",
      "artifacts/dream_reports/dream_20260520T155932/best/paper.tex",
      "artifacts/dream_reports/dream_20260520T155932/median/paper.tex",
      "artifacts/dream_reports/dream_20260520T155932/worst/paper.tex",
      "docs/paper/results_v2.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/results.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/abstract.tex",
      "docs/paper/discussion.tex",
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "artifacts/dream_reports/dream_20260525T050917/best/paper.tex",
      "artifacts/dream_reports/dream_20260525T050917/median/paper.tex",
      "artifacts/dream_reports/dream_20260525T050917/worst/paper.tex",
      "docs/paper/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/tab_model_properties_56d5eb.tex",
      "artifacts/_project/paper/tab_model_properties.tex",
      "artifacts/tab_model_properties.tex",
      "artifacts/_project/paper/tab_main_results_8f3985.tex",
      "artifacts/_project/paper/tab_main_results.tex",
      "artifacts/tab_main_results.tex",
      "docs/paper/experiments.tex",
      "docs/paper/analysis.tex"
    ],
    "durationMs": 66,
    "numFiles": 48,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_019V16Xu1Ea5k9FCoGp8ZtU3`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "eed9879b-db90-4025-baba-32c19a97caa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdC7C1ZzbhmPAvPh1kHegH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11791,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11791
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

_source line 10 · 2026-05-27T04:29:52.598Z_

<details><summary>↩ Tool result · `toolu_019V16Xu1Ea5k9FCoGp8ZtU3`</summary>

```text
artifacts/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md
artifacts/architecture_report.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778878965.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/director/loop_3.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2_1778890120.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_3_1778900113.md
.claude/sessions/agent_175a0fc4/CLAUDE.md
.claude/sessions/agent_175a0fc4/AGENTS.md
task_context/history/agent/loop_2_1778903096.md
task_context/history/agent/loop_4.md
.claude/sessions/agent_567a8628/CLAUDE.md
.claude/sessions/agent_567a8628/AGENTS.md
task_context/history/reviewer/loop_3.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_4_1778929745.md
.claude/sessions/agent_117c0105/CLAUDE.md
.claude/sessions/agent_117c0105/AGENTS.md
artifacts/mvp_imm_v8b_twostage/diagnosis.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/review_report.md
artifacts/dream_reports/dream_20260516T075046/best/review_report.md
artifacts/dream_reports/dream_20260516T075046/worst/review_report.md
task_context/history/reviewer/loop_4.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_5.md
artifacts/research_lora_mode_collapse_fix.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_5_1778944487.md
task_context/history/agent/loop_6.md
task_context/history/director/loop_6.md
artifacts/_project/chart/paper_figures_v1.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_7.md
.claude/sessions/agent_a95c4df4/CLAUDE.md
.claude/sessions/agent_a95c4df4/AGENTS.md
artifacts/checkpoint_integrity_report.md
.claude/sessions/agent_0a8b3dc9/CLAUDE.md
.claude/sessions/agent_0a8b3dc9/AGENTS.md
.claude/sessions/agent_2dc1719e/CLAUDE.md
.claude/sessions/agent_2dc1719e/AGENTS.md
.claude/sessions/agent_94e13d08/CLAUDE.md
.claude/sessions/agent_94e13d08/AGENTS.md
artifacts/eval_random_prune_baseline/data/eval_random_prune_baseline.md
task_context/history/director/loop_7.md
task_context/history/reviewer/loop_7.md
artifacts/diagnosis_fullft_batch64_v2_crash.md
.claude/sessions/agent_6035f7a4/CLAUDE.md
.claude/sessions/agent_6035f7a4/AGENTS.md
.claude/sessions/agent_cb22994e/CLAUDE.md
.claude/sessions/agent_cb22994e/AGENTS.md
task_context/history/agent/loop_8.md
.claude/sessions/agent_22ede7c8/CLAUDE.md
.claude/sessions/agent_22ede7c8/AGENTS.md
task_context/history/agent/loop_8_1779019207.md
artifacts/eval_results/sim_rollout_diagnosis.md
artifacts/eval_results/lerobot_eval_investigation.md
artifacts/eval_results/official_eval_final_report.md
task_context/history/agent/loop_8_1779019220.md
.claude/sessions/agent_3da918a8/CLAUDE.md
.claude/sessions/agent_3da918a8/AGENTS.md
task_context/history/agent/loop_8_1779065803.md
.claude/sessions/agent_f8c49312/CLAUDE.md
.claude/sessions/agent_f8c49312/AGENTS.md
docs/paper/notes/vla_iap_analysis.md
docs/paper/notes/narrative_options.md
artifacts/_project/intermediate/smart_compress_framework_summary.md
artifacts/_project/intermediate/smart_compress_framework.md
.claude/sessions/agent_3c70b6f7/CLAUDE.md
.claude/sessions/agent_3c70b6f7/AGENTS.md
task_context/history/agent/loop_9.md
.claude/sessions/agent_a88e8af3/CLAUDE.md
.claude/sessions/agent_a88e8af3/AGENTS.md
task_context/history/reviewer/loop_8.md
task_context/history/agent/loop_9_1779331605.md
.claude/sessions/agent_409ae0a0/CLAUDE.md
.claude/sessions/agent_409ae0a0/AGENTS.md
.claude/sessions/agent_74764901/CLAUDE.md
.claude/sessions/agent_74764901/AGENTS.md
.claude/sessions/agent_0430c1e3/CLAUDE.md
.claude/sessions/agent_0430c1e3/AGENTS.md
.claude/sessions/agent_76bd8ee3/CLAUDE.md
.claude/sessions/agent_76bd8ee3/AGENTS.md
artifacts/train_smart_compress_m128_resume/report/analysis.md
artifacts/review_reports/round_1.md
artifacts/worker_output_baseline_control_crash.md
.claude/sessions/agent_0bb6eb29/CLAUDE.md
.claude/sessions/agent_0bb6eb29/AGENTS.md
.claude/sessions/agent_f517032d/CLAUDE.md
.claude/sessions/agent_f517032d/AGENTS.md
artifacts/review_reports/round_2.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "08c91d4e-abe6-4836-b947-6eb72aa57358",
  "tool_use_result": {
    "filenames": [
      "artifacts/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md",
      "artifacts/architecture_report.md",
      "task_context/history/reviewer/loop_1.md",
      "task_context/history/director/loop_1.md",
      "task_context/history/agent/loop_1.md",
      "task_context/history/agent/loop_1_1778878965.md",
      "task_context/history/director/loop_2.md",
      "task_context/history/agent/loop_2.md",
      "task_context/history/director/loop_3.md",
      "task_context/history/reviewer/loop_2.md",
      "task_context/history/agent/loop_2_1778890120.md",
      "task_context/history/agent/loop_3.md",
      "task_context/history/agent/loop_3_1778900113.md",
      ".claude/sessions/agent_175a0fc4/CLAUDE.md",
      ".claude/sessions/agent_175a0fc4/AGENTS.md",
      "task_context/history/agent/loop_2_1778903096.md",
      "task_context/history/agent/loop_4.md",
      ".claude/sessions/agent_567a8628/CLAUDE.md",
      ".claude/sessions/agent_567a8628/AGENTS.md",
      "task_context/history/reviewer/loop_3.md",
      "task_context/history/director/loop_4.md",
      "task_context/history/agent/loop_4_1778929745.md",
      ".claude/sessions/agent_117c0105/CLAUDE.md",
      ".claude/sessions/agent_117c0105/AGENTS.md",
      "artifacts/mvp_imm_v8b_twostage/diagnosis.md",
      "docs/IDEA_BRIEF.md",
      "artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260516T075046/median/review_report.md",
      "artifacts/dream_reports/dream_20260516T075046/best/review_report.md",
      "artifacts/dream_reports/dream_20260516T075046/worst/review_report.md",
      "task_context/history/reviewer/loop_4.md",
      "task_context/history/director/loop_5.md",
      "task_context/history/agent/loop_5.md",
      "artifacts/research_lora_mode_collapse_fix.md",
      "task_context/history/reviewer/loop_5.md",
      "task_context/history/agent/loop_5_1778944487.md",
      "task_context/history/agent/loop_6.md",
      "task_context/history/director/loop_6.md",
      "artifacts/_project/chart/paper_figures_v1.md",
      "task_context/history/reviewer/loop_6.md",
      "task_context/history/agent/loop_7.md",
      ".claude/sessions/agent_a95c4df4/CLAUDE.md",
      ".claude/sessions/agent_a95c4df4/AGENTS.md",
      "artifacts/checkpoint_integrity_report.md",
      ".claude/sessions/agent_0a8b3dc9/CLAUDE.md",
      ".claude/sessions/agent_0a8b3dc9/AGENTS.md",
      ".claude/sessions/agent_2dc1719e/CLAUDE.md",
      ".claude/sessions/agent_2dc1719e/AGENTS.md",
      ".claude/sessions/agent_94e13d08/CLAUDE.md",
      ".claude/sessions/agent_94e13d08/AGENTS.md",
      "artifacts/eval_random_prune_baseline/data/eval_random_prune_baseline.md",
      "task_context/history/director/loop_7.md",
      "task_context/history/reviewer/loop_7.md",
      "artifacts/diagnosis_fullft_batch64_v2_crash.md",
      ".claude/sessions/agent_6035f7a4/CLAUDE.md",
      ".claude/sessions/agent_6035f7a4/AGENTS.md",
      ".claude/sessions/agent_cb22994e/CLAUDE.md",
      ".claude/sessions/agent_cb22994e/AGENTS.md",
      "task_context/history/agent/loop_8.md",
      ".claude/sessions/agent_22ede7c8/CLAUDE.md",
      ".claude/sessions/agent_22ede7c8/AGENTS.md",
      "task_context/history/agent/loop_8_1779019207.md",
      "artifacts/eval_results/sim_rollout_diagnosis.md",
      "artifacts/eval_results/lerobot_eval_investigation.md",
      "artifacts/eval_results/official_eval_final_report.md",
      "task_context/history/agent/loop_8_1779019220.md",
      ".claude/sessions/agent_3da918a8/CLAUDE.md",
      ".claude/sessions/agent_3da918a8/AGENTS.md",
      "task_context/history/agent/loop_8_1779065803.md",
      ".claude/sessions/agent_f8c49312/CLAUDE.md",
      ".claude/sessions/agent_f8c49312/AGENTS.md",
      "docs/paper/notes/vla_iap_analysis.md",
      "docs/paper/notes/narrative_options.md",
      "artifacts/_project/intermediate/smart_compress_framework_summary.md",
      "artifacts/_project/intermediate/smart_compress_framework.md",
      ".claude/sessions/agent_3c70b6f7/CLAUDE.md",
      ".claude/sessions/agent_3c70b6f7/AGENTS.md",
      "task_context/history/agent/loop_9.md",
      ".claude/sessions/agent_a88e8af3/CLAUDE.md",
      ".claude/sessions/agent_a88e8af3/AGENTS.md",
      "task_context/history/reviewer/loop_8.md",
      "task_context/history/agent/loop_9_1779331605.md",
      ".claude/sessions/agent_409ae0a0/CLAUDE.md",
      ".claude/sessions/agent_409ae0a0/AGENTS.md",
      ".claude/sessions/agent_74764901/CLAUDE.md",
      ".claude/sessions/agent_74764901/AGENTS.md",
      ".claude/sessions/agent_0430c1e3/CLAUDE.md",
      ".claude/sessions/agent_0430c1e3/AGENTS.md",
      ".claude/sessions/agent_76bd8ee3/CLAUDE.md",
      ".claude/sessions/agent_76bd8ee3/AGENTS.md",
      "artifacts/train_smart_compress_m128_resume/report/analysis.md",
      "artifacts/review_reports/round_1.md",
      "artifacts/worker_output_baseline_control_crash.md",
      ".claude/sessions/agent_0bb6eb29/CLAUDE.md",
      ".claude/sessions/agent_0bb6eb29/AGENTS.md",
      ".claude/sessions/agent_f517032d/CLAUDE.md",
      ".claude/sessions/agent_f517032d/AGENTS.md",
      "artifacts/review_reports/round_2.md"
    ],
    "durationMs": 62,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
There are two main locations with paper tex files:
1. `docs/paper/` - seems to be the main paper directory
2. `artifacts/_project/paper/` - seems to be another version

Let me read the key files to audit each section. I'll start by reading the main paper files and the paper_framing.md.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "9194eb86-4d99-495a-86c1-7d2f424e20a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 12_

Two main locations: `docs/paper/` (main) and `artifacts/_project/paper/` (possibly older drafts). Let me read all sections in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "5893ee9f-be5c-48fd-a00b-04d3a91bcc57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01CxfzjdpbrQ6Ju3uqYbF5hJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "89402e98-40d9-4e5e-bda6-a98ee9da69e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 14 · 2026-05-27T04:29:59.405Z_

<details><summary>↩ Tool result · `toolu_01CxfzjdpbrQ6Ju3uqYbF5hJ`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{method}
27	
28	\input{experiments}
29	
30	\input{analysis}
31	
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "0fb40a67-de92-45aa-a6af-12b7694ca762",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{analysis}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01XYH4mAj5sUpR5cEeRpGEye`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "c0cba7a1-a59b-4dff-bcac-9199976475b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 16 · 2026-05-27T04:30:00.011Z_

<details><summary>↩ Tool result · `toolu_01XYH4mAj5sUpR5cEeRpGEye`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. At moderate compression, L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. Attention-based scoring exhibits within-model reversals across task suites. No scoring method is universally safe: task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to $20{\times}$. A zero-mask ablation isolates the mechanism: on $\pi_{0.5}$, zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion strategies fail, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "dbdd131b-9882-43ac-8138-ff5de17d57c1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\\pi_{0.5}$ preserves 98\\% task success while SmolVLA collapses to 0\\%---why?\n\nWe identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\\,{=}\\,$0.038 (near-immune linear projection) to CV$\\,{=}\\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\\,M--7\\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.\n\nImportance-based selection is not universally beneficial---it can be actively harmful. At moderate compression, L2 norm selection preserves 98\\% success on $\\pi_{0.5}$ where random yields 5\\% (93\\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\\,pp. Attention-based scoring exhibits within-model reversals across task suites. No scoring method is universally safe: task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to $20{\\times}$. A zero-mask ablation isolates the mechanism: on $\\pi_{0.5}$, zeroing 10\\% of tokens preserves 98.0\\% SR while physical removal collapses to 9.0\\%---the 89\\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion strategies fail, a lightweight re-encoding module (${\\sim}$5\\% extra parameters) recovers $>$60\\% success at 75\\% compression.\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_0168eXPYyQMcVgs4XyvAcx3i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "0f2ba056-dcdc-4436-8afd-4e0aa4668564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 18 · 2026-05-27T04:30:00.401Z_

<details><summary>↩ Tool result · `toolu_0168eXPYyQMcVgs4XyvAcx3i`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy: uniform pruning, importance-based scoring, or learned re-encoding.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%) across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and a growing body of work extends it to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture.
15	
16	These methods implicitly assume that pruning transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each imposes distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure. No prior work evaluates pruning robustness across both connector architectures and task complexity.
17	
18	We present an empirical study of VLA token compressibility, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\ref{fig:teaser}). Token-independent connectors (linear projections, MLP projectors) degrade gracefully, while token-entangling connectors produce qualitatively different failures: SmolVLA's pixel-shuffle collapses to near-zero (${\leq}$6.6\%) at every retention ratio, while X-VLA's BART encoder exhibits sharp threshold drops. The coefficient of variation (CV) of post-connector token L2 norms captures this on a continuous spectrum (0.038 to 0.314 across all three connector families) and correlates with both pruning tolerance and method sensitivity: $\pi_{0.5}$ exhibits a $17{\times}$ greater method gap than X-VLA at $k{=}0.95$. Under sufficient compression, scoring effectiveness becomes connector-dependent: L2 norm aids $\pi_{0.5}$ across the cliff zone ($+$44.6\,pp on Long at $k{=}0.925$; $+$35.2\,pp on Goal at $k{=}0.85$, decaying to $+$5.6\,pp at $k{=}0.95$) but reverses at aggressive ratios ($-$36\,pp at $k{=}0.5$); on X-VLA it is anti-informative across all ratios ($-$8 to $-$27\,pp), while attention recovers near-baseline performance ($+$31\,pp on Long). Task complexity amplifies these connector-dependent patterns: under random pruning at $k{=}0.9$, X-VLA loses just 1.4 percentage points on single-step Object but 27.8 percentage points on multi-step Goal, a $20{\times}$ amplification.
19	
20	For pixel-shuffle connectors where all pruning strategies yield near-zero SR, we introduce Vision Token Re-encoder (VTR), a lightweight cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) that recovers over 60\% success rate at 75\% compression through learned re-encoding.
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item A compressibility analysis across five VLA architectures (450M to 7B) on four LIBERO~\cite{liu2023libero} task suites, identifying connector architecture as the primary determinant of pruning robustness, with task complexity and scoring method as modulating factors.
25	    \item CV of token L2 norms as a single-pass diagnostic that provides a coarse indicator of connector compressibility type (uniform, graded, or catastrophic) without downstream evaluation. Validated on four closed-loop architectures; we expect the trend to generalize but acknowledge the limited sample.
26	    \item A zero-mask ablation isolating the failure mechanism: on $\pi_{0.5}$, zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\% (89\,pp gap), proving position disruption---not information loss---drives the failure. Vision Token Re-encoder (VTR) further confirms this by recovering a pixel-shuffle VLA from 0.0\% to over 60\% at 75\% compression through learned re-encoding.
27	\end{itemize}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "58402f24-000d-452a-9b42-0a2a3f648785",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_hero_overview.pdf}\n\\caption{Overview of VLA token compressibility.\n\\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.\n\\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.\n\\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy: uniform pruning, importance-based scoring, or learned re-encoding.}\n\\label{fig:teaser}\n\\end{figure*}\n\nRemove 5\\% of vision tokens from SmolVLA and its success rate collapses from 59.2\\% to near-zero (${\\leq}$6.6\\%) across all task suites and pruning methods. Apply the same 5\\% reduction to $\\pi_{0.5}$ and it retains 98.2\\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\\ 4B parameters) but the connector architecture. Token pruning is well-established for ViTs~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and a growing body of work extends it to VLAs~\\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture.\n\nThese methods implicitly assume that pruning transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\\cite{black2024pi0}, MLP projectors~\\cite{kim2024openvla}, pixel-shuffle folding~\\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\\cite{zheng2025xvla}. Each imposes distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure. No prior work evaluates pruning robustness across both connector architectures and task complexity.\n\nWe present an empirical study of VLA token compressibility, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\\ref{fig:teaser}). Token-independent connectors (linear projections, MLP projectors) degrade gracefully, while token-entangling connectors produce qualitatively different failures: SmolVLA's pixel-shuffle collapses to near-zero (${\\leq}$6.6\\%) at every retention ratio, while X-VLA's BART encoder exhibits sharp threshold drops. The coefficient of variation (CV) of post-connector token L2 norms captures this on a continuous spectrum (0.038 to 0.314 across all three connector families) and correlates with both pruning tolerance and method sensitivity: $\\pi_{0.5}$ exhibits a $17{\\times}$ greater method gap than X-VLA at $k{=}0.95$. Under sufficient compression, scoring effectiveness becomes connector-dependent: L2 norm aids $\\pi_{0.5}$ across the cliff zone ($+$44.6\\,pp on Long at $k{=}0.925$; $+$35.2\\,pp on Goal at $k{=}0.85$, decaying to $+$5.6\\,pp at $k{=}0.95$) but reverses at aggressive ratios ($-$36\\,pp at $k{=}0.5$); on X-VLA it is anti-informative across all ratios ($-$8 to $-$27\\,pp), while attention recovers near-baseline performance ($+$31\\,pp on Long). Task complexity amplifies these connector-dependent patterns: under random pruning at $k{=}0.9$, X-VLA loses just 1.4 percentage points on single-step Object but 27.8 percentage points on multi-step Goal, a $20{\\times}$ amplification.\n\nFor pixel-shuffle connectors where all pruning strategies yield near-zero SR, we introduce Vision Token Re-encoder (VTR), a lightweight cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) that recovers over 60\\% success rate at 75\\% compression through learned re-encoding.\n\nOur contributions are:\n\\begin{itemize}\n    \\item A compressibility analysis across five VLA architectures (450M to 7B) on four LIBERO~\\cite{liu2023libero} task suites, identifying connector architecture as the primary determinant of pruning robustness, with task complexity and scoring method as modulating factors.\n    \\item CV of token L2 norms as a single-pass diagnostic that provides a coarse indicator of connector compressibility type (uniform, graded, or catastrophic) without downstream evaluation. Validated on four closed-loop architectures; we expect the trend to generalize but acknowledge the limited sample.\n    \\item A zero-mask ablation isolating the failure mechanism: on $\\pi_{0.5}$, zeroing 10\\% of tokens preserves 98.0\\% SR while physical removal collapses to 9.0\\% (89\\,pp gap), proving position disruption---not information loss---drives the failure. Vision Token Re-encoder (VTR) further confirms this by recovering a pixel-shuffle VLA from 0.0\\% to over 60\\% at 75\\% compression through learned re-encoding.\n\\end{itemize}\n",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_011CKVV4iK1BzJ8FocGp4HUt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "88b430a3-ed9b-407c-ad9e-0920356f2e6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 20 · 2026-05-27T04:30:00.958Z_

<details><summary>↩ Tool result · `toolu_011CKVV4iK1BzJ8FocGp4HUt`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss. Their success rests on classification's insensitivity to spatial layout; robotic manipulation inverts this assumption, as grasping depends on spatial arrangement. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using language-backbone attention signals. ``Don't Run with Scissors''~\cite{jabbour2025dontrun} analyzes VLM token pruning for visual question answering; our work targets closed-loop robotic manipulation, where pruning failures directly impact physical task execution rather than text generation quality. VLA-specific methods have emerged in parallel: VLA-IAP~\cite{cheng2026vlaiap} aligns pruning with action-prediction importance, VLA-Cache~\cite{xu2025vlacache} compresses at the KV-cache level, EfficientVLA~\cite{yang2025efficientvla} combines pruning with merging, and VLA-Pruner~\cite{liu2025vlapruner} learns a pruning policy jointly with the action head. LightVLA~\cite{jiang2026lightvla} introduces differentiable pruning and Compressor-VLA~\cite{gao2025compressorvla} applies instruction-guided compression, both targeting individual architectures; our work instead asks how architectural choices determine which compression approaches succeed or fail, finding that scoring validity is architecture-dependent; L2 norm selection is anti-informative on entangling connectors while attention scoring recovers near-baseline performance.
9	
10	\paragraph{Vision connectors.}
11	The connector between ViT and language backbone governs how spatial information distributes across tokens. LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries (structurally similar to our VTR re-encoder); pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels, adopted by SmolVLA~\cite{shukor2025smolvla}. These create qualitatively different token dependencies; independent connectors leave patch information separable, while entangling connectors distribute content across tokens. The pruning consequences have not been characterized.
12	
13	We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility, introducing CV of token norms as a single-pass diagnostic that correlates with compressibility without closed-loop evaluation.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "d25de98c-4174-40a5-a408-1dcd06e70a6f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{ViT token pruning.}\nDynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, and Token Merging~\\cite{bolya2023tome} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss. Their success rests on classification's insensitivity to spatial layout; robotic manipulation inverts this assumption, as grasping depends on spatial arrangement. None has been evaluated in closed-loop VLA control.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nFastV~\\cite{chen2024fastv} and PruMerge~\\cite{shang2024prumerge} reduce vision tokens in VLMs using language-backbone attention signals. ``Don't Run with Scissors''~\\cite{jabbour2025dontrun} analyzes VLM token pruning for visual question answering; our work targets closed-loop robotic manipulation, where pruning failures directly impact physical task execution rather than text generation quality. VLA-specific methods have emerged in parallel: VLA-IAP~\\cite{cheng2026vlaiap} aligns pruning with action-prediction importance, VLA-Cache~\\cite{xu2025vlacache} compresses at the KV-cache level, EfficientVLA~\\cite{yang2025efficientvla} combines pruning with merging, and VLA-Pruner~\\cite{liu2025vlapruner} learns a pruning policy jointly with the action head. LightVLA~\\cite{jiang2026lightvla} introduces differentiable pruning and Compressor-VLA~\\cite{gao2025compressorvla} applies instruction-guided compression, both targeting individual architectures; our work instead asks how architectural choices determine which compression approaches succeed or fail, finding that scoring validity is architecture-dependent; L2 norm selection is anti-informative on entangling connectors while attention scoring recovers near-baseline performance.\n\n\\paragraph{Vision connectors.}\nThe connector between ViT and language backbone governs how spatial information distributes across tokens. LLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries (structurally similar to our VTR re-encoder); pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels, adopted by SmolVLA~\\cite{shukor2025smolvla}. These create qualitatively different token dependencies; independent connectors leave patch information separable, while entangling connectors distribute content across tokens. The pruning consequences have not been characterized.\n\nWe provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility, introducing CV of token norms as a single-pass diagnostic that correlates with compressibility without closed-loop evaluation.\n",
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Ldxa4MwDeoUriVze1k2oZT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "9e2fa5cb-b972-40cb-aa00-b009ba227051",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 22 · 2026-05-27T04:30:01.421Z_

<details><summary>↩ Tool result · `toolu_01Ldxa4MwDeoUriVze1k2oZT`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft}, an OpenVLA fine-tuning variant evaluated offline, shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches into each output token's channel dimension (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT are analyzed via offline metrics only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v2.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear projection; OpenVLA: 3-layer MLP) process each patch individually, yielding low CV. Token-entangling connectors (X-VLA: 12-layer BART encoder; SmolVLA: pixel-shuffle $4{\times}4$) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}
21	\label{fig:architecture}
22	\end{figure*}
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}
28	\label{tab:model_properties}
29	\begin{tabular}{lrlcrll}
30	\toprule
31	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
32	\midrule
33	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 & Indep.\ & Closed-loop \\
34	X-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\
35	OpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\ & Closed-loop \\
36	SmolVLA & 450M & Pixel-shuffle $4{\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\
37	\midrule
38	$\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\ & Offline \\
39	OFT$^\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\ & Offline \\
40	\bottomrule
41	\multicolumn{7}{l}{\footnotesize $^\dagger$ OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
42	\end{tabular}
43	\end{table}
44	
45	\subsection{Pruning Protocol}
46	\label{sec:pruning_protocol}
47	
48	We apply post-connector token pruning at retention ratio $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\lfloor k \cdot N \rfloor$ tokens that are passed to the LLM backbone.
49	
50	Two strategies bracket expected performance:
51	
52	\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.
53	
54	\textbf{Random subsampling} selects $\lfloor k \cdot N \rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.
55	
56	Both strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.
57	
58	We prune post-connector because this point isolates the connector's effect on token information structure. Pre-connector pruning would test ViT redundancy; KV-cache pruning~\cite{xu2025vlacache} would test LLM attention patterns.
59	
60	\subsection{Compressibility Diagnostic: Importance CV}
61	\label{sec:cv_diagnostic}
62	
63	We quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:
64	\begin{equation}
65	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
66	\label{eq:cv}
67	\end{equation}
68	where $t_i$ denotes the $i$-th post-connector vision token, and $\sigma$, $\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.
69	
70	CV is a single-pass diagnostic requiring one forward pass through the vision encoder and connector, with no downstream evaluation. The metric captures a continuous spectrum: $\pi_{0}$ (CV$\,{=}\,$0.038) produces near-uniform norms, SmolVLA (CV$\,{=}\,$0.314) exhibits high heterogeneity from pixel-shuffle, and the remaining models span the interval (Table~\ref{tab:model_properties}). CV correlates with both pruning tolerance and sensitivity to method choice: low-CV models have near-uniform tokens where \emph{which} tokens are removed matters more than \emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy. We report success rate (SR) as the primary closed-loop metric throughout.
71	
72	\subsection{Vision Token Re-encoder (VTR)}
73	\label{sec:vtr}
74	
75	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this through learned re-encoding: a cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens, aggregating information from the entire spatial field into $M$ compressed representations. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N{=}128$ serves as a passthrough control. A parameter-matched MLP adapter (average pooling + two-layer MLP, no cross-attention) isolates whether gains stem from cross-attention or from re-encoding itself.
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "7df03eac-dddf-4ad5-a725-a8f8285c31d0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \\emph{coupling}.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft}, an OpenVLA fine-tuning variant evaluated offline, shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches into each output token's channel dimension (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT are analyzed via offline metrics only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v2.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear projection; OpenVLA: 3-layer MLP) process each patch individually, yielding low CV. Token-entangling connectors (X-VLA: 12-layer BART encoder; SmolVLA: pixel-shuffle $4{\\times}4$) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated in this study. Coupling indicates whether the connector processes patches independently or creates cross-token dependencies. $N$ = number of vision tokens input to the LLM backbone. Models are grouped by evaluation protocol and ordered by CV within each group.}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 880M & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$ OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, where $k$ denotes the fraction of $N$ vision tokens retained. Given $N$ post-connector tokens, pruning produces $\\lfloor k \\cdot N \\rfloor$ tokens that are passed to the LLM backbone.\n\nTwo strategies bracket expected performance:\n\n\\textbf{L2 norm selection} ranks tokens by their L2 norm and retains the top-$k$ fraction. This importance-based strategy provides a favorable test: if a genuine importance hierarchy exists among tokens, L2 selection should outperform random baselines.\n\n\\textbf{Random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. Because it ignores token content entirely, random selection provides a conservative lower bound.\n\nBoth strategies physically remove unselected tokens and re-index position IDs to close gaps in the sequence. Pruned tokens are discarded, not replaced with zero vectors or mask tokens.\n\nWe prune post-connector because this point isolates the connector's effect on token information structure. Pre-connector pruning would test ViT redundancy; KV-cache pruning~\\cite{xu2025vlacache} would test LLM attention patterns.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify the heterogeneity of post-connector token representations using the coefficient of variation (CV) of their L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $t_i$ denotes the $i$-th post-connector vision token, and $\\sigma$, $\\mu$ are the standard deviation and mean computed over all $N$ token norms from a single observation.\n\nCV is a single-pass diagnostic requiring one forward pass through the vision encoder and connector, with no downstream evaluation. The metric captures a continuous spectrum: $\\pi_{0}$ (CV$\\,{=}\\,$0.038) produces near-uniform norms, SmolVLA (CV$\\,{=}\\,$0.314) exhibits high heterogeneity from pixel-shuffle, and the remaining models span the interval (Table~\\ref{tab:model_properties}). CV correlates with both pruning tolerance and sensitivity to method choice: low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy. We report success rate (SR) as the primary closed-loop metric throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information that cannot be recovered from the remaining tokens. Vision Token Re-encoder (VTR) addresses this through learned re-encoding: a cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens, aggregating information from the entire spatial field into $M$ compressed representations. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N{=}128$ serves as a passthrough control. A parameter-matched MLP adapter (average pooling + two-layer MLP, no cross-attention) isolates whether gains stem from cross-attention or from re-encoding itself.\n",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01PvKxNNo2ztPaK1iwA5Uodi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "0b813d42-1b0e-4624-b0b1-aa9ae23774ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 24 · 2026-05-27T04:30:01.890Z_

<details><summary>↩ Tool result · `toolu_01PvKxNNo2ztPaK1iwA5Uodi`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_{0.5}$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_{0}$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\,{=}\,$0.219). All six architectures contribute to the CV diagnostic (Section~\ref{sec:cv_sensitivity}). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	We follow the pruning protocol of Section~\ref{sec:pruning_protocol} at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	The pruning response depends on token independence imposed by the connector and task complexity (Figure~\ref{fig:teaser}). Token-independent connectors degrade gracefully; token-entangling connectors exhibit sharp, task-dependent collapse.
17	
18	\begin{figure}[t]
19	\centering
20	\includegraphics[width=\linewidth]{figures/paper/fig_pruning_overview.pdf}
21	\caption{Pruning degradation on LIBERO-Object (best scoring method per model; all curves use L2 norm, which is optimal or near-optimal for each architecture at $k{\geq}0.85$). Four VLAs span a complete degradation spectrum: $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
22	\label{fig:pruning_overview}
23	\end{figure}
24	
25	Table~\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\ref{fig:pruning_overview}).
26	
27	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} On Object, L2 selection yields a plateau (${\geq}$98.0\%) through $k{=}0.85$, then drops to 55.0\% at $k{=}0.7$. Random selection shows a different trajectory (74.0\% at $k{=}0.95$, non-monotonic thereafter). The method gap reaches 89.2\,pp at $k{=}0.9$ (Table~\ref{tab:main_results}). Low-CV models are not pruning-immune but uniformly critical: the choice of \emph{which} tokens to remove matters more than how many.
28	
29	\textbf{X-VLA (linear + BART encoder, CV$\,{=}\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 preserves 99.0\% at $k{=}0.95$ and 97.6\% at $k{=}0.9$, then falls sharply with non-monotonic recovery (Table~\ref{tab:main_results}). The same model at $k{=}0.9$ achieves only 70.2\% on Goal, a 27.4\,pp cross-task gap driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR to 47.0\% (L2) and 48.2\% (random); the 1.2\,pp method gap amid 47.0\,pp degradation confirms the BART encoder distributes information uniformly across tokens even as it amplifies compositional task demands.
30	
31	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA reveals that even within a single token-independent architecture, the optimal scoring method is suite-dependent (Table~\ref{tab:main_results}). At $k{=}0.9$ on Object, L2 outperforms random by $+$7.8\,pp (70.6\% vs.\ 62.8\%), consistent with the MLP projector's genuine importance gradient; attention-based scoring is worst at 61.4\% ($-$12.6\,pp from baseline), suggesting that attention weights misidentify salient tokens for object manipulation. On Spatial, the ranking inverts: attention is best at 80.4\% ($+$0.4\,pp, lossless), random near-baseline at 79.8\%, while L2 \emph{underperforms} at 75.0\% ($-$5.0\,pp). On Goal, attention achieves 73.2\% ($-$1.6\,pp, near-lossless), L2 matches baseline (74.8\%), and random anomalously exceeds it (79.6\%). On Long, all three methods converge (L2: 43.6\%, random: 46.8\%, attention: 44.0\%), with method gaps ${\leq}$3.2\,pp amid 6--9\,pp baseline degradation. This within-model crossover---attention worst on Object ($-$12.6\,pp) yet best on Spatial ($+$0.4\,pp), L2 best on Object yet worst on Spatial---demonstrates that no scoring method is universally safe, even within a single connector type.
32	
33	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} SmolVLA collapses to near-zero SR (${\leq}$6.6\%) across all four suites, both pruning methods, and all retention ratios including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\ref{sec:pixel_shuffle}.
34	
35	\textbf{Task complexity amplification.} Multi-step tasks amplify degradation in a connector-dependent manner. Under random pruning at $k{=}0.9$, X-VLA loses 1.4\,pp on Object but 27.8\,pp on Goal ($20{\times}$ amplification). Token-entangling connectors show sharper amplification because compositional tasks require information integration across the cross-token dependencies that pruning disrupts (Appendix~\ref{app:cross_suite_extended}).
36	
37	\begin{table*}[t]
38	\centering
39	\small
40	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \textbf{bold}. SmolVLA collapses to ${\leq}$6.6\% across all conditions. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42); cross-seed variance reported in Appendix Tables~\ref{tab:pi05_l2_multiseed} and~\ref{tab:openvla_multiseed} where available. \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
41	\label{tab:main_results}
42	\begin{tabular}{llccccc}
43	\toprule
44	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
45	\midrule
46	\multirow{4}{*}{$\pi_{0.5}$}
47	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
48	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
49	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
50	& Long    & \textbf{91.6} & 86.8 / 61.2 & 81.0 / 31.8 & 63.2 / 64.6 & 50.2 / 50.2 \\
51	\midrule
52	\multirow{4}{*}{X-VLA}
53	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
54	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
55	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
56	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
57	\midrule
58	\multirow{4}{*}{OpenVLA}
59	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
60	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
61	& Spatial & \textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
62	& Long    & \textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
63	\midrule
64	\multirow{4}{*}{SmolVLA}
65	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
66	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
67	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
68	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
69	\bottomrule
70	\end{tabular}
71	\end{table*}
72	
73	\subsection{Pixel-Shuffle Entanglement}
74	\label{sec:pixel_shuffle}
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=0.85\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
79	\caption{Pixel-shuffle $4{\times}4$ folding: each block of 16 SigLIP patches is channel-concatenated into one token. Removing any token eliminates a non-overlapping $4{\times}4$ receptive field (gray) with no redundancy from neighboring tokens.}
80	\label{fig:pixel_shuffle}
81	\end{figure}
82	
83	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields with no inter-token redundancy. SmolVLA collapses to ${\leq}$6.6\% SR at $k{=}0.95$ across all suites and methods, verified on two checkpoints (44.8\% and 59.2\% baselines); the cliff is architectural. No scoring function can identify dispensable tokens because all carry spatially entangled information; the failure is that any removal breaks completeness. Token-independent connectors retain per-patch locality, so partial removal preserves spatial coverage.
84	
85	\subsection{Position Disruption vs.\ Information Loss}
86	\label{sec:zeromask}
87	
88	The preceding results show that $\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We isolate whether this failure stems from information loss (missing pixel content) or position disruption (shifted token indices in the LLM's sequence).
89	
90	\textbf{Zero-mask ablation.} We compare two conditions at $k{=}0.9$ with random token selection on $\pi_{0.5}$ Object: (1)~\emph{hard pruning}, which physically removes selected tokens and compacts the remaining sequence; (2)~\emph{zero-masking}, which replaces selected token embeddings with zero vectors while preserving all token positions. Both conditions destroy identical visual information---the same 10\% of vision tokens carry no signal---but only hard pruning alters the positional structure of the remaining sequence.
91	
92	Zero-masking preserves 98.0\% SR ($-$0.2\,pp from the 98.2\% baseline), while hard pruning collapses to 9.0\% ($-$89.2\,pp). The 89\,pp gap is entirely attributable to position disruption: $\pi_{0.5}$'s linear connector with learned positional encodings creates a rigid position-to-semantics mapping that tolerates complete signal destruction but not index shifts.
93	
94	This result provides causal evidence for the connector dependence observed in Section~\ref{sec:two_axis}: token-independent connectors do not make tokens dispensable---they make token \emph{positions} critical. The practical implication is that pruning methods for low-CV architectures must either preserve positional structure (e.g., zero-masking, learned compression) or re-encode positions after deletion.
95	
96	\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}
97	\label{sec:cv_sensitivity}
98	
99	Token importance CV (Table~\ref{tab:model_properties}) correlates with the retention ratio at which pruning method choice becomes critical. At $k{=}0.95$, we compare the three closed-loop models with nonzero SR.
100	
101	For $\pi_{0.5}$ (CV$\,{=}\,$0.055), the method gap at $k{=}0.95$ is substantial on Object (Table~\ref{tab:main_results}): L2 retains the full baseline (98.2\%) while random selection degrades markedly. Near-uniform norms cause L2 ranking to exploit spatial correlations rather than genuine importance, while random selection preserves the uniform coverage these models depend on.
102	
103	For X-VLA (CV$\,{=}\,$0.151), the gap averages 0.8\,pp across all four suites (range 0.2--1.4\,pp).
104	
105	For OpenVLA (CV$\,{=}\,$0.215), the method gap at $k{=}0.9$ is suite-dependent: L2 outperforms random by $+$7.8\,pp on Object (70.6\% vs.\ 62.8\%) but underperforms by $-$4.8\,pp on Spatial (75.0\% vs.\ 79.8\%), while both methods match baseline on Goal (${\leq}$4.8\,pp gap). This within-model crossover demonstrates that scoring validity depends on task semantics even for a single connector type.
106	
107	X-VLA shows method gaps ${\leq}$1.4\,pp at $k{=}0.95$ across all four suites (Figure~\ref{fig:method_gap}). OpenVLA's suite-dependent method gap, ranging from $+$7.8\,pp (L2 favored) to $-$4.8\,pp (random favored), illustrates that higher CV enables but does not guarantee L2 advantage.
108	
109	\begin{figure}[t]
110	\centering
111	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
112	\caption{Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$. $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$, reflecting CV-correlated divergence in pruning method sensitivity.}
113	\label{fig:method_gap}
114	\end{figure}
115	
116	At $k{=}0.5$, method-independence breaks down: $\Delta$(R$-$L2) on Object is $+$36.0\,pp ($\pi_{0.5}$), $+$27.2\,pp (X-VLA), $-$3.4\,pp (OpenVLA). Random preserves spatial diversity; L2 clusters correlated tokens, exploiting the genuine gradient only for CV$\,{>}\,$0.2.
117	
118	In practice, CV partitions models into three compressibility classes: \emph{uniform} (CV$\,{<}\,$0.1; safe for moderate pruning but method-sensitive), \emph{graded} (CV$\,{\approx}\,$0.15--0.22; threshold-dependent degradation, L2 increasingly effective with higher CV on single-step tasks but diminishing on multi-step tasks), and \emph{catastrophic} (CV$\,{>}\,$0.3; no pruning tolerance). This coarse classification, validated on four closed-loop architectures, provides actionable guidance without requiring downstream evaluation.
119	
120	\textbf{Architecture-dependent importance scoring.} Extending to attention-based scoring on X-VLA ($k{=}0.5$) reveals that scoring validity depends on connector architecture (Table~\ref{tab:attention_pruning}). L2 norm falls below random on all four suites ($-$8 to $-$27\,pp), while attention scoring recovers near-baseline performance (${\geq}$92.8\%, peaking at 99.2\% on Object). The BART encoder's cross-token self-attention distributes information uniformly, rendering L2 norms anti-informative: Goal L2 is non-monotonic ($k{=}0.7$: 53.4\% $<$ $k{=}0.5$: 59.0\%), confirming that retaining more L2-selected tokens is actively harmful. By contrast, on $\pi_{0.5}$'s linear connector, attention is ineffective: neutral on three suites ($\pm$3\,pp vs.\ random) but catastrophically harmful on Object ($-$30.4\,pp), where attention scores select semantically relevant tokens that lack the spatial precision required for object discrimination. On Long, attention degrades steeply from $k{=}0.95$ ($-$14.6\,pp per step: 77.0\% $\to$ 63.8\% at $k{=}0.9$), while L2 loses only 8.8\,pp across the same range; once past the cliff ($k{\leq}0.85$), attention plateaus at ${\sim}$50\% through $k{=}0.5$ ($-$1.8\,pp total), indicating that the cliff eliminates all recoverable information and further removal has no marginal effect. This confirms that attention is a poor importance proxy for $\pi_{0.5}$'s linear connector. Meanwhile, the L2 importance margin decays from $+$35.2\,pp ($k{=}0.85$) to $+$5.6\,pp ($k{=}0.95$), a connector-dependent scoring reversal (Figure~\ref{fig:scoring_crossover}; Appendix~\ref{app:attention_pruning}). OpenVLA's MLP connector reinforces the token-independent pattern on Object ($+$7.8\,pp for L2 at $k{=}0.9$), but the advantage reverses on Spatial ($-$4.8\,pp), showing that scoring validity is jointly determined by connector architecture and task semantics.
121	
122	\textbf{Disruption peak in random pruning.} Random pruning on $\pi_{0.5}$ is surprisingly unreliable at conservative retention ratios, with task-dependent severity. At $k{=}0.85$, random selection drops to 52.4\% on Goal, 56.6\% on Spatial, and 3.6--5.6\% on Object (two seeds), all below their $k{=}0.5$ performance (73.6\%, 71.6\%, 69.4\% respectively). The Object collapse is confirmed across two seeds and independent RNG implementations (seed42: 5.6\%, seed43: 3.6\%; CI overlap), ruling out both sampling noise and RNG artifacts. L2 selection shows no such valley: Object L2 at $k{=}0.85$ retains 99.0\%, yielding an importance margin exceeding $+$90\,pp, the strongest in our study. The disruption window at ${\sim}$15\% removal falls in a critical regime where enough tokens are displaced to break $\pi_{0.5}$'s learned positional computation patterns, but too few are removed to trigger the robust degradation mode observed at $k{=}0.5$. L2 scoring avoids this vulnerability entirely, demonstrating that importance-based selection is not merely a marginal improvement but a qualitative necessity at intermediate pruning ratios. On Long, the disruption window shifts to even more conservative ratios: at $k{=}0.925$, where just 7.5\% of tokens are removed, random collapses to 38.6\% while L2 preserves 83.2\%, a 44.6\,pp gap that exceeds the $k{=}0.85$ margin of 28.6\,pp (Figure~\ref{fig:cliff_highlight}). Compositional tasks thus amplify the disruption peak, requiring importance-based selection at progressively smaller removal fractions. The contrasting curve shapes---L2 monotonically decreasing versus random's V-shape recovery at $k{\leq}0.7$---arise from an interaction between selection strategy and positional encoding (Section~\ref{sec:analysis}).
123	
124	\begin{figure}[t]
125	\centering
126	\includegraphics[width=\linewidth]{figures/paper/fig_cliff_highlight.pdf}
127	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long. L2 norm degrades monotonically ($-$8.8\,pp from $k{=}0.95$ to $0.85$); attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$25.4\,pp), then plateaus through $k{=}0.5$ (only $-$1.8\,pp further); random exhibits a V-shape with collapse at $k{=}0.925$ (44.6\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$. The divergence reflects position encoding sensitivity (Section~\ref{sec:analysis}).}
128	\label{fig:cliff_highlight}
129	\end{figure}
130	
131	\textbf{Importance margin gradient.} The L2 importance margin (the advantage of L2 over random at $k{=}0.85$) decreases monotonically with task complexity on $\pi_{0.5}$: Object $+$93\,pp (99.0\% vs.\ 5.6\%) $>$ Goal $+$35.2\,pp $>$ Long $+$28.6\,pp (78.0\% vs.\ 49.4\%). As compositional demands increase, L2 norms become a weaker proxy for token utility: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles, compressing the margin between importance-based and random selection.
132	
133	\textbf{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$28.6\,pp for L2) masks extreme per-task heterogeneity (per-task $\sigma{=}$21.5\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\% while random achieves 52\% ($-$44\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.
134	
135	\begin{figure}[h]
136	\centering
137	\includegraphics[width=\linewidth]{figures/paper/fig_scoring_crossover.pdf}
138	\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\Delta{<}3.5$\,pp). $\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\% regardless of method. Compact 2$\times$2 summary in Appendix Table~\ref{tab:scoring_crossover_summary}.}
139	\label{fig:scoring_crossover}
140	\end{figure}
141	
142	\subsection{VTR Recovery}
143	\label{sec:vtr_recovery}
144	
145	Vision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. A cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) uses $M$ learned queries to attend over all 128 source tokens, recovering SmolVLA from 0.0\% to over 60\% SR at 75\% compression ($M{=}32$: 60.1 $\pm$ 1.3\%, 3 seeds). The M-curve is flat ($M{=}16$ matches $M{=}128$ within 1.1\,pp), and a parameter-matched MLP adapter achieves comparable performance (63.4 $\pm$ 2.6\%, $p{=}0.15$), confirming the gain stems from re-encoding itself. Cross-suite generalization: Spatial 53.2\%, Goal 56.4\%, both from 0.0\%. Training uses batch size 4 on one GPU (vs.\ 512 across 8 GPUs officially); the lower baseline (44.8\% vs.\ 59.2\%) reflects this gap (Appendix~\ref{app:smart_compress_details},~\ref{app:vtr_full}).
146	
147	\begin{table}[h]
148	\centering
149	\small
150	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\%; VTR recovers ${\geq}$57\% at up to 87.5\% compression. MLP adapter ($p{=}0.15$ vs.\ cross-attention) confirms re-encoding, not cross-attention specifically, drives the gain. Full results in Appendix~\ref{app:vtr_full}.}
151	\label{tab:vtr_main}
152	\begin{tabular}{lccr}
153	\toprule
154	Configuration & $M$ & Compress.\ & SR (\%) \\
155	\midrule
156	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
157	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
158	\midrule
159	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
160	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
161	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\subsection{Computational Efficiency}
167	\label{sec:efficiency}
168	
169	Token pruning shortens the LLM's input sequence and reduces computation in both attention and feedforward layers. Self-attention FLOPs scale quadratically with sequence length: removing $(1{-}k) \cdot N$ vision tokens from a total sequence of $L = N + L_\text{other}$ tokens reduces attention cost to a fraction
170	\begin{equation}
171	\rho_\text{attn} = \left(\frac{L - (1{-}k) \cdot N}{L}\right)^{\!2},
172	\label{eq:flops_ratio}
173	\end{equation}
174	while FFN costs decrease linearly by $(1{-}k) \cdot N / L$. The practical impact scales with the vision-to-total token ratio. For $\pi_{0.5}$, vision tokens dominate the input ($N{=}768$ of $L{\approx}900$): at $k{=}0.9$, where L2 scoring preserves full SR (98.2\%), removing 77 tokens cuts attention FLOPs by ${\sim}$16\% and FFN cost by ${\sim}$9\%. At $k{=}0.5$ the savings reach ${\sim}$67\% attention and ${\sim}$43\% FFN, but SR drops substantially (Table~\ref{tab:main_results}). X-VLA's compact 50-token representation limits absolute savings regardless of pruning ratio. For SmolVLA, VTR at $M{=}16$ achieves 87.5\% vision token compression with ${\leq}$1.1\,pp below the passthrough control ($M{=}128$: 56.9\% vs.\ 58.0\%; Section~\ref{sec:vtr_recovery}), the largest practical reduction in our study.
175	
176	\paragraph{Limitations.}
177	All evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; cross-seed validation shows $\Delta \leq 5.8$\,pp (Appendix~\ref{app:pi05_multiseed},~\ref{app:openvla_multiseed}). Extended discussion in Appendix~\ref{app:discussion}.
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "08be5610-1f56-460b-8453-5816ff932d0a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nWe evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.\n\nFour models are evaluated in closed-loop robotic control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B parameters, linear projection with $\\times\\!\\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\\cite{lewis2020bart}, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$ folding, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models are analyzed via offline metrics only: $\\pi_{0}$~\\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\\,{=}\\,$0.038) and OFT~\\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\\,{=}\\,$0.219). All six architectures contribute to the CV diagnostic (Section~\\ref{sec:cv_sensitivity}). Table~\\ref{tab:model_properties} summarizes model properties and connector details.\n\nWe follow the pruning protocol of Section~\\ref{sec:pruning_protocol} at retention ratios $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, reporting mean success rate (SR) over 500 episodes with Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\nThe pruning response depends on token independence imposed by the connector and task complexity (Figure~\\ref{fig:teaser}). Token-independent connectors degrade gracefully; token-entangling connectors exhibit sharp, task-dependent collapse.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (best scoring method per model; all curves use L2 norm, which is optimal or near-optimal for each architecture at $k{\\geq}0.85$). Four VLAs span a complete degradation spectrum: $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nTable~\\ref{tab:main_results} presents closed-loop success rates across four models, four LIBERO suites, two pruning methods, and four retention ratios. The data reveal four qualitatively distinct response patterns spanning the connector spectrum (Figure~\\ref{fig:pruning_overview}).\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} On Object, L2 selection yields a plateau (${\\geq}$98.0\\%) through $k{=}0.85$, then drops to 55.0\\% at $k{=}0.7$. Random selection shows a different trajectory (74.0\\% at $k{=}0.95$, non-monotonic thereafter). The method gap reaches 89.2\\,pp at $k{=}0.9$ (Table~\\ref{tab:main_results}). Low-CV models are not pruning-immune but uniformly critical: the choice of \\emph{which} tokens to remove matters more than how many.\n\n\\textbf{X-VLA (linear + BART encoder, CV$\\,{=}\\,$0.151).} X-VLA exhibits threshold-graded behavior with a pronounced interaction between retention ratio and task complexity. On Object, L2 preserves 99.0\\% at $k{=}0.95$ and 97.6\\% at $k{=}0.9$, then falls sharply with non-monotonic recovery (Table~\\ref{tab:main_results}). The same model at $k{=}0.9$ achieves only 70.2\\% on Goal, a 27.4\\,pp cross-task gap driven entirely by task complexity. On Long, removing just 3 of 50 tokens ($k{=}0.95$) collapses SR to 47.0\\% (L2) and 48.2\\% (random); the 1.2\\,pp method gap amid 47.0\\,pp degradation confirms the BART encoder distributes information uniformly across tokens even as it amplifies compositional task demands.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA reveals that even within a single token-independent architecture, the optimal scoring method is suite-dependent (Table~\\ref{tab:main_results}). At $k{=}0.9$ on Object, L2 outperforms random by $+$7.8\\,pp (70.6\\% vs.\\ 62.8\\%), consistent with the MLP projector's genuine importance gradient; attention-based scoring is worst at 61.4\\% ($-$12.6\\,pp from baseline), suggesting that attention weights misidentify salient tokens for object manipulation. On Spatial, the ranking inverts: attention is best at 80.4\\% ($+$0.4\\,pp, lossless), random near-baseline at 79.8\\%, while L2 \\emph{underperforms} at 75.0\\% ($-$5.0\\,pp). On Goal, attention achieves 73.2\\% ($-$1.6\\,pp, near-lossless), L2 matches baseline (74.8\\%), and random anomalously exceeds it (79.6\\%). On Long, all three methods converge (L2: 43.6\\%, random: 46.8\\%, attention: 44.0\\%), with method gaps ${\\leq}$3.2\\,pp amid 6--9\\,pp baseline degradation. This within-model crossover---attention worst on Object ($-$12.6\\,pp) yet best on Spatial ($+$0.4\\,pp), L2 best on Object yet worst on Spatial---demonstrates that no scoring method is universally safe, even within a single connector type.\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} SmolVLA collapses to near-zero SR (${\\leq}$6.6\\%) across all four suites, both pruning methods, and all retention ratios including $k{=}0.95$ where only 6 of 128 tokens are removed. This catastrophic cliff is detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\textbf{Task complexity amplification.} Multi-step tasks amplify degradation in a connector-dependent manner. Under random pruning at $k{=}0.9$, X-VLA loses 1.4\\,pp on Object but 27.8\\,pp on Goal ($20{\\times}$ amplification). Token-entangling connectors show sharper amplification because compositional tasks require information integration across the cross-token dependencies that pruning disrupts (Appendix~\\ref{app:cross_suite_extended}).\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning at four retention ratios. Best result per row in \\textbf{bold}. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42); cross-seed variance reported in Appendix Tables~\\ref{tab:pi05_l2_multiseed} and~\\ref{tab:openvla_multiseed} where available. \\textsuperscript{$\\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}\n\\label{tab:main_results}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 81.0 / 31.8 & 63.2 / 64.6 & 50.2 / 50.2 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{OpenVLA}\n& Object  & \\textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\\textsuperscript{$\\dagger$} & -- / -- & 39.2 / 35.8 \\\\\n& Goal    & \\textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Spatial & \\textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Long    & \\textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{Pixel-shuffle $4{\\times}4$ folding: each block of 16 SigLIP patches is channel-concatenated into one token. Removing any token eliminates a non-overlapping $4{\\times}4$ receptive field (gray) with no redundancy from neighboring tokens.}\n\\label{fig:pixel_shuffle}\n\\end{figure}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields with no inter-token redundancy. SmolVLA collapses to ${\\leq}$6.6\\% SR at $k{=}0.95$ across all suites and methods, verified on two checkpoints (44.8\\% and 59.2\\% baselines); the cliff is architectural. No scoring function can identify dispensable tokens because all carry spatially entangled information; the failure is that any removal breaks completeness. Token-independent connectors retain per-patch locality, so partial removal preserves spatial coverage.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\nThe preceding results show that $\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We isolate whether this failure stems from information loss (missing pixel content) or position disruption (shifted token indices in the LLM's sequence).\n\n\\textbf{Zero-mask ablation.} We compare two conditions at $k{=}0.9$ with random token selection on $\\pi_{0.5}$ Object: (1)~\\emph{hard pruning}, which physically removes selected tokens and compacts the remaining sequence; (2)~\\emph{zero-masking}, which replaces selected token embeddings with zero vectors while preserving all token positions. Both conditions destroy identical visual information---the same 10\\% of vision tokens carry no signal---but only hard pruning alters the positional structure of the remaining sequence.\n\nZero-masking preserves 98.0\\% SR ($-$0.2\\,pp from the 98.2\\% baseline), while hard pruning collapses to 9.0\\% ($-$89.2\\,pp). The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector with learned positional encodings creates a rigid position-to-semantics mapping that tolerates complete signal destruction but not index shifts.\n\nThis result provides causal evidence for the connector dependence observed in Section~\\ref{sec:two_axis}: token-independent connectors do not make tokens dispensable---they make token \\emph{positions} critical. The practical implication is that pruning methods for low-CV architectures must either preserve positional structure (e.g., zero-masking, learned compression) or re-encode positions after deletion.\n\n\\subsection{When Does Pruning Method Matter? CV as Sensitivity Indicator}\n\\label{sec:cv_sensitivity}\n\nToken importance CV (Table~\\ref{tab:model_properties}) correlates with the retention ratio at which pruning method choice becomes critical. At $k{=}0.95$, we compare the three closed-loop models with nonzero SR.\n\nFor $\\pi_{0.5}$ (CV$\\,{=}\\,$0.055), the method gap at $k{=}0.95$ is substantial on Object (Table~\\ref{tab:main_results}): L2 retains the full baseline (98.2\\%) while random selection degrades markedly. Near-uniform norms cause L2 ranking to exploit spatial correlations rather than genuine importance, while random selection preserves the uniform coverage these models depend on.\n\nFor X-VLA (CV$\\,{=}\\,$0.151), the gap averages 0.8\\,pp across all four suites (range 0.2--1.4\\,pp).\n\nFor OpenVLA (CV$\\,{=}\\,$0.215), the method gap at $k{=}0.9$ is suite-dependent: L2 outperforms random by $+$7.8\\,pp on Object (70.6\\% vs.\\ 62.8\\%) but underperforms by $-$4.8\\,pp on Spatial (75.0\\% vs.\\ 79.8\\%), while both methods match baseline on Goal (${\\leq}$4.8\\,pp gap). This within-model crossover demonstrates that scoring validity depends on task semantics even for a single connector type.\n\nX-VLA shows method gaps ${\\leq}$1.4\\,pp at $k{=}0.95$ across all four suites (Figure~\\ref{fig:method_gap}). OpenVLA's suite-dependent method gap, ranging from $+$7.8\\,pp (L2 favored) to $-$4.8\\,pp (random favored), illustrates that higher CV enables but does not guarantee L2 advantage.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$. $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$, reflecting CV-correlated divergence in pruning method sensitivity.}\n\\label{fig:method_gap}\n\\end{figure}\n\nAt $k{=}0.5$, method-independence breaks down: $\\Delta$(R$-$L2) on Object is $+$36.0\\,pp ($\\pi_{0.5}$), $+$27.2\\,pp (X-VLA), $-$3.4\\,pp (OpenVLA). Random preserves spatial diversity; L2 clusters correlated tokens, exploiting the genuine gradient only for CV$\\,{>}\\,$0.2.\n\nIn practice, CV partitions models into three compressibility classes: \\emph{uniform} (CV$\\,{<}\\,$0.1; safe for moderate pruning but method-sensitive), \\emph{graded} (CV$\\,{\\approx}\\,$0.15--0.22; threshold-dependent degradation, L2 increasingly effective with higher CV on single-step tasks but diminishing on multi-step tasks), and \\emph{catastrophic} (CV$\\,{>}\\,$0.3; no pruning tolerance). This coarse classification, validated on four closed-loop architectures, provides actionable guidance without requiring downstream evaluation.\n\n\\textbf{Architecture-dependent importance scoring.} Extending to attention-based scoring on X-VLA ($k{=}0.5$) reveals that scoring validity depends on connector architecture (Table~\\ref{tab:attention_pruning}). L2 norm falls below random on all four suites ($-$8 to $-$27\\,pp), while attention scoring recovers near-baseline performance (${\\geq}$92.8\\%, peaking at 99.2\\% on Object). The BART encoder's cross-token self-attention distributes information uniformly, rendering L2 norms anti-informative: Goal L2 is non-monotonic ($k{=}0.7$: 53.4\\% $<$ $k{=}0.5$: 59.0\\%), confirming that retaining more L2-selected tokens is actively harmful. By contrast, on $\\pi_{0.5}$'s linear connector, attention is ineffective: neutral on three suites ($\\pm$3\\,pp vs.\\ random) but catastrophically harmful on Object ($-$30.4\\,pp), where attention scores select semantically relevant tokens that lack the spatial precision required for object discrimination. On Long, attention degrades steeply from $k{=}0.95$ ($-$14.6\\,pp per step: 77.0\\% $\\to$ 63.8\\% at $k{=}0.9$), while L2 loses only 8.8\\,pp across the same range; once past the cliff ($k{\\leq}0.85$), attention plateaus at ${\\sim}$50\\% through $k{=}0.5$ ($-$1.8\\,pp total), indicating that the cliff eliminates all recoverable information and further removal has no marginal effect. This confirms that attention is a poor importance proxy for $\\pi_{0.5}$'s linear connector. Meanwhile, the L2 importance margin decays from $+$35.2\\,pp ($k{=}0.85$) to $+$5.6\\,pp ($k{=}0.95$), a connector-dependent scoring reversal (Figure~\\ref{fig:scoring_crossover}; Appendix~\\ref{app:attention_pruning}). OpenVLA's MLP connector reinforces the token-independent pattern on Object ($+$7.8\\,pp for L2 at $k{=}0.9$), but the advantage reverses on Spatial ($-$4.8\\,pp), showing that scoring validity is jointly determined by connector architecture and task semantics.\n\n\\textbf{Disruption peak in random pruning.} Random pruning on $\\pi_{0.5}$ is surprisingly unreliable at conservative retention ratios, with task-dependent severity. At $k{=}0.85$, random selection drops to 52.4\\% on Goal, 56.6\\% on Spatial, and 3.6--5.6\\% on Object (two seeds), all below their $k{=}0.5$ performance (73.6\\%, 71.6\\%, 69.4\\% respectively). The Object collapse is confirmed across two seeds and independent RNG implementations (seed42: 5.6\\%, seed43: 3.6\\%; CI overlap), ruling out both sampling noise and RNG artifacts. L2 selection shows no such valley: Object L2 at $k{=}0.85$ retains 99.0\\%, yielding an importance margin exceeding $+$90\\,pp, the strongest in our study. The disruption window at ${\\sim}$15\\% removal falls in a critical regime where enough tokens are displaced to break $\\pi_{0.5}$'s learned positional computation patterns, but too few are removed to trigger the robust degradation mode observed at $k{=}0.5$. L2 scoring avoids this vulnerability entirely, demonstrating that importance-based selection is not merely a marginal improvement but a qualitative necessity at intermediate pruning ratios. On Long, the disruption window shifts to even more conservative ratios: at $k{=}0.925$, where just 7.5\\% of tokens are removed, random collapses to 38.6\\% while L2 preserves 83.2\\%, a 44.6\\,pp gap that exceeds the $k{=}0.85$ margin of 28.6\\,pp (Figure~\\ref{fig:cliff_highlight}). Compositional tasks thus amplify the disruption peak, requiring importance-based selection at progressively smaller removal fractions. The contrasting curve shapes---L2 monotonically decreasing versus random's V-shape recovery at $k{\\leq}0.7$---arise from an interaction between selection strategy and positional encoding (Section~\\ref{sec:analysis}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long. L2 norm degrades monotonically ($-$8.8\\,pp from $k{=}0.95$ to $0.85$); attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$25.4\\,pp), then plateaus through $k{=}0.5$ (only $-$1.8\\,pp further); random exhibits a V-shape with collapse at $k{=}0.925$ (44.6\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$. The divergence reflects position encoding sensitivity (Section~\\ref{sec:analysis}).}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} The L2 importance margin (the advantage of L2 over random at $k{=}0.85$) decreases monotonically with task complexity on $\\pi_{0.5}$: Object $+$93\\,pp (99.0\\% vs.\\ 5.6\\%) $>$ Goal $+$35.2\\,pp $>$ Long $+$28.6\\,pp (78.0\\% vs.\\ 49.4\\%). As compositional demands increase, L2 norms become a weaker proxy for token utility: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles, compressing the margin between importance-based and random selection.\n\n\\textbf{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$28.6\\,pp for L2) masks extreme per-task heterogeneity (per-task $\\sigma{=}$21.5\\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \\emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\\% while random achieves 52\\% ($-$44\\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_scoring_crossover.pdf}\n\\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\\Delta{<}3.5$\\,pp). $\\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\\% regardless of method. Compact 2$\\times$2 summary in Appendix Table~\\ref{tab:scoring_crossover_summary}.}\n\\label{fig:scoring_crossover}\n\\end{figure}\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVision Token Re-encoder (VTR) addresses the catastrophic cliff through learned re-encoding rather than hard deletion. A cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all 128 source tokens, recovering SmolVLA from 0.0\\% to over 60\\% SR at 75\\% compression ($M{=}32$: 60.1 $\\pm$ 1.3\\%, 3 seeds). The M-curve is flat ($M{=}16$ matches $M{=}128$ within 1.1\\,pp), and a parameter-matched MLP adapter achieves comparable performance (63.4 $\\pm$ 2.6\\%, $p{=}0.15$), confirming the gain stems from re-encoding itself. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both from 0.0\\%. Training uses batch size 4 on one GPU (vs.\\ 512 across 8 GPUs officially); the lower baseline (44.8\\% vs.\\ 59.2\\%) reflects this gap (Appendix~\\ref{app:smart_compress_details},~\\ref{app:vtr_full}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR recovers ${\\geq}$57\\% at up to 87.5\\% compression. MLP adapter ($p{=}0.15$ vs.\\ cross-attention) confirms re-encoding, not cross-attention specifically, drives the gain. Full results in Appendix~\\ref{app:vtr_full}.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Computational Efficiency}\n\\label{sec:efficiency}\n\nToken pruning shortens the LLM's input sequence and reduces computation in both attention and feedforward layers. Self-attention FLOPs scale quadratically with sequence length: removing $(1{-}k) \\cdot N$ vision tokens from a total sequence of $L = N + L_\\text{other}$ tokens reduces attention cost to a fraction\n\\begin{equation}\n\\rho_\\text{attn} = \\left(\\frac{L - (1{-}k) \\cdot N}{L}\\right)^{\\!2},\n\\label{eq:flops_ratio}\n\\end{equation}\nwhile FFN costs decrease linearly by $(1{-}k) \\cdot N / L$. The practical impact scales with the vision-to-total token ratio. For $\\pi_{0.5}$, vision tokens dominate the input ($N{=}768$ of $L{\\approx}900$): at $k{=}0.9$, where L2 scoring preserves full SR (98.2\\%), removing 77 tokens cuts attention FLOPs by ${\\sim}$16\\% and FFN cost by ${\\sim}$9\\%. At $k{=}0.5$ the savings reach ${\\sim}$67\\% attention and ${\\sim}$43\\% FFN, but SR drops substantially (Table~\\ref{tab:main_results}). X-VLA's compact 50-token representation limits absolute savings regardless of pruning ratio. For SmolVLA, VTR at $M{=}16$ achieves 87.5\\% vision token compression with ${\\leq}$1.1\\,pp below the passthrough control ($M{=}128$: 56.9\\% vs.\\ 58.0\\%; Section~\\ref{sec:vtr_recovery}), the largest practical reduction in our study.\n\n\\paragraph{Limitations.}\nAll evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; cross-seed validation shows $\\Delta \\leq 5.8$\\,pp (Appendix~\\ref{app:pi05_multiseed},~\\ref{app:openvla_multiseed}). Extended discussion in Appendix~\\ref{app:discussion}.\n",
      "numLines": 178,
      "startLine": 1,
      "totalLines": 178
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01C48C3vGEFXjWCEi6ZnMqaR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "d1c18422-d0aa-465e-a299-6fc5f83941d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 26 · 2026-05-27T04:30:02.402Z_

<details><summary>↩ Tool result · `toolu_01C48C3vGEFXjWCEi6ZnMqaR`</summary>

```text
1	\section{Discussion}
2	\label{sec:analysis}
3	
4	\paragraph{Re-encoding and CV diagnostics.}
5	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\,{=}\,$0.151) from $\pi_0$'s uniformly critical profile (CV$\,{=}\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}). For extended mechanistic analysis of how connector architecture creates the observed token independence structure, see Appendices~\ref{app:connector_analysis} and~\ref{app:reencoding_analysis}.
6	
7	\paragraph{Task complexity compresses the importance margin.}
8	The CV diagnostic correctly identifies connector-level compressibility, but practitioners must additionally consider task complexity. On LIBERO-Object (single-step manipulation), L2 norm selection outperforms random on OpenVLA at $k{=}0.9$ ($+$7.8\,pp: L2 70.6\% vs.\ Random 62.8\%). However, this advantage is not robust to deeper compression: at $k{=}0.85$, the importance margin flips to $-$5.2\,pp (Random 60.4\% $>$ L2 55.2\% $\approx$ Attention 55.0\%). The three methods exhibit distinct cliff locations: L2 cliffs earliest ($k{=}0.9{\to}0.85$, $-$15.4\,pp), random next ($k{=}0.85{\to}0.7$, $-$16\,pp), and attention latest ($k{=}0.75{\to}0.7$, $-$9.4\,pp), with attention maintaining a plateau from $k{=}0.85$ to $k{=}0.75$ ($-$1.8\,pp). This staggered cliff onset defines an effective compression window for each scoring method (Figure~\ref{fig:openvla_sweep}). At $k{=}0.5$, all three methods converge within 4.8\,pp (L2: 39.2\%, Random: 35.8\%, Attention: 40.6\%), and scoring choice ceases to matter. On LIBERO-Goal, degradation is smooth with no cliff: all three methods converge within 2\,pp at $k{=}0.7$ (L2: 68.4\%, Random: 68.4\%, Attention: 66.4\%). Notably, random pruning at $k{=}0.9$ \emph{exceeds} the unpruned baseline (79.6\% vs.\ 74.8\%, $+$4.8\,pp; cross-seed confirmed at 80.4\%), suggesting that OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization, reducing redundant token interference. On LIBERO-Long (multi-step, temporally extended tasks), the advantage vanishes earlier and inverts more sharply. At $k{=}0.9$, all three methods converge within 3.2\,pp (Random: 46.8\%, Attention: 44.0\%, L2: 43.6\%). At $k{=}0.85$, attention-based scoring \emph{increases} to 45.8\% while L2 drops to 38.8\%, opening a 7.0\,pp gap. At $k{=}0.7$, the method ranking fully inverts relative to Object: Random (38.8\%) $>$ L2 (31.2\%) $>$ Attention (24.0\%). The negative importance margin amplifies with compression: the Attention--Random gap widens from $-$2.8\,pp ($k{=}0.9$) to $-$14.8\,pp ($k{=}0.7$), with attention degrading $2.5{\times}$ faster than random. Multi-step tasks distribute critical visual information across tokens with heterogeneous norm profiles; both L2 and attention scoring cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires. Random selection, by preserving uniform spatial coverage, provides a more robust signal under these conditions (Figure~\ref{fig:openvla_sweep}).
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\linewidth]{figures/paper/fig_openvla_sweep.pdf}
13	\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}
14	\label{fig:openvla_sweep}
15	\end{figure}
16	
17	This is a concrete manifestation of the two-axis framework (Section~\ref{sec:two_axis}): Axis~1 (connector architecture) determines \emph{whether} pruning is viable; Axis~2 (task complexity) determines \emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.
18	
19	\paragraph{Position encoding mediates the V-shape recovery.}
20	The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\% $\to$ 50.2\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 31.8\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\% at $k{=}0.7$ to 12\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\%---exceeding the $k{=}0.9$ level by $2{\times}$. The zero-mask ablation (Section~\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\% SR, while physically removing the same tokens collapses to 9.0\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.
21	
22	\paragraph{Limitations.}
23	All experiments use LIBERO simulation; models differ in backbone and fusion, preventing causal isolation (Appendix~\ref{app:confounders}). $\pi_0$ is offline only; the CV correlation spans three models; the cliff model captures onset sharpness (RMSE$\,{=}\,$0.025). The position aliasing explanation for the V-shape recovery (above) is consistent with our data but remains a hypothesis---direct measurement of RoPE frequency interference under non-contiguous indexing is needed for confirmation. At extreme compression ($k{=}0.7$), random and L2 converge within noise on $\pi_{0.5}$ Long (64.6\% vs.\ 63.2\%, $\Delta{=}1.4$\,pp $<$ cross-seed variation), consistent with the broader pattern that scoring methods lose discriminative power under heavy compression.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "b8fd1968-88b1-4d57-8fe5-270a8af1e342",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
      "content": "\\section{Discussion}\n\\label{sec:analysis}\n\n\\paragraph{Re-encoding and CV diagnostics.}\nBoth cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \\approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\\,{=}\\,$0.151) from $\\pi_0$'s uniformly critical profile (CV$\\,{=}\\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\\ref{app:cv_strategy_interaction},~\\ref{app:cv_extended}). For extended mechanistic analysis of how connector architecture creates the observed token independence structure, see Appendices~\\ref{app:connector_analysis} and~\\ref{app:reencoding_analysis}.\n\n\\paragraph{Task complexity compresses the importance margin.}\nThe CV diagnostic correctly identifies connector-level compressibility, but practitioners must additionally consider task complexity. On LIBERO-Object (single-step manipulation), L2 norm selection outperforms random on OpenVLA at $k{=}0.9$ ($+$7.8\\,pp: L2 70.6\\% vs.\\ Random 62.8\\%). However, this advantage is not robust to deeper compression: at $k{=}0.85$, the importance margin flips to $-$5.2\\,pp (Random 60.4\\% $>$ L2 55.2\\% $\\approx$ Attention 55.0\\%). The three methods exhibit distinct cliff locations: L2 cliffs earliest ($k{=}0.9{\\to}0.85$, $-$15.4\\,pp), random next ($k{=}0.85{\\to}0.7$, $-$16\\,pp), and attention latest ($k{=}0.75{\\to}0.7$, $-$9.4\\,pp), with attention maintaining a plateau from $k{=}0.85$ to $k{=}0.75$ ($-$1.8\\,pp). This staggered cliff onset defines an effective compression window for each scoring method (Figure~\\ref{fig:openvla_sweep}). At $k{=}0.5$, all three methods converge within 4.8\\,pp (L2: 39.2\\%, Random: 35.8\\%, Attention: 40.6\\%), and scoring choice ceases to matter. On LIBERO-Goal, degradation is smooth with no cliff: all three methods converge within 2\\,pp at $k{=}0.7$ (L2: 68.4\\%, Random: 68.4\\%, Attention: 66.4\\%). Notably, random pruning at $k{=}0.9$ \\emph{exceeds} the unpruned baseline (79.6\\% vs.\\ 74.8\\%, $+$4.8\\,pp; cross-seed confirmed at 80.4\\%), suggesting that OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization, reducing redundant token interference. On LIBERO-Long (multi-step, temporally extended tasks), the advantage vanishes earlier and inverts more sharply. At $k{=}0.9$, all three methods converge within 3.2\\,pp (Random: 46.8\\%, Attention: 44.0\\%, L2: 43.6\\%). At $k{=}0.85$, attention-based scoring \\emph{increases} to 45.8\\% while L2 drops to 38.8\\%, opening a 7.0\\,pp gap. At $k{=}0.7$, the method ranking fully inverts relative to Object: Random (38.8\\%) $>$ L2 (31.2\\%) $>$ Attention (24.0\\%). The negative importance margin amplifies with compression: the Attention--Random gap widens from $-$2.8\\,pp ($k{=}0.9$) to $-$14.8\\,pp ($k{=}0.7$), with attention degrading $2.5{\\times}$ faster than random. Multi-step tasks distribute critical visual information across tokens with heterogeneous norm profiles; both L2 and attention scoring cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires. Random selection, by preserving uniform spatial coverage, provides a more robust signal under these conditions (Figure~\\ref{fig:openvla_sweep}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_openvla_sweep.pdf}\n\\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}\n\\label{fig:openvla_sweep}\n\\end{figure}\n\nThis is a concrete manifestation of the two-axis framework (Section~\\ref{sec:two_axis}): Axis~1 (connector architecture) determines \\emph{whether} pruning is viable; Axis~2 (task complexity) determines \\emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.\n\n\\paragraph{Position encoding mediates the V-shape recovery.}\nThe monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\\% $\\to$ 50.2\\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 31.8\\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\\% at $k{=}0.7$ to 12\\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\\%---exceeding the $k{=}0.9$ level by $2{\\times}$. The zero-mask ablation (Section~\\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\\% SR, while physically removing the same tokens collapses to 9.0\\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.\n\n\\paragraph{Limitations.}\nAll experiments use LIBERO simulation; models differ in backbone and fusion, preventing causal isolation (Appendix~\\ref{app:confounders}). $\\pi_0$ is offline only; the CV correlation spans three models; the cliff model captures onset sharpness (RMSE$\\,{=}\\,$0.025). The position aliasing explanation for the V-shape recovery (above) is consistent with our data but remains a hypothesis---direct measurement of RoPE frequency interference under non-contiguous indexing is needed for confirmation. At extreme compression ($k{=}0.7$), random and L2 converge within noise on $\\pi_{0.5}$ Long (64.6\\% vs.\\ 63.2\\%, $\\Delta{=}1.4$\\,pp $<$ cross-seed variation), consistent with the broader pattern that scoring methods lose discriminative power under heavy compression.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01L27ptGrhcFfyDz8BfrBioP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "7c1215b7-f51b-4fff-92e0-ebcf39247ec5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 28 · 2026-05-27T04:30:03.441Z_

<details><summary>↩ Tool result · `toolu_01L27ptGrhcFfyDz8BfrBioP`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Connector architecture is the primary factor governing VLA token compressibility. Across five architectures and four LIBERO suites, token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\times}$ from Object to Goal). While confounders prevent causal isolation (Appendix~\ref{app:confounders}), connector design is the most consistent structural predictor. CV partitions models into uniform, graded, and catastrophic classes in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and k-dependent: L2 norm aids independent connectors at moderate ratios but reverses at aggressive compression; attention shows the converse on entangling connectors. In the cliff zone ($k{=}0.85$--$0.95$), scoring method alone determines success or failure: at $k{=}0.925$ on $\pi_{0.5}$ Long, L2 preserves 83\% while random collapses to 39\% (44.6\,pp gap). Method differentiation requires pruning stress---at $k{=}0.9$ on OpenVLA, all three scoring methods converge within 3\,pp on Long. A zero-mask ablation confirms the mechanism: on $\pi_{0.5}$, zeroing 10\% of tokens retains 98.0\% SR while physical removal collapses to 9.0\%, proving position disruption---not information loss---drives the failure. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression.
5	
6	Two directions remain open: real-robot validation and adaptive per-task pruning schedules. Code and evaluation data will be released upon acceptance. \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "df489181-7333-47ca-a356-36c094143c2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nConnector architecture is the primary factor governing VLA token compressibility. Across five architectures and four LIBERO suites, token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\\times}$ from Object to Goal). While confounders prevent causal isolation (Appendix~\\ref{app:confounders}), connector design is the most consistent structural predictor. CV partitions models into uniform, graded, and catastrophic classes in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and k-dependent: L2 norm aids independent connectors at moderate ratios but reverses at aggressive compression; attention shows the converse on entangling connectors. In the cliff zone ($k{=}0.85$--$0.95$), scoring method alone determines success or failure: at $k{=}0.925$ on $\\pi_{0.5}$ Long, L2 preserves 83\\% while random collapses to 39\\% (44.6\\,pp gap). Method differentiation requires pruning stress---at $k{=}0.9$ on OpenVLA, all three scoring methods converge within 3\\,pp on Long. A zero-mask ablation confirms the mechanism: on $\\pi_{0.5}$, zeroing 10\\% of tokens retains 98.0\\% SR while physical removal collapses to 9.0\\%, proving position disruption---not information loss---drives the failure. Where all deletion fails, VTR recovers over 60\\% SR at 75\\% compression.\n\nTwo directions remain open: real-robot validation and adaptive per-task pruning schedules. Code and evaluation data will be released upon acceptance. \\textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.",
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01DcuzRD97K7HnbdSNr1WjiZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "c78ca624-6753-4024-ab4a-cb3eb6626d58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 30 · 2026-05-27T04:30:03.834Z_

<details><summary>↩ Tool result · `toolu_01DcuzRD97K7HnbdSNr1WjiZ`</summary>

```text
1	% Discussion section moved to Appendix (§\ref{app:discussion}) for space.
2	% Three-sentence limitations retained at end of Experiments section.
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "a47cd6cb-d97c-482f-a6db-d071bff32b3f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex",
      "content": "% Discussion section moved to Appendix (§\\ref{app:discussion}) for space.\n% Three-sentence limitations retained at end of Experiments section.\n",
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_011iBkzRHadPWZWMCV2GCH3N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "efe0ef51-690a-4203-bda2-92bf5873731d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y42GPSBYBvgK2tPV3VZsKG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2801,
      "cache_read_input_tokens": 23632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2801
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

_source line 32 · 2026-05-27T04:30:04.830Z_

<details><summary>↩ Tool result · `toolu_011iBkzRHadPWZWMCV2GCH3N`</summary>

```text
1	\appendix
2	
3	\section{Extended Discussion}
4	\label{app:discussion}
5	
6	\paragraph{Limitations (extended).}
7	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
8	
9	\paragraph{Non-monotonicity as structural property.}
10	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
11	
12	\paragraph{$\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}
13	Random selection on $\pi_{0.5}$ Object collapses from 74.0\% at $k{=}0.95$ to 9.0\% at $k{=}0.9$, then recovers to 74.0\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\%, Object~65.0\%, Goal~60.4\%), but Long drops to 35.0\%, below its $k{=}0.5$ performance of 61.6\% (Table~\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\pi_{0.5}$ Object drops to 5.6\% at $k{=}0.85$ versus 69.4\% at $k{=}0.5$ ($-$63.8\,pp), more than double X-VLA Long's $-$26.6\,pp. The V-shaped recovery at $k \leq 0.7$ remains unexplained.
14	
15	\begin{table}[ht]
16	\centering
17	\small
18	\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\ $\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\%) but drops to 35.0\% on Long (below $k{=}0.5$); $\pi_{0.5}$ exhibits a severe disruption peak on Object.}
19	\label{tab:xvla_k085_crosssuite}
20	\begin{tabular}{lcccc}
21	\toprule
22	Suite & X-VLA SR (\%) & $\Delta$ & $\pi_{0.5}$ SR (\%) & $\Delta$ \\
23	\midrule
24	Object & 65.0 & $-$34.2 & 3.6--5.6\textsuperscript{$\dagger$} & $-$93 to $-$95 \\
25	Goal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\
26	Spatial & 68.2 & $-$24.8 & --- & --- \\
27	Long & 35.0 & $-$59.0 & --- & --- \\
28	\bottomrule
29	\multicolumn{5}{l}{\footnotesize\textsuperscript{$\dagger$}Two seeds: seed42$\,{=}\,$5.6\% (post-fix), seed43$\,{=}\,$3.6\%. $\Delta$ from respective baselines.}
30	\end{tabular}
31	\end{table}
32	
33	\paragraph{Small-$N$ interactions.}
34	X-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\,pp on Goal and $-$47.0\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.
35	
36	\paragraph{Design implications.}
37	Practitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.
38	
39	
40	\section{Cross-Suite Task Complexity Analysis}
41	\label{app:cross_suite_extended}
42	
43	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
44	
45	$\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
46	
47	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\% ($-$1.6\,pp from the 99.2\% baseline), while Goal drops to 70.2\% ($-$28.2\,pp from 98.4\% baseline). Under random pruning at the same ratio, Object loses just 1.4\,pp (97.8\%) while Goal loses 27.8\,pp (70.6\%), a $20{\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\% (L2) and 48.2\% (random), a 47.0\,pp loss with only 1.2\,pp method gap, while Object at the same ratio loses only 0.2\,pp.
48	
49	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
50	
51	
52	\section{Pruning Protocol Details}
53	\label{app:pruning_details}
54	
55	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
56	
57	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_{0.5}$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
58	
59	The $\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.
60	
61	
62	\section{SmolVLA Pruning Ablation}
63	\label{app:smolvla_ablation}
64	
65	\begin{table}[ht]
66	\centering
67	\small
68	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. Two independent evaluations of the official HF checkpoint (59.2\% and 57.2\% baseline, within CI) confirm the cliff-edge across scoring methods.}
69	\label{tab:smolvla_ablation}
70	\begin{tabular}{llccrr}
71	\toprule
72	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
73	\midrule
74	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
75	\midrule
76	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
77	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
78	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
79	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
80	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
81	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
82	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
83	\midrule
84	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol A (59.2\% baseline)}} \\
85	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\
86	Random & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
87	\midrule
88	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol B (57.2\% baseline)}} \\
89	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\
90	Random & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\
91	L2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\
92	L2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
93	\bottomrule
94	\end{tabular}
95	\end{table}
96	
97	
98	\section{Per-Task Breakdown Tables}
99	\label{app:per_task}
100	
101	\subsection{SmolVLA Baseline Per-Task Results}
102	
103	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
104	
105	\begin{table}[ht]
106	\centering
107	\small
108	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
109	\label{tab:smolvla_baseline_pertask}
110	\begin{tabular}{lc}
111	\toprule
112	Task & SR (\%) \\
113	\midrule
114	alphabet\_soup & 22 \\
115	bbq\_sauce & 60 \\
116	butter & 42 \\
117	chocolate\_pudding & 38 \\
118	cream\_cheese & 58 \\
119	ketchup & 26 \\
120	milk & 62 \\
121	orange\_juice & 38 \\
122	salad\_dressing & 50 \\
123	tomato\_sauce & 52 \\
124	\midrule
125	\textbf{Overall} & \textbf{44.8} \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\subsection{Official SmolVLA Checkpoint Per-Task Results}
131	
132	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
133	
134	\begin{table}[ht]
135	\centering
136	\small
137	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
138	\label{tab:smolvla_official_pertask}
139	\begin{tabular}{lcc}
140	\toprule
141	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
142	\midrule
143	alphabet\_soup & 64 & 0 \\
144	bbq\_sauce & 38 & 0 \\
145	butter & 78 & 0 \\
146	chocolate\_pudding & 90 & 0 \\
147	cream\_cheese & 40 & 0 \\
148	ketchup & 60 & 0 \\
149	milk & 52 & 0 \\
150	orange\_juice & 80 & 0 \\
151	salad\_dressing & 44 & 0 \\
152	tomato\_sauce & 46 & 0 \\
153	\midrule
154	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
155	\bottomrule
156	\end{tabular}
157	\end{table}
158	
159	\subsection{OpenVLA Per-Task Results Under Pruning}
160	
161	\begin{table}[ht]
162	\centering
163	\small
164	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
165	\label{tab:openvla_pertask}
166	\begin{tabular}{lccccc}
167	\toprule
168	Task & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\
169	\midrule
170	alphabet\_soup & 76 & 70 & 74 & 60 & 14 \\
171	bbq\_sauce & 38 & 28 & 46 & 44 & 30 \\
172	butter & 84 & 76 & 10 & 2 & 0 \\
173	chocolate\_pudding & 54 & 56 & 32 & 40 & 10 \\
174	cream\_cheese & 84 & 78 & 18 & 8 & 0 \\
175	ketchup & 82 & 70 & 68 & 50 & 30 \\
176	milk & 46 & 42 & 40 & 24 & 8 \\
177	orange\_juice & 74 & 60 & 76 & 72 & 42 \\
178	salad\_dressing & 64 & 54 & 64 & 36 & 64 \\
179	tomato\_sauce & 92 & 86 & 62 & 38 & 8 \\
180	\midrule
181	\textbf{Overall} & \textbf{69.4} & \textbf{62.0} & \textbf{49.0} & \textbf{37.4} & \textbf{20.6} \\
182	\bottomrule
183	\end{tabular}
184	\end{table}
185	
186	\subsection{OpenVLA Full Degradation Curve}
187	
188	\begin{table}[ht]
189	\centering
190	\small
191	\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\%. All confidence intervals are Wilson 95\%.}
192	\label{tab:openvla_full}
193	\begin{tabular}{ccrr}
194	\toprule
195	$k$ & Tokens Retained & SR (\%) & Wilson 95\% CI \\
196	\midrule
197	1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\
198	0.95 & 243 & 69.4 & [65.2, 73.3] \\
199	0.90 & 230 & 62.0 & [57.7, 66.2] \\
200	0.70 & 179 & 49.0 & [44.6, 53.4] \\
201	0.50 & 128 & 37.4 & [33.3, 41.7] \\
202	0.30 & 77 & 20.6 & [17.2, 24.4] \\
203	\bottomrule
204	\end{tabular}
205	\end{table}
206	
207	\subsection{$\pi_{0.5}$ L2 Norm Multi-Seed Consistency}
208	\label{app:pi05_multiseed}
209	
210	\begin{table}[ht]
211	\centering
212	\small
213	\caption{$\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\sigma{=}0.1$\,pp at $k{=}0.5$). V-depth: 17.6\,pp (seed42), 21.8\,pp (seed43).}
214	\label{tab:pi05_l2_multiseed}
215	\begin{tabular}{ccccc}
216	\toprule
217	$k$ & Seed 42 (\%) & Seed 43 (\%) & Mean $\pm$ Std & $\Delta$ (pp) \\
218	\midrule
219	0.70 & 55.0 & 57.8 & $56.4 \pm 2.0$ & $+$2.8 \\
220	0.50 & 33.4 & 33.6 & $33.5 \pm 0.1$ & $+$0.2 \\
221	0.30 & 51.0 & 55.4 & $53.2 \pm 3.1$ & $+$4.4 \\
222	\bottomrule
223	\end{tabular}
224	\end{table}
225	
226	\subsection{$\pi_{0.5}$ Cross-Suite Comparison}
227	\label{app:pi05_crosssuite}
228	
229	\begin{table}[ht]
230	\centering
231	\small
232	\caption{$\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\%) and LIBERO-Spatial (baseline 97.2\%), seed\,42, 500 episodes each. Object random exhibits a deep cliff at $k \in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\leq 2.4$\,pp difference at $k \geq 0.85$).}
233	\label{tab:pi05_crosssuite}
234	\begin{tabular}{ccccc}
235	\toprule
236	\multirow{2}{*}{$k$} & \multicolumn{2}{c}{LIBERO-Object (\%)} & \multicolumn{2}{c}{LIBERO-Spatial (\%)} \\
237	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
238	 & L2 Norm & Random & L2 Norm & Random \\
239	\midrule
240	1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\
241	0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\
242	0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\
243	0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\
244	0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\
245	0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\
246	0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\
247	0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\
248	\bottomrule
249	\end{tabular}
250	\end{table}
251	
252	\begin{figure}[ht]
253	\centering
254	\includegraphics[width=0.85\linewidth]{figures/paper/fig_crosssuite.pdf}
255	\caption{$\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \in [0.85, 0.925]$ with 68\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}
256	\label{fig:crosssuite}
257	\end{figure}
258	
259	The random cliff at $k \in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\% ($k{=}0.95$) to 5.6\% ($k{=}0.85$), whereas Spatial retains 58.4\% at $k{=}0.85$ ($\Delta{=}53$\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\% $>$ $k{=}0.9$: 54.6\%, $\Delta{=}5.8$\,pp), but this is an order of magnitude smaller than Object's 68\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.
260	
261	L2 norm selection is consistent across suites at high retention ($k \geq 0.85$): Object and Spatial differ by $\leq 2.4$\,pp (Table~\ref{tab:pi05_crosssuite}). At $k \leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\% at $k{=}0.5$; Spatial valley: 55.6\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.
262	
263	\subsection{Token Importance Spatial Distribution}
264	\label{app:token_heatmap}
265	
266	\begin{figure}[ht]
267	\centering
268	\includegraphics[width=0.85\linewidth]{figures/paper/fig_token_heatmap.pdf}
269	\caption{$\pi_{0.5}$ token importance spatial distribution (16$\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\sim$265--267; edge rows 0, 14--15: norm $\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\ 21.87; CV${=}$0.059). The 33\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}
270	\label{fig:token_heatmap}
271	\end{figure}
272	
273	Token importance heatmaps reveal that $\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\times$16 spatial grid after the $\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.
274	
275	Random removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.
276	
277	\subsection{Hypergeometric Cliff Model}
278	\label{app:cliff_model}
279	
280	\begin{figure}[ht]
281	\centering
282	\includegraphics[width=0.85\linewidth]{figures/paper/fig_cliff_model.pdf}
283	\caption{Hypergeometric cliff model for $\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\ observed success rate (solid) across the cliff zone $k \in [0.85, 0.95]$; RMSE${=}$0.025. (b)~$P(\text{collapse})$ curves for Object ($C{=}91$, concentrated) and Spatial ($C \approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}
284	\label{fig:cliff_model}
285	\end{figure}
286	
287	The random cliff on $\pi_{0.5}$ Object (Section~\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \in \{0.9, 0.925, 0.95\}$; all post-fix confirmed). When $\lfloor N(1{-}k) \rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\mathrm{Hypergeometric}(N, C, \lfloor N(1{-}k) \rfloor)$. We define performance collapse as removing $\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.
288	
289	The model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\text{collapse}){=}10\%$ (cliff onset), $k{=}0.937$ where $P(\text{collapse}){=}50\%$ (midpoint), and $k{=}0.904$ where $P(\text{collapse}){=}90\%$ (near-complete collapse). The cliff width $\Delta k \approx 0.056$ between 10\% and 90\% collapse probability matches the observed transition from 74.0\% SR ($k{=}0.95$) to 9.0\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \leq 0.7$, where success rate rebounds to 74.0\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.
290	
291	The cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\% of the grid), creating a steep increase in $P(\text{collapse} \geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \approx 5$ tokens, making the probability of simultaneously removing $\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\% at $k{=}0.85$ vs.\ Object's 5.6\%).
292	
293	\subsection{OpenVLA Multi-Seed Consistency}
294	\label{app:openvla_multiseed}
295	
296	\begin{table}[ht]
297	\centering
298	\small
299	\caption{OpenVLA success rates (\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\ref{tab:main_results}) uses seed 42 for both L2 and random.}
300	\label{tab:openvla_multiseed}
301	\begin{tabular}{cccc}
302	\toprule
303	$k$ & Seed 7 (\%) & Seed 43 (\%) & $\Delta$ (pp) \\
304	\midrule
305	0.90 & 62.0 & 62.2 & $+$0.2 \\
306	0.70 & 49.0 & 44.4 & $-$4.6 \\
307	0.50 & 37.4 & 35.6 & $-$1.8 \\
308	\bottomrule
309	\end{tabular}
310	\end{table}
311	
312	\subsection{L2 Norm vs.\ Random Scoring on OpenVLA}
313	\label{app:l2_vs_random}
314	
315	\begin{table}[ht]
316	\centering
317	\small
318	\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\,{=}\,$42; random uses seed$\,{=}\,$7. Main text (Table~\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\%, $k{=}0.5$: 35.8\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\% (L2 outperforms by 3.6\,pp); same-seed at $k{=}0.7$ yields 44.4\% (L2 outperforms by 5.4\,pp). $\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}
319	\label{tab:openvla_l2_vs_random}
320	\begin{tabular}{cccc}
321	\toprule
322	$k$ & L2 Norm SR (\%) & Random SR (\%) & $\Delta$ (pp) \\
323	\midrule
324	0.95 & 70.6 & 69.4 & $+$1.2 \\
325	0.90 & 70.6 & 62.0 & $+$8.6 \\
326	0.70 & 49.8 & 49.0 & $+$0.8 \\
327	0.50 & 39.2 & 37.4 & $+$1.8 \\
328	0.30 & 25.0 & 20.6 & $+$4.4 \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	\subsection{X-VLA Cliff Localization: Per-Task Analysis}
334	\label{app:xvla_cliff}
335	
336	\begin{table}[ht]
337	\centering
338	\small
339	\caption{X-VLA per-task success rates (\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \pm 0.7$\% at $k{=}0.80$, $67.9 \pm 0.3$\% at $k{=}0.85$). Despite retaining \emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\,pp overall. Four tasks (\textbf{bold}) suffer catastrophic interference ($\Delta \leq -50$\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\Delta| \leq 10$\,pp). Cross-seed variance is $\leq 4$\,pp per task.}
340	\label{tab:xvla_cliff_pertask}
341	\begin{tabular}{lccr}
342	\toprule
343	Task & $k{=}0.80$ (\%) & $k{=}0.85$ (\%) & $\Delta$ (pp) \\
344	\midrule
345	alphabet\_soup & 100.0 & 100.0 & 0 \\
346	bbq\_sauce & 85.0 & 87.0 & $+$2 \\
347	\textbf{butter} & \textbf{57.0} & \textbf{0.0} & $\boldsymbol{-57}$ \\
348	\textbf{chocolate\_pudding} & \textbf{88.0} & \textbf{35.0} & $\boldsymbol{-53}$ \\
349	\textbf{cream\_cheese} & \textbf{98.0} & \textbf{45.0} & $\boldsymbol{-53}$ \\
350	\textbf{ketchup} & \textbf{79.0} & \textbf{27.0} & $\boldsymbol{-52}$ \\
351	milk & 85.0 & 95.0 & $+$10 \\
352	orange\_juice & 96.0 & 98.0 & $+$2 \\
353	salad\_dressing & 100.0 & 100.0 & 0 \\
354	tomato\_sauce & 98.0 & 91.0 & $-$7 \\
355	\midrule
356	\textbf{Overall} & \textbf{89.0} & \textbf{67.9} & $\boldsymbol{-21.1}$ \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	The non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\_pudding, cream\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\_soup, salad\_dressing) feature distinctive objects or high-contrast targets.
362	
363	\subsection{VTR Per-Task Comparison}
364	
365	\begin{table}[ht]
366	\centering
367	\small
368	\caption{VTR per-task success rates on LIBERO-Object for $M \in \{32, 64, 128\}$ (seed 42; 3-seed means are reported in Table~\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\%--61.6\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}
369	\label{tab:smart_compress_pertask}
370	\begin{tabular}{lcccc}
371	\toprule
372	Task & $M{=}32$ (\%) & $M{=}64$ (\%) & $M{=}128$ (\%) \\
373	\midrule
374	alphabet\_soup & 68 & 74 & 62 \\
375	bbq\_sauce & 46 & 56 & 34 \\
376	butter & 82 & 84 & 82 \\
377	chocolate\_pudding & 90 & 74 & 82 \\
378	cream\_cheese & 64 & 38 & 58 \\
379	ketchup & 66 & 64 & 62 \\
380	milk & 76 & 62 & 56 \\
381	orange\_juice & 28 & 46 & 58 \\
382	salad\_dressing & 60 & 64 & 54 \\
383	tomato\_sauce & 36 & 54 & 50 \\
384	\midrule
385	\textbf{Overall} & \textbf{61.6} & \textbf{61.6} & \textbf{59.8} \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	\subsection{VTR Multi-Seed Results}
391	
392	\begin{table}[ht]
393	\centering
394	\small
395	\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\pm$ std reported.}
396	\label{tab:multi_seed}
397	\begin{tabular}{lccccr}
398	\toprule
399	$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\pm$ Std \\
400	\midrule
401	32 & 61.6 & 59.2 & 59.6 & 60.1 $\pm$ 1.3 \\
402	64 & 61.6 & 60.0 & 64.4 & 62.0 $\pm$ 2.3 \\
403	96 & 52.6 & 58.2 & 52.8 & 54.5 $\pm$ 3.2 \\
404	128 & 59.8 & 54.0 & 60.2 & 58.0 $\pm$ 3.5 \\
405	\bottomrule
406	\end{tabular}
407	\end{table}
408	
409	
410	\section{VTR Full Results}
411	\label{app:vtr_full}
412	
413	\begin{table}[ht]
414	\centering
415	\small
416	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
417	\label{tab:vtr_results}
418	\begin{tabular}{lccr}
419	\toprule
420	Configuration & $M$ & Compression & SR (\%) \\
421	\midrule
422	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
423	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
424	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
425	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
426	\midrule
427	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
428	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
429	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
430	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
431	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
432	\midrule
433	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	
439	\section{Full VTR Ablation}
440	\label{app:smart_compress_full}
441	
442	Table~\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \in \{32, 64, 128\}$ all achieve $\sim$60\% SR, exceeding the 44.8\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5\% compression) does performance decline modestly to 55.8\%, still 11 points above baseline. The $M{=}96$ dip (mean 54.5\% across three seeds, Table~\ref{tab:multi_seed}) may reflect an intermediate bottleneck that introduces representational redundancy without the regularization benefit of stronger compression ($M{=}32$, $M{=}64$).
443	
444	Table~\ref{tab:cross_suite} reports performance across task suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long. On LIBERO-Spatial, VTR achieves 53.2\% SR (vs.\ 0\% under hard pruning); on LIBERO-Goal, 56.4\% SR ($-6.6$pp from the 63.0\% unpruned baseline, vs.\ 0\% under pruning). The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures even within the training distribution. Per-task results are in Table~\ref{tab:smart_compress_pertask}.
445	
446	\begin{table}[ht]
447	\centering
448	\small
449	\caption{Full VTR ablation on LIBERO-Object across five compression levels. $M{=}32$ and $M{=}64$ achieve similar SR ($\sim$60\%); $M{=}96$ shows a modest dip; the $M{=}128$ passthrough confirms the gain originates from re-encoding.}
450	\label{tab:smart_compress_full}
451	\begin{tabular}{lcccrr}
452	\toprule
453	Method & $M$ & Reduction & SR (\%) & Episodes & Wilson 95\% CI \\
454	\midrule
455	\textit{Baseline} & 128 & 0\% & 44.8 & 500 & [40.5, 49.2] \\
456	\textit{Extended training} & -- & -- & 45.0 & 500 & [40.7, 49.3] \\
457	\textit{Hard pruning} & -- & 50--90\% & 0.0 & 500+ & [0, 0.76] \\
458	\midrule
459	VTR & 128 & 0\% & 58.0 & 1500 & $\pm$3.5 \\
460	VTR & 96 & 25\% & 52.6 & 500 & [48.2, 56.9] \\
461	VTR & 64 & 50\% & 61.6 & 500 & [57.3, 65.8] \\
462	VTR & 32 & 75\% & 61.6 & 500 & [57.3, 65.8] \\
463	VTR & 16 & 87.5\% & 55.8 & 500 & [51.4, 60.1] \\
464	\bottomrule
465	\end{tabular}
466	
467	\vspace{2pt}
468	{\footnotesize $M{=}128$ reports mean $\pm$ std over 3 seeds (500 episodes each). Other VTR rows report single seed (seed 42) with Wilson 95\% CI. See Table~\ref{tab:multi_seed} for full multi-seed results.}
469	\end{table}
470	
471	
472	\section{VTR Evaluation Across Task Suites}
473	\label{app:cross_suite}
474	
475	Table~\ref{tab:cross_suite} reports the performance of VTR ($M{=}32$) across three LIBERO suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long (40 tasks, 1693 episodes total). On LIBERO-Goal, performance drops from 63.0\% to 56.4\% ($-6.6$pp). On LIBERO-Spatial, VTR achieves 53.2\% SR, where the official SmolVLA checkpoint scores 43.8\% and hard pruning yields near-zero (0.6\%). While 53.2\% nominally exceeds the official Spatial baseline, this difference concentrates in two of ten tasks (+44pp and +48pp respectively); the remaining eight tasks show a net difference of only +0.2pp. We therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline. The qualitative pattern (cliff-edge vulnerability and re-encoding recovery) extends across the three tested task structures within the training distribution. The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures.
476	
477	\begin{table}[ht]
478	\centering
479	\small
480	\caption{VTR ($M{=}32$) evaluation across LIBERO task suites. All suites are in-distribution (training covers Object, Spatial, Goal, Long). Hard pruning (any method, $k{=}0.50$) produces 0\% or near-zero on all suites.}
481	\label{tab:cross_suite}
482	\begin{tabular}{lccc}
483	\toprule
484	Suite & Baseline (unpruned) & VTR $M{=}32$ & Hard Pruning $k{=}0.50$ \\
485	\midrule
486	Object & 44.8\% & 61.6\% & 0\% \\
487	Spatial & 51.8\% & 53.2\% & 0.6\% \\
488	Goal & 63.0\% & 56.4\% & 0\% \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	
494	\section{VTR Training Details}
495	\label{app:smart_compress_details}
496	
497	The VTR module is a cross-attention pooling layer inserted between SmolVLA's pixel-shuffle vision connector and the Qwen2-0.5B language backbone. It consists of $M$ learned query vectors that attend over the 128 vision tokens through standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compressor adds 22.2M trainable parameters (approximately 5\% of SmolVLA's 451.5M total). Training is end-to-end: compressor and VLA policy parameters are jointly optimized.
498	
499	\begin{table}[ht]
500	\centering
501	\small
502	\caption{VTR training hyperparameters. All configurations ($M \in \{16, 32, 64, 96, 128\}$) use identical procedures; only the number of query vectors differs.}
503	\label{tab:training_hyperparams}
504	\begin{tabular}{ll}
505	\toprule
506	Hyperparameter & Value \\
507	\midrule
508	\multicolumn{2}{l}{\textit{Model}} \\
509	\quad Base checkpoint & SmolVLA-Base (pretrained, before LIBERO fine-tuning) \\
510	\quad Compressor architecture & Cross-attention, 2 layers, 12 heads, dropout 0.1 \\
511	\quad Compressor parameters & 22.2M \\
512	\quad Total trainable parameters & 122.1M / 472.2M (25.85\%) \\
513	\midrule
514	\multicolumn{2}{l}{\textit{Optimization}} \\
515	\quad Optimizer & AdamW ($\beta_1{=}0.9$, $\beta_2{=}0.95$, weight decay $10^{-10}$) \\
516	\quad Learning rate & $10^{-4}$ \\
517	\quad Schedule & Linear warmup (1K steps, start factor 0.01) $\to$ cosine \\
518	\quad & annealing ($\eta_{\min}{=}2.5 \times 10^{-6}$) \\
519	\quad Max gradient norm & 10.0 \\
520	\quad Total training steps & 100,000 \\
521	\midrule
522	\multicolumn{2}{l}{\textit{Data \& batching}} \\
523	\quad Dataset & HuggingFaceVLA/libero (40 tasks, 1693 episodes across \\
524	\quad & Object, Spatial, Goal, Long suites) \\
525	\quad Batch size & 4 (no gradient accumulation)$^\dagger$ \\
526	\quad Num workers & 4 \\
527	\quad Eval interval & every 5K steps \\
528	\quad Checkpoint interval & every 1K steps \\
529	\midrule
530	\multicolumn{2}{l}{\textit{Hardware \& runtime}} \\
531	\quad Hardware & 1$\times$ NVIDIA RTX 4090 D (24GB) \\
532	\quad Precision & fp32 (no mixed precision) \\
533	\quad Wall clock & $\sim$6h 43m per configuration \\
534	\quad Training speed & 4.1 samples/sec \\
535	\quad Seed & 42 (seeds 43, 44 for multi-seed runs) \\
536	\midrule
537	\multicolumn{2}{l}{\textit{$M=32$ final metrics}} \\
538	\quad Train action loss & 0.11 \\
539	\quad Eval action loss & 0.052 \\
540	\midrule
541	\multicolumn{2}{l}{\textit{$M=64$ final metrics}} \\
542	\quad Train action loss & 0.045 \\
543	\quad Eval action loss & 0.062 \\
544	\bottomrule
545	\end{tabular}
546	
547	\vspace{2pt}
548	{\footnotesize $^\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\% vs.\ 87.3\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}
549	\end{table}
550	
551	The loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\ 0.045) but lower eval loss (0.052 vs.\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\ref{sec:metric_disconnect}).
552	
553	\subsection{MLP Adapter Control}
554	\label{app:mlp_adapter}
555	
556	To verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \times d_{\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\% reduction), the MLP adapter achieves $63.4 \pm 2.6$\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \pm 1.3$\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.
557	
558	
559	\section{Offline Single-Step Action Error Analysis}
560	\label{app:offline_error}
561	
562	Table~\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 distance of 0.414 from ground truth; under ACIS pruning at $k{=}0.50$, this increases to 1.391 ($3.4\times$). The per-dimension breakdown of the pruned-vs-unpruned difference reveals that the gripper dimension dominates (L2 = 1.02), corresponding to complete gripper state inversion on many frames. Position errors (0.20--0.30 per axis) are moderate individually but compound across the 7-dimensional action space. These single-step errors are large enough to push the robot off-trajectory within a few steps, explaining why 0\% of pruned episodes succeed in closed-loop evaluation despite moderate average offline metrics.
563	
564	\begin{table}[ht]
565	\centering
566	\small
567	\caption{Single-step action prediction error (SmolVLA, $k{=}0.50$, ACIS, zero-mask, 200 LIBERO-Object evaluation frames). Pruning increases action error by $3.4\times$ and introduces catastrophic gripper inversions.}
568	\label{tab:offline_action_error}
569	\begin{tabular}{lcc}
570	\toprule
571	Metric & Unpruned & Pruned ($k{=}0.50$) \\
572	\midrule
573	Action L2 vs.\ ground truth & 0.414 & 1.391 \\
574	Pruned vs.\ unpruned L2 & \multicolumn{2}{c}{1.284} \\
575	Relative action error & -- & 111.5\% \\
576	\midrule
577	\multicolumn{3}{l}{\textit{Per-dimension L2 (pruned vs.\ unpruned)}} \\
578	\quad Position $(x, y, z)$ & -- & 0.20, 0.25, 0.30 \\
579	\quad Rotation $(r_x, r_y, r_z)$ & -- & 0.01, 0.02, 0.01 \\
580	\quad Gripper & -- & 1.02 \\
581	\bottomrule
582	\end{tabular}
583	\end{table}
584	
585	
586	\section{Supplementary Figures}
587	\label{app:supplementary_figures}
588	
589	% fig_pixel_shuffle moved to Section~\ref{sec:pixel_shuffle} in main text.
590	
591	\begin{figure}[ht]
592	\centering
593	\includegraphics[width=\linewidth]{figures/paper/fig_entropy_layers.pdf}
594	\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\pi_{0}$ (18 layers). SmolVLA and $\pi_{0}$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\pi_{0}$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.85$).}
595	\label{fig:entropy_layers}
596	\end{figure}
597	
598	
599	\section{Attention Entropy Measurement Details}
600	\label{app:entropy_details}
601	
602	We measure the attention entropy ratio as the normalized Shannon entropy of the attention weights that the action decoder assigns to vision token positions. For a model with $N$ vision tokens, the entropy ratio is:
603	\begin{equation}
604	H_{\text{ratio}} = \frac{-\sum_{i=1}^{N} \alpha_i \log \alpha_i}{\log N}
605	\end{equation}
606	where $\alpha_i$ is the attention weight on the $i$-th vision token. The ratio ranges from 0 (all attention on one token) to 1 (uniform attention).
607	
608	\paragraph{SmolVLA.} Measured on 2400 frames from LIBERO rollouts (overall entropy) and 260 frames across all 10 LIBERO-Object tasks (per-layer analysis across 16 layers). The mean per-layer entropy ratio is 0.95 (range: 0.93 to 0.98), consistent with near-uniform attention across all 128 vision tokens. The per-layer breakdown confirms this uniformity is not an averaging artifact:
609	\begin{itemize}[nosep]
610	    \item All 16 layers: 0.93--0.98 (spread 0.05)
611	    \item Minimum: layer 13 (0.93)
612	\end{itemize}
613	The flat profile across all processing depths confirms that pixel-shuffle tokens resist selective attention at every layer: because each token encodes 16 spatially contiguous patches via channel concatenation, all tokens are comparably information-dense, and the transformer has no basis for developing spatial selectivity.
614	
615	\paragraph{$\pi_{0}$.} Measured on 100 frames from LIBERO-Object (tasks 20--29) across all 18 layers of the Gemma-based PaliGemma backbone (512 vision tokens: 256 per image $\times$ 2 cameras). The mean suffix-to-vision entropy ratio is 0.959 (range: 0.931--0.983, std 0.013), near-uniform across all layers with no progressive sharpening:
616	\begin{itemize}[nosep]
617	    \item All 18 layers: 0.931--0.983 (spread 0.052)
618	    \item Minimum: 0.931; Maximum: 0.983
619	\end{itemize}
620	The flat entropy profile, combined with $\pi_{0}$'s extremely low CV (0.038), is consistent with its high tolerance to pruning: tokens carry near-equal importance and receive near-equal attention. Removing any subset approximates uniform spatial downsampling, preserving a proportional share of the visual field without disrupting the attention distribution.
621	
622	\paragraph{OpenVLA.} Measured on 250 frames from real LIBERO rollouts. The overall entropy ratio is 0.64. The layer-wise breakdown reveals progressive sharpening:
623	\begin{itemize}[nosep]
624	    \item Shallow layers (0--1): 0.95--0.98
625	    \item Early layers (2--4): 0.70--0.80
626	    \item Mid layers (12--20): 0.57--0.66
627	    \item Deep layers (24--30): 0.48--0.57 (minimum 0.48 at layer 29)
628	\end{itemize}
629	12.1\% of total attention weight falls on vision tokens overall, and within that fraction, the distribution is non-uniform in deeper layers. This progressive concentration indicates that OpenVLA has learned to selectively attend to task-relevant spatial locations, a pattern enabled by the MLP projector's preservation of per-patch spatial granularity.
630	
631	\paragraph{Measurement conditions.} All models are measured on real LIBERO rollout data: SmolVLA on 2400 frames (overall entropy) and 260 frames (per-layer analysis), $\pi_{0}$ on 100 frames from LIBERO-Object, OpenVLA on 250 frames from 50 episodes $\times$ 5 initial frames. Sample size differences reflect computational constraints (OpenVLA's 7B forward pass is substantially more expensive), but all measurements use task-relevant visual inputs. Entropy statistics show low variance across frames (std $< 0.02$ for OpenVLA, std $= 0.013$ for $\pi_{0}$).
632	
633	
634	\section{Connector Architecture and Token Independence}
635	\label{app:connector_analysis}
636	
637	The six-architecture taxonomy (Table~\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.
638	
639	Pixel-shuffle connectors create maximal entanglement. SmolVLA's $4 \times 4$ spatial folding packs 16 patches into each token by channel concatenation (CV $= 0.314$, the highest in our study). The folding is fixed and irreversible: removing one token eliminates an entire receptive field, and no downstream layer can recover the discarded content. Tokens encode non-overlapping spatial regions with heterogeneous visual content, making every token simultaneously essential and non-redundant.
640	
641	Pure linear projections produce the opposite extreme. $\pi_{0}$ maps each SigLIP patch through a single linear layer with no cross-token interaction, yielding CV $= 0.038$ and near-maximal entropy (0.959). Tokens are genuinely interchangeable: any subset preserves the same per-patch information density as any other subset of equal size.
642	
643	$\pi_{0.5}$ reveals a subtlety that $\pi_{0}$'s offline-only evaluation conceals. The $\times\!\sqrt{d}$ learned scaling preserves near-uniform norms (CV $= 0.055$), yet the closed-loop response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\% SR while L2 norm-based removal collapses to 33.4\%. The 36\,pp gap arises because L2 ranking in a low-CV distribution selects spatially clustered tokens whose slight norm variations correlate with image regions, destroying the spatial coverage that this architecture requires. Token position analysis confirms this mechanism: at $k{=}0.5$, L2 selection produces a single dominant cluster containing 100\% of retained tokens with only 78\% spatial coverage, whereas $k{=}0.7$ yields two clusters with 97\% in the largest and 100\% coverage (Appendix~\ref{app:token_position}).
644	
645	X-VLA's 12-layer BART encoder~\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\,pp), confirming it as an architectural property.
646	
647	MLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\% SR under 78\% pruning).
648	
649	Parameter count does not predict pruning tolerance. Ordered by scale: SmolVLA (450M) $<$ X-VLA (880M) $<$ $\pi_{0}$ (3.3B) $<$ $\pi_{0.5}$ (4B) $<$ OpenVLA (7B). Ordered by tolerance, SmolVLA remains the minimum, but $\pi_{0}$ and $\pi_{0.5}$ at 3.3--4B surpass OpenVLA at 7B, and X-VLA at 880M tolerates more aggressive pruning than OpenVLA. The CV spectrum (0.038 to 0.314) tracks connector complexity rather than parameter count across a 16$\times$ scale range.
650	
651	
652	\section{CV as Diagnostic Metric: Extended Analysis}
653	\label{app:cv_extended}
654	\label{sec:diagnostic}
655	
656	Token importance CV correlates with both the tolerance class of a model and the optimal pruning strategy, a correlation that emerges from a single mechanistic principle: CV measures the strength of the importance gradient that scoring methods can exploit.
657	
658	Low-CV models have near-uniform L2 norms. L2 norm ranking in this regime captures spatial artifacts (slight norm variations that correlate with image position) rather than genuine importance differences. Selection based on these artifacts concentrates retained tokens on spatially correlated patches, destroying the uniform coverage that low-CV architectures depend on. Random selection preserves spatial uniformity by construction. The mechanism predicts that the random-over-L2 advantage should grow as CV decreases, and the data in Table~\ref{tab:scaling_law} confirm this. On LIBERO-Object at $k{=}0.5$: $\Delta = +$36.0\,pp ($\pi_{0.5}$, CV $= 0.055$) $\to$ $+$26.9\,pp (X-VLA, CV $= 0.151$) $\to$ $-$3.4\,pp (OpenVLA, CV $= 0.215$). At $k{=}0.7$, the same ordering holds for $\pi_{0.5}$ and X-VLA ($+$22.2\,pp $\to$ $+$6.5\,pp); OpenVLA lacks a seed-matched pair at this ratio. The pattern persists across retention ratios, strengthening the interpretation from a coincidence at a single operating point to a structural property of the connector.
659	
660	On simple manipulation tasks (Object), high-CV models present a genuine importance gradient where L2 norm ranking aligns with actual information content. OpenVLA (CV $= 0.215$) sits near the crossover on Object: L2 outperforms random by 7.8\,pp at $k{=}0.9$ where the gradient is most exploitable, shrinking to 3.4\,pp at $k{=}0.5$ as the proportion of removed tokens exceeds the gradient's discriminative range. On complex multi-step tasks, this advantage diminishes or reverses: OpenVLA Long at $k{=}0.9$ shows Random outperforming L2 by 3.2\,pp (46.8\% vs.\ 43.6\%), as compositional tasks distribute critical information across tokens with heterogeneous norm profiles (Section~\ref{sec:analysis}).
661	
662	Extreme compression introduces a partial reversal. At $k{=}0.3$, $\pi_{0.5}$'s L2 selection achieves $53.2 \pm 3.1$\% SR (2 seeds) vs.\ random's 36.4\%. When very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. The V-shaped L2 curve is confirmed across seeds ($\sigma{=}0.1$\,pp at the $k{=}0.5$ valley). The reversal does not invalidate the CV diagnostic; it adds a budget-dependent interaction that future work should characterize across more models.
663	
664	Attention entropy provides a mechanistic supplement that resolves an apparent paradox. SmolVLA's entropy (0.952) is nearly as high as $\pi_{0}$'s (0.959), yet SmolVLA collapses under any pruning. SmolVLA's tokens are uniformly \emph{attended} but carry heterogeneous \emph{content} due to pixel-shuffle folding. Entropy captures how the LLM allocates attention across tokens; CV captures the input-side importance structure. Entropy alone cannot distinguish ``interchangeable'' ($\pi_{0}$) from ``entangled'' (SmolVLA), but CV separates them cleanly (0.038 vs.\ 0.314). OpenVLA's progressive entropy sharpening from 0.98 to 0.48 across layers (Figure~\ref{fig:entropy_layers}) is consistent with a graded regime where the LLM progressively concentrates on higher-importance tokens.
665	
666	
667	\section{Why Re-Encoding Succeeds: Extended Analysis}
668	\label{app:reencoding_analysis}
669	\label{sec:learned_compression}
670	
671	Learned re-encoding overcomes pixel-shuffle failure because it breaks the rigid spatial entanglement that the $4 \times 4$ folding creates. Cross-attention pooling integrates information across receptive field boundaries, redistributing content from the original 128 tokens into $M$ compressed representations no longer tied to fixed spatial blocks.
672	
673	The $M{=}128$ passthrough configuration suggests that re-encoding, not compression, is the key factor. Passthrough adds parameters without reducing token count, yet gains 13\,pp over the baseline (44.8\% $\to$ 58.0\%). The relatively stable M-curve ($M{=}16$: 56.9\% closely matches $M{=}128$: 58.0\%, within 1.1\,pp) shows that once entanglement is broken, token count is secondary.
674	
675	A parameter-matched MLP adapter (22.14M parameters) achieves 63.4\% SR at $M{=}32$, statistically indistinguishable from cross-attention ($p = 0.15$). Re-encoding through any learned mapping that integrates across token boundaries suffices; the attention mechanism itself is not essential.
676	
677	The remedy is specific to the pathology. VTR succeeds precisely on architectures whose rigid spatial entanglement demands learned redistribution; for token-independent connectors where each patch already carries self-contained information, re-encoding is unnecessary.
678	
679	
680	\section{Offline Metrics Underestimate Closed-Loop Failure}
681	\label{app:offline_disconnect}
682	\label{sec:metric_disconnect}
683	
684	Offline evaluation systematically underestimates pruning-induced failure because per-step averages dilute catastrophic single-step events that individually terminate episodes.
685	
686	X-VLA at $k{=}0.3$ demonstrates the gap directly: offline loss is 1.0014 (near-baseline), yet closed-loop SR drops to $22.0 \pm 0.9$\% ($-$77\,pp). A single gripper inversion (L2 $= 1.02$) is a minor perturbation in average action error but terminates an episode irreversibly. $\pi_{0}$'s offline loss at $k{=}0.1$ shows a 2.4\% \emph{improvement} over the unpruned baseline (offline metrics only; no closed-loop evaluation available), a result that closed-loop evaluation may contradict if similar catastrophic events occur at deployment frequency.
687	
688	$\pi_{0.5}$ adds a distinct form of evidence: the 36\,pp gap between L2 and random removal at $k{=}0.5$ is invisible to any offline metric that averages across token subsets or selection methods. Offline evaluation would report degradation for both methods; only closed-loop evaluation reveals that the \emph{choice} of pruning strategy, not just the pruning ratio, is associated with whether the model remains functional.
689	
690	
691	\section{Confounder Analysis}
692	\label{app:confounders}
693	
694	The six architectures span three connector families but differ simultaneously in LLM backbone (PaliGemma for $\pi_{0}$/$\pi_{0.5}$, Llama-2 for OpenVLA, Qwen2 for SmolVLA), preventing clean isolation of the connector effect from backbone differences. The $\pi_{0}$--OpenVLA comparison (same 256 SigLIP-based tokens, different connector, backbone, and encoder fusion strategy) provides the closest available approximation, but a matched-backbone experiment remains the ideal control. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation. Token count also varies across models (50 for X-VLA, 128 for SmolVLA, 256 for $\pi_{0}$/OpenVLA, 768 for $\pi_{0.5}$); the $\pi_{0}$--OpenVLA pair controls for this confounder within the CV analysis while still exhibiting the predicted CV-gap relationship.
695	
696	The spatial clustering hypothesis for L2 failure on low-CV models is confirmed by token position analysis (Appendix~\ref{app:token_position}).
697	
698	OpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\,pp across retention ratios regardless of random seed.
699	
700	
701	\section{Token Position Analysis}
702	\label{app:token_position}
703	
704	To validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\pi_{0.5}$ across three retention ratios.
705	
706	At $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\% of retained tokens in the largest cluster and 100\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\% SR at this retention ratio.
707	
708	At $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\% of retained tokens with only 78\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\% SR, the V-shape valley).
709	
710	At $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\% in the largest and 78\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \pm 3.1$\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.
711	
712	These results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.
713	
714	
715	\section{CV Scaling Law: Full Data}
716	\label{app:cv_scaling_table}
717	
718	\begin{table}[ht]
719	\centering
720	\small
721	\caption{L2 norm vs.\ random removal at two retention ratios. The gap $\Delta$(R$-$L2) scales monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy on simple tasks (see Section~\ref{sec:analysis} for task-dependent caveats). Data shown for LIBERO-Object; the monotonic ordering holds across retention ratios despite a 2$\times$ change in token budget.}
722	\label{tab:scaling_law}
723	\begin{tabular}{lccccc}
724	\toprule
725	Model & CV & Tokens & L2 SR (\%) & Random SR (\%) & $\Delta$(R$-$L2) \\
726	\midrule
727	\multicolumn{6}{l}{\textit{$k{=}0.5$ (50\% retention)}} \\
728	$\pi_{0.5}$ & 0.055 & 768 & 33.4 & \textbf{69.4} & $+$36.0 \\
729	X-VLA & 0.151 & 50 & 43.4$\pm$0.8 & \textbf{70.3}$\pm$0.9 & $+$26.9 \\
730	OpenVLA & 0.215 & 256 & \textbf{39.2} & 35.8 & $-$3.4 \\
731	\midrule
732	\multicolumn{6}{l}{\textit{$k{=}0.7$ (70\% retention)}} \\
733	$\pi_{0.5}$ & 0.055 & 768 & 55.0 & \textbf{74.0} & $+$19.0 \\
734	X-VLA & 0.151 & 50 & 58.6$\pm$0.4 & \textbf{65.1}$\pm$0.1 & $+$6.5 \\
735	OpenVLA\textsuperscript{$\dagger$} & 0.215 & 256 & -- & -- & -- \\
736	\bottomrule
737	\multicolumn{6}{l}{\footnotesize\textsuperscript{$\dagger$}$k{=}0.7$ omitted: no seed-matched L2/Random pair available.}
738	\end{tabular}
739	\end{table}
740	
741	
742	\section{CV-Strategy Interaction at Extreme Compression}
743	\label{app:cv_strategy_interaction}
744	
745	The monotonic CV-gap relationship (Table~\ref{tab:scaling_law}) holds at $k{=}0.5$ and $k{=}0.7$, but partially reverses at $k{=}0.3$ for $\pi_{0.5}$. At this extreme budget, L2 norm selection achieves $53.2 \pm 3.1$\% SR (2 seeds) vs.\ random's 36.4\%, favoring L2 by $\sim$17\,pp. The reversal is consistent across both seeds (seed42: 51.0\%, seed43: 55.4\%; Table~\ref{tab:pi05_l2_multiseed}).
746	
747	The mechanism is intuitive: when very few tokens remain ($k{=}0.3$ retains 230 of 768 tokens), even spatially clustered high-norm tokens provide more visual signal than a sparse random sample. At intermediate budgets ($k{=}0.5$, 384 tokens), random selection preserves enough spatial coverage to outperform L2's clustered selection; at extreme budgets, coverage from random selection becomes too sparse to be useful, and the concentrated signal from L2 selection dominates.
748	
749	The interaction implies that the optimal pruning strategy depends on both CV and the absolute token budget. For low-CV models, the crossover point between random-preferred and L2-preferred regimes lies between $k{=}0.3$ and $k{=}0.5$. Characterizing this crossover across additional models and budgets is left to future work.
750	
751	
752	\section{Inference Cost-Benefit Analysis}
753	\label{app:cost_benefit}
754	
755	The primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.
756	
757	End-to-end inference latency improves only modestly: 154.78\,ms at $M{=}32$ versus 164.33\,ms at full token count, a $1.06\times$ speedup (6\% reduction). At $M{=}64$: 156.16\,ms ($1.05\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (451.5M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.
758	
759	\paragraph{Comparison with the official checkpoint.}
760	VTR at $M = 32$ ($60.1 \pm 1.3$\% over 3 seeds) recovers from 0\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\%, CI [54.8\%, 63.4\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\ 64, single vs.\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\%, not matching the official baseline.
761	
762	\subsection{Attention-Based Scoring}
763	\label{app:attention_pruning}
764	
765	Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
766	
767	\begin{table}[h]
768	\centering
769	\small
770	\caption{X-VLA success rates (\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \textsuperscript{*}Best of three attention variants.}
771	\label{tab:attention_pruning}
772	\begin{tabular}{lccccc}
773	\toprule
774	Suite & attn\_last & attn\_mean & attn\_rollout & L2 & Random \\
775	\midrule
776	Object & \textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\
777	Spatial & 88.8 & 91.6 & \textbf{92.8} & 58.8 & 71.4 \\
778	Long & 90.2 & 94.0 & \textbf{94.8} & 45.0 & 61.6 \\
779	Goal & \multicolumn{3}{c}{\textbf{98.2}\textsuperscript{*}} & 59.0 & 67.2 \\
780	\bottomrule
781	\end{tabular}
782	\end{table}
783	
784	L2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\,pp (Goal) to $-$27.2\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\geq}$92.8\%), with rollout peaking at 94.8\% on Long (seed43 confirms $\Delta{\leq}$0.6\,pp). On Object, all three attention variants achieve ${\geq}$97.4\%, far exceeding both L2 (43.4\%) and random (70.6\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\%) but worst among attention methods on Spatial (88.8\%) and Long (90.2\%), while rollout shows the opposite pattern.
785	
786	The L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\,{=}\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\% $<$ $k{=}0.5$: 59.0\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\,{=}\,$31.5\,pp, range 0--92\%), while attention scoring keeps all tasks above 80\%. The double dissociation extends to $\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\pm$3\,pp). On Object, attention collapses to 37.8\% ($-$31.6\,pp vs.\ random's 69.4\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\times}10^{-6},\, 3.6{\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.
787	
788	\begin{table}[ht]
789	\centering
790	\small
791	\caption{$\pi_{0.5}$ attention vs.\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}
792	\label{tab:pi05_attention_crosssuite}
793	\begin{tabular}{lccc}
794	\toprule
795	Suite & Attention (\%) & Random (\%) & $\Delta$ (pp) \\
796	\midrule
797	Goal & 71.2 & 73.6 & $-$2.4 \\
798	Spatial & 72.6 & 71.6 & $+$1.0 \\
799	Long & 49.4 & 46.8 & $+$2.6 \\
800	Object & 37.8 & 69.4 & $-$31.6 \\
801	\bottomrule
802	\end{tabular}
803	\end{table} By contrast, $\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\,pp at $k{=}0.85$, decaying to $+$5.6\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\ref{fig:scoring_crossover}).
804	
805	\begin{table}[h]
806	\centering
807	\small
808	\caption{Scoring reversal summary: $\Delta$ vs.\ random at $k{=}0.5$, except \textsuperscript{*}Goal suite across $k \in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\ref{fig:scoring_crossover}.}
809	\label{tab:scoring_crossover_summary}
810	\begin{tabular}{lcc}
811	\toprule
812	& Attention & L2 norm \\
813	\midrule
814	Entangling (X-VLA) & Effective ($+$31\,pp) & Anti-inform.\ ($-$8 to $-$27\,pp) \\
815	Token-indep.\ ($\pi_{0.5}$) & Ineffective\textsuperscript{$\dagger$} ($-$2 to $-$30\,pp) & Effective\textsuperscript{*} ($+$35.2$\to$$+$5.6\,pp) \\
816	\bottomrule
817	\multicolumn{3}{l}{\footnotesize\textsuperscript{$\dagger$}Neutral on 3/4 suites ($\pm$3\,pp); harmful on Object ($-$30.4\,pp).}
818	\end{tabular}
819	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "171bd826-99c5-437d-8f77-c65470e2f32c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Extended Discussion}\n\\label{app:discussion}\n\n\\paragraph{Limitations (extended).}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}\nRandom selection on $\\pi_{0.5}$ Object collapses from 74.0\\% at $k{=}0.95$ to 9.0\\% at $k{=}0.9$, then recovers to 74.0\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\\%, Object~65.0\\%, Goal~60.4\\%), but Long drops to 35.0\\%, below its $k{=}0.5$ performance of 61.6\\% (Table~\\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\\pi_{0.5}$ Object drops to 5.6\\% at $k{=}0.85$ versus 69.4\\% at $k{=}0.5$ ($-$63.8\\,pp), more than double X-VLA Long's $-$26.6\\,pp. The V-shaped recovery at $k \\leq 0.7$ remains unexplained.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\\ $\\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\\%) but drops to 35.0\\% on Long (below $k{=}0.5$); $\\pi_{0.5}$ exhibits a severe disruption peak on Object.}\n\\label{tab:xvla_k085_crosssuite}\n\\begin{tabular}{lcccc}\n\\toprule\nSuite & X-VLA SR (\\%) & $\\Delta$ & $\\pi_{0.5}$ SR (\\%) & $\\Delta$ \\\\\n\\midrule\nObject & 65.0 & $-$34.2 & 3.6--5.6\\textsuperscript{$\\dagger$} & $-$93 to $-$95 \\\\\nGoal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\\\\nSpatial & 68.2 & $-$24.8 & --- & --- \\\\\nLong & 35.0 & $-$59.0 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Two seeds: seed42$\\,{=}\\,$5.6\\% (post-fix), seed43$\\,{=}\\,$3.6\\%. $\\Delta$ from respective baselines.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\\,pp on Goal and $-$47.0\\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n\n\n\\section{Cross-Suite Task Complexity Analysis}\n\\label{app:cross_suite_extended}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\\% ($-$1.6\\,pp from the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$28.2\\,pp from 98.4\\% baseline). Under random pruning at the same ratio, Object loses just 1.4\\,pp (97.8\\%) while Goal loses 27.8\\,pp (70.6\\%), a $20{\\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\% (L2) and 48.2\\% (random), a 47.0\\,pp loss with only 1.2\\,pp method gap, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. Two independent evaluations of the official HF checkpoint (59.2\\% and 57.2\\% baseline, within CI) confirm the cliff-edge across scoring methods.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol A (59.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol B (57.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\\\\nRandom & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task Breakdown Tables}\n\\label{app:per_task}\n\n\\subsection{SmolVLA Baseline Per-Task Results}\n\nTable~\\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\\ref{tab:smolvla_ablation}) produce 0\\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\\% already reported.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\\%.}\n\\label{tab:smolvla_baseline_pertask}\n\\begin{tabular}{lc}\n\\toprule\nTask & SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 22 \\\\\nbbq\\_sauce & 60 \\\\\nbutter & 42 \\\\\nchocolate\\_pudding & 38 \\\\\ncream\\_cheese & 58 \\\\\nketchup & 26 \\\\\nmilk & 62 \\\\\norange\\_juice & 38 \\\\\nsalad\\_dressing & 50 \\\\\ntomato\\_sauce & 52 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{44.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Official SmolVLA Checkpoint Per-Task Results}\n\nTable~\\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\\_libero). Under 50\\% random token removal, all tasks produce 0\\% SR, identical to the fine-tuned checkpoint results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\\%. Under 50\\% random pruning, all tasks collapse to 0\\%. An independent evaluation (protocol B) yields 57.2\\% baseline with identical cliff-edge (Table~\\ref{tab:smolvla_ablation}).}\n\\label{tab:smolvla_official_pertask}\n\\begin{tabular}{lcc}\n\\toprule\nTask & Baseline SR (\\%) & $k{=}0.5$ SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 64 & 0 \\\\\nbbq\\_sauce & 38 & 0 \\\\\nbutter & 78 & 0 \\\\\nchocolate\\_pudding & 90 & 0 \\\\\ncream\\_cheese & 40 & 0 \\\\\nketchup & 60 & 0 \\\\\nmilk & 52 & 0 \\\\\norange\\_juice & 80 & 0 \\\\\nsalad\\_dressing & 44 & 0 \\\\\ntomato\\_sauce & 46 & 0 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{59.2} & \\textbf{0.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Per-Task Results Under Pruning}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA per-task success rates (\\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\\%. Tasks requiring fine-grained discrimination (butter, cream\\_cheese) degrade earliest; visually distinctive targets (orange\\_juice, salad\\_dressing) are most resilient.}\n\\label{tab:openvla_pertask}\n\\begin{tabular}{lccccc}\n\\toprule\nTask & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\\\\n\\midrule\nalphabet\\_soup & 76 & 70 & 74 & 60 & 14 \\\\\nbbq\\_sauce & 38 & 28 & 46 & 44 & 30 \\\\\nbutter & 84 & 76 & 10 & 2 & 0 \\\\\nchocolate\\_pudding & 54 & 56 & 32 & 40 & 10 \\\\\ncream\\_cheese & 84 & 78 & 18 & 8 & 0 \\\\\nketchup & 82 & 70 & 68 & 50 & 30 \\\\\nmilk & 46 & 42 & 40 & 24 & 8 \\\\\norange\\_juice & 74 & 60 & 76 & 72 & 42 \\\\\nsalad\\_dressing & 64 & 54 & 64 & 36 & 64 \\\\\ntomato\\_sauce & 92 & 86 & 62 & 38 & 8 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{69.4} & \\textbf{62.0} & \\textbf{49.0} & \\textbf{37.4} & \\textbf{20.6} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Full Degradation Curve}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\\%. All confidence intervals are Wilson 95\\%.}\n\\label{tab:openvla_full}\n\\begin{tabular}{ccrr}\n\\toprule\n$k$ & Tokens Retained & SR (\\%) & Wilson 95\\% CI \\\\\n\\midrule\n1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\\\\n0.95 & 243 & 69.4 & [65.2, 73.3] \\\\\n0.90 & 230 & 62.0 & [57.7, 66.2] \\\\\n0.70 & 179 & 49.0 & [44.6, 53.4] \\\\\n0.50 & 128 & 37.4 & [33.3, 41.7] \\\\\n0.30 & 77 & 20.6 & [17.2, 24.4] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ L2 Norm Multi-Seed Consistency}\n\\label{app:pi05_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\\sigma{=}0.1$\\,pp at $k{=}0.5$). V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43).}\n\\label{tab:pi05_l2_multiseed}\n\\begin{tabular}{ccccc}\n\\toprule\n$k$ & Seed 42 (\\%) & Seed 43 (\\%) & Mean $\\pm$ Std & $\\Delta$ (pp) \\\\\n\\midrule\n0.70 & 55.0 & 57.8 & $56.4 \\pm 2.0$ & $+$2.8 \\\\\n0.50 & 33.4 & 33.6 & $33.5 \\pm 0.1$ & $+$0.2 \\\\\n0.30 & 51.0 & 55.4 & $53.2 \\pm 3.1$ & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ Cross-Suite Comparison}\n\\label{app:pi05_crosssuite}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\\%) and LIBERO-Spatial (baseline 97.2\\%), seed\\,42, 500 episodes each. Object random exhibits a deep cliff at $k \\in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\\leq 2.4$\\,pp difference at $k \\geq 0.85$).}\n\\label{tab:pi05_crosssuite}\n\\begin{tabular}{ccccc}\n\\toprule\n\\multirow{2}{*}{$k$} & \\multicolumn{2}{c}{LIBERO-Object (\\%)} & \\multicolumn{2}{c}{LIBERO-Spatial (\\%)} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & L2 Norm & Random & L2 Norm & Random \\\\\n\\midrule\n1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\\\\n0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\\\\n0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\\\\n0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\\\\n0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\\\\n0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\\\\n0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\\\\n0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_crosssuite.pdf}\n\\caption{$\\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \\in [0.85, 0.925]$ with 68\\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}\n\\label{fig:crosssuite}\n\\end{figure}\n\nThe random cliff at $k \\in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\\% ($k{=}0.95$) to 5.6\\% ($k{=}0.85$), whereas Spatial retains 58.4\\% at $k{=}0.85$ ($\\Delta{=}53$\\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\\% $>$ $k{=}0.9$: 54.6\\%, $\\Delta{=}5.8$\\,pp), but this is an order of magnitude smaller than Object's 68\\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.\n\nL2 norm selection is consistent across suites at high retention ($k \\geq 0.85$): Object and Spatial differ by $\\leq 2.4$\\,pp (Table~\\ref{tab:pi05_crosssuite}). At $k \\leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\\% at $k{=}0.5$; Spatial valley: 55.6\\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.\n\n\\subsection{Token Importance Spatial Distribution}\n\\label{app:token_heatmap}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_token_heatmap.pdf}\n\\caption{$\\pi_{0.5}$ token importance spatial distribution (16$\\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\\sim$265--267; edge rows 0, 14--15: norm $\\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\\ 21.87; CV${=}$0.059). The 33\\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}\n\\label{fig:token_heatmap}\n\\end{figure}\n\nToken importance heatmaps reveal that $\\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\\times$16 spatial grid after the $\\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.\n\nRandom removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \\to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.\n\n\\subsection{Hypergeometric Cliff Model}\n\\label{app:cliff_model}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_cliff_model.pdf}\n\\caption{Hypergeometric cliff model for $\\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\\ observed success rate (solid) across the cliff zone $k \\in [0.85, 0.95]$; RMSE${=}$0.025. (b)~$P(\\text{collapse})$ curves for Object ($C{=}91$, concentrated) and Spatial ($C \\approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}\n\\label{fig:cliff_model}\n\\end{figure}\n\nThe random cliff on $\\pi_{0.5}$ Object (Section~\\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \\in \\{0.9, 0.925, 0.95\\}$; all post-fix confirmed). When $\\lfloor N(1{-}k) \\rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\\mathrm{Hypergeometric}(N, C, \\lfloor N(1{-}k) \\rfloor)$. We define performance collapse as removing $\\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.\n\nThe model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\\text{collapse}){=}10\\%$ (cliff onset), $k{=}0.937$ where $P(\\text{collapse}){=}50\\%$ (midpoint), and $k{=}0.904$ where $P(\\text{collapse}){=}90\\%$ (near-complete collapse). The cliff width $\\Delta k \\approx 0.056$ between 10\\% and 90\\% collapse probability matches the observed transition from 74.0\\% SR ($k{=}0.95$) to 9.0\\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \\leq 0.7$, where success rate rebounds to 74.0\\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.\n\nThe cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\\% of the grid), creating a steep increase in $P(\\text{collapse} \\geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \\approx 5$ tokens, making the probability of simultaneously removing $\\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\\% at $k{=}0.85$ vs.\\ Object's 5.6\\%).\n\n\\subsection{OpenVLA Multi-Seed Consistency}\n\\label{app:openvla_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates (\\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\\ref{tab:main_results}) uses seed 42 for both L2 and random.}\n\\label{tab:openvla_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & Seed 7 (\\%) & Seed 43 (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.90 & 62.0 & 62.2 & $+$0.2 \\\\\n0.70 & 49.0 & 44.4 & $-$4.6 \\\\\n0.50 & 37.4 & 35.6 & $-$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L2 Norm vs.\\ Random Scoring on OpenVLA}\n\\label{app:l2_vs_random}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\\,{=}\\,$42; random uses seed$\\,{=}\\,$7. Main text (Table~\\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\\%, $k{=}0.5$: 35.8\\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\\% (L2 outperforms by 3.6\\,pp); same-seed at $k{=}0.7$ yields 44.4\\% (L2 outperforms by 5.4\\,pp). $\\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}\n\\label{tab:openvla_l2_vs_random}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm SR (\\%) & Random SR (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.95 & 70.6 & 69.4 & $+$1.2 \\\\\n0.90 & 70.6 & 62.0 & $+$8.6 \\\\\n0.70 & 49.8 & 49.0 & $+$0.8 \\\\\n0.50 & 39.2 & 37.4 & $+$1.8 \\\\\n0.30 & 25.0 & 20.6 & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{X-VLA Cliff Localization: Per-Task Analysis}\n\\label{app:xvla_cliff}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{X-VLA per-task success rates (\\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \\pm 0.7$\\% at $k{=}0.80$, $67.9 \\pm 0.3$\\% at $k{=}0.85$). Despite retaining \\emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\\,pp overall. Four tasks (\\textbf{bold}) suffer catastrophic interference ($\\Delta \\leq -50$\\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\\Delta| \\leq 10$\\,pp). Cross-seed variance is $\\leq 4$\\,pp per task.}\n\\label{tab:xvla_cliff_pertask}\n\\begin{tabular}{lccr}\n\\toprule\nTask & $k{=}0.80$ (\\%) & $k{=}0.85$ (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nalphabet\\_soup & 100.0 & 100.0 & 0 \\\\\nbbq\\_sauce & 85.0 & 87.0 & $+$2 \\\\\n\\textbf{butter} & \\textbf{57.0} & \\textbf{0.0} & $\\boldsymbol{-57}$ \\\\\n\\textbf{chocolate\\_pudding} & \\textbf{88.0} & \\textbf{35.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{cream\\_cheese} & \\textbf{98.0} & \\textbf{45.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{ketchup} & \\textbf{79.0} & \\textbf{27.0} & $\\boldsymbol{-52}$ \\\\\nmilk & 85.0 & 95.0 & $+$10 \\\\\norange\\_juice & 96.0 & 98.0 & $+$2 \\\\\nsalad\\_dressing & 100.0 & 100.0 & 0 \\\\\ntomato\\_sauce & 98.0 & 91.0 & $-$7 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{89.0} & \\textbf{67.9} & $\\boldsymbol{-21.1}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\\_pudding, cream\\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\\_soup, salad\\_dressing) feature distinctive objects or high-contrast targets.\n\n\\subsection{VTR Per-Task Comparison}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR per-task success rates on LIBERO-Object for $M \\in \\{32, 64, 128\\}$ (seed 42; 3-seed means are reported in Table~\\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\\%--61.6\\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}\n\\label{tab:smart_compress_pertask}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & $M{=}32$ (\\%) & $M{=}64$ (\\%) & $M{=}128$ (\\%) \\\\\n\\midrule\nalphabet\\_soup & 68 & 74 & 62 \\\\\nbbq\\_sauce & 46 & 56 & 34 \\\\\nbutter & 82 & 84 & 82 \\\\\nchocolate\\_pudding & 90 & 74 & 82 \\\\\ncream\\_cheese & 64 & 38 & 58 \\\\\nketchup & 66 & 64 & 62 \\\\\nmilk & 76 & 62 & 56 \\\\\norange\\_juice & 28 & 46 & 58 \\\\\nsalad\\_dressing & 60 & 64 & 54 \\\\\ntomato\\_sauce & 36 & 54 & 50 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{61.6} & \\textbf{61.6} & \\textbf{59.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{VTR Multi-Seed Results}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\\pm$ std reported.}\n\\label{tab:multi_seed}\n\\begin{tabular}{lccccr}\n\\toprule\n$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\\pm$ Std \\\\\n\\midrule\n32 & 61.6 & 59.2 & 59.6 & 60.1 $\\pm$ 1.3 \\\\\n64 & 61.6 & 60.0 & 64.4 & 62.0 $\\pm$ 2.3 \\\\\n96 & 52.6 & 58.2 & 52.8 & 54.5 $\\pm$ 3.2 \\\\\n128 & 59.8 & 54.0 & 60.2 & 58.0 $\\pm$ 3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Full Results}\n\\label{app:vtr_full}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (passthrough) within 1.1\\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}\n\\label{tab:vtr_results}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compression & SR (\\%) \\\\\n\\midrule\n\\textit{SmolVLA-Base (LoRA)} & 128 & 0\\% & 44.8 \\\\\n\\textit{SmolVLA official} & 128 & 0\\% & 59.2 \\\\\n\\textit{Baseline control (+100K steps)} & 128 & 0\\% & 45.0 \\\\\n\\textit{Hard pruning (any $k$)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 64 & 50\\% & \\textbf{62.0 $\\pm$ 2.2} \\\\\nCross-attn VTR & 96 & 25\\% & 54.5 $\\pm$ 3.2 \\\\\nCross-attn VTR & 128 & 0\\% & 58.0 $\\pm$ 3.5 \\\\\n\\midrule\nMLP adapter ($\\sim$22M) & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Full VTR Ablation}\n\\label{app:smart_compress_full}\n\nTable~\\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \\in \\{32, 64, 128\\}$ all achieve $\\sim$60\\% SR, exceeding the 44.8\\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5\\% compression) does performance decline modestly to 55.8\\%, still 11 points above baseline. The $M{=}96$ dip (mean 54.5\\% across three seeds, Table~\\ref{tab:multi_seed}) may reflect an intermediate bottleneck that introduces representational redundancy without the regularization benefit of stronger compression ($M{=}32$, $M{=}64$).\n\nTable~\\ref{tab:cross_suite} reports performance across task suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long. On LIBERO-Spatial, VTR achieves 53.2\\% SR (vs.\\ 0\\% under hard pruning); on LIBERO-Goal, 56.4\\% SR ($-6.6$pp from the 63.0\\% unpruned baseline, vs.\\ 0\\% under pruning). The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures even within the training distribution. Per-task results are in Table~\\ref{tab:smart_compress_pertask}.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Full VTR ablation on LIBERO-Object across five compression levels. $M{=}32$ and $M{=}64$ achieve similar SR ($\\sim$60\\%); $M{=}96$ shows a modest dip; the $M{=}128$ passthrough confirms the gain originates from re-encoding.}\n\\label{tab:smart_compress_full}\n\\begin{tabular}{lcccrr}\n\\toprule\nMethod & $M$ & Reduction & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 500 & [40.5, 49.2] \\\\\n\\textit{Extended training} & -- & -- & 45.0 & 500 & [40.7, 49.3] \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & 500+ & [0, 0.76] \\\\\n\\midrule\nVTR & 128 & 0\\% & 58.0 & 1500 & $\\pm$3.5 \\\\\nVTR & 96 & 25\\% & 52.6 & 500 & [48.2, 56.9] \\\\\nVTR & 64 & 50\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 32 & 75\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 16 & 87.5\\% & 55.8 & 500 & [51.4, 60.1] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $M{=}128$ reports mean $\\pm$ std over 3 seeds (500 episodes each). Other VTR rows report single seed (seed 42) with Wilson 95\\% CI. See Table~\\ref{tab:multi_seed} for full multi-seed results.}\n\\end{table}\n\n\n\\section{VTR Evaluation Across Task Suites}\n\\label{app:cross_suite}\n\nTable~\\ref{tab:cross_suite} reports the performance of VTR ($M{=}32$) across three LIBERO suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long (40 tasks, 1693 episodes total). On LIBERO-Goal, performance drops from 63.0\\% to 56.4\\% ($-6.6$pp). On LIBERO-Spatial, VTR achieves 53.2\\% SR, where the official SmolVLA checkpoint scores 43.8\\% and hard pruning yields near-zero (0.6\\%). While 53.2\\% nominally exceeds the official Spatial baseline, this difference concentrates in two of ten tasks (+44pp and +48pp respectively); the remaining eight tasks show a net difference of only +0.2pp. We therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline. The qualitative pattern (cliff-edge vulnerability and re-encoding recovery) extends across the three tested task structures within the training distribution. The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR ($M{=}32$) evaluation across LIBERO task suites. All suites are in-distribution (training covers Object, Spatial, Goal, Long). Hard pruning (any method, $k{=}0.50$) produces 0\\% or near-zero on all suites.}\n\\label{tab:cross_suite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Baseline (unpruned) & VTR $M{=}32$ & Hard Pruning $k{=}0.50$ \\\\\n\\midrule\nObject & 44.8\\% & 61.6\\% & 0\\% \\\\\nSpatial & 51.8\\% & 53.2\\% & 0.6\\% \\\\\nGoal & 63.0\\% & 56.4\\% & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Training Details}\n\\label{app:smart_compress_details}\n\nThe VTR module is a cross-attention pooling layer inserted between SmolVLA's pixel-shuffle vision connector and the Qwen2-0.5B language backbone. It consists of $M$ learned query vectors that attend over the 128 vision tokens through standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compressor adds 22.2M trainable parameters (approximately 5\\% of SmolVLA's 451.5M total). Training is end-to-end: compressor and VLA policy parameters are jointly optimized.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR training hyperparameters. All configurations ($M \\in \\{16, 32, 64, 96, 128\\}$) use identical procedures; only the number of query vectors differs.}\n\\label{tab:training_hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nHyperparameter & Value \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Model}} \\\\\n\\quad Base checkpoint & SmolVLA-Base (pretrained, before LIBERO fine-tuning) \\\\\n\\quad Compressor architecture & Cross-attention, 2 layers, 12 heads, dropout 0.1 \\\\\n\\quad Compressor parameters & 22.2M \\\\\n\\quad Total trainable parameters & 122.1M / 472.2M (25.85\\%) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Optimization}} \\\\\n\\quad Optimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.95$, weight decay $10^{-10}$) \\\\\n\\quad Learning rate & $10^{-4}$ \\\\\n\\quad Schedule & Linear warmup (1K steps, start factor 0.01) $\\to$ cosine \\\\\n\\quad & annealing ($\\eta_{\\min}{=}2.5 \\times 10^{-6}$) \\\\\n\\quad Max gradient norm & 10.0 \\\\\n\\quad Total training steps & 100,000 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Data \\& batching}} \\\\\n\\quad Dataset & HuggingFaceVLA/libero (40 tasks, 1693 episodes across \\\\\n\\quad & Object, Spatial, Goal, Long suites) \\\\\n\\quad Batch size & 4 (no gradient accumulation)$^\\dagger$ \\\\\n\\quad Num workers & 4 \\\\\n\\quad Eval interval & every 5K steps \\\\\n\\quad Checkpoint interval & every 1K steps \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Hardware \\& runtime}} \\\\\n\\quad Hardware & 1$\\times$ NVIDIA RTX 4090 D (24GB) \\\\\n\\quad Precision & fp32 (no mixed precision) \\\\\n\\quad Wall clock & $\\sim$6h 43m per configuration \\\\\n\\quad Training speed & 4.1 samples/sec \\\\\n\\quad Seed & 42 (seeds 43, 44 for multi-seed runs) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=32$ final metrics}} \\\\\n\\quad Train action loss & 0.11 \\\\\n\\quad Eval action loss & 0.052 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=64$ final metrics}} \\\\\n\\quad Train action loss & 0.045 \\\\\n\\quad Eval action loss & 0.062 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\\% vs.\\ 87.3\\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}\n\\end{table}\n\nThe loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\\ 0.045) but lower eval loss (0.052 vs.\\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\\ref{sec:metric_disconnect}).\n\n\\subsection{MLP Adapter Control}\n\\label{app:mlp_adapter}\n\nTo verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \\times d_{\\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\\% reduction), the MLP adapter achieves $63.4 \\pm 2.6$\\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \\pm 1.3$\\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.\n\n\n\\section{Offline Single-Step Action Error Analysis}\n\\label{app:offline_error}\n\nTable~\\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 distance of 0.414 from ground truth; under ACIS pruning at $k{=}0.50$, this increases to 1.391 ($3.4\\times$). The per-dimension breakdown of the pruned-vs-unpruned difference reveals that the gripper dimension dominates (L2 = 1.02), corresponding to complete gripper state inversion on many frames. Position errors (0.20--0.30 per axis) are moderate individually but compound across the 7-dimensional action space. These single-step errors are large enough to push the robot off-trajectory within a few steps, explaining why 0\\% of pruned episodes succeed in closed-loop evaluation despite moderate average offline metrics.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Single-step action prediction error (SmolVLA, $k{=}0.50$, ACIS, zero-mask, 200 LIBERO-Object evaluation frames). Pruning increases action error by $3.4\\times$ and introduces catastrophic gripper inversions.}\n\\label{tab:offline_action_error}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Unpruned & Pruned ($k{=}0.50$) \\\\\n\\midrule\nAction L2 vs.\\ ground truth & 0.414 & 1.391 \\\\\nPruned vs.\\ unpruned L2 & \\multicolumn{2}{c}{1.284} \\\\\nRelative action error & -- & 111.5\\% \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-dimension L2 (pruned vs.\\ unpruned)}} \\\\\n\\quad Position $(x, y, z)$ & -- & 0.20, 0.25, 0.30 \\\\\n\\quad Rotation $(r_x, r_y, r_z)$ & -- & 0.01, 0.02, 0.01 \\\\\n\\quad Gripper & -- & 1.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Supplementary Figures}\n\\label{app:supplementary_figures}\n\n% fig_pixel_shuffle moved to Section~\\ref{sec:pixel_shuffle} in main text.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_entropy_layers.pdf}\n\\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\\pi_{0}$ (18 layers). SmolVLA and $\\pi_{0}$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\\pi_{0}$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.85$).}\n\\label{fig:entropy_layers}\n\\end{figure}\n\n\n\\section{Attention Entropy Measurement Details}\n\\label{app:entropy_details}\n\nWe measure the attention entropy ratio as the normalized Shannon entropy of the attention weights that the action decoder assigns to vision token positions. For a model with $N$ vision tokens, the entropy ratio is:\n\\begin{equation}\nH_{\\text{ratio}} = \\frac{-\\sum_{i=1}^{N} \\alpha_i \\log \\alpha_i}{\\log N}\n\\end{equation}\nwhere $\\alpha_i$ is the attention weight on the $i$-th vision token. The ratio ranges from 0 (all attention on one token) to 1 (uniform attention).\n\n\\paragraph{SmolVLA.} Measured on 2400 frames from LIBERO rollouts (overall entropy) and 260 frames across all 10 LIBERO-Object tasks (per-layer analysis across 16 layers). The mean per-layer entropy ratio is 0.95 (range: 0.93 to 0.98), consistent with near-uniform attention across all 128 vision tokens. The per-layer breakdown confirms this uniformity is not an averaging artifact:\n\\begin{itemize}[nosep]\n    \\item All 16 layers: 0.93--0.98 (spread 0.05)\n    \\item Minimum: layer 13 (0.93)\n\\end{itemize}\nThe flat profile across all processing depths confirms that pixel-shuffle tokens resist selective attention at every layer: because each token encodes 16 spatially contiguous patches via channel concatenation, all tokens are comparably information-dense, and the transformer has no basis for developing spatial selectivity.\n\n\\paragraph{$\\pi_{0}$.} Measured on 100 frames from LIBERO-Object (tasks 20--29) across all 18 layers of the Gemma-based PaliGemma backbone (512 vision tokens: 256 per image $\\times$ 2 cameras). The mean suffix-to-vision entropy ratio is 0.959 (range: 0.931--0.983, std 0.013), near-uniform across all layers with no progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item All 18 layers: 0.931--0.983 (spread 0.052)\n    \\item Minimum: 0.931; Maximum: 0.983\n\\end{itemize}\nThe flat entropy profile, combined with $\\pi_{0}$'s extremely low CV (0.038), is consistent with its high tolerance to pruning: tokens carry near-equal importance and receive near-equal attention. Removing any subset approximates uniform spatial downsampling, preserving a proportional share of the visual field without disrupting the attention distribution.\n\n\\paragraph{OpenVLA.} Measured on 250 frames from real LIBERO rollouts. The overall entropy ratio is 0.64. The layer-wise breakdown reveals progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item Shallow layers (0--1): 0.95--0.98\n    \\item Early layers (2--4): 0.70--0.80\n    \\item Mid layers (12--20): 0.57--0.66\n    \\item Deep layers (24--30): 0.48--0.57 (minimum 0.48 at layer 29)\n\\end{itemize}\n12.1\\% of total attention weight falls on vision tokens overall, and within that fraction, the distribution is non-uniform in deeper layers. This progressive concentration indicates that OpenVLA has learned to selectively attend to task-relevant spatial locations, a pattern enabled by the MLP projector's preservation of per-patch spatial granularity.\n\n\\paragraph{Measurement conditions.} All models are measured on real LIBERO rollout data: SmolVLA on 2400 frames (overall entropy) and 260 frames (per-layer analysis), $\\pi_{0}$ on 100 frames from LIBERO-Object, OpenVLA on 250 frames from 50 episodes $\\times$ 5 initial frames. Sample size differences reflect computational constraints (OpenVLA's 7B forward pass is substantially more expensive), but all measurements use task-relevant visual inputs. Entropy statistics show low variance across frames (std $< 0.02$ for OpenVLA, std $= 0.013$ for $\\pi_{0}$).\n\n\n\\section{Connector Architecture and Token Independence}\n\\label{app:connector_analysis}\n\nThe six-architecture taxonomy (Table~\\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.\n\nPixel-shuffle connectors create maximal entanglement. SmolVLA's $4 \\times 4$ spatial folding packs 16 patches into each token by channel concatenation (CV $= 0.314$, the highest in our study). The folding is fixed and irreversible: removing one token eliminates an entire receptive field, and no downstream layer can recover the discarded content. Tokens encode non-overlapping spatial regions with heterogeneous visual content, making every token simultaneously essential and non-redundant.\n\nPure linear projections produce the opposite extreme. $\\pi_{0}$ maps each SigLIP patch through a single linear layer with no cross-token interaction, yielding CV $= 0.038$ and near-maximal entropy (0.959). Tokens are genuinely interchangeable: any subset preserves the same per-patch information density as any other subset of equal size.\n\n$\\pi_{0.5}$ reveals a subtlety that $\\pi_{0}$'s offline-only evaluation conceals. The $\\times\\!\\sqrt{d}$ learned scaling preserves near-uniform norms (CV $= 0.055$), yet the closed-loop response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR while L2 norm-based removal collapses to 33.4\\%. The 36\\,pp gap arises because L2 ranking in a low-CV distribution selects spatially clustered tokens whose slight norm variations correlate with image regions, destroying the spatial coverage that this architecture requires. Token position analysis confirms this mechanism: at $k{=}0.5$, L2 selection produces a single dominant cluster containing 100\\% of retained tokens with only 78\\% spatial coverage, whereas $k{=}0.7$ yields two clusters with 97\\% in the largest and 100\\% coverage (Appendix~\\ref{app:token_position}).\n\nX-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\n\nMLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\n\nParameter count does not predict pruning tolerance. Ordered by scale: SmolVLA (450M) $<$ X-VLA (880M) $<$ $\\pi_{0}$ (3.3B) $<$ $\\pi_{0.5}$ (4B) $<$ OpenVLA (7B). Ordered by tolerance, SmolVLA remains the minimum, but $\\pi_{0}$ and $\\pi_{0.5}$ at 3.3--4B surpass OpenVLA at 7B, and X-VLA at 880M tolerates more aggressive pruning than OpenVLA. The CV spectrum (0.038 to 0.314) tracks connector complexity rather than parameter count across a 16$\\times$ scale range.\n\n\n\\section{CV as Diagnostic Metric: Extended Analysis}\n\\label{app:cv_extended}\n\\label{sec:diagnostic}\n\nToken importance CV correlates with both the tolerance class of a model and the optimal pruning strategy, a correlation that emerges from a single mechanistic principle: CV measures the strength of the importance gradient that scoring methods can exploit.\n\nLow-CV models have near-uniform L2 norms. L2 norm ranking in this regime captures spatial artifacts (slight norm variations that correlate with image position) rather than genuine importance differences. Selection based on these artifacts concentrates retained tokens on spatially correlated patches, destroying the uniform coverage that low-CV architectures depend on. Random selection preserves spatial uniformity by construction. The mechanism predicts that the random-over-L2 advantage should grow as CV decreases, and the data in Table~\\ref{tab:scaling_law} confirm this. On LIBERO-Object at $k{=}0.5$: $\\Delta = +$36.0\\,pp ($\\pi_{0.5}$, CV $= 0.055$) $\\to$ $+$26.9\\,pp (X-VLA, CV $= 0.151$) $\\to$ $-$3.4\\,pp (OpenVLA, CV $= 0.215$). At $k{=}0.7$, the same ordering holds for $\\pi_{0.5}$ and X-VLA ($+$22.2\\,pp $\\to$ $+$6.5\\,pp); OpenVLA lacks a seed-matched pair at this ratio. The pattern persists across retention ratios, strengthening the interpretation from a coincidence at a single operating point to a structural property of the connector.\n\nOn simple manipulation tasks (Object), high-CV models present a genuine importance gradient where L2 norm ranking aligns with actual information content. OpenVLA (CV $= 0.215$) sits near the crossover on Object: L2 outperforms random by 7.8\\,pp at $k{=}0.9$ where the gradient is most exploitable, shrinking to 3.4\\,pp at $k{=}0.5$ as the proportion of removed tokens exceeds the gradient's discriminative range. On complex multi-step tasks, this advantage diminishes or reverses: OpenVLA Long at $k{=}0.9$ shows Random outperforming L2 by 3.2\\,pp (46.8\\% vs.\\ 43.6\\%), as compositional tasks distribute critical information across tokens with heterogeneous norm profiles (Section~\\ref{sec:analysis}).\n\nExtreme compression introduces a partial reversal. At $k{=}0.3$, $\\pi_{0.5}$'s L2 selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%. When very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. The V-shaped L2 curve is confirmed across seeds ($\\sigma{=}0.1$\\,pp at the $k{=}0.5$ valley). The reversal does not invalidate the CV diagnostic; it adds a budget-dependent interaction that future work should characterize across more models.\n\nAttention entropy provides a mechanistic supplement that resolves an apparent paradox. SmolVLA's entropy (0.952) is nearly as high as $\\pi_{0}$'s (0.959), yet SmolVLA collapses under any pruning. SmolVLA's tokens are uniformly \\emph{attended} but carry heterogeneous \\emph{content} due to pixel-shuffle folding. Entropy captures how the LLM allocates attention across tokens; CV captures the input-side importance structure. Entropy alone cannot distinguish ``interchangeable'' ($\\pi_{0}$) from ``entangled'' (SmolVLA), but CV separates them cleanly (0.038 vs.\\ 0.314). OpenVLA's progressive entropy sharpening from 0.98 to 0.48 across layers (Figure~\\ref{fig:entropy_layers}) is consistent with a graded regime where the LLM progressively concentrates on higher-importance tokens.\n\n\n\\section{Why Re-Encoding Succeeds: Extended Analysis}\n\\label{app:reencoding_analysis}\n\\label{sec:learned_compression}\n\nLearned re-encoding overcomes pixel-shuffle failure because it breaks the rigid spatial entanglement that the $4 \\times 4$ folding creates. Cross-attention pooling integrates information across receptive field boundaries, redistributing content from the original 128 tokens into $M$ compressed representations no longer tied to fixed spatial blocks.\n\nThe $M{=}128$ passthrough configuration suggests that re-encoding, not compression, is the key factor. Passthrough adds parameters without reducing token count, yet gains 13\\,pp over the baseline (44.8\\% $\\to$ 58.0\\%). The relatively stable M-curve ($M{=}16$: 56.9\\% closely matches $M{=}128$: 58.0\\%, within 1.1\\,pp) shows that once entanglement is broken, token count is secondary.\n\nA parameter-matched MLP adapter (22.14M parameters) achieves 63.4\\% SR at $M{=}32$, statistically indistinguishable from cross-attention ($p = 0.15$). Re-encoding through any learned mapping that integrates across token boundaries suffices; the attention mechanism itself is not essential.\n\nThe remedy is specific to the pathology. VTR succeeds precisely on architectures whose rigid spatial entanglement demands learned redistribution; for token-independent connectors where each patch already carries self-contained information, re-encoding is unnecessary.\n\n\n\\section{Offline Metrics Underestimate Closed-Loop Failure}\n\\label{app:offline_disconnect}\n\\label{sec:metric_disconnect}\n\nOffline evaluation systematically underestimates pruning-induced failure because per-step averages dilute catastrophic single-step events that individually terminate episodes.\n\nX-VLA at $k{=}0.3$ demonstrates the gap directly: offline loss is 1.0014 (near-baseline), yet closed-loop SR drops to $22.0 \\pm 0.9$\\% ($-$77\\,pp). A single gripper inversion (L2 $= 1.02$) is a minor perturbation in average action error but terminates an episode irreversibly. $\\pi_{0}$'s offline loss at $k{=}0.1$ shows a 2.4\\% \\emph{improvement} over the unpruned baseline (offline metrics only; no closed-loop evaluation available), a result that closed-loop evaluation may contradict if similar catastrophic events occur at deployment frequency.\n\n$\\pi_{0.5}$ adds a distinct form of evidence: the 36\\,pp gap between L2 and random removal at $k{=}0.5$ is invisible to any offline metric that averages across token subsets or selection methods. Offline evaluation would report degradation for both methods; only closed-loop evaluation reveals that the \\emph{choice} of pruning strategy, not just the pruning ratio, is associated with whether the model remains functional.\n\n\n\\section{Confounder Analysis}\n\\label{app:confounders}\n\nThe six architectures span three connector families but differ simultaneously in LLM backbone (PaliGemma for $\\pi_{0}$/$\\pi_{0.5}$, Llama-2 for OpenVLA, Qwen2 for SmolVLA), preventing clean isolation of the connector effect from backbone differences. The $\\pi_{0}$--OpenVLA comparison (same 256 SigLIP-based tokens, different connector, backbone, and encoder fusion strategy) provides the closest available approximation, but a matched-backbone experiment remains the ideal control. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation. Token count also varies across models (50 for X-VLA, 128 for SmolVLA, 256 for $\\pi_{0}$/OpenVLA, 768 for $\\pi_{0.5}$); the $\\pi_{0}$--OpenVLA pair controls for this confounder within the CV analysis while still exhibiting the predicted CV-gap relationship.\n\nThe spatial clustering hypothesis for L2 failure on low-CV models is confirmed by token position analysis (Appendix~\\ref{app:token_position}).\n\nOpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\\,pp across retention ratios regardless of random seed.\n\n\n\\section{Token Position Analysis}\n\\label{app:token_position}\n\nTo validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\\pi_{0.5}$ across three retention ratios.\n\nAt $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\\% of retained tokens in the largest cluster and 100\\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\\% SR at this retention ratio.\n\nAt $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\\% of retained tokens with only 78\\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\\% SR, the V-shape valley).\n\nAt $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\\% in the largest and 78\\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \\pm 3.1$\\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.\n\nThese results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.\n\n\n\\section{CV Scaling Law: Full Data}\n\\label{app:cv_scaling_table}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{L2 norm vs.\\ random removal at two retention ratios. The gap $\\Delta$(R$-$L2) scales monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy on simple tasks (see Section~\\ref{sec:analysis} for task-dependent caveats). Data shown for LIBERO-Object; the monotonic ordering holds across retention ratios despite a 2$\\times$ change in token budget.}\n\\label{tab:scaling_law}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & CV & Tokens & L2 SR (\\%) & Random SR (\\%) & $\\Delta$(R$-$L2) \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.5$ (50\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 33.4 & \\textbf{69.4} & $+$36.0 \\\\\nX-VLA & 0.151 & 50 & 43.4$\\pm$0.8 & \\textbf{70.3}$\\pm$0.9 & $+$26.9 \\\\\nOpenVLA & 0.215 & 256 & \\textbf{39.2} & 35.8 & $-$3.4 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.7$ (70\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 55.0 & \\textbf{74.0} & $+$19.0 \\\\\nX-VLA & 0.151 & 50 & 58.6$\\pm$0.4 & \\textbf{65.1}$\\pm$0.1 & $+$6.5 \\\\\nOpenVLA\\textsuperscript{$\\dagger$} & 0.215 & 256 & -- & -- & -- \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize\\textsuperscript{$\\dagger$}$k{=}0.7$ omitted: no seed-matched L2/Random pair available.}\n\\end{tabular}\n\\end{table}\n\n\n\\section{CV-Strategy Interaction at Extreme Compression}\n\\label{app:cv_strategy_interaction}\n\nThe monotonic CV-gap relationship (Table~\\ref{tab:scaling_law}) holds at $k{=}0.5$ and $k{=}0.7$, but partially reverses at $k{=}0.3$ for $\\pi_{0.5}$. At this extreme budget, L2 norm selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%, favoring L2 by $\\sim$17\\,pp. The reversal is consistent across both seeds (seed42: 51.0\\%, seed43: 55.4\\%; Table~\\ref{tab:pi05_l2_multiseed}).\n\nThe mechanism is intuitive: when very few tokens remain ($k{=}0.3$ retains 230 of 768 tokens), even spatially clustered high-norm tokens provide more visual signal than a sparse random sample. At intermediate budgets ($k{=}0.5$, 384 tokens), random selection preserves enough spatial coverage to outperform L2's clustered selection; at extreme budgets, coverage from random selection becomes too sparse to be useful, and the concentrated signal from L2 selection dominates.\n\nThe interaction implies that the optimal pruning strategy depends on both CV and the absolute token budget. For low-CV models, the crossover point between random-preferred and L2-preferred regimes lies between $k{=}0.3$ and $k{=}0.5$. Characterizing this crossover across additional models and budgets is left to future work.\n\n\n\\section{Inference Cost-Benefit Analysis}\n\\label{app:cost_benefit}\n\nThe primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.\n\nEnd-to-end inference latency improves only modestly: 154.78\\,ms at $M{=}32$ versus 164.33\\,ms at full token count, a $1.06\\times$ speedup (6\\% reduction). At $M{=}64$: 156.16\\,ms ($1.05\\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (451.5M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.\n\n\\paragraph{Comparison with the official checkpoint.}\nVTR at $M = 32$ ($60.1 \\pm 1.3$\\% over 3 seeds) recovers from 0\\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\\%, CI [54.8\\%, 63.4\\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \\approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\\ 64, single vs.\\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\\%, not matching the official baseline.\n\n\\subsection{Attention-Based Scoring}\n\\label{app:attention_pruning}\n\nTable~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{X-VLA success rates (\\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \\textsuperscript{*}Best of three attention variants.}\n\\label{tab:attention_pruning}\n\\begin{tabular}{lccccc}\n\\toprule\nSuite & attn\\_last & attn\\_mean & attn\\_rollout & L2 & Random \\\\\n\\midrule\nObject & \\textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\\\\nSpatial & 88.8 & 91.6 & \\textbf{92.8} & 58.8 & 71.4 \\\\\nLong & 90.2 & 94.0 & \\textbf{94.8} & 45.0 & 61.6 \\\\\nGoal & \\multicolumn{3}{c}{\\textbf{98.2}\\textsuperscript{*}} & 59.0 & 67.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nL2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\\,pp (Goal) to $-$27.2\\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\\geq}$92.8\\%), with rollout peaking at 94.8\\% on Long (seed43 confirms $\\Delta{\\leq}$0.6\\,pp). On Object, all three attention variants achieve ${\\geq}$97.4\\%, far exceeding both L2 (43.4\\%) and random (70.6\\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\\%) but worst among attention methods on Spatial (88.8\\%) and Long (90.2\\%), while rollout shows the opposite pattern.\n\nThe L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\\,{=}\\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\\% $<$ $k{=}0.5$: 59.0\\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\\,{=}\\,$31.5\\,pp, range 0--92\\%), while attention scoring keeps all tasks above 80\\%. The double dissociation extends to $\\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\\pm$3\\,pp). On Object, attention collapses to 37.8\\% ($-$31.6\\,pp vs.\\ random's 69.4\\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\\times}10^{-6},\\, 3.6{\\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ attention vs.\\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}\n\\label{tab:pi05_attention_crosssuite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Attention (\\%) & Random (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nGoal & 71.2 & 73.6 & $-$2.4 \\\\\nSpatial & 72.6 & 71.6 & $+$1.0 \\\\\nLong & 49.4 & 46.8 & $+$2.6 \\\\\nObject & 37.8 & 69.4 & $-$31.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table} By contrast, $\\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\\,pp at $k{=}0.85$, decaying to $+$5.6\\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\\ref{fig:scoring_crossover}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Scoring reversal summary: $\\Delta$ vs.\\ random at $k{=}0.5$, except \\textsuperscript{*}Goal suite across $k \\in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\\ref{fig:scoring_crossover}.}\n\\label{tab:scoring_crossover_summary}\n\\begin{tabular}{lcc}\n\\toprule\n& Attention & L2 norm \\\\\n\\midrule\nEntangling (X-VLA) & Effective ($+$31\\,pp) & Anti-inform.\\ ($-$8 to $-$27\\,pp) \\\\\nToken-indep.\\ ($\\pi_{0.5}$) & Ineffective\\textsuperscript{$\\dagger$} ($-$2 to $-$30\\,pp) & Effective\\textsuperscript{*} ($+$35.2$\\to$$+$5.6\\,pp) \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Neutral on 3/4 suites ($\\pm$3\\,pp); harmful on Object ($-$30.4\\,pp).}\n\\end{tabular}\n\\end{table}",
      "numLines": 819,
      "startLine": 1,
      "totalLines": 819
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
Now I need to read the paper_framing.md and check for any additional files. Let me also check what's in the artifacts/_project/paper/ directory for comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "9cd72482-9dd8-4ba6-8c78-afebeec16b28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011an8ZAocWFgJ8WRpNXLJt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42608,
      "cache_read_input_tokens": 26433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42608
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

_source line 34_

Now let me read the paper framing document and check for any remaining files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "7138ca4c-04a0-4302-9d86-a60bc97b305e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011an8ZAocWFgJ8WRpNXLJt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42608,
      "cache_read_input_tokens": 26433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42608
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

_source line 35_

<details open><summary>🔧 Tool call — Agent · `toolu_013B7RzQQq3QusUgTfHdx3Sg`</summary>

```json
{
  "description": "Find paper_framing.md",
  "subagent_type": "Explore",
  "prompt": "Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing \"paper_framing\" in the docs/ or artifacts/ directories. Report the full paths found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "02edd3c3-aa1b-4e1d-9471-c46995a83f9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011an8ZAocWFgJ8WRpNXLJt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42608,
      "cache_read_input_tokens": 26433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42608
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

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a831fdadb79810023",
  "tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "description": "Find paper_framing.md",
  "task_type": "local_agent",
  "prompt": "Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing \"paper_framing\" in the docs/ or artifacts/ directories. Report the full paths found.",
  "uuid": "8cbad8bb-d7f4-49ad-9954-b791082655ea",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

## Round 1

39 recorded events

### User

_source line 37 · 2026-05-27T04:30:11.342Z_

Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing "paper_framing" in the docs/ or artifacts/ directories. Report the full paths found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "2b9172d7-aafd-4116-8672-86df7ad1b001"
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01Dgob6uCX7Z5LnRPo3NS1qN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "d81ea5c6-a26b-4a30-b28f-80cffeec2e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011an8ZAocWFgJ8WRpNXLJt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42608,
      "cache_read_input_tokens": 26433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42608
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

_source line 39 · 2026-05-27T04:30:12.234Z_

<details><summary>↩ Tool result · `toolu_01Dgob6uCX7Z5LnRPo3NS1qN`</summary>

```text
1	% experimental_setup.tex -- Section 3: Experimental Setup
2	
3	\section{Experimental Setup}
4	\label{sec:experimental_setup}
5	
6	We design a controlled ablation study to test whether vision token reduction can preserve closed-loop VLA performance under any configuration. The study varies three independent axes (scoring function, retention ratio, pruning mechanism) around a shared baseline, using a lightweight learned scorer whose training does not alter the pretrained VLA weights. This section describes the scorer, the ablation design, and the evaluation protocol.
7	
8	\subsection{ACIS Importance Scorer}
9	\label{sec:acis_scorer}
10	
11	To select which vision tokens to prune, we train an Attention-weighted Cumulative Importance Score (ACIS) module that predicts a scalar importance score for each of the 256 projected vision tokens (Section~\ref{sec:smolvla_arch}). The ACIS scorer is a lightweight MLP with 3.46M parameters, constituting 0.77\% of SmolVLA's 451.5M total. At inference time, the scorer adds 0.24\% FLOPs overhead and 0.63\% wall-clock latency overhead relative to the unmodified forward pass.
12	
13	Training follows a Stage-1-only protocol: the ACIS scorer parameters are optimized while all VLA expert weights (vision encoder, MLP connector, LLM backbone, and action head) remain frozen. This separation is deliberate. Fine-tuning the full model during scorer training would conflate two effects: the model could learn to compensate for missing tokens rather than learning to score token importance. By freezing the expert, we ensure that the scorer must identify genuinely important tokens under the original model's representation, and that any subsequent failure cannot be attributed to training-induced degradation of action prediction.
14	
15	The scorer is trained with an importance margin loss that encourages a clear separation between the scores of retained tokens and those of pruned tokens. Given a retention ratio $k$, the loss penalizes configurations where the top-$k$ and bottom-$(1{-}k)$ token scores overlap, producing a well-separated ranking at convergence. At inference, tokens are sorted by ACIS score and the top-$k$ fraction is kept.
16	
17	\subsection{Ablation Design}
18	\label{sec:ablation_design}
19	
20	The ablation study varies three axes, each designed to rule out a specific failure hypothesis. Table~\ref{tab:ablation_matrix} in Section~\ref{sec:results} reports results for all conditions.
21	
22	\paragraph{Axis 1: Scoring function.}
23	We compare the learned ACIS scorer against uniform random token selection. If both produce the same outcome, the failure is not caused by the scorer selecting the wrong tokens.
24	
25	\paragraph{Axis 2: Retention ratio $k$.}
26	We test $k \in \{0.5, 0.7, 0.9\}$, corresponding to removing 50\%, 30\%, and 10\% of vision tokens respectively. If even $k{=}0.9$ (removing only 26 of 256 tokens) fails, the collapse is not caused by excessive information loss.
27	
28	\paragraph{Axis 3: Pruning mechanism.}
29	We implement three distinct mechanisms for handling pruned tokens:
30	\begin{itemize}[nosep,leftmargin=*]
31	  \item \textbf{Zero-mask}: pruned token embeddings are replaced with zero vectors. The sequence length is unchanged, but the model receives out-of-distribution (OOD) activation patterns at the masked positions.
32	  \item \textbf{True removal}: pruned tokens are physically removed from the input sequence. The LLM processes a shorter sequence with no OOD artifacts, but positional encodings shift for all tokens after the removal point.
33	  \item \textbf{Token merge}: following the bipartite matching strategy of ToMe~\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.
34	\end{itemize}
35	If all three mechanisms fail identically, the collapse is not an artifact of any particular masking strategy.
36	
37	The three axes are partially crossed. We run ACIS with zero-masking at all three retention ratios ($k{=}0.5, 0.7, 0.9$), random scoring with zero-masking at $k{=}0.5$, and ACIS at $k{=}0.5$ with true removal and merge. This yields six pruning conditions plus the unpruned baseline, covering the critical contrasts needed to isolate each failure hypothesis.
38	
39	\subsection{Evaluation Protocol}
40	\label{sec:eval_protocol}
41	
42	All conditions are evaluated on the three LIBERO suites described in Section~\ref{sec:libero_bench}: Object, Spatial, and Goal. Each suite contains 10 tasks, and we run 50 closed-loop episodes per task, producing 500 episodes per suite per condition.
43	
44	The baseline condition uses \emph{bypass mode}: the same trained model checkpoint with the ACIS scorer present but pruning disabled, so all 256 vision tokens pass through to the LLM. This ensures that any performance difference between the baseline and pruning conditions is caused by the token reduction itself, not by differences in model weights or the presence of the scorer module.
45	
46	We report Success Rate (SR) as the primary metric, defined as the fraction of episodes in which the robot completes the full task within the time limit. Because SR is a binary outcome measured over independent episodes, we compute Wilson score 95\% confidence intervals for all reported values. For reference, Wilson 95\% CI for 0 successes out of 500 episodes is $[0.0\%, 0.76\%]$, and for 224 out of 500 is $[40.5\%, 49.2\%]$. These intervals account for the discrete, bounded nature of binary proportions and provide tighter coverage than normal approximation intervals at extreme success rates.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "a8ede1dd-7af8-4039-8dff-b099d1e15480",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex",
      "content": "% experimental_setup.tex -- Section 3: Experimental Setup\n\n\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe design a controlled ablation study to test whether vision token reduction can preserve closed-loop VLA performance under any configuration. The study varies three independent axes (scoring function, retention ratio, pruning mechanism) around a shared baseline, using a lightweight learned scorer whose training does not alter the pretrained VLA weights. This section describes the scorer, the ablation design, and the evaluation protocol.\n\n\\subsection{ACIS Importance Scorer}\n\\label{sec:acis_scorer}\n\nTo select which vision tokens to prune, we train an Attention-weighted Cumulative Importance Score (ACIS) module that predicts a scalar importance score for each of the 256 projected vision tokens (Section~\\ref{sec:smolvla_arch}). The ACIS scorer is a lightweight MLP with 3.46M parameters, constituting 0.77\\% of SmolVLA's 451.5M total. At inference time, the scorer adds 0.24\\% FLOPs overhead and 0.63\\% wall-clock latency overhead relative to the unmodified forward pass.\n\nTraining follows a Stage-1-only protocol: the ACIS scorer parameters are optimized while all VLA expert weights (vision encoder, MLP connector, LLM backbone, and action head) remain frozen. This separation is deliberate. Fine-tuning the full model during scorer training would conflate two effects: the model could learn to compensate for missing tokens rather than learning to score token importance. By freezing the expert, we ensure that the scorer must identify genuinely important tokens under the original model's representation, and that any subsequent failure cannot be attributed to training-induced degradation of action prediction.\n\nThe scorer is trained with an importance margin loss that encourages a clear separation between the scores of retained tokens and those of pruned tokens. Given a retention ratio $k$, the loss penalizes configurations where the top-$k$ and bottom-$(1{-}k)$ token scores overlap, producing a well-separated ranking at convergence. At inference, tokens are sorted by ACIS score and the top-$k$ fraction is kept.\n\n\\subsection{Ablation Design}\n\\label{sec:ablation_design}\n\nThe ablation study varies three axes, each designed to rule out a specific failure hypothesis. Table~\\ref{tab:ablation_matrix} in Section~\\ref{sec:results} reports results for all conditions.\n\n\\paragraph{Axis 1: Scoring function.}\nWe compare the learned ACIS scorer against uniform random token selection. If both produce the same outcome, the failure is not caused by the scorer selecting the wrong tokens.\n\n\\paragraph{Axis 2: Retention ratio $k$.}\nWe test $k \\in \\{0.5, 0.7, 0.9\\}$, corresponding to removing 50\\%, 30\\%, and 10\\% of vision tokens respectively. If even $k{=}0.9$ (removing only 26 of 256 tokens) fails, the collapse is not caused by excessive information loss.\n\n\\paragraph{Axis 3: Pruning mechanism.}\nWe implement three distinct mechanisms for handling pruned tokens:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item \\textbf{Zero-mask}: pruned token embeddings are replaced with zero vectors. The sequence length is unchanged, but the model receives out-of-distribution (OOD) activation patterns at the masked positions.\n  \\item \\textbf{True removal}: pruned tokens are physically removed from the input sequence. The LLM processes a shorter sequence with no OOD artifacts, but positional encodings shift for all tokens after the removal point.\n  \\item \\textbf{Token merge}: following the bipartite matching strategy of ToMe~\\cite{bolya2023tome}, each pruned token is merged with its nearest retained neighbor by averaging their embeddings. Sequence length and total information content are both preserved.\n\\end{itemize}\nIf all three mechanisms fail identically, the collapse is not an artifact of any particular masking strategy.\n\nThe three axes are partially crossed. We run ACIS with zero-masking at all three retention ratios ($k{=}0.5, 0.7, 0.9$), random scoring with zero-masking at $k{=}0.5$, and ACIS at $k{=}0.5$ with true removal and merge. This yields six pruning conditions plus the unpruned baseline, covering the critical contrasts needed to isolate each failure hypothesis.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nAll conditions are evaluated on the three LIBERO suites described in Section~\\ref{sec:libero_bench}: Object, Spatial, and Goal. Each suite contains 10 tasks, and we run 50 closed-loop episodes per task, producing 500 episodes per suite per condition.\n\nThe baseline condition uses \\emph{bypass mode}: the same trained model checkpoint with the ACIS scorer present but pruning disabled, so all 256 vision tokens pass through to the LLM. This ensures that any performance difference between the baseline and pruning conditions is caused by the token reduction itself, not by differences in model weights or the presence of the scorer module.\n\nWe report Success Rate (SR) as the primary metric, defined as the fraction of episodes in which the robot completes the full task within the time limit. Because SR is a binary outcome measured over independent episodes, we compute Wilson score 95\\% confidence intervals for all reported values. For reference, Wilson 95\\% CI for 0 successes out of 500 episodes is $[0.0\\%, 0.76\\%]$, and for 224 out of 500 is $[40.5\\%, 49.2\\%]$. These intervals account for the discrete, bounded nature of binary proportions and provide tighter coverage than normal approximation intervals at extreme success rates.\n",
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01CYyRWc8GB7VK6D8n3RZWk9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "909a0778-c72f-431b-97e4-f2d67fd16428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011an8ZAocWFgJ8WRpNXLJt6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42608,
      "cache_read_input_tokens": 26433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42608
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

_source line 41 · 2026-05-27T04:30:12.723Z_

<details><summary>↩ Tool result · `toolu_01CYyRWc8GB7VK6D8n3RZWk9`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
5	
6	\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}
7	\label{sec:smolvla_results}
8	
9	SmolVLA~\cite{shukor2025smolvla} uses a pixel-shuffle vision connector that spatially rearranges patch embeddings before projecting them into the language model's embedding space. This operation creates inter-token spatial dependencies: each output token encodes information from a local grid of input patches. We hypothesize that this coupling makes the token sequence fragile under any form of pruning, since removing or masking a single token disrupts the spatial structure that downstream layers expect.
10	
11	\paragraph{Setup.}
12	We use a SmolVLA checkpoint fine-tuned on LIBERO-Object with the ACIS (Adaptive Contextual Importance Scoring) module attached but pruning disabled during training. The baseline (bypass mode) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result on LIBERO is 87.3\% SR, trained with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch size due to compute constraints, yielding a lower baseline. The relevant comparison is the relative change under pruning, not the absolute SR.} We then activate pruning under six configurations that vary three axes: scoring function (learned ACIS vs.\ random), retention ratio $k \in \{0.5, 0.7, 0.9\}$, and pruning mechanism (zero-masking, true token removal, token merging via ToMe~\cite{bolya2023tome}).
13	
14	\paragraph{All configurations collapse to 0\% SR.}
15	Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% success rate (Wilson CI upper bounds $\leq$1.26\%; see Table~\ref{tab:smolvla_ablation} for per-condition episode counts). Three observations make this result striking:
16	
17	\begin{enumerate}
18	    \item \textbf{Scoring-independent.} Random token selection performs identically to the learned ACIS scorer. The failure does not stem from poor importance estimation.
19	    \item \textbf{Ratio-independent.} Retaining 90\% of tokens ($k{=}0.9$, removing only 10\%) causes the same catastrophic failure as retaining 50\%. There is no graceful degradation at any operating point.
20	    \item \textbf{Mechanism-independent.} Zero-masking, true removal (sequence shortening), and token merging all produce identical 0\% SR. The failure is not an artifact of a particular implementation choice.
21	\end{enumerate}
22	
23	The convergence of all six conditions to 0\% SR, against a 44.8\% baseline, constitutes a cliff-edge failure pattern: performance does not degrade gradually but collapses entirely once any tokens are disturbed.
24	
25	\begin{table}[t]
26	\centering
27	\small
28	\caption{SmolVLA token pruning ablation on LIBERO-Object. All six pruning configurations collapse to 0\% SR regardless of scoring function, retention ratio, or mechanism. The baseline achieves 44.8\% with pruning disabled.}
29	\label{tab:smolvla_ablation}
30	\begin{tabular}{llccrr}
31	\toprule
32	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
33	\midrule
34	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
35	\midrule
36	ACIS & 0.5 & Zero-mask & 0.0 & 300 & [0, 1.26] \\
37	ACIS & 0.7 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
38	ACIS & 0.9 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
39	Random & 0.5 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
40	ACIS & 0.5 & True removal & 0.0 & 500 & [0, 0.80] \\
41	ACIS & 0.5 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	\paragraph{Geometric prior confirms the pattern.}
47	As additional evidence, we evaluate a non-learned geometric prior (Sobel edge-based scoring) at $k \in \{0.5, 0.7, 0.9\}$, all producing 0\% SR.\footnote{The geometric prior experiments use a different model checkpoint than the ACIS bypass baseline, so we report them separately from Table~\ref{tab:smolvla_ablation}. The qualitative conclusion is identical: any form of token disturbance causes complete failure.}
48	
49	\paragraph{Cross-suite confirmation.}
50	The cliff-edge pattern generalizes beyond LIBERO-Object. On LIBERO-Spatial (baseline 51.8\% SR) and LIBERO-Goal (baseline 63.0\% SR), ACIS pruning at $k{=}0.5$ with true removal produces 0\% SR in both suites (0/500 episodes each, CI [0\%, 0.76\%]). The failure is not task-specific but architectural.
51	
52	\paragraph{Interpretation.}
53	The pixel-shuffle connector in SmolVLA creates a structured token lattice where spatial adjacency carries semantic meaning. When any subset of tokens is removed, masked, or merged, the resulting sequence violates the implicit spatial contract that downstream transformer layers learned during pretraining. This interpretation aligns with the connector's design: pixel-shuffle compresses spatial resolution by interleaving channels, producing tokens whose meaning depends on their position within the original grid. We formalize this analysis in Section~\ref{sec:analysis}.
54	
55	
56	\subsection{OpenVLA: Graceful Degradation}
57	\label{sec:openvla_results}
58	
59	OpenVLA~\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.
60	
61	\paragraph{Setup.}
62	We evaluate the OpenVLA-7B checkpoint on LIBERO-Object under random token removal (true removal, no learned scorer). The baseline achieves 74.0\% SR (370/500 episodes). We apply pruning at $k{=}0.5$, retaining 50\% of vision tokens selected uniformly at random.
63	
64	\paragraph{Graded degradation instead of collapse.}
65	Table~\ref{tab:openvla_degradation} shows the results. At $k{=}0.5$, OpenVLA achieves 37.4\% SR (187/500), a relative drop of 49.5\% from baseline. This stands in sharp contrast to SmolVLA, where the same 50\% retention ratio produces 0\% SR. OpenVLA loses performance proportionally to the information removed, rather than collapsing catastrophically.
66	
67	\begin{table}[t]
68	\centering
69	\small
70	\caption{OpenVLA token pruning on LIBERO-Object. Unlike SmolVLA, OpenVLA shows graded degradation under random token removal, consistent with its MLP projector preserving per-token independence.}
71	\label{tab:openvla_degradation}
72	\begin{tabular}{cccrr}
73	\toprule
74	$k$ & SR (\%) & Relative Drop (\%) & Episodes & Wilson 95\% CI \\
75	\midrule
76	1.0 (baseline) & 74.0 & -- & 500 & [70.0, 77.7] \\
77	0.5 & 37.4 & 49.5 & 500 & [33.3, 41.7] \\
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	\paragraph{Per-task analysis reveals graded variance.}
83	The per-task breakdown at $k{=}0.5$ shows a wide range of success rates: from 2\% (butter) to 72\% (orange\_juice). Tasks involving visually distinct target objects (orange\_juice, alphabet\_soup at 60\%) retain higher success rates, while tasks requiring fine-grained visual discrimination among similar objects (butter at 2\%, cream\_cheese at 8\%) suffer the most. This graded, task-dependent degradation pattern confirms that OpenVLA retains partial visual information under pruning rather than losing all task-relevant signal.
84	
85	\paragraph{Architectural contrast.}
86	The divergence between SmolVLA and OpenVLA under identical pruning conditions (random selection, $k{=}0.5$, true removal) points to the vision connector as a key factor. Both models operate on the same benchmark with the same visual input, but they differ in two respects: the vision connector (pixel-shuffle vs.\ MLP projector) and model scale (0.5B vs.\ 7B parameters). The most salient architectural difference in the vision-to-language pathway is the connector design. SmolVLA drops from 44.8\% to 0\%; OpenVLA drops from 74.0\% to 37.4\%. We cannot fully disentangle connector design from model capacity in this comparison. However, SmolVLA's collapse at $k{=}0.9$ (removing only 13 of 128 tokens per camera) is difficult to attribute to limited capacity alone, since the model demonstrably solves these tasks at full token count. Section~\ref{sec:analysis} provides additional evidence from attention entropy distributions (0.98 vs.\ 0.62) that supports a connector-level explanation, and Section~\ref{sec:discussion} discusses the scale confound explicitly.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "84de1517-fba8-42aa-92f8-e617f6682324",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\\% confidence intervals.\n\n\\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}\n\\label{sec:smolvla_results}\n\nSmolVLA~\\cite{shukor2025smolvla} uses a pixel-shuffle vision connector that spatially rearranges patch embeddings before projecting them into the language model's embedding space. This operation creates inter-token spatial dependencies: each output token encodes information from a local grid of input patches. We hypothesize that this coupling makes the token sequence fragile under any form of pruning, since removing or masking a single token disrupts the spatial structure that downstream layers expect.\n\n\\paragraph{Setup.}\nWe use a SmolVLA checkpoint fine-tuned on LIBERO-Object with the ACIS (Adaptive Contextual Importance Scoring) module attached but pruning disabled during training. The baseline (bypass mode) achieves 44.8\\% SR (224/500, CI [40.5\\%, 49.2\\%]).\\footnote{The official SmolVLA result on LIBERO is 87.3\\% SR, trained with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch size due to compute constraints, yielding a lower baseline. The relevant comparison is the relative change under pruning, not the absolute SR.} We then activate pruning under six configurations that vary three axes: scoring function (learned ACIS vs.\\ random), retention ratio $k \\in \\{0.5, 0.7, 0.9\\}$, and pruning mechanism (zero-masking, true token removal, token merging via ToMe~\\cite{bolya2023tome}).\n\n\\paragraph{All configurations collapse to 0\\% SR.}\nTable~\\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\\% success rate (Wilson CI upper bounds $\\leq$1.26\\%; see Table~\\ref{tab:smolvla_ablation} for per-condition episode counts). Three observations make this result striking:\n\n\\begin{enumerate}\n    \\item \\textbf{Scoring-independent.} Random token selection performs identically to the learned ACIS scorer. The failure does not stem from poor importance estimation.\n    \\item \\textbf{Ratio-independent.} Retaining 90\\% of tokens ($k{=}0.9$, removing only 10\\%) causes the same catastrophic failure as retaining 50\\%. There is no graceful degradation at any operating point.\n    \\item \\textbf{Mechanism-independent.} Zero-masking, true removal (sequence shortening), and token merging all produce identical 0\\% SR. The failure is not an artifact of a particular implementation choice.\n\\end{enumerate}\n\nThe convergence of all six conditions to 0\\% SR, against a 44.8\\% baseline, constitutes a cliff-edge failure pattern: performance does not degrade gradually but collapses entirely once any tokens are disturbed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SmolVLA token pruning ablation on LIBERO-Object. All six pruning configurations collapse to 0\\% SR regardless of scoring function, retention ratio, or mechanism. The baseline achieves 44.8\\% with pruning disabled.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.5 & Zero-mask & 0.0 & 300 & [0, 1.26] \\\\\nACIS & 0.7 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.9 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.5 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.5 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.5 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Geometric prior confirms the pattern.}\nAs additional evidence, we evaluate a non-learned geometric prior (Sobel edge-based scoring) at $k \\in \\{0.5, 0.7, 0.9\\}$, all producing 0\\% SR.\\footnote{The geometric prior experiments use a different model checkpoint than the ACIS bypass baseline, so we report them separately from Table~\\ref{tab:smolvla_ablation}. The qualitative conclusion is identical: any form of token disturbance causes complete failure.}\n\n\\paragraph{Cross-suite confirmation.}\nThe cliff-edge pattern generalizes beyond LIBERO-Object. On LIBERO-Spatial (baseline 51.8\\% SR) and LIBERO-Goal (baseline 63.0\\% SR), ACIS pruning at $k{=}0.5$ with true removal produces 0\\% SR in both suites (0/500 episodes each, CI [0\\%, 0.76\\%]). The failure is not task-specific but architectural.\n\n\\paragraph{Interpretation.}\nThe pixel-shuffle connector in SmolVLA creates a structured token lattice where spatial adjacency carries semantic meaning. When any subset of tokens is removed, masked, or merged, the resulting sequence violates the implicit spatial contract that downstream transformer layers learned during pretraining. This interpretation aligns with the connector's design: pixel-shuffle compresses spatial resolution by interleaving channels, producing tokens whose meaning depends on their position within the original grid. We formalize this analysis in Section~\\ref{sec:analysis}.\n\n\n\\subsection{OpenVLA: Graceful Degradation}\n\\label{sec:openvla_results}\n\nOpenVLA~\\cite{kim2024openvla} uses a two-layer MLP projector to map vision encoder outputs (from DINOv2 and SigLIP~\\cite{zhai2023siglip}) into the Llama-2 language model's embedding space. Unlike pixel-shuffle, the MLP projector processes each patch token independently through a shared linear transformation. This design preserves per-token independence: the representation of one token carries no implicit dependency on neighboring tokens' presence.\n\n\\paragraph{Setup.}\nWe evaluate the OpenVLA-7B checkpoint on LIBERO-Object under random token removal (true removal, no learned scorer). The baseline achieves 74.0\\% SR (370/500 episodes). We apply pruning at $k{=}0.5$, retaining 50\\% of vision tokens selected uniformly at random.\n\n\\paragraph{Graded degradation instead of collapse.}\nTable~\\ref{tab:openvla_degradation} shows the results. At $k{=}0.5$, OpenVLA achieves 37.4\\% SR (187/500), a relative drop of 49.5\\% from baseline. This stands in sharp contrast to SmolVLA, where the same 50\\% retention ratio produces 0\\% SR. OpenVLA loses performance proportionally to the information removed, rather than collapsing catastrophically.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{OpenVLA token pruning on LIBERO-Object. Unlike SmolVLA, OpenVLA shows graded degradation under random token removal, consistent with its MLP projector preserving per-token independence.}\n\\label{tab:openvla_degradation}\n\\begin{tabular}{cccrr}\n\\toprule\n$k$ & SR (\\%) & Relative Drop (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n1.0 (baseline) & 74.0 & -- & 500 & [70.0, 77.7] \\\\\n0.5 & 37.4 & 49.5 & 500 & [33.3, 41.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Per-task analysis reveals graded variance.}\nThe per-task breakdown at $k{=}0.5$ shows a wide range of success rates: from 2\\% (butter) to 72\\% (orange\\_juice). Tasks involving visually distinct target objects (orange\\_juice, alphabet\\_soup at 60\\%) retain higher success rates, while tasks requiring fine-grained visual discrimination among similar objects (butter at 2\\%, cream\\_cheese at 8\\%) suffer the most. This graded, task-dependent degradation pattern confirms that OpenVLA retains partial visual information under pruning rather than losing all task-relevant signal.\n\n\\paragraph{Architectural contrast.}\nThe divergence between SmolVLA and OpenVLA under identical pruning conditions (random selection, $k{=}0.5$, true removal) points to the vision connector as a key factor. Both models operate on the same benchmark with the same visual input, but they differ in two respects: the vision connector (pixel-shuffle vs.\\ MLP projector) and model scale (0.5B vs.\\ 7B parameters). The most salient architectural difference in the vision-to-language pathway is the connector design. SmolVLA drops from 44.8\\% to 0\\%; OpenVLA drops from 74.0\\% to 37.4\\%. We cannot fully disentangle connector design from model capacity in this comparison. However, SmolVLA's collapse at $k{=}0.9$ (removing only 13 of 128 tokens per camera) is difficult to attribute to limited capacity alone, since the model demonstrably solves these tasks at full token count. Section~\\ref{sec:analysis} provides additional evidence from attention entropy distributions (0.98 vs.\\ 0.62) that supports a connector-level explanation, and Section~\\ref{sec:discussion} discusses the scale confound explicitly.\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a831fdadb79810023",
  "tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "description": "Finding **/paper_framing.md",
  "usage": {
    "total_tokens": 18437,
    "tool_uses": 1,
    "duration_ms": 1566
  },
  "last_tool_name": "Glob",
  "uuid": "1c1e69ee-7478-4af7-a7ac-7c4d56aa730d",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Glob · `toolu_01WpGPA4SBBFjpAHBAYksBnb`</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "8fba8db7-fc37-48a9-a77c-a8b98e193e32",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mp48nMiAEHDVg5mu2Z7bDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18428,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18428,
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

_source line 44 · 2026-05-27T04:30:13.014Z_

<details><summary>↩ Tool result · `toolu_01WpGPA4SBBFjpAHBAYksBnb`</summary>

```text
artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "65b6fcc4-a27e-41fd-8b2c-d0f3791f10d4"
}
```

</details>

---

### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a831fdadb79810023",
  "tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "description": "Finding **/docs/**/*paper_framing*",
  "usage": {
    "total_tokens": 18440,
    "tool_uses": 2,
    "duration_ms": 1999
  },
  "last_tool_name": "Glob",
  "uuid": "f4741b80-dc79-48f3-a9ce-d96fae2168c2",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Glob · `toolu_01UJBaHRtBokyt7ibh5rAF9Q`</summary>

```json
{
  "pattern": "**/docs/**/*paper_framing*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "a16c6a83-ff28-4253-bdd3-ff370f7910bb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mp48nMiAEHDVg5mu2Z7bDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18428,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18428,
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

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a831fdadb79810023",
  "tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "description": "Finding **/artifacts/**/*paper_framing*",
  "usage": {
    "total_tokens": 18443,
    "tool_uses": 3,
    "duration_ms": 2168
  },
  "last_tool_name": "Glob",
  "uuid": "c5405960-2d2e-4102-b9b4-a6dc02af193d",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Glob · `toolu_01G7J9gAH63ZcLAJ3AhCYjwy`</summary>

```json
{
  "pattern": "**/artifacts/**/*paper_framing*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "330f7de4-24c3-4678-a7a7-1ab6a578e8e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Mp48nMiAEHDVg5mu2Z7bDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18428,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18428,
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

_source line 49 · 2026-05-27T04:30:13.571Z_

<details><summary>↩ Tool result · `toolu_01UJBaHRtBokyt7ibh5rAF9Q`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "84b8d5d9-4fba-4267-b83b-1cf925881361"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-27T04:30:13.648Z_

<details><summary>↩ Tool result · `toolu_01G7J9gAH63ZcLAJ3AhCYjwy`</summary>

```text
artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "414abadb-30a4-4f45-a4cc-2fa21678b7d0"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a831fdadb79810023",
  "tool_use_id": "toolu_013B7RzQQq3QusUgTfHdx3Sg",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper_framing.md",
  "usage": {
    "total_tokens": 20133,
    "tool_uses": 3,
    "duration_ms": 7163
  },
  "uuid": "f0d732d4-4201-4667-bb9b-2d33efee399f",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9"
}
```

---

### Tool result

_source line 52 · 2026-05-27T04:30:18.507Z_

<details><summary>↩ Tool result · `toolu_013B7RzQQq3QusUgTfHdx3Sg`</summary>

```text
I found multiple paper_framing.md files in the project directory. Here are the full paths:

**Root level:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md`

**In artifacts/dream_reports:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md`

**No matching files found in docs/ directory.**

There are 10 total paper_framing.md files found: 1 at the root level and 9 within the artifacts/dream_reports directory structure across three dated dream report folders (best, median, and worst subdirectories for each).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "00bf6b6d-fab4-4064-949a-c2b3638d7208",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing \"paper_framing\" in the docs/ or artifacts/ directories. Report the full paths found.",
    "agentId": "a831fdadb79810023",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I found multiple paper_framing.md files in the project directory. Here are the full paths:\n\n**Root level:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md`\n\n**In artifacts/dream_reports:**\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md`\n- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md`\n\n**No matching files found in docs/ directory.**\n\nThere are 10 total paper_framing.md files found: 1 at the root level and 9 within the artifacts/dream_reports directory structure across three dated dream report folders (best, median, and worst subdirectories for each)."
      }
    ],
    "totalDurationMs": 7165,
    "totalTokens": 20797,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 18428,
      "output_tokens": 677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 677,
          "cache_read_input_tokens": 18428,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1685,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 3,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Let me read the root-level paper_framing.md to check the core claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "7c88d4ce-5d76-413a-8618-d0f7292f20be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X3erA9by1LX4iwJSMto5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4260,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 54_

Let me read the root-level paper_framing.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "a630b698-5da8-4f29-9c27-6729bf564d21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X3erA9by1LX4iwJSMto5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4260,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_017QoiScCiAWRWkiB5aKbUcr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "6d24e88c-77b6-41ca-9832-a5ac50911753",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X3erA9by1LX4iwJSMto5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4260,
      "cache_creation_input_tokens": 1097,
      "cache_read_input_tokens": 69041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1097
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

_source line 56 · 2026-05-27T04:30:23.206Z_

<details><summary>↩ Tool result · `toolu_017QoiScCiAWRWkiB5aKbUcr`</summary>

```text
1	# Paper Framing — importance_margin_vla_compress
2	
3	## Target Venue
4	- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)
5	- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)
6	
7	## Title (working)
8	"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
9	
10	## Core Insight
11	
12	**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA "threshold-graded" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:
13	
14	**Axis 1 — Token Coupling (connector architecture):**
15	| Type | Connectors | CV Range | Mechanism |
16	|------|-----------|----------|-----------|
17	| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |
18	| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |
19	
20	**Axis 2 — Task Complexity:**
21	| Level | Suites | Characteristics |
22	|-------|--------|----------------|
23	| **Simple** | Object, Spatial | Single-step, pruning impact contained |
24	| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |
25	
26	**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:
27	- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)
28	- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance
29	- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen
30	- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification
31	
32	**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.
33	
34	_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_
35	- **Linear projection** (π0 3.3B, π0.5 4B): **"Uniformly Critical" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:
36	  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline
37	  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95
38	  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**
39	  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor
40	  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone
41	  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change
42	  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:
43	  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation
44	  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)
45	  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**
46	  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage
47	  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:
48	  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR
49	  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)
50	  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.
51	  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.
52	  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.
53	  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**
54	  Baseline: 97.2%. Random pruning profile:
55	  | k | Object | Spatial | Δ | Pattern |
56	  |---|--------|---------|---|---------|
57	  | 0.95 | 71.1% | deploying | — | — |
58	  | 0.925 | 28.8% (2-seed) | — | — | — |
59	  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |
60	  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |
61	  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |
62	  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |
63	  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |
64	  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.
65	  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.
66	  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.
67	  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).
68	  **Paper value:** strengthens "uniformly critical" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.
69	- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**
70	- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).
71	- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.
72	
73	Key controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.
74	
75	Learned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.
76	
77	## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)
78	**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)
79	
80	**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.
81	
82	**Method contribution**: Diagnose-then-Compress framework:
83	- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)
84	  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass
85	  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314
86	  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.
87	  - **Key discovery**: X-VLA "linear projection" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)
88	  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):
89	    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant
90	    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)
91	    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate
92	    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded
93	    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic
94	  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.
95	  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)
96	  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative
97	- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression
98	- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)
99	- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as "VTR ceiling depends on connector type" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.
100	
101	**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.
102	
103	**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.
104	
105	## Core Claims (5 claims, expanded from 4)
106	
107	### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)
108	Pruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:
109	
110	**Axis 1 — Token Coupling (connector determines base sensitivity):**
111	- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation
112	- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades
113	
114	**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**
115	- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)
116	- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)
117	- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)
118	
119	**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)
120	
121	**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:
122	1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity
123	2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification
124	3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks
125	
126	🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**
127	
128	Both L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:
129	
130	- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.
131	  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)
132	  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2
133	  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)
134	  - k=0.3: L2norm=25.0%, random=pending (re-running)
135	
136	- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:
137	  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)
138	  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)
139	  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)
140	  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.
141	  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.
142	  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.
143	  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.
144	
145	- **SmolVLA**: all methods = 0% at all k values → trivially method independent.
146	
147	**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.
148	
149	**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.
150	
151	**Paper narrative upgrade**: From "connector determines compressibility" to "connector determines both compressibility AND optimal compression strategy." This is a significantly stronger and more novel contribution.
152	
153	**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.
154	
155	### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement
156	SmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.
157	
158	**Evidence**:
159	- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic
160	- k=0.9 (remove 13/128 tokens) = 0% SR
161	- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%
162	- Attention entropy ratio 0.952 (near-uniform, TV=0.05)
163	- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%
164	- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])
165	
166	### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)
167	Pure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): "robust-then-cliff" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.
168	
169	**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):
170	- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]
171	- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]
172	- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]
173	- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]
174	- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)
175	- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff
176	- k=0.2: **~4.0%** (-96pp) — near-zero
177	- k=0.1: **~0.0%** (-100pp) — complete failure
178	✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).
179	
180	**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:
181	- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)
182	- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)
183	- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.
184	
185	**Random pruning comparison (D127-D130, D132 REVERSAL)**:
186	- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression
187	- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.
188	- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both
189	- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).
190	- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.
191	- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.
192	- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.
193	- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 "sweet spot" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.
194	- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.
195	- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.
196	- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**
197	
198	**Cross-suite generalization (D117, updated with full results)**:
199	- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)
200	- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)
201	- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.
202	
203	**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:
204	
205	X-VLA pruning curve comparison across suites:
206	
207	| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |
208	|-------|-------|-------|-----|-------|----------|----------|
209	| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |
210	| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |
211	| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |
212	
213	**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:
214	- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline
215	- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim
216	
217	**Per-task non-monotonic pruning remains valid (selected tasks)**:
218	
219	| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |
220	|------|-------|-------|-------|---------|
221	| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |
222	| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |
223	| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |
224	| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |
225	| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |
226	
227	- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation
228	- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.
229	- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal
230	
231	**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.
232	
233	**Task-level analysis (Spatial, k=0.5 vs baseline)**:
234	- Robust (Δ≤10pp): T0 "between plate and ramekin" (-4pp), T4 "in top drawer" (-2pp) — global spatial / unambiguous target
235	- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed
236	- Catastrophic (Δ>40pp): T5 "on ramekin" (-48pp, 0%), T9 "on cabinet" (-58pp), T7 "on stove" (-64pp), T1 "next to ramekin" (-78pp)
237	- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness
238	
239	**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all "pick bowl...") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.
240	
241	**Paper framing upgrade (Reviewer suggestion, agreed)**:
242	- From "connector determines pruning tolerance" → "pruning sensitivity = f(connector_type, task_semantics)"
243	- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)
244	- Task semantic structure determines degradation *severity* within that class
245	- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)
246	- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)
247	- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.
248	
249	π0 evidence:
250	- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983
251	- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])
252	- Importance CV: π0 = 0.038 (lowest in spectrum)
253	
254	**Key insight**: "Linear projection" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.
255	
256	### Claim 3b: MLP Projector → Graded Degradation
257	Multi-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.
258	
259	**Evidence** (OpenVLA 6-point degradation curve):
260	- k=1.0: 74.0% (baseline)
261	- k=0.95: 69.4% (-6% relative)
262	- k=0.9: 62.0% (-16% relative)
263	- k=0.7: 49.0% (-34% relative)
264	- k=0.5: 37.4% (-49% relative)
265	- k=0.3: 20.6% (-72% relative)
266	- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)
267	- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.
268	- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head
269	- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)
270	
271	### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)
272	**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from "re-encoding boost" to "near-lossless compression recovery".**
273	
274	Two independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).
275	
276	**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.
277	
278	**Evidence** (all confirmed):
279	
280	Cross-attention re-encoding (M sweep, 3-seed where available):
281	| M | Compression | SR (3-seed mean±std) | Seeds | Notes |
282	|---|------------|-----|-----|-----|
283	| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |
284	| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |
285	| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |
286	| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |
287	| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |
288	
289	MLP adapter control (M=32, ~22.14M params, 3-seed):
290	| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |
291	|---|---|---|-----|-----|-----|
292	| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |
293	| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |
294	
295	Two-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)
296	
297	### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)
298	Token importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**
299	
300	**k=0.5 (main table):**
301	| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |
302	|-------|-----|--------|-------------|-------------|----------|
303	| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |
304	| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |
305	| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |
306	
307	**k=0.7 (second validation, D142):**
308	| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |
309	|-------|-----|--------|-------------|-------------|----------|
310	| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |
311	| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |
312	| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |
313	⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)
314	⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)
315	
316	³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp
317	⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp
318	
319	¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.
320	
321	✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.
322	
323	**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**
324	
325	| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |
326	|-------|-----|--------|-----------|-------------|-------------|----------|
327	| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |
328	| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |
329	| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |
330	
331	⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1
332	⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1
333	
334	At k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).
335	
336	**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.
337	
338	**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:
339	| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |
340	|---|-----------------|-----------------|-----------|---------------|
341	| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |
342	| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |
343	| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |
344	
345	¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.
346	
347	**V-shape fully confirmed (2 seeds, both methods)**:
348	- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable
349	- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%
350	- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)
351	- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed
352	- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.
353	
354	**Mechanism confirmed by token position visualization (D141)**:
355	- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage
356	- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration
357	- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity
358	
359	The non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.
360	
361	**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: "CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models."
362	
363	**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.
364	
365	**Evidence** (Reviewer-verified, D132 PASS):
366	
367	X-VLA vs OpenVLA full comparison:
368	
369	| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |
370	|---|---|---|---|---|
371	| | L2norm | Random | L2norm | Random |
372	| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |
373	| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |
374	| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |
375	| 0.8 | 89.0% | 89.4% (≈0) | — | — |
376	| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |
377	| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |
378	| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |
379	
380	¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.
381	² OpenVLA random k=0.3 result file missing, re-running on westd-38929.
382	³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.
383	
384	**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**
385	
386	| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |
387	|------|---------|--------|--------|------------|---------|
388	| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |
389	| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |
390	| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |
391	| T7 milk | 100% | 38% | 38% | 82% | +44 |
392	| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |
393	| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |
394	
395	L2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.
396	T6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.
397	T4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.
398	
399	**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.
400	
401	**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the "slightly larger" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.
402	
403	**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).
404	
405	**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.
406	
407	**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.
408	
409	## Story Spine
410	
411	**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.
412	
413	**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that "token pruning works or fails uniformly" is untested. The critical architectural factor determining prunability is unknown.
414	
415	**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:
416	- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219
417	- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314
418	CV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).
419	
420	**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.
421	
422	**Headline result**: "Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%."
423	
424	## Paper Structure (7-model version)
425	
426	1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework
427	2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis
428	3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics
429	4. **Main Results**:
430	   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)
431	   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)
432	   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)
433	   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)
434	   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)
435	   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)
436	   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)
437	   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)
438	5. **Analysis**:
439	   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)
440	   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)
441	   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)
442	6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work
443	7. **Conclusion**: 5 claims summary
444	
445	## Anticipated Reviewer Concerns
446	
447	### RC1: Only 2 models → **FULLY ADDRESSED**
448	**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.
449	
450	### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**
451	**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies "larger models are more robust" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.
452	
453	### RC3: Why not test SmolVLA without pixel_shuffle?
454	**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.
455	
456	### RC4: Smart compression — is re-encoding or compression the mechanism?
457	**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.
458	
459	### RC5: Relationship to VLA-IAP
460	**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.
461	
462	### RC6: Is this just "different models behave differently"?
463	**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.
464	
465	### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**
466	**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.
467	
468	## All Experimental Evidence (confirmed)
469	
470	### SmolVLA Cliff-Edge
471	- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%
472	- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%
473	- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%
474	- Attention entropy: 0.952 (flat, TV=0.05)
475	- Official checkpoint Object: 59.2% → 0% at k=0.5
476	- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites
477	- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.
478	
479	### OpenVLA Degradation Curve
480	- k=1.0: 74.0% (370/500)
481	- k=0.95: 69.4% (-6% relative)
482	- k=0.9: 62.0% (-16% relative)
483	- k=0.7: 49.0% (245/500, -34% relative)
484	- k=0.5: 37.4% (187/500, -49% relative)
485	- k=0.3: 20.6% (103/500, -72% relative)
486	- Entropy: 0.639 (progressive sharpening, TV=0.50)
487	
488	### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)
489	| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |
490	|-------|-----------|--------|---------------|---------------|-------|
491	| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |
492	| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |
493	| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |
494	| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |
495	| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |
496	| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |
497	
498	Diagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):
499	| Model | Connector (effective) | Entropy | CV | Pruning Behavior |
500	|-------|----------------------|---------|------|------------------|
501	| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |
502	| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |
503	| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |
504	| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |
505	| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |
506	| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |
507	
508	Key insights (updated with 7-model data):
509	1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.
510	2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.
511	3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT "high entropy" like π0.
512	4. **Effective connector complexity matters more than nominal label**: X-VLA is "linear proj" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss "effective connector" = projection + any intermediate processing.
513	5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure
514	6. Framing: CV captures "degree of non-linear mixing in the vision-to-LLM pathway." More mixing → higher CV → less tolerant of pruning.
515	
516	### Smart Compress (Learned Re-encoding)
517	Cross-attention (VTC) M sweep (3-seed where available):
518	- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128
519	- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)
520	- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)
521	- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance
522	- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control
523	- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.
524	
525	MLP adapter (M=32, 3-seed):
526	- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)
527	- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3
528	- t-test p≈0.15, no significant difference — confirms architecture-independence
529	
530	### D109: VTR on OpenVLA (MLP projector) — FAILED
531	- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)
532	- Failure mode: model outputs identical action every timestep (severe overfitting)
533	- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.
534	- VTC-only M=32 and M=64 training in progress on westd-41074:2-3
535	
536	### Cross-Suite VTR Generalization (SmolVLA)
537	- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)
538	- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)
539	- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.
540	- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.
541	
542	### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)
543	- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence
544	- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real
545	- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms
546	- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values
547	- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)
548	
549	### Supplementary
550	- Inference latency: 6% speedup at M=32
551	- KV-cache: 75% memory reduction at M=32
552	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "d536d75a-55c9-4764-957d-60b1a105779e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md",
      "content": "# Paper Framing — importance_margin_vla_compress\n\n## Target Venue\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\n\n## Title (working)\n\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\"\n\n## Core Insight\n\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \"threshold-graded\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\n\n**Axis 1 — Token Coupling (connector architecture):**\n| Type | Connectors | CV Range | Mechanism |\n|------|-----------|----------|-----------|\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\n\n**Axis 2 — Task Complexity:**\n| Level | Suites | Characteristics |\n|-------|--------|----------------|\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\n\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\n\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\n\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\n- **Linear projection** (π0 3.3B, π0.5 4B): **\"Uniformly Critical\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\n  Baseline: 97.2%. Random pruning profile:\n  | k | Object | Spatial | Δ | Pattern |\n  |---|--------|---------|---|---------|\n  | 0.95 | 71.1% | deploying | — | — |\n  | 0.925 | 28.8% (2-seed) | — | — | — |\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\n  **Paper value:** strengthens \"uniformly critical\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\n\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\n\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\n\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\n\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\n\n**Method contribution**: Diagnose-then-Compress framework:\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\n  - **Key discovery**: X-VLA \"linear projection\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \"VTR ceiling depends on connector type\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\n\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\n\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\n\n## Core Claims (5 claims, expanded from 4)\n\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\n\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\n\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\n\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\n\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\n\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\n\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\n\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\n\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\n\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\n\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\n\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\n\n**Paper narrative upgrade**: From \"connector determines compressibility\" to \"connector determines both compressibility AND optimal compression strategy.\" This is a significantly stronger and more novel contribution.\n\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\n\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\n\n**Evidence**:\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\n- k=0.9 (remove 13/128 tokens) = 0% SR\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\n\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \"robust-then-cliff\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\n\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\n- k=0.2: **~4.0%** (-96pp) — near-zero\n- k=0.1: **~0.0%** (-100pp) — complete failure\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\n\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\n\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \"sweet spot\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\n\n**Cross-suite generalization (D117, updated with full results)**:\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\n\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\n\nX-VLA pruning curve comparison across suites:\n\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\n|-------|-------|-------|-----|-------|----------|----------|\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\n\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\n\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\n\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\n|------|-------|-------|-------|---------|\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\n\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\n\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\n\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\n- Robust (Δ≤10pp): T0 \"between plate and ramekin\" (-4pp), T4 \"in top drawer\" (-2pp) — global spatial / unambiguous target\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\n- Catastrophic (Δ>40pp): T5 \"on ramekin\" (-48pp, 0%), T9 \"on cabinet\" (-58pp), T7 \"on stove\" (-64pp), T1 \"next to ramekin\" (-78pp)\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\n\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \"pick bowl...\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\n\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\n- From \"connector determines pruning tolerance\" → \"pruning sensitivity = f(connector_type, task_semantics)\"\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\n- Task semantic structure determines degradation *severity* within that class\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\n\nπ0 evidence:\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\n- Importance CV: π0 = 0.038 (lowest in spectrum)\n\n**Key insight**: \"Linear projection\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\n\n### Claim 3b: MLP Projector → Graded Degradation\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\n\n**Evidence** (OpenVLA 6-point degradation curve):\n- k=1.0: 74.0% (baseline)\n- k=0.95: 69.4% (-6% relative)\n- k=0.9: 62.0% (-16% relative)\n- k=0.7: 49.0% (-34% relative)\n- k=0.5: 37.4% (-49% relative)\n- k=0.3: 20.6% (-72% relative)\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\n\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \"re-encoding boost\" to \"near-lossless compression recovery\".**\n\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\n\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\n\n**Evidence** (all confirmed):\n\nCross-attention re-encoding (M sweep, 3-seed where available):\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\n|---|------------|-----|-----|-----|\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\n\nMLP adapter control (M=32, ~22.14M params, 3-seed):\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\n|---|---|---|-----|-----|-----|\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\n\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\n\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\n\n**k=0.5 (main table):**\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\n|-------|-----|--------|-------------|-------------|----------|\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\n\n**k=0.7 (second validation, D142):**\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\n|-------|-----|--------|-------------|-------------|----------|\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\n\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\n\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\n\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\n\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\n\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\n|-------|-----|--------|-----------|-------------|-------------|----------|\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\n\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\n\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\n\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\n\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\n|---|-----------------|-----------------|-----------|---------------|\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\n\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\n\n**V-shape fully confirmed (2 seeds, both methods)**:\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\n\n**Mechanism confirmed by token position visualization (D141)**:\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\n\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\n\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\"\n\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\n\n**Evidence** (Reviewer-verified, D132 PASS):\n\nX-VLA vs OpenVLA full comparison:\n\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\n|---|---|---|---|---|\n| | L2norm | Random | L2norm | Random |\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\n\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\n\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\n\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\n|------|---------|--------|--------|------------|---------|\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\n\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\n\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\n\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \"slightly larger\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\n\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\n\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\n\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\n\n## Story Spine\n\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\n\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \"token pruning works or fails uniformly\" is untested. The critical architectural factor determining prunability is unknown.\n\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\n\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\n\n**Headline result**: \"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\"\n\n## Paper Structure (7-model version)\n\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\n4. **Main Results**:\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\n5. **Analysis**:\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\n7. **Conclusion**: 5 claims summary\n\n## Anticipated Reviewer Concerns\n\n### RC1: Only 2 models → **FULLY ADDRESSED**\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\n\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \"larger models are more robust\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\n\n### RC3: Why not test SmolVLA without pixel_shuffle?\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\n\n### RC4: Smart compression — is re-encoding or compression the mechanism?\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\n\n### RC5: Relationship to VLA-IAP\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\n\n### RC6: Is this just \"different models behave differently\"?\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\n\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\n\n## All Experimental Evidence (confirmed)\n\n### SmolVLA Cliff-Edge\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\n- Attention entropy: 0.952 (flat, TV=0.05)\n- Official checkpoint Object: 59.2% → 0% at k=0.5\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\n\n### OpenVLA Degradation Curve\n- k=1.0: 74.0% (370/500)\n- k=0.95: 69.4% (-6% relative)\n- k=0.9: 62.0% (-16% relative)\n- k=0.7: 49.0% (245/500, -34% relative)\n- k=0.5: 37.4% (187/500, -49% relative)\n- k=0.3: 20.6% (103/500, -72% relative)\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\n\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\n|-------|-----------|--------|---------------|---------------|-------|\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\n\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\n|-------|----------------------|---------|------|------------------|\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\n\nKey insights (updated with 7-model data):\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \"high entropy\" like π0.\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \"linear proj\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \"effective connector\" = projection + any intermediate processing.\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\n6. Framing: CV captures \"degree of non-linear mixing in the vision-to-LLM pathway.\" More mixing → higher CV → less tolerant of pruning.\n\n### Smart Compress (Learned Re-encoding)\nCross-attention (VTC) M sweep (3-seed where available):\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\n\nMLP adapter (M=32, 3-seed):\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\n- t-test p≈0.15, no significant difference — confirms architecture-independence\n\n### D109: VTR on OpenVLA (MLP projector) — FAILED\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\n- Failure mode: model outputs identical action every timestep (severe overfitting)\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\n\n### Cross-Suite VTR Generalization (SmolVLA)\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\n\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\n\n### Supplementary\n- Inference latency: 6% speedup at M=32\n- KV-cache: 75% memory reduction at M=32\n",
      "numLines": 552,
      "startLine": 1,
      "totalLines": 552
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
Now I have a comprehensive view of the paper. Let me also check the X-VLA attention results, the figures directory, and references file to complete the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "c7816ad2-6ae7-4538-a596-6cd4112e72ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfksue3DbLJxYPerNwop4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24613,
      "cache_read_input_tokens": 70138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24613
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

_source line 58_

Now let me check if figures and references exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "e1fba26f-0109-481c-92e2-414fd6f5c5a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfksue3DbLJxYPerNwop4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24613,
      "cache_read_input_tokens": 70138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24613
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

_source line 59_

<details open><summary>🔧 Tool call — Glob · `toolu_01T53v9vWAJDDd2GH5Y5qG7x`</summary>

```json
{
  "pattern": "docs/paper/figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "b7fefee3-cda1-4f9e-a16e-ed2c3c000cc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfksue3DbLJxYPerNwop4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24613,
      "cache_read_input_tokens": 70138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24613
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

_source line 60 · 2026-05-27T04:30:28.643Z_

<details><summary>↩ Tool result · `toolu_01T53v9vWAJDDd2GH5Y5qG7x`</summary>

```text
docs/paper/figures/paper/fig_attention_heatmap.pdf
docs/paper/figures/paper/fig_action_divergence.pdf
docs/paper/figures/paper/fig_token_heatmap.pdf
docs/paper/figures/paper/fig_entropy_layers.pdf
docs/paper/figures/paper/fig_pixel_shuffle.pdf
docs/paper/figures/paper/fig_crosssuite.pdf
docs/paper/figures/paper/fig_cliff_model.pdf
docs/paper/figures/paper/fig_degradation_curve.pdf
docs/paper/figures/paper/fig_cliff_edge.pdf
docs/paper/figures/paper/fig_compression_curve.pdf
docs/paper/figures/paper/fig_architecture.pdf
docs/paper/figures/paper/fig_architecture_v2.pdf
docs/paper/figures/paper/fig_method_gap.pdf
docs/paper/figures/paper/fig_hero_overview.pdf
docs/paper/figures/paper/fig_scoring_crossover.pdf
docs/paper/figures/paper/fig_pruning_overview.pdf
docs/paper/figures/paper/fig_teaser.pdf
docs/paper/figures/paper/fig_openvla_sweep.pdf
docs/paper/figures/paper/fig_cliff_highlight.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "1f12ee54-d3ff-4fdd-93d2-2fa1aaf0b992",
  "tool_use_result": {
    "filenames": [
      "docs/paper/figures/paper/fig_attention_heatmap.pdf",
      "docs/paper/figures/paper/fig_action_divergence.pdf",
      "docs/paper/figures/paper/fig_token_heatmap.pdf",
      "docs/paper/figures/paper/fig_entropy_layers.pdf",
      "docs/paper/figures/paper/fig_pixel_shuffle.pdf",
      "docs/paper/figures/paper/fig_crosssuite.pdf",
      "docs/paper/figures/paper/fig_cliff_model.pdf",
      "docs/paper/figures/paper/fig_degradation_curve.pdf",
      "docs/paper/figures/paper/fig_cliff_edge.pdf",
      "docs/paper/figures/paper/fig_compression_curve.pdf",
      "docs/paper/figures/paper/fig_architecture.pdf",
      "docs/paper/figures/paper/fig_architecture_v2.pdf",
      "docs/paper/figures/paper/fig_method_gap.pdf",
      "docs/paper/figures/paper/fig_hero_overview.pdf",
      "docs/paper/figures/paper/fig_scoring_crossover.pdf",
      "docs/paper/figures/paper/fig_pruning_overview.pdf",
      "docs/paper/figures/paper/fig_teaser.pdf",
      "docs/paper/figures/paper/fig_openvla_sweep.pdf",
      "docs/paper/figures/paper/fig_cliff_highlight.pdf"
    ],
    "durationMs": 57,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Glob · `toolu_01L4ePnMe5b4k8fzyyTh68XW`</summary>

```json
{
  "pattern": "docs/paper/references.*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "68b2e785-cb44-4b09-adbb-a46e5e3d7c82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfksue3DbLJxYPerNwop4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24613,
      "cache_read_input_tokens": 70138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24613
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

_source line 62 · 2026-05-27T04:30:29.617Z_

<details><summary>↩ Tool result · `toolu_01L4ePnMe5b4k8fzyyTh68XW`</summary>

```text
docs/paper/references.bib.prev
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "315aac8a-5118-4a51-b86b-4cbe46399dc9",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib.prev",
      "docs/paper/references.bib"
    ],
    "durationMs": 64,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_01JuHjASHao5CChVA98szfQ4`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/ 2>/dev/null | head -30; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib 2>/dev/null || echo \"NO_REFERENCES_BIB\"",
  "description": "Check figures and references files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "62bedb91-041b-4515-a3f1-679d40f3c123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfksue3DbLJxYPerNwop4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24613,
      "cache_read_input_tokens": 70138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24613
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

_source line 64 · 2026-05-27T04:30:31.183Z_

<details><summary>↩ Tool result · `toolu_01JuHjASHao5CChVA98szfQ4`</summary>

```text
total 9384
drwxr-xr-x 6 ubuntu ubuntu    4096 May 27 00:27 .
drwxr-xr-x 3 ubuntu ubuntu    4096 May 20 12:35 ..
-rw-r--r-- 1 ubuntu ubuntu   38360 May 18 18:12 fig_action_divergence.pdf
-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture.pdf
-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture_v2.pdf
-rw-r--r-- 1 ubuntu ubuntu  266752 May 22 14:21 fig_architecture_v2.png
-rw-r--r-- 1 ubuntu ubuntu   34161 May 18 18:12 fig_attention_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu   34985 May 22 14:18 fig_cliff_edge.pdf
-rw-r--r-- 1 ubuntu ubuntu   33320 May 27 00:27 fig_cliff_highlight.pdf
-rw-r--r-- 1 ubuntu ubuntu  154046 May 27 00:27 fig_cliff_highlight.png
-rw-r--r-- 1 ubuntu ubuntu   37441 May 22 14:14 fig_cliff_model.pdf
-rw-r--r-- 1 ubuntu ubuntu   26360 May 22 14:18 fig_compression_curve.pdf
-rw-r--r-- 1 ubuntu ubuntu   31132 May 22 14:14 fig_crosssuite.pdf
-rw-r--r-- 1 ubuntu ubuntu  197642 May 22 14:14 fig_crosssuite.png
-rw-r--r-- 1 ubuntu ubuntu   57361 May 22 14:18 fig_degradation_curve.pdf
-rw-r--r-- 1 ubuntu ubuntu  336496 May 22 14:18 fig_degradation_curve.png
-rw-r--r-- 1 ubuntu ubuntu  175091 May 22 13:34 fig_degradation_overview.png
-rw-r--r-- 1 ubuntu ubuntu   30759 May 22 14:14 fig_entropy_layers.pdf
-rw-r--r-- 1 ubuntu ubuntu  151216 May 22 14:14 fig_entropy_layers.png
-rw-r--r-- 1 ubuntu ubuntu  311633 May 24 08:26 fig_hero_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu 2126046 May 24 08:26 fig_hero_overview.png
-rw-r--r-- 1 ubuntu ubuntu 3768870 May 24 08:26 fig_hero_overview_real.png
-rw-r--r-- 1 ubuntu ubuntu   22092 May 24 02:11 fig_method_gap.pdf
-rw-r--r-- 1 ubuntu ubuntu  100579 May 24 02:11 fig_method_gap.png
-rw-r--r-- 1 ubuntu ubuntu   29272 May 26 21:33 fig_openvla_sweep.pdf
-rw-r--r-- 1 ubuntu ubuntu  226567 May 26 21:33 fig_openvla_sweep.png
-rw-r--r-- 1 ubuntu ubuntu   23434 May 22 14:14 fig_pixel_shuffle.pdf
-rw-r--r-- 1 ubuntu ubuntu   35105 May 25 20:08 fig_pruning_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu  128828 May 25 20:08 fig_pruning_overview.png
---
-rw-r--r-- 1 ubuntu ubuntu 23480 May 24 02:30 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "f26aafac-69d5-45ea-977f-766080ffdac6",
  "tool_use_result": {
    "stdout": "total 9384\ndrwxr-xr-x 6 ubuntu ubuntu    4096 May 27 00:27 .\ndrwxr-xr-x 3 ubuntu ubuntu    4096 May 20 12:35 ..\n-rw-r--r-- 1 ubuntu ubuntu   38360 May 18 18:12 fig_action_divergence.pdf\n-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture.pdf\n-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture_v2.pdf\n-rw-r--r-- 1 ubuntu ubuntu  266752 May 22 14:21 fig_architecture_v2.png\n-rw-r--r-- 1 ubuntu ubuntu   34161 May 18 18:12 fig_attention_heatmap.pdf\n-rw-r--r-- 1 ubuntu ubuntu   34985 May 22 14:18 fig_cliff_edge.pdf\n-rw-r--r-- 1 ubuntu ubuntu   33320 May 27 00:27 fig_cliff_highlight.pdf\n-rw-r--r-- 1 ubuntu ubuntu  154046 May 27 00:27 fig_cliff_highlight.png\n-rw-r--r-- 1 ubuntu ubuntu   37441 May 22 14:14 fig_cliff_model.pdf\n-rw-r--r-- 1 ubuntu ubuntu   26360 May 22 14:18 fig_compression_curve.pdf\n-rw-r--r-- 1 ubuntu ubuntu   31132 May 22 14:14 fig_crosssuite.pdf\n-rw-r--r-- 1 ubuntu ubuntu  197642 May 22 14:14 fig_crosssuite.png\n-rw-r--r-- 1 ubuntu ubuntu   57361 May 22 14:18 fig_degradation_curve.pdf\n-rw-r--r-- 1 ubuntu ubuntu  336496 May 22 14:18 fig_degradation_curve.png\n-rw-r--r-- 1 ubuntu ubuntu  175091 May 22 13:34 fig_degradation_overview.png\n-rw-r--r-- 1 ubuntu ubuntu   30759 May 22 14:14 fig_entropy_layers.pdf\n-rw-r--r-- 1 ubuntu ubuntu  151216 May 22 14:14 fig_entropy_layers.png\n-rw-r--r-- 1 ubuntu ubuntu  311633 May 24 08:26 fig_hero_overview.pdf\n-rw-r--r-- 1 ubuntu ubuntu 2126046 May 24 08:26 fig_hero_overview.png\n-rw-r--r-- 1 ubuntu ubuntu 3768870 May 24 08:26 fig_hero_overview_real.png\n-rw-r--r-- 1 ubuntu ubuntu   22092 May 24 02:11 fig_method_gap.pdf\n-rw-r--r-- 1 ubuntu ubuntu  100579 May 24 02:11 fig_method_gap.png\n-rw-r--r-- 1 ubuntu ubuntu   29272 May 26 21:33 fig_openvla_sweep.pdf\n-rw-r--r-- 1 ubuntu ubuntu  226567 May 26 21:33 fig_openvla_sweep.png\n-rw-r--r-- 1 ubuntu ubuntu   23434 May 22 14:14 fig_pixel_shuffle.pdf\n-rw-r--r-- 1 ubuntu ubuntu   35105 May 25 20:08 fig_pruning_overview.pdf\n-rw-r--r-- 1 ubuntu ubuntu  128828 May 25 20:08 fig_pruning_overview.png\n---\n-rw-r--r-- 1 ubuntu ubuntu 23480 May 24 02:30 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
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

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the main table data consistency issue — specifically the π0.5 data. The paper_framing.md has different numbers in some places compared to what's in the tex files. Let me also check if there's a scoring_crossover figure mentioned but potentially missing, and verify the key data points.

Let me now check the specific issue about π0.5 pollution from D248 — Goal suite data. I need to check which data in the main results table (tab:main_results) comes from which server.

Let me also check the X-VLA data more carefully. The main table shows some X-VLA data that needs verification.


I'm also noticing the SmolVLA Spatial baseline discrepancy that paper_framing.md flags. Now I have enough information to compile my audit findings. The abstract appears complete and well-polished, with all the key numbers aligning properly — the CV range from 0.038 to 0.314, the SmolVLA collapse at k=0.95, the 89 percentage point zero-mask gap, and VTR performance above 60% at 75% compression all check out against the experimental results.

There's a minor inconsistency I'm catching though: the abstract states "five VLA architectures" but when I count the models in Table 1 — π0, π0.5, X-VLA, OpenVLA, and SmolVLA — that's actually five, which matches. The method section mentions six architectures spanning three vision connector families, but the abstract's focus on five appears to be the core closed-loop models being evaluated. The Introduction looks solid with clear contributions and consistent numbers. Related Work covers the relevant token efficiency and vision connector literature, positioning this work well against concurrent approaches. For the Method section, I'm verifying that the six models and three connector families are properly documented, with Table 1 showing complete model properties and the pruning protocol clearly laid out with L2 norm as the core metric.

Now I'm checking the experimental results—the main results table has significant gaps across multiple model-task-pruning combinations, particularly for OpenVLA across most conditions and several X-VLA entries, which need to be filled in before this section can be finalized.

I'm also investigating a potential data pollution issue with the π0.5 pruning method, specifically in the Goal and Long task columns at lower k values, though the k≥0.9 results appear reliable and the Object/Spatial columns seem unaffected. I'm realizing the scope of the data contamination issue — most of the Goal column results are potentially inflated due to the lenient success condition, while only the k≥0.9 results for Long tasks might be trustworthy. The strict rerun is underway to get clean numbers.

Looking at the paper structure now: the main sections are well-finalized with proper subsections, referenced figures, and limitations discussed. The conclusion covers the key claims and includes AI disclosure. The appendix is comprehensive with extensive ablations and cross-suite analysis across all the different experimental conditions.

Now I'm checking for consistency issues across the tables. There are some baseline value discrepancies I need to track down — SmolVLA Spatial shows different percentages depending on which table I'm looking at (44.6% in the main experiments versus 51.8% in the VTR cross-suite), and the Goal baseline also varies between 60.8% and 63.0%. The Object baseline difference is explained by the paper using the official checkpoint while VTR uses a LoRA variant, but these inconsistencies need reconciliation to ensure the results are clearly presented.

I also notice the abstract mentions five architectures while the method section says six, and there's a minor discrepancy with X-VLA Goal (98.4% versus 98.0%). For constraint C001 about Spatial suite baselines, I need to verify whether the paper is using the correct official or full-FT baseline rather than LoRA, since the VTR cross-suite table shows 51.8% which doesn't match the 6.2% LoRA baseline mentioned in the constraint. Looking at the cross-suite table more carefully, the 51.8% baseline appears to be from a different checkpoint than the main results table's 44.6% for SmolVLA Spatial, which creates some confusion about which baseline is being used for comparison. The paper does acknowledge the nuance around the 53.2% result, noting it concentrates in just two of ten tasks. Now I need to check whether the main results table's π0.5 Goal row uses polluted data for the baseline and k-values. The crossover analysis also relies on that same π0.5 Goal/Long data, so if it's polluted, the actual performance degradation could be worse than what's reported, which would actually strengthen the task complexity argument but shift the specific numbers. I'm also noticing some baseline discrepancies between the main table and paper_framing — X-VLA Spatial shows 93.0% versus 91.6%, and Goal shows 98.4% versus 98.0% — these could be from different checkpoints or evaluation runs. I found the fig_scoring_crossover.pdf file and noticed the discussion.tex was moved to the appendix with just comments remaining.

Looking at the structure, the actual analysis section is in analysis.tex which gets included in main.tex, and while it's labeled as sec:analysis, the section itself is titled "Discussion" — a bit confusing but it works. I'm verifying all the referenced figures have corresponding PDFs, and they do, so I have what I need to write the audit. Looking at the file list more carefully, fig_scoring_crossover.pdf is actually there in the glob output, so that's confirmed. Now I'm compiling the full audit of issues, starting with the critical data pollution problem on π0.5 Goal and Long conditions where the lenient success threshold inflated baseline and pruned SR results across multiple table rows.

The importance margin gradient claim showing Object outperforming Goal and Long, the task complexity discussion relying on π0.5 data, and the abstract's reference to four LIBERO suites all depend on this potentially unreliable data. Beyond that, Table 2 has numerous missing values scattered across X-VLA and OpenVLA rows at various k thresholds, though the paper's main narrative focuses on k=0.9 results which are mostly populated, so these gaps may not undermine the core arguments.

Now I'm noticing SmolVLA's baseline numbers shift across different tables and checkpoints—the main table shows Spatial at 44.6% while the VTR cross-suite table reports 51.8%, and the paper frames it as 43.8% elsewhere, which creates confusion even though they're pulling from different model versions. There's also an inconsistency between the abstract claiming five VLA architectures and the methods section describing six, with OFT being the potential sixth as an OpenVLA fine-tuning variant that may or may not be counted separately. The X-VLA baselines themselves show high performance numbers that need verification against the reported values.

On the maintenance side, discussion.tex is essentially empty with the actual content living in analysis.tex instead, and there are old draft files scattered in the sections directory that aren't being used but could create confusion. I should verify that the Smart Compress versus LoRA comparison on Spatial follows the constraint about not treating that as evidence of improvement over the uncompressed baseline—the appendix text seems careful about this already. I also need to check that all citations in the document have corresponding entries in the references file.

For the lower priority items, the appendix is quite lengthy at around 800 lines, though CoRL typically doesn't count appendices toward page limits, and I should confirm that all referenced figures exist as PDFs and that the LaTeX compilation runs without errors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "f5f3669d-25f2-46b1-afb7-4ca09ec92d50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQKLDQMbRBn7a6ynBdwSvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 94751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
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

_source line 66_

I have all the information needed. Let me now load the tools to save the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "d3277250-dfb4-4723-9fc2-01f10d319d87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQKLDQMbRBn7a6ynBdwSvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 94751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
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

_source line 67_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B7srGDcXQLVgZw5EbAWRTU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "88df7421-82b8-4751-bbc6-ac8892a34191",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQKLDQMbRBn7a6ynBdwSvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 94751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
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

_source line 68 · 2026-05-27T04:32:12.779Z_

<details><summary>↩ Tool result · `toolu_01B7srGDcXQLVgZw5EbAWRTU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "773a7855-85a4-4fd1-a834-c2f4315c835f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the audit document and register it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "fd9f404e-8950-4fd4-9eb9-4519aceba5b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QdvxLELpDKFAMY65AFsjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 96737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5374
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 70_

<details open><summary>🔧 Tool call — Write · `toolu_01WVtpM18BYomY5JMGTi4Pbf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
  "content": "# Paper Section Audit — CoRL 2026 Submission\n\n**Audit date**: 2026-05-27  \n**Deadline**: ~5h remaining  \n**Paper location**: `docs/paper/` (main.tex + section files)  \n**Main structure**: Abstract → Introduction → Related Work → Method → Experiments → Discussion → Conclusion → Appendix\n\n---\n\n## Section Status Summary\n\n| Section | 文件 | 状态 | 具体问题 | 优先级 |\n|---------|------|------|----------|--------|\n| Abstract | `abstract.tex` | **定稿** | \"five VLA architectures\" vs Method \"six\" — 需统一 | P2 |\n| Introduction | `introduction.tex` | **定稿** | 与 paper_framing 2-axis framework 对齐，claims 一致 | — |\n| Related Work | `related_work.tex` | **定稿** | 完整，覆盖 6 篇 concurrent work | — |\n| Method | `method.tex` | **定稿** | 6 模型 Table 1 完整，CV 公式、VTR 描述清晰 | — |\n| Experiments | `experiments.tex` | **待数据/待修改** | 3 个关键问题，见下 | **P0/P1** |\n| Discussion | `analysis.tex` | **定稿** | OpenVLA sweep 分析完整，limitations 在位 | — |\n| Conclusion | `conclusion.tex` | **定稿** | 5 claims 总结，AI disclosure 已加 | — |\n| Appendix | `appendix.tex` | **基本定稿** | ~820 行，SmolVLA baseline 不一致需修 | P1 |\n| References | `references.bib` | **存在** | 未做编译验证 | P3 |\n| Figures | `figures/paper/` | **完整** | 19 个 PDF 全在位，所有 \\includegraphics 有对应文件 | — |\n\n---\n\n## Critical Issues (P0)\n\n### 1. π0.5 Goal/Long 数据污染 (D248)\n\ncqa1 上的 π0.5 实验使用宽松 success 条件 (`done|reward>0.5`)，导致 SR 可能虚高。\n\n**受影响的 Table 2 单元格**:\n| Suite | 受影响列 | 当前值 | 可信度 |\n|-------|----------|--------|--------|\n| Goal | baseline | 96.4% | **不可信** — 可能虚高 |\n| Goal | k=0.95 (89.4/84.0) | 全部 | **不可信** |\n| Goal | k=0.9 (90.6/62.2) | 全部 | **不可信** |\n| Goal | k=0.7 (71.2/78.2) | 全部 | **不可信** |\n| Goal | k=0.5 (59.2/73.6) | 全部 | **不可信** |\n| Long | k=0.7 (63.2/64.6) | 全部 | **不可信** (k≤0.85) |\n| Long | k=0.5 (50.2/50.2) | 全部 | **不可信** (k≤0.85) |\n| Long | baseline (91.6%) | — | **待确认** — 来源需查 |\n| Long | k=0.95 (86.8/61.2) | — | **可信** (k≥0.9) |\n| Long | k=0.9 (81.0/31.8) | — | **可信** (k≥0.9) |\n\n**受影响的论文 claims**:\n- Abstract: \"task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to 20×\" — 20× 来自 X-VLA（不受影响），但 π0.5 Goal/Long 数据支撑同一论点\n- Sec 5.5 (Experiments): importance margin gradient \"Object +93pp > Goal +35.2pp > Long +28.6pp\" — Goal 和 Long 的 margin 值依赖污染数据\n- Sec 5.7 (cliff highlight): π0.5 Long k=0.85 random=49.4% 对比 — k=0.85 处于 k≤0.85 污染区间\n- Discussion: OpenVLA 的 task complexity 分析不受影响（独立数据源）\n\n**Strict 重跑进度**: k=0.95/0.9/0.85 Attn Long 正在进行中。\n\n**建议处理方案**:\n- **方案 A (保守)**: 从 Table 2 移除所有不可信 π0.5 Goal 数据，标注 \"—\"，仅保留 Object/Spatial/Long k≥0.9。Task complexity 论点仅用 X-VLA 数据（不受污染）\n- **方案 B (折中)**: 保留数据但加脚注 \"π0.5 Goal and Long (k≤0.85) results use a lenient success criterion; strict re-evaluation in progress. X-VLA cross-suite patterns (unaffected) provide independent support for the task complexity claim.\"\n- **方案 C**: 如果 strict 重跑在截止前完成，替换数据\n\n### 2. Table 2 数据缺口 (\"--\" 单元格)\n\n共 19+ 个 \"--\" 单元格：\n\n| 模型 | 缺失 | 影响 |\n|------|------|------|\n| X-VLA Spatial | k=0.7 L2 | 文中未引用 |\n| X-VLA Long | k=0.7 L2/R | 文中未引用 |\n| OpenVLA Object | k=0.95 R, k=0.7 L2/R | k=0.95 R 缺失稍影响叙事 |\n| OpenVLA Goal | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Spatial | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Long | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n\n**评估**: 论文叙事主要围绕 k=0.9 和 k=0.5 展开。OpenVLA 的 k=0.9 三方法对比数据完整（含 attention†），支撑 scoring crossover 论点。X-VLA 的 attention 对比在 k=0.5 完整（Table 8）。**缺口不阻塞核心 claims，但 Table 2 视觉上稀疏。**\n\n**建议**: 接受现状，或将 OpenVLA 改为仅展示 k=0.9 和 k=0.5 两列（去掉 k=0.95/k=0.7 空列）。\n\n---\n\n## High Priority Issues (P1)\n\n### 3. SmolVLA 跨 suite baselines 不一致\n\n| Suite | Table 2 (main) | VTR cross-suite table (App) | paper_framing |\n|-------|----------------|---------------------------|---------------|\n| Object | 59.2% (official) | 44.8% (LoRA) | 59.2% official |\n| Spatial | 44.6% | 51.8% | 43.8% or 44.6% |\n| Goal | 60.8% | 63.0% | 60.8% |\n\n- Table 2 用 official checkpoint baseline；VTR appendix 用 LoRA checkpoint baseline\n- Spatial 有三个不同值 (43.8% / 44.6% / 51.8%)\n- 论文 appendix 文本已做 caveat 处理，但数字混乱容易让 reviewer 质疑\n\n**建议**: 在 VTR cross-suite table (Tab 10) 加脚注明确说明 \"baselines from LoRA-trained checkpoint (batch size 4); main table baselines from official checkpoint\"。统一 Spatial 基线值。\n\n### 4. \"Five\" vs \"Six\" architectures 不一致\n\n- Abstract line 4: \"five VLA architectures (450M--7B parameters)\"\n- Method Sec 3.1 line 7: \"six VLA architectures spanning three vision connector families\"\n- Table 1 列出 6 行（含 OFT）\n\n**建议**: 统一为 \"six VLA architectures\" 或在 abstract 说 \"five VLA architectures (with a sixth offline variant)\"。最简单是改 abstract 为 \"six\"。\n\n### 5. X-VLA baseline 小幅偏差\n\n| Suite | Table 2 | paper_framing |\n|-------|---------|---------------|\n| Spatial | 93.0% | 91.6% |\n| Goal | 98.4% | 98.0% |\n\n可能来自不同 eval seed 或不同 checkpoint。Table 2 是论文定稿数据，paper_framing 是早期记录。**如果 Table 2 数据可信，以 Table 2 为准。** 但需确认 93.0% 和 98.4% 来源无误。\n\n---\n\n## Medium Priority Issues (P2)\n\n### 6. discussion.tex 是空 stub\n\n文件内容仅为注释：\"Discussion section moved to Appendix\"。实际 Discussion 内容在 `analysis.tex`（标题为 `\\section{Discussion}`，label 为 `sec:analysis`）。main.tex include 的是 `\\input{analysis}`。功能正常但维护混乱。\n\n### 7. sections/ 目录残留旧稿\n\n`docs/paper/sections/` 下有 `results_draft.tex`, `analysis_draft.tex`, `related_work_draft.tex` 等旧版文件，不被 main.tex include。不影响编译但增加困惑。\n\n### 8. Constraint C001 合规性\n\nC001 要求 \"Spatial suite 对比禁止用 LoRA baseline (6.2%)\"。检查结果：\n- VTR cross-suite table 中 Spatial baseline=51.8%，VTR=53.2%（差值仅 1.4pp）\n- 文本明确说 \"we therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline\"\n- **合规** — 未使用 LoRA 6.2% baseline 做对比\n\n---\n\n## Low Priority Issues (P3)\n\n### 9. LaTeX 编译未验证\n\nreferences.bib 存在（23KB），所有 figure PDF 在位。未实际运行 `pdflatex` 验证编译。建议在提交前做一次完整编译。\n\n### 10. Appendix 长度\n\nAppendix 约 820 行 LaTeX，包含 18 个 tables/figures。CoRL 通常不限 appendix 页数，但过长可能影响 reviewer 体验。当前内容信息密度高，无明显冗余。\n\n---\n\n## Claim-Framing 一致性检查\n\n| Core Claim (paper_framing) | 论文中对应 | 一致性 |\n|---------------------------|-----------|--------|\n| Claim 1: 2-Axis Framework | Sec 4.2 + Fig 1 teaser | **一致** — connector × task complexity |\n| Claim 2: Pixel-shuffle entanglement | Sec 4.3 + Fig 5 | **一致** — 0% at k=0.95, official+LoRA 双 checkpoint |\n| Claim 3: Connector determines tolerance | Sec 3.1 Table 1 + Sec 4.2-4.5 | **一致** — CV spectrum 0.038→0.314 |\n| Claim 4: VTR recovery | Sec 4.6 + Table 4 | **一致** — 60.1±1.3% at M=32, MLP adapter control |\n| Claim 5: CV predicts optimal strategy | Sec 4.5 + Table 6 (appendix) | **一致** — monotonic Δ(R-L2) trend |\n\n**额外 claims 在论文但不在 framing**:\n- Zero-mask ablation (Sec 4.4): 89pp gap，position disruption — 论文中新增的重要发现\n- Per-task reversal within L2-dominant regimes (Sec 4.5 末段): Task 6 reversal — 细粒度分析\n\n---\n\n## 优先行动建议 (按时间紧迫度)\n\n1. **[P0, 30min]** 决定 π0.5 Goal/Long 污染数据处理方案 (A/B/C)，如选 B 则写脚注\n2. **[P1, 10min]** 统一 abstract \"five\"→\"six\" architectures\n3. **[P1, 15min]** 确认 X-VLA Spatial=93.0% 和 Goal=98.4% 数据来源\n4. **[P1, 15min]** 统一 SmolVLA Spatial baseline (44.6% vs 51.8% vs 43.8%)，加 VTR table 脚注\n5. **[P2, 5min]** 确认 Table 2 \"--\" 缺口可接受\n6. **[P3, 10min]** 运行一次完整 LaTeX 编译\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "66d1d8a6-71c1-4ef0-8427-f04f0f229a9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QdvxLELpDKFAMY65AFsjR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5374,
      "cache_read_input_tokens": 96737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5374
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 71 · 2026-05-27T04:33:34.710Z_

<details><summary>↩ Tool result · `toolu_01WVtpM18BYomY5JMGTi4Pbf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "338f3593-027d-44a3-8c80-b3cffc1dd48d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
    "content": "# Paper Section Audit — CoRL 2026 Submission\n\n**Audit date**: 2026-05-27  \n**Deadline**: ~5h remaining  \n**Paper location**: `docs/paper/` (main.tex + section files)  \n**Main structure**: Abstract → Introduction → Related Work → Method → Experiments → Discussion → Conclusion → Appendix\n\n---\n\n## Section Status Summary\n\n| Section | 文件 | 状态 | 具体问题 | 优先级 |\n|---------|------|------|----------|--------|\n| Abstract | `abstract.tex` | **定稿** | \"five VLA architectures\" vs Method \"six\" — 需统一 | P2 |\n| Introduction | `introduction.tex` | **定稿** | 与 paper_framing 2-axis framework 对齐，claims 一致 | — |\n| Related Work | `related_work.tex` | **定稿** | 完整，覆盖 6 篇 concurrent work | — |\n| Method | `method.tex` | **定稿** | 6 模型 Table 1 完整，CV 公式、VTR 描述清晰 | — |\n| Experiments | `experiments.tex` | **待数据/待修改** | 3 个关键问题，见下 | **P0/P1** |\n| Discussion | `analysis.tex` | **定稿** | OpenVLA sweep 分析完整，limitations 在位 | — |\n| Conclusion | `conclusion.tex` | **定稿** | 5 claims 总结，AI disclosure 已加 | — |\n| Appendix | `appendix.tex` | **基本定稿** | ~820 行，SmolVLA baseline 不一致需修 | P1 |\n| References | `references.bib` | **存在** | 未做编译验证 | P3 |\n| Figures | `figures/paper/` | **完整** | 19 个 PDF 全在位，所有 \\includegraphics 有对应文件 | — |\n\n---\n\n## Critical Issues (P0)\n\n### 1. π0.5 Goal/Long 数据污染 (D248)\n\ncqa1 上的 π0.5 实验使用宽松 success 条件 (`done|reward>0.5`)，导致 SR 可能虚高。\n\n**受影响的 Table 2 单元格**:\n| Suite | 受影响列 | 当前值 | 可信度 |\n|-------|----------|--------|--------|\n| Goal | baseline | 96.4% | **不可信** — 可能虚高 |\n| Goal | k=0.95 (89.4/84.0) | 全部 | **不可信** |\n| Goal | k=0.9 (90.6/62.2) | 全部 | **不可信** |\n| Goal | k=0.7 (71.2/78.2) | 全部 | **不可信** |\n| Goal | k=0.5 (59.2/73.6) | 全部 | **不可信** |\n| Long | k=0.7 (63.2/64.6) | 全部 | **不可信** (k≤0.85) |\n| Long | k=0.5 (50.2/50.2) | 全部 | **不可信** (k≤0.85) |\n| Long | baseline (91.6%) | — | **待确认** — 来源需查 |\n| Long | k=0.95 (86.8/61.2) | — | **可信** (k≥0.9) |\n| Long | k=0.9 (81.0/31.8) | — | **可信** (k≥0.9) |\n\n**受影响的论文 claims**:\n- Abstract: \"task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to 20×\" — 20× 来自 X-VLA（不受影响），但 π0.5 Goal/Long 数据支撑同一论点\n- Sec 5.5 (Experiments): importance margin gradient \"Object +93pp > Goal +35.2pp > Long +28.6pp\" — Goal 和 Long 的 margin 值依赖污染数据\n- Sec 5.7 (cliff highlight): π0.5 Long k=0.85 random=49.4% 对比 — k=0.85 处于 k≤0.85 污染区间\n- Discussion: OpenVLA 的 task complexity 分析不受影响（独立数据源）\n\n**Strict 重跑进度**: k=0.95/0.9/0.85 Attn Long 正在进行中。\n\n**建议处理方案**:\n- **方案 A (保守)**: 从 Table 2 移除所有不可信 π0.5 Goal 数据，标注 \"—\"，仅保留 Object/Spatial/Long k≥0.9。Task complexity 论点仅用 X-VLA 数据（不受污染）\n- **方案 B (折中)**: 保留数据但加脚注 \"π0.5 Goal and Long (k≤0.85) results use a lenient success criterion; strict re-evaluation in progress. X-VLA cross-suite patterns (unaffected) provide independent support for the task complexity claim.\"\n- **方案 C**: 如果 strict 重跑在截止前完成，替换数据\n\n### 2. Table 2 数据缺口 (\"--\" 单元格)\n\n共 19+ 个 \"--\" 单元格：\n\n| 模型 | 缺失 | 影响 |\n|------|------|------|\n| X-VLA Spatial | k=0.7 L2 | 文中未引用 |\n| X-VLA Long | k=0.7 L2/R | 文中未引用 |\n| OpenVLA Object | k=0.95 R, k=0.7 L2/R | k=0.95 R 缺失稍影响叙事 |\n| OpenVLA Goal | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Spatial | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Long | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n\n**评估**: 论文叙事主要围绕 k=0.9 和 k=0.5 展开。OpenVLA 的 k=0.9 三方法对比数据完整（含 attention†），支撑 scoring crossover 论点。X-VLA 的 attention 对比在 k=0.5 完整（Table 8）。**缺口不阻塞核心 claims，但 Table 2 视觉上稀疏。**\n\n**建议**: 接受现状，或将 OpenVLA 改为仅展示 k=0.9 和 k=0.5 两列（去掉 k=0.95/k=0.7 空列）。\n\n---\n\n## High Priority Issues (P1)\n\n### 3. SmolVLA 跨 suite baselines 不一致\n\n| Suite | Table 2 (main) | VTR cross-suite table (App) | paper_framing |\n|-------|----------------|---------------------------|---------------|\n| Object | 59.2% (official) | 44.8% (LoRA) | 59.2% official |\n| Spatial | 44.6% | 51.8% | 43.8% or 44.6% |\n| Goal | 60.8% | 63.0% | 60.8% |\n\n- Table 2 用 official checkpoint baseline；VTR appendix 用 LoRA checkpoint baseline\n- Spatial 有三个不同值 (43.8% / 44.6% / 51.8%)\n- 论文 appendix 文本已做 caveat 处理，但数字混乱容易让 reviewer 质疑\n\n**建议**: 在 VTR cross-suite table (Tab 10) 加脚注明确说明 \"baselines from LoRA-trained checkpoint (batch size 4); main table baselines from official checkpoint\"。统一 Spatial 基线值。\n\n### 4. \"Five\" vs \"Six\" architectures 不一致\n\n- Abstract line 4: \"five VLA architectures (450M--7B parameters)\"\n- Method Sec 3.1 line 7: \"six VLA architectures spanning three vision connector families\"\n- Table 1 列出 6 行（含 OFT）\n\n**建议**: 统一为 \"six VLA architectures\" 或在 abstract 说 \"five VLA architectures (with a sixth offline variant)\"。最简单是改 abstract 为 \"six\"。\n\n### 5. X-VLA baseline 小幅偏差\n\n| Suite | Table 2 | paper_framing |\n|-------|---------|---------------|\n| Spatial | 93.0% | 91.6% |\n| Goal | 98.4% | 98.0% |\n\n可能来自不同 eval seed 或不同 checkpoint。Table 2 是论文定稿数据，paper_framing 是早期记录。**如果 Table 2 数据可信，以 Table 2 为准。** 但需确认 93.0% 和 98.4% 来源无误。\n\n---\n\n## Medium Priority Issues (P2)\n\n### 6. discussion.tex 是空 stub\n\n文件内容仅为注释：\"Discussion section moved to Appendix\"。实际 Discussion 内容在 `analysis.tex`（标题为 `\\section{Discussion}`，label 为 `sec:analysis`）。main.tex include 的是 `\\input{analysis}`。功能正常但维护混乱。\n\n### 7. sections/ 目录残留旧稿\n\n`docs/paper/sections/` 下有 `results_draft.tex`, `analysis_draft.tex`, `related_work_draft.tex` 等旧版文件，不被 main.tex include。不影响编译但增加困惑。\n\n### 8. Constraint C001 合规性\n\nC001 要求 \"Spatial suite 对比禁止用 LoRA baseline (6.2%)\"。检查结果：\n- VTR cross-suite table 中 Spatial baseline=51.8%，VTR=53.2%（差值仅 1.4pp）\n- 文本明确说 \"we therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline\"\n- **合规** — 未使用 LoRA 6.2% baseline 做对比\n\n---\n\n## Low Priority Issues (P3)\n\n### 9. LaTeX 编译未验证\n\nreferences.bib 存在（23KB），所有 figure PDF 在位。未实际运行 `pdflatex` 验证编译。建议在提交前做一次完整编译。\n\n### 10. Appendix 长度\n\nAppendix 约 820 行 LaTeX，包含 18 个 tables/figures。CoRL 通常不限 appendix 页数，但过长可能影响 reviewer 体验。当前内容信息密度高，无明显冗余。\n\n---\n\n## Claim-Framing 一致性检查\n\n| Core Claim (paper_framing) | 论文中对应 | 一致性 |\n|---------------------------|-----------|--------|\n| Claim 1: 2-Axis Framework | Sec 4.2 + Fig 1 teaser | **一致** — connector × task complexity |\n| Claim 2: Pixel-shuffle entanglement | Sec 4.3 + Fig 5 | **一致** — 0% at k=0.95, official+LoRA 双 checkpoint |\n| Claim 3: Connector determines tolerance | Sec 3.1 Table 1 + Sec 4.2-4.5 | **一致** — CV spectrum 0.038→0.314 |\n| Claim 4: VTR recovery | Sec 4.6 + Table 4 | **一致** — 60.1±1.3% at M=32, MLP adapter control |\n| Claim 5: CV predicts optimal strategy | Sec 4.5 + Table 6 (appendix) | **一致** — monotonic Δ(R-L2) trend |\n\n**额外 claims 在论文但不在 framing**:\n- Zero-mask ablation (Sec 4.4): 89pp gap，position disruption — 论文中新增的重要发现\n- Per-task reversal within L2-dominant regimes (Sec 4.5 末段): Task 6 reversal — 细粒度分析\n\n---\n\n## 优先行动建议 (按时间紧迫度)\n\n1. **[P0, 30min]** 决定 π0.5 Goal/Long 污染数据处理方案 (A/B/C)，如选 B 则写脚注\n2. **[P1, 10min]** 统一 abstract \"five\"→\"six\" architectures\n3. **[P1, 15min]** 确认 X-VLA Spatial=93.0% 和 Goal=98.4% 数据来源\n4. **[P1, 15min]** 统一 SmolVLA Spatial baseline (44.6% vs 51.8% vs 43.8%)，加 VTR table 脚注\n5. **[P2, 5min]** 确认 Table 2 \"--\" 缺口可接受\n6. **[P3, 10min]** 运行一次完整 LaTeX 编译\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01YWtLDT8XpZsTxp9o9b1JjR`</summary>

```json
{
  "name": "paper_section_audit",
  "type": "report",
  "description": "CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查",
  "project": "importance_margin_vla_compress",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
  "tags": [
    "paper",
    "audit",
    "corl2026"
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
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "61a9ba5c-587e-4142-bf48-d9d07ddb89f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6xrevSstcrA3FkVJzviRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3858,
      "cache_read_input_tokens": 102111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3858
      },
      "output_tokens": 44,
      "service_tier": "standard",
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

_source line 73 · 2026-05-27T04:33:40.500Z_

<details><summary>↩ Tool result · `toolu_01YWtLDT8XpZsTxp9o9b1JjR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_67ccde\", \"name\": \"paper_section_audit\", \"type\": \"report\", \"description\": \"CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/report/paper_section_audit.md\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T04:33:39.633720+00:00\", \"tags\": [\"paper\", \"audit\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "e8be4b4e-a43c-422d-b2c3-d42da8ddd619",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260527_67ccde\\\", \\\"name\\\": \\\"paper_section_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查\\\", \\\"path\\\": \\\"projects/importance_margin_vla_compress/artifacts/_project/report/paper_section_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"importance_margin_vla_compress\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-27T04:33:39.633720+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"audit\\\", \\\"corl2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_67ccde\", \"name\": \"paper_section_audit\", \"type\": \"report\", \"description\": \"CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/report/paper_section_audit.md\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T04:33:39.633720+00:00\", \"tags\": [\"paper\", \"audit\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

盘点完成。核心发现：

**论文整体成熟度高** — Abstract/Intro/Related Work/Method/Discussion/Conclusion 均已定稿，figures 全在位，claims 与 paper_framing 一致。

**3 个需立即处理的问题**：

1. **[P0] π0.5 Goal/Long 数据污染** — cqa1 宽松 success 条件影响 Table 2 整行 π0.5 Goal 数据和 Long k≤0.85 数据。建议加脚注说明，并用 X-VLA（不受影响）独立支撑 task complexity claim
2. **[P1] "Five" vs "six" architectures** — Abstract 说 five，Method 说 six，需统一
3. **[P1] SmolVLA Spatial baseline 三个不同值** (43.8%/44.6%/51.8%) — VTR cross-suite table 需加脚注区分 checkpoint 来源

Table 2 有 19+ "--" 缺口，但核心叙事围绕 k=0.9 展开，数据完整，缺口不阻塞。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "uuid": "fa16a412-2505-4f2d-a019-e5e4c5045038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuzXPZhU3Z5JGrjr1o61xu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 105969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 557
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

### Task result

_source line 75_

盘点完成。核心发现：

**论文整体成熟度高** — Abstract/Intro/Related Work/Method/Discussion/Conclusion 均已定稿，figures 全在位，claims 与 paper_framing 一致。

**3 个需立即处理的问题**：

1. **[P0] π0.5 Goal/Long 数据污染** — cqa1 宽松 success 条件影响 Table 2 整行 π0.5 Goal 数据和 Long k≤0.85 数据。建议加脚注说明，并用 X-VLA（不受影响）独立支撑 task complexity claim
2. **[P1] "Five" vs "six" architectures** — Abstract 说 five，Method 说 six，需统一
3. **[P1] SmolVLA Spatial baseline 三个不同值** (43.8%/44.6%/51.8%) — VTR cross-suite table 需加脚注区分 checkpoint 来源

Table 2 有 19+ "--" 缺口，但核心叙事围绕 k=0.9 展开，数据完整，缺口不阻塞。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 241624,
  "duration_api_ms": 242596,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "c65b4c77-7ef2-4e07-b0a0-786ef1b1f4f9",
  "total_cost_usd": 1.2312577999999998,
  "usage": {
    "input_tokens": 4272,
    "cache_creation_input_tokens": 94685,
    "cache_read_input_tokens": 600653,
    "output_tokens": 11366,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 94685,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 320,
        "cache_read_input_tokens": 105969,
        "cache_creation_input_tokens": 557,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 557
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1546,
      "outputTokens": 1022,
      "cacheReadInputTokens": 18428,
      "cacheCreationInputTokens": 20113,
      "webSearchRequests": 0,
      "costUSD": 0.03364005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4272,
      "outputTokens": 11366,
      "cacheReadInputTokens": 600653,
      "cacheCreationInputTokens": 94685,
      "webSearchRequests": 0,
      "costUSD": 1.19761775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "09c413a0-15c5-48d1-93ab-b06b69b88a1b"
}
```

</details>

---
